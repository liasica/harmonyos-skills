---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/request-user-authorization
title: 向用户申请授权
breadcrumb: 指南 > 系统 > 安全 > 程序访问控制 > 应用权限管控 > 申请应用权限 > 向用户申请授权
category: harmonyos-guides
scraped_at: 2026-04-29T13:30:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:435ca86ad11f69fdb57672da4ac6982c3956533bfaa0b888cc4f4d992c4c1517
---

当应用需要访问用户的隐私信息或使用系统能力时，如获取位置信息、访问日历、使用相机拍摄照片或录制视频等，应向用户申请授权。这些权限属于user\_grant权限。

当应用申请user\_grant权限时，需完成以下步骤：

1. 在配置文件中，声明应用需要请求的权限。
2. 将应用中需要申请权限的目标对象与对应权限关联，确保用户明确哪些操作需授予应用指定权限。

   以上两步请参考章节[声明权限](declare-permissions.md)完成。
3. 运行应用时，用户触发访问目标对象时应调用接口，精准触发动态授权弹框。接口内部会检查当前用户是否已授权所需权限，若未授权，将拉起动态授权弹框请求用户授权。
4. 检查用户的授权结果，确认用户已授权后，再进行下一步操作。

本章节将详细介绍如何完成步骤3和4。

## 约束与限制

* user\_grant权限授权要基于用户可知可控的原则，需要应用在运行时主动调用系统动态申请权限的接口，系统弹框由用户授权，用户结合应用运行场景的上下文，识别出应用申请相应敏感权限的合理性，从而做出正确的选择。
* 系统不鼓励频繁弹窗打扰用户。如果用户拒绝授权，将无法再次弹窗，应用需引导用户在系统设置中手动授予权限。或是调用[requestPermissionOnSetting](request-user-authorization-second.md)，拉起权限设置弹窗，引导用户授权。
* 系统权限弹窗不可被遮挡。

  系统权限弹窗不可被其他组件或控件遮挡，弹窗信息需完整展示，便于用户识别并完成授权。

  如果系统权限弹窗与其他组件/控件同时在相同位置展示，系统权限弹窗将默认覆盖其他组件/控件。
* 每次执行需要目标权限的操作时，应用都必须检查自己是否已经具有该权限。

  如需检查用户是否已向您的应用授予特定权限，可以使用[checkAccessToken()](../harmonyos-references/js-apis-abilityaccessctrl.md#checkaccesstoken9)函数。此方法会返回[PERMISSION\_GRANTED](../harmonyos-references/js-apis-abilityaccessctrl.md#grantstatus)或[PERMISSION\_DENIED](../harmonyos-references/js-apis-abilityaccessctrl.md#grantstatus)。具体示例可参考下文。
* 每次访问受目标权限保护的接口之前，都需要使用[requestPermissionsFromUser()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)接口请求相应的权限。

  用户可能在动态授予权限后通过系统设置来取消应用的权限，因此不能将之前授予的授权状态持久化。
* 应用在onWindowStageCreate()回调中申请授权时，需要等待异步接口loadContent()/setUIContent()执行结束后或在loadContent()/setUIContent()回调中调用[requestPermissionsFromUser()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)。

  应用在UIExtensionAbility申请授权时，需要在onWindowStageCreate函数执行结束后或在onWindowStageCreate函数回调中调用[requestPermissionsFromUser()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)。

## 开发步骤

以申请使用位置权限为例进行说明。

效果展示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/0Grn-2ifQEawSR7LD198tg/zh-cn_image_0000002589244659.png?HW-CC-KV=V1&HW-CC-Date=20260429T053033Z&HW-CC-Expire=86400&HW-CC-Sign=72B689DF4FF012AE5E628FB830728886F3B56618BFEB5D360339E8442A118CA6)

1. 申请ohos.permission.LOCATION、ohos.permission.APPROXIMATELY\_LOCATION权限，配置方式请参见[声明权限](declare-permissions.md)。
2. 校验当前是否已经授权。

   在进行权限申请之前，需要先检查当前应用程序是否已经被授予权限。可以通过调用[checkAccessToken()](../harmonyos-references/js-apis-abilityaccessctrl.md#checkaccesstoken9)方法来校验当前是否已经授权。如果已经授权，则可以直接访问目标操作，否则需要进行下一步操作，即向用户申请授权。

   ```
   1. import { abilityAccessCtrl, bundleManager, Permissions } from '@kit.AbilityKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';

   4. async function checkPermissionGrant(permission: Permissions): Promise<abilityAccessCtrl.GrantStatus> {
   5. let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
   6. let grantStatus: abilityAccessCtrl.GrantStatus = abilityAccessCtrl.GrantStatus.PERMISSION_DENIED;

   8. // 获取应用程序的accessTokenID。
   9. let tokenId: number = 0;
   10. try {
   11. let bundleInfo: bundleManager.BundleInfo =
   12. await bundleManager.getBundleInfoForSelf(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION);
   13. let appInfo: bundleManager.ApplicationInfo = bundleInfo.appInfo;
   14. tokenId = appInfo.accessTokenId;
   15. } catch (error) {
   16. const err: BusinessError = error as BusinessError;
   17. console.error(`Failed to get bundle info for self, code: ${err.code}, message: ${err.message}`);
   18. }

   20. // 校验应用是否被授予权限。
   21. try {
   22. grantStatus = await atManager.checkAccessToken(tokenId, permission);
   23. } catch (error) {
   24. const err: BusinessError = error as BusinessError;
   25. console.error(`Failed to check access token, code: ${err.code}, message: ${err.message}`);
   26. }

   28. return grantStatus;
   29. }

   31. async function checkPermissions(): Promise<void> {
   32. let grantStatus1: boolean = await checkPermissionGrant('ohos.permission.LOCATION') === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED;// 获取精确定位权限状态。
   33. let grantStatus2: boolean = await checkPermissionGrant('ohos.permission.APPROXIMATELY_LOCATION') === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED;// 获取模糊定位权限状态。
   34. // 精确定位权限只能跟模糊定位权限一起申请，或者已经有模糊定位权限才能申请精确定位权限。
   35. if (grantStatus2 && !grantStatus1) {
   36. // 申请精确定位权限。
   37. // ···
   38. } else if (!grantStatus1 && !grantStatus2) {
   39. // 申请模糊定位权限与精确定位权限或单独申请模糊定位权限。
   40. // ···
   41. } else {
   42. // 已经授权，可以继续访问目标操作。
   43. // ···
   44. }
   45. }
   ```

   [PermissionUtil.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/RequestUserAuthorization/entry/src/main/ets/utils/PermissionUtil.ets#L17-L69)
3. 动态向用户申请授权。

   动态向用户申请权限是指在应用程序运行时向用户请求授权的过程。可以通过调用[requestPermissionsFromUser()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)方法来实现。该方法接收一个权限列表参数，例如位置、日历、相机、麦克风等。用户可以选择授予权限或者拒绝授权。

   可以在UIAbility的onWindowStageCreate()回调中调用[requestPermissionsFromUser()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)方法动态请求授权，或根据业务需要在UI中请求授权。

   应用在onWindowStageCreate()回调中申请授权时，需要等待异步接口loadContent()/setUIContent()执行结束后或在loadContent()/setUIContent()回调中调用[requestPermissionsFromUser()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)，否则在Content加载完成前，requestPermissionsFromUser会调用失败。

   应用在UIExtensionAbility申请授权时，需要在onWindowStageCreate函数执行结束后或在onWindowStageCreate函数回调中调用[requestPermissionsFromUser()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)。

   * 在UIAbility中向用户申请授权。

   ```
   1. import { abilityAccessCtrl, common, Permissions, UIAbility } from '@kit.AbilityKit';
   2. import { window } from '@kit.ArkUI';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. const permissions: Permissions[] = ['ohos.permission.LOCATION', 'ohos.permission.APPROXIMATELY_LOCATION'];

   7. function reqPermissionsFromUser(permissions: Array<Permissions>, context: common.UIAbilityContext): void {
   8. let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
   9. // requestPermissionsFromUser会判断权限的授权状态来决定是否唤起弹窗。
   10. atManager.requestPermissionsFromUser(context, permissions).then((data) => {
   11. let grantStatus: number[] = data.authResults;
   12. let length: number = grantStatus.length;
   13. for (let i = 0; i < length; i++) {
   14. if (grantStatus[i] === 0) {
   15. // 用户授权，可以继续访问目标操作。
   16. console.info(`${permissions[i]} is granted by user.`);
   17. } else {
   18. // 用户拒绝授权，提示用户必须授权才能访问当前页面的功能，并引导用户到系统设置中打开相应的权限。
   19. return;
   20. }
   21. }
   22. // 授权成功。
   23. }).catch((err: BusinessError) => {
   24. console.error(`Failed to request permissions from user, code: ${err.code}, message: ${err.message}`);
   25. })
   26. }

   28. export default class SecondAbility extends UIAbility {
   29. // ...
   30. onWindowStageCreate(windowStage: window.WindowStage): void {
   31. // ...
   32. windowStage.loadContent('secondpages/Index', (err) => {
   33. reqPermissionsFromUser(permissions, this.context);
   34. // ...
   35. });
   36. }
   37. // ...
   38. }
   ```

   [SecondAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/RequestUserAuthorization/entry/src/main/ets/secondability/SecondAbility.ets#L18-L108)

   * 在UI中向用户申请授权。

   ```
   1. import { abilityAccessCtrl, common, Permissions } from '@kit.AbilityKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';

   4. const permissions: Permissions[] = ['ohos.permission.LOCATION', 'ohos.permission.APPROXIMATELY_LOCATION'];

   6. function reqPermissionsFromUser(permissions: Array<Permissions>, context: common.UIAbilityContext): void {
   7. let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
   8. // requestPermissionsFromUser会判断权限的授权状态来决定是否唤起弹窗
   9. atManager.requestPermissionsFromUser(context, permissions).then((data) => {
   10. let grantStatus: number[] = data.authResults;
   11. let length: number = grantStatus.length;
   12. for (let i = 0; i < length; i++) {
   13. if (grantStatus[i] === 0) {
   14. // 用户授权，可以继续访问目标操作
   15. console.info(`${permissions[i]} is granted by user.`);
   16. } else {
   17. // 用户拒绝授权，提示用户必须授权才能访问当前页面的功能，并引导用户到系统设置中打开相应的权限
   18. return;
   19. }
   20. }
   21. // 授权成功
   22. }).catch((err: BusinessError) => {
   23. console.error(`Failed to request permissions from user, code: ${err.code}, message: ${err.message}`);
   24. })
   25. }

   27. @Entry
   28. @Component
   29. struct Index {
   30. aboutToAppear() {
   31. const context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
   32. reqPermissionsFromUser(permissions, context);
   33. }

   35. build() {
   36. // ...
   37. }
   38. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/RequestUserAuthorization/entry/src/main/ets/reqpermissioninui/pages/Index.ets#L17-L67)
4. 处理授权结果。

   调用[requestPermissionsFromUser()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)方法后，应用程序将等待用户授权的结果。

   如果用户授权，则可以继续访问目标操作。

   如果用户拒绝授权，则需要提示用户必须授权才能访问当前页面的功能，并引导用户到系统应用“设置”中打开相应的权限；或是调用[requestPermissionOnSetting()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissiononsetting12)，拉起权限设置弹框，引导用户授权。

   路径：设置 > 隐私与安全 > 权限类型（如位置信息） > 具体应用
