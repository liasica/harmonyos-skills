---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-vector-store-guidelines
title: 通过向量数据库实现数据持久化 (C/C++)
breadcrumb: 指南 > 应用框架 > ArkData（方舟数据管理） > 应用数据持久化 > 通过向量数据库实现数据持久化 (C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cb1d84c6de7ffb484ca85c77976956f0481f602f7835d35ec678f355910c18da
---

## 场景介绍

向量数据库是一种支持存储、管理和检索向量数据的数据库，也支持标量的关系型数据处理。数据类型"floatvector"用来存储数据向量化的结果，从而实现对这些数据的快速检索和相似性搜索‌。

从API version 18开始，支持通过向量数据库实现数据持久化。

## 基本概念

* **结果集**：指用户查询之后的结果集合，可以对数据进行访问。结果集提供了灵活的数据访问方式，可以更方便地拿到用户想要的数据。
* **floatvector**：该数据类型表示向量数据，例如[1.0, 3.0, 2.4, 5.1, 6.2, 11.7]。

## 约束限制

* 系统默认日志方式是[WAL](data-terminology.md#wal模式)（Write Ahead Log）模式，系统默认落盘方式是[FULL模式](data-terminology.md#full模式)。
* 数据库中默认有4个读连接和1个写连接，线程获取到空闲读连接时，即可进行读取操作。当没有空闲读连接时，会创建新的读连接。
* 为保证数据的准确性，数据库同一时间只能支持一个写操作，并发的写操作会串行执行。
* 当应用被卸载完成后，设备上的相关数据库文件及临时文件会被自动清除。
* 为保证插入并读取数据成功，建议一条数据不要超过2M。超出该大小，插入成功，读取失败。

## 规格限制

详情见[规格限制](data-persistence-by-vector-store.md#规格限制)。

## 接口说明

详细的接口说明请参考[RDB](../harmonyos-references/capi-rdb.md)。

| 接口名称 | 描述 |
| --- | --- |
| int OH\_Rdb\_SetDbType(OH\_Rdb\_ConfigV2 \*config, int dbType) | 设置数据库类型。 |
| OH\_Rdb\_Store \*OH\_Rdb\_CreateOrOpen(const OH\_Rdb\_ConfigV2 \*config, int \*errCode) | 获得一个相关的OH\_Rdb\_Store实例(调用OH\_Rdb\_SetDbType设置dbType为RDB\_CAYLEY)，操作向量数据库。 |
| int OH\_Rdb\_ExecuteV2(OH\_Rdb\_Store \*store, const char \*sql, const OH\_Data\_Values \*args, OH\_Data\_Value \*\*result) | 执行有返回值的SQL语句，用来执行写操作，支持参数绑定，语句中的各种表达式和操作符之间的关系操作符号(例如=、>、<)不超过1000个。 |
| int OH\_Rdb\_ExecuteByTrxId(OH\_Rdb\_Store \*store, int64\_t trxId, const char \*sql) | 使用指定的事务ID执行无返回值的SQL语句，事务ID为0时不使用事务。 |
| OH\_Cursor \*OH\_Rdb\_ExecuteQuery(OH\_Rdb\_Store \*store, const char \*sql) | 根据指定SQL语句查询数据库中的数据。 |
| OH\_Cursor \*OH\_Rdb\_ExecuteQueryV2(OH\_Rdb\_Store \*store, const char \*sql, const OH\_Data\_Values \*args) | 根据指定SQL语句查询数据库中的数据，支持参数绑定，语句中的各种表达式和操作符之间的关系操作符号(例如=、>、<)不超过1000个。 |
| int OH\_Rdb\_DeleteStoreV2(const OH\_Rdb\_ConfigV2 \*config) | 删除数据库。 |
| int OH\_Cursor\_GetFloatVectorCount(OH\_Cursor \*cursor, int32\_t columnIndex, size\_t \*length) | 获取当前行中指定列的浮点数数组大小。 |
| int OH\_Cursor\_GetFloatVector(OH\_Cursor \*cursor, int32\_t columnIndex, float \*val, size\_t inLen, size\_t \*outLen) | 以浮点数数组的形式获取当前行中指定列的值，其中inLen不能小于实际的数组大小。 |

## 开发步骤

**添加动态链接库**

CMakeLists.txt中添加以下lib。

```
1. libnative_rdb_ndk.z.so
```

**头文件**

```
1. #include <hilog/log.h>
2. #include <database/data/oh_data_values.h>
3. #include <database/rdb/oh_cursor.h>
4. #include <database/rdb/relational_store.h>
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/VectorStore/entry/src/main/cpp/napi_init.cpp#L19-L25)

1. 判断当前系统是否支持向量数据库，若不支持，则表示当前系统不具备向量数据库能力。示例代码如下：

   ```
   1. int numType = 0;
   2. // 如果numType为2则支持向量数据库，为1则不支持向量数据库
   3. OH_Rdb_GetSupportedDbType(&numType);
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/VectorStore/entry/src/main/cpp/napi_init.cpp#L212-L216)
2. 当前系统支持向量数据库时，获取OH\_Rdb\_Store实例。示例代码如下：

   ```
   1. // 创建OH_Rdb_Config对象
   2. OH_Rdb_ConfigV2 *config = OH_Rdb_CreateConfig();
   3. // 该路径为应用沙箱路径
   4. // 数据库文件创建位置位于沙箱路径 /data/storage/el2/database/rdb/rdb_vector_test.db
   5. OH_Rdb_SetDatabaseDir(config, "/data/storage/el2/database");
   6. // 数据库文件名
   7. OH_Rdb_SetStoreName(config, "rdb_vector_test.db");
   8. // 应用包名
   9. OH_Rdb_SetBundleName(config, "com.samples.vectorStore");
   10. // 数据库是否加密
   11. OH_Rdb_SetEncrypted(config, false);
   12. // 数据库文件安全等级
   13. OH_Rdb_SetSecurityLevel(config, OH_Rdb_SecurityLevel::S1);
   14. // 数据库文件存放的安全区域
   15. OH_Rdb_SetArea(config, RDB_SECURITY_AREA_EL1);
   16. // 数据库类型
   17. OH_Rdb_SetDbType(config, RDB_CAYLEY);

   19. // 获取OH_Rdb_Store实例
   20. int errCode = 0;
   21. OH_Rdb_Store *store_ = OH_Rdb_CreateOrOpen(config, &errCode);
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/VectorStore/entry/src/main/cpp/napi_init.cpp#L220-L242)
3. 获取到OH\_Rdb\_Store后，建表并插入数据。

   说明

   向量数据库没有显式的flush操作实现持久化，数据插入即保存在持久化文件。

   示例代码如下：

   ```
   1. char createTableSql[] =
   2. "CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY AUTOINCREMENT, data1 floatvector(2));";
   3. // 执行建表语句
   4. OH_Rdb_ExecuteByTrxId(store_, 0, createTableSql);

   6. // 不使用参数绑定插入数据
   7. OH_Rdb_ExecuteV2(store_, "INSERT INTO test (id, data1) VALUES (0, '[3.4, 4.5]');", nullptr, nullptr);
   8. // 使用参数绑定插入数据
   9. OH_Data_Values *values = OH_Values_Create();
   10. OH_Values_PutInt(values, 1);
   11. float test[] = { 1.2, 2.3 };
   12. size_t len = sizeof(test) / sizeof(test[0]);
   13. OH_Values_PutFloatVector(values, test, len);
   14. char insertSql[] = "INSERT INTO test (id, data1) VALUES (?, ?);";
   15. OH_Rdb_ExecuteV2(store_, insertSql, values, nullptr);
   16. OH_Values_Destroy(values);
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/VectorStore/entry/src/main/cpp/napi_init.cpp#L165-L182)
4. 获取到OH\_Rdb\_Store后，修改或删除数据。示例代码如下：

   ```
   1. // 不使用参数绑定修改数据
   2. OH_Rdb_ExecuteV2(store_, "update test set data1 = '[5.1, 6.1]' where id = 0;", nullptr, nullptr);

   4. // 使用参数绑定修改数据
   5. float test1[2] = { 5.5, 6.6 };
   6. OH_Data_Values *values1 = OH_Values_Create();
   7. size_t len1 = sizeof(test1) / sizeof(test1[0]);
   8. OH_Values_PutFloatVector(values1, test1, len1);
   9. OH_Values_PutInt(values1, 1);
   10. OH_Rdb_ExecuteV2(store_, "update test set data1 = ? where id = ?", values1, nullptr);
   11. OH_Values_Destroy(values1);

   13. // 不使用参数绑定删除数据
   14. OH_Rdb_ExecuteV2(store_, "delete from test where id = 0", nullptr, nullptr);

   16. // 使用参数绑定删除数据
   17. OH_Data_Values *values2 = OH_Values_Create();
   18. OH_Values_PutInt(values2, 1);
   19. OH_Rdb_ExecuteV2(store_, "delete from test where id = ?", values2, nullptr);
   20. OH_Values_Destroy(values2);
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/VectorStore/entry/src/main/cpp/napi_init.cpp#L184-L205)
5. 获取到OH\_Rdb\_Store后，查询数据。

   说明

   当应用完成查询数据操作，不再使用结果集（OH\_Cursor）时，请及时调用destroy方法关闭结果集，释放系统为其分配的内存。

   示例代码如下：

   ```
   1. // 不使用参数绑定查询数据
   2. OH_Cursor *cursor = OH_Rdb_ExecuteQueryV2(store_, "select * from test where id = 1;", nullptr);
   3. if (cursor == NULL) {
   4. OH_LOG_ERROR(LOG_APP, "Query failed.");
   5. return;
   6. }
   7. // getRowCount会遍历全表获取行数，存在性能开销。请根据实际场景合理使用。
   8. int rowCount = 0;
   9. cursor->getRowCount(cursor, &rowCount);
   10. while (cursor->goToNextRow(cursor) == OH_Rdb_ErrCode::RDB_OK) {
   11. size_t count = 0;
   12. // floatvector数组是第二列数据，1表示列下标索引
   13. OH_Cursor_GetFloatVectorCount(cursor, 1, &count);
   14. float test[count];
   15. size_t outLen;
   16. OH_Cursor_GetFloatVector(cursor, 1, test, count, &outLen);
   17. }
   18. cursor->destroy(cursor);
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/VectorStore/entry/src/main/cpp/napi_init.cpp#L36-L55)

   ```
   1. // 使用参数绑定查询数据
   2. char querySql[] = "select * from test where id = ?;";
   3. OH_Data_Values *values = OH_Values_Create();
   4. OH_Values_PutInt(values, 1);
   5. OH_Cursor *cursor = OH_Rdb_ExecuteQueryV2(store_, querySql, values);
   6. if (cursor == NULL) {
   7. OH_LOG_ERROR(LOG_APP, "Query failed.");
   8. return;
   9. }
   10. while (cursor->goToNextRow(cursor) == OH_Rdb_ErrCode::RDB_OK) {
   11. size_t count = 0;
   12. // floatvector数组是第二列数据，1表示列下标索引
   13. OH_Cursor_GetFloatVectorCount(cursor, 1, &count);
   14. float test[count];
   15. size_t outLen;
   16. OH_Cursor_GetFloatVector(cursor, 1, test, count, &outLen);
   17. }
   18. OH_Values_Destroy(values);
   19. cursor->destroy(cursor);
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/VectorStore/entry/src/main/cpp/napi_init.cpp#L60-L83)

   ```
   1. // 子查询，创建第二张表
   2. OH_Rdb_ExecuteV2(store_, "CREATE TABLE IF NOT EXISTS example(id text PRIMARY KEY);", nullptr, nullptr);
   3. char querySql[] = "select * from test where id in (select id from example);";
   4. OH_Cursor *cursor = OH_Rdb_ExecuteQueryV2(store_, querySql, nullptr);
   5. if (cursor == NULL) {
   6. OH_LOG_ERROR(LOG_APP, "Query failed.");
   7. return;
   8. }
   9. while (cursor->goToNextRow(cursor) == OH_Rdb_ErrCode::RDB_OK) {
   10. size_t count = 0;
   11. // floatvector数组是第二列数据，1表示列下标索引
   12. OH_Cursor_GetFloatVectorCount(cursor, 1, &count);
   13. float test[count];
   14. size_t outLen;
   15. OH_Cursor_GetFloatVector(cursor, 1, test, count, &outLen);
   16. }
   17. cursor->destroy(cursor);
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/VectorStore/entry/src/main/cpp/napi_init.cpp#L88-L106)

   ```
   1. // 聚合查询
   2. OH_Cursor *cursor = OH_Rdb_ExecuteQueryV2(store_,
   3. "select * from test where data1 <-> '[1.0, 1.0]' > 0 group by id having max(data1 <=> '[1.0, 1.0]');", nullptr);
   4. if (cursor == NULL) {
   5. OH_LOG_ERROR(LOG_APP, "Query failed.");
   6. return;
   7. }
   8. while (cursor->goToNextRow(cursor) == OH_Rdb_ErrCode::RDB_OK) {
   9. size_t count = 0;
   10. // floatvector数组是第二列数据，1表示列下标索引
   11. OH_Cursor_GetFloatVectorCount(cursor, 1, &count);
   12. float test[count];
   13. size_t outLen;
   14. OH_Cursor_GetFloatVector(cursor, 1, test, count, &outLen);
   15. }
   16. cursor->destroy(cursor);
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/VectorStore/entry/src/main/cpp/napi_init.cpp#L111-L128)

   ```
   1. // 多表查询
   2. OH_Cursor *cursor = OH_Rdb_ExecuteQueryV2(store_, "select id, data1 <-> '[1.5, 5.6]' as distance from test "
   3. "union select id, data1 <-> '[1.5, 5.6]' as distance from test order by distance limit 5;", nullptr);
   4. if (cursor == NULL) {
   5. OH_LOG_ERROR(LOG_APP, "Query failed.");
   6. return;
   7. }
   8. while (cursor->goToNextRow(cursor) == OH_Rdb_ErrCode::RDB_OK) {
   9. size_t count = 0;
   10. // floatvector数组是第二列数据，1表示列下标索引
   11. OH_Cursor_GetFloatVectorCount(cursor, 1, &count);
   12. float test[count];
   13. size_t outLen;
   14. OH_Cursor_GetFloatVector(cursor, 1, test, count, &outLen);
   15. }
   16. cursor->destroy(cursor);
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/VectorStore/entry/src/main/cpp/napi_init.cpp#L133-L150)
6. 创建视图并执行查询。示例代码如下：

   ```
   1. OH_Rdb_ExecuteV2(store_, "CREATE VIEW v1 as select * from test where id > 0;", nullptr, nullptr);
   2. OH_Cursor *cursor = OH_Rdb_ExecuteQueryV2(store_, "select * from v1;", nullptr);
   3. if (cursor == NULL) {
   4. OH_LOG_ERROR(LOG_APP, "Query failed.");
   5. return;
   6. }
   7. cursor->destroy(cursor);
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/VectorStore/entry/src/main/cpp/napi_init.cpp#L247-L255)
7. ‌使用向量索引进行查询，提升查询效率。

   向量数据库索引‌是一种以向量作为键的索引机制，旨在提供高效且快速的搜索能力。

   当前支持的向量索引基础语法和扩展语法如下：

   * 基础语法如下：

     ```
     1. // index_name为索引名称，index_type是索引类型，dist_function是索引距离度量类型
     2. CREATE INDEX [IF NOT EXISTS] index_name ON table_name USING index_type (column_name dist_function);

     4. DROP INDEX table_name.index_name;
     ```
   * 扩展语法如下：

     ```
     1. CREATE INDEX [基础语法] [WITH(parameter = value [, ...])];
     ```

   **表1** 索引类型(index\_type)

   | 类型 | 备注说明 |
   | --- | --- |
   | gsdiskann | 适用于处理高维稠密向量数据，如文本嵌入、图像特征等。 |

   **表2** 索引距离度量类型(dist\_function)

   | 类型 | 计算符号 | 备注说明 |
   | --- | --- | --- |
   | L2 | <-> | 欧式距离。 |
   | COSINE | <=> | 余弦距离。 |

   **表3** 扩展语法参数(parameter)

   | 参数名称 | 取值范围和约束 | 备注说明 |
   | --- | --- | --- |
   | QUEUE\_SIZE | 设置范围是[10, 1000]，默认值 20。 | 代表创建索引搜索近邻的时候候选队列的长度，queue\_size越大，构建速度降低，召回率有略微提升。 |
   | OUT\_DEGREE | 设置范围是[1, 1200] ，默认值 60。 | 邻居节点出度数量。out\_degree与pageSize也有关系，out\_degree的数量超过pageSize的存储范围将报错GRD\_INVALID\_ARGS。 |

   说明

   * 删除索引的时候需要指定表名称，即Drop Index table.index\_name。
   * 随表一起创建的索引不能删除，如建表时创建的主键。
   * 向量索引的命中条件。必须是ORDER BY + LIMIT类型的查询，ORDER BY只有一个排序条件，这个条件是向量距离条件；ORDER BY与DESC连用，不会使用向量索引；查询距离度量与创建索引时的度量需要保持一致，例如创建向量索引时使用L2，在查询时使用<->进行度量才可以命中索引。

   示例代码如下：

   ```
   1. // 基础用法，创建的索引名称为diskann_l2_idx，索引列为data1，类型为gsdiskann，距离度量类型为L2
   2. OH_Rdb_ExecuteV2(store_, "CREATE INDEX diskann_l2_idx ON test USING GSDISKANN(data1 L2);", nullptr, nullptr);

   4. // 删除表test中的diskann_l2_idx索引
   5. OH_Rdb_ExecuteV2(store_, "DROP INDEX test.diskann_l2_idx;", nullptr, nullptr);

   7. // 扩展语法，设置QUEUE_SIZE为20，OUT_DEGREE为50
   8. OH_Rdb_ExecuteV2(store_, "CREATE INDEX diskann_l2_idx ON test USING GSDISKANN(data1 L2) WITH "
   9. "(queue_size=20, out_degree=50);", nullptr, nullptr);
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/VectorStore/entry/src/main/cpp/napi_init.cpp#L257-L267)
8. 配置数据老化功能。当应用的数据需要定期清理时，可以按时间或空间配置数据老化策略，从而实现数据的自动化清理。

   语法如下所示：

   ```
   1. CREATE TABLE table_name(column_name type [, ...]) [WITH(parameter = value [, ...])];
   ```

   其中，parameter为可配置的参数，value为对应取值，具体情况见下表。

   **表4** 数据老化策略参数(parameter)

   | 参数名称 | 必填 | 取值范围和使用说明 |
   | --- | --- | --- |
   | time\_col | 是 | 列名。类型必须为整数且不为空。 |
   | interval | 否 | 老化任务线程的执行间隔时间，超过该时间后执行写操作，触发老化任务，删除符合老化条件的数据；若在间隔时间内执行写操作，不会触发老化任务。取值范围是[5 second, 1 year]，时间单位支持second、minute、hour、day、month、year，不区分大小写或复数形式(1 hour和1 hours均可)，默认是1 day。 |
   | ttl | 否 | 数据保留时间。取值范围是[1 hour, 1 year]，时间单位支持second、minute、hour、day、month、year，不区分大小写或复数形式(1 hour和1 hours均可)，默认是3 month。 |
   | max\_num | 否 | 数据量限制。取值范围是[100, 1024]，默认是1024。老化任务在执行完过期数据删除后，如剩余表内数据超过max\_num行，则会找到距离过期时间最近的时间点，删除该时间点对应的所有数据，直到数据量少于max\_num。 |

   时间相关参数会按数值换算为秒作为原子单位，取值规则如下所示：

   | 单位 | 向下换算为秒取值 |
   | --- | --- |
   | year | 365 \* 24 \* 60 \* 60 |
   | month | 30 \* 24 \* 60 \* 60 |
   | day | 24 \* 60 \* 60 |
   | hour | 60 \* 60 |
   | minute | 60 |

   例如配置ttl = '3 months'，实际ttl会被换算为3 \* (30 \* 24 \* 60 \* 60) = 7776000 seconds。

   示例代码如下：

   ```
   1. // 每隔五分钟执行写操作后，会触发数据老化任务
   2. OH_Rdb_ExecuteV2(store_,"CREATE TABLE test2(rec_time integer not null) WITH "
   3. "(time_col = 'rec_time', interval = '5 minute');", nullptr, nullptr);
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/VectorStore/entry/src/main/cpp/napi_init.cpp#L269-L273)
9. 配置数据压缩功能。该功能在建表时配置，可以压缩数据类型为text的列数据。

   从API version 20开始，支持数据压缩功能。

   语法如下所示：

   ```
   1. CREATE TABLE table_name(content text [, ...]) [WITH(compress_col = 'content')];
   ```

   其中，compress\_col为必填参数，value是类型为text的数据列名，可以与数据老化功能同时配置。

   示例代码如下：

   ```
   1. // content列配置了数据压缩，并且配置了数据老化。
   2. OH_Rdb_ExecuteV2(store_,"CREATE TABLE IF NOT EXISTS test3 (time integer not null, content text) with "
   3. "(time_col = 'time', interval = '5 minute', compress_col = 'content');", nullptr, nullptr);
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/VectorStore/entry/src/main/cpp/napi_init.cpp#L275-L279)
10. 删除数据库。示例代码如下：

    ```
    1. OH_Rdb_CloseStore(store_);
    2. OH_Rdb_DeleteStoreV2(config);
    ```

    [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/VectorStore/entry/src/main/cpp/napi_init.cpp#L281-L284)
