---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-28
title: 对图片进行“图片转格式”操作后，图片预览图有比较长时间的空白
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 对图片进行“图片转格式”操作后，图片预览图有比较长时间的空白
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:42+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:dfba363d2b4ff17327367d7d3654ae62f80346417c053fedf43b759dfcb8a065
---

## 问题现象

应用对图片进行“图片转格式”操作后，图片预览空白，没有展示图片信息。等待比较长的一段时间后图片才展现。点击“下载”无响应。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/cFHgvaXNSvSnufr-ve7Kag/zh-cn_image_0000002628392598.png "点击放大")

## 背景知识

* [Image](../harmonyos-references/ts-basic-components-image.md)为图片组件，常用于在应用中显示图片。Image支持加载PixelMap、ResourceStr和DrawableDescriptor类型的数据源，支持PNG、JPG、JPEG、BMP、SVG、WebP、GIF和HEIF类型的图片格式，不支持APNG和SVGA格式。
* [图片解码](../harmonyos-guides/image-decoding-arts.md)：指将所支持格式的图片文件解码成PixelMap，以便在应用或系统中进行图片显示或图片处理。当前支持解码的图片格式包括JPEG、PNG、GIF、RAW、WebP、BMP、HEIC（API12起）。
* [图片编码](../harmonyos-guides/image-encoding-arts.md)：指将PixelMap编码成不同格式的图片文件，用于后续处理，如保存、传输等。当前支持编码的图片格式包括JPEG、WebP、PNG、HEIC（API12起）、GIF（API18起，需要使用PackToDataFromPixelmapSequence或PackToFileFromPixelmapSequence接口进行编码）。

## 问题定位

复现场景发现，应用的图片转换，整个转换过程在服务端执行，需要上传和下载。等待一段时间下载到图片之后，是可以获取到图片的预览图，图片通过Image组件展现，点击“下载”无响应。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/Jl8IuNhrSZaYA9a0JDqHRg/zh-cn_image_0000002658791865.png "点击放大")

通过分析hilog日志，得到如下关键信息，可知图片通过http请求获取，返回数据超过最大限制或curl返回码错误。

```txt
[http_exec.cpp:1291] response data exceeds the maximum limit
[http_exec.cpp:312] CURLcode result 23
```

## 分析结论

图片上传到服务端进行转换，下载到客户端进行展现和保存。请求服务端超过了图片最大限制或请求报错，导致图片获取失败。

## 修改建议

应用可通过HarmonyOS Image Kit图片处理服务，对要转换的图片进行[图片解码](../harmonyos-guides/image-decoding-arts.md)转化为PixelMap对象，再将PixelMap对象进行[图片编码](../harmonyos-guides/image-encoding-arts.md)保存为想要的图片格式，从而达到图片转换的目的。可在客户端处理，减少服务端网络和计算压力，增强应用体验。
