---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-js-update
title: 更新关键资产(ArkTS)
breadcrumb: 指南 > 系统 > 安全 > Asset Store Kit（关键资产存储服务） > Asset Store Kit开发指导(ArkTS) > 更新关键资产(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:97e546ca058069458981fbf291e94ed5d5c8da09ce53ed3cc433dfe84f47bae0
---

## 接口介绍

开发者可以查阅API文档，获取关键资产更新接口的详细说明：[update(query: AssetMap, attributesToUpdate: AssetMap)](../harmonyos-references/js-apis-asset.md#assetupdate)、同步接口[updateSync(query: AssetMap, attributesToUpdate: AssetMap)](../harmonyos-references/js-apis-asset.md#assetupdatesync12)。

在更新关键资产时，关键资产属性的内容（AssetMap）参数如下表所示：

注意

下表中“ALIAS”和名称包含“DATA\_LABEL”的关键资产属性，用于存储业务自定义信息，其内容不会被加密，请勿存放敏感个人数据。

* **query的参数列表：**

  | 属性名称（Tag） | 属性内容（Value） | 是否必选 | 说明 |
  | --- | --- | --- | --- |
  | ALIAS | 类型为Uint8Array，长度为1-256字节。 | 必选 | 关键资产别名，每条关键资产的唯一索引。 |
  | ACCESSIBILITY | 类型为number，取值范围详见[Accessibility](../harmonyos-references/js-apis-asset.md#accessibility)。 | 可选 | 基于锁屏状态的访问控制。 |
  | REQUIRE\_PASSWORD\_SET | 类型为boolean。 | 可选 | 是否仅在设置了锁屏密码的情况下，可访问关键资产。为true时表示更新仅用户设置了锁屏密码才允许访问的关键资产；为false时表示更新无论用户是否设置锁屏密码，均可访问的关键资产。 |
  | AUTH\_TYPE | 类型为number，取值范围详见[AuthType](../harmonyos-references/js-apis-asset.md#authtype)。 | 可选 | 访问关键资产所需的用户认证类型。 |
  | SYNC\_TYPE | 类型为number，取值范围详见[SyncType](../harmonyos-references/js-apis-asset.md#synctype)。 | 可选 | 关键资产支持的同步类型。 |
  | IS\_PERSISTENT | 类型为boolean。 | 可选 | 在应用卸载时是否需要保留关键资产。为true时表示更新应用卸载后会被保留的关键资产；为false时表示更新应用卸载后会被删除的关键资产。 |
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
  | REQUIRE\_ATTR\_ENCRYPTED14+ | 类型为boolean。 | 可选 | 是否更新业务自定义附属信息被加密的数据。为true时表示更新业务自定义附属信息加密存储的数据，为false时表示更新业务自定义附属信息不加密存储的数据。默认值为false。 |
  | GROUP\_ID18+ | 类型为Uint8Array，长度为7-127字节。 | 可选 | 待更新的关键资产所属群组，默认更新不属于任何群组的关键资产。 |
* **attributesToUpdate的参数列表：**

  | 属性名称（Tag） | 属性内容（Value） | 是否必选 | 说明 |
  | --- | --- | --- | --- |
  | SECRET | 类型为Uint8Array，长度为1-1024字节。 | 可选 | 关键资产明文。 |
  | DATA\_LABEL\_NORMAL\_1 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且无完整性保护。  **说明：** API12前长度为1-512字节。 |
  | DATA\_LABEL\_NORMAL\_2 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且无完整性保护。  **说明：** API12前长度为1-512字节。 |
  | DATA\_LABEL\_NORMAL\_3 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且无完整性保护。  **说明：** API12前长度为1-512字节。 |
  | DATA\_LABEL\_NORMAL\_4 | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且无完整性保护。  **说明：** API12前长度为1-512字节。 |
  | DATA\_LABEL\_NORMAL\_LOCAL\_112+ | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属的本地信息，内容由业务自定义且无完整性保护，该项信息不会进行同步。 |
  | DATA\_LABEL\_NORMAL\_LOCAL\_212+ | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属的本地信息，内容由业务自定义且无完整性保护，该项信息不会进行同步。 |
  | DATA\_LABEL\_NORMAL\_LOCAL\_312+ | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属的本地信息，内容由业务自定义且无完整性保护，该项信息不会进行同步。 |
  | DATA\_LABEL\_NORMAL\_LOCAL\_412+ | 类型为Uint8Array，长度为1-2048字节。 | 可选 | 关键资产附属的本地信息，内容由业务自定义且无完整性保护，该项信息不会进行同步。 |

## 代码示例

说明

本模块提供了异步和同步两套接口，以下为异步接口的使用示例，同步接口详见[@ohos.security.asset (关键资产存储服务)](../harmonyos-references/js-apis-asset.md)。

在指定群组中更新一条关键资产的使用示例详见[更新群组关键资产](asset-js-group-access-control.md#更新群组关键资产)。

在更新前，需确保已有关键资产，可参考[指南文档](asset-js-add.md)新增关键资产，否则将抛出NOT\_FOUND错误（错误码24000002）。

更新别名是demo\_alias的关键资产，将关键资产明文更新为demo\_pwd\_new，附属属性更新成demo\_label\_new。

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

   [update.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/AssetStoreKit/AssetStoreArkTS/entry/src/main/ets/operations/update.ets#L17-L26)
2. 参考如下示例代码，进行业务功能开发。

   ```
   1. let query: asset.AssetMap = new Map();
   2. query.set(asset.Tag.ALIAS, stringToArray('demo_alias'));
   3. let attrsToUpdate: asset.AssetMap = new Map();
   4. attrsToUpdate.set(asset.Tag.SECRET, stringToArray('demo_pwd_new'));
   5. attrsToUpdate.set(asset.Tag.DATA_LABEL_NORMAL_1, stringToArray('demo_label_new'));
   6. try {
   7. asset.update(query, attrsToUpdate).then(() => {
   8. console.info(`Succeeded in updating Asset.`);
   9. // ...
   10. }).catch((err: BusinessError) => {
   11. console.error(`Failed to update Asset. Code is ${err.code}, message is ${err.message}`);
   12. // ...
   13. });
   14. } catch (error) {
   15. let err = error as BusinessError;
   16. console.error(`Failed to update Asset. Code is ${err.code}, message is ${err.message}`);
   17. // ...
   18. }
   ```

   [update.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/AssetStoreKit/AssetStoreArkTS/entry/src/main/ets/operations/update.ets#L30-L55)
