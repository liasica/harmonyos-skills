---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-js-remove
title: 删除关键资产(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Asset Store Kit（关键资产存储服务） > Asset Store Kit开发指导(ArkTS) > 删除关键资产(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:20e4300544b7944bd5987030bff2bbbe80733a9fd81b1e14f00f543354ef8d1e
---

## 接口介绍

开发者可以查阅API文档，获取关键资产删除接口的详细说明：[remove(query: AssetMap)](../harmonyos-references/js-apis-asset.md#assetremove)、同步接口[removeSync(query: AssetMap)](../harmonyos-references/js-apis-asset.md#assetremovesync12)。

在删除关键资产时，关键资产属性的内容（AssetMap）参数如下表所示：

注意

下表中“ALIAS”和名称包含“DATA\_LABEL”的关键资产属性，用于存储业务自定义信息，其内容不会被加密，请勿存放敏感个人数据。

| 属性名称（Tag） | 属性内容（Value） | 是否必选 | 说明 |
| --- | --- | --- | --- |
| ALIAS | 类型为Uint8Array，长度为1-256字节。 | 可选 | 关键资产别名，每条关键资产的唯一索引。 |
| ACCESSIBILITY | 类型为number，取值范围详见[Accessibility](../harmonyos-references/js-apis-asset.md#accessibility)。 | 可选 | 基于锁屏状态的访问控制。 |
| REQUIRE\_PASSWORD\_SET | 类型为boolean。 | 可选 | 是否仅在设置了锁屏密码的情况下，可访问关键资产。为true时表示删除仅用户设置了锁屏密码才允许访问的关键资产；为false时表示删除无论用户是否设置锁屏密码，均可访问的关键资产。 |
| AUTH\_TYPE | 类型为number，取值范围详见[AuthType](../harmonyos-references/js-apis-asset.md#authtype)。 | 可选 | 访问关键资产所需的用户认证类型。 |
| SYNC\_TYPE | 类型为number，取值范围详见[SyncType](../harmonyos-references/js-apis-asset.md#synctype)。 | 可选 | 关键资产支持的同步类型。 |
| IS\_PERSISTENT | 类型为boolean。 | 可选 | 在应用卸载时是否需要保留关键资产。为true时表示删除应用卸载后会被保留的关键资产；为false时表示删除应用卸载后会被删除的关键资产。 |
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
| REQUIRE\_ATTR\_ENCRYPTED14+ | 类型为boolean。 | 可选 | 是否删除业务自定义附属信息被加密的数据。为true时表示删除业务自定义附属信息加密存储的数据，为false时表示删除业务自定义附属信息不加密存储的数据。默认值为false。 |
| GROUP\_ID18+ | 类型为Uint8Array，长度为7-127字节。 | 可选 | 待删除的关键资产所属群组，默认删除不属于任何群组的关键资产。 |

## 代码示例

说明

本模块提供了异步和同步两套接口，以下为异步接口的使用示例，同步接口详见[@ohos.security.asset (关键资产存储服务)](../harmonyos-references/js-apis-asset.md)。

在指定群组中删除一条关键资产的使用示例详见[删除群组关键资产](asset-js-group-access-control.md#删除群组关键资产)。

在删除前，需确保已有关键资产，可参考[指南文档](asset-js-add.md)新增关键资产，否则将抛出NOT\_FOUND错误（错误码24000002）。

删除一条别名是demo\_alias的关键资产。

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

   [remove.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/AssetStoreKit/AssetStoreArkTS/entry/src/main/ets/operations/remove.ets#L17-L26)
2. 参考如下示例代码，进行业务功能开发。

   ```
   1. let query: asset.AssetMap = new Map();
   2. query.set(asset.Tag.ALIAS, stringToArray('demo_alias')); // 此处指定别名删除单条关键资产，也可不指定别名删除多条关键资产。
   3. try {
   4. asset.remove(query).then(() => {
   5. console.info(`Succeeded in removing Asset.`);
   6. // ...
   7. }).catch((err: BusinessError) => {
   8. console.error(`Failed to remove Asset. Code is ${err.code}, message is ${err.message}`);
   9. // ...
   10. });
   11. } catch (error) {
   12. let err = error as BusinessError;
   13. console.error(`Failed to remove Asset. Code is ${err.code}, message is ${err.message}`);
   14. // ...
   15. }
   ```

   [remove.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/AssetStoreKit/AssetStoreArkTS/entry/src/main/ets/operations/remove.ets#L30-L52)
