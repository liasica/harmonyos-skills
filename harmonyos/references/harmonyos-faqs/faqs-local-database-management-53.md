---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-53
title: PersistentStorage、Preferences、键值型数据库、关系型数据库的区别及适用场景
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > PersistentStorage、Preferences、键值型数据库、关系型数据库的区别及适用场景
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:29+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0233d06b0d63a17c789ff037450ae71d48f56014eee51982bdf7caed31d16377
---

## 问题现象

PersistentStorage、用户首选项（Preferences）、键值型数据库（KV-Store）、关系型数据库（RelationalStore）都是用于持久化存储数据的机制，但适用场景和特点有所不同，用户在使用时该如何选择？

## 解决方案

[PersistentStorage](../harmonyos-guides/arkts-persiststorage.md#从appstorage中访问persistentstorage初始化的属性)、[用户首选项（Preferences）](../harmonyos-guides/data-persistence-by-preferences.md)、[键值型数据库（KV-Store）](../harmonyos-guides/data-persistence-by-kv-store.md)、[关系型数据库（RelationalStore）](../harmonyos-guides/data-persistence-by-rdb-store.md)适用场景如下：

|  | PersistentStorage | 用户首选项（Preferences） | 键值型数据库（KV-Store） | 关系型数据库（RelationalStore） |
| --- | --- | --- | --- | --- |
| 介绍 | PersistentStorage持久化存储UI状态，通常和AppStorage配合使用，选择AppStorage存储的数据写入磁盘，以确保这些属性在应用程序重新启动时的值与应用程序关闭时的值相同。 | Preferences是用于存储应用程序设置的轻量级数据库。它提供了一种简单的机制来存储和检索应用程序的配置信息，数据通常以键值对的形式存储。Preferences的数据是同步存储的，适用于存储少量的结构化数据。 | 一种非关系型数据库，其数据以“键值”对的形式进行组织、索引和存储，其中“键”作为唯一标识符。 | 关系型数据库基于SQLite组件，适用于存储包含复杂关系数据的场景。 |
| 适用场景 | 1. 需要持久化存储UI状态的应用程序。 2. 需要在UI实例初始化后进行持久化操作。 3. 希望在应用程序关闭后重新启动时恢复上次的状态。 | 1. 需要存储应用程序的配置信息。 2. 需要支持数据的快速读取和写入。 3. 希望在应用程序的不同部分共享数据。 4. 应用保存用户的个性化设置（字体大小，是否开启夜间模式）。 | 存储的数据没有复杂的关系模型，比如存储商品名称及对应价格、员工工号及今日是否已出勤等。 | 数据之间有较强的对应关系场景，比如一个班级的学生信息，需要包括姓名、学号、各科成绩等；公司的雇员信息，需要包括姓名、工号、职位等。 |
| 是否支持加密 | 不涉及。 | 不支持。 | 支持，[参考数据库加密文档](../harmonyos-guides/data-encryption.md)。 | 支持，[参考数据库加密文档](../harmonyos-guides/data-encryption.md)。 |
| 限制条件 | 1. 不支持嵌套对象（对象数组，对象的属性是对象等）。 2. PersistentStorage适用于存储<2KB的轻量数据，其同步写入磁盘机制会影响UI线程性能。需存储大量数据时，应改用数据库API以避免界面渲染卡顿。 [更多详细参考官方文档](../harmonyos-guides/arkts-persiststorage.md#限制条件)。 | 1. 首选项无法保证多进程并发安全，易导致数据损坏，不支持多进程使用。 2. Key键为string类型，非空且长度≤1024字节。 3. 字符串类型的Value使用UTF-8编码，可为空，非空时长度不超过16MB。 4. 内存随数据量增加而增长，建议存储≤50MB轻量数据，大数据的同步持久化操作易引发主线程卡顿，可能出现appfreeze问题。 [更多详细参考官方文档](../harmonyos-guides/data-persistence-by-preferences.md#约束限制)。 | 1. 设备协同数据库，针对每条记录，Key的长度≤896 Byte，Value的长度<4 MB。 2. 单版本数据库，针对每条记录，Key的长度≤1 KB，Value的长度<4 MB。 3. 每个应用程序最多支持同时打开16个键值型分布式数据库。 4. 键值型数据库事件回调方法中不允许进行阻塞操作，例如修改UI组件。 [更多详细参考官方文档](../harmonyos-guides/data-persistence-by-kv-store.md#约束限制)。 | 1. 为保证数据的准确性，数据库同一时间只能支持一个写操作。 2. 为保证插入并读取数据成功，建议一条数据不要超过2M。超出该大小，插入成功，读取失败。 3. 当应用被卸载完成后，设备上的相关数据库文件及临时文件会被自动清除。 [更多详细参考官方文档](../harmonyos-guides/data-persistence-by-rdb-store.md#约束限制) 。 |
