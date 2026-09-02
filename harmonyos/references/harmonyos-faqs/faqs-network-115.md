---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-115
title: 如何解决Socket bind失败问题
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 如何解决Socket bind失败问题
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a99b5ee7fe934daba6278724a51ec4425fac1e5eadaf8e080f93baa7e2d530ec
---

## 问题现象

1. 使用TCPSocket\UDPSocket bind失败，报错：
   * 报错场景一：2301013 Permission denied。
   * 报错场景二：2301099 Address not available。
2. bind绑定指定端口未报错，但是分配到一个随机端口。

## 背景知识

* [SOCKET 错误码](../harmonyos-references/errorcode-net-socket.md)：错误码映射关系为2301000+[内核错误码](../harmonyos-references/errorcode-kernel.md)。比如2301013就是2301000+内核错误码13，在应用申请系统保留端口导致无权访问等场景出现。
* [bind](../harmonyos-references/js-apis-socket.md#bind-1)接口：在创建Socket连接时，可以使用bind方法绑定IP地址和端口，端口可以由用户指定或由系统随机分配。如果端口冲突，系统会rebind随机分配端口号。
* Socket通过TCP/UDP协议进行通信可以参考：[应用TCP/UDP协议进行通信](../harmonyos-guides/socket-connection.md#应用tcpudp协议进行通信)。

## 问题定位

* 错误信息提示Permission denied拒绝访问，需检查port参数设置是否过低，属于系统保留端口。
* 错误信息提示Address not available不能分配的地址，检查是否误绑了目标服务端IP地址或其他无效地址，Socket连接bind方法需要绑定本机IP地址。

## 分析结论

* bind时设置了系统保留端口，普通应用没有权限，应改设较大数值的端口。
* Socket连接bind方法入参地址有误，应绑定本机IP地址而非目标服务端IP地址。
* 可以在Socket进行bind时传入手机客户端的IP和默认端口(默认端口可不填)解决上述问题。

## 修改建议

1. 报错2301013 Permission denied，建议客户端bind更大的端口，避免使用系统保留端口。
2. 报错2301099 Address not available，可以使用0.0.0.0（IPv4通配符）或::（IPv6通配符）绑定本地所有地址：

   ```ts
   // socket绑定0.0.0.0作为本机IP地址，参考样例:
   bindAllAddress() {
     let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
     let bindAddr: socket.NetAddress = {
       address: '0.0.0.0', // 本端地址
       port: 1234
     };
     udp.bind(bindAddr)
       .then(() => {
         console.info('bind success');
       })
       .catch((err: BusinessError) => {
         console.error('bind fail', err);
       });
   }
   ```

   如果是通过[wifiManager.getIpInfo](../harmonyos-references/js-apis-wifimanager.md#wifimanagergetipinfo)接口获取到的IpInfo.ipAddress地址，需要转换为IP常用格式。

   ```ts
   // 获取WiFi IPV4地址，参考样例:
   getWifiIp() {
     let localAddress = this.resolveIP(wifiManager.getIpInfo().ipAddress) as string;
     console.info(`localAddress: ${localAddress}`);
     console.info(`IP校验结果为: ${this.checkIp(localAddress)}`);
   }

   resolveIP(ip: number): string {
     if (ip < 0 || ip > 0xFFFFFFFF) {
       console.info('The number is not normal!');
     }
     return (ip >>> 24) + '.' + (ip >> 16 & 0xFF) + '.' + (ip >> 8 & 0xFF) + '.' + (ip & 0xFF);
   }

   checkIp(ip: string): boolean {
     let ipRegex = /^((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)$/;
     return ipRegex.test(ip);
   }
   ```
3. 对于绑定指定端口失败，由于系统具备自动rebind机制随机分配端口，需要通过[getLocalAddress](../harmonyos-references/js-apis-socket.md#getlocaladdress12)接口自行判断是否绑定指定端口：

   ```ts
   bindWithoutRandomPort(address: socket.NetAddress) {
     let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
     udp.bind(address, (error: BusinessError) => {
       if (error) {
         console.error(`:${JSON.stringify(error)}`);
         return;
       }
       if (!address.port) {
         console.info('应用绑定成功');
         return;
       }
       udp.getLocalAddress().then((localAddress: socket.NetAddress) => {
         console.info(`成功获取UDP Socket地址Address=${JSON.stringify(localAddress)}`);
         if (address.port === localAddress.port) {
           console.info('应用绑定的端口正确');
         } else {
           console.error(`应用重新绑定了另外的端口: ${localAddress.port}`);
           // ...
         }
       }).catch((err: Error) => {
         console.error(`获取UDP Socket地址失败: ${JSON.stringify(err)}`);
       });
     });
   }
   ```

完整示例参考如下：

**说明** 

需要在module.json5文件中申请[ohos.permission.INTERNET](../harmonyos-guides/permissions-for-all.md#ohospermissioninternet)和[ohos.permission.GET\_WIFI\_INFO](../harmonyos-guides/permissions-for-all.md#ohospermissionget_wifi_info)权限。

```ts
import { wifiManager } from '@kit.ConnectivityKit';
import { socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct SocketBindExample {
  // 获取WiFi IPV4地址，参考样例:
  getWifiIp() {
    let localAddress = this.resolveIP(wifiManager.getIpInfo().ipAddress) as string;
    console.info(`localAddress: ${localAddress}`);
    console.info(`IP校验结果为: ${this.checkIp(localAddress)}`);
  }

  resolveIP(ip: number): string {
    if (ip < 0 || ip > 0xFFFFFFFF) {
      console.info('The number is not normal!');
    }
    return (ip >>> 24) + '.' + (ip >> 16 & 0xFF) + '.' + (ip >> 8 & 0xFF) + '.' + (ip & 0xFF);
  }

  checkIp(ip: string): boolean {
    let ipRegex = /^((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)$/;
    return ipRegex.test(ip);
  }

  // socket绑定0.0.0.0作为本机IP地址，参考样例:
  bindAllAddress() {
    let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
    let bindAddr: socket.NetAddress = {
      address: '0.0.0.0', // 本端地址
      port: 1234
    };
    udp.bind(bindAddr)
      .then(() => {
        console.info('bind success');
      })
      .catch((err: BusinessError) => {
        console.error('bind fail', err);
      });
  }

  bindWithoutRandomPort(address: socket.NetAddress) {
    let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
    udp.bind(address, (error: BusinessError) => {
      if (error) {
        console.error(`:${JSON.stringify(error)}`);
        return;
      }
      if (!address.port) {
        console.info('应用绑定成功');
        return;
      }
      udp.getLocalAddress().then((localAddress: socket.NetAddress) => {
        console.info(`成功获取UDP Socket地址Address=${JSON.stringify(localAddress)}`);
        if (address.port === localAddress.port) {
          console.info('应用绑定的端口正确');
        } else {
          console.error(`应用重新绑定了另外的端口: ${localAddress.port}`);
          // ...
        }
      }).catch((err: Error) => {
        console.error(`获取UDP Socket地址失败: ${JSON.stringify(err)}`);
      });
    });
  }

  build() {
    Column({ space: 16 }) {
      Button('获取WiFi分配的IP地址').onClick(() => {
        this.getWifiIp();
      });
      Button('通配符绑到所有本地地址').onClick(() => {
        this.bindAllAddress();
      });
      Button('绑定指定端口').onClick(() => {
        this.bindWithoutRandomPort({ address: '::', family: 2, port: 3000 });
      });
    }.width('100%').height('100%').justifyContent(FlexAlign.Center);
  }
}
```

## 常见FAQ

Q：通过Socket连接向IP地址为192.168.1.1的路由器发送数据，应如何绑定IP地址？

A：建议绑定本地回环地址127.0.0.1或者0.0.0.0。
