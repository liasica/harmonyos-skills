---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/reader-setting-other
title: 修改翻页方式、字体大小及行间距
breadcrumb: 指南 > 应用服务 > Reader Kit（阅读服务） > 书籍内容排版 > 修改阅读设置 > 修改翻页方式、字体大小及行间距
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5e0118fc96230a01c02ce6dc4b6b297786c509168e78bcd0130cffadbb216065
---

当应用需要支持修改默认的翻页方式、字体大小、行间距时，开发者可通过[ReaderSetting](../harmonyos-references/reader-read-core.md#readersetting)的flipMode、fontSize、lineHeight属性，实现对翻页方式、字体大小、行间距的实时修改。

## 接口说明

修改翻页方式、字体大小及行间距主要涉及1个接口，具体介绍如下表所示。

| 接口名 | 描述 |
| --- | --- |
| [setPageConfig](../harmonyos-references/reader-read-core.md#setpageconfig)(pageConfig: ReaderSetting): void | 设置或者修改页面排版属性。 |

## 开发准备

在修改翻页方式、字体大小及行间距之前，请先确保已经“[构建阅读器](reader-read-page.md)”。

## 开发步骤

1. 修改翻页方式。

   ```
   1. this.readerSetting.flipMode = '1'; // 0代表仿真翻页，1代表横滑翻页
   ```
2. 修改字体大小。

   ```
   1. this.readerSetting.fontSize = 20;
   ```
3. 修改行间距。

   ```
   1. this.readerSetting.lineHeight = 2;
   ```
4. 调用ReaderComponentController组件控制器的setPageConfig接口，重新渲染界面。

   ```
   1. this.readerComponentController.setPageConfig(this.readerSetting);
   ```
