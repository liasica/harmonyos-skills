---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-e
title: Enums
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > ArkTS API > @ohos.data.relationalStore (关系型数据库) > Enums
category: harmonyos-references
scraped_at: 2026-04-28T07:59:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a3820f65de40a594b3190929a87a9b228039e58386a3e1cfca0622a560c158b4
---

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## SecurityLevel

PhonePC/2in1TabletTVWearable

数据库的安全级别枚举。请使用枚举名称而非枚举值。数据库的安全等级仅支持由低向高设置，不支持由高向低设置。

说明

若需要进行同步操作，数据库安全等级应不高于对端设备安全等级，具体可见[跨设备同步访问控制机制](../harmonyos-guides/sync-app-data-across-devices-overview.md#跨设备同步访问控制机制)。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| S1 | 1 | 表示数据库的安全级别为低级别，当数据泄露时会产生较低影响。例如，包含壁纸等系统数据的数据库。 |
| S2 | 2 | 表示数据库的安全级别为中级别，当数据泄露时会产生较大影响。例如，包含录音、视频等用户生成数据或通话记录等信息的数据库。 |
| S3 | 3 | 表示数据库的安全级别为高级别，当数据泄露时会产生重大影响。例如，包含用户运动、健康、位置等信息的数据库。 |
| S4 | 4 | 表示数据库的安全级别为关键级别，当数据泄露时会产生严重影响。例如，包含认证凭据、财务数据等信息的数据库。 |

## EncryptionAlgo14+

PhonePC/2in1TabletTVWearable

数据库的加密方式枚举。请使用枚举名称而非枚举值。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AES\_256\_GCM | 0 | 数据库使用AES\_256\_GCM加密。 |
| AES\_256\_CBC | 1 | 数据库使用AES\_256\_CBC加密。 |
| PLAIN\_TEXT22+ | 2 | 数据库不进行加密。 |

## HmacAlgo14+

PhonePC/2in1TabletTVWearable

数据库的HMAC算法枚举。请使用枚举名称而非枚举值。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SHA1 | 0 | HMAC\_SHA1算法。 |
| SHA256 | 1 | HMAC\_SHA256算法。 |
| SHA512 | 2 | HMAC\_SHA512算法。 |

## KdfAlgo14+

PhonePC/2in1TabletTVWearable

数据库的PBKDF2算法枚举。请使用枚举名称而非枚举值。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| KDF\_SHA1 | 0 | PBKDF2\_HMAC\_SHA1算法。 |
| KDF\_SHA256 | 1 | PBKDF2\_HMAC\_SHA256算法。 |
| KDF\_SHA512 | 2 | PBKDF2\_HMAC\_SHA512算法。 |

## Tokenizer17+

PhonePC/2in1TabletTVWearable

描述fts（全文搜索）场景下使用的分词器枚举。请使用枚举名称而非枚举值。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE\_TOKENIZER | 0 | 不使用分词器。 |
| ICU\_TOKENIZER | 1 | 表示使用icu分词器，支持中文以及多国语言。指定icu分词器时，可指定使用哪种语言，例如zh\_CN表示中文，tr\_TR表示土耳其语等。详细支持的语言种类，请查阅[ICU分词器](https://gitcode.com/openharmony/third_party_icu/blob/master/icu4c/source/data/lang/zh.txt)。详细的语言缩写，请查阅该目录（[ICU支持的语言缩写](https://gitcode.com/openharmony/third_party_icu/tree/master/icu4c/source/data/locales)）下的文件名。 |
| CUSTOM\_TOKENIZER18+ | 2 | 表示使用自研分词器，可支持中文（简体、繁体）、英文、阿拉伯数字。CUSTOM\_TOKENIZER相比ICU\_TOKENIZER在分词准确率、常驻内存占用上更有优势。自研分词器支持默认分词模式和短词分词模式（short\_words）两种，使用参数cut\_mode可指定模式，不指定模式时使用默认模式。 |

在使用不同的分词器时，使用的创表语句会有所区别。

**示例：**

示例代码中this.context定义见Stage模型的应用[Context](js-apis-inner-application-context.md)。

使用ICU\_TOKENIZER分词器时，创建表的示例：

```
1. import { relationalStore } from '@kit.ArkData'; // 导入模块
2. import { UIAbility } from '@kit.AbilityKit';
3. import { window } from '@kit.ArkUI';

5. // 此处示例在Stage模式、Ability中实现，使用者也可以在其他合理场景中使用
6. class EntryAbility extends UIAbility {
7. async onWindowStageCreate(windowStage: window.WindowStage) {
8. let store: relationalStore.RdbStore | undefined = undefined;
9. const STORE_CONFIG: relationalStore.StoreConfig = {
10. name: "MyStore.db",
11. securityLevel: relationalStore.SecurityLevel.S3,
12. tokenizer: relationalStore.Tokenizer.ICU_TOKENIZER
13. };
14. store = await relationalStore.getRdbStore(this.context, STORE_CONFIG);

16. const SQL_CREATE_TABLE = "CREATE VIRTUAL TABLE example USING fts4(name, content, tokenize=icu zh_CN)";
17. if (store != undefined) {
18. (store as relationalStore.RdbStore).executeSql(SQL_CREATE_TABLE, (err) => {
19. if (err) {
20. console.error(`ExecuteSql failed, code is ${err.code},message is ${err.message}`);
21. return;
22. }
23. console.info('create virtual table done.');
24. });
25. }
26. }
27. }
```

使用CUSTOM\_TOKENIZER分词器时，创建表的示例：

```
1. import { relationalStore } from '@kit.ArkData'; // 导入模块
2. import { UIAbility } from '@kit.AbilityKit';
3. import { window } from '@kit.ArkUI';

5. // 此处示例在Stage模式、Ability中实现，使用者也可以在其他合理场景中使用
6. class EntryAbility extends UIAbility {
7. async onWindowStageCreate(windowStage: window.WindowStage) {
8. let store: relationalStore.RdbStore | undefined = undefined;
9. const STORE_CONFIG: relationalStore.StoreConfig = {
10. name: "MyStore.db",
11. securityLevel: relationalStore.SecurityLevel.S3,
12. tokenizer: relationalStore.Tokenizer.CUSTOM_TOKENIZER
13. };
14. store = await relationalStore.getRdbStore(this.context, STORE_CONFIG);

16. const SQL_CREATE_TABLE = "CREATE VIRTUAL TABLE example USING fts5(name, content, tokenize='customtokenizer')";
17. if (store != undefined) {
18. (store as relationalStore.RdbStore).executeSql(SQL_CREATE_TABLE, (err) => {
19. if (err) {
20. console.error(`ExecuteSql failed, code is ${err.code},message is ${err.message}`);
21. return;
22. }
23. console.info('create virtual table done.');
24. });
25. }
26. }
27. }
```

使用CUSTOM\_TOKENIZER分词器，并指定分词模式时，创建表的示例：

```
1. import { relationalStore } from '@kit.ArkData'; // 导入模块
2. import { UIAbility } from '@kit.AbilityKit';
3. import { window } from '@kit.ArkUI';

5. export default class EntryAbility extends UIAbility {
6. async onWindowStageCreate(windowStage: window.WindowStage) {
7. console.info('custom tokenizer example: window stage create begin.');
8. let store: relationalStore.RdbStore | undefined = undefined;
9. const storeConfig: relationalStore.StoreConfig = {
10. name: "MyStore.db",
11. securityLevel: relationalStore.SecurityLevel.S3
12. };
13. let customType = relationalStore.Tokenizer.CUSTOM_TOKENIZER;
14. let customTypeSupported = relationalStore.isTokenizerSupported(customType);
15. if (customTypeSupported) {
16. storeConfig.tokenizer = customType;
17. } else {
18. console.info('custom tokenizer example: not support custom tokenizer.');
19. return;
20. }
21. store = await relationalStore.getRdbStore(this.context, storeConfig);

23. const sqlCreateTable =
24. "CREATE VIRTUAL TABLE example USING fts5(name, content, tokenize='customtokenizer cut_mode short_words')";
25. if (store != undefined) {
26. (store as relationalStore.RdbStore).executeSql(sqlCreateTable, (err) => {
27. if (err) {
28. console.error(`custom tokenizer example: ExecuteSql failed, code is ${err.code},message is ${err.message}`);
29. return;
30. }
31. console.info('custom tokenizer example: create virtual table done.');
32. });
33. }
34. }
35. }
```

## AssetStatus10+

PhonePC/2in1TabletTVWearable

描述资产附件的状态枚举。请使用枚举名称而非枚举值。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ASSET\_NORMAL | 1 | 表示资产状态正常。 |
| ASSET\_INSERT | 2 | 表示资产需要插入到云端。 |
| ASSET\_UPDATE | 3 | 表示资产需要更新到云端。 |
| ASSET\_DELETE | 4 | 表示资产需要在云端删除。 |
| ASSET\_ABNORMAL | 5 | 表示资产状态异常。 |
| ASSET\_DOWNLOADING | 6 | 表示资产正在下载到本地设备。 |

## SyncMode

PhonePC/2in1TabletTVWearable

指数据库同步模式。请使用枚举名称而非枚举值。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SYNC\_MODE\_PUSH | 0 | 表示数据从本地设备推送到远程设备。  **系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core |
| SYNC\_MODE\_PULL | 1 | 表示数据从远程设备拉至本地设备。  **系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core |
| SYNC\_MODE\_TIME\_FIRST10+ | 4 | 表示数据从修改时间较近的一端同步到修改时间较远的一端。  **系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client |
| SYNC\_MODE\_NATIVE\_FIRST10+ | 5 | 表示数据从本地设备同步到云端。  **系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client |
| SYNC\_MODE\_CLOUD\_FIRST10+ | 6 | 表示数据从云端同步到本地设备。  **系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client |

## Origin11+

PhonePC/2in1TabletTV

表示数据来源。请使用枚举名称而非枚举值。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LOCAL | 0 | 表示本地数据。 |
| CLOUD | 1 | 表示云端同步的数据。 |
| REMOTE | 2 | 表示端端同步的数据。 |

## Field11+

PhonePC/2in1TabletTV

用于谓词查询条件的特殊字段。请使用枚举名称而非枚举值。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CURSOR\_FIELD | '#\_cursor' | 用于cursor查找的字段名。 |
| ORIGIN\_FIELD | '#\_origin' | 用于cursor查找时指定数据来源的字段名。 |
| DELETED\_FLAG\_FIELD | '#\_deleted\_flag' | 用于cursor查找的结果集返回时填充的字段，表示云端删除的数据同步到本地后数据是否清理。  返回的结果集中，该字段对应的value为false表示数据未清理，true表示数据已清理。 |
| DATA\_STATUS\_FIELD12+ | '#\_data\_status' | 用于cursor查找的结果集返回时填充的字段，返回的结果集中，该字段对应的0表示正常数据，1表示退出账号保留数据，2表示云侧同步删除，3表示退出账户删除数据。 |
| OWNER\_FIELD | '#\_cloud\_owner' | 用于共享表中查找owner时，返回的结果集中填充的字段，表示当前共享记录的共享发起者。 |
| PRIVILEGE\_FIELD | '#\_cloud\_privilege' | 用于共享表中查找共享数据权限时，返回的结果集中填充的字段，表示当前共享记录的允许的操作权限。 |
| SHARING\_RESOURCE\_FIELD | '#\_sharing\_resource\_field' | 用于数据共享查找共享数据的共享资源时，返回的结果集中填充的字段，表示共享数据的共享资源标识。 |

## SubscribeType

PhonePC/2in1TabletTVWearable

描述订阅类型。请使用枚举名称而非枚举值。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUBSCRIBE\_TYPE\_REMOTE | 0 | 订阅远程数据更改。  **系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core |
| SUBSCRIBE\_TYPE\_CLOUD10+ | 1 | 订阅云端数据更改。  **系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client |
| SUBSCRIBE\_TYPE\_CLOUD\_DETAILS10+ | 2 | 订阅云端数据更改详情。  **系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client |
| SUBSCRIBE\_TYPE\_LOCAL\_DETAILS12+ | 3 | 订阅本地数据更改详情。  **系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core |

## RebuildType12+

PhonePC/2in1TabletTVWearable

描述数据库重建类型的枚举。请使用枚举名称而非枚举值。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 表示数据库未进行重建。 |
| REBUILT | 1 | 表示数据库进行了重建并且生成了空数据库，需要应用重新建表和恢复数据。 |
| REPAIRED | 2 | 表示数据库进行了修复，恢复了未损坏的数据，当前只有向量数据库（在[StoreConfig](arkts-apis-data-relationalstore-i.md#storeconfig)中配置vector为true）具备该能力。 |

## ChangeType10+

PhonePC/2in1TabletTVWearable

描述数据变更类型的枚举。请使用枚举名称而非枚举值。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DATA\_CHANGE | 0 | 表示是数据发生变更。 |
| ASSET\_CHANGE | 1 | 表示是资产附件发生了变更。 |

## DistributedType10+

PhonePC/2in1TabletTVWearable

描述表的分布式类型的枚举。请使用枚举名称而非枚举值。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DISTRIBUTED\_DEVICE | 0 | 表示在不同设备之间分布式的数据库表。  **系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core |
| DISTRIBUTED\_CLOUD | 1 | 表示在设备和云端之间分布式的数据库表。  **系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client |

## ConflictResolution10+

PhonePC/2in1TabletTVWearable

插入和修改接口的冲突解决模式。请使用枚举名称而非枚举值。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ON\_CONFLICT\_NONE | 0 | 表示当冲突发生时，不做任何处理。 |
| ON\_CONFLICT\_ROLLBACK | 1 | 表示当冲突发生时，中止SQL语句并回滚当前事务。 |
| ON\_CONFLICT\_ABORT | 2 | 表示当冲突发生时，中止当前SQL语句，并撤销当前 SQL 语句所做的任何更改，但是由同一事务中先前的 SQL 语句引起的更改被保留并且事务保持活动状态。 |
| ON\_CONFLICT\_FAIL | 3 | 表示当冲突发生时，中止当前 SQL 语句。但它不会撤销失败的 SQL 语句的先前更改，也不会结束事务。 |
| ON\_CONFLICT\_IGNORE | 4 | 表示当冲突发生时，跳过包含违反约束的行并继续处理 SQL 语句的后续行。 |
| ON\_CONFLICT\_REPLACE | 5 | 表示当冲突发生时，在插入或更新当前行之前删除导致约束违例的预先存在的行，并且命令会继续正常执行。 |

## Progress10+

PhonePC/2in1TabletTVWearable

描述端云同步过程的枚举。请使用枚举名称而非枚举值。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SYNC\_BEGIN | 0 | 表示端云同步过程开始。 |
| SYNC\_IN\_PROGRESS | 1 | 表示正在端云同步过程中。 |
| SYNC\_FINISH | 2 | 表示端云同步过程已完成。 |

## ProgressCode10+

PhonePC/2in1TabletTVWearable

表示端云同步过程的状态。请使用枚举名称而非枚举值。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUCCESS | 0 | 表示端云同步过程成功。 |
| UNKNOWN\_ERROR | 1 | 表示端云同步过程遇到未知错误。 |
| NETWORK\_ERROR | 2 | 表示端云同步过程遇到网络错误。 |
| CLOUD\_DISABLED | 3 | 表示云端不可用。 |
| LOCKED\_BY\_OTHERS | 4 | 表示有其他设备正在端云同步，本设备无法进行端云同步。  请确保无其他设备占用云端资源后，再使用本设备进行端云同步任务。 |
| RECORD\_LIMIT\_EXCEEDED | 5 | 表示本次端云同步需要同步的条目或大小超出最大值。由云端配置最大值。 |
| NO\_SPACE\_FOR\_ASSET | 6 | 表示云空间剩余空间小于待同步的资产大小。 |
| BLOCKED\_BY\_NETWORK\_STRATEGY12+ | 7 | 表示端云同步被网络策略限制。 |

## TransactionType14+

PhonePC/2in1TabletTVWearable

描述创建事务对象的枚举。请使用枚举名称而非枚举值。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFERRED | 0 | 表示创建一个DEFERRED类型的事务对象，该类型的事务对象在创建时只会关闭自动提交而不会真正开始事务，只有在首次读或写操作时会真正开始一个读或写事务。 |
| IMMEDIATE | 1 | 表示创建一个IMMEDIATE类型的事务对象，该类型的事务对象在创建时会真正开始一个写事务；如果有别的写事务未提交，则会创建失败，返回错误码14800024。 |
| EXCLUSIVE | 2 | 表示创建一个EXCLUSIVE类型的事务对象，该类型的事务在WAL模式下和IMMEDIATE相同，但在其他日志模式下能够防止事务期间有其他连接读取数据库。 |

## ColumnType18+

PhonePC/2in1TabletTVWearable

描述数据库列存储类型的枚举。请使用枚举名称而非枚举值。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NULL | 0 | 表示列数据类型为NULL。 |
| INTEGER | 1 | 表示列数据类型为64位整数。可用于保存8位（包括布尔值）、16位、32位、64位整数。如果64位整数大于2^53或小于-2^53，需使用[getString](arkts-apis-data-relationalstore-resultset.md#getstring)将64位整数转换为字符串。 |
| REAL | 2 | 表示列类型为浮点数。 |
| TEXT | 3 | 表示列类型为字符串。 |
| BLOB | 4 | 表示列类型为Uint8Array。 |
| ASSET | 5 | 表示列类型为[Asset](arkts-apis-data-relationalstore-i.md#asset10)。 |
| ASSETS | 6 | 表示列类型为[Assets](arkts-apis-data-relationalstore-t.md#assets10)。 |
| FLOAT\_VECTOR | 7 | 表示列类型为Float32Array。 |
| UNLIMITED\_INT | 8 | 表示列类型为bigint。 |

## DistributedTableType23+

PhonePC/2in1TabletTVWearable

分布式表类型的枚举。请使用枚举名称而非枚举值。此配置项为数据库级配置，如果数据库中有多张分布式表，则所有表必须使用相同的分布式表类型，且不支持切换升级。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**模型约束：** 此接口仅可在Stage模型下可用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEVICE\_COLLABORATION | 0 | 多设备协同表，各设备的数据将被隔离存储在独立的分布式表中，而非写入本地表，分布式表名为在原来表名前拼接对端设备的DeviceID标识符。 |
| SINGLE\_VERSION | 1 | 单版本表，数据通过分布式数据管理框架直接写入对端设备的本地表中。 |
