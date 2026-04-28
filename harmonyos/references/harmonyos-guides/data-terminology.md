---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-terminology
title: ArkData术语
breadcrumb: 指南 > 应用框架 > ArkData（方舟数据管理） > ArkData术语
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:24+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:68d7876beb753286e712607048a701918cdcd4bb7f539aa52d260d4ac8a2bf34
---

## WAL模式

WAL（Write Ahead Log）模式是SQLite日志模式中的一种，区别于传统的rollback journal（回滚日志）模式，用于提升并发性能和写入效率。

详细介绍，请查看SQLite [Write-Ahead Logging](https://sqlite.org/wal.html)介绍。

## FULL模式

FULL模式是SQLite中数据库同步写入策略之一，当每次执行数据修改时，SQLite都会调用底层操作系统的xSync方法，保证所有数据均安全写入磁盘。可在系统崩溃、断电场景保证数据库不会损坏。

详细介绍，请查看SQLite [synchronous](https://sqlite.org/pragma.html#pragma_synchronous)。
