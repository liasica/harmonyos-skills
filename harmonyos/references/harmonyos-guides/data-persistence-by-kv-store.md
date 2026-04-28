---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-persistence-by-kv-store
title: 通过键值型数据库实现数据持久化 (ArkTS)
breadcrumb: 指南 > 应用框架 > ArkData（方舟数据管理） > 应用数据持久化 > 通过键值型数据库实现数据持久化 (ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b6b8e76f026fd75f14672d4785cda58f5669eb35d00ee5ca6785f59ad802e9ca
---

## 场景介绍

键值型数据库存储键值对形式的数据，当需要存储的数据没有复杂的关系模型，比如存储商品名称及对应价格、员工工号及今日是否已出勤等，由于数据复杂度低，更容易兼容不同数据库版本和设备类型，因此推荐使用键值型数据库持久化此类数据。

## 约束限制

* 设备协同数据库，针对每条记录，Key的长度≤896 Byte，Value的长度<4 MB。
* 单版本数据库，针对每条记录，Key的长度≤1 KB，Value的长度<4 MB。
* 每个应用程序最多支持同时打开16个键值型分布式数据库。
* 键值型数据库事件回调方法中不允许进行阻塞操作，例如修改UI组件。

## 接口说明

以下是键值型数据库持久化功能的相关接口，更多接口及使用方式请见[分布式键值数据库](../harmonyos-references/js-apis-distributedkvstore.md)。

| 接口名称 | 描述 |
| --- | --- |
| createKVManager(config: KVManagerConfig): KVManager | 创建一个KVManager对象实例，用于管理数据库对象。 |
| getKVStore<T>(storeId: string, options: Options, callback: AsyncCallback<T>): void | 指定options和storeId，创建并得到指定类型的KVStore数据库。 |
| put(key: string, value: Uint8Array | string | number | boolean, callback: AsyncCallback<void>): void | 添加指定类型的键值对到数据库。 |
| get(key: string, callback: AsyncCallback<boolean | string | number | Uint8Array>): void | 获取指定键的值。 |
| delete(key: string, callback: AsyncCallback<void>): void | 从数据库中删除指定键值的数据。 |
| closeKVStore(appId: string, storeId: string, callback: AsyncCallback<void>): void | 通过storeId的值关闭指定的分布式键值数据库。 |
| deleteKVStore(appId: string, storeId: string, callback: AsyncCallback<void>): void | 通过storeId的值删除指定的分布式键值数据库。 |

## 开发步骤

1. 若要使用键值型数据库，首先要使用createKVManager()方法获取一个KVManager实例，用于管理数据库对象。示例代码如下所示：

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
   13. // Stage模型context从EntryAbility.ets中获取
   14. const context = EntryAbility.getContext();

   16. // FA模型获取context
   17. import { featureAbility } from '@kit.AbilityKit';
   18. import { BusinessError } from '@kit.BasicServicesKit';

   20. let context = featureAbility.getContext();

   22. // 下面所有接口的代码都实现在KvInterface中
   23. export class KvInterface {
   24. }
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
2. 使用getKVStore()方法创建并获取键值数据库。示例代码如下所示：

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
3. 使用on()方法订阅分布式数据变化，如需关闭订阅分布式数据变化，调用[off('dataChange')](../harmonyos-references/js-apis-distributedkvstore.md#offdatachange)关闭。示例代码如下所示：

   ```
   1. public On = (() =>{
   2. Logger.info('On start');
   3. if(kvStore === undefined) {
   4. Logger.info('On: kvStore not initialized');
   5. return;
   6. }
   7. try {
   8. kvStore.on('dataChange', distributedKVStore.SubscribeType.SUBSCRIBE_TYPE_ALL, (data) => {
   9. Logger.info(`dataChange callback call data: ${data}`);
   10. });
   11. } catch (e) {
   12. let error = e as BusinessError;
   13. Logger.error(`An unexpected error occurred. code:${error.code},message:${error.message}`);
   14. }
   15. })
   ```

   [KvStoreInterface.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/KvStore/KvStoreSamples/entry/src/main/ets/pages/KvStoreInterface.ets#L295-L311)
4. 调用put()方法向键值数据库中插入数据。示例代码如下所示：

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

   说明

   当Key值存在时，put()方法会修改其值，否则新增一条数据。
5. 调用get()方法获取指定键的值。示例代码如下所示：

   ```
   1. public Get = (() => {
   2. Logger.info('Get start');
   3. if (kvStore === undefined) {
   4. Logger.info('Get: kvStore not initialized');
   5. return;
   6. }
   7. const KEY_TEST_STRING_ELEMENT = 'key_test_string';
   8. try {
   9. kvStore.get(KEY_TEST_STRING_ELEMENT, (err, data) => {
   10. if (err != undefined) {
   11. Logger.error(`Failed to get data. Code:${err.code},message:${err.message}`);
   12. return;
   13. }
   14. Logger.info(`Succeeded in getting data. Data:${data}`);
   15. });
   16. } catch (e) {
   17. let error = e as BusinessError;
   18. Logger.error(`Failed to get data. Code:${error.code},message:${error.message}`);
   19. }
   20. })
   ```

   [KvStoreInterface.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/KvStore/KvStoreSamples/entry/src/main/ets/pages/KvStoreInterface.ets#L131-L152)
6. 调用delete()方法删除指定键值的数据。示例代码如下所示：

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
7. 调用closeKVStore()方法通过storeId的值关闭指定的分布式键值数据库。示例代码如下所示：

   ```
   1. public CloseKVStore = (()=>{
   2. Logger.info('CloseKVStore start');
   3. if (kvManager === undefined) {
   4. Logger.info('KvManager not initialized');
   5. return;
   6. }
   7. try {
   8. // appId为应用的bundleName
   9. kvStore = undefined;
   10. kvManager.closeKVStore(appId, storeId, (err: BusinessError)=> {
   11. if (err) {
   12. Logger.error(`Failed to close KVStore.code is ${err.code},message is ${err.message}`);
   13. return;
   14. }
   15. Logger.info('Succeeded in closing KVStore');
   16. });
   17. } catch (e) {
   18. let error = e as BusinessError;
   19. Logger.error(`An unexpected error occurred. Code:${error.code},message:${error.message}`);
   20. }
   21. })
   ```

   [KvStoreInterface.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/KvStore/KvStoreSamples/entry/src/main/ets/pages/KvStoreInterface.ets#L247-L269)
8. 调用deleteKVStore()方法通过storeId的值删除指定的分布式键值数据库。示例代码如下所示：

   ```
   1. public DeleteKvStore = (()=>{
   2. Logger.info('DeleteKvStore start');
   3. if (kvManager === undefined) {
   4. Logger.info('KvManager not initialized');
   5. return;
   6. }
   7. try {
   8. // appId为应用的bundleName
   9. kvStore = undefined;
   10. kvManager.deleteKVStore(appId, storeId, (err: BusinessError)=> {
   11. if (err) {
   12. Logger.error(`Failed to delete KVStore.code is ${err.code},message is ${err.message}`);
   13. return;
   14. }
   15. Logger.info('Succeeded in deleting KVStore');
   16. });
   17. } catch (e) {
   18. let error = e as BusinessError;
   19. Logger.error(`An unexpected error occurred. Code:${error.code},message:${error.message}`);
   20. }
   21. })
   ```

   [KvStoreInterface.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/KvStore/KvStoreSamples/entry/src/main/ets/pages/KvStoreInterface.ets#L271-L293)

## 示例代码

* [实现键值型数据库读写功能](https://gitcode.com/HarmonyOS_Samples/KVStore)
