---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/open-permission-on-setting
title: 手动设置授权
breadcrumb: 指南 > 系统 > 安全 > 程序访问控制 > 应用权限管控 > 申请应用权限 > 手动设置授权
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0eecd0be33d8a65e7840df91dc220a248c3d0359e8977b240902b30685eef8b9
---

当应用需要访问用户的隐私信息或使用敏感系统能力时，如拦截键盘输入事件，应向用户申请授权。这些权限属于[manual\_settings](app-permission-mgmt-overview.md#manual_settings手动设置授权)权限。

当应用申请manual\_settings权限时，需完成以下步骤：

1. 在应用市场（AGC）侧申请Profile文件并在Profile内添加ACL权限。申请Profile的操作需在应用市场（AGC）完成，详细步骤请参阅[申请发布Profile](../app/agc-help-release-profile-0000002248341090.md)。
2. 在module.json5配置文件中[声明权限](declare-permissions.md)。
3. 运行应用时，用户触发访问目标对象时应检查用户的授权结果，若未授权，引导用户跳转到系统应用“设置”中进行授权。
4. 检查用户的授权结果，确认用户已授权后，再进行下一步操作。

本章节将详细介绍如何完成步骤3和4。

## 开发步骤

以申请拦截键盘输入事件权限为例进行说明，目前该权限仅在PC/2in1设备上生效。

1. 申请ohos.permission.HOOK\_KEY\_EVENT权限，配置方式请参见[申请发布Profile](../app/agc-help-release-profile-0000002248341090.md)与[声明权限](declare-permissions.md)。
2. 校验当前是否已经授权。

   在进行权限申请之前，需要先检查当前应用程序是否已经被授予权限。可以通过调用[checkAccessToken()](../harmonyos-references/js-apis-abilityaccessctrl.md#checkaccesstoken9)方法来校验当前是否已经授权。如果已经授权，则可以直接访问目标操作，否则需要进行下一步操作，即引导用户跳转到系统应用“设置”中进行授权。

   ```
   1. import { abilityAccessCtrl, bundleManager, Permissions } from '@kit.AbilityKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';

   4. async function checkPermissionGrant(permission: Permissions): Promise<abilityAccessCtrl.GrantStatus> {
   5. let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
   6. let grantStatus: abilityAccessCtrl.GrantStatus = abilityAccessCtrl.GrantStatus.PERMISSION_DENIED;

   8. // 获取应用程序的accessTokenID
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

   20. // 校验应用是否被授予权限
   21. try {
   22. grantStatus = await atManager.checkAccessToken(tokenId, permission);
   23. } catch (error) {
   24. const err: BusinessError = error as BusinessError;
   25. console.error(`Failed to check access token, code: ${err.code}, message: ${err.message}`);
   26. }

   28. return grantStatus;
   29. }

   31. async function checkPermissions(): Promise<void> {
   32. let grantStatus: boolean = await checkPermissionGrant('ohos.permission.HOOK_KEY_EVENT') === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED;// 获取拦截键盘输入事件权限状态。
   33. if (grantStatus) {
   34. // 已经授权，可以继续访问目标操作
   35. console.info(`permission is granted.`);
   36. } else {
   37. // 未授权，引导用户跳转到系统应用“设置”中进行授权
   38. console.info(`permission is not granted.`);
   39. }
   40. }
   ```
3. 引导用户跳转到系统应用“设置”中进行授权。

   若用户未授权，则需要提示用户必须授权才能访问当前页面的功能，并引导用户到系统应用“设置”中打开相应的权限；或通过调用[openPermissionOnSetting()](../harmonyos-references/js-apis-abilityaccessctrl.md#openpermissiononsetting22)方法拉起弹窗，引导用户授权。

   在“设置”中的路径如下：

   路径一：设置 > 隐私和安全 > 权限类型（如键盘输入辅助） > 某个应用

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/cyMcQAE6QEKDl9HIURM9Pg/zh-cn_image_0000002583478357.png?HW-CC-KV=V1&HW-CC-Date=20260427T234201Z&HW-CC-Expire=86400&HW-CC-Sign=3502365ECA9CAE8C454E648911B0CFC6D9746686EB746E7BFEFA9D9C2AE4AD78)

   路径二：设置 > 应用和元服务 > 某个应用 > 权限类型（如键盘输入辅助）

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/2s2rb_95SYWNgEpwNQE-aw/zh-cn_image_0000002552798708.png?HW-CC-KV=V1&HW-CC-Date=20260427T234201Z&HW-CC-Expire=86400&HW-CC-Sign=A26077A6CE670EE0B1E08542AD4C1996553B9117D3494ACC328E81C093B8B053)

   应用在UIAbility的onWindowStageCreate()回调中调用[openPermissionOnSetting()](../harmonyos-references/js-apis-abilityaccessctrl.md#openpermissiononsetting22)方法引导用户跳转到“设置”，或根据业务需要在UI中引导用户跳转到“设置”。

   应用在onWindowStageCreate()回调中申请授权时，需要等待异步接口loadContent()/setUIContent()执行结束后或在loadContent()/setUIContent()回调中调用[openPermissionOnSetting()](../harmonyos-references/js-apis-abilityaccessctrl.md#openpermissiononsetting22)，否则在Content加载完成前，openPermissionOnSetting会调用失败。

   效果展示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/TiLn89JFSTqQjDXoIe7SwQ/zh-cn_image_0000002583438403.png?HW-CC-KV=V1&HW-CC-Date=20260427T234201Z&HW-CC-Expire=86400&HW-CC-Sign=AC640BC41B1BEA56111FE4B614AFE03CDDD0D0440AA2BADE043B9E414F2FC6FE)

   * 在UIAbility中引导用户跳转到系统应用“设置”中的对应路径。

     ```
     1. import { abilityAccessCtrl, common, Permissions, UIAbility } from '@kit.AbilityKit';
     2. import { window } from '@kit.ArkUI';
     3. import { BusinessError } from '@kit.BasicServicesKit';

     5. function openPermOnSetting(permission: Permissions, context: common.UIAbilityContext): void {
     6. let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
     7. // openPermissionOnSetting会判断权限的授权状态来决定是否唤起弹窗
     8. atManager.openPermissionOnSetting(context, permission).then((data) => {
     9. if (data === abilityAccessCtrl.SelectedResult.REJECTED) {
     10. // 用户不允许跳转到“设置”
     11. console.info(`user not allowed.`);
     12. } else if (data === abilityAccessCtrl.SelectedResult.OPENED) {
     13. // 用户选择跳转到“设置”
     14. console.info(`user allowed to setting.`);
     15. } else {
     16. // 权限已授权，无需弹窗
     17. console.info(`permission is granted.`);
     18. }
     19. }).catch((err: BusinessError) => {
     20. console.error(`Failed to openPermissionOnSetting, code: ${err.code}, message: ${err.message}`);
     21. })
     22. }

     24. export default class OpenPermAbility extends UIAbility {
     25. onWindowStageCreate(windowStage: window.WindowStage): void {
     26. // ···
     27. windowStage.loadContent('openpermpages/Index', (err) => {
     28. openPermOnSetting('ohos.permission.HOOK_KEY_EVENT', this.context);
     29. // ···
     30. });
     31. }
     32. // ···
     33. }
     ```
   * 在UI中引导用户跳转到系统应用“设置”中的对应路径。

     ```
     1. import { abilityAccessCtrl, common, Permissions } from '@kit.AbilityKit';
     2. import { BusinessError } from '@kit.BasicServicesKit';

     4. function openPermOnSetting(permission: Permissions, context: common.UIAbilityContext): void {
     5. let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
     6. // openPermissionOnSetting会判断权限的授权状态来决定是否唤起弹窗
     7. atManager.openPermissionOnSetting(context, permission).then((data) => {
     8. if (data === abilityAccessCtrl.SelectedResult.REJECTED) {
     9. // 用户不允许跳转到“设置”
     10. console.info(`user not allowed.`);
     11. } else if (data === abilityAccessCtrl.SelectedResult.OPENED) {
     12. // 用户选择跳转到“设置”
     13. console.info(`user allowed to setting.`);
     14. } else {
     15. // 权限已授权，无需弹窗
     16. console.info(`permission is granted.`);
     17. }
     18. }).catch((err: BusinessError) => {
     19. console.error(`Failed to openPermissionOnSetting, code: ${err.code}, message: ${err.message}`);
     20. })
     21. }

     23. @Entry
     24. @Component
     25. struct Index {
     26. aboutToAppear() {
     27. const context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
     28. openPermOnSetting('ohos.permission.HOOK_KEY_EVENT', context);
     29. }

     31. build() {
     32. // ···
     33. }
     34. }
     ```
4. 处理授权结果。

   调用[openPermissionOnSetting()](../harmonyos-references/js-apis-abilityaccessctrl.md#openpermissiononsetting22)方法后，应用程序需重新校验是否已经授权。

   如果用户授权，则可以继续访问目标操作。

   如果用户拒绝授权，则需要提示用户必须授权才能访问当前页面的功能，重新引导用户跳转到系统应用“设置”中的对应路径打开权限。
