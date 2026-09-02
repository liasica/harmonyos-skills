---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributed-data
title: "@ohos.data.distributedData (分布式数据管理)"
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > ArkTS API > 已停止维护的接口 > @ohos.data.distributedData (分布式数据管理)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:42+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:daab10c4273434b1284561f6ec19d07694e2d5d2b62f5499074a5b1625246145
---

分布式数据管理为应用程序提供不同设备间数据库的分布式协同能力。通过调用分布式数据各个接口，应用程序可将数据保存到分布式数据库中，并可对分布式数据库中的数据进行增加、删除、修改、查询、同步等操作。

该模块提供以下分布式数据管理相关的常用功能：

* [KVManager](js-apis-distributed-data.md#kvmanager)：数据管理实例，用于获取KVStore的相关信息。
* [KvStoreResultSet8+](js-apis-distributed-data.md#kvstoreresultset8)：提供获取KVStore数据库结果集的相关方法，包括查询和移动数据读取位置等。
* [Query8+](js-apis-distributed-data.md#query8)：使用谓词表示数据库查询，提供创建Query实例、查询数据库中的数据和添加谓词的方法。
* [KVStore](js-apis-distributed-data.md#kvstore)：KVStore数据库实例，提供增加数据、删除数据和订阅数据变更、订阅数据同步完成的方法。
* [SingleKVStore](js-apis-distributed-data.md#singlekvstore)：单版本分布式数据库，继承自[KVStore](js-apis-distributed-data.md#kvstore)，不对数据所属设备进行区分，提供查询数据和同步数据的方法。
* [DeviceKVStore8+](js-apis-distributed-data.md#devicekvstore8)：设备协同数据库，继承自[KVStore](js-apis-distributed-data.md#kvstore)，以设备维度对数据进行区分，提供查询数据和同步数据的方法。

**说明** 

* 从API Version 9开始，该接口不再维护，推荐使用新接口[@ohos.data.distributedKVStore (分布式键值数据库)](js-apis-distributedkvstore.md)。
* 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块中所有需要获取deviceId的接口，都仅系统应用可用。

## 导入模块

```js
import distributedData from '@ohos.data.distributedData';
```

## distributedData.createKVManager

createKVManager(config: KVManagerConfig, callback: AsyncCallback<KVManager>): void

创建一个KVManager对象实例，用于管理数据库对象，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [KVManagerConfig](js-apis-distributed-data.md#kvmanagerconfig) | 是 | 提供KVManager实例的配置信息，包括调用方的Bundle名称和用户信息。 |
| callback | AsyncCallback<[KVManager](js-apis-distributed-data.md#kvmanager)> | 是 | 回调函数。返回创建的KVManager对象实例。 |

**示例：**

```js
let kvManager;
try {
    const kvManagerConfig = {
        bundleName : 'com.example.datamanagertest',
        userInfo : {
            userId : '0',
            userType : distributedData.UserType.SAME_USER_ID
        }
    }
    distributedData.createKVManager(kvManagerConfig, function (err, manager) {
        if (err) {
            console.error("Failed to create KVManager: "  + JSON.stringify(err));
            return;
        }
        console.info("Succeeded in creating KVManager");
        kvManager = manager;
    });
} catch (e) {
    console.error("An unexpected error occurred. Error:" + e);
}
```

## distributedData.createKVManager

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

```js
try {
  const kvManagerConfig = {
    bundleName: 'com.example.datamanagertest',
    userInfo: {
      userId: '0',
      userType: distributedData.UserType.SAME_USER_ID
    }
  }
  distributedData.createKVManager(kvManagerConfig).then((manager) => {
    console.info("Succeeded in creating KVManager");
    kvManager = manager;
  }).catch((err) => {
    console.error("Failed to create KVManager: " + JSON.stringify(err));
  });
} catch (e) {
  console.error("An unexpected error occurred. Error:" + e);
}
```

## KVManagerConfig

提供KVManager实例的配置信息，包括调用方的Bundle名称和用户信息。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userInfo | [UserInfo](js-apis-distributed-data.md#userinfo) | 是 | 调用方的用户信息。 |
| bundleName | string | 是 | 调用方的Bundle名称。 |

## UserInfo

用户信息。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userId | string | 否 | 指示要设置的用户ID，默认为'0'。 |
| userType | [UserType](js-apis-distributed-data.md#usertype) | 否 | 指示要设置的用户类型，默认为0。 |

## UserType

用户类型枚举。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SAME\_USER\_ID | 0 | 使用同一账号登录不同设备的用户。 |

## KVManager

数据管理实例，用于获取KVStore的相关信息。在调用KVManager的方法前，需要先通过[createKVManager](js-apis-distributed-data.md#distributeddatacreatekvmanager)构建一个KVManager实例。

### getKVStore

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

```js
let kvStore;
let kvManager;
try {
    const options = {
        createIfMissing : true,
        encrypt : false,
        backup : false,
        autoSync : true,
        kvStoreType : distributedData.KVStoreType.SINGLE_VERSION,
        securityLevel : distributedData.SecurityLevel.S3,
    };
    kvManager.getKVStore('storeId', options, function (err, store) {
        if (err) {
            console.error("getKVStore err: "  + JSON.stringify(err));
            return;
        }
        console.info("getKVStore success");
        kvStore = store;
    });
} catch (e) {
    console.error("An unexpected error occurred. Error:" + e);
}
```

### getKVStore

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

```js
let kvStore;
let kvManager;
try {
    const options = {
        createIfMissing : true,
        encrypt : false,
        backup : false,
        autoSync : true,
        kvStoreType : distributedData.KVStoreType.SINGLE_VERSION,
        securityLevel : distributedData.SecurityLevel.S3,
    };
    kvManager.getKVStore('storeId', options).then((store) => {
        console.info("getKVStore success");
        kvStore = store;
    }).catch((err) => {
        console.error("getKVStore err: "  + JSON.stringify(err));
    });
} catch (e) {
    console.error("An unexpected error occurred. Error:" + e);
}
```

### closeKVStore8+

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

```js
let kvStore;
let kvManager;
const options = {
    createIfMissing: true,
    encrypt: false,
    backup: false,
    autoSync: false,
    kvStoreType: distributedData.KVStoreType.SINGLE_VERSION,
    schema: undefined,
    securityLevel: distributedData.SecurityLevel.S3,
}
try {
    kvManager.getKVStore('storeId', options, async function (err, store) {
        console.info('getKVStore success');
        kvStore = store;
        kvManager.closeKVStore('appId', 'storeId', kvStore, function (err, data) {
            console.info('closeKVStore success');
        });
    });
} catch (e) {
    console.error('closeKVStore e ' + e);
}
```

### closeKVStore8+

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

```js
let kvManager;
let kvStore;
const options = {
    createIfMissing: true,
    encrypt: false,
    backup: false,
    autoSync: false,
    kvStoreType: distributedData.KVStoreType.SINGLE_VERSION,
    schema: undefined,
    securityLevel: distributedData.SecurityLevel.S3,
}
try {
    kvManager.getKVStore('storeId', options).then(async (store) => {
        console.info('getKVStore success');
        kvStore = store;
        kvManager.closeKVStore('appId', 'storeId', kvStore).then(() => {
            console.info('closeKVStore success');
        }).catch((err) => {
            console.error('closeKVStore err ' + JSON.stringify(err));
        });
    }).catch((err) => {
        console.error('CloseKVStore getKVStore err ' + JSON.stringify(err));
    });
} catch (e) {
    console.error('closeKVStore e ' + e);
}
```

### deleteKVStore8+

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

```js
let kvManager;
let kvStore;
const options = {
    createIfMissing : true,
    encrypt : false,
    backup : false,
    autoSync : true,
    kvStoreType : distributedData.KVStoreType.SINGLE_VERSION,
    schema : undefined,
    securityLevel : distributedData.SecurityLevel.S3,
}
try {
    kvManager.getKVStore('store', options, async function (err, store) {
        console.info('getKVStore success');
        kvStore = store;
        kvManager.deleteKVStore('appId', 'storeId', function (err, data) {
            console.info('deleteKVStore success');
        });
    });
} catch (e) {
    console.error('DeleteKVStore e ' + e);
}
```

### deleteKVStore8+

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

```js
let kvManager;
let kvStore;
const options = {
    createIfMissing : true,
    encrypt : false,
    backup : false,
    autoSync : true,
    kvStoreType : distributedData.KVStoreType.SINGLE_VERSION,
    schema : undefined,
    securityLevel : distributedData.SecurityLevel.S3,
}
try {
    kvManager.getKVStore('storeId', options).then(async (store) => {
        console.info('getKVStore success');
        kvStore = store;
        kvManager.deleteKVStore('appId', 'storeId').then(() => {
            console.info('deleteKVStore success');
        }).catch((err) => {
            console.error('deleteKVStore err ' + JSON.stringify(err));
        });
    }).catch((err) => {
        console.error('getKVStore err ' + JSON.stringify(err));
    });
} catch (e) {
    console.error('deleteKVStore e ' + e);
}
```

### getAllKVStoreId8+

getAllKVStoreId(appId: string, callback: AsyncCallback<string[]>): void

获取所有通过[getKVStore](js-apis-distributed-data.md#getkvstore)方法创建的且没有调用[deleteKVStore](js-apis-distributed-data.md#deletekvstore8)方法删除的KVStore数据库的storeId，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appId | string | 是 | 所调用数据库方的包名。 |
| callback | AsyncCallback<string[]> | 是 | 回调函数。返回所有创建的KvStore数据库的storeId。 |

**示例：**

```js
let kvManager;
try {
    kvManager.getAllKVStoreId('appId', function (err, data) {
        console.info('GetAllKVStoreId success');
        console.info('GetAllKVStoreId size = ' + data.length);
    });
} catch (e) {
    console.error('GetAllKVStoreId e ' + e);
}
```

### getAllKVStoreId8+

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

```js
let kvManager;
try {
    console.info('GetAllKVStoreId');
    kvManager.getAllKVStoreId('appId').then((data) => {
        console.info('getAllKVStoreId success');
        console.info('size = ' + data.length);
    }).catch((err) => {
        console.error('getAllKVStoreId err ' + JSON.stringify(err));
    });
} catch(e) {
    console.error('getAllKVStoreId e ' + e);
}
```

### on('distributedDataServiceDie')8+

on(event: 'distributedDataServiceDie', deathCallback: Callback<void>): void

订阅服务状态变更通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 订阅的事件名，固定为'distributedDataServiceDie'，即服务状态变更事件。 |
| deathCallback | Callback<void> | 是 | 回调函数。 |

**示例：**

```js
let kvManager;
try {
    console.info('KVManagerOn');
    const deathCallback = function () {
        console.info('death callback call');
    }
    kvManager.on('distributedDataServiceDie', deathCallback);
} catch (e) {
    console.error("An unexpected error occurred. Error:" + e);
}
```

### off('distributedDataServiceDie')8+

off(event: 'distributedDataServiceDie', deathCallback?: Callback<void>): void

取消订阅服务状态变更通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取消订阅的事件名，固定为'distributedDataServiceDie'，即服务状态变更事件。 |
| deathCallback | Callback<void> | 否 | 取消订阅的函数。如不设置callback，则取消所有已订阅的函数。 |

**示例：**

```js
let kvManager;
try {
    console.info('KVManagerOff');
    const deathCallback = function () {
        console.info('death callback call');
    }
    kvManager.off('distributedDataServiceDie', deathCallback);
} catch (e) {
    console.error("An unexpected error occurred. Error:" + e);
}
```

## Options

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

KVStore数据库类型枚举。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEVICE\_COLLABORATION | 0 | 表示多设备协同数据库。  **数据库特点：** 数据以设备的维度管理，不存在冲突；支持按照设备的维度查询数据。  **系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore |
| SINGLE\_VERSION | 1 | 表示单版本数据库。  **数据库特点：** 数据不分设备，设备之间修改相同的key会覆盖。  **系统能力：** SystemCapability.DistributedDataManager.KVStore.Core |
| MULTI\_VERSION | 2 | 表示多版本数据库。当前暂不支持使用此接口。  **系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore |

## SecurityLevel

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

表示数据库模式，可以在创建或打开数据库时创建Schema对象并将它们放入[Options](js-apis-distributed-data.md#options)中。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

| 名称 | 类型 | 可读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| root8+ | [FieldNode](js-apis-distributed-data.md#fieldnode8) | 是 | 是 | 表示json根对象。 |
| indexes8+ | Array<string> | 是 | 是 | 表示json类型的字符串数组。 |
| mode8+ | number | 是 | 是 | 表示Schema的模式。 |
| skip8+ | number | 是 | 是 | Schema的跳跃大小。 |

### constructor8+

constructor()

用于创建Schema实例的构造函数。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

## FieldNode8+

表示 Schema 实例的节点，提供定义存储在数据库中的值的方法。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

| 名称 | 类型 | 可读 | 可写 | 说明 |
| --- | --- | --- | --- | --- |
| nullable8+ | boolean | 是 | 是 | 表示数据库字段是否可以为空。 |
| default8+ | string | 是 | 是 | 表示FieldNode的默认值。 |
| type8+ | number | 是 | 是 | 表示指定节点对应数据类型的值。 |

### constructor8+

constructor(name: string)

用于创建带有string字段FieldNode实例的构造函数。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | FieldNode的值。 |

### appendChild8+

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

```js
import ddm from '@ohos.data.distributedData';
try {
    let node = new ddm.FieldNode("root");
    let child1 = new ddm.FieldNode("child1");
    let child2 = new ddm.FieldNode("child2");
    let child3 = new ddm.FieldNode("child3");
    node.appendChild(child1);
    node.appendChild(child2);
    node.appendChild(child3);
    console.info("appendNode " + JSON.stringify(node));
    child1 = null;
    child2 = null;
    child3 = null;
    node = null;
} catch (e) {
    console.error("AppendChild " + e);
}
```

## KvStoreResultSet8+

提供获取KVStore数据库结果集的相关方法，包括查询和移动数据读取位置等。

在调用KvStoreResultSet的方法前，需要先通过[getKVStore](js-apis-distributed-data.md#getkvstore)构建一个KVStore实例。

### getCount8+

getCount(): number

获取结果集中的总行数。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回数据的总行数。 |

**示例：**

```js
let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('batch_test_string_key').then((result) => {
        console.info('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.error('getResultSet failed: ' + err);
    });
    const count = resultSet.getCount();
    console.info("getCount succeed:" + count);
} catch (e) {
    console.error("getCount failed: " + e);
}
```

### getPosition8+

getPosition(): number

获取结果集中当前的读取位置。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回当前读取位置。 |

**示例：**

```js
let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('batch_test_string_key').then((result) => {
        console.info('getResultSet succeeded.');
        resultSet = result;
    }).catch((err) => {
        console.error('getResultSet failed: ' + err);
    });
    const position = resultSet.getPosition();
    console.info("getPosition succeed:" + position);
} catch (e) {
    console.error("getPosition failed: " + e);
}
```

### moveToFirst8+

moveToFirst(): boolean

将读取位置移动到第一行。如果结果集为空，则返回false。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示操作成功；返回false则表示操作失败。 |

**示例：**

```js
let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('batch_test_string_key').then((result) => {
        console.info('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.error('getResultSet failed: ' + err);
    });
    const moved1 = resultSet.moveToFirst();
    console.info("moveToFirst succeed: " + moved1);
} catch (e) {
    console.error("moveToFirst failed " + e);
}
```

### moveToLast8+

moveToLast(): boolean

将读取位置移动到最后一行。如果结果集为空，则返回false。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示操作成功；返回false则表示操作失败。 |

**示例：**

```js
let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('batch_test_string_key').then((result) => {
        console.info('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.error('getResultSet failed: ' + err);
    });
    const moved2 = resultSet.moveToLast();
    console.info("moveToLast succeed:" + moved2);
} catch (e) {
    console.error("moveToLast failed: " + e);
}
```

### moveToNext8+

moveToNext(): boolean

将读取位置移动到下一行。如果结果集为空，则返回false。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示操作成功；返回false则表示操作失败。 |

**示例：**

```js
let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('batch_test_string_key').then((result) => {
        console.info('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.error('getResultSet failed: ' + err);
    });
    const moved3 = resultSet.moveToNext();
    console.info("moveToNext succeed: " + moved3);
} catch (e) {
    console.error("moveToNext failed: " + e);
}
```

### moveToPrevious8+

moveToPrevious(): boolean

将读取位置移动到上一行。如果结果集为空，则返回false。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示操作成功；返回false则表示操作失败。 |

**示例：**

```js
let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('batch_test_string_key').then((result) => {
        console.info('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.error('getResultSet failed: ' + err);
    });
    const moved4 = resultSet.moveToPrevious();
    console.info("moveToPrevious succeed:" + moved4);
} catch (e) {
    console.error("moveToPrevious failed: " + e);
}
```

### move8+

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

```js
let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('batch_test_string_key').then((result) => {
        console.info('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.error('getResultSet failed: ' + err);
    });
    const moved5 = resultSet.move(1);
    console.info("move succeed:" + moved5);
} catch (e) {
    console.error("move failed: " + e);
}
```

### moveToPosition8+

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

```js
let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('batch_test_string_key').then((result) => {
        console.info('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.error('getResultSet failed: ' + err);
    });
    const moved6 = resultSet.moveToPosition(1);
    console.info("moveToPosition succeed: " + moved6);
} catch (e) {
    console.error("moveToPosition failed: " + e);
}
```

### isFirst8+

isFirst(): boolean

检查读取位置是否为第一行。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示读取位置为第一行；返回false表示读取位置不是第一行。 |

**示例：**

```js
let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('batch_test_string_key').then((result) => {
        console.info('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.error('getResultSet failed: ' + err);
    });
    const isfirst = resultSet.isFirst();
    console.info("Check isFirst succeed:" + isfirst);
} catch (e) {
    console.error("Check isFirst failed: " + e);
}
```

### isLast8+

isLast(): boolean

检查读取位置是否为最后一行。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示读取位置为最后一行；返回false表示读取位置不是最后一行。 |

**示例：**

```js
let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('batch_test_string_key').then((result) => {
        console.info('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.error('getResultSet failed: ' + err);
    });
    const islast = resultSet.isLast();
    console.info("Check isLast succeed: " + islast);
} catch (e) {
    console.error("Check isLast failed: " + e);
}
```

### isBeforeFirst8+

isBeforeFirst(): boolean

检查读取位置是否在第一行之前。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示读取位置在第一行之前；返回false表示读取位置不在第一行之前。 |

**示例：**

```js
let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('batch_test_string_key').then((result) => {
        console.info('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.error('getResultSet failed: ' + err);
    });
    const isbeforefirst = resultSet.isBeforeFirst();
    console.info("Check isBeforeFirst succeed: " + isbeforefirst);
} catch (e) {
    console.error("Check isBeforeFirst failed: " + e);
}
```

### isAfterLast8+

isAfterLast(): boolean

检查读取位置是否在最后一行之后。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示读取位置在最后一行之后；返回false表示读取位置不在最后一行之后。 |

**示例：**

```js
let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('batch_test_string_key').then((result) => {
        console.info('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.error('getResultSet failed: ' + err);
    });
    const isafterlast = resultSet.isAfterLast();
    console.info("Check isAfterLast succeed:" + isafterlast);
} catch (e) {
    console.error("Check isAfterLast failed: " + e);
}
```

### getEntry8+

getEntry(): Entry

从当前位置获取对应的键值对。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Entry](js-apis-distributed-data.md#entry) | 返回键值对。 |

**示例：**

```js
let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('batch_test_string_key').then((result) => {
        console.info('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.error('getResultSet failed: ' + err);
    });
    const entry  = resultSet.getEntry();
    console.info("getEntry succeed:" + JSON.stringify(entry));
} catch (e) {
    console.error("getEntry failed: " + e);
}
```

## Query8+

使用谓词表示数据库查询，提供创建Query实例、查询数据库中的数据和添加谓词的方法。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

### constructor8+

constructor()

用于创建Query实例的构造函数。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

### reset8+

reset(): Query

重置Query对象。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributed-data.md#query8) | 返回重置的Query对象。 |

**示例：**

```js
try {
    let query = new distributedData.Query();
    query.equalTo("key", "value");
    console.info("query is " + query.getSqlLike());
    query.reset();
    console.info("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.error("simply calls should be ok :" + e);
}
```

### equalTo8+

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

```js
try {
    let query = new distributedData.Query();
    query.equalTo("field", "value");
    console.info("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.error("duplicated calls should be ok :" + e);
}
```

### notEqualTo8+

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

```js
try {
    let query = new distributedData.Query();
    query.notEqualTo("field", "value");
    console.info("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.error("duplicated calls should be ok :" + e);
}
```

### greaterThan8+

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

```js
try {
    let query = new distributedData.Query();
    query.greaterThan("field", "value");
    console.info("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.error("duplicated calls should be ok :" + e);
}
```

### lessThan8+

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

```js
try {
    let query = new distributedData.Query();
    query.lessThan("field", "value");
    console.info("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.error("duplicated calls should be ok :" + e);
}
```

### greaterThanOrEqualTo8+

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

```js
try {
    let query = new distributedData.Query();
    query.greaterThanOrEqualTo("field", "value");
    console.info("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.error("duplicated calls should be ok :" + e);
}
```

### lessThanOrEqualTo8+

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

```js
try {
    let query = new distributedData.Query();
    query.lessThanOrEqualTo("field", "value");
    console.info("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.error("duplicated calls should be ok :" + e);
}
```

### isNull8+

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

```js
try {
    let query = new distributedData.Query();
    query.isNull("field");
    console.info("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.error("duplicated calls should be ok :" + e);
}
```

### inNumber8+

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

```js
try {
    let query = new distributedData.Query();
    query.inNumber("field", [0, 1]);
    console.info("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.error("duplicated calls should be ok :" + e);
}
```

### inString8+

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

```js
try {
    let query = new distributedData.Query();
    query.inString("field", ['test1', 'test2']);
    console.info("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.error("duplicated calls should be ok :" + e);
}
```

### notInNumber8+

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

```js
try {
    let query = new distributedData.Query();
    query.notInNumber("field", [0, 1]);
    console.info("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.error("duplicated calls should be ok :" + e);
}
```

### notInString8+

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

```js
try {
    let query = new distributedData.Query();
    query.notInString("field", ['test1', 'test2']);
    console.info("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.error("duplicated calls should be ok :" + e);
}
```

### like8+

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

```js
try {
    let query = new distributedData.Query();
    query.like("field", "value");
    console.info("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.error("duplicated calls should be ok :" + e);
}
```

### unlike8+

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

```js
try {
    let query = new distributedData.Query();
    query.unlike("field", "value");
    console.info("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.error("duplicated calls should be ok :" + e);
}
```

### and8+

and(): Query

构造一个带有与条件的查询对象。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributed-data.md#query8) | 返回查询对象。 |

**示例：**

```js
try {
    let query = new distributedData.Query();
    query.notEqualTo("field", "value1");
    query.and();
    query.notEqualTo("field", "value2");
    console.info("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.error("duplicated calls should be ok :" + e);
}
```

### or8+

or(): Query

构造一个带有或条件的Query对象。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributed-data.md#query8) | 返回查询对象。 |

**示例：**

```js
try {
    let query = new distributedData.Query();
    query.notEqualTo("field", "value1");
    query.or();
    query.notEqualTo("field", "value2");
    console.info("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.error("duplicated calls should be ok :" + e);
}
```

### orderByAsc8+

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

```js
try {
    let query = new distributedData.Query();
    query.notEqualTo("field", "value");
    query.orderByAsc("field");
    console.info("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.error("duplicated calls should be ok :" + e);
}
```

### orderByDesc8+

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

```js
try {
    let query = new distributedData.Query();
    query.notEqualTo("field", "value");
    query.orderByDesc("field");
    console.info("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.error("duplicated calls should be ok :" + e);
}
```

### limit8+

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

```js
let total = 10;
let offset = 1;
try {
    let query = new distributedData.Query();
    query.notEqualTo("field", "value");
    query.limit(total, offset);
    console.info("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.error("duplicated calls should be ok :" + e);
}
```

### isNotNull8+

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

```js
try {
    let query = new distributedData.Query();
    query.isNotNull("field");
    console.info("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.error("duplicated calls should be ok :" + e);
}
```

### beginGroup8+

beginGroup(): Query

创建一个带有左括号的查询条件组。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributed-data.md#query8) | 返回Query对象。 |

**示例：**

```js
try {
    let query = new distributedData.Query();
    query.beginGroup();
    query.isNotNull("field");
    query.endGroup();
    console.info("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.error("duplicated calls should be ok :" + e);
}
```

### endGroup8+

endGroup(): Query

创建一个带有右括号的查询条件组。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributed-data.md#query8) | 返回Query对象。 |

**示例：**

```js
try {
    let query = new distributedData.Query();
    query.beginGroup();
    query.isNotNull("field");
    query.endGroup();
    console.info("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.error("duplicated calls should be ok :" + e);
}
```

### prefixKey8+

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

```js
try {
    let query = new distributedData.Query();
    query.prefixKey("$.name");
    query.prefixKey("0");
    console.info("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.error("duplicated calls should be ok :" + e);
}
```

### setSuggestIndex8+

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

```js
try {
    let query = new distributedData.Query();
    query.setSuggestIndex("$.name");
    query.setSuggestIndex("0");
    console.info("query is " + query.getSqlLike());
    query = null;
} catch (e) {
   console.error("duplicated calls should be ok :" + e);
}
```

### deviceId8+

deviceId(deviceId:string):Query

添加设备ID作为key的前缀。

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

```js
try {
    let query = new distributedData.Query();
    query.deviceId("deviceId");
    console.info("query is " + query.getSqlLike());
} catch (e) {
    console.error("should be ok on Method Chaining : " + e);
}
```

### getSqlLike8+

getSqlLike():string

获取Query对象的查询语句。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回一个字段列中包含对应子串的结果。 |

**示例：**

```js
try {
    let query = new distributedData.Query();
    let sql1 = query.getSqlLike();
    console.info("GetSqlLike sql=" + sql1);
} catch (e) {
    console.error("duplicated calls should be ok : " + e);
}
```

## KVStore

KVStore数据库实例，提供增加数据、删除数据和订阅数据变更、订阅数据同步完成的方法。

在调用KVStore的方法前，需要先通过[getKVStore](js-apis-distributed-data.md#getkvstore)构建一个KVStore实例。

### put

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

```js
let kvStore;
const KEY_TEST_STRING_ELEMENT = 'key_test_string';
const VALUE_TEST_STRING_ELEMENT = 'value-test-string';
try {
    kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT, function (err,data) {
        if (err != undefined) {
            console.error("put err: " + JSON.stringify(err));
            return;
        }
        console.info("put success");
    });
}catch (e) {
    console.error("An unexpected error occurred. Error:" + e);
}
```

### put

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

```js
let kvStore;
const KEY_TEST_STRING_ELEMENT = 'key_test_string';
const VALUE_TEST_STRING_ELEMENT = 'value-test-string';
try {
    kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT).then((data) => {
        console.info("put success: " + JSON.stringify(data));
    }).catch((err) => {
        console.error("put err: " + JSON.stringify(err));
    });
}catch (e) {
    console.error("An unexpected error occurred. Error:" + e);
}
```

### delete

delete(key: string, callback: AsyncCallback<void>): void

从数据库中删除指定键值的数据，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要删除数据的key，不能为空且长度不大于[MAX\_KEY\_LENGTH](js-apis-distributed-data.md#constants)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```js
let kvStore;
const KEY_TEST_STRING_ELEMENT = 'key_test_string';
const VALUE_TEST_STRING_ELEMENT = 'value-test-string';
try {
    kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT, function (err,data) {
        if (err != undefined) {
            console.error("put err: " + JSON.stringify(err));
            return;
        }
        console.info("put success");
        kvStore.delete(KEY_TEST_STRING_ELEMENT, function (err,data) {
            if (err != undefined) {
                console.error("delete err: " + JSON.stringify(err));
                return;
            }
            console.info("delete success");
        });
    });
}catch (e) {
    console.error("An unexpected error occurred. Error:" + e);
}
```

### delete

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

```js
let kvStore;
const KEY_TEST_STRING_ELEMENT = 'key_test_string';
const VALUE_TEST_STRING_ELEMENT = 'value-test-string';
try {
    kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT).then((data) => {
        console.info("put success: " + JSON.stringify(data));
        kvStore.delete(KEY_TEST_STRING_ELEMENT).then((data) => {
            console.info("delete success");
        }).catch((err) => {
            console.error("delete err: " + JSON.stringify(err));
        });
    }).catch((err) => {
        console.error("put err: " + JSON.stringify(err));
    });
}catch (e) {
    console.error("An unexpected error occurred. Error:" + e);
}
```

### on('dataChange')

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

```js
let kvStore;
kvStore.on('dataChange', distributedData.SubscribeType.SUBSCRIBE_TYPE_LOCAL, function (data) {
    console.info("dataChange callback call data: " + JSON.stringify(data));
});
```

### on('syncComplete')

on(event: 'syncComplete', syncCallback: Callback<Array<[string, number]>>): void

订阅同步完成事件回调通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 订阅的事件名，固定为'syncComplete'，表示同步完成事件。 |
| syncCallback | Callback<Array<[string, number]>> | 是 | 回调函数。用于向调用方发送同步结果的回调。 |

**示例：**

```js
let kvStore;
kvStore.on('syncComplete', function (data) {
    console.info("callback call data: " + data);
});
```

### off('dataChange')8+

off(event:'dataChange', listener?: Callback<ChangeNotification>): void

取消订阅数据变更通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取消订阅的事件名，固定为'dataChange'，表示数据变更事件。 |
| listener | Callback<[ChangeNotification](js-apis-distributed-data.md#changenotification)> | 否 | 取消订阅的函数。如不设置callback，则取消所有订阅的函数。 |

**示例：**

```js
let kvStore;
class KvstoreModel {
    call(data) {
        console.info("dataChange: " + data);
    }
    subscribeDataChange() {
        if (kvStore != null) {
            kvStore.on('dataChange', distributedData.SubscribeType.SUBSCRIBE_TYPE_REMOTE, this.call);
        }
    }
    unsubscribeDataChange() {
        if (kvStore != null) {
            kvStore.off('dataChange', this.call);
        }
    }
}
```

### off('syncComplete')8+

off(event: 'syncComplete', syncCallback?: Callback<Array<[string, number]>>): void

取消订阅同步完成事件回调通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取消订阅的事件名，固定为'syncComplete'，表示同步完成事件。 |
| syncCallback | Callback<Array<[string, number]>> | 否 | 取消订阅的函数。如不设置callback，则取消所有订阅的函数。 |

**示例：**

```js
let kvStore;
class KvstoreModel {
    call(data) {
        console.info("syncComplete: " + data);
    }
    subscribeSyncComplete() {
        if (kvStore != null) {
            kvStore.on('syncComplete', this.call);
        }
    }
    unsubscribeSyncComplete() {
        if (kvStore != null) {
            kvStore.off('syncComplete', this.call);
        }
    }
}
```

### putBatch8+

putBatch(entries: Entry[], callback: AsyncCallback<void>): void

批量插入键值对到KVStore数据库中，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| entries | [Entry](js-apis-distributed-data.md#entry)[] | 是 | 表示要批量插入的键值对。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```js
let kvStore;
try {
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
    }
    console.info('entries: ' + JSON.stringify(entries));
    kvStore.putBatch(entries, async function (err,data) {
        console.info('putBatch success');
        kvStore.getEntries('batch_test_string_key', function (err,entries) {
            console.info('getEntries success');
            console.info('entries.length: ' + entries.length);
            console.info('entries[0]: ' + JSON.stringify(entries[0]));
        });
    });
}catch(e) {
    console.error('PutBatch e ' + JSON.stringify(e));
}
```

### putBatch8+

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

```js
let kvStore;
try {
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
    }
    console.info('entries: ' + JSON.stringify(entries));
    kvStore.putBatch(entries).then(async (err) => {
        console.info('putBatch success');
        kvStore.getEntries('batch_test_string_key').then((entries) => {
            console.info('getEntries success');
            console.info('PutBatch ' + JSON.stringify(entries));
        }).catch((err) => {
            console.error('getEntries fail ' + JSON.stringify(err));
        });
    }).catch((err) => {
        console.error('putBatch fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.error('PutBatch e ' + JSON.stringify(e));
}
```

### deleteBatch8+

deleteBatch(keys: string[], callback: AsyncCallback<void>): void

批量删除KVStore数据库中的键值对，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keys | string[] | 是 | 表示要批量删除的键值对。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```js
let kvStore;
try {
    let entries = [];
    let keys = [];
    for (var i = 0; i < 5; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
        keys.push(key + i);
    }
    console.info('entries: ' + JSON.stringify(entries));
    kvStore.putBatch(entries, async function (err,data) {
        console.info('putBatch success');
        kvStore.deleteBatch(keys, async function (err,data) {
            console.info('deleteBatch success');
        });
    });
}catch(e) {
    console.error('DeleteBatch e ' + e);
}
```

### deleteBatch8+

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

```js
let kvStore;
try {
    let entries = [];
    let keys = [];
    for (var i = 0; i < 5; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
        keys.push(key + i);
    }
    console.info('entries: ' + JSON.stringify(entries));
    kvStore.putBatch(entries).then(async (err) => {
        console.info('putBatch success');
        kvStore.deleteBatch(keys).then((err) => {
            console.info('deleteBatch success');
        }).catch((err) => {
            console.error('deleteBatch fail ' + JSON.stringify(err));
        });
    }).catch((err) => {
        console.error('putBatch fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.error('DeleteBatch e ' + e);
}
```

### startTransaction8+

startTransaction(callback: AsyncCallback<void>): void

启动KVStore数据库中的事务，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```js
let kvStore;
function putBatchString(len, prefix) {
    let entries = [];
    for (var i = 0; i < len; i++) {
        var entry = {
            key : prefix + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
    }
    return entries;
}
try {
    var count = 0;
    kvStore.on('dataChange', 0, function (data) {
        console.info('startTransaction 0' + data)
        count++;
    });
    kvStore.startTransaction(async function (err,data) {
        console.info('startTransaction success');
        let entries = putBatchString(10, 'batch_test_string_key');
        console.info('entries: ' + JSON.stringify(entries));
        kvStore.putBatch(entries, async function (err,data) {
            console.info('putBatch success');
        });
    });
}catch(e) {
    console.error('startTransaction e ' + e);
}
```

### startTransaction8+

startTransaction(): Promise<void>

启动KVStore数据库中的事务，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```js
let kvStore;
try {
    var count = 0;
    kvStore.on('dataChange', distributedData.SubscribeType.SUBSCRIBE_TYPE_ALL, function (data) {
        console.info('startTransaction ' + JSON.stringify(data));
        count++;
    });
    kvStore.startTransaction().then(async (err) => {
        console.info('startTransaction success');
    }).catch((err) => {
        console.error('startTransaction fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.error('startTransaction e ' + e);
}
```

### commit8+

commit(callback: AsyncCallback<void>): void

提交KVStore数据库中的事务，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```js
let kvStore;
try {
    kvStore.commit(function (err,data) {
        if (err == undefined) {
            console.info('commit success');
        } else {
            console.error('commit fail');
        }
    });
}catch(e) {
    console.error('Commit e ' + e);
}
```

### commit8+

commit(): Promise<void>

提交KVStore数据库中的事务，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```js
let kvStore;
try {
    kvStore.commit().then(async (err) => {
        console.info('commit success');
    }).catch((err) => {
        console.error('commit fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.error('Commit e ' + e);
}
```

### rollback8+

rollback(callback: AsyncCallback<void>): void

在KVStore数据库中回滚事务，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```js
let kvStore;
try {
    kvStore.rollback(function (err,data) {
        if (err == undefined) {
            console.info('commit success');
        } else {
            console.error('commit fail');
        }
    });
}catch(e) {
    console.error('Rollback e ' + e);
}
```

### rollback8+

rollback(): Promise<void>

在KVStore数据库中回滚事务，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```js
let kvStore;
try {
    kvStore.rollback().then(async (err) => {
        console.info('rollback success');
    }).catch((err) => {
        console.error('rollback fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.error('Rollback e ' + e);
}
```

### enableSync8+

enableSync(enabled: boolean, callback: AsyncCallback<void>): void

设定是否开启同步，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 设定是否开启同步，true表示开启同步，false表示不启用同步。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```js
let kvStore;
try {
    kvStore.enableSync(true, function (err,data) {
        if (err == undefined) {
            console.info('enableSync success');
        } else {
            console.error('enableSync fail');
        }
    });
}catch(e) {
    console.error('EnableSync e ' + e);
}
```

### enableSync8+

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

```js
let kvStore;
try {
    kvStore.enableSync(true).then((err) => {
        console.info('enableSync success');
    }).catch((err) => {
        console.error('enableSync fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.error('EnableSync e ' + e);
}
```

### setSyncRange8+

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

```js
let kvStore;
try {
    const localLabels = ['A', 'B'];
    const remoteSupportLabels = ['C', 'D'];
    kvStore.setSyncRange(localLabels, remoteSupportLabels, function (err,data) {
        console.info('SetSyncRange put success');
    });
}catch(e) {
    console.error('SetSyncRange e ' + e);
}
```

### setSyncRange8+

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

```js
let kvStore;
try {
    const localLabels = ['A', 'B'];
    const remoteSupportLabels = ['C', 'D'];
    kvStore.setSyncRange(localLabels, remoteSupportLabels).then((err) => {
        console.info('setSyncRange success');
    }).catch((err) => {
        console.error('delete fail ' + err);
    });
}catch(e) {
    console.error('SetSyncRange e ' + e);
}
```

## SubscribeType

订阅类型枚举。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUBSCRIBE\_TYPE\_LOCAL | 0 | 表示订阅本地数据变更。 |
| SUBSCRIBE\_TYPE\_REMOTE | 1 | 表示订阅远端数据变更。 |
| SUBSCRIBE\_TYPE\_ALL | 2 | 表示订阅远端和本地数据变更。 |

## ChangeNotification

数据变更时通知的对象，包括数据插入的数据、更新的数据、删除的数据和设备ID。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| insertEntries | [Entry](js-apis-distributed-data.md#entry)[] | 是 | 数据添加记录。 |
| updateEntries | [Entry](js-apis-distributed-data.md#entry)[] | 是 | 数据更新记录。 |
| deleteEntries | [Entry](js-apis-distributed-data.md#entry)[] | 是 | 数据删除记录。 |
| deviceId | string | 是 | 设备ID，此处为设备UUID。 |

## Entry

存储在数据库中的键值对。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 键值。 |
| value | [Value](js-apis-distributed-data.md#value) | 是 | 值对象。 |

## Value

存储在数据库中的值对象。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [ValueType](js-apis-distributed-data.md#value) | 是 | 值类型。 |
| value | Uint8Array | string | number | boolean | 是 | 值。 |

## ValueType

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

单版本数据库，继承自[KVStore](js-apis-distributed-data.md#kvstore)数据库，提供查询数据和同步数据的方法。

单版本数据库，不对数据所属设备进行区分，不同设备使用相同键写入数据会互相覆盖。比如，可以使用单版本数据库实现个人日历、联系人数据在不同设备间的数据同步。

在调用SingleKVStore的方法前，需要先通过[getKVStore](js-apis-distributed-data.md#getkvstore)构建一个SingleKVStore实例。

### get

get(key: string, callback: AsyncCallback<Uint8Array | string | boolean | number>): void

获取指定键的值，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要查询数据的key，不能为空且长度不大于[MAX\_KEY\_LENGTH](js-apis-distributed-data.md#constants)。 |
| callback | AsyncCallback<Uint8Array | string | boolean | number> | 是 | 回调函数。返回获取查询的值。 |

**示例：**

```js
let kvStore;
const KEY_TEST_STRING_ELEMENT = 'key_test_string';
const VALUE_TEST_STRING_ELEMENT = 'value-test-string';
try {
    kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT, function (err,data) {
        if (err != undefined) {
            console.error("put err: " + JSON.stringify(err));
            return;
        }
        console.info("put success");
        kvStore.get(KEY_TEST_STRING_ELEMENT, function (err,data) {
            console.info("get success data: " + data);
        });
    });
}catch (e) {
    console.error("An unexpected error occurred. Error:" + e);
}
```

### get

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

```js
let kvStore;
const KEY_TEST_STRING_ELEMENT = 'key_test_string';
const VALUE_TEST_STRING_ELEMENT = 'value-test-string';
try {
    kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT).then((data) => {
        console.info("put success: " + JSON.stringify(data));
        kvStore.get(KEY_TEST_STRING_ELEMENT).then((data) => {
            console.info("get success data: " + data);
        }).catch((err) => {
            console.error("get err: " + JSON.stringify(err));
        });
    }).catch((err) => {
        console.error("put err: " + JSON.stringify(err));
    });
}catch (e) {
    console.error("An unexpected error occurred. Error:" + e);
}
```

### getEntries8+

getEntries(keyPrefix: string, callback: AsyncCallback<Entry[]>): void

获取匹配指定键前缀的所有键值对，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyPrefix | string | 是 | 表示要匹配的键前缀。 |
| callback | AsyncCallback<[Entry](js-apis-distributed-data.md#entry)[]> | 是 | 回调函数。返回匹配指定前缀的键值对列表。 |

**示例：**

```js
let kvStore;
try {
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_number_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.INTEGER,
                value : 222
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries, async function (err,data) {
        console.info('putBatch success');
        kvStore.getEntries('batch_test_number_key', function (err,entries) {
            console.info('getEntries success');
            console.info('entries.length: ' + entries.length);
            console.info('entries[0]: ' + JSON.stringify(entries[0]));
        });
    });
}catch(e) {
    console.error('PutBatch e ' + e);
}
```

### getEntries8+

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

```js
let kvStore;
try {
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
    }
    console.info('entries: ' + entries);
    kvStore.putBatch(entries).then(async (err) => {
        console.info('putBatch success');
        kvStore.getEntries('batch_test_string_key').then((entries) => {
            console.info('getEntries success');
            console.info('entries.length: ' + entries.length);
            console.info('entries[0]: ' + JSON.stringify(entries[0]));
            console.info('entries[0].value: ' + JSON.stringify(entries[0].value));
            console.info('entries[0].value.value: ' + entries[0].value.value);
        }).catch((err) => {
            console.error('getEntries fail ' + JSON.stringify(err));
        });
    }).catch((err) => {
        console.error('putBatch fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.error('PutBatch e ' + e);
}
```

### getEntries8+

getEntries(query: Query, callback: AsyncCallback<Entry[]>): void

获取与指定Query对象匹配的键值对列表，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | [Query](js-apis-distributed-data.md#query8) | 是 | 表示要匹配的键前缀。 |
| callback | AsyncCallback<[Entry](js-apis-distributed-data.md#entry)[]> | 是 | 回调函数。返回与指定Query对象匹配的键值对列表。 |

**示例：**

```js
let kvStore;
try {
    var arr = new Uint8Array([21,31]);
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_bool_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.BYTE_ARRAY,
                value : arr
            }
        }
        entries.push(entry);
    }
    console.info('entries: ' + JSON.stringify(entries));
    kvStore.putBatch(entries, async function (err,data) {
        console.info('putBatch success');
        const query = new distributedData.Query();
        query.prefixKey("batch_test");
        kvStore.getEntries(query, function (err,entries) {
            console.info('getEntries success');
            console.info('entries.length: ' + entries.length);
            console.info('entries[0]: ' + JSON.stringify(entries[0]));
        });
    });
    console.info('GetEntries success');
}catch(e) {
    console.error('GetEntries e ' + e);
}
```

### getEntries8+

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

```js
let kvStore;
try {
    var arr = new Uint8Array([21,31]);
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_bool_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.BYTE_ARRAY,
                value : arr
            }
        }
        entries.push(entry);
    }
    console.info('entries: ' + JSON.stringify(entries));
    kvStore.putBatch(entries).then(async (err) => {
        console.info('putBatch success');
        const query = new distributedData.Query();
        query.prefixKey("batch_test");
        kvStore.getEntries(query).then((entries) => {
            console.info('getEntries success');
        }).catch((err) => {
            console.error('getEntries fail ' + JSON.stringify(err));
        });
    }).catch((err) => {
        console.error('GetEntries putBatch fail ' + JSON.stringify(err))
    });
    console.info('GetEntries success');
}catch(e) {
    console.error('GetEntries e ' + e);
}
```

### getResultSet8+

getResultSet(keyPrefix: string, callback: AsyncCallback<KvStoreResultSet>): void

从KvStore数据库中获取具有指定前缀的结果集，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyPrefix | string | 是 | 表示要匹配的键前缀。 |
| callback | AsyncCallback<[KvStoreResultSet](js-apis-distributed-data.md#kvstoreresultset8)> | 是 | 回调函数。返回具有指定前缀的结果集。 |

**示例：**

```js
let kvStore;
try {
    let resultSet;
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries, async function (err, data) {
        console.info('GetResultSet putBatch success');
        kvStore.getResultSet('batch_test_string_key', async function (err, result) {
            console.info('GetResultSet getResultSet succeed.');
            resultSet = result;
            kvStore.closeResultSet(resultSet, function (err, data) {
                console.info('GetResultSet closeResultSet success');
            })
        });
    });
}catch(e) {
    console.error('GetResultSet e ' + e);
}
```

### getResultSet8+

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

```js
let kvStore;
try {
    let resultSet;
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries).then(async (err) => {
        console.info('putBatch success');
    }).catch((err) => {
        console.error('PutBatch putBatch fail ' + JSON.stringify(err));
    });
    kvStore.getResultSet('batch_test_string_key').then((result) => {
        console.info('GetResult getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.error('getResultSet failed: ' + JSON.stringify(err));
    });
    kvStore.closeResultSet(resultSet).then((err) => {
        console.info('GetResult closeResultSet success');
    }).catch((err) => {
        console.error('closeResultSet fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.error('GetResult e ' + e);
}
```

### getResultSet8+

getResultSet(query: Query, callback: AsyncCallback<KvStoreResultSet>): void

获取与指定Query对象匹配的KvStoreResultSet对象，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | Query | 是 | 表示查询对象。 |
| callback | AsyncCallback<[KvStoreResultSet](js-apis-distributed-data.md#kvstoreresultset8)> | 是 | 回调函数，获取与指定Query对象匹配的KvStoreResultSet对象。 |

**示例：**

```js
let kvStore;
try {
    let resultSet;
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries, async function (err, data) {
        console.info('putBatch success');
        const query = new distributedData.Query();
        query.prefixKey("batch_test");
        kvStore.getResultSet(query, async function (err, result) {
            console.info('getResultSet succeed.');
            resultSet = result;
        });
    });
} catch(e) {
    console.error('GetResultSet e ' + e);
}
```

### getResultSet8+

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

```js
let kvStore;
try {
    let resultSet;
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries).then(async (err) => {
        console.info('putBatch success');
    }).catch((err) => {
        console.error('putBatch fail ' + JSON.stringify(err));
    });
    const query = new distributedData.Query();
    query.prefixKey("batch_test");
    kvStore.getResultSet(query).then((result) => {
        console.info(' getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.error('getResultSet failed: ' + JSON.stringify(err));
    });
}catch(e) {
    console.error('GetResultSet e ' + e);
}
```

### closeResultSet8+

closeResultSet(resultSet: KvStoreResultSet, callback: AsyncCallback<void>): void

关闭由[SingleKVStore.getResultSet](js-apis-distributed-data.md#getresultset8)返回的KvStoreResultSet对象，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resultSet | [KvStoreResultSet](js-apis-distributed-data.md#kvstoreresultset8) | 是 | 表示要关闭的KvStoreResultSet对象。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```js
let kvStore;
try {
    let resultSet = null;
    kvStore.closeResultSet(resultSet, function (err, data) {
        if (err == undefined) {
            console.info('closeResultSet success');
        } else {
            console.error('closeResultSet fail');
        }
    });
}catch(e) {
    console.error('CloseResultSet e ' + e);
}
```

### closeResultSet8+

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

```js
let kvStore;
try {
    let resultSet = null;
    kvStore.closeResultSet(resultSet).then(() => {
        console.info('closeResultSet success');
    }).catch((err) => {
        console.error('closeResultSet fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.error('CloseResultSet e ' + e);
}
```

### getResultSize8+

getResultSize(query: Query, callback: AsyncCallback<number>): void

获取与指定Query对象匹配的结果数，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | [Query](js-apis-distributed-data.md#query8) | 是 | 表示查询对象。 |
| callback | AsyncCallback<number> | 是 | 回调函数。返回与指定Query对象匹配的结果数。 |

**示例：**

```js
let kvStore;
try {
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries, async function (err, data) {
        console.info('putBatch success');
        const query = new distributedData.Query();
        query.prefixKey("batch_test");
        kvStore.getResultSize(query, async function (err, resultSize) {
            console.info('getResultSet succeed.');
        });
    });
} catch(e) {
    console.error('GetResultSize e ' + e);
}
```

### getResultSize8+

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

```js
let kvStore;
try {
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries).then(async (err) => {
        console.info('putBatch success');
    }).catch((err) => {
        console.error('putBatch fail ' + JSON.stringify(err));
    });
    const query = new distributedData.Query();
    query.prefixKey("batch_test");
    kvStore.getResultSize(query).then((resultSize) => {
        console.info('getResultSet succeed.');
    }).catch((err) => {
        console.error('getResultSet failed: ' + JSON.stringify(err));
    });
}catch(e) {
    console.error('GetResultSize e ' + e);
}
```

### removeDeviceData8+

removeDeviceData(deviceId: string, callback: AsyncCallback<void>): void

删除指定设备的数据，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 表示要删除设备的名称。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```js
let kvStore;
const KEY_TEST_STRING_ELEMENT = 'key_test_string_2';
const VALUE_TEST_STRING_ELEMENT = 'value-string-002';
try {
    kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT, async function (err,data) {
        console.info('put success');
        const deviceid = 'no_exist_device_id';
        kvStore.removeDeviceData(deviceid, async function (err,data) {
            if (err == undefined) {
                console.info('removeDeviceData success');
            } else {
                console.error('removeDeviceData fail');
                kvStore.get(KEY_TEST_STRING_ELEMENT, async function (err,data) {
                    console.info('RemoveDeviceData get success');
                });
            }
        });
    });
}catch(e) {
    console.error('RemoveDeviceData e ' + e);
}
```

### removeDeviceData8+

removeDeviceData(deviceId: string): Promise<void>

删除指定设备的数据，使用Promise异步回调。

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

```js
let kvStore;
const KEY_TEST_STRING_ELEMENT = 'key_test_string_2';
const VALUE_TEST_STRING_ELEMENT = 'value-string-001';
try {
    kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT).then((err) => {
        console.info('removeDeviceData put success');
    }).catch((err) => {
        console.error('put fail ' + JSON.stringify(err));
    });
    const deviceid = 'no_exist_device_id';
    kvStore.removeDeviceData(deviceid).then((err) => {
        console.info('removeDeviceData success');
    }).catch((err) => {
        console.error('removeDeviceData fail ' + JSON.stringify(err));
    });
    kvStore.get(KEY_TEST_STRING_ELEMENT).then((data) => {
        console.info('get success data:' + data);
    }).catch((err) => {
        console.error('RemoveDeviceData get fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.error('RemoveDeviceData e ' + e);
}
```

### sync

sync(deviceIds: string[], mode: SyncMode, delayMs?: number): void

在手动同步方式下，触发数据库同步。

**需要权限**： ohos.permission.DISTRIBUTED\_DATASYNC。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceIds | string[] | 是 | 同一组网环境下，需要同步的设备的networkId列表。 |
| mode | [SyncMode](js-apis-distributed-data.md#syncmode) | 是 | 同步模式。 |
| delayMs | number | 否 | 可选参数，允许延时时间，单位：ms（毫秒），默认为0。 |

**示例：**

```js
let kvStore;
const KEY_TEST_SYNC_ELEMENT = 'key_test_sync';
const VALUE_TEST_SYNC_ELEMENT = 'value-string-001';
const deviceIds = ['networkId1', 'networkId2'];
try {
  kvStore.on('syncComplete', function (data) {
    console.info('Sync dataChange');
  });
  kvStore.put(KEY_TEST_SYNC_ELEMENT + 'testSync101', VALUE_TEST_SYNC_ELEMENT, function (err, data) {
    if (err != undefined) {
      console.error("put err: " + JSON.stringify(err));
      return;
    }
    console.info('Succeeded in putting data');
    const mode = distributedData.SyncMode.PULL_ONLY;
    kvStore.sync(deviceIds, mode, 1000);
  });
} catch (e) {
  console.error('Sync e' + e);
}
```

### on('dataChange')8+

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

```js
let kvStore;
kvStore.on('dataChange', distributedData.SubscribeType.SUBSCRIBE_TYPE_LOCAL, function (data) {
    console.info("dataChange callback call data: " + JSON.stringify(data));
});
```

### on('syncComplete')8+

on(event: 'syncComplete', syncCallback: Callback<Array<[string, number]>>): void

订阅同步完成事件回调通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 订阅的事件名，固定为'syncComplete'，表示同步完成事件。 |
| syncCallback | Callback<Array<[string, number]>> | 是 | 回调函数。用于向调用方发送同步结果的回调。 |

**示例：**

```js
let kvStore;
const KEY_TEST_FLOAT_ELEMENT = 'key_test_float';
const VALUE_TEST_FLOAT_ELEMENT = 321.12;
try {
    kvStore.on('syncComplete', function (data) {
        console.info('syncComplete ' + data)
    });
    kvStore.put(KEY_TEST_FLOAT_ELEMENT, VALUE_TEST_FLOAT_ELEMENT).then((data) => {
        console.info('syncComplete put success');
    }).catch((error) => {
        console.error('syncComplete put fail ' + error);
    });
}catch(e) {
    console.error('syncComplete put e ' + e);
}
```

### off('dataChange')8+

off(event:'dataChange', listener?: Callback<ChangeNotification>): void

取消订阅数据变更通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取消订阅的事件名，固定为'dataChange'，表示数据变更事件。 |
| listener | Callback<[ChangeNotification](js-apis-distributed-data.md#changenotification)> | 否 | 取消订阅的函数。如不设置callback，则取消所有订阅的函数。 |

**示例：**

```js
let kvStore;
class KvstoreModel {
    call(data) {
        console.info("dataChange: " + data);
    }
    subscribeDataChange() {
        if (kvStore != null) {
            kvStore.on('dataChange', distributedData.SubscribeType.SUBSCRIBE_TYPE_REMOTE, this.call);
        }
    }
    unsubscribeDataChange() {
        if (kvStore != null) {
            kvStore.off('dataChange', this.call);
        }
    }
}
```

### off('syncComplete')8+

off(event: 'syncComplete', syncCallback?: Callback<Array<[string, number]>>): void

取消订阅同步完成事件回调通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取消订阅的事件名，固定为'syncComplete'，表示同步完成事件。 |
| syncCallback | Callback<Array<[string, number]>> | 否 | 取消订阅的函数。如不设置callback，则取消所有订阅的函数。 |

**示例：**

```js
let kvStore;
class KvstoreModel {
    call(data) {
        console.info("syncComplete: " + data);
    }
    subscribeSyncComplete() {
        if (kvStore != null) {
            kvStore.on('syncComplete', this.call);
        }
    }
    unsubscribeSyncComplete() {
        if (kvStore != null) {
            kvStore.off('syncComplete', this.call);
        }
    }
}
```

### setSyncParam8+

setSyncParam(defaultAllowedDelayMs: number, callback: AsyncCallback<void>): void

设置数据库同步允许的默认延迟，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| defaultAllowedDelayMs | number | 是 | 表示数据库同步允许的默认延迟，以毫秒为单位。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```js
let kvStore;
try {
    const defaultAllowedDelayMs = 500;
    kvStore.setSyncParam(defaultAllowedDelayMs, function (err,data) {
        console.info('SetSyncParam put success');
    });
}catch(e) {
    console.error('testSingleKvStoreSetSyncParam e ' + e);
}
```

### setSyncParam8+

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

```js
let kvStore;
try {
    const defaultAllowedDelayMs = 500;
    kvStore.setSyncParam(defaultAllowedDelayMs).then((err) => {
        console.info('SetSyncParam put success');
    }).catch((err) => {
        console.error('SetSyncParam put fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.error('SetSyncParam e ' + e);
}
```

### getSecurityLevel8+

getSecurityLevel(callback: AsyncCallback<SecurityLevel>): void

获取数据库的安全级别，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[SecurityLevel](js-apis-distributed-data.md#securitylevel)> | 是 | 回调函数。返回数据库的安全级别。 |

**示例：**

```js
let kvStore;
try {
    kvStore.getSecurityLevel(function (err,data) {
        console.info('getSecurityLevel success');
    });
}catch(e) {
    console.error('GetSecurityLevel e ' + e);
}
```

### getSecurityLevel8+

getSecurityLevel(): Promise<SecurityLevel>

获取数据库的安全级别，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SecurityLevel](js-apis-distributed-data.md#securitylevel)> | Promise对象。返回数据库的安全级别。 |

**示例：**

```js
let kvStore;
try {
    kvStore.getSecurityLevel().then((data) => {
        console.info(' getSecurityLevel success');
    }).catch((err) => {
        console.error('getSecurityLevel fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.error('GetSecurityLevel e ' + e);
}
```

## DeviceKVStore8+

设备协同数据库，继承自KVStore，提供查询数据和同步数据的方法。

设备协同数据库，以设备维度对数据进行区分，每台设备仅能写入和修改本设备的数据，其它设备的数据对其是只读的，无法修改其它设备的数据。

比如，可以使用设备协同数据库实现设备间的图片分享，可以查看其他设备的图片，但无法修改和删除其他设备的图片。

在调用DeviceKVStore的方法前，需要先通过[getKVStore](js-apis-distributed-data.md#getkvstore)构建一个DeviceKVStore实例。

### get8+

get(deviceId: string, key: string, callback: AsyncCallback<boolean|string|number|Uint8Array>): void

获取与指定设备ID和key匹配的string值，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 标识要查询其数据的设备。 |
| key | string | 是 | 表示要查询key值的键。 |
| callback | AsyncCallback<boolean|string|number|Uint8Array> | 是 | 回调函数，返回匹配给定条件的字符串值。 |

**示例：**

```js
let kvStore;
const KEY_TEST_STRING_ELEMENT = 'key_test_string_2';
const VALUE_TEST_STRING_ELEMENT = 'value-string-002';
try{
    kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT, async function (err,data) {
        console.info('put success');
        kvStore.get('localDeviceId', KEY_TEST_STRING_ELEMENT, function (err,data) {
            console.info('get success');
        });
    })
}catch(e) {
    console.error('get e' + e);
}
```

### get8+

get(deviceId: string, key: string): Promise<boolean|string|number|Uint8Array>

获取与指定设备ID和key匹配的string值，使用Promise异步回调。

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

```js
let kvStore;
const KEY_TEST_STRING_ELEMENT = 'key_test_string_2';
const VALUE_TEST_STRING_ELEMENT = 'value-string-002';
try {
    kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT).then(async (data) => {
        console.info(' put success');
        kvStore.get('localDeviceId', KEY_TEST_STRING_ELEMENT).then((data) => {
            console.info('get success');
        }).catch((err) => {
            console.error('get fail ' + JSON.stringify(err));
        });
    }).catch((error) => {
        console.error('put error' + error);
    });
} catch (e) {
    console.error('Get e ' + e);
}
```

### getEntries8+

getEntries(deviceId: string, keyPrefix: string, callback: AsyncCallback<Entry[]>): void

获取与指定设备ID和key前缀匹配的所有键值对，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 标识要查询其数据的设备。 |
| keyPrefix | string | 是 | 表示要匹配的键前缀。 |
| callback | AsyncCallback<[Entry](js-apis-distributed-data.md#entry)[]> | 是 | 回调函数，返回满足给定条件的所有键值对的列表。 |

**示例：**

```js
let kvStore;
try {
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
    }
    console.info('entries: ' + entries);
    kvStore.putBatch(entries, async function (err,data) {
        console.info('putBatch success');
        kvStore.getEntries('localDeviceId', 'batch_test_string_key', function (err,entries) {
            console.info('getEntries success');
            console.info('entries.length: ' + entries.length);
            console.info('entries[0]: ' + JSON.stringify(entries[0]));
        });
    });
}catch(e) {
    console.error('PutBatch e ' + e);
}
```

### getEntries8+

getEntries(deviceId: string, keyPrefix: string): Promise<Entry[]>

获取与指定设备ID和key前缀匹配的所有键值对，使用Promise异步回调。

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

```js
let kvStore;
try {
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
    }
    console.info('entries: ' + entries);
    kvStore.putBatch(entries).then(async (err) => {
        console.info('putBatch success');
        kvStore.getEntries('localDeviceId', 'batch_test_string_key').then((entries) => {
            console.info('getEntries success');
            console.info('entries.length: ' + entries.length);
            console.info('entries[0]: ' + JSON.stringify(entries[0]));
            console.info('entries[0].value: ' + JSON.stringify(entries[0].value));
            console.info('entries[0].value.value: ' + entries[0].value.value);
        }).catch((err) => {
            console.error('getEntries fail ' + JSON.stringify(err));
        });
    }).catch((err) => {
        console.error('putBatch fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.error('PutBatch e ' + e);
}
```

### getEntries8+

getEntries(query: Query, callback: AsyncCallback<Entry[]>): void

获取与指定Query对象匹配的键值对列表，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | [Query](js-apis-distributed-data.md#query8) | 是 | 表示查询对象。 |
| callback | AsyncCallback<[Entry](js-apis-distributed-data.md#entry)[]> | 是 | 回调函数，返回与指定Query对象匹配的键值对列表。 |

**示例：**

```js
let kvStore;
try {
    var arr = new Uint8Array([21,31]);
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_bool_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.BYTE_ARRAY,
                value : arr
            }
        }
        entries.push(entry);
    }
    console.info('entries: ' + JSON.stringify(entries));
    kvStore.putBatch(entries, async function (err,data) {
        console.info('putBatch success');
        const query = new distributedData.Query();
        query.prefixKey("batch_test");
        query.deviceId('localDeviceId');
        kvStore.getEntries(query, function (err,entries) {
            console.info('getEntries success');
            console.info('entries.length: ' + entries.length);
            console.info('entries[0]: ' + JSON.stringify(entries[0]));
        });
    });
    console.info('GetEntries success');
}catch(e) {
    console.error('GetEntries e ' + e);
}
```

### getEntries8+

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

```js
let kvStore;
try {
    var arr = new Uint8Array([21,31]);
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_bool_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.BYTE_ARRAY,
                value : arr
            }
        }
        entries.push(entry);
    }
    console.info('entries: ' + JSON.stringify(entries));
    kvStore.putBatch(entries).then(async (err) => {
        console.info('putBatch success');
        const query = new distributedData.Query();
        query.prefixKey("batch_test");
        kvStore.getEntries(query).then((entries) => {
            console.info('getEntries success');
        }).catch((err) => {
            console.error('getEntries fail ' + JSON.stringify(err));
        });
    }).catch((err) => {
        console.error('GetEntries putBatch fail ' + JSON.stringify(err))
    });
    console.info('GetEntries success');
}catch(e) {
    console.error('GetEntries e ' + e);
}
```

### getEntries8+

getEntries(deviceId: string, query: Query, callback: AsyncCallback<Entry[]>): void

获取与指定设备ID和Query对象匹配的键值对列表，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 键值对所属的设备ID。 |
| query | [Query](js-apis-distributed-data.md#query8) | 是 | 表示查询对象。 |
| callback | AsyncCallback<[Entry](js-apis-distributed-data.md#entry)[]> | 是 | 回调函数。返回与指定设备ID和Query对象匹配的键值对列表。 |

**示例：**

```js
let kvStore;
try {
    var arr = new Uint8Array([21,31]);
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_bool_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.BYTE_ARRAY,
                value : arr
            }
        }
        entries.push(entry);
    }
    console.info('entries: ' + JSON.stringify(entries));
    kvStore.putBatch(entries, async function (err,data) {
        console.info('putBatch success');
        var query = new distributedData.Query();
        query.deviceId('localDeviceId');
        query.prefixKey("batch_test");
        kvStore.getEntries('localDeviceId', query, function (err,entries) {
            console.info('getEntries success');
            console.info('entries.length: ' + entries.length);
            console.info('entries[0]: ' + JSON.stringify(entries[0]));
        })
    });
    console.info('GetEntries success');
}catch(e) {
    console.error('GetEntries e ' + e);
}
```

### getEntries8+

getEntries(deviceId: string, query: Query): Promise<Entry[]>

获取与指定设备ID和Query对象匹配的键值对列表，使用Promise异步回调。

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

```js
let kvStore;
try {
    var arr = new Uint8Array([21,31]);
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_bool_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.BYTE_ARRAY,
                value : arr
            }
        }
        entries.push(entry);
    }
    console.info('entries: ' + JSON.stringify(entries));
    kvStore.putBatch(entries).then(async (err) => {
        console.info('putBatch success');
        var query = new distributedData.Query();
        query.deviceId('localDeviceId');
        query.prefixKey("batch_test");
        kvStore.getEntries('localDeviceId', query).then((entries) => {
            console.info('getEntries success');
        }).catch((err) => {
            console.error('getEntries fail ' + JSON.stringify(err));
        });
    }).catch((err) => {
        console.error('putBatch fail ' + JSON.stringify(err));
    });
    console.info('GetEntries success');
}catch(e) {
    console.error('GetEntries e ' + e);
}
```

### getResultSet8+

getResultSet(deviceId: string, keyPrefix: string, callback: AsyncCallback<KvStoreResultSet>): void

获取与指定设备ID和key前缀匹配的KvStoreResultSet对象，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 标识要查询其数据的设备。 |
| keyPrefix | string | 是 | 表示要匹配的键前缀。 |
| callback | AsyncCallback<[KvStoreResultSet](js-apis-distributed-data.md#kvstoreresultset8)> | 是 | 回调函数。返回与指定设备ID和key前缀匹配的KvStoreResultSet对象。 |

**示例：**

```js
let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('localDeviceId', 'batch_test_string_key', async function (err, result) {
        console.info('getResultSet succeed.');
        resultSet = result;
        kvStore.closeResultSet(resultSet, function (err, data) {
            console.info('closeResultSet success');
        })
    });
}catch(e) {
    console.error('GetResultSet e ' + e);
}
```

### getResultSet8+

getResultSet(deviceId: string, keyPrefix: string): Promise<KvStoreResultSet>

获取与指定设备ID和key前缀匹配的KvStoreResultSet对象，使用Promise异步回调。

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

```js
let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('localDeviceId', 'batch_test_string_key').then((result) => {
        console.info('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.error('getResultSet failed: ' + JSON.stringify(err));
    });
    kvStore.closeResultSet(resultSet).then((err) => {
        console.info('closeResultSet success');
    }).catch((err) => {
        console.error('closeResultSet fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.error('GetResultSet e ' + e);
}
```

### getResultSet8+

getResultSet(query: Query, callback: AsyncCallback<KvStoreResultSet>): void

获取与指定Query对象匹配的KvStoreResultSet对象，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | [Query](js-apis-distributed-data.md#query8) | 是 | 表示查询对象。 |
| callback | AsyncCallback<[KvStoreResultSet](js-apis-distributed-data.md#kvstoreresultset8)> | 是 | 回调函数，返回与指定Query对象匹配的KvStoreResultSet对象。 |

**示例：**

```js
let kvStore;
try {
    let resultSet;
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries, async function (err, data) {
        console.info('putBatch success');
        const query = new distributedData.Query();
        query.prefixKey("batch_test");
        query.deviceId('localDeviceId');
        kvStore.getResultSet(query, async function (err, result) {
            console.info('getResultSet succeed.');
            resultSet = result;
            kvStore.closeResultSet(resultSet, function (err, data) {
                console.info('closeResultSet success');
            })
        });
    });
} catch(e) {
    console.error('GetResultSet e ' + e);
}
```

### getResultSet8+

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

```js
let kvStore;
try {
    let resultSet;
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries).then(async (err) => {
        console.info('putBatch success');
    }).catch((err) => {
        console.error('putBatch fail ' + err);
    });
    const query = new distributedData.Query();
    query.deviceId('localDeviceId');
    query.prefixKey("batch_test");
    console.info("GetResultSet " + query.getSqlLike());
    kvStore.getResultSet(query).then((result) => {
        console.info('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.error('getResultSet failed: ' + JSON.stringify(err));
    });
    kvStore.closeResultSet(resultSet).then((err) => {
        console.info('closeResultSet success');
    }).catch((err) => {
        console.error('closeResultSet fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.error('GetResultSet e ' + e);
}
```

### getResultSet8+

getResultSet(deviceId: string, query: Query, callback: AsyncCallback<KvStoreResultSet>): void

获取与指定设备ID和Query对象匹配的KvStoreResultSet对象，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | KvStoreResultSet对象所属的设备ID。 |
| query | [Query](js-apis-distributed-data.md#query8) | 是 | 表示查询对象。 |
| callback | AsyncCallback<[KvStoreResultSet](js-apis-distributed-data.md#kvstoreresultset8)> | 是 | 回调函数。返回与指定设备ID和Query对象匹配的KvStoreResultSet对象。 |

**示例：**

```js
let kvStore;
try {
    let resultSet;
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries, async function (err, data) {
        console.info('putBatch success');
        const query = new distributedData.Query();
        query.prefixKey("batch_test");
        kvStore.getResultSet('localDeviceId', query, async function (err, result) {
            console.info('getResultSet succeed.');
            resultSet = result;
            kvStore.closeResultSet(resultSet, function (err, data) {
                console.info('closeResultSet success');
            })
        });
    });
} catch(e) {
    console.error('GetResultSet e ' + e);
}
```

### getResultSet8+

getResultSet(deviceId: string, query: Query): Promise<KvStoreResultSet>

获取与指定设备ID和Query对象匹配的KvStoreResultSet对象，使用Promise异步回调。

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

```js
let kvStore;
try {
    let resultSet;
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries).then(async (err) => {
        console.info('GetResultSet putBatch success');
    }).catch((err) => {
        console.error('PutBatch putBatch fail ' + JSON.stringify(err));
    });
    const query = new distributedData.Query();
    query.prefixKey("batch_test");
    kvStore.getResultSet('localDeviceId', query).then((result) => {
        console.info('GetResultSet getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.error('GetResultSet getResultSet failed: ' + JSON.stringify(err));
    });
    query.deviceId('localDeviceId');
    console.info("GetResultSet " + query.getSqlLike());
    kvStore.closeResultSet(resultSet).then((err) => {
        console.info('GetResultSet closeResultSet success');
    }).catch((err) => {
        console.error('GetResultSet closeResultSet fail ' + JSON.stringify(err));
    });

}catch(e) {
    console.error('GetResultSet e ' + e);
}
```

### closeResultSet8+

closeResultSet(resultSet: KvStoreResultSet, callback: AsyncCallback<void>): void

关闭由[DeviceKVStore.getResultSet](js-apis-distributed-data.md#getresultset8-4)返回的KvStoreResultSet对象，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resultSet | [KvStoreResultSet](js-apis-distributed-data.md#kvstoreresultset8) | 是 | 指示要关闭的KvStoreResultSet对象。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```js
let kvStore;
try {
    console.info('CloseResultSet success');
    let resultSet = null;
    kvStore.closeResultSet(resultSet, function (err, data) {
        if (err == undefined) {
            console.info('closeResultSet success');
        } else {
            console.error('closeResultSet fail');
        }
    });
}catch(e) {
    console.error('CloseResultSet e ' + e);
}
```

### closeResultSet8+

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

```js
let kvStore;
try {
    console.info('CloseResultSet success');
    let resultSet = null;
    kvStore.closeResultSet(resultSet).then(() => {
        console.info('closeResultSet success');
    }).catch((err) => {
        console.error('closeResultSet fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.error('CloseResultSet e ' + e);
}
```

### getResultSize8+

getResultSize(query: Query, callback: AsyncCallback<number>): void

获取与指定Query对象匹配的结果数，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | [Query](js-apis-distributed-data.md#query8) | 是 | 表示查询对象。 |
| callback | AsyncCallback<number> | 是 | 回调函数，返回与指定Query对象匹配的结果数。 |

**示例：**

```js
let kvStore;
try {
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries, async function (err, data) {
        console.info('putBatch success');
        const query = new distributedData.Query();
        query.prefixKey("batch_test");
        query.deviceId('localDeviceId');
        kvStore.getResultSize(query, async function (err, resultSize) {
            console.info('getResultSet succeed.');
        });
    });
} catch(e) {
    console.error('GetResultSize e ' + e);
}
```

### getResultSize8+

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

```js
let kvStore;
try {
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries).then(async (err) => {
        console.info('putBatch success');
    }).catch((err) => {
        console.error('putBatch fail ' + JSON.stringify(err));
    });
    const query = new distributedData.Query();
    query.prefixKey("batch_test");
    query.deviceId('localDeviceId');
    kvStore.getResultSize(query).then((resultSize) => {
        console.info('getResultSet succeed.');
    }).catch((err) => {
        console.error('getResultSet failed: ' + JSON.stringify(err));
    });
}catch(e) {
    console.error('GetResultSize e ' + e);
}
```

### getResultSize8+

getResultSize(deviceId: string, query: Query, callback: AsyncCallback<number>): void;

获取与指定设备ID和Query对象匹配的结果数，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | KvStoreResultSet对象所属的设备ID。 |
| query | [Query](js-apis-distributed-data.md#query8) | 是 | 表示查询对象。 |
| callback | AsyncCallback<number> | 是 | 回调函数。返回与指定设备ID和Query对象匹配的结果数。 |

**示例：**

```js
let kvStore;
try {
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries, async function (err, data) {
        console.info('putBatch success');
        const query = new distributedData.Query();
        query.prefixKey("batch_test");
        kvStore.getResultSize('localDeviceId', query, async function (err, resultSize) {
            console.info('getResultSet succeed.');
        });
    });
} catch(e) {
    console.error('GetResultSize e ' + e);
}
```

### getResultSize8+

getResultSize(deviceId: string, query: Query): Promise<number>

获取与指定设备ID和Query对象匹配的结果数，使用Promise异步回调。

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

```js
let kvStore;
try {
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries).then(async (err) => {
        console.info('putBatch success');
    }).catch((err) => {
        console.error('putBatch fail ' + JSON.stringify(err));
    });
    var query = new distributedData.Query();
    query.prefixKey("batch_test");
    kvStore.getResultSize('localDeviceId', query).then((resultSize) => {
        console.info('getResultSet succeed.');
    }).catch((err) => {
        console.error('getResultSet failed: ' + JSON.stringify(err));
    });
}catch(e) {
    console.error('GetResultSize e ' + e);
}
```

### removeDeviceData8+

removeDeviceData(deviceId: string, callback: AsyncCallback<void>): void

从当前数据库中删除指定设备的数据，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 标识要删除其数据的设备。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**示例：**

```js
let kvStore;
const KEY_TEST_STRING_ELEMENT = 'key_test_string';
const VALUE_TEST_STRING_ELEMENT = 'value-string-001';
try {
    kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT, async function (err,data) {
        console.info('RemoveDeviceData  put success');
        const deviceid = 'no_exist_device_id';
        kvStore.removeDeviceData(deviceid, async function (err,data) {
            if (err == undefined) {
                console.info('removeDeviceData success');
            } else {
                console.error('removeDeviceData fail');
                kvStore.get('localDeviceId', KEY_TEST_STRING_ELEMENT, async function (err,data) {
                    console.info('RemoveDeviceData get success');
                });
            }
        });
    });
}catch(e) {
    console.error('RemoveDeviceData e ' + e);
}
```

### removeDeviceData8+

removeDeviceData(deviceId: string): Promise<void>

从当前数据库中删除指定设备的数据，使用Promise异步回调。

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

```js
let kvStore;
const KEY_TEST_STRING_ELEMENT = 'key_test_string';
const VALUE_TEST_STRING_ELEMENT = 'value-string-001';
try {
    kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT).then((err) => {
        console.info('RemoveDeviceData put success');
    }).catch((err) => {
        console.error('RemoveDeviceData put fail ' + JSON.stringify(err));
    });
    const deviceid = 'no_exist_device_id';
    kvStore.removeDeviceData(deviceid).then((err) => {
        console.info('removeDeviceData success');
    }).catch((err) => {
        console.error('removeDeviceData fail ' + JSON.stringify(err));
    });
    kvStore.get('localDeviceId', KEY_TEST_STRING_ELEMENT).then((data) => {
        console.info('RemoveDeviceData get success data:' + data);
    }).catch((err) => {
        console.error('RemoveDeviceData get fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.error('RemoveDeviceData e ' + e);
}
```

### sync8+

sync(deviceIds: string[], mode: SyncMode, delayMs?: number): void

在手动同步方式下，触发数据库同步。

**需要权限**： ohos.permission.DISTRIBUTED\_DATASYNC。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceIds | string[] | 是 | 需要同步DeviceKVStore数据库的设备networkId列表。 |
| mode | [SyncMode](js-apis-distributed-data.md#syncmode) | 是 | 同步模式。 |
| delayMs | number | 否 | 可选参数，允许延时时间，单位：ms（毫秒），默认为0。 |

**示例：**

```js
let kvStore;
const KEY_TEST_SYNC_ELEMENT = 'key_test_sync';
const VALUE_TEST_SYNC_ELEMENT = 'value-string-001';
const deviceIds = ['networkId1', 'networkId2'];
try {
  kvStore.on('syncComplete', function (data) {
    console.info('Sync dataChange');
  });
  kvStore.put(KEY_TEST_SYNC_ELEMENT + 'testSync101', VALUE_TEST_SYNC_ELEMENT, function (err, data) {
    if (err != undefined) {
      console.error("put err: " + JSON.stringify(err));
      return;
    }
    console.info('Succeeded in putting data');
    const mode = distributedData.SyncMode.PULL_ONLY;
    kvStore.sync(deviceIds, mode, 1000);
  });
} catch (e) {
  console.error('Sync e' + e);
}
```

### on('dataChange')8+

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

```js
let kvStore;
kvStore.on('dataChange', distributedData.SubscribeType.SUBSCRIBE_TYPE_LOCAL, function (data) {
    console.info("dataChange callback call data: " + JSON.stringify(data));
});
```

### on('syncComplete')8+

on(event: 'syncComplete', syncCallback: Callback<Array<[string, number]>>): void

订阅同步完成事件回调通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 订阅的事件名，固定为'syncComplete'，表示同步完成事件。 |
| syncCallback | Callback<Array<[string, number]>> | 是 | 回调函数。用于向调用方发送同步结果的回调。 |

**示例：**

```js
let kvStore;
const KEY_TEST_FLOAT_ELEMENT = 'key_test_float';
const VALUE_TEST_FLOAT_ELEMENT = 321.12;
try {
    kvStore.on('syncComplete', function (data) {
        console.info('syncComplete ' + data)
    });
    kvStore.put(KEY_TEST_FLOAT_ELEMENT, VALUE_TEST_FLOAT_ELEMENT).then((data) => {
        console.info('syncComplete put success');
    }).catch((error) => {
        console.error('syncComplete put fail ' + error);
    });
}catch(e) {
    console.error('syncComplete put e ' + e);
}
```

### off('dataChange')8+

off(event:'dataChange', listener?: Callback<ChangeNotification>): void

取消订阅数据变更通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取消订阅的事件名，固定为'dataChange'，表示数据变更事件。 |
| listener | Callback<[ChangeNotification](js-apis-distributed-data.md#changenotification)> | 否 | 取消订阅的函数。如不设置callback，则取消所有订阅的函数。 |

**示例：**

```js
let kvStore;
class KvstoreModel {
    call(data) {
        console.info("dataChange: " + data);
    }
    subscribeDataChange() {
        if (kvStore != null) {
            kvStore.on('dataChange', distributedData.SubscribeType.SUBSCRIBE_TYPE_REMOTE, this.call);
        }
    }
    unsubscribeDataChange() {
        if (kvStore != null) {
            kvStore.off('dataChange', this.call);
        }
    }
}
```

### off('syncComplete')8+

off(event: 'syncComplete', syncCallback?: Callback<Array<[string, number]>>): void

取消订阅同步完成事件回调通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取消订阅的事件名，固定为'syncComplete'，表示同步完成事件。 |
| syncCallback | Callback<Array<[string, number]>> | 否 | 取消订阅的函数。如不设置callback，则取消所有订阅的函数。 |

**示例：**

```js
let kvStore;
class KvstoreModel {
    call(data) {
        console.info("syncComplete: " + data);
    }
    subscribeSyncComplete() {
        if (kvStore != null) {
            kvStore.on('syncComplete', this.call);
        }
    }
    unsubscribeSyncComplete() {
        if (kvStore != null) {
            kvStore.off('syncComplete', this.call);
        }
    }
}
```

## SyncMode

同步模式枚举。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PULL\_ONLY | 0 | 表示只能从远端拉取数据到本端。 |
| PUSH\_ONLY | 1 | 表示只能从本端推送数据到远端。 |
| PUSH\_PULL | 2 | 表示从本端推送数据到远端，然后从远端拉取数据到本端。 |
