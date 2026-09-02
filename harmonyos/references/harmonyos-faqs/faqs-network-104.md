---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-104
title: App进入后台，是否会回收网络权限
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > App进入后台，是否会回收网络权限
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:36+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:62de20d1825719b39d7e2607d4c7adb69be0b7935873462942eeb1f7e75de94c
---

## 问题现象

App进入后台，是否会回收网络权限，导致后台的长时任务无法运行？

## 解决方案

在ArkTS中，当应用[进入后台](../harmonyos-references/js-apis-app-ability-uiability.md#onbackground)时，系统会回收部分权限，包括网络权限。此机制旨在优化系统资源分配，确保前台应用能够正常运行。如果应用需要在后台继续进行网络活动，需要申请[长时任务](../harmonyos-guides/continuous-task.md)权限，以避免被系统终止。
