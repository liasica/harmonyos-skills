---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributedkvstore
title: @ohos.data.distributedKVStore (分布式键值数据库)
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > ArkTS API > @ohos.data.distributedKVStore (分布式键值数据库)
category: harmonyos-references
scraped_at: 2026-04-28T07:59:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:04e58a6ac1a16dd7e6a2a225e588587a315c98f73eba41375ab50a6718857c69
---

分布式键值数据库为应用程序提供不同设备间数据库的分布式协同能力。通过调用分布式键值数据库各个接口，应用程序可将数据保存到分布式键值数据库中，并可对分布式键值数据库中的数据进行增加、删除、修改、查询、端端同步等操作。

该模块提供以下常用功能：

* [KVManager](js-apis-distributedkvstore.md#kvmanager)：分布式键值数据库管理实例，用于获取数据库的相关信息。
* [KVStoreResultSet](js-apis-distributedkvstore.md#kvstoreresultset)：提供获取数据库结果集的相关方法，包括查询和移动数据读取位置等。
* [Query](js-apis-distributedkvstore.md#query)：使用谓词表示数据库查询，提供创建Query实例、查询数据库中的数据和添加谓词的方法。
* [SingleKVStore](js-apis-distributedkvstore.md#singlekvstore)：单版本分布式键值数据库，不对数据所属设备进行区分，提供查询数据和端端同步数据的方法。
* [DeviceKVStore](js-apis-distributedkvstore.md#devicekvstore)：设备协同数据库，继承自[SingleKVStore](js-apis-distributedkvstore.md#singlekvstore)，以设备维度对数据进行区分，提供查询数据和端端同步数据的方法。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { distributedKVStore } from '@kit.ArkData';
```

## KVManagerConfig

PhonePC/2in1TabletTVWearable

提供KVManager实例的配置信息，包括调用方的包名和应用的上下文。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [BaseContext](js-apis-inner-application-basecontext.md) | 否 | 否 | 应用的上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-uiabilitycontext.md)。  从API version 10开始，context的参数类型为[BaseContext](js-apis-inner-application-basecontext.md)。 |
| bundleName | string | 否 | 否 | 调用方的包名。 |

## Constants

PhonePC/2in1TabletTVWearable

分布式键值数据库常量。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| MAX\_KEY\_LENGTH | number | 是 | 否 | 值为1024，表示数据库中Key允许的最大长度，单位字节。 |
| MAX\_VALUE\_LENGTH | number | 是 | 否 | 值为4194303，表示数据库中Value允许的最大长度，单位字节。 |
| MAX\_KEY\_LENGTH\_DEVICE | number | 是 | 否 | 值为896，表示设备协同数据库中Key允许的最大长度，单位字节。 |
| MAX\_STORE\_ID\_LENGTH | number | 是 | 否 | 值为128，表示数据库标识符允许的最大长度，单位字节。 |
| MAX\_QUERY\_LENGTH | number | 是 | 否 | 值为512000，表示最大查询长度，单位字节。 |
| MAX\_BATCH\_SIZE | number | 是 | 否 | 值为128，表示最大批处理操作数量。 |

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

## Value

PhonePC/2in1TabletTVWearable

存储在数据库中的值对象。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [ValueType](js-apis-distributedkvstore.md#valuetype) | 否 | 否 | 值类型。 |
| value | Uint8Array | string | number | boolean | 否 | 否 | 值。 |

## Entry

PhonePC/2in1TabletTVWearable

存储在数据库中的键值对。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| key | string | 否 | 否 | 键值。 |
| value | [Value](js-apis-distributedkvstore.md#value) | 否 | 否 | 值对象。 |

## ChangeNotification

PhonePC/2in1TabletTVWearable

数据变更时通知的对象，包括插入的数据、更新的数据、删除的数据和设备ID。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| insertEntries | [Entry](js-apis-distributedkvstore.md#entry)[] | 否 | 否 | 数据添加记录。 |
| updateEntries | [Entry](js-apis-distributedkvstore.md#entry)[] | 否 | 否 | 数据更新记录。 |
| deleteEntries | [Entry](js-apis-distributedkvstore.md#entry)[] | 否 | 否 | 数据删除记录。 |
| deviceId | string | 否 | 否 | 设备ID，此处为设备UUID。 |

## SyncMode

PhonePC/2in1TabletTVWearable

同步模式枚举。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PULL\_ONLY | 0 | 表示只能从远端拉取数据到本端。 |
| PUSH\_ONLY | 1 | 表示只能从本端推送数据到远端。 |
| PUSH\_PULL | 2 | 表示从本端推送数据到远端，然后从远端拉取数据到本端。 |

## SubscribeType

PhonePC/2in1TabletTVWearable

订阅类型枚举。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUBSCRIBE\_TYPE\_LOCAL | 0 | 表示订阅本地数据变更。 |
| SUBSCRIBE\_TYPE\_REMOTE | 1 | 表示订阅远端数据变更。 |
| SUBSCRIBE\_TYPE\_ALL | 2 | 表示订阅远端和本地数据变更。 |

## KVStoreType

PhonePC/2in1TabletTVWearable

分布式键值数据库类型枚举。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEVICE\_COLLABORATION | 0 | 表示多设备协同数据库。  **数据库特点：** 数据以设备的维度管理，不存在冲突；支持按照设备的维度查询数据。  **系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore |
| SINGLE\_VERSION | 1 | 表示单版本数据库。  **数据库特点：** 数据不分设备，设备之间修改相同的Key会覆盖。  **系统能力：** SystemCapability.DistributedDataManager.KVStore.Core |

## SecurityLevel

PhonePC/2in1TabletTVWearable

数据库的安全级别枚举。

说明

在单设备使用场景下，KV数据库支持修改securityLevel参数进行安全等级升级。升级操作需要注意以下几点：

* 该操作不支持跨设备同步的数据库。不同安全等级的数据库之间不能进行数据同步。若需升级数据库的安全等级，建议重新创建更高安全等级的数据库。
* 关闭当前数据库后，修改securityLevel参数以重新设置数据库的安全等级，然后重新打开数据库。
* 该操作仅支持升级，例如从S2到S3，不支持降级，例如从S3到S2。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| S1 | 2 | 表示数据库的安全级别为低级别，数据的泄露、篡改、破坏、销毁可能会给个人或组织导致有限的不利影响。  例如，性别、国籍，用户申请记录等。 |
| S2 | 3 | 表示数据库的安全级别为中级别，数据的泄露、篡改、破坏、销毁可能会给个人或组织导致严重的不利影响。  例如，个人详细通信地址，姓名昵称等。 |
| S3 | 5 | 表示数据库的安全级别为高级别，数据的泄露、篡改、破坏、销毁可能会给个人或组织导致严峻的不利影响。  例如，个人实时精确定位信息、运动轨迹等。 |
| S4 | 6 | 表示数据库的安全级别为关键级别，业界法律法规中定义的特殊数据类型，涉及个人的最私密领域的信息，一旦泄露、篡改、破坏、销毁可能会给个人或组织造成重大的不利影响。  例如，政治观点、宗教、哲学信仰、工会成员资格、基因数据、生物信息、健康、性生活状况、性取向、设备认证鉴权或个人的信用卡等财务信息。 |

## Options

PhonePC/2in1TabletTVWearable

用于提供创建数据库的配置信息。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| createIfMissing | boolean | 否 | 是 | 当数据库文件不存在时是否创建数据库，true为创建，false为不创建，默认为true。  **系统能力：** SystemCapability.DistributedDataManager.KVStore.Core |
| encrypt | boolean | 否 | 是 | 设置数据库文件是否加密，true为加密，false为不加密，默认为false。  **系统能力：** SystemCapability.DistributedDataManager.KVStore.Core |
| backup | boolean | 否 | 是 | 设置数据库文件是否备份，true为备份，false为不备份，默认为true。  **系统能力：** SystemCapability.DistributedDataManager.KVStore.Core |
| autoSync | boolean | 否 | 是 | 设置数据库是否支持跨设备自动同步。默认为false，即只支持手动同步。配置为true，即只支持在跨设备Call调用实现的多端协同中生效，其他场景无法生效。  **系统能力：** SystemCapability.DistributedDataManager.KVStore.Core  **需要权限**： ohos.permission.DISTRIBUTED\_DATASYNC |
| kvStoreType | [KVStoreType](js-apis-distributedkvstore.md#kvstoretype) | 否 | 是 | 设置要创建的数据库类型，默认为DEVICE\_COLLABORATION，即多设备协同数据库。  **系统能力：** SystemCapability.DistributedDataManager.KVStore.Core |
| securityLevel | [SecurityLevel](js-apis-distributedkvstore.md#securitylevel) | 否 | 否 | 设置数据库安全级别。  **系统能力：** SystemCapability.DistributedDataManager.KVStore.Core |
| schema | [Schema](js-apis-distributedkvstore.md#schema) | 否 | 是 | 设置定义存储在数据库中的值，默认为undefined，即不使用Schema。  **系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore |

## Schema

PhonePC/2in1TabletTVWearable

表示数据库模式，可以在创建或打开数据库时创建Schema对象并将它们放入[Options](js-apis-distributedkvstore.md#options)中。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| root | [FieldNode](js-apis-distributedkvstore.md#fieldnode) | 否 | 否 | 存放了Value中所有字段的定义。 |
| indexes | Array<string> | 否 | 否 | 索引字段定义，只有通过此字段指定的FieldNode才会创建索引，格式为：'$.field1', '$.field2'。 |
| mode | number | 否 | 否 | Schema的模式，可以取值0或1，0表示COMPATIBLE模式，1表示STRICT模式。 |
| skip | number | 否 | 否 | 支持在检查Value时，跳过skip指定的字节数，且取值范围为[0, 4 \* 1024 \* 1024 - 2]字节。 |

STRICT：STRICT模式要求用户插入的值必须与Schema定义严格匹配，字段数量和格式都不能有差异。如果不匹配，数据库将在插入数据时返回错误。

COMPATIBLE：选择为COMPATIBLE模式时，数据库在检查Value格式时较为宽松，只要Value具有Schema描述的特征即可，允许存在额外字段。例如，定义了id、name字段时，可以插入id、name、age等多个字段。

### constructor

PhonePC/2in1TabletTVWearable

constructor()

用于创建Schema实例的构造函数。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**示例：**

```
1. let child1 = new distributedKVStore.FieldNode('id');
2. child1.type = distributedKVStore.ValueType.INTEGER;
3. child1.nullable = false;
4. child1.default = '1';
5. let child2 = new distributedKVStore.FieldNode('name');
6. child2.type = distributedKVStore.ValueType.STRING;
7. child2.nullable = false;
8. child2.default = 'zhangsan';

10. let schema = new distributedKVStore.Schema();
11. schema.root.appendChild(child1);
12. schema.root.appendChild(child2);
13. schema.indexes = ['$.id', '$.name'];
14. schema.mode = 1;
15. schema.skip = 0;
```

## FieldNode

PhonePC/2in1TabletTVWearable

表示 Schema 实例的节点，提供定义存储在数据库中的值的方法。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| nullable | boolean | 否 | 否 | 表示数据库字段是否可以为空。true表示此节点数据可以为空，false表示此节点数据不能为空。 |
| default | string | 否 | 否 | 表示FieldNode的默认值。default需传入type对应类型可解析的字符串字面量，确保内容类型与type字段类型一致。 |
| type | number | 否 | 否 | 表示指定节点对应的数据类型，取值为[ValueType](js-apis-distributedkvstore.md#valuetype)对应的枚举值。暂不支持BYTE\_ARRAY，使用此类型会导致[getKVStore](js-apis-distributedkvstore.md#getkvstore)失败。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor(name: string)

用于创建带有string字段FieldNode实例的构造函数。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | FieldNode的值，不能为空，且不大于64个字符。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |

### appendChild

PhonePC/2in1TabletTVWearable

appendChild(child: FieldNode): boolean

在当前 FieldNode 中添加一个子节点。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| child | [FieldNode](js-apis-distributedkvstore.md#fieldnode) | 是 | 要附加的域节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示子节点成功添加到FieldNode；返回false则表示操作失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. try {
2. let node: distributedKVStore.FieldNode | null = new distributedKVStore.FieldNode("root");
3. let child1: distributedKVStore.FieldNode | null = new distributedKVStore.FieldNode("child1");
4. let child2: distributedKVStore.FieldNode | null = new distributedKVStore.FieldNode("child2");
5. let child3: distributedKVStore.FieldNode | null = new distributedKVStore.FieldNode("child3");
6. node.appendChild(child1);
7. node.appendChild(child2);
8. node.appendChild(child3);
9. console.info("appendNode " + JSON.stringify(node));
10. child1 = null;
11. child2 = null;
12. child3 = null;
13. node = null;
14. } catch (e) {
15. console.error("AppendChild " + e);
16. }
```

## distributedKVStore.createKVManager

PhonePC/2in1TabletTVWearable

createKVManager(config: KVManagerConfig): KVManager

创建一个KVManager对象实例，用于管理数据库对象。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [KVManagerConfig](js-apis-distributedkvstore.md#kvmanagerconfig) | 是 | 提供KVManager实例的配置信息，包括调用方的包名（不能为空）和用户信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [KVManager](js-apis-distributedkvstore.md#kvmanager) | 返回创建的KVManager对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

Stage模型下的示例：

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let kvManager: distributedKVStore.KVManager;
5. let appId: string = 'com.example.datamanagertest';

7. export default class EntryAbility extends UIAbility {
8. onCreate() {
9. console.info("MyAbilityStage onCreate");
10. let context = this.context;
11. const kvManagerConfig: distributedKVStore.KVManagerConfig = {
12. context: context,
13. bundleName: appId
14. }
15. try {
16. kvManager = distributedKVStore.createKVManager(kvManagerConfig);
17. console.info("Succeeded in creating KVManager");
18. } catch (e) {
19. let error = e as BusinessError;
20. console.error(`Failed to create KVManager.code is ${error.code},message is ${error.message}`);
21. }
22. if (kvManager !== undefined) {
23. // 进行后续创建数据库等相关操作
24. // ...
25. }
26. }
27. }
```

FA模型下的示例：

```
1. import { featureAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let kvManager: distributedKVStore.KVManager;
5. let appId: string = 'com.example.datamanagertest';
6. let context = featureAbility.getContext();
7. const kvManagerConfig: distributedKVStore.KVManagerConfig = {
8. context: context,
9. bundleName: appId
10. }
11. try {
12. kvManager = distributedKVStore.createKVManager(kvManagerConfig);
13. console.info("Succeeded in creating KVManager");
14. } catch (e) {
15. let error = e as BusinessError;
16. console.error(`Failed to create KVManager.code is ${error.code},message is ${error.message}`);
17. }
18. if (kvManager !== undefined) {
19. kvManager = kvManager as distributedKVStore.KVManager;
20. // 进行后续创建数据库等相关操作
21. // ...
22. }
```

## KVManager

PhonePC/2in1TabletTVWearable

分布式键值数据库管理实例，用于获取分布式键值数据库的相关信息。在调用KVManager的方法前，需要先通过[createKVManager](js-apis-distributedkvstore.md#distributedkvstorecreatekvmanager)构建一个KVManager实例。

### getKVStore

PhonePC/2in1TabletTVWearable

getKVStore<T>(storeId: string, options: Options, callback: AsyncCallback<T>): void

通过指定options和storeId，创建并获取分布式键值数据库，使用callback异步回调。

注意：

在获取已有的分布式键值数据库时，如果数据库文件无法打开（例如文件头损坏），将触发自动重建逻辑，并返回新创建的分布式键值数据库实例。建议对重要且无法重新生成的数据使用备份恢复功能，以防止数据丢失。有关备份恢复的使用方法，请参阅[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| storeId | string | 是 | 数据库唯一标识符，长度不大于[MAX\_STORE\_ID\_LENGTH](js-apis-distributedkvstore.md#constants)，且只能包含字母数字或下划线\_。 |
| options | [Options](js-apis-distributedkvstore.md#options) | 是 | 创建分布式键值实例的配置信息。 |
| callback | AsyncCallback<T> | 是 | 回调函数。返回创建的分布式键值数据库实例（根据kvStoreType的不同，可以创建SingleKVStore实例和DeviceKVStore实例）。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100002 | Open existed database with changed options. |
| 15100003 | Database corrupted. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let kvStore: distributedKVStore.SingleKVStore | null = null;
4. try {
5. const options: distributedKVStore.Options = {
6. createIfMissing: true,
7. encrypt: false,
8. backup: false,
9. autoSync: false,
10. kvStoreType: distributedKVStore.KVStoreType.SINGLE_VERSION,
11. securityLevel: distributedKVStore.SecurityLevel.S3
12. };
13. kvManager.getKVStore('storeId', options, (err: BusinessError, store: distributedKVStore.SingleKVStore) => {
14. if (err) {
15. console.error(`Failed to get KVStore.code is ${err.code},message is ${err.message}`);
16. return;
17. }
18. console.info("Succeeded in getting KVStore");
19. kvStore = store;
20. if (kvStore !== null) {
21. // 进行后续相关数据操作，包括数据的增、删、改、查、订阅数据变化等操作
22. // ...
23. }
24. });
25. } catch (e) {
26. let error = e as BusinessError;
27. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
28. }
```

### getKVStore

PhonePC/2in1TabletTVWearable

getKVStore<T>(storeId: string, options: Options): Promise<T>

指定options和storeId，创建并获取分布式键值数据库，使用Promise回调。

注意：

获取已有的分布式键值数据库时，如果数据库文件无法打开（如文件头损坏），将触发自动重建逻辑，并返回新创建的分布式键值数据库实例。建议对重要且无法重新生成的数据使用备份恢复功能，防止数据丢失。备份恢复的使用方法详见[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| storeId | string | 是 | 数据库唯一标识符，长度不大于[MAX\_STORE\_ID\_LENGTH](js-apis-distributedkvstore.md#constants)，且只能包含字母数字或下划线\_。 |
| options | [Options](js-apis-distributedkvstore.md#options) | 是 | 创建分布式键值实例的配置信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<T> | Promise对象。返回创建的分布式键值数据库实例（根据kvStoreType的不同，可以创建SingleKVStore实例和DeviceKVStore实例）。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100002 | Open existed database with changed options. |
| 15100003 | Database corrupted. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let kvStore: distributedKVStore.SingleKVStore | null = null;
4. try {
5. const options: distributedKVStore.Options = {
6. createIfMissing: true,
7. encrypt: false,
8. backup: false,
9. autoSync: false,
10. kvStoreType: distributedKVStore.KVStoreType.SINGLE_VERSION,
11. securityLevel: distributedKVStore.SecurityLevel.S3
12. };
13. kvManager.getKVStore<distributedKVStore.SingleKVStore>('storeId', options).then((store: distributedKVStore.SingleKVStore) => {
14. console.info("Succeeded in getting KVStore");
15. kvStore = store;
16. }).catch((err: BusinessError) => {
17. console.error(`Failed to get KVStore.code is ${err.code},message is ${err.message}`);
18. });
19. } catch (e) {
20. let error = e as BusinessError;
21. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
22. }
```

### closeKVStore

PhonePC/2in1TabletTVWearable

closeKVStore(appId: string, storeId: string, callback: AsyncCallback<void>): void

通过storeId的值关闭指定的分布式键值数据库，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appId | string | 是 | 应用的BundleName，不可为空且长度不大于256字符。 |
| storeId | string | 是 | 要关闭的数据库唯一标识符，长度不大于[MAX\_STORE\_ID\_LENGTH](js-apis-distributedkvstore.md#constants)，且只能包含字母数字或下划线\_。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当要关闭的数据库成功关闭，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let kvStore: distributedKVStore.SingleKVStore | null = null;
4. const options: distributedKVStore.Options = {
5. createIfMissing: true,
6. encrypt: false,
7. backup: false,
8. autoSync: false,
9. kvStoreType: distributedKVStore.KVStoreType.SINGLE_VERSION,
10. schema: undefined,
11. securityLevel: distributedKVStore.SecurityLevel.S3
12. }
13. try {
14. kvManager.getKVStore('storeId', options, async (err: BusinessError, store: distributedKVStore.SingleKVStore | null) => {
15. if (err != undefined) {
16. console.error(`Failed to get KVStore.code is ${err.code},message is ${err.message}`);
17. return;
18. }
19. console.info('Succeeded in getting KVStore');
20. kvStore = store;
21. kvStore = null;
22. store = null;
23. if (kvManager != undefined) {
24. // appId为createKVManager中的appId
25. kvManager.closeKVStore(appId, 'storeId', (err: BusinessError)=> {
26. if (err != undefined) {
27. console.error(`Failed to close KVStore.code is ${err.code},message is ${err.message}`);
28. return;
29. }
30. console.info('Succeeded in closing KVStore');
31. });
32. }
33. });
34. } catch (e) {
35. let error = e as BusinessError;
36. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
37. }
```

### closeKVStore

PhonePC/2in1TabletTVWearable

closeKVStore(appId: string, storeId: string): Promise<void>

通过storeId的值关闭指定的分布式键值数据库，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appId | string | 是 | 应用的BundleName，不可为空且长度不大于256字符。 |
| storeId | string | 是 | 要关闭的数据库唯一标识符，长度不大于[MAX\_STORE\_ID\_LENGTH](js-apis-distributedkvstore.md#constants)，且只能包含字母数字或下划线\_。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let kvStore: distributedKVStore.SingleKVStore | null = null;

5. const options: distributedKVStore.Options = {
6. createIfMissing: true,
7. encrypt: false,
8. backup: false,
9. autoSync: false,
10. kvStoreType: distributedKVStore.KVStoreType.SINGLE_VERSION,
11. schema: undefined,
12. securityLevel: distributedKVStore.SecurityLevel.S3
13. }
14. try {
15. kvManager.getKVStore<distributedKVStore.SingleKVStore>('storeId', options).then(async (store: distributedKVStore.SingleKVStore | null) => {
16. console.info('Succeeded in getting KVStore');
17. kvStore = store;
18. kvStore = null;
19. store = null;
20. if (kvManager != undefined) {
21. // appId为createKVManager中的appId
22. kvManager.closeKVStore(appId, 'storeId').then(() => {
23. console.info('Succeeded in closing KVStore');
24. }).catch((err: BusinessError) => {
25. console.error(`Failed to close KVStore.code is ${err.code},message is ${err.message}`);
26. });
27. }
28. }).catch((err: BusinessError) => {
29. console.error(`Failed to get KVStore.code is ${err.code},message is ${err.message}`);
30. });
31. } catch (e) {
32. let error = e as BusinessError;
33. console.error(`Failed to close KVStore.code is ${error.code},message is ${error.message}`);
34. }
```

### deleteKVStore

PhonePC/2in1TabletTVWearable

deleteKVStore(appId: string, storeId: string, callback: AsyncCallback<void>): void

通过storeId的值删除指定的分布式键值数据库，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appId | string | 是 | 应用的BundleName，不可为空且长度不大于256字符。 |
| storeId | string | 是 | 要删除的数据库唯一标识符，长度不大于[MAX\_STORE\_ID\_LENGTH](js-apis-distributedkvstore.md#constants)，且只能包含字母数字或下划线\_。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当要删除的数据库成功删除，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |
| 15100004 | Not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let kvStore: distributedKVStore.SingleKVStore | null = null;

5. const options: distributedKVStore.Options = {
6. createIfMissing: true,
7. encrypt: false,
8. backup: false,
9. autoSync: false,
10. kvStoreType: distributedKVStore.KVStoreType.SINGLE_VERSION,
11. schema: undefined,
12. securityLevel: distributedKVStore.SecurityLevel.S3
13. }
14. try {
15. kvManager.getKVStore('storeId', options, async (err: BusinessError, store: distributedKVStore.SingleKVStore | null) => {
16. if (err != undefined) {
17. console.error(`Failed to get KVStore.code is ${err.code},message is ${err.message}`);
18. return;
19. }
20. console.info('Succeeded in getting KVStore');
21. kvStore = store;
22. kvStore = null;
23. store = null;
24. if (kvManager != undefined) {
25. // appId为createKVManager中的appId
26. kvManager.deleteKVStore(appId, 'storeId', (err: BusinessError) => {
27. if (err != undefined) {
28. console.error(`Failed to delete KVStore.code is ${err.code},message is ${err.message}`);
29. return;
30. }
31. console.info(`Succeeded in deleting KVStore`);
32. });
33. }
34. });
35. } catch (e) {
36. let error = e as BusinessError;
37. console.error(`Failed to delete KVStore.code is ${error.code},message is ${error.message}`);
38. }
```

### deleteKVStore

PhonePC/2in1TabletTVWearable

deleteKVStore(appId: string, storeId: string): Promise<void>

通过storeId的值删除指定的分布式键值数据库，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appId | string | 是 | 应用的BundleName，不可为空且长度不大于256字符。 |
| storeId | string | 是 | 要删除的数据库唯一标识符，长度不大于[MAX\_STORE\_ID\_LENGTH](js-apis-distributedkvstore.md#constants)，且只能包含字母数字或下划线\_。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |
| 15100004 | Not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let kvStore: distributedKVStore.SingleKVStore | null = null;

5. const options: distributedKVStore.Options = {
6. createIfMissing: true,
7. encrypt: false,
8. backup: false,
9. autoSync: false,
10. kvStoreType: distributedKVStore.KVStoreType.SINGLE_VERSION,
11. schema: undefined,
12. securityLevel: distributedKVStore.SecurityLevel.S3
13. }
14. try {
15. kvManager.getKVStore<distributedKVStore.SingleKVStore>('storeId', options).then(async (store: distributedKVStore.SingleKVStore | null) => {
16. console.info('Succeeded in getting KVStore');
17. kvStore = store;
18. kvStore = null;
19. store = null;
20. if (kvManager != undefined) {
21. // appId为createKVManager中的appId
22. kvManager.deleteKVStore(appId, 'storeId').then(() => {
23. console.info('Succeeded in deleting KVStore');
24. }).catch((err: BusinessError) => {
25. console.error(`Failed to delete KVStore.code is ${err.code},message is ${err.message}`);
26. });
27. }
28. }).catch((err: BusinessError) => {
29. console.error(`Failed to get KVStore.code is ${err.code},message is ${err.message}`);
30. });
31. } catch (e) {
32. let error = e as BusinessError;
33. console.error(`Failed to delete KVStore.code is ${error.code},message is ${error.message}`);
34. }
```

### getAllKVStoreId

PhonePC/2in1TabletTVWearable

getAllKVStoreId(appId: string, callback: AsyncCallback<string[]>): void

获取所有通过[getKVStore](js-apis-distributedkvstore.md#getkvstore)方法创建的且没有调用[deleteKVStore](js-apis-distributedkvstore.md#deletekvstore)方法删除的分布式键值数据库的storeId，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appId | string | 是 | 应用的BundleName，不可为空且长度不大于256字符。 |
| callback | AsyncCallback<string[]> | 是 | 回调函数。返回所有创建的分布式键值数据库的storeId。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. // appId为createKVManager中的appId
5. kvManager.getAllKVStoreId(appId, (err: BusinessError, data: string[]) => {
6. if (err != undefined) {
7. console.error(`Failed to get AllKVStoreId.code is ${err.code},message is ${err.message}`);
8. return;
9. }
10. console.info('Succeeded in getting AllKVStoreId');
11. console.info(`GetAllKVStoreId size = ${data.length}`);
12. });
13. } catch (e) {
14. let error = e as BusinessError;
15. console.error(`Failed to get AllKVStoreId.code is ${error.code},message is ${error.message}`);
16. }
```

### getAllKVStoreId

PhonePC/2in1TabletTVWearable

getAllKVStoreId(appId: string): Promise<string[]>

获取所有通过[getKVStore](js-apis-distributedkvstore.md#getkvstore)方法创建的且没有调用[deleteKVStore](js-apis-distributedkvstore.md#deletekvstore)方法删除的分布式键值数据库的storeId，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appId | string | 是 | 应用的BundleName，不可为空且长度不大于256字符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string[]> | Promise对象。返回所有创建的分布式键值数据库的storeId。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. // appId为createKVManager中的appId
5. console.info('GetAllKVStoreId');
6. kvManager.getAllKVStoreId(appId).then((data: string[]) => {
7. console.info('Succeeded in getting AllKVStoreId');
8. console.info(`GetAllKVStoreId size = ${data.length}`);
9. }).catch((err: BusinessError) => {
10. console.error(`Failed to get AllKVStoreId.code is ${err.code},message is ${err.message}`);
11. });
12. } catch (e) {
13. let error = e as BusinessError;
14. console.error(`Failed to get AllKVStoreId.code is ${error.code},message is ${error.message}`);
15. }
```

### on('distributedDataServiceDie')

PhonePC/2in1TabletTVWearable

on(event: 'distributedDataServiceDie', deathCallback: Callback<void>): void

订阅服务状态变更通知。如果服务终止，需要重新注册数据变更通知和端端同步完成事件回调通知，并且端端同步操作会返回失败。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 订阅的事件名，固定为'distributedDataServiceDie'，即服务状态变更事件。 |
| deathCallback | Callback<void> | 是 | 回调函数。订阅成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. console.info('KVManagerOn');
5. const deathCallback = () => {
6. console.info('death callback call');
7. }
8. kvManager.on('distributedDataServiceDie', deathCallback);
9. } catch (e) {
10. let error = e as BusinessError;
11. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
12. }
```

### off('distributedDataServiceDie')

PhonePC/2in1TabletTVWearable

off(event: 'distributedDataServiceDie', deathCallback?: Callback<void>): void

取消订阅服务状态变更通知。参数中的deathCallback必须是已经订阅过的deathCallback，否则会取消订阅失败。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取消订阅的事件名，固定为'distributedDataServiceDie'，即服务状态变更事件。 |
| deathCallback | Callback<void> | 否 | 回调函数。如果该参数不填，那么会将之前订阅过的所有的deathCallback取消订阅。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. console.info('KVManagerOff');
5. const deathCallback = () => {
6. console.info('death callback call');
7. }
8. kvManager.off('distributedDataServiceDie', deathCallback);
9. } catch (e) {
10. let error = e as BusinessError;
11. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
12. }
```

## KVStoreResultSet

PhonePC/2in1TabletTVWearable

提供获取数据库结果集的相关方法，包括查询和移动数据读取位置等。同时允许打开的结果集的最大数量为8个。

KVStoreResultSet实例不会实时刷新。使用结果集后，如果数据库中的数据发生变化（如增删改操作），需要重新查询才能获取到最新的数据。

在调用KVStoreResultSet的方法前，需要先通过[getKVStore](js-apis-distributedkvstore.md#getkvstore)构建一个SingleKVStore或者DeviceKVStore实例。

说明

KVStoreResultSet的游标起始位置为-1。

### getCount

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
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let resultSet: distributedKVStore.KVStoreResultSet;
5. let count: number;
6. kvStore.getResultSet('batch_test_string_key').then((result: distributedKVStore.KVStoreResultSet) => {
7. console.info('getResultSet succeed.');
8. resultSet = result;
9. count = resultSet.getCount();
10. console.info("getCount succeed:" + count);
11. }).catch((err: BusinessError) => {
12. console.error('getResultSet failed: ' + err);
13. });
14. } catch (e) {
15. console.error("getCount failed: " + e);
16. }
```

### getPosition

PhonePC/2in1TabletTVWearable

getPosition(): number

获取结果集中当前的读取位置。读取位置会因[moveToFirst](js-apis-distributedkvstore.md#movetofirst)、[moveToLast](js-apis-distributedkvstore.md#movetolast)等操作而发生变化。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回当前读取位置。取值范围>= -1，值为 -1 时表示还未开始读取，值为 0 时表示第一行。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let resultSet: distributedKVStore.KVStoreResultSet;
5. let position: number;
6. kvStore.getResultSet('batch_test_string_key').then((result: distributedKVStore.KVStoreResultSet) => {
7. console.info('getResultSet succeeded.');
8. resultSet = result;
9. position = resultSet.getPosition();
10. console.info("getPosition succeed:" + position);
11. }).catch((err: BusinessError) => {
12. console.error('getResultSet failed: ' + err);
13. });
14. } catch (e) {
15. console.error("getPosition failed: " + e);
16. }
```

### moveToFirst

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
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let resultSet: distributedKVStore.KVStoreResultSet;
5. let moved: boolean;
6. kvStore.getResultSet('batch_test_string_key').then((result: distributedKVStore.KVStoreResultSet) => {
7. console.info('getResultSet succeed.');
8. resultSet = result;
9. moved = resultSet.moveToFirst();
10. console.info("moveToFirst succeed: " + moved);
11. }).catch((err: BusinessError) => {
12. console.error('getResultSet failed: ' + err);
13. });
14. } catch (e) {
15. console.error("moveToFirst failed " + e);
16. }
```

### moveToLast

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
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let resultSet: distributedKVStore.KVStoreResultSet;
5. let moved: boolean;
6. kvStore.getResultSet('batch_test_string_key').then((result: distributedKVStore.KVStoreResultSet) => {
7. console.info('getResultSet succeed.');
8. resultSet = result;
9. moved = resultSet.moveToLast();
10. console.info("moveToLast succeed:" + moved);
11. }).catch((err: BusinessError) => {
12. console.error('getResultSet failed: ' + err);
13. });
14. } catch (e) {
15. console.error("moveToLast failed: " + e);
16. }
```

### moveToNext

PhonePC/2in1TabletTVWearable

moveToNext(): boolean

将读取位置移动到下一行。如果结果集为空，则返回false。适用于全量获取数据库结果集的场景。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示操作成功；返回false则表示操作失败。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let resultSet: distributedKVStore.KVStoreResultSet;
5. let moved: boolean;
6. kvStore.getResultSet('batch_test_string_key').then((result: distributedKVStore.KVStoreResultSet) => {
7. console.info('getResultSet succeed.');
8. resultSet = result;
9. do {
10. moved = resultSet.moveToNext();
11. console.info("moveToNext succeed: " + moved);
12. } while (moved)
13. }).catch((err: BusinessError) => {
14. console.error('getResultSet failed: ' + err);
15. });
16. } catch (e) {
17. console.error("moveToNext failed: " + e);
18. }
```

### moveToPrevious

PhonePC/2in1TabletTVWearable

moveToPrevious(): boolean

将读取位置移动到上一行。如果结果集为空，则返回false。适用于全量获取数据库结果集的场景。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示操作成功；返回false则表示操作失败。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let resultSet: distributedKVStore.KVStoreResultSet;
5. let moved: boolean;
6. kvStore.getResultSet('batch_test_string_key').then((result: distributedKVStore.KVStoreResultSet) => {
7. console.info('getResultSet succeed.');
8. resultSet = result;
9. moved = resultSet.moveToLast();
10. moved = resultSet.moveToPrevious();
11. console.info("moveToPrevious succeed:" + moved);
12. }).catch((err: BusinessError) => {
13. console.error('getResultSet failed: ' + err);
14. });
15. } catch (e) {
16. console.error("moveToPrevious failed: " + e);
17. }
```

### move

PhonePC/2in1TabletTVWearable

move(offset: number): boolean

将读取位置移动到当前位置的相对偏移量。即当前游标位置向下偏移 offset 行。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 是 | 表示与当前位置的相对偏移量，正偏移表示向前移动，负偏移表示向后移动。当游标超出结果集最前或者最后的位置时，接口返回false。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示操作成功；返回false则表示操作失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let resultSet: distributedKVStore.KVStoreResultSet;
5. let moved: boolean;
6. kvStore.getResultSet('batch_test_string_key').then((result: distributedKVStore.KVStoreResultSet) => {
7. console.info('Succeeded in getting resultSet');
8. resultSet = result;
9. moved = resultSet.move(2); // 若当前位置为0，将读取位置从绝对位置为0的位置移动2行，即移动到绝对位置为2，行数为3的位置
10. console.info(`Succeeded in moving.moved = ${moved}`);
11. }).catch((err: BusinessError) => {
12. console.error(`Failed to get resultSet.code is ${err.code},message is ${err.message}`);
13. });
14. } catch (e) {
15. let error = e as BusinessError;
16. console.error(`Failed to move.code is ${error.code},message is ${error.message}`);
17. }
```

### moveToPosition

PhonePC/2in1TabletTVWearable

moveToPosition(position: number): boolean

将读取位置从 0 移动到绝对位置。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| position | number | 是 | 表示绝对位置。当绝对位置超出结果集最前或者最后的位置时，接口返回false。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示操作成功；返回false则表示操作失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let resultSet: distributedKVStore.KVStoreResultSet;
5. let moved: boolean;
6. kvStore.getResultSet('batch_test_string_key').then((result: distributedKVStore.KVStoreResultSet) => {
7. console.info('Succeeded in getting resultSet');
8. resultSet = result;
9. moved = resultSet.moveToPosition(1);
10. console.info(`Succeeded in moving to position.moved=${moved}`);
11. }).catch((err: BusinessError) => {
12. console.error(`Failed to get resultSet.code is ${err.code},message is ${err.message}`);
13. });
14. } catch (e) {
15. let error = e as BusinessError;
16. console.error(`Failed to move to position.code is ${error.code},message is ${error.message}`);
17. }
```

### isFirst

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
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let resultSet: distributedKVStore.KVStoreResultSet;
5. let isFirst: boolean;
6. kvStore.getResultSet('batch_test_string_key').then((result: distributedKVStore.KVStoreResultSet) => {
7. console.info('getResultSet succeed.');
8. resultSet = result;
9. isFirst = resultSet.isFirst();
10. console.info("Check isFirst succeed:" + isFirst);
11. }).catch((err: BusinessError) => {
12. console.error('getResultSet failed: ' + err);
13. });
14. } catch (e) {
15. console.error("Check isFirst failed: " + e);
16. }
```

### isLast

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
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let resultSet: distributedKVStore.KVStoreResultSet;
5. let isLast: boolean;
6. kvStore.getResultSet('batch_test_string_key').then((result: distributedKVStore.KVStoreResultSet) => {
7. console.info('getResultSet succeed.');
8. resultSet = result;
9. isLast = resultSet.isLast();
10. console.info("Check isLast succeed: " + isLast);
11. }).catch((err: BusinessError) => {
12. console.error('getResultSet failed: ' + err);
13. });
14. } catch (e) {
15. console.error("Check isLast failed: " + e);
16. }
```

### isBeforeFirst

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
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let resultSet: distributedKVStore.KVStoreResultSet;
5. kvStore.getResultSet('batch_test_string_key').then((result: distributedKVStore.KVStoreResultSet) => {
6. console.info('getResultSet succeed.');
7. resultSet = result;
8. let isBeforeFirst = resultSet.isBeforeFirst();
9. console.info("Check isBeforeFirst succeed: " + isBeforeFirst);
10. }).catch((err: BusinessError) => {
11. console.error('getResultSet failed: ' + err);
12. });
13. } catch (e) {
14. console.error("Check isBeforeFirst failed: " + e);
15. }
```

### isAfterLast

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
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let resultSet: distributedKVStore.KVStoreResultSet;
5. kvStore.getResultSet('batch_test_string_key').then((result: distributedKVStore.KVStoreResultSet) => {
6. console.info('getResultSet succeed.');
7. resultSet = result;
8. let isAfterLast = resultSet.isAfterLast();
9. console.info("Check isAfterLast succeed:" + isAfterLast);
10. }).catch((err: BusinessError) => {
11. console.error('getResultSet failed: ' + err);
12. });
13. } catch (e) {
14. console.error("Check isAfterLast failed: " + e);
15. }
```

### getEntry

PhonePC/2in1TabletTVWearable

getEntry(): Entry

从当前位置获取对应的键值对。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Entry](js-apis-distributedkvstore.md#entry) | 返回键值对。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let resultSet: distributedKVStore.KVStoreResultSet;
5. kvStore.getResultSet('batch_test_string_key').then((result: distributedKVStore.KVStoreResultSet) => {
6. console.info('getResultSet succeed.');
7. resultSet = result;
8. let entry = resultSet.getEntry();
9. console.info("getEntry succeed:" + JSON.stringify(entry));
10. }).catch((err: BusinessError) => {
11. console.error('getResultSet failed: ' + err);
12. });
13. } catch (e) {
14. console.error("getEntry failed: " + e);
15. }
```

## Query

PhonePC/2in1TabletTVWearable

使用谓词表示数据库查询，提供创建Query实例、查询数据库中的数据和添加谓词的方法。一个Query对象中谓词数量上限为256个。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

### constructor

PhonePC/2in1TabletTVWearable

constructor()

用于创建Query实例的构造函数。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

### reset

PhonePC/2in1TabletTVWearable

reset(): Query

重置Query对象。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributedkvstore.md#query) | 返回重置的Query对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let query: distributedKVStore.Query | null = new distributedKVStore.Query();
5. if (query != null) {
6. query.equalTo("key", "value");
7. console.info("query is " + query.getSqlLike());
8. query.reset();
9. console.info("query is " + query.getSqlLike());
10. }
11. query = null;
12. } catch (e) {
13. console.error("simply calls should be ok :" + e);
14. }
```

### equalTo

PhonePC/2in1TabletTVWearable

equalTo(field: string, value: number|string|boolean): Query

构造一个Query对象来查询具有指定字段的条目，其值等于指定的值。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

说明

使用equalTo时需要结合[Schema](js-apis-distributedkvstore.md#schema)使用。

使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../harmonyos-guides/data-persistence-by-kv-store.md#开发步骤)中使用getKVStore()方法创建并获取键值数据库示例。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含'^'。包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |
| value | number|string|boolean | 是 | 表示指定的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributedkvstore.md#query) | 返回Query对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let query: distributedKVStore.Query | null = new distributedKVStore.Query();
5. if (query != null) {
6. query.equalTo("field", "value");
7. console.info(`query is ${query.getSqlLike()}`);
8. }
9. query = null;
10. } catch (e) {
11. let error = e as BusinessError;
12. console.error(`duplicated calls should be ok.code is ${error.code},message is ${error.message}`);
13. }
```

### notEqualTo

PhonePC/2in1TabletTVWearable

notEqualTo(field: string, value: number|string|boolean): Query

构造一个Query对象以查询具有指定字段且值不等于指定值的条目。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

说明

使用notEqualTo时需要结合[Schema](js-apis-distributedkvstore.md#schema)使用。

使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../harmonyos-guides/data-persistence-by-kv-store.md#开发步骤)中使用getKVStore()方法创建并获取键值数据库示例。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含'^'。包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |
| value | number|string|boolean | 是 | 表示指定的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributedkvstore.md#query) | 返回Query对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let query: distributedKVStore.Query | null = new distributedKVStore.Query();
5. if (query != null) {
6. query.notEqualTo("field", "value");
7. console.info(`query is ${query.getSqlLike()}`);
8. }
9. query = null;
10. } catch (e) {
11. let error = e as BusinessError;
12. console.error(`duplicated calls should be ok.code is ${error.code},message is ${error.message}`);
13. }
```

### greaterThan

PhonePC/2in1TabletTVWearable

greaterThan(field: string, value: number|string|boolean): Query

构造一个Query对象以查询具有大于指定值的指定字段的条目。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

说明

使用greaterThan时需要结合[Schema](js-apis-distributedkvstore.md#schema)使用。

使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../harmonyos-guides/data-persistence-by-kv-store.md#开发步骤)中使用getKVStore()方法创建并获取键值数据库示例。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含'^'。包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |
| value | number|string|boolean | 是 | 表示指定的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributedkvstore.md#query) | 返回Query对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let query: distributedKVStore.Query | null = new distributedKVStore.Query();
5. if (query != null) {
6. query.greaterThan("field", "value");
7. console.info(`query is ${query.getSqlLike()}`);
8. }
9. query = null;
10. } catch (e) {
11. let error = e as BusinessError;
12. console.error(`duplicated calls should be ok.code is ${error.code},message is ${error.message}`);
13. }
```

### lessThan

PhonePC/2in1TabletTVWearable

lessThan(field: string, value: number|string): Query

构造一个Query对象以查询具有小于指定值的指定字段的条目。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

说明

使用lessThan时需要结合[Schema](js-apis-distributedkvstore.md#schema)使用。

使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../harmonyos-guides/data-persistence-by-kv-store.md#开发步骤)中使用getKVStore()方法创建并获取键值数据库示例。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含'^'。包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |
| value | number|string | 是 | 表示指定的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributedkvstore.md#query) | 返回Query对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let query: distributedKVStore.Query | null = new distributedKVStore.Query();
5. if (query != null) {
6. query.lessThan("field", "value");
7. console.info(`query is ${query.getSqlLike()}`);
8. }
9. query = null;
10. } catch (e) {
11. let error = e as BusinessError;
12. console.error(`duplicated calls should be ok.code is ${error.code},message is ${error.message}`);
13. }
```

### greaterThanOrEqualTo

PhonePC/2in1TabletTVWearable

greaterThanOrEqualTo(field: string, value: number|string): Query

构造一个Query对象以查询具有指定字段且值大于或等于指定值的条目。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

说明

使用greaterThanOrEqualTo时需要结合[Schema](js-apis-distributedkvstore.md#schema)使用。

使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../harmonyos-guides/data-persistence-by-kv-store.md#开发步骤)中使用getKVStore()方法创建并获取键值数据库示例。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含'^'。包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |
| value | number|string | 是 | 表示指定的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributedkvstore.md#query) | 返回Query对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let query: distributedKVStore.Query | null = new distributedKVStore.Query();
5. if (query != null) {
6. query.greaterThanOrEqualTo("field", "value");
7. console.info(`query is ${query.getSqlLike()}`);
8. }
9. query = null;
10. } catch (e) {
11. let error = e as BusinessError;
12. console.error(`duplicated calls should be ok.code is ${error.code},message is ${error.message}`);
13. }
```

### lessThanOrEqualTo

PhonePC/2in1TabletTVWearable

lessThanOrEqualTo(field: string, value: number|string): Query

构造一个Query对象以查询具有指定字段且值小于或等于指定值的条目。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

说明

使用lessThanOrEqualTo时需要结合[Schema](js-apis-distributedkvstore.md#schema)使用。

使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../harmonyos-guides/data-persistence-by-kv-store.md#开发步骤)中使用getKVStore()方法创建并获取键值数据库示例。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含'^'。包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |
| value | number|string | 是 | 表示指定的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributedkvstore.md#query) | 返回Query对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let query: distributedKVStore.Query | null = new distributedKVStore.Query();
5. if (query != null) {
6. query.lessThanOrEqualTo("field", "value");
7. console.info(`query is ${query.getSqlLike()}`);
8. }
9. query = null;
10. } catch (e) {
11. let error = e as BusinessError;
12. console.error(`duplicated calls should be ok.code is ${error.code},message is ${error.message}`);
13. }
```

### isNull

PhonePC/2in1TabletTVWearable

isNull(field: string): Query

构造一个Query对象以查询具有值为null的指定字段的条目。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

说明

使用isNull时需要结合[Schema](js-apis-distributedkvstore.md#schema)使用。

使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../harmonyos-guides/data-persistence-by-kv-store.md#开发步骤)中使用getKVStore()方法创建并获取键值数据库示例。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含'^'。包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributedkvstore.md#query) | 返回Query对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let query: distributedKVStore.Query | null = new distributedKVStore.Query();
5. if (query != null) {
6. query.isNull("field");
7. console.info(`query is ${query.getSqlLike()}`);
8. }
9. query = null;
10. } catch (e) {
11. let error = e as BusinessError;
12. console.error(`duplicated calls should be ok.code is ${error.code},message is ${error.message}`);
13. }
```

### inNumber

PhonePC/2in1TabletTVWearable

inNumber(field: string, valueList: number[]): Query

构造一个Query对象以查询具有指定字段的条目，其值在指定的值列表中。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

说明

使用inNumber时需要结合[Schema](js-apis-distributedkvstore.md#schema)使用。

使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../harmonyos-guides/data-persistence-by-kv-store.md#开发步骤)中使用getKVStore()方法创建并获取键值数据库示例。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含'^'。包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |
| valueList | number[] | 是 | 表示指定的值列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributedkvstore.md#query) | 返回Query对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let query: distributedKVStore.Query | null = new distributedKVStore.Query();
5. if (query != null) {
6. query.inNumber("field", [0, 1]);
7. console.info(`query is ${query.getSqlLike()}`);
8. }
9. query = null;
10. } catch (e) {
11. let error = e as BusinessError;
12. console.error(`duplicated calls should be ok.code is ${error.code},message is ${error.message}`);
13. }
```

### inString

PhonePC/2in1TabletTVWearable

inString(field: string, valueList: string[]): Query

构造一个Query对象以查询具有指定字段的条目，其值在指定的字符串值列表中。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

说明

使用inString时需要结合[Schema](js-apis-distributedkvstore.md#schema)使用。

使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../harmonyos-guides/data-persistence-by-kv-store.md#开发步骤)中使用getKVStore()方法创建并获取键值数据库示例。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含'^'。包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |
| valueList | string[] | 是 | 表示指定的字符串值列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributedkvstore.md#query) | 返回Query对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let query: distributedKVStore.Query | null = new distributedKVStore.Query();
5. if (query != null) {
6. query.inString("field", ['test1', 'test2']);
7. console.info(`query is ${query.getSqlLike()}`);
8. }
9. query = null;
10. } catch (e) {
11. let error = e as BusinessError;
12. console.error(`duplicated calls should be ok.code is ${error.code},message is ${error.message}`);
13. }
```

### notInNumber

PhonePC/2in1TabletTVWearable

notInNumber(field: string, valueList: number[]): Query

构造一个Query对象以查询具有指定字段的条目，该字段的值不在指定的值列表中。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

说明

使用notInNumber时需要结合[Schema](js-apis-distributedkvstore.md#schema)使用。

使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../harmonyos-guides/data-persistence-by-kv-store.md#开发步骤)中使用getKVStore()方法创建并获取键值数据库示例。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含'^'。包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |
| valueList | number[] | 是 | 表示指定的值列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributedkvstore.md#query) | 返回Query对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let query: distributedKVStore.Query | null = new distributedKVStore.Query();
5. if (query != null) {
6. query.notInNumber("field", [0, 1]);
7. console.info(`query is ${query.getSqlLike()}`);
8. }
9. query = null;
10. } catch (e) {
11. let error = e as BusinessError;
12. console.error(`duplicated calls should be ok.code is ${error.code},message is ${error.message}`);
13. }
```

### notInString

PhonePC/2in1TabletTVWearable

notInString(field: string, valueList: string[]): Query

构造一个Query对象以查询具有指定字段且值不在指定字符串值列表中的条目。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

说明

使用notInString时需要结合[Schema](js-apis-distributedkvstore.md#schema)使用。

使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../harmonyos-guides/data-persistence-by-kv-store.md#开发步骤)中使用getKVStore()方法创建并获取键值数据库示例。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含'^'。包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |
| valueList | string[] | 是 | 表示指定的字符串值列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributedkvstore.md#query) | 返回Query对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let query: distributedKVStore.Query | null = new distributedKVStore.Query();
5. if (query != null) {
6. query.notInString("field", ['test1', 'test2']);
7. console.info(`query is ${query.getSqlLike()}`);
8. }
9. query = null;
10. } catch (e) {
11. let error = e as BusinessError;
12. console.error(`duplicated calls should be ok.code is ${error.code},message is ${error.message}`);
13. }
```

### like

PhonePC/2in1TabletTVWearable

like(field: string, value: string): Query

构造一个Query对象以查询具有与指定字符串值相似的指定字段的条目。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

说明

使用like时需要结合[Schema](js-apis-distributedkvstore.md#schema)使用。

使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../harmonyos-guides/data-persistence-by-kv-store.md#开发步骤)中使用getKVStore()方法创建并获取键值数据库示例。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含'^'。包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |
| value | string | 是 | 表示指定的字符串值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributedkvstore.md#query) | 返回Query对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let query: distributedKVStore.Query | null = new distributedKVStore.Query();
5. if (query != null) {
6. query.like("field", "value");
7. console.info(`query is ${query.getSqlLike()}`);
8. }
9. query = null;
10. } catch (e) {
11. let error = e as BusinessError;
12. console.error(`duplicated calls should be ok.code is ${error.code},message is ${error.message}`);
13. }
```

### unlike

PhonePC/2in1TabletTVWearable

unlike(field: string, value: string): Query

构造一个Query对象以查询具有与指定字符串值不相似的指定字段的条目。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

说明

使用unlike时需要结合[Schema](js-apis-distributedkvstore.md#schema)使用。

使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../harmonyos-guides/data-persistence-by-kv-store.md#开发步骤)中使用getKVStore()方法创建并获取键值数据库示例。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含'^'。包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |
| value | string | 是 | 表示指定的字符串值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributedkvstore.md#query) | 返回Query对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let query: distributedKVStore.Query | null = new distributedKVStore.Query();
5. if (query != null) {
6. query.unlike("field", "value");
7. console.info(`query is ${query.getSqlLike()}`);
8. }
9. query = null;
10. } catch (e) {
11. let error = e as BusinessError;
12. console.error(`duplicated calls should be ok.code is ${error.code},message is ${error.message}`);
13. }
```

### and

PhonePC/2in1TabletTVWearable

and(): Query

构造一个带有与条件的查询对象。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributedkvstore.md#query) | 返回查询对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let query: distributedKVStore.Query | null = new distributedKVStore.Query();
5. if (query != null) {
6. query.notEqualTo("field", "value1");
7. query.and();
8. query.notEqualTo("field", "value2");
9. console.info("query is " + query.getSqlLike());
10. }
11. query = null;
12. } catch (e) {
13. console.error("duplicated calls should be ok :" + e);
14. }
```

### or

PhonePC/2in1TabletTVWearable

or(): Query

构造一个带有或条件的Query对象。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributedkvstore.md#query) | 返回查询对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let query: distributedKVStore.Query | null = new distributedKVStore.Query();
5. if (query != null) {
6. query.notEqualTo("field", "value1");
7. query.or();
8. query.notEqualTo("field", "value2");
9. console.info("query is " + query.getSqlLike());
10. }
11. query = null;
12. } catch (e) {
13. console.error("duplicated calls should be ok :" + e);
14. }
```

### orderByAsc

PhonePC/2in1TabletTVWearable

orderByAsc(field: string): Query

构造一个Query对象，将查询结果按升序排序。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

说明

使用orderByAsc时需要结合[Schema](js-apis-distributedkvstore.md#schema)使用。

使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../harmonyos-guides/data-persistence-by-kv-store.md#开发步骤)中使用getKVStore()方法创建并获取键值数据库示例。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含'^'。包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributedkvstore.md#query) | 返回Query对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let query: distributedKVStore.Query | null = new distributedKVStore.Query();
5. if (query != null) {
6. query.notEqualTo("field", "value");
7. query.orderByAsc("field");
8. console.info(`query is ${query.getSqlLike()}`);
9. }
10. query = null;
11. } catch (e) {
12. let error = e as BusinessError;
13. console.error(`duplicated calls should be ok.code is ${error.code},message is ${error.message}`);
14. }
```

### orderByDesc

PhonePC/2in1TabletTVWearable

orderByDesc(field: string): Query

构造一个Query对象，将查询结果按降序排序。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

说明

使用orderByDesc时需要结合[Schema](js-apis-distributedkvstore.md#schema)使用。

使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../harmonyos-guides/data-persistence-by-kv-store.md#开发步骤)中使用getKVStore()方法创建并获取键值数据库示例。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含'^'。包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributedkvstore.md#query) | 返回Query对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let query: distributedKVStore.Query | null = new distributedKVStore.Query();
5. if (query != null) {
6. query.notEqualTo("field", "value");
7. query.orderByDesc("field");
8. console.info(`query is ${query.getSqlLike()}`);
9. }
10. query = null;
11. } catch (e) {
12. let error = e as BusinessError;
13. console.error(`duplicated calls should be ok.code is ${error.code},message is ${error.message}`);
14. }
```

### limit

PhonePC/2in1TabletTVWearable

limit(total: number, offset: number): Query

构造一个Query对象来指定结果的数量和开始位置。该接口必须要在Query对象查询和升降序等操作之后调用，调用limit接口后，不可再对Query对象进行查询和升降序等操作。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| total | number | 是 | 表示最大数据记录数，取值应为非负整数。  当total为负数时，表示查询整个结果集。 |
| offset | number | 是 | 指定查询结果的起始位置，取值应为非负整数。  当offset为负数时，表示查询整个结果集。  当offset超出结果集最后位置时，查询结果为空。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributedkvstore.md#query) | 返回Query对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let total = 10;
4. let offset = 1;
5. try {
6. let query: distributedKVStore.Query | null = new distributedKVStore.Query();
7. if (query != null) {
8. query.notEqualTo("field", "value");
9. query.limit(total, offset);
10. console.info(`query is ${query.getSqlLike()}`);
11. }
12. query = null;
13. } catch (e) {
14. let error = e as BusinessError;
15. console.error(`duplicated calls should be ok.code is ${error.code},message is ${error.message}`);
16. }
```

### isNotNull

PhonePC/2in1TabletTVWearable

isNotNull(field: string): Query

构造一个Query对象以查询具有值不为null的指定字段的条目。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

说明

使用isNotNull时需要结合[Schema](js-apis-distributedkvstore.md#schema)使用。

使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../harmonyos-guides/data-persistence-by-kv-store.md#开发步骤)中使用getKVStore()方法创建并获取键值数据库示例。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含'^'。包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributedkvstore.md#query) | 返回Query对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let query: distributedKVStore.Query | null = new distributedKVStore.Query();
5. if (query != null) {
6. query.isNotNull("field");
7. console.info(`query is ${query.getSqlLike()}`);
8. }
9. query = null;
10. } catch (e) {
11. let error = e as BusinessError;
12. console.error(`duplicated calls should be ok.code is ${error.code},message is ${error.message}`);
13. }
```

### beginGroup

PhonePC/2in1TabletTVWearable

beginGroup(): Query

创建一个带有左括号的查询条件组。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributedkvstore.md#query) | 返回Query对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let query: distributedKVStore.Query | null = new distributedKVStore.Query();
5. if (query != null) {
6. query.beginGroup();
7. query.isNotNull("field");
8. query.endGroup();
9. console.info("query is " + query.getSqlLike());
10. }
11. query = null;
12. } catch (e) {
13. console.error("duplicated calls should be ok :" + e);
14. }
```

### endGroup

PhonePC/2in1TabletTVWearable

endGroup(): Query

创建一个带有右括号的查询条件组。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributedkvstore.md#query) | 返回Query对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let query: distributedKVStore.Query | null = new distributedKVStore.Query();
5. if (query != null) {
6. query.beginGroup();
7. query.isNotNull("field");
8. query.endGroup();
9. console.info("query is " + query.getSqlLike());
10. }
11. query = null;
12. } catch (e) {
13. console.error("duplicated calls should be ok :" + e);
14. }
```

### prefixKey

PhonePC/2in1TabletTVWearable

prefixKey(prefix: string): Query

创建具有指定键前缀的查询条件。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| prefix | string | 是 | 表示指定的键前缀，不能包含'^'。包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributedkvstore.md#query) | 返回Query对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let query: distributedKVStore.Query | null = new distributedKVStore.Query();
5. if (query != null) {
6. query.prefixKey("$.name");
7. query.prefixKey("0");
8. console.info(`query is ${query.getSqlLike()}`);
9. }
10. query = null;
11. } catch (e) {
12. let error = e as BusinessError;
13. console.error(`duplicated calls should be ok.code is ${error.code},message is ${error.message}`);
14. }
```

### setSuggestIndex

PhonePC/2in1TabletTVWearable

setSuggestIndex(index: string): Query

设置一个指定的索引，将优先用于查询。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | string | 是 | 指示要设置的索引，不能包含'^'。包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributedkvstore.md#query) | 返回Query对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let query: distributedKVStore.Query | null = new distributedKVStore.Query();
5. if (query != null) {
6. query.setSuggestIndex("$.name");
7. query.setSuggestIndex("0");
8. console.info(`query is ${query.getSqlLike()}`);
9. }
10. query = null;
11. } catch (e) {
12. let error = e as BusinessError;
13. console.error(`duplicated calls should be ok.code is ${error.code},message is ${error.message}`);
14. }
```

### deviceId

PhonePC/2in1TabletTVWearable

deviceId(deviceId:string):Query

添加设备ID作为Key的前缀。

说明

其中deviceId为[DeviceBasicInfo](js-apis-distributeddevicemanager.md#devicebasicinfo)中的networkId，通过调用[deviceManager.getAvailableDeviceListSync](js-apis-distributeddevicemanager.md#getavailabledevicelistsync)方法得到。

deviceId具体获取方式请参考[sync接口示例](js-apis-distributedkvstore.md#sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 指示查询的设备ID，不能为空。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Query](js-apis-distributedkvstore.md#query) | 返回Query对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let query: distributedKVStore.Query | null = new distributedKVStore.Query();
5. if (query != null) {
6. query.deviceId("deviceId");
7. console.info(`query is ${query.getSqlLike()}`);
8. }
9. } catch (e) {
10. let error = e as BusinessError;
11. console.error(`duplicated calls should be ok.code is ${error.code},message is ${error.message}`);
12. }
```

### getSqlLike

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
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let query: distributedKVStore.Query | null = new distributedKVStore.Query();
5. if (query != null) {
6. let sql1 = query.getSqlLike();
7. console.info(`GetSqlLike sql= ${sql1}`);
8. }
9. } catch (e) {
10. console.error("duplicated calls should be ok : " + e);
11. }
```

## SingleKVStore

PhonePC/2in1TabletTVWearable

SingleKVStore数据库实例，提供增加数据、删除数据和订阅数据变更、订阅数据端端同步完成的方法。

在调用SingleKVStore的方法前，需要先通过[getKVStore](js-apis-distributedkvstore.md#getkvstore)构建一个SingleKVStore实例。

### put

PhonePC/2in1TabletTVWearable

put(key: string, value: Uint8Array | string | number | boolean, callback: AsyncCallback<void>): void

添加指定类型键值对到数据库，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要添加数据的Key，不能为空且长度不大于[MAX\_KEY\_LENGTH](js-apis-distributedkvstore.md#constants)。 |
| value | Uint8Array | string | number | boolean | 是 | 要添加数据的value，支持Uint8Array、number 、 string 、boolean，Uint8Array、string 的长度不大于[MAX\_VALUE\_LENGTH](js-apis-distributedkvstore.md#constants)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。数据添加成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const KEY_TEST_STRING_ELEMENT = 'key_test_string';
4. const VALUE_TEST_STRING_ELEMENT = 'value-test-string';
5. try {
6. kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT, (err: BusinessError) => {
7. if (err != undefined) {
8. console.error(`Failed to put.code is ${err.code},message is ${err.message}`);
9. return;
10. }
11. console.info("Succeeded in putting");
12. });
13. } catch (e) {
14. let error = e as BusinessError;
15. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
16. }
```

### put

PhonePC/2in1TabletTVWearable

put(key: string, value: Uint8Array | string | number | boolean): Promise<void>

添加指定类型键值对到数据库，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要添加数据的Key，不能为空且长度不大于[MAX\_KEY\_LENGTH](js-apis-distributedkvstore.md#constants)。 |
| value | Uint8Array | string | number | boolean | 是 | 要添加数据的value，支持Uint8Array、number 、 string 、boolean，Uint8Array、string 的长度不大于[MAX\_VALUE\_LENGTH](js-apis-distributedkvstore.md#constants)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const KEY_TEST_STRING_ELEMENT = 'key_test_string';
4. const VALUE_TEST_STRING_ELEMENT = 'value-test-string';
5. try {
6. kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT).then(() => {
7. console.info(`Succeeded in putting data`);
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to put.code is ${err.code},message is ${err.message}`);
10. });
11. } catch (e) {
12. let error = e as BusinessError;
13. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
14. }
```

### putBatch

PhonePC/2in1TabletTVWearable

putBatch(entries: Entry[], callback: AsyncCallback<void>): void

批量插入键值对到SingleKVStore数据库中，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| entries | [Entry](js-apis-distributedkvstore.md#entry)[] | 是 | 表示要批量插入的键值对。一个entries对象中允许的最大数据量为512M。 |
| callback | AsyncCallback<void> | 是 | 回调函数。数据批量插入成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let entries: distributedKVStore.Entry[] = [];
5. for (let i = 0; i < 10; i++) {
6. let key = 'batch_test_string_key';
7. let entry: distributedKVStore.Entry = {
8. key: key + i,
9. value: {
10. type: distributedKVStore.ValueType.STRING,
11. value: 'batch_test_string_value'
12. }
13. }
14. entries.push(entry);
15. }
16. console.info(`entries: ${entries}`);
17. kvStore.putBatch(entries, async (err: BusinessError) => {
18. if (err != undefined) {
19. console.error(`Failed to put Batch.code is ${err.code},message is ${err.message}`);
20. return;
21. }
22. console.info('Succeeded in putting Batch');
23. if (kvStore != null) {
24. kvStore.getEntries('batch_test_string_key', (err: BusinessError, entries: distributedKVStore.Entry[]) => {
25. if (err != undefined) {
26. console.error(`Failed to get Entries.code is ${err.code},message is ${err.message}`);
27. }
28. console.info('Succeeded in getting Entries');
29. console.info(`entries.length: ${entries.length}`);
30. console.info(`entries[0]: ${entries[0]}`);
31. });
32. } else {
33. console.error('KvStore is null'); // 后续示例代码与此处保持一致
34. }
35. });
36. } catch (e) {
37. let error = e as BusinessError;
38. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message} `);
39. }
```

### putBatch

PhonePC/2in1TabletTVWearable

putBatch(entries: Entry[]): Promise<void>

批量插入键值对到SingleKVStore数据库中，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| entries | [Entry](js-apis-distributedkvstore.md#entry)[] | 是 | 表示要批量插入的键值对。一个entries对象中允许的最大数据量为512M。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let entries: distributedKVStore.Entry[] = [];
5. for (let i = 0; i < 10; i++) {
6. let key = 'batch_test_string_key';
7. let entry: distributedKVStore.Entry = {
8. key: key + i,
9. value: {
10. type: distributedKVStore.ValueType.STRING,
11. value: 'batch_test_string_value'
12. }
13. }
14. entries.push(entry);
15. }
16. console.info(`entries: ${entries}`);
17. kvStore.putBatch(entries).then(async () => {
18. console.info('Succeeded in putting Batch');
19. if (kvStore != null) {
20. kvStore.getEntries('batch_test_string_key').then((entries: distributedKVStore.Entry[]) => {
21. console.info('Succeeded in getting Entries');
22. console.info(`PutBatch ${entries}`);
23. }).catch((err: BusinessError) => {
24. console.error(`Failed to get Entries.code is ${err.code},message is ${err.message}`);
25. });
26. }
27. }).catch((err: BusinessError) => {
28. console.error(`Failed to put Batch.code is ${err.code},message is ${err.message}`);
29. });
30. } catch (e) {
31. let error = e as BusinessError;
32. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message} `);
33. }
```

### delete

PhonePC/2in1TabletTVWearable

delete(key: string, callback: AsyncCallback<void>): void

从数据库中删除指定键值的数据，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要删除数据的Key，不能为空且长度不大于[MAX\_KEY\_LENGTH](js-apis-distributedkvstore.md#constants)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。删除指定的数据成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const KEY_TEST_STRING_ELEMENT = 'key_test_string';
4. const VALUE_TEST_STRING_ELEMENT = 'value-test-string';
5. try {
6. kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT, (err: BusinessError) => {
7. if (err != undefined) {
8. console.error(`Failed to put.code is ${err.code},message is ${err.message}`);
9. return;
10. }
11. console.info('Succeeded in putting');
12. if (kvStore != null) {
13. kvStore.delete(KEY_TEST_STRING_ELEMENT, (err: BusinessError) => {
14. if (err != undefined) {
15. console.error(`Failed to delete.code is ${err.code},message is ${err.message}`);
16. return;
17. }
18. console.info('Succeeded in deleting');
19. });
20. }
21. });
22. } catch (e) {
23. let error = e as BusinessError;
24. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
25. }
```

### delete

PhonePC/2in1TabletTVWearable

delete(key: string): Promise<void>

从数据库中删除指定键值的数据，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要删除数据的Key，不能为空且长度不大于[MAX\_KEY\_LENGTH](js-apis-distributedkvstore.md#constants)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const KEY_TEST_STRING_ELEMENT = 'key_test_string';
4. const VALUE_TEST_STRING_ELEMENT = 'value-test-string';
5. try {
6. kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT).then(() => {
7. console.info(`Succeeded in putting data`);
8. if (kvStore != null) {
9. kvStore.delete(KEY_TEST_STRING_ELEMENT).then(() => {
10. console.info('Succeeded in deleting');
11. }).catch((err: BusinessError) => {
12. console.error(`Failed to delete.code is ${err.code},message is ${err.message}`);
13. });
14. }
15. }).catch((err: BusinessError) => {
16. console.error(`Failed to put.code is ${err.code},message is ${err.message}`);
17. });
18. } catch (e) {
19. let error = e as BusinessError;
20. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
21. }
```

### deleteBatch

PhonePC/2in1TabletTVWearable

deleteBatch(keys: string[], callback: AsyncCallback<void>): void

批量删除SingleKVStore数据库中的键值对，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keys | string[] | 是 | 表示要批量删除的键值对，不能为空。 |
| callback | AsyncCallback<void> | 是 | 回调函数。批量删除指定的数据成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let entries: distributedKVStore.Entry[] = [];
5. let keys: string[] = [];
6. for (let i = 0; i < 5; i++) {
7. let key = 'batch_test_string_key';
8. let entry: distributedKVStore.Entry = {
9. key: key + i,
10. value: {
11. type: distributedKVStore.ValueType.STRING,
12. value: 'batch_test_string_value'
13. }
14. }
15. entries.push(entry);
16. keys.push(key + i);
17. }
18. console.info(`entries: ${entries}`);
19. kvStore.putBatch(entries, async (err: BusinessError) => {
20. if (err != undefined) {
21. console.error(`Failed to put Batch.code is ${err.code},message is ${err.message}`);
22. return;
23. }
24. console.info('Succeeded in putting Batch');
25. if (kvStore != null) {
26. kvStore.deleteBatch(keys, async (err: BusinessError) => {
27. if (err != undefined) {
28. console.error(`Failed to delete Batch.code is ${err.code},message is ${err.message}`);
29. return;
30. }
31. console.info('Succeeded in deleting Batch');
32. });
33. }
34. });
35. } catch (e) {
36. let error = e as BusinessError;
37. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
38. }
```

### deleteBatch

PhonePC/2in1TabletTVWearable

deleteBatch(keys: string[]): Promise<void>

批量删除SingleKVStore数据库中的键值对，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keys | string[] | 是 | 表示要批量删除的键值对，不能为空。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let entries: distributedKVStore.Entry[] = [];
5. let keys: string[] = [];
6. for (let i = 0; i < 5; i++) {
7. let key = 'batch_test_string_key';
8. let entry: distributedKVStore.Entry = {
9. key: key + i,
10. value: {
11. type: distributedKVStore.ValueType.STRING,
12. value: 'batch_test_string_value'
13. }
14. }
15. entries.push(entry);
16. keys.push(key + i);
17. }
18. console.info(`entries: ${entries}`);
19. kvStore.putBatch(entries).then(async () => {
20. console.info('Succeeded in putting Batch');
21. if (kvStore != null) {
22. kvStore.deleteBatch(keys).then(() => {
23. console.info('Succeeded in deleting Batch');
24. }).catch((err: BusinessError) => {
25. console.error(`Failed to delete Batch.code is ${err.code},message is ${err.message}`);
26. });
27. }
28. }).catch((err: BusinessError) => {
29. console.error(`Failed to put Batch.code is ${err.code},message is ${err.message}`);
30. });
31. } catch (e) {
32. let error = e as BusinessError;
33. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
34. }
```

### removeDeviceData

PhonePC/2in1TabletTVWearable

removeDeviceData(deviceId: string, callback: AsyncCallback<void>): void

删除指定设备的数据，使用callback异步回调。

说明

其中deviceId为[DeviceBasicInfo](js-apis-distributeddevicemanager.md#devicebasicinfo)中的networkId，通过调用[deviceManager.getAvailableDeviceListSync](js-apis-distributeddevicemanager.md#getavailabledevicelistsync)方法得到。

deviceId具体获取方式请参考[sync接口示例](js-apis-distributedkvstore.md#sync)

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 设备的networkId。 |
| callback | AsyncCallback<void> | 是 | 回调函数。删除指定设备的数据成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const KEY_TEST_STRING_ELEMENT = 'key_test_string_2';
4. const VALUE_TEST_STRING_ELEMENT = 'value-string-002';
5. try {
6. kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT, async (err: BusinessError) => {
7. if (err) {
8. console.error(`Failed to put device data: ${err.code} - ${err.message}`);
9. return;
10. }
11. console.info('Succeeded in putting data');
12. const deviceid = 'no_exist_device_id';
13. if (kvStore) {
14. kvStore.removeDeviceData(deviceid, async (err: BusinessError) => {
15. if (err) {
16. console.error(`Failed to remove device data: ${err.code} - ${err.message}`);
17. if (kvStore) {
18. kvStore.get(KEY_TEST_STRING_ELEMENT, async (err: BusinessError, data: boolean | string | number | Uint8Array) => {
19. if (err) {
20. console.error(`Failed to get data: ${err.code} - ${err.message}`);
21. return;
22. }
23. console.info(`Succeeded in getting data.data=${data}`);
24. });
25. }
26. } else {
27. console.info('Succeeded in removing device data');
28. }
29. });
30. }
31. });
32. } catch (e) {
33. let error = e as BusinessError;
34. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`)
35. }
```

### removeDeviceData

PhonePC/2in1TabletTVWearable

removeDeviceData(deviceId: string): Promise<void>

删除指定设备的数据，使用Promise异步回调。

说明

其中deviceId为[DeviceBasicInfo](js-apis-distributeddevicemanager.md#devicebasicinfo)中的networkId，通过调用[deviceManager.getAvailableDeviceListSync](js-apis-distributeddevicemanager.md#getavailabledevicelistsync)方法得到。

deviceId具体获取方式请参考[sync接口示例](js-apis-distributedkvstore.md#sync)

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 设备的networkId。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const KEY_TEST_STRING_ELEMENT = 'key_test_string_2';
4. const VALUE_TEST_STRING_ELEMENT = 'value-string-001';
5. try {
6. kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT).then(() => {
7. console.info('Succeeded in putting data');
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to put data.code is ${err.code},message is ${err.message} `);
10. });
11. const deviceid = 'no_exist_device_id';
12. kvStore.removeDeviceData(deviceid).then(() => {
13. console.info('succeeded in removing device data');
14. }).catch((err: BusinessError) => {
15. console.error(`Failed to remove device data.code is ${err.code},message is ${err.message} `);
16. });
17. kvStore.get(KEY_TEST_STRING_ELEMENT).then((data: boolean | string | number | Uint8Array) => {
18. console.info(`Succeeded in getting data. Data=${data}`);
19. }).catch((err: BusinessError) => {
20. console.error(`Failed to get data.code is ${err.code},message is ${err.message} `);
21. });
22. } catch (e) {
23. let error = e as BusinessError;
24. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`)
25. }
```

### get

PhonePC/2in1TabletTVWearable

get(key: string, callback: AsyncCallback<boolean | string | number | Uint8Array>): void

获取指定键的值，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要查询数据的Key，不能为空且长度不大于[MAX\_KEY\_LENGTH](js-apis-distributedkvstore.md#constants)。 |
| callback | AsyncCallback<boolean | string | number | Uint8Array> | 是 | 回调函数。返回获取查询的值。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100003 | Database corrupted. |
| 15100004 | Not found. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

4. const KEY_TEST_STRING_ELEMENT = 'key_test_string';
5. const VALUE_TEST_STRING_ELEMENT = 'value-test-string';
6. try {
7. kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT, (err: BusinessError) => {
8. if (err != undefined) {
9. console.error(`Failed to put.code is ${err.code},message is ${err.message}`);
10. return;
11. }
12. console.info("Succeeded in putting");
13. if (kvStore != null) {
14. kvStore.get(KEY_TEST_STRING_ELEMENT, (err: BusinessError, data: boolean | string | number | Uint8Array) => {
15. if (err != undefined) {
16. console.error(`Failed to get.code is ${err.code},message is ${err.message}`);
17. return;
18. }
19. console.info(`Succeeded in getting data.data=${data}`);
20. });
21. }
22. });
23. } catch (e) {
24. let error = e as BusinessError;
25. console.error(`Failed to get.code is ${error.code},message is ${error.message}`);
26. }
```

### get

PhonePC/2in1TabletTVWearable

get(key: string): Promise<boolean | string | number | Uint8Array>

获取指定键的值，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要查询数据的Key，不能为空且长度不大于[MAX\_KEY\_LENGTH](js-apis-distributedkvstore.md#constants)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean | string | number | Uint8Array> | Promise对象。返回获取查询的值。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100003 | Database corrupted. |
| 15100004 | Not found. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

4. const KEY_TEST_STRING_ELEMENT = 'key_test_string';
5. const VALUE_TEST_STRING_ELEMENT = 'value-test-string';
6. try {
7. kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT).then(() => {
8. console.info(`Succeeded in putting data`);
9. if (kvStore != null) {
10. kvStore.get(KEY_TEST_STRING_ELEMENT).then((data: boolean | string | number | Uint8Array) => {
11. console.info(`Succeeded in getting data.data=${data}`);
12. }).catch((err: BusinessError) => {
13. console.error(`Failed to get.code is ${err.code},message is ${err.message}`);
14. });
15. }
16. }).catch((err: BusinessError) => {
17. console.error(`Failed to put.code is ${err.code},message is ${err.message}`);
18. });
19. } catch (e) {
20. let error = e as BusinessError;
21. console.error(`Failed to get.code is ${error.code},message is ${error.message}`);
22. }
```

### getEntries

PhonePC/2in1TabletTVWearable

getEntries(keyPrefix: string, callback: AsyncCallback<Entry[]>): void

获取匹配指定键前缀的所有键值对，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyPrefix | string | 是 | 表示要匹配的键前缀。不能包含'^'，包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |
| callback | AsyncCallback<[Entry](js-apis-distributedkvstore.md#entry)[]> | 是 | 回调函数。返回匹配指定前缀的键值对列表。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let entries: distributedKVStore.Entry[] = [];
5. for (let i = 0; i < 10; i++) {
6. let key = 'batch_test_string_key';
7. let entry: distributedKVStore.Entry = {
8. key: key + i,
9. value: {
10. type: distributedKVStore.ValueType.STRING,
11. value: 'batch_test_string_value'
12. }
13. }
14. entries.push(entry);
15. }
16. console.info(`entries: ${entries}`);
17. kvStore.putBatch(entries, async (err: BusinessError) => {
18. if (err != undefined) {
19. console.error(`Failed to put Batch.code is ${err.code},message is ${err.message}`);
20. return;
21. }
22. console.info('Succeeded in putting Batch');
23. if (kvStore != null) {
24. kvStore.getEntries('batch_test_string_key', (err: BusinessError, entries: distributedKVStore.Entry[]) => {
25. if (err != undefined) {
26. console.error(`Failed to get Entries.code is ${err.code},message is ${err.message}`);
27. return;
28. }
29. console.info('Succeeded in getting Entries');
30. console.info(`entries.length: ${entries.length}`);
31. console.info(`entries[0]: ${entries[0]}`);
32. });
33. }
34. });
35. } catch (e) {
36. let error = e as BusinessError;
37. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message} `);
38. }
```

### getEntries

PhonePC/2in1TabletTVWearable

getEntries(keyPrefix: string): Promise<Entry[]>

获取匹配指定键前缀的所有键值对，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyPrefix | string | 是 | 表示要匹配的键前缀。不能包含'^'，包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Entry](js-apis-distributedkvstore.md#entry)[]> | Promise对象。返回匹配指定前缀的键值对列表。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. let entries: distributedKVStore.Entry[] = [];
6. for (let i = 0; i < 10; i++) {
7. let key = 'batch_test_string_key';
8. let entry: distributedKVStore.Entry = {
9. key: key + i,
10. value: {
11. type: distributedKVStore.ValueType.STRING,
12. value: 'batch_test_string_value'
13. }
14. }
15. entries.push(entry);
16. }
17. console.info(`entries: ${entries}`);
18. kvStore.putBatch(entries).then(async () => {
19. console.info('Succeeded in putting Batch');
20. if (kvStore != null) {
21. kvStore.getEntries('batch_test_string_key').then((entries: distributedKVStore.Entry[]) => {
22. console.info('Succeeded in getting Entries');
23. console.info(`PutBatch ${entries}`);
24. }).catch((err: BusinessError) => {
25. console.error(`Failed to get Entries.code is ${err.code},message is ${err.message}`);
26. });
27. }
28. }).catch((err: BusinessError) => {
29. console.error(`Failed to put Batch.code is ${err.code},message is ${err.message}`);
30. });
31. } catch (e) {
32. let error = e as BusinessError;
33. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message} `);
34. }
```

### getEntries

PhonePC/2in1TabletTVWearable

getEntries(query: Query, callback: AsyncCallback<Entry[]>): void

获取与指定Query对象匹配的键值对列表，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | [Query](js-apis-distributedkvstore.md#query) | 是 | 表示要匹配的键前缀。 |
| callback | AsyncCallback<[Entry](js-apis-distributedkvstore.md#entry)[]> | 是 | 回调函数。返回与指定Query对象匹配的键值对列表。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let arr = new Uint8Array([21, 31]);
5. let entries: distributedKVStore.Entry[] = [];
6. for (let i = 0; i < 10; i++) {
7. let key = 'batch_test_bool_key';
8. let entry: distributedKVStore.Entry = {
9. key: key + i,
10. value: {
11. type: distributedKVStore.ValueType.BYTE_ARRAY,
12. value: arr
13. }
14. }
15. entries.push(entry);
16. }
17. console.info(`entries: {entries}`);
18. kvStore.putBatch(entries, async (err: BusinessError) => {
19. console.info('Succeeded in putting Batch');
20. const query = new distributedKVStore.Query();
21. query.prefixKey("batch_test");
22. if (kvStore != null) {
23. kvStore.getEntries(query, (err: BusinessError, entries: distributedKVStore.Entry[]) => {
24. if (err != undefined) {
25. console.error(`Failed to get Entries.code is ${err.code},message is ${err.message}`);
26. return;
27. }
28. console.info('Succeeded in getting Entries');
29. console.info(`entries.length: ${entries.length}`);
30. console.info(`entries[0]: ${entries[0]}`);
31. });
32. }
33. });
34. } catch (e) {
35. let error = e as BusinessError;
36. console.error(`Failed to get Entries.code is ${error.code},message is ${error.message}`);
37. }
```

### getEntries

PhonePC/2in1TabletTVWearable

getEntries(query: Query): Promise<Entry[]>

获取与指定Query对象匹配的键值对列表，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | [Query](js-apis-distributedkvstore.md#query) | 是 | 表示查询对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Entry](js-apis-distributedkvstore.md#entry)[]> | Promise对象。返回与指定Query对象匹配的键值对列表。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let arr = new Uint8Array([21, 31]);
5. let entries: distributedKVStore.Entry[] = [];
6. for (let i = 0; i < 10; i++) {
7. let key = 'batch_test_bool_key';
8. let entry: distributedKVStore.Entry = {
9. key: key + i,
10. value: {
11. type: distributedKVStore.ValueType.BYTE_ARRAY,
12. value: arr
13. }
14. }
15. entries.push(entry);
16. }
17. console.info(`entries: {entries}`);
18. kvStore.putBatch(entries).then(async () => {
19. console.info('Succeeded in putting Batch');
20. const query = new distributedKVStore.Query();
21. query.prefixKey("batch_test");
22. if (kvStore != null) {
23. kvStore.getEntries(query).then((entries: distributedKVStore.Entry[]) => {
24. console.info('Succeeded in getting Entries');
25. }).catch((err: BusinessError) => {
26. console.error(`Failed to get Entries.code is ${err.code},message is ${err.message}`);
27. });
28. }
29. }).catch((err: BusinessError) => {
30. console.error(`Failed to get Entries.code is ${err.code},message is ${err.message}`)
31. });
32. console.info('Succeeded in getting Entries');
33. } catch (e) {
34. let error = e as BusinessError;
35. console.error(`Failed to get Entries.code is ${error.code},message is ${error.message}`);
36. }
```

### getResultSet

PhonePC/2in1TabletTVWearable

getResultSet(keyPrefix: string, callback: AsyncCallback<KVStoreResultSet>): void

从SingleKVStore数据库中获取具有指定前缀的结果集，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyPrefix | string | 是 | 表示要匹配的键前缀。不能包含'^'，包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |
| callback | AsyncCallback<[KVStoreResultSet](js-apis-distributedkvstore.md#kvstoreresultset)> | 是 | 回调函数。返回具有指定前缀的结果集。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100001 | Over max limits. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let resultSet: distributedKVStore.KVStoreResultSet;
5. let entries: distributedKVStore.Entry[] = [];
6. for (let i = 0; i < 10; i++) {
7. let key = 'batch_test_string_key';
8. let entry: distributedKVStore.Entry = {
9. key: key + i,
10. value: {
11. type: distributedKVStore.ValueType.STRING,
12. value: 'batch_test_string_value'
13. }
14. }
15. entries.push(entry);
16. }
17. kvStore.putBatch(entries, async (err: BusinessError) => {
18. if (err != undefined) {
19. console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
20. return;
21. }
22. console.info('Succeeded in putting batch');
23. if (kvStore != null) {
24. kvStore.getResultSet('batch_test_string_key', async (err: BusinessError, result: distributedKVStore.KVStoreResultSet) => {
25. if (err != undefined) {
26. console.error(`Failed to get resultset.code is ${err.code},message is ${err.message}`);
27. return;
28. }
29. console.info('Succeeded in getting result set');
30. resultSet = result;
31. if (kvStore != null) {
32. kvStore.closeResultSet(resultSet, (err :BusinessError) => {
33. if (err != undefined) {
34. console.error(`Failed to close resultset.code is ${err.code},message is ${err.message}`);
35. return;
36. }
37. console.info('Succeeded in closing result set');
38. });
39. }
40. });
41. }
42. });
43. } catch (e) {
44. let error = e as BusinessError;
45. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
46. }
```

### getResultSet

PhonePC/2in1TabletTVWearable

getResultSet(keyPrefix: string): Promise<KVStoreResultSet>

从SingleKVStore数据库中获取具有指定前缀的结果集，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyPrefix | string | 是 | 表示要匹配的键前缀。不能包含'^'，包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[KVStoreResultSet](js-apis-distributedkvstore.md#kvstoreresultset)> | Promise对象。返回具有指定前缀的结果集。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100001 | Over max limits. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let resultSet: distributedKVStore.KVStoreResultSet;
5. let entries: distributedKVStore.Entry[] = [];
6. for (let i = 0; i < 10; i++) {
7. let key = 'batch_test_string_key';
8. let entry: distributedKVStore.Entry = {
9. key: key + i,
10. value: {
11. type: distributedKVStore.ValueType.STRING,
12. value: 'batch_test_string_value'
13. }
14. }
15. entries.push(entry);
16. }
17. kvStore.putBatch(entries).then(async () => {
18. console.info('Succeeded in putting batch');
19. }).catch((err: BusinessError) => {
20. console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
21. });
22. kvStore.getResultSet('batch_test_string_key').then((result: distributedKVStore.KVStoreResultSet) => {
23. console.info('Succeeded in getting result set');
24. resultSet = result;
25. if (kvStore != null) {
26. kvStore.closeResultSet(resultSet).then(() => {
27. console.info('Succeeded in closing result set');
28. }).catch((err: BusinessError) => {
29. console.error(`Failed to close resultset.code is ${err.code},message is ${err.message}`);
30. });
31. }
32. }).catch((err: BusinessError) => {
33. console.error(`Failed to get resultset.code is ${err.code},message is ${err.message}`);
34. });
35. } catch (e) {
36. let error = e as BusinessError;
37. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
38. }
```

### getResultSet

PhonePC/2in1TabletTVWearable

getResultSet(query: Query, callback: AsyncCallback<KVStoreResultSet>): void

获取与指定Query对象匹配的KVStoreResultSet对象，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | Query | 是 | 表示查询对象。 |
| callback | AsyncCallback<[KVStoreResultSet](js-apis-distributedkvstore.md#kvstoreresultset)> | 是 | 回调函数，获取与指定Query对象匹配的KVStoreResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100001 | Over max limits. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let resultSet: distributedKVStore.KVStoreResultSet;
5. let entries: distributedKVStore.Entry[] = [];
6. for (let i = 0; i < 10; i++) {
7. let key = 'batch_test_string_key';
8. let entry: distributedKVStore.Entry = {
9. key: key + i,
10. value: {
11. type: distributedKVStore.ValueType.STRING,
12. value: 'batch_test_string_value'
13. }
14. }
15. entries.push(entry);
16. }
17. kvStore.putBatch(entries, async (err: BusinessError) => {
18. if (err != undefined) {
19. console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
20. return;
21. }
22. console.info('Succeeded in putting batch');
23. const query = new distributedKVStore.Query();
24. query.prefixKey("batch_test");
25. if (kvStore != null) {
26. kvStore.getResultSet(query, async (err: BusinessError, result: distributedKVStore.KVStoreResultSet) => {
27. if (err != undefined) {
28. console.error(`Failed to get resultset.code is ${err.code},message is ${err.message}`);
29. return;
30. }
31. console.info('Succeeded in getting result set');
32. });
33. }
34. });
35. } catch (e) {
36. let error = e as BusinessError;
37. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
38. }
```

### getResultSet

PhonePC/2in1TabletTVWearable

getResultSet(query: Query): Promise<KVStoreResultSet>

获取与指定Query对象匹配的KVStoreResultSet对象，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | [Query](js-apis-distributedkvstore.md#query) | 是 | 表示查询对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[KVStoreResultSet](js-apis-distributedkvstore.md#kvstoreresultset)> | Promise对象。获取与指定Query对象匹配的KVStoreResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100001 | Over max limits. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let resultSet: distributedKVStore.KVStoreResultSet;
5. let entries: distributedKVStore.Entry[] = [];
6. for (let i = 0; i < 10; i++) {
7. let key = 'batch_test_string_key';
8. let entry: distributedKVStore.Entry = {
9. key: key + i,
10. value: {
11. type: distributedKVStore.ValueType.STRING,
12. value: 'batch_test_string_value'
13. }
14. }
15. entries.push(entry);
16. }
17. kvStore.putBatch(entries).then(async () => {
18. console.info('Succeeded in putting batch');
19. }).catch((err: BusinessError) => {
20. console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
21. });
22. const query = new distributedKVStore.Query();
23. query.prefixKey("batch_test");
24. kvStore.getResultSet(query).then((result: distributedKVStore.KVStoreResultSet) => {
25. console.info('Succeeded in getting result set');
26. resultSet = result;
27. }).catch((err: BusinessError) => {
28. console.error(`Failed to get resultset.code is ${err.code},message is ${err.message}`);
29. });
30. } catch (e) {
31. let error = e as BusinessError;
32. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
33. }
```

### closeResultSet

PhonePC/2in1TabletTVWearable

closeResultSet(resultSet: KVStoreResultSet, callback: AsyncCallback<void>): void

关闭由[SingleKvStore.getResultSet](js-apis-distributedkvstore.md#getresultset-1)返回的KVStoreResultSet对象，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resultSet | [KVStoreResultSet](js-apis-distributedkvstore.md#kvstoreresultset) | 是 | 表示要关闭的KVStoreResultSet对象。 |
| callback | AsyncCallback<void> | 是 | 回调函数。关闭KVStoreResultSet对象成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let resultSet: distributedKVStore.KVStoreResultSet;
4. try {
5. kvStore.getResultSet('batch_test_string_key', async (err: BusinessError, result: distributedKVStore.KVStoreResultSet) => {
6. if (err != undefined) {
7. console.error(`Failed to get resultset.code is ${err.code},message is ${err.message}`);
8. return;
9. }
10. console.info('Succeeded in getting result set');
11. resultSet = result;
12. if (kvStore != null) {
13. kvStore.closeResultSet(resultSet, (err: BusinessError) => {
14. if (err != undefined) {
15. console.error(`Failed to close resultset.code is ${err.code},message is ${err.message}`);
16. return;
17. }
18. console.info('Succeeded in closing result set');
19. })
20. }
21. });
22. } catch (e) {
23. let error = e as BusinessError;
24. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
25. }
```

### closeResultSet

PhonePC/2in1TabletTVWearable

closeResultSet(resultSet: KVStoreResultSet): Promise<void>

关闭由[SingleKvStore.getResultSet](js-apis-distributedkvstore.md#getresultset-1)返回的KVStoreResultSet对象，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resultSet | [KVStoreResultSet](js-apis-distributedkvstore.md#kvstoreresultset) | 是 | 表示要关闭的KVStoreResultSet对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let resultSet: distributedKVStore.KVStoreResultSet;
4. try {
5. kvStore.getResultSet('batch_test_string_key').then((result: distributedKVStore.KVStoreResultSet) => {
6. console.info('Succeeded in getting result set');
7. resultSet = result;
8. if (kvStore != null) {
9. kvStore.closeResultSet(resultSet).then(() => {
10. console.info('Succeeded in closing result set');
11. }).catch((err: BusinessError) => {
12. console.error(`Failed to close resultset.code is ${err.code},message is ${err.message}`);
13. });
14. }
15. }).catch((err: BusinessError) => {
16. console.error(`Failed to get resultset.code is ${err.code},message is ${err.message}`);
17. });

19. } catch (e) {
20. let error = e as BusinessError;
21. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
22. }
```

### getResultSize

PhonePC/2in1TabletTVWearable

getResultSize(query: Query, callback: AsyncCallback<number>): void

获取与指定Query对象匹配的结果数，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | [Query](js-apis-distributedkvstore.md#query) | 是 | 表示查询对象。 |
| callback | AsyncCallback<number> | 是 | 回调函数。返回与指定Query对象匹配的结果数。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100004 | Not found. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let entries: distributedKVStore.Entry[] = [];
5. for (let i = 0; i < 10; i++) {
6. let key = 'batch_test_string_key';
7. let entry: distributedKVStore.Entry = {
8. key: key + i,
9. value: {
10. type: distributedKVStore.ValueType.STRING,
11. value: 'batch_test_string_value'
12. }
13. }
14. entries.push(entry);
15. }
16. kvStore.putBatch(entries, (err: BusinessError) => {
17. console.info('Succeeded in putting batch');
18. const query = new distributedKVStore.Query();
19. query.prefixKey("batch_test");
20. if (kvStore != null) {
21. kvStore.getResultSize(query, (err: BusinessError, resultSize: number) => {
22. if (err != undefined) {
23. console.error(`Failed to get result size.code is ${err.code},message is ${err.message}`);
24. return;
25. }
26. console.info('Succeeded in getting result set size');
27. });
28. }
29. });
30. } catch (e) {
31. let error = e as BusinessError;
32. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
33. }
```

### getResultSize

PhonePC/2in1TabletTVWearable

getResultSize(query: Query): Promise<number>

获取与指定Query对象匹配的结果数，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | [Query](js-apis-distributedkvstore.md#query) | 是 | 表示查询对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。获取与指定Query对象匹配的结果数。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100004 | Not found. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let entries: distributedKVStore.Entry[] = [];
5. for (let i = 0; i < 10; i++) {
6. let key = 'batch_test_string_key';
7. let entry: distributedKVStore.Entry = {
8. key: key + i,
9. value: {
10. type: distributedKVStore.ValueType.STRING,
11. value: 'batch_test_string_value'
12. }
13. }
14. entries.push(entry);
15. }
16. kvStore.putBatch(entries).then(async () => {
17. console.info('Succeeded in putting batch');
18. }).catch((err: BusinessError) => {
19. console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
20. });
21. const query = new distributedKVStore.Query();
22. query.prefixKey("batch_test");
23. kvStore.getResultSize(query).then((resultSize: number) => {
24. console.info('Succeeded in getting result set size');
25. }).catch((err: BusinessError) => {
26. console.error(`Failed to get result size.code is ${err.code},message is ${err.message}`);
27. });
28. } catch (e) {
29. let error = e as BusinessError;
30. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
31. }
```

### backup

PhonePC/2in1TabletTVWearable

backup(file:string, callback: AsyncCallback<void>):void

以指定名称备份数据库，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string | 是 | 备份数据库的指定名称，不能为空且长度不大于[MAX\_KEY\_LENGTH](js-apis-distributedkvstore.md#constants)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当以指定名称备份数据库成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let backupFile = "BK001";
4. try {
5. kvStore.backup(backupFile, (err: BusinessError) => {
6. if (err) {
7. console.error(`Failed to backup.code is ${err.code},message is ${err.message} `);
8. } else {
9. console.info(`Succeeded in backupping data`);
10. }
11. });
12. } catch (e) {
13. let error = e as BusinessError;
14. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
15. }
```

### backup

PhonePC/2in1TabletTVWearable

backup(file:string): Promise<void>

以指定名称备份数据库，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string | 是 | 备份数据库的指定名称，不能为空且长度不大于[MAX\_KEY\_LENGTH](js-apis-distributedkvstore.md#constants)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let backupFile = "BK001";
4. try {
5. kvStore.backup(backupFile).then(() => {
6. console.info(`Succeeded in backupping data`);
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to backup.code is ${err.code},message is ${err.message}`);
9. });
10. } catch (e) {
11. let error = e as BusinessError;
12. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
13. }
```

### restore

PhonePC/2in1TabletTVWearable

restore(file:string, callback: AsyncCallback<void>):void

从指定的数据库文件恢复数据库，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string | 是 | 指定的数据库文件名称，不能为空且长度不大于[MAX\_KEY\_LENGTH](js-apis-distributedkvstore.md#constants)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当从指定的数据库文件恢复数据库成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let backupFile = "BK001";
4. try {
5. kvStore.restore(backupFile, (err: BusinessError) => {
6. if (err) {
7. console.error(`Failed to restore.code is ${err.code},message is ${err.message}`);
8. } else {
9. console.info(`Succeeded in restoring data`);
10. }
11. });
12. } catch (e) {
13. let error = e as BusinessError;
14. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
15. }
```

### restore

PhonePC/2in1TabletTVWearable

restore(file:string): Promise<void>

从指定的数据库文件恢复数据库，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string | 是 | 指定的数据库文件名称，不能为空且长度不大于[MAX\_KEY\_LENGTH](js-apis-distributedkvstore.md#constants)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let backupFile = "BK001";
4. try {
5. kvStore.restore(backupFile).then(() => {
6. console.info(`Succeeded in restoring data`);
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to restore.code is ${err.code},message is ${err.message}`);
9. });
10. } catch (e) {
11. let error = e as BusinessError;
12. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
13. }
```

### deleteBackup

PhonePC/2in1TabletTVWearable

deleteBackup(files:Array<string>, callback: AsyncCallback<Array<[string, number]>>):void

根据指定名称删除备份文件，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| files | Array<string> | 是 | 删除备份文件所指定的名称，不能为空且长度不大于[MAX\_KEY\_LENGTH](js-apis-distributedkvstore.md#constants)。 |
| callback | AsyncCallback<Array<[string, number]>> | 是 | 回调函数，返回删除备份的文件名及其处理结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let files = ["BK001", "BK002"];
4. try {
5. kvStore.deleteBackup(files, (err: BusinessError, data: [string, number][]) => {
6. if (err) {
7. console.error(`Failed to delete Backup.code is ${err.code},message is ${err.message}`);
8. } else {
9. console.info(`Succeed in deleting Backup.data=${data}`);
10. }
11. });
12. } catch (e) {
13. let error = e as BusinessError;
14. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
15. }
```

### deleteBackup

PhonePC/2in1TabletTVWearable

deleteBackup(files:Array<string>): Promise<Array<[string, number]>>

根据指定名称删除备份文件，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| files | Array<string> | 是 | 删除备份文件所指定的名称，不能为空且长度不大于[MAX\_KEY\_LENGTH](js-apis-distributedkvstore.md#constants)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[string, number]>> | Promise对象，返回删除备份的文件名及其处理结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let files = ["BK001", "BK002"];
4. try {
5. kvStore.deleteBackup(files).then((data: [string, number][]) => {
6. console.info(`Succeed in deleting Backup.data=${data}`);
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to delete Backup.code is ${err.code},message is ${err.message}`);
9. })
10. } catch (e) {
11. let error = e as BusinessError;
12. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
13. }
```

### startTransaction

PhonePC/2in1TabletTVWearable

startTransaction(callback: AsyncCallback<void>): void

启动SingleKVStore数据库中的事务，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。启动SingleKVStore数据库中的事务成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 15100005 | Database or result set already closed. |

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. function putBatchString(len: number, prefix: string) {
4. let entries: distributedKVStore.Entry[] = [];
5. for (let i = 0; i < len; i++) {
6. let entry: distributedKVStore.Entry = {
7. key: prefix + i,
8. value: {
9. type: distributedKVStore.ValueType.STRING,
10. value: 'batch_test_string_value'
11. }
12. }
13. entries.push(entry);
14. }
15. return entries;
16. } // 自定义函数，放置在作用域最外侧，防止语法检查报错

18. try {
19. let count = 0;
20. kvStore.on('dataChange', 0, (data: distributedKVStore.ChangeNotification) => {
21. console.info(`startTransaction 0 ${data}`);
22. count++;
23. });
24. kvStore.startTransaction(async (err: BusinessError) => {
25. if (err != undefined) {
26. console.error(`Failed to start Transaction.code is ${err.code},message is ${err.message}`);
27. return;
28. }
29. console.info('Succeeded in starting Transaction');
30. let entries = putBatchString(10, 'batch_test_string_key');
31. console.info(`entries: ${entries}`);
32. if (kvStore != null) {
33. kvStore.putBatch(entries, async (err: BusinessError) => {
34. if (err != undefined) {
35. console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
36. return;
37. }
38. console.info('Succeeded in putting Batch');
39. });
40. }
41. });
42. } catch (e) {
43. let error = e as BusinessError;
44. console.error(`Failed to start Transaction.code is ${error.code},message is ${error.message}`);
45. }
```

### startTransaction

PhonePC/2in1TabletTVWearable

startTransaction(): Promise<void>

启动SingleKVStore数据库中的事务，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 15100005 | Database or result set already closed. |

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let count = 0;
5. kvStore.on('dataChange', distributedKVStore.SubscribeType.SUBSCRIBE_TYPE_ALL, (data: distributedKVStore.ChangeNotification) => {
6. console.info(`startTransaction 0 ${data}`);
7. count++;
8. });
9. kvStore.startTransaction().then(async () => {
10. console.info('Succeeded in starting Transaction');
11. }).catch((err: BusinessError) => {
12. console.error(`Failed to start Transaction.code is ${err.code},message is ${err.message}`);
13. });
14. } catch (e) {
15. let error = e as BusinessError;
16. console.error(`Failed to start Transaction.code is ${error.code},message is ${error.message}`);
17. }
```

### commit

PhonePC/2in1TabletTVWearable

commit(callback: AsyncCallback<void>): void

提交SingleKVStore数据库中的事务，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。提交SingleKVStore数据库中的事务成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. kvStore.commit((err: BusinessError) => {
5. if (err) {
6. console.error(`Failed to commit. Code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info('Succeeded in committing');
9. }
10. });
11. } catch (e) {
12. let error = e as BusinessError;
13. console.error(`An unexpected error occurred. Code is ${error.code}, message is ${error.message}`);
14. }
```

### commit

PhonePC/2in1TabletTVWearable

commit(): Promise<void>

提交SingleKVStore数据库中的事务，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. kvStore.commit().then(async () => {
5. console.info('Succeeded in committing');
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to commit.code is ${err.code},message is ${err.message}`);
8. });
9. } catch (e) {
10. let error = e as BusinessError;
11. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
12. }
```

### rollback

PhonePC/2in1TabletTVWearable

rollback(callback: AsyncCallback<void>): void

在SingleKVStore数据库中回滚事务，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。SingleKVStore数据库中回滚事务成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. kvStore.rollback((err: BusinessError) => {
5. if (err) {
6. console.error(`Failed to rollback. Code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info('Succeeded in rolling back');
9. }
10. });
11. } catch (e) {
12. let error = e as BusinessError;
13. console.error(`An unexpected error occurred. Code is ${error.code}, message is ${error.message}`);
14. }
```

### rollback

PhonePC/2in1TabletTVWearable

rollback(): Promise<void>

在SingleKVStore数据库中回滚事务，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. kvStore.rollback().then(async () => {
5. console.info('Succeeded in rolling back');
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to rollback.code is ${err.code},message is ${err.message}`);
8. });
9. } catch (e) {
10. let error = e as BusinessError;
11. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
12. }
```

### enableSync

PhonePC/2in1TabletTVWearable

enableSync(enabled: boolean, callback: AsyncCallback<void>): void

设定是否开启端端同步，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 设定是否开启端端同步，true表示开启端端同步，false表示不启用端端同步。 |
| callback | AsyncCallback<void> | 是 | 回调函数。设定成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error.Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameters types. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. kvStore.enableSync(true, (err: BusinessError) => {
5. if (err) {
6. console.error(`Failed to enable sync. Code is ${err.code}, message is ${err.message}`);
7. } else {
8. console.info('Succeeded in enabling sync');
9. }
10. });
11. } catch (e) {
12. let error = e as BusinessError;
13. console.error(`An unexpected error occurred. Code is ${error.code}, message is ${error.message}`);
14. }
```

### enableSync

PhonePC/2in1TabletTVWearable

enableSync(enabled: boolean): Promise<void>

设定是否开启端端同步，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 设定是否开启端端同步，true表示开启端端同步，false表示不启用端端同步。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. kvStore.enableSync(true).then(() => {
5. console.info('Succeeded in enabling sync');
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to enable sync.code is ${err.code},message is ${err.message}`);
8. });
9. } catch (e) {
10. let error = e as BusinessError;
11. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
12. }
```

### setSyncRange

PhonePC/2in1TabletTVWearable

setSyncRange(localLabels: string[], remoteSupportLabels: string[], callback: AsyncCallback<void>): void

设置同步范围标签，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localLabels | string[] | 是 | 表示本地设备的同步标签。 |
| remoteSupportLabels | string[] | 是 | 表示要同步数据的设备的同步标签。 |
| callback | AsyncCallback<void> | 是 | 回调函数。设置成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. const localLabels = ['A', 'B'];
5. const remoteSupportLabels = ['C', 'D'];
6. kvStore.setSyncRange(localLabels, remoteSupportLabels, (err: BusinessError) => {
7. if (err != undefined) {
8. console.error(`Failed to set syncRange.code is ${err.code},message is ${err.message}`);
9. return;
10. }
11. console.info('Succeeded in setting syncRange');
12. });
13. } catch (e) {
14. let error = e as BusinessError;
15. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
16. }
```

### setSyncRange

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

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. const localLabels = ['A', 'B'];
5. const remoteSupportLabels = ['C', 'D'];
6. kvStore.setSyncRange(localLabels, remoteSupportLabels).then(() => {
7. console.info('Succeeded in setting syncRange');
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to set syncRange.code is ${err.code},message is ${err.message}`);
10. });
11. } catch (e) {
12. let error = e as BusinessError;
13. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
14. }
```

### setSyncParam

PhonePC/2in1TabletTVWearable

setSyncParam(defaultAllowedDelayMs: number, callback: AsyncCallback<void>): void

设置数据库端端同步允许的默认延时，使用callback异步回调。

说明

设置默认延时后，调用[sync](js-apis-distributedkvstore.md#sync)接口不会立即触发端端同步，而是等待指定的延时时间后再执行。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| defaultAllowedDelayMs | number | 是 | 表示一个延时时间，单位为毫秒（ms），取值范围为0或[100, 86400000]。 |
| callback | AsyncCallback<void> | 是 | 回调函数。设置成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. const defaultAllowedDelayMs = 500;
5. kvStore.setSyncParam(defaultAllowedDelayMs, (err: BusinessError) => {
6. if (err != undefined) {
7. console.error(`Failed to set syncParam.code is ${err.code},message is ${err.message}`);
8. return;
9. }
10. console.info('Succeeded in setting syncParam');
11. });
12. } catch (e) {
13. let error = e as BusinessError;
14. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
15. }
```

### setSyncParam

PhonePC/2in1TabletTVWearable

setSyncParam(defaultAllowedDelayMs: number): Promise<void>

设置数据库端端同步允许的默认延时，使用Promise异步回调。

说明

设置默认延时后，调用[sync](js-apis-distributedkvstore.md#sync)接口不会立即触发端端同步，而是等待指定的延时时间后再执行。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| defaultAllowedDelayMs | number | 是 | 表示一个延时时间，单位为毫秒（ms），取值范围为0或[100, 86400000]。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. const defaultAllowedDelayMs = 500;
5. kvStore.setSyncParam(defaultAllowedDelayMs).then(() => {
6. console.info('Succeeded in setting syncParam');
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to set syncParam.code is ${err.code},message is ${err.message}`);
9. });
10. } catch (e) {
11. let error = e as BusinessError;
12. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
13. }
```

### sync

PhonePC/2in1TabletTVWearable

sync(deviceIds: string[], mode: SyncMode, delayMs?: number): void

在手动同步方式下，触发数据库端端同步。关于键值型数据库的端端同步方式说明，请见[键值型数据库跨设备数据同步](../harmonyos-guides/data-sync-of-kv-store.md)。

说明

其中deviceIds为[DeviceBasicInfo](js-apis-distributeddevicemanager.md#devicebasicinfo)中的networkId, 通过调用[deviceManager.getAvailableDeviceListSync](js-apis-distributeddevicemanager.md#getavailabledevicelistsync)方法得到。

**需要权限**： ohos.permission.DISTRIBUTED\_DATASYNC。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceIds | string[] | 是 | 同一组网环境下，需要同步的设备的networkId列表。 |
| mode | [SyncMode](js-apis-distributedkvstore.md#syncmode) | 是 | 同步模式。 |
| delayMs | number | 否 | 可选参数，允许延时时间，单位：ms（毫秒），默认为0。设置delayMs后，调用sync接口时延时时间为delayMs。未设置时以[setSyncParam](js-apis-distributedkvstore.md#setsyncparam)设置的时长为准。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100004 | Not found. |

**示例：**

```
1. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let devManager: distributedDeviceManager.DeviceManager;
6. const KEY_TEST_SYNC_ELEMENT = 'key_test_sync';
7. const VALUE_TEST_SYNC_ELEMENT = 'value-string-001';
8. // create deviceManager
9. export default class EntryAbility extends UIAbility {
10. onCreate() {
11. let context = this.context;
12. try {
13. devManager = distributedDeviceManager.createDeviceManager(context.applicationInfo.name);
14. let deviceIds: string[] = [];
15. if (devManager != null) {
16. let devices = devManager.getAvailableDeviceListSync();
17. for (let i = 0; i < devices.length; i++) {
18. deviceIds[i] = devices[i].networkId as string;
19. }
20. }
21. try {
22. if (kvStore != null) {
23. kvStore.on('syncComplete', (data: [string, number][]) => {
24. console.info('Sync dataChange');
25. });
26. if (kvStore != null) {
27. kvStore.put(KEY_TEST_SYNC_ELEMENT + 'testSync101', VALUE_TEST_SYNC_ELEMENT, (err: BusinessError) => {
28. if (err != undefined) {
29. console.error(`Failed to sync.code is ${err.code},message is ${err.message}`);
30. return;
31. }
32. console.info('Succeeded in putting data');
33. const mode = distributedKVStore.SyncMode.PULL_ONLY;
34. if (kvStore != null) {
35. kvStore.sync(deviceIds, mode, 1000);
36. }
37. });
38. }
39. }
40. } catch (e) {
41. let error = e as BusinessError;
42. console.error(`Failed to sync.code is ${error.code},message is ${error.message}`);
43. }

45. } catch (err) {
46. let error = err as BusinessError;
47. console.error("createDeviceManager errCode:" + error.code + ",errMessage:" + error.message);
48. }
49. }
50. }
```

### sync

PhonePC/2in1TabletTVWearable

sync(deviceIds: string[], query: Query, mode: SyncMode, delayMs?: number): void

在手动同步方式下，触发数据库端端同步，此方法为同步方法。关于键值型数据库的端端同步方式说明，请见[键值型数据库跨设备数据同步](../harmonyos-guides/data-sync-of-kv-store.md)。

说明

其中deviceIds为[DeviceBasicInfo](js-apis-distributeddevicemanager.md#devicebasicinfo)中的networkId, 通过调用[deviceManager.getAvailableDeviceListSync](js-apis-distributeddevicemanager.md#getavailabledevicelistsync)方法得到。

**需要权限**： ohos.permission.DISTRIBUTED\_DATASYNC。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceIds | string[] | 是 | 同一组网环境下，需要同步的设备的networkId列表。 |
| query | [Query](js-apis-distributedkvstore.md#query) | 是 | 表示数据库的查询谓词条件。 |
| mode | [SyncMode](js-apis-distributedkvstore.md#syncmode) | 是 | 同步模式。 |
| delayMs | number | 否 | 可选参数，允许延时时间，单位：ms（毫秒），默认为0。设置delayMs后，调用sync接口时延时时间为delayMs。未设置时以[setSyncParam](js-apis-distributedkvstore.md#setsyncparam)设置的时长为准。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100004 | Not found. |

**示例：**

```
1. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. const KEY_TEST_SYNC_ELEMENT = 'key_test_sync';
6. const VALUE_TEST_SYNC_ELEMENT = 'value-string-001';
7. // create deviceManager
8. export default class EntryAbility extends UIAbility {
9. onCreate() {
10. let context = this.context;
11. try {
12. let devManager = distributedDeviceManager.createDeviceManager(context.applicationInfo.name);
13. let deviceIds: string[] = [];
14. if (devManager != null) {
15. let devices = devManager.getAvailableDeviceListSync();
16. for (let i = 0; i < devices.length; i++) {
17. deviceIds[i] = devices[i].networkId as string;
18. }
19. }
20. try {
21. if (kvStore != null) {
22. kvStore.on('syncComplete', (data: [string, number][]) => {
23. console.info('Sync dataChange');
24. });
25. if (kvStore != null) {
26. kvStore.put(KEY_TEST_SYNC_ELEMENT + 'testSync101', VALUE_TEST_SYNC_ELEMENT, (err: BusinessError) => {
27. if (err != undefined) {
28. console.error(`Failed to sync.code is ${err.code},message is ${err.message}`);
29. return;
30. }
31. console.info('Succeeded in putting data');
32. const mode = distributedKVStore.SyncMode.PULL_ONLY;
33. const query = new distributedKVStore.Query();
34. query.prefixKey("batch_test");
35. query.deviceId(devManager.getLocalDeviceNetworkId());
36. if (kvStore != null) {
37. kvStore.sync(deviceIds, query, mode, 1000);
38. }
39. });
40. }
41. }
42. } catch (e) {
43. let error = e as BusinessError;
44. console.error(`Failed to sync.code is ${error.code},message is ${error.message}`);
45. }

47. } catch (err) {
48. let error = err as BusinessError;
49. console.error("createDeviceManager errCode:" + error.code + ",errMessage:" + error.message);
50. }
51. }
52. }
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
| type | [SubscribeType](js-apis-distributedkvstore.md#subscribetype) | 是 | 表示订阅的类型。 |
| listener | Callback<[ChangeNotification](js-apis-distributedkvstore.md#changenotification)> | 是 | 回调函数。成功返回数据变更时通知的对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100001 | Over max limits. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. kvStore.on('dataChange', distributedKVStore.SubscribeType.SUBSCRIBE_TYPE_LOCAL, (data: distributedKVStore.ChangeNotification) => {
5. console.info(`dataChange callback call data: ${data}`);
6. });
7. } catch (e) {
8. let error = e as BusinessError;
9. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
10. }
```

### on('syncComplete')

PhonePC/2in1TabletTVWearable

on(event: 'syncComplete', syncCallback: Callback<Array<[string, number]>>): void

订阅端端同步完成事件回调通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 订阅的事件名，固定为'syncComplete'，表示同步完成事件。 |
| syncCallback | Callback<Array<[string, number]>> | 是 | 回调函数。用于向调用方发送同步结果的回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

4. const KEY_TEST_FLOAT_ELEMENT = 'key_test_float';
5. const VALUE_TEST_FLOAT_ELEMENT = 321.12;
6. try {
7. kvStore.on('syncComplete', (data: [string, number][]) => {
8. console.info(`syncComplete ${data}`);
9. });
10. kvStore.put(KEY_TEST_FLOAT_ELEMENT, VALUE_TEST_FLOAT_ELEMENT).then(() => {
11. console.info('succeeded in putting');
12. }).catch((err: BusinessError) => {
13. console.error(`Failed to put.code is ${err.code},message is ${err.message}`);
14. });
15. } catch (e) {
16. let error = e as BusinessError;
17. console.error(`Failed to subscribe syncComplete.code is ${error.code},message is ${error.message}`);
18. }
```

### off('dataChange')

PhonePC/2in1TabletTVWearable

off(event:'dataChange', listener?: Callback<ChangeNotification>): void

取消订阅数据变更通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取消订阅的事件名，固定为'dataChange'，表示数据变更事件。 |
| listener | Callback<[ChangeNotification](js-apis-distributedkvstore.md#changenotification)> | 否 | 取消订阅的函数。如不设置callback，则取消所有已订阅的函数。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. class KvstoreModel {
4. call(data: distributedKVStore.ChangeNotification) {
5. console.info(`dataChange : ${data}`);
6. }

8. subscribeDataChange() {
9. try {
10. if (kvStore != null) {
11. kvStore.on('dataChange', distributedKVStore.SubscribeType.SUBSCRIBE_TYPE_REMOTE, this.call);
12. }
13. } catch (err) {
14. let error = err as BusinessError;
15. console.error(`Failed to subscribeDataChange.code is ${error.code},message is ${error.message}`);
16. }
17. }

19. unsubscribeDataChange() {
20. try {
21. if (kvStore != null) {
22. kvStore.off('dataChange', this.call);
23. }
24. } catch (err) {
25. let error = err as BusinessError;
26. console.error(`Failed to unsubscribeDataChange.code is ${error.code},message is ${error.message}`);
27. }
28. }
29. }
```

### off('syncComplete')

PhonePC/2in1TabletTVWearable

off(event: 'syncComplete', syncCallback?: Callback<Array<[string, number]>>): void

取消订阅端端同步完成事件回调通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取消订阅的事件名，固定为'syncComplete'，表示同步完成事件。 |
| syncCallback | Callback<Array<[string, number]>> | 否 | 取消订阅的同步完成回调函数。如果该参数不填，则取消所有已订阅的同步完成回调函数。如果存在同一个数据库的多个ArkTS实例(通过[getKVStore](js-apis-distributedkvstore.md#getkvstore)接口获取)分别注册监听了同步完成事件，则对于任意一个ArkTS实例取消其所有已订阅的同步完成回调函数时，其余ArkTS实例已订阅的所有同步完成回调函数也会被取消。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. class KvstoreModel {
4. call(data: [string, number][]) {
5. console.info(`syncComplete : ${data}`);
6. }

8. subscribeDataChange() {
9. try {
10. if (kvStore != null) {
11. kvStore.on('syncComplete', this.call);
12. }
13. } catch (err) {
14. let error = err as BusinessError;
15. console.error(`Failed to subscribeDataChange.code is ${error.code},message is ${error.message}`);
16. }
17. }

19. unsubscribeDataChange() {
20. try {
21. if (kvStore != null) {
22. kvStore.off('syncComplete', this.call);
23. }
24. } catch (err) {
25. let error = err as BusinessError;
26. console.error(`Failed to unsubscribeDataChange.code is ${error.code},message is ${error.message}`);
27. }
28. }
29. }
```

### getSecurityLevel

PhonePC/2in1TabletTVWearable

getSecurityLevel(callback: AsyncCallback<SecurityLevel>): void

获取数据库的安全级别，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[SecurityLevel](js-apis-distributedkvstore.md#securitylevel)> | 是 | 回调函数。返回数据库的安全级别。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. kvStore.getSecurityLevel((err: BusinessError, data: distributedKVStore.SecurityLevel) => {
5. if (err != undefined) {
6. console.error(`Failed to get SecurityLevel.code is ${err.code},message is ${err.message}`);
7. return;
8. }
9. console.info('Succeeded in getting securityLevel');
10. });
11. } catch (e) {
12. let error = e as BusinessError;
13. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
14. }
```

### getSecurityLevel

PhonePC/2in1TabletTVWearable

getSecurityLevel(): Promise<SecurityLevel>

获取数据库的安全级别，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SecurityLevel](js-apis-distributedkvstore.md#securitylevel)> | Promise对象。返回数据库的安全级别。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. kvStore.getSecurityLevel().then((data: distributedKVStore.SecurityLevel) => {
5. console.info('Succeeded in getting securityLevel');
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to get SecurityLevel.code is ${err.code},message is ${err.message}`);
8. });
9. } catch (e) {
10. let error = e as BusinessError;
11. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
12. }
```

## DeviceKVStore

PhonePC/2in1TabletTVWearable

设备协同数据库，继承自SingleKVStore，提供查询数据和端端同步数据的方法，可以使用SingleKVStore的方法例如：put、putBatch等。

设备协同数据库，以设备维度对数据进行区分，每台设备仅能写入和修改本设备的数据，其它设备的数据对其是只读的，无法修改其它设备的数据。

比如，可以使用设备协同数据库实现设备间的图片分享，可以查看其他设备的图片，但无法修改和删除其他设备的图片。

在调用DeviceKVStore的方法前，需要先通过[getKVStore](js-apis-distributedkvstore.md#getkvstore)构建一个DeviceKVStore实例。

### get

PhonePC/2in1TabletTVWearable

get(key: string, callback: AsyncCallback<boolean | string | number | Uint8Array>): void

获取本设备指定键的值，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要查询数据的Key，不能为空且长度不大于[MAX\_KEY\_LENGTH](js-apis-distributedkvstore.md#constants)。 |
| callback | AsyncCallback<boolean | string | number | Uint8Array> | 是 | 回调函数。返回获取查询的值。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100003 | Database corrupted. |
| 15100004 | Not found. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const KEY_TEST_STRING_ELEMENT = 'key_test_string';
4. const VALUE_TEST_STRING_ELEMENT = 'value-test-string';
5. try {
6. kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT, (err: BusinessError) => {
7. if (err != undefined) {
8. console.error(`Failed to put.code is ${err.code},message is ${err.message}`);
9. return;
10. }
11. console.info("Succeeded in putting");
12. if (kvStore != null) {
13. kvStore.get(KEY_TEST_STRING_ELEMENT, (err: BusinessError, data: boolean | string | number | Uint8Array) => {
14. if (err != undefined) {
15. console.error(`Failed to get.code is ${err.code},message is ${err.message}`);
16. return;
17. }
18. console.info(`Succeeded in getting data. Data=${data}`);
19. });
20. }
21. });
22. } catch (e) {
23. let error = e as BusinessError;
24. console.error(`Failed to get.code is ${error.code},message is ${error.message}`);
25. }
```

### get

PhonePC/2in1TabletTVWearable

get(key: string): Promise<boolean | string | number | Uint8Array>

获取本设备指定键的值，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要查询数据的Key，不能为空且长度不大于[MAX\_KEY\_LENGTH](js-apis-distributedkvstore.md#constants)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean | string | number | Uint8Array> | Promise对象。返回获取查询的值。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100003 | Database corrupted. |
| 15100004 | Not found. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const KEY_TEST_STRING_ELEMENT = 'key_test_string';
4. const VALUE_TEST_STRING_ELEMENT = 'value-test-string';
5. try {
6. kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT).then(() => {
7. console.info(`Succeeded in putting data`);
8. if (kvStore != null) {
9. kvStore.get(KEY_TEST_STRING_ELEMENT).then((data: boolean | string | number | Uint8Array) => {
10. console.info(`Succeeded in getting data.data=${data}`);
11. }).catch((err: BusinessError) => {
12. console.error(`Failed to get.code is ${err.code},message is ${err.message}`);
13. });
14. }
15. }).catch((err: BusinessError) => {
16. console.error(`Failed to put.code is ${err.code},message is ${err.message}`);
17. });
18. } catch (e) {
19. let error = e as BusinessError;
20. console.error(`Failed to get.code is ${error.code},message is ${error.message}`);
21. }
```

### get

PhonePC/2in1TabletTVWearable

get(deviceId: string, key: string, callback: AsyncCallback<boolean | string | number | Uint8Array>): void

获取与指定设备ID和Key匹配的值，使用callback异步回调。

说明

其中deviceId通过调用[deviceManager.getAvailableDeviceListSync](js-apis-distributeddevicemanager.md#getavailabledevicelistsync)方法得到。

deviceId具体获取方式请参考[sync接口示例](js-apis-distributedkvstore.md#sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 标识要查询其数据的设备。 |
| key | string | 是 | 表示要查询Key值的键, 不能为空且长度不大于[MAX\_KEY\_LENGTH](js-apis-distributedkvstore.md#constants)。 |
| callback | AsyncCallback<boolean|string|number|Uint8Array> | 是 | 回调函数，返回匹配给定条件的字符串值。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100003 | Database corrupted. |
| 15100004 | Not found. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const KEY_TEST_STRING_ELEMENT = 'key_test_string_2';
4. const VALUE_TEST_STRING_ELEMENT = 'value-string-002';
5. try {
6. kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT, async (err: BusinessError) => {
7. if (err != undefined) {
8. console.error(`Failed to put.code is ${err.code},message is ${err.message}`);
9. return;
10. }
11. console.info('Succeeded in putting');
12. if (kvStore != null) {
13. kvStore.get('localDeviceId', KEY_TEST_STRING_ELEMENT, (err: BusinessError, data: boolean | string | number | Uint8Array) => {
14. if (err != undefined) {
15. console.error(`Failed to get.code is ${err.code},message is ${err.message}`);
16. return;
17. }
18. console.info('Succeeded in getting');
19. });
20. }
21. })
22. } catch (e) {
23. let error = e as BusinessError;
24. console.error(`Failed to get.code is ${error.code},message is ${error.message}`);
25. }
```

### get

PhonePC/2in1TabletTVWearable

get(deviceId: string, key: string): Promise<boolean | string | number | Uint8Array>

获取与指定设备ID和Key匹配的值，使用Promise异步回调。

说明

其中deviceId通过调用[deviceManager.getAvailableDeviceListSync](js-apis-distributeddevicemanager.md#getavailabledevicelistsync)方法得到。

deviceId具体获取方式请参考[sync接口示例](js-apis-distributedkvstore.md#sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 标识要查询其数据的设备。 |
| key | string | 是 | 表示要查询Key值的键, 不能为空且长度不大于[MAX\_KEY\_LENGTH](js-apis-distributedkvstore.md#constants)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean|string|number|Uint8Array> | Promise对象。返回匹配给定条件的字符串值。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100003 | Database corrupted. |
| 15100004 | Not found. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. const KEY_TEST_STRING_ELEMENT = 'key_test_string_2';
4. const VALUE_TEST_STRING_ELEMENT = 'value-string-002';
5. try {
6. kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT).then(async () => {
7. console.info('Succeeded in putting');
8. if (kvStore != null) {
9. kvStore.get('localDeviceId', KEY_TEST_STRING_ELEMENT).then((data: boolean | string | number | Uint8Array) => {
10. console.info('Succeeded in getting');
11. }).catch((err: BusinessError) => {
12. console.error(`Failed to get.code is ${err.code},message is ${err.message}`);
13. });
14. }
15. }).catch((error: BusinessError) => {
16. console.error(`Failed to put.code is ${error.code},message is ${error.message}`);
17. });
18. } catch (e) {
19. let error = e as BusinessError;
20. console.error(`Failed to get.code is ${error.code},message is ${error.message}`);
21. }
```

### getEntries

PhonePC/2in1TabletTVWearable

getEntries(keyPrefix: string, callback: AsyncCallback<Entry[]>): void

获取匹配本设备指定键前缀的所有键值对，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyPrefix | string | 是 | 表示要匹配的键前缀。不能包含'^'，包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |
| callback | AsyncCallback<[Entry](js-apis-distributedkvstore.md#entry)[]> | 是 | 回调函数。返回匹配指定前缀的键值对列表。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let entries: distributedKVStore.Entry[] = [];
5. for (let i = 0; i < 10; i++) {
6. let key = 'batch_test_string_key';
7. let entry: distributedKVStore.Entry = {
8. key: key + i,
9. value: {
10. type: distributedKVStore.ValueType.STRING,
11. value: 'batch_test_string_value'
12. }
13. }
14. entries.push(entry);
15. }
16. console.info(`entries: ${entries}`);
17. kvStore.putBatch(entries, async (err: BusinessError) => {
18. if (err != undefined) {
19. console.error(`Failed to put Batch.code is ${err.code},message is ${err.message}`);
20. return;
21. }
22. console.info('Succeeded in putting Batch');
23. if (kvStore != null) {
24. kvStore.getEntries('batch_test_string_key', (err: BusinessError, entries: distributedKVStore.Entry[]) => {
25. if (err != undefined) {
26. console.error(`Failed to get Entries.code is ${err.code},message is ${err.message}`);
27. return;
28. }
29. console.info('Succeeded in getting Entries');
30. console.info(`entries.length: ${entries.length}`);
31. console.info(`entries[0]: ${entries[0]}`);
32. });
33. }
34. });
35. } catch (e) {
36. let error = e as BusinessError;
37. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message} `);
38. }
```

### getEntries

PhonePC/2in1TabletTVWearable

getEntries(keyPrefix: string): Promise<Entry[]>

获取匹配本设备指定键前缀的所有键值对，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyPrefix | string | 是 | 表示要匹配的键前缀。不能包含'^'，包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Entry](js-apis-distributedkvstore.md#entry)[]> | Promise对象。返回匹配指定前缀的键值对列表。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let entries: distributedKVStore.Entry[] = [];
5. for (let i = 0; i < 10; i++) {
6. let key = 'batch_test_string_key';
7. let entry: distributedKVStore.Entry = {
8. key: key + i,
9. value: {
10. type: distributedKVStore.ValueType.STRING,
11. value: 'batch_test_string_value'
12. }
13. }
14. entries.push(entry);
15. }
16. console.info(`entries: ${entries}`);
17. kvStore.putBatch(entries).then(async () => {
18. console.info('Succeeded in putting Batch');
19. if (kvStore != null) {
20. kvStore.getEntries('batch_test_string_key').then((entries: distributedKVStore.Entry[]) => {
21. console.info('Succeeded in getting Entries');
22. console.info(`PutBatch ${entries}`);
23. }).catch((err: BusinessError) => {
24. console.error(`Failed to get Entries.code is ${err.code},message is ${err.message}`);
25. });
26. }
27. }).catch((err: BusinessError) => {
28. console.error(`Failed to put Batch.code is ${err.code},message is ${err.message}`);
29. });
30. } catch (e) {
31. let error = e as BusinessError;
32. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message} `);
33. }
```

### getEntries

PhonePC/2in1TabletTVWearable

getEntries(deviceId: string, keyPrefix: string, callback: AsyncCallback<Entry[]>): void

获取与指定设备ID和Key前缀匹配的所有键值对，使用callback异步回调。

说明

其中deviceId通过调用[deviceManager.getAvailableDeviceListSync](js-apis-distributeddevicemanager.md#getavailabledevicelistsync)方法得到。

deviceId具体获取方式请参考[sync接口示例](js-apis-distributedkvstore.md#sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 标识要查询其数据的设备。 |
| keyPrefix | string | 是 | 表示要匹配的键前缀。不能包含'^'，包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |
| callback | AsyncCallback<[Entry](js-apis-distributedkvstore.md#entry)[]> | 是 | 回调函数，返回满足给定条件的所有键值对的列表。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let entries: distributedKVStore.Entry[] = [];
5. for (let i = 0; i < 10; i++) {
6. let key = 'batch_test_string_key';
7. let entry: distributedKVStore.Entry = {
8. key: key + i,
9. value: {
10. type: distributedKVStore.ValueType.STRING,
11. value: 'batch_test_string_value'
12. }
13. }
14. entries.push(entry);
15. }
16. console.info(`entries : ${entries}`);
17. kvStore.putBatch(entries, async (err: BusinessError) => {
18. if (err != undefined) {
19. console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
20. return;
21. }
22. console.info('Succeeded in putting batch');
23. if (kvStore != null) {
24. kvStore.getEntries('localDeviceId', 'batch_test_string_key', (err: BusinessError, entries: distributedKVStore.Entry[]) => {
25. if (err != undefined) {
26. console.error(`Failed to get entries.code is ${err.code},message is ${err.message}`);
27. return;
28. }
29. console.info('Succeeded in getting entries');
30. console.info(`entries.length: ${entries.length}`);
31. console.info(`entries[0]: ${entries[0]}`);
32. });
33. }
34. });
35. } catch (e) {
36. let error = e as BusinessError;
37. console.error(`Failed to put batch.code is ${error.code},message is ${error.message}`);
38. }
```

### getEntries

PhonePC/2in1TabletTVWearable

getEntries(deviceId: string, keyPrefix: string): Promise<Entry[]>

获取与指定设备ID和Key前缀匹配的所有键值对，使用Promise异步回调。

说明

其中deviceId通过调用[deviceManager.getAvailableDeviceListSync](js-apis-distributeddevicemanager.md#getavailabledevicelistsync)方法得到。

deviceId具体获取方式请参考[sync接口示例](js-apis-distributedkvstore.md#sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 标识要查询其数据的设备。 |
| keyPrefix | string | 是 | 表示要匹配的键前缀。不能包含'^'，包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Entry](js-apis-distributedkvstore.md#entry)[]> | Promise对象。返回匹配给定条件的所有键值对的列表。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let entries: distributedKVStore.Entry[] = [];
5. for (let i = 0; i < 10; i++) {
6. let key = 'batch_test_string_key';
7. let entry: distributedKVStore.Entry = {
8. key: key + i,
9. value: {
10. type: distributedKVStore.ValueType.STRING,
11. value: 'batch_test_string_value'
12. }
13. }
14. entries.push(entry);
15. }
16. console.info(`entries: ${entries}`);
17. kvStore.putBatch(entries).then(async () => {
18. console.info('Succeeded in putting batch');
19. if (kvStore != null) {
20. kvStore.getEntries('localDeviceId', 'batch_test_string_key').then((entries: distributedKVStore.Entry[]) => {
21. console.info('Succeeded in getting entries');
22. console.info(`entries.length: ${entries.length}`);
23. console.info(`entries[0]: ${entries[0]}`);
24. console.info(`entries[0].value: ${entries[0].value}`);
25. console.info(`entries[0].value.value: ${entries[0].value.value}`);
26. }).catch((err: BusinessError) => {
27. console.error(`Failed to get entries.code is ${err.code},message is ${err.message}`);
28. });
29. }
30. }).catch((err: BusinessError) => {
31. console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
32. });
33. } catch (e) {
34. let error = e as BusinessError;
35. console.error(`Failed to put batch.code is ${error.code},message is ${error.message}`);
36. }
```

### getEntries

PhonePC/2in1TabletTVWearable

getEntries(query: Query, callback: AsyncCallback<Entry[]>): void

获取本设备与指定Query对象匹配的键值对列表，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | [Query](js-apis-distributedkvstore.md#query) | 是 | 表示要匹配的键前缀。 |
| callback | AsyncCallback<[Entry](js-apis-distributedkvstore.md#entry)[]> | 是 | 回调函数。返回本设备与指定Query对象匹配的键值对列表。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let arr = new Uint8Array([21, 31]);
5. let entries: distributedKVStore.Entry[] = [];
6. for (let i = 0; i < 10; i++) {
7. let key = 'batch_test_bool_key';
8. let entry: distributedKVStore.Entry = {
9. key: key + i,
10. value: {
11. type: distributedKVStore.ValueType.BYTE_ARRAY,
12. value: arr
13. }
14. }
15. entries.push(entry);
16. }
17. console.info(`entries: {entries}`);
18. kvStore.putBatch(entries, (err: BusinessError) => {
19. console.info('Succeeded in putting Batch');
20. const query = new distributedKVStore.Query();
21. query.prefixKey("batch_test");
22. if (kvStore != null) {
23. kvStore.getEntries(query, (err: BusinessError, entries: distributedKVStore.Entry[]) => {
24. if (err != undefined) {
25. console.error(`Failed to get Entries.code is ${err.code},message is ${err.message}`);
26. return;
27. }
28. console.info('Succeeded in getting Entries');
29. console.info(`entries.length: ${entries.length}`);
30. console.info(`entries[0]: ${entries[0]}`);
31. });
32. }
33. });
34. } catch (e) {
35. let error = e as BusinessError;
36. console.error(`Failed to get Entries.code is ${error.code},message is ${error.message}`);
37. }
```

### getEntries

PhonePC/2in1TabletTVWearable

getEntries(query: Query): Promise<Entry[]>

获取本设备与指定Query对象匹配的键值对列表，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | [Query](js-apis-distributedkvstore.md#query) | 是 | 表示查询对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Entry](js-apis-distributedkvstore.md#entry)[]> | Promise对象。返回本设备与指定Query对象匹配的键值对列表。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let arr = new Uint8Array([21, 31]);
5. let entries: distributedKVStore.Entry[] = [];
6. for (let i = 0; i < 10; i++) {
7. let key = 'batch_test_bool_key';
8. let entry: distributedKVStore.Entry = {
9. key: key + i,
10. value: {
11. type: distributedKVStore.ValueType.BYTE_ARRAY,
12. value: arr
13. }
14. }
15. entries.push(entry);
16. }
17. console.info(`entries: {entries}`);
18. kvStore.putBatch(entries).then(async () => {
19. console.info('Succeeded in putting Batch');
20. const query = new distributedKVStore.Query();
21. query.prefixKey("batch_test");
22. if (kvStore != null) {
23. kvStore.getEntries(query).then((entries: distributedKVStore.Entry[]) => {
24. console.info('Succeeded in getting Entries');
25. }).catch((err: BusinessError) => {
26. console.error(`Failed to get Entries.code is ${err.code},message is ${err.message}`);
27. });
28. }
29. }).catch((err: BusinessError) => {
30. console.error(`Failed to get Entries.code is ${err.code},message is ${err.message}`)
31. });
32. console.info('Succeeded in getting Entries');
33. } catch (e) {
34. let error = e as BusinessError;
35. console.error(`Failed to get Entries.code is ${error.code},message is ${error.message}`);
36. }
```

### getEntries

PhonePC/2in1TabletTVWearable

getEntries(deviceId: string, query: Query, callback: AsyncCallback<Entry[]>): void

获取与指定设备ID和Query对象匹配的键值对列表，使用callback异步回调。

说明

其中deviceId通过调用[deviceManager.getAvailableDeviceListSync](js-apis-distributeddevicemanager.md#getavailabledevicelistsync)方法得到。

deviceId具体获取方式请参考[sync接口示例](js-apis-distributedkvstore.md#sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 设备的networkId。 |
| query | [Query](js-apis-distributedkvstore.md#query) | 是 | 表示查询对象。 |
| callback | AsyncCallback<[Entry](js-apis-distributedkvstore.md#entry)[]> | 是 | 回调函数。返回与指定设备ID和Query对象匹配的键值对列表。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let arr = new Uint8Array([21, 31]);
5. let entries: distributedKVStore.Entry[] = [];
6. for (let i = 0; i < 10; i++) {
7. let key = 'batch_test_bool_key';
8. let entry: distributedKVStore.Entry = {
9. key: key + i,
10. value: {
11. type: distributedKVStore.ValueType.BYTE_ARRAY,
12. value: arr
13. }
14. }
15. entries.push(entry);
16. }
17. console.info(`entries: ${entries}`);
18. kvStore.putBatch(entries, async (err: BusinessError) => {
19. if (err != undefined) {
20. console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
21. return;
22. }
23. console.info('Succeeded in putting batch');
24. let query = new distributedKVStore.Query();
25. query.deviceId('localDeviceId');
26. query.prefixKey("batch_test");
27. if (kvStore != null) {
28. kvStore.getEntries('localDeviceId', query, (err: BusinessError, entries: distributedKVStore.Entry[]) => {
29. if (err != undefined) {
30. console.error(`Failed to get entries.code is ${err.code},message is ${err.message}`);
31. return;
32. }
33. console.info('Succeeded in getting entries');
34. console.info(`entries.length: ${entries.length}`);
35. console.info(`entries[0]: ${entries[0]}`);
36. })
37. }
38. });
39. console.info('Succeeded in getting entries');
40. } catch (e) {
41. let error = e as BusinessError;
42. console.error(`Failed to get entries.code is ${error.code},message is ${error.message}`);
43. }
```

### getEntries

PhonePC/2in1TabletTVWearable

getEntries(deviceId: string, query: Query): Promise<Entry[]>

获取与指定设备ID和Query对象匹配的键值对列表，使用Promise异步回调。

说明

其中deviceId通过调用[deviceManager.getAvailableDeviceListSync](js-apis-distributeddevicemanager.md#getavailabledevicelistsync)方法得到。

deviceId具体获取方式请参考[sync接口示例](js-apis-distributedkvstore.md#sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 设备的networkId。 |
| query | [Query](js-apis-distributedkvstore.md#query) | 是 | 表示查询对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Entry](js-apis-distributedkvstore.md#entry)[]> | Promise对象。返回与指定设备ID和Query对象匹配的键值对列表。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let arr = new Uint8Array([21, 31]);
5. let entries: distributedKVStore.Entry[] = [];
6. for (let i = 0; i < 10; i++) {
7. let key = 'batch_test_bool_key';
8. let entry: distributedKVStore.Entry = {
9. key: key + i,
10. value: {
11. type: distributedKVStore.ValueType.BYTE_ARRAY,
12. value: arr
13. }
14. }
15. entries.push(entry);
16. }
17. console.info(`entries: ${entries}`);
18. kvStore.putBatch(entries).then(async () => {
19. console.info('Succeeded in putting batch');
20. let query = new distributedKVStore.Query();
21. query.deviceId('localDeviceId');
22. query.prefixKey("batch_test");
23. if (kvStore != null) {
24. kvStore.getEntries('localDeviceId', query).then((entries: distributedKVStore.Entry[]) => {
25. console.info('Succeeded in getting entries');
26. }).catch((err: BusinessError) => {
27. console.error(`Failed to get entries.code is ${err.code},message is ${err.message}`);
28. });
29. }
30. }).catch((err: BusinessError) => {
31. console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
32. });
33. console.info('Succeeded in getting entries');
34. } catch (e) {
35. let error = e as BusinessError;
36. console.error(`Failed to get entries.code is ${error.code},message is ${error.message}`);
37. }
```

### getResultSet

PhonePC/2in1TabletTVWearable

getResultSet(keyPrefix: string, callback: AsyncCallback<KVStoreResultSet>): void

从DeviceKVStore数据库中获取本设备具有指定前缀的结果集，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyPrefix | string | 是 | 表示要匹配的键前缀。不能包含'^'，包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |
| callback | AsyncCallback<[KVStoreResultSet](js-apis-distributedkvstore.md#kvstoreresultset)> | 是 | 回调函数。返回具有指定前缀的结果集。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100001 | Over max limits. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let resultSet: distributedKVStore.KVStoreResultSet;
5. let entries: distributedKVStore.Entry[] = [];
6. for (let i = 0; i < 10; i++) {
7. let key = 'batch_test_string_key';
8. let entry: distributedKVStore.Entry = {
9. key: key + i,
10. value: {
11. type: distributedKVStore.ValueType.STRING,
12. value: 'batch_test_string_value'
13. }
14. }
15. entries.push(entry);
16. }
17. kvStore.putBatch(entries, async (err: BusinessError) => {
18. if (err != undefined) {
19. console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
20. return;
21. }
22. console.info('Succeeded in putting batch');
23. if (kvStore != null) {
24. kvStore.getResultSet('batch_test_string_key', async (err: BusinessError, result: distributedKVStore.KVStoreResultSet) => {
25. if (err != undefined) {
26. console.error(`Failed to get resultset.code is ${err.code},message is ${err.message}`);
27. return;
28. }
29. console.info('Succeeded in getting result set');
30. resultSet = result;
31. if (kvStore != null) {
32. kvStore.closeResultSet(resultSet, (err: BusinessError) => {
33. if (err != undefined) {
34. console.error(`Failed to close resultset.code is ${err.code},message is ${err.message}`);
35. return;
36. }
37. console.info('Succeeded in closing result set');
38. })
39. }
40. });
41. }
42. });
43. } catch (e) {
44. let error = e as BusinessError;
45. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
46. }
```

### getResultSet

PhonePC/2in1TabletTVWearable

getResultSet(keyPrefix: string): Promise<KVStoreResultSet>

从DeviceKVStore数据库中获取本设备具有指定前缀的结果集，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyPrefix | string | 是 | 表示要匹配的键前缀。不能包含'^'，包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[KVStoreResultSet](js-apis-distributedkvstore.md#kvstoreresultset)> | Promise对象。返回具有指定前缀的结果集。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100001 | Over max limits. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let resultSet: distributedKVStore.KVStoreResultSet;
5. let entries: distributedKVStore.Entry[] = [];
6. for (let i = 0; i < 10; i++) {
7. let key = 'batch_test_string_key';
8. let entry: distributedKVStore.Entry = {
9. key: key + i,
10. value: {
11. type: distributedKVStore.ValueType.STRING,
12. value: 'batch_test_string_value'
13. }
14. }
15. entries.push(entry);
16. }
17. kvStore.putBatch(entries).then(async () => {
18. console.info('Succeeded in putting batch');
19. }).catch((err: BusinessError) => {
20. console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
21. });
22. kvStore.getResultSet('batch_test_string_key').then((result: distributedKVStore.KVStoreResultSet) => {
23. console.info('Succeeded in getting result set');
24. resultSet = result;
25. if (kvStore != null) {
26. kvStore.closeResultSet(resultSet).then(() => {
27. console.info('Succeeded in closing result set');
28. }).catch((err: BusinessError) => {
29. console.error(`Failed to close resultset.code is ${err.code},message is ${err.message}`);
30. });
31. }
32. }).catch((err: BusinessError) => {
33. console.error(`Failed to get resultset.code is ${err.code},message is ${err.message}`);
34. });
35. } catch (e) {
36. let error = e as BusinessError;
37. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
38. }
```

### getResultSet

PhonePC/2in1TabletTVWearable

getResultSet(deviceId: string, keyPrefix: string, callback: AsyncCallback<KVStoreResultSet>): void

获取与指定设备ID和Key前缀匹配的KVStoreResultSet对象，使用callback异步回调。

说明

其中deviceId通过调用[deviceManager.getAvailableDeviceListSync](js-apis-distributeddevicemanager.md#getavailabledevicelistsync)方法得到。

deviceId具体获取方式请参考[sync接口示例](js-apis-distributedkvstore.md#sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 标识要查询其数据的设备。 |
| keyPrefix | string | 是 | 表示要匹配的键前缀。不能包含'^'，包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |
| callback | AsyncCallback<[KVStoreResultSet](js-apis-distributedkvstore.md#kvstoreresultset)> | 是 | 回调函数。返回与指定设备ID和Key前缀匹配的KVStoreResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100001 | Over max limits. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let resultSet: distributedKVStore.KVStoreResultSet;
5. kvStore.getResultSet('localDeviceId', 'batch_test_string_key', async (err: BusinessError, result: distributedKVStore.KVStoreResultSet) => {
6. if (err != undefined) {
7. console.error(`Failed to get resultSet.code is ${err.code},message is ${err.message}`);
8. return;
9. }
10. console.info('Succeeded in getting resultSet');
11. resultSet = result;
12. if (kvStore != null) {
13. kvStore.closeResultSet(resultSet, (err: BusinessError) => {
14. if (err != undefined) {
15. console.error(`Failed to close resultSet.code is ${err.code},message is ${err.message}`);
16. return;
17. }
18. console.info('Succeeded in closing resultSet');
19. })
20. }
21. });
22. } catch (e) {
23. let error = e as BusinessError;
24. console.error(`Failed to get resultSet.code is ${error.code},message is ${error.message}`);
25. }
```

### getResultSet

PhonePC/2in1TabletTVWearable

getResultSet(deviceId: string, keyPrefix: string): Promise<KVStoreResultSet>

获取与指定设备ID和Key前缀匹配的KVStoreResultSet对象，使用Promise异步回调。

说明

其中deviceId通过调用[deviceManager.getAvailableDeviceListSync](js-apis-distributeddevicemanager.md#getavailabledevicelistsync)方法得到。

deviceId具体获取方式请参考[sync接口示例](js-apis-distributedkvstore.md#sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 标识要查询其数据的设备。 |
| keyPrefix | string | 是 | 表示要匹配的键前缀。不能包含'^'，包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[KVStoreResultSet](js-apis-distributedkvstore.md#kvstoreresultset)> | Promise对象。返回与指定设备ID和Key前缀匹配的KVStoreResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100001 | Over max limits. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let resultSet: distributedKVStore.KVStoreResultSet;
5. kvStore.getResultSet('localDeviceId', 'batch_test_string_key').then((result: distributedKVStore.KVStoreResultSet) => {
6. console.info('Succeeded in getting resultSet');
7. resultSet = result;
8. if (kvStore != null) {
9. kvStore.closeResultSet(resultSet).then(() => {
10. console.info('Succeeded in closing resultSet');
11. }).catch((err: BusinessError) => {
12. console.error(`Failed to close resultSet.code is ${err.code},message is ${err.message}`);
13. });
14. }
15. }).catch((err: BusinessError) => {
16. console.error(`Failed to get resultSet.code is ${err.code},message is ${err.message}`);
17. });
18. } catch (e) {
19. let error = e as BusinessError;
20. console.error(`Failed to get resultSet.code is ${error.code},message is ${error.message}`);
21. }
```

### getResultSet

PhonePC/2in1TabletTVWearable

getResultSet(deviceId: string, query: Query, callback: AsyncCallback<KVStoreResultSet>): void

获取与指定设备ID和Query对象匹配的KVStoreResultSet对象，使用callback异步回调。

说明

其中deviceId通过调用[deviceManager.getAvailableDeviceListSync](js-apis-distributeddevicemanager.md#getavailabledevicelistsync)方法得到。

deviceId具体获取方式请参考[sync接口示例](js-apis-distributedkvstore.md#sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | KVStoreResultSet对象所属的设备ID。 |
| query | [Query](js-apis-distributedkvstore.md#query) | 是 | 表示查询对象。 |
| callback | AsyncCallback<[KVStoreResultSet](js-apis-distributedkvstore.md#kvstoreresultset)> | 是 | 回调函数。返回与指定设备ID和Query对象匹配的KVStoreResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100001 | Over max limits. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let resultSet: distributedKVStore.KVStoreResultSet;
5. let entries: distributedKVStore.Entry[] = [];
6. for (let i = 0; i < 10; i++) {
7. let key = 'batch_test_string_key';
8. let entry: distributedKVStore.Entry = {
9. key: key + i,
10. value: {
11. type: distributedKVStore.ValueType.STRING,
12. value: 'batch_test_string_value'
13. }
14. }
15. entries.push(entry);
16. }
17. kvStore.putBatch(entries, async (err: BusinessError) => {
18. if (err != undefined) {
19. console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
20. return;
21. }
22. console.info('Succeeded in putting batch');
23. const query = new distributedKVStore.Query();
24. query.prefixKey("batch_test");
25. if (kvStore != null) {
26. kvStore.getResultSet('localDeviceId', query, async (err: BusinessError, result: distributedKVStore.KVStoreResultSet) => {
27. if (err != undefined) {
28. console.error(`Failed to get resultSet.code is ${err.code},message is ${err.message}`);
29. return;
30. }
31. console.info('Succeeded in getting resultSet');
32. resultSet = result;
33. if (kvStore != null) {
34. kvStore.closeResultSet(resultSet, (err: BusinessError) => {
35. if (err != undefined) {
36. console.error(`Failed to close resultSet.code is ${err.code},message is ${err.message}`);
37. return;
38. }
39. console.info('Succeeded in closing resultSet');
40. })
41. }
42. });
43. }
44. });
45. } catch (e) {
46. let error = e as BusinessError;
47. console.error(`Failed to get resultSet.code is ${error.code},message is ${error.message}`);
48. }
```

### getResultSet

PhonePC/2in1TabletTVWearable

getResultSet(deviceId: string, query: Query): Promise<KVStoreResultSet>

获取与指定设备ID和Query对象匹配的KVStoreResultSet对象，使用Promise异步回调。

说明

其中deviceId通过调用[deviceManager.getAvailableDeviceListSync](js-apis-distributeddevicemanager.md#getavailabledevicelistsync)方法得到。

deviceId具体获取方式请参考[sync接口示例](js-apis-distributedkvstore.md#sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | KVStoreResultSet对象所属的设备ID。 |
| query | [Query](js-apis-distributedkvstore.md#query) | 是 | 表示查询对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[KVStoreResultSet](js-apis-distributedkvstore.md#kvstoreresultset)> | Promise对象。返回与指定设备ID和Query对象匹配的KVStoreResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100001 | Over max limits. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let resultSet: distributedKVStore.KVStoreResultSet;
5. let entries: distributedKVStore.Entry[] = [];
6. for (let i = 0; i < 10; i++) {
7. let key = 'batch_test_string_key';
8. let entry: distributedKVStore.Entry = {
9. key: key + i,
10. value: {
11. type: distributedKVStore.ValueType.STRING,
12. value: 'batch_test_string_value'
13. }
14. }
15. entries.push(entry);
16. }
17. kvStore.putBatch(entries).then(async () => {
18. console.info('Succeeded in putting batch');
19. }).catch((err: BusinessError) => {
20. console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
21. });
22. const query = new distributedKVStore.Query();
23. query.prefixKey("batch_test");
24. if (kvStore != null) {
25. kvStore.getResultSet('localDeviceId', query).then((result: distributedKVStore.KVStoreResultSet) => {
26. console.info('Succeeded in getting resultSet');
27. resultSet = result;
28. if (kvStore != null) {
29. kvStore.closeResultSet(resultSet).then(() => {
30. console.info('Succeeded in closing resultSet');
31. }).catch((err: BusinessError) => {
32. console.error(`Failed to close resultSet.code is ${err.code},message is ${err.message}`);
33. });
34. }
35. }).catch((err: BusinessError) => {
36. console.error(`Failed to get resultSet.code is ${err.code},message is ${err.message}`);
37. });
38. }
39. query.deviceId('localDeviceId');
40. console.info("GetResultSet " + query.getSqlLike());

42. } catch (e) {
43. let error = e as BusinessError;
44. console.error(`Failed to get resultSet.code is ${error.code},message is ${error.message}`);
45. }
```

### getResultSet

PhonePC/2in1TabletTVWearable

getResultSet(query: Query): Promise<KVStoreResultSet>

获取与本设备指定Query对象匹配的KVStoreResultSet对象，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | [Query](js-apis-distributedkvstore.md#query) | 是 | 表示查询对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[KVStoreResultSet](js-apis-distributedkvstore.md#kvstoreresultset)> | Promise对象。获取与本设备指定Query对象匹配的KVStoreResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100001 | Over max limits. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let resultSet: distributedKVStore.KVStoreResultSet;
5. let entries: distributedKVStore.Entry[] = [];
6. for (let i = 0; i < 10; i++) {
7. let key = 'batch_test_string_key';
8. let entry: distributedKVStore.Entry = {
9. key: key + i,
10. value: {
11. type: distributedKVStore.ValueType.STRING,
12. value: 'batch_test_string_value'
13. }
14. }
15. entries.push(entry);
16. }
17. kvStore.putBatch(entries).then(async () => {
18. console.info('Succeeded in putting batch');
19. }).catch((err: BusinessError) => {
20. console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
21. });
22. const query = new distributedKVStore.Query();
23. query.prefixKey("batch_test");
24. kvStore.getResultSet(query).then((result: distributedKVStore.KVStoreResultSet) => {
25. console.info('Succeeded in getting result set');
26. resultSet = result;
27. }).catch((err: BusinessError) => {
28. console.error(`Failed to get resultset.code is ${err.code},message is ${err.message}`);
29. });
30. } catch (e) {
31. let error = e as BusinessError;
32. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
33. }
```

### getResultSet

PhonePC/2in1TabletTVWearable

getResultSet(query: Query, callback:AsyncCallback<KVStoreResultSet>): void

获取与本设备指定Query对象匹配的KVStoreResultSet对象，使用callback异步回调。

说明

其中deviceId通过调用[deviceManager.getAvailableDeviceListSync](js-apis-distributeddevicemanager.md#getavailabledevicelistsync)方法得到。

deviceId具体获取方式请参考[sync接口示例](js-apis-distributedkvstore.md#sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | [Query](js-apis-distributedkvstore.md#query) | 是 | 表示查询对象。 |
| callback | AsyncCallback<[KVStoreResultSet](js-apis-distributedkvstore.md#kvstoreresultset)> | 是 | 回调函数，获取与指定Predicates对象匹配的KVStoreResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100001 | Over max limits. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let resultSet: distributedKVStore.KVStoreResultSet;
5. let entries: distributedKVStore.Entry[] = [];
6. for (let i = 0; i < 10; i++) {
7. let key = 'batch_test_string_key';
8. let entry: distributedKVStore.Entry = {
9. key: key + i,
10. value: {
11. type: distributedKVStore.ValueType.STRING,
12. value: 'batch_test_string_value'
13. }
14. }
15. entries.push(entry);
16. }
17. kvStore.putBatch(entries, async (err: BusinessError) => {
18. if (err != undefined) {
19. console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
20. return;
21. }
22. console.info('Succeeded in putting batch');
23. const query = new distributedKVStore.Query();
24. query.prefixKey("batch_test");
25. if (kvStore != null) {
26. kvStore.getResultSet(query, async (err: BusinessError, result: distributedKVStore.KVStoreResultSet) => {
27. if (err != undefined) {
28. console.error(`Failed to get resultSet.code is ${err.code},message is ${err.message}`);
29. return;
30. }
31. console.info('Succeeded in getting resultSet');
32. resultSet = result;
33. if (kvStore != null) {
34. kvStore.closeResultSet(resultSet, (err: BusinessError) => {
35. if (err != undefined) {
36. console.error(`Failed to close resultSet.code is ${err.code},message is ${err.message}`);
37. return;
38. }
39. console.info('Succeeded in closing resultSet');
40. })
41. }
42. });
43. }
44. });
45. } catch (e) {
46. let error = e as BusinessError;
47. console.error(`Failed to get resultSet`);
48. }
```

### getResultSize

PhonePC/2in1TabletTVWearable

getResultSize(query: Query, callback: AsyncCallback<number>): void

获取与本设备指定Query对象匹配的结果数，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | [Query](js-apis-distributedkvstore.md#query) | 是 | 表示查询对象。 |
| callback | AsyncCallback<number> | 是 | 回调函数。返回与本设备指定Query对象匹配的结果数。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100004 | Not found. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let entries: distributedKVStore.Entry[] = [];
5. for (let i = 0; i < 10; i++) {
6. let key = 'batch_test_string_key';
7. let entry: distributedKVStore.Entry = {
8. key: key + i,
9. value: {
10. type: distributedKVStore.ValueType.STRING,
11. value: 'batch_test_string_value'
12. }
13. }
14. entries.push(entry);
15. }
16. kvStore.putBatch(entries, (err: BusinessError) => {
17. console.info('Succeeded in putting batch');
18. const query = new distributedKVStore.Query();
19. query.prefixKey("batch_test");
20. if (kvStore != null) {
21. kvStore.getResultSize(query, (err: BusinessError, resultSize: number) => {
22. if (err != undefined) {
23. console.error(`Failed to get result size.code is ${err.code},message is ${err.message}`);
24. return;
25. }
26. console.info('Succeeded in getting result set size');
27. });
28. }
29. });
30. } catch (e) {
31. let error = e as BusinessError;
32. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
33. }
```

### getResultSize

PhonePC/2in1TabletTVWearable

getResultSize(query: Query): Promise<number>

获取与本设备指定Query对象匹配的结果数，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | [Query](js-apis-distributedkvstore.md#query) | 是 | 表示查询对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。获取与本设备指定Query对象匹配的结果数。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100004 | Not found. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let entries: distributedKVStore.Entry[] = [];
5. for (let i = 0; i < 10; i++) {
6. let key = 'batch_test_string_key';
7. let entry: distributedKVStore.Entry = {
8. key: key + i,
9. value: {
10. type: distributedKVStore.ValueType.STRING,
11. value: 'batch_test_string_value'
12. }
13. }
14. entries.push(entry);
15. }
16. kvStore.putBatch(entries).then(async () => {
17. console.info('Succeeded in putting batch');
18. }).catch((err: BusinessError) => {
19. console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
20. });
21. const query = new distributedKVStore.Query();
22. query.prefixKey("batch_test");
23. kvStore.getResultSize(query).then((resultSize: number) => {
24. console.info('Succeeded in getting result set size');
25. }).catch((err: BusinessError) => {
26. console.error(`Failed to get result size.code is ${err.code},message is ${err.message}`);
27. });
28. } catch (e) {
29. let error = e as BusinessError;
30. console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
31. }
```

### getResultSize

PhonePC/2in1TabletTVWearable

getResultSize(deviceId: string, query: Query, callback: AsyncCallback<number>): void;

获取与指定设备ID和Query对象匹配的结果数，使用callback异步回调。

说明

其中deviceId通过调用[deviceManager.getAvailableDeviceListSync](js-apis-distributeddevicemanager.md#getavailabledevicelistsync)方法得到。

deviceId具体获取方式请参考[sync接口示例](js-apis-distributedkvstore.md#sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | KVStoreResultSet对象所属的设备ID。 |
| query | [Query](js-apis-distributedkvstore.md#query) | 是 | 表示查询对象。 |
| callback | AsyncCallback<number> | 是 | 回调函数。返回与指定设备ID和Query对象匹配的结果数。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100004 | Not found. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let entries: distributedKVStore.Entry[] = [];
5. for (let i = 0; i < 10; i++) {
6. let key = 'batch_test_string_key';
7. let entry: distributedKVStore.Entry = {
8. key: key + i,
9. value: {
10. type: distributedKVStore.ValueType.STRING,
11. value: 'batch_test_string_value'
12. }
13. }
14. entries.push(entry);
15. }
16. kvStore.putBatch(entries, (err: BusinessError) => {
17. if (err != undefined) {
18. console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
19. return;
20. }
21. console.info('Succeeded in putting batch');
22. const query = new distributedKVStore.Query();
23. query.prefixKey("batch_test");
24. if (kvStore != null) {
25. kvStore.getResultSize('localDeviceId', query, (err: BusinessError, resultSize: number) => {
26. if (err != undefined) {
27. console.error(`Failed to get resultSize.code is ${err.code},message is ${err.message}`);
28. return;
29. }
30. console.info('Succeeded in getting resultSize');
31. });
32. }
33. });
34. } catch (e) {
35. let error = e as BusinessError;
36. console.error(`Failed to get resultSize.code is ${error.code},message is ${error.message}`);
37. }
```

### getResultSize

PhonePC/2in1TabletTVWearable

getResultSize(deviceId: string, query: Query): Promise<number>

获取与指定设备ID和Query对象匹配的结果数，使用Promise异步回调。

说明

其中deviceId通过调用[deviceManager.getAvailableDeviceListSync](js-apis-distributeddevicemanager.md#getavailabledevicelistsync)方法得到。

deviceId具体获取方式请参考[sync接口示例](js-apis-distributedkvstore.md#sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | KVStoreResultSet对象所属的设备ID。 |
| query | [Query](js-apis-distributedkvstore.md#query) | 是 | 表示查询对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回与指定设备ID和Query对象匹配的结果数。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](errorcode-distributedkvstore.md)和[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100004 | Not found. |
| 15100005 | Database or result set already closed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. let entries: distributedKVStore.Entry[] = [];
5. for (let i = 0; i < 10; i++) {
6. let key = 'batch_test_string_key';
7. let entry: distributedKVStore.Entry = {
8. key: key + i,
9. value: {
10. type: distributedKVStore.ValueType.STRING,
11. value: 'batch_test_string_value'
12. }
13. }
14. entries.push(entry);
15. }
16. kvStore.putBatch(entries).then(async () => {
17. console.info('Succeeded in putting batch');
18. }).catch((err: BusinessError) => {
19. console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
20. });
21. let query = new distributedKVStore.Query();
22. query.prefixKey("batch_test");
23. kvStore.getResultSize('localDeviceId', query).then((resultSize: number) => {
24. console.info('Succeeded in getting resultSize');
25. }).catch((err: BusinessError) => {
26. console.error(`Failed to get resultSize.code is ${err.code},message is ${err.message}`);
27. });
28. } catch (e) {
29. let error = e as BusinessError;
30. console.error(`Failed to get resultSize.code is ${error.code},message is ${error.message}`);
31. }
```
