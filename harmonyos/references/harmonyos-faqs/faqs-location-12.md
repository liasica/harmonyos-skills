---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-location-12
title: 动态申请后台位置权限失败该如何处理
breadcrumb: FAQ > 应用服务开发 > 位置服务（Location Kit） > 动态申请后台位置权限失败该如何处理
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:02c1b932fdd399fd9153ff9a54e017acea4e725affd7d84ba7c091aa41b47ae8
---

## 问题现象

按如下截图方式申请后台位置权限时，未弹出授权窗口，导致无法获取位置信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/JEfcCoyJQ9qgqF3BOfV3oA/zh-cn_image_0000002658913749.png "点击放大")

## 背景知识

系统提供的定位权限有：

* ohos.permission.LOCATION：用于获取[精准位置](../harmonyos-guides/permissions-for-all-user.md#ohospermissionlocation)，精准度在米级别。
* ohos.permission.APPROXIMATELY\_LOCATION：用于获取[模糊位置](../harmonyos-guides/permissions-for-all-user.md#ohospermissionapproximately_location)，精确度为5公里。
* ohos.permission.LOCATION\_IN\_BACKGROUND：用于[后台获取位置](../harmonyos-guides/permissions-for-all-user.md#ohospermissionlocation_in_background)，应用切换到后台仍然需要获取定位信息的场景。

由于安全隐私要求，应用不能通过弹窗的形式被授予后台位置权限，应用如果需要使用后台位置权限，需要引导用户到设置界面手动授予。

## 解决方案

1. 当APP运行在前台，且需要访问设备位置信息时，需要向用户获取位置授权。

   ```screen
   import abilityAccessCtrl, { Permissions } from '@ohos.abilityAccessCtrl';
   import common from '@ohos.app.ability.common';
   import { BusinessError } from '@ohos.base';

   @Entry
   @Component
   struct locationTest {
     private permissions: Array<Permissions> = [
       'ohos.permission.APPROXIMATELY_LOCATION',
       'ohos.permission.LOCATION'
     ];

     reqPermissionsFromUser(permissions: Array<Permissions>, context: common.UIAbilityContext): void {
       const atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
       // requestPermissionsFromUser会判断权限的授权状态来决定是否唤起弹窗
       atManager.requestPermissionsFromUser(context, permissions).then((data) => {
         let grantStatus: Array<number> = data.authResults;
         let length: number = grantStatus.length;
         for (let i = 0; i < length; i++) {
           if (grantStatus[i] === 0) {
             // 用户授权，可以继续访问目标操作
           } else {
             // 用户拒绝授权，提示用户必须授权才能访问当前页面的功能，并引导用户到系统设置中打开相应的权限
             return;
           }
         }
         // 授权成功
       }).catch((err: BusinessError) => {
         console.error(`Failed to request permissions from user. Code is ${err.code}, message is ${err.message}`);
       });
     }

     aboutToAppear() {
       const context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
       this.reqPermissionsFromUser(this.permissions, context);
     }

     build() {
       Text('申请位置权限')
     }
   }
   ```

   效果预览：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/_3Jdv7rYSDezGmsd3f1M8Q/zh-cn_image_0000002658793803.png "点击放大")
2. 当用户点击弹窗授予前台位置权限后，如果APP运行到后台时也需要获取用户的位置信息，应用可以通过弹窗、提示窗等形式告知用户前往设置界面授予后台位置权限，在设置界面中将位置信息访问权限设置为**始终允许**，点击**确认按钮**，调用openPermissionsInSystemSettings()方法跳转到应用设置界面。

   效果预览：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/hN4FOlq1T16Xrdq64E81MA/zh-cn_image_0000002628394532.png "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/AseLquZcQc-QgZ1gvabPSA/zh-cn_image_0000002628554426.png "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/ebpdULWtR9-ywM0nRJ4IMg/zh-cn_image_0000002658913751.png "点击放大")

   ```screen
   import { AlertDialog } from '@kit.ArkUI';
   import common from '@ohos.app.ability.common';
   import { Want } from '@kit.AbilityKit';

   @Entry
   @Component
   struct locationTest2 {
     private dialogControllerConfirm: CustomDialogController = new CustomDialogController({
       builder: AlertDialog({
         primaryTitle: '温馨提示',
         content: '为了保证正常导航，需要将位置信息访问权限设置为【始终允许】',
         primaryButton: {
           value: '取消',
           action: () => {
             // 取消逻辑
           },
         },
         secondaryButton: {
           value: '确认',
           role: ButtonRole.ERROR,
           action: () => {
             this.openPermissionsInSystemSettings();
           }
         },
       }),
     });

     openPermissionsInSystemSettings(): void {
       let wantInfo: Want = {
         bundleName: 'com.huawei.hmos.settings',
         abilityName: 'com.huawei.hmos.settings.MainAbility',
         uri: 'application_info_entry',
         parameters: {
           settingsParamBundleName: 'com.huawei.locationTest' // 打开指定应用的详情页面
         }
       };
       const context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
       context.startAbility(wantInfo).then(() => {
         // 打开成功
       }).catch(() => {
         // 异常处理
       });
     }

     build() {
       Button('跳转位置设置页面')
         .onClick(() => {
           this.dialogControllerConfirm.open();
         })
     }
   }
   ```

   注：在entry模块的module.json5，需要将后台位置权限配置进去，位置信息访问权限设置界面才会看到**始终允许**的选项。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/fIIQ9NP-SG63l5gGOZxnPQ/zh-cn_image_0000002658793805.png "点击放大")

## 总结

申请后台位置权限，除了要配置ohos.permission.LOCATION\_IN\_BACKGROUND权限到entry模块的module.json5文件中，还需要引导用户去应用设置界面设置位置权限为**始终允许**才能生效。
