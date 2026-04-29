---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-faq-3
title: 分享时提示“您选择的文件不支持分享”
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > Share Kit常见问题 > 分享时提示“您选择的文件不支持分享”
category: harmonyos-guides
scraped_at: 2026-04-29T13:40:43+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:6ca6848e7c29115a73822ef3b74e631b84c589c0ad66eb468578674721fdabdd
---

**现象描述：**

预览区内容无法正常显示，点击分享方式区或操作区均提示“您选择的文件不支持分享”。

**可能原因：**

Share Kit无法访问应用提供的文件URI路径，可能的原因：

1. 文件URI格式错误。
2. 文件URI路径不存在或无权限访问。

**处理步骤：**

1. 排查文件URI格式是否正确，文件URI的格式请参考：[文件URI规范](share-app-file.md#文件uri规范)。
2. 排查分享过程中，文件是否真实存在并且拥有文件的访问权限，可使用[fs.stat](../harmonyos-references/js-apis-file-fs.md#fileiostat)尝试访问文件，并通过比较文件创建时间和分享发起时间确认文件存在。
