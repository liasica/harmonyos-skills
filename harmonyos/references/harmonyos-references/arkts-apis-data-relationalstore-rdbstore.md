---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-rdbstore
title: Interface (RdbStore)
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > ArkTS API > @ohos.data.relationalStore (关系型数据库) > Interface (RdbStore)
category: harmonyos-references
scraped_at: 2026-04-29T13:49:30+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:ee2ee3db540782f5cebff0638c4567a3ef392ad01fcfda02037a3c792018f466
---

提供管理关系数据库（RDB）方法的接口。

在使用以下API前，请先通过[getRdbStore](arkts-apis-data-relationalstore-f.md#relationalstoregetrdbstore-1)方法获取RdbStore实例，并使用该实例调用对应接口方法。

在此基础上，建议优先使用[execute](arkts-apis-data-relationalstore-rdbstore.md#execute12)方法完成数据库表结构和初始数据的初始化，以确保相关接口调用的前置条件已满足。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { relationalStore } from '@kit.ArkData';
```

## 属性

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| version10+ | number | 否 | 否 | 设置和获取数据库版本，值为大于0的正整数。  读取和设置version属性会占用数据库连接，避免对该属性进行频繁操作。  使用临时变量保存读取到的version值，在数据库变更完成后将其赋值给RdbStore实例的version属性。数据库升级时变更version属性的场景，请参考[开发指南示例代码](../harmonyos-guides/data-persistence-by-rdb-store.md#开发步骤)。 |
| rebuilt12+ | [RebuildType](arkts-apis-data-relationalstore-e.md#rebuildtype12) | 是 | 否 | 用于获取数据库是否进行过重建或修复。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |

**示例：**

示例代码中this.context定义见Stage模型的应用[Context](js-apis-inner-application-context.md)。

```
1. // 设置数据库版本
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. let store: relationalStore.RdbStore | undefined = undefined;

8. class EntryAbility extends UIAbility {
9. onWindowStageCreate(windowStage: window.WindowStage) {
10. const STORE_CONFIG: relationalStore.StoreConfig = {
11. name: "RdbTest.db",
12. securityLevel: relationalStore.SecurityLevel.S3
13. };
14. const SQL_CREATE_TABLE = 'CREATE TABLE IF NOT EXISTS EMPLOYEE (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, AGE INTEGER, SALARY REAL, CODES BLOB, IDENTITY UNLIMITED INT, ASSETDATA ASSET, ASSETSDATA ASSETS, FLOATARRAY floatvector(128))';
15. relationalStore.getRdbStore(this.context, STORE_CONFIG).then(async (rdbStore: relationalStore.RdbStore) => {
16. store = rdbStore;
17. await (store as relationalStore.RdbStore).executeSql(SQL_CREATE_TABLE);
18. console.info('Get RdbStore successfully.');

20. // 设置数据库版本
21. if (store != undefined) {
22. (store as relationalStore.RdbStore).version = 3;
23. // 获取数据库版本
24. console.info(`RdbStore version is ${store.version}`);
25. // 获取数据库是否重建
26. console.info(`RdbStore rebuilt is ${store.rebuilt}`);
27. }
28. }).catch((err: BusinessError) => {
29. console.error(`Get RdbStore failed, code is ${err.code}, message is ${err.message}`);
30. });
31. }
32. }
```

## insert

PhonePC/2in1TabletTVWearable

insert(table: string, values: ValuesBucket, callback: AsyncCallback<number>):void

向目标表中插入一行数据，使用callback异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的[query](arkts-apis-data-relationalstore-rdbstore.md#query)或[querySql](arkts-apis-data-relationalstore-rdbstore.md#querysql)接口获取ResultSet后，调用[getValue](arkts-apis-data-relationalstore-resultset.md#getvalue12)、[getString](arkts-apis-data-relationalstore-resultset.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 指定的目标表名。 |
| values | [ValuesBucket](arkts-apis-data-relationalstore-t.md#valuesbucket) | 是 | 表示要插入到表中的数据行。 |
| callback | AsyncCallback<number> | 是 | 指定callback回调函数。如果操作成功，返回行ID；否则返回-1。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. let value1 = "Lisa";
2. let value2 = 18;
3. let value3 = 100.5;
4. let value4 = new Uint8Array([1, 2, 3, 4, 5]);

6. // 以下三种方式可用
7. const valueBucket1: relationalStore.ValuesBucket = {
8. 'NAME': value1,
9. 'AGE': value2,
10. 'SALARY': value3,
11. 'CODES': value4
12. };
13. const valueBucket2: relationalStore.ValuesBucket = {
14. NAME: value1,
15. AGE: value2,
16. SALARY: value3,
17. CODES: value4
18. };
19. const valueBucket3: relationalStore.ValuesBucket = {
20. "NAME": value1,
21. "AGE": value2,
22. "SALARY": value3,
23. "CODES": value4
24. };

26. if (store != undefined) {
27. (store as relationalStore.RdbStore).insert("EMPLOYEE", valueBucket1, (err: BusinessError, rowId: number) => {
28. if (err) {
29. console.error(`Insert is failed, code is ${err.code},message is ${err.message}`);
30. return;
31. }
32. console.info(`Insert is successful, rowId = ${rowId}`);
33. });
34. }
```

## insert10+

PhonePC/2in1TabletTVWearable

insert(table: string, values: ValuesBucket, conflict: ConflictResolution, callback: AsyncCallback<number>):void

向目标表中插入一行数据，可以通过conflict参数指定冲突解决模式[ConflictResolution](arkts-apis-data-relationalstore-e.md#conflictresolution10)，使用callback异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的[query](arkts-apis-data-relationalstore-rdbstore.md#query)或[querySql](arkts-apis-data-relationalstore-rdbstore.md#querysql)接口获取ResultSet后，调用[getValue](arkts-apis-data-relationalstore-resultset.md#getvalue12)、[getString](arkts-apis-data-relationalstore-resultset.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 指定的目标表名。 |
| values | [ValuesBucket](arkts-apis-data-relationalstore-t.md#valuesbucket) | 是 | 表示要插入到表中的数据行。 |
| conflict | [ConflictResolution](arkts-apis-data-relationalstore-e.md#conflictresolution10) | 是 | 指定冲突解决模式。 |
| callback | AsyncCallback<number> | 是 | 指定callback回调函数。如果操作成功，返回行ID；否则返回-1。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. let value1 = "Lisa";
2. let value2 = 18;
3. let value3 = 100.5;
4. let value4 = new Uint8Array([1, 2, 3, 4, 5]);

6. // 以下三种方式可用
7. const valueBucket1: relationalStore.ValuesBucket = {
8. 'NAME': value1,
9. 'AGE': value2,
10. 'SALARY': value3,
11. 'CODES': value4
12. };
13. const valueBucket2: relationalStore.ValuesBucket = {
14. NAME: value1,
15. AGE: value2,
16. SALARY: value3,
17. CODES: value4
18. };
19. const valueBucket3: relationalStore.ValuesBucket = {
20. "NAME": value1,
21. "AGE": value2,
22. "SALARY": value3,
23. "CODES": value4
24. };

26. if (store != undefined) {
27. (store as relationalStore.RdbStore).insert("EMPLOYEE", valueBucket1, relationalStore.ConflictResolution.ON_CONFLICT_REPLACE,
28. (err: BusinessError, rowId: number) => {
29. if (err) {
30. console.error(`Insert is failed, code is ${err.code},message is ${err.message}`);
31. return;
32. }
33. console.info(`Insert is successful, rowId = ${rowId}`);
34. });
35. }
```

## insert

PhonePC/2in1TabletTVWearable

insert(table: string, values: ValuesBucket):Promise<number>

向目标表中插入一行数据，使用Promise异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的[query](arkts-apis-data-relationalstore-rdbstore.md#query)或[querySql](arkts-apis-data-relationalstore-rdbstore.md#querysql)接口获取ResultSet后，调用[getValue](arkts-apis-data-relationalstore-resultset.md#getvalue12)、[getString](arkts-apis-data-relationalstore-resultset.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 指定的目标表名。 |
| values | [ValuesBucket](arkts-apis-data-relationalstore-t.md#valuesbucket) | 是 | 表示要插入到表中的数据行。 |

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
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let value1 = "Lisa";
4. let value2 = 18;
5. let value3 = 100.5;
6. let value4 = new Uint8Array([1, 2, 3, 4, 5]);

8. // 以下三种方式可用
9. const valueBucket1: relationalStore.ValuesBucket = {
10. 'NAME': value1,
11. 'AGE': value2,
12. 'SALARY': value3,
13. 'CODES': value4
14. };
15. const valueBucket2: relationalStore.ValuesBucket = {
16. NAME: value1,
17. AGE: value2,
18. SALARY: value3,
19. CODES: value4
20. };
21. const valueBucket3: relationalStore.ValuesBucket = {
22. "NAME": value1,
23. "AGE": value2,
24. "SALARY": value3,
25. "CODES": value4
26. };

28. if (store != undefined) {
29. (store as relationalStore.RdbStore).insert("EMPLOYEE", valueBucket1).then((rowId: number) => {
30. console.info(`Insert is successful, rowId = ${rowId}`);
31. }).catch((err: BusinessError) => {
32. console.error(`Insert is failed, code is ${err.code},message is ${err.message}`);
33. });
34. }
```

## insert10+

PhonePC/2in1TabletTVWearable

insert(table: string, values: ValuesBucket, conflict: ConflictResolution):Promise<number>

向目标表中插入一行数据，可以通过conflict参数指定冲突解决模式[ConflictResolution](arkts-apis-data-relationalstore-e.md#conflictresolution10)，使用Promise异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的[query](arkts-apis-data-relationalstore-rdbstore.md#query)或[querySql](arkts-apis-data-relationalstore-rdbstore.md#querysql)接口获取ResultSet后，调用[getValue](arkts-apis-data-relationalstore-resultset.md#getvalue12)、[getString](arkts-apis-data-relationalstore-resultset.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 指定的目标表名。 |
| values | [ValuesBucket](arkts-apis-data-relationalstore-t.md#valuesbucket) | 是 | 表示要插入到表中的数据行。 |
| conflict | [ConflictResolution](arkts-apis-data-relationalstore-e.md#conflictresolution10) | 是 | 指定冲突解决模式。 |

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
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let value1 = "Lisa";
4. let value2 = 18;
5. let value3 = 100.5;
6. let value4 = new Uint8Array([1, 2, 3, 4, 5]);

8. // 以下三种方式可用
9. const valueBucket1: relationalStore.ValuesBucket = {
10. 'NAME': value1,
11. 'AGE': value2,
12. 'SALARY': value3,
13. 'CODES': value4
14. };
15. const valueBucket2: relationalStore.ValuesBucket = {
16. NAME: value1,
17. AGE: value2,
18. SALARY: value3,
19. CODES: value4
20. };
21. const valueBucket3: relationalStore.ValuesBucket = {
22. "NAME": value1,
23. "AGE": value2,
24. "SALARY": value3,
25. "CODES": value4
26. };

28. if (store != undefined) {
29. (store as relationalStore.RdbStore).insert("EMPLOYEE", valueBucket1, relationalStore.ConflictResolution.ON_CONFLICT_REPLACE).then((rowId: number) => {
30. console.info(`Insert is successful, rowId = ${rowId}`);
31. }).catch((err: BusinessError) => {
32. console.error(`Insert is failed, code is ${err.code},message is ${err.message}`);
33. });
34. }
```

## insertSync12+

PhonePC/2in1TabletTVWearable

insertSync(table: string, values: ValuesBucket, conflict?: ConflictResolution):number

向目标表中插入一行数据。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的[query](arkts-apis-data-relationalstore-rdbstore.md#query)或[querySql](arkts-apis-data-relationalstore-rdbstore.md#querysql)接口获取ResultSet后，调用[getValue](arkts-apis-data-relationalstore-resultset.md#getvalue12)、[getString](arkts-apis-data-relationalstore-resultset.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

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
| number | 如果操作成功，返回行ID；否则返回-1。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. let value1 = "Lisa";
2. let value2 = 18;
3. let value3 = 100.5;
4. let value4 = new Uint8Array([1, 2, 3, 4, 5]);

6. // 以下三种方式可用
7. const valueBucket1: relationalStore.ValuesBucket = {
8. 'NAME': value1,
9. 'AGE': value2,
10. 'SALARY': value3,
11. 'CODES': value4
12. };
13. const valueBucket2: relationalStore.ValuesBucket = {
14. NAME: value1,
15. AGE: value2,
16. SALARY: value3,
17. CODES: value4
18. };
19. const valueBucket3: relationalStore.ValuesBucket = {
20. "NAME": value1,
21. "AGE": value2,
22. "SALARY": value3,
23. "CODES": value4
24. };

26. if (store != undefined) {
27. try {
28. let rowId: number = (store as relationalStore.RdbStore).insertSync("EMPLOYEE", valueBucket1, relationalStore.ConflictResolution.ON_CONFLICT_REPLACE);
29. console.info(`Insert is successful, rowId = ${rowId}`);
30. } catch (err) {
31. console.error(`Insert is failed, code is ${err.code},message is ${err.message}`);
32. }
33. }
```

## insertSync12+

PhonePC/2in1TabletTVWearable

insertSync(table: string, values: sendableRelationalStore.ValuesBucket, conflict?: ConflictResolution):number

传入Sendable数据，向目标表中插入一行数据。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的[query](arkts-apis-data-relationalstore-rdbstore.md#query)或[querySql](arkts-apis-data-relationalstore-rdbstore.md#querysql)接口获取ResultSet后，调用[getValue](arkts-apis-data-relationalstore-resultset.md#getvalue12)、[getString](arkts-apis-data-relationalstore-resultset.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 指定的目标表名。 |
| values | [sendableRelationalStore.ValuesBucket](js-apis-data-sendablerelationalstore.md#valuesbucket) | 是 | 表示要插入到表中的可跨线程传递数据。 |
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
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. import { sendableRelationalStore } from '@kit.ArkData';

3. const valuesBucket: relationalStore.ValuesBucket = {
4. "NAME": 'hangman',
5. "AGE": 18,
6. "SALARY": 100.5,
7. "CODES": new Uint8Array([1, 2, 3])
8. };
9. const sendableValuesBucket = sendableRelationalStore.toSendableValuesBucket(valuesBucket);

11. if (store != undefined) {
12. try {
13. let rowId: number = (store as relationalStore.RdbStore).insertSync("EMPLOYEE", sendableValuesBucket, relationalStore.ConflictResolution.ON_CONFLICT_REPLACE);
14. console.info(`Insert is successful, rowId = ${rowId}`);
15. } catch (err) {
16. console.error(`Insert is failed, code is ${err.code},message is ${err.message}`);
17. }
18. }
```

## batchInsert

PhonePC/2in1TabletTVWearable

batchInsert(table: string, values: Array<ValuesBucket>, callback: AsyncCallback<number>):void

向目标表中插入一组数据，使用callback异步回调。

接口报错，表示插入数据失败；接口没有报错但返回值为-1时，也表示插入数据失败。

按每批32766个参数，分批以[ConflictResolution.ON\_CONFLICT\_REPLACE](arkts-apis-data-relationalstore-e.md#conflictresolution10)策略写入，参数数量计算方式为插入数据条数乘以插入数据的所有字段的并集大小，中途失败则立即返回。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

从API version 20开始，支持向量数据库（在[StoreConfig](arkts-apis-data-relationalstore-i.md#storeconfig)中配置vector为true）。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 指定的目标表名。 |
| values | Array<[ValuesBucket](arkts-apis-data-relationalstore-t.md#valuesbucket)> | 是 | 表示要插入到表中的一组数据。 |
| callback | AsyncCallback<number> | 是 | 指定callback回调函数。如果操作成功，返回插入的数据个数，否则返回-1。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. let value1 = "Lisa";
2. let value2 = 18;
3. let value3 = 100.5;
4. let value4 = new Uint8Array([1, 2, 3, 4, 5]);
5. let value5 = "Jack";
6. let value6 = 19;
7. let value7 = 101.5;
8. let value8 = new Uint8Array([6, 7, 8, 9, 10]);
9. let value9 = "Tom";
10. let value10 = 20;
11. let value11 = 102.5;
12. let value12 = new Uint8Array([11, 12, 13, 14, 15]);

14. const valueBucket1: relationalStore.ValuesBucket = {
15. 'NAME': value1,
16. 'AGE': value2,
17. 'SALARY': value3,
18. 'CODES': value4
19. };
20. const valueBucket2: relationalStore.ValuesBucket = {
21. 'NAME': value5,
22. 'AGE': value6,
23. 'SALARY': value7,
24. 'CODES': value8
25. };
26. const valueBucket3: relationalStore.ValuesBucket = {
27. 'NAME': value9,
28. 'AGE': value10,
29. 'SALARY': value11,
30. 'CODES': value12
31. };

33. let valueBuckets = new Array(valueBucket1, valueBucket2, valueBucket3);
34. if (store != undefined) {
35. (store as relationalStore.RdbStore).batchInsert("EMPLOYEE", valueBuckets, (err, insertNum) => {
36. if (err || insertNum == -1) {
37. console.error(`batchInsert is failed, code is ${err.code},message is ${err.message}`);
38. return;
39. }
40. console.info(`batchInsert is successful, the number of values that were inserted = ${insertNum}`);
41. })
42. }
```

## batchInsert

PhonePC/2in1TabletTVWearable

batchInsert(table: string, values: Array<ValuesBucket>):Promise<number>

向目标表中插入一组数据，使用Promise异步回调。

接口报错，表示插入数据失败；接口没有报错但返回值为-1时，也表示插入数据失败。

按每批32766个参数，分批以[ConflictResolution.ON\_CONFLICT\_REPLACE](arkts-apis-data-relationalstore-e.md#conflictresolution10)策略写入，参数数量计算方式为插入数据条数乘以插入数据的所有字段的并集大小，中途失败则立即返回。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

从API version 20开始，该接口支持向量数据库（在[StoreConfig](arkts-apis-data-relationalstore-i.md#storeconfig)中配置vector为true）使用。

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
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

关系型数据库：

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let value1 = "Lisa";
4. let value2 = 18;
5. let value3 = 100.5;
6. let value4 = new Uint8Array([1, 2, 3, 4, 5]);
7. let value5 = "Jack";
8. let value6 = 19;
9. let value7 = 101.5;
10. let value8 = new Uint8Array([6, 7, 8, 9, 10]);
11. let value9 = "Tom";
12. let value10 = 20;
13. let value11 = 102.5;
14. let value12 = new Uint8Array([11, 12, 13, 14, 15]);

16. const valueBucket1: relationalStore.ValuesBucket = {
17. 'NAME': value1,
18. 'AGE': value2,
19. 'SALARY': value3,
20. 'CODES': value4
21. };
22. const valueBucket2: relationalStore.ValuesBucket = {
23. 'NAME': value5,
24. 'AGE': value6,
25. 'SALARY': value7,
26. 'CODES': value8
27. };
28. const valueBucket3: relationalStore.ValuesBucket = {
29. 'NAME': value9,
30. 'AGE': value10,
31. 'SALARY': value11,
32. 'CODES': value12
33. };

35. let valueBuckets = new Array(valueBucket1, valueBucket2, valueBucket3);
36. if (store != undefined) {
37. (store as relationalStore.RdbStore).batchInsert("EMPLOYEE", valueBuckets).then((insertNum: number) => {
38. if (insertNum == -1) {
39. console.error(`batchInsert is failed`);
40. return;
41. }
42. console.info(`batchInsert is successful, the number of values that were inserted = ${insertNum}`);
43. }).catch((err: BusinessError) => {
44. console.error(`batchInsert is failed, code is ${err.code},message is ${err.message}`);
45. })
46. }
```

向量数据库：

```
1. let createSql = "CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY AUTOINCREMENT, data1 floatvector(2));";
2. await store!.execute(createSql, 0, undefined);  // 创建关系表，第二个参数0表示不开启显示事务，第三个参数undefined表示sql未使用绑定参数化
3. let floatVector = Float32Array.from([1.2, 2.3]);
4. let valueBucketArray = new Array<relationalStore.ValuesBucket>();
5. for (let i = 0; i < 100; i++) { // 构造一个BucketArray用于写入
6. const row : relationalStore.ValuesBucket = {
7. "id" : i,
8. "data1" : floatVector,
9. }
10. valueBucketArray.push(row);
11. }
12. await store!.batchInsert("test", valueBucketArray); // 执行批量写入
```

## batchInsertSync12+

PhonePC/2in1TabletTVWearable

batchInsertSync(table: string, values: Array<ValuesBucket>):number

向目标表中插入一组数据。

接口报错，表示插入数据失败；接口没有报错但返回值为-1时，也表示插入数据失败。

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
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. let value1 = "Lisa";
2. let value2 = 18;
3. let value3 = 100.5;
4. let value4 = new Uint8Array([1, 2, 3, 4, 5]);
5. let value5 = "Jack";
6. let value6 = 19;
7. let value7 = 101.5;
8. let value8 = new Uint8Array([6, 7, 8, 9, 10]);
9. let value9 = "Tom";
10. let value10 = 20;
11. let value11 = 102.5;
12. let value12 = new Uint8Array([11, 12, 13, 14, 15]);

14. const valueBucket1: relationalStore.ValuesBucket = {
15. 'NAME': value1,
16. 'AGE': value2,
17. 'SALARY': value3,
18. 'CODES': value4
19. };
20. const valueBucket2: relationalStore.ValuesBucket = {
21. 'NAME': value5,
22. 'AGE': value6,
23. 'SALARY': value7,
24. 'CODES': value8
25. };
26. const valueBucket3: relationalStore.ValuesBucket = {
27. 'NAME': value9,
28. 'AGE': value10,
29. 'SALARY': value11,
30. 'CODES': value12
31. };

33. let valueBuckets = new Array(valueBucket1, valueBucket2, valueBucket3);
34. if (store != undefined) {
35. try {
36. let insertNum: number = (store as relationalStore.RdbStore).batchInsertSync("EMPLOYEE", valueBuckets);
37. if (insertNum == -1) {
38. console.error(`batchInsertSync is failed`);
39. return;
40. }
41. console.info(`batchInsert is successful, the number of values that were inserted = ${insertNum}`);
42. } catch (err) {
43. console.error(`batchInsert is failed, code is ${err.code},message is ${err.message}`);
44. }
45. }
```

## batchInsertWithConflictResolution18+

PhonePC/2in1TabletTVWearable

batchInsertWithConflictResolution(table: string, values: Array<ValuesBucket>, conflict: ConflictResolution): Promise<number>

向目标表中插入一组数据，可以通过conflict参数指定冲突解决模式[ConflictResolution](arkts-apis-data-relationalstore-e.md#conflictresolution10)。使用Promise异步回调。

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
| conflict | [ConflictResolution](arkts-apis-data-relationalstore-e.md#conflictresolution10) | 是 | 指定冲突解决模式。 |

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
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let value1 = "Lisa";
4. let value2 = 18;
5. let value3 = 100.5;
6. let value4 = new Uint8Array([1, 2, 3, 4, 5]);
7. let value5 = "Jack";
8. let value6 = 19;
9. let value7 = 101.5;
10. let value8 = new Uint8Array([6, 7, 8, 9, 10]);
11. let value9 = "Tom";
12. let value10 = 20;
13. let value11 = 102.5;
14. let value12 = new Uint8Array([11, 12, 13, 14, 15]);

16. const valueBucket1: relationalStore.ValuesBucket = {
17. 'NAME': value1,
18. 'AGE': value2,
19. 'SALARY': value3,
20. 'CODES': value4
21. };
22. const valueBucket2: relationalStore.ValuesBucket = {
23. 'NAME': value5,
24. 'AGE': value6,
25. 'SALARY': value7,
26. 'CODES': value8
27. };
28. const valueBucket3: relationalStore.ValuesBucket = {
29. 'NAME': value9,
30. 'AGE': value10,
31. 'SALARY': value11,
32. 'CODES': value12
33. };

35. let valueBuckets = new Array(valueBucket1, valueBucket2, valueBucket3);
36. if (store != undefined) {
37. (store as relationalStore.RdbStore).batchInsertWithConflictResolution("EMPLOYEE", valueBuckets, relationalStore.ConflictResolution.ON_CONFLICT_REPLACE).then((insertNum: number) => {
38. console.info(`batchInsert is successful, insertNum = ${insertNum}`);
39. }).catch((err: BusinessError) => {
40. console.error(`batchInsert is failed, code is ${err.code},message is ${err.message}`);
41. });
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
| conflict | [ConflictResolution](arkts-apis-data-relationalstore-e.md#conflictresolution10) | 是 | 指定冲突解决模式。 |

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
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. let value1 = "Lisa";
2. let value2 = 18;
3. let value3 = 100.5;
4. let value4 = new Uint8Array([1, 2, 3, 4, 5]);
5. let value5 = "Jack";
6. let value6 = 19;
7. let value7 = 101.5;
8. let value8 = new Uint8Array([6, 7, 8, 9, 10]);
9. let value9 = "Tom";
10. let value10 = 20;
11. let value11 = 102.5;
12. let value12 = new Uint8Array([11, 12, 13, 14, 15]);

14. const valueBucket1: relationalStore.ValuesBucket = {
15. 'NAME': value1,
16. 'AGE': value2,
17. 'SALARY': value3,
18. 'CODES': value4
19. };
20. const valueBucket2: relationalStore.ValuesBucket = {
21. 'NAME': value5,
22. 'AGE': value6,
23. 'SALARY': value7,
24. 'CODES': value8
25. };
26. const valueBucket3: relationalStore.ValuesBucket = {
27. 'NAME': value9,
28. 'AGE': value10,
29. 'SALARY': value11,
30. 'CODES': value12
31. };

33. let valueBuckets = new Array(valueBucket1, valueBucket2, valueBucket3);
34. if (store != undefined) {
35. try {
36. let insertNum: number = (store as relationalStore.RdbStore).batchInsertWithConflictResolutionSync("EMPLOYEE", valueBuckets, relationalStore.ConflictResolution.ON_CONFLICT_REPLACE);
37. console.info(`batchInsert is successful, the number of values that were inserted = ${insertNum}`);
38. } catch (err) {
39. console.error(`batchInsert is failed, code is ${err.code},message is ${err.message}`);
40. }
41. }
```

## batchInsertWithReturning23+

PhonePC/2in1TabletTVWearable

batchInsertWithReturning(table: string, values: Array<ValuesBucket>, config: ReturningConfig, conflict?: ConflictResolution): Promise<Result>

向目标表中插入一组数据，可以通过conflict参数指定当发生数据冲突时的解决模式[ConflictResolution](arkts-apis-data-relationalstore-e.md#conflictresolution10)，返回[Result](arkts-apis-data-relationalstore-i.md#result23)。使用Promise异步回调。

单次插入参数的最大数量限制为32766，超出上限会返回14800001错误码。参数数量计算方式为插入数据条数乘以插入数据的所有字段总数。

例如：插入数据的所有字段总数为10，则最多可以插入3276条数据（3276\*10=32760）。

请确保在调用接口时遵守此限制，以避免因参数数量过多而导致错误。

conflict参数不建议使用ON\_CONFLICT\_FAIL策略，可能无法返回正确的结果。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**模型约束：** 此接口仅在Stage模型下可用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 要插入的目标表名。注意：正确的表名不应包含空格、逗号和星号，不能以点开头和结尾等，否则会抛出参数错误。 |
| values | Array<[ValuesBucket](arkts-apis-data-relationalstore-t.md#valuesbucket)> | 是 | 要插入到表中的一组数据。注意：空数组、含有重复资产数据会抛出参数错误。 |
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
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. async function batchInsertWithReturningExample(rdbStore: relationalStore.RdbStore)
2. {
3. const valueBucket1: relationalStore.ValuesBucket = { 'NAME': 'zhangsan', 'AGE': 18 };
4. const valueBucket2: relationalStore.ValuesBucket = { 'NAME': 'lisi', 'AGE': 20 };
5. const config: relationalStore.ReturningConfig = { columns: ['NAME', 'AGE'] };
6. const valueBuckets = new Array(valueBucket1, valueBucket2);
7. try {
8. let results = await rdbStore.batchInsertWithReturning("EMPLOYEE", valueBuckets, config);
9. console.info(`batchInsertWithReturningExample is successful, changed is ${results.changed}`);
10. while(results.resultSet.goToNextRow()) {
11. const row = results.resultSet.getRow();
12. console.info(`batchInsertWithReturningExample, name is ${row['NAME']}, age is ${row['AGE']}`);
13. }
14. } catch (e) {
15. console.error(`batchInsertWithReturningExample failed. code is ${e.code}, message is ${e.message}`);
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
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. function batchInsertWithReturningSyncExample(rdbStore: relationalStore.RdbStore)
2. {
3. const valueBucket1: relationalStore.ValuesBucket = { 'NAME': 'zhangsan', 'AGE': 18 };
4. const valueBucket2: relationalStore.ValuesBucket = { 'NAME': 'lisi', 'AGE': 20 };
5. const config: relationalStore.ReturningConfig = { columns: ['NAME', 'AGE'] };
6. const valueBuckets = new Array(valueBucket1, valueBucket2);
7. try {
8. let results = rdbStore.batchInsertWithReturningSync("EMPLOYEE", valueBuckets, config);
9. console.info(`batchInsertWithReturningSyncExample is successful, changed is ${results.changed}`);
10. while(results.resultSet.goToNextRow()) {
11. const row = results.resultSet.getRow();
12. console.info(`batchInsertWithReturningSyncExample, name is ${row['NAME']}, age is ${row['AGE']}`);
13. }
14. } catch (e) {
15. console.error(`batchInsertWithReturningSyncExample failed. code is ${e.code}, message is ${e.message}`);
16. }
17. }
```

## update

PhonePC/2in1TabletTVWearable

update(values: ValuesBucket, predicates: RdbPredicates, callback: AsyncCallback<number>):void

根据RdbPredicates的指定实例对象更新数据库中的数据，使用callback异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的[query](arkts-apis-data-relationalstore-rdbstore.md#query)或[querySql](arkts-apis-data-relationalstore-rdbstore.md#querysql)接口获取ResultSet后，调用[getValue](arkts-apis-data-relationalstore-resultset.md#getvalue12)、[getString](arkts-apis-data-relationalstore-resultset.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| values | [ValuesBucket](arkts-apis-data-relationalstore-t.md#valuesbucket) | 是 | values指示数据库中要更新的数据行。键值对与数据库表的列名相关联。 |
| predicates | [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 是 | RdbPredicates的实例对象指定的更新条件。 |
| callback | AsyncCallback<number> | 是 | 指定的callback回调方法。返回受影响的行数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. let value1 = "Rose";
2. let value2 = 22;
3. let value3 = 200.5;
4. let value4 = new Uint8Array([1, 2, 3, 4, 5]);

6. // 以下三种方式可用
7. const valueBucket1: relationalStore.ValuesBucket = {
8. 'NAME': value1,
9. 'AGE': value2,
10. 'SALARY': value3,
11. 'CODES': value4
12. };
13. const valueBucket2: relationalStore.ValuesBucket = {
14. NAME: value1,
15. AGE: value2,
16. SALARY: value3,
17. CODES: value4
18. };
19. const valueBucket3: relationalStore.ValuesBucket = {
20. "NAME": value1,
21. "AGE": value2,
22. "SALARY": value3,
23. "CODES": value4
24. };

26. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
27. predicates.equalTo("NAME", "Lisa");
28. if (store != undefined) {
29. (store as relationalStore.RdbStore).update(valueBucket1, predicates, (err, rows) => {
30. if (err) {
31. console.error(`Updated failed, code is ${err.code},message is ${err.message}`);
32. return;
33. }
34. console.info(`Updated row count: ${rows}`);
35. });
36. }
```

## update10+

PhonePC/2in1TabletTVWearable

update(values: ValuesBucket, predicates: RdbPredicates, conflict: ConflictResolution, callback: AsyncCallback<number>):void

根据RdbPredicates的指定实例对象更新数据库中的数据，可以通过conflict参数指定冲突解决模式[ConflictResolution](arkts-apis-data-relationalstore-e.md#conflictresolution10)，使用callback异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的[query](arkts-apis-data-relationalstore-rdbstore.md#query)或[querySql](arkts-apis-data-relationalstore-rdbstore.md#querysql)接口获取ResultSet后，调用[getValue](arkts-apis-data-relationalstore-resultset.md#getvalue12)、[getString](arkts-apis-data-relationalstore-resultset.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| values | [ValuesBucket](arkts-apis-data-relationalstore-t.md#valuesbucket) | 是 | values指示数据库中要更新的数据行。键值对与数据库表的列名相关联。 |
| predicates | [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 是 | RdbPredicates的实例对象指定的更新条件。 |
| conflict | [ConflictResolution](arkts-apis-data-relationalstore-e.md#conflictresolution10) | 是 | 指定冲突解决模式。 |
| callback | AsyncCallback<number> | 是 | 指定的callback回调方法。返回受影响的行数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. let value1 = "Rose";
2. let value2 = 22;
3. let value3 = 200.5;
4. let value4 = new Uint8Array([1, 2, 3, 4, 5]);

6. // 以下三种方式可用
7. const valueBucket1: relationalStore.ValuesBucket = {
8. 'NAME': value1,
9. 'AGE': value2,
10. 'SALARY': value3,
11. 'CODES': value4
12. };
13. const valueBucket2: relationalStore.ValuesBucket = {
14. NAME: value1,
15. AGE: value2,
16. SALARY: value3,
17. CODES: value4
18. };
19. const valueBucket3: relationalStore.ValuesBucket = {
20. "NAME": value1,
21. "AGE": value2,
22. "SALARY": value3,
23. "CODES": value4
24. };

26. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
27. predicates.equalTo("NAME", "Lisa");
28. if (store != undefined) {
29. (store as relationalStore.RdbStore).update(valueBucket1, predicates, relationalStore.ConflictResolution.ON_CONFLICT_REPLACE, (err, rows) => {
30. if (err) {
31. console.error(`Updated failed, code is ${err.code},message is ${err.message}`);
32. return;
33. }
34. console.info(`Updated row count: ${rows}`);
35. });
36. }
```

## update

PhonePC/2in1TabletTVWearable

update(values: ValuesBucket, predicates: RdbPredicates):Promise<number>

根据RdbPredicates的指定实例对象更新数据库中的数据，使用Promise异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的[query](arkts-apis-data-relationalstore-rdbstore.md#query)或[querySql](arkts-apis-data-relationalstore-rdbstore.md#querysql)接口获取ResultSet后，调用[getValue](arkts-apis-data-relationalstore-resultset.md#getvalue12)、[getString](arkts-apis-data-relationalstore-resultset.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| values | [ValuesBucket](arkts-apis-data-relationalstore-t.md#valuesbucket) | 是 | values指示数据库中要更新的数据行。键值对与数据库表的列名相关联。 |
| predicates | [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 是 | RdbPredicates的实例对象指定的更新条件。 |

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
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let value1 = "Rose";
4. let value2 = 22;
5. let value3 = 200.5;
6. let value4 = new Uint8Array([1, 2, 3, 4, 5]);

8. // 以下三种方式可用
9. const valueBucket1: relationalStore.ValuesBucket = {
10. 'NAME': value1,
11. 'AGE': value2,
12. 'SALARY': value3,
13. 'CODES': value4
14. };
15. const valueBucket2: relationalStore.ValuesBucket = {
16. NAME: value1,
17. AGE: value2,
18. SALARY: value3,
19. CODES: value4
20. };
21. const valueBucket3: relationalStore.ValuesBucket = {
22. "NAME": value1,
23. "AGE": value2,
24. "SALARY": value3,
25. "CODES": value4
26. };

28. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
29. predicates.equalTo("NAME", "Lisa");
30. if (store != undefined) {
31. (store as relationalStore.RdbStore).update(valueBucket1, predicates).then(async (rows: number) => {
32. console.info(`Updated row count: ${rows}`);
33. }).catch((err: BusinessError) => {
34. console.error(`Updated failed, code is ${err.code},message is ${err.message}`);
35. });
36. }
```

## update10+

PhonePC/2in1TabletTVWearable

update(values: ValuesBucket, predicates: RdbPredicates, conflict: ConflictResolution):Promise<number>

根据RdbPredicates的指定实例对象更新数据库中的数据，可以通过conflict参数指定冲突解决模式[ConflictResolution](arkts-apis-data-relationalstore-e.md#conflictresolution10)，使用Promise异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的[query](arkts-apis-data-relationalstore-rdbstore.md#query)或[querySql](arkts-apis-data-relationalstore-rdbstore.md#querysql)接口获取ResultSet后，调用[getValue](arkts-apis-data-relationalstore-resultset.md#getvalue12)、[getString](arkts-apis-data-relationalstore-resultset.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| values | [ValuesBucket](arkts-apis-data-relationalstore-t.md#valuesbucket) | 是 | values指示数据库中要更新的数据行。键值对与数据库表的列名相关联。 |
| predicates | [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 是 | RdbPredicates的实例对象指定的更新条件。 |
| conflict | [ConflictResolution](arkts-apis-data-relationalstore-e.md#conflictresolution10) | 是 | 指定冲突解决模式。 |

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
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let value1 = "Rose";
4. let value2 = 22;
5. let value3 = 200.5;
6. let value4 = new Uint8Array([1, 2, 3, 4, 5]);

8. // 以下三种方式可用
9. const valueBucket1: relationalStore.ValuesBucket = {
10. 'NAME': value1,
11. 'AGE': value2,
12. 'SALARY': value3,
13. 'CODES': value4
14. };
15. const valueBucket2: relationalStore.ValuesBucket = {
16. NAME: value1,
17. AGE: value2,
18. SALARY: value3,
19. CODES: value4
20. };
21. const valueBucket3: relationalStore.ValuesBucket = {
22. "NAME": value1,
23. "AGE": value2,
24. "SALARY": value3,
25. "CODES": value4
26. };

28. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
29. predicates.equalTo("NAME", "Lisa");
30. if (store != undefined) {
31. (store as relationalStore.RdbStore).update(valueBucket1, predicates, relationalStore.ConflictResolution.ON_CONFLICT_REPLACE).then(async (rows: number) => {
32. console.info(`Updated row count: ${rows}`);
33. }).catch((err: BusinessError) => {
34. console.error(`Updated failed, code is ${err.code},message is ${err.message}`);
35. });
36. }
```

## updateSync12+

PhonePC/2in1TabletTVWearable

updateSync(values: ValuesBucket, predicates: RdbPredicates, conflict?: ConflictResolution):number

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
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. let value1 = "Rose";
2. let value2 = 22;
3. let value3 = 200.5;
4. let value4 = new Uint8Array([1, 2, 3, 4, 5]);

6. // 以下三种方式可用
7. const valueBucket1: relationalStore.ValuesBucket = {
8. 'NAME': value1,
9. 'AGE': value2,
10. 'SALARY': value3,
11. 'CODES': value4
12. };
13. const valueBucket2: relationalStore.ValuesBucket = {
14. NAME: value1,
15. AGE: value2,
16. SALARY: value3,
17. CODES: value4
18. };
19. const valueBucket3: relationalStore.ValuesBucket = {
20. "NAME": value1,
21. "AGE": value2,
22. "SALARY": value3,
23. "CODES": value4
24. };

26. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
27. predicates.equalTo("NAME", "Lisa");
28. if (store != undefined) {
29. try {
30. let rows: number = (store as relationalStore.RdbStore).updateSync(valueBucket1, predicates, relationalStore.ConflictResolution.ON_CONFLICT_REPLACE);
31. console.info(`Updated row count: ${rows}`);
32. } catch (err) {
33. console.error(`Updated failed, code is ${err.code},message is ${err.message}`);
34. }
35. }
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
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. async function updateWithReturningExample(rdbStore: relationalStore.RdbStore)
2. {
3. const valueBucket1: relationalStore.ValuesBucket = { 'NAME': 'lisi', 'AGE': 21 };
4. const valueBucket2: relationalStore.ValuesBucket = { 'NAME': 'lisi', 'AGE': 18 };
5. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
6. predicates.equalTo('NAME', 'lisi');
7. const config: relationalStore.ReturningConfig = { columns: ['NAME', 'AGE'] };
8. try {
9. rdbStore.batchInsertWithReturningSync("EMPLOYEE", [valueBucket1, valueBucket2], config);
10. valueBucket1['NAME'] = "zhangsan";
11. valueBucket1['AGE'] = 18;
12. let results = await rdbStore.updateWithReturning(valueBucket1, predicates, config);
13. console.info(`updateWithReturningExample is successful, changed is ${results.changed}`);
14. while(results.resultSet.goToNextRow()) {
15. const row = results.resultSet.getRow();
16. console.info(`updateWithReturningExample, name is ${row['NAME']}, age is ${row['AGE']}`);
17. }
18. } catch (e) {
19. console.error(`updateWithReturningExample failed. code is ${e.code}, message is ${e.message}`);
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
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. function updateWithReturningSyncExample(rdbStore: relationalStore.RdbStore)
2. {
3. const valueBucket1: relationalStore.ValuesBucket = { 'NAME': 'lisi', 'AGE': 21 };
4. const valueBucket2: relationalStore.ValuesBucket = { 'NAME': 'lisi', 'AGE': 18 };
5. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
6. predicates.equalTo('NAME', 'lisi');
7. const config: relationalStore.ReturningConfig = { columns: ['NAME', 'AGE'] };
8. try {
9. rdbStore.batchInsertWithReturningSync("EMPLOYEE", [valueBucket1, valueBucket2], config);
10. valueBucket1['NAME'] = "zhangsan";
11. valueBucket1['AGE'] = 18;
12. let results = rdbStore.updateWithReturningSync(valueBucket1, predicates, config);
13. console.info(`updateWithReturningSyncExample is successful, changed is ${results.changed}`);
14. while(results.resultSet.goToNextRow()) {
15. const row = results.resultSet.getRow();
16. console.info(`updateWithReturningSyncExample, name is ${row['NAME']}, age is ${row['AGE']}`);
17. }
18. } catch (e) {
19. console.error(`updateWithReturningSyncExample failed. code is ${e.code}, message is ${e.message}`);
20. }
21. }
```

## delete

PhonePC/2in1TabletTVWearable

delete(predicates: RdbPredicates, callback: AsyncCallback<number>):void

根据RdbPredicates的指定实例对象从数据库中删除数据，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicates | [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 是 | RdbPredicates的实例对象指定的删除条件。 |
| callback | AsyncCallback<number> | 是 | 指定callback回调函数。返回受影响的行数量。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
2. predicates.equalTo("NAME", "Lisa");
3. if (store != undefined) {
4. (store as relationalStore.RdbStore).delete(predicates, (err, rows) => {
5. if (err) {
6. console.error(`Delete failed, code is ${err.code},message is ${err.message}`);
7. return;
8. }
9. console.info(`Delete rows: ${rows}`);
10. });
11. }
```

## delete

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
| Promise<number> | Promise对象。返回受影响的行数量。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
4. predicates.equalTo("NAME", "Lisa");
5. if (store != undefined) {
6. (store as relationalStore.RdbStore).delete(predicates).then((rows: number) => {
7. console.info(`Delete rows: ${rows}`);
8. }).catch((err: BusinessError) => {
9. console.error(`Delete failed, code is ${err.code},message is ${err.message}`);
10. });
11. }
```

## deleteSync12+

PhonePC/2in1TabletTVWearable

deleteSync(predicates: RdbPredicates):number

根据RdbPredicates的指定实例对象从数据库中删除数据。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicates | [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 是 | RdbPredicates的实例对象指定的删除条件。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| number | 返回受影响的行数量。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
2. predicates.equalTo("NAME", "Lisa");
3. if (store != undefined) {
4. try {
5. let rows: number = (store as relationalStore.RdbStore).deleteSync(predicates);
6. console.info(`Delete rows: ${rows}`);
7. } catch (err) {
8. console.error(`Delete failed, code is ${err.code},message is ${err.message}`);
9. }
10. }
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
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. async function deleteWithReturningExample(rdbStore: relationalStore.RdbStore)
2. {
3. const valueBucket1: relationalStore.ValuesBucket = { 'NAME': 'lisi', 'AGE': 21 };
4. const valueBucket2: relationalStore.ValuesBucket = { 'NAME': 'zhangsan', 'AGE': 18 };
5. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
6. const config: relationalStore.ReturningConfig = { columns: ['NAME', 'AGE'] };
7. try {
8. rdbStore.batchInsertWithReturningSync("EMPLOYEE", [valueBucket1, valueBucket2], config);
9. let results = await rdbStore.deleteWithReturning(predicates, config);
10. console.info(`deleteWithReturningExample is successful, changed is ${results.changed}`);
11. while(results.resultSet.goToNextRow()) {
12. const row = results.resultSet.getRow();
13. console.info(`deleteWithReturningExample, name is ${row['NAME']}, age is ${row['AGE']}`);
14. }
15. } catch (e) {
16. console.error(`deleteWithReturningExample failed. code is ${e.code}, message is ${e.message}`);
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
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. function deleteWithReturningSyncExample(rdbStore: relationalStore.RdbStore)
2. {
3. const valueBucket1: relationalStore.ValuesBucket = { 'NAME': 'lisi', 'AGE': 21 };
4. const valueBucket2: relationalStore.ValuesBucket = { 'NAME': 'zhangsan', 'AGE': 18 };
5. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
6. const config: relationalStore.ReturningConfig = { columns: ['NAME', 'AGE'] };
7. try {
8. rdbStore.batchInsertWithReturningSync("EMPLOYEE", [valueBucket1, valueBucket2], config);
9. let results = rdbStore.deleteWithReturningSync(predicates, config);
10. console.info(`deleteWithReturningSyncExample is successful, changed is ${results.changed}`);
11. while(results.resultSet.goToNextRow()) {
12. const row = results.resultSet.getRow();
13. console.info(`deleteWithReturningSyncExample, name is ${row['NAME']}, age is ${row['AGE']}`);
14. }
15. } catch (e) {
16. console.error(`deleteWithReturningSyncExample failed. code is ${e.code}, message is ${e.message}`);
17. }
18. }
```

## query10+

PhonePC/2in1TabletTVWearable

query(predicates: RdbPredicates, callback: AsyncCallback<ResultSet>):void

根据指定条件查询数据库中的数据，使用callback异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，使用此接口获取ResultSet后，调用[getValue](arkts-apis-data-relationalstore-resultset.md#getvalue12)、[getString](arkts-apis-data-relationalstore-resultset.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicates | [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 是 | RdbPredicates的实例对象指定的查询条件。 |
| callback | AsyncCallback<[ResultSet](arkts-apis-data-relationalstore-resultset.md)> | 是 | 指定callback回调函数。如果操作成功，则返回ResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |

**示例：**

```
1. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
2. predicates.equalTo("NAME", "Rose");
3. if (store != undefined) {
4. (store as relationalStore.RdbStore).query(predicates, async (err, resultSet) => {
5. if (err) {
6. console.error(`Query failed, code is ${err.code},message is ${err.message}`);
7. return;
8. }
9. console.info(`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}`);
10. // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
11. try {
12. while (resultSet.goToNextRow()) {
13. const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
14. const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
15. const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
16. const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
17. console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
18. }
19. } catch (err) {
20. console.error(`Query failed, code is ${err.code},message is ${err.message}`);
21. } finally {
22. // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
23. resultSet.close();
24. }
25. });
26. }
```

## query

PhonePC/2in1TabletTVWearable

query(predicates: RdbPredicates, columns: Array<string>, callback: AsyncCallback<ResultSet>):void

根据指定条件查询数据库中的数据，支持指定要查询的列，使用callback异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，使用此接口获取ResultSet后，调用[getValue](arkts-apis-data-relationalstore-resultset.md#getvalue12)、[getString](arkts-apis-data-relationalstore-resultset.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicates | [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 是 | RdbPredicates的实例对象指定的查询条件。 |
| columns | Array<string> | 是 | 表示要查询的列。如果值为空，则查询应用于所有列。 |
| callback | AsyncCallback<[ResultSet](arkts-apis-data-relationalstore-resultset.md)> | 是 | 指定callback回调函数。如果操作成功，则返回ResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |

**示例：**

```
1. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
2. predicates.equalTo("NAME", "Rose");
3. if (store != undefined) {
4. (store as relationalStore.RdbStore).query(predicates, ["ID", "NAME", "AGE", "SALARY", "CODES"], async (err, resultSet) => {
5. if (err) {
6. console.error(`Query failed, code is ${err.code},message is ${err.message}`);
7. return;
8. }
9. console.info(`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}`);
10. // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
11. try {
12. while (resultSet.goToNextRow()) {
13. const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
14. const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
15. const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
16. const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
17. console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
18. }
19. } catch (err) {
20. console.error(`Query failed, code is ${err.code},message is ${err.message}`);
21. } finally {
22. // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
23. resultSet.close();
24. }
25. });
26. }
```

## query

PhonePC/2in1TabletTVWearable

query(predicates: RdbPredicates, columns?: Array<string>):Promise<ResultSet>

根据指定条件查询数据库中的数据，使用Promise异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，使用此接口获取ResultSet后，调用[getValue](arkts-apis-data-relationalstore-resultset.md#getvalue12)、[getString](arkts-apis-data-relationalstore-resultset.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

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
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
4. predicates.equalTo("NAME", "Rose");
5. if (store != undefined) {
6. (store as relationalStore.RdbStore).query(predicates, ["ID", "NAME", "AGE", "SALARY", "CODES"]).then(async (resultSet: relationalStore.ResultSet) => {
7. console.info(`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}`);
8. // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
9. try {
10. while (resultSet.goToNextRow()) {
11. const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
12. const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
13. const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
14. const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
15. console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
16. }
17. } catch (err) {
18. console.error(`Query failed, code is ${err.code},message is ${err.message}`);
19. } finally {
20. // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
21. resultSet.close();
22. }
23. }).catch((err: BusinessError) => {
24. console.error(`Query failed, code is ${err.code},message is ${err.message}`);
25. });
26. }
```

## querySync12+

PhonePC/2in1TabletTVWearable

querySync(predicates: RdbPredicates, columns?: Array<string>):ResultSet

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
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |

**示例：**

```
1. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
2. predicates.equalTo("NAME", "Rose");
3. if (store != undefined) {
4. let resultSet: relationalStore.ResultSet | undefined;
5. try {
6. resultSet = store.querySync(predicates, ["ID", "NAME", "AGE", "SALARY", "CODES"]);
7. console.info(`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}`);
8. // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
9. while (resultSet.goToNextRow()) {
10. const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
11. const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
12. const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
13. const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
14. console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
15. }
16. } catch (err) {
17. console.error(`Query failed, code is ${err.code}, message is ${err.message}`);
18. } finally {
19. // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
20. if (resultSet) {
21. resultSet.close();
22. }
23. }
24. }
```

## queryWithoutRowCount23+

PhonePC/2in1TabletTVWearable

queryWithoutRowCount(predicates: RdbPredicates, columns?: Array<string>): Promise<LiteResultSet>

根据指定条件查询数据库中的数据，查询时不计算行数，性能优于[query](arkts-apis-data-relationalstore-rdbstore.md#query-1)接口。使用Promise异步回调。

**模型约束：** 此接口仅在Stage模型下可用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicates | [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 是 | RdbPredicates的实例对象指定的查询条件。 |
| columns | Array<string> | 否 | 表示要查询的列。如果值为空，则查询该表的所有列。默认值为空。 |

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
1. async function queryWithoutRowCountEmployee(store : relationalStore.RdbStore) {
2. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
3. predicates.equalTo("NAME", "Rose");
4. if (store != undefined) {
5. let resultSet: relationalStore.LiteResultSet | undefined;
6. try {
7. resultSet = await store.queryWithoutRowCount(predicates, ["ID", "NAME", "AGE", "SALARY", "CODES"]);
8. if (resultSet != undefined) {
9. // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
10. while (resultSet.goToNextRow()) {
11. const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
12. const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
13. const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
14. const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
15. console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
16. }
17. }
18. } catch (err) {
19. console.error(`Query failed, code is ${err.code}, message is ${err.message}`);
20. } finally {
21. // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
22. if (resultSet != undefined) {
23. resultSet.close();
24. }
25. }
26. }
27. }
```

## queryWithoutRowCountSync23+

PhonePC/2in1TabletTVWearable

queryWithoutRowCountSync(predicates: RdbPredicates, columns?: Array<string>): LiteResultSet

根据指定条件查询数据库中的数据，查询时不计算行数。对queryWithoutRowCountSync同步接口获得的LiteResultSet进行操作时，若逻辑复杂且循环次数过多，可能造成freeze问题，建议将此步骤放到[taskpool](js-apis-taskpool.md)线程中执行。

**模型约束：** 此接口仅在Stage模型下可用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

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
1. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
2. predicates.equalTo("NAME", "Rose");
3. if (store != undefined) {
4. let resultSet: relationalStore.LiteResultSet | undefined;
5. try {
6. resultSet = store.queryWithoutRowCountSync(predicates, ["ID", "NAME", "AGE", "SALARY", "CODES"]);
7. if (resultSet != undefined) {
8. // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
9. while (resultSet.goToNextRow()) {
10. const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
11. const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
12. const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
13. const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
14. console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
15. }
16. }
17. } catch (err) {
18. console.error(`Query failed, code is ${err.code}, message is ${err.message}`);
19. } finally {
20. // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
21. if (resultSet != undefined) {
22. resultSet.close();
23. }
24. }
25. }
```

## querySqlWithoutRowCount23+

PhonePC/2in1TabletTVWearable

querySqlWithoutRowCount(sql: string, bindArgs?: Array<ValueType>): Promise<LiteResultSet>

根据指定条件查询数据库中的数据，查询时不计算行数。使用Promise异步回调。性能优于[querySql](arkts-apis-data-relationalstore-rdbstore.md#querysql-1)接口。SQL语句中的各种表达式和操作符之间的关系操作符号不超过1000个。

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
1. async function querySqlWithoutRowCountEmployee(store : relationalStore.RdbStore) {
2. if (store != undefined) {
3. let resultSet: relationalStore.LiteResultSet | undefined;
4. try {
5. resultSet = await store.querySqlWithoutRowCount('select * from EMPLOYEE where name = ?', ["Rose"]);
6. if (resultSet != undefined) {
7. // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
8. while (resultSet.goToNextRow()) {
9. const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
10. const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
11. const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
12. const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
13. console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
14. }
15. }
16. } catch (err) {
17. console.error(`Query failed, code is ${err.code}, message is ${err.message}`);
18. } finally {
19. // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
20. if (resultSet != undefined) {
21. resultSet.close();
22. }
23. }
24. }
25. }
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
1. if (store != undefined) {
2. let resultSet: relationalStore.LiteResultSet | undefined;
3. try {
4. resultSet = store.querySqlWithoutRowCountSync('select * from EMPLOYEE where name = ?', ["Rose"]);
5. if (resultSet != undefined) {
6. // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
7. while (resultSet.goToNextRow()) {
8. const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
9. const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
10. const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
11. const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
12. console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
13. }
14. }
15. } catch (err) {
16. console.error(`Query failed, code is ${err.code}, message is ${err.message}`);
17. } finally {
18. // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
19. if (resultSet != undefined) {
20. resultSet.close();
21. }
22. }
23. }
```

## remoteQuery

PhonePC/2in1TabletTVWearable

remoteQuery(device: string, table: string, predicates: RdbPredicates, columns: Array<string> , callback: AsyncCallback<ResultSet>): void

根据指定条件查询远程设备数据库中的数据。使用callback异步回调。

说明

其中device通过调用[deviceManager.getAvailableDeviceListSync](js-apis-distributeddevicemanager.md#getavailabledevicelistsync)方法得到。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| device | string | 是 | 指定的远程设备ID。 |
| table | string | 是 | 指定的目标表名。 |
| predicates | [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 是 | RdbPredicates的实例对象，指定查询的条件。 |
| columns | Array<string> | 是 | 表示要查询的列。如果值为空，则查询应用于所有列。 |
| callback | AsyncCallback<[ResultSet](arkts-apis-data-relationalstore-resultset.md)> | 是 | 指定callback回调函数。如果操作成功，则返回ResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |

**示例：**

```
1. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let dmInstance: distributedDeviceManager.DeviceManager;
5. let deviceId: string | undefined = undefined;

7. try {
8. dmInstance = distributedDeviceManager.createDeviceManager("com.example.appdatamgrverify");
9. let devices = dmInstance.getAvailableDeviceListSync();
10. if (!devices || devices.length === 0) {
11. console.error("No available devices found");
12. } else {
13. deviceId = devices[0].networkId;
14. }
15. } catch (err) {
16. let code = (err as BusinessError).code;
17. let message = (err as BusinessError).message;
18. console.error("createDeviceManager errCode:" + code + ",errMessage:" + message);
19. }

21. let predicates = new relationalStore.RdbPredicates('EMPLOYEE');
22. predicates.greaterThan("id", 0);
23. if (store != undefined && deviceId != undefined) {
24. (store as relationalStore.RdbStore).remoteQuery(deviceId, "EMPLOYEE", predicates, ["ID", "NAME", "AGE", "SALARY", "CODES"], async (err, resultSet) => {
25. if (err) {
26. console.error(`Query failed, code is ${err.code},message is ${err.message}`);
27. return;
28. }
29. console.info(`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}`);
30. // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
31. try {
32. while (resultSet.goToNextRow()) {
33. const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
34. const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
35. const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
36. const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
37. console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
38. }
39. } catch (err) {
40. console.error(`Query failed, code is ${err.code},message is ${err.message}`);
41. } finally {
42. // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
43. resultSet.close();
44. }
45. });
46. }
```

## remoteQuery

PhonePC/2in1TabletTVWearable

remoteQuery(device: string, table: string, predicates: RdbPredicates, columns: Array<string>): Promise<ResultSet>

根据指定条件查询远程设备数据库中的数据。使用Promise异步回调。

说明

其中device通过调用[deviceManager.getAvailableDeviceListSync](js-apis-distributeddevicemanager.md#getavailabledevicelistsync)方法得到。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| device | string | 是 | 指定的远程设备ID。 |
| table | string | 是 | 指定的目标表名。 |
| predicates | [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 是 | RdbPredicates的实例对象，指定查询的条件。 |
| columns | Array<string> | 是 | 表示要查询的列。如果值为空，则查询应用于所有列。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[ResultSet](arkts-apis-data-relationalstore-resultset.md)> | Promise对象。如果操作成功，则返回ResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |

**示例：**

```
1. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let dmInstance: distributedDeviceManager.DeviceManager;
5. let deviceId: string | undefined = undefined;

7. try {
8. dmInstance = distributedDeviceManager.createDeviceManager("com.example.appdatamgrverify");
9. let devices: Array<distributedDeviceManager.DeviceBasicInfo> = dmInstance.getAvailableDeviceListSync();
10. if (!devices || devices.length === 0) {
11. console.error("No available devices found");
12. } else {
13. deviceId = devices[0].networkId;
14. }
15. } catch (err) {
16. let code = (err as BusinessError).code;
17. let message = (err as BusinessError).message;
18. console.error("createDeviceManager errCode:" + code + ",errMessage:" + message);
19. }

21. let predicates = new relationalStore.RdbPredicates('EMPLOYEE');
22. predicates.greaterThan("id", 0);
23. if (store != undefined && deviceId != undefined) {
24. (store as relationalStore.RdbStore).remoteQuery(deviceId, "EMPLOYEE", predicates, ["ID", "NAME", "AGE", "SALARY", "CODES"]).then(async (resultSet: relationalStore.ResultSet) => {
25. console.info(`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}`);
26. // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
27. try {
28. while (resultSet.goToNextRow()) {
29. const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
30. const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
31. const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
32. const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
33. console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
34. }
35. } catch (err) {
36. console.error(`Query failed, code is ${err.code},message is ${err.message}`);
37. } finally {
38. // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
39. resultSet.close();
40. }
41. }).catch((err: BusinessError) => {
42. console.error(`Failed to remoteQuery, code is ${err.code},message is ${err.message}`);
43. });
44. }
```

## querySql10+

PhonePC/2in1TabletTVWearable

querySql(sql: string, callback: AsyncCallback<ResultSet>):void

根据指定SQL语句查询数据库中的数据，SQL语句中的各种表达式和操作符之间的关系操作符号不超过1000个，使用callback异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，使用此接口获取ResultSet后，调用[getValue](arkts-apis-data-relationalstore-resultset.md#getvalue12)、[getString](arkts-apis-data-relationalstore-resultset.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

该接口支持向量数据库（在[StoreConfig](arkts-apis-data-relationalstore-i.md#storeconfig)中配置vector为true）使用，当前支持的语法见[规格限制](../harmonyos-guides/data-persistence-by-vector-store.md#规格限制)。

聚合函数不支持嵌套使用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sql | string | 是 | 指定要执行的SQL语句。 |
| callback | AsyncCallback<[ResultSet](arkts-apis-data-relationalstore-resultset.md)> | 是 | 指定callback回调函数。如果操作成功，则返回ResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |

**示例：**

关系型数据库：

```
1. if (store != undefined) {
2. (store as relationalStore.RdbStore).querySql("SELECT * FROM EMPLOYEE CROSS JOIN BOOK WHERE BOOK.NAME = 'sanguo'", async (err, resultSet) => {
3. if (err) {
4. console.error(`Query failed, code is ${err.code},message is ${err.message}`);
5. return;
6. }
7. console.info(`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}`);
8. // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
9. try {
10. while (resultSet.goToNextRow()) {
11. const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
12. const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
13. const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
14. const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
15. console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
16. }
17. } catch (err) {
18. console.error(`Query failed, code is ${err.code},message is ${err.message}`);
19. } finally {
20. // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
21. resultSet.close();
22. }
23. });
24. }
```

向量数据库：

```
1. // 相似度的计算符号是<->，余弦距离的计算符号是<=>
2. const querySql = "select id, repr <-> '[1.5,5.6]' as distance from test ORDER BY repr <-> '[1.5,5.6]' limit 10 offset 1;";
3. let resultSet = await store.querySql(querySql);

5. // 聚合查询，其中group by支持多列
6. const querySql1 = "select id, repr from test group by id, repr having max(repr<=>'[1.5,5.6]');";
7. let resultSet1 = await store.querySql(querySql1);

9. // 子查询，最大支持嵌套32层
10. const querySql2 = "select * from test where id in (select id from test1)";
11. let resultSet2 = await store.querySql(querySql2);
```

## querySql

PhonePC/2in1TabletTVWearable

querySql(sql: string, bindArgs: Array<ValueType>, callback: AsyncCallback<ResultSet>):void

根据指定SQL语句查询数据库中的数据，SQL语句中的各种表达式和操作符之间的关系操作符号不超过1000个，支持传入SQL语句中参数的值，使用callback异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，使用此接口获取ResultSet后，调用[getValue](arkts-apis-data-relationalstore-resultset.md#getvalue12)、[getString](arkts-apis-data-relationalstore-resultset.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

该接口支持向量数据库（在[StoreConfig](arkts-apis-data-relationalstore-i.md#storeconfig)中配置vector为true）使用，当前支持的语法见[规格限制](../harmonyos-guides/data-persistence-by-vector-store.md#规格限制)。

聚合函数不支持嵌套使用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sql | string | 是 | 指定要执行的SQL语句。 |
| bindArgs | Array<[ValueType](arkts-apis-data-relationalstore-t.md#valuetype)> | 是 | SQL语句中参数的值。该值与sql参数语句中的占位符相对应。当sql参数语句完整时，该参数需为空数组。 |
| callback | AsyncCallback<[ResultSet](arkts-apis-data-relationalstore-resultset.md)> | 是 | 指定callback回调函数。如果操作成功，则返回ResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |

**示例：**

```
1. if (store != undefined) {
2. (store as relationalStore.RdbStore).querySql("SELECT * FROM EMPLOYEE CROSS JOIN BOOK WHERE BOOK.NAME = ?", ['sanguo'], async (err, resultSet) => {
3. if (err) {
4. console.error(`Query failed, code is ${err.code},message is ${err.message}`);
5. return;
6. }
7. console.info(`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}`);
8. // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
9. try {
10. while (resultSet.goToNextRow()) {
11. const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
12. const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
13. const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
14. const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
15. console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
16. }
17. } catch (err) {
18. console.error(`Query failed, code is ${err.code},message is ${err.message}`);
19. } finally {
20. // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
21. resultSet.close();
22. }
23. });
24. }
```

## querySql

PhonePC/2in1TabletTVWearable

querySql(sql: string, bindArgs?: Array<ValueType>):Promise<ResultSet>

根据指定SQL语句查询数据库中的数据，SQL语句中的各种表达式和操作符之间的关系操作符号不超过1000个，使用Promise异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，使用此接口获取ResultSet后，调用[getValue](arkts-apis-data-relationalstore-resultset.md#getvalue12)、[getString](arkts-apis-data-relationalstore-resultset.md#getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

该接口支持向量数据库（在[StoreConfig](arkts-apis-data-relationalstore-i.md#storeconfig)中配置vector为true）使用，当前支持的语法见[规格限制](../harmonyos-guides/data-persistence-by-vector-store.md#规格限制)。

聚合函数不支持嵌套使用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sql | string | 是 | 指定要执行的SQL语句。 |
| bindArgs | Array<[ValueType](arkts-apis-data-relationalstore-t.md#valuetype)> | 否 | SQL语句中参数的值。该值与sql参数语句中的占位符相对应。当sql参数语句完整时，该参数不填。 |

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
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |

**示例：**

关系型数据库：

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. if (store != undefined) {
4. (store as relationalStore.RdbStore).querySql("SELECT * FROM EMPLOYEE CROSS JOIN BOOK WHERE BOOK.NAME = 'sanguo'").then(async (resultSet: relationalStore.ResultSet) => {
5. console.info(`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}`);
6. // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
7. try {
8. while (resultSet.goToNextRow()) {
9. const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
10. const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
11. const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
12. const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
13. console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
14. }
15. } catch (err) {
16. console.error(`Query failed, code is ${err.code},message is ${err.message}`);
17. } finally {
18. // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
19. resultSet.close();
20. }
21. }).catch((err: BusinessError) => {
22. console.error(`Query failed, code is ${err.code},message is ${err.message}`);
23. });
24. }
```

向量数据库：

```
1. // 查询id为1，与[1.5, 2.5]相似度小于0.5，且以相似度进行升序排序的前10条数据
2. const querySql = "select id, repr <-> ? as distance from test where id = ? and repr <-> ? < 0.5 ORDER BY repr <-> ? limit 10;";
3. const vectorValue: Float32Array = new Float32Array([1.5, 2.5]);
4. let resultSet = await store.querySql(querySql, [vectorValue, 1, vectorValue, vectorValue]);
```

## querySqlSync12+

PhonePC/2in1TabletTVWearable

querySqlSync(sql: string, bindArgs?: Array<ValueType>):ResultSet

根据指定SQL语句查询数据库中的数据，SQL语句中的各种表达式和操作符之间的关系操作符号不超过1000个。对query同步接口获得的resultSet进行操作时，若逻辑复杂且循环次数过多，可能造成freeze问题，建议将此步骤放到[taskpool](js-apis-taskpool.md)线程中执行。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sql | string | 是 | 指定要执行的SQL语句。 |
| bindArgs | Array<[ValueType](arkts-apis-data-relationalstore-t.md#valuetype)> | 否 | SQL语句中参数的值。该值与sql参数语句中的占位符相对应。当sql参数语句完整时，该参数不填。默认值为空。 |

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
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |

**示例：**

```
1. if (store != undefined) {
2. let resultSet: relationalStore.ResultSet | undefined;
3. try {
4. resultSet = store.querySqlSync("SELECT * FROM EMPLOYEE CROSS JOIN BOOK WHERE BOOK.NAME = 'sanguo'");
5. console.info(`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}`);
6. // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
7. while (resultSet.goToNextRow()) {
8. const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
9. const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
10. const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
11. const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
12. console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
13. }
14. } catch (err) {
15. console.error(`Query failed, code is ${err.code},message is ${err.message}`);
16. } finally {
17. // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
18. if (resultSet) {
19. resultSet.close();
20. }
21. }
22. }
```

## executeSql10+

PhonePC/2in1TabletTVWearable

executeSql(sql: string, callback: AsyncCallback<void>):void

执行指定的SQL语句，语句中的各种表达式和操作符之间的关系操作符号不超过1000个，使用callback异步回调。

此接口不支持执行查询、附加数据库和事务操作，可以使用[querySql](arkts-apis-data-relationalstore-rdbstore.md#querysql10)、[query](arkts-apis-data-relationalstore-rdbstore.md#query10)、[attach](arkts-apis-data-relationalstore-rdbstore.md#attach12)、[beginTransaction](arkts-apis-data-relationalstore-rdbstore.md#begintransaction)、[commit](arkts-apis-data-relationalstore-rdbstore.md#commit)等接口代替。

不支持分号分隔的多条语句。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sql | string | 是 | 指定要执行的SQL语句。 |
| callback | AsyncCallback<void> | 是 | 指定callback回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported the sql(attach,begin,commit,rollback etc.). |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. const SQL_DELETE_TABLE = "DELETE FROM test WHERE name = 'zhangsan'";
2. if (store != undefined) {
3. (store as relationalStore.RdbStore).executeSql(SQL_DELETE_TABLE, (err) => {
4. if (err) {
5. console.error(`ExecuteSql failed, code is ${err.code},message is ${err.message}`);
6. return;
7. }
8. console.info('Delete table done.');
9. });
10. }
```

## executeSql

PhonePC/2in1TabletTVWearable

executeSql(sql: string, bindArgs: Array<ValueType>, callback: AsyncCallback<void>):void

执行指定的SQL语句，支持传入SQL语句中参数的值，语句中的各种表达式和操作符之间的关系操作符号不超过1000个，使用callback异步回调。

此接口不支持执行查询、附加数据库和事务操作，可以使用[querySql](arkts-apis-data-relationalstore-rdbstore.md#querysql10)、[query](arkts-apis-data-relationalstore-rdbstore.md#query10)、[attach](arkts-apis-data-relationalstore-rdbstore.md#attach12)、[beginTransaction](arkts-apis-data-relationalstore-rdbstore.md#begintransaction)、[commit](arkts-apis-data-relationalstore-rdbstore.md#commit)等接口代替。

不支持分号分隔的多条语句。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sql | string | 是 | 指定要执行的SQL语句。 |
| bindArgs | Array<[ValueType](arkts-apis-data-relationalstore-t.md#valuetype)> | 是 | SQL语句中参数的值。该值与sql参数语句中的占位符相对应。当sql参数语句完整时，该参数需为空数组。 |
| callback | AsyncCallback<void> | 是 | 指定callback回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported the sql(attach,begin,commit,rollback etc.). |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. const SQL_DELETE_TABLE = "DELETE FROM test WHERE name = ?";
2. if (store != undefined) {
3. (store as relationalStore.RdbStore).executeSql(SQL_DELETE_TABLE, ['zhangsan'], (err) => {
4. if (err) {
5. console.error(`ExecuteSql failed, code is ${err.code},message is ${err.message}`);
6. return;
7. }
8. console.info('Delete table done.');
9. });
10. }
```

## executeSql

PhonePC/2in1TabletTVWearable

executeSql(sql: string, bindArgs?: Array<ValueType>):Promise<void>

执行指定的SQL语句，语句中的各种表达式和操作符之间的关系操作符号不超过1000个，使用Promise异步回调。

此接口不支持执行查询、附加数据库和事务操作，可以使用[querySql](arkts-apis-data-relationalstore-rdbstore.md#querysql10)、[query](arkts-apis-data-relationalstore-rdbstore.md#query10)、[attach](arkts-apis-data-relationalstore-rdbstore.md#attach12)、[beginTransaction](arkts-apis-data-relationalstore-rdbstore.md#begintransaction)、[commit](arkts-apis-data-relationalstore-rdbstore.md#commit)等接口代替。

不支持分号分隔的多条语句。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sql | string | 是 | 指定要执行的SQL语句。 |
| bindArgs | Array<[ValueType](arkts-apis-data-relationalstore-t.md#valuetype)> | 否 | SQL语句中参数的值。该值与sql参数语句中的占位符相对应。当sql参数语句完整时，该参数不填。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported the sql(attach,begin,commit,rollback etc.). |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const SQL_DELETE_TABLE = "DELETE FROM test WHERE name = 'zhangsan'";
4. if (store != undefined) {
5. (store as relationalStore.RdbStore).executeSql(SQL_DELETE_TABLE).then(() => {
6. console.info('Delete table done.');
7. }).catch((err: BusinessError) => {
8. console.error(`ExecuteSql failed, code is ${err.code},message is ${err.message}`);
9. });
10. }
```

## execute12+

PhonePC/2in1TabletTVWearable

execute(sql: string, args?: Array<ValueType>):Promise<ValueType>

执行包含指定参数的SQL语句，语句中的各种表达式和操作符之间的关系操作符号不超过1000个，返回值类型为ValueType，使用Promise异步回调。

该接口支持执行增删改操作，支持执行PRAGMA语法的sql，支持对表的操作（建表、删表、修改表），返回结果类型由执行具体sql的结果决定。

此接口不支持执行查询、附加数据库和事务操作，可以使用[querySql](arkts-apis-data-relationalstore-rdbstore.md#querysql10)、[query](arkts-apis-data-relationalstore-rdbstore.md#query10)、[attach](arkts-apis-data-relationalstore-rdbstore.md#attach12)、[beginTransaction](arkts-apis-data-relationalstore-rdbstore.md#begintransaction)、[commit](arkts-apis-data-relationalstore-rdbstore.md#commit)等接口代替。

向量数据库使用该接口执行插入操作，数据来源于子查询时，支持全字段插入，暂不支持部分字段插入。

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
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

关系型数据库：

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // 校验数据库完整性
4. if (store != undefined) {
5. const SQL_CHECK_INTEGRITY = 'PRAGMA integrity_check';
6. (store as relationalStore.RdbStore).execute(SQL_CHECK_INTEGRITY).then((data) => {
7. console.info(`check result: ${data}`);
8. }).catch((err: BusinessError) => {
9. console.error(`check failed, code is ${err.code}, message is ${err.message}`);
10. });
11. }

13. // 删除表中所有数据
14. if (store != undefined) {
15. const SQL_DELETE_TABLE = 'DELETE FROM test';
16. (store as relationalStore.RdbStore).execute(SQL_DELETE_TABLE).then((data) => {
17. console.info(`delete result: ${data}`);
18. }).catch((err: BusinessError) => {
19. console.error(`delete failed, code is ${err.code}, message is ${err.message}`);
20. });
21. }

23. // 删表
24. if (store != undefined) {
25. const SQL_DROP_TABLE = 'DROP TABLE test';
26. (store as relationalStore.RdbStore).execute(SQL_DROP_TABLE).then((data) => {
27. console.info(`drop result: ${data}`);
28. }).catch((err: BusinessError) => {
29. console.error(`drop failed, code is ${err.code}, message is ${err.message}`);
30. });
31. }
```

向量数据库：

```
1. // FLOATVECTOR(2)是维度为2的向量属性，后续操作repr需依照该维度进行。
2. let createSql = "CREATE TABLE test (ID INTEGER PRIMARY KEY,REPR FLOATVECTOR(2));";
3. // 建表
4. await store!.execute(createSql);
5. // 使用参数绑定插入数据
6. let insertSql = "insert into test VALUES(?, ?);";
7. const vectorValue: Float32Array = Float32Array.from([1.5, 6.6]);
8. await store!.execute(insertSql, [0, vectorValue]);
9. // 不使用绑定参数直接执行
10. await store!.execute("insert into test values(1, '[3.5, 1.8]');");
```

## execute12+

PhonePC/2in1TabletTVWearable

execute(sql: string, txId: number, args?: Array<ValueType>): Promise<ValueType>

执行包含指定参数的SQL语句，语句中的各种表达式和操作符之间的关系操作符号不超过1000个，使用Promise异步回调。

该接口仅支持向量数据库（在[StoreConfig](arkts-apis-data-relationalstore-i.md#storeconfig)中配置vector为true）使用。使用该接口执行插入操作，数据来源于子查询时，支持全字段插入，暂不支持部分字段插入。

此接口不支持执行查询，可以使用[querySql](arkts-apis-data-relationalstore-rdbstore.md#querysql10)接口代替。

不支持分号分隔的多条语句。

不支持开头包含注释的语句。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sql | string | 是 | 指定要执行的SQL语句。 |
| txId | number | 是 | 通过[beginTrans](arkts-apis-data-relationalstore-rdbstore.md#begintrans12)获取的事务ID，如果传0，该语句默认在单独事务内。 |
| args | Array<[ValueType](arkts-apis-data-relationalstore-t.md#valuetype)> | 否 | SQL语句中参数的值。该值与sql参数语句中的占位符相对应。该参数不填，填null或者填undefined，都认为是sql参数语句完整。 |

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
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. if (store != null) {
3. let txId: number;
4. (store as relationalStore.RdbStore).beginTrans().then((temTxId: number) => {
5. txId = temTxId;
6. (store as relationalStore.RdbStore).execute("DELETE FROM TEST WHERE age = ? OR age = ?", txId, ["18", "20"])
7. .then(() => {
8. if (txId !== undefined) {
9. (store as relationalStore.RdbStore).commit(txId);
10. }
11. })
12. .catch((err: BusinessError) => {
13. if (txId !== undefined) {
14. (store as relationalStore.RdbStore).rollback(txId);
15. }
16. console.error(`execute sql failed, code is ${err.code},message is ${err.message}`);
17. });
18. });
19. }
```

## executeSync12+

PhonePC/2in1TabletTVWearable

executeSync(sql: string, args?: Array<ValueType>): ValueType

执行包含指定参数的SQL语句，语句中的各种表达式和操作符之间的关系操作符号不超过1000个，返回值类型为ValueType。

该接口支持执行增删改操作，支持执行PRAGMA语法的sql，支持对表的操作（建表、删表、修改表），返回结果类型由执行具体sql的结果决定。

此接口不支持执行查询、附加数据库和事务操作，可以使用[querySql](arkts-apis-data-relationalstore-rdbstore.md#querysql10)、[query](arkts-apis-data-relationalstore-rdbstore.md#query10)、[attach](arkts-apis-data-relationalstore-rdbstore.md#attach12)、[beginTransaction](arkts-apis-data-relationalstore-rdbstore.md#begintransaction)、[commit](arkts-apis-data-relationalstore-rdbstore.md#commit)等接口代替。

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
| [ValueType](arkts-apis-data-relationalstore-t.md#valuetype) | 返回sql执行后的结果 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. // 校验数据库完整性
2. if (store != undefined) {
3. const SQL_CHECK_INTEGRITY = 'PRAGMA integrity_check';
4. try {
5. let data = (store as relationalStore.RdbStore).executeSync(SQL_CHECK_INTEGRITY);
6. console.info(`check result: ${data}`);
7. } catch (err) {
8. console.error(`check failed, code is ${err.code}, message is ${err.message}`);
9. }
10. }

12. // 删除表中所有数据
13. if (store != undefined) {
14. const SQL_DELETE_TABLE = 'DELETE FROM test';
15. try {
16. let data = (store as relationalStore.RdbStore).executeSync(SQL_DELETE_TABLE);
17. console.info(`delete result: ${data}`);
18. } catch (err) {
19. console.error(`delete failed, code is ${err.code}, message is ${err.message}`);
20. }
21. }

23. // 删表
24. if (store != undefined) {
25. const SQL_DROP_TABLE = 'DROP TABLE test';
26. try {
27. let data = (store as relationalStore.RdbStore).executeSync(SQL_DROP_TABLE);
28. console.info(`drop result: ${data}`);
29. } catch (err) {
30. console.error(`drop failed, code is ${err.code}, message is ${err.message}`);
31. }
32. }
```

## getModifyTime10+

PhonePC/2in1TabletTVWearable

getModifyTime(table: string, columnName: string, primaryKeys: PRIKeyType[], callback: AsyncCallback<ModifyTime>): void

获取数据库表中数据的最后修改时间，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 指定要查询的数据库表的表名。 |
| columnName | string | 是 | 指定要查询的数据库表的列名。 |
| primaryKeys | [PRIKeyType](arkts-apis-data-relationalstore-t.md#prikeytype10)[] | 是 | 指定要查询的行的主键。  如果数据库表无主键，参数columnName需传入"rowid"，此时primaryKeys为要查询的数据库表的行号。  如果数据库表无主键，参数columnName传入不为"rowid"，返回对应的错误码。 |
| callback | AsyncCallback<[ModifyTime](arkts-apis-data-relationalstore-t.md#modifytime10)> | 是 | 指定callback回调函数。如果操作成功，则返回ModifyTime对象，表示数据的最后修改时间。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Need 3 - 4 parameter(s)! 2. The RdbStore must be not nullptr. 3. The tablesNames must be not empty string. 4. The columnName must be not empty string. 5. The PRIKey must be number or string. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**示例：**

```
1. let PRIKey = [1, 4, 2, 3];
2. if (store != undefined) {
3. (store as relationalStore.RdbStore).getModifyTime("EMPLOYEE", "NAME", PRIKey, (err, modifyTime: relationalStore.ModifyTime) => {
4. if (err) {
5. console.error(`getModifyTime failed, code is ${err.code},message is ${err.message}`);
6. return;
7. }
8. let size = modifyTime.size;
9. });
10. }
```

## getModifyTime10+

PhonePC/2in1TabletTVWearable

getModifyTime(table: string, columnName: string, primaryKeys: PRIKeyType[]): Promise<ModifyTime>

获取数据库表中数据的最后修改时间，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 指定要查询的数据库表的表名。 |
| columnName | string | 是 | 指定要查询的数据库表的列名。 |
| primaryKeys | [PRIKeyType](arkts-apis-data-relationalstore-t.md#prikeytype10)[] | 是 | 指定要查询的行的主键。  如果数据库表无主键，参数columnName需传入"rowid"，此时primaryKeys为要查询的数据库表的行号。  如果数据库表无主键，参数columnName传入不为"rowid"，返回对应的错误码。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[ModifyTime](arkts-apis-data-relationalstore-t.md#modifytime10)> | 返回ModifyTime类型的Promise对象，表示数据最后的修改时间。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Need 3 - 4 parameter(s)! 2. The RdbStore must be not nullptr.3. The tablesNames must be not empty string. 4. The columnName must be not empty string. 5. The PRIKey must be number or string. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let PRIKey = [1, 2, 3];
4. if (store != undefined) {
5. (store as relationalStore.RdbStore).getModifyTime("EMPLOYEE", "NAME", PRIKey)
6. .then((modifyTime: relationalStore.ModifyTime) => {
7. let size = modifyTime.size;
8. })
9. .catch((err: BusinessError) => {
10. console.error(`getModifyTime failed, code is ${err.code},message is ${err.message}`);
11. });
12. }
```

## beginTransaction

PhonePC/2in1TabletTVWearable

beginTransaction():void

在开始执行SQL语句之前，开始事务。

此接口不允许嵌套事务，且不支持在多进程或多线程中使用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: The RdbStore verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. let value1 = "Lisa";
2. let value2 = 18;
3. let value3 = 100.5;
4. let value4 = new Uint8Array([1, 2, 3]);

6. if (store != undefined) {
7. (store as relationalStore.RdbStore).beginTransaction();
8. const valueBucket: relationalStore.ValuesBucket = {
9. 'NAME': value1,
10. 'AGE': value2,
11. 'SALARY': value3,
12. 'CODES': value4
13. };
14. (store as relationalStore.RdbStore).insert("test", valueBucket);
15. (store as relationalStore.RdbStore).commit();
16. }
```

## beginTrans12+

PhonePC/2in1TabletTVWearable

beginTrans(): Promise<number>

在开始执行SQL语句之前，开始事务，使用Promise异步回调。

与[beginTransaction](arkts-apis-data-relationalstore-rdbstore.md#begintransaction)的区别在于：该接口会返回事务ID，[execute](arkts-apis-data-relationalstore-rdbstore.md#execute12-1)可以指定不同事务ID达到事务隔离目的。

该接口仅支持向量数据库（在[StoreConfig](arkts-apis-data-relationalstore-i.md#storeconfig)中配置vector为true）使用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回事务ID。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: The RdbStore verification failed. |
| 801 | Capability not supported the sql(attach,begin,commit,rollback etc.). |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. if (store != null) {
3. let txId: number;
4. (store as relationalStore.RdbStore).beginTrans().then((temTxId: number) => {
5. txId = temTxId;
6. (store as relationalStore.RdbStore).execute("DELETE FROM TEST WHERE age = ? OR age = ?", txId, ["18", "20"])
7. .then(() => {
8. if (txId !== undefined) {
9. (store as relationalStore.RdbStore).commit(txId);
10. }
11. })
12. .catch((err: BusinessError) => {
13. if (txId !== undefined) {
14. (store as relationalStore.RdbStore).rollback(txId);
15. }
16. console.error(`execute sql failed, code is ${err.code},message is ${err.message}`);
17. });
18. });
19. }
```

## createTransaction14+

PhonePC/2in1TabletTVWearable

createTransaction(options?: TransactionOptions): Promise<Transaction>

创建一个事务对象并开始事务，使用Promise异步回调。

与[beginTransaction](arkts-apis-data-relationalstore-rdbstore.md#begintransaction)的区别在于：createTransaction接口会返回一个事务对象，不同事务对象之间是隔离的。使用事务对象进行插入、删除或更新数据等操作，无法被注册数据变更通知[on('dataChange')](arkts-apis-data-relationalstore-rdbstore.md#ondatachange)监听到。

一个store最多支持同时存在四个事务对象，超过后会返回14800015错误码，此时需要检查是否持有事务对象时间过长或并发事务过多，若确认无法通过上述优化解决问题，建议等待现有事务释放后，再尝试新建事务对象。

优先使用createTransaction，不再推荐使用beginTransaction。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [TransactionOptions](arkts-apis-data-relationalstore-i.md#transactionoptions14) | 否 | 表示事务对象的配置信息。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[Transaction](arkts-apis-data-relationalstore-transaction.md)> | Promise对象，返回事务对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database is busy. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. if (store != undefined) {
4. (store as relationalStore.RdbStore).createTransaction().then(async (transaction: relationalStore.Transaction) => {
5. transaction.execute("DELETE FROM test WHERE age = ? OR age = ?", [21, 20]).then(() => {
6. transaction.commit();
7. }).catch((e: BusinessError) => {
8. transaction.rollback();
9. console.error(`execute sql failed, code is ${e.code},message is ${e.message}`);
10. });
11. }).catch((err: BusinessError) => {
12. console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
13. });
14. }
```

## commit

PhonePC/2in1TabletTVWearable

commit():void

提交已执行的SQL语句，跟[beginTransaction](arkts-apis-data-relationalstore-rdbstore.md#begintransaction)配合使用。

此接口不允许嵌套事务，且不支持在多进程或多线程中使用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: The RdbStore verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**示例：**

```
1. let value1 = "Lisa";
2. let value2 = 18;
3. let value3 = 100.5;
4. let value4 = new Uint8Array([1, 2, 3]);

6. if (store != undefined) {
7. (store as relationalStore.RdbStore).beginTransaction();
8. const valueBucket: relationalStore.ValuesBucket = {
9. 'NAME': value1,
10. 'AGE': value2,
11. 'SALARY': value3,
12. 'CODES': value4
13. };
14. (store as relationalStore.RdbStore).insert("test", valueBucket);
15. (store as relationalStore.RdbStore).commit();
16. }
```

## commit12+

PhonePC/2in1TabletTVWearable

commit(txId : number):Promise<void>

提交已执行的SQL语句，跟[beginTrans](arkts-apis-data-relationalstore-rdbstore.md#begintrans12)配合使用，使用Promise异步回调。

该接口仅支持向量数据库（在[StoreConfig](arkts-apis-data-relationalstore-i.md#storeconfig)中配置vector为true）使用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| txId | number | 是 | 通过[beginTrans](arkts-apis-data-relationalstore-rdbstore.md#begintrans12)获取的事务ID。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. if (store != null) {
3. let txId: number;
4. (store as relationalStore.RdbStore).beginTrans().then((temTxId: number) => {
5. txId = temTxId;
6. (store as relationalStore.RdbStore).execute("DELETE FROM TEST WHERE age = ? OR age = ?", txId, ["18", "20"])
7. .then(() => {
8. if (txId !== undefined) {
9. (store as relationalStore.RdbStore).commit(txId);
10. }
11. })
12. .catch((err: BusinessError) => {
13. if (txId !== undefined) {
14. (store as relationalStore.RdbStore).rollback(txId);
15. }
16. console.error(`execute sql failed, code is ${err.code},message is ${err.message}`);
17. });
18. });
19. }
```

## rollBack

PhonePC/2in1TabletTVWearable

rollBack():void

回滚已经执行的SQL语句。

此接口不允许嵌套事务，且不支持在多进程或多线程中使用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: The RdbStore verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let value1 = "Lisa";
4. let value2 = 18;
5. let value3 = 100.5;
6. let value4 = new Uint8Array([1, 2, 3]);

8. if (store != undefined) {
9. try {
10. (store as relationalStore.RdbStore).beginTransaction();
11. const valueBucket: relationalStore.ValuesBucket = {
12. 'NAME': value1,
13. 'AGE': value2,
14. 'SALARY': value3,
15. 'CODES': value4
16. };
17. (store as relationalStore.RdbStore).insert("test", valueBucket);
18. (store as relationalStore.RdbStore).commit();
19. } catch (err) {
20. let code = (err as BusinessError).code;
21. let message = (err as BusinessError).message;
22. console.error(`Transaction failed, code is ${code},message is ${message}`);
23. (store as relationalStore.RdbStore).rollBack();
24. }
25. }
```

## rollback12+

PhonePC/2in1TabletTVWearable

rollback(txId : number):Promise<void>

回滚已经执行的SQL语句，跟[beginTrans](arkts-apis-data-relationalstore-rdbstore.md#begintrans12)配合使用，使用Promise异步回调。

该接口仅支持向量数据库（在[StoreConfig](arkts-apis-data-relationalstore-i.md#storeconfig)中配置vector为true）使用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| txId | number | 是 | 通过[beginTrans](arkts-apis-data-relationalstore-rdbstore.md#begintrans12)获取的事务ID。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. if (store != null) {
3. let txId: number;
4. (store as relationalStore.RdbStore).beginTrans().then((temTxId: number) => {
5. txId = temTxId;
6. (store as relationalStore.RdbStore).execute("DELETE FROM TEST WHERE age = ? OR age = ?", txId, ["18", "20"])
7. .then(() => {
8. if (txId !== undefined) {
9. (store as relationalStore.RdbStore).commit(txId);
10. }
11. })
12. .catch((err: BusinessError) => {
13. if (txId !== undefined) {
14. (store as relationalStore.RdbStore).rollback(txId);
15. }
16. console.error(`execute sql failed, code is ${err.code},message is ${err.message}`);
17. });
18. });
19. }
```

## backup

PhonePC/2in1TabletTVWearable

backup(destName:string, callback: AsyncCallback<void>):void

以指定名称备份数据库，使用callback异步回调。

该接口支持向量数据库（在[StoreConfig](arkts-apis-data-relationalstore-i.md#storeconfig)中配置vector为true）使用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| destName | string | 是 | 指定数据库的备份文件名。 |
| callback | AsyncCallback<void> | 是 | 指定callback回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800010 | Failed to open or delete the database by an invalid database path. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**示例：**

```
1. if (store != undefined) {
2. (store as relationalStore.RdbStore).backup("dbBackup.db", (err) => {
3. if (err) {
4. console.error(`Backup failed, code is ${err.code},message is ${err.message}`);
5. return;
6. }
7. console.info('Backup success.');
8. });
9. }
```

## backup

PhonePC/2in1TabletTVWearable

backup(destName:string): Promise<void>

以指定名称备份数据库，使用Promise异步回调。

该接口支持向量数据库（在[StoreConfig](arkts-apis-data-relationalstore-i.md#storeconfig)中配置vector为true）使用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| destName | string | 是 | 指定数据库的备份文件名。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. if (store != undefined) {
4. let promiseBackup = (store as relationalStore.RdbStore).backup("dbBackup.db");
5. promiseBackup.then(() => {
6. console.info('Backup success.');
7. }).catch((err: BusinessError) => {
8. console.error(`Backup failed, code is ${err.code},message is ${err.message}`);
9. });
10. }
```

## restore

PhonePC/2in1TabletTVWearable

restore(srcName:string, callback: AsyncCallback<void>):void

从指定的数据库备份文件恢复数据库，使用callback异步回调。

该接口支持向量数据库（在[StoreConfig](arkts-apis-data-relationalstore-i.md#storeconfig)中配置vector为true）使用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| srcName | string | 是 | 指定数据库的备份文件名。 |
| callback | AsyncCallback<void> | 是 | 指定callback回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**示例：**

```
1. if (store != undefined) {
2. (store as relationalStore.RdbStore).restore("dbBackup.db", (err) => {
3. if (err) {
4. console.error(`Restore failed, code is ${err.code},message is ${err.message}`);
5. return;
6. }
7. console.info('Restore success.');
8. });
9. }
```

## restore

PhonePC/2in1TabletTVWearable

restore(srcName:string): Promise<void>

从指定的数据库备份文件恢复数据库，使用Promise异步回调。

该接口支持向量数据库（在[StoreConfig](arkts-apis-data-relationalstore-i.md#storeconfig)中配置vector为true）使用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| srcName | string | 是 | 指定数据库的备份文件名。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. if (store != undefined) {
4. let promiseRestore = (store as relationalStore.RdbStore).restore("dbBackup.db");
5. promiseRestore.then(() => {
6. console.info('Restore success.');
7. }).catch((err: BusinessError) => {
8. console.error(`Restore failed, code is ${err.code},message is ${err.message}`);
9. });
10. }
```

## setDistributedTables

PhonePC/2in1TabletTVWearable

setDistributedTables(tables: Array<string>, callback: AsyncCallback<void>): void

设置分布式数据库表，使用callback异步回调。

**需要权限：** ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tables | Array<string> | 是 | 要设置的分布式数据库的表名。 |
| callback | AsyncCallback<void> | 是 | 指定callback回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |

**示例：**

```
1. if (store != undefined) {
2. (store as relationalStore.RdbStore).setDistributedTables(["EMPLOYEE"], (err) => {
3. if (err) {
4. console.error(`SetDistributedTables failed, code is ${err.code},message is ${err.message}`);
5. return;
6. }
7. console.info('SetDistributedTables successfully.');
8. });
9. }
```

## setDistributedTables

PhonePC/2in1TabletTVWearable

setDistributedTables(tables: Array<string>): Promise<void>

设置分布式数据库表，使用Promise异步回调。

**需要权限：** ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tables | Array<string> | 是 | 要设置的分布式数据库的表名。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. if (store != undefined) {
4. (store as relationalStore.RdbStore).setDistributedTables(["EMPLOYEE"]).then(() => {
5. console.info('SetDistributedTables successfully.');
6. }).catch((err: BusinessError) => {
7. console.error(`SetDistributedTables failed, code is ${err.code},message is ${err.message}`);
8. });
9. }
```

## setDistributedTables10+

PhonePC/2in1TabletTVWearable

setDistributedTables(tables: Array<string>, type: DistributedType, callback: AsyncCallback<void>): void

设置分布式数据库表，支持指定表的分布式类型，使用callback异步回调。

**需要权限：** ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tables | Array<string> | 是 | 要设置的分布式数据库的表名。 |
| type | [DistributedType](arkts-apis-data-relationalstore-e.md#distributedtype10) | 是 | 表的分布式类型。 |
| callback | AsyncCallback<void> | 是 | 指定callback回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |
| 14800051 | The type of the distributed table does not match. |

**示例：**

```
1. if (store != undefined) {
2. (store as relationalStore.RdbStore).setDistributedTables(["EMPLOYEE"], relationalStore.DistributedType.DISTRIBUTED_CLOUD, (err) => {
3. if (err) {
4. console.error(`SetDistributedTables failed, code is ${err.code},message is ${err.message}`);
5. return;
6. }
7. console.info('SetDistributedTables successfully.');
8. });
9. }
```

## setDistributedTables10+

PhonePC/2in1TabletTVWearable

setDistributedTables(tables: Array<string>, type: DistributedType, config: DistributedConfig, callback: AsyncCallback<void>): void

设置分布式数据库表，支持指定表的分布式类型和表的分布式配置信息，使用callback异步回调。

**需要权限：** ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tables | Array<string> | 是 | 要设置的分布式数据库的表名。 |
| type | [DistributedType](arkts-apis-data-relationalstore-e.md#distributedtype10) | 是 | 表的分布式类型。 |
| config | [DistributedConfig](arkts-apis-data-relationalstore-i.md#distributedconfig10) | 是 | 表的分布式配置信息。 |
| callback | AsyncCallback<void> | 是 | 指定callback回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |
| 14800051 | The type of the distributed table does not match. |

**示例：**

```
1. if (store != undefined) {
2. (store as relationalStore.RdbStore).setDistributedTables(["EMPLOYEE"], relationalStore.DistributedType.DISTRIBUTED_CLOUD, {
3. autoSync: true
4. }, (err) => {
5. if (err) {
6. console.error(`SetDistributedTables failed, code is ${err.code},message is ${err.message}`);
7. return;
8. }
9. console.info('SetDistributedTables successfully.');
10. });
11. }
```

## setDistributedTables10+

PhonePC/2in1TabletTVWearable

setDistributedTables(tables: Array<string>, type?: DistributedType, config?: DistributedConfig): Promise<void>

设置分布式数据库表，支持指定表的分布式类型和表的分布式配置信息，使用Promise异步回调。

**需要权限：** ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tables | Array<string> | 是 | 要设置的分布式数据库的表名。 |
| type | [DistributedType](arkts-apis-data-relationalstore-e.md#distributedtype10) | 否 | 表的分布式类型。默认值是relationalStore.DistributedType.DISTRIBUTED\_DEVICE。 |
| config | [DistributedConfig](arkts-apis-data-relationalstore-i.md#distributedconfig10) | 否 | 表的分布式配置信息。不传入时默认autoSync为false，需要调用[cloudSync](arkts-apis-data-relationalstore-rdbstore.md#cloudsync10-3)接口触发端云同步。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |
| 14800051 | The type of the distributed table does not match. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. if (store != undefined) {
4. (store as relationalStore.RdbStore).setDistributedTables(["EMPLOYEE"], relationalStore.DistributedType.DISTRIBUTED_CLOUD, {
5. autoSync: true
6. }).then(() => {
7. console.info('SetDistributedTables successfully.');
8. }).catch((err: BusinessError) => {
9. console.error(`SetDistributedTables failed, code is ${err.code},message is ${err.message}`);
10. });
11. }
```

## obtainDistributedTableName

PhonePC/2in1TabletTVWearable

obtainDistributedTableName(device: string, table: string, callback: AsyncCallback<string>): void

根据远程设备的本地表名获取指定远程设备的分布式表名。在查询远程设备数据库时，需要使用分布式表名，使用callback异步回调。

说明

其中device通过调用[deviceManager.getAvailableDeviceListSync](js-apis-distributeddevicemanager.md#getavailabledevicelistsync)方法得到。

**需要权限：** ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| device | string | 是 | 远程设备ID 。 |
| table | string | 是 | 远程设备的本地表名。 |
| callback | AsyncCallback<string> | 是 | 指定的callback回调函数。如果操作成功，返回远程设备的分布式表名。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |

**示例：**

```
1. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let dmInstance: distributedDeviceManager.DeviceManager;
5. let deviceId: string | undefined = undefined;

7. try {
8. dmInstance = distributedDeviceManager.createDeviceManager("com.example.appdatamgrverify");
9. let devices = dmInstance.getAvailableDeviceListSync();
10. if (!devices || devices.length === 0) {
11. console.error("No available devices found");
12. } else {
13. deviceId = devices[0].networkId;
14. }
15. } catch (err) {
16. let code = (err as BusinessError).code;
17. let message = (err as BusinessError).message;
18. console.error("createDeviceManager errCode:" + code + ",errMessage:" + message);
19. }

21. if (store != undefined && deviceId != undefined) {
22. (store as relationalStore.RdbStore).obtainDistributedTableName(deviceId, "EMPLOYEE", (err, tableName) => {
23. if (err) {
24. console.error(`ObtainDistributedTableName failed, code is ${err.code},message is ${err.message}`);
25. return;
26. }
27. console.info(`ObtainDistributedTableName successfully, tableName= ${tableName}`);
28. });
29. }
```

## obtainDistributedTableName

PhonePC/2in1TabletTVWearable

obtainDistributedTableName(device: string, table: string): Promise<string>

根据远程设备的本地表名获取指定远程设备的分布式表名。在查询远程设备数据库时，需要使用分布式表名，使用Promise异步回调。

说明

其中device通过调用[deviceManager.getAvailableDeviceListSync](js-apis-distributeddevicemanager.md#getavailabledevicelistsync)方法得到。

**需要权限：** ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| device | string | 是 | 远程设备ID。 |
| table | string | 是 | 远程设备的本地表名。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象。如果操作成功，返回远程设备的分布式表名。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |

**示例：**

```
1. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let dmInstance: distributedDeviceManager.DeviceManager;
5. let deviceId: string | undefined = undefined;

7. try {
8. dmInstance = distributedDeviceManager.createDeviceManager("com.example.appdatamgrverify");
9. let devices = dmInstance.getAvailableDeviceListSync();
10. if (!devices || devices.length === 0) {
11. console.error("No available devices found");
12. } else {
13. deviceId = devices[0].networkId;
14. }
15. } catch (err) {
16. let code = (err as BusinessError).code;
17. let message = (err as BusinessError).message;
18. console.error("createDeviceManager errCode:" + code + ",errMessage:" + message);
19. }

21. if (store != undefined && deviceId != undefined) {
22. (store as relationalStore.RdbStore).obtainDistributedTableName(deviceId, "EMPLOYEE").then((tableName: string) => {
23. console.info(`ObtainDistributedTableName successfully, tableName= ${tableName}`);
24. }).catch((err: BusinessError) => {
25. console.error(`ObtainDistributedTableName failed, code is ${err.code},message is ${err.message}`);
26. });
27. }
```

## sync

PhonePC/2in1TabletTVWearable

sync(mode: SyncMode, predicates: RdbPredicates, callback: AsyncCallback<Array<[string, number]>>): void

在设备之间同步数据，使用callback异步回调。

**需要权限：** ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [SyncMode](arkts-apis-data-relationalstore-e.md#syncmode) | 是 | 指同步模式。该值可以是relationalStore.SyncMode.SYNC\_MODE\_PUSH、relationalStore.SyncMode.SYNC\_MODE\_PULL。 |
| predicates | [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 是 | 约束同步数据和设备。 |
| callback | AsyncCallback<Array<[string, number]>> | 是 | 指定的callback回调函数，用于向调用者发送同步结果。string：设备ID；number：每个设备同步状态，0表示成功，1表示失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |

**示例：**

```
1. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let dmInstance: distributedDeviceManager.DeviceManager;
5. let deviceIds: Array<string> = [];

7. try {
8. dmInstance = distributedDeviceManager.createDeviceManager("com.example.appdatamgrverify");
9. let devices: Array<distributedDeviceManager.DeviceBasicInfo> = dmInstance.getAvailableDeviceListSync();
10. for (let i = 0; i < devices.length; i++) {
11. deviceIds[i] = devices[i].networkId!;
12. }
13. } catch (err) {
14. let code = (err as BusinessError).code;
15. let message = (err as BusinessError).message;
16. console.error("createDeviceManager errCode:" + code + ",errMessage:" + message);
17. }

19. let predicates = new relationalStore.RdbPredicates('EMPLOYEE');
20. predicates.inDevices(deviceIds);
21. if (store != undefined) {
22. (store as relationalStore.RdbStore).sync(relationalStore.SyncMode.SYNC_MODE_PUSH, predicates, (err, result) => {
23. if (err) {
24. console.error(`Sync failed, code is ${err.code},message is ${err.message}`);
25. return;
26. }
27. console.info('Sync done.');
28. for (let i = 0; i < result.length; i++) {
29. console.info(`device= ${result[i][0]}, status= ${result[i][1]}`);
30. }
31. });
32. }
```

## sync

PhonePC/2in1TabletTVWearable

sync(mode: SyncMode, predicates: RdbPredicates): Promise<Array<[string, number]>>

在设备之间同步数据，使用Promise异步回调。

**需要权限：** ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [SyncMode](arkts-apis-data-relationalstore-e.md#syncmode) | 是 | 指同步模式。该值可以是relationalStore.SyncMode.SYNC\_MODE\_PUSH、relationalStore.SyncMode.SYNC\_MODE\_PULL。 |
| predicates | [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 是 | 约束同步数据和设备。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[string, number]>> | Promise对象，用于向调用者发送同步结果。string：设备ID；number：每个设备同步状态，0表示成功，1表示失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |

**示例：**

```
1. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let dmInstance: distributedDeviceManager.DeviceManager;
5. let deviceIds: Array<string> = [];

7. try {
8. dmInstance = distributedDeviceManager.createDeviceManager("com.example.appdatamgrverify");
9. let devices: Array<distributedDeviceManager.DeviceBasicInfo> = dmInstance.getAvailableDeviceListSync();
10. for (let i = 0; i < devices.length; i++) {
11. deviceIds[i] = devices[i].networkId!;
12. }
13. } catch (err) {
14. let code = (err as BusinessError).code;
15. let message = (err as BusinessError).message;
16. console.error("createDeviceManager errCode:" + code + ",errMessage:" + message);
17. }

19. let predicates = new relationalStore.RdbPredicates('EMPLOYEE');
20. predicates.inDevices(deviceIds);
21. if (store != undefined) {
22. (store as relationalStore.RdbStore).sync(relationalStore.SyncMode.SYNC_MODE_PUSH, predicates).then((result: Object[][]) => {
23. console.info('Sync done.');
24. for (let i = 0; i < result.length; i++) {
25. console.info(`device= ${result[i][0]}, status= ${result[i][1]}`);
26. }
27. }).catch((err: BusinessError) => {
28. console.error(`Sync failed, code is ${err.code},message is ${err.message}`);
29. });
30. }
```

## cloudSync10+

PhonePC/2in1TabletTV

cloudSync(mode: SyncMode, progress: Callback<ProgressDetails>, callback: AsyncCallback<void>): void

手动执行对所有分布式表的端云同步，使用callback异步回调。使用该接口需要实现[端云服务](js-apis-data-clouddata.md)功能。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [SyncMode](arkts-apis-data-relationalstore-e.md#syncmode) | 是 | 表示数据库的同步模式。 |
| progress | Callback<[ProgressDetails](arkts-apis-data-relationalstore-i.md#progressdetails10)> | 是 | 用来处理数据库同步详细信息的回调函数。 |
| callback | AsyncCallback<void> | 是 | 指定的callback回调函数，用于向调用者发送同步结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Need 2 - 4 parameter(s). 2. The RdbStore must be not nullptr. 3. The mode must be a SyncMode of cloud. 4. The progress must be a callback type. 5. The callback must be a function. |
| 801 | Capability not supported. |
| 14800014 | The target instance is already closed. |

**示例：**

```
1. if (store != undefined) {
2. (store as relationalStore.RdbStore).cloudSync(relationalStore.SyncMode.SYNC_MODE_CLOUD_FIRST, (progressDetails) => {
3. console.info(`Progress: ${progressDetails}`);
4. }, (err) => {
5. if (err) {
6. console.error(`Cloud sync failed, code is ${err.code},message is ${err.message}`);
7. return;
8. }
9. console.info('Cloud sync succeeded');
10. });
11. }
```

## cloudSync10+

PhonePC/2in1TabletTV

cloudSync(mode: SyncMode, progress: Callback<ProgressDetails>): Promise<void>

手动执行对所有分布式表的端云同步，使用Promise异步回调。使用该接口需要实现[端云服务](js-apis-data-clouddata.md)功能。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [SyncMode](arkts-apis-data-relationalstore-e.md#syncmode) | 是 | 表示数据库的同步模式。 |
| progress | Callback<[ProgressDetails](arkts-apis-data-relationalstore-i.md#progressdetails10)> | 是 | 用来处理数据库同步详细信息的回调函数。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，用于向调用者发送同步结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Need 2 - 4 parameter(s). 2. The RdbStore must be not nullptr. 3. The mode must be a SyncMode of cloud. 4. The progress must be a callback type. |
| 801 | Capability not supported. |
| 14800014 | The target instance is already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. if (store != undefined) {
4. (store as relationalStore.RdbStore).cloudSync(relationalStore.SyncMode.SYNC_MODE_CLOUD_FIRST, (progressDetail: relationalStore.ProgressDetails) => {
5. console.info(`progress: ${progressDetail}`);
6. }).then(() => {
7. console.info('Cloud sync succeeded');
8. }).catch((err: BusinessError) => {
9. console.error(`cloudSync failed, code is ${err.code},message is ${err.message}`);
10. });
11. }
```

## cloudSync10+

PhonePC/2in1TabletTV

cloudSync(mode: SyncMode, tables: string[], progress: Callback<ProgressDetails>, callback: AsyncCallback<void>): void

手动执行对指定表的端云同步，使用callback异步回调。使用该接口需要实现[端云服务](js-apis-data-clouddata.md)功能。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [SyncMode](arkts-apis-data-relationalstore-e.md#syncmode) | 是 | 表示数据库的同步模式。 |
| tables | string[] | 是 | 指定同步的表名。 |
| progress | Callback<[ProgressDetails](arkts-apis-data-relationalstore-i.md#progressdetails10)> | 是 | 用来处理数据库同步详细信息的回调函数。 |
| callback | AsyncCallback<void> | 是 | 指定的callback回调函数，用于向调用者发送同步结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Need 2 - 4 parameter(s). 2. The RdbStore must be not nullptr. 3. The mode must be a SyncMode of cloud. 4. The tablesNames must be not empty. 5. The progress must be a callback type. 6.The callback must be a function. |
| 801 | Capability not supported. |
| 14800014 | The target instance is already closed. |

**示例：**

```
1. const tables = ["table1", "table2"];

3. if (store != undefined) {
4. (store as relationalStore.RdbStore).cloudSync(relationalStore.SyncMode.SYNC_MODE_CLOUD_FIRST, tables, (progressDetail: relationalStore.ProgressDetails) => {
5. console.info(`Progress: ${progressDetail}`);
6. }, (err) => {
7. if (err) {
8. console.error(`Cloud sync failed, code is ${err.code},message is ${err.message}`);
9. return;
10. }
11. console.info('Cloud sync succeeded');
12. });
13. };
```

## cloudSync10+

PhonePC/2in1TabletTV

cloudSync(mode: SyncMode, tables: string[], progress: Callback<ProgressDetails>): Promise<void>

手动执行对指定表的端云同步，使用Promise异步回调。使用该接口需要实现[端云服务](js-apis-data-clouddata.md)功能。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [SyncMode](arkts-apis-data-relationalstore-e.md#syncmode) | 是 | 表示数据库的同步模式。 |
| tables | string[] | 是 | 指定同步的表名。 |
| progress | Callback<[ProgressDetails](arkts-apis-data-relationalstore-i.md#progressdetails10)> | 是 | 用来处理数据库同步详细信息的回调函数。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，用于向调用者发送同步结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Need 2 - 4 parameter(s). 2. The RdbStore must be not nullptr. 3. The mode must be a SyncMode of cloud. 4. The tablesNames must be not empty. 5. The progress must be a callback type |
| 801 | Capability not supported. |
| 14800014 | The target instance is already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const tables = ["table1", "table2"];

5. if (store != undefined) {
6. (store as relationalStore.RdbStore).cloudSync(relationalStore.SyncMode.SYNC_MODE_CLOUD_FIRST, tables, (progressDetail: relationalStore.ProgressDetails) => {
7. console.info(`progress: ${progressDetail}`);
8. }).then(() => {
9. console.info('Cloud sync succeeded');
10. }).catch((err: BusinessError) => {
11. console.error(`cloudSync failed, code is ${err.code},message is ${err.message}`);
12. });
13. };
```

## on('dataChange')

PhonePC/2in1TabletTVWearable

on(event: 'dataChange', type: SubscribeType, observer: Callback<Array<string>>): void

注册数据库的数据变更的事件监听。当分布式数据库中的数据发生更改时，将调用回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取值为'dataChange'，表示数据更改。 |
| type | [SubscribeType](arkts-apis-data-relationalstore-e.md#subscribetype) | 是 | 订阅类型。 |
| observer | Callback<Array<string>> | 是 | 指分布式数据库中数据更改事件的观察者。Array<string>为数据库中的数据发生改变的对端设备ID。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800014 | The target instance is already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let storeObserver = (devices: Array<string>) => {
4. if (devices !== undefined) {
5. for (let i = 0; i < devices.length; i++) {
6. console.info(`device= ${devices[i]} data changed`);
7. }
8. }
9. };

11. try {
12. if (store != undefined) {
13. (store as relationalStore.RdbStore).on('dataChange', relationalStore.SubscribeType.SUBSCRIBE_TYPE_REMOTE, storeObserver);
14. }
15. } catch (err) {
16. let code = (err as BusinessError).code;
17. let message = (err as BusinessError).message;
18. console.error(`Register observer failed, code is ${code},message is ${message}`);
19. }
```

## on('dataChange')10+

PhonePC/2in1TabletTVWearable

on(event: 'dataChange', type: SubscribeType, observer: Callback<Array<string>>| Callback<Array<ChangeInfo>>): void

注册数据库的数据变更的事件监听。当分布式数据库或本地数据库中的数据发生更改时，将调用回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取值为'dataChange'，表示数据更改。 |
| type | [SubscribeType](arkts-apis-data-relationalstore-e.md#subscribetype) | 是 | 订阅类型。 |
| observer | Callback<Array<string>> | Callback<Array<[ChangeInfo](arkts-apis-data-relationalstore-i.md#changeinfo10)>> | 是 | 回调函数。  当type为SUBSCRIBE\_TYPE\_REMOTE，observer类型需为Callback<Array<string>>，其中Array<string>为数据库中的数据发生改变的对端设备ID。  当type为SUBSCRIBE\_TYPE\_CLOUD，observer类型需为Callback<Array<string>>，其中Array<string>为数据库中的数据发生改变的云端账号。  当type为SUBSCRIBE\_TYPE\_CLOUD\_DETAILS，observer类型需为Callback<Array<ChangeInfo>>，其中Array<ChangeInfo>为数据库端云同步过程的详情。  当type为SUBSCRIBE\_TYPE\_LOCAL\_DETAILS，observer类型需为Callback<Array<ChangeInfo>>，其中Array<ChangeInfo>为本地数据库中的数据更改的详情。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 202 | Permission verification failed, application which is not a system application uses system API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800014 | The target instance is already closed. |

**示例1：type为SUBSCRIBE\_TYPE\_REMOTE**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let storeObserver = (devices: Array<string>) => {
4. if (devices !== undefined) {
5. for (let i = 0; i < devices.length; i++) {
6. console.info(`device= ${devices[i]} data changed`);
7. }
8. }
9. };

11. try {
12. if (store != undefined) {
13. (store as relationalStore.RdbStore).on('dataChange', relationalStore.SubscribeType.SUBSCRIBE_TYPE_REMOTE, storeObserver);
14. }
15. } catch (err) {
16. let code = (err as BusinessError).code;
17. let message = (err as BusinessError).message;
18. console.error(`Register observer failed, code is ${code},message is ${message}`);
19. }
```

**示例2：type为SUBSCRIBE\_TYPE\_LOCAL\_DETAILS**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let changeInfos = (changeInfos: Array<relationalStore.ChangeInfo>) => {
4. for (let i = 0; i < changeInfos.length; i++) {
5. console.info(`changeInfos = ${JSON.stringify(changeInfos[i])}`);
6. }
7. };

9. try {
10. if (store != undefined) {
11. (store as relationalStore.RdbStore).on('dataChange', relationalStore.SubscribeType.SUBSCRIBE_TYPE_LOCAL_DETAILS, changeInfos);
12. }
13. } catch (err) {
14. let code = (err as BusinessError).code;
15. let message = (err as BusinessError).message;
16. console.error(`on dataChange fail, code is ${code},message is ${message}`);
17. }

19. let value1 = "Lisa";
20. let value2 = 18;
21. let value3 = 100.5;
22. let value4 = new Uint8Array([1, 2, 3]);

24. try {
25. const valueBucket: relationalStore.ValuesBucket = {
26. 'name': value1,
27. 'age': value2,
28. 'salary': value3,
29. 'blobType': value4
30. };

32. if (store != undefined) {
33. (store as relationalStore.RdbStore).insert('test', valueBucket);
34. }
35. } catch (err) {
36. let code = (err as BusinessError).code;
37. let message = (err as BusinessError).message;
38. console.error(`insert fail, code is ${code},message is ${message}`);
39. }
```

## on10+

PhonePC/2in1TabletTVWearable

on(event: string, interProcess: boolean, observer: Callback<void>): void

注册数据库的进程内或者进程间事件监听。当调用[emit](arkts-apis-data-relationalstore-rdbstore.md#emit10)接口时，将调用回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 订阅事件名称，与emit接口触发事件时的名称一致。 |
| interProcess | boolean | 是 | 指定是进程间还是本进程订阅。  true：进程间。  false：本进程。 |
| observer | Callback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |
| 14800050 | Failed to obtain the subscription service. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let storeObserver = () => {
4. console.info(`storeObserver`);
5. };

7. try {
8. if (store != undefined) {
9. (store as relationalStore.RdbStore).on('storeObserver', false, storeObserver);
10. }
11. } catch (err) {
12. let code = (err as BusinessError).code;
13. let message = (err as BusinessError).message;
14. console.error(`Register observer failed, code is ${code},message is ${message}`);
15. }
```

## on('autoSyncProgress')11+

PhonePC/2in1TabletTVWearable

on(event: 'autoSyncProgress', progress: Callback<ProgressDetails>): void

在已打开端云同步，并且网络状态正常的条件下，注册自动同步进度通知，自动同步进行时调用回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取值为'autoSyncProgress'，表示自动同步进度通知。 |
| progress | Callback<[ProgressDetails](arkts-apis-data-relationalstore-i.md#progressdetails10)> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. 4. The event must be a not empty string. 5. The progress must be function. |
| 801 | Capability not supported. |
| 14800014 | The target instance is already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let progressDetail = (progressDetail: relationalStore.ProgressDetails) => {
4. console.info(`progress: ${progressDetail}`);
5. };

7. try {
8. if (store != undefined) {
9. (store as relationalStore.RdbStore).on('autoSyncProgress', progressDetail);
10. }
11. } catch (err) {
12. let code = (err as BusinessError).code;
13. let message = (err as BusinessError).message;
14. console.error(`Register observer failed, code is ${code},message is ${message}`);
15. }
```

## on('statistics')12+

PhonePC/2in1TabletTVWearable

on(event: 'statistics', observer: Callback<SqlExecutionInfo>): void

订阅SQL统计信息。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 订阅事件名称，取值为'statistics'，表示sql执行时间的统计。 |
| observer | Callback<[SqlExecutionInfo](arkts-apis-data-relationalstore-i.md#sqlexecutioninfo12)> | 是 | 回调函数。用于返回数据库中SQL执行时间的统计信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let sqlExecutionInfo = (sqlExecutionInfo: relationalStore.SqlExecutionInfo) => {
4. if (sqlExecutionInfo.sql.length > 0) {
5. console.info(`sql: ${sqlExecutionInfo.sql[0]}`);
6. console.info(`totalTime: ${sqlExecutionInfo.totalTime}`);
7. console.info(`waitTime: ${sqlExecutionInfo.waitTime}`);
8. console.info(`prepareTime: ${sqlExecutionInfo.prepareTime}`);
9. console.info(`executeTime: ${sqlExecutionInfo.executeTime}`);
10. }
11. };

13. try {
14. if (store != undefined) {
15. (store as relationalStore.RdbStore).on('statistics', sqlExecutionInfo);
16. }
17. } catch (err) {
18. let code = (err as BusinessError).code;
19. let message = (err as BusinessError).message;
20. console.error(`Register observer failed, code is ${code},message is ${message}`);
21. }

23. try {
24. let value1 = "Lisa";
25. let value2 = 18;
26. let value3 = 100.5;
27. let value4 = new Uint8Array([1, 2, 3, 4, 5]);

29. const valueBucket: relationalStore.ValuesBucket = {
30. 'NAME': value1,
31. 'AGE': value2,
32. 'SALARY': value3,
33. 'CODES': value4
34. };
35. if (store != undefined) {
36. (store as relationalStore.RdbStore).insert('test', valueBucket);
37. }
38. } catch (err) {
39. console.error(`insert fail, code:${err.code}, message: ${err.message}`);
40. }
```

## on('sqliteErrorOccurred')20+

PhonePC/2in1TabletTVWearable

on(event: 'sqliteErrorOccurred', observer: Callback<ExceptionMessage>): void

记录执行SQL语句时的异常日志。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 订阅事件名称，取值为'sqliteErrorOccurred'，记录SQL语句执行过程中的错误信息。 |
| observer | Callback<[ExceptionMessage](arkts-apis-data-relationalstore-i.md#exceptionmessage20)> | 是 | 回调函数。用于返回SQL执行时出现的异常信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 801 | Capability not supported. |
| 14800014 | The target instance is already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. if (store != undefined) {
5. store.on('sqliteErrorOccurred', exceptionMessage => {
6. let sqliteCode = exceptionMessage.code;
7. let sqliteMessage = exceptionMessage.message;
8. let errSQL = exceptionMessage.sql;
9. console.error(`error log is ${sqliteCode}, errMessage is ${sqliteMessage}, errSQL is ${errSQL}`);
10. })
11. }
12. } catch (err) {
13. let code = (err as BusinessError).code;
14. let message = (err as BusinessError).message;
15. console.error(`Register observer failed, code is ${code},message is ${message}`);
16. }
17. const CREATE_TABLE_TEST = "CREATE TABLE IF NOT EXISTS test (" + "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
18. "name TEXT NOT NULL, " + "age INTEGER, " + "salary REAL)";
19. try {
20. let value = new Uint8Array([1, 2, 3, 4, 5]);
21. const valueBucket: relationalStore.ValuesBucket = {
22. 'name': "Lisa",
23. 'age': 18,
24. 'salary': 100.5,
25. 'codes': value,
26. };
27. if (store != undefined) {
28. await (store as relationalStore.RdbStore).executeSql(CREATE_TABLE_TEST);
29. await (store as relationalStore.RdbStore).insert('test', valueBucket);
30. }
31. } catch (err) {
32. console.error(`Insert fail, code:${err.code}, message: ${err.message}`);
33. }
```

## on('perfStat')20+

PhonePC/2in1TabletTVWearable

on(event: 'perfStat', observer: Callback<SqlExecutionInfo>): void

订阅SQL统计信息。使用[createTransaction](arkts-apis-data-relationalstore-rdbstore.md#createtransaction14)创建的事务进行相关操作（[Transaction](arkts-apis-data-relationalstore-transaction.md)），只会在事务结束（COMMIT/ROLLBACK）时通知一次统计信息。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 订阅事件名称，取值为'perfStat'，统计执行SQL的时间。 |
| observer | Callback<[SqlExecutionInfo](arkts-apis-data-relationalstore-i.md#sqlexecutioninfo12)> | 是 | 回调函数。用于返回数据库执行SQL的时间。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 801 | Capability not supported. |
| 14800014 | The target instance is already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let sqlExecutionInfo = (sqlExecutionInfo: relationalStore.SqlExecutionInfo) => {
4. if (sqlExecutionInfo.sql.length > 0) {
5. console.info(`sql: ${sqlExecutionInfo.sql[0]}`);
6. console.info(`totalTime: ${sqlExecutionInfo.totalTime}`);
7. console.info(`waitTime: ${sqlExecutionInfo.waitTime}`);
8. console.info(`prepareTime: ${sqlExecutionInfo.prepareTime}`);
9. console.info(`executeTime: ${sqlExecutionInfo.executeTime}`);
10. }
11. };

13. try {
14. if (store != undefined) {
15. (store as relationalStore.RdbStore).on('perfStat', sqlExecutionInfo);
16. }
17. } catch (err) {
18. let code = (err as BusinessError).code;
19. let message = (err as BusinessError).message;
20. console.error(`Register observer failed, code is ${code},message is ${message}`);
21. }

23. try {
24. let value1 = "Lisa";
25. let value2 = 18;
26. let value3 = 100.5;
27. let value4 = new Uint8Array([1, 2, 3, 4, 5]);

29. const valueBucket: relationalStore.ValuesBucket = {
30. 'NAME': value1,
31. 'AGE': value2,
32. 'SALARY': value3,
33. 'CODES': value4
34. };
35. if (store != undefined) {
36. const rowId = await store.insert('EMPLOYEE', valueBucket);
37. console.info(`Insert success, rowId is: ${rowId}`);
38. }
39. } catch (err) {
40. console.error(`insert fail, code:${err.code}, message: ${err.message}`);
41. }
```

## off('dataChange')

PhonePC/2in1TabletTVWearable

off(event:'dataChange', type: SubscribeType, observer: Callback<Array<string>>): void

取消数据变更的事件监听。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取值为'dataChange'，表示数据更改。 |
| type | [SubscribeType](arkts-apis-data-relationalstore-e.md#subscribetype) | 是 | 订阅类型。 |
| observer | Callback<Array<string>> | 是 | 指已注册的数据更改观察者。Array<string>为数据库中的数据发生改变的对端设备ID。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800014 | The target instance is already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let storeObserver = (devices: Array<string>) => {
4. if (devices !== undefined) {
5. for (let i = 0; i < devices.length; i++) {
6. console.info(`device= ${devices[i]} data changed`);
7. }
8. }
9. };

11. try {
12. if (store != undefined) {
13. // 此处不能使用Lambda表达式
14. (store as relationalStore.RdbStore).on('dataChange', relationalStore.SubscribeType.SUBSCRIBE_TYPE_REMOTE, storeObserver);
15. }
16. } catch (err) {
17. let code = (err as BusinessError).code;
18. let message = (err as BusinessError).message;
19. console.error(`Register observer failed, code is ${code},message is ${message}`);
20. }

22. try {
23. if (store != undefined) {
24. (store as relationalStore.RdbStore).off('dataChange', relationalStore.SubscribeType.SUBSCRIBE_TYPE_REMOTE, storeObserver);
25. }
26. } catch (err) {
27. let code = (err as BusinessError).code;
28. let message = (err as BusinessError).message;
29. console.error(`Unregister observer failed, code is ${code},message is ${message}`);
30. }
```

## off('dataChange')10+

PhonePC/2in1TabletTVWearable

off(event:'dataChange', type: SubscribeType, observer?: Callback<Array<string>>| Callback<Array<ChangeInfo>>): void

取消数据变更的事件监听。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取值为'dataChange'，表示数据更改。 |
| type | [SubscribeType](arkts-apis-data-relationalstore-e.md#subscribetype) | 是 | 订阅类型。 |
| observer | Callback<Array<string>>| Callback<Array<[ChangeInfo](arkts-apis-data-relationalstore-i.md#changeinfo10)>> | 否 | 回调函数。  当type为SUBSCRIBE\_TYPE\_REMOTE，observer类型需为Callback<Array<string>>，其中Array<string>为数据库中的数据发生改变的对端设备ID。  当type为SUBSCRIBE\_TYPE\_CLOUD，observer类型需为Callback<Array<string>>，其中Array<string>为数据库中的数据发生改变的云端账号。  当type为SUBSCRIBE\_TYPE\_CLOUD\_DETAILS，observer类型需为Callback<Array<ChangeInfo>>，其中Array<ChangeInfo>为数据库端云同步过程的详情。  当type为SUBSCRIBE\_TYPE\_LOCAL\_DETAILS，observer类型需为Callback<Array<ChangeInfo>>，其中Array<ChangeInfo>为本地数据库中的数据更改的详情。  当observer没有传入时，表示取消当前type类型下所有数据变更的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 202 | Permission verification failed, application which is not a system application uses system API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800014 | The target instance is already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let storeObserver = (devices: Array<string>) => {
4. if (devices !== undefined) {
5. for (let i = 0; i < devices.length; i++) {
6. console.info(`device= ${devices[i]} data changed`);
7. }
8. }
9. };

11. try {
12. if (store != undefined) {
13. (store as relationalStore.RdbStore).on('dataChange', relationalStore.SubscribeType.SUBSCRIBE_TYPE_REMOTE, storeObserver);
14. }
15. } catch (err) {
16. let code = (err as BusinessError).code;
17. let message = (err as BusinessError).message;
18. console.error(`Register observer failed, code is ${code},message is ${message}`);
19. }

21. try {
22. if (store != undefined) {
23. (store as relationalStore.RdbStore).off('dataChange', relationalStore.SubscribeType.SUBSCRIBE_TYPE_REMOTE, storeObserver);
24. }
25. } catch (err) {
26. let code = (err as BusinessError).code;
27. let message = (err as BusinessError).message;
28. console.error(`Unregister observer failed, code is ${code},message is ${message}`);
29. }
```

## off10+

PhonePC/2in1TabletTVWearable

off(event: string, interProcess: boolean, observer?: Callback<void>): void

取消数据库的进程内或者进程间事件监听。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取消订阅事件名称。事件名称与on接口调用时订阅事件的名称一致。 |
| interProcess | boolean | 是 | 指定是进程间还是本进程取消订阅。  true：进程间。  false：本进程。 |
| observer | Callback<void> | 否 | 该参数存在，则取消指定Callback监听回调，否则取消该event事件的所有监听回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |
| 14800050 | Failed to obtain the subscription service. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let storeObserver = () => {
4. console.info(`storeObserver`);
5. };

7. try {
8. if (store != undefined) {
9. (store as relationalStore.RdbStore).on('storeObserver', false, storeObserver);
10. }
11. } catch (err) {
12. let code = (err as BusinessError).code;
13. let message = (err as BusinessError).message;
14. console.error(`Register observer failed, code is ${code},message is ${message}`);
15. }

17. try {
18. if (store != undefined) {
19. (store as relationalStore.RdbStore).off('storeObserver', false, storeObserver);
20. }
21. } catch (err) {
22. let code = (err as BusinessError).code;
23. let message = (err as BusinessError).message;
24. console.error(`Unregister observer failed, code is ${code},message is ${message}`);
25. }
```

## off('autoSyncProgress')11+

PhonePC/2in1TabletTVWearable

off(event: 'autoSyncProgress', progress?: Callback<ProgressDetails>): void

取消订阅自动同步进度的通知。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取值为'autoSyncProgress'，表示自动同步进度通知。 |
| progress | Callback<[ProgressDetails](arkts-apis-data-relationalstore-i.md#progressdetails10)> | 否 | 指已注册的自动同步进度观察者。该参数存在，则取消订阅指定回调，该参数为null或undefined或不存在，则取消订阅所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Need 1 - 3 parameter(s)! 2. The RdbStore must be valid. 3. The event must be a not empty string. 4. The progress must be function. |
| 801 | Capability not supported. |
| 14800014 | The target instance is already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let progressDetail = (progressDetail: relationalStore.ProgressDetails) => {
4. console.info(`progress: ${progressDetail}`);
5. };

7. try {
8. if (store != undefined) {
9. (store as relationalStore.RdbStore).on('autoSyncProgress', progressDetail);
10. }
11. } catch (err) {
12. let code = (err as BusinessError).code;
13. let message = (err as BusinessError).message;
14. console.error(`Register observer failed, code is ${code},message is ${message}`);
15. }

17. try {
18. if (store != undefined) {
19. (store as relationalStore.RdbStore).off('autoSyncProgress', progressDetail);
20. }
21. } catch (err) {
22. let code = (err as BusinessError).code;
23. let message = (err as BusinessError).message;
24. console.error(`Unregister failed, code is ${code},message is ${message}`);
25. }
```

## off('statistics')12+

PhonePC/2in1TabletTVWearable

off(event: 'statistics', observer?: Callback<SqlExecutionInfo>): void

取消订阅SQL统计信息。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取消订阅事件名称。取值为'statistics'，表示sql执行时间的统计。 |
| observer | Callback<[SqlExecutionInfo](arkts-apis-data-relationalstore-i.md#sqlexecutioninfo12)> | 否 | 回调函数。该参数存在，则取消指定Callback监听回调，否则取消该event事件的所有监听回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. if (store != undefined) {
5. (store as relationalStore.RdbStore).off('statistics');
6. }
7. } catch (err) {
8. let code = (err as BusinessError).code;
9. let message = (err as BusinessError).message;
10. console.error(`Unregister observer failed, code is ${code},message is ${message}`);
11. }
```

## off('sqliteErrorOccurred')20+

PhonePC/2in1TabletTVWearable

off(event: 'sqliteErrorOccurred', observer?: Callback<ExceptionMessage>): void

停止记录SQL执行过程中的异常日志。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取消订阅事件名称，取值为'sqliteErrorOccurred'，记录SQL语句执行过程中的错误信息。 |
| observer | Callback<[ExceptionMessage](arkts-apis-data-relationalstore-i.md#exceptionmessage20)> | 否 | 回调函数。该参数存在，则取消指定Callback监听回调，否则取消该event事件的所有监听回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 801 | Capability not supported. |
| 14800014 | The target instance is already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. if (store != undefined) {
5. (store as relationalStore.RdbStore).off('sqliteErrorOccurred');
6. }
7. } catch (err) {
8. let code = (err as BusinessError).code;
9. let message = (err as BusinessError).message;
10. console.error(`Unregister observer failed, code is ${code},message is ${message}`);
11. }
```

## off('perfStat')20+

PhonePC/2in1TabletTVWearable

off(event: 'perfStat', observer?: Callback<SqlExecutionInfo>): void

取消订阅SQL统计信息。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取消订阅事件名称。取值为'perfStat'，统计执行SQL的时间。 |
| observer | Callback<[SqlExecutionInfo](arkts-apis-data-relationalstore-i.md#sqlexecutioninfo12)> | 否 | 回调函数，表示订阅时的回调函数。该参数存在，则取消指定Callback监听回调，否则取消该event事件的所有监听回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 801 | Capability not supported. |
| 14800014 | The target instance is already closed. |

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. if (store != undefined) {
5. (store as relationalStore.RdbStore).off('perfStat');
6. }
7. } catch (err) {
8. let code = (err as BusinessError).code;
9. let message = (err as BusinessError).message;
10. console.error(`Unregister observer failed, code is ${code},message is ${message}`);
11. }
```

## emit10+

PhonePC/2in1TabletTVWearable

emit(event: string): void

通知通过[on](arkts-apis-data-relationalstore-rdbstore.md#on10)注册的进程间或者进程内监听事件。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 通知订阅事件的名称，可自定义事件名称，不能与系统已有事件[dataChange](arkts-apis-data-relationalstore-rdbstore.md#ondatachange)，[autoSyncProgress](arkts-apis-data-relationalstore-rdbstore.md#onautosyncprogress11)，[statistics](arkts-apis-data-relationalstore-rdbstore.md#onstatistics12)名称重复。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |
| 14800050 | Failed to obtain the subscription service. |

**示例：**

```
1. if (store != undefined) {
2. (store as relationalStore.RdbStore).emit('storeObserver');
3. }
```

## cleanDirtyData11+

PhonePC/2in1TabletTV

cleanDirtyData(table: string, cursor: number, callback: AsyncCallback<void>): void

清理云端删除的数据同步到本地后，未自动清理的，且数据的游标（cursor）小于指定游标的数据。使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 表示当前数据库的表的名称。 |
| cursor | number | 是 | 整数类型，表示数据游标，小于此游标的脏数据将被清理。 |
| callback | AsyncCallback<void> | 是 | 指定的callback回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Need 1 - 3 parameter(s)! 2. The RdbStore must be not nullptr. 3. The tablesNames must be not empty string. 4. The cursor must be valid cursor. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**示例：**

```
1. if (store != undefined) {
2. (store as relationalStore.RdbStore).cleanDirtyData('test_table', 100, (err) => {
3. if (err) {
4. console.error(`clean dirty data failed, code is ${err.code},message is ${err.message}`);
5. return;
6. }
7. console.info('clean dirty data succeeded');
8. });
9. }
```

## cleanDirtyData11+

PhonePC/2in1TabletTV

cleanDirtyData(table: string, callback: AsyncCallback<void>): void

清理云端删除的数据同步到本地后，未自动清理的所有数据。使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 表示当前数据库的表的名称。 |
| callback | AsyncCallback<void> | 是 | 指定的callback回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Need 1 - 3 parameter(s). 2. The RdbStore must be not nullptr. 3. The tablesNames must be not empty string. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**示例：**

```
1. if (store != undefined) {
2. (store as relationalStore.RdbStore).cleanDirtyData('test_table', (err) => {
3. if (err) {
4. console.error(`clean dirty data failed, code is ${err.code},message is ${err.message}`);
5. return;
6. }
7. console.info('clean dirty data succeeded');
8. });
9. }
```

## cleanDirtyData11+

PhonePC/2in1TabletTV

cleanDirtyData(table: string, cursor?: number): Promise<void>

清理云端删除的数据同步到本地后，未自动清理的，且数据的游标（cursor）小于指定游标的数据，使用Promise异步回调。若无cursor参数，将全部清理。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 表示当前数据库的表的名称。 |
| cursor | number | 否 | 整数类型，表示数据游标，小于此游标的脏数据将被清理。当此参数不填时，清理当前表的所有脏数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Need 1 - 3 parameter(s)! 2. The RdbStore must be not nullptr. 3. The tablesNames must be not empty string. 4. The cursor must be valid cursor. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. if (store != undefined) {
4. (store as relationalStore.RdbStore).cleanDirtyData('test_table', 100).then(() => {
5. console.info('clean dirty data  succeeded');
6. }).catch((err: BusinessError) => {
7. console.error(`clean dirty data failed, code is ${err.code},message is ${err.message}`);
8. });
9. }
```

## attach12+

PhonePC/2in1TabletTVWearable

attach(fullPath: string, attachName: string, waitTime?: number) : Promise<number>

将一个数据库文件附加到当前数据库中，以便在SQL语句中可以直接访问附加数据库中的数据，使用Promise异步回调。

数据库文件来自文件，且此API不支持附加加密数据库。调用attach接口后，数据库切换为非WAL模式，性能会存在一定的劣化。

attach时，数据库会切换为非WAL模式，切换模式需要确保所有的ResultSet都已经Close，所有的写操作已经结束，否则会报错14800015。

attach不能并发调用，否则可能出现未响应情况并报错14800015，需要重试。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fullPath | string | 是 | 表示要附加的数据库的路径。 |
| attachName | string | 是 | 表示附加后的数据库的别名。 |
| waitTime | number | 否 | 表示附加数据库文件的等待时长，单位：s。默认值2s，最小值1s，最大值300s。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回附加数据库的数量。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800010 | Failed to open or delete the database by an invalid database path. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800016 | The database alias already exists. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**示例：**

```
1. // 非加密数据库附加非加密数据库。
2. import { BusinessError } from '@kit.BasicServicesKit';

4. if (store != undefined) {
5. (store as relationalStore.RdbStore).attach("/path/rdbstore1.db", "attachDB").then((number: number) => {
6. console.info('attach succeeded');
7. }).catch((err: BusinessError) => {
8. console.error(`attach failed, code is ${err.code},message is ${err.message}`);
9. });
10. }
```

## attach12+

PhonePC/2in1TabletTVWearable

attach(context: Context, config: StoreConfig, attachName: string, waitTime?: number) : Promise<number>

将一个当前应用的数据库附加到当前数据库中，以便在SQL语句中可以直接访问附加数据库中的数据，使用Promise异步回调。

此API不支持加密数据库附加非加密数据库。调用attach接口后，数据库切换为非WAL模式，性能会存在一定的劣化。

attach时，数据库会切换为非WAL模式，切换模式需要确保所有的ResultSet都已经Close，所有的写操作已经结束，否则会报错14800015。

attach不能并发调用，否则可能出现未响应情况并报错14800015，需要重试。除此之外，attach附加加密数据库时，可能受到并发的影响，出现解密失败的情况，报错14800011，需要显式指定加密参数并重试。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用的上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| config | [StoreConfig](arkts-apis-data-relationalstore-i.md#storeconfig) | 是 | 与此RDB存储相关的数据库配置。 |
| attachName | string | 是 | 表示附加后的数据库的别名。 |
| waitTime | number | 否 | 表示附加数据库文件的等待时长，单位：s。默认值2s，最小值1s，最大值300s。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回附加数据库的数量。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800010 | Failed to open or delete the database by an invalid database path. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800016 | The database alias already exists. |
| 14801001 | The operation is supported in the stage model only. |
| 14801002 | Invalid data group ID. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**示例1：非加密数据库附加非加密数据库**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let attachStore: relationalStore.RdbStore | undefined = undefined;

5. const STORE_CONFIG1: relationalStore.StoreConfig = {
6. name: "rdbstore1.db",
7. securityLevel: relationalStore.SecurityLevel.S3
8. };

10. relationalStore.getRdbStore(this.context, STORE_CONFIG1).then(async (rdbStore: relationalStore.RdbStore) => {
11. attachStore = rdbStore;
12. console.info('Get RdbStore successfully.');
13. if (store != undefined) {
14. (store as relationalStore.RdbStore).attach(this.context, STORE_CONFIG1, "attachDB").then((number: number) => {
15. console.info(`attach succeeded, number is ${number}`);
16. }).catch((err: BusinessError) => {
17. console.error(`attach failed, code is ${err.code},message is ${err.message}`);
18. });
19. }
20. }).catch((err: BusinessError) => {
21. console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
22. });
```

**示例2：非加密数据库附加加密数据库**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let attachStore: relationalStore.RdbStore | undefined = undefined;

5. const STORE_CONFIG2: relationalStore.StoreConfig = {
6. name: "rdbstore2.db",
7. encrypt: true,
8. securityLevel: relationalStore.SecurityLevel.S3
9. };

11. relationalStore.getRdbStore(this.context, STORE_CONFIG2).then(async (rdbStore: relationalStore.RdbStore) => {
12. attachStore = rdbStore;
13. console.info('Get RdbStore successfully.');
14. if (store != undefined) {
15. (store as relationalStore.RdbStore).attach(this.context, STORE_CONFIG2, "attachDB2", 10).then((number: number) => {
16. console.info(`attach succeeded, number is ${number}`);
17. }).catch((err: BusinessError) => {
18. console.error(`attach failed, code is ${err.code},message is ${err.message}`);
19. });
20. }
21. }).catch((err: BusinessError) => {
22. console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
23. });
```

## detach12+

PhonePC/2in1TabletTVWearable

detach(attachName: string, waitTime?: number) : Promise<number>

将附加的数据库从当前数据库中分离，使用Promise异步回调。

当所有的附加的数据库被分离后，数据库会重新切换为WAL模式。

在detach之前，所有的数据库操作要确保已经结束，所有的ResultSet已经Close。并且不能并发调用，可能出现未响应情况，需要重试。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| attachName | string | 是 | 表示附加后的数据库的别名。 |
| waitTime | number | 否 | 表示分离数据库的等待时长，单位：s。默认值2s，最小值1s，最大值300s。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回分离后剩余附加的数据库的数量。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. if (store != undefined) {
4. (store as relationalStore.RdbStore).detach("attachDB").then((number: number) => {
5. console.info(`detach succeeded, number is ${number}`);
6. }).catch((err: BusinessError) => {
7. console.error(`detach failed, code is ${err.code},message is ${err.message}`);
8. });
9. }
```

## lockRow12+

PhonePC/2in1TabletTVWearable

lockRow(predicates: RdbPredicates):Promise<void>

根据RdbPredicates的指定实例对象从数据库中锁定数据，锁定数据不执行端云同步，使用Promise异步回调。

该接口只支持主键为基本类型的表、不支持共享表、无主键表和复合类型主键表。

该接口不支持依赖关系表之间的锁传递，如果表存在依赖关系，需要根据依赖关系手动调用该接口。

该接口不支持对已删除数据的操作。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicates | [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 是 | RdbPredicates的实例对象指定的锁定条件。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800018 | No data meets the condition. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
4. predicates.equalTo("NAME", "Lisa");
5. if (store != undefined) {
6. (store as relationalStore.RdbStore).lockRow(predicates).then(() => {
7. console.info(`Lock success`);
8. }).catch((err: BusinessError) => {
9. console.error(`Lock failed, code is ${err.code},message is ${err.message}`);
10. });
11. }
```

## unlockRow12+

PhonePC/2in1TabletTVWearable

unlockRow(predicates: RdbPredicates):Promise<void>

根据RdbPredicates的指定实例对象从数据库中解锁数据，使用Promise异步回调。

该接口只支持主键为基本类型的表、不支持共享表、无主键表和复合类型主键表。

该接口不支持依赖关系表之间的锁传递，如果表存在依赖关系，需要根据依赖关系手动调用该接口。

该接口不支持对已删除数据的操作。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicates | [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 是 | RdbPredicates的实例对象指定的锁定条件。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800018 | No data meets the condition. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
4. predicates.equalTo("NAME", "Lisa");
5. if (store != undefined) {
6. (store as relationalStore.RdbStore).unlockRow(predicates).then(() => {
7. console.info(`Unlock success`);
8. }).catch((err: BusinessError) => {
9. console.error(`Unlock failed, code is ${err.code},message is ${err.message}`);
10. });
11. }
```

## queryLockedRow12+

PhonePC/2in1TabletTVWearable

queryLockedRow(predicates: RdbPredicates, columns?: Array<string>):Promise<ResultSet>

根据指定条件查询数据库中锁定的数据，使用Promise异步回调。

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

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
4. predicates.equalTo("NAME", "Rose");
5. if (store != undefined) {
6. (store as relationalStore.RdbStore).queryLockedRow(predicates, ["ID", "NAME", "AGE", "SALARY", "CODES"]).then(async (resultSet: relationalStore.ResultSet) => {
7. console.info(`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}`);
8. // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
9. try {
10. while (resultSet.goToNextRow()) {
11. const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
12. const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
13. const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
14. const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
15. console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
16. }
17. } catch (err) {
18. console.error(`Query failed, code is ${err.code},message is ${err.message}`);
19. } finally {
20. // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
21. resultSet.close();
22. }
23. }).catch((err: BusinessError) => {
24. console.error(`Query failed, code is ${err.code},message is ${err.message}`);
25. });
26. }
```

## close12+

PhonePC/2in1TabletTVWearable

close(): Promise<void>

关闭数据库，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: The RdbStore verification failed. |
| 14800000 | Inner error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. if (store != undefined) {
4. (store as relationalStore.RdbStore).close().then(() => {
5. console.info(`close succeeded`);
6. }).catch((err: BusinessError) => {
7. console.error(`close failed, code is ${err.code},message is ${err.message}`);
8. });
9. }
```

## rekey20+

PhonePC/2in1TabletTVWearable

rekey(cryptoParam?: CryptoParam): Promise<void>

手动更新加密数据库的密钥。使用Promise异步回调。

不支持对非WAL模式的数据库进行密钥更新。

手动更新密钥时需要独占访问数据库，此时若存在任何未释放的结果集（ResultSet）、事务（Transaction）或其他进程打开的数据库均会引发失败。

仅支持加密数据库进行密钥更新，不支持非加密数据库变加密数据库及加密数据库变非加密数据库，且需要保持加密参数和密钥生成方式与建库时一致。

数据库越大，密钥更新所需的时间越长。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cryptoParam | [CryptoParam](arkts-apis-data-relationalstore-i.md#cryptoparam14) | 否 | 指定用户自定义的加密参数。  当此参数不填时，使用默认的加密参数，见CryptoParam。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 801 | Capability not supported. |
| 14800001 | Invalid arguments. Possible causes: 1.Parameter is out of valid range. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |

**示例：**

示例代码中this.context定义见Stage模型的应用[Context](js-apis-inner-application-context.md)。

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. // 示例1：使用默认的加密参数
4. export default class EntryAbility extends UIAbility {
5. onCreate() {
6. let store: relationalStore.RdbStore | undefined = undefined;
7. const STORE_CONFIG1: relationalStore.StoreConfig = {
8. name: 'rdbstore1.db',
9. securityLevel: relationalStore.SecurityLevel.S3,
10. encrypt: true
11. };

13. relationalStore.getRdbStore(this.context, STORE_CONFIG1).then(async (rdbStore: relationalStore.RdbStore) => {
14. store = rdbStore;
15. console.info('Get RdbStore successfully.');

17. let cryptoParam1: relationalStore.CryptoParam = {
18. encryptionKey: new Uint8Array()
19. };

21. if (store != undefined) {
22. try {
23. (store as relationalStore.RdbStore).rekey(cryptoParam1);
24. console.info('rekey is successful');
25. } catch (err) {
26. console.error(`rekey is failed, code is ${err.code},message is ${err.message}`);
27. }
28. }
29. }).catch((err: BusinessError) => {
30. console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
31. });
32. }
33. }
```

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. // 示例2：使用自定义的加密参数
4. export default class EntryAbility extends UIAbility {
5. onCreate() {
6. let store: relationalStore.RdbStore | undefined = undefined;
7. let cryptoParam: relationalStore.CryptoParam = {
8. encryptionKey: new Uint8Array([1, 2, 3, 4, 5, 6]),
9. iterationCount: 1000,
10. encryptionAlgo: relationalStore.EncryptionAlgo.AES_256_GCM,
11. hmacAlgo: relationalStore.HmacAlgo.SHA256,
12. kdfAlgo: relationalStore.KdfAlgo.KDF_SHA256,
13. cryptoPageSize: 1024
14. };

16. const STORE_CONFIG2: relationalStore.StoreConfig = {
17. name: 'rdbstore2.db',
18. securityLevel: relationalStore.SecurityLevel.S3,
19. encrypt: true,
20. cryptoParam: cryptoParam
21. };

23. relationalStore.getRdbStore(this.context, STORE_CONFIG2).then(async (rdbStore: relationalStore.RdbStore) => {
24. store = rdbStore;
25. console.info('Get RdbStore successfully.');
26. let cryptoParam2: relationalStore.CryptoParam = {
27. encryptionKey: new Uint8Array([6, 5, 4, 3, 2, 1]),
28. iterationCount: 1000,
29. encryptionAlgo: relationalStore.EncryptionAlgo.AES_256_GCM,
30. hmacAlgo: relationalStore.HmacAlgo.SHA256,
31. kdfAlgo: relationalStore.KdfAlgo.KDF_SHA256,
32. cryptoPageSize: 1024
33. };

35. if (store != undefined) {
36. try {
37. (store as relationalStore.RdbStore).rekey(cryptoParam2);
38. console.info('rekey is successful');
39. } catch (err) {
40. console.error(`rekey is failed, code is ${err.code},message is ${err.message}`);
41. }
42. }
43. }).catch((err: BusinessError) => {
44. console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
45. });
46. }
47. }
```

## setLocale20+

PhonePC/2in1TabletTVWearable

setLocale(locale: string) : Promise<void>

设置自定义排序的语言。使用Promise异步回调。

该值符合ISO 639标准，但是仅支持ICU中的部分语言，对于不支持的语言，设置自定义排序的语言时会报错14800001。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locale | string | 是 | 设置自定义排序的语言。该值符合ISO 639标准，如："zh"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 801 | Capability not supported. |
| 14800001 | Invalid arguments. Possible causes: 1.Parameter is out of valid range. |
| 14800014 | The target instance is already closed. |
| 14800024 | SQLite: The database file is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800034 | SQLite: Library used incorrectly. |

**示例：**

```
1. try {
2. if (store != undefined) {
3. await store.setLocale("zh");
4. store.querySql("SELECT * FROM EMPLOYEE ORDER BY NAME COLLATE LOCALES", async (err, resultSet) => {
5. if (err) {
6. console.error(`Query failed, code: ${err.code}, message: ${err.message}`);
7. return;
8. }
9. console.info(`ResultSet rowCount ${resultSet.rowCount}`);
10. });
11. }
12. } catch (err) {
13. console.error(`SetLocale failed, code: ${err.code}, message: ${err.message}`);
14. }
```

## rekeyEx22+

PhonePC/2in1TabletTVWearable

rekeyEx(cryptoParam: CryptoParam): Promise<void>

手动更新数据库的密钥或加密参数，使用Promise异步回调。

不支持对非WAL模式的数据库进行密钥更新。

手动更新时需要独占访问数据库，此时若存在任何未释放的结果集（ResultSet）、事务（Transaction）或其他进程打开的数据库均会导致更新失败。

支持加密数据库的参数更新，以及加密数据库与非加密数据库之间的相互转换。

数据库越大，执行更新所需的时间越长。

说明

加密参数变更需谨慎，在完成rekeyEx操作后，getRdbStore时必须使用新的参数来打开数据库，否则可能会导致开库失败。

如果rekey过程因设备断电等原因中断，操作可能成功也可能失败。因此，建议业务方做好兜底保障（使用RekeyEx前后的参数进行冗余重试），确保不会错误地判断数据库的状态，从而避免出现数据库无法打开的问题。

如果有加密参数变更，不建议getRdbStore时使用AllowedRebuild参数，防止因为传入的错误加密参数导致数据库发生重建。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cryptoParam | [CryptoParam](arkts-apis-data-relationalstore-i.md#cryptoparam14) | 是 | 指定用户自定义的加密参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 801 | Capability not supported. |
| 14800001 | Invalid arguments. Possible causes: 1.Parameter is out of valid range. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800021 | SQLite: Generic error. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |

**示例1：原数据库为默认参数加密数据库，更换密钥和加密参数**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. async onCreate() {
6. let store: relationalStore.RdbStore | undefined = undefined;
7. const configV1: relationalStore.StoreConfig = {
8. name: 'rdbstore1.db',
9. securityLevel: relationalStore.SecurityLevel.S3,
10. encrypt: true
11. };

13. try {
14. const rdbStore = await relationalStore.getRdbStore(this.context, configV1);
15. store = rdbStore;
16. console.info('Get RdbStore successfully.');

18. let cryptoParam: relationalStore.CryptoParam = {
19. encryptionKey: new Uint8Array(),
20. encryptionAlgo: relationalStore.EncryptionAlgo.AES_256_CBC,
21. hmacAlgo: relationalStore.HmacAlgo.SHA256,
22. kdfAlgo: relationalStore.KdfAlgo.KDF_SHA256,
23. iterationCount: 1000,
24. cryptoPageSize: 2048,
25. };

27. if (store != undefined) {
28. try {
29. await (store as relationalStore.RdbStore).rekeyEx(cryptoParam);
30. console.info('rekeyEx is successful');
31. } catch (err) {
32. console.error(`rekeyEx is failed, code is ${err.code},message is ${err.message}`);
33. }
34. }
35. // 在完成rekeyEx操作后，如果后续需要重新getRdbStore时必须使用新的参数来打开数据库
36. } catch (err) {
37. console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
38. };
39. }
40. }
```

**示例2：原数据库为自定义参数加密数据库，更换自定义密钥和加密参数**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. async onCreate() {
6. let store: relationalStore.RdbStore | undefined = undefined;
7. let cryptoParam: relationalStore.CryptoParam = {
8. // 安全提醒：1.空数组encryptionKey表示使用系统生成的密钥（仅适用于部分场景）；2.生产环境应使用应用沙箱密钥或安全存储服务管理密钥，不要在代码中硬编码固定密钥
9. encryptionKey: new Uint8Array([1, 2, 3, 4, 5, 6]),
10. iterationCount: 1000,
11. encryptionAlgo: relationalStore.EncryptionAlgo.AES_256_GCM,
12. hmacAlgo: relationalStore.HmacAlgo.SHA256,
13. kdfAlgo: relationalStore.KdfAlgo.KDF_SHA256,
14. cryptoPageSize: 1024
15. };
16. const configV1: relationalStore.StoreConfig = {
17. name: 'rdbstore1.db',
18. securityLevel: relationalStore.SecurityLevel.S3,
19. encrypt: true,
20. cryptoParam: cryptoParam
21. };

23. try {
24. const rdbStore = await relationalStore.getRdbStore(this.context, configV1);
25. store = rdbStore;
26. console.info('Get RdbStore successfully.');

28. let cryptoParam1: relationalStore.CryptoParam = {
29. encryptionKey: new Uint8Array([6, 5, 4, 3, 2, 1]),
30. iterationCount: 5000,
31. encryptionAlgo: relationalStore.EncryptionAlgo.AES_256_CBC,
32. hmacAlgo: relationalStore.HmacAlgo.SHA512,
33. kdfAlgo: relationalStore.KdfAlgo.KDF_SHA512,
34. cryptoPageSize: 2048
35. };

37. if (store != undefined) {
38. try {
39. await (store as relationalStore.RdbStore).rekeyEx(cryptoParam1);
40. console.info('rekeyEx is successful');
41. } catch (err) {
42. console.error(`rekeyEx is failed, code is ${err.code},message is ${err.message}`);
43. }
44. }
45. // 在完成rekeyEx操作后，如果后续需要重新getRdbStore时必须使用新的参数来打开数据库
46. } catch (err) {
47. console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
48. };
49. }
50. }
```

**示例3：原数据库为默认参数加密库，更换自定义密钥和加密参数**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. async onCreate() {
6. let store: relationalStore.RdbStore | undefined = undefined;
7. const configV1: relationalStore.StoreConfig = {
8. name: 'rdbstore1.db',
9. securityLevel: relationalStore.SecurityLevel.S3,
10. encrypt: true
11. };

13. try {
14. const rdbStore = await relationalStore.getRdbStore(this.context, configV1);
15. store = rdbStore;
16. console.info('Get RdbStore successfully.');

18. let cryptoParam: relationalStore.CryptoParam = {
19. // 安全提醒：1.空数组encryptionKey表示使用系统生成的密钥（仅适用于部分场景）；2.生产环境应使用应用沙箱密钥或安全存储服务管理密钥，不要在代码中硬编码固定密钥
20. encryptionKey: new Uint8Array([6, 5, 4, 3, 2, 1]),
21. encryptionAlgo: relationalStore.EncryptionAlgo.AES_256_CBC,
22. hmacAlgo: relationalStore.HmacAlgo.SHA256,
23. kdfAlgo: relationalStore.KdfAlgo.KDF_SHA256,
24. iterationCount: 1000,
25. cryptoPageSize: 2048,
26. };

28. if (store != undefined) {
29. try {
30. await (store as relationalStore.RdbStore).rekeyEx(cryptoParam);
31. console.info('rekeyEx is successful');
32. } catch (err) {
33. console.error(`rekeyEx is failed, code is ${err.code},message is ${err.message}`);
34. }
35. }
36. // 在完成rekeyEx操作后，如果后续需要重新getRdbStore时必须使用新的参数来打开数据库
37. } catch (err) {
38. console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
39. };
40. }
41. }
```

**示例4：原数据库为自定义参数加密数据库，更换数据库生成密钥和自定义加密参数**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. async onCreate() {
6. let store: relationalStore.RdbStore | undefined = undefined;
7. let cryptoParam: relationalStore.CryptoParam = {
8. // 安全提醒：1.空数组encryptionKey表示使用系统生成的密钥（仅适用于部分场景）；2.生产环境应使用应用沙箱密钥或安全存储服务管理密钥，不要在代码中硬编码固定密钥
9. encryptionKey: new Uint8Array([1, 2, 3, 4, 5, 6]),
10. iterationCount: 1000,
11. encryptionAlgo: relationalStore.EncryptionAlgo.AES_256_GCM,
12. hmacAlgo: relationalStore.HmacAlgo.SHA256,
13. kdfAlgo: relationalStore.KdfAlgo.KDF_SHA256,
14. cryptoPageSize: 1024
15. };
16. const configV1: relationalStore.StoreConfig = {
17. name: 'rdbstore2.db',
18. securityLevel: relationalStore.SecurityLevel.S3,
19. encrypt: true,
20. cryptoParam: cryptoParam
21. };

23. try {
24. const rdbStore = await relationalStore.getRdbStore(this.context, configV1);
25. store = rdbStore;
26. console.info('Get RdbStore successfully.');

28. let cryptoParam1: relationalStore.CryptoParam = {
29. encryptionKey: new Uint8Array(),
30. iterationCount: 5000,
31. encryptionAlgo: relationalStore.EncryptionAlgo.AES_256_CBC,
32. hmacAlgo: relationalStore.HmacAlgo.SHA512,
33. kdfAlgo: relationalStore.KdfAlgo.KDF_SHA512,
34. cryptoPageSize: 2048
35. };

37. if (store != undefined) {
38. try {
39. await (store as relationalStore.RdbStore).rekeyEx(cryptoParam1);
40. console.info('rekeyEx is successful');
41. } catch (err) {
42. console.error(`rekeyEx is failed, code is ${err.code},message is ${err.message}`);
43. }
44. }
45. // 在完成rekeyEx操作后，如果后续需要重新getRdbStore时必须使用新的参数来打开数据库
46. } catch (err) {
47. console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
48. };
49. }
50. }
```

**示例5：原数据库为自定义参数加密数据库，更换为非加密数据库**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. async onCreate() {
6. let store: relationalStore.RdbStore | undefined = undefined;
7. let cryptoParam: relationalStore.CryptoParam = {
8. // 安全提醒：1.空数组encryptionKey表示使用系统生成的密钥（仅适用于部分场景）；2.生产环境应使用应用沙箱密钥或安全存储服务管理密钥，不要在代码中硬编码固定密钥
9. encryptionKey: new Uint8Array([1, 2, 3, 4, 5, 6]),
10. iterationCount: 1000,
11. encryptionAlgo: relationalStore.EncryptionAlgo.AES_256_GCM,
12. hmacAlgo: relationalStore.HmacAlgo.SHA256,
13. kdfAlgo: relationalStore.KdfAlgo.KDF_SHA256,
14. cryptoPageSize: 1024
15. };
16. const configV1: relationalStore.StoreConfig = {
17. name: 'rdbstore1.db',
18. securityLevel: relationalStore.SecurityLevel.S3,
19. encrypt: true,
20. cryptoParam: cryptoParam
21. };

23. try {
24. const rdbStore = await relationalStore.getRdbStore(this.context, configV1);
25. store = rdbStore;
26. console.info('Get RdbStore successfully.');

28. let cryptoParam1: relationalStore.CryptoParam = {
29. encryptionKey: new Uint8Array(),
30. encryptionAlgo: relationalStore.EncryptionAlgo.PLAIN_TEXT
31. };

33. if (store != undefined) {
34. try {
35. await (store as relationalStore.RdbStore).rekeyEx(cryptoParam1);
36. console.info('rekeyEx is successful');
37. } catch (err) {
38. console.error(`rekeyEx is failed, code is ${err.code},message is ${err.message}`);
39. }
40. }
41. // 在完成rekeyEx操作后，如果后续需要重新getRdbStore时必须使用新的参数来打开数据库
42. } catch (err) {
43. console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
44. };
45. }
46. }
```

**示例6：原数据库为非加密数据库，更换为自定义参数加密数据库**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. async onCreate() {
6. let store: relationalStore.RdbStore | undefined = undefined;
7. const configV1: relationalStore.StoreConfig = {
8. name: 'rdbstore1.db',
9. securityLevel: relationalStore.SecurityLevel.S3,
10. encrypt: false,
11. };

13. try {
14. const rdbStore = await relationalStore.getRdbStore(this.context, configV1);
15. store = rdbStore;
16. console.info('Get RdbStore successfully.');

18. let cryptoParam: relationalStore.CryptoParam = {
19. // 安全提醒：1.空数组encryptionKey表示使用系统生成的密钥（仅适用于部分场景）；2.生产环境应使用应用沙箱密钥或安全存储服务管理密钥，不要在代码中硬编码固定密钥
20. encryptionKey: new Uint8Array([1, 2, 3, 4, 5, 6]),
21. iterationCount: 1000,
22. encryptionAlgo: relationalStore.EncryptionAlgo.AES_256_GCM,
23. hmacAlgo: relationalStore.HmacAlgo.SHA256,
24. kdfAlgo: relationalStore.KdfAlgo.KDF_SHA256,
25. cryptoPageSize: 1024
26. };

28. if (store != undefined) {
29. try {
30. await (store as relationalStore.RdbStore).rekeyEx(cryptoParam);
31. console.info('rekeyEx is successful');
32. } catch (err) {
33. console.error(`rekeyEx is failed, code is ${err.code},message is ${err.message}`);
34. }
35. }
36. // 在完成rekeyEx操作后，如果后续需要重新getRdbStore时必须使用新的参数来打开数据库
37. } catch (err) {
38. console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
39. };
40. }
41. }
```
