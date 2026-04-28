---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/preview-faq-1
title: openPreview打开显示预览失败
breadcrumb: 指南 > 应用服务 > Preview Kit（文件预览服务） > Preview Kit常见问题 > openPreview打开显示预览失败
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d97a70b975016d3999a1cf887b57dc65c385066f6b54fb2a142fb726cda78f11
---

Preview Kit的[openPreview](../harmonyos-references/preview-arkts.md#openpreview)接口在传入文件预览信息时，当前仅支持传入文件的[uri](user-file-uri-intro.md)，不支持传入文件的沙箱路径。

如果调用openPreview接口后，显示预览失败，请检查传入的是否为uri并且检查传入的uri是否存在。
