---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-native-remove
title: 删除关键资产(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Asset Store Kit（关键资产存储服务） > Asset Store Kit开发指导(C/C++) > 删除关键资产(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1fd5ed5174d07149294f01f7e4937d89b1f76f9f4af01492e82d1f123e329124
---

## 接口介绍

开发者可以查阅API文档，获取关键资产删除接口的详细说明：[OH\_Asset\_Remove](../harmonyos-references/capi-asset-api-h.md#oh_asset_remove)。

在删除关键资产时，关键资产属性的内容参数如下表所示：

注意

下表中“ASSET\_TAG\_ALIAS”和名称包含“ASSET\_TAG\_DATA\_LABEL”的关键资产属性，用于存储业务自定义信息，其内容不会被加密，请勿存放敏感个人数据。

| 属性名称（Asset\_Tag） | 属性内容（Asset\_Value） | 是否必选 | 说明 |
| --- | --- | --- | --- |
| ASSET\_TAG\_ALIAS | 类型为uint8[]，长度为1-256字节。 | 可选 | 关键资产别名，每条关键资产的唯一索引。 |
| ASSET\_TAG\_ACCESSIBILITY | 类型为uint32\_t，取值范围详见[Asset\_Accessibility](../harmonyos-references/capi-asset-type-h.md#asset_accessibility)。 | 可选 | 基于锁屏状态的访问控制。 |
| ASSET\_TAG\_REQUIRE\_PASSWORD\_SET | 类型为bool。 | 可选 | 是否仅在设置了锁屏密码的情况下，可访问关键资产。为true时表示删除仅用户设置了锁屏密码才允许访问的关键资产；为false时表示删除无论用户是否设置锁屏密码，均可访问的关键资产。 |
| ASSET\_TAG\_AUTH\_TYPE | 类型为uint32\_t，取值范围详见[Asset\_AuthType](../harmonyos-references/capi-asset-type-h.md#asset_authtype)。 | 可选 | 访问关键资产所需的用户认证类型。 |
| ASSET\_TAG\_SYNC\_TYPE | 类型为uint32\_t，取值范围详见[Asset\_SyncType](../harmonyos-references/capi-asset-type-h.md#asset_synctype)。 | 可选 | 关键资产支持的同步类型。 |
| ASSET\_TAG\_IS\_PERSISTENT | 类型为bool。 | 可选 | 在应用卸载时是否需要保留关键资产。为true时表示删除应用卸载后会被保留的关键资产；为false时表示删除应用卸载后会被删除的关键资产。 |
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
| ASSET\_TAG\_REQUIRE\_ATTR\_ENCRYPTED14+ | 类型为bool。 | 可选 | 是否删除业务自定义附属信息被加密的数据。为true时表示删除业务自定义附属信息加密存储的数据，为false时表示删除业务自定义附属信息不加密存储的数据。默认值为false。 |
| ASSET\_TAG\_GROUP\_ID18+ | 类型为uint8[]，长度为7-127字节。 | 可选 | 待删除的关键资产所属群组，默认删除不属于任何群组的关键资产。 |

## 代码示例

说明

在删除前，需确保已有关键资产，可参考[指南文档](asset-native-add.md)新增关键资产，否则将抛出NOT\_FOUND错误（错误码24000002）。

删除别名是demo\_alias的关键资产。

在指定群组中删除一条关键资产的示例代码详见[删除群组关键资产](asset-native-group-access-control.md#删除群组关键资产)。

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
   1. static napi_value RemoveAsset(napi_env env, napi_callback_info info)
   2. {
   3. const char *aliasStr = "demo_alias";

   5. Asset_Blob alias = {(uint32_t)(strlen(aliasStr)), (uint8_t *)aliasStr};
   6. Asset_Attr attr[] = {
   7. {.tag = ASSET_TAG_ALIAS, .value.blob = alias}, // 此处指定别名删除单条关键资产，也可不指定别名删除多条关键资产。
   8. };

   10. int32_t removeResult = OH_Asset_Remove(attr, sizeof(attr) / sizeof(attr[0]));
   11. napi_value ret;
   12. napi_create_int32(env, removeResult, &ret);
   13. return ret;
   14. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/AssetStoreKit/AssetStoreNdk/entry/src/main/cpp/napi_init.cpp#L46-L61)
