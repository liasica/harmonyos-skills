---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-terminology
title: ArkData术语
breadcrumb: 指南 > 应用框架 > ArkData（方舟数据管理） > ArkData术语
category: harmonyos-guides
scraped_at: 2026-09-15T07:01:14+08:00
doc_updated_at: 2026-09-14
content_hash: sha256:cf2c0f9b78009092a7761896ba842f31cb7ee897a2da7f72c43f1777c27a66cb
---

## C

### Cross-device Data Sync；跨设备数据同步

将同应用数据库中的数据同步到组网环境中其他设备的功能（即分布式功能）。根据数据生命周期分为临时数据（使用分布式数据对象）和持久数据（使用关系型数据库或键值型数据库）。同应用跨设备数据同步仅支持最终一致性。详细介绍请查看[同应用跨设备数据同步概述](sync-app-data-across-devices-overview.md)。

## D

### DataShare；数据共享

跨应用数据共享机制，提供数据提供方和数据访问方的数据协同能力。实现方式包括DataShareExtensionAbility（数据共享扩展能力）、DataShareHelper（数据共享助手）和静默数据访问。

### Distributed Data Object；分布式数据对象

提供对象型结构数据的分布式能力，支持跨设备的变量"全局"访问，通过sessionId标识实现设备间数据同步。适用于跨端迁移和多端协同场景。

## E

### E-class Encrypted Database；E类加密数据库

安全级别较高的加密数据库，用于存储用户敏感信息。在锁屏时触发密钥销毁，解锁后密钥恢复。详细介绍请查看[E类加密数据库的使用](encrypted-estore-guidelines.md)。

## F

### FULL Mode；FULL模式

FULL模式是SQLite中数据库同步写入策略之一，当每次执行数据修改时，SQLite都会调用底层操作系统的xSync方法，保证所有数据均安全写入磁盘。可在系统崩溃、断电场景保证数据库不会损坏。

详细介绍请查看SQLite [synchronous](https://sqlite.org/pragma.html#pragma_synchronous)。

## K

### KV-Store (Key-Value Store)；键值型数据库

数据以"键值"对形式存储。提供读写、加密、备份能力，支持单版本数据库和设备协同数据库两种类型。适合数据关系简单的业务数据存储场景、非关系型数据库场景以及跨设备兼容场景。

## P

### Predicate；谓词

用于定义数据库操作条件的词项，常用于查询、更新、删除数据等场景。

### Preferences；用户首选项

轻量级键值型数据持久化能力，用于保存应用的配置信息、用户偏好设置等轻量级数据。数据以文本形式保存，应用使用时全量加载到内存。支持XML存储模式（默认存储模式，通用性强，支持跨平台，不支持多进程并发场景）和GSKV存储模式（支持多进程并发场景）。

## R

### RelationalStore；关系型数据库

基于SQLite组件提供的数据持久化方案，以行和列形式存储数据。支持增删改查接口和自定义SQL语句，提供事务、索引等特性。从API version 18开始支持向量数据库能力。详细介绍请查看[@ohos.data.relationalStore (关系型数据库)](../harmonyos-references/arkts-apis-data-relationalstore.md)。

### ResultSet；结果集

指用户查询之后的结果集合，可以对数据进行访问。结果集提供了灵活的数据访问方式，可以更方便地拿到用户想要的数据。

## S

### Security Level；安全等级

数据和设备分类分级的标识体系。数据安全标签分为S1（低）、S2（中）、S3（高）、S4（严重）四个等级，用于标识数据敏感程度；设备安全等级分为SL1~SL5五个等级，取决于设备的安全能力。跨设备同步时，数据安全标签不高于对端设备安全等级方可同步。详细介绍请查看[基于设备分类和数据分级的访问控制](access-control-by-device-and-data-level.md)。

## T

### Transaction；事务

用于保证数据库操作原子性的对象。可通过RdbStore的createTransaction接口获取Transaction对象，提供commit、rollback方法，确保多个操作同时成功或同时失败。支持DEFERRED（默认）、IMMEDIATE、EXCLUSIVE三种事务类型。

## U

### UDMF (Unified Data Management Framework)；统一数据管理框架

标准化数据管理框架，为跨应用、跨设备的数据交互提供统一的数据语言。包括UTD（标准化数据类型）和UDS（标准化数据结构），详细介绍请查看[标准化数据定义概述](unified-data-definition-overview.md)。

## V

### Vector Store；向量数据库

支持存储、管理和检索向量数据的数据库，从API version 18开始支持。基于关系型数据库实现，支持向量索引、数据老化、数据压缩等功能。适用于推荐系统、相似图像检索、自然语言处理等AI场景。

## W

### WAL Mode (Write Ahead Log)；WAL模式

WAL（Write Ahead Log）模式是SQLite日志模式中的一种，区别于传统的rollback journal（回滚日志）模式，用于提升并发性能和写入效率。

详细介绍请查看SQLite [Write-Ahead Logging](https://sqlite.org/wal.html)。
