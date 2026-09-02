---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-agent-framework-4
title: 如何使用“真机测试”中的agent_login_session_id字段
breadcrumb: FAQ > AI功能开发 > 计算平台 > 智能体框架（Agent Framework） > 如何使用“真机测试”中的agent_login_session_id字段
category: harmonyos-faqs
scraped_at: 2026-09-02T14:55:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9cf46f5aaa90b6a9c3f3f4cc7d236afc1f314842a81b60b2a2365d74025a1968
---

## 问题现象

小艺开放平台创建智能体后，使用“真机测试”，工作流插件运行时，没有看到系统变量字段agent\_login\_session\_id，如何解决？

## 解决方案

agent\_login\_session\_id是智能体登录后才能使用，不会在开发阶段显示。当智能体正式发布或者真机调试时，且用户在真机上使用时默认生成。
