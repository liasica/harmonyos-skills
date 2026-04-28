---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-38
title: 数据存储方案如何选择
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 数据存储方案如何选择
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:19+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1e2c9b05fa9fa8725d5c8dde4d48bd916907d21ecfa3da2a34949282bd997393
---

**问题描述**

HarmonyOS标准系统支持典型的存储数据形态，包括用户首选项、键值型数据库、关系型数据库。

如果开发者需要实现应用级或多个页面的状态数据共享，就需要使用应用级别的状态管理。ArkTS根据不同特性，提供了以下几种UI状态管理能力：

LocalStorage：页面级UI状态存储

AppStorage：应用全局的UI状态存储

PersistentStorage：持久化存储UI状态

开发者选择合适的数据存储方案时，应考虑以下因素：数据类型、访问模式、性能要求、成本预算和扩展性需求。

**解决措施**

开发者应根据数据类型、访问模式等核心因素，结合各存储方案的功能特性进行选择。根据数据特性和使用场景，主要存储方案可分为以下几类：

|  |  |
| --- | --- |
| [LocalStorage：页面级UI状态存储](../harmonyos-guides/arkts-localstorage.md) | 页面级UI状态存储，用于UIAbility内、页面间的状态共享。 |
| [AppStorage：应用全局的UI状态存储](../harmonyos-guides/arkts-appstorage.md) | 单例LocalStorage对象，由UI框架在应用程序启动时创建，为应用程序UI状态属性提供中央存储。 |
| [PersistentStorage：持久化存储UI状态](../harmonyos-guides/arkts-persiststorage.md) | 持久化存储UI状态，和AppStorage配合使用，选择AppStorage存储的数据写入磁盘，以确保这些属性在应用程序重新启动时的值与应用程序关闭时的值相同。 |
| [@ohos.data.preferences (用户首选项)](../harmonyos-references/js-apis-data-preferences.md) | 用于保存应用的配置信息。数据通过文本的形式保存在设备中，应用使用过程中会将文本中的数据全量加载到内存中，所以访问速度快、效率高，但不适合需要存储大量数据的场景。 |
| [@ohos.data.distributedKVStore (分布式键值数据库)](../harmonyos-references/js-apis-distributedkvstore.md) | 一种非关系型数据库，其数据以“键值”对的形式进行组织、索引和存储，其中“键”作为唯一标识符。适合数据关系和业务关系较少的业务数据存储，同时因其在分布式场景中降低了解决数据库版本兼容问题的复杂度，和数据同步过程中冲突解决的复杂度而被使用。相比于关系型数据库，更容易做到跨设备跨版本兼容。 |
| [@ohos.data.relationalStore (关系型数据库)](../harmonyos-references/js-apis-data-relationalstore.md) | 一种关系型数据库，以行和列的形式存储数据，广泛用于应用中的关系型数据的处理，包括一系列的增、删、改、查等接口，开发者也可以运行自己定义的SQL语句来满足复杂业务场景的需要。 |
