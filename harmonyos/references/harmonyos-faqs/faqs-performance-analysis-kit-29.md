---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-29
title: 如何查看ArkCompiler出现Error日志时，具体的异常调用栈信息
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何查看ArkCompiler出现Error日志时，具体的异常调用栈信息
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:17+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:6c3f407fa476698278685e397852098ac59a88ea784f761418fb05236c7f2177
---

Native抛异常，如需查看backtrace，运行以下命令。

打开异常栈：

```
1. hdc shell param set persist.ark.properties 0x125c
2. hdc shell reboot
```

恢复默认值：

```
1. hdc shell param set persist.ark.properties 0x105c
2. hdc shell reboot
```
