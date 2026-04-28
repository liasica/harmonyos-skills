---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-native-add
title: 新增关键资产(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Asset Store Kit（关键资产存储服务） > Asset Store Kit开发指导(C/C++) > 新增关键资产(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9471f283501c2798fadc34acfae2ced1df33e1d0fef56827ba2d6fc01ced9eb3
---

## 接口介绍

开发者可以查阅API文档，获取关键资产新增接口的详细说明：[OH\_Asset\_Add](../harmonyos-references/capi-asset-api-h.md#oh_asset_add)。

在新增关键资产时，关键资产属性的内容参数如下表所示：

注意

下表中“ASSET\_TAG\_ALIAS”和名称包含“ASSET\_TAG\_DATA\_LABEL”的关键资产属性，用于存储业务自定义信息，其内容不会被加密，请勿存放敏感个人数据。

| 属性名称（Asset\_Tag） | 属性内容（Asset\_Value） | 是否必选 | 说明 |
| --- | --- | --- | --- |
| ASSET\_TAG\_SECRET | 类型为uint8[]，长度为1-1024字节。 | 必选 | 关键资产明文。 |
| ASSET\_TAG\_ALIAS | 类型为uint8[]，长度为1-256字节。 | 必选 | 关键资产别名，每条关键资产的唯一索引。 |
| ASSET\_TAG\_ACCESSIBILITY | 类型为uint32\_t，取值范围详见[Asset\_Accessibility](../harmonyos-references/capi-asset-type-h.md#asset_accessibility)。 | 可选 | 基于锁屏状态的访问控制，默认值为ASSET\_ACCESSIBILITY\_DEVICE\_FIRST\_UNLOCKED，即首次解锁后可访问。 |
| ASSET\_TAG\_REQUIRE\_PASSWORD\_SET | 类型为bool。 | 可选 | 是否仅在设置了锁屏密码的情况下，可访问关键资产。为true时，表示仅在用户设置了锁屏密码的情况下，关键资产才允许被访问；为false时，表示无论用户是否设置锁屏密码，关键资产均允许被访问。默认值为false。 |
| ASSET\_TAG\_AUTH\_TYPE | 类型为uint32\_t，取值范围详见[Asset\_AuthType](../harmonyos-references/capi-asset-type-h.md#asset_authtype)。 | 可选 | 访问关键资产所需的用户认证类型，默认值为ASSET\_AUTH\_TYPE\_NONE，即访问关键资产前无需用户认证。 |
| ASSET\_TAG\_SYNC\_TYPE | 类型为uint32\_t，取值范围详见[Asset\_SyncType](../harmonyos-references/capi-asset-type-h.md#asset_synctype)。 | 可选 | 关键资产支持的同步类型，默认值为ASSET\_SYNC\_TYPE\_NEVER，即不允许同步该关键资产。 |
| ASSET\_TAG\_IS\_PERSISTENT | 类型为bool。 | 可选 | 在应用卸载时是否需要保留关键资产。为true时表示应用卸载后，应用存储的关键资产将被保留；为false时表示应用卸载后，应用存储的关键资产将被删除。默认值为false。  **注意：** 设置此属性时，需[申请权限](declare-permissions.md)ohos.permission.STORE\_PERSISTENT\_DATA。 |
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
| ASSET\_TAG\_CONFLICT\_RESOLUTION | 类型为uint32\_t，取值范围详见[Asset\_ConflictResolution](../harmonyos-references/capi-asset-type-h.md#asset_conflictresolution)。 | 可选 | 新增关键资产时的冲突（如：别名相同）处理策略，默认值为ASSET\_CONFLICT\_THROW\_ERROR，即抛出异常，由业务进行后续处理。 |
| ASSET\_TAG\_REQUIRE\_ATTR\_ENCRYPTED14+ | 类型为bool。 | 可选 | 是否加密业务自定义附属信息。为true时表示业务自定义附属信息加密存储，为false时表示业务自定义附属信息不加密存储。默认值为false。 |
| ASSET\_TAG\_GROUP\_ID18+ | 类型为uint8[]，长度为7-127字节。 | 可选 | 待新增的关键资产所属群组，默认新增不属于任何群组的关键资产。 |
| ASSET\_TAG\_WRAP\_TYPE18+ | 类型为uint32\_t，取值范围详见[Asset\_WrapType](../harmonyos-references/capi-asset-type-h.md#asset_wraptype)。 | 可选 | 关键资产支持的加密导入导出类型，默认值为ASSET\_WRAP\_TYPE\_NEVER，即不允许加密导入导出关键资产。 |

## 约束和限制

* 基于别名的访问

  关键资产以密文的形式存储在ASSET数据库中，以业务身份和别名作为索引。业务需保证每条关键资产的别名唯一。
* 业务自定义数据存储

  + ASSET为业务预留了12个关键资产自定义属性，名称以"ASSET\_TAG\_DATA\_LABEL"开头。对于超过12个自定义属性的情况，业务可以将多段数据按照一定的格式（如JSON）拼接到同一个ASSET属性中。
  + ASSET对部分属性会进行完整性保护，这部分属性名称以"ASSET\_TAG\_DATA\_LABEL\_CRITICAL"开头，且写入后不支持更新。

## 代码示例

新增密码为demo\_pwd、别名为demo\_alias、附属信息为demo\_label的关键资产。用户首次解锁设备后，该关键资产可被访问。

在指定群组中新增一条关键资产的示例代码详见[新增群组关键资产](asset-native-group-access-control.md#新增群组关键资产)。

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
   1. static napi_value AddAsset(napi_env env, napi_callback_info info)
   2. {
   3. const char *secretStr = "demo_pwd";
   4. const char *aliasStr = "demo_alias";
   5. const char *labelStr = "demo_label";

   7. Asset_Blob secret = {(uint32_t)(strlen(secretStr)), (uint8_t *)secretStr};
   8. Asset_Blob alias = {(uint32_t)(strlen(aliasStr)), (uint8_t *)aliasStr};
   9. Asset_Blob label = {(uint32_t)(strlen(labelStr)), (uint8_t *)labelStr};
   10. Asset_Attr attr[] = {
   11. {.tag = ASSET_TAG_ACCESSIBILITY, .value.u32 = ASSET_ACCESSIBILITY_DEVICE_FIRST_UNLOCKED},
   12. {.tag = ASSET_TAG_SECRET, .value.blob = secret},
   13. {.tag = ASSET_TAG_ALIAS, .value.blob = alias},
   14. {.tag = ASSET_TAG_DATA_LABEL_NORMAL_1, .value.blob = label},
   15. };

   17. int32_t addResult = OH_Asset_Add(attr, sizeof(attr) / sizeof(attr[0]));
   18. napi_value ret;
   19. napi_create_int32(env, addResult, &ret);
   20. return ret;
   21. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/AssetStoreKit/AssetStoreNdk/entry/src/main/cpp/napi_init.cpp#L22-L44)
