---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-25
title: 如何解决调用两次fs接口写文件，但第二次写入的内容未完全覆盖第一次写入的内容的问题
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 如何解决调用两次fs接口写文件，但第二次写入的内容未完全覆盖第一次写入的内容的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:30+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:26a2bbb3802d18a956cda2a85a888139a7773f5e44dbedd0ef526f89364aeb93
---

清空文件时必须要设置OpenMode.TRUNC，默认覆盖模式(WRITE\_ONLY)只是覆盖不会清除，TRUNC模式会先清空文件内容。参考代码如下：

```typescript
fileIo.openSync(dst, fileIo.OpenMode.WRITE_ONLY | fileIo.OpenMode.TRUNC | fileIo.OpenMode.CREATE);
```
