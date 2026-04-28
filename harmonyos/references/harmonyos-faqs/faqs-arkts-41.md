---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-41
title: 对于多线程操作首选项和数据库是不是线程安全的？还是每一个线程独立的
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > 对于多线程操作首选项和数据库是不是线程安全的？还是每一个线程独立的
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:24+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1a6fa647300c6d54c3a6fc2cb04f394b562c834eadfb74e38bed4db3f2060b3c
---

该方法是线程安全的。

* 首选项默认支持线程安全，允许多个线程同时读取数据。为了防止数据不一致，写入操作必须进行同步控制。
* 数据库SQLite和ORM框架均为线程安全。需要合理管理连接和操作。
