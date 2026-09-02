---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-intents-kit-3
title: 意图框架意图共享功能中insightIntent.shareIntent与意图共享接口的区别
breadcrumb: FAQ > AI功能开发 > 机器学习 > 意图框架服务（Intents Kit） > 意图框架意图共享功能中insightIntent.shareIntent与意图共享接口的区别
category: harmonyos-faqs
scraped_at: 2026-09-02T14:55:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:66c3f88553462a180f838dac7f0f3bc5c5052ee0b0bece696f43aed821d631ee
---

## 问题现象

HarmonyOS意图共享功能，什么时候用自带的API:insightIntent.shareIntent，什么时候用意图共享接口？二者有什么区别？

## 解决方案

功能范围：insightIntent.shareIntent是一个系统级的API，用于应用与系统之间的数据共享，而意图共享接口作为云侧接口更侧重于应用或服务内部的数据交换。

使用目的：insightIntent.shareIntent主要用于利用系统的智能推荐和调度能力，提高应用的可见性和用户体验；而意图共享接口通过云侧共享数据，简化了应用端侧内部的复杂性，提高开发效率。
