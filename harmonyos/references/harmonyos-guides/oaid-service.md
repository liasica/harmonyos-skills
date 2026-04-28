---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/oaid-service
title: 开放匿名设备标识服务
breadcrumb: 指南 > 应用服务 > Ads Kit（广告服务） > 开放匿名设备标识服务
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8eff7d9ea91036e0f864f2f626a1408010c56e3e0827f009364c66995789b59e
---

## 获取OAID信息

### 场景介绍

开放匿名设备标识符（Open Anonymous Device Identifier, OAID，以下简称OAID）：是一种非永久性设备标识符，基于开放匿名设备标识符，可在保护用户个人数据隐私安全的前提下，向用户提供个性化广告，同时三方监测平台也可以向广告主提供转化归因分析。

媒体App、广告平台、三方监测平台等开发者，可获取设备上的OAID，您可基于OAID进行个性化广告推荐或广告转化归因分析。

OAID是基于华为自有算法生成的32位类UUID（Universally Unique Identifier）标识符，格式为xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx。

OAID的特性：

* OAID是设备级标识符，同一台设备上不同的App获取到的OAID值一样。
* OAID的获取受应用的“跨应用关联访问权限”开关影响：当应用的“跨应用关联访问权限”开关开启时，该应用可获取到非全0的有效OAID；当应用的“跨应用关联访问权限”开关关闭时，该应用仅能获取到全0的OAID。
* 同一台设备上首个应用开启应用“跨应用关联访问权限”开关时，会首次生成OAID。

  说明

  设置项“跨应用关联访问权限”在HarmonyOS NEXT Developer Beta5及更早版本名称为“应用跟踪访问权限”。

OAID会在下述场景中发生变化：

* 用户将设备恢复出厂设置。
* 用户操作重置OAID。

### 约束和限制

开放匿名设备标识服务能力支持Phone、Tablet、PC/2in1设备，并且从6.0.0（20）版本开始，新增支持TV设备。

使用PC/2in1设备时，需要确保设备上智慧营销服务或广告服务的版本在8.4.80.300及以上，版本号可通过选择“设置> 应用和元服务 > 更多应用”查看。

获取OAID信息前，请确保已充分告知用户相关信息并取得用户授权同意。请务必先弹出隐私协议窗口，获得用户的明确同意后再获取OAID。未经用户同意，获取 OAID 将涉嫌违反数据采集相关规定，可能会面临隐私合规风险。

### 接口说明

| 接口名 | 描述 |
| --- | --- |
| [getOAID](../harmonyos-references/js-apis-oaid.md#identifiergetoaid)(): Promise<string> | 获取OAID，通过Promise异步返回结果。 |
| [getOAID](../harmonyos-references/js-apis-oaid.md#identifiergetoaid-1)(callback: AsyncCallback<string>): void | 获取OAID，通过Callback异步回调返回值。 |

说明

如调用getOAID接口需要申请ohos.permission.APP\_TRACKING\_CONSENT权限，且“要求应用请求关联”保持关闭状态。存在如下三种情况：

1.如应用已配置ohos.permission.APP\_TRACKING\_CONSENT权限，且“跨应用关联访问权限”为“允许”，则返回OAID。

2.如应用已配置ohos.permission.APP\_TRACKING\_CONSENT权限，且“跨应用关联访问权限”为“禁止”，则返回00000000-0000-0000-0000-000000000000。

3.如应用未配置ohos.permission.APP\_TRACKING\_CONSENT权限，则返回00000000-0000-0000-0000-000000000000。

### 开发步骤

1. 在模块的module.json5文件中，申请跨应用关联权限[ohos.permission.APP\_TRACKING\_CONSENT](permissions-for-all-user.md#ohospermissionapp_tracking_consent)，该权限为user\_grant权限，当申请的权限为user\_grant权限时，reason，abilities标签必填，配置方式参见[requestPermissions标签说明](declare-permissions.md#在配置文件中声明权限)，示例代码如下所示：

   ```
   1. {
   2. "module": {
   3. "requestPermissions": [
   4. {
   5. "name": "ohos.permission.APP_TRACKING_CONSENT",
   6. "reason": "$string:reason",
   7. "usedScene": {
   8. "abilities": [
   9. "EntryFormAbility"
   10. ],
   11. "when": "inuse"
   12. }
   13. }
   14. ]
   15. }
   16. }
   ```
2. 应用在需要获取OAID信息时，应通过调用requestPermissionsFromUser接口获取对应权限。

   说明

   其中context的获取方式参见[各类Context的获取方式](application-context-stage.md#context的获取方式)。示例代码如下所示：

   ```
   1. import { abilityAccessCtrl, PermissionRequestResult } from '@kit.AbilityKit';
   2. import { identifier } from '@kit.AdsKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';

   5. async function requestOAID(context: Context): Promise<string | undefined> {
   6. // 向用户请求授权广告跨应用关联访问权限
   7. let isPermissionGranted: boolean = false;
   8. try {
   9. const atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
   10. const result: PermissionRequestResult =
   11. await atManager.requestPermissionsFromUser(context, ['ohos.permission.APP_TRACKING_CONSENT']);
   12. isPermissionGranted = result.authResults[0] === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED;
   13. } catch (err) {
   14. hilog.error(0x0000, 'testTag', `Failed to request permission. Code is ${err.code}, message is ${err.message}`);
   15. }
   16. if (isPermissionGranted) {
   17. hilog.info(0x0000, 'testTag', 'Succeeded in requesting permission');
   18. try {
   19. const oaid = await identifier.getOAID();
   20. hilog.info(0x0000, 'testTag', 'Succeeded in getting OAID');
   21. return oaid;
   22. } catch (err) {
   23. hilog.error(0x0000, 'testTag', `Failed to get OAID. Code is ${err.code}, message is ${err.message}`);
   24. }
   25. } else {
   26. hilog.error(0x0000, 'testTag', 'Failed to request permission. User rejected');
   27. }
   28. return undefined;
   29. }
   ```
