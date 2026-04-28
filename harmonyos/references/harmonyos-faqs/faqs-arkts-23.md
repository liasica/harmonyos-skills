---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-23
title: pthread创建的线程中如何读取rawfile
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > pthread创建的线程中如何读取rawfile
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:59+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:3adf39fb604b4e5912089add16cc0af94bf6d673c5e3bd4849333ef1c6f1f6e1
---

可在线程安全函数中读取。

1. 在UI主线程中获取并保存资源文件对象。
2. 创建线程安全的函数。
3. 在非UI主线程中调用线程安全函数。
4. 在线程安全函数中，读取rawfile目录下的文件资源。
