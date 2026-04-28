---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-34
title: 插入数据之后，RDB数据库的WAL文件体积异常
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 插入数据之后，RDB数据库的WAL文件体积异常
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:18+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:f88151732ffef6973c207521c1f2092fe49f77bedb127354d10336da9c017141
---

**解决措施**

在开启读事务或结果集未关闭的情况下持续执行增删改操作，会导致WAL文件大小超过默认上限，此时系统会抛出错误码14800047。

处理该错误码时，检查结果集或事务状态。
