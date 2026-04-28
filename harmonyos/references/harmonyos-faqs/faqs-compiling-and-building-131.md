---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-131
title: 如何解决编译报错“Cannot add xxxx items to index”的问题
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何解决编译报错“Cannot add xxxx items to index”的问题
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:35+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:0d532f7be5210aabf2d05a54405a7d5fd44dd208b9d4e6ac85303f5d71788d07
---

**问题现象**

编译报错“Cannot add xxxx items to index”。

**问题原因**

被编译文件中某函数内部有大量object literal, array literal和string，导致item的数量超过了上限（65536）。

**解决方案**

排查相关文件，将存在上述原因的函数进行拆分。
