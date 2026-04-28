---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-cloud-sync-of-rdb-store
title: 端云数据同步关系型数据库端侧开发指导 (ArkTS)
breadcrumb: 指南 > 应用框架 > ArkData（方舟数据管理） > 同应用端云数据同步（分布式） > 端云数据同步关系型数据库端侧开发指导 (ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:20+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:e71b08f203d091cb836815c3a86b18931cf9f4925f473334a2ae670ce560d9a6
---

## 场景介绍

端云数据同步：关系型数据库提供端云同步的能力，云作为数据的中心节点，设备通过与云的数据同步，实现同账号设备间的数据一致性。

说明

从HarmonyOS 6.1.0开始，支持使用关系型数据库实现端云数据同步。

## 约束限制

* 每个应用程序最多支持同时打开16个关系型分布式数据库。
* 单个数据库最多支持注册8个订阅数据变化的回调。
* 安全级别为S4的数据库不能同步至云端。
* 单个资产大小的支持范围为1B~50G。
* 设备之间相同表的主键要确保唯一（尤其不能使用自增主键）。
* 删除资产相关数据时，端云同步不主动删除本地资产文件，需要应用自行管理。
* 端云同步表的列只能新增，不能修改和删除，否则会出现不兼容问题。
* 资产名默认填写成同步表中对应的资产类型列名。
* 关系型数据库支持SQLite数据类型和SQLite约束（其中NOT NULL约束无需添加）。

## 接口说明

以下为使用关系型数据库实现端云数据同步的相关接口，更多接口及使用方式可见[关系型数据库](../harmonyos-references/js-apis-data-relationalstore.md)和[端云服务](../harmonyos-references/js-apis-data-clouddata.md)。

| 接口名称 | 描述 |
| --- | --- |
| getRdbStore(context: Context, config: StoreConfig): Promise<RdbStore> | 指定context和config，创建并得到指定类型的RdbStore数据库。 |
| setDistributedTables(tables: Array<string>, type?: DistributedType, config?: DistributedConfig): Promise<void> | 设置分布式数据库表。 |
| on(event: 'dataChange', type: SubscribeType, observer: Callback<Array<string>>| Callback<Array<ChangeInfo>>): void | 注册数据库的数据变更的事件监听。当分布式数据库或本地数据库中的数据发生更改时，将调用回调。 |
| off(event:'dataChange', type: SubscribeType, observer?: Callback<Array<string>>| Callback<Array<ChangeInfo>>): void | 取消数据变更的事件监听。 |
| cloudSync(mode: SyncMode, tables: string[], progress: Callback<ProgressDetails>, callback: AsyncCallback<void>): void | 手动执行对指定表的端云同步。 |
| setCloudStrategy(strategy: StrategyType, param?: Array<commonType.ValueType>): Promise<void> | 设置应用自身的云同步策略，若未设置，则执行全局策略setGlobalCloudStrategy，全局策略若未设置，默认使用WIFI和蜂窝策略。 |

## 开发步骤

以设备A发生数据变更，设备B订阅数据变化通知实现端-云-端数据同步为例。

1. 导入模块。

   ```
   1. import { relationalStore,cloudData } from '@kit.ArkData';
   ```
2. 设备A创建关系型数据库，设置端云同步分布式表。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';

   3. let store:relationalStore.RdbStore | undefined = undefined
   4. // 创建关系型数据库，设置端云同步分布式表
   5. const STORE_CONFIG: relationalStore.StoreConfig = {
   6. name: 'RdbTest.db', // 数据库文件名
   7. securityLevel: relationalStore.SecurityLevel.S1 // 数据库安全级别
   8. };
   9. store = await relationalStore.getRdbStore(getContext(), STORE_CONFIG);
   10. try {
   11. if (store != undefined) {
   12. await store.executeSql('CREATE TABLE IF NOT EXISTS EMPLOYEE(employeeId TEXT PRIMARY KEY,NAME TEXT NOT NULL,AGE INTEGER,SALARY REAL NOT NULL,CODES BLOASSET ASSET)',
   13. null);
   14. await store.executeSql('CREATE TABLE IF NOT EXISTS SALARY(costId TEXT PRIMARY KEY,employeeId TEXT,SALARY REAL NOT NULL, performance_SALARY REAL, BONOUREAL)',
   15. null);
   16. // 设置分布式同步表，支持表在设备和云端之间分布式
   17. let config: relationalStore.DistributedConfig = {
   18. autoSync: true // true表示该表支持自动同步和手动同步，false表示该表只支持手动同步，不支持自动同步
   19. };
   20. // 设置分布式数据库表
   21. store.setDistributedTables(["EMPLOYEE", "SALARY"], relationalStore.DistributedType.DISTRIBUTED_CLOUD, config);
   22. // 进行数据的相关操作.....
   23. }
   24. } catch (err) {
   25. console.error(`executeSql or setDistributedTables failed,errcode:${JSON.stringify(err)}.`);
   26. }
   ```
3. 设备B设置端云同步策略。

   ```
   1. try {
   2. // 设置网络策略为仅允许WIFI网络同步
   3. await cloudData.setCloudStrategy(cloudData.StrategyType.NETWORK, [cloudData.NetWorkStrategy.WIFI]).then(() => {
   4. console.info(`setCloudStrategy success.`);
   5. }).catch((err: BusinessError) => {
   6. console.error(`setCloudStrategy failed,errcode:${JSON.stringify(err)}.`);
   7. });
   8. } catch (err) {
   9. console.error(`setCloudStrategy failed,errcode:${JSON.stringify(err)}.`);
   10. }
   ```
4. 端云数据同步。

   * 当步骤2中autoSync设置为true时，表示已开启端云数据自动同步。云侧数据变化通知不一定会及时，此时如果设备B确认设备A数据发生了变化，可以执行cloudSync()方法进行手动同步。
   * 当步骤2中autoSync设置为false时，不支持端云数据自动同步，只能通过手动执行同步方法进行端云同步。

     ```
     1. try {
     2. if (store != undefined) {
     3. // 手动执行对指定表的端云同步，使用SYNC_MODE_TIME_FIRST模式，进行手动同步，表示数据从修改时间较近的一端同步到修改时间较远的一端。
     4. const tables = ["table1", "table2"];
     5. store.cloudSync(relationalStore.SyncMode.SYNC_MODE_TIME_FIRST, tables, (ProgressDetails: relationalStore.ProgressDetails)=> {
     6. console.info("Progress:" + `\n` + JSON.stringify(ProgressDetails));
     7. }, (err: BusinessError) => {
     8. if (err) {
     9. console.error(`Cloud sync failed,code is ${err. code},message is ${err.message}`);
     10. return;
     11. }
     12. console.info(`Cloud sync success`);
     13. });
     14. }
     15. } catch (err) {
     16. console.error(`cloudSync failed,errcode:${JSON.stringify(err)}.`);
     17. }
     ```
5. 设备B订阅数据变化通知监听。

   只有订阅后的端侧设备才能收到通知，当进程终止或崩溃后无法收到通知。如果需要在启动时获取云端数据变化，可以使用cursor进行查询。

   ```
   1. let accountObserver = (accounts: Array<string>) => {
   2. for (let i = 0; i < accounts.length; i++) {
   3. console.info(`${accounts[i]} data changed`);
   4. }
   5. }

   7. try {
   8. // 订阅云端数据更改,需要传入accountObserver函数
   9. if (store != undefined) {
   10. (store as relationalStore.RdbStore).on("dataChange", relationalStore.SubscribeType.SUBSCRIBE_TYPE_CLOUD, accountObserver);
   11. }
   12. } catch (err) {
   13. console.error(`Register observer failed,code is ${err.code},message is ${err.message}`);
   14. }

   16. try {
   17. // 当前不需要订阅端云数据变化时，可以将其取消
   18. if(store != undefined) {
   19. (store as relationalStore.RdbStore).off('dataChange', relationalStore.SubscribeType.SUBSCRIBE_TYPE_CLOUD, accountObserver);
   20. }
   21. } catch (err) {
   22. let code = (err as BusinessError).code;
   23. let message = (err as BusinessError).message
   24. console.error(`Unregister observer failed, code is ${code},message is ${message}`);
   25. }
   ```
6. 设备B收到数据变化通知后，可以使用cursor查询云侧数据变化。

   * 通过cursor可以查询同步表中变化的数据。数据管理会给每行数据绑定一个cursor字段，每次增删改都会将cursor字段赋值为最大值+1。应用通过使用predicates.greaterThan(relationalStore.Field.CURSOR\_FIELD, currentCursor)传入上次的最大cursor，如果数据经过更改，数据库会返回比上次更大的curosr。
   * 开库需要把autoCleanDirtyData字段设置为false，不然感知不到删除的数据。autoCleanDirtyData字段设置为false之后，云端删除数据时并不会删除本地数据，应用可以通过cursor查询到删除的数据，需要调用cleanDirtyData方法删除本地数据。

     ```
     1. const STORE_CONFIG: relationalStore.StoreConfig = {
     2. name: 'RdbTest.db',
     3. autoCleanDirtyData: false,
     4. securityLevel: relationalStore.SecurityLevel.S1
     5. };
     6. store = await relationalStore.getRdbStore(getContext(), STORE_CONFIG);
     7. // ...
     8. // 此处需要应用获取之前保存的cursor: getCursor()
     9. // 获取应用上次已同步的cursor，需要应用自己持久化
     10. let currentCursor: number = 0; // 已获取的上次同步cursor
     11. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
     12. predicates.greaterThan(relationalStore.Field.CURSOR_FIELD, currentCursor);
     13. predicates.and();
     14. // 只获取云端变化的数据
     15. predicates.equalTo(relationalStore.Field.ORIGIN_FIELD, relationalStore.Origin.CLOUD);
     16. predicates.orderByAsc(relationalStore.Field.CURSOR_FIELD);
     17. if (store == undefined) {
     18. return;
     19. }
     20. // uuid：同步表中的主键
     21. let resultSet: relationalStore.ResultSet = await store.query(predicates, ["uuid"]);
     22. if (!resultSet || !resultSet.goToFirstRow()) {
     23. return;
     24. }
     25. let cursor: number = 0;
     26. let deleteFlag: number = 0;
     27. do {
     28. cursor = resultSet.getLong(resultSet.getColumnIndex(relationalStore.Field.CURSOR_FIELD));
     29. deleteFlag = resultSet.getLong(resultSet.getColumnIndex(relationalStore.Field.DELETED_FLAG_FIELD));
     30. // 判断应用是否存在端云同步删除操作
     31. if (deleteFlag) {
     32. // 处理删除逻辑
     33. } else {
     34. // 处理非删除逻辑
     35. }
     36. } while (resultSet.goToNextRow());
     37. // 清理脏数据
     38. store.cleanDirtyData("EMPLOYEE", cursor);
     39. // 保存新的cursor值，以便下次获取数据同步更新使用
     40. // SaveCursor("EMPLOYEE", cursor)
     41. resultSet.close();
     ```
