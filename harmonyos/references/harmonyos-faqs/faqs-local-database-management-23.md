---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-23
title: 关系型数据库RDB支持哪些搜索能力
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 关系型数据库RDB支持哪些搜索能力
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:16+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b96c4879dd5a443f71415b0896b3064d78e534f4c89955b8eec2b51f56ab0bc7
---

SQL查询：SQLite 支持标准的 SQL 查询语法，可以执行 SELECT、INSERT、UPDATE、DELETE 等操作。

索引：SQLite 允许在列上创建索引，以提高查询性能。可以使用 CREATE INDEX 语句在 SQLite 中创建索引。

连接查询：SQLite 支持多个表之间的连接查询，可以使用 JOIN 关键字来实现表的关联查询。

全文搜索：SQLite通过FTS3扩展模块支持全文搜索功能，可以使用全文搜索扩展来实现对文本数据的搜索和匹配。
