---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-faq-34
title: 按需加载场景中，是否支持同时存在多个任务？
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > AppGallery Kit常见问题 > 按需加载场景中，是否支持同时存在多个任务？
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3145115b9029f4d74bb3c794223af0b866809877cdfa6f5961959c1b5fd06cf6
---

不支持，同一应用同时只能存在一个按需分发任务。

**解决措施**

1. fetchModules接口支持多个模块同时下载安装，可以将多个任务合并为一个任务。
2. 通过on接口监听上一个任务的下载安装状态，安装成功后即可发起下一个任务。
