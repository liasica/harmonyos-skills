---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-409
title: Navigation如何设置默认页
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Navigation如何设置默认页
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:47+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:3979120e8130b5b32268b92f45c7d2edf20a1413616afc2aa5a1398251c3cbdf
---

**问题描述**

初始横屏时，Navigation会分栏显示，由于此时没有页面在路由栈中，分栏右侧无内容显示，如何为右侧增加一个默认页。

**解决措施**

开发者可以通过[onNavigationModeChange](../harmonyos-references/ts-basic-components-navigation.md#onnavigationmodechange11)方法对Navigation的模式进行监听，并手动控制是否加载默认页：

* 如果Navigation切为分栏模式显示，栈中没有页面，则push默认占位页。
* 如果页面切换为单栏显示且栈中只有占位页，则将占位页删除，若分栏模式时栈中已有页面，则保持现有页面不变。

从API20开始，开发者可通过设置在Navigation组件的[splitPlaceholder](../harmonyos-references/ts-basic-components-navigation.md#splitplaceholder20)属性，来设置默认占位页。
