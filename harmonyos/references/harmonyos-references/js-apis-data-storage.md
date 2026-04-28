---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-storage
title: @ohos.data.storage (轻量级存储)
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > ArkTS API > 已停止维护的接口 > @ohos.data.storage (轻量级存储)
category: harmonyos-references
scraped_at: 2026-04-28T07:59:24+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:075334c37a597345d3b6b791529edbf9b2981afad510be8b20a99f1f00641ad4
---

轻量级存储为应用提供key-value键值型的文件数据处理能力，支持应用对数据进行轻量级存储及查询。数据存储形式为键值对，键的类型为字符串型，值的存储数据类型包括数字型、字符型、布尔型。

说明

* 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 从API version 9开始，该接口不再维护，推荐使用新接口[@ohos.data.preferences](js-apis-data-preferences.md)。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import data_storage from '@ohos.data.storage';
```

## 常量

PhonePC/2in1TabletTVWearable

**系统能力：** 以下各项对应的系统能力均为SystemCapability.DistributedDataManager.Preferences.Core

| 名称 | 类型 | 可读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| MAX\_KEY\_LENGTH | number | 是 | 否 | key的最大长度限制为80字节。 |
| MAX\_VALUE\_LENGTH | number | 是 | 否 | value的最大长度限制为16MB。 |

## data\_storage.getStorageSync

PhonePC/2in1TabletTVWearable

getStorageSync(path: string): Storage

读取指定文件，将数据加载到Storage实例，用于数据操作。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 应用程序内部数据存储路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Storage](js-apis-data-storage.md#storage) | 获取到要操作的Storage实例，用于进行数据存储操作。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let path;
4. let context = featureAbility.getContext();
5. context.getFilesDir().then((filePath) => {
6. path = filePath;
7. console.info("======================>getFilesDirPromise====================>");

9. let storage = data_storage.getStorageSync(path + '/mystore');
10. storage.putSync('startup', 'auto');
11. storage.flushSync();
12. });
```

## data\_storage.getStorage

PhonePC/2in1TabletTVWearable

getStorage(path: string, callback: AsyncCallback<Storage>): void

读取指定文件，将数据加载到Storage实例，用于数据操作，使用callback方式返回结果，此方法为异步方法。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 应用程序内部数据存储路径。 |
| callback | AsyncCallback<[Storage](js-apis-data-storage.md#storage)> | 是 | 回调函数。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let path;
4. let context = featureAbility.getContext();
5. context.getFilesDir().then((filePath) => {
6. path = filePath;
7. console.info("======================>getFilesDirPromise====================>");

9. data_storage.getStorage(path + '/mystore', function (err, storage) {
10. if (err) {
11. console.info("Failed to get the storage. path: " + path + '/mystore');
12. return;
13. }
14. storage.putSync('startup', 'auto');
15. storage.flushSync();
16. })
17. });
```

## data\_storage.getStorage

PhonePC/2in1TabletTVWearable

getStorage(path: string): Promise<Storage>

读取指定文件，将数据加载到Storage实例，用于数据操作，使用Promise方式返回结果，此方法为异步方法。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 应用程序内部数据存储路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Storage](js-apis-data-storage.md#storage)> | Promise实例，用于异步获取结果。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let path;
4. let context = featureAbility.getContext();
5. context.getFilesDir().then((filePath) => {
6. path = filePath;
7. console.info("======================>getFilesDirPromise====================>");

9. let getPromise = data_storage.getStorage(path + '/mystore');
10. getPromise.then((storage) => {
11. storage.putSync('startup', 'auto');
12. storage.flushSync();
13. }).catch((err) => {
14. console.info("Failed to get the storage. path: " + path + '/mystore');
15. })
16. });
```

## data\_storage.deleteStorageSync

PhonePC/2in1TabletTVWearable

deleteStorageSync(path: string): void

从内存中移除指定文件对应的Storage单实例，并删除指定文件及其备份文件、损坏文件。删除指定文件时，应用不允许再使用该实例进行数据操作，否则会出现数据一致性问题。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 应用程序内部数据存储路径。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let path;
4. let context = featureAbility.getContext();
5. context.getFilesDir().then((filePath) => {
6. path = filePath;
7. console.info("======================>getFilesDirPromise====================>");

9. data_storage.deleteStorageSync(path + '/mystore');
10. });
```

## data\_storage.deleteStorage

PhonePC/2in1TabletTVWearable

deleteStorage(path: string, callback: AsyncCallback<void>): void

从内存中移除指定文件对应的Storage单实例，并删除指定文件及其备份文件、损坏文件。删除指定文件时，应用不允许再使用该实例进行数据操作，否则会出现数据一致性问题，使用callback方式返回结果，此方法为异步方法。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 应用程序内部数据存储路径。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let path;
4. let context = featureAbility.getContext();
5. context.getFilesDir().then((filePath) => {
6. path = filePath;
7. console.info("======================>getFilesDirPromise====================>");

9. data_storage.deleteStorage(path + '/mystore', function (err) {
10. if (err) {
11. console.info("Failed to delete the storage with err: " + err);
12. return;
13. }
14. console.info("Succeeded in deleting the storage.");
15. })
16. });
```

## data\_storage.deleteStorage

PhonePC/2in1TabletTVWearable

deleteStorage(path: string): Promise<void>

从内存中移除指定文件对应的Storage单实例，并删除指定文件及其备份文件、损坏文件。删除指定文件时，应用不允许再使用该实例进行数据操作，否则会出现数据一致性问题，使用promise方式返回结果，此方法为异步方法。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 应用程序内部数据存储路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise实例，用于异步获取结果。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let path;
4. let context = featureAbility.getContext();
5. context.getFilesDir().then((filePath) => {
6. path = filePath;
7. console.info("======================>getFilesDirPromise====================>");

9. let promisedelSt = data_storage.deleteStorage(path + '/mystore');
10. promisedelSt.then(() => {
11. console.info("Succeeded in deleting the storage.");
12. }).catch((err) => {
13. console.info("Failed to delete the storage with err: " + err);
14. })
15. });
```

## data\_storage.removeStorageFromCacheSync

PhonePC/2in1TabletTVWearable

removeStorageFromCacheSync(path: string): void

从内存中移除指定文件对应的Storage单实例。移除Storage单实例时，应用不允许再使用该实例进行数据操作，否则会出现数据一致性问题。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 应用程序内部数据存储路径。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let path;
4. let context = featureAbility.getContext();
5. context.getFilesDir().then((filePath) => {
6. path = filePath;
7. console.info("======================>getFilesDirPromise====================>");

9. data_storage.removeStorageFromCacheSync(path + '/mystore');
10. });
```

## data\_storage.removeStorageFromCache

PhonePC/2in1TabletTVWearable

removeStorageFromCache(path: string, callback: AsyncCallback<void>): void

从内存中移除指定文件对应的Storage单实例。移除Storage单实例时，应用不允许再使用该实例进行数据操作，否则会出现数据一致性问题。使用callback方式返回结果，此方法为异步方法。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 应用程序内部数据存储路径。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let path;
4. let context = featureAbility.getContext();
5. context.getFilesDir().then((filePath) => {
6. path = filePath;
7. console.info("======================>getFilesDirPromise====================>");

9. data_storage.removeStorageFromCache(path + '/mystore', function (err) {
10. if (err) {
11. console.info("Failed to remove storage from cache with err: " + err);
12. return;
13. }
14. console.info("Succeeded in removing storage from cache.");
15. })
16. });
```

## data\_storage.removeStorageFromCache

PhonePC/2in1TabletTVWearable

removeStorageFromCache(path: string): Promise<void>

从内存中移除指定文件对应的Storage单实例。移除Storage单实例时，应用不允许再使用该实例进行数据操作，否则会出现数据一致性问题。使用Promise方式返回结果，此方法为异步方法。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 应用程序内部数据存储路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise实例，用于异步获取结果。 |

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let path;
4. let context = featureAbility.getContext();
5. context.getFilesDir().then((filePath) => {
6. path = filePath;
7. console.info("======================>getFilesDirPromise====================>");

9. let promiserevSt = data_storage.removeStorageFromCache(path + '/mystore')
10. promiserevSt.then(() => {
11. console.info("Succeeded in removing storage from cache.");
12. }).catch((err) => {
13. console.info("Failed to remove storage from cache with err: " + err);
14. })
15. });
```

## Storage

PhonePC/2in1TabletTVWearable

提供获取和修改存储数据的接口。

下列接口都需先使用[data\_storage.getStorage](js-apis-data-storage.md#data_storagegetstorage)或[data\_storage.getStorageSync](js-apis-data-storage.md#data_storagegetstoragesync)获取到Storage实例，再通过此实例调用对应接口。

### getSync

PhonePC/2in1TabletTVWearable

getSync(key: string, defValue: ValueType): ValueType

获取键对应的值，如果值为null或者非默认值类型，返回默认数据defValue。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要获取的存储key名称，不能为空。 |
| defValue | [ValueType](js-apis-data-storage.md#valuetype) | 是 | 给定key的存储不存在，则要返回的默认值。支持number、string、boolean。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ValueType | 键对应的值，如果值为null或者非默认值类型，返回默认数据。 |

**示例：**

```
1. let value = storage.getSync('startup', 'default');
2. console.info("The value of startup is " + value);
```

### get

PhonePC/2in1TabletTVWearable

get(key: string, defValue: ValueType, callback: AsyncCallback<ValueType>): void

获取键对应的值，如果值为null或者非默认值类型，返回默认数据defValue。使用callback方式返回结果，此方法为异步方法。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要获取的存储key名称，不能为空。 |
| defValue | [ValueType](js-apis-data-storage.md#valuetype) | 是 | 默认返回值。支持number、string、boolean。 |
| callback | AsyncCallback<ValueType> | 是 | 回调函数。 |

**示例：**

```
1. storage.get('startup', 'default', function(err, value) {
2. if (err) {
3. console.info("Failed to get the value of startup with err: " + err);
4. return;
5. }
6. console.info("The value of startup is " + value);
7. })
```

### get

PhonePC/2in1TabletTVWearable

get(key: string, defValue: ValueType): Promise<ValueType>

获取键对应的值，如果值为null或者非默认值类型，返回默认数据defValue。使用Promise方式返回结果，此方法为异步方法。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要获取的存储key名称，不能为空。 |
| defValue | [ValueType](js-apis-data-storage.md#valuetype) | 是 | 默认返回值。支持number、string、boolean。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<ValueType> | Promise实例，用于异步获取结果。 |

**示例：**

```
1. let promiseget = storage.get('startup', 'default');
2. promiseget.then((value) => {
3. console.info("The value of startup is " + value)
4. }).catch((err) => {
5. console.info("Failed to get the value of startup with err: " + err);
6. })
```

### putSync

PhonePC/2in1TabletTVWearable

putSync(key: string, value: ValueType): void

首先获取指定文件对应的Storage实例，然后借助Storage API将数据写入Storage实例，通过flush或者flushSync将Storage实例持久化。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要修改的存储的key，不能为空。 |
| value | [ValueType](js-apis-data-storage.md#valuetype) | 是 | 存储的新值。支持number、string、boolean。 |

**示例：**

```
1. storage.putSync('startup', 'auto');
```

### put

PhonePC/2in1TabletTVWearable

put(key: string, value: ValueType, callback: AsyncCallback<void>): void

首先获取指定文件对应的Storage实例，然后借助Storage API将数据写入Storage实例，通过flush或者flushSync将Storage实例持久化。使用callback方式返回结果，此方法为异步方法。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要修改的存储的key，不能为空。 |
| value | [ValueType](js-apis-data-storage.md#valuetype) | 是 | 存储的新值。支持number、string、boolean。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. storage.put('startup', 'auto', function (err) {
2. if (err) {
3. console.info("Failed to put the value of startup with err: " + err);
4. return;
5. }
6. console.info("Succeeded in putting the value of startup.");
7. })
```

### put

PhonePC/2in1TabletTVWearable

put(key: string, value: ValueType): Promise<void>

首先获取指定文件对应的Storage实例，然后借助Storage API将数据写入Storage实例，通过flush或者flushSync将Storage实例持久化。使用Promise方式返回结果，此方法为异步方法。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要修改的存储的key，不能为空。 |
| value | [ValueType](js-apis-data-storage.md#valuetype) | 是 | 存储的新值。支持number、string、boolean。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise实例，用于异步处理。 |

**示例：**

```
1. let promiseput = storage.put('startup', 'auto');
2. promiseput.then(() => {
3. console.info("Succeeded in putting the value of startup.");
4. }).catch((err) => {
5. console.info("Failed to put the value of startup with err: " + err);
6. })
```

### hasSync

PhonePC/2in1TabletTVWearable

hasSync(key: string): boolean

检查存储对象是否包含名为给定key的存储。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要获取的存储key名称，不能为空。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true 表示存在，false表示不存在。 |

**示例：**

```
1. let isExist = storage.hasSync('startup');
2. if (isExist) {
3. console.info("The key of startup is contained.");
4. }
```

### has

PhonePC/2in1TabletTVWearable

has(key: string, callback: AsyncCallback<boolean>): boolean

检查存储对象是否包含名为给定key的存储。使用callback方式返回结果，此方法为异步方法。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要获取的存储key名称，不能为空。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true表示存在，false表示不存在。 |

**示例：**

```
1. storage.has('startup', function (err, isExist) {
2. if (err) {
3. console.info("Failed to check the key of startup with err: " + err);
4. return;
5. }
6. if (isExist) {
7. console.info("The key of startup is contained.");
8. }
9. })
```

### has

PhonePC/2in1TabletTVWearable

has(key: string): Promise<boolean>

检查存储对象是否包含名为给定key的存储。使用Promise方式返回结果，此方法为异步方法。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要获取的存储key名称，不能为空。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise实例，用于异步处理。 |

**示例：**

```
1. let promisehas = storage.has('startup')
2. promisehas.then((isExist) => {
3. if (isExist) {
4. console.info("The key of startup is contained.");
5. }
6. }).catch((err) => {
7. console.info("Failed to check the key of startup with err: " + err);
8. })
```

### deleteSync

PhonePC/2in1TabletTVWearable

deleteSync(key: string): void

从存储对象中删除名为给定key的存储。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要获取的存储key名称。它不能为空。 |

**示例：**

```
1. storage.deleteSync('startup');
```

### delete

PhonePC/2in1TabletTVWearable

delete(key: string, callback: AsyncCallback<void>): void

从存储对象中删除名为给定key的存储。使用callback方式返回结果，此方法为异步方法。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要获取的存储key名称，不能为空。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. storage.delete('startup', function (err) {
2. if (err) {
3. console.info("Failed to delete startup key failed err: " + err);
4. return;
5. }
6. console.info("Succeeded in deleting startup key.");
7. })
```

### delete

PhonePC/2in1TabletTVWearable

delete(key: string): Promise<void>

从存储对象删除名为给定key的存储。使用Promise方式返回结果，此方法为异步方法。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要获取的存储key名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise实例，用于异步处理。 |

**示例：**

```
1. let promisedel = storage.delete('startup')
2. promisedel.then(() => {
3. console.info("Succeeded in deleting startup key.");
4. }).catch((err) => {
5. console.info("Failed to delete startup key failed err: " + err);
6. })
```

### flushSync

PhonePC/2in1TabletTVWearable

flushSync(): void

将当前storage对象中的修改保存到当前的storage，并同步存储到文件中。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**示例：**

```
1. storage.flushSync();
```

### flush

PhonePC/2in1TabletTVWearable

flush(callback: AsyncCallback<void>): void

将当前storage对象中的修改保存到当前的storage，并异步存储到文件中。使用callback方式返回结果，此方法为异步方法。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. storage.flush(function (err) {
2. if (err) {
3. console.info("Failed to flush to file with err: " + err);
4. return;
5. }
6. console.info("Succeeded in flushing to file.");
7. })
```

### flush

PhonePC/2in1TabletTVWearable

flush(): Promise<void>

将当前storage对象中的修改保存到当前的storage，并异步存储到文件中。使用Promise方式返回结果，此方法为异步方法。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise实例，用于异步处理。 |

**示例：**

```
1. let promiseflush = storage.flush();
2. promiseflush.then(() => {
3. console.info("Succeeded in flushing to file.");
4. }).catch((err) => {
5. console.info("Failed to flush to file with err: " + err);
6. })
```

### clearSync

PhonePC/2in1TabletTVWearable

clearSync(): void

清除此存储对象中的所有存储。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**示例：**

```
1. storage.clearSync();
```

### clear

PhonePC/2in1TabletTVWearable

clear(callback: AsyncCallback<void>): void

清除此存储对象中的所有存储。使用callback方式返回结果，此方法为异步方法。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```
1. storage.clear(function (err) {
2. if (err) {
3. console.info("Failed to clear the storage with err: " + err);
4. return;
5. }
6. console.info("Succeeded in clearing the storage.");
7. })
```

### clear

PhonePC/2in1TabletTVWearable

clear(): Promise<void>

清除此存储对象中的所有存储。使用Promise方式返回结果，此方法为异步方法。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise实例，用于异步处理。 |

**示例：**

```
1. let promiseclear = storage.clear();
2. promiseclear.then(() => {
3. console.info("Succeeded in clearing the storage.");
4. }).catch((err) => {
5. console.info("Failed to clear the storage with err: " + err);
6. })
```

### on('change')

PhonePC/2in1TabletTVWearable

on(type: 'change', callback: Callback<StorageObserver>): void

订阅数据变更者类需要实现StorageObserver接口，订阅的key的值发生变更后，在执行flush/flushSync方法后，callback方法会被回调。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件类型，固定值'change'，表示数据变更。 |
| callback | Callback<[StorageObserver](js-apis-data-storage.md#storageobserver)> | 是 | 回调对象实例。 |

**示例：**

```
1. let observer = function (key) {
2. console.info("The key of " + key + " changed.");
3. }
4. storage.on('change', observer);
5. storage.putSync('startup', 'auto');
6. storage.flushSync();  // observer will be called.
```

### off('change')

PhonePC/2in1TabletTVWearable

off(type: 'change', callback: Callback<StorageObserver>): void

当不再进行订阅数据变更时，使用此接口取消订阅。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件类型，固定值'change'，表示数据变更。 |
| callback | Callback<[StorageObserver](js-apis-data-storage.md#storageobserver)> | 是 | 需要取消的回调对象实例。 |

**示例：**

```
1. let observer = function (key) {
2. console.info("The key of " + key + " changed.");
3. }
4. storage.off('change', observer);
```

## StorageObserver

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 变更的数据内容。 |

## ValueType

PhonePC/2in1TabletTVWearable

type ValueType = number | string | boolean

用于表示允许的数据字段类型。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

| 类型 | 说明 |
| --- | --- |
| number | 表示值类型为数字。 |
| string | 表示值类型为字符。 |
| boolean | 表示值类型为布尔值。 |
