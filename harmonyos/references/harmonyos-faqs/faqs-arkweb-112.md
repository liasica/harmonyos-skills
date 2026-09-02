---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-112
title: Web页面如何适配深色模式
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web页面如何适配深色模式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:fe7b11974a5571a77478c8ea9eed8d27843a7215a896901a34c75ee82f63c7cd
---

## 问题现象

设备开启深色模式时，应用的Web页面没有适配，页面背景及字体颜色均毫无变化。

## 背景知识

[Web深色模式适配](../harmonyos-guides/web-set-dark-mode.md)：ArkWeb提供灵活控制Web组件深色模式的能力，支持独立于系统进行设置。此外，ArkWeb还可以强制不同网页适配深色模式，以兼容不同的系统主题。

## 问题定位

1. 检查Web是否开启深色模式。Web深色模式接口[darkMode()](../harmonyos-references/arkts-basic-components-web-attributes.md#darkmode9)默认状态为关闭，需显式声明为[WebDarkMode.On](../harmonyos-references/arkts-basic-components-web-e.md#webdarkmode9)或[WebDarkMode.Auto](../harmonyos-references/arkts-basic-components-web-e.md#webdarkmode9)，才能开启深色模式。
2. Web已开启深色模式时，检查网页是否定义深色样式。网页的深色样式需要网页开发者适配。如果未定义深色样式，即使Web开启深色模式，网页样式也会保持不变。若需强制适配，可以使用[forceDarkAccess()](../harmonyos-references/arkts-basic-components-web-attributes.md#forcedarkaccess9)接口开启强制深色模式。
3. Web已开启强制深色模式时，检查网页是否声明支持深色配色方案。通过color-scheme声明支持深色配色方案的网页，在强制深色模式下色值不会被Web转换。同时，如果网页内元素自定义了颜色样式，则不会被color-scheme影响。因此表现为网页样式未切换为深色样式。此时，需要网页开发者进行适配修改。

## 分析结论

应用Web页面未显式声明为WebDarkMode.On或WebDarkMode.Auto，或者未通过forceDarkAccess()接口开启强制深色模式。且Web页面未使用color-scheme的CSS属性和prefers-color-scheme媒体查询属性进行深色模式适配。

## 修改建议

Web页面适配深色模式，官方提供了深色模式/强制深色模式/color-scheme三种方法，具体三种方法的区别及使用方法可参考：[Web深色模式适配](../harmonyos-guides/web-set-dark-mode.md)。
