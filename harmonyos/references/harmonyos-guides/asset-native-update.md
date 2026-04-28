---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-native-update
title: 更新关键资产(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Asset Store Kit（关键资产存储服务） > Asset Store Kit开发指导(C/C++) > 更新关键资产(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:46213606eafd0be604115649f268543fb2688b7ec3ccffde01575622d8aa829d
---

## 接口介绍

开发者可以查阅API文档，获取关键资产更新接口的详细说明：[OH\_Asset\_Update](../harmonyos-references/capi-asset-api-h.md#oh_asset_update)。

在更新关键资产时，关键资产属性的内容参数如下表所示：

注意

下表中“ASSET\_TAG\_ALIAS”和名称包含“ASSET\_TAG\_DATA\_LABEL”的关键资产属性，用于存储业务自定义信息，其内容不会被加密，请勿存放敏感个人数据。

* **query的参数列表：**

  | 属性名称（Asset\_Tag） | 属性内容（Asset\_Value） | 是否必选 | 说明 |
  | --- | --- | --- | --- |
  | ASSET\_TAG\_ALIAS | 类型为uint8[]，长度为1-256字节。 | 必选 | 关键资产别名，每条关键资产的唯一索引。 |
  | ASSET\_TAG\_ACCESSIBILITY | 类型为uint32\_t，取值范围详见[Asset\_Accessibility](../harmonyos-references/capi-asset-type-h.md#asset_accessibility)。 | 可选 | 基于锁屏状态的访问控制。 |
  | ASSET\_TAG\_REQUIRE\_PASSWORD\_SET | 类型为bool。 | 可选 | 是否仅在设置了锁屏密码的情况下，可访问关键资产。为true时表示更新仅用户设置了锁屏密码才允许访问的关键资产；为false时表示更新无论用户是否设置锁屏密码，均可访问的关键资产。 |
  | ASSET\_TAG\_AUTH\_TYPE | 类型为uint32\_t，取值范围详见[Asset\_AuthType](../harmonyos-references/capi-asset-type-h.md#asset_authtype)。 | 可选 | 访问关键资产所需的用户认证类型。 |
  | ASSET\_TAG\_SYNC\_TYPE | 类型为uint32\_t，取值范围详见[Asset\_SyncType](../harmonyos-references/capi-asset-type-h.md#asset_synctype)。 | 可选 | 关键资产支持的同步类型。 |
  | ASSET\_TAG\_IS\_PERSISTENT | 类型为bool。 | 可选 | 在应用卸载时是否需要保留关键资产。为true时表示更新应用卸载后会被保留的关键资产；为false时表示更新应用卸载后会被删除的关键资产。 |
  | ASSET\_TAG\_DATA\_LABEL\_CRITICAL\_1 | 类型为uint8[]，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且有完整性保护。  **说明：** API12前长度为1-512字节。 |
  | ASSET\_TAG\_DATA\_LABEL\_CRITICAL\_2 | 类型为uint8[]，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且有完整性保护。  **说明：** API12前长度为1-512字节。 |
  | ASSET\_TAG\_DATA\_LABEL\_CRITICAL\_3 | 类型为uint8[]，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且有完整性保护。  **说明：** API12前长度为1-512字节。 |
  | ASSET\_TAG\_DATA\_LABEL\_CRITICAL\_4 | 类型为uint8[]，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且有完整性保护。  **说明：** API12前长度为1-512字节。 |
  | ASSET\_TAG\_DATA\_LABEL\_NORMAL\_1 | 类型为uint8[]，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且无完整性保护。  **说明：** API12前长度为1-512字节。 |
  | ASSET\_TAG\_DATA\_LABEL\_NORMAL\_2 | 类型为uint8[]，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且无完整性保护。  **说明：** API12前长度为1-512字节。 |
  | ASSET\_TAG\_DATA\_LABEL\_NORMAL\_3 | 类型为uint8[]，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且无完整性保护。  **说明：** API12前长度为1-512字节。 |
  | ASSET\_TAG\_DATA\_LABEL\_NORMAL\_4 | 类型为uint8[]，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且无完整性保护。  **说明：** API12前长度为1-512字节。 |
  | ASSET\_TAG\_DATA\_LABEL\_NORMAL\_LOCAL\_112+ | 类型为uint8[]，长度为1-2048字节。 | 可选 | 关键资产附属的本地信息，内容由业务自定义且无完整性保护，该项信息不会进行同步。 |
  | ASSET\_TAG\_DATA\_LABEL\_NORMAL\_LOCAL\_212+ | 类型为uint8[]，长度为1-2048字节。 | 可选 | 关键资产附属的本地信息，内容由业务自定义且无完整性保护，该项信息不会进行同步。 |
  | ASSET\_TAG\_DATA\_LABEL\_NORMAL\_LOCAL\_312+ | 类型为uint8[]，长度为1-2048字节。 | 可选 | 关键资产附属的本地信息，内容由业务自定义且无完整性保护，该项信息不会进行同步。 |
  | ASSET\_TAG\_DATA\_LABEL\_NORMAL\_LOCAL\_412+ | 类型为uint8[]，长度为1-2048字节。 | 可选 | 关键资产附属的本地信息，内容由业务自定义且无完整性保护，该项信息不会进行同步。 |
  | ASSET\_TAG\_REQUIRE\_ATTR\_ENCRYPTED14+ | 类型为bool。 | 可选 | 是否更新业务自定义附属信息被加密的数据。为true时表示更新业务自定义附属信息加密存储的数据，为false时表示更新业务自定义附属信息不加密存储的数据。默认值为false。 |
  | ASSET\_TAG\_GROUP\_ID18+ | 类型为uint8[]，长度为7-127字节。 | 可选 | 待更新的关键资产所属群组，默认更新不属于任何群组的关键资产。 |
* **attributesToUpdate的参数列表：**

  | 属性名称（Asset\_Tag） | 属性内容（Asset\_Value） | 是否必选 | 说明 |
  | --- | --- | --- | --- |
  | ASSET\_TAG\_SECRET | 类型为uint8[]，长度为1-1024字节。 | 可选 | 关键资产明文。 |
  | ASSET\_TAG\_DATA\_LABEL\_NORMAL\_1 | 类型为uint8[]，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且无完整性保护。  **说明：** API12前长度为1-512字节。 |
  | ASSET\_TAG\_DATA\_LABEL\_NORMAL\_2 | 类型为uint8[]，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且无完整性保护。  **说明：** API12前长度为1-512字节。 |
  | ASSET\_TAG\_DATA\_LABEL\_NORMAL\_3 | 类型为uint8[]，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且无完整性保护。  **说明：** API12前长度为1-512字节。 |
  | ASSET\_TAG\_DATA\_LABEL\_NORMAL\_4 | 类型为uint8[]，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且无完整性保护。  **说明：** API12前长度为1-512字节。 |
  | ASSET\_TAG\_DATA\_LABEL\_NORMAL\_LOCAL\_112+ | 类型为uint8[]，长度为1-2048字节。 | 可选 | 关键资产附属的本地信息，内容由业务自定义且无完整性保护，该项信息不会进行同步。 |
  | ASSET\_TAG\_DATA\_LABEL\_NORMAL\_LOCAL\_212+ | 类型为uint8[]，长度为1-2048字节。 | 可选 | 关键资产附属的本地信息，内容由业务自定义且无完整性保护，该项信息不会进行同步。 |
  | ASSET\_TAG\_DATA\_LABEL\_NORMAL\_LOCAL\_312+ | 类型为uint8[]，长度为1-2048字节。 | 可选 | 关键资产附属的本地信息，内容由业务自定义且无完整性保护，该项信息不会进行同步。 |
  | ASSET\_TAG\_DATA\_LABEL\_NORMAL\_LOCAL\_412+ | 类型为uint8[]，长度为1-2048字节。 | 可选 | 关键资产附属的本地信息，内容由业务自定义且无完整性保护，该项信息不会进行同步。 |

## 代码示例

说明

在更新前，需确保已有关键资产，可参考[指南文档](asset-native-add.md)新增关键资产，否则将抛出NOT\_FOUND错误（错误码24000002）。

更新别名是demo\_alias的关键资产，将关键资产明文更新为demo\_pwd\_new，附属信息更新成demo\_label\_new。

在指定群组中更新一条关键资产的示例代码详见[更新群组关键资产](asset-native-group-access-control.md#更新群组关键资产)。

1. 在CMake脚本中链接相关动态库。

   ```
   1. target_link_libraries(entry PUBLIC libasset_ndk.z.so)
   ```
2. 引用头文件。

   ```
   1. #include "napi/native_api.h"
   2. #include <string.h>
   3. #include "asset/asset_api.h"
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/AssetStoreKit/AssetStoreNdk/entry/src/main/cpp/napi_init.cpp#L16-L20)
3. 参考如下示例代码，进行业务功能开发。

   ```
   1. static napi_value UpdateAsset(napi_env env, napi_callback_info info)
   2. {
   3. const char *aliasStr = "demo_alias";
   4. const char *secretStr = "demo_pwd_new";
   5. const char *labelStr = "demo_label_new";

   7. Asset_Blob alias = {(uint32_t)(strlen(aliasStr)), (uint8_t *)aliasStr};
   8. Asset_Blob new_secret = {(uint32_t)(strlen(secretStr)), (uint8_t *)secretStr};
   9. Asset_Blob new_label = {(uint32_t)(strlen(labelStr)), (uint8_t *)labelStr};
   10. Asset_Attr query[] = {{.tag = ASSET_TAG_ALIAS, .value.blob = alias }};
   11. Asset_Attr attributesToUpdate[] = {
   12. {.tag = ASSET_TAG_SECRET, .value.blob = new_secret},
   13. {.tag = ASSET_TAG_DATA_LABEL_NORMAL_1, .value.blob = new_label},
   14. };

   16. int32_t updateResult = OH_Asset_Update(query, sizeof(query) / sizeof(query[0]), attributesToUpdate,
   17. sizeof(attributesToUpdate) / sizeof(attributesToUpdate[0]));
   18. napi_value ret;
   19. napi_create_int32(env, updateResult, &ret);
   20. return ret;
   21. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/AssetStoreKit/AssetStoreNdk/entry/src/main/cpp/napi_init.cpp#L63-L85)
