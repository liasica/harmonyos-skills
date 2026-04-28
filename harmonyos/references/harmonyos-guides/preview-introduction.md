---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/preview-introduction
title: Preview Kit简介
breadcrumb: 指南 > 应用服务 > Preview Kit（文件预览服务） > Preview Kit简介
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:45ba679d4aad8f78aca8a2fd9348220e9e81f4a995c7ebe0076bada9edfcbd1e
---

Preview Kit（文件预览服务）为应用提供便捷的文件快速预览和文件打开加速能力。

* 应用可以通过Preview Kit提供的预览API，快速启动预览界面，实现对各类文件的预览。

  通过Preview Kit，用户可以对用户文件（包括图片、视频、音频、文本、html等）进行内容查看。同时用户还可以通过点击右上角的“使用其他应用打开”的按钮跳转到具体的应用进行展示，从而进行其他操作，如图片的旋转、放大等。

  目前，Preview Kit实现Office的预览能力，主要是借助WPS的能力实现的，预览界面会有WPS提供的技术支持，并展示WPS的入口，统一按照文件预览的风格进行页面布局。
* Preview Kit还提供了文件打开加速功能，通常用户打开一个较大文件通常要花费几秒甚至十几秒，文件打开加速服务提供了预加载机制提前加载文件，缩短用户打开文件时间，给用户提供流畅顺滑的爽感体验。详见[文件打开加速功能](preview-openfileboost.md)。
* Preview Kit还提供了通用文件缓存加速功能，通常用户打开或浏览一个文件时，应用需要对文件中的图片、视频等内容进行解码，花费较长时间，通用文件缓存加速功能提供了缓存机制将解码数据缓存到磁盘中，后续用户再次打开或浏览该文件，应用无需执行解码流程，可直接从磁盘中获取缓存的解码数据，省去耗时的解码时间，缩短用户打开或浏览文件的时间，给用户提供极致流畅的体验。详见[通用文件缓存加速功能](preview-filecacheboost.md)。

## 文件预览场景介绍

Preview Kit能够对图片、视频、音频、文本、html进行预览查看，满足绝大多数办公开发的需求，包括：

* 预览展示：呈现文件的基本内容，如文本、图片等，支持选中多文件，在预览列表切换显示。
* 文件分享：将文件以分享的形式传给另一个软件。
* 使用其他软件打开：使用预览打开时，会获取到该文件类型的默认打开软件，然后点击“使用其他应用打开”进行跳转。
* 图片翻转放大：在非2in1设备时，预览能够对图片进行旋转放大等处理。

## 文件打开加速场景介绍

文档类应用接入后，文件打开加速服务会根据算法推荐用户可能打开的文件信息给应用，应用可提前在后台对文件进行预加载， 一旦用户打开已经预加载的文件，则整个打开过程可以在很短时间内完成。给用户提供顺滑流畅的文件打开体验。

## 通用文件缓存加速场景介绍

通过文件缓存服务，应用在打开或浏览文件时，文件缓存服务会创建一个以key为索引名的缓存文件，用于存放缓存数据，系统会对应用所有的缓存做持久化管理。应用再次打开或浏览文件时，需先用key值查找是否有对应的缓存，如果命中，则直接从磁盘中读取缓存数据，无需重复计算解码，大大减少了重复解码时间，给用户提供顺滑流畅的文件打开及浏览体验。

## 约束与限制

### 支持的国家和地区

当前Preview Kit仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

### 支持的设备

文件预览功能支持华为Phone、Tablet和2in1，文件打开加速功能仅支持2in1设备。

## 模拟器支持的情况

本Kit支持模拟器，但与真机存在部分能力差异，具体差异如下。

* 通用差异：请参见“[模拟器与真机的差异](ide-emulator-specification.md#section1227613205203)”。
* 模拟器的文件预览功能不支持.pdf/.pptx/.xlsx/.docx等文档类文件格式的预览。
* 模拟器不支持文件打开加速功能和通用文件缓存加速功能。

## 文件预览支持的文件类型

Preview Kit支持图片、视频、音频、文本、html进行查看，表中提供的为常见的部分格式类型，实际支持情况可采用[canPreview](../harmonyos-references/preview-arkts.md#canpreview)接口进行判断文件是否支持预览。

| 类型 | 文件后缀 | mimeType类型 |
| --- | --- | --- |
| 文本 | txt、cpp、c、h、java、xhtml、xml | text/plain、text/x-c++src、text/x-csrc、text/x-chdr、text/x-java、application/xhtml+xml、text/xml |
| 网页 | html、htm | text/html |
| 图片 | jpg、png、gif、webp、bmp、svg | image/jpeg、image/png、image/gif、image/webp、image/bmp、image/svg+xml |
| 音频 | m4a、aac、mp3、ogg、wav | audio/mp4a-latm、audio/aac、audio/mpeg、audio/ogg、audio/x-wav |
| 视频 | mp4、mkv、ts | video/mp4、video/x-matroska、video/mp2ts |
| 文件夹 | 无 | 无 |
| 文档 | pdf | application/pdf |
| Office文档 | doc、docx、xls、xlsx、ppt、pptx、csv、ofd | application/msword、application/vnd.openxmlformats-officedocument.wordprocessingml.document、application/vnd.ms-excel、application/vnd.openxmlformats-officedocument.spreadsheetml.sheet、application/vnd.ms-powerpoint、application/vnd.openxmlformats-officedocument.presentationml.presentation、text/csv、general.ofd |

## 文件打开加速支持的文件类型

后缀为doc、docx、xls、xlsx、ppt、pptx的文件。

## 文件预览基本概念

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/cGqZeAneRLqGoGPJKW8wtw/zh-cn_image_0000002583439151.png?HW-CC-KV=V1&HW-CC-Date=20260427T235025Z&HW-CC-Expire=86400&HW-CC-Sign=A299B30F0972105B7A95DD8AEFD431BA8CCC6FCEC86614F46CB1905CBF60640F)

* 模态窗：和父窗口绑定，模态窗存在时父窗口不可移动，不可操作，模态窗永远置于父窗口前面。
* 应用窗：应用窗口，可以通过AMS启动。
* AMS：AbilityManagerService，用于协调各Ability运行关系、及对生命周期进行调度的系统服务。

## 通用文件缓存加速基本概念

* key

在通用文件缓存加速服务中，Key值是每个缓存文件对象的唯一标识符，用于管理缓存数据。Key值可以通过哈希算法计算文件内容得到，例如可以将一张图片进行SHA-256哈希运算，得到的哈希值作为该图片缓存对象的Key值。
