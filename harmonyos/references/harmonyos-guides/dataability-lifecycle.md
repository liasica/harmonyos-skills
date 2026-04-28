---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/dataability-lifecycle
title: DataAbility的生命周期
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > FA模型开发指导 > FA模型应用组件 > DataAbility组件开发指导 > DataAbility的生命周期
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:00+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:e7c1abb46a334417430332e2f1d06d877d159f45d25f4e93c094899bd4974161
---

应用开发者可以根据业务场景实现data.js/data.ets中的生命周期相关接口。DataAbility生命周期接口说明见下表。

**表1** DataAbility相关生命周期API功能介绍

| 接口名 | 描述 |
| --- | --- |
| onInitialized?(info: AbilityInfo): void | 在Ability初始化调用，通过此回调方法执行RDB等初始化操作。 |
| update?(uri: string, valueBucket: rdb.ValuesBucket, predicates: dataAbility.DataAbilityPredicates, callback: AsyncCallback<number>): void | 更新数据库中的数据。 |
| query?(uri: string, columns: Array<string>, predicates: dataAbility.DataAbilityPredicates, callback: AsyncCallback<ResultSet>): void | 查询数据库中的数据。 |
| delete?(uri: string, predicates: dataAbility.DataAbilityPredicates, callback: AsyncCallback<number>): void | 删除一条或多条数据。 |
| normalizeUri?(uri: string, callback: AsyncCallback<string>): void | 对URI进行规范化。一个规范化的URI可以支持跨设备使用、持久化、备份和还原等，当上下文改变时仍然可以引用到相同的数据项。 |
| batchInsert?(uri: string, valueBuckets: Array<rdb.ValuesBucket>, callback: AsyncCallback<number>): void | 向数据库中插入多条数据。 |
| denormalizeUri?(uri: string, callback: AsyncCallback<string>): void | 将一个由normalizeUri生成的规范化URI转换成非规范化的URI。 |
| insert?(uri: string, valueBucket: rdb.ValuesBucket, callback: AsyncCallback<number>): void | 向数据中插入一条数据。 |
| openFile?(uri: string, mode: string, callback: AsyncCallback<number>): void | 打开一个文件。 |
| getFileTypes?(uri: string, mimeTypeFilter: string, callback: AsyncCallback<Array<string>>): void | 获取文件的MIME类型。 |
| getType?(uri: string, callback: AsyncCallback<string>): void | 获取URI指定数据相匹配的MIME类型。 |
| executeBatch?(ops: Array<DataAbilityOperation>, callback: AsyncCallback<Array<DataAbilityResult>>): void | 批量操作数据库中的数据。 |
| call?(method: string, arg: string, extras: PacMap, callback: AsyncCallback<PacMap>): void | 自定义方法。 |
