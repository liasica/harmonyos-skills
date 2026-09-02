---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-update
title: 应用市场更新功能
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 应用市场更新功能
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:52+08:00
doc_updated_at: 2026-08-03
content_hash: sha256:8500d4ffec68fdcb8c41969b0d2fb00e585850489f924df81dba85c94763b2bc
---

应用市场更新功能为已上架应用提供版本检测、显示更新提醒能力。开发者使用应用市场更新功能可以在应用内提醒用户及时更新到最新版本。

## 场景介绍

当应用启动完成或用户在应用中主动检查应用新版本时，开发者可以通过本服务，来查询应用是否有可更新的版本。如果存在可更新版本，您可以通过本服务为用户显示更新提醒。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/cy6SJrr0QI2d8d_nSGwpvA/zh-cn_image_0000002706834794.png)

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/fPT8apwJRcSfmksWYKszmw/zh-cn_image_0000002736313903.png)

1. 应用调用检查更新接口。
2. 升级服务API返回是否有新版本。
3. 调用显示升级对话框接口。
4. 升级服务API向应用返回显示结果。

## 约束与限制

* 应用市场更新功能支持Phone、Tablet、PC/2in1设备。并且从5.1.1(19)版本开始，新增支持TV设备；从6.0.0(20)版本开始，新增支持Wearable设备。
* 应用市场更新功能不支持模拟器，请使用真机调试。在模拟器中使用该服务将会提示：无法获取内容，请点击屏幕重试。
* 应用已在应用市场上架。

## 接口说明

应用市场更新服务提供以下接口，具体API说明详见[接口文档](../harmonyos-references/store-updatemanager.md)。

| 接口名 | 描述 |
| --- | --- |
| [checkAppUpdate](../harmonyos-references/store-updatemanager.md#updatemanagercheckappupdate)(context: [common.UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md)): Promise<[CheckUpdateResult](../harmonyos-references/store-updatemanager.md#checkupdateresult)> | 检查更新接口，用于检测当前是否有新版本。 |
| [showUpdateDialog](../harmonyos-references/store-updatemanager.md#updatemanagershowupdatedialog)(context:[common.UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md)): Promise<[ShowUpdateResultCode](../harmonyos-references/store-updatemanager.md#showupdateresultcode)> | 显示升级对话框接口，用于提示用户进行升级。 |

## 开发步骤

### 检测应用新版本

1. 导入updateManager模块及相关公共模块。

   ```typescript
   import { updateManager } from '@kit.AppGalleryKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import type { common } from '@kit.AbilityKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 构造参数，其中入参为[common.UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md)类型的Context。

   ```typescript
   let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
   ```
3. 调用[checkAppUpdate](../harmonyos-references/store-updatemanager.md#updatemanagercheckappupdate)方法检查应用版本是否有更新。

   ```typescript
   try {
     updateManager.checkAppUpdate(context)
       .then((checkResult: updateManager.CheckUpdateResult) => {
         hilog.info(0, 'TAG', 'Succeeded in checking Result updateAvailable:' + checkResult.updateAvailable);
       }).catch((error: BusinessError) => {
       hilog.error(0, 'TAG', `checkAppUpdate onError.code is ${error.code}, message is ${error.message}`);
     });
   } catch (error) {
     hilog.error(0, 'TAG', `checkAppUpdate onError.code is ${error.code}, message is ${error.message}`);
   }
   ```

**说明** 

* 本地安装版本须低于应用市场在架版本才能检查到更新。
* 本地安装版本须和应用市场在架版本签名信息保持一致。
* 暂不支持邀请测试和公开测试。

### 显示升级对话框

1. 导入updateManager 模块及相关公共模块。

   ```typescript
   import { updateManager } from '@kit.AppGalleryKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import type { common } from '@kit.AbilityKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 构造参数，其中入参为[common.UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md)类型的Context。

   ```typescript
   let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
   ```
3. 调用[showUpdateDialog](../harmonyos-references/store-updatemanager.md#updatemanagershowupdatedialog)方法显示升级对话框。

   ```typescript
   try {
     updateManager.showUpdateDialog(context)
       .then((resultCode: updateManager.ShowUpdateResultCode) => {
         hilog.info(0, 'TAG', 'Succeeded in showing UpdateDialog resultCode:' + resultCode);
       })
       .catch((error: BusinessError) => {
         hilog.error(0, 'TAG', `showUpdateDialog onError.code is ${error.code}, message is ${error.message}`);
       });
   } catch (error) {
     hilog.error(0, 'TAG', `showUpdateDialog onError.code is ${error.code}, message is ${error.message}`);
   }
   ```
