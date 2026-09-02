---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-121
title: 用户目录下没有npmrc文件
breadcrumb: FAQ > DevEco Studio > 编译构建 > 用户目录下没有npmrc文件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5df9882c66182f42c3646e6bb0d6462df3a308b891fdb1c3941e92cd7be1940f
---

**问题现象**

新建项目时出现错误：Error: The hvigor depends on the npmrc file. Configure the npmrc file first. 请先配置npmrc文件。

**问题原因**

用户目录下不存在 .npmrc 文件。

**解决措施**

在用户目录下创建.npmrc文件，配置以下信息：

```powershell
registry=https://repo.huaweicloud.com/repository/npm/
@ohos:registry=https://repo.harmonyos.com/npm/
```
