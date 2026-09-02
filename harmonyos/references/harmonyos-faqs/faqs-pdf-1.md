---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-pdf-1
title: HarmonyOS应用内使用PdfView或Web组件预览PDF文件失败的排查方案
breadcrumb: FAQ > 应用服务开发 > PDF文档解析服务（PDF Kit） > HarmonyOS应用内使用PdfView或Web组件预览PDF文件失败的排查方案
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:24+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:023656be3d56ed36df68896a21fa36a0abc0ce64f24e3e8590c53b1531b9b4de
---

## 问题现象

* 场景一：使用PdfView组件预览PDF文件时，出现预览失败，显示空白的现象。
* 场景二：使用Web组件预览PDF文件时，出现预览失败，显示空白的现象。
* 场景三：使用PdfView组件预览PDF文件时，报错1011301006，提示PDF文档未加载。

## 背景知识

* [PdfView预览组件](../harmonyos-guides/pdf-pdfview-implements.md)：HarmonyOS应用通过集成该组件完成PDF文件的预览功能。

  [预览PDF文档](../harmonyos-guides/pdf-pdfview-component.md)：通过加载本地路径的PDF文档，实现打开PDF文档的预览功能（为了避免文件目录的权限问题，建议通过沙箱目录加载和保存PDF文档）。

  | 接口名 | 描述 |
  | --- | --- |
  | [loadDocument()](../harmonyos-references/pdf-arkts-pdfviewmanage.md#loaddocument) | 加载PDF文档。 |
  | [saveDocument()](../harmonyos-references/pdf-arkts-pdfviewmanage.md#savedocument) | 保存PDF文档。 |
* [Web组件预览PDF文档](../harmonyos-guides/web-pdf-preview.md)：Web组件提供了在网页中预览PDF的能力。应用通过Web组件的[src](../harmonyos-references/arkts-basic-components-web-i.md#weboptions)参数和[loadUrl()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#loadurl)接口加载PDF文档。

  **说明** 

  由于PDF预览页面会根据用户操作使用window.localStorage记录侧边导航栏的展开状态，因此需要开启文档对象模型存储[domStorageAccess](../harmonyos-references/arkts-basic-components-web-attributes.md#domstorageaccess)权限。

## 问题定位

1. [PdfView预览组件](../harmonyos-guides/pdf-pdfview-implements.md)提供预览PDF文档能力：搜索[loadDocument()](../harmonyos-references/pdf-arkts-pdfviewmanage.md#loaddocument)，检查传入的文件是否属于本地文件，不支持在线预览。
2. 使用Web组件的PDF文档预览能力：
   * 搜索[domStorageAccess](../harmonyos-references/arkts-basic-components-web-attributes.md#domstorageaccess)，检查是否开启文档对象模型存储接口。
   * 搜索Web组件的[src](../harmonyos-references/arkts-basic-components-web-i.md#weboptions)参数和[loadUrl()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#loadurl)接口，检查传入的URL是否正确。

     **说明** 

     对于加载应用沙箱内PDF文档，检查是否开启应用中文件系统的访问[fileAccess](../harmonyos-references/arkts-basic-components-web-attributes.md#fileaccess)权限。

     Web组件的第一个参数变量src不能通过状态变量（例如：@State）动态更改地址，如需更改，请通过loadUrl()重新加载。
3. 使用PdfView组件预览PDF文件时报错1011301006：检查是否在组件初始化完成后调用了[loadDocument()](../harmonyos-references/pdf-arkts-pdfviewmanage.md#loaddocument)加载PDF文档，以及加载过程是否中断。

## 分析结论

### 场景一

[PdfView预览组件](../harmonyos-guides/pdf-pdfview-implements.md)提供预览PDF文档能力，由于不支持在线预览，导致预览失败。

### 场景二

使用Web组件的PDF文档预览能力：

1. 由于未开启Web组件的文档对象模型存储（[domStorageAccess](../harmonyos-references/arkts-basic-components-web-attributes.md#domstorageaccess)）接口，导致预览失败。
2. 传入Web组件中[src](../harmonyos-references/arkts-basic-components-web-i.md#weboptions)参数和[loadUrl()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#loadurl)接口的URL不正确，导致预览失败。

### 场景三

使用PdfView组件预览PDF文件时，文档尚未通过初始化流程加载或加载过程中断，导致报错1011301006，提示PDF文档未加载。详见[1011301006 PDF文档未加载](../harmonyos-references/errorcode-pdf.md#section1011301006-pdf文档未加载)。

## 修改建议

### 场景一

应用需要预览在线PDF文档时，可以先将PDF文件下载到本地，然后再通过PdfView组件进行预览，具体可参见[预览PDF文档](../harmonyos-guides/pdf-pdfview-component.md)。

### 场景二

1. 将[domStorageAccess](../harmonyos-references/arkts-basic-components-web-attributes.md#domstorageaccess)的值设置为true，开启文档对象模型存储。
2. 正确使用Web组件的[src](../harmonyos-references/arkts-basic-components-web-i.md#weboptions)参数和[loadUrl()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#loadurl)接口加载PDF文件。大致分为预览加载网络PDF文档、预览加载应用沙箱内PDF文档（需要开启应用中文件系统的访问[fileAccess](../harmonyos-references/arkts-basic-components-web-attributes.md#fileaccess)权限）和预览加载本地PDF文档。详情请参考[使用Web组件的PDF文档预览能力](../harmonyos-guides/web-pdf-preview.md)。

### 场景三

调用[loadDocument()](../harmonyos-references/pdf-arkts-pdfviewmanage.md#loaddocument)重新触发PDF文档加载过程。

## FAQ

Q：Windows(X86)系统模拟器中使用Web组件加载PDF文档，为什么无法显示？

A：模拟器加载PDF文档只支持在MacOS(ARM)版本上运行，Windows(X86)系统的模拟器不支持加载预览。

Q：PdfView和Web组件加载PDF文档有什么区别？

A：PdfView和Web组件都可用于加载PDF文档，但在设计定位、功能侧重和使用场景上存在明显差异。

1. 加载来源与方式：
   * PdfView：只支持加载本地文件（应用沙箱或rawfile目录），不支持直接加载网络PDF。如果需要预览在线文档，必须先下载到本地再加载。
   * Web：支持加载网络PDF、应用沙箱内PDF以及本地rawfile资源，加载方式更灵活。网络PDF直接通过URL加载，本地文件则通过文件路径或$rawfile方式。
2. 功能支持：
   * PdfView：专注于文档预览，提供高亮、搜索关键字、批注、页面布局（单页/连续）、页面适配模式等能力。不支持获取或展示PDF目录（书签），目录功能需借助[pdfService](../harmonyos-references/pdf-arkts-pdfservice.md)实现。
   * Web：通过内置的PDF渲染引擎预览，支持工具栏、侧边导航窗格、缩放、背景色设置等，可通过URL参数（如#toolbar=0&navpanes=0）控制显示状态。支持监听PDF加载成功/失败、滚动到底部等事件。
