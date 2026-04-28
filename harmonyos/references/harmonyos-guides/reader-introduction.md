---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/reader-introduction
title: Reader Kit简介
breadcrumb: 指南 > 应用服务 > Reader Kit（阅读服务） > Reader Kit简介
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6ae3542dd5eb0fd97d0b25d8ebef7876d794f5d55ef3d18aa328286f02bd9bcf
---

Reader Kit（阅读服务）为开发者提供多种格式电子书的解析、排版、阅读交互能力，开发者可以借助Reader Kit的能力和组件快速构建书籍阅读能力。

## 能力范围

Reader Kit提供的能力如下：

* 多种格式书籍的解析能力：提供对txt、epub、mobi、azw、azw3格式书籍进行解析的能力，可获取书籍中的书名、作者、书封、目录以及目录对应的正文内容。
* txt、富文本内容排版能力：支持对标准的txt、富文本内容（html+css）按仿真和横滑方式进行分页排版，并提供排版快照和排版信息。
* 阅读页组件（ReadPageComponent）：支持对书籍排版内容的显示、多种翻页交互和翻页动效，以及翻页阅读过程中阅读器所需要的进度、行为感知能力。

## 亮点/特征

* 支持多种电子书籍格式解析，提供标准规范的书籍信息和内容数据。
* 对富文本内容（html+css）的排版符合W3C标准规范，且对排版过程做了高效的算法优化，提高了排版速度和效率。
* 对内容进行展示时，除了支持系统字体之外，还支持扩展自定义字体，满足用户的个性化需求。
* 阅读页组件（ReadPageComponent）提供常用的阅读交互能力，支持多种翻页方式，采用OpenGL（C/C++）绘制翻页动效，阅读过程更丝滑，更流畅。

## 基本概念

* ReadPageComponent

  Reader Kit封装的阅读页UI组件[ReadPageComponent](../harmonyos-references/reader-api-readpagecomponent.md)（ets），支持对书籍排版内容的显示、多种翻页交互和翻页动效，以及翻页阅读过程中阅读器所需要的进度、行为感知能力。
* BookParser

  电子书解析引擎[bookParser](../harmonyos-references/reader-book-parser.md)，支持txt、epub、mobi、azw、azw3格式书籍文件的解析。
* spine(书脊)

  书的背脊；平装书或精装书封面和封底的联结处。一般印有书名、作者名、出版单位名等。在Reader Kit中，spine(书脊)定义了书籍内容的阅读顺序，每一个[SpineItem](../harmonyos-references/reader-book-parser.md#spineitem)表示一个可阅读的内容节点，标识着可阅读的一个内容资源。

## 约束和限制

* 在书籍处理过程中，Reader Kit只支持有本地文件的书籍，不支持在线的文件流，且不同的书籍文件需要存放在应用沙箱下的不同目录。
* 在书籍处理过程中，Reader Kit不提供对书籍的DRM保护能力。
* 解析能力只支持对txt、epub、mobi、azw、azw3标准格式的书籍文件进行解析，对于非标准格式的书籍在解析时可能会抛出异常，开发者需要捕获和处理。
* 排版引擎及交互能力需要配套Reader Kit的阅读页组件（ReadPageComponent）使用。

### 设备限制

Reader Kit仅适用于HarmonyOS NEXT 5.0.4及以上版本的Phone、PC/2in1、Tablet设备。

### 支持的国家/地区

Reader Kit当前仅在中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）提供服务。

## 模拟器支持情况

本Kit暂不支持模拟器。

## 示例代码

Reader Kit开发指南涉及到的示例代码均为片段，全量示例代码请参考：[CodeLabs](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_NEXT-ReaderKit)或[SampleCode](https://gitcode.com/HarmonyOS_Samples/readerkit_samplecode_arkts)。CodeLabs和SampleCode包括了导入本地书籍、构建阅读器、构建目录列表、修改阅读设置等场景的完整实践示例，可帮助开发者更好地使用Reader Kit API。
