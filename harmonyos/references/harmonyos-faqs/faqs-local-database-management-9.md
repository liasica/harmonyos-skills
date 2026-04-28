---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-9
title: 如何使用Sqlite全文检索能力
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 如何使用Sqlite全文检索能力
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:14+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:2fa534ac7ba018ad99bd152f5b5174839e5a0d5b97d5b01f95c3a911f186e736
---

**解决措施**

没有提供直接的接口，需要执行SQL语句CREATE VIRTUAL TABLE语句建立FTS表，再使用MATCH操作符实现检索。

[executeSql](../harmonyos-references/arkts-apis-data-relationalstore-rdbstore.md#executesql10)：执行包含指定参数但不返回值的SQL语句。

[querySql](../harmonyos-references/arkts-apis-data-relationalstore-rdbstore.md#querysql10)：根据指定的SQL语句查询数据库中的数据。
