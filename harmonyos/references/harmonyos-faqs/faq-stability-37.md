---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-37
title: 点击桌面图标跳转到设置界面
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 点击桌面图标跳转到设置界面
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5ba2778643ba0c92f72c8012174fb1268e4ddc45d39bc800a21f83e75d12ea51
---

## 问题现象

点击桌面应用图标，软件打不开，默认跳转到该应用的应用详情页。

## 背景知识

[skills标签](../harmonyos-guides/module-configuration-file.md#skills标签)：该标签标识UIAbility组件或者ExtensionAbility组件能够接收的[Want](../harmonyos-guides/want-overview.md)的特征。

配置规则：

* 对于Entry类型的HAP，应用可以配置多个具有入口能力的skills标签（即配置了ohos.want.action.home和entity.system.home）。
* 对于Feature类型的HAP，只有应用可以配置具有入口能力的skills标签，服务不允许配置。

## 问题定位

检查模块中module.json5文件中是否配置skills标签，标签下的entities是否配置或配置内容是否包括"entity.system.home"，并且actions是否配置或配置内容是否包括"ohos.want.action.home"。

## 分析结论

skills标签下的entities未配置或配置内容不包括"entity.system.home"，并且actions未配置或配置内容不包括"ohos.want.action.home"导致。

## 修改建议

在模块中module.json5中skills标签配置如下内容：将entities属性配置为"entity.system.home"，并将actions属性配置为"ohos.want.action.home"。
