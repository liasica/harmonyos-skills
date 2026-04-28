---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-pdfdata
title: Class (PdfData)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > Class (PdfData)
category: harmonyos-references
scraped_at: 2026-04-28T08:05:02+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c2ed65446e6e11787461474dce29f5be4a6f7dd5124f6c9a99cc6c57a56592ff
---

createPdf函数输出数据流类。

说明

* 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 14开始支持。
* 示例效果请以真机运行为准。
* 在网页生成PDF过程中，返回的是数据流，由PdfData类封装。

## pdfArrayBuffer14+

PhonePC/2in1TabletTVWearable

pdfArrayBuffer(): Uint8Array

获取网页生成的数据流。完整示例代码参考[createPdf](arkts-apis-webview-webviewcontroller.md#createpdf14)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 数据流。 |
