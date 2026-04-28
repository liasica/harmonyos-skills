---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-f
title: Functions
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > ArkTS API > @ohos.data.relationalStore (关系型数据库) > Functions
category: harmonyos-references
scraped_at: 2026-04-28T07:59:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bdb73438ee5cc573bb40fa77d6c972db8d89124bf3da55089ec9b09206a78b69
---

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { relationalStore } from '@kit.ArkData';
```

## relationalStore.getRdbStore

PhonePC/2in1TabletTVWearable

getRdbStore(context: Context, config: StoreConfig, callback: AsyncCallback<RdbStore>): void

创建或打开已有的关系型数据库，开发者可以根据自己的需求配置config参数，然后通过RdbStore调用相关接口执行数据操作。使用callback异步回调。

对应沙箱路径下无数据库文件时，将创建数据库文件，文件创建位置详见[StoreConfig](arkts-apis-data-relationalstore-i.md#storeconfig)。对应路径下已有数据库文件时，将打开已有数据库文件。

开发者在创建数据库时，应谨慎配置是否进行数据库加密的参数[encrypt](arkts-apis-data-relationalstore-i.md#storeconfig)，数据库创建后，禁止对该参数进行修改。

| 当前开库的加密类型 | 本设备上创建该数据库时的加密类型 | 结果 |
| --- | --- | --- |
| 非加密 | 加密 | 将数据库以加密方式打开。 |
| 加密 | 非加密 | 将数据库以非加密方式打开。 |

getRdbStore支持多线程并发操作。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用的上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| config | [StoreConfig](arkts-apis-data-relationalstore-i.md#storeconfig) | 是 | 与此RDB存储相关的数据库配置。 |
| callback | AsyncCallback<[RdbStore](arkts-apis-data-relationalstore-rdbstore.md)> | 是 | 指定callback回调函数，返回RdbStore对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800010 | Failed to open or delete the database by an invalid database path. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14801001 | The operation is supported in the stage model only. |
| 14801002 | Invalid data group ID. |
| 14800017 | StoreConfig is changed. |
| 14800020 | The secret key is corrupted or lost. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |

**示例：**

FA模型示例：

```
1. import { featureAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let store: relationalStore.RdbStore | undefined = undefined;
5. let context = featureAbility.getContext();

7. const STORE_CONFIG: relationalStore.StoreConfig = {
8. name: "RdbTest.db",
9. securityLevel: relationalStore.SecurityLevel.S3
10. };

12. relationalStore.getRdbStore(context, STORE_CONFIG, async (err: BusinessError, rdbStore: relationalStore.RdbStore) => {
13. if (err) {
14. console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
15. return;
16. }
17. console.info('Get RdbStore successfully.');
18. store = rdbStore;
19. // 成功获取到 rdbStore 后执行后续操作
20. });
```

Stage模型示例：

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let store: relationalStore.RdbStore | undefined = undefined;

7. class EntryAbility extends UIAbility {
8. onWindowStageCreate(windowStage: window.WindowStage) {
9. const STORE_CONFIG: relationalStore.StoreConfig = {
10. name: "RdbTest.db",
11. securityLevel: relationalStore.SecurityLevel.S3
12. };

14. relationalStore.getRdbStore(this.context, STORE_CONFIG, async (err: BusinessError, rdbStore: relationalStore.RdbStore) => {
15. if (err) {
16. console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
17. return;
18. }
19. console.info('Get RdbStore successfully.');
20. store = rdbStore;
21. // 成功获取到 rdbStore 后执行后续操作
22. });
23. }
24. }
```

## relationalStore.getRdbStore

PhonePC/2in1TabletTVWearable

getRdbStore(context: Context, config: StoreConfig): Promise<RdbStore>

创建或打开已有的关系型数据库，开发者可以根据自己的需求配置config参数，然后通过RdbStore调用相关接口执行数据操作。使用Promise异步回调。

对应沙箱路径下无数据库文件时，将创建数据库文件，文件创建位置详见[StoreConfig](arkts-apis-data-relationalstore-i.md#storeconfig)。对应路径下已有数据库文件时，将打开已有数据库文件。

开发者在创建数据库时，应谨慎配置是否进行数据库加密的参数[encrypt](arkts-apis-data-relationalstore-i.md#storeconfig)，数据库创建后，禁止对该参数进行修改。

| 当前开库的加密类型 | 本设备上创建该数据库时的加密类型 | 结果 |
| --- | --- | --- |
| 非加密 | 加密 | 将数据库以加密方式打开。 |
| 加密 | 非加密 | 将数据库以非加密方式打开。 |

getRdbStore支持多线程并发操作。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用的上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| config | [StoreConfig](arkts-apis-data-relationalstore-i.md#storeconfig) | 是 | 与此RDB存储相关的数据库配置。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[RdbStore](arkts-apis-data-relationalstore-rdbstore.md)> | Promise对象。返回RdbStore对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../harmonyos-guides/data-backup-and-restore.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800010 | Failed to open or delete the database by an invalid database path. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14801001 | The operation is supported in the stage model only. |
| 14801002 | Invalid data group ID. |
| 14800017 | StoreConfig is changed. |
| 14800020 | The secret key is corrupted or lost. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |

**示例：**

FA模型示例：

```
1. import { featureAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let store: relationalStore.RdbStore | undefined = undefined;
5. let context = featureAbility.getContext();

7. const STORE_CONFIG: relationalStore.StoreConfig = {
8. name: "RdbTest.db",
9. securityLevel: relationalStore.SecurityLevel.S3
10. };

12. relationalStore.getRdbStore(context, STORE_CONFIG).then(async (rdbStore: relationalStore.RdbStore) => {
13. store = rdbStore;
14. console.info('Get RdbStore successfully.');
15. }).catch((err: BusinessError) => {
16. console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
17. });
```

Stage模型示例：

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. let store: relationalStore.RdbStore | undefined = undefined;

7. class EntryAbility extends UIAbility {
8. onWindowStageCreate(windowStage: window.WindowStage) {
9. const STORE_CONFIG: relationalStore.StoreConfig = {
10. name: "RdbTest.db",
11. securityLevel: relationalStore.SecurityLevel.S3
12. };

14. relationalStore.getRdbStore(this.context, STORE_CONFIG).then(async (rdbStore: relationalStore.RdbStore) => {
15. store = rdbStore;
16. console.info('Get RdbStore successfully.');
17. }).catch((err: BusinessError) => {
18. console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
19. });
20. }
21. }
```

## relationalStore.deleteRdbStore

PhonePC/2in1TabletTVWearable

deleteRdbStore(context: Context, name: string, callback: AsyncCallback<void>): void

删除数据库文件，使用callback异步回调。

删除成功后，建议将数据库对象置为null。建立数据库时，若在[StoreConfig](arkts-apis-data-relationalstore-i.md#storeconfig)中配置了自定义路径，则调用此接口进行删库无效，必须使用 [deleteRdbStore](arkts-apis-data-relationalstore-f.md#relationalstoredeleterdbstore10) 接口进行删库。

当使用向量数据库时，在调用deleteRdbStore接口前，应当确保向量数据库已打开的RdbStore和ResultSet均已成功关闭。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用的上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| name | string | 是 | 数据库名称。 |
| callback | AsyncCallback<void> | 是 | 指定callback回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800010 | Failed to open or delete the database by an invalid database path. |

**示例：**

FA模型示例：

```
1. import { featureAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let context = featureAbility.getContext();

6. relationalStore.deleteRdbStore(context, "RdbTest.db", (err: BusinessError) => {
7. if (err) {
8. console.error(`Delete RdbStore failed, code is ${err.code},message is ${err.message}`);
9. return;
10. }
11. // 数据库删除成功后，已初始化的RdbStore实例将无法继续使用。
12. // 及时将相关变量置空以释放资源。
13. console.info('Delete RdbStore successfully.');
14. });
```

Stage模型示例：

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. class EntryAbility extends UIAbility {
6. onWindowStageCreate(windowStage: window.WindowStage) {
7. relationalStore.deleteRdbStore(this.context, "RdbTest.db", (err: BusinessError) => {
8. if (err) {
9. console.error(`Delete RdbStore failed, code is ${err.code},message is ${err.message}`);
10. return;
11. }
12. // 数据库删除成功后，已初始化的RdbStore实例将无法继续使用。
13. // 及时将相关变量置空以释放资源。
14. console.info('Delete RdbStore successfully.');
15. });
16. }
17. }
```

## relationalStore.deleteRdbStore

PhonePC/2in1TabletTVWearable

deleteRdbStore(context: Context, name: string): Promise<void>

使用指定的数据库文件配置删除数据库，使用Promise异步回调。

删除成功后，建议将数据库对象置为null。建立数据库时，若在[StoreConfig](arkts-apis-data-relationalstore-i.md#storeconfig)中配置了自定义路径，则调用此接口进行删库无效，必须使用 [deleteRdbStore](arkts-apis-data-relationalstore-f.md#relationalstoredeleterdbstore10-1) 接口进行删库。

当使用向量数据库时，在调用deleteRdbStore接口前，应当确保向量数据库已打开的RdbStore和ResultSet均已成功关闭。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用的上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| name | string | 是 | 数据库名称。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800010 | Failed to open or delete the database by an invalid database path. |

**示例：**

FA模型示例：

```
1. import { featureAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let context = featureAbility.getContext();

6. relationalStore.deleteRdbStore(context, "RdbTest.db").then(() => {
7. // 数据库删除成功后，已初始化的RdbStore实例将无法继续使用。
8. // 及时将相关变量置空以释放资源。
9. console.info('Delete RdbStore successfully.');
10. }).catch((err: BusinessError) => {
11. console.error(`Delete RdbStore failed, code is ${err.code},message is ${err.message}`);
12. });
```

Stage模型示例：

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. class EntryAbility extends UIAbility {
6. onWindowStageCreate(windowStage: window.WindowStage) {
7. relationalStore.deleteRdbStore(this.context, "RdbTest.db").then(() => {
8. // 数据库删除成功后，已初始化的RdbStore实例将无法继续使用。
9. // 及时将相关变量置空以释放资源。
10. console.info('Delete RdbStore successfully.');
11. }).catch((err: BusinessError) => {
12. console.error(`Delete RdbStore failed, code is ${err.code},message is ${err.message}`);
13. });
14. }
15. }
```

## relationalStore.deleteRdbStore10+

PhonePC/2in1TabletTVWearable

deleteRdbStore(context: Context, config: StoreConfig, callback: AsyncCallback<void>): void

使用指定的数据库文件配置删除数据库，使用callback异步回调。

删除成功后，建议将数据库对象置为null。若数据库文件处于公共沙箱目录下，则删除数据库时必须使用该接口，当存在多个进程操作同一个数据库的情况，建议向其他进程发送数据库删除通知使其感知并处理。建立数据库时，若在[StoreConfig](arkts-apis-data-relationalstore-i.md#storeconfig)中配置了自定义路径，则必须调用此接口进行删库。

当使用向量数据库时，在调用deleteRdbStore接口前，应当确保向量数据库已打开的RdbStore和ResultSet均已成功关闭。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用的上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| config | [StoreConfig](arkts-apis-data-relationalstore-i.md#storeconfig) | 是 | 与此RDB存储相关的数据库配置。 |
| callback | AsyncCallback<void> | 是 | 指定callback回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800010 | Failed to open or delete the database by an invalid database path. |
| 14801001 | The operation is supported in the stage model only. |
| 14801002 | Invalid data group ID. |

**示例：**

FA模型示例：

```
1. import { featureAbility } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let context = featureAbility.getContext();

6. const STORE_CONFIG: relationalStore.StoreConfig = {
7. name: "RdbTest.db",
8. securityLevel: relationalStore.SecurityLevel.S3
9. };

11. relationalStore.deleteRdbStore(context, STORE_CONFIG, (err: BusinessError) => {
12. if (err) {
13. console.error(`Delete RdbStore failed, code is ${err.code},message is ${err.message}`);
14. return;
15. }
16. // 数据库删除成功后，已初始化的RdbStore实例将无法继续使用。
17. // 及时将相关变量置空以释放资源。
18. console.info('Delete RdbStore successfully.');
19. });
```

Stage模型示例：

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. class EntryAbility extends UIAbility {
6. onWindowStageCreate(windowStage: window.WindowStage) {
7. const STORE_CONFIG: relationalStore.StoreConfig = {
8. name: "RdbTest.db",
9. securityLevel: relationalStore.SecurityLevel.S3
10. };
11. relationalStore.deleteRdbStore(this.context, STORE_CONFIG, (err: BusinessError) => {
12. if (err) {
13. console.error(`Delete RdbStore failed, code is ${err.code},message is ${err.message}`);
14. return;
15. }
16. // 数据库删除成功后，已初始化的RdbStore实例将无法继续使用。
17. // 及时将相关变量置空以释放资源。
18. console.info('Delete RdbStore successfully.');
19. });
20. }
21. }
```

## relationalStore.deleteRdbStore10+

PhonePC/2in1TabletTVWearable

deleteRdbStore(context: Context, config: StoreConfig): Promise<void>

使用指定的数据库文件配置删除数据库，使用Promise异步回调。

删除成功后，建议将数据库对象置为null。若数据库文件处于公共沙箱目录下，则删除数据库时必须使用该接口，当存在多个进程操作同一个数据库的情况，建议向其他进程发送数据库删除通知使其感知并处理。建立数据库时，若在[StoreConfig](arkts-apis-data-relationalstore-i.md#storeconfig)中配置了自定义路径，则必须调用此接口进行删库。

当使用向量数据库时，在调用deleteRdbStore接口前，应当确保向量数据库已打开的RdbStore和ResultSet均已成功关闭。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用的上下文。  FA模型的应用Context定义见[Context](js-apis-inner-app-context.md)。  Stage模型的应用Context定义见[Context](js-apis-inner-application-context.md)。 |
| config | [StoreConfig](arkts-apis-data-relationalstore-i.md#storeconfig) | 是 | 与此RDB存储相关的数据库配置。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800010 | Failed to open or delete the database by an invalid database path. |
| 14801001 | The operation is supported in the stage model only. |
| 14801002 | Invalid data group ID. |

**示例：**

FA模型示例：

```
1. import { featureAbility } from "@kit.AbilityKit";
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let context = featureAbility.getContext();

6. const STORE_CONFIG: relationalStore.StoreConfig = {
7. name: "RdbTest.db",
8. securityLevel: relationalStore.SecurityLevel.S3
9. };

11. relationalStore.deleteRdbStore(context, STORE_CONFIG).then(() => {
12. // 数据库删除成功后，已初始化的RdbStore实例将无法继续使用。
13. // 及时将相关变量置空以释放资源。
14. console.info('Delete RdbStore successfully.');
15. }).catch((err: BusinessError) => {
16. console.error(`Delete RdbStore failed, code is ${err.code},message is ${err.message}`);
17. });
```

Stage模型示例：

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. class EntryAbility extends UIAbility {
6. onWindowStageCreate(windowStage: window.WindowStage) {
7. const STORE_CONFIG: relationalStore.StoreConfig = {
8. name: "RdbTest.db",
9. securityLevel: relationalStore.SecurityLevel.S3
10. };
11. relationalStore.deleteRdbStore(this.context, STORE_CONFIG).then(() => {
12. // 数据库删除成功后，已初始化的RdbStore实例将无法继续使用。
13. // 及时将相关变量置空以释放资源。
14. console.info('Delete RdbStore successfully.');
15. }).catch((err: BusinessError) => {
16. console.error(`Delete RdbStore failed, code is ${err.code},message is ${err.message}`);
17. });
18. }
19. }
```

## relationalStore.isVectorSupported18+

PhonePC/2in1TabletTVWearable

isVectorSupported(): boolean

判断系统是否提供向量数据库能力。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值**：

| 类型 | 说明 |
| --- | --- |
| boolean | 系统具备向量数据库能力时返回true，否则返回false。 |

**示例：**

```
1. import { contextConstant, UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { relationalStore } from '@kit.ArkData';

6. let store: relationalStore.RdbStore | undefined = undefined;
7. export default class EntryAbility extends UIAbility {
8. async onWindowStageCreate(windowStage: window.WindowStage) {
9. let supported = relationalStore.isVectorSupported();
10. if (supported) {
11. // 支持向量数据库
12. console.info("Vector database supported on current platform.");
13. const STORE_CONFIG: relationalStore.StoreConfig = {
14. name: "VectorTest.db",
15. securityLevel: relationalStore.SecurityLevel.S3,
16. vector: true
17. };
18. try {
19. const context = this.context.getApplicationContext().createAreaModeContext(contextConstant.AreaMode.EL3);
20. const rdbStore = await relationalStore.getRdbStore(context, STORE_CONFIG);
21. console.info('Get RdbStore successfully.');
22. store = rdbStore;
23. // 成功获取到 rdbStore 后执行后续操作
24. } catch (error) {
25. const err = error as BusinessError;
26. console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
27. }
28. } else {
29. console.info("Vector database not supported on current platform.");
30. }
31. }
32. }
```

## relationalStore.isTokenizerSupported18+

PhonePC/2in1TabletTVWearable

isTokenizerSupported(tokenizer: Tokenizer): boolean

判断当前平台是否支持传入的分词器，此为同步接口。

如果当前平台支持传入的分词器时，此接口返回值为true；反之，返回值为false。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tokenizer | [Tokenizer](arkts-apis-data-relationalstore-e.md#tokenizer17) | 是 | 需要被判断是否支持的分词器。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true表示当前平台支持当前传入的分词器，false表示当前平台不支持当前传入的分词器。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. let customType = relationalStore.Tokenizer.CUSTOM_TOKENIZER;
2. let customTypeSupported = relationalStore.isTokenizerSupported(customType);
3. console.info("custom tokenizer supported on current platform: " + customTypeSupported);
```

## relationalStore.getInsertSqlInfo20+

PhonePC/2in1TabletTVWearable

getInsertSqlInfo(table: string, values: ValuesBucket, conflict?: ConflictResolution): SqlInfo

获取用于插入数据的SQL语句，此为同步接口。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 要写入数据的数据库表名。 |
| values | [ValuesBucket](arkts-apis-data-relationalstore-t.md#valuesbucket) | 是 | 要写入数据库中数据的字段信息以及对应的值信息。 |
| conflict | [ConflictResolution](arkts-apis-data-relationalstore-e.md#conflictresolution10) | 否 | 指定冲突解决模式。默认值是relationalStore.ConflictResolution.ON\_CONFLICT\_NONE。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SqlInfo](arkts-apis-data-relationalstore-i.md#sqlinfo20) | SqlInfo对象，其中sql为返回的sql语句，args为执行SQL中的参数信息。 |

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1. Parameter is out of valid range. |

**示例：**

```
1. const bucket: relationalStore.ValuesBucket = {
2. name: "Logitech",
3. age: 18,
4. sex: "man",
5. desc: "asserter"
6. };
7. const sqlInfo: relationalStore.SqlInfo = relationalStore.getInsertSqlInfo(
8. "USER",
9. bucket,
10. relationalStore.ConflictResolution.ON_CONFLICT_NONE
11. );
```

## relationalStore.getUpdateSqlInfo20+

PhonePC/2in1TabletTVWearable

getUpdateSqlInfo(predicates: RdbPredicates, values: ValuesBucket, conflict?: ConflictResolution): SqlInfo

获取用于更新数据的SQL语句，此为同步接口。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicates | [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 是 | 与指定字段匹配的谓词。 |
| values | [ValuesBucket](arkts-apis-data-relationalstore-t.md#valuesbucket) | 是 | 要写入数据库中数据的字段信息以及对应的值信息。 |
| conflict | [ConflictResolution](arkts-apis-data-relationalstore-e.md#conflictresolution10) | 否 | 指定冲突解决模式。 默认值是relationalStore.ConflictResolution.ON\_CONFLICT\_NONE。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SqlInfo](arkts-apis-data-relationalstore-i.md#sqlinfo20) | SqlInfo对象，其中sql为返回的sql语句，args为执行SQL中的参数信息。 |

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1. Parameter is out of valid range. |

**示例：**

```
1. const bucket: relationalStore.ValuesBucket = {
2. name: "Logitech",
3. age: 18,
4. sex: "man",
5. desc: "asserter"
6. };
7. const predicates = new relationalStore.RdbPredicates("users");
8. const sqlInfo: relationalStore.SqlInfo = relationalStore.getUpdateSqlInfo(
9. predicates,
10. bucket,
11. relationalStore.ConflictResolution.ON_CONFLICT_NONE
12. );
```

## relationalStore.getDeleteSqlInfo20+

PhonePC/2in1TabletTVWearable

getDeleteSqlInfo(predicates: RdbPredicates): SqlInfo

获取用于删除数据的SQL语句，此为同步接口。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicates | [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 是 | 与指定字段匹配的谓词。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SqlInfo](arkts-apis-data-relationalstore-i.md#sqlinfo20) | SqlInfo对象，其中sql为返回的sql语句，args为执行SQL中的参数信息。 |

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1. Parameter is out of valid range. |

**示例：**

```
1. const predicates = new relationalStore.RdbPredicates("users");
2. predicates.equalTo("tableName", "a");
3. predicates.notEqualTo("age", 18);
4. const sqlInfo: relationalStore.SqlInfo = relationalStore.getDeleteSqlInfo(predicates);
```

## relationalStore.getQuerySqlInfo20+

PhonePC/2in1TabletTVWearable

getQuerySqlInfo(predicates: RdbPredicates, columns?: Array<string>): SqlInfo

获取用于查询数据的SQL语句，此为同步接口。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicates | [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 是 | 与指定字段匹配的谓词。 |
| columns | Array<string> | 否 | 要查询的列；如果不指定此参数，则查询所有列。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SqlInfo](arkts-apis-data-relationalstore-i.md#sqlinfo20) | SqlInfo对象，其中sql为返回的sql语句，args为执行SQL中的参数信息。 |

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1. Parameter is out of valid range. |

**示例：**

```
1. const predicates = new relationalStore.RdbPredicates("users");
2. predicates.notEqualTo("age", 18);
3. predicates.equalTo("name", "zhangsan");
4. const sqlInfo: relationalStore.SqlInfo = relationalStore.getQuerySqlInfo(predicates);
```
