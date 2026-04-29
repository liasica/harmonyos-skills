---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-advertisement
title: Advertisement (请求的广告内容)
breadcrumb: API参考 > 应用服务 > Ads Kit（广告服务） > ArkTS API > advertisement > Advertisement (请求的广告内容)
category: harmonyos-references
scraped_at: 2026-04-29T14:06:56+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:79e215016d50b10f9152fc204324c5e93db1bb5a2b2d76812e523a0d9547a94f
---

本模块为请求的广告内容。

说明

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1Tablet

```
1. import { advertising } from '@kit.AdsKit';
```

## Advertisement

PhonePC/2in1Tablet

请求的广告内容。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| adType | number | 否 | 否 | 广告类型。  - 1：开屏广告。  - 3：原生广告。  - 7：激励广告。  - 8：横幅广告。  - 12：插屏广告。  - 60：贴片广告。  不填默认为原生广告类型。 |
| uniqueId | string | 否 | 否 | 广告唯一标识。 |
| rewarded | boolean | 否 | 否 | 广告是否获得奖励。  - true：获得奖励。  - false：没有获得奖励。 |
| shown | boolean | 否 | 否 | 广告是否展示。  - true：展示。  - false：未展示。 |
| clicked | boolean | 否 | 否 | 广告是否被点击。  - true：被点击。  - false：未被点击。 |
| rewardVerifyConfig | Map<string, string> | 否 | 否 | 服务器验证参数。  {  customData: "test",  userId: "12345"  } |
| [key: string] | Object | 否 | 是 | 自定义参数。  - isFullScreen：类型boolean。开屏广告自定义参数，用于标识返回的广告是否为全屏，true为全屏广告，false为半屏广告。  - biddingInfo：类型Object。用于获取实时竞价相关结果。  - biddingInfo.price：类型number。本条广告的eCPM（Effective Cost Per Mille，每一千次展示可以获得的广告收入）。  - biddingInfo.cur:类型string。 本条广告的价格币种。支持币种：CNY（单位：元）、USD（单位：美元）、EUR（单位：欧元）、GBP（单位：英镑）、JPY（单位：日元）。  - biddingInfo.nurl：类型string。媒体回传竞价成功结果的URL。  - biddingInfo.lurl：类型string。媒体回传竞价失败通知其他DSP竞价成功结果的URL。 |
