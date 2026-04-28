---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-sync-of-kv-store
title: 键值型数据库跨设备数据同步 (ArkTS)
breadcrumb: 指南 > 应用框架 > ArkData（方舟数据管理） > 同应用跨设备数据同步（分布式） > 键值型数据库跨设备数据同步 (ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d4ff2959299facbe81e9fdebd2625dd508df37564847eaeeaf61f50c66ca30cb
---

## 场景介绍

键值型数据库适合不涉及过多数据关系和业务关系的业务数据存储，比SQL数据库存储拥有更好的读写性能，同时因其在分布式场景中降低了解决数据库版本兼容问题的复杂度，和数据端端同步过程中冲突解决的复杂度而被广泛使用。

## 基本概念

在使用键值型数据库跨设备数据端端同步前，请先了解以下概念。

### 单版本数据库

单版本是指数据在本地是以单个条目为单位的方式保存，当用户修改时，直接在这个条目上进行修改。在数据端端同步后多个设备全局只保留一份数据，多个设备的相同记录（主码相同）会按时间最新保留一条记录，数据不分设备，设备之间修改相同的key会覆盖。端端同步也以此为基础，按照它在本地被写入或更改的顺序将当前最新一次修改逐条同步至远端设备，常用于联系人、天气等应用存储场景。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/PliYIxSYRburMTLl_6gc9w/zh-cn_image_0000002583477523.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T233816Z&HW-CC-Expire=86400&HW-CC-Sign=9A9D5EC373574CED53C9F329E9844C5F433FA9FBED9EA141453A11E02FCE8B3F)

### 多设备协同数据库

多设备协同分布式数据库建立在单版本数据库之上，对应用程序存入的键值型数据中的Key前面拼接了本设备的DeviceID标识符，这样能保证每个设备产生的数据严格隔离。数据以设备的维度管理，不存在冲突；支持按照设备的维度查询数据。

底层按照设备的维度管理这些数据，多设备协同数据库支持以设备的维度查询分布式数据，但是不支持修改远端设备同步过来的数据。需要分开查询各设备数据的可以使用设备协同版本数据库。常用于图库缩略图存储场景。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/hSfvLY2cQRiPKRrk9SL3PA/zh-cn_image_0000002552797874.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T233816Z&HW-CC-Expire=86400&HW-CC-Sign=CC9AD878CF758393440DCBC9288CF2DBC269BCB59A88380AB4D8FADC40672C48)

## 端端同步方式

数据管理服务提供了两种同步方式：手动同步和自动同步。键值型数据库可选择其中一种方式实现同应用跨设备数据端端同步。

### 手动同步

由应用程序调用sync接口来触发，需要指定端端同步的设备列表和同步模式。同步模式分为PULL\_ONLY（将远端数据拉取到本端）、PUSH\_ONLY（将本端数据推送到远端）和PUSH\_PULL（将本端数据推送到远端同时也将远端数据拉取到本端）。[带有Query参数的端端同步接口](../harmonyos-references/js-apis-distributedkvstore.md#sync-1)，支持按条件过滤的方法进行端端同步，将符合条件的数据同步到远端。

### 自动同步

在跨设备Call调用实现的多端协同场景中，在应用程序更新数据后，由分布式数据库自动将本端数据推送到远端，同时也将远端数据拉取到本端来完成数据同步，应用不需要主动调用sync接口。

## 运作机制

底层通信组件完成设备发现和认证，会通知上层应用程序设备上线。收到设备上线的消息后数据管理服务可以在两个设备之间建立加密的数据传输通道，利用该通道在两个设备之间进行数据端端同步。

### 数据跨设备端端同步机制

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/WZN_ktBkS46nMWLWS3tHIQ/zh-cn_image_0000002583437569.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T233816Z&HW-CC-Expire=86400&HW-CC-Sign=9C4722473D40A5A6F02C63B94FF49B2A3D03C0624E2B3D274214CEAA6A117868)

如图所示，通过put、delete接口触发自动端端同步，将分布式数据通过通信适配层发送给对端设备，实现分布式数据的自动端端同步。

手动同步则是手动调用sync接口触发端端同步，将分布式数据通过通信适配层发送给对端设备。

### 数据变化通知机制

增、删、改数据时，会给订阅者发送数据变化的通知。主要分为本地数据变化通知和分布式数据变化通知。

* **本地数据变化通知**：本地设备的应用内订阅数据变化通知，数据库增删改数据时，会收到通知。
* **分布式数据变化通知**：同一应用订阅组网内其他设备数据变化的通知，其他设备增删改数据时，本设备会收到通知。

## 约束限制

* 设备协同数据库，针对每条记录，Key的长度≤896 Byte，Value的长度<4 MB。
* 单版本数据库，针对每条记录，Key的长度≤1 KB，Value的长度<4 MB。
* 键值型数据库不支持应用程序自定义冲突解决策略。
* 每个应用程序可以同时打开最多16个键值型分布式数据库。
* 单个数据库可以注册最多8个订阅数据变化的回调。

## 接口说明

以下是单版本键值型分布式数据库跨设备数据端端同步功能的相关接口，更多接口及使用方式请见[分布式键值数据库](../harmonyos-references/js-apis-distributedkvstore.md)。

| 接口名称 | 描述 |
| --- | --- |
| createKVManager(config: KVManagerConfig): KVManager | 创建一个KVManager对象实例，用于管理数据库对象。 |
| getKVStore<T>(storeId: string, options: Options, callback: AsyncCallback<T>): void | 指定options和storeId，创建并得到指定类型的KVStore数据库。 |
| put(key: string, value: Uint8Array | string | number | boolean, callback: AsyncCallback<void>): void | 插入和更新数据。 |
| on(event: 'dataChange', type: SubscribeType, listener: Callback<ChangeNotification>): void | 订阅数据库中数据的变化。 |
| get(key: string, callback: AsyncCallback<boolean | string | number | Uint8Array>): void | 查询指定Key键的值。 |
| sync(deviceIds: string[], mode: SyncMode, delayMs?: number): void | 在手动模式下，触发数据库端端同步。 |

## 开发步骤

此处以单版本键值型数据库跨设备数据端端同步的开发为例。以下是具体的开发流程和开发步骤。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/sHh_RUusSpqqKfH5OYQbmg/zh-cn_image_0000002552957524.png?HW-CC-KV=V1&HW-CC-Date=20260427T233816Z&HW-CC-Expire=86400&HW-CC-Sign=8736B3C8BEB75746CAC291964477712B5B9216178390D546C545BB70F41557F7)

说明

数据只允许向数据安全标签不高于对端设备安全等级的设备同步数据，具体规则可见[跨设备同步访问控制机制](access-control-by-device-and-data-level.md#跨设备同步访问控制机制)。

1. 导入模块获取context。

   ```
   1. // 导入模块
   2. // 在pages目录下新建KvStoreInterface.ets
   3. import { distributedKVStore } from '@kit.ArkData';
   4. import { BusinessError } from '@kit.BasicServicesKit';
   5. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
   6. import EntryAbility from '../entryability/EntryAbility';
   7. // Logger为hilog封装后实现的打印功能
   8. import Logger from '../common/Logger';

   10. let kvManager: distributedKVStore.KVManager | undefined = undefined;
   11. let kvStore: distributedKVStore.SingleKVStore | undefined = undefined;
   12. let appId: string = 'com.example.kvstoresamples';
   13. let storeId: string = 'storeId';
   14. // Stage模型context从EntryAbility.ets中获取
   15. const context = EntryAbility.getContext();

   17. // FA模型获取context
   18. import { featureAbility } from '@kit.AbilityKit';
   19. import { BusinessError } from '@kit.BasicServicesKit';

   21. let context = featureAbility.getContext();

   23. // 下面所有接口的代码都实现在KvInterface中
   24. export class KvInterface {
   25. }
   ```
2. 请求权限。

   1. 需要申请ohos.permission.DISTRIBUTED\_DATASYNC权限，配置方式请参见[声明权限](declare-permissions.md)。
   2. 同时需要在应用首次启动时弹窗向用户申请授权，使用方式请参见[向用户申请授权](request-user-authorization.md)。
3. 根据配置调用createKVManager()方法构造分布式数据库管理类实例。

   1. 根据应用上下文创建kvManagerConfig对象。
   2. 创建分布式数据库管理器实例。

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
4. 调用getKVStore()方法获取并得到指定类型的键值型数据库。

   1. 声明需要创建的分布式数据库ID描述（例如示例代码中的'storeId'）。
   2. 创建分布式数据库，建议关闭自动端端同步功能（autoSync:false），方便后续对端端同步功能进行验证，需要端端同步时主动调用sync接口。

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
5. 调用on()方法订阅分布式数据变化，如需关闭订阅分布式数据变化，调用[off('dataChange')](../harmonyos-references/js-apis-distributedkvstore.md#offdatachange)关闭。

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
6. 调用put()方法将数据写入分布式数据库。

   1. 构造需要写入分布式数据库的Key（键）和Value（值）。
   2. 将键值数据写入分布式数据库。

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
7. 调用get()方法查询分布式数据库数据。

   1. 构造需要从单版本分布式数据库中查询的Key（键）。
   2. 从单版本分布式数据库中获取数据。

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
8. 调用sync()方法同步数据到其他设备。

   选择同一组网环境下的设备以及同步模式（需用户在应用首次启动的弹窗中确认选择同步模式），进行数据端端同步。

   说明

   在手动端端同步的方式下，其中的deviceIds通过调用[devManager.getAvailableDeviceListSync](../harmonyos-references/js-apis-distributeddevicemanager.md#getavailabledevicelistsync)方法得到。

   ```
   1. public Sync = (() =>{
   2. Logger.info('Sync start');
   3. if(kvStore === undefined) {
   4. Logger.info('Sync: kvStore not initialized');
   5. return;
   6. }
   7. let devManager: distributedDeviceManager.DeviceManager;
   8. try {
   9. // create deviceManager
   10. devManager = distributedDeviceManager.createDeviceManager(context.applicationInfo.name);
   11. // deviceIds由deviceManager调用getAvailableDeviceListSync方法得到
   12. let deviceIds: string[] = [];
   13. if (devManager != null) {
   14. let devices = devManager.getAvailableDeviceListSync();
   15. for (let i = 0; i < devices.length; i++) {
   16. deviceIds[i] = devices[i].networkId as string;
   17. }
   18. }
   19. if (deviceIds.length === 0) {
   20. Logger.info('Sync failed networkId is empty.');
   21. return;
   22. }
   23. try {
   24. // 1000表示最大延迟时间为1000ms
   25. kvStore.sync(deviceIds, distributedKVStore.SyncMode.PUSH_PULL, 1000);
   26. } catch (e) {
   27. let error = e as BusinessError;
   28. Logger.error(`An unexpected error occurred. Code:${error.code},message:${error.message}`);
   29. }
   30. } catch (err) {
   31. let error = err as BusinessError;
   32. Logger.error('createDeviceManager errCode:' + error.code + ',errMessage:' + error.message);
   33. }
   34. })
   ```

   [KvStoreInterface.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/KvStore/KvStoreSamples/entry/src/main/ets/pages/KvStoreInterface.ets#L313-L348)
