---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-175
title: 网页在HarmonyOS PC上的华为浏览器中无法打开如何处理
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 网页在HarmonyOS PC上的华为浏览器中无法打开如何处理
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:33+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:45875a3810948ab3ee37416f73851ccd52a505fa8f3eade6beee1aec2b48ea67
---

## 问题现象

在HarmonyOS操作系统的PC上使用华为浏览器存在部分网页无法打开的场景，应该如何处理？

## 解决方案

出现该问题的原因是该网页对应的代码没有适配HarmonyOS的UA，解决方案有两种：

* 方案一：打开网页-->点开右上角四个点-->点击菜单栏的浏览器UA标识-->点击电脑版。
* 方案二：修改网站的代码，适配HarmonyOS的UA，具体可[参考文档](../harmonyos-guides/web-default-useragent.md)。
