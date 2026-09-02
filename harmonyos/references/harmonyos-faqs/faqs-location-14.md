---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-location-14
title: 应用如何获取定位权限
breadcrumb: FAQ > 应用服务开发 > 位置服务（Location Kit） > 应用如何获取定位权限
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:49+08:00
doc_updated_at: 2026-07-24
content_hash: sha256:a25941602dfc73db2153418cce878cdb1f75235b2b0e8e1939e50aacf837b992
---

## 问题现象

1. 应用处于后台，如何获取定位权限？
2. 判断是否有定位权限，一直是没有授权，然后用LocationButton重新申请的时候，result一直是“1”，没有弹窗提醒授权。

   ```ts
   import { abilityAccessCtrl, bundleManager, Permissions } from '@kit.AbilityKit';

   @Entry
   @Component
   export struct Test {
     build() {
     }

     async checkPermissionGrant(permission: Permissions): Promise<abilityAccessCtrl.GrantStatus> {
       let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
       let grantStatus: abilityAccessCtrl.GrantStatus = abilityAccessCtrl.GrantStatus.PERMISSION_DENIED;

       // 获取应用程序的accessTokenID
       let tokenId: number = 0;
       let bundleInfo: bundleManager.BundleInfo =
         await bundleManager.getBundleInfoForSelf(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION);
       console.info('Succeeded in getting Bundle.');
       let appInfo: bundleManager.ApplicationInfo = bundleInfo.appInfo;
       tokenId = appInfo.accessTokenId;

       // 校验应用是否被授予权限
       grantStatus = await atManager.checkAccessToken(tokenId, permission);
       console.info('Succeeded in checking access token.');
       return grantStatus;
     }

     async checkPermissions1(): Promise<boolean> {
       let grantStatus1: boolean = await this.checkPermissionGrant('ohos.permission.LOCATION') ===
       abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED; // 获取精确定位权限状态
       let grantStatus2: boolean = await this.checkPermissionGrant('ohos.permission.APPROXIMATELY_LOCATION') ===
       abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED; // 获取模糊定位权限状态

       // 根据权限状态采取相应措施
       if (grantStatus1 && grantStatus2) {
         console.info('已获得所有必要的定位权限，可以继续进行操作。');
         return true
       } else if (grantStatus1 || grantStatus2) {
         console.info('已获得部分定位权限，需要申请剩余权限。');
         return false
       } else {
         console.info('未获得任何定位权限，需要向用户申请权限。');
         return false
       }
     }
   }
   ```

## 背景知识

应用在使用定位能力时，首先需要声明所需的定位权限，同时向用户申请权限。向用户申请授权可分为首次和二次。

详细可参考如下：

1. [声明权限](../harmonyos-guides/declare-permissions.md)。
2. [向用户申请授权](../harmonyos-guides/request-user-authorization.md)。
3. [二次向用户申请授权](../harmonyos-guides/request-user-authorization-second.md)。

## 问题定位

1. module.json5是否配置定位权限，如果有后台任务是否配置后台定位权限。
2. 询问用户授权时，需要使用定位权限组，同时判断多个定位权限。

## 分析结论

1. 始终允许权限需要在ohos.permission.LOCATION和ohos.permission.APPROXIMATELY\_LOCATION的基础上增加后台定位权限ohos.permission.LOCATION\_IN\_BACKGROUND，由于安全隐私要求，应用不能通过弹窗的形式被授予后台位置权限，应用如果需要使用后台位置权限，需要引导用户到设置界面手动授予。
2. 对于定位权限来说，模糊定位和精准定位权限要一起申请授权。LocationButton从API Version 15开始不再维护，推荐使用[requestPermissionsFromUser](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9-1)。

## 修改建议

1. 应用应通过弹窗、提示窗等形式告知用户前往设置界面授予后台位置权限。

   用户在设置界面中的选择“始终允许”应用访问位置信息权限，完成手动授予。

   设置路径：

   路径一：设置->隐私与安全->位置->具体应用。

   路径二：设置->应用和元服务->具体应用->位置。
2. 同时判断ohos.permission.LOCATION和ohos.permission.APPROXIMATELY\_LOCATION权限。

   代码参考[向用户申请授权](../harmonyos-guides/request-user-authorization.md)开发步骤第3步：动态向用户申请授权。

## 常见FAQ

Q：在系统应用设置页面开、关位置权限后，如何更新应用内的位置权限状态。

A：可以通过[订阅位置服务状态变化](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanageronlocationenabledchange)，发生变化时触发回调函数来更新应用内的位置权限状态。

Q：是否有开启系统位置功能的API？

A：Location Kit目前没有开启系统位置功能的API，需要引导用户手动开启“位置”功能开关。代码参考：[requestGlobalSwitch](../harmonyos-references/js-apis-abilityaccessctrl.md#requestglobalswitch12)。

Q：应用获取定位信息是否需要在AppGallery Connect管理页面的“开放能力”里额外提交申请？

A：不需要。定位权限属于HarmonyOS权限，只需在应用的module.json5配置文件中声明定位权限（如ohos.permission.APPROXIMATELY\_LOCATION、ohos.permission.LOCATION），并在运行时动态向用户请求授权即可，无需在AppGallery Connect管理页面额外开通。
