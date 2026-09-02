---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-reader-3
title: Reader Kit（阅读服务）支持的能力及使用注意事项
breadcrumb: FAQ > 应用服务开发 > 电子书阅读服务（Reader Kit） > Reader Kit（阅读服务）支持的能力及使用注意事项
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:25+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:fe92770f1d1c10f7eff2904567c0438f9ac00376d75e693b3bcd22c3577bb134
---

## 问题现象

Reader Kit（阅读服务）支持什么能力？使用时有哪些注意事项？

## 背景知识

[Reader Kit（阅读服务）](../harmonyos-guides/reader-kit-guide.md)为开发者提供多种格式电子书的解析、排版、阅读交互能力，开发者可以借助Reader Kit的能力和组件快速构建书籍阅读能力。

| [约束和限制](../harmonyos-guides/reader-introduction.md#约束和限制) | 说明 |
| --- | --- |
| [设备限制](../harmonyos-guides/reader-introduction.md#设备限制) | Reader Kit仅适用于HarmonyOS NEXT 5.0.4及以上版本的Phone、PC/2in1、Tablet设备，暂不支持模拟器使用。 |
| [支持的国家/地区](../harmonyos-guides/reader-introduction.md#支持的国家地区) | Reader Kit当前仅在中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）提供服务。 |

## 解决方案

1. 支持的能力：Reader Kit（阅读服务）支持[书籍内容解析](../harmonyos-guides/reader-parser.md)、[书籍内容排版](../harmonyos-guides/reader-content.md)、[书籍内容交互](../harmonyos-guides/reader-interaction.md)。

   | 能力 | 说明 |
   | --- | --- |
   | 书籍内容解析 | [获取书籍信息](../harmonyos-guides/reader-book-info.md)：当应用需要导入本地书籍到书架时，开发者可通过[DocumentViewPicker](../harmonyos-references/js-apis-file-picker.md#documentviewpicker)先将书籍文件导入到[应用沙箱目录](../harmonyos-guides/app-sandbox-directory.md)。然后利用解析能力获取书籍信息，用于书架中书封，书名，作者等信息的展示。  [获取目录列表](../harmonyos-guides/reader-catalog-list.md)：当应用需要展示书籍目录列表时，开发者可通过解析能力获取目录节点列表，实现目录列表中章节名称按顺序、层级的展示。当用户点击目录节点时，开发者也需要获取目录位置及资源信息，用于跳转到指定位置。 |
   | 书籍内容排版 | [构建阅读器](../harmonyos-guides/reader-read-page.md)：Reader Kit提供的阅读页组件ReadPageComponent，支持对标准的txt和富文本内容（html+css）按仿真和横滑方式进行分页排版的能力、支持翻页阅读过程中所需要的进度和行为感知能力。利用ReadPageComponent，开发者可快速实现书籍阅读的能力。  [修改阅读设置](../harmonyos-guides/reader-setting.md)：开发者可设置[自定义字体](../harmonyos-guides/reader-setting-font.md)、[自定义页面背景](../harmonyos-guides/reader-setting-background.md)，[修改翻页方式、字体大小及行间距](../harmonyos-guides/reader-setting-other.md)，[适配深、浅色模式](../harmonyos-guides/reader-setting-color-mode.md)，[监听文本缩放因子变化](../harmonyos-guides/reader-setting-scaled-density.md)。 |
   | 书籍内容交互 | [手动触发翻页](../harmonyos-guides/reader-flip-page.md)：Reader Kit的交互能力已经集成了手指点击和触摸滑动翻页，如果开发者需要增加其它翻页场景时（如：耳机播控翻页），可使用手动翻页接口实现自定义翻页场景。  [阅读进度通知](../harmonyos-guides/reader-progress.md)：当页面展示时，会通过页面展示回调接口返回页面渲染信息。页面渲染信息提供用于阅读进度跳转的domPos及resourceIndex属性，开发者可将属性缓存到数据库当中，用于阅读进度的恢复。 |
2. 使用Reader Kit（阅读服务）的[ArkTS API](../harmonyos-references/reader-arkts.md)和[ReadPageComponent（阅读页组件）](../harmonyos-references/reader-api-readpagecomponent.md)开发阅读相关的应用时：

   **说明** 

   * 书籍解析支持的文件类型：txt、epub、mobi、azw、azw3。
   * 在线的文件流：Reader Kit只支持本地文件的书籍，不支持在线的文件流。
   * 文件的存放目录：不同的书籍文件需要存放在应用沙箱下的不同目录。
   * 自定义字体：设置[ReaderSetting](../harmonyos-references/reader-read-core.md#readersetting)的fontPath属性为空时，使用的是系统的默认字体，而不是系统的当前字体。
   * ReadPageComponent（阅读页组件）顶部和底部留白：阅读页组件顶部和底部预留了页眉页脚，呈现效果为顶部和底部有空白。
   * 自定义页面背景：通过ReaderSetting的themeColor属性设置主题背景色时，需要注意背景色的值有如下限制：对于16进制颜色值，只支持6位颜色值，不支持透明度；对于rgba颜色值，透明度的值只支持1。
   * [init](../harmonyos-references/reader-read-core.md#init)初始化接口：在集成[ReaderComponentController](../harmonyos-references/reader-read-core.md#readercomponentcontroller)时，初始化接口一定要优先于controller的其他接口之前执行。
