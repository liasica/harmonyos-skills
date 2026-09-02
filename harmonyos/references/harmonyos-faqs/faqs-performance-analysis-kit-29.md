---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-29
title: 如何查看ArkCompiler出现Error日志时，具体的异常调用栈信息
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何查看ArkCompiler出现Error日志时，具体的异常调用栈信息
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:145650581f3b54bfa709299ae978e38e3223733662e4860507deee0e0dc2f870
---

Native抛异常，如需查看backtrace，运行以下命令。

打开异常栈：

```powershell
hdc shell param set persist.ark.properties 0x125c 
hdc shell reboot
```

恢复默认值：

```powershell
hdc shell param set persist.ark.properties 0x105c 
hdc shell reboot
```
