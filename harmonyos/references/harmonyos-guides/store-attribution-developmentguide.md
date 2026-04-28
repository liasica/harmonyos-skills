---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-attribution-developmentguide
title: 登记归因来源及转化
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 应用归因服务 > 登记归因来源及转化
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:23c07a6e2251dbe7f8f3cd685db37b4683e59c0a5f74450578c850af729ecd20
---

说明

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

   ```
   1. import { attributionManager } from '@kit.AppGalleryKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError,deviceInfo } from '@kit.BasicServicesKit';
   ```
2. 构造参数[AdSourceInfo](../harmonyos-references/store-attributionmanager.md#adsourceinfo)。

   ```
   1. const adSourceInfo: attributionManager.AdSourceInfo = {
   2. // 在应用归因云侧注册应用生态伙伴角色时，由应用归因服务分配
   3. adTechId: '20****e8',
   4. campaignId: '',
   5. // 开发者应用上架华为应用市场的appId，不带C
   6. destinationId: '10******',
   7. sourceType: attributionManager.SourceType.IMPRESSION,
   8. // 归因监测平台id
   9. mmpIds: ['2f****5','2f7***5'],
   10. // 分发平台关注的业务信息
   11. serviceTag: '123***2',
   12. // 用于计算签名的随机数，不带'-'
   13. nonce: '123***2',
   14. timestamp: Date.now(),
   15. // 签名值
   16. signature: 'MEQCIEQlmZ****zKBSE8QnhLTIHZZZ****ZpRqRxHss65Ko****JgJKjdrWdkL****juEx2RmFS7da****ZRVZ8RyMyUXg=='
   17. };
   18. let osApiVersion: number = deviceInfo.sdkApiVersion;
   19. if (osApiVersion >= 22) {
   20. adSourceInfo.campaignId = '1*******9';
   21. } else {
   22. adSourceInfo.campaignId = '1****6';
   23. }
   ```
3. 调用[attributionManager.registerSource](../harmonyos-references/store-attributionmanager.md#attributionmanagerregistersource)方法登记归因来源信息。

   ```
   1. try {
   2. attributionManager.registerSource(adSourceInfo).then(() => {
   3. hilog.info(0, 'TAG', 'Succeeded in registering source.');
   4. }).catch((error: BusinessError) => {
   5. hilog.error(0, 'TAG', `registerSource error.code is ${error.code}, message is ${error.message}`);
   6. })
   7. } catch (error) {
   8. hilog.error(0, 'TAG', `registerSource error.code is ${error.code}, message is ${error.message}`);
   9. }
   ```

### 登记归因转化

1. 导入相关模块。

   ```
   1. import { attributionManager } from '@kit.AppGalleryKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError,deviceInfo } from '@kit.BasicServicesKit';
   ```
2. 构造参数[AdTriggerInfo](../harmonyos-references/store-attributionmanager.md#adtriggerinfo)。

   ```
   1. const adTriggerInfo: attributionManager.AdTriggerInfo = {
   2. businessScene: 5,
   3. // 转化事件编码，从应用归因云端管理平台获取
   4. triggerData: 123
   5. };
   6. let osApiVersion: number = deviceInfo.sdkApiVersion;
   7. if (osApiVersion >= 22) {
   8. // Since API 22, added the actual occurrence time parameter.
   9. adTriggerInfo.timestamp = Date.now();
   10. adTriggerInfo.serviceTag = 'testServiceTag';
   11. }
   ```
3. 调用[attributionManager.registerTrigger](../harmonyos-references/store-attributionmanager.md#attributionmanagerregistertrigger)方法登记转化信息。

   ```
   1. try {
   2. attributionManager.registerTrigger(adTriggerInfo).then(() => {
   3. hilog.info(0, 'TAG', 'Succeeded in registering triggerdata.');
   4. }).catch((error: BusinessError) => {
   5. hilog.error(0, 'TAG', `registerTrigger error.code is ${error.code}, message is ${error.message}`);
   6. })
   7. } catch (error) {
   8. hilog.error(0, 'TAG', `registerTrigger error.code is ${error.code}, message is ${error.message}`);
   9. }
   ```
