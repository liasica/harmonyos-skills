---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-introduction
title: PDF Kit简介
breadcrumb: 指南 > 应用服务 > PDF Kit（PDF服务） > PDF Kit简介
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b6282c7f5722bd2be9c24702b0f5fcd900eab9ace858a75f7a2ba4f267dc2d24
---

PDF Kit（PDF服务）包含pdfService和PdfView组件。

pdfService提供了加载和保存PDF文档、在PDF页面中添加文本内容、图片、批注、页眉页脚、水印、背景图片、书签、判断PDF文档是否加密及删除文档加密等相关的功能，对PDF文档的操作有更多的应用场景。

PdfView组件提供了文档预览功能，如：PDF文档预览、高亮显示、搜索关键字，批注等场景。

PDF Kit更多的示例代码请参考[CodeLab](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_PDFKit-Codelab-Clientdemo-ArkTS)和[SampleCode](https://gitcode.com/harmonyos_samples/pdfkit_-sample-code_-arkts)。

## pdfService与PdfView能力比较

| PDF Kit能力 | pdfService是否支持 | PdfView预览组件是否支持 |
| --- | --- | --- |
| 打开和保存文档 | 支持 | 支持 |
| 释放文档 | 支持 | 支持 |
| PDF文档转图片 | 支持 | 支持 |
| 添加、删除批注 | 支持 | 支持 |
| 管理书签 | 支持 | 不支持 |
| 添加、编辑、删除PDF页 | 支持 | 不支持 |
| 添加、删除文本内容 | 支持 | 不支持 |
| 添加、删除图片内容 | 支持 | 不支持 |
| 编辑页眉页脚、水印、背景 | 支持 | 不支持 |
| 判断PDF文档是否加密 | 支持 | 不支持 |
| 删除文档加密 | 支持 | 不支持 |
| PDF文档预览 | 不支持 | 支持 |
| 搜索关键字 | 不支持 | 支持 |
| PDF文档监听回调 | 不支持 | 支持 |

## 约束与限制

### 支持的国家和地区

当前PDF Kit仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

### 支持的设备

PDF Kit相关能力支持在Phone、Tablet和PC/2in1设备上运行。

## 模拟器支持的情况

本Kit支持模拟器开发，但与真机存在部分能力差异，具体差异如下：

* 通用差异：请参见“[模拟器与真机的差异](ide-emulator-specification.md#section1227613205203)”。
* 支持ARM模拟器，不支持x86模拟器。
