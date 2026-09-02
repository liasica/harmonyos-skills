---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-transaction
title: Interface (Transaction)
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > ArkTS API > @ohos.data.relationalStore (关系型数据库) > Interface (Transaction)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:40+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bb64f87285205e36eda841f7cc3bbeac5f1694c06fed977e0bf875e22c9d2db0
---

提供以事务方式管理数据库的方法。事务对象是通过[createTransaction](arkts-apis-data-relationalstore-rdbstore.md#createtransaction14)接口创建的，不同事务对象之间的操作是隔离的，不同类型事务的区别见[TransactionType](arkts-apis-data-relationalstore-e.md#transactiontype14) 。

当前关系型数据库同一时刻仅支持一个写事务，所以如果当前[RdbStore](arkts-apis-data-relationalstore-rdbstore.md)存在写事务未释放，创建IMMEDIATE或EXCLUSIVE事务会返回14800024错误码。如果是创建的DEFERRED事务，则可能在首次使用DEFERRED事务调用写操作时返回14800024错误码。通过IMMEDIATE或EXCLUSIVE创建写事务或者DEFERRED事务升级到写事务之后，[RdbStore](arkts-apis-data-relationalstore-rdbstore.md)的写操作也会返回14800024错误码。

当事务并发量较高且写事务持续时间较长时，返回14800024错误码的次数可能会变多，开发者可以通过减少事务占用时长减少14800024出现的次数，也可以通过重试的方式处理14800024错误码。

在使用以下API前，请先通过[createTransaction](arkts-apis-data-relationalstore-rdbstore.md#createtransaction14)方法获取Transaction实例，再通过此实例调用对应方法。

**说明** 

* 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 14开始支持。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**示例：**

示例代码中this.context定义见Stage模型的应用[Context](js-apis-inner-application-context.md)。

```ts
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

let store: relationalStore.RdbStore | undefined = undefined;

export default class EntryAbility extends UIAbility {
  async onWindowStageCreate(windowStage: window.WindowStage) {
    const STORE_CONFIG: relationalStore.StoreConfig = {
      name: 'RdbTest.db',
      securityLevel: relationalStore.SecurityLevel.S3
    };

    try {
      const rdbStore = await relationalStore.getRdbStore(this.context, STORE_CONFIG);
      store = rdbStore;
      console.info('Get RdbStore successfully.');
    } catch (error) {
      const err = error as BusinessError;
      console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
    }

    if (store != undefined) {
      await store.executeSql('CREATE TABLE IF NOT EXISTS EMPLOYEE (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, AGE INTEGER, SALARY REAL, CODES BLOB, IDENTITY UNLIMITED INT, ASSETDATA ASSET, ASSETSDATA ASSETS, FLOATARRAY floatvector(128))');
      store.createTransaction().then(async (transaction: relationalStore.Transaction) => {
        console.info(`createTransaction success`);
        // 成功获取到事务对象后执行后续操作
      }).catch((err: BusinessError) => {
        console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
      });
    }
  }
}
```

## 导入模块

```ts
import { relationalStore } from '@kit.ArkData';
```

## commit14+

commit(): Promise<void>

提交已执行的SQL语句，使用Promise异步回调。如果是使用异步接口执行sql语句，请确保异步接口执行完成之后再调用commit接口，否则可能会丢失SQL操作。调用commit接口之后，该Transaction对象及创建的ResultSet对象都将被关闭。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

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

```ts
if (store != undefined) {
  try {
    const transaction = await store.createTransaction();
    try {
      await transaction.execute('CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, age INTEGER, salary REAL)');
      await transaction.commit();
    } catch (error) {
      const err = error as BusinessError;
      await transaction.rollback();
      console.error(`execute sql failed, code is ${err.code},message is ${err.message}`);
    }
  } catch (error) {
    const err = error as BusinessError;
    console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
  }
}
```

## rollback14+

rollback(): Promise<void>

回滚已经执行的SQL语句，使用Promise异步回调。调用rollback接口之后，该Transaction对象及创建的ResultSet对象都会被关闭。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

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

```ts
if (store != undefined) {
  try {
    const transaction = await store.createTransaction();
    try {
      await transaction.execute('DELETE FROM TEST WHERE age = ? OR age = ?', ['18', '20']);
      await transaction.commit();
    } catch (error) {
      const err = error as BusinessError;
      await transaction.rollback();
      console.error(`execute sql failed, code is ${err.code},message is ${err.message}`);
    }
  } catch (error) {
    const err = error as BusinessError;
    console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
  }
}
```

## insert14+

insert(table: string, values: ValuesBucket, conflict?: ConflictResolution): Promise<number>

向目标表中插入一行数据，使用Promise异步回调。

由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。

如果单条数据超过此限制，在后续通过RdbStore的[query](arkts-apis-data-relationalstore-rdbstore.md#query)或[querySql](arkts-apis-data-relationalstore-rdbstore.md#querysql)接口获取ResultSet后，调用[getValue](arkts-apis-data-relationalstore-resultset.md#getvalue12)、[getString](arkts-apis-data-relationalstore-resultset.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

如需读取超过2MB的数据，请使用[queryByStep](arkts-apis-data-relationalstore-rdbstore.md#querybystep)接口。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 指定的目标表名，不能为空字符串，不应包含空格、逗号和星号，不能以点开头和结尾等，否则会抛出401错误码。 |
| values | [ValuesBucket](arkts-apis-data-relationalstore-t.md#valuesbucket) | 是 | 表示要插入到表中的数据行。 |
| conflict | [ConflictResolution](arkts-apis-data-relationalstore-e.md#conflictresolution10) | 否 | 指定冲突解决模式。默认值是relationalStore.ConflictResolution.ON\_CONFLICT\_NONE。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回插入数据的行ID。 |

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

```ts
const valueBucket1: relationalStore.ValuesBucket = {
  NAME: 'Lisa',
  AGE: 18,
  SALARY: 100.5,
  CODES: new Uint8Array([1, 2, 3, 4, 5])
};

if (store != undefined) {
  try {
    const transaction = await store.createTransaction();
    try {
      const rowId = await transaction.insert('EMPLOYEE', valueBucket1, relationalStore.ConflictResolution.ON_CONFLICT_REPLACE);
      await transaction.commit();
      console.info(`Insert is successful, rowId = ${rowId}`);
    } catch (error) {
      const err = error as BusinessError;
      await transaction.rollback();
      console.error(`Insert is failed, code is ${err.code},message is ${err.message}`);
    }
  } catch (error) {
    const err = error as BusinessError;
    console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
  }
}
```

## insertSync14+

insertSync(table: string, values: ValuesBucket | sendableRelationalStore.ValuesBucket, conflict?: ConflictResolution): number

向目标表中插入一行数据。

由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。

如果单条数据超过此限制，在后续通过RdbStore的[query](arkts-apis-data-relationalstore-rdbstore.md#query)或[querySql](arkts-apis-data-relationalstore-rdbstore.md#querysql)接口获取ResultSet后，调用[getValue](arkts-apis-data-relationalstore-resultset.md#getvalue12)、[getString](arkts-apis-data-relationalstore-resultset.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

如需读取超过2MB的数据，请使用[queryByStep](arkts-apis-data-relationalstore-rdbstore.md#querybystep)接口。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 指定的目标表名，不能为空字符串。 |
| values | [ValuesBucket](arkts-apis-data-relationalstore-t.md#valuesbucket) | [sendableRelationalStore.ValuesBucket](js-apis-data-sendablerelationalstore.md#valuesbucket) | 是 | 表示要插入到表中的数据行。 |
| conflict | [ConflictResolution](arkts-apis-data-relationalstore-e.md#conflictresolution10) | 否 | 指定冲突解决模式。默认值是relationalStore.ConflictResolution.ON\_CONFLICT\_NONE。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| number | 返回插入数据的行ID。 |

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

```ts
let value5 = 'Lisa';
let value6 = 18;
let value7 = 100.5;
let value8 = new Uint8Array([1, 2, 3, 4, 5]);

const valueBucket2: relationalStore.ValuesBucket = {
  NAME: value5,
  AGE: value6,
  SALARY: value7,
  CODES: value8
};
if (store != undefined) {
  try {
    const transaction = await store.createTransaction();
    try {
      let rowId: number = transaction.insertSync(
        'EMPLOYEE',
        valueBucket2,
        relationalStore.ConflictResolution.ON_CONFLICT_REPLACE
      );
      await transaction.commit();
      console.info(`Insert is successful, rowId = ${rowId}`);
    } catch (e) {
      await transaction.rollback();
      console.error(`Insert is failed, code is ${e.code},message is ${e.message}`);
    }
  } catch (error) {
    const err = error as BusinessError;
    console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
  }
}
```

## batchInsert14+

batchInsert(table: string, values: Array<ValuesBucket>): Promise<number>

向目标表中插入一组数据，使用Promise异步回调。

由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。

如果单条数据超过此限制，在后续通过RdbStore的[query](arkts-apis-data-relationalstore-rdbstore.md#query)或[querySql](arkts-apis-data-relationalstore-rdbstore.md#querysql)接口获取ResultSet后，调用[getValue](arkts-apis-data-relationalstore-resultset.md#getvalue12)、[getString](arkts-apis-data-relationalstore-resultset.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

如需读取超过2MB的数据，请使用[queryByStep](arkts-apis-data-relationalstore-rdbstore.md#querybystep)接口。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

按每批32766个参数，分批以[ConflictResolution.ON\_CONFLICT\_REPLACE](arkts-apis-data-relationalstore-e.md#conflictresolution10)策略写入，参数数量计算方式为插入数据条数乘以插入数据的所有字段的并集大小，中途失败则立即返回。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 指定的目标表名，不能为空字符串。 |
| values | Array<[ValuesBucket](arkts-apis-data-relationalstore-t.md#valuesbucket)> | 是 | 表示要插入到表中的一组数据。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回批量插入的数据个数。 |

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

```ts
const valueBucket3: relationalStore.ValuesBucket = {
  NAME: 'Lisa',
  AGE: 18,
  SALARY: 100.5,
  CODES: new Uint8Array([1, 2, 3, 4, 5])
};
const valueBucket4: relationalStore.ValuesBucket = {
  NAME: 'Jack',
  AGE: 19,
  SALARY: 101.5,
  CODES: new Uint8Array([6, 7, 8, 9, 10])
};
const valueBucket5: relationalStore.ValuesBucket = {
  NAME: 'Tom',
  AGE: 20,
  SALARY: 102.5,
  CODES: new Uint8Array([11, 12, 13, 14, 15])
};

let valueBuckets = new Array(valueBucket3, valueBucket4, valueBucket5);
if (store != undefined) {
  try {
    const transaction = await store.createTransaction();
    try {
      const insertNum = await transaction.batchInsert('EMPLOYEE', valueBuckets);
      await transaction.commit();
      console.info(`batchInsert is successful, the number of values that were inserted = ${insertNum}`);
    } catch (error) {
      const err = error as BusinessError;
      await transaction.rollback();
      console.error(`batchInsert is failed, code is ${err.code},message is ${err.message}`);
    }
  } catch (error) {
    const err = error as BusinessError;
    console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
  }
}
```

## batchInsertSync14+

batchInsertSync(table: string, values: Array<ValuesBucket>): number

向目标表中插入一组数据。

由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。

如果单条数据超过此限制，在后续通过RdbStore的[query](arkts-apis-data-relationalstore-rdbstore.md#query)或[querySql](arkts-apis-data-relationalstore-rdbstore.md#querysql)接口获取ResultSet后，调用[getValue](arkts-apis-data-relationalstore-resultset.md#getvalue12)、[getString](arkts-apis-data-relationalstore-resultset.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

如需读取超过2MB的数据，请使用[queryByStep](arkts-apis-data-relationalstore-rdbstore.md#querybystep)接口。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

按每批32766个参数，分批以[ConflictResolution.ON\_CONFLICT\_REPLACE](arkts-apis-data-relationalstore-e.md#conflictresolution10)策略写入，参数数量计算方式为插入数据条数乘以插入数据的所有字段的并集大小，中途失败则立即返回。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 指定的目标表名，不能为空字符串。 |
| values | Array<[ValuesBucket](arkts-apis-data-relationalstore-t.md#valuesbucket)> | 是 | 表示要插入到表中的一组数据。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| number | 返回批量插入的数据个数。 |

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

```ts
const valueBucket6: relationalStore.ValuesBucket = {
  NAME: 'Lisa',
  AGE: 18,
  SALARY: 100.5,
  CODES: new Uint8Array([1, 2, 3, 4, 5])
};
const valueBucket7: relationalStore.ValuesBucket = {
  NAME: 'Jack',
  AGE: 19,
  SALARY: 101.5,
  CODES: new Uint8Array([6, 7, 8, 9, 10])
};
const valueBucket8: relationalStore.ValuesBucket = {
  NAME: 'Tom',
  AGE: 20,
  SALARY: 102.5,
  CODES: new Uint8Array([11, 12, 13, 14, 15])
};

let valueBuckets2 = new Array(valueBucket6, valueBucket7, valueBucket8);
if (store != undefined) {
  try {
    const transaction = await store.createTransaction();
    try {
      let insertNum: number = (transaction as relationalStore.Transaction).batchInsertSync('EMPLOYEE', valueBuckets2);
      await transaction.commit();
      console.info(`batchInsert is successful, the number of values that were inserted = ${insertNum}`);
    } catch (error) {
      const err = error as BusinessError;
      await transaction.rollback();
      console.error(`batchInsert is failed, code is ${err.code},message is ${err.message}`);
    }
  } catch (error) {
    const err = error as BusinessError;
    console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
  }
}
```

## batchInsertWithConflictResolution18+

batchInsertWithConflictResolution(table: string, values: Array<ValuesBucket>, conflict: ConflictResolution): Promise<number>

向目标表中插入一组数据，可以通过conflict参数指定冲突解决模式[ConflictResolution](arkts-apis-data-relationalstore-e.md#conflictresolution10)，使用Promise异步回调。

由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。

如果单条数据超过此限制，在后续通过RdbStore的[query](arkts-apis-data-relationalstore-rdbstore.md#query)或[querySql](arkts-apis-data-relationalstore-rdbstore.md#querysql)接口获取ResultSet后，调用[getValue](arkts-apis-data-relationalstore-resultset.md#getvalue12)、[getString](arkts-apis-data-relationalstore-resultset.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

如需读取超过2MB的数据，请使用[queryByStep](arkts-apis-data-relationalstore-rdbstore.md#querybystep)接口。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

单次插入参数的最大数量限制为32766，超出上限会返回14800000错误码。参数数量计算方式为插入数据条数乘以插入数据的所有字段的并集大小。

例如：插入数据的所有字段的并集大小为10，则最多可以插入3276条数据（3276\*10=32760）。

请确保在调用接口时遵守此限制，以避免因参数数量过多而导致错误。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 指定的目标表名，不能为空字符串。 |
| values | Array<[ValuesBucket](arkts-apis-data-relationalstore-t.md#valuesbucket)> | 是 | 表示要插入到表中的一组数据。 |
| conflict | [ConflictResolution](arkts-apis-data-relationalstore-e.md#conflictresolution10) | 是 | 指定冲突解决模式。如果是ON\_CONFLICT\_ROLLBACK模式，当发生冲突时会回滚整个事务。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回批量插入的数据个数。 |

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

```ts
const valueBucket9: relationalStore.ValuesBucket = {
  NAME: 'Lisa',
  AGE: 18,
  SALARY: 100.5,
  CODES: new Uint8Array([1, 2, 3, 4, 5])
};
const valueBucketA: relationalStore.ValuesBucket = {
  NAME: 'Jack',
  AGE: 19,
  SALARY: 101.5,
  CODES: new Uint8Array([6, 7, 8, 9, 10])
};
const valueBucketB: relationalStore.ValuesBucket = {
  NAME: 'Tom',
  AGE: 20,
  SALARY: 102.5,
  CODES: new Uint8Array([11, 12, 13, 14, 15])
};

let valueBuckets3 = new Array(valueBucket9, valueBucketA, valueBucketB);

if (store != undefined) {
  try {
    const transaction = await store.createTransaction();
    try {
      const insertNum = await transaction.batchInsertWithConflictResolution(
        'EMPLOYEE',
        valueBuckets3,
        relationalStore.ConflictResolution.ON_CONFLICT_REPLACE
      );
      await transaction.commit();
      console.info(`batchInsert is successful, the number of values that were inserted = ${insertNum}`);
    } catch (error) {
      const err = error as BusinessError;
      await transaction.rollback();
      console.error(`batchInsert is failed, code is ${err.code},message is ${err.message}`);
    }
  } catch (error) {
    const err = error as BusinessError;
    console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
  }
}
```

## batchInsertWithConflictResolutionSync18+

batchInsertWithConflictResolutionSync(table: string, values: Array<ValuesBucket>, conflict: ConflictResolution): number

向目标表中插入一组数据，可以通过conflict参数指定冲突解决模式[ConflictResolution](arkts-apis-data-relationalstore-e.md#conflictresolution10)。

由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。

如果单条数据超过此限制，在后续通过RdbStore的[query](arkts-apis-data-relationalstore-rdbstore.md#query)或[querySql](arkts-apis-data-relationalstore-rdbstore.md#querysql)接口获取ResultSet后，调用[getValue](arkts-apis-data-relationalstore-resultset.md#getvalue12)、[getString](arkts-apis-data-relationalstore-resultset.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

如需读取超过2MB的数据，请使用[queryByStep](arkts-apis-data-relationalstore-rdbstore.md#querybystep)接口。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

单次插入参数的最大数量限制为32766，超出上限会返回14800000错误码。参数数量计算方式为插入数据条数乘以插入数据的所有字段的并集大小。

例如：插入数据的所有字段的并集大小为10，则最多可以插入3276条数据（3276\*10=32760）。

请确保在调用接口时遵守此限制，以避免因参数数量过多而导致错误。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 指定的目标表名，不能为空字符串。 |
| values | Array<[ValuesBucket](arkts-apis-data-relationalstore-t.md#valuesbucket)> | 是 | 表示要插入到表中的一组数据。 |
| conflict | [ConflictResolution](arkts-apis-data-relationalstore-e.md#conflictresolution10) | 是 | 指定冲突解决模式。如果是ON\_CONFLICT\_ROLLBACK模式，当发生冲突时会回滚整个事务。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| number | 返回批量插入的数据个数。 |

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

```ts
const valueBucketC: relationalStore.ValuesBucket = {
  NAME: 'Lisa',
  AGE: 18,
  SALARY: 100.5,
  CODES: new Uint8Array([1, 2, 3, 4, 5])
};
const valueBucketD: relationalStore.ValuesBucket = {
  NAME: 'Jack',
  AGE: 19,
  SALARY: 101.5,
  CODES: new Uint8Array([6, 7, 8, 9, 10])
};
const valueBucketE: relationalStore.ValuesBucket = {
  NAME: 'Tom',
  AGE: 20,
  SALARY: 102.5,
  CODES: new Uint8Array([11, 12, 13, 14, 15])
};

let valueBuckets4 = new Array(valueBucketC, valueBucketD, valueBucketE);
if (store != undefined) {
  try {
    const transaction = await store.createTransaction();
    try {
      const insertNum = transaction.batchInsertWithConflictResolutionSync(
        'EMPLOYEE',
        valueBuckets4,
        relationalStore.ConflictResolution.ON_CONFLICT_REPLACE
      );
      await transaction.commit();
      console.info(`batchInsert is successful, the number of values that were inserted = ${insertNum}`);
    } catch (error) {
      const err = error as BusinessError;
      await transaction.rollback();
      console.error(`batchInsert is failed, code is ${err.code},message is ${err.message}`);
    }
  } catch (error) {
    const err = error as BusinessError;
    console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
  }
}
```

## batchInsertWithReturning23+

batchInsertWithReturning(table: string, values: Array<ValuesBucket>, config: ReturningConfig, conflict?: ConflictResolution): Promise<Result>

向目标表中插入一组数据，可以通过conflict参数指定当发生数据冲突时的解决模式[ConflictResolution](arkts-apis-data-relationalstore-e.md#conflictresolution10)，返回[Result](arkts-apis-data-relationalstore-i.md#result23)。使用Promise异步回调。

由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。

如果单条数据超过此限制，在后续通过RdbStore的[query](arkts-apis-data-relationalstore-rdbstore.md#query)或[querySql](arkts-apis-data-relationalstore-rdbstore.md#querysql)接口获取ResultSet后，调用[getValue](arkts-apis-data-relationalstore-resultset.md#getvalue12)、[getString](arkts-apis-data-relationalstore-resultset.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

如需读取超过2MB的数据，请使用[queryByStep](arkts-apis-data-relationalstore-rdbstore.md#querybystep)接口。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

单次插入参数的最大数量限制为32766，超出上限会返回14800001错误码。参数数量计算方式为插入数据条数乘以插入数据的所有字段的并集大小。

例如：插入数据的所有字段的并集大小为10，则最多可以插入3276条数据（3276\*10=32760）。

请确保在调用接口时遵守此限制，以避免因参数数量过多而导致错误。

conflict参数不建议使用ON\_CONFLICT\_FAIL策略，可能无法返回正确的结果。

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
| Promise<[Result](arkts-apis-data-relationalstore-i.md#result23)> | Promise对象。返回受影响的数据集。 |

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

```ts
async function transBatchInsertWithReturningExample(trans: relationalStore.Transaction)
{
  const valueBucket1: relationalStore.ValuesBucket = { 'NAME': 'zhangsan', 'AGE': 18 };
  const valueBucket2: relationalStore.ValuesBucket = { 'NAME': 'lisi', 'AGE': 20 };
  const config: relationalStore.ReturningConfig = { columns: ['NAME', 'AGE'] };
  const valueBuckets = new Array(valueBucket1, valueBucket2);
  try {
    let results = await trans.batchInsertWithReturning("EMPLOYEE", valueBuckets, config);
    console.info(`transBatchInsertWithReturningExample is successful, changed is ${results.changed}`);
    while(results.resultSet.goToNextRow()) {
      const row = results.resultSet.getRow();
      console.info(`transBatchInsertWithReturningExample, name is ${row['NAME']}, age is ${row['AGE']}`);
    }
  } catch (e) {
    console.error(`transBatchInsertWithReturningExample failed. code is ${e.code}, message is ${e.message}`);
  }
}
```

## batchInsertWithReturningSync23+

batchInsertWithReturningSync(table: string, values: Array<ValuesBucket>, config: ReturningConfig, conflict?: ConflictResolution): Result

向目标表中插入一组数据，可以通过conflict参数指定当发生数据冲突时的解决模式[ConflictResolution](arkts-apis-data-relationalstore-e.md#conflictresolution10)，返回[Result](arkts-apis-data-relationalstore-i.md#result23)。

由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。

如果单条数据超过此限制，在后续通过RdbStore的[query](arkts-apis-data-relationalstore-rdbstore.md#query)或[querySql](arkts-apis-data-relationalstore-rdbstore.md#querysql)接口获取ResultSet后，调用[getValue](arkts-apis-data-relationalstore-resultset.md#getvalue12)、[getString](arkts-apis-data-relationalstore-resultset.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

如需读取超过2MB的数据，请使用[queryByStep](arkts-apis-data-relationalstore-rdbstore.md#querybystep)接口。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

单次插入参数的最大数量限制为32766，超出上限会返回14800001错误码。参数数量计算方式为插入数据条数乘以插入数据的所有字段的并集大小。

例如：插入数据的所有字段的并集大小为10，则最多可以插入3276条数据（3276\*10=32760）。

请确保在调用接口时遵守此限制，以避免因参数数量过多而导致错误。

conflict参数不建议使用ON\_CONFLICT\_FAIL策略，可能无法返回正确的结果。

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
| [Result](arkts-apis-data-relationalstore-i.md#result23) | 返回受影响的数据集。 |

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

```ts
function transBatchInsertWithReturningSyncExample(trans: relationalStore.Transaction)
{
  const valueBucket1: relationalStore.ValuesBucket = { 'NAME': 'zhangsan', 'AGE': 18 };
  const valueBucket2: relationalStore.ValuesBucket = { 'NAME': 'lisi', 'AGE': 20 };
  const config: relationalStore.ReturningConfig = { columns: ['NAME', 'AGE'] };
  const valueBuckets = new Array(valueBucket1, valueBucket2);
  try {
    let results = trans.batchInsertWithReturningSync("EMPLOYEE", valueBuckets, config);
    console.info(`transBatchInsertWithReturningSyncExample is successful, changed is ${results.changed}`);
    while(results.resultSet.goToNextRow()) {
      const row = results.resultSet.getRow();
      console.info(`transBatchInsertWithReturningSyncExample, name is ${row['NAME']}, age is ${row['AGE']}`);
    }
  } catch (e) {
    console.error(`transBatchInsertWithReturningSyncExample failed. code is ${e.code}, message is ${e.message}`);
  }
}
```

## update14+

update(values: ValuesBucket, predicates: RdbPredicates, conflict?: ConflictResolution): Promise<number>

根据RdbPredicates的指定实例对象更新数据库中的数据，使用Promise异步回调。

由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。

如果单条数据超过此限制，在后续通过RdbStore的[query](arkts-apis-data-relationalstore-rdbstore.md#query)或[querySql](arkts-apis-data-relationalstore-rdbstore.md#querysql)接口获取ResultSet后，调用[getValue](arkts-apis-data-relationalstore-resultset.md#getvalue12)、[getString](arkts-apis-data-relationalstore-resultset.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

如需读取超过2MB的数据，请使用[queryByStep](arkts-apis-data-relationalstore-rdbstore.md#querybystep)接口。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

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
| Promise<number> | Promise对象。返回受影响的行数。 |

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

```ts
const valueBucketF: relationalStore.ValuesBucket = {
  NAME: 'Rose',
  AGE: 22,
  SALARY: 200.5,
  CODES: new Uint8Array([1, 2, 3, 4, 5])
};
let predicates = new relationalStore.RdbPredicates('EMPLOYEE');
predicates.equalTo('NAME', 'Lisa');

if (store != undefined) {
  try {
    const transaction = await store.createTransaction();
    try {
      const rows = await transaction.update(valueBucketF, predicates, relationalStore.ConflictResolution.ON_CONFLICT_REPLACE);
      await transaction.commit();
      console.info(`Updated row count: ${rows}`);
    } catch (error) {
      const err = error as BusinessError;
      await transaction.rollback();
      console.error(`Updated failed, code is ${err.code},message is ${err.message}`);
    }
  } catch (error) {
    const err = error as BusinessError;
    console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
  }
}
```

## updateSync14+

updateSync(values: ValuesBucket, predicates: RdbPredicates, conflict?: ConflictResolution): number

根据RdbPredicates的指定实例对象更新数据库中的数据。

由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。

如果单条数据超过此限制，在后续通过RdbStore的[query](arkts-apis-data-relationalstore-rdbstore.md#query)或[querySql](arkts-apis-data-relationalstore-rdbstore.md#querysql)接口获取ResultSet后，调用[getValue](arkts-apis-data-relationalstore-resultset.md#getvalue12)、[getString](arkts-apis-data-relationalstore-resultset.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

如需读取超过2MB的数据，请使用[queryByStep](arkts-apis-data-relationalstore-rdbstore.md#querybystep)接口。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

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

```ts
const valueBucketG: relationalStore.ValuesBucket = {
  NAME: 'Rose',
  AGE: 22,
  SALARY: 200.5,
  CODES: new Uint8Array([1, 2, 3, 4, 5])
};
let predicates1 = new relationalStore.RdbPredicates('EMPLOYEE');
predicates1.equalTo('NAME', 'Lisa');

if (store != undefined) {
  try {
    const transaction = await store.createTransaction();
    try {
      let rows = transaction.updateSync(valueBucketG, predicates1, relationalStore.ConflictResolution.ON_CONFLICT_REPLACE);
      await transaction.commit();
      console.info(`Updated row count: ${rows}`);
    } catch (error) {
      const err = error as BusinessError;
      await transaction.rollback();
      console.error(`Updated failed, code is ${err.code},message is ${err.message}`);
    }
  } catch (error) {
    const err = error as BusinessError;
    console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
  }
}
```

## updateWithReturning23+

updateWithReturning(values: ValuesBucket, predicates: RdbPredicates, config: ReturningConfig, conflict?: ConflictResolution): Promise<Result>

根据RdbPredicates的指定实例对象更新数据库中的数据，可以通过conflict参数指定当发生数据冲突时的解决模式[ConflictResolution](arkts-apis-data-relationalstore-e.md#conflictresolution10)，返回[Result](arkts-apis-data-relationalstore-i.md#result23)，使用Promise异步回调。

由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。

如果单条数据超过此限制，在后续通过RdbStore的[query](arkts-apis-data-relationalstore-rdbstore.md#query)或[querySql](arkts-apis-data-relationalstore-rdbstore.md#querysql)接口获取ResultSet后，调用[getValue](arkts-apis-data-relationalstore-resultset.md#getvalue12)、[getString](arkts-apis-data-relationalstore-resultset.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

如需读取超过2MB的数据，请使用[queryByStep](arkts-apis-data-relationalstore-rdbstore.md#querybystep)接口。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

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
| Promise<[Result](arkts-apis-data-relationalstore-i.md#result23)> | Promise对象。返回受影响的数据集。 |

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

```ts
async function transUpdateWithReturningExample(trans: relationalStore.Transaction)
{
  const valueBucket1: relationalStore.ValuesBucket = { 'NAME': 'lisi', 'AGE': 21 };
  const valueBucket2: relationalStore.ValuesBucket = { 'NAME': 'lisi', 'AGE': 18 };
  let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
  predicates.equalTo('NAME', 'lisi');
  const config: relationalStore.ReturningConfig = { columns: ['NAME', 'AGE'] };
  try {
    trans.batchInsertWithReturningSync("EMPLOYEE", [valueBucket1, valueBucket2], config);
    valueBucket1['NAME'] = "zhangsan";
    valueBucket1['AGE'] = 18;
    let results = await trans.updateWithReturning(valueBucket1, predicates, config);
    console.info(`transUpdateWithReturningExample is successful, changed is ${results.changed}`);
    while(results.resultSet.goToNextRow()) {
      const row = results.resultSet.getRow();
      console.info(`transUpdateWithReturningExample, name is ${row['NAME']}, age is ${row['AGE']}`);
    }
  } catch (e) {
    console.error(`transUpdateWithReturningExample failed. code is ${e.code}, message is ${e.message}`);
  }
}
```

## updateWithReturningSync23+

updateWithReturningSync(values: ValuesBucket, predicates: RdbPredicates, config: ReturningConfig, conflict?: ConflictResolution): Result

根据RdbPredicates的指定实例对象更新数据库中的数据，可以通过conflict参数指定当发生数据冲突时的解决模式[ConflictResolution](arkts-apis-data-relationalstore-e.md#conflictresolution10)，返回[Result](arkts-apis-data-relationalstore-i.md#result23)。

由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。

如果单条数据超过此限制，在后续通过RdbStore的[query](arkts-apis-data-relationalstore-rdbstore.md#query)或[querySql](arkts-apis-data-relationalstore-rdbstore.md#querysql)接口获取ResultSet后，调用[getValue](arkts-apis-data-relationalstore-resultset.md#getvalue12)、[getString](arkts-apis-data-relationalstore-resultset.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

如需读取超过2MB的数据，请使用[queryByStep](arkts-apis-data-relationalstore-rdbstore.md#querybystep)接口。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

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
| [Result](arkts-apis-data-relationalstore-i.md#result23) | 返回受影响的数据集。 |

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

```ts
function transUpdateWithReturningSyncExample(trans: relationalStore.Transaction)
{
  const valueBucket1: relationalStore.ValuesBucket = { 'NAME': 'lisi', 'AGE': 21 };
  const valueBucket2: relationalStore.ValuesBucket = { 'NAME': 'lisi', 'AGE': 18 };
  let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
  predicates.equalTo('NAME', 'lisi');
  const config: relationalStore.ReturningConfig = { columns: ['NAME', 'AGE'] };
  try {
    trans.batchInsertWithReturningSync("EMPLOYEE", [valueBucket1, valueBucket2], config);
    valueBucket1['NAME'] = "zhangsan";
    valueBucket1['AGE'] = 18;
    let results = trans.updateWithReturningSync(valueBucket1, predicates, config);
    console.info(`transUpdateWithReturningSyncExample is successful, changed is ${results.changed}`);
    while(results.resultSet.goToNextRow()) {
      const row = results.resultSet.getRow();
      console.info(`transUpdateWithReturningSyncExample, name is ${row['NAME']}, age is ${row['AGE']}`);
    }
  } catch (e) {
    console.error(`transUpdateWithReturningSyncExample failed. code is ${e.code}, message is ${e.message}`);
  }
}
```

## delete14+

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

```ts
let predicates2 = new relationalStore.RdbPredicates('EMPLOYEE');
predicates2.equalTo('NAME', 'Lisa');

if (store != undefined) {
  try {
    const transaction = await store.createTransaction();
    try {
      const rows = await transaction.delete(predicates2);
      await transaction.commit();
      console.info(`Delete rows: ${rows}`);
    } catch (error) {
      const err = error as BusinessError;
      await transaction.rollback();
      console.error(`Delete failed, code is ${err.code},message is ${err.message}`);
    }
  } catch (error) {
    const err = error as BusinessError;
    console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
  }
}
```

## deleteSync14+

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

```ts
let predicates3 = new relationalStore.RdbPredicates('EMPLOYEE');
predicates3.equalTo('NAME', 'Lisa');
if (store != undefined) {
  try {
    const transaction = await store.createTransaction();
    try {
      let rows = transaction.deleteSync(predicates3);
      await transaction.commit();
      console.info(`Delete rows: ${rows}`);
    } catch (error) {
      const err = error as BusinessError;
      await transaction.rollback();
      console.error(`Delete failed, code is ${err.code},message is ${err.message}`);
    }
  } catch (error) {
    const err = error as BusinessError;
    console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
  }
}
```

## deleteWithReturning23+

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
| Promise<[Result](arkts-apis-data-relationalstore-i.md#result23)> | Promise对象。返回受影响的数据集。 |

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

```ts
async function transDeleteWithReturningExample(trans: relationalStore.Transaction)
{
  const valueBucket1: relationalStore.ValuesBucket = { 'NAME': 'lisi', 'AGE': 21 };
  const valueBucket2: relationalStore.ValuesBucket = { 'NAME': 'zhangsan', 'AGE': 18 };
  let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
  const config: relationalStore.ReturningConfig = { columns: ['NAME', 'AGE'] };
  try {
    trans.batchInsertWithReturningSync("EMPLOYEE", [valueBucket1, valueBucket2], config);
    let results = await trans.deleteWithReturning(predicates, config);
    console.info(`transDeleteWithReturningExample is successful, changed is ${results.changed}`);
    while(results.resultSet.goToNextRow()) {
      const row = results.resultSet.getRow();
      console.info(`transDeleteWithReturningExample, name is ${row['NAME']}, age is ${row['AGE']}`);
    }
  } catch (e) {
    console.error(`transDeleteWithReturningExample failed. code is ${e.code}, message is ${e.message}`);
  }
}
```

## deleteWithReturningSync23+

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
| [Result](arkts-apis-data-relationalstore-i.md#result23) | 返回受影响的数据集。 |

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

```ts
function transDeleteWithReturningSyncExample(trans: relationalStore.Transaction)
{
  const valueBucket1: relationalStore.ValuesBucket = { 'NAME': 'lisi', 'AGE': 21 };
  const valueBucket2: relationalStore.ValuesBucket = { 'NAME': 'zhangsan', 'AGE': 18 };
  let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
  const config: relationalStore.ReturningConfig = { columns: ['NAME', 'AGE'] };
  try {
    trans.batchInsertWithReturningSync("EMPLOYEE", [valueBucket1, valueBucket2], config);
    let results = trans.deleteWithReturningSync(predicates, config);
    console.info(`transDeleteWithReturningSyncExample is successful, changed is ${results.changed}`);
    while(results.resultSet.goToNextRow()) {
      const row = results.resultSet.getRow();
      console.info(`transDeleteWithReturningSyncExample, name is ${row['NAME']}, age is ${row['AGE']}`);
    }
  } catch (e) {
    console.error(`transDeleteWithReturningSyncExample failed. code is ${e.code}, message is ${e.message}`);
  }
}
```

## query14+

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
| Promise<[ResultSet](arkts-apis-data-relationalstore-resultset.md)> | Promise对象。返回ResultSet对象。 |

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

```ts
let predicates4 = new relationalStore.RdbPredicates('EMPLOYEE');
predicates4.equalTo('NAME', 'Rose');

if (store != undefined) {
  try {
    const transaction = await store.createTransaction();
    try {
      const resultSet = await transaction.query(predicates4, ['ID', 'NAME', 'AGE', 'SALARY', 'CODES']);
      console.info(`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}`);
      // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
      while (resultSet.goToNextRow()) {
        const id = resultSet.getLong(resultSet.getColumnIndex('ID'));
        const name = resultSet.getString(resultSet.getColumnIndex('NAME'));
        const age = resultSet.getLong(resultSet.getColumnIndex('AGE'));
        const salary = resultSet.getDouble(resultSet.getColumnIndex('SALARY'));
        console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
      }
      // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
      resultSet.close();
      await transaction.commit();
    } catch (error) {
      const err = error as BusinessError;
      await transaction.rollback();
      console.error(`Query failed, code is ${err.code},message is ${err.message}`);
    }
  } catch (error) {
    const err = error as BusinessError;
    console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
  }
}
```

## querySync14+

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
| [ResultSet](arkts-apis-data-relationalstore-resultset.md) | 返回ResultSet对象。 |

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

```ts
let predicates5 = new relationalStore.RdbPredicates('EMPLOYEE');
predicates5.equalTo('NAME', 'Rose');

if (store != undefined) {
  try {
    const transaction = await store.createTransaction();
    try {
      let resultSet = transaction.querySync(predicates5, ['ID', 'NAME', 'AGE', 'SALARY', 'CODES']);
      console.info(`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}`);
      // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
      while (resultSet.goToNextRow()) {
        const id = resultSet.getLong(resultSet.getColumnIndex('ID'));
        const name = resultSet.getString(resultSet.getColumnIndex('NAME'));
        const age = resultSet.getLong(resultSet.getColumnIndex('AGE'));
        const salary = resultSet.getDouble(resultSet.getColumnIndex('SALARY'));
        console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
      }
      // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
      resultSet.close();
      await transaction.commit();
    } catch (error) {
      const err = error as BusinessError;
      await transaction.rollback();
      console.error(`Query failed, code is ${err.code},message is ${err.message}`);
    }
  } catch (error) {
    const err = error as BusinessError;
    console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
  }
}
```

## querySql14+

querySql(sql: string, args?: Array<ValueType>): Promise<ResultSet>

根据指定SQL语句查询数据库中的数据，SQL语句中的各种表达式和操作符之间的关系操作符号不超过1000个，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sql | string | 是 | 指定要执行的SQL语句，不能为空字符串。 |
| args | Array<[ValueType](arkts-apis-data-relationalstore-t.md#valuetype)> | 否 | SQL语句中参数的值。该值与sql参数语句中的占位符相对应。当sql参数语句完整时，该参数不填。默认值为空。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[ResultSet](arkts-apis-data-relationalstore-resultset.md)> | Promise对象。返回ResultSet对象。 |

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

```ts
if (store != undefined) {
  try {
    const transaction = await store.createTransaction();
    try {
      const resultSet = await transaction.querySql("SELECT * FROM EMPLOYEE CROSS JOIN BOOK WHERE BOOK.NAME = 'sanguo'");
      console.info(`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}`);
      // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
      while (resultSet.goToNextRow()) {
        const id = resultSet.getLong(resultSet.getColumnIndex('ID'));
        const name = resultSet.getString(resultSet.getColumnIndex('NAME'));
        const age = resultSet.getLong(resultSet.getColumnIndex('AGE'));
        const salary = resultSet.getDouble(resultSet.getColumnIndex('SALARY'));
        console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
      }
      // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
      resultSet.close();
      await transaction.commit();
    } catch (error) {
      const err = error as BusinessError;
      await transaction.rollback();
      console.error(`Query failed, code is ${err.code},message is ${err.message}`);
    }
  } catch (error) {
    const err = error as BusinessError;
    console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
  }
}
```

## querySqlSync14+

querySqlSync(sql: string, args?: Array<ValueType>): ResultSet

根据指定SQL语句查询数据库中的数据，SQL语句中的各种表达式和操作符之间的关系操作符号不超过1000个。对query同步接口获得的resultSet进行操作时，若逻辑复杂且循环次数过多，可能造成freeze问题，建议将此步骤放到[taskpool](js-apis-taskpool.md)线程中执行。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sql | string | 是 | 指定要执行的SQL语句，不能为空字符串。 |
| args | Array<[ValueType](arkts-apis-data-relationalstore-t.md#valuetype)> | 否 | SQL语句中参数的值。该值与sql参数语句中的占位符相对应。当sql参数语句完整时，该参数不填。默认值为空。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [ResultSet](arkts-apis-data-relationalstore-resultset.md) | 返回ResultSet对象。 |

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

```ts
if (store != undefined) {
  try {
    const transaction = await store.createTransaction();
    try {
      let resultSet = transaction.querySqlSync("SELECT * FROM EMPLOYEE CROSS JOIN BOOK WHERE BOOK.NAME = 'sanguo'");
      console.info(`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}`);
      // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
      while (resultSet.goToNextRow()) {
        const id = resultSet.getLong(resultSet.getColumnIndex('ID'));
        const name = resultSet.getString(resultSet.getColumnIndex('NAME'));
        const age = resultSet.getLong(resultSet.getColumnIndex('AGE'));
        const salary = resultSet.getDouble(resultSet.getColumnIndex('SALARY'));
        console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
      }
      // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
      resultSet.close();
      await transaction.commit();
    } catch (error) {
      const err = error as BusinessError;
      await transaction.rollback();
      console.error(`Query failed, code is ${err.code},message is ${err.message}`);
    }
  } catch (error) {
    const err = error as BusinessError;
    console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
  }
}
```

## queryWithoutRowCount23+

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
| Promise<[LiteResultSet](arkts-apis-data-relationalstore-literesultset.md)> | 返回LiteResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800014 | The target instance is already closed. |

**示例：**

```ts
async function queryWithoutRowCountExample(store : relationalStore.RdbStore) {
  let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
  predicates.equalTo("NAME", "Rose");
  if (store != undefined) {
    try {
      const transaction = await store.createTransaction();
      let resultSet: relationalStore.LiteResultSet | undefined;
      try {
        resultSet = await transaction.queryWithoutRowCount(predicates, ["ID", "NAME", "AGE", "SALARY", "CODES"]);
        if (resultSet != undefined) {
          // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
          while (resultSet.goToNextRow()) {
            const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
            const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
            const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
            const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
            console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
          }
          // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
          resultSet.close();
        }
        await transaction.commit();
      } catch (err) {
        console.error(`Query failed, code is ${err.code}, message is ${err.message}`);
        // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
        if (resultSet != undefined) {
          resultSet.close();
        }
        await transaction.rollback();
      }
    } catch (err) {
      console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
    }
  }
}
```

## queryWithoutRowCountSync23+

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
| [LiteResultSet](arkts-apis-data-relationalstore-literesultset.md) | 返回LiteResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800014 | The target instance is already closed. |

**示例：**

```ts
async function queryWithoutRowCountSyncExample(store : relationalStore.RdbStore) {
  let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
  predicates.equalTo("NAME", "Rose");
  if (store != undefined) {
    try {
      const transaction = await store.createTransaction();
      let resultSet: relationalStore.LiteResultSet | undefined;
      try {
        resultSet = transaction.queryWithoutRowCountSync(predicates, ["ID", "NAME", "AGE", "SALARY", "CODES"]);
        if (resultSet != undefined) {
          // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
          while (resultSet.goToNextRow()) {
            const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
            const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
            const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
            const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
            console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
          }
          // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
          resultSet.close();
        }
        await transaction.commit();
      } catch (err) {
        console.error(`Query failed, code is ${err.code}, message is ${err.message}`);
        // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
        if (resultSet != undefined) {
          resultSet.close();
        }
        await transaction.rollback();
      }
    } catch (err) {
      console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
    }
  }
}
```

## querySqlWithoutRowCount23+

querySqlWithoutRowCount(sql: string, bindArgs?: Array<ValueType>): Promise<LiteResultSet>

根据指定条件查询数据库中的数据，查询时不计算行数。使用Promise异步回调。性能优于[querySql](arkts-apis-data-relationalstore-transaction.md#querysql14)接口。SQL语句中的各种表达式和操作符之间的关系操作符号不超过1000个。

**模型约束：** 此接口仅在Stage模型下可用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sql | string | 是 | 指定要执行的SQL语句，不能为空字符串。 |
| bindArgs | Array<[ValueType](arkts-apis-data-relationalstore-t.md#valuetype)> | 否 | SQL语句中参数的值。该值与sql参数语句中的占位符相对应。当sql参数语句完整时，该参数不填。默认值为空。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[LiteResultSet](arkts-apis-data-relationalstore-literesultset.md)> | Promise对象。返回LiteResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1.Parameter is out of valid range. |
| 14800014 | The target instance is already closed. |

**示例：**

```ts
async function querySqlWithoutRowCountExample(store : relationalStore.RdbStore) {
  if (store != undefined) {
    try {
    const transaction = await store.createTransaction();
    let resultSet: relationalStore.LiteResultSet | undefined;
      try {
        resultSet = await transaction.querySqlWithoutRowCount('select * from EMPLOYEE where name = ?', ["Rose"]);
        if (resultSet != undefined) {
          // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
          while (resultSet.goToNextRow()) {
            const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
            const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
            const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
            const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
            console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
          }
          // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
          resultSet.close();
        }
        await transaction.commit();
      } catch (err) {
        console.error(`Query failed, code is ${err.code}, message is ${err.message}`);
        // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
        if (resultSet != undefined) {
          resultSet.close();
        }
        await transaction.rollback();
      }
    } catch (err) {
    console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
    }
  }
}
```

## querySqlWithoutRowCountSync23+

querySqlWithoutRowCountSync(sql: string, bindArgs?: Array<ValueType>):LiteResultSet

根据指定SQL语句查询数据库中的数据，查询时不计算行数。SQL语句中的各种表达式和操作符之间的关系操作符号不超过1000个。对querySqlWithoutRowCountSync同步接口获得的LiteResultSet进行操作时，若逻辑复杂且循环次数过多，可能造成freeze问题，建议将此步骤放到[taskpool](js-apis-taskpool.md)线程中执行。

**模型约束：** 此接口仅在Stage模型下可用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sql | string | 是 | 指定要执行的SQL语句，不能为空字符串。 |
| bindArgs | Array<[ValueType](arkts-apis-data-relationalstore-t.md#valuetype)> | 否 | SQL语句中参数的值。该值与sql参数语句中的占位符相对应。当sql参数语句完整时，该参数不填。默认值为空。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [LiteResultSet](arkts-apis-data-relationalstore-literesultset.md) | 返回LiteResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1.Parameter is out of valid range. |
| 14800014 | The target instance is already closed. |

**示例：**

```ts
async function querySqlWithoutRowCountSyncExample(store : relationalStore.RdbStore) {
  if (store != undefined) {
    try {
    const transaction = await store.createTransaction();
    let resultSet: relationalStore.LiteResultSet | undefined;
      try {
        resultSet = transaction.querySqlWithoutRowCountSync('select * from EMPLOYEE where name = ?', ["Rose"]);
        if (resultSet != undefined) {
          // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
          while (resultSet.goToNextRow()) {
            const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
            const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
            const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
            const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
            console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
          }
          // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
          resultSet.close();
        }
        await transaction.commit();
      } catch (err) {
        console.error(`Query failed, code is ${err.code}, message is ${err.message}`);
        // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
        if (resultSet != undefined) {
          resultSet.close();
        }
        await transaction.rollback();
      }
    } catch (err) {
    console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
    }
  }
}
```

## execute14+

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
| sql | string | 是 | 指定要执行的SQL语句，不能为空字符串。 |
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

```ts
if (store != undefined) {
  try {
    const transaction = await store.createTransaction();
    try {
      // 删除表中所有数据
      const SQL_DELETE_TABLE = 'DELETE FROM EMPLOYEE';
      const data = await transaction.execute(SQL_DELETE_TABLE);
      await transaction.commit();
      console.info(`delete result: ${data}`);
    } catch (error) {
      const err = error as BusinessError;
      await transaction.rollback();
      console.error(`delete failed, code is ${err.code}, message is ${err.message}`);
    }
  } catch (error) {
    const err = error as BusinessError;
    console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
  }
}
```

## executeSync14+

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
| sql | string | 是 | 指定要执行的SQL语句，不能为空字符串。 |
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

```ts
// 删除表中所有数据
if (store != undefined) {
  try {
    const transaction = await store.createTransaction();
    try {
      const SQL_DELETE_TABLE = 'DELETE FROM EMPLOYEE';
      let data = transaction.executeSync(SQL_DELETE_TABLE);
      await transaction.commit();
      console.info(`delete result: ${data}`);
    } catch (error) {
      const err = error as BusinessError;
      await transaction.rollback();
      console.error(`delete failed, code is ${err.code}, message is ${err.message}`);
    }
  } catch (error) {
    const err = error as BusinessError;
    console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
  }
}
```
