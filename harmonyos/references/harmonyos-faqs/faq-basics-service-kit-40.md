---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-40
title: 如何限制剪贴板数据的复制与粘贴范围
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 如何限制剪贴板数据的复制与粘贴范围
category: harmonyos-faqs
scraped_at: 2026-09-30T07:43:35+08:00
doc_updated_at: 2026-09-29
content_hash: sha256:eccd8959d3783283a060c084ad6d11018ce82adf4de2e33cad0189adfcf53dd3
---

## 问题现象

场景一：为了防止应用内复制的内容被粘贴到应用外部，需要对复制、粘贴行为进行限制，如何实现？

场景二：需要阻断剪贴板拷贝包含敏感数据的文件到外部，如何实现？

## 解决方案

场景一：在HarmonyOS中，剪贴板提供了[setAppShareOptions](../harmonyos-references/js-apis-pasteboard.md#setappshareoptions14)接口用于设置当前应用剪贴板数据的可粘贴范围。

场景二：设置[CopyOptions](../harmonyos-references/ts-appendix-enums.md#copyoptions9)属性为None，表示不支持复制，从而阻断剪贴板拷贝敏感数据到外部。
