---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-backup-and-restore
title: 数据库备份与恢复 (ArkTS)
breadcrumb: 指南 > 应用框架 > ArkData（方舟数据管理） > 数据可靠性与安全性 > 数据库备份与恢复 (ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:460f86b647a3bec512d616016d6ad7ed9c999106cf67a3131e07bc3b82e2b67e
---

## 场景介绍

如果操作或存储的过程中出现问题，开发者可以使用恢复功能，将数据库恢复到之前的状态，重新对数据库进行操作。

在数据库被篡改、删除、或者设备断电场景下，数据库可能会因为数据丢失、数据损坏、脏数据等而不可用，可以通过数据库的备份恢复能力将数据库恢复至可用状态。

键值型数据库和关系型数据库均支持对数据库的备份和恢复。另外，键值型数据库还支持删除数据库备份，以释放本地存储空间。

## 键值型数据库备份、恢复与删除

键值型数据库，通过backup接口实现数据库备份，通过restore接口实现数据库恢复，通过deletebackup接口删除数据库备份。具体接口及功能，可见[分布式键值数据库](../harmonyos-references/js-apis-distributedkvstore.md)。

1. 创建数据库。

   (1) 创建kvManager。

   (2) 配置数据库参数。

   (3) 创建kvStore。

   ```
   1. // 导入模块
   2. // 在pages目录下新建KvStoreInterface.ets
   3. import { distributedKVStore } from '@kit.ArkData';
   4. import { BusinessError } from '@kit.BasicServicesKit';
   5. import EntryAbility from '../entryability/EntryAbility';
   6. // Logger为hilog封装后实现的打印功能
   7. import Logger from '../common/Logger';

   9. let kvManager: distributedKVStore.KVManager | undefined = undefined;
   10. let kvStore: distributedKVStore.SingleKVStore | undefined = undefined;
   11. let appId: string = 'com.example.kvstoresamples';
   12. let storeId: string = 'storeId';
   13. const context = EntryAbility.getContext();

   15. // 下面所有接口的代码都实现在KvInterface中
   16. export class KvInterface {
   17. }
   ```

   ```
   1. public CreateKvManager = (() => {
   2. Logger.info('CreateKvManager start');
   3. if (typeof (kvManager) === 'undefined') {
   4. const kvManagerConfig: distributedKVStore.KVManagerConfig = {
   5. bundleName: appId,
   6. context: context
   7. };
   8. try {
   9. // 创建KVManager实例
   10. kvManager = distributedKVStore.createKVManager(kvManagerConfig);
   11. Logger.info('Succeeded in creating KVManager.');
   12. } catch (err) {
   13. Logger.error(`Failed to create KVManager. Code:${err.code},message:${err.message}`);
   14. }
   15. } else {
   16. Logger.info ('KVManager has created');
   17. }
   18. })
   ```

   [KvStoreInterface.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/KvStore/KvStoreSamples/entry/src/main/ets/pages/KvStoreInterface.ets#L29-L48)

   ```
   1. public GetKvStore = (() => {
   2. Logger.info('GetKvStore start');
   3. if (kvManager === undefined) {
   4. Logger.info('KvManager not initialized');
   5. return;
   6. }
   7. try {
   8. let child1 = new distributedKVStore.FieldNode('id');
   9. child1.type = distributedKVStore.ValueType.INTEGER;
   10. child1.nullable = false;
   11. child1.default = '1';
   12. let child2 = new distributedKVStore.FieldNode('name');
   13. child2.type = distributedKVStore.ValueType.STRING;
   14. child2.nullable = false;
   15. child2.default = 'zhangsan';

   17. let schema = new distributedKVStore.Schema();
   18. schema.root.appendChild(child1);
   19. schema.root.appendChild(child2);
   20. schema.indexes = ['$.id', '$.name'];
   21. // 0表示COMPATIBLE模式，1表示STRICT模式。
   22. schema.mode = 1;
   23. // 支持在检查Value时，跳过skip指定的字节数，且取值范围为[0,4M-2]。
   24. schema.skip = 0;

   26. const options: distributedKVStore.Options = {
   27. createIfMissing: true,
   28. // 设置数据库加密
   29. encrypt: true,
   30. backup: false,
   31. autoSync: false,
   32. // kvStoreType不填时，默认创建多设备协同数据库
   33. kvStoreType: distributedKVStore.KVStoreType.SINGLE_VERSION,
   34. // 多设备协同数据库：kvStoreType: distributedKVStore.KVStoreType.DEVICE_COLLABORATION,
   35. schema: schema,
   36. // schema未定义可以不填，定义方法请参考上方schema示例。
   37. securityLevel: distributedKVStore.SecurityLevel.S3
   38. };
   39. kvManager.getKVStore<distributedKVStore.SingleKVStore>(storeId, options,
   40. (err, store: distributedKVStore.SingleKVStore) => {
   41. if (err) {
   42. Logger.error(`Failed to get KVStore: Code:${err.code},message:${err.message}`);
   43. return;
   44. }
   45. Logger.info('Succeeded in getting KVStore.');
   46. kvStore = store;
   47. // 请确保获取到键值数据库实例后，再进行相关数据操作
   48. });
   49. } catch (e) {
   50. let error = e as BusinessError;
   51. Logger.error(`An unexpected error occurred. Code:${error.code},message:${error.message}`);
   52. }
   53. })
   ```

   [KvStoreInterface.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/KvStore/KvStoreSamples/entry/src/main/ets/pages/KvStoreInterface.ets#L50-L104)
2. 使用put()方法插入数据。

   ```
   1. public Put = (() => {
   2. Logger.info('Put start');
   3. if (kvStore === undefined) {
   4. Logger.info('Put: kvStore not initialized');
   5. return;
   6. }
   7. const KEY_TEST_STRING_ELEMENT = 'key_test_string';
   8. // 如果未定义Schema则Value可以传其他符合要求的值。
   9. const VALUE_TEST_STRING_ELEMENT = '{"id":0, "name":"lisi"}';
   10. try {
   11. kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT, (err) => {
   12. if (err !== undefined) {
   13. Logger.error(`Failed to put data. Code:${err.code},message:${err.message}`);
   14. return;
   15. }
   16. Logger.info('Succeeded in putting data.');
   17. });
   18. } catch (e) {
   19. let error = e as BusinessError;
   20. Logger.error(`An unexpected error occurred. Code:${error.code},message:${error.message}`);
   21. }
   22. })
   ```

   [KvStoreInterface.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/KvStore/KvStoreSamples/entry/src/main/ets/pages/KvStoreInterface.ets#L106-L129)
3. 使用backup()方法备份数据。

   ```
   1. public Backup = (() => {
   2. Logger.info('Backup start');
   3. if (kvStore === undefined) {
   4. Logger.info('Backup: kvStore not initialized');
   5. return;
   6. }
   7. let backupFile = 'BK001';
   8. try {
   9. kvStore.backup(backupFile, (err) => {
   10. if (err) {
   11. Logger.error(`Fail to backup data.code:${err.code},message:${err.message}`);
   12. } else {
   13. Logger.info('Succeeded in backing up data.');
   14. }
   15. });
   16. } catch (e) {
   17. let error = e as BusinessError;
   18. Logger.error(`An unexpected error occurred. Code:${error.code},message:${error.message}`);
   19. }
   20. })
   ```

   [KvStoreInterface.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/KvStore/KvStoreSamples/entry/src/main/ets/pages/KvStoreInterface.ets#L177-L198)
4. 使用delete()方法删除数据（模拟意外删除、篡改场景）。

   ```
   1. public Delete = (() => {
   2. Logger.info('DeleteData start');
   3. if (kvStore === undefined) {
   4. Logger.info('DeleteData: kvStore not initialized');
   5. return;
   6. }
   7. const KEY_TEST_STRING_ELEMENT = 'key_test_string';
   8. try {
   9. kvStore.delete(KEY_TEST_STRING_ELEMENT, (err) => {
   10. if (err !== undefined) {
   11. Logger.error(`Failed to delete data. Code:${err.code},message:${err.message}`);
   12. return;
   13. }
   14. Logger.info('Succeeded in deleting data.');
   15. });
   16. } catch (e) {
   17. let error = e as BusinessError;
   18. Logger.error(`An unexpected error occurred. Code:${error.code},message:${error.message}`);
   19. }
   20. })
   ```

   [KvStoreInterface.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/KvStore/KvStoreSamples/entry/src/main/ets/pages/KvStoreInterface.ets#L154-L175)
5. 使用restore()方法恢复数据。

   ```
   1. public Restore = (() => {
   2. Logger.info('Restore start');
   3. if (kvStore === undefined) {
   4. Logger.info('Restore: kvStore not initialized');
   5. return;
   6. }
   7. let backupFile = 'BK001';
   8. try {
   9. kvStore.restore(backupFile, (err) => {
   10. if (err) {
   11. Logger.error(`Fail to restore data. Code:${err.code},message:${err.message}`);
   12. } else {
   13. Logger.info('Succeeded in restoring data.');
   14. }
   15. });
   16. } catch (e) {
   17. let error = e as BusinessError;
   18. Logger.error(`An unexpected error occurred. Code:${error.code},message:${error.message}`);
   19. }
   20. })
   ```

   [KvStoreInterface.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/KvStore/KvStoreSamples/entry/src/main/ets/pages/KvStoreInterface.ets#L200-L221)
6. 当本地设备存储空间有限或需要重新备份时，还可使用deleteBackup()方法删除备份，释放存储空间。

   ```
   1. public DeleteBackup = (() => {
   2. Logger.info('DeleteBackup start');
   3. if (kvStore === undefined) {
   4. Logger.info('DeleteBackup: kvStore not initialized');
   5. return;
   6. }
   7. let backupFile = 'BK001';
   8. let files = [backupFile];
   9. try {
   10. kvStore.deleteBackup(files, (err: BusinessError, data: [string, number][]) => {
   11. if (err) {
   12. Logger.error(`Failed to delete Backup.code is ${err.code},message is ${err.message}`);
   13. } else {
   14. Logger.info(`Succeed in deleting Backup.data=${data}`);
   15. }
   16. });
   17. } catch (e) {
   18. let error = e as BusinessError;
   19. Logger.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
   20. }
   21. })
   ```

   [KvStoreInterface.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/KvStore/KvStoreSamples/entry/src/main/ets/pages/KvStoreInterface.ets#L223-L245)

## 关系型数据库备份

数据库操作或者存储过程中，有可能会因为各种原因发生非预期的数据库异常的情况，可以根据需要使用关系型数据库的备份能力，以便在数据库异常时，可靠高效地恢复数据保证业务数据正常使用。

关系型数据库支持手动备份和自动备份（仅系统应用可用）两种方式。

### 手动备份

手动备份：通过调用[backup](../harmonyos-references/arkts-apis-data-relationalstore-rdbstore.md#backup)接口实现数据库手动备份。示例如下：

```
1. import { relationalStore } from '@kit.ArkData';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { fileIo } from '@kit.CoreFileKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit'
5. import { UIContext } from '@kit.ArkUI';
6. import { common } from '@kit.AbilityKit';
```

[BackupAndRestore.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/RelationalStore/NativeDataEncryption/entry/src/main/ets/pages/backuprestore/BackupAndRestore.ets#L17-L22)

```
1. /* context为应用的上下文信息，由调用方自行获取，此处仅为示例。 */
2. const context = new UIContext().getHostContext() as common.UIAbilityContext;
3. let store: relationalStore.RdbStore | undefined = undefined;
4. const STORE_CONFIG: relationalStore.StoreConfig = {
5. name: 'RdbTest.db',
6. securityLevel: relationalStore.SecurityLevel.S3
7. };
8. try {
9. store = await relationalStore.getRdbStore(context, STORE_CONFIG);
10. await store.executeSql('CREATE TABLE IF NOT EXISTS EMPLOYEE (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, AGE INTEGER, SALARY REAL, CODES BLOB)');
11. hilog.info(DOMAIN, 'BackupAndRestore', 'Succeeded in getting RdbStore.');
12. } catch (e) {
13. const err = e as BusinessError;
14. hilog.error(DOMAIN, 'BackupAndRestore', `Failed to get RdbStore. Code:${err.code},message:${err.message}`);
15. }

17. if (!store) {
18. return;
19. }

21. try {
22. /**
23. * "Backup.db"为备份数据库文件名，默认在RdbStore同路径下备份。
24. * 也可指定绝对路径："/data/storage/el2/database/Backup.db"，文件路径需要存在，不会自动创建目录。
25. */
26. await store.backup('Backup.db');
27. hilog.info(DOMAIN, 'BackupAndRestore', `Succeeded in backing up RdbStore.`);
28. } catch (e) {
29. const err = e as BusinessError;
30. hilog.error(DOMAIN, 'BackupAndRestore', `Failed to backup RdbStore. Code:${err.code}, message:${err.message}`);
31. }
```

[BackupAndRestore.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/RelationalStore/NativeDataEncryption/entry/src/main/ets/pages/backuprestore/BackupAndRestore.ets#L35-L66)

## 关系型数据库异常重建

在创建或使用关系型数据库的过程中，抛出14800011异常错误码说明数据库出现异常，可以删除数据库后恢复数据。

需要通过在[StoreConfig](../harmonyos-references/arkts-apis-data-relationalstore-i.md#storeconfig)中配置allowRebuild参数为true以设置数据库在出现异常时自动删库。数据库重建成功后为空库，需要开发者重新建表并且使用提前备份好的数据进行数据恢复，备份操作可见[关系型数据库备份](data-backup-and-restore.md#关系型数据库备份)，数据恢复可见[关系型数据库恢复](data-backup-and-restore.md#关系型数据库数据恢复)。

若数据库异常前已配置StoreConfig中的allowRebuild为true，则数据库出现异常时将自动删库。

若数据库异常前未配置StoreConfig中的allowRebuild或allowRebuild配置为false，则需将其配置为true再次进行开库。具体示例如下：

```
1. let store: relationalStore.RdbStore | undefined = undefined;
2. /* context为应用的上下文信息，由调用方自行获取，此处仅为示例。 */
3. const context = new UIContext().getHostContext() as common.UIAbilityContext;
4. try {
5. const STORE_CONFIG: relationalStore.StoreConfig = {
6. name: 'RdbTest.db',
7. securityLevel: relationalStore.SecurityLevel.S3,
8. allowRebuild: true
9. };
10. store = await relationalStore.getRdbStore(context, STORE_CONFIG);
11. await store.executeSql('CREATE TABLE IF NOT EXISTS EMPLOYEE (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, AGE INTEGER, SALARY REAL, CODES BLOB)');
12. hilog.info(DOMAIN, 'BackupAndRestore', 'Succeeded in getting RdbStore.');
13. } catch (e) {
14. const err = e as BusinessError;
15. hilog.error(DOMAIN, 'BackupAndRestore', `Failed to get RdbStore. Code:${err.code}, message:${err.message}`);
16. }
```

[BackupAndRestore.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/RelationalStore/NativeDataEncryption/entry/src/main/ets/pages/backuprestore/BackupAndRestore.ets#L146-L162)

## 关系型数据库数据恢复

针对数据库出现异常的情况，在数据库重建成功后，需要用提前备份好的数据进行数据恢复。

恢复方式分以下两种，手动备份恢复和自动备份恢复（仅系统应用可用）。

### 恢复手动备份数据

关系型数据库通过调用backup接口可以实现[手动备份数据库](data-backup-and-restore.md#手动备份)，通过restore接口可以实现手动恢复数据库。

具体恢复过程和关键示例代码片段如下，完整示例代码请结合关系型数据库的备份、重建等上下文进行实现。

1. 抛出数据库异常错误码。

   ```
   1. let predicates = new relationalStore.RdbPredicates('EMPLOYEE');
   2. if (store != undefined) {
   3. (store as relationalStore.RdbStore).query(predicates, ['ID', 'NAME', 'AGE', 'SALARY', 'CODES'])
   4. .then((result: relationalStore.ResultSet) => {
   5. let resultSet = result;
   6. try {
   7. /* ...
   8. 业务的增删改逻辑
   9. ...
   10. */
   11. // 抛出异常
   12. if (resultSet?.rowCount == -1) {
   13. resultSet?.isColumnNull(0);
   14. }
   15. // todo resultSet.goToFirstRow()等其它接口也会抛异常
   16. while (resultSet.goToNextRow()) {
   17. hilog.info(DOMAIN, 'BackupAndRestore', JSON.stringify(resultSet.getRow()));
   18. }
   19. resultSet.close();
   20. } catch (err) {
   21. if (err.code === 14800011) {
   22. // 执行下文的步骤，即关闭结果集之后进行数据的恢复
   23. }
   24. hilog.info(DOMAIN, 'BackupAndRestore', JSON.stringify(err));
   25. }
   26. })
   27. }
   ```

   [BackupAndRestore.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/RelationalStore/NativeDataEncryption/entry/src/main/ets/pages/backuprestore/BackupAndRestore.ets#L83-L111)
2. 关闭所有打开着的结果集。

   ```
   1. let resultSets: relationalStore.ResultSet[] = []
   2. // 使用resultSet.close()方法关闭所有打开着的结果集
   3. for (let resultSet of resultSets) {
   4. try {
   5. resultSet.close();
   6. } catch (e) {
   7. if (e.code !== 14800014) {
   8. hilog.info(DOMAIN, 'BackupAndRestore', `Code:${e.code}, message:${e.message}`);
   9. }
   10. }
   11. }
   ```

   [BackupAndRestore.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/RelationalStore/NativeDataEncryption/entry/src/main/ets/pages/backuprestore/BackupAndRestore.ets#L114-L126)
3. 调用restore接口恢复数据。

   ```
   1. let store: relationalStore.RdbStore | undefined = undefined;
   2. /* context为应用的上下文信息，由调用方自行获取，此处仅为示例。 */
   3. const context = new UIContext().getHostContext() as common.UIAbilityContext;
   4. let STORE_CONFIG: relationalStore.StoreConfig = {
   5. name: 'RdbTest.db',
   6. securityLevel: relationalStore.SecurityLevel.S3,
   7. allowRebuild: true
   8. }
   9. try {
   10. /**
   11. * "Backup.db"为备份数据库文件名，默认在当前 store 所在路径下查找备份文件 Backup.db。
   12. * 如在备份时指定了绝对路径："/data/storage/el2/database/Backup.db", 需要传入绝对路径。
   13. */
   14. let backupFilePath = context.databaseDir + '/rdb/Backup.db';
   15. const backupExist: boolean = await fileIo.access(backupFilePath);
   16. if (!backupExist) {
   17. hilog.info(DOMAIN, 'BackupAndRestore', 'Backup is not exist.');
   18. // todo 开库建表
   19. // todo 自行生成数据
   20. return;
   21. }
   22. } catch (e) {
   23. hilog.info(DOMAIN, 'BackupAndRestore', `Code:${e.code}, message:${e.message}`);
   24. }

   26. try {
   27. store = await relationalStore.getRdbStore(context, STORE_CONFIG);
   28. // 调用restore接口恢复数据
   29. await store.restore('Backup.db');
   30. hilog.info(DOMAIN, 'BackupAndRestore', 'Restore from backup success.');
   31. } catch (e) {
   32. const err = e as BusinessError;
   33. hilog.error(DOMAIN, 'BackupAndRestore', `Failed to get RdbStore. Code:${err.code}, message:${err.message}`);
   34. }
   ```

   [BackupAndRestore.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/RelationalStore/NativeDataEncryption/entry/src/main/ets/pages/backuprestore/BackupAndRestore.ets#L169-L203)

## 示例代码

* [数据库的备份与恢复](https://gitcode.com/HarmonyOS_Samples/data-base-upgrade)
