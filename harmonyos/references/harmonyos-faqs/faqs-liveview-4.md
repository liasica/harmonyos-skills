---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-liveview-4
title: 为什么配置胶囊实况窗icon后，胶囊实况窗中显示应用icon
breadcrumb: FAQ > 应用服务开发 > 实况视图服务（Live View Kit） > 为什么配置胶囊实况窗icon后，胶囊实况窗中显示应用icon
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3273f9514e3596d02db6dcb82ec7748d00c89fbc2b9fbc370df58174b6031df9
---

## 问题现象

在liveViewData.capsule胶囊实况窗的icon参数中，配置指定的icon图片名称，为什么运行时胶囊实况窗中显示为应用的icon。

## 解决方案

liveViewData.capsule中icon参数配置的图片，需保证在工程的“/resources/rawfile”路径下，如果“/resources/rawfile”路径下没有该文件，则会默认显示应用icon。
