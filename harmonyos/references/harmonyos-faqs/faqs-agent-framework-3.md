---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-agent-framework-3
title: 应用内呼出智能体提示“智能体未授权给该应用”
breadcrumb: FAQ > AI功能开发 > 计算平台 > 智能体框架（Agent Framework） > 应用内呼出智能体提示“智能体未授权给该应用”
category: harmonyos-faqs
scraped_at: 2026-09-02T14:55:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:596c2e5938264e6ddc1a6508118b713a99b0e30a9f5c0695674ea4610c9e0a18
---

## 问题现象

应用内通过FunctionComponent拉起智能体，智能体测试已经跑通，但是在应用内调用显示未授权，提示“智能体未授权给该应用”？

## 解决方案

* 确保应用接入的智能体AgentID准确，并且该智能体已完成上架。
* 在智能体中配置了关联的应用信息，确保关联的应用包名、appId等信息一致并且在配置中开启关联应用。参考文档：[关联应用](../service/related-applications-0000002437785706.md)。
