---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-143
title: 申请用户授权拒绝后二次申请授权方案
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 申请用户授权拒绝后二次申请授权方案
category: harmonyos-faqs
scraped_at: 2026-09-30T07:42:04+08:00
doc_updated_at: 2026-09-29
content_hash: sha256:68a910d9e8f74b912685bbce0825c81140077f7bd395436acaaa487b9a093993
---

## 问题现象

通过requestPermissionsFromUser申请权限，这时用户拒绝授权；此时无法再拉起授权弹窗，如果跳设置详情页，会离开应用，体验不佳。

## 背景知识

* [abilityAccessCtrl.createAtManager](../harmonyos-references/js-apis-abilityaccessctrl.md#abilityaccessctrlcreateatmanager)：获取访问控制模块对象，访问控制管理。
* [atManager.requestPermissionsFromUser](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)：用于UIAbility/UIExtensionAbility拉起弹框请求用户授权。

## 解决方案

requestPermissionsFromUser后通过requestPermissionOnSetting拉起系统设置页半模态二次授权。

实践方案(以ohos.permission.CAMERA二次授权为例)

1. 在module.json5中配置权限参数requestPermissions：

   ```json
   {
           "name": "ohos.permission.CAMERA",
           "reason": "$string:permission_reason_camera",
           "usedScene": {
             "abilities": [
               "EntryAbility"
             ],
             "when": "always"
           }
         }
   ```
2. 可用[atManager.requestPermissionsFromUser](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)拉起弹框请求用户授权，返回类型[PermissionRequestResult](../harmonyos-references/js-apis-permissionrequestresult.md)，如果dialogShownResults为true，则代表首次弹窗请求授权。以申请ohos.permission.CAMERA为例：

   ```ts
   import { abilityAccessCtrl, Permissions } from '@kit.AbilityKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   @Entry
   @Component
   struct CheckPermission {

     build() {
       RelativeContainer() {
         Text('申请相机权限')
           .fontSize($r('app.float.page_text_font_size'))
           .fontWeight(FontWeight.Bold)
           .alignRules({
             center: { anchor: '__container__', align: VerticalAlign.Center },
             middle: { anchor: '__container__', align: HorizontalAlign.Center }
           })
           .onClick(() => {
             checkPermission(this.getUIContext().getHostContext()!);
           })
       }
       .height('100%')
       .width('100%')
     }
   }

   export function checkPermission(context: Context) {
     const PERMISSION_ARRAY: Permissions[] = ['ohos.permission.CAMERA'];
     const atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
     atManager.requestPermissionsFromUser(context, PERMISSION_ARRAY).then((data) => {
       if (data.authResults[0] === 0) {
         // 已授权
         console.info('request permission success.');
         return;
       }
       if (data.dialogShownResults && data.dialogShownResults.length > 0 && data.dialogShownResults[0]) {
         // 首次权限申请
         console.info('request permission first.');
       } else {
         // 如果是未授权状态，可通过requestPermissionOnSetting拉起系统设置半模态二次授权。
         atManager.requestPermissionOnSetting(context, PERMISSION_ARRAY)
           .then((data: Array<abilityAccessCtrl.GrantStatus>) => {
             console.info(`data: ${JSON.stringify(data)}`);
           })
           .catch((err: BusinessError) => {
             console.error(`code: ${err.code}, message: ${err.message}`);
           });
       }
     })
     .catch((err: BusinessError) => {
       console.error(`code: ${err.code}, message: ${err.message}`);
     });
   }
   ```

## 常见FAQ

Q：在某些情况下，需要引导用户跳转到指定应用的权限授权页面进行手动授权，但是官网指南中没有说明每种权限的URI，官网指南是否可以添加权限设置页面的URI列表？

A：由于系统设置应用中的URI涉及到内部实现，同时为了保证用户体验，设置提供了单独的接口，拉起申请权限申请弹窗，详见：[支持跳转系统应用的能力清单](../harmonyos-guides/system-app-startup.md#设置)。

Q：通知权限被拒绝后，如何再次拉起授权弹窗？

A：使用接口：[openNotificationSettings](../harmonyos-references/js-apis-notificationmanager.md#notificationmanageropennotificationsettings13)拉起应用的通知设置界面，该页面以半模态形式呈现，可用于设置通知开关、通知提醒方式等。使用Promise异步回调。示例代码如下：

```ts
function reqNotification(context: common.UIAbilityContext) {
  notificationManager.isNotificationEnabled().then((data: boolean) => {
    console.info(`isNotificationEnabled success, data: ${JSON.stringify(data)}`);
    if (!data) {
      notificationManager.requestEnableNotification(context).then(() => {
        console.info(`[ANS] requestEnableNotification success`);
      }).catch((err: BusinessError) => {
        if (1600004 == err.code) {
          console.error(`[ANS] requestEnableNotification refused, code is ${err.code}, message is ${err.message}`);
          notificationManager.openNotificationSettings(context); // 使用openNotificationSettings拉起应用通知设置的半模态页面。
        } else {
          console.error(`[ANS] requestEnableNotification failed, code is ${err.code}, message is ${err.message}`);
        }
      });
    }
  }).catch((err: BusinessError) => {
    console.error(`isNotificationEnabled fail, code is ${err.code}, message is ${err.message}`);
  });
};
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/8UFxr72ITkShq5bC4vA9WQ/zh-cn_image_0000002776400561.png "点击放大")

Q：因为首次申请和二次申请权限调用方法不同，那么如何区分是否首次申请权限？

A：有以下两种方式：

* 方案一：使用用户首选项持久化用户拒绝行为。
* 方案二：requestPermissionsFromUser的回调结果[PermissionRequestResult](../harmonyos-references/js-apis-permissionrequestresult.md)的属性dialogShownResults为true，表示用户首次申请；为false，表示权限已设置，无需弹窗，需要用户在"设置"中修改。

Q：如何区分用户拒绝授权的三种状态（首次拒绝、二次拒绝、永久拒绝）？

A：区分三种拒绝状态需结合[atManager.requestPermissionsFromUser](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)返回的[PermissionRequestResult](../harmonyos-references/js-apis-permissionrequestresult.md)中的authResults和dialogShownResults字段综合判断：

* authResults[0] === 0：已授权。
* authResults[0] === -1且dialogShownResults[0] === true：首次拒绝，系统弹出了授权弹窗且用户拒绝，后续可再次弹窗申请。
* authResults[0] === -1且dialogShownResults[0] === false：二次拒绝或永久拒绝，系统未弹出弹窗（用户此前已拒绝），需引导用户前往设置页授权。

[atManager.checkAccessToken](../harmonyos-references/js-apis-abilityaccessctrl.md#checkaccesstoken9)仅能查询当前权限是否已授予，无法单独区分拒绝类型，需配合弹窗结果综合判断。
