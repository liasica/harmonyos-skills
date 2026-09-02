---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/open-permission-on-setting
title: 手动设置授权
breadcrumb: 指南 > 系统 > 安全 > 程序访问控制 > 应用权限管控 > 申请应用权限 > 手动设置授权
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:58+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:b08f4744e3227aef80f4ffb199887e93b5ed23fd0df933ae155ed6d63efbcfe6
---

当应用需要访问用户的隐私信息或使用敏感系统能力时，如拦截键盘输入事件，应向用户申请授权。这些权限属于[manual\_settings](app-permission-mgmt-overview.md#manual_settings手动设置授权)权限。

当应用申请manual\_settings权限时，需完成以下步骤：

1. 在AppGallery Connect（AGC）申请Profile文件并在Profile内添加ACL权限。申请Profile的操作需在AGC完成，详细步骤请参阅[申请发布Profile](../app/agc-help-release-profile-0000002248341090.md)。
2. 在module.json5配置文件中[声明权限](declare-permissions.md)。
3. 运行应用时，用户触发访问目标对象时应检查用户的授权结果，若未授权，引导用户跳转到系统应用“设置”中进行授权。
4. 检查用户的授权结果，确认用户已授权后，再进行下一步操作。

本章节将详细介绍如何完成步骤3和4。

## 开发步骤

以申请拦截键盘输入事件权限为例进行说明，目前该权限仅在PC/2in1设备上生效。

1. 申请ohos.permission.HOOK\_KEY\_EVENT权限，配置方式请参见[申请发布Profile](../app/agc-help-release-profile-0000002248341090.md)与[声明权限](declare-permissions.md)。
2. 校验当前是否已经授权。

   在进行权限申请之前，需要先检查当前应用程序是否已经被授予权限。可以通过调用[checkAccessToken()](../harmonyos-references/js-apis-abilityaccessctrl.md#checkaccesstoken9)方法来校验当前是否已经授权。如果已经授权，则可以直接访问目标操作，否则需要进行下一步操作，即引导用户跳转到系统应用“设置”中进行授权。

   ```typescript
   import { abilityAccessCtrl, bundleManager, Permissions } from '@kit.AbilityKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   async function checkPermissionGrant(permission: Permissions): Promise<abilityAccessCtrl.GrantStatus> {
     let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
     let grantStatus: abilityAccessCtrl.GrantStatus = abilityAccessCtrl.GrantStatus.PERMISSION_DENIED;

     // 获取应用程序的accessTokenID
     let tokenId: number = 0;
     try {
       let bundleInfo: bundleManager.BundleInfo =
         await bundleManager.getBundleInfoForSelf(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION);
       let appInfo: bundleManager.ApplicationInfo = bundleInfo.appInfo;
       tokenId = appInfo.accessTokenId;
     } catch (error) {
       const err: BusinessError = error as BusinessError;
       console.error(`Failed to get bundle info for self, code: ${err.code}, message: ${err.message}`);
     }

     // 校验应用是否被授予权限
     try {
       grantStatus = await atManager.checkAccessToken(tokenId, permission);
     } catch (error) {
       const err: BusinessError = error as BusinessError;
       console.error(`Failed to check access token, code: ${err.code}, message: ${err.message}`);
     }

     return grantStatus;
   }

   async function checkPermissions(): Promise<void> {
     let grantStatus: boolean = await checkPermissionGrant('ohos.permission.HOOK_KEY_EVENT') === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED;// 获取拦截键盘输入事件权限状态。
     if (grantStatus) {
       // 已经授权，可以继续访问目标操作
       console.info(`permission is granted.`);
     } else {
       // 未授权，引导用户跳转到系统应用“设置”中进行授权
       console.info(`permission is not granted.`);
     }
   }
   ```
3. 引导用户跳转到系统应用“设置”中进行授权。

   若用户未授权，则需要提示用户必须授权才能访问当前页面的功能，并引导用户到系统应用“设置”中打开相应的权限；或通过调用[openPermissionOnSetting()](../harmonyos-references/js-apis-abilityaccessctrl.md#openpermissiononsetting22)方法拉起弹窗，引导用户授权。

   在“设置”中的路径如下：

   路径一：设置 > 隐私和安全 > 权限类型（如键盘输入辅助） > 某个应用

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/etW0JLgTRjuM9teMCHaBxA/zh-cn_image_0000002736313359.png)

   路径二：设置 > 应用和元服务 > 某个应用 > 权限类型（如键盘输入辅助）

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/dwvJcjemRcmP_3TmvAJ3hQ/zh-cn_image_0000002706674316.png)

   应用在UIAbility的onWindowStageCreate()回调中调用[openPermissionOnSetting()](../harmonyos-references/js-apis-abilityaccessctrl.md#openpermissiononsetting22)方法引导用户跳转到“设置”，或根据业务需要在UI中引导用户跳转到“设置”。

   应用在onWindowStageCreate()回调中申请授权时，需要等待异步接口loadContent()/setUIContent()执行结束后或在loadContent()/setUIContent()回调中调用[openPermissionOnSetting()](../harmonyos-references/js-apis-abilityaccessctrl.md#openpermissiononsetting22)，否则在Content加载完成前，openPermissionOnSetting会调用失败。

   效果展示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/wzudJ4jHR06ygw1n2m22ig/zh-cn_image_0000002736433407.png)

   * 在UIAbility中引导用户跳转到系统应用“设置”中的对应路径。

     ```typescript
     import { abilityAccessCtrl, common, Permissions, UIAbility } from '@kit.AbilityKit';
     import { window } from '@kit.ArkUI';
     import { BusinessError } from '@kit.BasicServicesKit';

     function openPermOnSetting(permission: Permissions, context: common.UIAbilityContext): void {
       let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
       // openPermissionOnSetting会判断权限的授权状态来决定是否唤起弹窗
       atManager.openPermissionOnSetting(context, permission).then((data) => {
         if (data === abilityAccessCtrl.SelectedResult.REJECTED) {
           // 用户不允许跳转到“设置”
           console.info(`user not allowed.`);
         } else if (data === abilityAccessCtrl.SelectedResult.OPENED) {
           // 用户选择跳转到“设置”
           console.info(`user allowed to setting.`);
         } else {
           // 权限已授权，无需弹窗
           console.info(`permission is granted.`);
         }
       }).catch((err: BusinessError) => {
         console.error(`Failed to openPermissionOnSetting, code: ${err.code}, message: ${err.message}`);
       })
     }

     export default class OpenPermAbility extends UIAbility {
       onWindowStageCreate(windowStage: window.WindowStage): void {
         // ···
         windowStage.loadContent('openpermpages/Index', (err) => {
           openPermOnSetting('ohos.permission.HOOK_KEY_EVENT', this.context);
         // ···
         });
       }
     // ···
     }
     ```
   * 在UI中引导用户跳转到系统应用“设置”中的对应路径。

     ```typescript
     import { abilityAccessCtrl, common, Permissions } from '@kit.AbilityKit';
     import { BusinessError } from '@kit.BasicServicesKit';

     function openPermOnSetting(permission: Permissions, context: common.UIAbilityContext): void {
       let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
       // openPermissionOnSetting会判断权限的授权状态来决定是否唤起弹窗
       atManager.openPermissionOnSetting(context, permission).then((data) => {
         if (data === abilityAccessCtrl.SelectedResult.REJECTED) {
           // 用户不允许跳转到“设置”
           console.info(`user not allowed.`);
         } else if (data === abilityAccessCtrl.SelectedResult.OPENED) {
           // 用户选择跳转到“设置”
           console.info(`user allowed to setting.`);
         } else {
           // 权限已授权，无需弹窗
           console.info(`permission is granted.`);
         }
       }).catch((err: BusinessError) => {
         console.error(`Failed to openPermissionOnSetting, code: ${err.code}, message: ${err.message}`);
       })
     }

     @Entry
     @Component
     struct Index {
       aboutToAppear() {
         const context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
         openPermOnSetting('ohos.permission.HOOK_KEY_EVENT', context);
       }

       build() {
         // ···
       }
     }
     ```
4. 处理授权结果。

   调用[openPermissionOnSetting()](../harmonyos-references/js-apis-abilityaccessctrl.md#openpermissiononsetting22)方法后，应用程序需重新校验是否已经授权。

   如果用户授权，则可以继续访问目标操作。

   如果用户拒绝授权，则需要提示用户必须授权才能访问当前页面的功能，重新引导用户跳转到系统应用“设置”中的对应路径打开权限。
