---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-js-add
title: 新增关键资产(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Asset Store Kit（关键资产存储服务） > Asset Store Kit开发指导(ArkTS) > 新增关键资产(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0ea34fa9f538f82da74fb9623fdca3018e20acf87c2cdf23bb710e27adcd9128
---

## 接口介绍

开发者可以查阅API文档，获取关键资产新增接口的详细说明：[add(attributes: AssetMap)](../harmonyos-references/js-apis-asset.md#assetadd)、同步接口[addSync(attributes: AssetMap)](../harmonyos-references/js-apis-asset.md#assetaddsync12)。

在新增关键资产时，关键资产属性的内容（AssetMap）参数如下表所示：

注意

下表中“ALIAS”和名称包含“DATA\_LABEL”的关键资产属性，用于存储业务自定义信息，其内容不会被加密，请勿存放敏感个人数据。

| 属性名称（Tag） | 属性内容（Value） | 是否必选 | 说明 |
| --- | --- | --- | --- |
| SECRET | 类型为Uint8Array，长度为1-1024字节。 | 必选 | 关键资产明文。 |
| ALIAS | 类型为Uint8Array，长度为1-256字节。 | 必选 | 关键资产别名，每条关键资产的唯一索引。 |
| ACCESSIBILITY | 类型为number，取值范围详见[Accessibility](../harmonyos-references/js-apis-asset.md#accessibility)。 | 可选 | 基于锁屏状态的访问控制，默认值为DEVICE\_FIRST\_UNLOCKED，即首次解锁后可访问。 |
| REQUIRE\_PASSWORD\_SET | 类型为boolean。 | 可选 | 是否仅在设置了锁屏密码的情况下，可访问关键资产。为true时，表示仅在用户设置了锁屏密码的情况下，关键资产才允许被访问；为false时，表示无论用户是否设置锁屏密码，关键资产均允许被访问。默认值为false。 |
| AUTH\_TYPE | 类型为number，取值范围详见[AuthType](../harmonyos-references/js-apis-asset.md#authtype)。 | 可选 | 访问关键资产所需的用户认证类型，默认值为NONE，即访问关键资产前无需用户认证。 |
| SYNC\_TYPE | 类型为number，取值范围详见[SyncType](../harmonyos-references/js-apis-asset.md#synctype)。 | 可选 | 关键资产支持的同步类型，默认值为NEVER，即不允许同步该关键资产。 |
| IS\_PERSISTENT | 类型为boolean。 | 可选 | 在应用卸载时是否需要保留关键资产。为true时表示应用卸载后，应用存储的关键资产将被保留；为false时表示应用卸载后，应用存储的关键资产将被删除。默认值为false。  **注意：** 设置此属性时，需[申请权限](declare-permissions.md)ohos.permission.STORE\_PERSISTENT\_DATA。 |
| DATA\_LABEL\_CRITICAL\_1 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且有完整性保护。  **说明：** API12前长度为1-512字节。 |
| DATA\_LABEL\_CRITICAL\_2 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且有完整性保护。  **说明：** API12前长度为1-512字节。 |
| DATA\_LABEL\_CRITICAL\_3 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且有完整性保护。  **说明：** API12前长度为1-512字节。 |
| DATA\_LABEL\_CRITICAL\_4 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且有完整性保护。  **说明：** API12前长度为1-512字节。 |
| DATA\_LABEL\_NORMAL\_1 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且无完整性保护。  **说明：** API12前长度为1-512字节。 |
| DATA\_LABEL\_NORMAL\_2 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且无完整性保护。  **说明：** API12前长度为1-512字节。 |
| DATA\_LABEL\_NORMAL\_3 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且无完整性保护。  **说明：** API12前长度为1-512字节。 |
| DATA\_LABEL\_NORMAL\_4 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且无完整性保护。  **说明：** API12前长度为1-512字节。 |
| DATA\_LABEL\_NORMAL\_LOCAL\_112+ | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属的本地信息，内容由业务自定义且无完整性保护，该项信息不会进行同步。 |
| DATA\_LABEL\_NORMAL\_LOCAL\_212+ | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属的本地信息，内容由业务自定义且无完整性保护，该项信息不会进行同步。 |
| DATA\_LABEL\_NORMAL\_LOCAL\_312+ | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属的本地信息，内容由业务自定义且无完整性保护，该项信息不会进行同步。 |
| DATA\_LABEL\_NORMAL\_LOCAL\_412+ | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属的本地信息，内容由业务自定义且无完整性保护，该项信息不会进行同步。 |
| CONFLICT\_RESOLUTION | 类型为number，取值范围详见[ConflictResolution](../harmonyos-references/js-apis-asset.md#conflictresolution)。 | 可选 | 新增关键资产时的冲突（如：别名相同）处理策略，默认值为THROW\_ERROR，即抛出异常，由业务进行后续处理。 |
| REQUIRE\_ATTR\_ENCRYPTED14+ | 类型为boolean。 | 可选 | 是否加密业务自定义附属信息。为true时表示业务自定义附属信息加密存储，为false时表示业务自定义附属信息不加密存储。默认值为false。 |
| GROUP\_ID18+ | 类型为Uint8Array，长度为7-127字节。 | 可选 | 待新增的关键资产所属群组，默认新增不属于任何群组的关键资产。 |
| WRAP\_TYPE18+ | 类型为number，取值范围详见[WrapType](../harmonyos-references/js-apis-asset.md#wraptype18)。 | 可选 | 关键资产支持的加密导入导出类型，默认值为NEVER，即不允许加密导入导出关键资产。 |

## 约束和限制

* 基于别名的访问

  关键资产以密文的形式存储在ASSET数据库中，以业务身份 + 别名作为唯一索引。故业务需要保证每条关键资产的别名唯一。
* 业务自定义数据存储

  ASSET为业务预留了12个关键资产自定义属性，名称以"DATA\_LABEL"开头。对于超过12个自定义属性的情况，业务可以将多段数据按照一定的格式（如JSON）拼接到同一个ASSET属性中。

  ASSET对部分属性会进行完整性保护，这部分属性名称以"DATA\_LABEL\_CRITICAL"开头，写入后不支持更新。

## 代码示例

说明

本模块提供了异步和同步两套接口，以下为异步接口的使用示例，同步接口详见[@ohos.security.asset (关键资产存储服务)](../harmonyos-references/js-apis-asset.md)API文档。

在指定群组中新增一条关键资产的使用示例详见[新增群组关键资产](asset-js-group-access-control.md#新增群组关键资产)。

新增一条密码是demo\_pwd，别名是demo\_alias，附属信息是demo\_label的关键资产，该关键资产在用户首次解锁设备后可被访问。

1. 引用头文件，定义工具函数。

   ```
   1. import { asset } from '@kit.AssetStoreKit';
   2. import { util } from '@kit.ArkTS';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. function stringToArray(str: string): Uint8Array {
   6. let textEncoder = new util.TextEncoder();
   7. return textEncoder.encodeInto(str);
   8. }
   ```

   [add.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/AssetStoreKit/AssetStoreArkTS/entry/src/main/ets/operations/add.ets#L17-L26)
2. 参考如下示例代码，进行业务功能开发。

   ```
   1. let attr: asset.AssetMap = new Map();
   2. attr.set(asset.Tag.SECRET, stringToArray('demo_pwd'));
   3. attr.set(asset.Tag.ALIAS, stringToArray('demo_alias'));
   4. attr.set(asset.Tag.ACCESSIBILITY, asset.Accessibility.DEVICE_FIRST_UNLOCKED);
   5. attr.set(asset.Tag.DATA_LABEL_NORMAL_1, stringToArray('demo_label'));
   6. try {
   7. asset.add(attr).then(() => {
   8. console.info(`Succeeded in adding Asset.`);
   9. // ...
   10. }).catch((err: BusinessError) => {
   11. console.error(`Failed to add Asset. Code is ${err.code}, message is ${err.message}`);
   12. // ...
   13. })
   14. } catch (error) {
   15. let err = error as BusinessError;
   16. console.error(`Failed to add Asset. Code is ${err.code}, message is ${err.message}`);
   17. // ...
   18. }
   ```

   [add.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/AssetStoreKit/AssetStoreArkTS/entry/src/main/ets/operations/add.ets#L30-L55)
