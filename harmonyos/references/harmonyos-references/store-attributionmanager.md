---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/store-attributionmanager
title: attributionManager（应用归因服务）
breadcrumb: API参考 > 应用服务 > AppGallery Kit（应用市场服务） > ArkTS API > attributionManager（应用归因服务）
category: harmonyos-references
scraped_at: 2026-04-28T08:16:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8bb7aece6c04a09c82b7dfa4ae616c7d39b71a42ef2e87139210a47a1f45d87c
---

为媒体/分发平台提供向应用归因服务（华为提供的不依赖用户标识符的端侧归因能力）登记归因来源、开发者/归因监测平台向应用归因服务登记转化事件功能。

说明

调用接口需捕获异常。

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1TabletTV

```
1. import { attributionManager } from '@kit.AppGalleryKit';
```

## AdSourceInfo

PhonePC/2in1TabletTV

媒体/分发平台登记的归因来源信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.AttributionManager

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| adTechId | string | 否 | 否 | 分发平台对应的归因角色ID，本次登记归因来源对应营销任务所归属的分发平台的标识符。  分发平台向应用归因云侧[注册归因角色](../harmonyos-guides/store-attribution-register.md#注册归因角色)时，由应用归因服务分配，长度固定为8个字符。 |
| campaignId | string | 否 | 否 | 营销任务ID，登记归因来源对应的营销任务的ID，长度不超过6个字符。  **说明：** 从6.0.2(22)开始，该接口支持长度由不超过6个字符变为不超过9个字符。 |
| destinationId | string | 否 | 否 | 开发者应用上架华为应用市场的AppId，长度不超过64个字符。  **说明：** 您的应用ID参考[查看应用基本信息](../app/agc-help-appinfo-0000001100014694.md)获取。 |
| sourceType | [SourceType](store-attributionmanager.md#sourcetype) | 否 | 否 | 归因来源类型：  0：曝光。  1：点击。 |
| mmpIds | string[] | 否 | 是 | 本次广告投放，使用的归因监测平台对应的归因角色ID。最大数量2个，每个ID字符串长度固定为8个字符。  如果调用方传递了归因监测平台ID，应用归因服务会向归因监测平台回传归因结果；如果调用方没有传递归因监测平台ID，则归因监测平台收不到回传的归因结果。 |
| serviceTag | string | 否 | 是 | 分发平台关注的业务信息，如创意、素材等，长度不超过32个字符。  如果调用方传递了serviceTag，在[申请开通权限](../harmonyos-guides/store-attribution-register.md#开通权限)后应用归因服务会将serviceTag回传分发平台。 |
| nonce | string | 否 | 否 | 用于计算签名的随机数，每次广告请求，nonce唯一。长度固定为32个字符。  同一个adTechId下，同一个nonce最多可以登记5次曝光，5次点击类型的归因来源信息。 |
| timestamp | number | 否 | 否 | 请求广告的时间戳（即广告投放时间，登记归因来源时，要求广告时间与当前时间偏差不超过10分钟）。unix时间戳，单位：毫秒 |
| signature | string | 否 | 否 | 签名值，分发平台/媒体根据广告相应信息按照[归因来源签名计算规则](../harmonyos-guides/appgallery-attribution-appendix-triger.md#归因来源签名计算规则)计算生成签名并提供，长度不超过800个字符。 |

## AdTriggerInfo

PhonePC/2in1TabletTV

开发者登记的转化事件信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.AttributionManager

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| businessScene | number | 否 | 是 | 业务场景值，在开发者登记转化时，用于标识开发者的业务场景。  取值范围：[0,99]。 |
| triggerData | number | 否 | 否 | 转化事件编码。  [标准转化事件](../harmonyos-guides/store-attribution-trigger-standard.md)取值范围：[1, 200]。  [自定义转化事件](../harmonyos-guides/store-attribution-trigger-custom.md)取值范围：[501, 600]。 |
| timestamp | number | 否 | 是 | 转化事件发生时间（要求登记转化事件接口调用时间与转化事件发生时间的间隔默认不超过10分钟）。unix时间戳，单位：毫秒。  **起始版本：** 6.0.2(22) |
| serviceTag | string | 否 | 是 | 开发者关注的业务信息，长度不超过32个字符。  如果调用方传递了serviceTag，在[申请开通权限](../harmonyos-guides/store-attribution-register.md#开通权限)后应用归因服务会将serviceTag回传开发者。  **起始版本：** 6.0.2(22) |

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

## attributionManager.registerSource

PhonePC/2in1TabletTV

registerSource(adSourceInfo: AdSourceInfo): Promise<void>

登记归因来源接口，由媒体/分发平台接入注册。通过Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.AttributionManager

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| adSourceInfo | [AdSourceInfo](store-attributionmanager.md#adsourceinfo) | 是 | 媒体/分发平台登记归因来源信息。 |

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
| 1009300003 | The identity check error. |
| 1009300004 | The sign check error. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { attributionManager } from '@kit.AppGalleryKit';
3. // 参考指南附录生成签名方法部分代码
4. import { SignUtil } from '../common/utils/SignUtil';
5. import { util } from '@kit.ArkTS';
6. import { BusinessError,deviceInfo } from '@kit.BasicServicesKit';

8. const TAG: string = 'Attribution';

10. class  Attribution {
11. async registerSource(): Promise<void> {
12. try {
13. // 使用在应用归因服务云侧注册角色时，提供的公钥所对应的私钥
14. let privateKey: string =" ";
15. // 在应用归因云侧注册广告生态伙伴角色时，由应用归因服务分配
16. let adTechId: string = '20****8';
17. // 分发平台创建的营销任务id，6.0.2(22)之前支持长度不超过6个字符，6.0.2(22)及以上支持长度不超过9个字符
18. let campaignId: string = '';
19. let osApiVersion: number = deviceInfo.sdkApiVersion;
20. if (osApiVersion >= 22) {
21. campaignId = '1*******9';
22. } else {
23. campaignId = '1****6';
24. }
25. // 开发者应用上架华为应用市场的appId，不带C
26. let destinationId: string = '691****4';
27. // 归因监测平台id
28. let mmpIds: string[] = ['2f76e815'];
29. // 分发平台关注的业务信息
30. let serviceTag: string = 'testServiceTag';
31. // 用于计算签名的随机数，不带'-'
32. let nonce: string = util.generateRandomUUID().replace(/-/g, '');
33. // 时间戳
34. let timestamp: number = Date.now()
35. let adSourceInfo: attributionManager.AdSourceInfo = {
36. adTechId: adTechId,
37. campaignId: campaignId,
38. destinationId: destinationId,
39. // 归因来源类型：曝光
40. sourceType: attributionManager.SourceType.IMPRESSION,
41. mmpIds: mmpIds,
42. serviceTag: serviceTag,
43. nonce: nonce,
44. timestamp: timestamp,
45. // 签名值
46. signature: await SignUtil.getSign(SignUtil.genSignContent(adTechId, campaignId, destinationId, mmpIds, serviceTag, nonce, timestamp), privateKey)
47. };

49. attributionManager.registerSource(adSourceInfo).then(() => {
50. hilog.info(0, TAG, 'Succeeded in registering source.');
51. }).catch((error: BusinessError) => {
52. hilog.error(0, TAG, `registerSource error.code is ${error.code}, message is ${error.message}`);
53. })
54. } catch (error) {
55. hilog.error(0, TAG, `registerSource error.code is ${error.code}, message is ${error.message}`);
56. }
57. }
58. }
```

## attributionManager.registerTrigger

PhonePC/2in1TabletTV

registerTrigger(adTriggerInfo: AdTriggerInfo): Promise<void>

登记转化接口，由开发者接入注册。通过Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.AttributionManager

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| adTriggerInfo | [AdTriggerInfo](store-attributionmanager.md#adtriggerinfo) | 是 | 转化事件信息。 |

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
| 1009300003 | The identity check error. |

**示例：**

```
1. import { BusinessError,deviceInfo } from '@kit.BasicServicesKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { attributionManager } from '@kit.AppGalleryKit';

5. const TAG: string = 'Attribution';

7. class Attribution {
8. registerTrigger(): void {
9. try {
10. let adTriggerInfo: attributionManager.AdTriggerInfo = {
11. businessScene: 5,
12. // 转化事件编码，从应用归因云端管理平台获取
13. triggerData: 123,

15. };
16. let osApiVersion: number = deviceInfo.sdkApiVersion;
17. if (osApiVersion >= 22) {
18. // 从6.0.2（22）开始，增加事件转化时间
19. adTriggerInfo.timestamp = Date.now();
20. adTriggerInfo.serviceTag = 'testServiceTag';
21. };

23. attributionManager.registerTrigger(adTriggerInfo).then(() => {
24. hilog.info(0, TAG, 'Succeeded in registering triggerdata.');
25. }).catch((error: BusinessError) => {
26. hilog.error(0, TAG, `registerTrigger error.code is ${error.code}, message is ${error.message}`);
27. })
28. } catch (error) {
29. hilog.error(0, TAG, `registerTrigger error.code is ${error.code}, message is ${error.message}`);
30. }
31. }
32. }
```
