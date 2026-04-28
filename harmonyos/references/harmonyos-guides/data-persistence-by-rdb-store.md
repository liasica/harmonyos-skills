---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-persistence-by-rdb-store
title: 通过关系型数据库实现数据持久化 (ArkTS)
breadcrumb: 指南 > 应用框架 > ArkData（方舟数据管理） > 应用数据持久化 > 通过关系型数据库实现数据持久化 (ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e4a414a6178ff5cfd960fdfaa072424ccd257a077c20ec098145b345b899c27f
---

## 场景介绍

关系型数据库基于SQLite组件，适用于存储包含复杂关系数据的场景，比如一个班级的学生信息，需要包括姓名、学号、各科成绩等，又或者公司的雇员信息，需要包括姓名、工号、职位等，由于数据之间有较强的对应关系，复杂程度比键值型数据更高，此时需要使用关系型数据库来持久化保存数据。

大数据量场景下查询数据可能会导致耗时长甚至应用卡死，如有相关操作可参考文档[批量数据写数据库场景](batch-database-operations-guide.md)，且有建议如下：

* 单次查询数据量不超过5000条。
* 在[TaskPool](../harmonyos-references/js-apis-taskpool.md)中查询。
* 拼接SQL语句尽量简洁。
* 合理地分批次查询。

## 基本概念

* **谓词**：数据库中用来代表数据实体的性质、特征或者数据实体之间关系的词项，主要用来定义数据库的操作条件。
* **结果集**：指用户查询之后的结果集合，可以对数据进行访问。结果集提供了灵活的数据访问方式，可以更方便地拿到用户想要的数据。

## 运作机制

关系型数据库对应用提供通用的操作接口，底层使用SQLite作为持久化存储引擎，支持SQLite具有的数据库特性，包括但不限于事务、索引、视图、触发器、外键、参数化查询和预编译SQL语句。

**图1** 关系型数据库运作机制

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/Xn7jYJc_TGq8zPcVHxLZXA/zh-cn_image_0000002552957522.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T233815Z&HW-CC-Expire=86400&HW-CC-Sign=761C05DD150EA6EEC9EBB661D4668331FAA66ADA2F8CCDF27FACFF8ADBD49B98)

## 约束限制

* 系统默认日志方式是[WAL](data-terminology.md#wal模式)（Write Ahead Log）模式，系统默认落盘方式是[FULL模式](data-terminology.md#full模式)。
* 数据库中常驻有4个读连接和1个写连接。读连接会动态扩充，无可用读连接时，会创建新的读连接执行读操作。写连接不会动态扩充，无可用写连接时，会等待连接释放后执行写操作。
* 为保证数据的准确性，数据库同一时间只能支持一个写操作。
* 当应用被卸载完成后，设备上的相关数据库文件及临时文件会被自动清除。
* ArkTS侧支持的基本数据类型：number、string、二进制类型数据、boolean。
* 为保证插入并读取数据成功，建议一条数据不要超过2M。超出该大小，插入成功，读取失败。

## 接口说明

以下是关系型数据库持久化功能的相关接口，更多接口及使用方式请见[@ohos.data.relationalStore (关系型数据库)](../harmonyos-references/arkts-apis-data-relationalstore.md)。

| 接口名称 | 描述 |
| --- | --- |
| getRdbStore(context: Context, config: StoreConfig, callback: AsyncCallback<RdbStore>): void | 获得一个RdbStore，操作关系型数据库，用户可以根据自己的需求配置RdbStore的参数，然后通过RdbStore调用相关接口可以执行相关的数据操作。 |
| createTransaction(options?: TransactionOptions): Promise<Transaction> | 创建一个事务对象并开始事务。 |
| execute(sql: string, args?: Array<ValueType>):Promise<ValueType> | 执行包含指定参数的SQL语句。 |
| querySql(sql: string, bindArgs?: Array<ValueType>):Promise<ResultSet> | 根据指定SQL语句查询数据库中的数据。 |
| insert(table: string, values: ValuesBucket, conflict?: ConflictResolution): Promise<number> | 向目标表中插入一行数据。 |
| update(values: ValuesBucket, predicates: RdbPredicates, callback: AsyncCallback<number>):void | 根据predicates的指定实例对象更新数据库中的数据。 |
| delete(predicates: RdbPredicates, callback: AsyncCallback<number>):void | 根据predicates的指定实例对象从数据库中删除数据。 |
| query(predicates: RdbPredicates, columns: Array<string>, callback: AsyncCallback<ResultSet>):void | 根据指定条件查询数据库中的数据。 |
| deleteRdbStore(context: Context, name: string, callback: AsyncCallback<void>): void | 删除数据库。 |
| isTokenizerSupported(tokenizer: Tokenizer): boolean | 判断当前平台是否支持传入的分词器（将文本分解为更小单元的工具，这些单元可以是单词、子词、字符或者其他语言片段）。 |

## 开发步骤

因Stage模型、FA模型的差异，个别示例代码提供了在两种模型下的对应示例；示例代码未区分模型或没有对应注释说明时默认在两种模型下均适用。

关系型数据库操作或者存储过程中，有可能会因为各种原因发生非预期的数据库异常情况（抛出14800011），此时需要对数据库进行重建并恢复数据，以保障正常的应用开发，具体可见[关系型数据库异常重建](data-backup-and-restore.md#关系型数据库异常重建)。

1. 使用关系型数据库实现数据持久化，需要获取一个RdbStore，其中包括建库、建表、升降级等操作。推荐使用事务接口保证数据库升级流程原子性。

   示例代码如下所示：

   Stage模型示例：

   ```
   1. import { relationalStore } from '@kit.ArkData'; // 导入模块
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   4. const DOMAIN = 0x0000;

   6. let store: relationalStore.RdbStore | undefined = undefined;
   7. let tokenType = relationalStore.Tokenizer.ICU_TOKENIZER;
   8. let tokenTypeSupported = relationalStore.isTokenizerSupported(tokenType);
   9. if (!tokenTypeSupported) {
   10. tokenType = relationalStore.Tokenizer.NONE_TOKENIZER;
   11. hilog.error(DOMAIN, 'rdbDataPersistence', `ICU_TOKENIZER is not supported on this platform.`);
   12. }
   13. const STORE_CONFIG: relationalStore.StoreConfig = {
   14. // 数据库文件名
   15. name: 'RdbTest.db',
   16. // 数据库安全级别
   17. securityLevel: relationalStore.SecurityLevel.S3,
   18. // 可选参数，指定数据库是否加密，默认不加密
   19. encrypt: false,
   20. // 可选参数，数据库自定义路径。默认在本应用沙箱目录下创建RdbStore实例。
   21. customDir: 'customDir/subCustomDir',
   22. // 可选参数，指定数据库是否以只读方式打开。默认为false，表示数据库可读可写。为true时，只允许从数据库读取数据，不允许对数据库进行写操作，否则会返回错误码801。
   23. isReadOnly: false,
   24. // 可选参数，指定用户在全文搜索场景(FTS)下使用哪种分词器。默认在FTS下仅支持英文分词，不支持其他语言分词。
   25. tokenizer: tokenType,
   26. };
   27. // ...
   28. // 判断数据库版本，如果不匹配则需进行升降级操作
   29. // 假设当前数据库版本为3，表结构：EMPLOYEE (NAME, AGE, SALARY, CODES, IDENTITY)
   30. // 建表Sql语句, IDENTITY为bigint类型，sql中指定类型为UNLIMITED INT
   31. const SQL_CREATE_TABLE =
   32. 'CREATE TABLE IF NOT EXISTS EMPLOYEE (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, AGE INTEGER, SALARY REAL, CODES BLOB, ADDRESS TEXT)';
   33. if (store === undefined) {
   34. try {
   35. store = await relationalStore.getRdbStore(context, STORE_CONFIG);
   36. } catch (e) {
   37. const err = e as BusinessError;
   38. hilog.error(DOMAIN, 'rdbDataPersistence', `Failed to get RdbStore. Code:${err.code}, message:${err.message}`);
   39. return;
   40. }
   41. }
   42. hilog.info(DOMAIN, 'rdbDataPersistence', 'Succeeded in getting RdbStore.');
   43. if (store !== undefined) {
   44. let transaction = await store.createTransaction({});
   45. let storeVersion = await transaction.execute('PRAGMA user_version');
   46. // 当数据库创建时，数据库默认版本为0
   47. // 示例应用升级流程较短，所以使用单个事务。如果实际业务中升级逻辑较多，建议拆分多个独立事务串行执行。
   48. if (storeVersion === 0) {
   49. try {
   50. await transaction.execute(SQL_CREATE_TABLE); // 创建数据表，以便后续调用insert接口插入数据
   51. storeVersion = 1;
   52. hilog.info(DOMAIN, 'rdbDataPersistence', 'Upgrade store version from 0 to 1 success.');
   53. // 设置数据库的版本，入参为大于0的整数
   54. } catch (e) {
   55. const err = e as BusinessError;
   56. await transaction.rollback();
   57. hilog.error(DOMAIN, 'rdbDataPersistence', `Failed to execute sql. Code:${err.code}, message:${err.message}`);
   58. return;
   59. }
   60. }
   61. // 如果数据库版本不为0且和当前数据库版本不匹配，需要进行升降级操作
   62. // 当前数据库存在并且版本为1，数据库需要从1版本升级到2版本
   63. if (storeVersion === 1) {
   64. // version = 1：表结构：EMPLOYEE (NAME, AGE, SALARY, CODES, ADDRESS)
   65. // => version = 2：表结构：EMPLOYEE (NAME, AGE, SALARY, CODES, ADDRESS, IDENTITY)
   66. try {
   67. await transaction.execute('ALTER TABLE EMPLOYEE ADD COLUMN IDENTITY UNLIMITED INT');
   68. storeVersion = 2;
   69. hilog.info(DOMAIN, 'rdbDataPersistence', 'Upgrade store version from 1 to 2 success.');
   70. } catch (e) {
   71. const err = e as BusinessError;
   72. await transaction.rollback();
   73. hilog.error(DOMAIN, 'rdbDataPersistence', `Failed to execute sql. Code:${err.code}, message:${err.message}`);
   74. return;
   75. }
   76. }
   77. // 当前数据库存在并且版本为2，数据库需要从2版本升级到3版本
   78. if (storeVersion === 2) {
   79. // version = 2：表结构：EMPLOYEE (NAME, AGE, SALARY, CODES, ADDRESS, IDENTITY)
   80. // => version = 3：表结构：EMPLOYEE (NAME, AGE, SALARY, CODES, IDENTITY)
   81. try {
   82. await transaction.execute('ALTER TABLE EMPLOYEE DROP COLUMN ADDRESS');
   83. storeVersion = 3;
   84. await transaction.execute('PRAGMA user_version = 3');
   85. hilog.info(DOMAIN, 'rdbDataPersistence', 'Upgrade store version from 2 to 3 success.')
   86. } catch (e) {
   87. const err = e as BusinessError;
   88. await transaction.rollback();
   89. hilog.error(DOMAIN, 'rdbDataPersistence', `Failed to execute sql. Code:${err.code}, message:${err.message}`);
   90. return;
   91. }
   92. }
   93. await transaction.commit();
   94. // 请确保获取到RdbStore实例，完成数据表创建后，再进行数据库的增、删、改、查等操作
   95. }
   ```

   [RdbDataPersistence.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/RelationalStore/DataSyncAndPersistence/entry/src/main/ets/pages/datapersistence/RdbDataPersistence.ets#L16-L115)

   FA模型示例：

   ```
   1. import { relationalStore } from '@kit.ArkData'; // 导入模块
   2. import { featureAbility } from '@kit.AbilityKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. let context = featureAbility.getContext();

   7. const STORE_CONFIG: relationalStore.StoreConfig = {
   8. name: 'RdbTest.db', // 数据库文件名
   9. securityLevel: relationalStore.SecurityLevel.S3 // 数据库安全级别
   10. };

   12. // 假设当前数据库版本为3，表结构：EMPLOYEE (NAME, AGE, SALARY, CODES, IDENTITY)
   13. // 建表Sql语句，IDENTITY为bigint类型，sql中指定类型为UNLIMITED INT
   14. const SQL_CREATE_TABLE =
   15. 'CREATE TABLE IF NOT EXISTS EMPLOYEE (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, AGE INTEGER, SALARY REAL, CODES BLOB, IDENTITY UNLIMITED INT)';

   17. relationalStore.getRdbStore(context, STORE_CONFIG, async (err, store) => {
   18. if (err) {
   19. console.error(`Failed to get RdbStore. Code:${err.code}, message:${err.message}`);
   20. return;
   21. }
   22. console.info('Succeeded in getting RdbStore.');

   24. let storeVersion = store.version;
   25. // 当数据库创建时，数据库默认版本为0
   26. if (storeVersion === 0) {
   27. try {
   28. await store.execute(SQL_CREATE_TABLE); // 创建数据表，以便后续调用insert接口插入数据
   29. // 设置数据库的版本，入参为大于0的整数
   30. storeVersion = 3;
   31. } catch (e) {
   32. const err = e as BusinessError;
   33. console.error(`Failed to execute sql. Code:${err.code}, message:${err.message}`);
   34. }
   35. }

   37. // 如果数据库版本不为0且和当前数据库版本不匹配，需要进行升降级操作
   38. // 当前数据库存在并且版本为1，数据库需要从1版本升级到2版本
   39. if (storeVersion === 1) {
   40. try {
   41. // version = 1：表结构：EMPLOYEE (NAME, SALARY, CODES, ADDRESS) => version = 2：表结构：EMPLOYEE (NAME, AGE, SALARY, CODES, ADDRESS)
   42. await store.execute('ALTER TABLE EMPLOYEE ADD COLUMN AGE INTEGER');
   43. storeVersion = 2;
   44. console.info("Upgrade store version from 1 to 2 success.")
   45. } catch (e) {
   46. const err = e as BusinessError;
   47. console.error(`Failed to execute sql. Code:${err.code}, message:${err.message}`);
   48. }
   49. }

   51. // 当前数据库存在并且版本为2，数据库需要从2版本升级到3版本
   52. if (storeVersion === 2) {
   53. try {
   54. // version = 2：表结构：EMPLOYEE (NAME, AGE, SALARY, CODES, ADDRESS) => version = 3：表结构：EMPLOYEE (NAME, AGE, SALARY, CODES)
   55. await store.execute('ALTER TABLE EMPLOYEE DROP COLUMN ADDRESS');
   56. storeVersion = 3;
   57. console.info("Upgrade store version from 2 to 3 success.")
   58. } catch (e) {
   59. const err = e as BusinessError;
   60. console.error(`Failed to execute sql. Code:${err.code}, message:${err.message}`);
   61. }
   62. }
   63. store.version = storeVersion;
   64. // 请确保获取到RdbStore实例，完成数据表创建后，再进行数据库的增、删、改、查等操作
   65. });
   ```

   说明

   * 应用创建的数据库与其上下文（Context）有关，即使使用同样的数据库名称，但不同的应用上下文，会产生多个数据库，例如每个UIAbility都有各自的上下文。
   * 当应用首次获取数据库（调用getRdbStore）后，在应用沙箱内会产生对应的数据库文件。使用数据库的过程中，在与数据库文件相同的目录下可能会产生以-wal和-shm结尾的临时文件。此时若开发者希望移动数据库文件到其它地方使用查看，则需要同时移动这些临时文件，当应用被卸载完成后，其在设备上产生的数据库文件及临时文件也会被移除。
   * 错误码的详细介绍请参见[通用错误码](../harmonyos-references/errorcode-universal.md)和[关系型数据库错误码](../harmonyos-references/errorcode-data-rdb.md)。
2. 获取到RdbStore，完成数据表创建后，调用insert()接口插入数据。示例代码如下所示：

   ```
   1. // 插入数据
   2. let value1 = 'Lisa';
   3. let value2 = 18;
   4. let value3 = 100.5;
   5. let value4 = new Uint8Array([1, 2, 3, 4, 5]);
   6. let value5 = BigInt('15822401018187971961171');
   7. const valueBucket: relationalStore.ValuesBucket = {
   8. NAME: value1,
   9. AGE: value2,
   10. SALARY: value3,
   11. CODES: value4,
   12. IDENTITY: value5,
   13. };
   14. if (store !== undefined) {
   15. try {
   16. const rowId = await store.insert('EMPLOYEE', valueBucket);
   17. hilog.info(DOMAIN, 'rdbDataPersistence', `Succeeded in inserting data. rowId:${rowId}`);
   18. } catch (error) {
   19. const err = error as BusinessError;
   20. hilog.error(DOMAIN, 'rdbDataPersistence', `Failed to insert data. Code:${err.code}, message:${err.message}`);
   21. }
   22. }
   ```

   [RdbDataPersistence.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/RelationalStore/DataSyncAndPersistence/entry/src/main/ets/pages/datapersistence/RdbDataPersistence.ets#L117-L140)

   说明

   关系型数据库没有显式的flush操作实现持久化，数据插入即保存在持久化文件。
3. 根据谓词指定的实例对象，对数据进行修改或删除。

   调用update()方法修改数据，调用delete()方法删除数据。示例代码如下所示：

   ```
   1. // 修改数据、删除数据
   2. let value6 = 'Rose';
   3. let value7 = 22;
   4. let value8 = 200.5;
   5. let value9 = new Uint8Array([1, 2, 3, 4, 5]);
   6. let value10 = BigInt('15822401018187971967863');
   7. const valueBucket2: relationalStore.ValuesBucket = {
   8. NAME: value6,
   9. AGE: value7,
   10. SALARY: value8,
   11. CODES: value9,
   12. IDENTITY: value10,
   13. };

   15. // 修改数据
   16. let predicates1 = new relationalStore.RdbPredicates('EMPLOYEE'); // 创建表'EMPLOYEE'的predicates
   17. predicates1.equalTo('NAME', 'Lisa'); // 匹配表'EMPLOYEE'中'NAME'为'Lisa'的字段
   18. if (store !== undefined) {
   19. (store as relationalStore.RdbStore).update(valueBucket2, predicates1, (err: BusinessError, rows: number) => {
   20. if (err) {
   21. hilog.error(DOMAIN, 'rdbDataPersistence', `Failed to update data. Code:${err.code}, message:${err.message}`);
   22. return;
   23. }
   24. hilog.info(DOMAIN, 'rdbDataPersistence', `Succeeded in updating data. row count: ${rows}`);
   25. })
   26. }

   28. // 删除数据
   29. predicates1 = new relationalStore.RdbPredicates('EMPLOYEE');
   30. predicates1.equalTo('NAME', 'Lisa');
   31. if (store !== undefined) {
   32. (store as relationalStore.RdbStore).delete(predicates1, (err: BusinessError, rows: number) => {
   33. if (err) {
   34. hilog.error(DOMAIN, 'rdbDataPersistence', `Failed to delete data. Code:${err.code}, message:${err.message}`);
   35. return;
   36. }
   37. hilog.info(DOMAIN, 'rdbDataPersistence', `Delete rows: ${rows}`);
   38. })
   39. }
   ```

   [RdbDataPersistence.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/RelationalStore/DataSyncAndPersistence/entry/src/main/ets/pages/datapersistence/RdbDataPersistence.ets#L142-L182)
4. 根据谓词指定的查询条件查找数据。

   调用query()方法查找数据，返回一个ResultSet结果集。示例代码如下所示：

   ```
   1. // 查找数据
   2. let predicates2 = new relationalStore.RdbPredicates('EMPLOYEE');
   3. predicates2.equalTo('NAME', 'Rose');
   4. if (store !== undefined) {
   5. (store as relationalStore.RdbStore).query(predicates2, ['ID', 'NAME', 'AGE', 'SALARY', 'CODES', 'IDENTITY'], (err: BusinessError, resultSet) => {
   6. if (err) {
   7. hilog.error(DOMAIN, 'rdbDataPersistence', `Failed to query data. Code:${err.code}, message:${err.message}`);
   8. return;
   9. }
   10. hilog.info(DOMAIN, 'rdbDataPersistence', `ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}`);
   11. // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
   12. while (resultSet.goToNextRow()) {
   13. const id = resultSet.getLong(resultSet.getColumnIndex('ID'));
   14. const name = resultSet.getString(resultSet.getColumnIndex('NAME'));
   15. const age = resultSet.getLong(resultSet.getColumnIndex('AGE'));
   16. const salary = resultSet.getDouble(resultSet.getColumnIndex('SALARY'));
   17. const identity = resultSet.getValue(resultSet.getColumnIndex('IDENTITY'));
   18. hilog.info(DOMAIN, 'rdbDataPersistence', `id=${id}, name=${name}, age=${age}, salary=${salary}, identity=${identity}`);
   19. }
   20. // 释放数据集的内存
   21. resultSet.close();
   22. })
   23. }
   ```

   [RdbDataPersistence.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/RelationalStore/DataSyncAndPersistence/entry/src/main/ets/pages/datapersistence/RdbDataPersistence.ets#L184-L208)

   说明

   当应用完成查询数据操作，不再使用结果集（ResultSet）时，请及时调用close方法关闭结果集，释放系统为其分配的内存。

   当前RDB还支持进行FTS全文检索，可以根据中文或者英文进行文本检索，针对中文分词器支持ICU分词器。

   以中文关键字检索为例：

   ```
   1. // 中文关键字检索，查找数据
   2. if (store !== undefined && tokenTypeSupported) {
   3. // 创建全文检索表
   4. const SQL_CREATE_TABLE = 'CREATE VIRTUAL TABLE IF NOT EXISTS example USING fts4(name, content, tokenize=icu zh_CN)';
   5. try {
   6. await store.execute(SQL_CREATE_TABLE);
   7. hilog.info(DOMAIN, 'rdbDataPersistence', 'Succeeded in creating fts table.');
   8. } catch (error) {
   9. const err = error as BusinessError;
   10. hilog.error(DOMAIN, 'rdbDataPersistence', `Failed to creating fts table. code: ${err.code}, message: ${err.message}.`);
   11. }
   12. }
   13. if (store !== undefined) {
   14. try {
   15. const resultSet = await store.querySql('SELECT name FROM example WHERE example MATCH ?', ['测试']);
   16. while (resultSet.goToNextRow()) {
   17. const name = resultSet.getValue(resultSet.getColumnIndex('name'));
   18. hilog.info(DOMAIN, 'rdbDataPersistence', `name=${name}`);
   19. }
   20. resultSet.close();
   21. } catch (error) {
   22. const err = error as BusinessError;
   23. hilog.error(DOMAIN, 'rdbDataPersistence', `Query failed. code: ${err.code}, message: ${err.message}.`);
   24. }
   25. }
   ```

   [RdbDataPersistence.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/RelationalStore/DataSyncAndPersistence/entry/src/main/ets/pages/datapersistence/RdbDataPersistence.ets#L210-L236)
5. 使用事务对象执行数据的插入、删除和更新操作。

   调用createTransaction方法创建事务对象并执行相应操作。

   支持配置的事务类型有DEFERRED、IMMEDIATE和EXCLUSIVE，默认为DEFERRED。

   具体信息请参见[关系型数据库](../harmonyos-references/arkts-apis-data-relationalstore-rdbstore.md#createtransaction14)。

   ```
   1. // 使用事务对象执行数据的插入、删除和更新操作
   2. if (store !== undefined) {
   3. // 创建事务对象
   4. try {
   5. const transaction = await store.createTransaction();
   6. try {
   7. // 使用事务对象插入数据
   8. const rowId = await transaction.insert(
   9. 'EMPLOYEE',
   10. {
   11. NAME: 'Lisa',
   12. AGE: 18,
   13. SALARY: 100.5,
   14. CODES: new Uint8Array([1, 2, 3, 4, 5]),
   15. IDENTITY: BigInt('15822401018187971967763')
   16. },
   17. relationalStore.ConflictResolution.ON_CONFLICT_REPLACE
   18. );
   19. hilog.info(DOMAIN, 'rdbDataPersistence', `Insert is successful, rowId = ${rowId}`);

   21. const predicates = new relationalStore.RdbPredicates('EMPLOYEE');
   22. predicates.equalTo('NAME', 'Lisa');
   23. // 使用事务对象更新数据
   24. const rows = await transaction.update(
   25. {
   26. NAME: 'Rose',
   27. AGE: 22,
   28. SALARY: 200.5,
   29. CODES: new Uint8Array([1, 2, 3, 4, 5]),
   30. IDENTITY: BigInt('15822401018187971967763')
   31. },
   32. predicates,
   33. relationalStore.ConflictResolution.ON_CONFLICT_REPLACE
   34. );
   35. hilog.info(DOMAIN, 'rdbDataPersistence', `Updated row count: ${rows}`);

   37. // 使用事务对象删除数据
   38. await transaction.execute('DELETE FROM EMPLOYEE WHERE age = ? OR age = ?', [21, 20]);
   39. hilog.info(DOMAIN, 'rdbDataPersistence', `execute delete success`);

   41. // 提交事务
   42. await transaction.commit();
   43. hilog.info(DOMAIN, 'rdbDataPersistence', 'Transaction commit success.');
   44. } catch (error) {
   45. const err = error as BusinessError;
   46. // 执行失败回滚事务
   47. await transaction.rollback();
   48. hilog.error(DOMAIN, 'rdbDataPersistence', `Transaction execute failed, code is ${err.code}, message is ${err.message}`);
   49. }
   50. } catch (error) {
   51. const err = error as BusinessError;
   52. hilog.error(DOMAIN, 'rdbDataPersistence', `createTransaction failed, code is ${err.code}, message is ${err.message}`);
   53. }
   54. }
   ```

   [RdbDataPersistence.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/RelationalStore/DataSyncAndPersistence/entry/src/main/ets/pages/datapersistence/RdbDataPersistence.ets#L238-L293)
6. 在同路径下备份数据库。关系型数据库支持手动备份和自动备份（仅系统应用可用）两种方式，具体可见[关系型数据库备份](data-backup-and-restore.md#关系型数据库备份)。

   此处以手动备份为例：

   ```
   1. // 在同路径下备份数据库
   2. if (store !== undefined) {
   3. // 'Backup.db'为备份数据库文件名，默认在RdbStore同路径下备份。也可指定路径：customDir + 'Backup.db'
   4. (store as relationalStore.RdbStore).backup('Backup.db', (err: BusinessError) => {
   5. if (err) {
   6. hilog.error(DOMAIN, 'rdbDataPersistence', `Failed to backup RdbStore. Code:${err.code}, message:${err.message}`);
   7. return;
   8. }
   9. hilog.info(DOMAIN, 'rdbDataPersistence', `Succeeded in backing up RdbStore.`);
   10. })
   11. }
   ```

   [RdbDataPersistence.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/RelationalStore/DataSyncAndPersistence/entry/src/main/ets/pages/datapersistence/RdbDataPersistence.ets#L295-L307)
7. 从备份数据库中恢复数据。关系型数据库支持两种方式：恢复手动备份数据和恢复自动备份数据（仅系统应用可用），具体可见[关系型数据库数据恢复](data-backup-and-restore.md#关系型数据库数据恢复)。

   此处以调用[restore](../harmonyos-references/arkts-apis-data-relationalstore-rdbstore.md#restore)接口恢复手动备份数据为例：

   ```
   1. // 备份数据库中恢复数据
   2. if (store !== undefined) {
   3. (store as relationalStore.RdbStore).restore('Backup.db', (err: BusinessError) => {
   4. if (err) {
   5. hilog.error(DOMAIN, 'rdbDataPersistence', `Failed to restore RdbStore. Code:${err.code}, message:${err.message}`);
   6. return;
   7. }
   8. hilog.info(DOMAIN, 'rdbDataPersistence', `Succeeded in restoring RdbStore.`);
   9. })
   10. }
   ```

   [RdbDataPersistence.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/RelationalStore/DataSyncAndPersistence/entry/src/main/ets/pages/datapersistence/RdbDataPersistence.ets#L309-L320)
8. 删除数据库。

   调用deleteRdbStore()方法，删除数据库及数据库相关文件。示例代码如下：

   Stage模型示例：

   ```
   1. // 删除数据库
   2. relationalStore.deleteRdbStore(context, 'RdbTest.db', (err: BusinessError) => {
   3. if (err) {
   4. hilog.error(DOMAIN, 'rdbDataPersistence', `Failed to delete RdbStore. Code:${err.code}, message:${err.message}`);
   5. return;
   6. }
   7. hilog.info(DOMAIN, 'rdbDataPersistence', 'Succeeded in deleting RdbStore.');
   8. });
   ```

   [RdbDataPersistence.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/RelationalStore/DataSyncAndPersistence/entry/src/main/ets/pages/datapersistence/RdbDataPersistence.ets#L322-L331)
