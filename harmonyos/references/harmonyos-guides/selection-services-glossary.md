---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/selection-services-glossary
title: 划词服务术语
breadcrumb: 指南 > 系统 > 基础功能 > Basic Services Kit（基础服务） > 划词服务 > 划词服务术语
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:36+08:00
doc_updated_at: 2026-06-16
content_hash: sha256:7da71c7a157fdf0c38b2e13e1d2e711de7e72b34655c8e752c91acf844bd5d73
---

## S

### Selected Application；被划词应用

用户选中文本时所处的源应用。划词服务通过系统复制机制从中提取选中文本，无需该应用额外适配；不支持系统级复制的应用（如受控WebView、沙箱环境应用）则无法配合该功能。

### Selection Application；划词应用

实现了划词扩展能力的应用。该类应用被划词服务拉起后，可监听划词完成事件以获取用户选中文本，进而执行翻译、摘要、扩写等后续业务逻辑。

### Selection ExtensionAbility；划词扩展能力

一种ExtensionAbility组件类型。它允许应用在用户选词后获取选中文本，并管理划词面板的生命周期，从而方便实现翻译、摘要、扩写等业务逻辑。
