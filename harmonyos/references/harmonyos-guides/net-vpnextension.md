---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/net-vpnextension
title: 连接VPN
breadcrumb: 指南 > 系统 > 网络 > Network Kit（网络服务） > 连接网络 > 连接VPN
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:53+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0d1e55a53716061aaab73789abc9d41725c6085629586054426810fa267bb946
---

## 简介

VPN，即虚拟专用网络（Virtual Private Network），是在公用网络上建立专用网络的一种技术。在VPN网络中，任意两个节点间的连接并非依赖传统专用网络所需要的端到端的物理链路，而是构建在公用网络服务商提供的平台（如Internet）之上的逻辑网络。用户数据在这一逻辑链路中进行传输。

HarmonyOS为开发者提供了用于创建VPN的API解决方案。当前提供三方VPN能力主要用于创建虚拟网卡及配置VPN路由信息，连接隧道过程及内部连接的协议需要应用内部自行实现。本文将指导您如何开发自己的VPN客户端。

说明

* 为了保证应用的运行效率，所有API调用都是异步的，对于异步调用的API均提供了Promise的方式，以下示例均采用Promise方式，更多方式可以查阅[@ohos.net.vpnExtension (VPN增强管理)](../harmonyos-references/js-apis-net-vpnextension.md)。
* 完整的JS API说明以及示例代码请参考：[@ohos.net.vpnExtension (VPN增强管理)](../harmonyos-references/js-apis-net-vpnextension.md)。
* 使用该功能需要[ohos.permission.INTERNET](permissions-for-all.md#ohospermissioninternet)权限。

## VPN应用的显示体验

借助系统提供的[VPN Extension](../harmonyos-references/js-apis-net-vpnextension.md)接口开发者可以构建支持不同协议的VPN服务。HarmonyOS系统提供了界面 (UI) 使用户可以了解当前VPN应用服务的启动和连接：

* 在VPN应用首次启动连接之前，系统会显示VPN连接授权对话框。该对话框会提示用户是否信任该VPN应用并接受VPN连接请求。
* 当VPN启动连接成功时，状态栏显示一个VPN (钥匙) 图标以提醒用户VPN处于连接状态。

为了使用户可以方便的查看和配置，您的VPN应用还需要提供以下界面：

* 用于手动启动和停止连接的控件。
* 当VPN启动连接时，在通知栏显示VPN应用的连接状态或提供网络统计信息 (如连接时长、流量等) 。点击该通知能够将您的VPN应用调入前台。

## 开发步骤

### 创建VPN Extension Ability

如果想使您的应用支持VPN能力，首先您需要创建一个继承于VpnExtensionAbility的extensionAbilities。

```
1. // 举例：在应用的module.json5中定义MyVpnExtAbility。
2. "extensionAbilities": [
3. // ···
4. {
5. "name": "MyVpnExtAbility",
6. "srcEntry": "./ets/vpnability/VPNExtentionAbility.ets",
7. "type": "vpn"
8. }
9. ],
```

[module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/VPNControl_Case/entry/src/main/module.json5#L51-L74)

注意

如果DevEco Studio工具提示不能识别"type": "vpn"，需要您手动在SDK的toolchains\modulecheck\module.json文件中，给extensionAbilities对应的type枚举添加"vpn"定义，并清除build缓存和重启DevEco Studio工具。

接下来您需要在创建的VpnExtensionAbility中实现VPN的配置、启动和停止操作：

* 建立一个VPN的网络隧道，以UDP隧道为例（参考本文下方VPN Demo示例工程文件[napi\_init](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/NetWork_Kit/NetWorkKit_NetManager/VPNControl_Case/entry/src/main/cpp/napi_init.cpp)的UdpConnect()方法）；
* 通过VpnConnection.[protect](../harmonyos-references/js-apis-net-vpnextension.md#protect)保护前一步建立的UDP隧道；
* 构建VPN Config参数，参考[VPN Config参数说明](net-vpnextension.md#vpn-config参数说明)；
* 通过VpnConnection.[create](../harmonyos-references/js-apis-net-vpnextension.md#create)建立VPN网络连接；
* 处理虚拟网卡的数据，如：读写操作。

### 启动VPN Extension Ability

当VPN应用启动VPN连接时，需要调用startVpnExtensionAbility接口，携带需要启动的VpnExtensionAbility信息，其中bundleName需要与您的VPN应用bundleName一致，abilityName为您在前面创建的VpnExtensionAbility名。您可参考如下示例：

```
1. import { common, Want } from '@kit.AbilityKit';
2. import { vpnExtension } from '@kit.NetworkKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. // ···

6. const TITLE_FONT_SIZE = 35; // 标题字体大小
7. const BUTTON_FONT_SIZE = 25; // 按钮字体大小
8. const BUTTON_MARGIN = 16;

10. let want: Want = {
11. deviceId: '',
12. bundleName: 'com.samples.vpncontrol_case',
13. abilityName: 'MyVpnExtAbility',
14. };

16. @Entry
17. @Component
18. struct StartVpn {
19. @State message: string = 'VPN';
20. // ···
21. build() {
22. Row() {
23. Column() {
24. // ···
25. Text(this.message)
26. .fontSize(TITLE_FONT_SIZE)
27. .fontWeight(FontWeight.Bold)
28. // ···
29. .onClick(() => {
30. hilog.info(0x0000, 'testTag', 'developTag', '%{public}s', 'vpn Client');
31. })
32. // ···
33. Button($r('app.string.start_vpnExt'))
34. .onClick(() => {
35. // ···
36. vpnExtension.startVpnExtensionAbility(want)
37. // ···
38. })
39. .width('70%')
40. // ···
41. .fontSize(BUTTON_FONT_SIZE)
42. .margin(BUTTON_MARGIN)
43. // ···
44. }.width('100%');
45. }.height('100%');

47. }
48. }
```

[StartVpn.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/VPNControl_Case/entry/src/main/ets/pages/StartVpn.ets#L16-L196)

如果您的VPN应用未获取用户信任，系统将弹出VPN连接的授权对话框，当获取用户授权后，系统将自动调用并启动您实现的VPN Extension Ability的[onCreate](../harmonyos-references/js-apis-vpnextensionability.md#vpnextensionabilityoncreate)方法将被调用。

目前系统仅支持启动一个VPN连接服务，当VPN已经启动时应用新调用启动接口会收到系统拒绝错误，此时建议您的应用可以提醒用户先断开当前已经激活的VPN应用连接。

### 停止VPN Extension Ability

当VPN应用需要停止VPN连接时，需要调用stopVpnExtensionAbility接口，携带需要停止的VpnExtensionAbility信息。系统会对调用方做权限校验，stopVpnExtensionAbility的调用方应用必须获取了用户的VPN信任授权，且只允许停止应用自己启动的VpnExtensionAbility，所以接口传入的参数中bundleName需要与您的VPN应用bundleName一致，abilityName为指定停止VPN的VpnExtensionAbility名。

您可参考如下示例：

```
1. import { common, Want } from '@kit.AbilityKit';
2. import { vpnExtension } from '@kit.NetworkKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
```

[StopVpn.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/VPNControl_Case/entry/src/main/ets/pages/StopVpn.ets#L16-L20)

```
1. const TITLE_FONT_SIZE = 35; // 标题字体大小
2. const BUTTON_FONT_SIZE = 25; // 按钮字体大小
3. const BUTTON_MARGIN = 16;

5. let want: Want = {
6. deviceId: '',
7. bundleName: 'com.samples.vpncontrol_case',
8. abilityName: 'MyVpnExtAbility',
9. };

11. @Entry
12. @Component
13. struct StopVpn {
14. @State message: string = 'VPN';

16. // ...
17. build() {
18. Row() {
19. Column() {
20. // ...
21. Text(this.message)
22. .fontSize(TITLE_FONT_SIZE)
23. .fontWeight(FontWeight.Bold)
24. .onClick(() => {
25. hilog.info(0x0000, 'testTag', 'developTag', '%{public}s', 'vpn Client');
26. })
27. // ...
28. Button('Start Extension').onClick(() => {
29. vpnExtension.startVpnExtensionAbility(want);
30. }).width('70%').fontSize(20).margin(16);
31. Button($r('app.string.stop_vpnExt'))
32. .onClick(() => {
33. try {
34. hilog.info(0x0000, 'testTag', 'btn end')
35. vpnExtension.stopVpnExtensionAbility(want)
36. // ...
37. } catch (err) {
38. // ...
39. hilog.error(0x0000, 'testTag', 'developTag', 'stop vpnExt Fail %{public}s', JSON.stringify(err) ?? '');
40. }

42. })
43. .width('70%')
44. // ...
45. .fontSize(BUTTON_FONT_SIZE)
46. .margin(BUTTON_MARGIN)
47. }.width('100%');
48. }.height('100%');
49. }
50. }
```

[StopVpn.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/VPNControl_Case/entry/src/main/ets/pages/StopVpn.ets#L30-L131)

stopVpnExtensionAbility后，您的VPN Extension Ability的[onDestroy](../harmonyos-references/js-apis-vpnextensionability.md#vpnextensionabilityondestroy)方法将被调用，您可在此时destroy vpn连接。

```
1. private context = this.getUIContext().getHostContext() as common.VpnExtensionContext;
2. private vpnConnection: vpnExtension.VpnConnection = vpnExtension.createVpnConnection(this.context);

4. Destroy() {
5. hilog.info(0x0000, 'testTag', 'developTag', '%{public}s', 'vpn Destroy');
6. // ...
7. this.vpnConnection.destroy().then(() => {
8. hilog.info(0x0000, 'testTag', 'developTag', '%{public}s', 'vpn Destroy Success');
9. // ...
10. }).catch((err: Error) => {
11. hilog.error(0x0000, 'testTag', 'developTag', 'vpn Destroy Failed: %{public}s', JSON.stringify(err) ?? '');
12. // ...
13. })
14. }
```

[StopVpn.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/VPNControl_Case/entry/src/main/ets/pages/StopVpn.ets#L49-L72)

### 生成VPN Id

创建新的VPN时，应生成一个VPN Id作为VPN的唯一标识。

可参考如下示例：

```
1. import { vpnExtension, VpnExtensionAbility } from '@kit.NetworkKit';
2. // ...
3. export class VpnTest extends VpnExtensionAbility {
4. public vpnId: string = '';
5. // ...
6. getVpnId() {
7. // ...
8. let vpnConnection = vpnExtension.createVpnConnection(this.context);
9. vpnConnection?.generateVpnId().then((data) => {
10. if (data) {
11. this.vpnId = data;
12. }
13. });
14. // ...
15. }
16. };
```

[GetVpnIdTest.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/VPNControl_Case/entry/src/main/ets/vpnability/GetVpnIdTest.ets#L16-L44)

### 断开VPN

若需断开VPN，可参考如下示例：

```
1. import { vpnExtension, VpnExtensionAbility } from '@kit.NetworkKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. // ...
4. export class VpnTest extends VpnExtensionAbility {
5. public vpnId: string = 'test_vpn_id';
6. public vpnConnection: vpnExtension.VpnConnection | undefined;
7. // ...
8. destroy() {
9. // ...
10. this.vpnConnection = vpnExtension.createVpnConnection(this.context);
11. hilog.info(0x0000, 'testTag', 'create success');
12. this.vpnConnection?.destroy(this.vpnId);
13. // ...
14. }
15. };
```

[DestroyVpnTest.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/VPNControl_Case/entry/src/main/ets/vpnability/DestroyVpnTest.ets#L16-L44)

## 服务生命周期

为了保障设备的网络连接，当系统观察到VPN相关应用出现异常时会主动停止VPN连接：

* 当调用startVpnExtensionAbility接口的应用进程退出时。
* 当VPN服务进程销毁时。

## VPN Config参数说明

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| addresses | Array<[LinkAddress](../harmonyos-references/js-apis-net-connection.md#linkaddress)> | 否 | 否 | VPN虚拟网卡的IP地址。 |
| routes | Array<[RouteInfo](../harmonyos-references/js-apis-net-connection.md#routeinfo)> | 否 | 是 | VPN虚拟网卡的路由信息(目前最多可配置1024条路由)。 |
| dnsAddresses | Array<string> | 否 | 是 | DNS服务器地址信息。配置DNS服务器地址后，VPN启动状态下，被代理的应用上网时，使用配置的DNS服务器进行DNS查询。 |
| searchDomains | Array<string> | 否 | 是 | DNS的搜索域列表。 |
| mtu | number | 否 | 是 | 最大传输单元MTU值(单位：字节)。 |
| isIPv4Accepted | boolean | 否 | 是 | 是否支持IPV4，默认值为true。true：支持IPV4；false：不支持IPV4。 |
| isIPv6Accepted | boolean | 否 | 是 | 是否支持IPV6，默认值为false。true：支持IPV6；false：不支持IPV6。 |
| isInternal | boolean | 否 | 是 | 是否支持内置VPN，默认值为false。true：支持内置VPN；false：不支持内置VPN。 |
| isBlocking | boolean | 否 | 是 | 是否阻塞模式，默认值为false。true：是阻塞模式；false：不是阻塞模式。 |
| trustedApplications | Array<string> | 否 | 是 | 受信任的应用信息列表，以string类型表示的包名。配置此列表后，仅列表中的应用数据才能根据routes被VPN代理。  注：trustedApplications和blockedApplications列表不能同时配置。 |
| blockedApplications | Array<string> | 否 | 是 | 被阻止的应用信息列表，string类型表示的包名。当配置该列表后，该列表中的应用数据不会被VPN代理，其他应用可以根据routes配置被VPN代理。  注：trustedApplications和blockedApplications列表不能同时配置。 |

**示例：**

```
1. import { vpnExtension } from '@kit.NetworkKit';
2. import { common } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
```

[SetupVpn.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/VPNControl_Case/entry/src/main/ets/pages/SetupVpn.ets#L16-L20)

```
1. let vpnConfig: vpnExtension.VpnConfig = {
2. // 配置VPN虚拟网卡的IP地址。
3. addresses: [{
4. address: {
5. address:'192.x.x.5',
6. family:1
7. },
8. prefixLength:24
9. }],
10. // 配置路由参数。
11. routes: [{
12. // VPN虚拟网卡接口名固定为“vpn-tun”。
13. interface: 'vpn-tun',
14. destination: {
15. address: {
16. address:'10.x.x.8',
17. family:1,
18. port:8080
19. },
20. prefixLength:24
21. },
22. gateway: {
23. address:'10.x.x.5',
24. family:1,
25. port:8080
26. },
27. hasGateway: false,
28. isDefaultRoute: false,
29. }],
30. // 配置最大传输单元值。
31. mtu: 1400,
32. // 配置VPN使用的DNS服务器。
33. dnsAddresses: ['223.x.x.5', '223.x.x.6'],
34. // 受信任的应用信息列表。
35. trustedApplications: ['com.test.browser'],
36. // 被阻止的应用信息列表。
37. blockedApplications: ['com.test.games'],
38. }
```

```
1. let context = this.getUIContext().getHostContext() as common.VpnExtensionContext;
2. let vpnConnection: vpnExtension.VpnConnection = vpnExtension.createVpnConnection(context);
3. // 创建 VPN 连接并应用配置
4. vpnConnection.create(vpnConfig).then((data) => {
5. hilog.info(0x0000, 'testTag', 'vpn create ' + JSON.stringify(data));
6. // ...
7. })
```

[SetupVpn.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/NetWork_Kit/NetWorkKit_NetManager/VPNControl_Case/entry/src/main/ets/pages/SetupVpn.ets#L144-L163)

## VPN Demo示例

HarmonyOS开源项目包含一个名为[VPN](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/NetWork_Kit/NetWorkKit_NetManager/VPNControl_Case)的示例应用。此应用展示了如何设置和连接 VPN 服务。
