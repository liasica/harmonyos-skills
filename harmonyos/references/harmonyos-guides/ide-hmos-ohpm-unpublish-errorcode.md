---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-ohpm-unpublish-errorcode
title: ohpm unpublish错误码
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 命令行工具 > 三方依赖管理工具（ohpm） > 错误码 > ohpm unpublish错误码
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:39+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:5d6b960c3f8d99c4a5f574ef56c4542eadda47bea070f6fe889ddc5976b34429
---

## 00610001 执行下架命令时未指定版本号

**错误信息**

Delete All Version Pkg Not Force.

**错误描述**

未强制下架不同版本的包。

**可能原因**

执行ohpm unpublish pkg命令时，未指定三方库版本号，且未配置强制下架参数--force。

**处理步骤**

未指定三方库版本时，需添加--force参数，强制下架该库所有版本。
