---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-adsserviceextensionability
title: @ohos.advertising.AdsServiceExtensionAbility(广告扩展服务)
breadcrumb: API参考 > 应用服务 > Ads Kit（广告服务） > ArkTS API > @ohos.advertising.AdsServiceExtensionAbility(广告扩展服务)
category: harmonyos-references
scraped_at: 2026-04-28T08:16:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5c9360ed6b4b0a39e95384e2a9fd077eaaa835f8ad388eb39e24cd10b6bc17db
---

本模块为设备厂商提供广告扩展能力，设备厂商可自主实现请求广告的回调。

说明

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1Tablet

```
1. import { RespCallback } from '@kit.AdsKit';
```

## RespCallback

PhonePC/2in1Tablet

(respData: Map<string, Array<advertising.Advertisement>>): void

广告请求回调。

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| **参数名** | **类型** | 必填 | 说明 |
| --- | --- | --- | --- |
| respData | Map<string, Array<advertising.[Advertisement](js-apis-advertising.md#advertisement)>> | 是 | 广告请求回调数据。 |

**示例：**

```
1. import { advertising, RespCallback } from '@kit.AdsKit';

3. function setRespCallback(respCallback: RespCallback) {
4. const respData: Map<string, Array<advertising.Advertisement>> = new Map();
5. // 设置广告返回数据
6. // ...
7. respCallback(respData);
8. }
```
