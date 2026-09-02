---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-pdf-2
title: 如何实现PDF的预览缩略图
breadcrumb: FAQ > 应用服务开发 > PDF文档解析服务（PDF Kit） > 如何实现PDF的预览缩略图
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:46+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:8acf4e3f205a88b2feacb636c7ea73337a7864318c0d35c950666eab464da156
---

## 问题现象

如何展示PDF的预览缩略图，场景为仿照华为文件管理选择的样式展示文件缩略图，尝试过使用WEB加载PDF的网络url路径，但没有对应的效果。

## 背景知识

* [pdfViewManager（PDF预览）](../harmonyos-references/pdf-arkts-pdfviewmanage.md)中[getPagePixelMap](../harmonyos-references/pdf-arkts-pdfservice.md#getpagepixelmap)：获取对应PDF页面的缩略图，使用Promise异步回调。

  **参数：**

  | 参数名 | 类型 | 必填 | 说明 |
  | --- | --- | --- | --- |
  | pageIndex | number | 是 | 页面索引，0为起始页。 |
  | isSync | boolean | 否 | 是否同步获取PDF页面的缩略图，true：是，false：否，默认值：false。 |

  **返回值：**

  | 类型 | 说明 |
  | --- | --- |
  | Promise<[image.PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)> | Promise对象，返回image.PixelMap类型。 |

* [pdfService（PDF服务）](../harmonyos-references/pdf-arkts-pdfservice.md)中[getPagePixelMap](../harmonyos-references/pdf-arkts-pdfservice.md#getpagepixelmap)：获取当前页的图片。

  **返回值：**

  | 类型 | 说明 |
  | --- | --- |
  | [image.PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md) | 当前页的image.PixelMap类型。 |

## 解决方案

* 当需要把预览PDF文档的一些页面转化为图片时，调用[pdfViewManager（PDF预览）](../harmonyos-references/pdf-arkts-pdfviewmanage.md)中[getPagePixelMap](../harmonyos-references/pdf-arkts-pdfservice.md#getpagepixelmap)方法实现此功能，参考[PDF缩略图转换为图片](../harmonyos-guides/pdf-pdfview-page2img.md)。
* 当需要PDF文档页面转换为图片，或将页面的指定区域转换为图片时，调用[pdfService（PDF服务）](../harmonyos-references/pdf-arkts-pdfservice.md)中[getPagePixelMap](../harmonyos-references/pdf-arkts-pdfservice.md#getpagepixelmap)，[getAreaPixelMapWithOptions](../harmonyos-references/pdf-arkts-pdfservice.md#getareapixelmapwithoptions)或[getCustomPagePixelMap](../harmonyos-references/pdf-arkts-pdfservice.md#getcustompagepixelmap)方法获取当前页面或者页面区域，这时获取的是[image.PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)图像类型，参考[转换指定页面或指定区域为图片](../harmonyos-guides/pdf-get-img.md)。
