---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/net-dns
title: 使用DNS解析域名
breadcrumb: 指南 > 系统 > 网络 > Network Kit（网络服务） > 访问网络 > 使用DNS解析域名
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:52+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:90f798d7fd95d2441cd94531433db44c635f1bcdb2438c38802ccbc13630b819
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

说明

在本文档的示例中，资源文件中hostName需修改成一个实际的中文域名。

完整示例代码见：[DNS\_case](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/NetWork_Kit/NetWorkKit_Datatransmission/DNS_case)

1. 导入所需文件。

   ```
   1. import { connection } from '@kit.NetworkKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```

   [Unicode.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/DNS_case/entry/src/main/ets/pages/Unicode.ets#L16-L20)
2. 初始化数据成员。

   ```
   1. @State hostVal: string = '';     // 转码之后的主机名
   2. @State ipResult: string = '';    // 获取的IP地址结果
   3. private hostName: string = '';   // 初始主机名
   ```

   [Unicode.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/DNS_case/entry/src/main/ets/pages/Unicode.ets#L26-L30)
3. 获取资源文件中hostName值并赋值。

   ```
   1. aboutToAppear() {
   2. this.hostName =
   3. (this.getUIContext().getHostContext() as Context).resourceManager.getStringSync($r('app.string.hostName').id);
   4. }
   ```

   [Unicode.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/DNS_case/entry/src/main/ets/pages/Unicode.ets#L32-L37)
4. 创建网络地址解析函数，将域名转换为IP地址，isChange为是否将域名转码为ASCII编码的标识。

   ```
   1. getAddressName(isChange: boolean) {
   2. this.ipResult = '';
   3. connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
   4. if (netHandle.netId === 0) {
   5. // 当前没有已连接的网络时，netHandler的netId为0，属于异常场景。可根据实际情况添加处理机制。
   6. return;
   7. }
   8. if (isChange) {
   9. this.hostVal = connection.getDnsAscii(this.hostName);
   10. } else {
   11. this.hostVal = '';
   12. }
   13. netHandle.getAddressByName(isChange ? this.hostVal : this.hostName,
   14. (error: BusinessError, data: connection.NetAddress) => {
   15. if (error) {
   16. this.ipResult = `Failed to get address. Code:${error.code}, message:${error.message}`;
   17. hilog.error(0x0000, 'testTag', `Failed to get address. Code:${error.code}, message:${error.message}`);
   18. return;
   19. }
   20. this.ipResult = JSON.stringify(data);
   21. hilog.info(0x0000, 'testTag', `Succeeded to get data: ${JSON.stringify(data)}`);
   22. });
   23. });
   24. }
   ```

   [Unicode.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/DNS_case/entry/src/main/ets/pages/Unicode.ets#L39-L65)
5. 获取中文域名地址对应的IP。由于未经过ASCII编码，因此预期结果为获取IP失败。

   ```
   1. this.getAddressName(false);
   ```

   [Unicode.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/DNS_case/entry/src/main/ets/pages/Unicode.ets#L77-L79)
6. 将中文域名转换为对应ASCII编码后获取对应IP。

   ```
   1. this.getAddressName(true);
   ```

   [Unicode.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/DNS_case/entry/src/main/ets/pages/Unicode.ets#L82-L84)
7. 将转换后的ASCII编码转成原中文域名。

   ```
   1. this.hostVal = connection.getDnsUnicode(this.hostVal);
   ```

   [Unicode.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/DNS_case/entry/src/main/ets/pages/Unicode.ets#L96-L98)

## DNS接口支持配置获取的IP地址类型

从API version 23开始，DNS解析支持通过options参数指定IP地址类型（如 IPv4 或 IPv6），也支持在特定的网络连接NetHandle上按给定的IP类型解析主机名，从而实现更精准的地址解析。

完整示例代码见：[DNS\_case](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/NetWork_Kit/NetWorkKit_Datatransmission/DNS_case)

1. 导入所需文件。

   ```
   1. import { connection } from '@kit.NetworkKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```

   [DNS.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/DNS_case/entry/src/main/ets/pages/DNS.ets#L16-L19)
2. 初始化数据成员。

   ```
   1. @State hostName: string = 'www.example.com';
   ```

   [DNS.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/DNS_case/entry/src/main/ets/pages/DNS.ets#L25-L27)
3. 使用当前默认网络解析主机名以获取所有IP地址。

   ```
   1. connection.getAddressesByName(this.hostName).then((data: connection.NetAddress[]) => {
   2. hilog.info(0x0000, 'testTag', `Succeeded to get data: ${JSON.stringify(data)}`);
   3. })
   ```

   [DNS.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/DNS_case/entry/src/main/ets/pages/DNS.ets#L34-L38)
4. 使用当前默认网络，指定IP类型解析主机名以获取指定IP地址。

   ```
   1. let options: connection.QueryOptions = {
   2. family: connection.FamilyType.FAMILY_TYPE_IPV4
   3. };
   4. connection.getAddressesByNameWithOptions(this.hostName, options).then((data: connection.NetAddress[]) => {
   5. hilog.info(0x0000, 'testTag', `Succeeded to get data: ${JSON.stringify(data)}`);
   6. });
   ```

   [DNS.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/DNS_case/entry/src/main/ets/pages/DNS.ets#L44-L51)
5. 使用指定的网络连接（NetHandle），并按给定的IP类型解析主机名。

   ```
   1. let netSpecifier: connection.NetSpecifier = {
   2. netCapabilities: {
   3. // 假设当前默认网络是WiFi，需要创建蜂窝网络连接，可指定网络类型为蜂窝网。
   4. bearerTypes: [connection.NetBearType.BEARER_CELLULAR],
   5. // 指定网络能力为Internet。
   6. networkCap: [connection.NetCap.NET_CAPABILITY_INTERNET]
   7. },
   8. };

   10. // 指定超时时间为10s(默认值为0)。
   11. let timeout = 10 * 1000;

   13. // 创建NetConnection对象。
   14. let conn = connection.createNetConnection(netSpecifier, timeout);
   15. // 订阅事件，如果当前指定网络可用，通过on_netAvailable通知用户。
   16. conn.on('netAvailable', ((handle: connection.NetHandle) => {
   17. let options: connection.QueryOptions = {
   18. family: connection.FamilyType.FAMILY_TYPE_IPV4
   19. }
   20. // 当指定网络可用时，使用该网络连接解析主机名，并仅获取IPv4类型的地址
   21. handle.getAddressesByNameWithOptions(this.hostName, options).then((data: connection.NetAddress[]) => {
   22. hilog.info(0x0000, 'testTag', `Succeeded to get data: ${JSON.stringify(data)}`);
   23. })
   24. }));
   25. // 订阅事件，如果当前指定网络不可用，通过on_netUnavailable通知用户。
   26. conn.on('netUnavailable', ((data: void) => {
   27. hilog.info(0x0000, 'testTag', `net is unavailable, data is ${JSON.stringify(data)}`);
   28. }));
   ```

   [DNS.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_Datatransmission/DNS_case/entry/src/main/ets/pages/DNS.ets#L57-L86)
