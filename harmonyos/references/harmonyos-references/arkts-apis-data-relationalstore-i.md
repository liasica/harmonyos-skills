---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-i
title: Interfaces (其他)
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > ArkTS API > @ohos.data.relationalStore (关系型数据库) > Interfaces (其他)
category: harmonyos-references
scraped_at: 2026-04-28T07:59:17+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:2feaf927ca09f3190ce00f1e15affa4f591268d7898fe57397573ec91c2b7703
---

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## StoreConfig

PhonePC/2in1TabletTVWearable

管理关系数据库配置。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 数据库文件名，也是数据库唯一标识符。同一进程禁止创建两个同名的数据库，否则可能导致端端同步、端云同步、静默访问以及密钥备份等功能出现异常。  **系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core |
| securityLevel | [SecurityLevel](arkts-apis-data-relationalstore-e.md#securitylevel) | 否 | 否 | 设置数据库安全级别。  **系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core |
| encrypt | boolean | 否 | 是 | 指定数据库是否加密，默认不加密。数据库创建完成后，此参数不允许直接修改。如需变更数据库加密状态，请调用[rekeyEx](arkts-apis-data-relationalstore-rdbstore.md#rekeyex22)接口进行更新操作。  true：加密。  false：非加密。  **系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core |
| dataGroupId10+ | string | 否 | 是 | 应用组ID，需要向应用市场获取，详见[dataGroupId申请流程](../harmonyos-guides/ime-kit-security.md#共享沙箱介绍)。基于dataGroupId的数据共享支持两种场景：1.同一应用的不同进程间共享，只支持三方应用中输入法和输入法的扩展场景使用；2.不同应用间的数据共享，只支持系统应用使用。  **模型约束：** 此属性仅在Stage模型下可用。  从API version 10开始，支持此可选参数。dataGroupId共享沙箱的方式不支持多进程访问加密数据库，当此参数不填时，默认在本应用沙箱目录下创建RdbStore实例。  **系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core |
| customDir11+ | string | 否 | 是 | 数据库自定义路径。  **使用约束：** 数据库路径大小限制为128字节，如果超过该大小会开库失败，返回错误。  从API version 11开始，支持此可选参数。数据库将在如下的目录结构中被创建：context.databaseDir + "/rdb/" + customDir，其中context.databaseDir是应用沙箱对应的路径，"/rdb/"表示创建的是关系型数据库，customDir表示自定义的路径。当此参数不填时，默认在本应用沙箱目录下创建RdbStore实例。从API version 18开始，如果同时配置了rootDir参数，将打开或删除如下路径数据库：rootDir + "/" + customDir + "/" + name。  **系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core |
| rootDir18+ | string | 否 | 是 | 指定数据库根路径。  从API version 18开始，支持此可选参数。将从如下目录打开或删除数据库：rootDir + "/" + customDir。通过设置此参数打开的数据库为只读模式，不允许对数据库进行写操作，否则返回错误码801。配置此参数打开或删除数据库时，应确保对应路径下数据库文件存在，并且有读取权限，否则返回错误码14800010。  **系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core |
| autoCleanDirtyData11+ | boolean | 否 | 是 | 指定是否自动清理云端删除后同步到本地的数据，true表示自动清理，false表示手动清理，默认自动清理。  对于端云协同的数据库，当云端删除的数据同步到设备端时，可通过该参数设置设备端是否自动清理。手动清理可以通过[cleanDirtyData11+](arkts-apis-data-relationalstore-rdbstore.md#cleandirtydata11)接口清理。  从API version 11开始，支持此可选参数。  **系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client |
| allowRebuild12+ | boolean | 否 | 是 | 指定数据库是否支持异常时自动删除，并重建一个空库空表，默认不删除。  true：自动删除。  false：不自动删除。  从API version 12开始，支持此可选参数。  **系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core |
| isReadOnly12+ | boolean | 否 | 是 | 指定数据库是否只读，默认为数据库可读写。  true：只允许从数据库读取数据，不允许对数据库进行写操作，否则会返回错误码801。  false：允许对数据库进行读写操作。  从API version 12开始，支持此可选参数。  **系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core |
| pluginLibs12+ | Array<string> | 否 | 是 | 配置加载自定义动态库，数组中可传入多个动态库名称。具体请见[pluginLibs的使用约束和示例](arkts-apis-data-relationalstore-i.md#pluginlibs的使用约束和示例)。  **系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core |
| cryptoParam14+ | [CryptoParam](arkts-apis-data-relationalstore-i.md#cryptoparam14) | 否 | 是 | 指定用户自定义的加密参数。  当此参数不填时，使用默认的加密参数，见[CryptoParam](arkts-apis-data-relationalstore-i.md#cryptoparam14)各参数默认值。  此配置只有在encrypt选项设置为真或密钥非空时才有效。  从API version 14开始，支持此可选参数。  **系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core |
| vector18+ | boolean | 否 | 是 | 指定数据库是否是向量数据库，true表示向量数据库，false表示关系型数据库，默认为false。  向量数据库适用于存储和处理高维向量数据，关系型数据库适用于存储和处理结构化数据。  当使用向量数据库时，在调用deleteRdbStore接口前，应当确保向量数据库已打开的RdbStore和ResultSet均已成功关闭。  **系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core |
| tokenizer17+ | [Tokenizer](arkts-apis-data-relationalstore-e.md#tokenizer17) | 否 | 是 | 指定用户在fts场景下使用哪种分词器。  当此参数不填时，则在fts下不支持中文以及多国语言分词，但仍可支持英文分词。  如果用户想使用自定义分词器，可以通过pluginLibs参数进行配置，具体请见[pluginLibs的使用约束和示例](arkts-apis-data-relationalstore-i.md#pluginlibs的使用约束和示例)。  **系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core |
| persist18+ | boolean | 否 | 是 | 指定数据库是否需要持久化。true表示持久化，false表示不持久化，即内存数据库。默认为true。  内存数据库不支持加密、backup、restore、跨进程访问及分布式能力，securityLevel属性会被忽略。  **系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core |
| enableSemanticIndex20+ | boolean | 否 | 是 | 指定数据库是否启用语义索引处理功能。true表示启用语义索引处理功能，false表示不启用。默认为false。  **系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core |

## CryptoParam14+

PhonePC/2in1TabletTVWearable

数据库加密参数配置。此配置只有在StoreConfig的encrypt选项设置为true或密钥非空时有效。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| encryptionKey | Uint8Array | 否 | 否 | 指定数据库加/解密使用的密钥。  如传入密钥为空，则由数据库负责生成并保存密钥，并使用生成的密钥打开数据库文件。  使用完后用户需要将密钥内容全部置为零。 |
| iterationCount | number | 否 | 是 | 整数类型，指定数据库PBKDF2算法的迭代次数，默认值为10000。  迭代次数应当为大于零的整数，若非整数则向下取整。  不指定此参数或指定为零时，使用默认值10000，并使用默认加密算法AES\_256\_GCM。 |
| encryptionAlgo | [EncryptionAlgo](arkts-apis-data-relationalstore-e.md#encryptionalgo14) | 否 | 是 | 指定数据库加解密使用的加密算法。如不指定，默认值为 AES\_256\_GCM。 |
| hmacAlgo | [HmacAlgo](arkts-apis-data-relationalstore-e.md#hmacalgo14) | 否 | 是 | 指定数据库加解密使用的HMAC算法。如不指定，默认值为SHA256。 |
| kdfAlgo | [KdfAlgo](arkts-apis-data-relationalstore-e.md#kdfalgo14) | 否 | 是 | 指定数据库加解密使用的PBKDF2算法。如不指定，默认使用和HMAC算法相等的算法。 |
| cryptoPageSize | number | 否 | 是 | 整数类型，指定数据库加解密使用的页大小，单位：字节。如不指定，默认值为1024字节。  用户指定的页大小应为1024到65536范围内的整数，并且为2n。若指定值非整数，则向下取整。 |

## Asset10+

PhonePC/2in1TabletTVWearable

记录资产附件（文件、图片、视频等类型文件）的相关信息。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 资产的名称。 |
| uri | string | 否 | 否 | 资产的uri，在系统里的绝对路径。 |
| path | string | 否 | 否 | 资产在应用沙箱里的路径。 |
| createTime | string | 否 | 否 | 资产被创建出来的时间。 |
| modifyTime | string | 否 | 否 | 资产最后一次被修改的时间。 |
| size | string | 否 | 否 | 资产占用空间的大小。在端云同步机制中，本字段作为判定资产是否发生变更的关键依据之一，需确保在全链路中保持统一、一致的存储格式与取值逻辑。建议所有系统节点均采用标准化处理方式（单位为字节（Byte），取值为非负整数），避免因格式差异导致同步异常或误判。 |
| status | [AssetStatus](arkts-apis-data-relationalstore-e.md#assetstatus10) | 否 | 是 | 资产的状态，默认值为ASSET\_NORMAL。 |

## ChangeInfo10+

PhonePC/2in1TabletTVWearable

记录端云同步过程详情。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| table | string | 否 | 否 | 表示发生变化的表的名称。 |
| type | [ChangeType](arkts-apis-data-relationalstore-e.md#changetype10) | 否 | 否 | 表示发生变化的数据的类型，数据或者资产附件发生变化。 |
| inserted | Array<string> | Array<number> | 否 | 否 | 记录插入数据的位置，如果该表的主键是string类型，该值是主键的值，否则该值表示插入数据的行号。 |
| updated | Array<string> | Array<number> | 否 | 否 | 记录更新数据的位置，如果该表的主键是string类型，该值是主键的值，否则该值表示更新数据的行号。 |
| deleted | Array<string> | Array<number> | 否 | 否 | 记录删除数据的位置，如果该表的主键是string类型，该值是主键的值，否则该值表示删除数据的行号。 |

## DistributedConfig10+

PhonePC/2in1TabletTVWearable

记录表的分布式配置信息。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| autoSync | boolean | 否 | 否 | 表示该表是否支持端云自动同步。为true时，支持系统自动触发端云同步；为false时不支持系统自动触发端云同步，需要调用[cloudSync](arkts-apis-data-relationalstore-rdbstore.md#cloudsync10-3)接口触发端云同步。 |
| asyncDownloadAsset18+ | boolean | 否 | 是 | 表示当前数据库在端云同步时，同步或异步下载资产。true表示优先下载完所有数据后，使用异步任务下载资产；false表示同步下载资产；默认值为false。 |
| enableCloud18+ | boolean | 否 | 是 | 表示当前数据库是否允许端云同步。true表示允许端云同步；false表示不允许端云同步。默认值为true。 |
| tableType23+ | [DistributedTableType](arkts-apis-data-relationalstore-e.md#distributedtabletype23) | 否 | 是 | 分布式表类型。DEVICE\_COLLABORATION表示设备协作表；SINGLE\_VERSION表示单版本表。跨设备数据同步时，默认值为DEVICE\_COLLABORATION；端云数据同步时，默认值为SINGLE\_VERSION，不支持DEVICE\_COLLABORATION。 |

## Statistic10+

PhonePC/2in1TabletTVWearable

描述数据库表的端云同步过程的统计信息。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| total | number | 否 | 否 | 表示数据库表中需要端云同步的总行数。 |
| successful | number | 否 | 否 | 表示数据库表中端云同步成功的行数。 |
| failed | number | 否 | 否 | 表示数据库表中端云同步失败的行数。 |
| remained | number | 否 | 否 | 表示数据库表中端云同步剩余未执行的行数。 |

## TableDetails10+

PhonePC/2in1TabletTVWearable

描述数据库表执行端云同步任务上传和下载的统计信息。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| upload | [Statistic](arkts-apis-data-relationalstore-i.md#statistic10) | 否 | 否 | 表示数据库表中端云同步上传过程的统计信息。 |
| download | [Statistic](arkts-apis-data-relationalstore-i.md#statistic10) | 否 | 否 | 表示数据库表中端云同步下载过程的统计信息。 |

## ProgressDetails10+

PhonePC/2in1TabletTVWearable

描述数据库整体执行端云同步任务上传和下载的统计信息。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| schedule | [Progress](arkts-apis-data-relationalstore-e.md#progress10) | 否 | 否 | 表示端云同步过程。 |
| code | [ProgressCode](arkts-apis-data-relationalstore-e.md#progresscode10) | 否 | 否 | 表示端云同步过程的状态。 |
| details | Record<string, [TableDetails](arkts-apis-data-relationalstore-i.md#tabledetails10)> | 否 | 否 | 表示端云同步各表的统计信息。  键表示表名，值表示该表的端云同步过程统计信息。 |

## SqlExecutionInfo12+

PhonePC/2in1TabletTVWearable

描述数据库执行的SQL语句的统计信息。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sql | Array<string> | 否 | 否 | 表示执行的SQL语句的数组。当[batchInsert](arkts-apis-data-relationalstore-rdbstore.md#batchinsert)的参数太大时，可能有多个SQL。 |
| totalTime | number | 否 | 否 | 表示执行SQL语句的总时间，单位为μs。 |
| waitTime | number | 否 | 否 | 表示获取句柄的时间，单位为μs。 |
| prepareTime | number | 否 | 否 | 表示准备SQL和绑定参数的时间，单位为μs。 |
| executeTime | number | 否 | 否 | 表示执行SQL语句的时间，单位为μs。 |

## SqlInfo20+

PhonePC/2in1TabletTVWearable

描述数据库执行的SQL语句的详细信息。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sql | string | 否 | 否 | 表示执行的sql语句。 |
| args | Array<[ValueType](arkts-apis-data-relationalstore-t.md#valuetype)> | 否 | 否 | 表示执行SQL中的参数信息。 |

## ExceptionMessage20+

PhonePC/2in1TabletTVWearable

描述数据库执行的SQL语句的错误信息。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | number | 否 | 否 | 表示执行SQL返回的错误码，对应的取值和含义请见[sqlite错误码](https://www.sqlite.org/rescode.html) |
| message | string | 否 | 否 | 表示执行SQL返回的错误信息。 |
| sql | string | 否 | 否 | 表示报错执行的SQL语句。 |

## TransactionOptions14+

PhonePC/2in1TabletTVWearable

事务对象的配置信息。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| transactionType | [TransactionType](arkts-apis-data-relationalstore-e.md#transactiontype14) | 否 | 是 | 事务类型。默认为DEFERRED。 |

## pluginLibs的使用约束和示例

PhonePC/2in1TabletTVWearable

**使用约束：**

1. 动态库名的数量限制最多为16个，如果超过该数量会开库失败，返回错误码14800000。

2. 动态库名需为本应用沙箱路径下或系统路径下的动态库，如果动态库无法加载会开库失败，返回错误码14800010。

3. 动态库名需为完整路径，用于被sqlite加载。路径由[context.bundleCodeDir+ "/libs/arm64/" + so名称]组成，其中context.bundleCodeDir是应用沙箱对应的路径，"libs"是固定目录，"arm64"是由系统架构确定的子目录，例如，系统架构为arm64-v8a时，子目录为"arm64"。

样例：[context.bundleCodeDir+ "/libs/arm64/" + libtokenizer.so]。当此参数不填时，默认不加载动态库。

4. 动态库需要包含其全部依赖，避免依赖项丢失导致无法运行。

例如：在ndk工程中，使用默认编译参数构建libtokenizer.so，此动态库依赖c++标准库。在加载此动态库时，由于namespace与编译时不一致，链接到了错误的libc++\_shared.so，导致\_\_emutls\_get\_address符号找不到。要解决此问题，需在编译时静态链接c++标准库，具体请参见[NDK工程构建概述](../harmonyos-guides/build-with-ndk-overview.md)。

**使用pluginLibs加载开发者自定义分词器示例：**

1. 开发者需要实现一个fts5可加载分词器扩展，并将其编译成so，编译可参考[使用命令行CMake构建NDK工程](../harmonyos-guides/build-with-ndk-cmake.md)。

2. 将生成的so文件拷贝到工程目录"entry/libs/"文件夹下的相应子目录中(没有相应目录时用户可自行创建)，子目录根据系统架构确定。例如，系统架构为arm64-v8a时，放置在"entry/libs/arm64-v8a"目录下；系统架构为armeabi-v7a时，放置在"entry/libs/armeabi-v7a"目录下。

3. 加载自定义分词器。

```
1. import { relationalStore } from '@kit.ArkData'
2. import { UIAbility } from '@kit.AbilityKit';
3. import { window } from '@kit.ArkUI';
4. import { fileIo } from '@kit.CoreFileKit'

6. export default class EntryAbility extends UIAbility {
7. async onWindowStageCreate(windowStage: window.WindowStage) {
8. let rdbStore: relationalStore.RdbStore | undefined = undefined;
9. const STORE_CONFIG: relationalStore.StoreConfig = {
10. name: "testTokenize.db",
11. securityLevel: relationalStore.SecurityLevel.S1,
12. };
13. let bundleCodeDir = this.context.bundleCodeDir;
14. // libdistributeddb_extension.so为实现的fts5可加载分词器扩展编译成的so名称
15. let soPath = bundleCodeDir + "/libs/arm64/libdistributeddb_extension.so";
16. let res = await fileIo.access(soPath);
17. if (!res) {
18. console.error("Dynamic library not accessible");
19. return;
20. }
21. console.info("Dynamic library found and accessible");

23. // 将pluginLibs配置为需要加载的动态库拓展路径。
24. STORE_CONFIG.pluginLibs = [soPath];
25. try {
26. rdbStore = await relationalStore.getRdbStore(this.context, STORE_CONFIG);
27. // 使用自定义分词器创建fts5虚拟表，tokenize后面是实现的分词器名称
28. await rdbStore.executeSql("CREATE VIRTUAL TABLE IF NOT EXISTS pages USING fts5(title, keywords, body, tokenize=koowork_tokenizer);");
29. console.info("CREATE VIRTUAL TABLE OK");
30. await rdbStore.executeSql("INSERT INTO pages(keywords, title, body) VALUES('歌曲', 'xxx', '1234歌曲，像北哈升');");
31. console.info("INSERT VIRTUAL TABLE OK, body is '1234歌曲，像北哈升'");
32. await rdbStore.executeSql("INSERT INTO pages(keywords, title, body) VALUES('歌曲', 'xxx', '我爱北京天安门, 天安门上太阳升');");
33. console.info("INSERT VIRTUAL TABLE OK, body is '我爱北京天安门, 天安门上太阳升'");
34. let resultSet = await rdbStore.querySql("select * from pages where body match '天安门';");
35. while (resultSet.goToNextRow()) {
36. console.info(`query result success, match body:${resultSet.getString(resultSet.getColumnIndex("body"))}`);
37. }
38. resultSet.close();
39. await rdbStore.close();
40. } catch (err) {
41. console.error("RdbStore failed, err: code=" + err.code + " message=" + err.message);
42. }
43. }
44. }
```

## ReturningConfig23+

PhonePC/2in1TabletTVWearable

指定returning相关接口操作后需要返回的字段名列表和结果集中允许包含的最大记录数。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**模型约束：** 此接口仅在Stage模型下可用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| columns | Array<string> | 否 | 否 | 指定结果集中返回的字段，支持传入1到4个字段。注意：不能传入带有空格、逗号以及星号的字段名。 |
| maxReturningCount | number | 否 | 是 | 指定结果集返回的最大行数量，默认为1024条，最大支持32766条。注意：当实际修改行数超过maxReturningCount设置的值时，系统会丢弃超出部分的数据。 |

## Result23+

PhonePC/2in1TabletTVWearable

记录受影响的数据行数量和结果集。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**模型约束：** 此接口仅在Stage模型下可用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| changed | number | 是 | 否 | 表示受影响的行数量。 |
| resultSet | [LiteResultSet](arkts-apis-data-relationalstore-literesultset.md) | 是 | 否 | 表示受影响数据的结果集。默认返回1024行，最大支持32766行，超出部分将被丢弃。 |
