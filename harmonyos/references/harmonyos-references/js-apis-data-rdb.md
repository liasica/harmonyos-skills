---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-rdb
title: @ohos.data.rdb (关系型数据库)
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > ArkTS API > 已停止维护的接口 > @ohos.data.rdb (关系型数据库)
category: harmonyos-references
scraped_at: 2026-04-28T07:59:24+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5e6dd303b2e93a9c5caa7cda2511efd390d590646c2138e7ade4bf54a6688f65
---

关系型数据库（Relational Database，RDB）是一种基于关系模型来管理数据的数据库。关系型数据库基于SQLite组件提供了一套完整的对本地数据库进行管理的机制，对外提供了一系列的增、删、改、查等接口，也可以直接运行用户输入的SQL语句来满足复杂的场景需要。不支持Worker线程。

该模块提供以下关系型数据库相关的常用功能：

* [RdbPredicates](js-apis-data-rdb.md#rdbpredicates)：数据库中用来代表数据实体的性质、特征或者数据实体之间关系的词项，主要用来定义数据库的操作条件。
* [RdbStore](js-apis-data-rdb.md#rdbstore)：提供管理关系数据库（RDB）方法的接口。

说明

* 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 从API version 9开始，该接口不再维护，推荐使用新接口[@ohos.data.relationalStore](arkts-apis-data-relationalstore.md)。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import data_rdb from '@ohos.data.rdb';
```

## data\_rdb.getRdbStore

PhonePC/2in1TabletTVWearable

getRdbStore(context: Context, config: StoreConfig, version: number, callback: AsyncCallback<RdbStore>): void

获得一个相关的RdbStore，操作关系型数据库，用户可以根据自己的需求配置RdbStore的参数，然后通过RdbStore调用相关接口可以执行相关的数据操作，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用的上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-app-context.md)。 |
| config | [StoreConfig](js-apis-data-rdb.md#storeconfig) | 是 | 与此RDB存储相关的数据库配置。 |
| version | number | 是 | 数据库版本。  目前暂不支持通过version自动识别数据库升级降级操作，只能由开发者自行维护。 |
| callback | AsyncCallback<[RdbStore](js-apis-data-rdb.md#rdbstore)> | 是 | 指定callback回调函数，返回RdbStore对象。 |

**示例：**

FA模型示例：

```
1. import featureAbility from '@ohos.ability.featureAbility';
2. import relationalStore from '@ohos.data.relationalStore';
3. import window from '@ohos.window';
4. import { BusinessError } from '@ohos.base';

6. const STORE_CONFIG: data_rdb.StoreConfig = { name: "RdbTest.db"}
7. data_rdb.getRdbStore(this.context, STORE_CONFIG, 1, (err, rdbStore) => {
8. if (err) {
9. console.info("Get RdbStore failed, err: " + err)
10. return
11. }
12. console.log("Get RdbStore successfully.")
13. })
```

Stage模型示例：

```
1. import UIAbility from '@ohos.app.ability.UIAbility';
2. import { BusinessError } from "@ohos.base";
3. import window from '@ohos.window';

5. const STORE_CONFIG: data_rdb.StoreConfig = { name: "RdbTest.db"}
6. class EntryAbility extends UIAbility {
7. onWindowStageCreate(windowStage: window.WindowStage){
8. data_rdb.getRdbStore(this.context, STORE_CONFIG, 1, (err: BusinessError, rdbStore: data_rdb.RdbStore) => {
9. if (err) {
10. console.info("Get RdbStore failed, err: " + err)
11. return
12. }
13. console.log("Get RdbStore successfully.")
14. })
15. }
16. }
```

## data\_rdb.getRdbStore

PhonePC/2in1TabletTVWearable

getRdbStore(context: Context, config: StoreConfig, version: number): Promise<RdbStore>

获得一个相关的RdbStore，操作关系型数据库，用户可以根据自己的需求配置RdbStore的参数，然后通过RdbStore调用相关接口可以执行相关的数据操作，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用的上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-app-context.md)。 |
| config | [StoreConfig](js-apis-data-rdb.md#storeconfig) | 是 | 与此RDB存储相关的数据库配置。 |
| version | number | 是 | 数据库版本。  目前暂不支持通过version自动识别数据库升级降级操作，只能由开发者自行维护。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[RdbStore](js-apis-data-rdb.md#rdbstore)> | Promise对象。返回RdbStore对象。 |

**示例：**

FA模型示例：

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. const STORE_CONFIG: data_rdb.StoreConfig = { name: "RdbTest.db"}
4. let promise = data_rdb.getRdbStore(this.context, STORE_CONFIG, 1);
5. promise.then(async (rdbStore) => {
6. console.log("Get RdbStore successfully.")
7. }).catch((err: BusinessError) => {
8. console.log("Get RdbStore failed, err: " + err)
9. })
```

Stage模型示例：

```
1. import UIAbility from '@ohos.app.ability.UIAbility';
2. import { BusinessError } from "@ohos.base";
3. import window from '@ohos.window';

5. const STORE_CONFIG: data_rdb.StoreConfig = { name: "RdbTest.db"}
6. class EntryAbility extends UIAbility {
7. onWindowStageCreate(windowStage: window.WindowStage){
8. context = this.context
9. }
10. }

12. // 获取context后调用getRdbStore
13. let promise = data_rdb.getRdbStore(this.context, STORE_CONFIG, 1);
14. promise.then(async (rdbStore: data_rdb.RdbStore) => {
15. console.log("Get RdbStore successfully.")
16. }).catch((err: BusinessError) => {
17. console.log("Get RdbStore failed, err: " + err)
18. })
```

## data\_rdb.deleteRdbStore

PhonePC/2in1TabletTVWearable

deleteRdbStore(context: Context, name: string, callback: AsyncCallback<void>): void

删除数据库，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用的上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-app-context.md)。 |
| name | string | 是 | 数据库名称。 |
| callback | AsyncCallback<void> | 是 | 指定callback回调函数。 |

**示例：**

FA模型示例：

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. data_rdb.deleteRdbStore(this.context, "RdbTest.db", (err) => {
4. if (err) {
5. console.info("Delete RdbStore failed, err: " + err)
6. return
7. }
8. console.log("Delete RdbStore successfully.")
9. })
```

Stage模型示例：

```
1. import UIAbility from '@ohos.app.ability.UIAbility';
2. import window from '@ohos.window';

4. class EntryAbility extends UIAbility {
5. onWindowStageCreate(windowStage: window.WindowStage){
6. context = this.context
7. }
8. }

10. // 获取context后调用deleteRdbStore
11. data_rdb.deleteRdbStore(this.context, "RdbTest.db", (err) => {
12. if (err) {
13. console.info("Delete RdbStore failed, err: " + err)
14. return
15. }
16. console.log("Delete RdbStore successfully.")
17. })
```

## data\_rdb.deleteRdbStore

PhonePC/2in1TabletTVWearable

deleteRdbStore(context: Context, name: string): Promise<void>

使用指定的数据库文件配置删除数据库，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用的上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-app-context.md)。 |
| name | string | 是 | 数据库名称。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

FA模型示例：

```
1. import featureAbility from '@ohos.ability.featureAbility';

3. let promise = data_rdb.deleteRdbStore(this.context, "RdbTest.db")
4. promise.then(() => {
5. console.log("Delete RdbStore successfully.")
6. }).catch((err: BusinessError) => {
7. console.info("Delete RdbStore failed, err: " + err)
8. })
```

Stage模型示例：

```
1. import UIAbility from '@ohos.app.ability.UIAbility';
2. import { BusinessError } from "@ohos.base";
3. import window from '@ohos.window';

5. class EntryAbility extends UIAbility {
6. onWindowStageCreate(windowStage: window.WindowStage){
7. context = this.context
8. }
9. }

11. // 获取context后调用deleteRdbStore
12. let promise = data_rdb.deleteRdbStore(this.context, "RdbTest.db")
13. promise.then(()=>{
14. console.log("Delete RdbStore successfully.")
15. }).catch((err: BusinessError) => {
16. console.info("Delete RdbStore failed, err: " + err)
17. })
```

## ValueType

PhonePC/2in1TabletTVWearable

type ValueType = number | string | boolean

用于表示允许的数据字段类型。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 类型 | 说明 |
| --- | --- |
| number | 表示值类型为数字。 |
| string | 表示值类型为字符。 |
| boolean | 表示值类型为布尔值。 |

## ValuesBucket

PhonePC/2in1TabletTVWearable

type ValuesBucket = { [key: string]: ValueType | Uint8Array | null }

用于存储键值对的类型。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 键类型 | 值类型 |
| --- | --- |
| string | [ValueType](js-apis-data-rdb.md#valuetype)| Uint8Array | null |

## SyncMode8+

PhonePC/2in1TabletTVWearable

指数据库同步模式。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SYNC\_MODE\_PUSH | 0 | 表示数据从本地设备推送到远程设备。 |
| SYNC\_MODE\_PULL | 1 | 表示数据从远程设备拉至本地设备。 |

## SubscribeType8+

PhonePC/2in1TabletTVWearable

描述订阅类型。

**需要权限：** ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUBSCRIBE\_TYPE\_REMOTE | 0 | 订阅远程数据更改。 |

## StoreConfig

PhonePC/2in1TabletTVWearable

管理关系数据库配置。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 数据库文件名。 |

## RdbPredicates

PhonePC/2in1TabletTVWearable

表示关系型数据库（RDB）的谓词。该类确定RDB中条件表达式的值是true还是false。

### constructor

PhonePC/2in1TabletTVWearable

constructor(name: string)

构造函数。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 数据库表名。 |

**示例：**

```
1. let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
```

### inDevices8+

PhonePC/2in1TabletTVWearable

inDevices(devices: Array<string>): RdbPredicates

同步分布式数据库时连接到组网内指定的远程设备。

说明

其中devices通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| devices | Array<string> | 是 | 指定的组网内的远程设备ID。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](js-apis-data-rdb.md#rdbpredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. import deviceManager from '@ohos.distributedHardware.deviceManager';

3. let dmInstance: deviceManager.DeviceManager;
4. let deviceIds: Array<string> = [];
5. let devices: Array<string> = [];

7. deviceManager.createDeviceManager("com.example.appdatamgrverify", (err: BusinessError, manager: void) => {
8. if (err) {
9. console.log("create device manager failed, err=" + err);
10. return;
11. }
12. dmInstance = manager;
13. devices = dmInstance.getTrustedDeviceListSync();
14. for (let i = 0; i < devices.length; i++) {
15. deviceIds[i] = devices[i].deviceId;
16. }
17. })

19. let predicates = new data_rdb.RdbPredicates("EMPLOYEE");
20. predicates.inDevices(deviceIds);

22. let predicates = new data_rdb.RdbPredicates("EMPLOYEE");
23. predicates.inDevices(deviceIds);
```

### inAllDevices8+

PhonePC/2in1TabletTVWearable

inAllDevices(): RdbPredicates

同步分布式数据库时连接到组网内所有的远程设备。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](js-apis-data-rdb.md#rdbpredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
2. predicates.inAllDevices()
```

### equalTo

PhonePC/2in1TabletTVWearable

equalTo(field: string, value: ValueType): RdbPredicates

配置谓词以匹配数据字段为ValueType且值等于指定值的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | [ValueType](js-apis-data-rdb.md#valuetype) | 是 | 指示要与谓词匹配的值。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](js-apis-data-rdb.md#rdbpredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
2. predicates.equalTo("NAME", "lisi")
```

### notEqualTo

PhonePC/2in1TabletTVWearable

notEqualTo(field: string, value: ValueType): RdbPredicates

配置谓词以匹配数据字段为ValueType且值不等于指定值的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | [ValueType](js-apis-data-rdb.md#valuetype) | 是 | 指示要与谓词匹配的值。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](js-apis-data-rdb.md#rdbpredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
2. predicates.notEqualTo("NAME", "lisi")
```

### beginWrap

PhonePC/2in1TabletTVWearable

beginWrap(): RdbPredicates

向谓词添加左括号。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](js-apis-data-rdb.md#rdbpredicates) | 返回带有左括号的Rdb谓词。 |

**示例：**

```
1. let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
2. predicates.equalTo("NAME", "lisi")
3. .beginWrap()
4. .equalTo("AGE", 18)
5. .or()
6. .equalTo("SALARY", 200.5)
7. .endWrap()
```

### endWrap

PhonePC/2in1TabletTVWearable

endWrap(): RdbPredicates

向谓词添加右括号。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](js-apis-data-rdb.md#rdbpredicates) | 返回带有右括号的Rdb谓词。 |

**示例：**

```
1. let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
2. predicates.equalTo("NAME", "lisi")
3. .beginWrap()
4. .equalTo("AGE", 18)
5. .or()
6. .equalTo("SALARY", 200.5)
7. .endWrap()
```

### or

PhonePC/2in1TabletTVWearable

or(): RdbPredicates

将或条件添加到谓词中。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](js-apis-data-rdb.md#rdbpredicates) | 返回带有或条件的Rdb谓词。 |

**示例：**

```
1. let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
2. predicates.equalTo("NAME", "Lisa")
3. .or()
4. .equalTo("NAME", "Rose")
```

### and

PhonePC/2in1TabletTVWearable

and(): RdbPredicates

向谓词添加和条件。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](js-apis-data-rdb.md#rdbpredicates) | 返回带有和条件的Rdb谓词。 |

**示例：**

```
1. let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
2. predicates.equalTo("NAME", "Lisa")
3. .and()
4. .equalTo("SALARY", 200.5)
```

### contains

PhonePC/2in1TabletTVWearable

contains(field: string, value: string): RdbPredicates

配置谓词以匹配数据字段为string且value包含指定值的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | string | 是 | 指示要与谓词匹配的值。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](js-apis-data-rdb.md#rdbpredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
2. predicates.contains("NAME", "os")
```

### beginsWith

PhonePC/2in1TabletTVWearable

beginsWith(field: string, value: string): RdbPredicates

配置谓词以匹配数据字段为string且值以指定字符串开头的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | string | 是 | 指示要与谓词匹配的值。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](js-apis-data-rdb.md#rdbpredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
2. predicates.beginsWith("NAME", "os")
```

### endsWith

PhonePC/2in1TabletTVWearable

endsWith(field: string, value: string): RdbPredicates

配置谓词以匹配数据字段为string且值以指定字符串结尾的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | string | 是 | 指示要与谓词匹配的值。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](js-apis-data-rdb.md#rdbpredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
2. predicates.endsWith("NAME", "se")
```

### isNull

PhonePC/2in1TabletTVWearable

isNull(field: string): RdbPredicates

配置谓词以匹配值为null的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](js-apis-data-rdb.md#rdbpredicates) | 返回与指定字段匹配的谓词。 |

**示例**：

```
1. let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
2. predicates.isNull("NAME")
```

### isNotNull

PhonePC/2in1TabletTVWearable

isNotNull(field: string): RdbPredicates

配置谓词以匹配值不为null的指定字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](js-apis-data-rdb.md#rdbpredicates) | 返回与指定字段匹配的谓词。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
2. predicates.isNotNull("NAME")
```

### like

PhonePC/2in1TabletTVWearable

like(field: string, value: string): RdbPredicates

配置谓词以匹配数据字段为string且值类似于指定字符串的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | string | 是 | 指示要与谓词匹配的值。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](js-apis-data-rdb.md#rdbpredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
2. predicates.like("NAME", "%os%")
```

### glob

PhonePC/2in1TabletTVWearable

glob(field: string, value: string): RdbPredicates

配置RdbPredicates匹配数据字段为string的指定字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | string | 是 | 指示要与谓词匹配的值。  支持通配符，\*表示0个、1个或多个数字或字符，?表示1个数字或字符。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](js-apis-data-rdb.md#rdbpredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
2. predicates.glob("NAME", "?h*g")
```

### between

PhonePC/2in1TabletTVWearable

between(field: string, low: ValueType, high: ValueType): RdbPredicates

将谓词配置为匹配数据字段为ValueType且value在给定范围内的指定字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| low | [ValueType](js-apis-data-rdb.md#valuetype) | 是 | 指示与谓词匹配的最小值。 |
| high | [ValueType](js-apis-data-rdb.md#valuetype) | 是 | 指示要与谓词匹配的最大值。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](js-apis-data-rdb.md#rdbpredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
2. predicates.between("AGE", 10, 50)
```

### notBetween

PhonePC/2in1TabletTVWearable

notBetween(field: string, low: ValueType, high: ValueType): RdbPredicates

配置RdbPredicates以匹配数据字段为ValueType且value超出给定范围的指定字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| low | [ValueType](js-apis-data-rdb.md#valuetype) | 是 | 指示与谓词匹配的最小值。 |
| high | [ValueType](js-apis-data-rdb.md#valuetype) | 是 | 指示要与谓词匹配的最大值。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](js-apis-data-rdb.md#rdbpredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
2. predicates.notBetween("AGE", 10, 50)
```

### greaterThan

PhonePC/2in1TabletTVWearable

greaterThan(field: string, value: ValueType): RdbPredicates

配置谓词以匹配数据字段为ValueType且值大于指定值的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | [ValueType](js-apis-data-rdb.md#valuetype) | 是 | 指示要与谓词匹配的值。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](js-apis-data-rdb.md#rdbpredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
2. predicates.greaterThan("AGE", 18)
```

### lessThan

PhonePC/2in1TabletTVWearable

lessThan(field: string, value: ValueType): RdbPredicates

配置谓词以匹配数据字段为valueType且value小于指定值的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | [ValueType](js-apis-data-rdb.md#valuetype) | 是 | 指示要与谓词匹配的值。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](js-apis-data-rdb.md#rdbpredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
2. predicates.lessThan("AGE", 20)
```

### greaterThanOrEqualTo

PhonePC/2in1TabletTVWearable

greaterThanOrEqualTo(field: string, value: ValueType): RdbPredicates

配置谓词以匹配数据字段为ValueType且value大于或等于指定值的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | [ValueType](js-apis-data-rdb.md#valuetype) | 是 | 指示要与谓词匹配的值。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](js-apis-data-rdb.md#rdbpredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
2. predicates.greaterThanOrEqualTo("AGE", 18)
```

### lessThanOrEqualTo

PhonePC/2in1TabletTVWearable

lessThanOrEqualTo(field: string, value: ValueType): RdbPredicates

配置谓词以匹配数据字段为ValueType且value小于或等于指定值的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | [ValueType](js-apis-data-rdb.md#valuetype) | 是 | 指示要与谓词匹配的值。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](js-apis-data-rdb.md#rdbpredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
2. predicates.lessThanOrEqualTo("AGE", 20)
```

### orderByAsc

PhonePC/2in1TabletTVWearable

orderByAsc(field: string): RdbPredicates

配置谓词以匹配其值按升序排序的列。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](js-apis-data-rdb.md#rdbpredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
2. predicates.orderByAsc("NAME")
```

### orderByDesc

PhonePC/2in1TabletTVWearable

orderByDesc(field: string): RdbPredicates

配置谓词以匹配其值按降序排序的列。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](js-apis-data-rdb.md#rdbpredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
2. predicates.orderByDesc("AGE")
```

### distinct

PhonePC/2in1TabletTVWearable

distinct(): RdbPredicates

配置谓词以过滤重复记录并仅保留其中一个。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](js-apis-data-rdb.md#rdbpredicates) | 返回可用于过滤重复记录的谓词。 |

**示例：**

```
1. let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
2. predicates.equalTo("NAME", "Rose").distinct()
```

### limitAs

PhonePC/2in1TabletTVWearable

limitAs(value: number): RdbPredicates

设置最大数据记录数的谓词。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 最大数据记录数。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](js-apis-data-rdb.md#rdbpredicates) | 返回可用于设置最大数据记录数的谓词。 |

**示例：**

```
1. let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
2. predicates.equalTo("NAME", "Rose").limitAs(3)
```

### offsetAs

PhonePC/2in1TabletTVWearable

offsetAs(rowOffset: number): RdbPredicates

配置RdbPredicates以指定返回结果的起始位置。需要同步调用limitAs接口指定查询数量，否则将无查询结果。如需查询指定偏移位置后的所有行，limitAs接口调用需传参数-1。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rowOffset | number | 是 | 返回结果的起始位置，取值为正整数。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](js-apis-data-rdb.md#rdbpredicates) | 返回具有指定返回结果起始位置的谓词。 |

**示例：**

```
1. let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
2. predicates.equalTo("NAME", "Rose").limitAs(-1).offsetAs(3)
```

### groupBy

PhonePC/2in1TabletTVWearable

groupBy(fields: Array<string>): RdbPredicates

配置RdbPredicates按指定列分组查询结果。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fields | Array<string> | 是 | 指定分组依赖的列名。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](js-apis-data-rdb.md#rdbpredicates) | 返回分组查询列的谓词。 |

**示例：**

```
1. let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
2. predicates.groupBy(["AGE", "NAME"])
```

### indexedBy

PhonePC/2in1TabletTVWearable

indexedBy(field: string): RdbPredicates

配置RdbPredicates以指定索引列。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 索引列的名称。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](js-apis-data-rdb.md#rdbpredicates) | 返回具有指定索引列的RdbPredicates。 |

**示例：**

```
1. let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
2. predicates.indexedBy("SALARY_INDEX")
```

### in

PhonePC/2in1TabletTVWearable

in(field: string, value: Array<ValueType>): RdbPredicates

配置RdbPredicates以匹配数据字段为ValueType数组且值在给定范围内的指定字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | Array<[ValueType](js-apis-data-rdb.md#valuetype)> | 是 | 以ValueType型数组形式指定的要匹配的值。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](js-apis-data-rdb.md#rdbpredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
2. predicates.in("AGE", [18, 20])
```

### notIn

PhonePC/2in1TabletTVWearable

notIn(field: string, value: Array<ValueType>): RdbPredicates

将RdbPredicates配置为匹配数据字段为ValueType且值超出给定范围的指定字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | Array<[ValueType](js-apis-data-rdb.md#valuetype)> | 是 | 以ValueType数组形式指定的要匹配的值。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](js-apis-data-rdb.md#rdbpredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
2. predicates.notIn("NAME", ["Lisa", "Rose"])
```

## RdbStore

PhonePC/2in1TabletTVWearable

提供管理关系数据库（RDB）方法的接口。

在使用以下相关接口前，请使用[executeSql](js-apis-data-rdb.md#executesql8)接口初始化数据库表结构和相关数据。

### insert

PhonePC/2in1TabletTVWearable

insert(table: string, values: ValuesBucket, callback: AsyncCallback<number>):void

向目标表中插入一行数据，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 指定的目标表名。 |
| values | [ValuesBucket](js-apis-data-rdb.md#valuesbucket) | 是 | 表示要插入到表中的数据行。 |
| callback | AsyncCallback<number> | 是 | 指定callback回调函数。如果操作成功，返回行ID；否则返回-1。 |

**示例：**

```
1. import { ValuesBucket } from '@ohos.data.ValuesBucket';

3. let key1 = "NAME";
4. let key2 = "AGE";
5. let key3 = "SALARY";
6. let key4 = "CODES";
7. let value1 = "Lisi";
8. let value2 = 18;
9. let value3 = 100.5;
10. let value4 = new Uint8Array([1, 2, 3, 4, 5]);
11. const valueBucket: ValuesBucket = {
12. key1: value1,
13. key2: value2,
14. key3: value3,
15. key4: value4,
16. };

18. rdbStore.insert("EMPLOYEE", valueBucket, (status: number, rowId: number) => {
19. if (status) {
20. console.log("Insert is failed");
21. return;
22. }
23. console.log("Insert is successful, rowId = " + rowId);
24. })
```

### insert

PhonePC/2in1TabletTVWearable

insert(table: string, values: ValuesBucket):Promise<number>

向目标表中插入一行数据，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 指定的目标表名。 |
| values | [ValuesBucket](js-apis-data-rdb.md#valuesbucket) | 是 | 表示要插入到表中的数据行。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。如果操作成功，返回行ID；否则返回-1。 |

**示例：**

```
1. import { ValuesBucket } from '@ohos.data.ValuesBucket';

3. let key1 = "NAME";
4. let key2 = "AGE";
5. let key3 = "SALARY";
6. let key4 = "CODES";
7. let value1 = "Lisi";
8. let value2 = 18;
9. let value3 = 100.5;
10. let value4 = new Uint8Array([1, 2, 3, 4, 5]);
11. const valueBucket: ValuesBucket = {
12. key1: value1,
13. key2: value2,
14. key3: value3,
15. key4: value4,
16. };

18. let promise: void = rdbStore.insert("EMPLOYEE", valueBucket)
19. promise.then((rowId: BusinessError) => {
20. console.log("Insert is successful, rowId = " + rowId);
21. }).catch((status: number) => {
22. console.log("Insert is failed");
23. })
```

### batchInsert

PhonePC/2in1TabletTVWearable

batchInsert(table: string, values: Array<ValuesBucket>, callback: AsyncCallback<number>):void

向目标表中插入一组数据，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 指定的目标表名。 |
| values | Array<[ValuesBucket](js-apis-data-rdb.md#valuesbucket)> | 是 | 表示要插入到表中的一组数据。 |
| callback | AsyncCallback<number> | 是 | 指定callback回调函数。如果操作成功，返回插入的数据个数，否则返回-1。 |

**示例：**

```
1. import { ValuesBucket } from '@ohos.data.ValuesBucket';

3. let key1 = "NAME";
4. let key2 = "AGE";
5. let key3 = "SALARY";
6. let key4 = "CODES";
7. let value1 = "Lisa";
8. let value2 = 18;
9. let value3 = 100.5;
10. let value4 = new Uint8Array([1, 2, 3, 4, 5]);
11. let value5 = "Jack";
12. let value6 = 19;
13. let value7 = 101.5;
14. let value8 = new Uint8Array([6, 7, 8, 9, 10]);
15. let value9 = "Tom";
16. let value10 = 20;
17. let value11 = 102.5;
18. let value12 = new Uint8Array([11, 12, 13, 14, 15]);
19. const valueBucket1: ValuesBucket = {
20. key1: value1,
21. key2: value2,
22. key3: value3,
23. key4: value4,
24. };
25. const valueBucket2: ValuesBucket = {
26. key1: value5,
27. key2: value6,
28. key3: value7,
29. key4: value8,
30. };
31. const valueBucket3: ValuesBucket = {
32. key1: value9,
33. key2: value10,
34. key3: value11,
35. key4: value12,
36. };

38. let valueBuckets = new Array(valueBucket1, valueBucket2, valueBucket3);
39. rdbStore.batchInsert("EMPLOYEE", valueBuckets, (status: number, insertNum: number) => {
40. if (status) {
41. console.log("batchInsert is failed, status = " + status);
42. return;
43. }
44. console.log("batchInsert is successful, the number of values that were inserted = " + insertNum);
45. })
```

### batchInsert

PhonePC/2in1TabletTVWearable

batchInsert(table: string, values: Array<ValuesBucket>):Promise<number>

向目标表中插入一组数据，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 指定的目标表名。 |
| values | Array<[ValuesBucket](js-apis-data-rdb.md#valuesbucket)> | 是 | 表示要插入到表中的一组数据。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。如果操作成功，返回插入的数据个数，否则返回-1。 |

**示例：**

```
1. import { ValuesBucket } from '@ohos.data.ValuesBucket';

3. let key1 = "NAME";
4. let key2 = "AGE";
5. let key3 = "SALARY";
6. let key4 = "CODES";
7. let value1 = "Lisa";
8. let value2 = 18;
9. let value3 = 100.5;
10. let value4 = new Uint8Array([1, 2, 3, 4, 5]);
11. let value5 = "Jack";
12. let value6 = 19;
13. let value7 = 101.5;
14. let value8 = new Uint8Array([6, 7, 8, 9, 10]);
15. let value9 = "Tom";
16. let value10 = 20;
17. let value11 = 102.5;
18. let value12 = new Uint8Array([11, 12, 13, 14, 15]);
19. const valueBucket1: ValuesBucket = {
20. key1: value1,
21. key2: value2,
22. key3: value3,
23. key4: value4,
24. };
25. const valueBucket2: ValuesBucket = {
26. key1: value5,
27. key2: value6,
28. key3: value7,
29. key4: value8,
30. };
31. const valueBucket3: ValuesBucket = {
32. key1: value9,
33. key2: value10,
34. key3: value11,
35. key4: value12,
36. };

38. let valueBuckets = new Array(valueBucket1, valueBucket2, valueBucket3);
39. let promise: void = rdbStore.batchInsert("EMPLOYEE", valueBuckets);
40. promise.then((insertNum: number) => {
41. console.log("batchInsert is successful, the number of values that were inserted = " + insertNum);
42. }).catch((status: number) => {
43. console.log("batchInsert is failed, status = " + status);
44. })
```

### update

PhonePC/2in1TabletTVWearable

update(values: ValuesBucket, predicates: RdbPredicates, callback: AsyncCallback<number>):void

根据RdbPredicates的指定实例对象更新数据库中的数据，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| values | [ValuesBucket](js-apis-data-rdb.md#valuesbucket) | 是 | values指示数据库中要更新的数据行。键值对与数据库表的列名相关联。 |
| predicates | [RdbPredicates](js-apis-data-rdb.md#rdbpredicates) | 是 | RdbPredicates的实例对象指定的更新条件。 |
| callback | AsyncCallback<number> | 是 | 指定的callback回调方法。返回受影响的行数。 |

**示例：**

```
1. import { ValuesBucket } from '@ohos.data.ValuesBucket';

3. let key1 = "NAME";
4. let key2 = "AGE";
5. let key3 = "SALARY";
6. let key4 = "CODES";
7. let value1 = "Lisa";
8. let value2 = 18;
9. let value3 = 100.5;
10. let value4 = new Uint8Array([1, 2, 3, 4, 5]);

12. const valueBucket: ValuesBucket = {
13. key1: value1,
14. key2: value2,
15. key3: value3,
16. key4: value4,
17. };
18. let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
19. predicates.equalTo("NAME", "Lisa")
20. rdbStore.update(valueBucket, predicates, (err: BusinessError, rows: number) => {
21. if (err) {
22. console.info("Updated failed, err: " + err)
23. return
24. }
25. console.log("Updated row count: " + rows)
26. })
```

### update

PhonePC/2in1TabletTVWearable

update(values: ValuesBucket, predicates: RdbPredicates):Promise<number>

根据RdbPredicates的指定实例对象更新数据库中的数据，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| values | [ValuesBucket](js-apis-data-rdb.md#valuesbucket) | 是 | values指示数据库中要更新的数据行。键值对与数据库表的列名相关联。 |
| predicates | [RdbPredicates](js-apis-data-rdb.md#rdbpredicates) | 是 | RdbPredicates的实例对象指定的更新条件。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 指定的Promise回调方法。返回受影响的行数。 |

**示例：**

```
1. import { ValuesBucket } from '@ohos.data.ValuesBucket';

3. let key1 = "NAME";
4. let key2 = "AGE";
5. let key3 = "SALARY";
6. let key4 = "CODES";
7. let value1 = "Lisa";
8. let value2 = 18;
9. let value3 = 100.5;
10. let value4 = new Uint8Array([1, 2, 3, 4, 5]);

12. const valueBucket: ValuesBucket = {
13. key1: value1,
14. key2: value2,
15. key3: value3,
16. key4: value4,
17. };
18. let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
19. predicates.equalTo("NAME", "Lisa")
20. let promise: void = rdbStore.update(valueBucket, predicates)
21. promise.then(async (rows: number) => {
22. console.log("Updated row count: " + rows)
23. }).catch((err: BusinessError) => {
24. console.info("Updated failed, err: " + err)
25. })
```

### delete

PhonePC/2in1TabletTVWearable

delete(predicates: RdbPredicates, callback: AsyncCallback<number>):void

根据RdbPredicates的指定实例对象从数据库中删除数据，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicates | [RdbPredicates](js-apis-data-rdb.md#rdbpredicates) | 是 | RdbPredicates的实例对象指定的删除条件。 |
| callback | AsyncCallback<number> | 是 | 指定callback回调函数。返回受影响的行数。 |

**示例：**

```
1. let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
2. predicates.equalTo("NAME", "Lisa")
3. rdbStore.delete(predicates, (err: BusinessError, rows: number) => {
4. if (err) {
5. console.info("Delete failed, err: " + err)
6. return
7. }
8. console.log("Delete rows: " + rows)
9. })
```

### delete

PhonePC/2in1TabletTVWearable

delete(predicates: RdbPredicates):Promise<number>

根据RdbPredicates的指定实例对象从数据库中删除数据，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicates | [RdbPredicates](js-apis-data-rdb.md#rdbpredicates) | 是 | RdbPredicates的实例对象指定的删除条件。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回受影响的行数。 |

**示例：**

```
1. let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
2. predicates.equalTo("NAME", "Lisa")
3. let promise: void = rdbStore.delete(predicates)
4. promise.then((rows: number) => {
5. console.log("Delete rows: " + rows)
6. }).catch((err: BusinessError) => {
7. console.info("Delete failed, err: " + err)
8. })
```

### query

PhonePC/2in1TabletTVWearable

query(predicates: RdbPredicates, columns: Array<string>, callback: AsyncCallback<ResultSet>):void

根据指定条件查询数据库中的数据，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicates | [RdbPredicates](js-apis-data-rdb.md#rdbpredicates) | 是 | RdbPredicates的实例对象指定的查询条件。 |
| columns | Array<string> | 是 | 表示要查询的列。如果值为空，则查询应用于所有列。 |
| callback | AsyncCallback<[ResultSet](js-apis-data-resultset.md)> | 是 | 指定callback回调函数。如果操作成功，则返回ResultSet对象。 |

**示例：**

```
1. let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
2. predicates.equalTo("NAME", "Rose")
3. rdbStore.query(predicates, ["ID", "NAME", "AGE", "SALARY", "CODES"], (err: BusinessError, resultSet: void) => {
4. if (err) {
5. console.info("Query failed, err: " + err)
6. return
7. }
8. console.log("ResultSet column names: " + resultSet.columnNames)
9. console.log("ResultSet column count: " + resultSet.columnCount)
10. })
```

### query

PhonePC/2in1TabletTVWearable

query(predicates: RdbPredicates, columns?: Array<string>):Promise<ResultSet>

根据指定条件查询数据库中的数据，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicates | [RdbPredicates](js-apis-data-rdb.md#rdbpredicates) | 是 | RdbPredicates的实例对象指定的查询条件。 |
| columns | Array<string> | 否 | 表示要查询的列。如果值为空，则查询应用于所有列。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[ResultSet](js-apis-data-resultset.md)> | Promise对象。如果操作成功，则返回ResultSet对象。 |

**示例：**

```
1. let predicates = new data_rdb.RdbPredicates("EMPLOYEE")
2. predicates.equalTo("NAME", "Rose")
3. let promise: void = rdbStore.query(predicates, ["ID", "NAME", "AGE", "SALARY", "CODES"])
4. promise.then((resultSet: void) => {
5. console.log("ResultSet column names: " + resultSet.columnNames)
6. console.log("ResultSet column count: " + resultSet.columnCount)
7. }).catch((err: BusinessError) => {
8. console.info("Query failed, err: " + err)
9. })
```

### querySql8+

PhonePC/2in1TabletTVWearable

querySql(sql: string, bindArgs: Array<ValueType>, callback: AsyncCallback<ResultSet>):void

根据指定SQL语句查询数据库中的数据，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sql | string | 是 | 指定要执行的SQL语句。 |
| bindArgs | Array<[ValueType](js-apis-data-rdb.md#valuetype)> | 是 | SQL语句中参数的值。该值与sql参数语句中的占位符相对应。当sql参数语句完整时，该参数需为空数组。 |
| callback | AsyncCallback<[ResultSet](js-apis-data-resultset.md)> | 是 | 指定callback回调函数。如果操作成功，则返回ResultSet对象。 |

**示例：**

```
1. rdbStore.querySql("SELECT * FROM EMPLOYEE CROSS JOIN BOOK WHERE BOOK.NAME = ?", ['sanguo'], (err: BusinessError, resultSet: void) => {
2. if (err) {
3. console.info("Query failed, err: " + err)
4. return
5. }
6. console.log("ResultSet column names: " + resultSet.columnNames)
7. console.log("ResultSet column count: " + resultSet.columnCount)
8. })
```

### querySql8+

PhonePC/2in1TabletTVWearable

querySql(sql: string, bindArgs?: Array<ValueType>):Promise<ResultSet>

根据指定SQL语句查询数据库中的数据，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sql | string | 是 | 指定要执行的SQL语句。 |
| bindArgs | Array<[ValueType](js-apis-data-rdb.md#valuetype)> | 否 | SQL语句中参数的值。该值与sql参数语句中的占位符相对应。当sql参数语句完整时，该参数不填。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[ResultSet](js-apis-data-resultset.md)> | Promise对象。如果操作成功，则返回ResultSet对象。 |

**示例：**

```
1. let promise: void = rdbStore.querySql("SELECT * FROM EMPLOYEE CROSS JOIN BOOK WHERE BOOK.NAME = 'sanguo'")
2. promise.then((resultSet: void) => {
3. console.log("ResultSet column names: " + resultSet.columnNames)
4. console.log("ResultSet column count: " + resultSet.columnCount)
5. }).catch((err: BusinessError) => {
6. console.info("Query failed, err: " + err)
7. })
```

### executeSql8+

PhonePC/2in1TabletTVWearable

executeSql(sql: string, bindArgs: Array<ValueType>, callback: AsyncCallback<void>):void

执行包含指定参数但不返回值的SQL语句，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sql | string | 是 | 指定要执行的SQL语句。 |
| bindArgs | Array<[ValueType](js-apis-data-rdb.md#valuetype)> | 是 | SQL语句中参数的值。该值与sql参数语句中的占位符相对应。当sql参数语句完整时，该参数需为空数组。 |
| callback | AsyncCallback<void> | 是 | 指定callback回调函数。 |

**示例：**

```
1. const SQL_DELETE_TABLE = "DELETE FROM test WHERE name = ?"
2. rdbStore.executeSql(SQL_DELETE_TABLE, ['zhangsan'], (err: BusinessError) => {
3. if (err) {
4. console.info("ExecuteSql failed, err: " + err)
5. return
6. }
7. console.info('Delete table done.')
8. })
```

### executeSql8+

PhonePC/2in1TabletTVWearable

executeSql(sql: string, bindArgs?: Array<ValueType>):Promise<void>

执行包含指定参数但不返回值的SQL语句，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sql | string | 是 | 指定要执行的SQL语句。 |
| bindArgs | Array<[ValueType](js-apis-data-rdb.md#valuetype)> | 否 | SQL语句中参数的值。该值与sql参数语句中的占位符相对应。当sql参数语句完整时，该参数不填。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. const SQL_DELETE_TABLE = "DELETE FROM test WHERE name = 'zhangsan'"
2. let promise = rdbStore.executeSql(SQL_DELETE_TABLE)
3. promise.then(() => {
4. console.info('Delete table done.')
5. }).catch((err: BusinessError) => {
6. console.info("ExecuteSql failed, err: " + err)
7. })
```

### beginTransaction8+

PhonePC/2in1TabletTVWearable

beginTransaction():void

在开始执行SQL语句之前，开始事务。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**示例：**

```
1. import featureAbility from '@ohos.ability.featureAbility';
2. import { ValuesBucket } from '@ohos.data.ValuesBucket';

4. let key1 = "NAME";
5. let key2 = "AGE";
6. let key3 = "SALARY";
7. let key4 = "blobType";
8. let value1 = "Lisa";
9. let value2 = 18;
10. let value3 = 100.5;
11. let value4 = new Uint8Array([1, 2, 3]);

13. const valueBucket: ValuesBucket = {
14. key1: value1,
15. key2: value2,
16. key3: value3,
17. key4: value4,
18. };

20. data_rdb.getRdbStore(this.context, "RdbTest.db", 1, async (err: BusinessError, rdbStore) => {
21. rdbStore.beginTransaction()
22. await rdbStore.insert("test", valueBucket)
23. rdbStore.commit()
24. })
```

### commit8+

PhonePC/2in1TabletTVWearable

commit():void

提交已执行的SQL语句。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**示例：**

```
1. import { ValuesBucket } from '@ohos.data.ValuesBucket';
2. import featureAbility from '@ohos.ability.featureAbility';

4. let key1 = "NAME";
5. let key2 = "AGE";
6. let key3 = "SALARY";
7. let key4 = "blobType";
8. let value1 = "Lisa";
9. let value2 = 18;
10. let value3 = 100.5;
11. let value4 = new Uint8Array([1, 2, 3]);

13. const valueBucket: ValuesBucket = {
14. key1: value1,
15. key2: value2,
16. key3: value3,
17. key4: value4,
18. };

20. data_rdb.getRdbStore(this.context, "RdbTest.db", 1, async (err: BusinessError, rdbStore) => {
21. rdbStore.beginTransaction()
22. await rdbStore.insert("test", valueBucket)
23. rdbStore.commit()
24. })
```

### rollBack8+

PhonePC/2in1TabletTVWearable

rollBack():void

回滚已经执行的SQL语句。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**示例：**

```
1. import { ValuesBucket } from '@ohos.data.ValuesBucket';
2. import featureAbility from '@ohos.ability.featureAbility';

4. let key1 = "NAME";
5. let key2 = "AGE";
6. let key3 = "SALARY";
7. let key4 = "blobType";
8. let value1 = "Lisa";
9. let value2 = 18;
10. let value3 = 100.5;
11. let value4 = new Uint8Array([1, 2, 3]);

13. const valueBucket: ValuesBucket = {
14. key1: value1,
15. key2: value2,
16. key3: value3,
17. key4: value4,
18. };

20. const STORE_CONFIG = { name: "RdbTest.db"}
21. data_rdb.getRdbStore(this,context, "RdbTest.db", 1, async (err: BusinessError, rdbStore) => {
22. try {
23. rdbStore.beginTransaction()
24. await rdbStore.insert("test", valueBucket)
25. rdbStore.commit()
26. } catch (e) {
27. rdbStore.rollBack()
28. }
29. })
```

### setDistributedTables8+

PhonePC/2in1TabletTVWearable

setDistributedTables(tables: Array<string>, callback: AsyncCallback<void>): void

设置分布式列表，使用callback异步回调。

**需要权限：** ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tables | Array<string> | 是 | 要设置的分布式列表表名。 |
| callback | AsyncCallback<void> | 是 | 指定callback回调函数。 |

**示例：**

```
1. rdbStore.setDistributedTables(["EMPLOYEE"], (err: BusinessError) => {
2. if (err) {
3. console.info('SetDistributedTables failed, err: ' + err)
4. return
5. }
6. console.info('SetDistributedTables successfully.')
7. })
```

### setDistributedTables8+

PhonePC/2in1TabletTVWearable

setDistributedTables(tables: Array<string>): Promise<void>

设置分布式列表，使用Promise异步回调。

**需要权限：** ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tables | Array<string> | 是 | 要设置的分布式列表表名。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. let promise: void = rdbStore.setDistributedTables(["EMPLOYEE"])
2. promise.then(() => {
3. console.info("SetDistributedTables successfully.")
4. }).catch((err: BusinessError) => {
5. console.info("SetDistributedTables failed, err: " + err)
6. })
```

### obtainDistributedTableName8+

PhonePC/2in1TabletTVWearable

obtainDistributedTableName(device: string, table: string, callback: AsyncCallback<string>): void

根据远程设备的本地表名获取指定远程设备的分布式表名。在查询远程设备数据库时，需要使用分布式表名，使用callback异步回调。

说明

其中device通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

**需要权限：** ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| device | string | 是 | 远程设备ID 。 |
| table | string | 是 | 远程设备的本地表名。 |
| callback | AsyncCallback<string> | 是 | 指定的callback回调函数。如果操作成功，返回远程设备的分布式表名。 |

**示例：**

```
1. import deviceManager from '@ohos.distributedHardware.deviceManager';

3. let dmInstance: Array<string>;

5. deviceManager.createDeviceManager("com.example.appdatamgrverify", (err: BusinessError, manager: void) => {
6. if (err) {
7. console.log("create device manager failed, err=" + err);
8. return;
9. }
10. dmInstance = manager;
11. let devices: Array<string> = dmInstance.getTrustedDeviceListSync();
12. let deviceId: Array<string> = devices[0].deviceId;
13. })

15. rdbStore.obtainDistributedTableName(deviceId, "EMPLOYEE", (err: BusinessError, tableName: String) {
16. if (err) {
17. console.info('ObtainDistributedTableName failed, err: ' + err)
18. return
19. }
20. console.info('ObtainDistributedTableName successfully, tableName=.' + tableName)
21. })
```

### obtainDistributedTableName8+

PhonePC/2in1TabletTVWearable

obtainDistributedTableName(device: string, table: string): Promise<string>

根据远程设备的本地表名获取指定远程设备的分布式表名。在查询远程设备数据库时，需要使用分布式表名，使用Promise异步回调。

说明

其中device通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

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

**示例：**

```
1. import deviceManager from '@ohos.distributedHardware.deviceManager';

3. let dmInstance: Array<string>;

5. deviceManager.createDeviceManager("com.example.appdatamgrverify", (err: BusinessError, manager: void) => {
6. if (err) {
7. console.log("create device manager failed, err=" + err);
8. return;
9. }
10. dmInstance = manager;
11. let devices: Array<string> = dmInstance.getTrustedDeviceListSync();
12. let deviceId: Array<string> = devices[0].deviceId;
13. })

15. let promise: void = rdbStore.obtainDistributedTableName(deviceId, "EMPLOYEE")
16. promise.then((tableName: String) => {
17. console.info('ObtainDistributedTableName successfully, tableName= ' + tableName)
18. }).catch((err: BusinessError) => {
19. console.info('ObtainDistributedTableName failed, err: ' + err)
20. })
```

### sync8+

PhonePC/2in1TabletTVWearable

sync(mode: SyncMode, predicates: RdbPredicates, callback: AsyncCallback<Array<[string, number]>>): void

在设备之间同步数据，使用callback异步回调。

**需要权限：** ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [SyncMode](js-apis-data-rdb.md#syncmode8) | 是 | 指同步模式。该值可以是推、拉。 |
| predicates | [RdbPredicates](js-apis-data-rdb.md#rdbpredicates) | 是 | 约束同步数据和设备。 |
| callback | AsyncCallback<Array<[string, number]>> | 是 | 指定的callback回调函数，用于向调用者发送同步结果。string：设备ID；number：每个设备同步状态，0表示成功，其他值表示失败。 |

**示例：**

```
1. import deviceManager from '@ohos.distributedHardware.deviceManager';

3. let dmInstance: Array<string>;

5. deviceManager.createDeviceManager("com.example.appdatamgrverify", (err: BusinessError, manager: void) => {
6. if (err) {
7. console.log("create device manager failed, err=" + err);
8. return;
9. }
10. dmInstance = manager;
11. let devices: Array<string> = dmInstance.getTrustedDeviceListSync();
12. for (let i = 0; i < devices.length; i++) {
13. let deviceIds: Array<string> = devices[i].deviceId;
14. }
15. })

17. let predicates = new data_rdb.RdbPredicates('EMPLOYEE')
18. predicates.inDevices(deviceIds)
19. rdbStore.sync(data_rdb.SyncMode.SYNC_MODE_PUSH, predicates, (err: BusinessError, result: void) {
20. if (err) {
21. console.log('Sync failed, err: ' + err)
22. return
23. }
24. console.log('Sync done.')
25. for (let i = 0; i < result.length; i++) {
26. console.log('device=' + result[i][0] + ' status=' + result[i][1])
27. }
28. })
```

### sync8+

PhonePC/2in1TabletTVWearable

sync(mode: SyncMode, predicates: RdbPredicates): Promise<Array<[string, number]>>

在设备之间同步数据，使用Promise异步回调。

**需要权限：** ohos.permission.DISTRIBUTED\_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [SyncMode](js-apis-data-rdb.md#syncmode8) | 是 | 指同步模式。该值可以是推、拉。 |
| predicates | [RdbPredicates](js-apis-data-rdb.md#rdbpredicates) | 是 | 约束同步数据和设备。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[string, number]>> | Promise对象，用于向调用者发送同步结果。string：设备ID；number：每个设备同步状态，0表示成功，其他值表示失败。 |

**示例：**

```
1. import deviceManager from '@ohos.distributedHardware.deviceManager';

3. let dmInstance: Array<string>;

5. deviceManager.createDeviceManager("com.example.appdatamgrverify", (err: BusinessError, manager: void) => {
6. if (err) {
7. console.log("create device manager failed, err=" + err);
8. return;
9. }
10. dmInstance = manager;
11. let devices: Array<string> = dmInstance.getTrustedDeviceListSync();
12. for (let i = 0; i < devices.length; i++) {
13. let deviceIds: Array<string> = devices[i].deviceId;
14. }
15. })

17. let predicates = new data_rdb.RdbPredicates('EMPLOYEE')
18. predicates.inDevices(deviceIds)
19. let promise: void = rdbStore.sync(data_rdb.SyncMode.SYNC_MODE_PUSH, predicates)
20. promise.then((result: void) =>{
21. console.log('Sync done.')
22. for (let i = 0; i < result.length; i++) {
23. console.log('device=' + result[i][0] + ' status=' + result[i][1])
24. }
25. }).catch((err: BusinessError) => {
26. console.log('Sync failed')
27. })
```

### on('dataChange')8+

PhonePC/2in1TabletTVWearable

on(event: 'dataChange', type: SubscribeType, observer: Callback<Array<string>>): void

注册数据库的观察者。当分布式数据库中的数据发生更改时，将调用回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取值为'dataChange'，表示数据更改。 |
| type | [SubscribeType](js-apis-data-rdb.md#subscribetype8) | 是 | 订阅类型。 |
| observer | Callback<Array<string>> | 是 | 指分布式数据库中数据更改事件的观察者。Array<string>为数据库中的数据发生改变的对端设备ID。 |

**示例：**

```
1. let devices: Array<string>;

3. try {
4. rdbStore.on('dataChange', data_rdb.SubscribeType.SUBSCRIBE_TYPE_REMOTE, (storeObserver: Array<string>) => {
5. for (let i = 0; i < devices.length; i++) {
6. console.log('device=' + devices[i] + ' data changed')
7. }
8. })
9. } catch (err) {
10. console.log('Register observer failed')
11. }
```

### off('dataChange')8+

PhonePC/2in1TabletTVWearable

off(event:'dataChange', type: SubscribeType, observer: Callback<Array<string>>): void

从数据库中删除指定类型的指定观察者，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取值为'dataChange'，表示数据更改。 |
| type | [SubscribeType](js-apis-data-rdb.md#subscribetype8) | 是 | 订阅类型。 |
| observer | Callback<Array<string>> | 是 | 指已注册的数据更改观察者。Array<string>为数据库中的数据发生改变的对端设备ID。 |

**示例：**

```
1. let devices: Array<string>;

3. try {
4. rdbStore.off('dataChange', data_rdb.SubscribeType.SUBSCRIBE_TYPE_REMOTE, (storeObserver: Array<string>) => {
5. for (let i = 0; i < devices.length; i++) {
6. console.log('device=' + devices[i] + ' data changed')
7. }
8. })
9. } catch (err) {
10. console.log('Unregister observer failed')
11. }
```
