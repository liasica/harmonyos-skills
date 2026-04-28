---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-25
title: 如何解决调用两次fileIo接口写文件，但第二次写入的内容未完全覆盖第一次写入的内容的问题
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 如何解决调用两次fileIo接口写文件，但第二次写入的内容未完全覆盖第一次写入的内容的问题
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:27+08:00
doc_updated_at: 2026-04-21
content_hash: sha256:152bc7c37db35f3a64a7bae757e4efc1ab9ff05ed4a2ecbed616baee1a2df892
---

清空文件时必须要设置OpenMode.TRUNC，默认覆盖模式(WRITE\_ONLY)只是覆盖不会清除，TRUNC模式会先清空文件内容。参考代码如下：

```
1. fileIo.openSync(dst, fileIo.OpenMode.WRITE_ONLY | fileIo.OpenMode.TRUNC | fileIo.OpenMode.CREATE);
```
