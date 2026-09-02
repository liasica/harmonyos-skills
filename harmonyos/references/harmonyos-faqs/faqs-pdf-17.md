---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-pdf-17
title: PDF Kit水印相关问题汇总
breadcrumb: FAQ > 应用服务开发 > PDF文档解析服务（PDF Kit） > PDF Kit水印相关问题汇总
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:9d4566c1370a7a979f7d2daad880b7c20f0507b329c36303657ec08a7dafb1b5
---

## 问题现象

1. PDF的水印获取和判断存在只能判断当前打开PDF操作添加的水印吗？还是可以判断PDF文件已有的水印？
2. 文件原先使用pdfService添加的水印可以判断吗？还是只能判断本次打开文件使用pdfService添加的水印？
3. 使用addWatermark接口时，重复调用是叠加还是覆盖原有水印？调用removeWatermark方法是删除文档中全部水印还是单独删除某次添加的水印？
4. 若有多个水印，调用getWatermark是获取哪一个呢？
5. PDF水印添加是单个水印吗还是平铺（重复）呢？是否支持平铺（重复）？
6. PDF添加图片水印时，图片的尺寸和对齐方式是怎么样的？对应ImageFit中的哪个呢？
7. PDF添加水印和背景时，二者是谁在上面谁在下面，与添加顺序和isOnTop参数值有什么关联？
8. 如何给PDF添加水印？

## 背景知识

PDF水印能力由[pdfService能力](../harmonyos-guides/pdf-pdfservice-implements.md)提供，具体参考官网指导：[添加、删除水印](../harmonyos-guides/pdf-add-watermark.md)。对指定页面添加水印，包括文本水印或图片水印。

* 文本水印可以设置字体、大小、旋转，位置等属性。
* 图片水印可以设置缩放、旋转、透明度和位置等属性。

pdfService和PdfView区别参考：[pdfService与PdfView能力比较](../harmonyos-guides/pdf-introduction.md#pdfservice与pdfview能力比较)。

## 解决方案

1. 参考[hasWatermark](../harmonyos-references/pdf-arkts-pdfservice.md#haswatermark)和[getWatermark](../harmonyos-references/pdf-arkts-pdfservice.md#getwatermark)，PDF Kit提供了水印获取和判断接口，主要用于判断pdfService服务添加的水印，不能判断所有来源的水印。
2. 可以判断，文件若原先使用pdfService添加的水印可以被接口识别。
3. [addWatermark](../harmonyos-references/pdf-arkts-pdfservice.md#addwatermark)接口的重复调用会造成水印叠加，调用[removeWatermark](../harmonyos-references/pdf-arkts-pdfservice.md#removewatermark)方法会删除文档中的全部水印，需要删除后重新添加需要保留的水印。
4. 调用getWatermark方法，会获取最新一次添加的水印信息。
5. PDF文档添加水印是单个水印，不会平铺或重复，具体参考addWatermark。
6. PDF添加图片水印时，对应ImageFit中的Fill，即不保持宽高比进行放大缩小，使得图片或视频充满显示边界，对齐方式可以通过[WatermarkInfo](../harmonyos-references/pdf-arkts-pdfservice.md#watermarkinfo).horizontalAlignment及WatermarkInfo.verticalAlignment进行设置。
7. PDF添加水印和背景时，水印始终在背景的上面，与添加顺序无关。水印和背景的isOnTop配置，用来控制是否遮盖文字，isOnTop设置为true显示在文字上面遮盖文字，设置为false显示在文字下面不遮盖文字，与水印和背景层级关系无关。
8. PDF添加水印您可以参考：[PDF文档添加水印](../best-practices/bpta-add-watermark.md#section7418171112138)。
