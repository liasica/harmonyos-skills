---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-transaction
title: Interface (Transaction)
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > ArkTS API > @ohos.data.relationalStore (关系型数据库) > Interface (Transaction)
category: harmonyos-references
scraped_at: 2026-04-28T07:59:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6a3891918cf9356fa71210b35ce2921348229b99ff5addc6c8310d55233fa054
---

提供以事务方式管理数据库的方法。事务对象是通过[createTransaction](arkts-apis-data-relationalstore-rdbstore.md#createtransaction14)接口创建的，不同事务对象之间的操作是隔离的，不同类型事务的区别见[TransactionType](arkts-apis-data-relationalstore-e.md#transactiontype14) 。

当前关系型数据库同一时刻仅支持一个写事务，所以如果当前[RdbStore](arkts-apis-data-relationalstore-rdbstore.md)存在写事务未释放，创建IMMEDIATE或EXCLUSIVE事务会返回14800024错误码。如果是创建的DEFERRED事务，则可能在首次使用DEFERRED事务调用写操作时返回14800024错误码。通过IMMEDIATE或EXCLUSIVE创建写事务或者DEFERRED事务升级到写事务之后，[RdbStore](arkts-apis-data-relationalstore-rdbstore.md)的写操作也会返回14800024错误码。

当事务并发量较高且写事务持续时间较长时，返回14800024错误码的次数可能会变多，开发者可以通过减少事务占用时长减少14800024出现的次数，也可以通过重试的方式处理14800024错误码。

在使用以下API前，请先通过[createTransaction](arkts-apis-data-relationalstore-rdbstore.md#createtransaction14)方法获取Transaction实例，再通过此实例调用对应方法。

说明

* 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 14开始支持。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**示例：**

示例代码中this.context定义见Stage模型的应用[Context](js-apis-inner-application-context.md)。

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { window } from '@kit.ArkUI';

5. let store: relationalStore.RdbStore | undefined = undefined;

7. export default class EntryAbility extends UIAbility {
8. async onWindowStageCreate(windowStage: window.WindowStage) {
9. const STORE_CONFIG: relationalStore.StoreConfig = {
10. name: 'RdbTest.db',
11. securityLevel: relationalStore.SecurityLevel.S3
12. };

14. try {
15. const rdbStore = await relationalStore.getRdbStore(this.context, STORE_CONFIG);
16. store = rdbStore;
17. console.info('Get RdbStore successfully.');
18. } catch (error) {
19. const err = error as BusinessError;
20. console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
21. }

23. if (store != undefined) {
24. await store.executeSql('CREATE TABLE IF NOT EXISTS EMPLOYEE (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, AGE INTEGER, SALARY REAL, CODES BLOB, IDENTITY UNLIMITED INT, ASSETDATA ASSET, ASSETSDATA ASSETS, FLOATARRAY floatvector(128))');
25. store.createTransaction().then(async (transaction: relationalStore.Transaction) => {
26. console.info(`createTransaction success`);
27. // 成功获取到事务对象后执行后续操作
28. }).catch((err: BusinessError) => {
29. console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
30. });
31. }
32. }
33. }
```

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { relationalStore } from '@kit.ArkData';
```

## commit14+

PhonePC/2in1TabletTVWearable

commit(): Promise<void>

提交已执行的SQL语句，使用Promise异步回调。如果是使用异步接口执行sql语句，请确保异步接口执行完成之后再调用commit接口，否则可能会丢失SQL操作。调用commit接口之后，该Transaction对象及创建的ResultSet对象都将被关闭。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |

**示例：**

```
1. if (store != undefined) {
2. try {
3. const transaction = await store.createTransaction();
4. try {
5. await transaction.execute('CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, age INTEGER, salary REAL)');
6. await transaction.commit();
7. } catch (error) {
8. const err = error as BusinessError;
9. await transaction.rollback();
10. console.error(`execute sql failed, code is ${err.code},message is ${err.message}`);
11. }
12. } catch (error) {
13. const err = error as BusinessError;
14. console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
15. }
16. }
```

## rollback14+

PhonePC/2in1TabletTVWearable

rollback(): Promise<void>

回滚已经执行的SQL语句，使用Promise异步回调。调用rollback接口之后，该Transaction对象及创建的ResultSet对象都会被关闭。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |

**示例：**

```
1. if (store != undefined) {
2. try {
3. const transaction = await store.createTransaction();
4. try {
5. await transaction.execute('DELETE FROM TEST WHERE age = ? OR age = ?', ['18', '20']);
6. await transaction.commit();
7. } catch (error) {
8. const err = error as BusinessError;
9. await transaction.rollback();
10. console.error(`execute sql failed, code is ${err.code},message is ${err.message}`);
11. }
12. } catch (error) {
13. const err = error as BusinessError;
14. console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
15. }
16. }
```

## insert14+

PhonePC/2in1TabletTVWearable

insert(table: string, values: ValuesBucket, conflict?: ConflictResolution): Promise<number>

向目标表中插入一行数据，使用Promise异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的[query](arkts-apis-data-relationalstore-rdbstore.md#query)或[querySql](arkts-apis-data-relationalstore-rdbstore.md#querysql)接口获取ResultSet后，调用[getValue](arkts-apis-data-relationalstore-resultset.md#getvalue12)、[getString](arkts-apis-data-relationalstore-resultset.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 指定的目标表名。 |
| values | [ValuesBucket](arkts-apis-data-relationalstore-t.md#valuesbucket) | 是 | 表示要插入到表中的数据行。 |
| conflict | [ConflictResolution](arkts-apis-data-relationalstore-e.md#conflictresolution10) | 否 | 指定冲突解决模式。默认值是relationalStore.ConflictResolution.ON\_CONFLICT\_NONE。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。如果操作成功，返回行ID；否则返回-1。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800033 | SQLite: Data type mismatch. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. const valueBucket1: relationalStore.ValuesBucket = {
2. NAME: 'Lisa',
3. AGE: 18,
4. SALARY: 100.5,
5. CODES: new Uint8Array([1, 2, 3, 4, 5])
6. };

8. if (store != undefined) {
9. try {
10. const transaction = await store.createTransaction();
11. try {
12. const rowId = await transaction.insert('EMPLOYEE', valueBucket1, relationalStore.ConflictResolution.ON_CONFLICT_REPLACE);
13. await transaction.commit();
14. console.info(`Insert is successful, rowId = ${rowId}`);
15. } catch (error) {
16. const err = error as BusinessError;
17. await transaction.rollback();
18. console.error(`Insert is failed, code is ${err.code},message is ${err.message}`);
19. }
20. } catch (error) {
21. const err = error as BusinessError;
22. console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
23. }
24. }
```

## insertSync14+

PhonePC/2in1TabletTVWearable

insertSync(table: string, values: ValuesBucket | sendableRelationalStore.ValuesBucket, conflict?: ConflictResolution): number

向目标表中插入一行数据。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的[query](arkts-apis-data-relationalstore-rdbstore.md#query)或[querySql](arkts-apis-data-relationalstore-rdbstore.md#querysql)接口获取ResultSet后，调用[getValue](arkts-apis-data-relationalstore-resultset.md#getvalue12)、[getString](arkts-apis-data-relationalstore-resultset.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 指定的目标表名。 |
| values | [ValuesBucket](arkts-apis-data-relationalstore-t.md#valuesbucket) | [sendableRelationalStore.ValuesBucket](js-apis-data-sendablerelationalstore.md#valuesbucket) | 是 | 表示要插入到表中的数据行。 |
| conflict | [ConflictResolution](arkts-apis-data-relationalstore-e.md#conflictresolution10) | 否 | 指定冲突解决模式。默认值是relationalStore.ConflictResolution.ON\_CONFLICT\_NONE。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| number | 如果操作成功，返回行ID；否则返回-1。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800033 | SQLite: Data type mismatch. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. let value5 = 'Lisa';
2. let value6 = 18;
3. let value7 = 100.5;
4. let value8 = new Uint8Array([1, 2, 3, 4, 5]);

6. const valueBucket2: relationalStore.ValuesBucket = {
7. NAME: value5,
8. AGE: value6,
9. SALARY: value7,
10. CODES: value8
11. };
12. if (store != undefined) {
13. try {
14. const transaction = await store.createTransaction();
15. try {
16. let rowId: number = transaction.insertSync(
17. 'EMPLOYEE',
18. valueBucket2,
19. relationalStore.ConflictResolution.ON_CONFLICT_REPLACE
20. );
21. await transaction.commit();
22. console.info(`Insert is successful, rowId = ${rowId}`);
23. } catch (e) {
24. await transaction.rollback();
25. console.error(`Insert is failed, code is ${e.code},message is ${e.message}`);
26. }
27. } catch (error) {
28. const err = error as BusinessError;
29. console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
30. }
31. }
```

## batchInsert14+

PhonePC/2in1TabletTVWearable

batchInsert(table: string, values: Array<ValuesBucket>): Promise<number>

向目标表中插入一组数据，使用Promise异步回调。

按每批32766个参数，分批以[ConflictResolution.ON\_CONFLICT\_REPLACE](arkts-apis-data-relationalstore-e.md#conflictresolution10)策略写入，参数数量计算方式为插入数据条数乘以插入数据的所有字段的并集大小，中途失败则立即返回。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 指定的目标表名。 |
| values | Array<[ValuesBucket](arkts-apis-data-relationalstore-t.md#valuesbucket)> | 是 | 表示要插入到表中的一组数据。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。如果操作成功，返回插入的数据个数，否则返回-1。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800033 | SQLite: Data type mismatch. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. const valueBucket3: relationalStore.ValuesBucket = {
2. NAME: 'Lisa',
3. AGE: 18,
4. SALARY: 100.5,
5. CODES: new Uint8Array([1, 2, 3, 4, 5])
6. };
7. const valueBucket4: relationalStore.ValuesBucket = {
8. NAME: 'Jack',
9. AGE: 19,
10. SALARY: 101.5,
11. CODES: new Uint8Array([6, 7, 8, 9, 10])
12. };
13. const valueBucket5: relationalStore.ValuesBucket = {
14. NAME: 'Tom',
15. AGE: 20,
16. SALARY: 102.5,
17. CODES: new Uint8Array([11, 12, 13, 14, 15])
18. };

20. let valueBuckets = new Array(valueBucket3, valueBucket4, valueBucket5);
21. if (store != undefined) {
22. try {
23. const transaction = await store.createTransaction();
24. try {
25. const insertNum = await transaction.batchInsert('EMPLOYEE', valueBuckets);
26. await transaction.commit();
27. console.info(`batchInsert is successful, the number of values that were inserted = ${insertNum}`);
28. } catch (error) {
29. const err = error as BusinessError;
30. await transaction.rollback();
31. console.error(`batchInsert is failed, code is ${err.code},message is ${err.message}`);
32. }
33. } catch (error) {
34. const err = error as BusinessError;
35. console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
36. }
37. }
```

## batchInsertSync14+

PhonePC/2in1TabletTVWearable

batchInsertSync(table: string, values: Array<ValuesBucket>): number

向目标表中插入一组数据。

按每批32766个参数，分批以[ConflictResolution.ON\_CONFLICT\_REPLACE](arkts-apis-data-relationalstore-e.md#conflictresolution10)策略写入，参数数量计算方式为插入数据条数乘以插入数据的所有字段的并集大小，中途失败则立即返回。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 指定的目标表名。 |
| values | Array<[ValuesBucket](arkts-apis-data-relationalstore-t.md#valuesbucket)> | 是 | 表示要插入到表中的一组数据。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| number | 如果操作成功，返回插入的数据个数，否则返回-1。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800033 | SQLite: Data type mismatch. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. const valueBucket6: relationalStore.ValuesBucket = {
2. NAME: 'Lisa',
3. AGE: 18,
4. SALARY: 100.5,
5. CODES: new Uint8Array([1, 2, 3, 4, 5])
6. };
7. const valueBucket7: relationalStore.ValuesBucket = {
8. NAME: 'Jack',
9. AGE: 19,
10. SALARY: 101.5,
11. CODES: new Uint8Array([6, 7, 8, 9, 10])
12. };
13. const valueBucket8: relationalStore.ValuesBucket = {
14. NAME: 'Tom',
15. AGE: 20,
16. SALARY: 102.5,
17. CODES: new Uint8Array([11, 12, 13, 14, 15])
18. };

20. let valueBuckets2 = new Array(valueBucket6, valueBucket7, valueBucket8);
21. if (store != undefined) {
22. try {
23. const transaction = await store.createTransaction();
24. try {
25. let insertNum: number = (transaction as relationalStore.Transaction).batchInsertSync('EMPLOYEE', valueBuckets2);
26. await transaction.commit();
27. console.info(`batchInsert is successful, the number of values that were inserted = ${insertNum}`);
28. } catch (error) {
29. const err = error as BusinessError;
30. await transaction.rollback();
31. console.error(`batchInsert is failed, code is ${err.code},message is ${err.message}`);
32. }
33. } catch (error) {
34. const err = error as BusinessError;
35. console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
36. }
37. }
```

## batchInsertWithConflictResolution18+

PhonePC/2in1TabletTVWearable

batchInsertWithConflictResolution(table: string, values: Array<ValuesBucket>, conflict: ConflictResolution): Promise<number>

向目标表中插入一组数据，可以通过conflict参数指定冲突解决模式[ConflictResolution](arkts-apis-data-relationalstore-e.md#conflictresolution10)，使用Promise异步回调。

单次插入参数的最大数量限制为32766，超出上限会返回14800000错误码。参数数量计算方式为插入数据条数乘以插入数据的所有字段的并集大小。

例如：插入数据的所有字段的并集大小为10，则最多可以插入3276条数据（3276\*10=32760）。

请确保在调用接口时遵守此限制，以避免因参数数量过多而导致错误。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 指定的目标表名。 |
| values | Array<[ValuesBucket](arkts-apis-data-relationalstore-t.md#valuesbucket)> | 是 | 表示要插入到表中的一组数据。 |
| conflict | [ConflictResolution](arkts-apis-data-relationalstore-e.md#conflictresolution10) | 是 | 指定冲突解决模式。如果是ON\_CONFLICT\_ROLLBACK模式，当发生冲突时会回滚整个事务。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。如果操作成功，返回插入的数据个数，否则返回-1。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. const valueBucket9: relationalStore.ValuesBucket = {
2. NAME: 'Lisa',
3. AGE: 18,
4. SALARY: 100.5,
5. CODES: new Uint8Array([1, 2, 3, 4, 5])
6. };
7. const valueBucketA: relationalStore.ValuesBucket = {
8. NAME: 'Jack',
9. AGE: 19,
10. SALARY: 101.5,
11. CODES: new Uint8Array([6, 7, 8, 9, 10])
12. };
13. const valueBucketB: relationalStore.ValuesBucket = {
14. NAME: 'Tom',
15. AGE: 20,
16. SALARY: 102.5,
17. CODES: new Uint8Array([11, 12, 13, 14, 15])
18. };

20. let valueBuckets3 = new Array(valueBucket9, valueBucketA, valueBucketB);

22. if (store != undefined) {
23. try {
24. const transaction = await store.createTransaction();
25. try {
26. const insertNum = await transaction.batchInsertWithConflictResolution(
27. 'EMPLOYEE',
28. valueBuckets3,
29. relationalStore.ConflictResolution.ON_CONFLICT_REPLACE
30. );
31. await transaction.commit();
32. console.info(`batchInsert is successful, the number of values that were inserted = ${insertNum}`);
33. } catch (error) {
34. const err = error as BusinessError;
35. await transaction.rollback();
36. console.error(`batchInsert is failed, code is ${err.code},message is ${err.message}`);
37. }
38. } catch (error) {
39. const err = error as BusinessError;
40. console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
41. }
42. }
```

## batchInsertWithConflictResolutionSync18+

PhonePC/2in1TabletTVWearable

batchInsertWithConflictResolutionSync(table: string, values: Array<ValuesBucket>, conflict: ConflictResolution): number

向目标表中插入一组数据，可以通过conflict参数指定冲突解决模式[ConflictResolution](arkts-apis-data-relationalstore-e.md#conflictresolution10)。

单次插入参数的最大数量限制为32766，超出上限会返回14800000错误码。参数数量计算方式为插入数据条数乘以插入数据的所有字段的并集大小。

例如：插入数据的所有字段的并集大小为10，则最多可以插入3276条数据（3276\*10=32760）。

请确保在调用接口时遵守此限制，以避免因参数数量过多而导致错误。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 指定的目标表名。 |
| values | Array<[ValuesBucket](arkts-apis-data-relationalstore-t.md#valuesbucket)> | 是 | 表示要插入到表中的一组数据。 |
| conflict | [ConflictResolution](arkts-apis-data-relationalstore-e.md#conflictresolution10) | 是 | 指定冲突解决模式。如果是ON\_CONFLICT\_ROLLBACK模式，当发生冲突时会回滚整个事务。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| number | 如果操作成功，返回插入的数据个数，否则返回-1。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. const valueBucketC: relationalStore.ValuesBucket = {
2. NAME: 'Lisa',
3. AGE: 18,
4. SALARY: 100.5,
5. CODES: new Uint8Array([1, 2, 3, 4, 5])
6. };
7. const valueBucketD: relationalStore.ValuesBucket = {
8. NAME: 'Jack',
9. AGE: 19,
10. SALARY: 101.5,
11. CODES: new Uint8Array([6, 7, 8, 9, 10])
12. };
13. const valueBucketE: relationalStore.ValuesBucket = {
14. NAME: 'Tom',
15. AGE: 20,
16. SALARY: 102.5,
17. CODES: new Uint8Array([11, 12, 13, 14, 15])
18. };

20. let valueBuckets4 = new Array(valueBucketC, valueBucketD, valueBucketE);
21. if (store != undefined) {
22. try {
23. const transaction = await store.createTransaction();
24. try {
25. const insertNum = transaction.batchInsertWithConflictResolutionSync(
26. 'EMPLOYEE',
27. valueBuckets4,
28. relationalStore.ConflictResolution.ON_CONFLICT_REPLACE
29. );
30. await transaction.commit();
31. console.info(`batchInsert is successful, the number of values that were inserted = ${insertNum}`);
32. } catch (error) {
33. const err = error as BusinessError;
34. await transaction.rollback();
35. console.error(`batchInsert is failed, code is ${err.code},message is ${err.message}`);
36. }
37. } catch (error) {
38. const err = error as BusinessError;
39. console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
40. }
41. }
```

## batchInsertWithReturning23+

PhonePC/2in1TabletTVWearable

batchInsertWithReturning(table: string, values: Array<ValuesBucket>, config: ReturningConfig, conflict?: ConflictResolution): Promise<Result>

向目标表中插入一组数据，可以通过conflict参数指定当发生数据冲突时的解决模式[ConflictResolution](arkts-apis-data-relationalstore-e.md#conflictresolution10)，返回[Result](arkts-apis-data-relationalstore-i.md#result23)。使用Promise异步回调。

单次插入参数的最大数量限制为32766，超出上限会返回14800001错误码。参数数量计算方式为插入数据条数乘以插入数据的所有字段的并集大小。

例如：插入数据的所有字段的并集大小为10，则最多可以插入3276条数据（3276\*10=32760）。

请确保在调用接口时遵守此限制，以避免因参数数量过多而导致错误。

conflict参数不建议使用ON\_CONFLICT\_FAIL策略，可能无法返回正确的结果。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**模型约束：** 此接口仅在Stage模型下可用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 要插入的目标表名。注意：正确的表名不应包含空格、逗号和星号，不能以点开头和结尾等，否则会抛出参数错误。 |
| values | Array<[ValuesBucket](arkts-apis-data-relationalstore-t.md#valuesbucket)> | 是 | 表示要插入到表中的一组数据。注意：空数组、含有重复资产数据会抛出参数错误。 |
| config | [ReturningConfig](arkts-apis-data-relationalstore-i.md#returningconfig23) | 是 | 指定返回值的配置信息。 |
| conflict | [ConflictResolution](arkts-apis-data-relationalstore-e.md#conflictresolution10) | 否 | 指定冲突解决模式。默认为ON\_CONFLICT\_NONE。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Result](arkts-apis-data-relationalstore-i.md#result23)> | Promise对象。如果操作成功，返回受影响的数据集。 |

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1. Parameter is out of valid range. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. async function transBatchInsertWithReturningExample(trans: relationalStore.Transaction)
2. {
3. const valueBucket1: relationalStore.ValuesBucket = { 'NAME': 'zhangsan', 'AGE': 18 };
4. const valueBucket2: relationalStore.ValuesBucket = { 'NAME': 'lisi', 'AGE': 20 };
5. const config: relationalStore.ReturningConfig = { columns: ['NAME', 'AGE'] };
6. const valueBuckets = new Array(valueBucket1, valueBucket2);
7. try {
8. let results = await trans.batchInsertWithReturning("EMPLOYEE", valueBuckets, config);
9. console.info(`transBatchInsertWithReturningExample is successful, changed is ${results.changed}`);
10. while(results.resultSet.goToNextRow()) {
11. const row = results.resultSet.getRow();
12. console.info(`transBatchInsertWithReturningExample, name is ${row['NAME']}, age is ${row['AGE']}`);
13. }
14. } catch (e) {
15. console.error(`transBatchInsertWithReturningExample failed. code is ${e.code}, message is ${e.message}`);
16. }
17. }
```

## batchInsertWithReturningSync23+

PhonePC/2in1TabletTVWearable

batchInsertWithReturningSync(table: string, values: Array<ValuesBucket>, config: ReturningConfig, conflict?: ConflictResolution): Result

向目标表中插入一组数据，可以通过conflict参数指定当发生数据冲突时的解决模式[ConflictResolution](arkts-apis-data-relationalstore-e.md#conflictresolution10)，返回[Result](arkts-apis-data-relationalstore-i.md#result23)。

单次插入参数的最大数量限制为32766，超出上限会返回14800001错误码。参数数量计算方式为插入数据条数乘以插入数据的所有字段的并集大小。

例如：插入数据的所有字段的并集大小为10，则最多可以插入3276条数据（3276\*10=32760）。

请确保在调用接口时遵守此限制，以避免因参数数量过多而导致错误。

conflict参数不建议使用ON\_CONFLICT\_FAIL策略，可能无法返回正确的结果。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**模型约束：** 此接口仅在Stage模型下可用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 要插入的目标表名。注意：正确的表名不应包含空格、逗号和星号，不能以点开头和结尾等，否则会抛出参数错误。 |
| values | Array<[ValuesBucket](arkts-apis-data-relationalstore-t.md#valuesbucket)> | 是 | 表示要插入到表中的一组数据。注意：空数组、含有重复资产数据会抛出参数错误。 |
| config | [ReturningConfig](arkts-apis-data-relationalstore-i.md#returningconfig23) | 是 | 指定返回值的配置信息。 |
| conflict | [ConflictResolution](arkts-apis-data-relationalstore-e.md#conflictresolution10) | 否 | 指定冲突解决模式。默认为ON\_CONFLICT\_NONE。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Result](arkts-apis-data-relationalstore-i.md#result23) | 如果操作成功，返回受影响的数据集。 |

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1. Parameter is out of valid range. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. function transBatchInsertWithReturningSyncExample(trans: relationalStore.Transaction)
2. {
3. const valueBucket1: relationalStore.ValuesBucket = { 'NAME': 'zhangsan', 'AGE': 18 };
4. const valueBucket2: relationalStore.ValuesBucket = { 'NAME': 'lisi', 'AGE': 20 };
5. const config: relationalStore.ReturningConfig = { columns: ['NAME', 'AGE'] };
6. const valueBuckets = new Array(valueBucket1, valueBucket2);
7. try {
8. let results = trans.batchInsertWithReturningSync("EMPLOYEE", valueBuckets, config);
9. console.info(`transBatchInsertWithReturningSyncExample is successful, changed is ${results.changed}`);
10. while(results.resultSet.goToNextRow()) {
11. const row = results.resultSet.getRow();
12. console.info(`transBatchInsertWithReturningSyncExample, name is ${row['NAME']}, age is ${row['AGE']}`);
13. }
14. } catch (e) {
15. console.error(`transBatchInsertWithReturningSyncExample failed. code is ${e.code}, message is ${e.message}`);
16. }
17. }
```

## update14+

PhonePC/2in1TabletTVWearable

update(values: ValuesBucket, predicates: RdbPredicates, conflict?: ConflictResolution): Promise<number>

根据RdbPredicates的指定实例对象更新数据库中的数据，使用Promise异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的[query](arkts-apis-data-relationalstore-rdbstore.md#query)或[querySql](arkts-apis-data-relationalstore-rdbstore.md#querysql)接口获取ResultSet后，调用[getValue](arkts-apis-data-relationalstore-resultset.md#getvalue12)、[getString](arkts-apis-data-relationalstore-resultset.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| values | [ValuesBucket](arkts-apis-data-relationalstore-t.md#valuesbucket) | 是 | values指示数据库中要更新的数据行。键值对与数据库表的列名相关联。 |
| predicates | [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 是 | RdbPredicates的实例对象指定的更新条件。 |
| conflict | [ConflictResolution](arkts-apis-data-relationalstore-e.md#conflictresolution10) | 否 | 指定冲突解决模式。默认值是relationalStore.ConflictResolution.ON\_CONFLICT\_NONE。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 指定的Promise回调方法。返回受影响的行数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800033 | SQLite: Data type mismatch. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. const valueBucketF: relationalStore.ValuesBucket = {
2. NAME: 'Rose',
3. AGE: 22,
4. SALARY: 200.5,
5. CODES: new Uint8Array([1, 2, 3, 4, 5])
6. };
7. let predicates = new relationalStore.RdbPredicates('EMPLOYEE');
8. predicates.equalTo('NAME', 'Lisa');

10. if (store != undefined) {
11. try {
12. const transaction = await store.createTransaction();
13. try {
14. const rows = await transaction.update(valueBucketF, predicates, relationalStore.ConflictResolution.ON_CONFLICT_REPLACE);
15. await transaction.commit();
16. console.info(`Updated row count: ${rows}`);
17. } catch (error) {
18. const err = error as BusinessError;
19. await transaction.rollback();
20. console.error(`Updated failed, code is ${err.code},message is ${err.message}`);
21. }
22. } catch (error) {
23. const err = error as BusinessError;
24. console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
25. }
26. }
```

## updateSync14+

PhonePC/2in1TabletTVWearable

updateSync(values: ValuesBucket, predicates: RdbPredicates, conflict?: ConflictResolution): number

根据RdbPredicates的指定实例对象更新数据库中的数据。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的[query](arkts-apis-data-relationalstore-rdbstore.md#query)或[querySql](arkts-apis-data-relationalstore-rdbstore.md#querysql)接口获取ResultSet后，调用[getValue](arkts-apis-data-relationalstore-resultset.md#getvalue12)、[getString](arkts-apis-data-relationalstore-resultset.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| values | [ValuesBucket](arkts-apis-data-relationalstore-t.md#valuesbucket) | 是 | values指示数据库中要更新的数据行。键值对与数据库表的列名相关联。 |
| predicates | [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 是 | RdbPredicates的实例对象指定的更新条件。 |
| conflict | [ConflictResolution](arkts-apis-data-relationalstore-e.md#conflictresolution10) | 否 | 指定冲突解决模式。默认值是relationalStore.ConflictResolution.ON\_CONFLICT\_NONE。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| number | 返回受影响的行数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800033 | SQLite: Data type mismatch. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. const valueBucketG: relationalStore.ValuesBucket = {
2. NAME: 'Rose',
3. AGE: 22,
4. SALARY: 200.5,
5. CODES: new Uint8Array([1, 2, 3, 4, 5])
6. };
7. let predicates1 = new relationalStore.RdbPredicates('EMPLOYEE');
8. predicates1.equalTo('NAME', 'Lisa');

10. if (store != undefined) {
11. try {
12. const transaction = await store.createTransaction();
13. try {
14. let rows = transaction.updateSync(valueBucketG, predicates1, relationalStore.ConflictResolution.ON_CONFLICT_REPLACE);
15. await transaction.commit();
16. console.info(`Updated row count: ${rows}`);
17. } catch (error) {
18. const err = error as BusinessError;
19. await transaction.rollback();
20. console.error(`Updated failed, code is ${err.code},message is ${err.message}`);
21. }
22. } catch (error) {
23. const err = error as BusinessError;
24. console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
25. }
26. }
```

## updateWithReturning23+

PhonePC/2in1TabletTVWearable

updateWithReturning(values: ValuesBucket, predicates: RdbPredicates, config: ReturningConfig, conflict?: ConflictResolution): Promise<Result>

根据RdbPredicates的指定实例对象更新数据库中的数据，可以通过conflict参数指定当发生数据冲突时的解决模式[ConflictResolution](arkts-apis-data-relationalstore-e.md#conflictresolution10)，返回[Result](arkts-apis-data-relationalstore-i.md#result23)，使用Promise异步回调。

conflict参数不建议使用ON\_CONFLICT\_FAIL策略，可能无法返回正确的结果。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**模型约束：** 此接口仅在Stage模型下可用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| values | [ValuesBucket](arkts-apis-data-relationalstore-t.md#valuesbucket) | 是 | values指示数据库中要更新的数据行。键值对与数据库表的列名相关联。 |
| predicates | [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 是 | RdbPredicates的实例对象指定的更新条件。 |
| config | [ReturningConfig](arkts-apis-data-relationalstore-i.md#returningconfig23) | 是 | 指定返回值的配置信息。 |
| conflict | [ConflictResolution](arkts-apis-data-relationalstore-e.md#conflictresolution10) | 否 | 指定冲突解决模式。默认为ON\_CONFLICT\_NONE。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Result](arkts-apis-data-relationalstore-i.md#result23)> | Promise对象。如果操作成功，返回受影响的数据集。 |

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1. Parameter is out of valid range. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. async function transUpdateWithReturningExample(trans: relationalStore.Transaction)
2. {
3. const valueBucket1: relationalStore.ValuesBucket = { 'NAME': 'lisi', 'AGE': 21 };
4. const valueBucket2: relationalStore.ValuesBucket = { 'NAME': 'lisi', 'AGE': 18 };
5. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
6. predicates.equalTo('NAME', 'lisi');
7. const config: relationalStore.ReturningConfig = { columns: ['NAME', 'AGE'] };
8. try {
9. trans.batchInsertWithReturningSync("EMPLOYEE", [valueBucket1, valueBucket2], config);
10. valueBucket1['NAME'] = "zhangsan";
11. valueBucket1['AGE'] = 18;
12. let results = await trans.updateWithReturning(valueBucket1, predicates, config);
13. console.info(`transUpdateWithReturningExample is successful, changed is ${results.changed}`);
14. while(results.resultSet.goToNextRow()) {
15. const row = results.resultSet.getRow();
16. console.info(`transUpdateWithReturningExample, name is ${row['NAME']}, age is ${row['AGE']}`);
17. }
18. } catch (e) {
19. console.error(`transUpdateWithReturningExample failed. code is ${e.code}, message is ${e.message}`);
20. }
21. }
```

## updateWithReturningSync23+

PhonePC/2in1TabletTVWearable

updateWithReturningSync(values: ValuesBucket, predicates: RdbPredicates, config: ReturningConfig, conflict?: ConflictResolution): Result

根据RdbPredicates的指定实例对象更新数据库中的数据，可以通过conflict参数指定当发生数据冲突时的解决模式[ConflictResolution](arkts-apis-data-relationalstore-e.md#conflictresolution10)，返回[Result](arkts-apis-data-relationalstore-i.md#result23)。

conflict参数不建议使用ON\_CONFLICT\_FAIL策略，可能无法返回正确的结果。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**模型约束：** 此接口仅在Stage模型下可用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| values | [ValuesBucket](arkts-apis-data-relationalstore-t.md#valuesbucket) | 是 | values指示数据库中要更新的数据行。键值对与数据库表的列名相关联。 |
| predicates | [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 是 | RdbPredicates的实例对象指定的更新条件。 |
| config | [ReturningConfig](arkts-apis-data-relationalstore-i.md#returningconfig23) | 是 | 指定返回值的配置信息。 |
| conflict | [ConflictResolution](arkts-apis-data-relationalstore-e.md#conflictresolution10) | 否 | 指定冲突解决模式。默认为ON\_CONFLICT\_NONE。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Result](arkts-apis-data-relationalstore-i.md#result23) | 如果操作成功，返回受影响的数据集。 |

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1. Parameter is out of valid range. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. function transUpdateWithReturningSyncExample(trans: relationalStore.Transaction)
2. {
3. const valueBucket1: relationalStore.ValuesBucket = { 'NAME': 'lisi', 'AGE': 21 };
4. const valueBucket2: relationalStore.ValuesBucket = { 'NAME': 'lisi', 'AGE': 18 };
5. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
6. predicates.equalTo('NAME', 'lisi');
7. const config: relationalStore.ReturningConfig = { columns: ['NAME', 'AGE'] };
8. try {
9. trans.batchInsertWithReturningSync("EMPLOYEE", [valueBucket1, valueBucket2], config);
10. valueBucket1['NAME'] = "zhangsan";
11. valueBucket1['AGE'] = 18;
12. let results = trans.updateWithReturningSync(valueBucket1, predicates, config);
13. console.info(`transUpdateWithReturningSyncExample is successful, changed is ${results.changed}`);
14. while(results.resultSet.goToNextRow()) {
15. const row = results.resultSet.getRow();
16. console.info(`transUpdateWithReturningSyncExample, name is ${row['NAME']}, age is ${row['AGE']}`);
17. }
18. } catch (e) {
19. console.error(`transUpdateWithReturningSyncExample failed. code is ${e.code}, message is ${e.message}`);
20. }
21. }
```

## delete14+

PhonePC/2in1TabletTVWearable

delete(predicates: RdbPredicates):Promise<number>

根据RdbPredicates的指定实例对象从数据库中删除数据，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicates | [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 是 | RdbPredicates的实例对象指定的删除条件。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回受影响的行数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800021 | SQLite: Generic error. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800033 | SQLite: Data type mismatch. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. let predicates2 = new relationalStore.RdbPredicates('EMPLOYEE');
2. predicates2.equalTo('NAME', 'Lisa');

4. if (store != undefined) {
5. try {
6. const transaction = await store.createTransaction();
7. try {
8. const rows = await transaction.delete(predicates2);
9. await transaction.commit();
10. console.info(`Delete rows: ${rows}`);
11. } catch (error) {
12. const err = error as BusinessError;
13. await transaction.rollback();
14. console.error(`Delete failed, code is ${err.code},message is ${err.message}`);
15. }
16. } catch (error) {
17. const err = error as BusinessError;
18. console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
19. }
20. }
```

## deleteSync14+

PhonePC/2in1TabletTVWearable

deleteSync(predicates: RdbPredicates): number

根据RdbPredicates的指定实例对象从数据库中删除数据。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicates | [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 是 | RdbPredicates的实例对象指定的删除条件。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| number | 返回受影响的行数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800021 | SQLite: Generic error. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800033 | SQLite: Data type mismatch. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. let predicates3 = new relationalStore.RdbPredicates('EMPLOYEE');
2. predicates3.equalTo('NAME', 'Lisa');
3. if (store != undefined) {
4. try {
5. const transaction = await store.createTransaction();
6. try {
7. let rows = transaction.deleteSync(predicates3);
8. await transaction.commit();
9. console.info(`Delete rows: ${rows}`);
10. } catch (error) {
11. const err = error as BusinessError;
12. await transaction.rollback();
13. console.error(`Delete failed, code is ${err.code},message is ${err.message}`);
14. }
15. } catch (error) {
16. const err = error as BusinessError;
17. console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
18. }
19. }
```

## deleteWithReturning23+

PhonePC/2in1TabletTVWearable

deleteWithReturning(predicates: RdbPredicates, config: ReturningConfig): Promise<Result>

根据RdbPredicates的实例对象从数据库中删除数据，返回[Result](arkts-apis-data-relationalstore-i.md#result23)，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**模型约束：** 此接口仅在Stage模型下可用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicates | [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 是 | RdbPredicates的实例对象指定的删除条件。 |
| config | [ReturningConfig](arkts-apis-data-relationalstore-i.md#returningconfig23) | 是 | 指定返回值的配置信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Result](arkts-apis-data-relationalstore-i.md#result23)> | Promise对象。如果操作成功，返回受影响的数据集。 |

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1. Parameter is out of valid range. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. async function transDeleteWithReturningExample(trans: relationalStore.Transaction)
2. {
3. const valueBucket1: relationalStore.ValuesBucket = { 'NAME': 'lisi', 'AGE': 21 };
4. const valueBucket2: relationalStore.ValuesBucket = { 'NAME': 'zhangsan', 'AGE': 18 };
5. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
6. const config: relationalStore.ReturningConfig = { columns: ['NAME', 'AGE'] };
7. try {
8. trans.batchInsertWithReturningSync("EMPLOYEE", [valueBucket1, valueBucket2], config);
9. let results = await trans.deleteWithReturning(predicates, config);
10. console.info(`transDeleteWithReturningExample is successful, changed is ${results.changed}`);
11. while(results.resultSet.goToNextRow()) {
12. const row = results.resultSet.getRow();
13. console.info(`transDeleteWithReturningExample, name is ${row['NAME']}, age is ${row['AGE']}`);
14. }
15. } catch (e) {
16. console.error(`transDeleteWithReturningExample failed. code is ${e.code}, message is ${e.message}`);
17. }
18. }
```

## deleteWithReturningSync23+

PhonePC/2in1TabletTVWearable

deleteWithReturningSync(predicates: RdbPredicates, config: ReturningConfig): Result

根据RdbPredicates的实例对象从数据库中删除数据，返回[Result](arkts-apis-data-relationalstore-i.md#result23)。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**模型约束：** 此接口仅在Stage模型下可用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicates | [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 是 | RdbPredicates的实例对象指定的删除条件。 |
| config | [ReturningConfig](arkts-apis-data-relationalstore-i.md#returningconfig23) | 是 | 指定返回值的配置信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Result](arkts-apis-data-relationalstore-i.md#result23) | 如果操作成功，返回受影响的数据集。 |

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1. Parameter is out of valid range. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. function transDeleteWithReturningSyncExample(trans: relationalStore.Transaction)
2. {
3. const valueBucket1: relationalStore.ValuesBucket = { 'NAME': 'lisi', 'AGE': 21 };
4. const valueBucket2: relationalStore.ValuesBucket = { 'NAME': 'zhangsan', 'AGE': 18 };
5. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
6. const config: relationalStore.ReturningConfig = { columns: ['NAME', 'AGE'] };
7. try {
8. trans.batchInsertWithReturningSync("EMPLOYEE", [valueBucket1, valueBucket2], config);
9. let results = trans.deleteWithReturningSync(predicates, config);
10. console.info(`transDeleteWithReturningSyncExample is successful, changed is ${results.changed}`);
11. while(results.resultSet.goToNextRow()) {
12. const row = results.resultSet.getRow();
13. console.info(`transDeleteWithReturningSyncExample, name is ${row['NAME']}, age is ${row['AGE']}`);
14. }
15. } catch (e) {
16. console.error(`transDeleteWithReturningSyncExample failed. code is ${e.code}, message is ${e.message}`);
17. }
18. }
```

## query14+

PhonePC/2in1TabletTVWearable

query(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>

根据指定条件查询数据库中的数据，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicates | [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 是 | RdbPredicates的实例对象指定的查询条件。 |
| columns | Array<string> | 否 | 表示要查询的列。如果值为空，则查询应用于所有列。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[ResultSet](arkts-apis-data-relationalstore-resultset.md)> | Promise对象。如果操作成功，则返回ResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800021 | SQLite: Generic error. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. let predicates4 = new relationalStore.RdbPredicates('EMPLOYEE');
2. predicates4.equalTo('NAME', 'Rose');

4. if (store != undefined) {
5. try {
6. const transaction = await store.createTransaction();
7. try {
8. const resultSet = await transaction.query(predicates4, ['ID', 'NAME', 'AGE', 'SALARY', 'CODES']);
9. console.info(`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}`);
10. // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
11. while (resultSet.goToNextRow()) {
12. const id = resultSet.getLong(resultSet.getColumnIndex('ID'));
13. const name = resultSet.getString(resultSet.getColumnIndex('NAME'));
14. const age = resultSet.getLong(resultSet.getColumnIndex('AGE'));
15. const salary = resultSet.getDouble(resultSet.getColumnIndex('SALARY'));
16. console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
17. }
18. // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
19. resultSet.close();
20. await transaction.commit();
21. } catch (error) {
22. const err = error as BusinessError;
23. await transaction.rollback();
24. console.error(`Query failed, code is ${err.code},message is ${err.message}`);
25. }
26. } catch (error) {
27. const err = error as BusinessError;
28. console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
29. }
30. }
```

## querySync14+

PhonePC/2in1TabletTVWearable

querySync(predicates: RdbPredicates, columns?: Array<string>): ResultSet

根据指定条件查询数据库中的数据。对query同步接口获得的resultSet进行操作时，若逻辑复杂且循环次数过多，可能造成freeze问题，建议将此步骤放到[taskpool](js-apis-taskpool.md)线程中执行。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicates | [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 是 | RdbPredicates的实例对象指定的查询条件。 |
| columns | Array<string> | 否 | 表示要查询的列。如果值为空，则查询应用于所有列。默认值为空。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [ResultSet](arkts-apis-data-relationalstore-resultset.md) | 如果操作成功，则返回ResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800021 | SQLite: Generic error. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. let predicates5 = new relationalStore.RdbPredicates('EMPLOYEE');
2. predicates5.equalTo('NAME', 'Rose');

4. if (store != undefined) {
5. try {
6. const transaction = await store.createTransaction();
7. try {
8. let resultSet = transaction.querySync(predicates5, ['ID', 'NAME', 'AGE', 'SALARY', 'CODES']);
9. console.info(`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}`);
10. // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
11. while (resultSet.goToNextRow()) {
12. const id = resultSet.getLong(resultSet.getColumnIndex('ID'));
13. const name = resultSet.getString(resultSet.getColumnIndex('NAME'));
14. const age = resultSet.getLong(resultSet.getColumnIndex('AGE'));
15. const salary = resultSet.getDouble(resultSet.getColumnIndex('SALARY'));
16. console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
17. }
18. // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
19. resultSet.close();
20. await transaction.commit();
21. } catch (error) {
22. const err = error as BusinessError;
23. await transaction.rollback();
24. console.error(`Query failed, code is ${err.code},message is ${err.message}`);
25. }
26. } catch (error) {
27. const err = error as BusinessError;
28. console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
29. }
30. }
```

## querySql14+

PhonePC/2in1TabletTVWearable

querySql(sql: string, args?: Array<ValueType>): Promise<ResultSet>

根据指定SQL语句查询数据库中的数据，SQL语句中的各种表达式和操作符之间的关系操作符号不超过1000个，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sql | string | 是 | 指定要执行的SQL语句。 |
| args | Array<[ValueType](arkts-apis-data-relationalstore-t.md#valuetype)> | 否 | SQL语句中参数的值。该值与sql参数语句中的占位符相对应。当sql参数语句完整时，该参数不填。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[ResultSet](arkts-apis-data-relationalstore-resultset.md)> | Promise对象。如果操作成功，则返回ResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800021 | SQLite: Generic error. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. if (store != undefined) {
2. try {
3. const transaction = await store.createTransaction();
4. try {
5. const resultSet = await transaction.querySql("SELECT * FROM EMPLOYEE CROSS JOIN BOOK WHERE BOOK.NAME = 'sanguo'");
6. console.info(`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}`);
7. // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
8. while (resultSet.goToNextRow()) {
9. const id = resultSet.getLong(resultSet.getColumnIndex('ID'));
10. const name = resultSet.getString(resultSet.getColumnIndex('NAME'));
11. const age = resultSet.getLong(resultSet.getColumnIndex('AGE'));
12. const salary = resultSet.getDouble(resultSet.getColumnIndex('SALARY'));
13. console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
14. }
15. // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
16. resultSet.close();
17. await transaction.commit();
18. } catch (error) {
19. const err = error as BusinessError;
20. await transaction.rollback();
21. console.error(`Query failed, code is ${err.code},message is ${err.message}`);
22. }
23. } catch (error) {
24. const err = error as BusinessError;
25. console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
26. }
27. }
```

## querySqlSync14+

PhonePC/2in1TabletTVWearable

querySqlSync(sql: string, args?: Array<ValueType>): ResultSet

根据指定SQL语句查询数据库中的数据，SQL语句中的各种表达式和操作符之间的关系操作符号不超过1000个。对query同步接口获得的resultSet进行操作时，若逻辑复杂且循环次数过多，可能造成freeze问题，建议将此步骤放到[taskpool](js-apis-taskpool.md)线程中执行。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sql | string | 是 | 指定要执行的SQL语句。 |
| args | Array<[ValueType](arkts-apis-data-relationalstore-t.md#valuetype)> | 否 | SQL语句中参数的值。该值与sql参数语句中的占位符相对应。当sql参数语句完整时，该参数不填。默认值为空。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [ResultSet](arkts-apis-data-relationalstore-resultset.md) | 如果操作成功，则返回ResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800021 | SQLite: Generic error. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. if (store != undefined) {
2. try {
3. const transaction = await store.createTransaction();
4. try {
5. let resultSet = transaction.querySqlSync("SELECT * FROM EMPLOYEE CROSS JOIN BOOK WHERE BOOK.NAME = 'sanguo'");
6. console.info(`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}`);
7. // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
8. while (resultSet.goToNextRow()) {
9. const id = resultSet.getLong(resultSet.getColumnIndex('ID'));
10. const name = resultSet.getString(resultSet.getColumnIndex('NAME'));
11. const age = resultSet.getLong(resultSet.getColumnIndex('AGE'));
12. const salary = resultSet.getDouble(resultSet.getColumnIndex('SALARY'));
13. console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
14. }
15. // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
16. resultSet.close();
17. await transaction.commit();
18. } catch (error) {
19. const err = error as BusinessError;
20. await transaction.rollback();
21. console.error(`Query failed, code is ${err.code},message is ${err.message}`);
22. }
23. } catch (error) {
24. const err = error as BusinessError;
25. console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
26. }
27. }
```

## queryWithoutRowCount23+

PhonePC/2in1TabletTVWearable

queryWithoutRowCount(predicates: RdbPredicates, columns?: Array<string>): Promise<LiteResultSet>

根据指定条件查询数据库中的数据，查询时不计算行数，性能优于[query](arkts-apis-data-relationalstore-transaction.md#query14)接口。使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**模型约束：** 此接口仅在Stage模型下可用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicates | [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 是 | RdbPredicates的实例对象指定的查询条件。 |
| columns | Array<string> | 否 | 表示要查询的列。如果值为空，则查询应用于所有列。默认值为空。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[LiteResultSet](arkts-apis-data-relationalstore-literesultset.md)> | 如果操作成功，则返回LiteResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800014 | The target instance is already closed. |

**示例：**

```
1. async function queryWithoutRowCountExample(store : relationalStore.RdbStore) {
2. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
3. predicates.equalTo("NAME", "Rose");
4. if (store != undefined) {
5. try {
6. const transaction = await store.createTransaction();
7. let resultSet: relationalStore.LiteResultSet | undefined;
8. try {
9. resultSet = await transaction.queryWithoutRowCount(predicates, ["ID", "NAME", "AGE", "SALARY", "CODES"]);
10. if (resultSet != undefined) {
11. // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
12. while (resultSet.goToNextRow()) {
13. const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
14. const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
15. const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
16. const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
17. console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
18. }
19. // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
20. resultSet.close();
21. }
22. await transaction.commit();
23. } catch (err) {
24. console.error(`Query failed, code is ${err.code}, message is ${err.message}`);
25. // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
26. if (resultSet != undefined) {
27. resultSet.close();
28. }
29. await transaction.rollback();
30. }
31. } catch (err) {
32. console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
33. }
34. }
35. }
```

## queryWithoutRowCountSync23+

PhonePC/2in1TabletTVWearable

queryWithoutRowCountSync(predicates: RdbPredicates, columns?: Array<string>): LiteResultSet

根据指定条件查询数据库中的数据，查询时不计算行数。对queryWithoutRowCountSync同步接口获得的LiteResultSet进行操作时，若逻辑复杂且循环次数过多，可能造成freeze问题，建议将此步骤放到[taskpool](js-apis-taskpool.md)线程中执行。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**模型约束：** 此接口仅在Stage模型下可用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicates | [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 是 | RdbPredicates的实例对象指定的查询条件。 |
| columns | Array<string> | 否 | 表示要查询的列。如果值为空，则查询应用于所有列。默认值为空。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [LiteResultSet](arkts-apis-data-relationalstore-literesultset.md) | 如果操作成功，则返回LiteResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800014 | The target instance is already closed. |

**示例：**

```
1. async function queryWithoutRowCountSyncExample(store : relationalStore.RdbStore) {
2. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
3. predicates.equalTo("NAME", "Rose");
4. if (store != undefined) {
5. try {
6. const transaction = await store.createTransaction();
7. let resultSet: relationalStore.LiteResultSet | undefined;
8. try {
9. resultSet = transaction.queryWithoutRowCountSync(predicates, ["ID", "NAME", "AGE", "SALARY", "CODES"]);
10. if (resultSet != undefined) {
11. // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
12. while (resultSet.goToNextRow()) {
13. const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
14. const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
15. const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
16. const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
17. console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
18. }
19. // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
20. resultSet.close();
21. }
22. await transaction.commit();
23. } catch (err) {
24. console.error(`Query failed, code is ${err.code}, message is ${err.message}`);
25. // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
26. if (resultSet != undefined) {
27. resultSet.close();
28. }
29. await transaction.rollback();
30. }
31. } catch (err) {
32. console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
33. }
34. }
35. }
```

## querySqlWithoutRowCount23+

PhonePC/2in1TabletTVWearable

querySqlWithoutRowCount(sql: string, bindArgs?: Array<ValueType>): Promise<LiteResultSet>

根据指定条件查询数据库中的数据，查询时不计算行数。使用Promise异步回调。性能优于[querySql](arkts-apis-data-relationalstore-transaction.md#querysql14)接口。SQL语句中的各种表达式和操作符之间的关系操作符号不超过1000个。

**模型约束：** 此接口仅在Stage模型下可用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sql | string | 是 | 指定要执行的SQL语句。 |
| bindArgs | Array<[ValueType](arkts-apis-data-relationalstore-t.md#valuetype)> | 否 | SQL语句中参数的值。该值与sql参数语句中的占位符相对应。当sql参数语句完整时，该参数不填。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[LiteResultSet](arkts-apis-data-relationalstore-literesultset.md)> | Promise对象。如果操作成功，则返回LiteResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1.Parameter is out of valid range. |
| 14800014 | The target instance is already closed. |

**示例：**

```
1. async function querySqlWithoutRowCountExample(store : relationalStore.RdbStore) {
2. if (store != undefined) {
3. try {
4. const transaction = await store.createTransaction();
5. let resultSet: relationalStore.LiteResultSet | undefined;
6. try {
7. resultSet = await transaction.querySqlWithoutRowCount('select * from EMPLOYEE where name = ?', ["Rose"]);
8. if (resultSet != undefined) {
9. // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
10. while (resultSet.goToNextRow()) {
11. const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
12. const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
13. const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
14. const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
15. console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
16. }
17. // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
18. resultSet.close();
19. }
20. await transaction.commit();
21. } catch (err) {
22. console.error(`Query failed, code is ${err.code}, message is ${err.message}`);
23. // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
24. if (resultSet != undefined) {
25. resultSet.close();
26. }
27. await transaction.rollback();
28. }
29. } catch (err) {
30. console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
31. }
32. }
33. }
```

## querySqlWithoutRowCountSync23+

PhonePC/2in1TabletTVWearable

querySqlWithoutRowCountSync(sql: string, bindArgs?: Array<ValueType>):LiteResultSet

根据指定SQL语句查询数据库中的数据，查询时不计算行数。SQL语句中的各种表达式和操作符之间的关系操作符号不超过1000个。对querySqlWithoutRowCountSync同步接口获得的LiteResultSet进行操作时，若逻辑复杂且循环次数过多，可能造成freeze问题，建议将此步骤放到[taskpool](js-apis-taskpool.md)线程中执行。

**模型约束：** 此接口仅在Stage模型下可用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sql | string | 是 | 指定要执行的SQL语句。 |
| bindArgs | Array<[ValueType](arkts-apis-data-relationalstore-t.md#valuetype)> | 否 | SQL语句中参数的值。该值与sql参数语句中的占位符相对应。当sql参数语句完整时，该参数不填。默认值为空。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [LiteResultSet](arkts-apis-data-relationalstore-literesultset.md) | 如果操作成功，则返回LiteResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1.Parameter is out of valid range. |
| 14800014 | The target instance is already closed. |

**示例：**

```
1. async function querySqlWithoutRowCountSyncExample(store : relationalStore.RdbStore) {
2. if (store != undefined) {
3. try {
4. const transaction = await store.createTransaction();
5. let resultSet: relationalStore.LiteResultSet | undefined;
6. try {
7. resultSet = transaction.querySqlWithoutRowCountSync('select * from EMPLOYEE where name = ?', ["Rose"]);
8. if (resultSet != undefined) {
9. // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
10. while (resultSet.goToNextRow()) {
11. const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
12. const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
13. const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
14. const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
15. console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
16. }
17. // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
18. resultSet.close();
19. }
20. await transaction.commit();
21. } catch (err) {
22. console.error(`Query failed, code is ${err.code}, message is ${err.message}`);
23. // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
24. if (resultSet != undefined) {
25. resultSet.close();
26. }
27. await transaction.rollback();
28. }
29. } catch (err) {
30. console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
31. }
32. }
33. }
```

## execute14+

PhonePC/2in1TabletTVWearable

execute(sql: string, args?: Array<ValueType>): Promise<ValueType>

执行包含指定参数的SQL语句，语句中的各种表达式和操作符之间的关系操作符号不超过1000个，返回值类型为ValueType，使用Promise异步回调。

该接口支持执行增删改操作，支持执行PRAGMA语法的sql，支持对表的操作（建表、删表、修改表），返回结果类型由执行具体sql的结果决定。

此接口不支持执行查询、附加数据库和事务操作，查询可以使用[querySql](arkts-apis-data-relationalstore-transaction.md#querysql14)、[query](arkts-apis-data-relationalstore-transaction.md#query14)接口代替、附加数据库可以使用[attach](arkts-apis-data-relationalstore-rdbstore.md#attach12)接口代替。

不支持分号分隔的多条语句。

不支持开头包含注释的语句。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sql | string | 是 | 指定要执行的SQL语句。 |
| args | Array<[ValueType](arkts-apis-data-relationalstore-t.md#valuetype)> | 否 | SQL语句中参数的值。该值与sql参数语句中的占位符相对应。当sql参数语句完整时，该参数不填。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[ValueType](arkts-apis-data-relationalstore-t.md#valuetype)> | Promise对象，返回sql执行后的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported the sql(attach,begin,commit,rollback etc.). |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800033 | SQLite: Data type mismatch. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. if (store != undefined) {
2. try {
3. const transaction = await store.createTransaction();
4. try {
5. // 删除表中所有数据
6. const SQL_DELETE_TABLE = 'DELETE FROM EMPLOYEE';
7. const data = await transaction.execute(SQL_DELETE_TABLE);
8. await transaction.commit();
9. console.info(`delete result: ${data}`);
10. } catch (error) {
11. const err = error as BusinessError;
12. await transaction.rollback();
13. console.error(`delete failed, code is ${err.code}, message is ${err.message}`);
14. }
15. } catch (error) {
16. const err = error as BusinessError;
17. console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
18. }
19. }
```

## executeSync14+

PhonePC/2in1TabletTVWearable

executeSync(sql: string, args?: Array<ValueType>): ValueType

执行包含指定参数的SQL语句，语句中的各种表达式和操作符之间的关系操作符号不超过1000个，返回值类型为ValueType。

该接口支持执行增删改操作，支持执行PRAGMA语法的sql，支持对表的操作（建表、删表、修改表），返回结果类型由执行具体sql的结果决定。

此接口不支持执行查询、附加数据库和事务操作，查询可以使用[querySql](arkts-apis-data-relationalstore-transaction.md#querysql14)、[query](arkts-apis-data-relationalstore-transaction.md#query14)接口代替、附加数据库可以使用[attach](arkts-apis-data-relationalstore-rdbstore.md#attach12)接口代替。

不支持分号分隔的多条语句。

不支持开头包含注释的语句。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sql | string | 是 | 指定要执行的SQL语句。 |
| args | Array<[ValueType](arkts-apis-data-relationalstore-t.md#valuetype)> | 否 | SQL语句中参数的值。该值与sql参数语句中的占位符相对应。该参数不填，或者填null或undefined，都认为是sql参数语句完整。默认值为空。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [ValueType](arkts-apis-data-relationalstore-t.md#valuetype) | 返回sql执行后的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported the sql(attach,begin,commit,rollback etc.). |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800033 | SQLite: Data type mismatch. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. // 删除表中所有数据
2. if (store != undefined) {
3. try {
4. const transaction = await store.createTransaction();
5. try {
6. const SQL_DELETE_TABLE = 'DELETE FROM EMPLOYEE';
7. let data = transaction.executeSync(SQL_DELETE_TABLE);
8. await transaction.commit();
9. console.info(`delete result: ${data}`);
10. } catch (error) {
11. const err = error as BusinessError;
12. await transaction.rollback();
13. console.error(`delete failed, code is ${err.code}, message is ${err.message}`);
14. }
15. } catch (error) {
16. const err = error as BusinessError;
17. console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
18. }
19. }
```
