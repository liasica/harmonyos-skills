---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-pdfdata
title: Class (PdfData)
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > ArkTS API > @ohos.web.webview (Webview) > Class (PdfData)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:26+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2ef2b069880c237105b65fae7a3d872a017e59f3e1574e519b494b0a89cf8009
---

PdfData是Web组件用于封装网页生成的PDF数据流的类。当应用需要将Web组件加载的网页内容以PDF格式保存时，通过[WebviewController](arkts-apis-webview-webviewcontroller.md)的[createPdf](arkts-apis-webview-webviewcontroller.md#createpdf14)方法将网页内容转换为PDF数据流，该方法在回调或Promise中以PdfData对象返回。应用再通过PdfData的pdfArrayBuffer方法获取Uint8Array格式的数据流，结合文件IO接口将数据写入本地PDF文件。

PdfData适用于需要离线保存网页内容、生成网页PDF报告等场景。使用时需先加载Web组件并确保网页内容已渲染完成，再调用createPdf生成PDF数据流。

**说明** 

* 本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本Class首批接口从API version 14开始支持。
* 示例效果请以真机运行为准。
* 在网页生成PDF过程中，返回的是数据流，由PdfData类封装。

## pdfArrayBuffer14+

pdfArrayBuffer(): Uint8Array

获取网页生成的PDF数据流。完整示例代码参考[createPdf](arkts-apis-webview-webviewcontroller.md#createpdf14)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 网页生成的PDF数据流，可结合文件IO接口将数据写入本地PDF文件。 |
