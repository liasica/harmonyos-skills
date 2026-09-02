---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-persistence-by-rdb-store
title: 通过关系型数据库实现数据持久化 (ArkTS)
breadcrumb: 指南 > 应用框架 > ArkData（方舟数据管理） > 应用数据持久化 > 通过关系型数据库实现数据持久化 (ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:11+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:176653882ac323671ee341f15661298b84a03e04c7be380d39b8a5481f3ba840
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/FVRmDa2nS6GOSqccRHi4vg/zh-cn_image_0000002706833060.jpg)

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

   ```typescript
   import { relationalStore } from '@kit.ArkData'; // 导入模块
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { UIContext } from '@kit.ArkUI';
   import { common } from '@kit.AbilityKit';
   const DOMAIN = 0x0000;

   let store: relationalStore.RdbStore | undefined = undefined;
   let tokenType = relationalStore.Tokenizer.ICU_TOKENIZER;
   let tokenTypeSupported = relationalStore.isTokenizerSupported(tokenType);
   if (!tokenTypeSupported) {
     tokenType = relationalStore.Tokenizer.NONE_TOKENIZER;
     hilog.error(DOMAIN, 'rdbDataPersistence', `ICU_TOKENIZER is not supported on this platform.`);
   }
   const STORE_CONFIG: relationalStore.StoreConfig = {
     // 数据库文件名
     name: 'RdbTest.db',
     // 数据库安全级别
     securityLevel: relationalStore.SecurityLevel.S3,
     // 可选参数，指定数据库是否加密，默认不加密
     encrypt: false,
     // 可选参数，数据库自定义路径。默认在本应用沙箱目录下创建RdbStore实例。
     customDir: 'customDir/subCustomDir',
     // 可选参数，指定数据库是否以只读方式打开。默认为false，表示数据库可读可写。为true时，只允许从数据库读取数据，不允许对数据库进行写操作，否则会返回错误码801。
     isReadOnly: false,
     // 可选参数，指定用户在全文搜索场景(FTS)下使用哪种分词器。默认在FTS下仅支持英文分词，不支持其他语言分词。
     tokenizer: tokenType,
   };
   // ...
     // 判断数据库版本，如果不匹配则需进行升降级操作
     // 假设当前数据库版本为3，表结构：EMPLOYEE (NAME, AGE, SALARY, CODES, IDENTITY)
     // 建表Sql语句, IDENTITY为bigint类型，sql中指定类型为UNLIMITED INT
     const SQL_CREATE_TABLE =
       'CREATE TABLE IF NOT EXISTS EMPLOYEE (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, AGE INTEGER, SALARY REAL, CODES BLOB, ADDRESS TEXT)';
     if (store === undefined) {
       try {
         const context = new UIContext().getHostContext() as common.UIAbilityContext;
         store = await relationalStore.getRdbStore(context, STORE_CONFIG);
       } catch (e) {
         const err = e as BusinessError;
         hilog.error(DOMAIN, 'rdbDataPersistence', `Failed to get RdbStore. Code:${err.code}, message:${err.message}`);
         return;
       }
     }
     hilog.info(DOMAIN, 'rdbDataPersistence', 'Succeeded in getting RdbStore.');
     if (store !== undefined) {
       let transaction = await store.createTransaction({});
       let storeVersion = await transaction.execute('PRAGMA user_version');
       // 当数据库创建时，数据库默认版本为0
       // 示例应用升级流程较短，所以使用单个事务。如果实际业务中升级逻辑较多，建议拆分多个独立事务串行执行。
       if (storeVersion === 0) {
         try {
           await transaction.execute(SQL_CREATE_TABLE); // 创建数据表，以便后续调用insert接口插入数据
           storeVersion = 1;
           hilog.info(DOMAIN, 'rdbDataPersistence', 'Upgrade store version from 0 to 1 success.');
           // 设置数据库的版本，入参为大于0的整数
         } catch (e) {
           const err = e as BusinessError;
           await transaction.rollback();
           hilog.error(DOMAIN, 'rdbDataPersistence', `Failed to execute sql. Code:${err.code}, message:${err.message}`);
           return;
         }
       }
       // 如果数据库版本不为0且和当前数据库版本不匹配，需要进行升降级操作
       // 当前数据库存在并且版本为1，数据库需要从1版本升级到2版本
       if (storeVersion === 1) {
         // version = 1：表结构：EMPLOYEE (NAME, AGE, SALARY, CODES, ADDRESS)
         // => version = 2：表结构：EMPLOYEE (NAME, AGE, SALARY, CODES, ADDRESS, IDENTITY)
         try {
           await transaction.execute('ALTER TABLE EMPLOYEE ADD COLUMN IDENTITY UNLIMITED INT');
           storeVersion = 2;
           hilog.info(DOMAIN, 'rdbDataPersistence', 'Upgrade store version from 1 to 2 success.');
         } catch (e) {
           const err = e as BusinessError;
           await transaction.rollback();
           hilog.error(DOMAIN, 'rdbDataPersistence', `Failed to execute sql. Code:${err.code}, message:${err.message}`);
           return;
         }
       }
       // 当前数据库存在并且版本为2，数据库需要从2版本升级到3版本
       if (storeVersion === 2) {
         // version = 2：表结构：EMPLOYEE (NAME, AGE, SALARY, CODES, ADDRESS, IDENTITY)
         // => version = 3：表结构：EMPLOYEE (NAME, AGE, SALARY, CODES, IDENTITY)
         try {
           await transaction.execute('ALTER TABLE EMPLOYEE DROP COLUMN ADDRESS');
           storeVersion = 3;
           await transaction.execute('PRAGMA user_version = 3');
           hilog.info(DOMAIN, 'rdbDataPersistence', 'Upgrade store version from 2 to 3 success.')
         } catch (e) {
           const err = e as BusinessError;
           await transaction.rollback();
           hilog.error(DOMAIN, 'rdbDataPersistence', `Failed to execute sql. Code:${err.code}, message:${err.message}`);
           return;
         }
       }
       await transaction.commit();
       // 请确保获取到RdbStore实例，完成数据表创建后，再进行数据库的增、删、改、查等操作
     }
   ```

   FA模型示例：

   ```ts
   import { relationalStore } from '@kit.ArkData'; // 导入模块
   import { featureAbility } from '@kit.AbilityKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   let context = featureAbility.getContext();

   const STORE_CONFIG: relationalStore.StoreConfig = {
     name: 'RdbTest.db', // 数据库文件名
     securityLevel: relationalStore.SecurityLevel.S3 // 数据库安全级别
   };

   // 假设当前数据库版本为3，表结构：EMPLOYEE (NAME, AGE, SALARY, CODES, IDENTITY)
   // 建表Sql语句，IDENTITY为bigint类型，sql中指定类型为UNLIMITED INT
   const SQL_CREATE_TABLE =
     'CREATE TABLE IF NOT EXISTS EMPLOYEE (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, AGE INTEGER, SALARY REAL, CODES BLOB, IDENTITY UNLIMITED INT)';

   relationalStore.getRdbStore(context, STORE_CONFIG, async (err, store) => {
     if (err) {
       console.error(`Failed to get RdbStore. Code:${err.code}, message:${err.message}`);
       return;
     }
     console.info('Succeeded in getting RdbStore.');

     let storeVersion = store.version;
     // 当数据库创建时，数据库默认版本为0
     if (storeVersion === 0) {
       try {
         await store.execute(SQL_CREATE_TABLE); // 创建数据表，以便后续调用insert接口插入数据
         // 设置数据库的版本，入参为大于0的整数
         storeVersion = 3;
       } catch (e) {
         const err = e as BusinessError;
         console.error(`Failed to execute sql. Code:${err.code}, message:${err.message}`);
       }
     }

     // 如果数据库版本不为0且和当前数据库版本不匹配，需要进行升降级操作
     // 当前数据库存在并且版本为1，数据库需要从1版本升级到2版本
     if (storeVersion === 1) {
       try {
         // version = 1：表结构：EMPLOYEE (NAME, SALARY, CODES, ADDRESS) => version = 2：表结构：EMPLOYEE (NAME, AGE, SALARY, CODES, ADDRESS)
         await store.execute('ALTER TABLE EMPLOYEE ADD COLUMN AGE INTEGER');
         storeVersion = 2;
         console.info("Upgrade store version from 1 to 2 success.")
       } catch (e) {
         const err = e as BusinessError;
         console.error(`Failed to execute sql. Code:${err.code}, message:${err.message}`);
       }
     }

     // 当前数据库存在并且版本为2，数据库需要从2版本升级到3版本
     if (storeVersion === 2) {
       try {
         // version = 2：表结构：EMPLOYEE (NAME, AGE, SALARY, CODES, ADDRESS) => version = 3：表结构：EMPLOYEE (NAME, AGE, SALARY, CODES)
         await store.execute('ALTER TABLE EMPLOYEE DROP COLUMN ADDRESS');
         storeVersion = 3;
         console.info("Upgrade store version from 2 to 3 success.")
       } catch (e) {
         const err = e as BusinessError;
         console.error(`Failed to execute sql. Code:${err.code}, message:${err.message}`);
       }
     }
     store.version = storeVersion;
     // 请确保获取到RdbStore实例，完成数据表创建后，再进行数据库的增、删、改、查等操作
   });
   ```

   **说明** 

   * 应用创建的数据库与其上下文（Context）有关，即使使用同样的数据库名称，但不同的应用上下文，会产生多个数据库，例如每个UIAbility都有各自的上下文。
   * 当应用首次获取数据库（调用getRdbStore）后，在应用沙箱内会产生对应的数据库文件。使用数据库的过程中，在与数据库文件相同的目录下可能会产生以-wal和-shm结尾的临时文件。此时若开发者希望移动数据库文件到其它地方使用查看，则需要同时移动这些临时文件，当应用被卸载完成后，其在设备上产生的数据库文件及临时文件也会被移除。
   * 错误码的详细介绍请参见[通用错误码](../harmonyos-references/errorcode-universal.md)和[关系型数据库错误码](../harmonyos-references/errorcode-data-rdb.md)。
2. 获取到RdbStore，完成数据表创建后，调用insert()接口插入数据。示例代码如下所示：

   ```typescript
   // 插入数据
   let value1 = 'Lisa';
   let value2 = 18;
   let value3 = 100.5;
   let value4 = new Uint8Array([1, 2, 3, 4, 5]);
   let value5 = BigInt('15822401018187971961171');
   const valueBucket: relationalStore.ValuesBucket = {
     NAME: value1,
     AGE: value2,
     SALARY: value3,
     CODES: value4,
     IDENTITY: value5,
   };
   if (store !== undefined) {
     try {
       const rowId = await store.insert('EMPLOYEE', valueBucket);
       hilog.info(DOMAIN, 'rdbDataPersistence', `Succeeded in inserting data. rowId:${rowId}`);
     } catch (error) {
       const err = error as BusinessError;
       hilog.error(DOMAIN, 'rdbDataPersistence', `Failed to insert data. Code:${err.code}, message:${err.message}`);
     }
   }
   ```

   **说明** 

   关系型数据库没有显式的flush操作实现持久化，数据插入即保存在持久化文件。
3. 根据谓词指定的实例对象，对数据进行修改或删除。

   调用update()方法修改数据，调用delete()方法删除数据。示例代码如下所示：

   ```typescript
   // 修改数据、删除数据
   let value6 = 'Rose';
   let value7 = 22;
   let value8 = 200.5;
   let value9 = new Uint8Array([1, 2, 3, 4, 5]);
   let value10 = BigInt('15822401018187971967863');
   const valueBucket2: relationalStore.ValuesBucket = {
     NAME: value6,
     AGE: value7,
     SALARY: value8,
     CODES: value9,
     IDENTITY: value10,
   };

   // 修改数据
   let predicates1 = new relationalStore.RdbPredicates('EMPLOYEE'); // 创建表'EMPLOYEE'的predicates
   predicates1.equalTo('NAME', 'Lisa'); // 匹配表'EMPLOYEE'中'NAME'为'Lisa'的字段
   if (store !== undefined) {
     (store as relationalStore.RdbStore).update(valueBucket2, predicates1, (err: BusinessError, rows: number) => {
       if (err) {
         hilog.error(DOMAIN, 'rdbDataPersistence', `Failed to update data. Code:${err.code}, message:${err.message}`);
         return;
       }
       hilog.info(DOMAIN, 'rdbDataPersistence', `Succeeded in updating data. row count: ${rows}`);
     })
   }

   // 删除数据
   predicates1 = new relationalStore.RdbPredicates('EMPLOYEE');
   predicates1.equalTo('NAME', 'Lisa');
   if (store !== undefined) {
     (store as relationalStore.RdbStore).delete(predicates1, (err: BusinessError, rows: number) => {
       if (err) {
         hilog.error(DOMAIN, 'rdbDataPersistence', `Failed to delete data. Code:${err.code}, message:${err.message}`);
         return;
       }
       hilog.info(DOMAIN, 'rdbDataPersistence', `Delete rows: ${rows}`);
     })
   }
   ```
4. 根据谓词指定的查询条件查找数据。

   调用query()方法查找数据，返回一个ResultSet结果集。示例代码如下所示：

   ```typescript
   // 查找数据
   let predicates2 = new relationalStore.RdbPredicates('EMPLOYEE');
   predicates2.equalTo('NAME', 'Rose');
   if (store !== undefined) {
     (store as relationalStore.RdbStore).query(predicates2, ['ID', 'NAME', 'AGE', 'SALARY', 'CODES', 'IDENTITY'], (err: BusinessError, resultSet) => {
       if (err) {
         hilog.error(DOMAIN, 'rdbDataPersistence', `Failed to query data. Code:${err.code}, message:${err.message}`);
         return;
       }
       hilog.info(DOMAIN, 'rdbDataPersistence', `ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}`);
       // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
       while (resultSet.goToNextRow()) {
         const id = resultSet.getLong(resultSet.getColumnIndex('ID'));
         const name = resultSet.getString(resultSet.getColumnIndex('NAME'));
         const age = resultSet.getLong(resultSet.getColumnIndex('AGE'));
         const salary = resultSet.getDouble(resultSet.getColumnIndex('SALARY'));
         const identity = resultSet.getValue(resultSet.getColumnIndex('IDENTITY'));
         hilog.info(DOMAIN, 'rdbDataPersistence', `id=${id}, name=${name}, age=${age}, salary=${salary}, identity=${identity}`);
       }
       // 释放数据集的内存
       resultSet.close();
     })
   }
   ```

   **说明** 

   当应用完成查询数据操作，不再使用结果集（ResultSet）时，请及时调用close方法关闭结果集，释放系统为其分配的内存。

   当前RDB还支持进行FTS全文检索，可以根据中文或者英文进行文本检索，针对中文分词器支持ICU分词器。

   以中文关键字检索为例：

   ```typescript
   // 中文关键字检索，查找数据
   if (store !== undefined && tokenTypeSupported) {
     // 创建全文检索表
     const SQL_CREATE_TABLE = 'CREATE VIRTUAL TABLE IF NOT EXISTS example USING fts4(name, content, tokenize=icu zh_CN)';
     try {
       await store.execute(SQL_CREATE_TABLE);
       hilog.info(DOMAIN, 'rdbDataPersistence', 'Succeeded in creating fts table.');
     } catch (error) {
       const err = error as BusinessError;
       hilog.error(DOMAIN, 'rdbDataPersistence', `Failed to create fts table. code: ${err.code}, message: ${err.message}.`);
     }
   }
   if (store !== undefined) {
     try {
       const resultSet = await store.querySql('SELECT name FROM example WHERE example MATCH ?', ['测试']);
       while (resultSet.goToNextRow()) {
         const name = resultSet.getValue(resultSet.getColumnIndex('name'));
         hilog.info(DOMAIN, 'rdbDataPersistence', `name=${name}`);
       }
       resultSet.close();
     } catch (error) {
       const err = error as BusinessError;
       hilog.error(DOMAIN, 'rdbDataPersistence', `Query failed. code: ${err.code}, message: ${err.message}.`);
     }
   }
   ```
5. 使用事务对象执行数据的插入、删除和更新操作。

   调用createTransaction方法创建事务对象并执行相应操作。

   支持配置的事务类型有DEFERRED、IMMEDIATE和EXCLUSIVE，默认为DEFERRED。

   具体信息请参见[createTransaction](../harmonyos-references/arkts-apis-data-relationalstore-rdbstore.md#createtransaction14)。

   ```typescript
   // 使用事务对象执行数据的插入、删除和更新操作
   if (store !== undefined) {
     // 创建事务对象
     try {
       const transaction = await store.createTransaction();
       try {
         // 使用事务对象插入数据
         const rowId = await transaction.insert(
           'EMPLOYEE',
           {
             NAME: 'Lisa',
             AGE: 18,
             SALARY: 100.5,
             CODES: new Uint8Array([1, 2, 3, 4, 5]),
             IDENTITY: BigInt('15822401018187971967763')
           },
           relationalStore.ConflictResolution.ON_CONFLICT_REPLACE
         );
         hilog.info(DOMAIN, 'rdbDataPersistence', `Insert is successful, rowId = ${rowId}`);

         const predicates = new relationalStore.RdbPredicates('EMPLOYEE');
         predicates.equalTo('NAME', 'Lisa');
         // 使用事务对象更新数据
         const rows = await transaction.update(
           {
             NAME: 'Rose',
             AGE: 22,
             SALARY: 200.5,
             CODES: new Uint8Array([1, 2, 3, 4, 5]),
             IDENTITY: BigInt('15822401018187971967763')
           },
           predicates,
           relationalStore.ConflictResolution.ON_CONFLICT_REPLACE
         );
         hilog.info(DOMAIN, 'rdbDataPersistence', `Updated row count: ${rows}`);

         // 使用事务对象删除数据
         await transaction.execute('DELETE FROM EMPLOYEE WHERE age = ? OR age = ?', [21, 20]);
         hilog.info(DOMAIN, 'rdbDataPersistence', `execute delete success`);

         // 提交事务
         await transaction.commit();
         hilog.info(DOMAIN, 'rdbDataPersistence', 'Transaction commit success.');
       } catch (error) {
         const err = error as BusinessError;
         // 执行失败回滚事务
         await transaction.rollback();
         hilog.error(DOMAIN, 'rdbDataPersistence', `Transaction execute failed, code is ${err.code}, message is ${err.message}`);
       }
     } catch (error) {
       const err = error as BusinessError;
       hilog.error(DOMAIN, 'rdbDataPersistence', `createTransaction failed, code is ${err.code}, message is ${err.message}`);
     }
   }
   ```
6. 在同路径下备份数据库。关系型数据库支持手动备份和自动备份（仅系统应用可用）两种方式，具体可见[关系型数据库备份](data-backup-and-restore.md#关系型数据库备份)。

   此处以手动备份为例：

   ```typescript
   // 在同路径下备份数据库
   if (store !== undefined) {
     // 'Backup.db'为备份数据库文件名，默认在RdbStore同路径下备份。也可指定路径：customDir + 'Backup.db'
     (store as relationalStore.RdbStore).backup('Backup.db', (err: BusinessError) => {
       if (err) {
         hilog.error(DOMAIN, 'rdbDataPersistence', `Failed to backup RdbStore. Code:${err.code}, message:${err.message}`);
         return;
       }
       hilog.info(DOMAIN, 'rdbDataPersistence', `Succeeded in backing up RdbStore.`);
     })
   }
   ```
7. 从备份数据库中恢复数据。关系型数据库支持两种方式：恢复手动备份数据和恢复自动备份数据（仅系统应用可用），具体可见[关系型数据库数据恢复](data-backup-and-restore.md#关系型数据库数据恢复)。

   此处以调用[restore](../harmonyos-references/arkts-apis-data-relationalstore-rdbstore.md#restore)接口恢复手动备份数据为例：

   ```typescript
   // 备份数据库中恢复数据
   if (store !== undefined) {
     (store as relationalStore.RdbStore).restore('Backup.db', (err: BusinessError) => {
       if (err) {
         hilog.error(DOMAIN, 'rdbDataPersistence', `Failed to restore RdbStore. Code:${err.code}, message:${err.message}`);
         return;
       }
       hilog.info(DOMAIN, 'rdbDataPersistence', `Succeeded in restoring RdbStore.`);
     })
   }
   ```
8. 删除数据库。

   调用deleteRdbStore()方法，删除数据库及数据库相关文件。示例代码如下：

   Stage模型示例：

   ```typescript
   // 删除数据库
   const context = new UIContext().getHostContext() as common.UIAbilityContext;
   relationalStore.deleteRdbStore(context, 'RdbTest.db', (err: BusinessError) => {
     if (err) {
       hilog.error(DOMAIN, 'rdbDataPersistence', `Failed to delete RdbStore. Code:${err.code}, message:${err.message}`);
       return;
     }
     hilog.info(DOMAIN, 'rdbDataPersistence', 'Succeeded in deleting RdbStore.');
   });
   ```
