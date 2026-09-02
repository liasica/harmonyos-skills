---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-attribution-developmentguide
title: 登记归因来源及转化
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 应用归因服务 > 登记归因来源及转化
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:53+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:9a5b50ed770ec8ef4ec6966cbedeb3f8e83ef9b70df32542c0ea235381140a6d
---

**说明** 

6.0.2(22)版本开始，登记归因转化接口新增属性timestamp、serviceTag，支持设置转化事件时间及开发者关注的业务信息。

## 场景介绍

应用归因服务为媒体App、分发平台提供向端侧应用归因服务登记归因来源（即应用曝光点击事件）、开发者应用登记转化事件的能力。

端侧应用归因服务根据媒体应用登记的归因来源，以及开发者应用登记的转化事件，按照系统规则，在端侧完成归因计算。

## 接口说明

应用归因服务场景提供以下接口，具体API说明详见[接口文档](../harmonyos-references/store-attributionmanager.md)。

| 接口名 | 描述 |
| --- | --- |
| registerSource(adSourceInfo: AdSourceInfo): Promise<void> | 登记归因来源信息接口。 |
| registerTrigger(adTriggerInfo: AdTriggerInfo): Promise<void> | 登记归因转化信息接口。 |

## 开发步骤

### 登记归因来源

1. 导入相关模块。

   ```typescript
   import { BusinessError, deviceInfo } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { SignUtil } from '../common/utils/SignUtil';
   import { util } from '@kit.ArkTS';
   import { attributionManager } from '@kit.AppGalleryKit';
   ```
2. 构造参数[AdSourceInfo](../harmonyos-references/store-attributionmanager.md#adsourceinfo)。

   ```typescript
   // 私钥，由开发者生成，用于生成签名值使用
   let privateKey: string = '********u2rMtFw==';
   // 分发平台对应的归因角色ID，在应用归因云侧注册应用生态伙伴角色时，由应用归因服务分配
   let adTechId: string = '2******';
   // 广告平台创建的广告任务ID。
   // 自API 12起，campaignId长度小于等于6个字符
   // 自API 22起，campaignId长度小于等于9个字符
   let campaignId: string = '';
   let osApiVersion: number = deviceInfo.sdkApiVersion;
   if (osApiVersion >= 22) {
       campaignId = '1*******9';
   } else {
       campaignId = '1****6';
   }
   // 开发者应用上架华为应用市场的appId，不带C
   let destinationId: string = '6*********4';
   // 归因监测平台id
   let mmpIds: string[] = ['2f*****15'];
   // 分发平台关注的业务信息
   let serviceTag: string = 'testServiceTag';
   // 用于计算签名的随机数，不带'-'
   let nonce: string = util.generateRandomUUID().replace(/-/g, '');
   // 时间戳.
   let timestamp: number = Date.now()

   let adSourceInfo: attributionManager.AdSourceInfo = {
       adTechId: adTechId,
       campaignId: campaignId,
       destinationId: destinationId,
       // 曝光.
       sourceType: attributionManager.SourceType.IMPRESSION,
       mmpIds: mmpIds,
       serviceTag: serviceTag,
       nonce: nonce,
       timestamp: timestamp,
       // 签名值.
       signature: await SignUtil.getSign(this.getUIContext(),
           SignUtil.genSignContent(adTechId, campaignId, destinationId, mmpIds, serviceTag, nonce, timestamp),
           privateKey)
   };
   ```
3. 调用[attributionManager.registerSource](../harmonyos-references/store-attributionmanager.md#attributionmanagerregistersource)方法登记归因来源信息。

   ```typescript
   try {
       // ...
       attributionManager.registerSource(adSourceInfo).then(() => {
           hilog.info(0, TAG, 'registerSource success.');
           // ...
       }).catch((error: BusinessError) => {
           hilog.error(0, TAG, `registerSource error. code is ${error.code}, message is ${error.message}`);
           // ...
       })
   } catch (error) {
       hilog.error(0, TAG, `registerSource error. code is ${error.code}, message is ${error.message}`);
       // ...
   }
   ```

### 登记归因转化

1. 导入相关模块。

   ```typescript
   import { BusinessError, deviceInfo } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   // ...
   import { attributionManager } from '@kit.AppGalleryKit';
   ```
2. 构造参数[AdTriggerInfo](../harmonyos-references/store-attributionmanager.md#adtriggerinfo)。

   ```typescript
   let adTriggerInfo: attributionManager.AdTriggerInfo = {
       // 转化事件编码，从应用归因云端管理平台获取
       triggerData: 123,
       businessScene: 5
   };
   let osApiVersion: number = deviceInfo.sdkApiVersion;
   if (osApiVersion >= 22) {
       // 自API 22起，增加了实际发生时间参数。
       adTriggerInfo.timestamp = Date.now();
       // 自API 22起，增加了广告平台关注的业务信息。
       adTriggerInfo.serviceTag = 'testServiceTag';
   }
   ```
3. 调用[attributionManager.registerTrigger](../harmonyos-references/store-attributionmanager.md#attributionmanagerregistertrigger)方法登记转化信息。

   ```typescript
   try {
       // ...
       attributionManager.registerTrigger(adTriggerInfo).then(() => {
           hilog.info(0, TAG, 'registerTrigger success');
           // ...
       }).catch((error: BusinessError) => {
           hilog.error(0, TAG, `registerTrigger error. code is ${error.code}, message is ${error.message}`);
           // ...
       })
   } catch (error) {
       hilog.error(0, TAG, `registerTrigger error. code is ${error.code}, message is ${error.message}`);
       // ...
   }
   ```
