---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-21
title: 工程中存在多处-Wunused-command-line-argument告警，影响查看有效日志
breadcrumb: FAQ > DevEco Studio > 工程管理 > 工程中存在多处-Wunused-command-line-argument告警，影响查看有效日志
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:00+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:4c2f2617a8a6da739383c366a33eeadb900f939447ad803344aca4bcec5e2d7b
---

**问题描述**

```
1. clang: warning: argument unused during compilation: ‘–gcc-toolchain=C:/Users/username/AppData/Local/Huawei/Sdk/openharmony/9/native/llvm’ [-Wunused-command-line-argument]；
```

在API 9版本的clang编译器中，编译每个文件时都会出现warning。当前可以通过添加-Wno-unused-command-line-argument选项来屏蔽这些警告，但工程较多时，是否有一种方法可以全局屏蔽此警告？

**解决方案**

根据 clang 提示，这个告警是由-Werror和-Wunused-command-line-argument告警选项触发的。可能是代码中存在不支持的变量语法。可以通过配置-Wno-unused-command-line-argument关闭该检查项，或者将 SDK 升级到 API 11。
