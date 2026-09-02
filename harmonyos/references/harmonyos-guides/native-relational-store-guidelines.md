---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-relational-store-guidelines
title: 通过关系型数据库实现数据持久化 (C/C++)
breadcrumb: 指南 > 应用框架 > ArkData（方舟数据管理） > 应用数据持久化 > 通过关系型数据库实现数据持久化 (C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:11+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b964845051b20566937f89a9787e564f53e89b24fd334bfaf891db4a04430a2c
---

## 场景介绍

RelationalStore提供了一套完整的对本地数据库进行管理的机制，对外提供了一系列的增、删、改、查等接口，也可以直接运行用户输入的SQL语句来满足复杂的场景需要。

## 基本概念

* **谓词**：数据库中用来代表数据实体的性质、特征或者数据实体之间关系的词项，主要用来定义数据库的操作条件。
* **结果集**：指用户查询之后的结果集合，可以对数据进行访问。结果集提供了灵活的数据访问方式，可以更方便地拿到用户想要的数据。

## 约束限制

* 系统默认日志方式是WAL（Write Ahead Log）模式，系统默认落盘方式是FULL模式。
* 数据库中连接池的最大数量是4个，用以管理用户的读操作。
* 为保证数据的准确性，数据库同一时间仅支持一个写操作。
* 当应用被卸载完成后，设备上的相关数据库文件及临时文件会被自动清除。

## 接口说明

详细的接口说明请参考[RDB](../harmonyos-references/capi-rdb.md)。

| 接口名称 | 描述 |
| --- | --- |
| OH\_Rdb\_ConfigV2 \*OH\_Rdb\_CreateConfig() | 创建一个OH\_Rdb\_ConfigV2实例，并返回指向该实例的指针。使用完毕后需要调用OH\_Rdb\_DestroyConfig释放内存。 |
| int OH\_Rdb\_SetDatabaseDir(OH\_Rdb\_ConfigV2 \*config, const char \*databaseDir) | 给指定的数据库文件配置OH\_Rdb\_ConfigV2，设置数据库文件路径。 |
| int OH\_Rdb\_SetStoreName(OH\_Rdb\_ConfigV2 \*config, const char \*storeName) | 给指定的数据库文件配置OH\_Rdb\_ConfigV2，设置数据库名称。 |
| int OH\_Rdb\_SetBundleName(OH\_Rdb\_ConfigV2 \*config, const char \*bundleName) | 给指定的数据库文件配置OH\_Rdb\_ConfigV2，设置应用包名。 |
| int OH\_Rdb\_SetModuleName(OH\_Rdb\_ConfigV2 \*config, const char \*moduleName) | 给指定的数据库文件配置OH\_Rdb\_ConfigV2，设置应用模块名。 |
| int OH\_Rdb\_SetSecurityLevel(OH\_Rdb\_ConfigV2 \*config, int securityLevel) | 给指定的数据库文件配置OH\_Rdb\_ConfigV2，设置数据库安全级别OH\_Rdb\_SecurityLevel。 |
| int OH\_Rdb\_SetEncrypted(OH\_Rdb\_ConfigV2 \*config, bool isEncrypted) | 给指定的数据库文件配置OH\_Rdb\_ConfigV2，设置数据库是否加密。 |
| int OH\_Rdb\_SetArea(OH\_Rdb\_ConfigV2 \*config, int area) | 给指定的数据库文件配置OH\_Rdb\_ConfigV2，设置数据库安全区域等级Rdb\_SecurityArea。 |
| OH\_Rdb\_Store \*OH\_Rdb\_CreateOrOpen(const OH\_Rdb\_ConfigV2 \*config, int \*errCode) | 使用数据库配置OH\_Rdb\_ConfigV2，获得一个对应的OH\_Rdb\_Store实例，用来操作关系型数据库。 |
| OH\_Rdb\_Execute(OH\_Rdb\_Store \*store, const char \*sql) | 执行包含指定参数但不返回值的SQL语句。 |
| OH\_Rdb\_Insert(OH\_Rdb\_Store \*store, const char \*table, OH\_VBucket \*valuesBucket) | 向目标表中插入一行数据。 |
| int OH\_Rdb\_InsertWithConflictResolution(OH\_Rdb\_Store \*store, const char \*table, OH\_VBucket \*row, Rdb\_ConflictResolution resolution, int64\_t \*rowId) | 向目标表中插入一行数据，支持配置冲突解决策略。 |
| int OH\_Rdb\_UpdateWithConflictResolution(OH\_Rdb\_Store \*store, OH\_VBucket \*row, OH\_Predicates \*predicates, Rdb\_ConflictResolution resolution, int64\_t \*changes) | 根据指定条件更新数据库中的数据，支持配置冲突解决策略。 |
| OH\_Rdb\_Update(OH\_Rdb\_Store \*store, OH\_VBucket \*valuesBucket, OH\_Predicates \*predicates) | 根据OH\_Predicates的指定实例对象更新数据库中的数据。 |
| OH\_Rdb\_Delete(OH\_Rdb\_Store \*store, OH\_Predicates \*predicates) | 根据OH\_Predicates的指定实例对象从数据库中删除数据。 |
| int OH\_Predicates\_NotLike(OH\_Predicates \*predicates, const char \*field, const char \*pattern) | 设置OH\_Predicates以匹配数据类型为字符串且值不类似于指定值的字段。 |
| int OH\_Predicates\_Glob(OH\_Predicates \*predicates, const char \*field, const char \*pattern) | 设置OH\_Predicates以匹配指定字段（数据类型为字符串）且值包含通配符的字段。 |
| int OH\_Predicates\_NotGlob(OH\_Predicates \*predicates, const char \*field, const char \*pattern) | 设置OH\_Predicates以不匹配指定字段（数据类型为字符串）且值包含通配符的字段。 |
| OH\_Rdb\_Query(OH\_Rdb\_Store \*store, OH\_Predicates \*predicates, const char \*const \*columnNames, int length) | 根据指定条件查询数据库中的数据。 |
| OH\_Rdb\_DeleteStore(const OH\_Rdb\_Config \*config) | 删除数据库。 |
| OH\_VBucket\_PutAsset(OH\_VBucket \*bucket, const char \*field, Rdb\_Asset \*value) | 把Rdb\_Asset类型的数据放到指定的OH\_VBucket对象中。 |
| OH\_VBucket\_PutAssets(OH\_VBucket \*bucket, const char \*field, Rdb\_Asset \*value, uint32\_t count) | 把Rdb\_Asset数组类型的数据放到指定的OH\_VBucket对象中。 |
| OH\_Rdb\_FindModifyTime(OH\_Rdb\_Store \*store, const char \*tableName, const char \*columnName, OH\_VObject \*values) | 获取数据库指定表中指定列的数据的最后修改时间。 |
| OH\_RDB\_TransOptions \*OH\_RdbTrans\_CreateOptions(void) | 创建一个OH\_RDB\_TransOptions实例，配置事务对象。使用完毕后需要调用OH\_RdbTrans\_DestroyOptions释放内存。 |
| OH\_Cursor \*OH\_RdbTrans\_Query(OH\_Rdb\_Transaction \*trans, const OH\_Predicates \*predicates, const char \*columns[], int len) | 根据指定的条件查询数据库中的数据。 |
| OH\_Data\_Values \*OH\_Values\_Create(void) | 创建OH\_Data\_Values实例。使用完毕后需要调用OH\_Values\_Destroy释放内存。 |
| int OH\_Data\_Asset\_SetName(Data\_Asset \*asset, const char \*name) | 为资产类型数据设置名称。 |
| int OH\_Data\_Asset\_SetUri(Data\_Asset \*asset, const char \*uri) | 为资产类型数据设置绝对路径。 |
| int OH\_Data\_Asset\_SetPath(Data\_Asset \*asset, const char \*path) | 为资产类型数据设置应用沙箱里的相对路径。 |
| int OH\_Data\_Asset\_SetCreateTime(Data\_Asset \*asset, int64\_t createTime) | 为资产类型数据设置创建时间。 |
| int OH\_Data\_Asset\_SetModifyTime(Data\_Asset \*asset, int64\_t modifyTime) | 为资产类型数据设置最后修改时间。 |
| int OH\_Data\_Asset\_SetSize(Data\_Asset \*asset, size\_t size) | 为资产类型数据设置占用空间大小。 |
| int OH\_Data\_Asset\_SetStatus(Data\_Asset \*asset, Data\_AssetStatus status) | 为资产类型数据设置状态码。 |
| int OH\_Data\_Asset\_GetName(Data\_Asset \*asset, char \*name, size\_t \*length) | 获取资产类型数据的名称。 |
| int OH\_Data\_Asset\_GetUri(Data\_Asset \*asset, char \*uri, size\_t \*length) | 获取资产类型数据的绝对路径。 |
| int OH\_Data\_Asset\_GetPath(Data\_Asset \*asset, char \*path, size\_t \*length) | 获取资产类型数据在应用沙箱内的相对路径。 |
| int OH\_Data\_Asset\_GetCreateTime(Data\_Asset \*asset, int64\_t \*createTime) | 获取资产类型数据的创建时间。 |
| int OH\_Data\_Asset\_GetModifyTime(Data\_Asset \*asset, int64\_t \*modifyTime) | 获取资产类型数据的最后修改时间。 |
| int OH\_Data\_Asset\_GetSize(Data\_Asset \*asset, size\_t \*size) | 获取资产类型数据的占用空间大小。 |
| int OH\_Data\_Asset\_GetStatus(Data\_Asset \*asset, Data\_AssetStatus \*status) | 获取资产类型数据的状态码。 |
| Data\_Asset \*OH\_Data\_Asset\_CreateOne() | 创建一个资产类型实例。使用完毕后需要调用OH\_Data\_Asset\_DestroyOne释放内存。 |
| int OH\_Data\_Asset\_DestroyOne(Data\_Asset \*asset) | 销毁一个资产类型实例并回收内存。 |
| Data\_Asset \*\*OH\_Data\_Asset\_CreateMultiple(uint32\_t count) | 创建指定数量的资产类型实例。使用完毕后需要调用OH\_Data\_Asset\_DestroyMultiple释放内存。 |
| int OH\_Data\_Asset\_DestroyMultiple(Data\_Asset \*\*assets, uint32\_t count) | 销毁指定数量的资产类型实例并回收内存。 |
| int OH\_Rdb\_CreateTransaction(OH\_Rdb\_Store \*store, const OH\_RDB\_TransOptions \*options, OH\_Rdb\_Transaction \*\*trans) | 创建一个相关的OH\_Rdb\_Transaction实例，开启事务。 |
| int OH\_RdbTransOption\_SetType(OH\_RDB\_TransOptions \*options, OH\_RDB\_TransType type) | 设置事务对象类型。 |
| int OH\_RdbTrans\_Insert(OH\_Rdb\_Transaction \*trans, const char \*table, const OH\_VBucket \*row, int64\_t \*rowId) | 向目标表中插入一行数据。 |
| int OH\_RdbTrans\_InsertWithConflictResolution(OH\_Rdb\_Transaction \*trans, const char \*table, const OH\_VBucket \*row, Rdb\_ConflictResolution resolution, int64\_t \*rowId) | 将一行数据插入到目标表中，支持冲突解决。 |
| int OH\_RdbTrans\_UpdateWithConflictResolution(OH\_Rdb\_Transaction \*trans, const OH\_VBucket \*row, const OH\_Predicates \*predicates, Rdb\_ConflictResolution resolution, int64\_t \*changes) | 根据指定条件更新数据库中的数据，并支持冲突解决。 |
| int OH\_RdbTrans\_Delete(OH\_Rdb\_Transaction \*trans, const OH\_Predicates \*predicates, int64\_t \*changes) | 根据OH\_Predicates的指定实例对象从数据库中删除数据。 |
| int OH\_Value\_Destroy(OH\_Data\_Value \*value) | 销毁OH\_Data\_Value对象。 |
| int OH\_Values\_Destroy(OH\_Data\_Values \*values) | 销毁OH\_Data\_Values对象。 |
| int OH\_RdbTrans\_Execute(OH\_Rdb\_Transaction \*trans, const char \*sql, const OH\_Data\_Values \*args, OH\_Data\_Value \*\*result) | 执行包含指定参数的SQL语句。 |
| int OH\_RdbTrans\_Commit(OH\_Rdb\_Transaction \*trans) | 提交事务。 |
| int OH\_RdbTrans\_Rollback(OH\_Rdb\_Transaction \*trans) | 回滚事务。 |
| int OH\_RdbTrans\_Destroy(OH\_Rdb\_Transaction \*trans) | 销毁OH\_Rdb\_Transaction实例。 |
| int OH\_Rdb\_Attach(OH\_Rdb\_Store \*store, const OH\_Rdb\_ConfigV2 \*config, const char \*attachName, int64\_t waitTime, size\_t \*attachedNumber) | 将数据库文件附加到当前连接的数据库。 |
| int OH\_Rdb\_Detach(OH\_Rdb\_Store \*store, const char \*attachName, int64\_t waitTime, size\_t \*attachedNumber) | 从当前数据库中分离指定的数据库。 |
| int OH\_Rdb\_SetCustomDir(OH\_Rdb\_ConfigV2 \*config, const char \*customDir) | 设置数据库的自定义目录。 |
| int OH\_Rdb\_SetLocale(OH\_Rdb\_Store \*store, const char \*locale) | 支持不同语言的排序规则。 |
| int OH\_Rdb\_SetPlugins(OH\_Rdb\_ConfigV2 \*config, const char \*\*plugins, int32\_t length) | 设置具有特定功能（如全文检索）的动态库。 |

## 开发步骤

**添加动态链接库**

CMakeLists.txt中添加以下lib。

```txt
libnative_rdb_ndk.z.so, libhilog_ndk.z.so
```

**头文件**

```
#include <cstdlib>
#include <database/data/data_asset.h>
#include <database/rdb/oh_cursor.h>
#include <database/rdb/oh_predicates.h>
#include <database/rdb/oh_value_object.h>
#include <database/rdb/oh_values_bucket.h>
#include <database/rdb/relational_store.h>
#include <database/rdb/relational_store_error_code.h>
#include <hilog/log.h>
```

1. 获取OH\_Rdb\_Store实例，创建数据库文件。其中dataBaseDir变量为应用沙箱路径，Stage模式下建议使用数据库目录，参考[Context](../harmonyos-references/js-apis-inner-application-context.md)的databaseDir属性。FA模式下，由于没有接口获取数据库沙箱路径，可使用应用程序的文件目录，可参考[Context](../harmonyos-references/js-apis-inner-app-context.md)的getFilesDir接口。area为数据库文件存放的安全区域，详见[contextConstant](../harmonyos-references/js-apis-app-ability-contextconstant.md)，开发时需要实现由AreaMode枚举值对Rdb\_SecurityArea枚举值的转换。示例代码如下所示：

   ```
   // 创建OH_Rdb_ConfigV2对象
   OH_Rdb_ConfigV2 *config = OH_Rdb_CreateConfig();
   // 该路径为应用沙箱路径
   // 数据库文件创建位置将位于沙箱路径 /data/storage/el3/database/rdb/RdbTest.db
   OH_Rdb_SetDatabaseDir(config, "/data/storage/el3/database");
   // 数据库文件存放的安全区域，与databaseDir参数中el路径对应
   OH_Rdb_SetArea(config, RDB_SECURITY_AREA_EL3);
   // 数据库文件名
   OH_Rdb_SetStoreName(config, "RdbTest.db");
   // 应用包名
   OH_Rdb_SetBundleName(config, "com.samples.rdbstore");
   // 应用模块名
   OH_Rdb_SetModuleName(config, "entry");
   // 数据库文件安全等级
   OH_Rdb_SetSecurityLevel(config, OH_Rdb_SecurityLevel::S3);
   // 数据库是否加密
   OH_Rdb_SetEncrypted(config, false);
   // ···

   int errCode = 0;
   // 获取OH_Rdb_Store实例
   OH_Rdb_Store *store_ = OH_Rdb_CreateOrOpen(config, &errCode);
   if (store_ == NULL) {
       OH_LOG_ERROR(LOG_APP, "Create store failed, errCode: %{public}d", errCode);
       OH_Rdb_DestroyConfig(config);
       return;
   }
   if (errCode != OH_Rdb_ErrCode::RDB_OK) {
       OH_LOG_ERROR(LOG_APP, "Create attachStore failed, errCode: %{public}d", errCode);
       OH_Rdb_DestroyConfig(config);
       OH_Rdb_CloseStore(store_);
       return;
   }
   ```

   如果需要设置自定义数据库路径，可在上述代码// ...处调用OH\_Rdb\_SetCustomDir接口设置。如果需要设置为只读模式打开数据库，可在上述代码// ...处调用OH\_Rdb\_SetReadOnly接口设置。示例代码如下所示：

   ```
   // 可设置自定义数据库路径
   // 数据库文件创建位置将位于沙箱路径 /data/storage/el3/database/a/b/RdbTest.db
   OH_Rdb_SetCustomDir(config, "../a/b");
   // 可设置为只读模式打开数据库
   OH_Rdb_SetReadOnly(config, true);
   ```
2. 获取到OH\_Rdb\_Store后，调用OH\_Rdb\_Execute接口创建表，并调用OH\_Rdb\_Insert接口插入数据。示例代码如下所示：

   ```
   char createTableSql[] = "CREATE TABLE IF NOT EXISTS EMPLOYEE (ID INTEGER PRIMARY KEY AUTOINCREMENT, "
       "NAME TEXT NOT NULL, AGE INTEGER, SALARY REAL, CODES BLOB)";
   // 执行建表语句
   OH_Rdb_Execute(store_, createTableSql);
   ```

   ```
   // 创建键值对实例
   OH_VBucket *valueBucket = OH_Rdb_CreateValuesBucket();
   valueBucket->putText(valueBucket, "NAME", "Lisa");
   valueBucket->putInt64(valueBucket, "AGE", 18); // The value of AGE is 18
   valueBucket->putReal(valueBucket, "SALARY", 100.5); // The value of SALARY is 100.5
   uint8_t arr[] = {1, 2, 3, 4, 5};
   int len = sizeof(arr) / sizeof(arr[0]);
   valueBucket->putBlob(valueBucket, "CODES", arr, len);
   // 插入数据
   int rowId = OH_Rdb_Insert(store_, "EMPLOYEE", valueBucket);

   OH_VBucket *valueBucket2 = OH_Rdb_CreateValuesBucket();
   valueBucket2->putInt64(valueBucket2, "ID", 2); // The value of ID is 2
   valueBucket2->putText(valueBucket2, "NAME", "zhangsan");
   valueBucket2->putInt64(valueBucket2, "AGE", 24); // The value of AGE is 24
   valueBucket2->putReal(valueBucket2, "SALARY", 120.4); // The value of SALARY is 120.4
   int64_t rowId2 = -1;
   // 支持插入数据时配置冲突策略
   int result = OH_Rdb_InsertWithConflictResolution(store_, "EMPLOYEE", valueBucket2,
       Rdb_ConflictResolution::RDB_CONFLICT_REPLACE, &rowId2);
   // 销毁键值对实例
   valueBucket->destroy(valueBucket);
   valueBucket2->destroy(valueBucket2);
   ```

   **说明** 

   关系型数据库没有显式的flush操作实现持久化，数据插入即保存在持久化文件。
3. 根据谓词指定的实例对象，对数据进行修改或删除。

   调用OH\_Rdb\_Update方法修改数据，调用OH\_Rdb\_Delete方法删除数据。示例代码如下所示：

   ```
   // 创建valueBucket对象，用于存储要更新的新数据
   OH_VBucket *valueBucket = OH_Rdb_CreateValuesBucket();
   valueBucket->putText(valueBucket, "NAME", "Rose");
   valueBucket->putInt64(valueBucket, "AGE", 22); // The value of AGE is 22
   valueBucket->putReal(valueBucket, "SALARY", 200.5); // The value of SALARY is 200.5
   uint8_t arr[] = {1, 2, 3, 4, 5};
   int len = sizeof(arr) / sizeof(arr[0]);
   valueBucket->putBlob(valueBucket, "CODES", arr, len);
   // 创建谓词对象，指定更新条件：NAME为"Lisa"且SALARY为100.5
   OH_Predicates *predicates = OH_Rdb_CreatePredicates("EMPLOYEE");
   if (predicates == NULL) {
       OH_LOG_ERROR(LOG_APP, "CreatePredicates failed.");
       valueBucket->destroy(valueBucket);
       return;
   }
   OH_VObject *valueObject = OH_Rdb_CreateValueObject();
   const char *name = "Lisa";
   valueObject->putText(valueObject, name);
   predicates->equalTo(predicates, "NAME", valueObject)->andOperate(predicates);
   uint32_t count = 1;
   double salary = 100.5;
   valueObject->putDouble(valueObject, &salary, count);
   predicates->equalTo(predicates, "SALARY", valueObject);
   // 执行更新操作，将符合条件的数据更新为valueBucket中的值
   int changeRows = OH_Rdb_Update(store_, valueBucket, predicates);
   OH_Predicates *predicates2 = OH_Rdb_CreatePredicates("EMPLOYEE");
   if (predicates2 == NULL) {
       OH_LOG_ERROR(LOG_APP, "CreatePredicates failed.");
       valueObject->destroy(valueObject);
       valueBucket->destroy(valueBucket);
       return;
   }
   OH_VObject *valueObject2 = OH_Rdb_CreateValueObject();
   valueObject2->putText(valueObject2, "Rose");
   predicates2->equalTo(predicates2, "NAME", valueObject2);
   valueBucket->putInt64(valueBucket, "ID", 1); // The value of ID is 1
   valueBucket->putText(valueBucket, "NAME", "zhangsan");
   int64_t changeRows2 = -1;

   // 支持更新数据时配置冲突策略
   int result = OH_Rdb_UpdateWithConflictResolution(store_, valueBucket, predicates2,
       Rdb_ConflictResolution::RDB_CONFLICT_REPLACE, &changeRows2);
   valueObject->destroy(valueObject);
   valueObject2->destroy(valueObject2);
   valueBucket->destroy(valueBucket);
   predicates->destroy(predicates);
   predicates2->destroy(predicates2);
   ```

   ```
   // 删除数据
   OH_Predicates *predicates = OH_Rdb_CreatePredicates("EMPLOYEE");
   if (predicates == NULL) {
       OH_LOG_ERROR(LOG_APP, "CreatePredicates failed.");
       return;
   }
   OH_VObject *valueObject = OH_Rdb_CreateValueObject();
   const char *name = "Lisa";
   valueObject->putText(valueObject, name);
   predicates->equalTo(predicates, "NAME", valueObject);
   int deleteRows = OH_Rdb_Delete(store_, predicates);
   valueObject->destroy(valueObject);
   predicates->destroy(predicates);
   ```
4. 根据谓词指定的查询条件查找数据。

   调用OH\_Rdb\_Query方法查找数据，返回一个OH\_Cursor结果集。示例代码如下所示：

   ```
   OH_Predicates *predicates = OH_Rdb_CreatePredicates("EMPLOYEE");
   if (predicates == NULL) {
       OH_LOG_ERROR(LOG_APP, "CreatePredicates failed.");
       return;
   }
   const char *columnNames[] = {"NAME", "AGE"};
   int len = sizeof(columnNames) / sizeof(columnNames[0]);
   OH_Cursor *cursor = OH_Rdb_Query(store_, predicates, columnNames, len);
   if (cursor == NULL) {
       OH_LOG_ERROR(LOG_APP, "Query failed.");
       predicates->destroy(predicates);
       return;
   }
   int columnCount = 0;
   cursor->getColumnCount(cursor, &columnCount);

   // OH_Cursor是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始
   int64_t age;
   while (cursor->goToNextRow(cursor) == OH_Rdb_ErrCode::RDB_OK) {
       int32_t ageColumnIndex = -1;
       cursor->getColumnIndex(cursor, "AGE", &ageColumnIndex);
       if (ageColumnIndex != -1) {
           cursor->getInt64(cursor, ageColumnIndex, &age);
       }
   }

   // 释放谓词实例
   predicates->destroy(predicates);
   // 释放结果集
   cursor->destroy(cursor);
   ```

   配置谓词以LIKE模式或NOT LIKE模式匹配进行数据查询。示例代码如下：

   ```
   OH_Predicates *likePredicates = OH_Rdb_CreatePredicates("EMPLOYEE");
   if (likePredicates == NULL) {
       return;
   }
   OH_VObject *likePattern = OH_Rdb_CreateValueObject();
   likePattern->putText(likePattern, "zh%");
   // 配置谓词以LIKE模式匹配
   likePredicates->like(likePredicates, "NAME", likePattern);

   char *colName[] = { "NAME", "AGE" };
   auto *likeQueryCursor = OH_Rdb_Query(store_, likePredicates, colName, 2); // the length of columnNames is 2
   if (likeQueryCursor == NULL) {
       likePredicates->destroy(likePredicates);
       likePattern->destroy(likePattern);
       return;
   }
   size_t dataLength = 0;
   int colIndex = -1;
   while (likeQueryCursor->goToNextRow(likeQueryCursor) == OH_Rdb_ErrCode::RDB_OK) {
       likeQueryCursor->getColumnIndex(likeQueryCursor, "NAME", &colIndex);
       likeQueryCursor->getSize(likeQueryCursor, colIndex, &dataLength);
       char *name = (char *)malloc((dataLength + 1) * sizeof(char));
       likeQueryCursor->getText(likeQueryCursor, colIndex, name, dataLength + 1);
       free(name);
   }
   likeQueryCursor->destroy(likeQueryCursor);
   likePredicates->destroy(likePredicates);
   likePattern->destroy(likePattern);

   OH_Predicates *notLikePredicates = OH_Rdb_CreatePredicates("EMPLOYEE");
   if (notLikePredicates == NULL) {
       OH_LOG_ERROR(LOG_APP, "CreatePredicates failed.");
       return;
   }
   // 配置谓词以NOT LIKE模式匹配
   OH_Predicates_NotLike(notLikePredicates, "NAME", "zh%");
   auto *notLikeQueryCursor = OH_Rdb_Query(store_, notLikePredicates, colName, 2); // the length of columnNames is 2
   if (notLikeQueryCursor == NULL) {
       notLikePredicates->destroy(notLikePredicates);
       return;
   }
   dataLength = 0;
   colIndex = -1;
   while (notLikeQueryCursor->goToNextRow(notLikeQueryCursor) == OH_Rdb_ErrCode::RDB_OK) {
       notLikeQueryCursor->getColumnIndex(notLikeQueryCursor, "NAME", &colIndex);
       notLikeQueryCursor->getSize(notLikeQueryCursor, colIndex, &dataLength);
       char *name2 = (char *)malloc((dataLength + 1) * sizeof(char));
       notLikeQueryCursor->getText(notLikeQueryCursor, colIndex, name2, dataLength + 1);
       free(name2);
   }

   notLikePredicates->destroy(notLikePredicates);
   notLikeQueryCursor->destroy(notLikeQueryCursor);
   ```

   配置谓词以GLOB模式或NOT GLOB模式匹配进行数据查询。示例代码如下：

   ```
   OH_Predicates *globPredicates = OH_Rdb_CreatePredicates("EMPLOYEE");
   if (globPredicates == NULL) {
       OH_LOG_ERROR(LOG_APP, "CreatePredicates failed.");
       return;
   }
   // 配置谓词以GLOB模式匹配
   OH_Predicates_Glob(globPredicates, "NAME", "zh*");

   char *colName[] = { "NAME", "AGE" };
   auto *globQueryCursor = OH_Rdb_Query(store_, globPredicates, colName, 2); // the length of columnNames is 2
   if (globQueryCursor == NULL) {
       OH_LOG_ERROR(LOG_APP, "Query failed.");
       globPredicates->destroy(globPredicates);
       return;
   }
   size_t dataLength = 0;
   int colIndex = -1;
   while (globQueryCursor->goToNextRow(globQueryCursor) == OH_Rdb_ErrCode::RDB_OK) {
       globQueryCursor->getColumnIndex(globQueryCursor, "NAME", &colIndex);
       globQueryCursor->getSize(globQueryCursor, colIndex, &dataLength);
       char *name = (char *)malloc((dataLength + 1) * sizeof(char));
       globQueryCursor->getText(globQueryCursor, colIndex, name, dataLength + 1);
       free(name);
   }
   globQueryCursor->destroy(globQueryCursor);
   globPredicates->destroy(globPredicates);

   OH_Predicates *notGlobPredicates = OH_Rdb_CreatePredicates("EMPLOYEE");
   if (notGlobPredicates == NULL) {
       OH_LOG_ERROR(LOG_APP, "CreatePredicates failed.");
       return;
   }
   // 配置谓词以NOT GLOB模式匹配
   OH_Predicates_NotGlob(notGlobPredicates, "NAME", "zh*");
   auto *notGlobQueryCursor = OH_Rdb_Query(store_, notGlobPredicates, colName, 2); // the length of columnNames is 2
   if (notGlobQueryCursor == NULL) {
       OH_LOG_ERROR(LOG_APP, "Query failed.");
       notGlobPredicates->destroy(notGlobPredicates);
       return;
   }
   dataLength = 0;
   colIndex = -1;
   while (notGlobQueryCursor->goToNextRow(notGlobQueryCursor) == OH_Rdb_ErrCode::RDB_OK) {
       notGlobQueryCursor->getColumnIndex(notGlobQueryCursor, "NAME", &colIndex);
       notGlobQueryCursor->getSize(notGlobQueryCursor, colIndex, &dataLength);
       char *name2 = (char *)malloc((dataLength + 1) * sizeof(char));
       notGlobQueryCursor->getText(notGlobQueryCursor, colIndex, name2, dataLength + 1);
       free(name2);
   }
   notGlobQueryCursor->destroy(notGlobQueryCursor);
   notGlobPredicates->destroy(notGlobPredicates);
   ```

   如需指定排序时使用的语言规则，例如zh\_CN表示中文，tr\_TR表示土耳其语等。可调用OH\_Rdb\_SetLocale配置相应规则。

   ```
   OH_Rdb_SetLocale(store_, "zh_CN");
   ```

   如需配置fts（Full-Text Search，即全文搜索引擎）动态库，可使用OH\_Rdb\_SetPlugins接口进行配置。

   使用约束详见[StoreConfig](../harmonyos-references/arkts-apis-data-relationalstore-i.md#storeconfig)中pluginLibs配置项。

   ```
   const char *plugins[] = {
       "/data/storage/el1/bundle/libs/arm64/libtokenizer.so"
   };

   int32_t count = sizeof(plugins) / sizeof(plugins[0]);
   auto setResult = OH_Rdb_SetPlugins(config, plugins, count);
   ```
5. 使用事务对象进行插入、删除或更新数据操作。

   调用OH\_RdbTransOption\_SetType方法，配置要创建的事务类型，支持配置的事务类型有DEFERRED、IMMEDIATE和EXCLUSIVE，默认为DEFERRED。

   调用OH\_Rdb\_CreateTransaction方法创建事务对象，使用该事务对象执行相应事务操作。

   ```
   OH_RDB_TransOptions *options = OH_RdbTrans_CreateOptions();
   // 配置事务类型
   OH_RdbTransOption_SetType(options, RDB_TRANS_DEFERRED);
   OH_Rdb_Transaction *trans = nullptr;
   // 创建事务对象
   int res = OH_Rdb_CreateTransaction(store_, options, &trans);
   OH_RdbTrans_DestroyOptions(options);
   ```

   ```
   char transCreateTableSql[] =
       "CREATE TABLE IF NOT EXISTS transaction_table (id INTEGER PRIMARY KEY AUTOINCREMENT, data1 INTEGER, "
       "data2 INTEGER, data3 FLOAT, data4 TEXT, data5 BLOB, data6 ASSET, data7 ASSETS, data8 UNLIMITED INT, "
       "data9 FLOATVECTOR);";
       
   auto *execResult = OH_Value_Create();
       
   // 通过事务对象执行创建数据库表SQL语句
   int ret = OH_RdbTrans_Execute(trans, transCreateTableSql, nullptr, &execResult);
       
   // 创建OH_Data_Values实例
   OH_Data_Values *values = OH_Values_Create();
   ret = OH_Values_PutInt(values, 1); // The value of id is 1
   ret = OH_Values_PutInt(values, 2); // The value of data2 is 2
   ret = OH_Values_PutReal(values, 1.1); // The value of data3 is 1.1
   ret = OH_Values_PutText(values, "1"); // The value of data4 is 1
   unsigned char val[] = {1, 2};
   ret = OH_Values_PutBlob(values, val, sizeof(val) / sizeof(val[0]));
       
   Data_Asset *asset = OH_Data_Asset_CreateOne();
   ret = OH_Data_Asset_SetName(asset, "name");
   ret = OH_Values_PutAsset(values, asset);
   OH_Data_Asset_DestroyOne(asset);
       
   Data_Asset **assets = OH_Data_Asset_CreateMultiple(2); // The number of created Data_Assets is 2
   ret = OH_Data_Asset_SetName(assets[0], "name1");
   ret = OH_Data_Asset_SetName(assets[1], "name2");
   ret = OH_Values_PutAssets(values, assets, 2); // The number of Data_Assets is 2
   ret = OH_Data_Asset_DestroyMultiple(assets, 2); // The number of destroyed Data_Assets is 2
       
   uint64_t bigInt[] = {1, 2, 3, 4, 5};
   ret = OH_Values_PutUnlimitedInt(values, 0, bigInt, sizeof(bigInt) / sizeof(bigInt[0]));
       
   const char *insertSql = "INSERT INTO transaction_table "
                           "(data1, data2, data3, data4, data5, data6, data7, data8) VALUES (?, ?, ?, ?, ?, ?, ?, ?)";
   OH_Data_Value *outValue = nullptr;
       
   // 通过事务对象执行数据插入SQL语句
   ret = OH_RdbTrans_Execute(trans, insertSql, values, &outValue);
   OH_Value_Destroy(outValue);
   OH_Values_Destroy(values);
       
   OH_VBucket *transValueBucket = OH_Rdb_CreateValuesBucket();
   transValueBucket->putInt64(transValueBucket, "data1", 1); // The value of data1 is 1
   transValueBucket->putInt64(transValueBucket, "data2", 2); // The value of data2 is 2
   transValueBucket->putReal(transValueBucket, "data3", 1.1); // The value of data3 is 1.1
   transValueBucket->putText(transValueBucket, "data4", "1"); // The value of data4 is 1
   transValueBucket->putBlob(transValueBucket, "data5", val, sizeof(val) / sizeof(val[0]));
   int64_t insertRowId = -1;
   // 通过事务对象执行OH_VBucket数据插入
   int insertRet = OH_RdbTrans_Insert(trans, "transaction_table", transValueBucket, &insertRowId);
   transValueBucket->destroy(transValueBucket);
       
   OH_VBucket *transValueBucket2 = OH_Rdb_CreateValuesBucket();
   transValueBucket2->putInt64(transValueBucket2, "id", 1); // The value of id is 1
   transValueBucket2->putInt64(transValueBucket2, "data2", 2); // The value of data2 is 2
   transValueBucket2->putReal(transValueBucket2, "data3", 1.2); // The value of data3 is 1.2
       
   int64_t transInsertRow = -1;
   // 支持插入数据时配置冲突策略
   int result = OH_RdbTrans_InsertWithConflictResolution(
       trans, "transaction_table", transValueBucket2, Rdb_ConflictResolution::RDB_CONFLICT_REPLACE, &transInsertRow);
       
   transValueBucket2->destroy(transValueBucket2);
   ```

   ```
   OH_VBucket *transValueBucket3 = OH_Rdb_CreateValuesBucket();
   transValueBucket3->putInt64(transValueBucket3, "id", 1); // The value of id is 1
   transValueBucket3->putInt64(transValueBucket3, "data2", 3); // The value of data2 is 3
   transValueBucket3->putReal(transValueBucket3, "data3", 1.2); // The value of data3 is 1.2

   OH_Predicates *transUpdatePredicates = OH_Rdb_CreatePredicates("transaction_table");
   if (transUpdatePredicates == NULL) {
       OH_LOG_ERROR(LOG_APP, "CreatePredicates failed.");
       transValueBucket3->destroy(transValueBucket3);
       return;
   }
   auto targetValue = OH_Rdb_CreateValueObject();
   int64_t two = 2;
   targetValue->putInt64(targetValue, &two, 1); // The value of id is 1
   transUpdatePredicates->equalTo(transUpdatePredicates, "data2", targetValue);

   int64_t updateRows = -1;
   // 支持更新数据时配置冲突策略
   OH_RdbTrans_UpdateWithConflictResolution(trans, transValueBucket3, transUpdatePredicates,
                                            Rdb_ConflictResolution::RDB_CONFLICT_REPLACE, &updateRows);
   targetValue->destroy(targetValue);
   transValueBucket3->destroy(transValueBucket3);
   transUpdatePredicates->destroy(transUpdatePredicates);
   ```

   ```
   OH_Predicates *predicates = OH_Rdb_CreatePredicates("transaction_table");
   if (predicates == NULL) {
       OH_LOG_ERROR(LOG_APP, "CreatePredicates failed.");
       return;
   }
   const char *columns[] = {"data1", "data2", "data3"};
   // 通过事务对象执行数据查询
   OH_Cursor *cursor = OH_RdbTrans_Query(trans, predicates, columns, sizeof(columns) / sizeof(columns[0]));
   if (cursor == NULL) {
       OH_LOG_ERROR(LOG_APP, "Query failed.");
       predicates->destroy(predicates);
       return;
   }
   int columnCount = 0;
   cursor->getColumnCount(cursor, &columnCount);

   predicates->destroy(predicates);
   cursor->destroy(cursor);
   ```

   ```
   OH_Predicates *predicates2 = OH_Rdb_CreatePredicates("transaction_table");
   if (predicates2 == NULL) {
      OH_LOG_ERROR(LOG_APP, "CreatePredicates failed.");
      return;
   }
   OH_VObject *valueObject = OH_Rdb_CreateValueObject();
   if (valueObject == NULL) {
      OH_LOG_ERROR(LOG_APP, "CreateValueObject failed.");
      predicates2->destroy(predicates2);
      return;
   }
   valueObject->putText(valueObject, "1"); // Change the text value of the object to 1
   predicates2->equalTo(predicates2, "data4", valueObject);
   int64_t changes = -1;
   // 通过事务对象执行数据删除
   int deleteRet = OH_RdbTrans_Delete(trans, predicates2, &changes);
   predicates2->destroy(predicates2);
   valueObject->destroy(valueObject);
   ```

   ```
   // 提交事务
   OH_RdbTrans_Commit(trans);
   // 销毁事务
   OH_RdbTrans_Destroy(trans);
   ```

   ```
   OH_RDB_TransOptions *options2 = OH_RdbTrans_CreateOptions();
   OH_RdbTransOption_SetType(options2, RDB_TRANS_DEFERRED);
   OH_Rdb_Transaction *trans2 = nullptr;
   int transCreateRet = OH_Rdb_CreateTransaction(store_, options2, &trans2);
   OH_RdbTrans_DestroyOptions(options2);

   // 回滚事务
   OH_RdbTrans_Rollback(trans2);
   OH_RdbTrans_Destroy(trans2);
   ```
6. 附加数据库。

   调用OH\_Rdb\_Attach将一个数据库文件附加到当前数据库中，以便在SQL语句中可以直接访问附加数据库中的数据。

   此API不支持附加加密数据库。

   调用attach接口后，数据库切换为非WAL模式，性能会存在一定的劣化。切换模式需要确保所有的OH\_Cursor都已经销毁，所有的写操作已经结束，否则会报错14800015。

   attach不能并发调用，可能出现未响应情况，报错14800015，需要重试。

   当不再使用附加数据时，可调用OH\_Rdb\_Detach分离附加数据库。

   ```
   char attachStoreTableCreateSql[] = "CREATE TABLE IF NOT EXISTS EMPLOYEE (ID INTEGER PRIMARY KEY AUTOINCREMENT, "
       "NAME TEXT NOT NULL, AGE INTEGER, SALARY REAL, CODES BLOB)";
   OH_Rdb_ConfigV2 *attachDbConfig = OH_Rdb_CreateConfig();
   if (attachDbConfig == NULL) {
       OH_LOG_ERROR(LOG_APP, "Create store config failed.");
       return;
   }
   OH_Rdb_SetModuleName(attachDbConfig, "entry");
   OH_Rdb_SetDatabaseDir(attachDbConfig, "/data/storage/el3/database");
   OH_Rdb_SetArea(attachDbConfig, RDB_SECURITY_AREA_EL3);
   OH_Rdb_SetStoreName(attachDbConfig, "RdbAttach.db");
   OH_Rdb_SetSecurityLevel(attachDbConfig, OH_Rdb_SecurityLevel::S3);
   OH_Rdb_SetBundleName(attachDbConfig, "com.example.nativedemo");

   int errCode1 = 0;
   // 创建附加示例数据库 RdbAttach.db
   OH_Rdb_Store *attachStore = OH_Rdb_CreateOrOpen(attachDbConfig, &errCode1);

   if (attachStore == NULL) {
       OH_LOG_ERROR(LOG_APP, "Create attachStore failed, errCode: %{public}d", errCode1);
       OH_Rdb_DestroyConfig(attachDbConfig);
       return;
   }

   if (errCode1 != OH_Rdb_ErrCode::RDB_OK) {
       OH_LOG_ERROR(LOG_APP, "Create attachStore failed, errCode: %{public}d", errCode1);
       OH_Rdb_DestroyConfig(attachDbConfig);
       OH_Rdb_CloseStore(attachStore);
       return;
   }
   errCode1 = OH_Rdb_Execute(attachStore, attachStoreTableCreateSql);
   if (errCode1 != OH_Rdb_ErrCode::RDB_OK) {
       OH_LOG_ERROR(LOG_APP, "Create table failed, errCode: %{public}d", errCode1);
       OH_Rdb_DestroyConfig(attachDbConfig);
       OH_Rdb_CloseStore(attachStore);
       return;
   }
   OH_VBucket *valueBucket = OH_Rdb_CreateValuesBucket();
   valueBucket->putText(valueBucket, "NAME", "Lisa");
   valueBucket->putInt64(valueBucket, "AGE", 18); // The value of AGE is 18
   valueBucket->putReal(valueBucket, "SALARY", 100.5); // The value of SALARY is 100.5
   uint8_t arr[] = {1, 2, 3, 4, 5};
   int len = sizeof(arr) / sizeof(arr[0]);
   valueBucket->putBlob(valueBucket, "CODES", arr, len);
   int rowId = OH_Rdb_Insert(attachStore, "EMPLOYEE", valueBucket);
   OH_LOG_INFO(LOG_APP, "Insert data result: %{public}d", rowId);
   valueBucket->destroy(valueBucket);
   OH_Rdb_CloseStore(attachStore);
   // ...
   // 附加数据库
   size_t attachedNumber = 0;
   // The maximum waiting time allowed for attaching databases is 10
   errCode = OH_Rdb_Attach(store_, attachDbConfig, "attach", 10, &attachedNumber);
   OH_Rdb_DestroyConfig(attachDbConfig);
   if (errCode != OH_Rdb_ErrCode::RDB_OK) {
       OH_LOG_ERROR(LOG_APP, "Attach store failed, errCode: %{public}d", errCode);
       return;
   }
   OH_Predicates *predicates = OH_Rdb_CreatePredicates("attach.EMPLOYEE");
   if (predicates == NULL) {
       OH_LOG_ERROR(LOG_APP, "CreatePredicates failed.");
       // The maximum waiting time allowed for detaching databases is 10
       errCode = OH_Rdb_Detach(store_, "attach", 10, &attachedNumber);
       OH_LOG_INFO(LOG_APP, "Detach result: %{public}d", errCode);
       return;
   }
   char *colName[] = {};
   int len = sizeof(colName) / sizeof(colName[0]);
   OH_Cursor *cursor = OH_Rdb_Query(store_, predicates, colName, len);
   if (cursor == NULL) {
       OH_LOG_ERROR(LOG_APP, "Query failed.");
       // The maximum waiting time allowed for detaching databases is 10
       errCode = OH_Rdb_Detach(store_, "attach", 10, &attachedNumber);
       OH_LOG_INFO(LOG_APP, "Detach result: %{public}d", errCode);
       predicates->destroy(predicates);
       return;
   }
   int rowCount = -1;
   errCode = cursor->getRowCount(cursor, &rowCount);
   if (errCode != OH_Rdb_ErrCode::RDB_OK) {
       OH_LOG_ERROR(LOG_APP, "Get row count failed, errCode: %{public}d", errCode);
   } else {
       OH_LOG_INFO(LOG_APP, "Query success, row count: %{public}d", rowCount);
   }
   cursor->destroy(cursor);
   predicates->destroy(predicates);
   // 分离数据库
   // The maximum waiting time allowed for detaching databases is 10
   errCode = OH_Rdb_Detach(store_, "attach", 10, &attachedNumber);
   OH_LOG_INFO(LOG_APP, "Detach result: %{public}d", errCode);
   ```
7. 向数据库表中插入资产类型数据。

   ```
   // 列的属性为单个资产类型时，sql语句中应指定为asset，多个资产类型应指定为assets。
   char createAssetTableSql[] = "CREATE TABLE IF NOT EXISTS asset_table (id INTEGER PRIMARY KEY AUTOINCREMENT,"
       "data1 ASSET, data2 ASSETS );";
   const char *table = "asset_table";
   int errCode = OH_Rdb_Execute(store_, createAssetTableSql);
   OH_VBucket *valueBucket = OH_Rdb_CreateValuesBucket();
   Data_Asset *asset = OH_Data_Asset_CreateOne();
   OH_Data_Asset_SetName(asset, "name0");
   OH_Data_Asset_SetUri(asset, "uri0");
   OH_Data_Asset_SetPath(asset, "path0");
   OH_Data_Asset_SetCreateTime(asset, 1); // Set the creation time of Data_Asset to 1
   OH_Data_Asset_SetModifyTime(asset, 1); // Set the modify time of Data_Asset to 1
   OH_Data_Asset_SetSize(asset, 1); // Set the size of the Data_Asset to 1
   OH_Data_Asset_SetStatus(asset, Data_AssetStatus::ASSET_NORMAL);
   errCode = OH_VBucket_PutAsset(valueBucket, "data1", asset);

   Data_Asset **assets = OH_Data_Asset_CreateMultiple(2);

   OH_Data_Asset_SetName(assets[0], "name0");
   OH_Data_Asset_SetUri(assets[0], "uri0");
   OH_Data_Asset_SetPath(assets[0], "path0");
   OH_Data_Asset_SetCreateTime(assets[0], 1); // Set the creation time of Data_Asset to 1
   OH_Data_Asset_SetModifyTime(assets[0], 1); // Set the modify time of Data_Asset to 1
   OH_Data_Asset_SetSize(assets[0], 1); // Set the size of the Data_Asset to 1
   OH_Data_Asset_SetStatus(assets[0], Data_AssetStatus::ASSET_NORMAL);

   OH_Data_Asset_SetName(assets[1], "name1");
   OH_Data_Asset_SetUri(assets[1], "uri1");
   OH_Data_Asset_SetPath(assets[1], "path1");
   OH_Data_Asset_SetCreateTime(assets[1], 1); // Set the creation time of Data_Asset to 1
   OH_Data_Asset_SetModifyTime(assets[1], 1); // Set the modify time of Data_Asset to 1
   OH_Data_Asset_SetSize(assets[1], 1); // Set the size of the Data_Asset to 1
   OH_Data_Asset_SetStatus(assets[1], Data_AssetStatus::ASSET_NORMAL);

   uint32_t assetsCount = 2;
   errCode = OH_VBucket_PutAssets(valueBucket, "data2", assets, assetsCount);
   int rowID = OH_Rdb_Insert(store_, table, valueBucket);
   // 释放Data_Asset*和Data_Asset**
   OH_Data_Asset_DestroyMultiple(assets, assetsCount);
   OH_Data_Asset_DestroyOne(asset);
   valueBucket->destroy(valueBucket);
   ```
8. 从结果集中读取资产类型数据。

   ```
   OH_Predicates *predicates = OH_Rdb_CreatePredicates("asset_table");
   if (predicates == NULL) {
       OH_LOG_ERROR(LOG_APP, "CreatePredicates failed.");
       return;
   }
   OH_Cursor *cursor = OH_Rdb_Query(store_, predicates, NULL, 0);
   if (cursor == NULL) {
       predicates->destroy(predicates);
   } else {
       cursor->goToNextRow(cursor);
       
       uint32_t assetCount = 0;
       // assetCount作为出参获取该列资产类型数据的数量
       int errCode = cursor->getAssets(cursor, 2, nullptr, &assetCount); // Column index is 2
       Data_Asset **assets = OH_Data_Asset_CreateMultiple(assetCount);
       errCode = cursor->getAssets(cursor, 2, assets, &assetCount); // Column index is 2
       // The number of Data_Assets is 2
       if (assetCount < 2) {
           predicates->destroy(predicates);
           cursor->destroy(cursor);
       } else {
           Data_Asset *asset = assets[1];
           char name[10] = "";
           size_t nameLength = 10;
           errCode = OH_Data_Asset_GetName(asset, name, &nameLength);
           
           char uri[10] = "";
           size_t uriLength = 10;
           errCode = OH_Data_Asset_GetUri(asset, uri, &uriLength);
           
           char path[10] = "";
           size_t pathLength = 10;
           errCode = OH_Data_Asset_GetPath(asset, path, &pathLength);
           
           int64_t createTime = 0;
           errCode = OH_Data_Asset_GetCreateTime(asset, &createTime);
           
           int64_t modifyTime = 0;
           errCode = OH_Data_Asset_GetModifyTime(asset, &modifyTime);
           
           size_t size = 0;
           errCode = OH_Data_Asset_GetSize(asset, &size);
           
           Data_AssetStatus status = Data_AssetStatus::ASSET_NULL;
           errCode = OH_Data_Asset_GetStatus(asset, &status);
           
           predicates->destroy(predicates);
           OH_Data_Asset_DestroyMultiple(assets, assetCount);
           cursor->destroy(cursor);
       }
   }
   ```
9. 查询数据的最后修改时间。调用OH\_Rdb\_FindModifyTime查询指定表中指定列的数据的最后修改时间，该接口返回一个有两列数据的OH\_Cursor对象，第一列为传入的主键/RowId，第二列为最后修改时间。示例代码如下所示：

   ```
   constexpr uint32_t  tableCount = 1;
   const char *table[tableCount];
   table[0] = "EMPLOYEE";
   Rdb_DistributedConfig distributedConfig{ .version = 1, .isAutoSync = true };
   // 设置分布式表
   OH_Rdb_SetDistributedTables(store_, table, tableCount, RDB_DISTRIBUTED_CLOUD, &distributedConfig);
   // 查询数据的最后修改时间
   OH_VObject *values = OH_Rdb_CreateValueObject();
   int64_t keys[] = { 1 };
   values->putInt64(values, keys, 1); // The value of keys is 1
   OH_Cursor *cursor = OH_Rdb_FindModifyTime(store_, "EMPLOYEE", "ROWID", values);
   if (cursor == NULL) {
       return;
   }
   while (cursor->goToNextRow(cursor) == OH_Rdb_ErrCode::RDB_OK) {
       int64_t rowId;
       cursor->getInt64(cursor, 1, &rowId); // 1 is the column index
   }
   ```
10. 删除数据库。调用OH\_Rdb\_DeleteStoreV2方法，删除数据库及数据库相关文件。示例代码如下：

    ```
    // 释放数据库实例
    OH_Rdb_CloseStore(store_);
    // 删除数据库文件
    OH_Rdb_DeleteStoreV2(config);
    ```
