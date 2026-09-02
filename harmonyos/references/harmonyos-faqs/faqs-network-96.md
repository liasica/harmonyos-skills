---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-96
title: 如何限制UDPSocket通过特定网络发送广播
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 如何限制UDPSocket通过特定网络发送广播
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:36+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9345c43145e3890b90609c9322b99527f12e249976a9f7845c9cfdf0fa078117
---

## 问题现象

使用UDPSocket发送广播，发现广播是通过蜂窝网络发出去的，如何限制UDPSocket只通过WiFi网络发送广播？

## 背景知识

* [@ohos.net.socket](../harmonyos-references/js-apis-socket.md)模块提供利用Socket进行数据传输的能力，支持TCPSocket、UDPSocket、WebSocket和TLSSocket，仅可发送string、ArrayBuffer类型的数据。
* 广播地址：向同一子网所有主机发送数据的IP地址，其主机位全为1。比如192.168.43.0/24子网中的直接广播地址是192.168.43.255，受限广播地址为255.255.255.255。

## 解决方案

1. 将[UdpExtraOptions](../harmonyos-references/js-apis-socket.md#udpextraoptions)的broadcast参数设置为true开启广播功能：

   ```ts
   let udpExtraOptions: socket.UDPExtraOptions = {
     receiveBufferSize: 8192,
     sendBufferSize: 8192,
     reuseAddress: false,
     socketTimeout: 6000,
     broadcast: true // 开启广播
   };
   this.udpClient.bind({ address: '0.0.0.0', port: 8000, family: 1 } as socket.NetAddress, (error: Error) => {
     if (error) {
       console.error(`udp client bind fail: ${JSON.stringify(error)}`);
       return;
     }
     // 注意setExtraOptions需要在bind成功之后设置
     this.udpClient.setExtraOptions(udpExtraOptions, (err: BusinessError) => {
       if (err) {
         console.error(`setExtraOptions fail: ${JSON.stringify(err)}`);
         return;
       }
       console.info('setExtraOptions success');
     });
     this.bindSocket2BearType(this.udpClient, connection.NetBearType.BEARER_WIFI);
   });
   ```
2. 使用[connection.getAllNets](../harmonyos-references/js-apis-net-connection.md#connectiongetallnets)获取所有处于连接状态的网络句柄。并将网络句柄传入[connection.getNetCapabilities](../harmonyos-references/js-apis-net-connection.md#connectiongetnetcapabilities)接口，在回调函数中通过bearerTypes字段判断网络类型，筛选出所需的WiFi句柄。
3. 用WiFi句柄调用bindSocket将TCPSocket或UDPSocket绑定到当前网络：

   ```ts
   bindSocket2BearType(socketParam: socket.TCPSocket | socket.UDPSocket, bearType: connection.NetBearType) {
     if (!bearType) {
       return;
     }
     let netHandle: connection.NetHandle | undefined = undefined;
     connection.getAllNets((error: BusinessError, netHandles: connection.NetHandle[]) => {
       if (error) {
         console.error(`getAllNets failed: ${JSON.stringify(error)}`);
       }
       for (let index = 0; index < netHandles.length; index++) {
         try {
           let data = connection.getNetCapabilitiesSync(netHandles[index]);
           console.info(`Succeeded to get data: ${JSON.stringify(data)} `);
           if (bearType === data.bearerTypes[0]) {
             netHandle = netHandles[index];
           }
         } catch (error) {
           console.error(`failed to get net capabilities. Code:${error.code}, message:${error.message}`);
         }
       }
       if (netHandle) {
         (netHandle as connection.NetHandle).bindSocket(socketParam, (error: BusinessError, data: void) => {
           if (error) {
             console.error(`failed to bind socket. Code:${error.code}, message:${error.message}`);
           } else {
             console.info(`bindSocket success: ${JSON.stringify(data)}`);
           }
         });
       } else {
         console.error(`not find netHandle ${bearType}`);
       }
     });
   }
   ```
4. 向广播地址发送数据：

   ```ts
   let netAddress: socket.NetAddress = {
     address: this.broadcastIp, // 广播地址
     port: this.broadcastPort
   };
   let sendOptions: socket.UDPSendOptions = {
     data: (new Date()).getTime().toString() + ', Hello, server!',
     address: netAddress
   };
   this.udpClient.send(sendOptions, (err: BusinessError) => {
     if (err) {
       console.error(`udp client send broadcast fail: ${JSON.stringify(err)}`);
       return;
     }
     console.info('udp client send broadcast success');
   });
   ```

包含接收端的完整示例如下：

```ts
import { connection, socket } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { util } from '@kit.ArkTS';

@Entry
@Component
struct SocketSendBySpecificNet {
  private udpClient: socket.UDPSocket = socket.constructUDPSocketInstance();
  private broadcastIp: string = '255.255.255.255'; // 广播地址，可以是子网广播地址比如192.168.43.255或受限广播地址255.255.255.255
  private broadcastPort: number = 18256; // 广播包端口，需要双方协商

  aboutToAppear(): void {
    let udpExtraOptions: socket.UDPExtraOptions = {
      receiveBufferSize: 8192,
      sendBufferSize: 8192,
      reuseAddress: false,
      socketTimeout: 6000,
      broadcast: true // 开启广播
    };
    this.udpClient.bind({ address: '0.0.0.0', port: 8000, family: 1 } as socket.NetAddress, (error: Error) => {
      if (error) {
        console.error(`udp client bind fail: ${JSON.stringify(error)}`);
        return;
      }
      // 注意setExtraOptions需要在bind成功之后设置
      this.udpClient.setExtraOptions(udpExtraOptions, (err: BusinessError) => {
        if (err) {
          console.error(`setExtraOptions fail: ${JSON.stringify(err)}`);
          return;
        }
        console.info('setExtraOptions success');
      });
      this.bindSocket2BearType(this.udpClient, connection.NetBearType.BEARER_WIFI);
    });
  }

  bindSocket2BearType(socketParam: socket.TCPSocket | socket.UDPSocket, bearType: connection.NetBearType) {
    if (!bearType) {
      return;
    }
    let netHandle: connection.NetHandle | undefined = undefined;
    connection.getAllNets((error: BusinessError, netHandles: connection.NetHandle[]) => {
      if (error) {
        console.error(`getAllNets failed: ${JSON.stringify(error)}`);
      }
      for (let index = 0; index < netHandles.length; index++) {
        try {
          let data = connection.getNetCapabilitiesSync(netHandles[index]);
          console.info(`Succeeded to get data: ${JSON.stringify(data)} `);
          if (bearType === data.bearerTypes[0]) {
            netHandle = netHandles[index];
          }
        } catch (error) {
          console.error(`failed to get net capabilities. Code:${error.code}, message:${error.message}`);
        }
      }
      if (netHandle) {
        (netHandle as connection.NetHandle).bindSocket(socketParam, (error: BusinessError, data: void) => {
          if (error) {
            console.error(`failed to bind socket. Code:${error.code}, message:${error.message}`);
          } else {
            console.info(`bindSocket success: ${JSON.stringify(data)}`);
          }
        });
      } else {
        console.error(`not find netHandle ${bearType}`);
      }
    });
  }

  build() {
    Column({ space: 24 }) {
      Button('Socket通过特定网络发送广播').onClick(() => {
        let netAddress: socket.NetAddress = {
          address: this.broadcastIp, // 广播地址
          port: this.broadcastPort
        };
        let sendOptions: socket.UDPSendOptions = {
          data: (new Date()).getTime().toString() + ', Hello, server!',
          address: netAddress
        };
        this.udpClient.send(sendOptions, (err: BusinessError) => {
          if (err) {
            console.error(`udp client send broadcast fail: ${JSON.stringify(err)}`);
            return;
          }
          console.info('udp client send broadcast success');
        });
      });
      Button('接收广播包').onClick(() => {
        let udp: socket.UDPSocket = socket.constructUDPSocketInstance();
        udp.bind({ address: '0.0.0.0', port: this.broadcastPort, family: 1 } as socket.NetAddress, (error: Error) => {
          if (error) {
            console.error(`recv client bind fail: ${JSON.stringify(error)}`);
            return;
          }
          udp.on('message', (data: socket.SocketMessageInfo) => {
            console.info(`client recv data success: ${JSON.stringify(data)}`);
            let decoder = util.TextDecoder.create('utf-8');
            let str = decoder.decodeToString(new Uint8Array(data.message));
            console.info(`client recv broadcast: ${str}`);
          });
        });
      });
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%');
  }
}
```

## 常见FAQ

Q：bindSocket是否支持多次调用绑定多个Socket？

A：支持绑定多个Socket。
