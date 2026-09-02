---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-166
title: 应用内字体未跟随系统设置变化
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 应用内字体未跟随系统设置变化
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-07-22
content_hash: sha256:0b5454c0844c3bc250f19b5458d43a11f510da84857d9c82957fa13966a3fced
---

## 问题现象

改变系统字体大小、粗细，应用内字体未同步/部分发生变化。

## 背景知识

* [configuration标签](../harmonyos-guides/app-configuration-file.md#configuration标签)是一个profile文件资源，用于指定描述应用字体大小跟随系统变更的配置文件。
* [fontSize](../harmonyos-references/ts-basic-components-text.md#fontsize)可设置字体大小。
* [ApplicationContext.setFontSizeScale](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextsetfontsizescale13)可设置应用字体大小缩放比例。

## 问题定位

1. 排查应用AppScope/app.json5文件的configuration标签中是否将fontSizeScale属性配置为followSystem。
2. 排查组件是否在fontSize属性中设置了px来定义字体大小。
3. 排查应用是否使用setFontSizeScale设置了应用字体大小缩放比例。设置后，应用字体将不跟随系统变化，不再支持订阅系统字体大小变化。

## 分析结论

* 应用configuration标签中未将fontSizeScale属性配置为followSystem。
* 组件在fontSize属性中设置了px来定义字体大小，导致改变系统字体大小，应用内字体未同步/部分发生变化。
* 应用使用setFontSizeScale设置了应用字体大小缩放比例，导致改变系统字体大小、粗细，应用内字体未同步/部分发生变化。

## 修改建议

* 请参考[configuration标签](../harmonyos-guides/app-configuration-file.md#configuration标签)调整全局配置文件。
* 若需部分组件内容跟随系统字体变化，优先使用fp/vp单位。
* 不使用setFontSizeScale设置应用字体大小缩放比例。
