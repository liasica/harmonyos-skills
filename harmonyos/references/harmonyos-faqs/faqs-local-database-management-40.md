---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-40
title: 数据管理如何保证数据安全
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 数据管理如何保证数据安全
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:19+08:00
doc_updated_at: 2026-03-25
content_hash: sha256:2b0385fba8ab8cc9c775c79b6c79aad2d3a48d6e3dc7383ba9d752b7dd72a86f
---

**问题描述**

在系统运行过程中，如遇存储损坏、存储空间不足、文件系统权限问题或系统断电等情况，均可能导致数据库故障。数据管理应如何确保数据安全？

**解决措施**

数据管理通过备份恢复、加密存储、分级访问控制三项核心技术保障数据可靠性和安全性。

[数据库备份与恢复 (ArkTS)](../harmonyos-guides/data-backup-and-restore.md)：重要业务数据丢失等异常场景，可以通过备份恢复数据库，保证关键数据不丢失。

[数据库加密 (ArkTS)](../harmonyos-guides/data-encryption.md)：当数据库中存储如认证凭据、财务数据等高敏感信息时，可对数据库进行加密，提高数据库安全性。

[基于设备分类和数据分级的访问控制 (ArkTS)](../harmonyos-guides/access-control-by-device-and-data-level.md)：数据跨设备同步时，数据管理基于数据安全标签和设备安全等级进行访问控制，保证数据安全。
