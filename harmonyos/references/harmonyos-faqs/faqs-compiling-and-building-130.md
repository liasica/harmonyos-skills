---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-130
title: 如何解决编译报错“ERROR: ArkTS Compiler Error ERROR: /bin/sh: "xxxx/es2abc": Operation not permitted”的问题
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何解决编译报错“ERROR: ArkTS Compiler Error ERROR: /bin/sh: "xxxx/es2abc": Operation not permitted”的问题
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:35+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:8ff14840f9b0a393aa1ea2b30d7979258d26709ed9198409eebcec6b83022e9b
---

**问题现象**

编译报错“ERROR: ArkTS Compiler Error ERROR: /bin/sh: "xxxx/es2abc": Operation not permitted”。

**问题原因**

获取SDK后，Mac的安全设置会为可执行文件添加“来源于网络”的标识（com.apple.quarantine），导致文件无法执行。

**解决方案**

删除可执行文件的com.apple.quarantine标识。

```
1. xattr -d com.apple.quarantine /path/to/es2abc
```
