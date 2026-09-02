---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-basic-services-kit-new-00002
title: 基于系统选择服务实现划词功能
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 基于系统选择服务实现划词功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-07-22
content_hash: sha256:ccaf68ac20dcf4d86e0505f55ed3684045722ccb6ee556312e8ad86201603206
---

## 问题现象

应用需要实现划词功能（用鼠标选择文字的界面），当前未实现该功能影响使用翻译的效率。

## 背景知识

划词功能可以通过系统提供的Selection Services（选择服务）来实现，开发者可以通过该服务在文本被选中时展示自定义菜单并处理选中的文本。

## 解决方案

接入Selection Services实现划词功能：

参考[Selection Services应用开发指南](../harmonyos-guides/selection-services-application-guide.md)进行接入，配置自定义的选择菜单，并在回调中获取用户选中的文本内容，从而实现划词翻译功能。
