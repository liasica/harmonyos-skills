---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-attribution-test
title: 接入调试功能
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 应用归因服务 > 接入调试功能
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d0cc4018427f67963a5103d8573739ae23588d7ace25f805aaaf1f9f24a84bef
---

应用归因服务为开发者提供接入调试能力，支持开发者在接入过程中进行自助调试，通过调用调试接口验证接入的准确性及归因结果回传等基础能力，从而提升接入效率。

## 场景介绍

应用归因服务接入调试功能支持的场景如下：

* 校验接口调用是否准确

  调用调试接口，校验接口请求及业务逻辑，如参数校验、签名校验等，并提示相应错误码，支持开发者自行发现问题。
* 主动触发归因接口回传

  开发者设置归因数据后，调用调试接口主动、实时触发归因结果回传，验证完整的归因流程。

## 接口说明

应用归因服务接入调试功能提供以下接口，具体API说明详见[接口文档](../harmonyos-references/store-attributiontestmanager.md)。

| 接口名 | 描述 |
| --- | --- |
| validateSource(adSourceInfo: AdSourceInfo, publicKey: string): Promise<void> | 验证归因来源接口，用于媒体App/分发平台验证adSourceInfo入参的合法性。 |
| setPostback(postbackInfo: PostbackInfo): Promise<void> | 设置归因结果回传接口，用于应用生态伙伴：  - 验证triggerData是否合法。  - 设置调试使用的回传数据。 |
| flushPostbacks(adTechId: string): Promise<void> | 主动、实时触发归因结果回传接口，用于应用生态伙伴验证接收及处理回传的逻辑是否正确。 |

## 开发步骤

### 验证归因来源

1. 导入相关模块。

   ```
   1. import { attributionTestManager } from '@kit.AppGalleryKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError,deviceInfo} from '@kit.BasicServicesKit';
   ```
2. 构造参数，入参为[AdSourceInfo](../harmonyos-references/store-attributiontestmanager.md#adsourceinfo)、publickey。

   ```
   1. // 注册归因角色时提供给应用归因服务云侧的公钥
   2. let publicKey: string = '';
   3. let adSourceInfo: attributionTestManager.AdSourceInfo = {
   4. // 可以使用虚拟的adTechId
   5. adTechId: '2******8',
   6. campaignId: '',
   7. destinationId: '1*******8',
   8. sourceType: attributionTestManager.SourceType.IMPRESSION,
   9. mmpIds: ['1******8', '2******9'],
   10. serviceTag: 'testServiceTag',
   11. nonce: '123***2',
   12. timestamp: Date.now(),
   13. signature: 'MEQCIEQlmZ****zKBSE8QnhLTIHZZZ****ZpRqRxHss65Ko****JgJKjdrWdkL****juEx2RmFS7da****ZRVZ8RyMyUXg=='
   14. };
   15. let osApiVersion: number = deviceInfo.sdkApiVersion;
   16. if (osApiVersion >= 22) {
   17. adSourceInfo.campaignId = '1*******9';
   18. } else {
   19. adSourceInfo.campaignId = '1****6';
   20. }
   ```
3. 调用[attributionTestManager.validateSource](../harmonyos-references/store-attributiontestmanager.md#attributiontestmanagervalidatesource)方法验证归因来源。

   ```
   1. attributionTestManager.validateSource(adSourceInfo, publicKey).then(() => {
   2. hilog.info(0, "testTag", 'Succeeded in validating source.');
   3. }).catch((error: BusinessError) => {
   4. hilog.error(0, "testTag", `testValidateSource failed.code is ${error.code}, message is ${error.message}`);
   5. })
   ```

### 设置归因结果回传

1. 导入相关模块。

   ```
   1. import { attributionTestManager } from '@kit.AppGalleryKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError,deviceInfo } from '@kit.BasicServicesKit';
   ```
2. 构造参数，入参为[PostbackInfo](../harmonyos-references/store-attributiontestmanager.md#postbackinfo)。

   ```
   1. let postbackInfo: attributionTestManager.PostbackInfo = {
   2. adTechId: '1******8',
   3. campaignId: '',
   4. sourceId: '1*******8',
   5. destinationId: '1*******8',
   6. serviceTag: 'testServiceTag',
   7. businessScene: 5,
   8. triggerData: 123,
   9. postbackUrl: 'https://xxx.com'
   10. };
   11. let osApiVersion: number = deviceInfo.sdkApiVersion;
   12. if (osApiVersion >= 22) {
   13. postbackInfo.campaignId = '1*******9';
   14. } else {
   15. postbackInfo.campaignId = '1****6';
   16. }
   ```
3. 调用[attributionTestManager.setPostback](../harmonyos-references/store-attributiontestmanager.md#attributiontestmanagersetpostback)方法设置归因结果回传数据。

   ```
   1. attributionTestManager.setPostback(postbackInfo).then(() => {
   2. hilog.info(0, "testTag", 'Succeeded in setting postback.');
   3. }).catch((error: BusinessError) => {
   4. hilog.error(0, "testTag", `setPostback onError.code is ${error.code}, message is ${error.message}`);
   5. })
   ```

### 触发归因结果回传

1. 导入相关模块。

   ```
   1. import { attributionTestManager } from '@kit.AppGalleryKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 构造参数adTechId。

   ```
   1. let adTechId: string = '1******8';
   ```
3. 调用[attributionTestManager.flushPostbacks](../harmonyos-references/store-attributiontestmanager.md#attributiontestmanagerflushpostbacks)方法触发归因结果回传。

   ```
   1. attributionTestManager.flushPostbacks(adTechId).then(() => {
   2. hilog.info(0, "testTag", 'Succeeded in flushing postbacks.');
   3. }).catch((error: BusinessError) => {
   4. hilog.error(0, "testTag", `flushPostbacks onError.code is ${error.code}, message is ${error.message}`);
   5. })
   ```
