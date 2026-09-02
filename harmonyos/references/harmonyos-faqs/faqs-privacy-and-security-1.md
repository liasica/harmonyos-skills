---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-privacy-and-security-1
title: 文件隔离后被隔离文件能否通过系统文管或系统UI查看和操作
breadcrumb: FAQ > 应用质量 > 技术质量 > 隐私与安全 > 文件隔离后被隔离文件能否通过系统文管或系统UI查看和操作
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:52+08:00
doc_updated_at: 2026-07-31
content_hash: sha256:0f433dab5e899668f81b47dfee721664028261ba893101217bf757b37a4b7b3e
---

## 问题现象

通过[文件隔离](../harmonyos-guides/enterprisethreatprotection-virusremediation-isolate.md)API隔离文件后，除了通过[文件隔离恢复](../harmonyos-guides/enterprisethreatprotection-virusremediation-restore.md)和[文件隔离查询](../harmonyos-guides/enterprisethreatprotection-virusremediation-query.md)API之外，能否通过系统文管或其他途径查看被隔离的文件？能否通过系统UI来操作被隔离的文件（如隔离删除或恢复）？

## 解决方案

不能通过系统文管或其他途径查看被隔离的文件，只能通过文件隔离相关API处理。从HarmonyOS 7.0开始，可以通过[hidumper](../harmonyos-guides/hidumper.md)查看处置记录。无法通过系统UI来操作被隔离的文件（如隔离删除或恢复）。
