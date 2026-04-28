---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributed-data
title: @ohos.data.distributedData (分布式数据管理)
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > ArkTS API > 已停止维护的接口 > @ohos.data.distributedData (分布式数据管理)
category: harmonyos-references
scraped_at: 2026-04-28T07:59:22+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:746c15efde7421d3f81f1cb587ccce322c0a199a0db89c79ea797b1aa9ad443c
---

分布式数据管理为应用程序提供不同设备间数据库的分布式协同能力。通过调用分布式数据各个接口，应用程序可将数据保存到分布式数据库中，并可对分布式数据库中的数据进行增加、删除、修改、查询、同步等操作。

该模块提供以下分布式数据管理相关的常用功能：

* [KVManager](js-apis-distributed-data.md#kvmanager)：数据管理实例，用于获取KVStore的相关信息。
* [KvStoreResultSet8+](js-apis-distributed-data.md#kvstoreresultset8)：提供获取KVStore数据库结果集的相关方法，包括查询和移动数据读取位置等。
* [Query8+](js-apis-distributed-data.md#query8)：使用谓词表示数据库查询，提供创建Query实例、查询数据库中的数据和添加谓词的方法。
* [KVStore](js-apis-distributed-data.md#kvstore)：KVStore数据库实例，提供增加数据、删除数据和订阅数据变更、订阅数据同步完成的方法。
* [SingleKVStore](js-apis-distributed-data.md#singlekvstore)：单版本分布式数据库，继承自[KVStore](js-apis-distributed-data.md#kvstore)，不对数据所属设备进行区分，提供查询数据和同步数据的方法。
* [DeviceKVStore8+](js-apis-distributed-data.md#devicekvstore8)：设备协同数据库，继承自[KVStore](js-apis-distributed-data.md#kvstore)，以设备维度对数据进行区分，提供查询数据和同步数据的方法。

说明

* 从API Version 9开始，该接口不再维护，推荐使用新接口[@ohos.data.distributedKVStore](js-apis-distributedkvstore.md)。
* 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块中所有需要获取deviceId的接口，都仅系统应用可用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import distributedData from '@ohos.data.distributedData';
```

## distributedData.createKVManager

PhonePC/2in1TabletTVWearable

createKVManager(config: KVManagerConfig, callback: AsyncCallback<KVManager>): void

创建一个KVManager对象实例，用于管理数据库对象，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [KVManagerConfig](js-apis-distributed-data.md#kvmanagerconfig) | 是 | 提供KVManager实例的配置信息，包括调用方的Bundle名称和用户信息。 |
| callback | AsyncCallback<[KVManager](js-apis-distributed-data.md#kvmanager)> | 是 | 回调函数。返回创建的KVManager对象实例。 |

**示例：**

```
1. let kvManager;
2. try {
3. const kvManagerConfig = {
4. bundleName : 'com.example.datamanagertest',
5. userInfo : {
6. userId : '0',
7. userType : distributedData.UserType.SAME_USER_ID
8. }
9. }
10. distributedData.createKVManager(kvManagerConfig, function (err, manager) {
11. if (err) {
12. console.log("Failed to create KVManager: "  + JSON.stringify(err));
13. return;
14. }
15. console.log("Succeeded in creating KVManager");
16. kvManager = manager;
17. });
18. } catch (e) {
19. console.log("An unexpected error occurred. Error:" + e);
20. }
```

## distributedData.createKVManager

PhonePC/2in1TabletTVWearable

createKVManager(config: KVManagerConfig): Promise<KVManager>

创建一个KVManager对象实例，用于管理数据库对象，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [KVManagerConfig](js-apis-distributed-data.md#kvmanager) | 是 | 提供KVManager实例的配置信息，包括调用方的包名和用户信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[KVManager](js-apis-distributed-data.md#kvmanager)> | Promise对象。返回创建的KVManager对象实例。 |

**示例：**

```
1. try {
2. const kvManagerConfig = {
3. bundleName: 'com.example.datamanagertest',
4. userInfo: {
5. userId: '0',
6. userType: distributedData.UserType.SAME_USER_ID
7. }
8. }
9. distributedData.createKVManager(kvManagerConfig).then((manager) => {
10. console.log("Succeeded in creating KVManager");
11. kvManager = manager;
12. }).catch((err) => {
13. console.error("Failed to create KVManager: " + JSON.stringify(err));
14. });
15. } catch (e) {
16. console.log("An unexpected error occurred. Error:" + e);
17. }
```

## KVManagerConfig

PhonePC/2in1TabletTVWearable

提供KVManager实例的配置信息，包括调用方的Bundle名称和用户信息。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userInfo | [UserInfo](js-apis-distributed-data.md#userinfo) | 是 | 调用方的用户信息。 |
| bundleName | string | 是 | 调用方的Bundle名称。 |

## UserInfo

PhonePC/2in1TabletTVWearable

用户信息。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userId | string | 否 | 指示要设置的用户ID，默认为'0'。 |
| userType | [UserType](js-apis-distributed-data.md#usertype) | 否 | 指示要设置的用户类型，默认为0。 |

## UserType

PhonePC/2in1TabletTVWearable

用户类型枚举。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SAME\_USER\_ID | 0 | 使用同一账号登录不同设备的用户。 |

## KVManager

PhonePC/2in1TabletTVWearable

数据管理实例，用于获取KVStore的相关信息。在调用KVManager的方法前，需要先通过[createKVManager](js-apis-distributed-data.md#distributeddatacreatekvmanager)构建一个KVManager实例。

### getKVStore

PhonePC/2in1TabletTVWearable

getKVStore<T extends KVStore>(storeId: string, options: Options, callback: AsyncCallback<T>): void

通过指定Options和storeId，创建并获取KVStore数据库，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| storeId | string | 是 | 数据库唯一标识符，长度不大于[MAX\_STORE\_ID\_LENGTH](js-apis-distributed-data.md#constants)。 |
| options | [Options](js-apis-distributed-data.md#options) | 是 | 创建KVStore实例的配置信息。 |
| callback | AsyncCallback<T> | 是 | 回调函数。返回创建的KVStore数据库实例。 |

**示例：**

```
1. let kvStore;
2. let kvManager;
3. try {
4. const options = {
5. createIfMissing : true,
6. encrypt : false,
7. backup : false,
8. autoSync : true,
9. kvStoreType : distributedData.KVStoreType.SINGLE_VERSION,
10. securityLevel : distributedData.SecurityLevel.S3,
11. };
12. kvManager.getKVStore('storeId', options, function (err, store) {
13. if (err) {
14. console.log("getKVStore err: "  + JSON.stringify(err));
15. return;
16. }
17. console.log("getKVStore success");
18. kvStore = store;
19. });
20. } catch (e) {
21. console.log("An unexpected error occurred. Error:" + e);
22. }
```

### getKVStore

PhonePC/2in1TabletTVWearable

getKVStore<T extends KVStore>(storeId: string, options: Options): Promise<T>

通过指定Options和storeId，创建并获取KVStore数据库，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| storeId | string | 是 | 数据库唯一标识符，长度不大于[MAX\_STORE\_ID\_LENGTH](js-apis-distributed-data.md#constants)。 |
| options | [Options](js-apis-distributed-data.md#options) | 是 | 创建KVStore实例的配置信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<T> ，<T extends [KVStore](js-apis-distributed-data.md#kvstore)> | Promise对象。返回创建的KVStore数据库实例。 |

**示例：**

```
1. let kvStore;
2. let kvManager;
3. try {
4. const options = {
5. createIfMissing : true,
6. encrypt : false,
7. backup : false,
8. autoSync : true,
9. kvStoreType : distributedData.KVStoreType.SINGLE_VERSION,
10. securityLevel : distributedData.SecurityLevel.S3,
11. };
12. kvManager.getKVStore('storeId', options).then((store) => {
13. console.log("getKVStore success");
14. kvStore = store;
15. }).catch((err) => {
16. console.log("getKVStore err: "  + JSON.stringify(err));
17. });
18. } catch (e) {
19. console.log("An unexpected error occurred. Error:" + e);
20. }
```

### closeKVStore8+

PhonePC/2in1TabletTVWearable

closeKVStore(appId: string, storeId: string, kvStore: KVStore, callback: AsyncCallback<void>): void

通过storeId的值关闭指定的KVStore数据库，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appId | string | 是 | 所调用数据库方的包名。 |
| storeId | string | 是 | 要关闭的数据库唯一标识符，长度不大于[MAX\_STORE\_ID\_LENGTH](js-apis-distributed-data.md#constants)。 |
| kvStore | [KVStore](js-apis-distributed-data.md#kvstore) | 是 | 要关闭的KVStore数据库。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. let kvStore;
2. let kvManager;
3. const options = {
4. createIfMissing: true,
5. encrypt: false,
6. backup: false,
7. autoSync: false,
8. kvStoreType: distributedData.KVStoreType.SINGLE_VERSION,
9. schema: undefined,
10. securityLevel: distributedData.SecurityLevel.S3,
11. }
12. try {
13. kvManager.getKVStore('storeId', options, async function (err, store) {
14. console.log('getKVStore success');
15. kvStore = store;
16. kvManager.closeKVStore('appId', 'storeId', kvStore, function (err, data) {
17. console.log('closeKVStore success');
18. });
19. });
20. } catch (e) {
21. console.log('closeKVStore e ' + e);
22. }
```

### closeKVStore8+

PhonePC/2in1TabletTVWearable

closeKVStore(appId: string, storeId: string, kvStore: KVStore): Promise<void>

通过storeId的值关闭指定的KVStore数据库，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appId | string | 是 | 所调用数据库方的包名。 |
| storeId | string | 是 | 要关闭的数据库唯一标识符，长度不大于[MAX\_STORE\_ID\_LENGTH](js-apis-distributed-data.md#constants)。 |
| kvStore | [KVStore](js-apis-distributed-data.md#kvstore) | 是 | 要关闭的KVStore数据库。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. let kvManager;
2. let kvStore;
3. const options = {
4. createIfMissing: true,
5. encrypt: false,
6. backup: false,
7. autoSync: false,
8. kvStoreType: distributedData.KVStoreType.SINGLE_VERSION,
9. schema: undefined,
10. securityLevel: distributedData.SecurityLevel.S3,
11. }
12. try {
13. kvManager.getKVStore('storeId', options).then(async (store) => {
14. console.log('getKVStore success');
15. kvStore = store;
16. kvManager.closeKVStore('appId', 'storeId', kvStore).then(() => {
17. console.log('closeKVStore success');
18. }).catch((err) => {
19. console.log('closeKVStore err ' + JSON.stringify(err));
20. });
21. }).catch((err) => {
22. console.log('CloseKVStore getKVStore err ' + JSON.stringify(err));
23. });
24. } catch (e) {
25. console.log('closeKVStore e ' + e);
26. }
```

### deleteKVStore8+

PhonePC/2in1TabletTVWearable

deleteKVStore(appId: string, storeId: string, callback: AsyncCallback<void>): void

通过storeId的值删除指定的KVStore数据库，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appId | string | 是 | 所调用数据库方的包名。 |
| storeId | string | 是 | 要删除的数据库唯一标识符，长度不大于[MAX\_STORE\_ID\_LENGTH](js-apis-distributed-data.md#constants)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. let kvManager;
2. let kvStore;
3. const options = {
4. createIfMissing : true,
5. encrypt : false,
6. backup : false,
7. autoSync : true,
8. kvStoreType : distributedData.KVStoreType.SINGLE_VERSION,
9. schema : undefined,
10. securityLevel : distributedData.SecurityLevel.S3,
11. }
12. try {
13. kvManager.getKVStore('store', options, async function (err, store) {
14. console.log('getKVStore success');
15. kvStore = store;
16. kvManager.deleteKVStore('appId', 'storeId', function (err, data) {
17. console.log('deleteKVStore success');
18. });
19. });
20. } catch (e) {
21. console.log('DeleteKVStore e ' + e);
22. }
```

### deleteKVStore8+

PhonePC/2in1TabletTVWearable

deleteKVStore(appId: string, storeId: string): Promise<void>

通过storeId的值删除指定的KVStore数据库，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appId | string | 是 | 所调用数据库方的包名。 |
| storeId | string | 是 | 要删除的数据库唯一标识符，长度不大于[MAX\_STORE\_ID\_LENGTH](js-apis-distributed-data.md#constants)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. let kvManager;
2. let kvStore;
3. const options = {
4. createIfMissing : true,
5. encrypt : false,
6. backup : false,
7. autoSync : true,
8. kvStoreType : distributedData.KVStoreType.SINGLE_VERSION,
9. schema : undefined,
10. securityLevel : distributedData.SecurityLevel.S3,
11. }
12. try {
13. kvManager.getKVStore('storeId', options).then(async (store) => {
14. console.log('getKVStore success');
15. kvStore = store;
16. kvManager.deleteKVStore('appId', 'storeId').then(() => {
17. console.log('deleteKVStore success');
18. }).catch((err) => {
19. console.log('deleteKVStore err ' + JSON.stringify(err));
20. });
21. }).catch((err) => {
22. console.log('getKVStore err ' + JSON.stringify(err));
23. });
24. } catch (e) {
25. console.log('deleteKVStore e ' + e);
26. }
```

### getAllKVStoreId8+

PhonePC/2in1TabletTVWearable

getAllKVStoreId(appId: string, callback: AsyncCallback<string[]>): void

获取所有通过[getKVStore](js-apis-distributed-data.md#getkvstore)方法创建的且没有调用[deleteKVStore](js-apis-distributed-data.md#deletekvstore8)方法删除的KVStore数据库的storeId，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appId | string | 是 | 所调用数据库方的包名。 |
| callback | AsyncCallback<string[]> | 是 | 回调函数。返回所有创建的KvStore数据库的storeId。 |

**示例：**

```
1. let kvManager;
2. try {
3. kvManager.getAllKVStoreId('appId', function (err, data) {
4. console.log('GetAllKVStoreId success');
5. console.log('GetAllKVStoreId size = ' + data.length);
6. });
7. } catch (e) {
8. console.log('GetAllKVStoreId e ' + e);
9. }
```

### getAllKVStoreId8+

PhonePC/2in1TabletTVWearable

getAllKVStoreId(appId: string): Promise<string[]>

获取所有通过[getKVStore](js-apis-distributed-data.md#getkvstore)方法创建的且没有调用[deleteKVStore](js-apis-distributed-data.md#deletekvstore8)方法删除的KVStore数据库的storeId，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appId | string | 是 | 所调用数据库方的包名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string[]> | Promise对象。返回所有创建的KvStore数据库的storeId。 |

**示例：**

```
1. let kvManager;
2. try {
3. console.log('GetAllKVStoreId');
4. kvManager.getAllKVStoreId('appId').then((data) => {
5. console.log('getAllKVStoreId success');
6. console.log('size = ' + data.length);
7. }).catch((err) => {
8. console.log('getAllKVStoreId err ' + JSON.stringify(err));
9. });
10. } catch(e) {
11. console.log('getAllKVStoreId e ' + e);
12. }
```

### on('distributedDataServiceDie')8+

PhonePC/2in1TabletTVWearable

on(event: 'distributedDataServiceDie', deathCallback: Callback<void>): void

订阅服务状态变更通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 订阅的事件名，固定为'distributedDataServiceDie'，即服务状态变更事件。 |
| deathCallback | Callback<void> | 是 | 回调函数。 |

**示例：**

```
1. let kvManager;
2. try {
3. console.log('KVManagerOn');
4. const deathCallback = function () {
5. console.log('death callback call');
6. }
7. kvManager.on('distributedDataServiceDie', deathCallback);
8. } catch (e) {
9. console.log("An unexpected error occurred. Error:" + e);
10. }
```

### off('distributedDataServiceDie')8+

PhonePC/2in1TabletTVWearable

off(event: 'distributedDataServiceDie', deathCallback?: Callback<void>): void

取消订阅服务状态变更通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取消订阅的事件名，固定为'distributedDataServiceDie'，即服务状态变更事件。 |
| deathCallback | Callback<void> | 否 | 取消订阅的函数。如不设置callback，则取消所有已订阅的函数。 |

**示例：**

```
1. let kvManager;
2. try {
3. console.log('KVManagerOff');
4. const deathCallback = function () {
5. console.log('death callback call');
6. }
7. kvManager.off('distributedDataServiceDie', deathCallback);
8. } catch (e) {
9. console.log("An unexpected error occurred. Error:" + e);
10. }
```

## Options

PhonePC/2in1TabletTVWearable

用于提供创建数据库的配置信息。

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| createIfMissing | boolean | 否 | 当数据库文件不存在时是否创建数据库，默认为true，即创建。  **系统能力：** SystemCapability.DistributedDataManager.KVStore.Core |
| encrypt | boolean | 否 | 设置数据库文件是否加密，默认为false，即不加密。  **系统能力：** SystemCapability.DistributedDataManager.KVStore.Core |
| backup | boolean | 否 | 设置数据库文件是否备份，默认为true，即备份。  **系统能力：** SystemCapability.DistributedDataManager.KVStore.Core |
| autoSync | boolean | 否 | 设置数据库文件是否自动同步。默认为false，即手动同步。  **系统能力：** SystemCapability.DistributedDataManager.KVStore.Core  **需要权限**： ohos.permission.DISTRIBUTED\_DATASYNC |
| kvStoreType | [KVStoreType](js-apis-distributed-data.md#kvstoretype) | 否 | 设置要创建的数据库类型，默认为DEVICE\_COLLABORATION，即多设备协同数据库。  **系统能力：** SystemCapability.DistributedDataManager.KVStore.Core |
| securityLevel | [SecurityLevel](js-apis-distributed-data.md#securitylevel) | 否 | 设置数据库安全级别(S1-S4)。  **系统能力：** SystemCapability.DistributedDataManager.KVStore.Core |
| schema8+ | [Schema](js-apis-distributed-data.md#schema8) | 否 | 设置定义存储在数据库中的值，默认为undefined，即不使用schema。  **系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore |

## KVStoreType

PhonePC/2in1TabletTVWearable

KVStore数据库类型枚举。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEVICE\_COLLABORATION | 0 | 表示多设备协同数据库。  **数据库特点：** 数据以设备的维度管理，不存在冲突；支持按照设备的维度查询数据。  **系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore |
| SINGLE\_VERSION | 1 | 表示单版本数据库。  **数据库特点：** 数据不分设备，设备之间修改相同的key会覆盖。  **系统能力：** SystemCapability.DistributedDataManager.KVStore.Core |
| MULTI\_VERSION | 2 | 表示多版本数据库。当前暂不支持使用此接口。  **系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore |

## SecurityLevel

PhonePC/2in1TabletTVWearable

数据库的安全级别枚举。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NO\_LEVEL | 0 | 表示数据库不设置安全级别(已废弃)。  **系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore |
| S0 | 1 | 表示数据库的安全级别为公共级别(已废弃)。  **系统能力：** SystemCapability.DistributedDataManager.KVStore.Core |
| S1 | 2 | 表示数据库的安全级别为低级别，当数据泄露时会产生较低影响。例如，包含壁纸等系统数据的数据库。  **系统能力：** SystemCapability.DistributedDataManager.KVStore.Core |
| S2 | 3 | 表示数据库的安全级别为中级别，当数据泄露时会产生较大影响。例如，包含录音、视频等用户生成数据或通话记录等信息的数据库。  **系统能力：** SystemCapability.DistributedDataManager.KVStore.Core |
| S3 | 5 | 表示数据库的安全级别为高级别，当数据泄露时会产生重大影响。例如，包含用户运动、健康、位置等信息的数据库。  **系统能力：** SystemCapability.DistributedDataManager.KVStore.Core |
| S4 | 6 | 表示数据库的安全级别为关键级别，当数据泄露时会产生严重影响。例如，包含认证凭据、财务数据等信息的数据库。  **系统能力：** SystemCapability.DistributedDataManager.KVStore.Core |

## Constants

PhonePC/2in1TabletTVWearable

KVStore常量。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MAX\_KEY\_LENGTH | 1024 | 数据库中Key允许的最大长度，单位字节。 |
| MAX\_VALUE\_LENGTH | 4194303 | 数据库中Value允许的最大长度，单位字节。 |
| MAX\_KEY\_LENGTH\_DEVICE | 896 | 最大设备密钥长度，单位字节。 |
| MAX\_STORE\_ID\_LENGTH | 128 | 数据库标识符允许的最大长度，单位字节。 |
| MAX\_QUERY\_LENGTH | 512000 | 最大查询长度，单位字节。 |
| MAX\_BATCH\_SIZE | 128 | 最大批处理操作数量。 |

## Schema8+

PhonePC/2in1TabletTVWearable

表示数据库模式，可以在创建或打开数据库时创建Schema对象并将它们放入[Options](js-apis-distributed-data.md#options)中。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

| 名称 | 类型 | 可读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| root8+ | [FieldNode](js-apis-distributed-data.md#fieldnode8) | 是 | 是 | 表示json根对象。 |
| indexes8+ | Array<string> | 是 | 是 | 表示json类型的字符串数组。 |
| mode8+ | number | 是 | 是 | 表示Schema的模式。 |
| skip8+ | number | 是 | 是 | Schema的跳跃大小。 |

### constructor8+

PhonePC/2in1TabletTVWearable

constructor()

用于创建Schema实例的构造函数。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

## FieldNode8+

PhonePC/2in1TabletTVWearable

表示 Schema 实例的节点，提供定义存储在数据库中的值的方法。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

| 名称 | 类型 | 可读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| nullable8+ | boolean | 是 | 是 | 表示数据库字段是否可以为空。 |
| default8+ | string | 是 | 是 | 表示Fieldnode的默认值。 |
| type8+ | number | 是 | 是 | 表示指定节点对应数据类型的值。 |

### constructor8+

PhonePC/2in1TabletTVWearable

constructor(name: string)

用于创建带有string字段FieldNode实例的构造函数。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | FieldNode的值。 |

### appendChild8+

PhonePC/2in1TabletTVWearable

appendChild(child: FieldNode): boolean

在当前 FieldNode 中添加一个子节点。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| child | [FieldNode](js-apis-distributed-data.md#fieldnode8) | 是 | 要附加的域节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示子节点成功添加到FieldNode；返回false则表示操作失败。 |

**示例：**

```
1. import ddm from '@ohos.data.distributedData';
2. try {
3. let node = new ddm.FieldNode("root");
4. let child1 = new ddm.FieldNode("child1");
5. let child2 = new ddm.FieldNode("child2");
6. let child3 = new ddm.FieldNode("child3");
7. node.appendChild(child1);
8. node.appendChild(child2);
9. node.appendChild(child3);
10. console.log("appendNode " + JSON.stringify(node));
11. child1 = null;
12. child2 = null;
13. child3 = null;
14. node = null;
15. } catch (e) {
16. console.log("AppendChild " + e);
17. }
```

## KvStoreResultSet8+

PhonePC/2in1TabletTVWearable

提供获取KVStore数据库结果集的相关方法，包括查询和移动数据读取位置等。

在调用KvStoreResultSet的方法前，需要先通过[getKVStore](js-apis-distributed-data.md#getkvstore)构建一个KVStore实例。

### getCount8+

PhonePC/2in1TabletTVWearable

getCount(): number

获取结果集中的总行数。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回数据的总行数。 |

**示例：**

```
1. let kvStore;
2. try {
3. let resultSet;
4. kvStore.getResultSet('batch_test_string_key').then((result) => {
5. console.log('getResultSet succeed.');
6. resultSet = result;
7. }).catch((err) => {
8. console.log('getResultSet failed: ' + err);
9. });
10. const count = resultSet.getCount();
11. console.log("getCount succeed:" + count);
12. } catch (e) {
13. console.log("getCount failed: " + e);
14. }
```

### getPosition8+

PhonePC/2in1TabletTVWearable

getPosition(): number

获取结果集中当前的读取位置。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回当前读取位置。 |

**示例：**

```
1. let kvStore;
2. try {
3. let resultSet;
4. kvStore.getResultSet('batch_test_string_key').then((result) => {
5. console.log('getResultSet succeeded.');
6. resultSet = result;
7. }).catch((err) => {
8. console.log('getResultSet failed: ' + err);
9. });
10. const position = resultSet.getPosition();
11. console.log("getPosition succeed:" + position);
12. } catch (e) {
13. console.log("getPosition failed: " + e);
14. }
```

### moveToFirst8+

PhonePC/2in1TabletTVWearable

moveToFirst(): boolean

将读取位置移动到第一行。如果结果集为空，则返回false。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示操作成功；返回false则表示操作失败。 |

**示例：**

```
1. let kvStore;
2. try {
3. let resultSet;
4. kvStore.getResultSet('batch_test_string_key').then((result) => {
5. console.log('getResultSet succeed.');
6. resultSet = result;
7. }).catch((err) => {
8. console.log('getResultSet failed: ' + err);
9. });
10. const moved1 = resultSet.moveToFirst();
11. console.log("moveToFirst succeed: " + moved1);
12. } catch (e) {
13. console.log("moveToFirst failed " + e);
14. }
```

### moveToLast8+

PhonePC/2in1TabletTVWearable

moveToLast(): boolean

将读取位置移动到最后一行。如果结果集为空，则返回false。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示操作成功；返回false则表示操作失败。 |

**示例：**

```
1. let kvStore;
2. try {
3. let resultSet;
4. kvStore.getResultSet('batch_test_string_key').then((result) => {
5. console.log('getResultSet succeed.');
6. resultSet = result;
7. }).catch((err) => {
8. console.log('getResultSet failed: ' + err);
9. });
10. const moved2 = resultSet.moveToLast();
11. console.log("moveToLast succeed:" + moved2);
12. } catch (e) {
13. console.log("moveToLast failed: " + e);
14. }
```

### moveToNext8+

PhonePC/2in1TabletTVWearable

moveToNext(): boolean

将读取位置移动到下一行。如果结果集为空，则返回false。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示操作成功；返回false则表示操作失败。 |

**示例：**

```
1. let kvStore;
2. try {
3. let resultSet;
4. kvStore.getResultSet('batch_test_string_key').then((result) => {
5. console.log('getResultSet succeed.');
6. resultSet = result;
7. }).catch((err) => {
8. console.log('getResultSet failed: ' + err);
9. });
10. const moved3 = resultSet.moveToNext();
11. console.log("moveToNext succeed: " + moved3);
12. } catch (e) {
13. console.log("moveToNext failed: " + e);
14. }
```

### moveToPrevious8+

PhonePC/2in1TabletTVWearable

moveToPrevious(): boolean

将读取位置移动到上一行。如果结果集为空，则返回false。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示操作成功；返回false则表示操作失败。 |

**示例：**

```
1. let kvStore;
2. try {
3. let resultSet;
4. kvStore.getResultSet('batch_test_string_key').then((result) => {
5. console.log('getResultSet succeed.');
6. resultSet = result;
7. }).catch((err) => {
8. console.log('getResultSet failed: ' + err);
9. });
10. const moved4 = resultSet.moveToPrevious();
11. console.log("moveToPrevious succeed:" + moved4);
12. } catch (e) {
13. console.log("moveToPrevious failed: " + e);
14. }
```

### move8+

PhonePC/2in1TabletTVWearable

move(offset: number): boolean

将读取位置移动到当前位置的相对偏移量。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 是 | 表示与当前位置的相对偏移量，负偏移表示向后移动，正偏移表示向前移动。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示操作成功；返回false则表示操作失败。 |

**示例：**

```
1. let kvStore;
2. try {
3. let resultSet;
4. kvStore.getResultSet('batch_test_string_key').then((result) => {
5. console.log('getResultSet succeed.');
6. resultSet = result;
7. }).catch((err) => {
8. console.log('getResultSet failed: ' + err);
9. });
10. const moved5 = resultSet.move(1);
11. console.log("move succeed:" + moved5);
12. } catch (e) {
13. console.log("move failed: " + e);
14. }
```

### moveToPosition8+

PhonePC/2in1TabletTVWearable

moveToPosition(position: number): boolean

将读取位置从 0 移动到绝对位置。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| position | number | 是 | 表示绝对位置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示操作成功；返回false则表示操作失败。 |

**示例：**

```
1. let kvStore;
2. try {
3. let resultSet;
4. kvStore.getResultSet('batch_test_string_key').then((result) => {
5. console.log('getResultSet succeed.');
6. resultSet = result;
7. }).catch((err) => {
8. console.log('getResultSet failed: ' + err);
9. });
10. const moved6 = resultSet.moveToPosition(1);
11. console.log("moveToPosition succeed: " + moved6);
12. } catch (e) {
13. console.log("moveToPosition failed: " + e);
14. }
```

### isFirst8+

PhonePC/2in1TabletTVWearable

isFirst(): boolean

检查读取位置是否为第一行。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示读取位置为第一行；返回false表示读取位置不是第一行。 |

**示例：**

```
1. let kvStore;
2. try {
3. let resultSet;
4. kvStore.getResultSet('batch_test_string_key').then((result) => {
5. console.log('getResultSet succeed.');
6. resultSet = result;
7. }).catch((err) => {
8. console.log('getResultSet failed: ' + err);
9. });
10. const isfirst = resultSet.isFirst();
11. console.log("Check isFirst succeed:" + isfirst);
12. } catch (e) {
13. console.log("Check isFirst failed: " + e);
14. }
```

### isLast8+

PhonePC/2in1TabletTVWearable

isLast(): boolean

检查读取位置是否为最后一行。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示读取位置为最后一行；返回false表示读取位置不是最后一行。 |

**示例：**

```
1. let kvStore;
2. try {
3. let resultSet;
4. kvStore.getResultSet('batch_test_string_key').then((result) => {
5. console.log('getResultSet succeed.');
6. resultSet = result;
7. }).catch((err) => {
8. console.log('getResultSet failed: ' + err);
9. });
10. const islast = resultSet.isLast();
11. console.log("Check isLast succeed: " + islast);
12. } catch (e) {
13. console.log("Check isLast failed: " + e);
14. }
```

### isBeforeFirst8+

PhonePC/2in1TabletTVWearable

isBeforeFirst(): boolean

检查读取位置是否在第一行之前。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示读取位置在第一行之前；返回false表示读取位置不在第一行之前。 |

**示例：**

```
1. let kvStore;
2. try {
3. let resultSet;
4. kvStore.getResultSet('batch_test_string_key').then((result) => {
5. console.log('getResultSet succeed.');
6. resultSet = result;
7. }).catch((err) => {
8. console.log('getResultSet failed: ' + err);
9. });
10. const isbeforefirst = resultSet.isBeforeFirst();
11. console.log("Check isBeforeFirst succeed: " + isbeforefirst);
12. } catch (e) {
13. console.log("Check isBeforeFirst failed: " + e);
14. }
```

### isAfterLast8+

PhonePC/2in1TabletTVWearable

isAfterLast(): boolean

检查读取位置是否在最后一行之后。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示读取位置在最后一行之后；返回false表示读取位置不在最后一行之后。 |

**示例：**

```
1. let kvStore;
2. try {
3. let resultSet;
4. kvStore.getResultSet('batch_test_string_key').then((result) => {
5. console.log('getResultSet succeed.');
6. resultSet = result;
7. }).catch((err) => {
8. console.log('getResultSet failed: ' + err);
9. });
10. const isafterlast = resultSet.isAfterLast();
11. console.log("Check isAfterLast succeed:" + isafterlast);
12. } catch (e) {
13. console.log("Check isAfterLast failed: " + e);
14. }
```

### getEntry8+

PhonePC/2in1TabletTVWearable

getEntry(): Entry

从当前位置获取对应的键值对。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Entry](js-apis-distributed-data.md#entry) | 返回键值对。 |

**示例：**

```
1. let kvStore;
2. try {
3. let resultSet;
4. kvStore.getResultSet('batch_test_string_key').then((result) => {
5. console.log('getResultSet succeed.');
6. resultSet = result;
7. }).catch((err) => {
8. console.log('getResultSet failed: ' + err);
9. });
10. const entry  = resultSet.getEntry();
11. console.log("getEntry succeed:" + JSON.stringify(entry));
12. } catch (e) {
13. console.log("getEntry failed: " + e);
14. }
```

## Query8+

PhonePC/2in1TabletTVWearable

使用谓词表示数据库查询，提供创建Query实例、查询数据库中的数据和添加谓词的方法。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

### constructor8+

PhonePC/2in1TabletTVWearable

constructor()

用于创建Query实例的构造函数。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

### reset8+

PhonePC/2in1TabletTVWearable

reset(): Query

重置Query对象。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributed-data.md#query8) | 返回重置的Query对象。 |

**示例：**

```
1. try {
2. let query = new distributedData.Query();
3. query.equalTo("key", "value");
4. console.log("query is " + query.getSqlLike());
5. query.reset();
6. console.log("query is " + query.getSqlLike());
7. query = null;
8. } catch (e) {
9. console.log("simply calls should be ok :" + e);
10. }
```

### equalTo8+

PhonePC/2in1TabletTVWearable

equalTo(field: string, value: number|string|boolean): Query

构造一个Query对象来查询具有指定字段的条目，其值等于指定的值。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含' ^ '。 |
| value | number|string|boolean | 是 | 表示指定的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributed-data.md#query8) | 返回Query对象。 |

**示例：**

```
1. try {
2. let query = new distributedData.Query();
3. query.equalTo("field", "value");
4. console.log("query is " + query.getSqlLike());
5. query = null;
6. } catch (e) {
7. console.log("duplicated calls should be ok :" + e);
8. }
```

### notEqualTo8+

PhonePC/2in1TabletTVWearable

notEqualTo(field: string, value: number|string|boolean): Query

构造一个Query对象以查询具有指定字段且值不等于指定值的条目。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含' ^ '。 |
| value | number|string|boolean | 是 | 表示指定的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributed-data.md#query8) | 返回Query对象。 |

**示例：**

```
1. try {
2. let query = new distributedData.Query();
3. query.notEqualTo("field", "value");
4. console.log("query is " + query.getSqlLike());
5. query = null;
6. } catch (e) {
7. console.log("duplicated calls should be ok :" + e);
8. }
```

### greaterThan8+

PhonePC/2in1TabletTVWearable

greaterThan(field: string, value: number|string|boolean): Query

构造一个Query对象以查询具有大于指定值的指定字段的条目。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含' ^ '。 |
| value | number|string|boolean | 是 | 表示指定的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributed-data.md#query8) | 返回Query对象。 |

**示例：**

```
1. try {
2. let query = new distributedData.Query();
3. query.greaterThan("field", "value");
4. console.log("query is " + query.getSqlLike());
5. query = null;
6. } catch (e) {
7. console.log("duplicated calls should be ok :" + e);
8. }
```

### lessThan8+

PhonePC/2in1TabletTVWearable

lessThan(field: string, value: number|string): Query

构造一个Query对象以查询具有小于指定值的指定字段的条目。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含' ^ '。 |
| value | number|string | 是 | 表示指定的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributed-data.md#query8) | 返回Query对象。 |

**示例：**

```
1. try {
2. let query = new distributedData.Query();
3. query.lessThan("field", "value");
4. console.log("query is " + query.getSqlLike());
5. query = null;
6. } catch (e) {
7. console.log("duplicated calls should be ok :" + e);
8. }
```

### greaterThanOrEqualTo8+

PhonePC/2in1TabletTVWearable

greaterThanOrEqualTo(field: string, value: number|string): Query

构造一个Query对象以查询具有指定字段且值大于或等于指定值的条目。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含' ^ '。 |
| value | number|string | 是 | 表示指定的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributed-data.md#query8) | 返回Query对象。 |

**示例：**

```
1. try {
2. let query = new distributedData.Query();
3. query.greaterThanOrEqualTo("field", "value");
4. console.log("query is " + query.getSqlLike());
5. query = null;
6. } catch (e) {
7. console.log("duplicated calls should be ok :" + e);
8. }
```

### lessThanOrEqualTo8+

PhonePC/2in1TabletTVWearable

lessThanOrEqualTo(field: string, value: number|string): Query

构造一个Query对象以查询具有指定字段且值小于或等于指定值的条目。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含' ^ '。 |
| value | number|string | 是 | 表示指定的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributed-data.md#query8) | 返回Query对象。 |

**示例：**

```
1. try {
2. let query = new distributedData.Query();
3. query.lessThanOrEqualTo("field", "value");
4. console.log("query is " + query.getSqlLike());
5. query = null;
6. } catch (e) {
7. console.log("duplicated calls should be ok :" + e);
8. }
```

### isNull8+

PhonePC/2in1TabletTVWearable

isNull(field: string): Query

构造一个Query对象以查询具有值为null的指定字段的条目。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含' ^ '。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributed-data.md#query8) | 返回Query对象。 |

**示例：**

```
1. try {
2. let query = new distributedData.Query();
3. query.isNull("field");
4. console.log("query is " + query.getSqlLike());
5. query = null;
6. } catch (e) {
7. console.log("duplicated calls should be ok :" + e);
8. }
```

### inNumber8+

PhonePC/2in1TabletTVWearable

inNumber(field: string, valueList: number[]): Query

构造一个Query对象以查询具有指定字段的条目，其值在指定的值列表中。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含' ^ '。 |
| valueList | number[] | 是 | 表示指定的值列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributed-data.md#query8) | 返回Query对象。 |

**示例：**

```
1. try {
2. let query = new distributedData.Query();
3. query.inNumber("field", [0, 1]);
4. console.log("query is " + query.getSqlLike());
5. query = null;
6. } catch (e) {
7. console.log("duplicated calls should be ok :" + e);
8. }
```

### inString8+

PhonePC/2in1TabletTVWearable

inString(field: string, valueList: string[]): Query

构造一个Query对象以查询具有指定字段的条目，其值在指定的字符串值列表中。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含' ^ '。 |
| valueList | string[] | 是 | 表示指定的字符串值列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributed-data.md#query8) | 返回Query对象。 |

**示例：**

```
1. try {
2. let query = new distributedData.Query();
3. query.inString("field", ['test1', 'test2']);
4. console.log("query is " + query.getSqlLike());
5. query = null;
6. } catch (e) {
7. console.log("duplicated calls should be ok :" + e);
8. }
```

### notInNumber8+

PhonePC/2in1TabletTVWearable

notInNumber(field: string, valueList: number[]): Query

构造一个Query对象以查询具有指定字段的条目，该字段的值不在指定的值列表中。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含' ^ '。 |
| valueList | number[] | 是 | 表示指定的值列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributed-data.md#query8) | 返回Query对象。 |

**示例：**

```
1. try {
2. let query = new distributedData.Query();
3. query.notInNumber("field", [0, 1]);
4. console.log("query is " + query.getSqlLike());
5. query = null;
6. } catch (e) {
7. console.log("duplicated calls should be ok :" + e);
8. }
```

### notInString8+

PhonePC/2in1TabletTVWearable

notInString(field: string, valueList: string[]): Query

构造一个Query对象以查询具有指定字段且值不在指定字符串值列表中的条目。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含' ^ '。 |
| valueList | string[] | 是 | 表示指定的字符串值列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributed-data.md#query8) | 返回Query对象。 |

**示例：**

```
1. try {
2. let query = new distributedData.Query();
3. query.notInString("field", ['test1', 'test2']);
4. console.log("query is " + query.getSqlLike());
5. query = null;
6. } catch (e) {
7. console.log("duplicated calls should be ok :" + e);
8. }
```

### like8+

PhonePC/2in1TabletTVWearable

like(field: string, value: string): Query

构造一个Query对象以查询具有与指定字符串值相似的指定字段的条目。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含' ^ '。 |
| value | string | 是 | 表示指定的字符串值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributed-data.md#query8) | 返回Query对象。 |

**示例：**

```
1. try {
2. let query = new distributedData.Query();
3. query.like("field", "value");
4. console.log("query is " + query.getSqlLike());
5. query = null;
6. } catch (e) {
7. console.log("duplicated calls should be ok :" + e);
8. }
```

### unlike8+

PhonePC/2in1TabletTVWearable

unlike(field: string, value: string): Query

构造一个Query对象以查询具有与指定字符串值不相似的指定字段的条目。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含' ^ '。 |
| value | string | 是 | 表示指定的字符串值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributed-data.md#query8) | 返回Query对象。 |

**示例：**

```
1. try {
2. let query = new distributedData.Query();
3. query.unlike("field", "value");
4. console.log("query is " + query.getSqlLike());
5. query = null;
6. } catch (e) {
7. console.log("duplicated calls should be ok :" + e);
8. }
```

### and8+

PhonePC/2in1TabletTVWearable

and(): Query

构造一个带有与条件的查询对象。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributed-data.md#query8) | 返回查询对象。 |

**示例：**

```
1. try {
2. let query = new distributedData.Query();
3. query.notEqualTo("field", "value1");
4. query.and();
5. query.notEqualTo("field", "value2");
6. console.log("query is " + query.getSqlLike());
7. query = null;
8. } catch (e) {
9. console.log("duplicated calls should be ok :" + e);
10. }
```

### or8+

PhonePC/2in1TabletTVWearable

or(): Query

构造一个带有或条件的Query对象。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributed-data.md#query8) | 返回查询对象。 |

**示例：**

```
1. try {
2. let query = new distributedData.Query();
3. query.notEqualTo("field", "value1");
4. query.or();
5. query.notEqualTo("field", "value2");
6. console.log("query is " + query.getSqlLike());
7. query = null;
8. } catch (e) {
9. console.log("duplicated calls should be ok :" + e);
10. }
```

### orderByAsc8+

PhonePC/2in1TabletTVWearable

orderByAsc(field: string): Query

构造一个Query对象，将查询结果按升序排序。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含' ^ '。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributed-data.md#query8) | 返回Query对象。 |

**示例：**

```
1. try {
2. let query = new distributedData.Query();
3. query.notEqualTo("field", "value");
4. query.orderByAsc("field");
5. console.log("query is " + query.getSqlLike());
6. query = null;
7. } catch (e) {
8. console.log("duplicated calls should be ok :" + e);
9. }
```

### orderByDesc8+

PhonePC/2in1TabletTVWearable

orderByDesc(field: string): Query

构造一个Query对象，将查询结果按降序排序。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含' ^ '。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributed-data.md#query8) | 返回Query对象。 |

**示例：**

```
1. try {
2. let query = new distributedData.Query();
3. query.notEqualTo("field", "value");
4. query.orderByDesc("field");
5. console.log("query is " + query.getSqlLike());
6. query = null;
7. } catch (e) {
8. console.log("duplicated calls should be ok :" + e);
9. }
```

### limit8+

PhonePC/2in1TabletTVWearable

limit(total: number, offset: number): Query

构造一个Query对象来指定结果的数量和开始位置。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| total | number | 是 | 表示指定的结果数。 |
| offset | number | 是 | 表示起始位置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributed-data.md#query8) | 返回Query对象。 |

**示例：**

```
1. let total = 10;
2. let offset = 1;
3. try {
4. let query = new distributedData.Query();
5. query.notEqualTo("field", "value");
6. query.limit(total, offset);
7. console.log("query is " + query.getSqlLike());
8. query = null;
9. } catch (e) {
10. console.log("duplicated calls should be ok :" + e);
11. }
```

### isNotNull8+

PhonePC/2in1TabletTVWearable

isNotNull(field: string): Query

构造一个Query对象以查询具有值不为null的指定字段的条目。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含' ^ '。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributed-data.md#query8) | 返回Query对象。 |

**示例：**

```
1. try {
2. let query = new distributedData.Query();
3. query.isNotNull("field");
4. console.log("query is " + query.getSqlLike());
5. query = null;
6. } catch (e) {
7. console.log("duplicated calls should be ok :" + e);
8. }
```

### beginGroup8+

PhonePC/2in1TabletTVWearable

beginGroup(): Query

创建一个带有左括号的查询条件组。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributed-data.md#query8) | 返回Query对象。 |

**示例：**

```
1. try {
2. let query = new distributedData.Query();
3. query.beginGroup();
4. query.isNotNull("field");
5. query.endGroup();
6. console.log("query is " + query.getSqlLike());
7. query = null;
8. } catch (e) {
9. console.log("duplicated calls should be ok :" + e);
10. }
```

### endGroup8+

PhonePC/2in1TabletTVWearable

endGroup(): Query

创建一个带有右括号的查询条件组。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributed-data.md#query8) | 返回Query对象。 |

**示例：**

```
1. try {
2. let query = new distributedData.Query();
3. query.beginGroup();
4. query.isNotNull("field");
5. query.endGroup();
6. console.log("query is " + query.getSqlLike());
7. query = null;
8. } catch (e) {
9. console.log("duplicated calls should be ok :" + e);
10. }
```

### prefixKey8+

PhonePC/2in1TabletTVWearable

prefixKey(prefix: string): Query

创建具有指定键前缀的查询条件。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| prefix | string | 是 | 表示指定的键前缀。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributed-data.md#query8) | 返回Query对象。 |

**示例：**

```
1. try {
2. let query = new distributedData.Query();
3. query.prefixKey("$.name");
4. query.prefixKey("0");
5. console.log("query is " + query.getSqlLike());
6. query = null;
7. } catch (e) {
8. console.log("duplicated calls should be ok :" + e);
9. }
```

### setSuggestIndex8+

PhonePC/2in1TabletTVWearable

setSuggestIndex(index: string): Query

设置一个指定的索引，将优先用于查询。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | string | 是 | 指示要设置的索引。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributed-data.md#query8) | 返回Query对象。 |

**示例：**

```
1. try {
2. let query = new distributedData.Query();
3. query.setSuggestIndex("$.name");
4. query.setSuggestIndex("0");
5. console.log("query is " + query.getSqlLike());
6. query = null;
7. } catch (e) {
8. console.log("duplicated calls should be ok :" + e);
9. }
```

### deviceId8+

PhonePC/2in1TabletTVWearable

deviceId(deviceId:string):Query

添加设备ID作为key的前缀。

说明

其中deviceId通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

deviceId具体获取方式请参考[sync接口示例](js-apis-distributed-data.md#sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 指示查询的设备ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributed-data.md#query8) | 返回Query对象。 |

**示例：**

```
1. try {
2. let query = new distributedData.Query();
3. query.deviceId("deviceId");
4. console.log("query is " + query.getSqlLike());
5. } catch (e) {
6. console.log("should be ok on Method Chaining : " + e);
7. }
```

### getSqlLike8+

PhonePC/2in1TabletTVWearable

getSqlLike():string

获取Query对象的查询语句。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回一个字段列中包含对应子串的结果。 |

**示例：**

```
1. try {
2. let query = new distributedData.Query();
3. let sql1 = query.getSqlLike();
4. console.log("GetSqlLike sql=" + sql1);
5. } catch (e) {
6. console.log("duplicated calls should be ok : " + e);
7. }
```

## KVStore

PhonePC/2in1TabletTVWearable

KVStore数据库实例，提供增加数据、删除数据和订阅数据变更、订阅数据同步完成的方法。

在调用KVStore的方法前，需要先通过[getKVStore](js-apis-distributed-data.md#getkvstore)构建一个KVStore实例。

### put

PhonePC/2in1TabletTVWearable

put(key: string, value: Uint8Array | string | number | boolean, callback: AsyncCallback<void>): void

添加指定类型键值对到数据库，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要添加数据的key，不能为空且长度不大于[MAX\_KEY\_LENGTH](js-apis-distributed-data.md#constants)。 |
| value | Uint8Array | string | number | boolean | 是 | 要添加数据的value，支持Uint8Array、number 、 string 、boolean，Uint8Array、string 的长度不大于[MAX\_VALUE\_LENGTH](js-apis-distributed-data.md#constants)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. let kvStore;
2. const KEY_TEST_STRING_ELEMENT = 'key_test_string';
3. const VALUE_TEST_STRING_ELEMENT = 'value-test-string';
4. try {
5. kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT, function (err,data) {
6. if (err != undefined) {
7. console.log("put err: " + JSON.stringify(err));
8. return;
9. }
10. console.log("put success");
11. });
12. }catch (e) {
13. console.log("An unexpected error occurred. Error:" + e);
14. }
```

### put

PhonePC/2in1TabletTVWearable

put(key: string, value: Uint8Array | string | number | boolean): Promise<void>

添加指定类型键值对到数据库，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要添加数据的key，不能为空且长度不大于[MAX\_KEY\_LENGTH](js-apis-distributed-data.md#constants)。 |
| value | Uint8Array | string | number | boolean | 是 | 要添加数据的value，支持Uint8Array、number 、 string 、boolean，Uint8Array、string 的长度不大于[MAX\_VALUE\_LENGTH](js-apis-distributed-data.md#constants)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. let kvStore;
2. const KEY_TEST_STRING_ELEMENT = 'key_test_string';
3. const VALUE_TEST_STRING_ELEMENT = 'value-test-string';
4. try {
5. kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT).then((data) => {
6. console.log("put success: " + JSON.stringify(data));
7. }).catch((err) => {
8. console.log("put err: " + JSON.stringify(err));
9. });
10. }catch (e) {
11. console.log("An unexpected error occurred. Error:" + e);
12. }
```

### delete

PhonePC/2in1TabletTVWearable

delete(key: string, callback: AsyncCallback<void>): void

从数据库中删除指定键值的数据，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要删除数据的key，不能为空且长度不大于[MAX\_KEY\_LENGTH](js-apis-distributed-data.md#constants)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. let kvStore;
2. const KEY_TEST_STRING_ELEMENT = 'key_test_string';
3. const VALUE_TEST_STRING_ELEMENT = 'value-test-string';
4. try {
5. kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT, function (err,data) {
6. if (err != undefined) {
7. console.log("put err: " + JSON.stringify(err));
8. return;
9. }
10. console.log("put success");
11. kvStore.delete(KEY_TEST_STRING_ELEMENT, function (err,data) {
12. if (err != undefined) {
13. console.log("delete err: " + JSON.stringify(err));
14. return;
15. }
16. console.log("delete success");
17. });
18. });
19. }catch (e) {
20. console.log("An unexpected error occurred. Error:" + e);
21. }
```

### delete

PhonePC/2in1TabletTVWearable

delete(key: string): Promise<void>

从数据库中删除指定键值的数据，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要删除数据的key，不能为空且长度不大于[MAX\_KEY\_LENGTH](js-apis-distributed-data.md#constants)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. let kvStore;
2. const KEY_TEST_STRING_ELEMENT = 'key_test_string';
3. const VALUE_TEST_STRING_ELEMENT = 'value-test-string';
4. try {
5. kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT).then((data) => {
6. console.log("put success: " + JSON.stringify(data));
7. kvStore.delete(KEY_TEST_STRING_ELEMENT).then((data) => {
8. console.log("delete success");
9. }).catch((err) => {
10. console.log("delete err: " + JSON.stringify(err));
11. });
12. }).catch((err) => {
13. console.log("put err: " + JSON.stringify(err));
14. });
15. }catch (e) {
16. console.log("An unexpected error occurred. Error:" + e);
17. }
```

### on('dataChange')

PhonePC/2in1TabletTVWearable

on(event: 'dataChange', type: SubscribeType, listener: Callback<ChangeNotification>): void

订阅指定类型的数据变更通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 订阅的事件名，固定为'dataChange'，表示数据变更事件。 |
| type | [SubscribeType](js-apis-distributed-data.md#subscribetype) | 是 | 表示订阅的类型。 |
| listener | Callback<[ChangeNotification](js-apis-distributed-data.md#changenotification)> | 是 | 回调函数。 |

**示例：**

```
1. let kvStore;
2. kvStore.on('dataChange', distributedData.SubscribeType.SUBSCRIBE_TYPE_LOCAL, function (data) {
3. console.log("dataChange callback call data: " + JSON.stringify(data));
4. });
```

### on('syncComplete')

PhonePC/2in1TabletTVWearable

on(event: 'syncComplete', syncCallback: Callback<Array<[string, number]>>): void

订阅同步完成事件回调通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 订阅的事件名，固定为'syncComplete'，表示同步完成事件。 |
| syncCallback | Callback<Array<[string, number]>> | 是 | 回调函数。用于向调用方发送同步结果的回调。 |

**示例：**

```
1. let kvStore;
2. kvStore.on('syncComplete', function (data) {
3. console.log("callback call data: " + data);
4. });
```

### off('dataChange')8+

PhonePC/2in1TabletTVWearable

off(event:'dataChange', listener?: Callback<ChangeNotification>): void

取消订阅数据变更通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取消订阅的事件名，固定为'dataChange'，表示数据变更事件。 |
| listener | Callback<[ChangeNotification](js-apis-distributed-data.md#changenotification)> | 否 | 取消订阅的函数。如不设置callback，则取消所有订阅的函数。 |

**示例：**

```
1. let kvStore;
2. class KvstoreModel {
3. call(data) {
4. console.log("dataChange: " + data);
5. }
6. subscribeDataChange() {
7. if (kvStore != null) {
8. kvStore.on('dataChange', distributedData.SubscribeType.SUBSCRIBE_TYPE_REMOTE, this.call);
9. }
10. }
11. unsubscribeDataChange() {
12. if (kvStore != null) {
13. kvStore.off('dataChange', this.call);
14. }
15. }
16. }
```

### off('syncComplete')8+

PhonePC/2in1TabletTVWearable

off(event: 'syncComplete', syncCallback?: Callback<Array<[string, number]>>): void

取消订阅同步完成事件回调通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取消订阅的事件名，固定为'syncComplete'，表示同步完成事件。 |
| syncCallback | Callback<Array<[string, number]>> | 否 | 取消订阅的函数。如不设置callback，则取消所有订阅的函数。 |

**示例：**

```
1. let kvStore;
2. class KvstoreModel {
3. call(data) {
4. console.log("syncComplete: " + data);
5. }
6. subscribeSyncComplete() {
7. if (kvStore != null) {
8. kvStore.on('syncComplete', this.call);
9. }
10. }
11. unsubscribeSyncComplete() {
12. if (kvStore != null) {
13. kvStore.off('syncComplete', this.call);
14. }
15. }
16. }
```

### putBatch8+

PhonePC/2in1TabletTVWearable

putBatch(entries: Entry[], callback: AsyncCallback<void>): void

批量插入键值对到KVStore数据库中，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| entries | [Entry](js-apis-distributed-data.md#entry)[] | 是 | 表示要批量插入的键值对。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. let kvStore;
2. try {
3. let entries = [];
4. for (var i = 0; i < 10; i++) {
5. var key = 'batch_test_string_key';
6. var entry = {
7. key : key + i,
8. value : {
9. type : distributedData.ValueType.STRING,
10. value : 'batch_test_string_value'
11. }
12. }
13. entries.push(entry);
14. }
15. console.log('entries: ' + JSON.stringify(entries));
16. kvStore.putBatch(entries, async function (err,data) {
17. console.log('putBatch success');
18. kvStore.getEntries('batch_test_string_key', function (err,entries) {
19. console.log('getEntries success');
20. console.log('entries.length: ' + entries.length);
21. console.log('entries[0]: ' + JSON.stringify(entries[0]));
22. });
23. });
24. }catch(e) {
25. console.log('PutBatch e ' + JSON.stringify(e));
26. }
```

### putBatch8+

PhonePC/2in1TabletTVWearable

putBatch(entries: Entry[]): Promise<void>

批量插入键值对到KVStore数据库中，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| entries | [Entry](js-apis-distributed-data.md#entry)[] | 是 | 表示要批量插入的键值对。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. let kvStore;
2. try {
3. let entries = [];
4. for (var i = 0; i < 10; i++) {
5. var key = 'batch_test_string_key';
6. var entry = {
7. key : key + i,
8. value : {
9. type : distributedData.ValueType.STRING,
10. value : 'batch_test_string_value'
11. }
12. }
13. entries.push(entry);
14. }
15. console.log('entries: ' + JSON.stringify(entries));
16. kvStore.putBatch(entries).then(async (err) => {
17. console.log('putBatch success');
18. kvStore.getEntries('batch_test_string_key').then((entries) => {
19. console.log('getEntries success');
20. console.log('PutBatch ' + JSON.stringify(entries));
21. }).catch((err) => {
22. console.log('getEntries fail ' + JSON.stringify(err));
23. });
24. }).catch((err) => {
25. console.log('putBatch fail ' + JSON.stringify(err));
26. });
27. }catch(e) {
28. console.log('PutBatch e ' + JSON.stringify(e));
29. }
```

### deleteBatch8+

PhonePC/2in1TabletTVWearable

deleteBatch(keys: string[], callback: AsyncCallback<void>): void

批量删除KVStore数据库中的键值对，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keys | string[] | 是 | 表示要批量删除的键值对。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. let kvStore;
2. try {
3. let entries = [];
4. let keys = [];
5. for (var i = 0; i < 5; i++) {
6. var key = 'batch_test_string_key';
7. var entry = {
8. key : key + i,
9. value : {
10. type : distributedData.ValueType.STRING,
11. value : 'batch_test_string_value'
12. }
13. }
14. entries.push(entry);
15. keys.push(key + i);
16. }
17. console.log('entries: ' + JSON.stringify(entries));
18. kvStore.putBatch(entries, async function (err,data) {
19. console.log('putBatch success');
20. kvStore.deleteBatch(keys, async function (err,data) {
21. console.log('deleteBatch success');
22. });
23. });
24. }catch(e) {
25. console.log('DeleteBatch e ' + e);
26. }
```

### deleteBatch8+

PhonePC/2in1TabletTVWearable

deleteBatch(keys: string[]): Promise<void>

批量删除KVStore数据库中的键值对，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keys | string[] | 是 | 表示要批量删除的键值对。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. let kvStore;
2. try {
3. let entries = [];
4. let keys = [];
5. for (var i = 0; i < 5; i++) {
6. var key = 'batch_test_string_key';
7. var entry = {
8. key : key + i,
9. value : {
10. type : distributedData.ValueType.STRING,
11. value : 'batch_test_string_value'
12. }
13. }
14. entries.push(entry);
15. keys.push(key + i);
16. }
17. console.log('entries: ' + JSON.stringify(entries));
18. kvStore.putBatch(entries).then(async (err) => {
19. console.log('putBatch success');
20. kvStore.deleteBatch(keys).then((err) => {
21. console.log('deleteBatch success');
22. }).catch((err) => {
23. console.log('deleteBatch fail ' + JSON.stringify(err));
24. });
25. }).catch((err) => {
26. console.log('putBatch fail ' + JSON.stringify(err));
27. });
28. }catch(e) {
29. console.log('DeleteBatch e ' + e);
30. }
```

### startTransaction8+

PhonePC/2in1TabletTVWearable

startTransaction(callback: AsyncCallback<void>): void

启动KVStore数据库中的事务，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. let kvStore;
2. function putBatchString(len, prefix) {
3. let entries = [];
4. for (var i = 0; i < len; i++) {
5. var entry = {
6. key : prefix + i,
7. value : {
8. type : distributedData.ValueType.STRING,
9. value : 'batch_test_string_value'
10. }
11. }
12. entries.push(entry);
13. }
14. return entries;
15. }
16. try {
17. var count = 0;
18. kvStore.on('dataChange', 0, function (data) {
19. console.log('startTransaction 0' + data)
20. count++;
21. });
22. kvStore.startTransaction(async function (err,data) {
23. console.log('startTransaction success');
24. let entries = putBatchString(10, 'batch_test_string_key');
25. console.log('entries: ' + JSON.stringify(entries));
26. kvStore.putBatch(entries, async function (err,data) {
27. console.log('putBatch success');
28. });
29. });
30. }catch(e) {
31. console.log('startTransaction e ' + e);
32. }
```

### startTransaction8+

PhonePC/2in1TabletTVWearable

startTransaction(): Promise<void>

启动KVStore数据库中的事务，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. let kvStore;
2. try {
3. var count = 0;
4. kvStore.on('dataChange', distributedData.SubscribeType.SUBSCRIBE_TYPE_ALL, function (data) {
5. console.log('startTransaction ' + JSON.stringify(data));
6. count++;
7. });
8. kvStore.startTransaction().then(async (err) => {
9. console.log('startTransaction success');
10. }).catch((err) => {
11. console.log('startTransaction fail ' + JSON.stringify(err));
12. });
13. }catch(e) {
14. console.log('startTransaction e ' + e);
15. }
```

### commit8+

PhonePC/2in1TabletTVWearable

commit(callback: AsyncCallback<void>): void

提交KVStore数据库中的事务，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. let kvStore;
2. try {
3. kvStore.commit(function (err,data) {
4. if (err == undefined) {
5. console.log('commit success');
6. } else {
7. console.log('commit fail');
8. }
9. });
10. }catch(e) {
11. console.log('Commit e ' + e);
12. }
```

### commit8+

PhonePC/2in1TabletTVWearable

commit(): Promise<void>

提交KVStore数据库中的事务，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. let kvStore;
2. try {
3. kvStore.commit().then(async (err) => {
4. console.log('commit success');
5. }).catch((err) => {
6. console.log('commit fail ' + JSON.stringify(err));
7. });
8. }catch(e) {
9. console.log('Commit e ' + e);
10. }
```

### rollback8+

PhonePC/2in1TabletTVWearable

rollback(callback: AsyncCallback<void>): void

在KVStore数据库中回滚事务，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. let kvStore;
2. try {
3. kvStore.rollback(function (err,data) {
4. if (err == undefined) {
5. console.log('commit success');
6. } else {
7. console.log('commit fail');
8. }
9. });
10. }catch(e) {
11. console.log('Rollback e ' + e);
12. }
```

### rollback8+

PhonePC/2in1TabletTVWearable

rollback(): Promise<void>

在KVStore数据库中回滚事务，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. let kvStore;
2. try {
3. kvStore.rollback().then(async (err) => {
4. console.log('rollback success');
5. }).catch((err) => {
6. console.log('rollback fail ' + JSON.stringify(err));
7. });
8. }catch(e) {
9. console.log('Rollback e ' + e);
10. }
```

### enableSync8+

PhonePC/2in1TabletTVWearable

enableSync(enabled: boolean, callback: AsyncCallback<void>): void

设定是否开启同步，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 设定是否开启同步，true表示开启同步，false表示不启用同步。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. let kvStore;
2. try {
3. kvStore.enableSync(true, function (err,data) {
4. if (err == undefined) {
5. console.log('enableSync success');
6. } else {
7. console.log('enableSync fail');
8. }
9. });
10. }catch(e) {
11. console.log('EnableSync e ' + e);
12. }
```

### enableSync8+

PhonePC/2in1TabletTVWearable

enableSync(enabled: boolean): Promise<void>

设定是否开启同步，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 设定是否开启同步，true表示开启同步，false表示不启用同步。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. let kvStore;
2. try {
3. kvStore.enableSync(true).then((err) => {
4. console.log('enableSync success');
5. }).catch((err) => {
6. console.log('enableSync fail ' + JSON.stringify(err));
7. });
8. }catch(e) {
9. console.log('EnableSync e ' + e);
10. }
```

### setSyncRange8+

PhonePC/2in1TabletTVWearable

setSyncRange(localLabels: string[], remoteSupportLabels: string[], callback: AsyncCallback<void>): void

设置同步范围标签，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localLabels | string[] | 是 | 表示本地设备的同步标签。 |
| remoteSupportLabels | string[] | 是 | 表示要同步数据的设备的同步标签。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. let kvStore;
2. try {
3. const localLabels = ['A', 'B'];
4. const remoteSupportLabels = ['C', 'D'];
5. kvStore.setSyncRange(localLabels, remoteSupportLabels, function (err,data) {
6. console.log('SetSyncRange put success');
7. });
8. }catch(e) {
9. console.log('SetSyncRange e ' + e);
10. }
```

### setSyncRange8+

PhonePC/2in1TabletTVWearable

setSyncRange(localLabels: string[], remoteSupportLabels: string[]): Promise<void>

设置同步范围标签，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localLabels | string[] | 是 | 表示本地设备的同步标签。 |
| remoteSupportLabels | string[] | 是 | 表示要同步数据的设备的同步标签。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. let kvStore;
2. try {
3. const localLabels = ['A', 'B'];
4. const remoteSupportLabels = ['C', 'D'];
5. kvStore.setSyncRange(localLabels, remoteSupportLabels).then((err) => {
6. console.log('setSyncRange success');
7. }).catch((err) => {
8. console.log('delete fail ' + err);
9. });
10. }catch(e) {
11. console.log('SetSyncRange e ' + e);
12. }
```

## SubscribeType

PhonePC/2in1TabletTVWearable

订阅类型枚举。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUBSCRIBE\_TYPE\_LOCAL | 0 | 表示订阅本地数据变更。 |
| SUBSCRIBE\_TYPE\_REMOTE | 1 | 表示订阅远端数据变更。 |
| SUBSCRIBE\_TYPE\_ALL | 2 | 表示订阅远端和本地数据变更。 |

## ChangeNotification

PhonePC/2in1TabletTVWearable

数据变更时通知的对象，包括数据插入的数据、更新的数据、删除的数据和设备ID。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| insertEntries | [Entry](js-apis-distributed-data.md#entry)[] | 是 | 数据添加记录。 |
| updateEntries | [Entry](js-apis-distributed-data.md#entry)[] | 是 | 数据更新记录。 |
| deleteEntries | [Entry](js-apis-distributed-data.md#entry)[] | 是 | 数据删除记录。 |
| deviceId | string | 是 | 设备ID，此处为设备UUID。 |

## Entry

PhonePC/2in1TabletTVWearable

存储在数据库中的键值对。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 键值。 |
| value | [Value](js-apis-distributed-data.md#value) | 是 | 值对象。 |

## Value

PhonePC/2in1TabletTVWearable

存储在数据库中的值对象。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [ValueType](js-apis-distributed-data.md#value) | 是 | 值类型。 |
| value | Uint8Array | string | number | boolean | 是 | 值。 |

## ValueType

PhonePC/2in1TabletTVWearable

数据类型枚举。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STRING | 0 | 表示值类型为字符串。 |
| INTEGER | 1 | 表示值类型为整数。 |
| FLOAT | 2 | 表示值类型为浮点数。 |
| BYTE\_ARRAY | 3 | 表示值类型为字节数组。 |
| BOOLEAN | 4 | 表示值类型为布尔值。 |
| DOUBLE | 5 | 表示值类型为双浮点数。 |

## SingleKVStore

PhonePC/2in1TabletTVWearable

单版本数据库，继承自[KVStore](js-apis-distributed-data.md#kvstore)数据库，提供查询数据和同步数据的方法。

单版本数据库，不对数据所属设备进行区分，不同设备使用相同键写入数据会互相覆盖。比如，可以使用单版本数据库实现个人日历、联系人数据在不同设备间的数据同步。

在调用SingleKVStore的方法前，需要先通过[getKVStore](js-apis-distributed-data.md#getkvstore)构建一个SingleKVStore实例。

### get

PhonePC/2in1TabletTVWearable

get(key: string, callback: AsyncCallback<Uint8Array | string | boolean | number>): void

获取指定键的值，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要查询数据的key，不能为空且长度不大于[MAX\_KEY\_LENGTH](js-apis-distributed-data.md#constants)。 |
| callback | AsyncCallback<Uint8Array | string | boolean | number> | 是 | 回调函数。返回获取查询的值。 |

**示例：**

```
1. let kvStore;
2. const KEY_TEST_STRING_ELEMENT = 'key_test_string';
3. const VALUE_TEST_STRING_ELEMENT = 'value-test-string';
4. try {
5. kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT, function (err,data) {
6. if (err != undefined) {
7. console.log("put err: " + JSON.stringify(err));
8. return;
9. }
10. console.log("put success");
11. kvStore.get(KEY_TEST_STRING_ELEMENT, function (err,data) {
12. console.log("get success data: " + data);
13. });
14. });
15. }catch (e) {
16. console.log("An unexpected error occurred. Error:" + e);
17. }
```

### get

PhonePC/2in1TabletTVWearable

get(key: string): Promise<Uint8Array | string | boolean | number>

获取指定键的值，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要查询数据的key，不能为空且长度不大于[MAX\_KEY\_LENGTH](js-apis-distributed-data.md#constants)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array | string | boolean | number> | Promise对象。返回获取查询的值。 |

**示例：**

```
1. let kvStore;
2. const KEY_TEST_STRING_ELEMENT = 'key_test_string';
3. const VALUE_TEST_STRING_ELEMENT = 'value-test-string';
4. try {
5. kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT).then((data) => {
6. console.log("put success: " + JSON.stringify(data));
7. kvStore.get(KEY_TEST_STRING_ELEMENT).then((data) => {
8. console.log("get success data: " + data);
9. }).catch((err) => {
10. console.log("get err: " + JSON.stringify(err));
11. });
12. }).catch((err) => {
13. console.log("put err: " + JSON.stringify(err));
14. });
15. }catch (e) {
16. console.log("An unexpected error occurred. Error:" + e);
17. }
```

### getEntries8+

PhonePC/2in1TabletTVWearable

getEntries(keyPrefix: string, callback: AsyncCallback<Entry[]>): void

获取匹配指定键前缀的所有键值对，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyPrefix | string | 是 | 表示要匹配的键前缀。 |
| callback | AsyncCallback<[Entry](js-apis-distributed-data.md#entry)[]> | 是 | 回调函数。返回匹配指定前缀的键值对列表。 |

**示例：**

```
1. let kvStore;
2. try {
3. let entries = [];
4. for (var i = 0; i < 10; i++) {
5. var key = 'batch_test_number_key';
6. var entry = {
7. key : key + i,
8. value : {
9. type : distributedData.ValueType.INTEGER,
10. value : 222
11. }
12. }
13. entries.push(entry);
14. }
15. kvStore.putBatch(entries, async function (err,data) {
16. console.log('putBatch success');
17. kvStore.getEntries('batch_test_number_key', function (err,entries) {
18. console.log('getEntries success');
19. console.log('entries.length: ' + entries.length);
20. console.log('entries[0]: ' + JSON.stringify(entries[0]));
21. });
22. });
23. }catch(e) {
24. console.log('PutBatch e ' + e);
25. }
```

### getEntries8+

PhonePC/2in1TabletTVWearable

getEntries(keyPrefix: string): Promise<Entry[]>

获取匹配指定键前缀的所有键值对，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyPrefix | string | 是 | 表示要匹配的键前缀。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Entry](js-apis-distributed-data.md#entry)[]> | Promise对象。返回匹配指定前缀的键值对列表。 |

**示例：**

```
1. let kvStore;
2. try {
3. let entries = [];
4. for (var i = 0; i < 10; i++) {
5. var key = 'batch_test_string_key';
6. var entry = {
7. key : key + i,
8. value : {
9. type : distributedData.ValueType.STRING,
10. value : 'batch_test_string_value'
11. }
12. }
13. entries.push(entry);
14. }
15. console.log('entries: ' + entries);
16. kvStore.putBatch(entries).then(async (err) => {
17. console.log('putBatch success');
18. kvStore.getEntries('batch_test_string_key').then((entries) => {
19. console.log('getEntries success');
20. console.log('entries.length: ' + entries.length);
21. console.log('entries[0]: ' + JSON.stringify(entries[0]));
22. console.log('entries[0].value: ' + JSON.stringify(entries[0].value));
23. console.log('entries[0].value.value: ' + entries[0].value.value);
24. }).catch((err) => {
25. console.log('getEntries fail ' + JSON.stringify(err));
26. });
27. }).catch((err) => {
28. console.log('putBatch fail ' + JSON.stringify(err));
29. });
30. }catch(e) {
31. console.log('PutBatch e ' + e);
32. }
```

### getEntries8+

PhonePC/2in1TabletTVWearable

getEntries(query: Query, callback: AsyncCallback<Entry[]>): void

获取与指定Query对象匹配的键值对列表，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | [Query](js-apis-distributed-data.md#query8) | 是 | 表示要匹配的键前缀。 |
| callback | AsyncCallback<[Entry](js-apis-distributed-data.md#entry)[]> | 是 | 回调函数。返回与指定Query对象匹配的键值对列表。 |

**示例：**

```
1. let kvStore;
2. try {
3. var arr = new Uint8Array([21,31]);
4. let entries = [];
5. for (var i = 0; i < 10; i++) {
6. var key = 'batch_test_bool_key';
7. var entry = {
8. key : key + i,
9. value : {
10. type : distributedData.ValueType.BYTE_ARRAY,
11. value : arr
12. }
13. }
14. entries.push(entry);
15. }
16. console.log('entries: ' + JSON.stringify(entries));
17. kvStore.putBatch(entries, async function (err,data) {
18. console.log('putBatch success');
19. const query = new distributedData.Query();
20. query.prefixKey("batch_test");
21. kvStore.getEntries(query, function (err,entries) {
22. console.log('getEntries success');
23. console.log('entries.length: ' + entries.length);
24. console.log('entries[0]: ' + JSON.stringify(entries[0]));
25. });
26. });
27. console.log('GetEntries success');
28. }catch(e) {
29. console.log('GetEntries e ' + e);
30. }
```

### getEntries8+

PhonePC/2in1TabletTVWearable

getEntries(query: Query): Promise<Entry[]>

获取与指定Query对象匹配的键值对列表，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | [Query](js-apis-distributed-data.md#query8) | 是 | 表示查询对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Entry](js-apis-distributed-data.md#entry)[]> | Promise对象。返回与指定Query对象匹配的键值对列表。 |

**示例：**

```
1. let kvStore;
2. try {
3. var arr = new Uint8Array([21,31]);
4. let entries = [];
5. for (var i = 0; i < 10; i++) {
6. var key = 'batch_test_bool_key';
7. var entry = {
8. key : key + i,
9. value : {
10. type : distributedData.ValueType.BYTE_ARRAY,
11. value : arr
12. }
13. }
14. entries.push(entry);
15. }
16. console.log('entries: ' + JSON.stringify(entries));
17. kvStore.putBatch(entries).then(async (err) => {
18. console.log('putBatch success');
19. const query = new distributedData.Query();
20. query.prefixKey("batch_test");
21. kvStore.getEntries(query).then((entries) => {
22. console.log('getEntries success');
23. }).catch((err) => {
24. console.log('getEntries fail ' + JSON.stringify(err));
25. });
26. }).catch((err) => {
27. console.log('GetEntries putBatch fail ' + JSON.stringify(err))
28. });
29. console.log('GetEntries success');
30. }catch(e) {
31. console.log('GetEntries e ' + e);
32. }
```

### getResultSet8+

PhonePC/2in1TabletTVWearable

getResultSet(keyPrefix: string, callback: AsyncCallback<KvStoreResultSet>): void

从KvStore数据库中获取具有指定前缀的结果集，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyPrefix | string | 是 | 表示要匹配的键前缀。 |
| callback | AsyncCallback<[KvStoreResultSet](js-apis-distributed-data.md#kvstoreresultset8)> | 是 | 回调函数。返回具有指定前缀的结果集。 |

**示例：**

```
1. let kvStore;
2. try {
3. let resultSet;
4. let entries = [];
5. for (var i = 0; i < 10; i++) {
6. var key = 'batch_test_string_key';
7. var entry = {
8. key : key + i,
9. value : {
10. type : distributedData.ValueType.STRING,
11. value : 'batch_test_string_value'
12. }
13. }
14. entries.push(entry);
15. }
16. kvStore.putBatch(entries, async function (err, data) {
17. console.log('GetResultSet putBatch success');
18. kvStore.getResultSet('batch_test_string_key', async function (err, result) {
19. console.log('GetResultSet getResultSet succeed.');
20. resultSet = result;
21. kvStore.closeResultSet(resultSet, function (err, data) {
22. console.log('GetResultSet closeResultSet success');
23. })
24. });
25. });
26. }catch(e) {
27. console.log('GetResultSet e ' + e);
28. }
```

### getResultSet8+

PhonePC/2in1TabletTVWearable

getResultSet(keyPrefix: string): Promise<KvStoreResultSet>

从KVStore数据库中获取具有指定前缀的结果集，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyPrefix | string | 是 | 表示要匹配的键前缀。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[KvStoreResultSet](js-apis-distributed-data.md#kvstoreresultset8)> | Promise对象。返回具有指定前缀的结果集。 |

**示例：**

```
1. let kvStore;
2. try {
3. let resultSet;
4. let entries = [];
5. for (var i = 0; i < 10; i++) {
6. var key = 'batch_test_string_key';
7. var entry = {
8. key : key + i,
9. value : {
10. type : distributedData.ValueType.STRING,
11. value : 'batch_test_string_value'
12. }
13. }
14. entries.push(entry);
15. }
16. kvStore.putBatch(entries).then(async (err) => {
17. console.log('putBatch success');
18. }).catch((err) => {
19. console.log('PutBatch putBatch fail ' + JSON.stringify(err));
20. });
21. kvStore.getResultSet('batch_test_string_key').then((result) => {
22. console.log('GetResult getResultSet succeed.');
23. resultSet = result;
24. }).catch((err) => {
25. console.log('getResultSet failed: ' + JSON.stringify(err));
26. });
27. kvStore.closeResultSet(resultSet).then((err) => {
28. console.log('GetResult closeResultSet success');
29. }).catch((err) => {
30. console.log('closeResultSet fail ' + JSON.stringify(err));
31. });
32. }catch(e) {
33. console.log('GetResult e ' + e);
34. }
```

### getResultSet8+

PhonePC/2in1TabletTVWearable

getResultSet(query: Query, callback: AsyncCallback<KvStoreResultSet>): void

获取与指定Query对象匹配的KvStoreResultSet对象，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | Query | 是 | 表示查询对象。 |
| callback | AsyncCallback<[KvStoreResultSet](js-apis-distributed-data.md#kvstoreresultset8)> | 是 | 回调函数，获取与指定Query对象匹配的KvStoreResultSet对象。 |

**示例：**

```
1. let kvStore;
2. try {
3. let resultSet;
4. let entries = [];
5. for (var i = 0; i < 10; i++) {
6. var key = 'batch_test_string_key';
7. var entry = {
8. key : key + i,
9. value : {
10. type : distributedData.ValueType.STRING,
11. value : 'batch_test_string_value'
12. }
13. }
14. entries.push(entry);
15. }
16. kvStore.putBatch(entries, async function (err, data) {
17. console.log('putBatch success');
18. const query = new distributedData.Query();
19. query.prefixKey("batch_test");
20. kvStore.getResultSet(query, async function (err, result) {
21. console.log('getResultSet succeed.');
22. resultSet = result;
23. });
24. });
25. } catch(e) {
26. console.log('GetResultSet e ' + e);
27. }
```

### getResultSet8+

PhonePC/2in1TabletTVWearable

getResultSet(query: Query): Promise<KvStoreResultSet>

获取与指定Query对象匹配的KvStoreResultSet对象，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | [Query](js-apis-distributed-data.md#query8) | 是 | 表示查询对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[KvStoreResultSet](js-apis-distributed-data.md#kvstoreresultset8)> | Promise对象。获取与指定Query对象匹配的KvStoreResultSet对象。 |

**示例：**

```
1. let kvStore;
2. try {
3. let resultSet;
4. let entries = [];
5. for (var i = 0; i < 10; i++) {
6. var key = 'batch_test_string_key';
7. var entry = {
8. key : key + i,
9. value : {
10. type : distributedData.ValueType.STRING,
11. value : 'batch_test_string_value'
12. }
13. }
14. entries.push(entry);
15. }
16. kvStore.putBatch(entries).then(async (err) => {
17. console.log('putBatch success');
18. }).catch((err) => {
19. console.log('putBatch fail ' + JSON.stringify(err));
20. });
21. const query = new distributedData.Query();
22. query.prefixKey("batch_test");
23. kvStore.getResultSet(query).then((result) => {
24. console.log(' getResultSet succeed.');
25. resultSet = result;
26. }).catch((err) => {
27. console.log('getResultSet failed: ' + JSON.stringify(err));
28. });
29. }catch(e) {
30. console.log('GetResultSet e ' + e);
31. }
```

### closeResultSet8+

PhonePC/2in1TabletTVWearable

closeResultSet(resultSet: KvStoreResultSet, callback: AsyncCallback<void>): void

关闭由[SingleKVStore.getResultSet](js-apis-distributed-data.md#getresultset8)返回的KvStoreResultSet对象，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resultSet | [KvStoreResultSet](js-apis-distributed-data.md#kvstoreresultset8) | 是 | 表示要关闭的KvStoreResultSet对象。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. let kvStore;
2. try {
3. let resultSet = null;
4. kvStore.closeResultSet(resultSet, function (err, data) {
5. if (err == undefined) {
6. console.log('closeResultSet success');
7. } else {
8. console.log('closeResultSet fail');
9. }
10. });
11. }catch(e) {
12. console.log('CloseResultSet e ' + e);
13. }
```

### closeResultSet8+

PhonePC/2in1TabletTVWearable

closeResultSet(resultSet: KvStoreResultSet): Promise<void>

关闭由[SingleKVStore.getResultSet](js-apis-distributed-data.md#getresultset8)返回的KvStoreResultSet对象，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resultSet | [KvStoreResultSet](js-apis-distributed-data.md#kvstoreresultset8) | 是 | 表示要关闭的KvStoreResultSet对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. let kvStore;
2. try {
3. let resultSet = null;
4. kvStore.closeResultSet(resultSet).then(() => {
5. console.log('closeResultSet success');
6. }).catch((err) => {
7. console.log('closeResultSet fail ' + JSON.stringify(err));
8. });
9. }catch(e) {
10. console.log('CloseResultSet e ' + e);
11. }
```

### getResultSize8+

PhonePC/2in1TabletTVWearable

getResultSize(query: Query, callback: AsyncCallback<number>): void

获取与指定Query对象匹配的结果数，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | [Query](js-apis-distributed-data.md#query8) | 是 | 表示查询对象。 |
| callback | AsyncCallback<number> | 是 | 回调函数。返回与指定Query对象匹配的结果数。 |

**示例：**

```
1. let kvStore;
2. try {
3. let entries = [];
4. for (var i = 0; i < 10; i++) {
5. var key = 'batch_test_string_key';
6. var entry = {
7. key : key + i,
8. value : {
9. type : distributedData.ValueType.STRING,
10. value : 'batch_test_string_value'
11. }
12. }
13. entries.push(entry);
14. }
15. kvStore.putBatch(entries, async function (err, data) {
16. console.log('putBatch success');
17. const query = new distributedData.Query();
18. query.prefixKey("batch_test");
19. kvStore.getResultSize(query, async function (err, resultSize) {
20. console.log('getResultSet succeed.');
21. });
22. });
23. } catch(e) {
24. console.log('GetResultSize e ' + e);
25. }
```

### getResultSize8+

PhonePC/2in1TabletTVWearable

getResultSize(query: Query): Promise<number>

获取与指定Query对象匹配的结果数，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | [Query](js-apis-distributed-data.md#query8) | 是 | 表示查询对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。获取与指定Query对象匹配的结果数。 |

**示例：**

```
1. let kvStore;
2. try {
3. let entries = [];
4. for (var i = 0; i < 10; i++) {
5. var key = 'batch_test_string_key';
6. var entry = {
7. key : key + i,
8. value : {
9. type : distributedData.ValueType.STRING,
10. value : 'batch_test_string_value'
11. }
12. }
13. entries.push(entry);
14. }
15. kvStore.putBatch(entries).then(async (err) => {
16. console.log('putBatch success');
17. }).catch((err) => {
18. console.log('putBatch fail ' + JSON.stringify(err));
19. });
20. const query = new distributedData.Query();
21. query.prefixKey("batch_test");
22. kvStore.getResultSize(query).then((resultSize) => {
23. console.log('getResultSet succeed.');
24. }).catch((err) => {
25. console.log('getResultSet failed: ' + JSON.stringify(err));
26. });
27. }catch(e) {
28. console.log('GetResultSize e ' + e);
29. }
```

### removeDeviceData8+

PhonePC/2in1TabletTVWearable

removeDeviceData(deviceId: string, callback: AsyncCallback<void>): void

删除指定设备的数据，使用callback异步回调。

说明

其中deviceId通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

deviceId具体获取方式请参考[sync接口示例](js-apis-distributed-data.md#sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 表示要删除设备的名称。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. let kvStore;
2. const KEY_TEST_STRING_ELEMENT = 'key_test_string_2';
3. const VALUE_TEST_STRING_ELEMENT = 'value-string-002';
4. try {
5. kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT, async function (err,data) {
6. console.log('put success');
7. const deviceid = 'no_exist_device_id';
8. kvStore.removeDeviceData(deviceid, async function (err,data) {
9. if (err == undefined) {
10. console.log('removeDeviceData success');
11. } else {
12. console.log('removeDeviceData fail');
13. kvStore.get(KEY_TEST_STRING_ELEMENT, async function (err,data) {
14. console.log('RemoveDeviceData get success');
15. });
16. }
17. });
18. });
19. }catch(e) {
20. console.log('RemoveDeviceData e ' + e);
21. }
```

### removeDeviceData8+

PhonePC/2in1TabletTVWearable

removeDeviceData(deviceId: string): Promise<void>

删除指定设备的数据，使用Promise异步回调。

说明

其中deviceId通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

deviceId具体获取方式请参考[sync接口示例](js-apis-distributed-data.md#sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 表示要删除设备的名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. let kvStore;
2. const KEY_TEST_STRING_ELEMENT = 'key_test_string_2';
3. const VALUE_TEST_STRING_ELEMENT = 'value-string-001';
4. try {
5. kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT).then((err) => {
6. console.log('removeDeviceData put success');
7. }).catch((err) => {
8. console.log('put fail ' + JSON.stringify(err));
9. });
10. const deviceid = 'no_exist_device_id';
11. kvStore.removeDeviceData(deviceid).then((err) => {
12. console.log('removeDeviceData success');
13. }).catch((err) => {
14. console.log('removeDeviceData fail ' + JSON.stringify(err));
15. });
16. kvStore.get(KEY_TEST_STRING_ELEMENT).then((data) => {
17. console.log('get success data:' + data);
18. }).catch((err) => {
19. console.log('RemoveDeviceData get fail ' + JSON.stringify(err));
20. });
21. }catch(e) {
22. console.log('RemoveDeviceData e ' + e);
23. }
```

### sync

PhonePC/2in1TabletTVWearable

sync(deviceIds: string[], mode: SyncMode, delayMs?: number): void

在手动同步方式下，触发数据库同步。

说明

其中deviceIds为DeviceInfo中的networkId，通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

**需要权限**： ohos.permission.DISTRIBUTED\_DATASYNC。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceIds | string[] | 是 | 同一组网环境下，需要同步的设备的networkId列表。 |
| mode | [SyncMode](js-apis-distributed-data.md#syncmode) | 是 | 同步模式。 |
| delayMs | number | 否 | 可选参数，允许延时时间，单位：ms（毫秒），默认为0。 |

**示例：**

```
1. import deviceManager from '@ohos.distributedHardware.deviceManager';

3. let devManager;
4. let kvStore;
5. const KEY_TEST_SYNC_ELEMENT = 'key_test_sync';
6. const VALUE_TEST_SYNC_ELEMENT = 'value-string-001';
7. // create deviceManager
8. deviceManager.createDeviceManager('bundleName', (err, value) => {
9. if (!err) {
10. devManager = value;
11. let deviceIds = [];
12. if (devManager != null) {
13. var devices = devManager.getTrustedDeviceListSync();
14. for (var i = 0; i < devices.length; i++) {
15. deviceIds[i] = devices[i].networkId;
16. }
17. }
18. try {
19. kvStore.on('syncComplete', function (data) {
20. console.log('Sync dataChange');
21. });
22. kvStore.put(KEY_TEST_SYNC_ELEMENT + 'testSync101', VALUE_TEST_SYNC_ELEMENT, function (err, data) {
23. if (err != undefined) {
24. console.log("put err: " + JSON.stringify(err));
25. return;
26. }
27. console.log('Succeeded in putting data');
28. const mode = distributedData.SyncMode.PULL_ONLY;
29. kvStore.sync(deviceIds, mode, 1000);
30. });
31. } catch (e) {
32. console.log('Sync e' + e);
33. }
34. }
35. });
```

### on('dataChange')8+

PhonePC/2in1TabletTVWearable

on(event: 'dataChange', type: SubscribeType, listener: Callback<ChangeNotification>): void

订阅指定类型的数据变更通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 订阅的事件名，固定为'dataChange'，表示数据变更事件。 |
| type | [SubscribeType](js-apis-distributed-data.md#subscribetype) | 是 | 表示订阅的类型。 |
| listener | Callback<[ChangeNotification](js-apis-distributed-data.md#changenotification)> | 是 | 回调函数。 |

**示例：**

```
1. let kvStore;
2. kvStore.on('dataChange', distributedData.SubscribeType.SUBSCRIBE_TYPE_LOCAL, function (data) {
3. console.log("dataChange callback call data: " + JSON.stringify(data));
4. });
```

### on('syncComplete')8+

PhonePC/2in1TabletTVWearable

on(event: 'syncComplete', syncCallback: Callback<Array<[string, number]>>): void

订阅同步完成事件回调通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 订阅的事件名，固定为'syncComplete'，表示同步完成事件。 |
| syncCallback | Callback<Array<[string, number]>> | 是 | 回调函数。用于向调用方发送同步结果的回调。 |

**示例：**

```
1. let kvStore;
2. const KEY_TEST_FLOAT_ELEMENT = 'key_test_float';
3. const VALUE_TEST_FLOAT_ELEMENT = 321.12;
4. try {
5. kvStore.on('syncComplete', function (data) {
6. console.log('syncComplete ' + data)
7. });
8. kvStore.put(KEY_TEST_FLOAT_ELEMENT, VALUE_TEST_FLOAT_ELEMENT).then((data) => {
9. console.log('syncComplete put success');
10. }).catch((error) => {
11. console.log('syncComplete put fail ' + error);
12. });
13. }catch(e) {
14. console.log('syncComplete put e ' + e);
15. }
```

### off('dataChange')8+

PhonePC/2in1TabletTVWearable

off(event:'dataChange', listener?: Callback<ChangeNotification>): void

取消订阅数据变更通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取消订阅的事件名，固定为'dataChange'，表示数据变更事件。 |
| listener | Callback<[ChangeNotification](js-apis-distributed-data.md#changenotification)> | 否 | 取消订阅的函数。如不设置callback，则取消所有订阅的函数。 |

**示例：**

```
1. let kvStore;
2. class KvstoreModel {
3. call(data) {
4. console.log("dataChange: " + data);
5. }
6. subscribeDataChange() {
7. if (kvStore != null) {
8. kvStore.on('dataChange', distributedData.SubscribeType.SUBSCRIBE_TYPE_REMOTE, this.call);
9. }
10. }
11. unsubscribeDataChange() {
12. if (kvStore != null) {
13. kvStore.off('dataChange', this.call);
14. }
15. }
16. }
```

### off('syncComplete')8+

PhonePC/2in1TabletTVWearable

off(event: 'syncComplete', syncCallback?: Callback<Array<[string, number]>>): void

取消订阅同步完成事件回调通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取消订阅的事件名，固定为'syncComplete'，表示同步完成事件。 |
| syncCallback | Callback<Array<[string, number]>> | 否 | 取消订阅的函数。如不设置callback，则取消所有订阅的函数。 |

**示例：**

```
1. let kvStore;
2. class KvstoreModel {
3. call(data) {
4. console.log("syncComplete: " + data);
5. }
6. subscribeSyncComplete() {
7. if (kvStore != null) {
8. kvStore.on('syncComplete', this.call);
9. }
10. }
11. unsubscribeSyncComplete() {
12. if (kvStore != null) {
13. kvStore.off('syncComplete', this.call);
14. }
15. }
16. }
```

### setSyncParam8+

PhonePC/2in1TabletTVWearable

setSyncParam(defaultAllowedDelayMs: number, callback: AsyncCallback<void>): void

设置数据库同步允许的默认延迟，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| defaultAllowedDelayMs | number | 是 | 表示数据库同步允许的默认延迟，以毫秒为单位。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. let kvStore;
2. try {
3. const defaultAllowedDelayMs = 500;
4. kvStore.setSyncParam(defaultAllowedDelayMs, function (err,data) {
5. console.log('SetSyncParam put success');
6. });
7. }catch(e) {
8. console.log('testSingleKvStoreSetSyncParam e ' + e);
9. }
```

### setSyncParam8+

PhonePC/2in1TabletTVWearable

setSyncParam(defaultAllowedDelayMs: number): Promise<void>

设置数据库同步允许的默认延迟，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| defaultAllowedDelayMs | number | 是 | 表示数据库同步允许的默认延迟，以毫秒为单位。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. let kvStore;
2. try {
3. const defaultAllowedDelayMs = 500;
4. kvStore.setSyncParam(defaultAllowedDelayMs).then((err) => {
5. console.log('SetSyncParam put success');
6. }).catch((err) => {
7. console.log('SetSyncParam put fail ' + JSON.stringify(err));
8. });
9. }catch(e) {
10. console.log('SetSyncParam e ' + e);
11. }
```

### getSecurityLevel8+

PhonePC/2in1TabletTVWearable

getSecurityLevel(callback: AsyncCallback<SecurityLevel>): void

获取数据库的安全级别，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[SecurityLevel](js-apis-distributed-data.md#securitylevel)> | 是 | 回调函数。返回数据库的安全级别。 |

**示例：**

```
1. let kvStore;
2. try {
3. kvStore.getSecurityLevel(function (err,data) {
4. console.log('getSecurityLevel success');
5. });
6. }catch(e) {
7. console.log('GetSecurityLevel e ' + e);
8. }
```

### getSecurityLevel8+

PhonePC/2in1TabletTVWearable

getSecurityLevel(): Promise<SecurityLevel>

获取数据库的安全级别，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SecurityLevel](js-apis-distributed-data.md#securitylevel)> | Promise对象。返回数据库的安全级别。 |

**示例：**

```
1. let kvStore;
2. try {
3. kvStore.getSecurityLevel().then((data) => {
4. console.log(' getSecurityLevel success');
5. }).catch((err) => {
6. console.log('getSecurityLevel fail ' + JSON.stringify(err));
7. });
8. }catch(e) {
9. console.log('GetSecurityLevel e ' + e);
10. }
```

## DeviceKVStore8+

PhonePC/2in1TabletTVWearable

设备协同数据库，继承自KVStore，提供查询数据和同步数据的方法。

设备协同数据库，以设备维度对数据进行区分，每台设备仅能写入和修改本设备的数据，其它设备的数据对其是只读的，无法修改其它设备的数据。

比如，可以使用设备协同数据库实现设备间的图片分享，可以查看其他设备的图片，但无法修改和删除其他设备的图片。

在调用DeviceKVStore的方法前，需要先通过[getKVStore](js-apis-distributed-data.md#getkvstore)构建一个DeviceKVStore实例。

### get8+

PhonePC/2in1TabletTVWearable

get(deviceId: string, key: string, callback: AsyncCallback<boolean|string|number|Uint8Array>): void

获取与指定设备ID和key匹配的string值，使用callback异步回调。

说明

其中deviceId通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

deviceId具体获取方式请参考[sync接口示例](js-apis-distributed-data.md#sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 标识要查询其数据的设备。 |
| key | string | 是 | 表示要查询key值的键。 |
| callback | AsyncCallback<boolean|string|number|Uint8Array> | 是 | 回调函数，返回匹配给定条件的字符串值。 |

**示例：**

```
1. let kvStore;
2. const KEY_TEST_STRING_ELEMENT = 'key_test_string_2';
3. const VALUE_TEST_STRING_ELEMENT = 'value-string-002';
4. try{
5. kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT, async function (err,data) {
6. console.log('put success');
7. kvStore.get('localDeviceId', KEY_TEST_STRING_ELEMENT, function (err,data) {
8. console.log('get success');
9. });
10. })
11. }catch(e) {
12. console.log('get e' + e);
13. }
```

### get8+

PhonePC/2in1TabletTVWearable

get(deviceId: string, key: string): Promise<boolean|string|number|Uint8Array>

获取与指定设备ID和key匹配的string值，使用Promise异步回调。

说明

其中deviceId通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

deviceId具体获取方式请参考[sync接口示例](js-apis-distributed-data.md#sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 标识要查询其数据的设备。 |
| key | string | 是 | 表示要查询key值的键。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean|string|number|Uint8Array> | Promise对象。返回匹配给定条件的字符串值。 |

**示例：**

```
1. let kvStore;
2. const KEY_TEST_STRING_ELEMENT = 'key_test_string_2';
3. const VALUE_TEST_STRING_ELEMENT = 'value-string-002';
4. try {
5. kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT).then(async (data) => {
6. console.log(' put success');
7. kvStore.get('localDeviceId', KEY_TEST_STRING_ELEMENT).then((data) => {
8. console.log('get success');
9. }).catch((err) => {
10. console.log('get fail ' + JSON.stringify(err));
11. });
12. }).catch((error) => {
13. console.log('put error' + error);
14. });
15. } catch (e) {
16. console.log('Get e ' + e);
17. }
```

### getEntries8+

PhonePC/2in1TabletTVWearable

getEntries(deviceId: string, keyPrefix: string, callback: AsyncCallback<Entry[]>): void

获取与指定设备ID和key前缀匹配的所有键值对，使用callback异步回调。

说明

其中deviceId通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

deviceId具体获取方式请参考[sync接口示例](js-apis-distributed-data.md#sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 标识要查询其数据的设备。 |
| keyPrefix | string | 是 | 表示要匹配的键前缀。 |
| callback | AsyncCallback<[Entry](js-apis-distributed-data.md#entry)[]> | 是 | 回调函数，返回满足给定条件的所有键值对的列表。 |

**示例：**

```
1. let kvStore;
2. try {
3. let entries = [];
4. for (var i = 0; i < 10; i++) {
5. var key = 'batch_test_string_key';
6. var entry = {
7. key : key + i,
8. value : {
9. type : distributedData.ValueType.STRING,
10. value : 'batch_test_string_value'
11. }
12. }
13. entries.push(entry);
14. }
15. console.log('entries: ' + entries);
16. kvStore.putBatch(entries, async function (err,data) {
17. console.log('putBatch success');
18. kvStore.getEntries('localDeviceId', 'batch_test_string_key', function (err,entries) {
19. console.log('getEntries success');
20. console.log('entries.length: ' + entries.length);
21. console.log('entries[0]: ' + JSON.stringify(entries[0]));
22. });
23. });
24. }catch(e) {
25. console.log('PutBatch e ' + e);
26. }
```

### getEntries8+

PhonePC/2in1TabletTVWearable

getEntries(deviceId: string, keyPrefix: string): Promise<Entry[]>

获取与指定设备ID和key前缀匹配的所有键值对，使用Promise异步回调。

说明

其中deviceId通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

deviceId具体获取方式请参考[sync接口示例](js-apis-distributed-data.md#sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 标识要查询其数据的设备。 |
| keyPrefix | string | 是 | 表示要匹配的键前缀。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Entry](js-apis-distributed-data.md#entry)[]> | Promise对象。返回匹配给定条件的所有键值对的列表。 |

**示例：**

```
1. let kvStore;
2. try {
3. let entries = [];
4. for (var i = 0; i < 10; i++) {
5. var key = 'batch_test_string_key';
6. var entry = {
7. key : key + i,
8. value : {
9. type : distributedData.ValueType.STRING,
10. value : 'batch_test_string_value'
11. }
12. }
13. entries.push(entry);
14. }
15. console.log('entries: ' + entries);
16. kvStore.putBatch(entries).then(async (err) => {
17. console.log('putBatch success');
18. kvStore.getEntries('localDeviceId', 'batch_test_string_key').then((entries) => {
19. console.log('getEntries success');
20. console.log('entries.length: ' + entries.length);
21. console.log('entries[0]: ' + JSON.stringify(entries[0]));
22. console.log('entries[0].value: ' + JSON.stringify(entries[0].value));
23. console.log('entries[0].value.value: ' + entries[0].value.value);
24. }).catch((err) => {
25. console.log('getEntries fail ' + JSON.stringify(err));
26. });
27. }).catch((err) => {
28. console.log('putBatch fail ' + JSON.stringify(err));
29. });
30. }catch(e) {
31. console.log('PutBatch e ' + e);
32. }
```

### getEntries8+

PhonePC/2in1TabletTVWearable

getEntries(query: Query, callback: AsyncCallback<Entry[]>): void

获取与指定Query对象匹配的键值对列表，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | [Query](js-apis-distributed-data.md#query8) | 是 | 表示查询对象。 |
| callback | AsyncCallback<[Entry](js-apis-distributed-data.md#entry)[]> | 是 | 回调函数，返回与指定Query对象匹配的键值对列表。 |

**示例：**

```
1. let kvStore;
2. try {
3. var arr = new Uint8Array([21,31]);
4. let entries = [];
5. for (var i = 0; i < 10; i++) {
6. var key = 'batch_test_bool_key';
7. var entry = {
8. key : key + i,
9. value : {
10. type : distributedData.ValueType.BYTE_ARRAY,
11. value : arr
12. }
13. }
14. entries.push(entry);
15. }
16. console.log('entries: ' + JSON.stringify(entries));
17. kvStore.putBatch(entries, async function (err,data) {
18. console.log('putBatch success');
19. const query = new distributedData.Query();
20. query.prefixKey("batch_test");
21. query.deviceId('localDeviceId');
22. kvStore.getEntries(query, function (err,entries) {
23. console.log('getEntries success');
24. console.log('entries.length: ' + entries.length);
25. console.log('entries[0]: ' + JSON.stringify(entries[0]));
26. });
27. });
28. console.log('GetEntries success');
29. }catch(e) {
30. console.log('GetEntries e ' + e);
31. }
```

### getEntries8+

PhonePC/2in1TabletTVWearable

getEntries(query: Query): Promise<Entry[]>

获取与指定Query对象匹配的键值对列表，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | [Query](js-apis-distributed-data.md#query8) | 是 | 表示查询对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Entry](js-apis-distributed-data.md#entry)[]> | Promise对象。返回与指定Query对象匹配的键值对列表。 |

**示例：**

```
1. let kvStore;
2. try {
3. var arr = new Uint8Array([21,31]);
4. let entries = [];
5. for (var i = 0; i < 10; i++) {
6. var key = 'batch_test_bool_key';
7. var entry = {
8. key : key + i,
9. value : {
10. type : distributedData.ValueType.BYTE_ARRAY,
11. value : arr
12. }
13. }
14. entries.push(entry);
15. }
16. console.log('entries: ' + JSON.stringify(entries));
17. kvStore.putBatch(entries).then(async (err) => {
18. console.log('putBatch success');
19. const query = new distributedData.Query();
20. query.prefixKey("batch_test");
21. kvStore.getEntries(query).then((entries) => {
22. console.log('getEntries success');
23. }).catch((err) => {
24. console.log('getEntries fail ' + JSON.stringify(err));
25. });
26. }).catch((err) => {
27. console.log('GetEntries putBatch fail ' + JSON.stringify(err))
28. });
29. console.log('GetEntries success');
30. }catch(e) {
31. console.log('GetEntries e ' + e);
32. }
```

### getEntries8+

PhonePC/2in1TabletTVWearable

getEntries(deviceId: string, query: Query, callback: AsyncCallback<Entry[]>): void

获取与指定设备ID和Query对象匹配的键值对列表，使用callback异步回调。

说明

其中deviceId通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

deviceId具体获取方式请参考[sync接口示例](js-apis-distributed-data.md#sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 键值对所属的设备ID。 |
| query | [Query](js-apis-distributed-data.md#query8) | 是 | 表示查询对象。 |
| callback | AsyncCallback<[Entry](js-apis-distributed-data.md#entry)[]> | 是 | 回调函数。返回与指定设备ID和Query对象匹配的键值对列表。 |

**示例：**

```
1. let kvStore;
2. try {
3. var arr = new Uint8Array([21,31]);
4. let entries = [];
5. for (var i = 0; i < 10; i++) {
6. var key = 'batch_test_bool_key';
7. var entry = {
8. key : key + i,
9. value : {
10. type : distributedData.ValueType.BYTE_ARRAY,
11. value : arr
12. }
13. }
14. entries.push(entry);
15. }
16. console.log('entries: ' + JSON.stringify(entries));
17. kvStore.putBatch(entries, async function (err,data) {
18. console.log('putBatch success');
19. var query = new distributedData.Query();
20. query.deviceId('localDeviceId');
21. query.prefixKey("batch_test");
22. kvStore.getEntries('localDeviceId', query, function (err,entries) {
23. console.log('getEntries success');
24. console.log('entries.length: ' + entries.length);
25. console.log('entries[0]: ' + JSON.stringify(entries[0]));
26. })
27. });
28. console.log('GetEntries success');
29. }catch(e) {
30. console.log('GetEntries e ' + e);
31. }
```

### getEntries8+

PhonePC/2in1TabletTVWearable

getEntries(deviceId: string, query: Query): Promise<Entry[]>

获取与指定设备ID和Query对象匹配的键值对列表，使用Promise异步回调。

说明

其中deviceId通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

deviceId具体获取方式请参考[sync接口示例](js-apis-distributed-data.md#sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 键值对所属的设备ID。 |
| query | [Query](js-apis-distributed-data.md#query8) | 是 | 表示查询对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Entry](js-apis-distributed-data.md#entry)[]> | Promise对象。返回与指定设备ID和Query对象匹配的键值对列表。 |

**示例：**

```
1. let kvStore;
2. try {
3. var arr = new Uint8Array([21,31]);
4. let entries = [];
5. for (var i = 0; i < 10; i++) {
6. var key = 'batch_test_bool_key';
7. var entry = {
8. key : key + i,
9. value : {
10. type : distributedData.ValueType.BYTE_ARRAY,
11. value : arr
12. }
13. }
14. entries.push(entry);
15. }
16. console.log('entries: ' + JSON.stringify(entries));
17. kvStore.putBatch(entries).then(async (err) => {
18. console.log('putBatch success');
19. var query = new distributedData.Query();
20. query.deviceId('localDeviceId');
21. query.prefixKey("batch_test");
22. kvStore.getEntries('localDeviceId', query).then((entries) => {
23. console.log('getEntries success');
24. }).catch((err) => {
25. console.log('getEntries fail ' + JSON.stringify(err));
26. });
27. }).catch((err) => {
28. console.log('putBatch fail ' + JSON.stringify(err));
29. });
30. console.log('GetEntries success');
31. }catch(e) {
32. console.log('GetEntries e ' + e);
33. }
```

### getResultSet8+

PhonePC/2in1TabletTVWearable

getResultSet(deviceId: string, keyPrefix: string, callback: AsyncCallback<KvStoreResultSet>): void

获取与指定设备ID和key前缀匹配的KvStoreResultSet对象，使用callback异步回调。

说明

其中deviceId通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

deviceId具体获取方式请参考[sync接口示例](js-apis-distributed-data.md#sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 标识要查询其数据的设备。 |
| keyPrefix | string | 是 | 表示要匹配的键前缀。 |
| callback | AsyncCallback<[KvStoreResultSet](js-apis-distributed-data.md#kvstoreresultset8)> | 是 | 回调函数。返回与指定设备ID和key前缀匹配的KvStoreResultSet对象。 |

**示例：**

```
1. let kvStore;
2. try {
3. let resultSet;
4. kvStore.getResultSet('localDeviceId', 'batch_test_string_key', async function (err, result) {
5. console.log('getResultSet succeed.');
6. resultSet = result;
7. kvStore.closeResultSet(resultSet, function (err, data) {
8. console.log('closeResultSet success');
9. })
10. });
11. }catch(e) {
12. console.log('GetResultSet e ' + e);
13. }
```

### getResultSet8+

PhonePC/2in1TabletTVWearable

getResultSet(deviceId: string, keyPrefix: string): Promise<KvStoreResultSet>

获取与指定设备ID和key前缀匹配的KvStoreResultSet对象，使用Promise异步回调。

说明

其中deviceId通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

deviceId具体获取方式请参考[sync接口示例](js-apis-distributed-data.md#sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 标识要查询其数据的设备。 |
| keyPrefix | string | 是 | 表示要匹配的键前缀。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[KvStoreResultSet](js-apis-distributed-data.md#kvstoreresultset8)> | Promise对象。返回与指定设备ID和key前缀匹配的KvStoreResultSet对象。 |

**示例：**

```
1. let kvStore;
2. try {
3. let resultSet;
4. kvStore.getResultSet('localDeviceId', 'batch_test_string_key').then((result) => {
5. console.log('getResultSet succeed.');
6. resultSet = result;
7. }).catch((err) => {
8. console.log('getResultSet failed: ' + JSON.stringify(err));
9. });
10. kvStore.closeResultSet(resultSet).then((err) => {
11. console.log('closeResultSet success');
12. }).catch((err) => {
13. console.log('closeResultSet fail ' + JSON.stringify(err));
14. });
15. }catch(e) {
16. console.log('GetResultSet e ' + e);
17. }
```

### getResultSet8+

PhonePC/2in1TabletTVWearable

getResultSet(query: Query, callback: AsyncCallback<KvStoreResultSet>): void

获取与指定Query对象匹配的KvStoreResultSet对象，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | [Query](js-apis-distributed-data.md#query8) | 是 | 表示查询对象。 |
| callback | AsyncCallback<[KvStoreResultSet](js-apis-distributed-data.md#kvstoreresultset8)> | 是 | 回调函数，返回与指定Query对象匹配的KvStoreResultSet对象。 |

**示例：**

```
1. let kvStore;
2. try {
3. let resultSet;
4. let entries = [];
5. for (var i = 0; i < 10; i++) {
6. var key = 'batch_test_string_key';
7. var entry = {
8. key : key + i,
9. value : {
10. type : distributedData.ValueType.STRING,
11. value : 'batch_test_string_value'
12. }
13. }
14. entries.push(entry);
15. }
16. kvStore.putBatch(entries, async function (err, data) {
17. console.log('putBatch success');
18. const query = new distributedData.Query();
19. query.prefixKey("batch_test");
20. query.deviceId('localDeviceId');
21. kvStore.getResultSet(query, async function (err, result) {
22. console.log('getResultSet succeed.');
23. resultSet = result;
24. kvStore.closeResultSet(resultSet, function (err, data) {
25. console.log('closeResultSet success');
26. })
27. });
28. });
29. } catch(e) {
30. console.log('GetResultSet e ' + e);
31. }
```

### getResultSet8+

PhonePC/2in1TabletTVWearable

getResultSet(query: Query): Promise<KvStoreResultSet>

获取与指定Query对象匹配的KvStoreResultSet对象，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | [Query](js-apis-distributed-data.md#query8) | 是 | 表示查询对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[KvStoreResultSet](js-apis-distributed-data.md#kvstoreresultset8)> | Promise对象。返回与指定Query对象匹配的KvStoreResultSet对象。 |

**示例：**

```
1. let kvStore;
2. try {
3. let resultSet;
4. let entries = [];
5. for (var i = 0; i < 10; i++) {
6. var key = 'batch_test_string_key';
7. var entry = {
8. key : key + i,
9. value : {
10. type : distributedData.ValueType.STRING,
11. value : 'batch_test_string_value'
12. }
13. }
14. entries.push(entry);
15. }
16. kvStore.putBatch(entries).then(async (err) => {
17. console.log('putBatch success');
18. }).catch((err) => {
19. console.log('putBatch fail ' + err);
20. });
21. const query = new distributedData.Query();
22. query.deviceId('localDeviceId');
23. query.prefixKey("batch_test");
24. console.log("GetResultSet " + query.getSqlLike());
25. kvStore.getResultSet(query).then((result) => {
26. console.log('getResultSet succeed.');
27. resultSet = result;
28. }).catch((err) => {
29. console.log('getResultSet failed: ' + JSON.stringify(err));
30. });
31. kvStore.closeResultSet(resultSet).then((err) => {
32. console.log('closeResultSet success');
33. }).catch((err) => {
34. console.log('closeResultSet fail ' + JSON.stringify(err));
35. });
36. }catch(e) {
37. console.log('GetResultSet e ' + e);
38. }
```

### getResultSet8+

PhonePC/2in1TabletTVWearable

getResultSet(deviceId: string, query: Query, callback: AsyncCallback<KvStoreResultSet>): void

获取与指定设备ID和Query对象匹配的KvStoreResultSet对象，使用callback异步回调。

说明

其中deviceId通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

deviceId具体获取方式请参考[sync接口示例](js-apis-distributed-data.md#sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | KvStoreResultSet对象所属的设备ID。 |
| query | [Query](js-apis-distributed-data.md#query8) | 是 | 表示查询对象。 |
| callback | AsyncCallback<[KvStoreResultSet](js-apis-distributed-data.md#kvstoreresultset8)> | 是 | 回调函数。返回与指定设备ID和Query对象匹配的KvStoreResultSet对象。 |

**示例：**

```
1. let kvStore;
2. try {
3. let resultSet;
4. let entries = [];
5. for (var i = 0; i < 10; i++) {
6. var key = 'batch_test_string_key';
7. var entry = {
8. key : key + i,
9. value : {
10. type : distributedData.ValueType.STRING,
11. value : 'batch_test_string_value'
12. }
13. }
14. entries.push(entry);
15. }
16. kvStore.putBatch(entries, async function (err, data) {
17. console.log('putBatch success');
18. const query = new distributedData.Query();
19. query.prefixKey("batch_test");
20. kvStore.getResultSet('localDeviceId', query, async function (err, result) {
21. console.log('getResultSet succeed.');
22. resultSet = result;
23. kvStore.closeResultSet(resultSet, function (err, data) {
24. console.log('closeResultSet success');
25. })
26. });
27. });
28. } catch(e) {
29. console.log('GetResultSet e ' + e);
30. }
```

### getResultSet8+

PhonePC/2in1TabletTVWearable

getResultSet(deviceId: string, query: Query): Promise<KvStoreResultSet>

获取与指定设备ID和Query对象匹配的KvStoreResultSet对象，使用Promise异步回调。

说明

其中deviceId通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

deviceId具体获取方式请参考[sync接口示例](js-apis-distributed-data.md#sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | KvStoreResultSet对象所属的设备ID。 |
| query | [Query](js-apis-distributed-data.md#query8) | 是 | 表示查询对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[KvStoreResultSet](js-apis-distributed-data.md#kvstoreresultset8)> | Promise对象。返回与指定设备ID和Query对象匹配的KvStoreResultSet对象。 |

**示例：**

```
1. let kvStore;
2. try {
3. let resultSet;
4. let entries = [];
5. for (var i = 0; i < 10; i++) {
6. var key = 'batch_test_string_key';
7. var entry = {
8. key : key + i,
9. value : {
10. type : distributedData.ValueType.STRING,
11. value : 'batch_test_string_value'
12. }
13. }
14. entries.push(entry);
15. }
16. kvStore.putBatch(entries).then(async (err) => {
17. console.log('GetResultSet putBatch success');
18. }).catch((err) => {
19. console.log('PutBatch putBatch fail ' + JSON.stringify(err));
20. });
21. const query = new distributedData.Query();
22. query.prefixKey("batch_test");
23. kvStore.getResultSet('localDeviceId', query).then((result) => {
24. console.log('GetResultSet getResultSet succeed.');
25. resultSet = result;
26. }).catch((err) => {
27. console.log('GetResultSet getResultSet failed: ' + JSON.stringify(err));
28. });
29. query.deviceId('localDeviceId');
30. console.log("GetResultSet " + query.getSqlLike());
31. kvStore.closeResultSet(resultSet).then((err) => {
32. console.log('GetResultSet closeResultSet success');
33. }).catch((err) => {
34. console.log('GetResultSet closeResultSet fail ' + JSON.stringify(err));
35. });

37. }catch(e) {
38. console.log('GetResultSet e ' + e);
39. }
```

### closeResultSet8+

PhonePC/2in1TabletTVWearable

closeResultSet(resultSet: KvStoreResultSet, callback: AsyncCallback<void>): void

关闭由[DeviceKVStore.getResultSet](js-apis-distributed-data.md#getresultset8-4)返回的KvStoreResultSet对象，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resultSet | [KvStoreResultSet](js-apis-distributed-data.md#kvstoreresultset8) | 是 | 指示要关闭的KvStoreResultSet对象。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. let kvStore;
2. try {
3. console.log('CloseResultSet success');
4. let resultSet = null;
5. kvStore.closeResultSet(resultSet, function (err, data) {
6. if (err == undefined) {
7. console.log('closeResultSet success');
8. } else {
9. console.log('closeResultSet fail');
10. }
11. });
12. }catch(e) {
13. console.log('CloseResultSet e ' + e);
14. }
```

### closeResultSet8+

PhonePC/2in1TabletTVWearable

closeResultSet(resultSet: KvStoreResultSet): Promise<void>

关闭由[DeviceKVStore.getResultSet](js-apis-distributed-data.md#getresultset8-4)返回的KvStoreResultSet对象，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resultSet | [KvStoreResultSet](js-apis-distributed-data.md#kvstoreresultset8) | 是 | 指示要关闭的KvStoreResultSet对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. let kvStore;
2. try {
3. console.log('CloseResultSet success');
4. let resultSet = null;
5. kvStore.closeResultSet(resultSet).then(() => {
6. console.log('closeResultSet success');
7. }).catch((err) => {
8. console.log('closeResultSet fail ' + JSON.stringify(err));
9. });
10. }catch(e) {
11. console.log('CloseResultSet e ' + e);
12. }
```

### getResultSize8+

PhonePC/2in1TabletTVWearable

getResultSize(query: Query, callback: AsyncCallback<number>): void

获取与指定Query对象匹配的结果数，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | [Query](js-apis-distributed-data.md#query8) | 是 | 表示查询对象。 |
| callback | AsyncCallback<number> | 是 | 回调函数，返回与指定Query对象匹配的结果数。 |

**示例：**

```
1. let kvStore;
2. try {
3. let entries = [];
4. for (var i = 0; i < 10; i++) {
5. var key = 'batch_test_string_key';
6. var entry = {
7. key : key + i,
8. value : {
9. type : distributedData.ValueType.STRING,
10. value : 'batch_test_string_value'
11. }
12. }
13. entries.push(entry);
14. }
15. kvStore.putBatch(entries, async function (err, data) {
16. console.log('putBatch success');
17. const query = new distributedData.Query();
18. query.prefixKey("batch_test");
19. query.deviceId('localDeviceId');
20. kvStore.getResultSize(query, async function (err, resultSize) {
21. console.log('getResultSet succeed.');
22. });
23. });
24. } catch(e) {
25. console.log('GetResultSize e ' + e);
26. }
```

### getResultSize8+

PhonePC/2in1TabletTVWearable

getResultSize(query: Query): Promise<number>

获取与指定Query对象匹配的结果数，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | [Query](js-apis-distributed-data.md#query8) | 是 | 表示查询对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回与指定Query对象匹配的结果数。 |

**示例：**

```
1. let kvStore;
2. try {
3. let entries = [];
4. for (var i = 0; i < 10; i++) {
5. var key = 'batch_test_string_key';
6. var entry = {
7. key : key + i,
8. value : {
9. type : distributedData.ValueType.STRING,
10. value : 'batch_test_string_value'
11. }
12. }
13. entries.push(entry);
14. }
15. kvStore.putBatch(entries).then(async (err) => {
16. console.log('putBatch success');
17. }).catch((err) => {
18. console.log('putBatch fail ' + JSON.stringify(err));
19. });
20. const query = new distributedData.Query();
21. query.prefixKey("batch_test");
22. query.deviceId('localDeviceId');
23. kvStore.getResultSize(query).then((resultSize) => {
24. console.log('getResultSet succeed.');
25. }).catch((err) => {
26. console.log('getResultSet failed: ' + JSON.stringify(err));
27. });
28. }catch(e) {
29. console.log('GetResultSize e ' + e);
30. }
```

### getResultSize8+

PhonePC/2in1TabletTVWearable

getResultSize(deviceId: string, query: Query, callback: AsyncCallback<number>): void;

获取与指定设备ID和Query对象匹配的结果数，使用callback异步回调。

说明

其中deviceId通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

deviceId具体获取方式请参考[sync接口示例](js-apis-distributed-data.md#sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | KvStoreResultSet对象所属的设备ID。 |
| query | [Query](js-apis-distributed-data.md#query8) | 是 | 表示查询对象。 |
| callback | AsyncCallback<number> | 是 | 回调函数。返回与指定设备ID和Query对象匹配的结果数。 |

**示例：**

```
1. let kvStore;
2. try {
3. let entries = [];
4. for (var i = 0; i < 10; i++) {
5. var key = 'batch_test_string_key';
6. var entry = {
7. key : key + i,
8. value : {
9. type : distributedData.ValueType.STRING,
10. value : 'batch_test_string_value'
11. }
12. }
13. entries.push(entry);
14. }
15. kvStore.putBatch(entries, async function (err, data) {
16. console.log('putBatch success');
17. const query = new distributedData.Query();
18. query.prefixKey("batch_test");
19. kvStore.getResultSize('localDeviceId', query, async function (err, resultSize) {
20. console.log('getResultSet succeed.');
21. });
22. });
23. } catch(e) {
24. console.log('GetResultSize e ' + e);
25. }
```

### getResultSize8+

PhonePC/2in1TabletTVWearable

getResultSize(deviceId: string, query: Query): Promise<number>

获取与指定设备ID和Query对象匹配的结果数，使用Promise异步回调。

说明

其中deviceId通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

deviceId具体获取方式请参考[sync接口示例](js-apis-distributed-data.md#sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | KvStoreResultSet对象所属的设备ID。 |
| query | [Query](js-apis-distributed-data.md#query8) | 是 | 表示查询对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回与指定设备ID和Query对象匹配的结果数。 |

**示例：**

```
1. let kvStore;
2. try {
3. let entries = [];
4. for (var i = 0; i < 10; i++) {
5. var key = 'batch_test_string_key';
6. var entry = {
7. key : key + i,
8. value : {
9. type : distributedData.ValueType.STRING,
10. value : 'batch_test_string_value'
11. }
12. }
13. entries.push(entry);
14. }
15. kvStore.putBatch(entries).then(async (err) => {
16. console.log('putBatch success');
17. }).catch((err) => {
18. console.log('putBatch fail ' + JSON.stringify(err));
19. });
20. var query = new distributedData.Query();
21. query.prefixKey("batch_test");
22. kvStore.getResultSize('localDeviceId', query).then((resultSize) => {
23. console.log('getResultSet succeed.');
24. }).catch((err) => {
25. console.log('getResultSet failed: ' + JSON.stringify(err));
26. });
27. }catch(e) {
28. console.log('GetResultSize e ' + e);
29. }
```

### removeDeviceData8+

PhonePC/2in1TabletTVWearable

removeDeviceData(deviceId: string, callback: AsyncCallback<void>): void

从当前数据库中删除指定设备的数据，使用callback异步回调。

说明

其中deviceId通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

deviceId具体获取方式请参考[sync接口示例](js-apis-distributed-data.md#sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 标识要删除其数据的设备。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. let kvStore;
2. const KEY_TEST_STRING_ELEMENT = 'key_test_string';
3. const VALUE_TEST_STRING_ELEMENT = 'value-string-001';
4. try {
5. kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT, async function (err,data) {
6. console.log('RemoveDeviceData  put success');
7. const deviceid = 'no_exist_device_id';
8. kvStore.removeDeviceData(deviceid, async function (err,data) {
9. if (err == undefined) {
10. console.log('removeDeviceData success');
11. } else {
12. console.log('removeDeviceData fail');
13. kvStore.get('localDeviceId', KEY_TEST_STRING_ELEMENT, async function (err,data) {
14. console.log('RemoveDeviceData get success');
15. });
16. }
17. });
18. });
19. }catch(e) {
20. console.log('RemoveDeviceData e ' + e);
21. }
```

### removeDeviceData8+

PhonePC/2in1TabletTVWearable

removeDeviceData(deviceId: string): Promise<void>

从当前数据库中删除指定设备的数据，使用Promise异步回调。

说明

其中deviceId通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

deviceId具体获取方式请参考[sync接口示例](js-apis-distributed-data.md#sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 标识要删除其数据的设备。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. let kvStore;
2. const KEY_TEST_STRING_ELEMENT = 'key_test_string';
3. const VALUE_TEST_STRING_ELEMENT = 'value-string-001';
4. try {
5. kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT).then((err) => {
6. console.log('RemoveDeviceData put success');
7. }).catch((err) => {
8. console.log('RemoveDeviceData put fail ' + JSON.stringify(err));
9. });
10. const deviceid = 'no_exist_device_id';
11. kvStore.removeDeviceData(deviceid).then((err) => {
12. console.log('removeDeviceData success');
13. }).catch((err) => {
14. console.log('removeDeviceData fail ' + JSON.stringify(err));
15. });
16. kvStore.get('localDeviceId', KEY_TEST_STRING_ELEMENT).then((data) => {
17. console.log('RemoveDeviceData get success data:' + data);
18. }).catch((err) => {
19. console.log('RemoveDeviceData get fail ' + JSON.stringify(err));
20. });
21. }catch(e) {
22. console.log('RemoveDeviceData e ' + e);
23. }
```

### sync8+

PhonePC/2in1TabletTVWearable

sync(deviceIds: string[], mode: SyncMode, delayMs?: number): void

在手动同步方式下，触发数据库同步。

说明

其中deviceIds为DeviceInfo中的networkId，通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

**需要权限**： ohos.permission.DISTRIBUTED\_DATASYNC。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceIds | string[] | 是 | 需要同步DeviceKVStore数据库的设备networkId列表。 |
| mode | [SyncMode](js-apis-distributed-data.md#syncmode) | 是 | 同步模式。 |
| delayMs | number | 否 | 可选参数，允许延时时间，单位：ms（毫秒），默认为0。 |

**示例：**

```
1. import deviceManager from '@ohos.distributedHardware.deviceManager';

3. let devManager;
4. let kvStore;
5. const KEY_TEST_SYNC_ELEMENT = 'key_test_sync';
6. const VALUE_TEST_SYNC_ELEMENT = 'value-string-001';
7. // create deviceManager
8. deviceManager.createDeviceManager('bundleName', (err, value) => {
9. if (!err) {
10. devManager = value;
11. let deviceIds = [];
12. if (devManager != null) {
13. var devices = devManager.getTrustedDeviceListSync();
14. for (var i = 0; i < devices.length; i++) {
15. deviceIds[i] = devices[i].networkId;
16. }
17. }
18. try {
19. kvStore.on('syncComplete', function (data) {
20. console.log('Sync dataChange');
21. });
22. kvStore.put(KEY_TEST_SYNC_ELEMENT + 'testSync101', VALUE_TEST_SYNC_ELEMENT, function (err, data) {
23. if (err != undefined) {
24. console.log("put err: " + JSON.stringify(err));
25. return;
26. }
27. console.log('Succeeded in putting data');
28. const mode = distributedData.SyncMode.PULL_ONLY;
29. kvStore.sync(deviceIds, mode, 1000);
30. });
31. } catch (e) {
32. console.log('Sync e' + e);
33. }
34. }
35. });
```

### on('dataChange')8+

PhonePC/2in1TabletTVWearable

on(event: 'dataChange', type: SubscribeType, listener: Callback<ChangeNotification>): void

订阅指定类型的数据变更通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 订阅的事件名，固定为'dataChange'，表示数据变更事件。 |
| type | [SubscribeType](js-apis-distributed-data.md#subscribetype) | 是 | 表示订阅的类型。 |
| listener | Callback<[ChangeNotification](js-apis-distributed-data.md#changenotification)> | 是 | 回调函数。 |

**示例：**

```
1. let kvStore;
2. kvStore.on('dataChange', distributedData.SubscribeType.SUBSCRIBE_TYPE_LOCAL, function (data) {
3. console.log("dataChange callback call data: " + JSON.stringify(data));
4. });
```

### on('syncComplete')8+

PhonePC/2in1TabletTVWearable

on(event: 'syncComplete', syncCallback: Callback<Array<[string, number]>>): void

订阅同步完成事件回调通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 订阅的事件名，固定为'syncComplete'，表示同步完成事件。 |
| syncCallback | Callback<Array<[string, number]>> | 是 | 回调函数。用于向调用方发送同步结果的回调。 |

**示例：**

```
1. let kvStore;
2. const KEY_TEST_FLOAT_ELEMENT = 'key_test_float';
3. const VALUE_TEST_FLOAT_ELEMENT = 321.12;
4. try {
5. kvStore.on('syncComplete', function (data) {
6. console.log('syncComplete ' + data)
7. });
8. kvStore.put(KEY_TEST_FLOAT_ELEMENT, VALUE_TEST_FLOAT_ELEMENT).then((data) => {
9. console.log('syncComplete put success');
10. }).catch((error) => {
11. console.log('syncComplete put fail ' + error);
12. });
13. }catch(e) {
14. console.log('syncComplete put e ' + e);
15. }
```

### off('dataChange')8+

PhonePC/2in1TabletTVWearable

off(event:'dataChange', listener?: Callback<ChangeNotification>): void

取消订阅数据变更通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取消订阅的事件名，固定为'dataChange'，表示数据变更事件。 |
| listener | Callback<[ChangeNotification](js-apis-distributed-data.md#changenotification)> | 否 | 取消订阅的函数。如不设置callback，则取消所有订阅的函数。 |

**示例：**

```
1. let kvStore;
2. class KvstoreModel {
3. call(data) {
4. console.log("dataChange: " + data);
5. }
6. subscribeDataChange() {
7. if (kvStore != null) {
8. kvStore.on('dataChange', distributedData.SubscribeType.SUBSCRIBE_TYPE_REMOTE, this.call);
9. }
10. }
11. unsubscribeDataChange() {
12. if (kvStore != null) {
13. kvStore.off('dataChange', this.call);
14. }
15. }
16. }
```

### off('syncComplete')8+

PhonePC/2in1TabletTVWearable

off(event: 'syncComplete', syncCallback?: Callback<Array<[string, number]>>): void

取消订阅同步完成事件回调通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取消订阅的事件名，固定为'syncComplete'，表示同步完成事件。 |
| syncCallback | Callback<Array<[string, number]>> | 否 | 取消订阅的函数。如不设置callback，则取消所有订阅的函数。 |

**示例：**

```
1. let kvStore;
2. class KvstoreModel {
3. call(data) {
4. console.log("syncComplete: " + data);
5. }
6. subscribeSyncComplete() {
7. if (kvStore != null) {
8. kvStore.on('syncComplete', this.call);
9. }
10. }
11. unsubscribeSyncComplete() {
12. if (kvStore != null) {
13. kvStore.off('syncComplete', this.call);
14. }
15. }
16. }
```

## SyncMode

PhonePC/2in1TabletTVWearable

同步模式枚举。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PULL\_ONLY | 0 | 表示只能从远端拉取数据到本端。 |
| PUSH\_ONLY | 1 | 表示只能从本端推送数据到远端。 |
| PUSH\_PULL | 2 | 表示从本端推送数据到远端，然后从远端拉取数据到本端。 |
