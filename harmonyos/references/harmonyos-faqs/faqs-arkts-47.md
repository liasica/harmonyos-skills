---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-47
title: 是否可以在TaskPool中动态加载模块（HAR、HSP、SO）
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > 是否可以在TaskPool中动态加载模块（HAR、HSP、SO）
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:25+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:e1c01df90dc79e26b920763c2dd4a5f0a79d397b4a2987797a56d2b961a453a6
---

TaskPool的动态加载能力与主线程相同。然而，TaskPool线程加载后，由于模块化线程隔离，无法被主线程复用。
