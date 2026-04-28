---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/store-attributiontestmanager
title: attributionTestManager（应用归因接入调试功能）
breadcrumb: API参考 > 应用服务 > AppGallery Kit（应用市场服务） > ArkTS API > attributionTestManager（应用归因接入调试功能）
category: harmonyos-references
scraped_at: 2026-04-28T08:16:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d1411d125450c2d74bac86e33ee6794bed19a86ed02576949c9c0bf4feaa3fd7
---

提供验证归因来源、设置归因结果回传、触发归因结果回传调试功能。

说明

调用接口需捕获异常。

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1TabletTV

```
1. import { attributionTestManager } from '@kit.AppGalleryKit';
```

## attributionTestManager.validateSource

PhonePC/2in1TabletTV

validateSource(adSourceInfo: AdSourceInfo, publicKey: string): Promise<void>

验证媒体App/分发平台登记的归因来源信息，通过Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.AttributionManager

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| adSourceInfo | [AdSourceInfo](store-attributiontestmanager.md#adsourceinfo) | 是 | 媒体app/分发平台登记的归因来源信息。 |
| publicKey | string | 是 | 已[生成密钥对](../harmonyos-guides/store-attribution-register.md#生成密钥对)中的公钥。注册归因角色时提供给应用归因服务云侧的公钥。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](store-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1009300001 | The specified service extension connect failed. |
| 1009300002 | System internal error. |
| 1009300101 | AdTechId is missing in the request. |
| 1009300102 | CampaignId is missing in the request. |
| 1009300104 | DestinationId is missing in the request. |
| 1009300105 | SourceType is missing in the request. |
| 1009300106 | Nonce is missing in the request. |
| 1009300107 | Timestamp is missing in the request. |
| 1009300108 | Signature is missing in the request. |
| 1009300111 | AdSourceInfo is missing in the request. |
| 1009300112 | PublicKey is missing in the request. |
| 1009300114 | The signature verification failed in the testing environment. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { attributionTestManager } from '@kit.AppGalleryKit';
3. // 参考指南附录生成签名方法部分代码
4. import { SignUtil } from '../common/utils/SignUtil';
5. import { util } from '@kit.ArkTS';
6. import { deviceInfo } from '@kit.BasicServicesKit';

8. const TAG: string = 'AttributionTest';

10. class  AttributionTest {

12. async validateSource(): Promise<void> {
13. try {
14. // 使用在应用归因服务云侧注册角色时，提供的公钥和对应的私钥, 验证接口， 用户可自己生成
15. let privateKey: string = '';
16. let publicKey: string = '';
17. // 在应用归因云侧注册广告生态伙伴角色时，由应用归因服务分配
18. let adTechId: string = '12345678';
19. // 分发平台创建的营销任务id
20. let campaignId: string = ' ';
21. let osApiVersion: number = deviceInfo.sdkApiVersion;
22. if (osApiVersion >= 22) {
23. campaignId = '1*******9';
24. } else {
25. campaignId = '1****6';
26. }
27. // 开发者应用上架华为应用市场的appId，不带C
28. let destinationId: string = '102345678';
29. // 归因监测平台id
30. let mmpIds: string[] = ['12345678', '23456789'];
31. // 分发平台关注的业务信息
32. let serviceTag: string = 'testServiceTag';
33. // 用于计算签名的随机数，不带'-'
34. let nonce: string = util.generateRandomUUID().replace(/-/g, '');
35. // 时间戳
36. let timestamp: number = Date.now()
37. let adSourceInfo: attributionTestManager.AdSourceInfo = {
38. adTechId: adTechId,
39. campaignId: campaignId,
40. destinationId: destinationId,
41. // 归因来源类型：曝光
42. sourceType: attributionTestManager.SourceType.IMPRESSION,
43. mmpIds: mmpIds,
44. serviceTag: serviceTag,
45. nonce: nonce,
46. timestamp: timestamp,
47. // 签名值
48. signature: await SignUtil.getSign(SignUtil.genSignContent(adTechId, campaignId, destinationId, mmpIds, serviceTag, nonce, timestamp), privateKey)
49. };

51. await attributionTestManager.validateSource(adSourceInfo, publicKey);
52. hilog.info(0, TAG, 'Succeeded in validating source.');
53. } catch (error) {
54. hilog.error(0, TAG, `validateSource error.code is ${error.code}, message is ${error.message}`);
55. }
56. }
57. }
```

## attributionTestManager.setPostback

PhonePC/2in1TabletTV

setPostback(postbackInfo: PostbackInfo): Promise<void>

设置归因结果回传信息。用于验证triggerData的合法性，设置调试使用的归因结果回传信息，通过Promise异步回调。

说明

单个adTechId下，待回传的调试postbackInfo数据量<=5。

单个设备下，待回传的调试postbackInfo数据量<=100。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.AttributionManager

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| postbackInfo | [PostbackInfo](store-attributiontestmanager.md#postbackinfo) | 是 | 归因结果回传信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](store-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1009300001 | The specified service extension connect failed. |
| 1009300002 | System internal error. |
| 1009300101 | AdTechId is missing in the request. |
| 1009300102 | CampaignId is missing in the request. |
| 1009300103 | SourceId is missing in the request. |
| 1009300104 | DestinationId is missing in the request. |
| 1009300109 | TriggerData is missing in the request. |
| 1009300110 | PostbackUrl is missing in the request. |
| 1009300113 | PostbackInfo is missing in the request. |
| 1009300115 | Too many postbacks setting to the testing environment. |

**示例**：

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { attributionTestManager } from '@kit.AppGalleryKit';
3. import { deviceInfo } from '@kit.BasicServicesKit';

5. const TAG: string = 'Attributiontest';

7. @Entry
8. @Component
9. struct Attribution {
10. build() {
11. Column({ space: 20 }) {
12. Button("set_postback")
13. .onClick(() => {
14. this.setPostback();
15. })
16. .width('100%')
17. }
18. .margin(16)
19. .height('100%')
20. .justifyContent(FlexAlign.Center)
21. }

23. async setPostback(): Promise<void> {
24. try {
25. let postbackInfo: attributionTestManager.PostbackInfo = {
26. // 在应用归因云侧注册广告生态伙伴角色时，由应用归因服务分配
27. adTechId: '12345678',
28. // 分发平台创建的营销任务id
29. campaignId: ' ',
30. // 媒体应用id
31. sourceId: '112345678',
32. // 开发者应用上架华为应用市场的appId，不带C
33. destinationId: '102345678',
34. // 分发平台关注的业务信息
35. serviceTag: 'testServiceTag',
36. // 业务场景值
37. businessScene: 5,
38. // 转化事件编码
39. triggerData: 123,
40. // 用于接收归因回传归因结果的URL地址，推荐使用HTTPS协议
41. postbackUrl: 'https://xxx.com'
42. };
43. let osApiVersion: number = deviceInfo.sdkApiVersion;
44. if (osApiVersion >= 22) {
45. postbackInfo.campaignId = '1*******9';
46. } else {
47. postbackInfo.campaignId = '1****6';
48. }
49. // 设置归因结果回传信息
50. attributionTestManager.setPostback(postbackInfo).then(() => {
51. hilog.info(0, TAG, 'Succeeded in setting postback.');
52. }).catch((error: BusinessError) => {
53. hilog.error(0, TAG, `setPostback onError.code is ${error.code}, message is ${error.message}`);
54. })
55. } catch (error) {
56. hilog.error(0, TAG, `setPostback onError.code is ${error.code}, message is ${error.message}`);
57. }
58. }
59. }
```

## attributionTestManager.flushPostbacks

PhonePC/2in1TabletTV

flushPostbacks(adTechId: string): Promise<void>

触发归因结果回传。验证开发者服务器接收及处理归因回传结果的逻辑是否正确，通过Promise异步回调。

说明

单个设备上，每5秒调用次数<=1。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.AttributionManager

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| adTechId | string | 是 | 分发平台对应的归因角色ID，本次登记归因来源对应营销任务所归属的分发平台的标识符，长度固定为8个字符。  使用setPostback()接口中成功设置的adTechId值。  **说明：** 调试过程不依赖云侧注册，开发者可以使用虚拟的adTechId。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](store-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1009300001 | The specified service extension connect failed. |
| 1009300002 | System internal error. |
| 1009300101 | AdTechId is missing in the request. |
| 1009300116 | There is no postback to be sent of this adTechId. |
| 1009300117 | Failed to send postbacks to the postbackUrl. |
| 1009300119 | Network error. |
| 1009300120 | Request too frequent. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import {attributionTestManager } from '@kit.AppGalleryKit';

4. const TAG: string = 'AttributionTest';

6. @Entry
7. @Component
8. struct Attribution {
9. build() {
10. Column({ space: 20 }) {
11. Button("flush_postbacks")
12. .id('flush_postbacks')
13. .onClick(() => {
14. this.flushPostbacks();
15. })
16. .width('100%')
17. }
18. .margin(16)
19. .height('100%')
20. .justifyContent(FlexAlign.Center)
21. }

23. async flushPostbacks(): Promise<void> {
24. try {
25. // 分发平台对应的归因角色ID
26. let adTechId: string = '1******8';
27. // 触发归因结果回传
28. await attributionTestManager.flushPostbacks(adTechId);
29. hilog.info(0, TAG, 'flushPostbacks success.');
30. } catch (error) {
31. hilog.error(0, TAG, `flushPostbacks error. code is ${error.code}, message is ${error.message}`);
32. }
33. }
34. }
```

## AdSourceInfo

PhonePC/2in1TabletTV

媒体app/分发平台登记的归因来源信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.AttributionManager

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| adTechId | string | 否 | 否 | 分发平台对应的归因角色ID，本次登记归因来源对应营销任务所归属的分发平台的标识符。  分发平台向应用归因云侧[注册归因角色](../harmonyos-guides/store-attribution-register.md#注册归因角色)时，由应用归因服务分配，长度固定为8个字符。  **说明：** 调试过程不依赖云侧注册，开发者可以使用虚拟的adTechId。 |
| campaignId | string | 否 | 否 | 营销任务ID，登记归因来源对应的营销任务的ID，长度不超过6个字符。  **说明：** 从6.0.2(22)开始，该接口支持长度由不超过6个字符变为不超过9个字符。 |
| destinationId | string | 否 | 否 | 开发者应用上架华为应用市场的AppId，长度不超过64个字符。  **说明：** 您的应用ID参考[查看应用基本信息](../app/agc-help-appinfo-0000001100014694.md)获取。 |
| sourceType | [SourceType](store-attributiontestmanager.md#sourcetype) | 否 | 否 | 归因来源类型：  0：曝光。  1：点击。 |
| mmpIds | string[] | 否 | 是 | 本次广告投放，使用的归因监测平台对应的归因角色ID。最大数量2个，每个ID字符串长度固定为8个字符。  如果调用方传递了归因监测平台ID，应用归因服务会向归因监测平台回传归因结果；如果调用方没有传递归因监测平台ID，则归因监测平台收不到回传的归因结果。 |
| serviceTag | string | 否 | 是 | 分发平台关注的业务信息，如创意、素材等，长度不超过32个字符。  如果调用方传递了serviceTag，在[申请开通权限](../harmonyos-guides/store-attribution-register.md#开通权限)后应用归因服务会将serviceTag回传分发平台。 |
| nonce | string | 否 | 否 | 用于计算签名的随机数，每次广告请求，nonce唯一。长度固定为32个字符。 |
| timestamp | number | 否 | 否 | 请求广告的时间戳。（即广告投放时间，与当前时间偏差不超过10分钟）。unix时间戳，单位：毫秒。 |
| signature | string | 否 | 否 | 签名值，分发平台/媒体根据广告相应信息按照[归因来源签名计算规则](../harmonyos-guides/appgallery-attribution-appendix-triger.md#归因来源签名计算规则)计算并提供，长度不超过800个字符。 |

## PostbackInfo

PhonePC/2in1TabletTV

待回传数据信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.AttributionManager

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| adTechId | string | 否 | 否 | 分发平台对应的归因角色ID，本次登记归因来源对应营销任务所归属的分发平台的标识符。  使用setPostback()接口中成功设置的adTechId值。  **说明：** 调试过程不依赖云侧注册，开发者可以使用虚拟的adTechId。 |
| campaignId | string | 否 | 否 | 营销任务ID，登记归因来源对应的营销任务的ID，长度不超过6个字符。  **说明：** 从6.0.2(22)开始，该接口支持长度由不超过6字符变为不超过9字符。 |
| sourceId | string | 否 | 否 | 媒体应用id，长度不超过64个字符。 |
| destinationId | string | 否 | 否 | 开发者应用上架华为应用市场的AppId，长度不超过64个字符。 |
| serviceTag | string | 否 | 是 | 分发平台关注的业务信息，如创意、素材等，长度不超过32个字符。  如果调用方传递了serviceTag，在[申请开通权限](../harmonyos-guides/store-attribution-register.md#开通权限)后应用归因服务会将serviceTag回传分发平台。 |
| businessScene | number | 否 | 是 | 业务场景值，在开发者登记转化时，用于标识开发者的业务场景。  取值范围：[0,99]。 |
| triggerData | number | 否 | 否 | 转化事件编码。  取值范围：[0,999]。 |
| postbackUrl | string | 否 | 否 | 用于接收归因回传归因结果的URL地址，推荐使用HTTPS协议。 |

## SourceType

PhonePC/2in1TabletTV

归因来源类型的枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.AttributionManager

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| IMPRESSION | 0 | 归因来源类型：曝光。 |
| CLICK | 1 | 归因来源类型：点击。 |
