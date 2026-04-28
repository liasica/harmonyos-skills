---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-vpnextension
title: @ohos.net.vpnExtension (VPN增强管理)
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > ArkTS API > @ohos.net.vpnExtension (VPN增强管理)
category: harmonyos-references
scraped_at: 2026-04-28T08:08:26+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:180955d8897f360f11ee61fdd91583f29560daeb248147d7ac2dc56c9d4c2ab2
---

三方VPN管理模块，支持三方VPN的启动和停止功能。三方VPN是指由第三方提供的VPN服务，它们通常提供更多的功能和更广泛的网络连接选项，包括更多的安全和隐私功能，以及更全面的定制选项。当前提供三方VPN能力主要用于创建虚拟网卡及配置VPN路由信息，连接隧道过程及内部连接的协议需要应用内部自行实现。

说明

本模块首批接口从 API version 11 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

以下模块不支持在VpnExtensionAbility中引用，可能会导致程序异常退出。

* [@ohos.contact (联系人)](js-apis-contact.md)
* [@ohos.geolocation](js-apis-geolocation.md)、[@ohos.geoLocationManager (位置服务)](js-apis-geolocationmanager.md)
* [@ohos.multimedia.audio(音频管理)](arkts-apis-audio.md)
* [@ohos.multimedia.camera(相机管理)](arkts-apis-camera.md)
* [@ohos.telephony.call (拨打电话)](js-apis-call.md)
* [@ohos.telephony.sim (SIM卡管理)](js-apis-sim.md)
* [@ohos.telephony.sms (短信服务)](js-apis-sms.md)

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { vpnExtension } from '@kit.NetworkKit';
```

## LinkAddress

PhonePC/2in1TabletTVWearable

type LinkAddress = connection.LinkAddress

获取网络链接信息。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 类型 | 说明 |
| --- | --- |
| [connection.LinkAddress](js-apis-net-connection.md#linkaddress) | 网络链路信息。 |

## RouteInfo

PhonePC/2in1TabletTVWearable

type RouteInfo = connection.RouteInfo

获取网络路由信息。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 类型 | 说明 |
| --- | --- |
| [connection.RouteInfo](js-apis-net-connection.md#routeinfo) | 网络路由信息。 |

## VpnExtensionContext

PhonePC/2in1TabletTVWearable

type VpnExtensionContext = \_VpnExtensionContext

VPN扩展的上下文。它允许访问serviceExtension特定资源。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| [\_VpnExtensionContext](js-apis-inner-application-vpnextensioncontext.md) | VPN扩展的上下文。 |

## vpnExtension.startVpnExtensionAbility

PhonePC/2in1TabletTVWearable

startVpnExtensionAbility(want: Want): Promise<void>

启动新的三方VPN功能。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 指示要启动的信息。  **说明：** 从API version 22开始，支持在VPN首次启动时传递want中的parameters字段。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[元能力子系统错误码](errorcode-ability.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter is not valid parameter. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |
| 16200001 | The caller has been released. |

**示例：**

Stage 模型示例：

```
1. import { Want } from '@kit.AbilityKit';
2. import { vpnExtension } from '@kit.NetworkKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let want: Want = {
6. deviceId: "",
7. bundleName: "com.example.myvpndemo",
8. abilityName: "MyVpnExtAbility",
9. };

11. @Entry
12. @Component
13. struct Index {
14. @State message: string = 'Hello World'

16. build() {
17. Row() {
18. Column() {
19. Text(this.message)
20. .fontSize(40)
21. .fontWeight(FontWeight.Bold).onClick(() => {
22. console.info("btn click")
23. })
24. Button('Start Extension').onClick(() => {
25. vpnExtension.startVpnExtensionAbility(want).then(() => {
26. console.info('startVpnExtensionAbility success');
27. }).catch((err: BusinessError) => {
28. console.error('startVpnExtensionAbility error: ' + JSON.stringify(err));
29. })
30. }).width('70%').fontSize(30).margin(16)
31. }.width('100%')
32. }.height('100%')
33. }
34. }
```

## vpnExtension.stopVpnExtensionAbility

PhonePC/2in1TabletTVWearable

stopVpnExtensionAbility(want: Want): Promise<void>

停止同一应用程序中的服务。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 指示要启动的信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[元能力子系统错误码](errorcode-ability.md)和[通用错误码](errorcode-universal.md)。

| 错误码 ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter is not valid parameter. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000006 | Cross-user operations are not allowed. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |
| 16200001 | The caller has been released. |

**示例：**

Stage 模型示例：

```
1. import { Want } from '@kit.AbilityKit';
2. import { vpnExtension } from '@kit.NetworkKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let want: Want = {
6. deviceId: "",
7. bundleName: "com.example.myvpndemo",
8. abilityName: "MyVpnExtAbility",
9. };

11. @Entry
12. @Component
13. struct Index {
14. @State message: string = 'Hello World'

16. build() {
17. Row() {
18. Column() {
19. Text(this.message)
20. .fontSize(50)
21. .fontWeight(FontWeight.Bold).onClick(() => {
22. console.info("btn click")
23. })
24. Button('Start Extension').onClick(() => {
25. vpnExtension.startVpnExtensionAbility(want).then(() => {
26. console.info('startVpnExtensionAbility success');
27. }).catch((err: BusinessError) => {
28. console.error('startVpnExtensionAbility error: ' + JSON.stringify(err));
29. })
30. }).width('70%').fontSize(30).margin(16)
31. Button('Stop Extension').onClick(() => {
32. console.info("btn end")
33. vpnExtension.stopVpnExtensionAbility(want).then(() => {
34. console.info('stopVpnExtensionAbility success');
35. }).catch((err: BusinessError) => {
36. console.error('stopVpnExtensionAbility error: ' + JSON.stringify(err));
37. })
38. }).width('70%').fontSize(30).margin(16)

40. }.width('100%')
41. }.height('100%')
42. }
43. }
```

## vpnExtension.createVpnConnection

PhonePC/2in1TabletWearable

createVpnConnection(context: VpnExtensionContext): VpnConnection

创建一个三方VPN连接对象。

说明

调用createVpnConnection接口前，需要先调用startVpnExtensionAbility接口启用VPN功能。

**系统能力**：SystemCapability.Communication.NetManager.Vpn

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [VpnExtensionContext](js-apis-inner-application-vpnextensioncontext.md) | 是 | 指定 context。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [VpnConnection](js-apis-net-vpnextension.md#vpnconnection) | 返回一个VPN连接对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例：**

Stage 模型示例：

```
1. import { vpnExtension, VpnExtensionAbility } from '@kit.NetworkKit';
2. import { common, Want } from '@kit.AbilityKit';

4. let context: vpnExtension.VpnExtensionContext;
5. export default class MyVpnExtAbility extends VpnExtensionAbility {
6. onCreate(want: Want) {
7. let vpnConnection : vpnExtension.VpnConnection = vpnExtension.createVpnConnection(context);
8. console.info("VPN createVpnConnection: " + JSON.stringify(vpnConnection));
9. }
10. }
```

## VpnConnection

PhonePC/2in1TabletWearable

VPN连接对象。在调用VpnConnection的方法前，需要先通过vpnExt.createVpnConnection创建VPN连接对象。

### create

PhonePC/2in1TabletWearable

create(config: VpnConfig): Promise<number>

使用config创建一个VPN网络。使用Promise异步回调。

说明

建议在不需要VPN网络的时候配对调用[destroy()](js-apis-net-vpnextension.md#destroy)或[destroy(vpnId: string)](js-apis-net-vpnextension.md#destroy20)接口销毁启动的VPN网络，并执行资源清理等操作。

**系统能力**：SystemCapability.Communication.NetManager.Vpn

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [VpnConfig](js-apis-net-vpnextension.md#vpnconfig) | 是 | 指定VPN网络的配置信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 以 Promise 形式返回获取结果，返回指定虚拟网卡的文件描述符 fd。 |

**错误码：**

以下错误码的详细介绍请参见[VPN错误码](errorcode-net-vpn.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2200001 | Invalid parameter value. |
| 2200002 | Operation failed. Cannot connect to service. |
| 2200003 | System internal error. |
| 2203001 | VPN creation denied, please check the user type. |
| 2203002 | VPN exist already, please execute destroy first. |

**示例：**

```
1. import { vpnExtension, VpnExtensionAbility } from '@kit.NetworkKit';
2. import { common, Want } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let context: vpnExtension.VpnExtensionContext;
6. export default class MyVpnExtAbility extends VpnExtensionAbility {
7. private tunIp: string = '10.0.0.5';
8. private blockedAppName: string = 'com.example.myvpndemo';
9. onCreate(want: Want) {
10. let vpnConnection : vpnExtension.VpnConnection = vpnExtension.createVpnConnection(context);
11. console.info("vpn createVpnConnection: " + JSON.stringify(vpnConnection));
12. this.SetupVpn();

14. // 不需要VPN网络时，调用destroy()接口销毁启动的VPN网络，并执行资源清理等操作。
15. vpnConnection.destroy().then(() => {
16. console.info("destroy success.");
17. }).catch((error : BusinessError) => {
18. console.error(`destroy fail. Code:${error.code}, message:${error.message}`);
19. });
20. }
21. SetupVpn() {
22. class Address {
23. address: string;
24. family: number;

26. constructor(address: string, family: number) {
27. this.address = address;
28. this.family = family;
29. }
30. }

32. class AddressWithPrefix {
33. address: Address;
34. prefixLength: number;

36. constructor(address: Address, prefixLength: number) {
37. this.address = address;
38. this.prefixLength = prefixLength;
39. }
40. }

42. class Config {
43. addresses: AddressWithPrefix[];
44. mtu: number;
45. dnsAddresses: string[];
46. trustedApplications: string[];
47. blockedApplications: string[];

49. constructor(
50. tunIp: string,
51. blockedAppName: string
52. ) {
53. this.addresses = [
54. new AddressWithPrefix(new Address(tunIp, 1), 24)
55. ];
56. this.mtu = 1400;
57. this.dnsAddresses = ["114.114.114.114"];
58. this.trustedApplications = [];
59. this.blockedApplications = [blockedAppName];
60. }
61. }

63. let config = new Config(this.tunIp, this.blockedAppName);

65. try {
66. let vpnConnection : vpnExtension.VpnConnection = vpnExtension.createVpnConnection(context);
67. vpnConnection.create(config).then((data) => {
68. hilog.error(0x0000, 'developTag', 'tunfd: %{public}s', JSON.stringify(data) ?? '');
69. })
70. } catch (error) {
71. hilog.error(0x0000, 'developTag', 'VPN setUp fail: %{public}s', JSON.stringify(error) ?? '');
72. }
73. }
74. }
```

### protect

PhonePC/2in1TabletWearable

protect(socketFd: number): Promise<void>

保护套接字不受VPN连接影响，通过该套接字发送的数据将直接基于物理网络收发，因此其流量不会通过VPN转发。使用Promise方式作为异步方法。

**系统能力**：SystemCapability.Communication.NetManager.Vpn

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| socketFd | number | 是 | 指定保护的 socketfd，该文件描述符通过[getSocketFd](js-apis-socket.md#getsocketfd10-1)获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[VPN错误码](errorcode-net-vpn.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2200001 | Invalid parameter value. |
| 2200002 | Operation failed. Cannot connect to service. |
| 2200003 | System internal error. |
| 2203004 | Invalid socket file descriptor. |

**示例：**

```
1. import { vpnExtension, VpnExtensionAbility } from '@kit.NetworkKit';
2. import { common, Want } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. let g_tunnelFd = -1;
6. let context: vpnExtension.VpnExtensionContext;
7. export default class MyVpnExtAbility extends VpnExtensionAbility {
8. private vpnServerIp: string = '192.168.31.13';
9. onCreate(want: Want) {
10. let vpnConnection : vpnExtension.VpnConnection = vpnExtension.createVpnConnection(context);
11. console.info("VPN createVpnConnection: " + JSON.stringify(vpnConnection));
12. this.CreateTunnel();
13. this.Protect();
14. }
15. CreateTunnel() {
16. g_tunnelFd = 8888;
17. }
18. Protect() {
19. hilog.info(0x0000, 'developTag', '%{public}s', 'VPN Protect');
20. let vpnConnection : vpnExtension.VpnConnection = vpnExtension.createVpnConnection(context);
21. vpnConnection.protect(g_tunnelFd).then(() => {
22. hilog.info(0x0000, 'developTag', '%{public}s', 'VPN Protect Success');
23. }).catch((err : Error) => {
24. hilog.error(0x0000, 'developTag', 'VPN Protect Failed %{public}s', JSON.stringify(err) ?? '');
25. })
26. }
27. }
```

### destroy

PhonePC/2in1TabletWearable

destroy(): Promise<void>

销毁启动的VPN网络。使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetManager.Vpn

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[VPN错误码](errorcode-net-vpn.md)和[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 2200002 | Operation failed. Cannot connect to service. |
| 2200003 | System internal error. |

**示例：**

```
1. import { vpnExtension, VpnExtensionAbility } from '@kit.NetworkKit';
2. import { common, Want } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let context: vpnExtension.VpnExtensionContext;
6. export default class MyVpnExtAbility extends VpnExtensionAbility {
7. onCreate(want: Want) {
8. let vpnConnection : vpnExtension.VpnConnection = vpnExtension.createVpnConnection(context);
9. console.info("VPN createVpnConnection: " + JSON.stringify(vpnConnection));
10. vpnConnection.destroy().then(() => {
11. console.info("destroy success.");
12. }).catch((error : BusinessError) => {
13. console.error("destroy fail" + JSON.stringify(error));
14. });
15. }
16. }
```

### destroy20+

PhonePC/2in1TabletWearable

destroy(vpnId: string): Promise<void>

根据vpnId销毁指定的VPN网络。使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetManager.Vpn

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| vpnId | string | 是 | vpn唯一标识。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[VPN错误码](errorcode-net-vpn.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19900001 | Invalid parameter value. |
| 19900002 | System internal error. |

**示例：**

```
1. import { vpnExtension, VpnExtensionAbility } from '@kit.NetworkKit';
2. import { BusinessError } from "@kit.BasicServicesKit";

4. export default class MyVpnExtAbility extends VpnExtensionAbility {
5. onCreate() {
6. let vpnConnection = vpnExtension.createVpnConnection(this.context);

8. // 可通过generateVpnId()获取vpnId
9. let vpnId = 'testVpnId';
10. vpnConnection.destroy(vpnId).then(() => {
11. console.info("destroy success");
12. }).catch((error: BusinessError) => {
13. console.error(`destroy fail, Code is ${error.code}, message is ${error.message}`);
14. });
15. }
16. }
```

### generateVpnId20+

PhonePC/2in1TabletWearable

generateVpnId(): Promise<string>

生成VPN唯一标识。使用Promise异步回调。

如需使用系统多VPN能力，需调用该接口生成vpnId，配置到VpnConfig中。

注意

当前系统多VPN能力仅支持IPv4。

**系统能力**：SystemCapability.Communication.NetManager.Vpn

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | 以Promise形式返回获取结果，返回vpnId。 |

**错误码：**

以下错误码的详细介绍请参见[VPN错误码](errorcode-net-vpn.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 19900001 | Invalid parameter value. |
| 19900002 | System internal error. |

**示例：**

```
1. import { vpnExtension, VpnExtensionAbility } from '@kit.NetworkKit';
2. import { BusinessError } from "@kit.BasicServicesKit";

4. export default class MyVpnExtAbility extends VpnExtensionAbility {
5. onCreate() {
6. let vpnConnection = vpnExtension.createVpnConnection(this.context);
7. vpnConnection.generateVpnId().then((data) => {
8. if (data) {
9. console.info("generateVpnId success, vpnId = " + JSON.stringify(data));
10. }
11. }).catch((error: BusinessError) => {
12. console.error(`generateVpnId fail, Code is ${error.code}, message is ${error.message}`);
13. });
14. }
15. }
```

### protectProcessNet22+

PhonePC/2in1TabletWearable

protectProcessNet(): Promise<void>

保护应用进程不受VPN连接影响，被保护的进程直接基于物理网络收发数据，流量不通过VPN转发。使用Promise异步回调。

**系统能力**：SystemCapability.Communication.NetManager.Vpn

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**示例：**

```
1. import { vpnExtension, VpnExtensionAbility } from '@kit.NetworkKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. let g_tunnelFd = -1;
5. export default class MyVpnExtAbility  extends VpnExtensionAbility {
6. onCreate() {
7. let vpnConnection = vpnExtension.createVpnConnection(this.context);
8. console.info("VPN createVpnConnection: " + JSON.stringify(vpnConnection));
9. this.ProtectNetByProcess();
10. }
11. CreateTunnel() {
12. g_tunnelFd = 8888;
13. }
14. ProtectNetByProcess() {
15. hilog.info(0x0000, 'developTag', '%{public}s', 'vpn ProtectNetByProcess');
16. let vpnConnection = vpnExtension.createVpnConnection(this.context);
17. vpnConnection.protectProcessNet().then(() => {
18. hilog.info(0x0000, 'developTag', '%{public}s', 'vpn ProtectNetByProcess Success');
19. this.CreateTunnel();
20. }).catch((err: Error) => {
21. hilog.error(0x0000, 'developTag', 'vpn ProtectNetByProcess Failed %{public}s', JSON.stringify(err) ?? '');
22. })
23. }
24. }
```

## VpnConfig

PhonePC/2in1TabletWearable

三方VPN配置参数。

**系统能力**：SystemCapability.Communication.NetManager.Vpn

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| addresses | Array<[LinkAddress](js-apis-net-connection.md#linkaddress)> | 否 | 否 | VPN虚拟网卡的IP地址。API version 23之前，最多支持64个IP地址；从API version 23开始，最多支持2000个IP地址。 |
| vpnId20+ | string | 否 | 是 | VPN唯一标识。 |
| routes | Array<[RouteInfo](js-apis-net-connection.md#routeinfo)> | 否 | 是 | VPN虚拟网卡的路由信息（API version 23前最多可配置1024条路由；从API version 23开始最多可配置10000条路由）。 |
| dnsAddresses | Array<string> | 否 | 是 | DNS服务器地址信息。当配置DNS服务器地址后，VPN启动状态下被代理的应用上网时，使用配置的DNS服务器做DNS查询。 |
| searchDomains | Array<string> | 否 | 是 | DNS的搜索域列表。 |
| mtu | number | 否 | 是 | 最大传输单元MTU值（单位：字节）。取值范围：[576，1500]。 |
| isIPv4Accepted | boolean | 否 | 是 | 是否支持IPv4。true表示支持，false表示不支持, 默认值为true。  **注意**：若支持IPv4功能，需要在addresses中配置IPv4类型的IP地址。 |
| isIPv6Accepted | boolean | 否 | 是 | 是否支持IPv6。true表示支持，false表示不支持, 默认值为false。  **注意**：若支持IPv6功能，需要在addresses中配置IPv6类型的IP地址。 |
| isInternal | boolean | 否 | 是 | 是否支持内置VPN。true表示支持，false表示不支持, 默认值为false。 |
| isBlocking | boolean | 否 | 是 | 是否阻塞模式。true表示阻塞模式，false表示非阻塞模式, 默认值为false。 |
| trustedApplications | Array<string> | 否 | 是 | 受信任的应用信息列表，string类型表示的包名。当配置该列表后，仅该列表中的应用数据才能根据routes被VPN代理。API version 23前最多可配置64个受信任的应用包名；从API version 23开始最多可配置256个受信任的应用包名。  **注意**：trustedApplications和blockedApplications列表不能同时配置。 |
| blockedApplications | Array<string> | 否 | 是 | 被阻止的应用信息列表，string类型表示的包名。当配置该列表后，该列表中的应用数据不会被VPN代理，其他应用可以根据routes配置被VPN代理。API version 23前最多可配置64个被阻止的应用包名；从API version 23开始最多可配置256个被阻止的应用包名。  **注意**：trustedApplications和blockedApplications列表不能同时配置。 |

**示例：**

```
1. import { vpnExtension} from '@kit.NetworkKit';

3. let vpnConfig: vpnExtension.VpnConfig = {
4. addresses: [],
5. vpnId: '123',
6. routes: [{
7. interface: "eth0",
8. destination: {
9. address: {
10. address:'',
11. family:1,
12. port:8080
13. },
14. prefixLength:1
15. },
16. gateway: {
17. address:'',
18. family:1,
19. port:8080
20. },
21. hasGateway: true,
22. isDefaultRoute: true,
23. }],
24. mtu: 1400,
25. dnsAddresses: ["223.5.5.5", "223.6.6.6"],
26. trustedApplications: [],
27. blockedApplications: [],
28. }
29. let context: vpnExtension.VpnExtensionContext;

31. function vpnCreate(){
32. let vpnConnection: vpnExtension.VpnConnection = vpnExtension.createVpnConnection(context);
33. vpnConnection.create(vpnConfig).then((data) => {
34. console.info("VPN create " + JSON.stringify(data));
35. })
36. }
```
