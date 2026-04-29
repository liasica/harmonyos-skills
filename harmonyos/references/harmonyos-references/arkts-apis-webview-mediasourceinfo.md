---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-mediasourceinfo
title: Class (MediaSourceInfo)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > Class (MediaSourceInfo)
category: harmonyos-references
scraped_at: 2026-04-29T13:55:29+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:e2da3b0d9fb350c15aed56396efb5e0f96d716fe1b276d405cbe2766b587790d
---

表示媒体源的信息。

说明

* 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 12开始支持。
* 示例效果请以真机运行为准。

## 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type12+ | [SourceType](arkts-apis-webview-e.md#sourcetype12) | 否 | 否 | 媒体源的类型。 |
| source12+ | string | 否 | 否 | 媒体源地址。 |
| format12+ | string | 否 | 否 | 媒体源格式，可能为空，需要开发者自行判断格式。 |
