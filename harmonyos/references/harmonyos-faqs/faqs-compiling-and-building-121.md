---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-121
title: 用户目录下没有.npmrc文件
breadcrumb: FAQ > DevEco Studio > 编译构建 > 用户目录下没有.npmrc文件
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:33+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:c199cbc41af00e8b648419836d44b8ceef6d78d1b588b89d15aeaeaec7acce75
---

**问题现象**

新建项目时出现错误：Error: The hvigor depends on the npmrc file. Configure the npmrc file first. 请先配置npmrc文件。

**问题原因**

用户目录下不存在 .npmrc 文件。

**解决措施**

在用户目录下创建.npmrc文件，配置以下信息：

```
1. registry=https://repo.huaweicloud.com/repository/npm/
2. @ohos:registry=https://repo.harmonyos.com/npm/
```
