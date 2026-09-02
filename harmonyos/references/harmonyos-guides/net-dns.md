---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/net-dns
title: 使用DNS解析域名
breadcrumb: 指南 > 系统 > 网络 > Network Kit（网络服务） > 访问网络 > 使用DNS解析域名
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d3b8a3d813a9edabf5d076dcf03c52cc50476185831096d53b25e9e73a362168
---

## 场景介绍

域名解析（DNS, Domain Name System）功能允许应用将主机名（域名）转换为IP地址。支持中文字符与ASCII码之间的转换、获取指定域名的IP地址列表、以及在不同网络环境下进行域名解析。

当前支持功能如下：

| 功能名称 | 功能描述 | 开始支持的版本 |
| --- | --- | --- |
| Unicode与ASCII转换 | 支持中文域名与ASCII编码之间的相互转换 | API version 23 |
| 获取主机名的所有IP地址 | 使用当前默认网络解析主机名，获取所有IP地址 | API version 23 |
| 指定IP类型解析主机名 | 使用当前默认网络，指定IP类型（IPv4/IPv6）解析主机名 | API version 23 |
| 指定网络连接解析主机名 | 使用特定网络连接[NetHandle](../harmonyos-references/js-apis-net-connection.md#nethandle)解析主机名 | API version 23 |

## DNS解析支持中文域名转码

从API version 23开始，DNS解析支持中文转码，支持中文域名与ASCII编码之间的相互转换。

**说明** 

在本文档的示例中，资源文件中hostName需修改成一个实际的中文域名。

完整示例代码见：[DNS\_case](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/NetWork_Kit/NetWorkKit_Datatransmission/DNS_case)

1. 导入所需文件。

   ```typescript
   import { connection } from '@kit.NetworkKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 初始化数据成员。

   ```typescript
   @State hostVal: string = '';     // 转码之后的主机名
   @State ipResult: string = '';    // 获取的IP地址结果
   private hostName: string = '';   // 初始主机名
   ```
3. 获取资源文件中hostName值并赋值。

   ```typescript
   aboutToAppear() {
     this.hostName =
       (this.getUIContext().getHostContext() as Context).resourceManager.getStringSync($r('app.string.hostName').id);
   }
   ```
4. 创建网络地址解析函数，将域名转换为IP地址，isChange为是否将域名转码为ASCII编码的标识。

   ```typescript
   getAddressName(isChange: boolean) {
     this.ipResult = '';
     connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
       if (netHandle.netId === 0) {
         // 当前没有已连接的网络时，netHandler的netId为0，属于异常场景。可根据实际情况添加处理机制。
         return;
       }
       if (isChange) {
         this.hostVal = connection.getDnsAscii(this.hostName);
       } else {
         this.hostVal = '';
       }
       netHandle.getAddressByName(isChange ? this.hostVal : this.hostName,
         (error: BusinessError, data: connection.NetAddress) => {
           if (error) {
             this.ipResult = `Failed to get address. Code:${error.code}, message:${error.message}`;
             hilog.error(0x0000, 'testTag', `Failed to get address. Code:${error.code}, message:${error.message}`);
             return;
           }
           this.ipResult = JSON.stringify(data);
           hilog.info(0x0000, 'testTag', `Succeeded to get data: ${JSON.stringify(data)}`);
         });
     });
   }
   ```
5. 获取中文域名地址对应的IP。由于未经过ASCII编码，因此预期结果为获取IP失败。

   ```typescript
   this.getAddressName(false);
   ```
6. 将中文域名转换为对应ASCII编码后获取对应IP。

   ```typescript
   this.getAddressName(true);
   ```
7. 将转换后的ASCII编码转成原中文域名。

   ```typescript
   this.hostVal = connection.getDnsUnicode(this.hostVal);
   ```

## DNS接口支持配置获取的IP地址类型

从API version 23开始，DNS解析支持通过options参数指定IP地址类型（如 IPv4 或 IPv6），也支持在特定的网络连接NetHandle上按给定的IP类型解析主机名，从而实现更精准的地址解析。

完整示例代码见：[DNS\_case](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/NetWork_Kit/NetWorkKit_Datatransmission/DNS_case)

1. 导入所需文件。

   ```typescript
   import { connection } from '@kit.NetworkKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 初始化数据成员。

   ```typescript
   @State hostName: string = 'www.example.com';
   ```
3. 使用当前默认网络解析主机名以获取所有IP地址。

   ```typescript
   connection.getAddressesByName(this.hostName).then((data: connection.NetAddress[]) => {
     hilog.info(0x0000, 'testTag', `Succeeded to get data: ${JSON.stringify(data)}`);
   })
   ```
4. 使用当前默认网络，指定IP类型解析主机名以获取指定IP地址。

   ```typescript
   let options: connection.QueryOptions = {
     family: connection.FamilyType.FAMILY_TYPE_IPV4
   };
   connection.getAddressesByNameWithOptions(this.hostName, options).then((data: connection.NetAddress[]) => {
     hilog.info(0x0000, 'testTag', `Succeeded to get data: ${JSON.stringify(data)}`);
   });
   ```
5. 使用指定的网络连接（NetHandle），并按给定的IP类型解析主机名。

   ```typescript
   let netSpecifier: connection.NetSpecifier = {
     netCapabilities: {
       // 假设当前默认网络是WiFi，需要创建蜂窝网络连接，可指定网络类型为蜂窝网。
       bearerTypes: [connection.NetBearType.BEARER_CELLULAR],
       // 指定网络能力为Internet。
       networkCap: [connection.NetCap.NET_CAPABILITY_INTERNET]
     },
   };

   // 指定超时时间为10s(默认值为0)。
   let timeout = 10 * 1000;

   // 创建NetConnection对象。
   let conn = connection.createNetConnection(netSpecifier, timeout);
   // 订阅事件，如果当前指定网络可用，通过on_netAvailable通知用户。
   conn.on('netAvailable', ((handle: connection.NetHandle) => {
     let options: connection.QueryOptions = {
       family: connection.FamilyType.FAMILY_TYPE_IPV4
     }
     // 当指定网络可用时，使用该网络连接解析主机名，并仅获取IPv4类型的地址
     handle.getAddressesByNameWithOptions(this.hostName, options).then((data: connection.NetAddress[]) => {
       hilog.info(0x0000, 'testTag', `Succeeded to get data: ${JSON.stringify(data)}`);
     })
   }));
   // 订阅事件，如果当前指定网络不可用，通过on_netUnavailable通知用户。
   conn.on('netUnavailable', ((data: void) => {
     hilog.info(0x0000, 'testTag', `net is unavailable, data is ${JSON.stringify(data)}`);
   }));
   ```
