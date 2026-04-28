---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-native-query
title: 查询关键资产(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Asset Store Kit（关键资产存储服务） > Asset Store Kit开发指导(C/C++) > 查询关键资产(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:50be569a0fe6189df65d771c686b50854defa31d1fc5c17ac18d274333633c76
---

## 接口介绍

开发者可以查阅API文档，获取关键资产查询接口的详细说明：[OH\_Asset\_Query](../harmonyos-references/capi-asset-api-h.md#oh_asset_query)。

在查询关键资产时，关键资产属性的内容参数如下表所示：

注意

下表中“ASSET\_TAG\_ALIAS”和名称包含“ASSET\_TAG\_DATA\_LABEL”的关键资产属性，用于存储业务自定义信息，其内容不会被加密，请勿存放敏感个人数据。

查询关键资产明文ASSET\_TAG\_SECRET需要解密，查询时间较长，需要将Asset\_ReturnType设置为ASSET\_RETURN\_ALL；只查询其他关键资产属性不需解密，查询时间较短，需要将Asset\_ReturnType设置为ASSET\_RETURN\_ATTRIBUTES。

| 属性名称（Asset\_Tag） | 属性内容（Asset\_Value） | 是否必选 | 说明 |
| --- | --- | --- | --- |
| ASSET\_TAG\_ALIAS | 类型为uint8[]，长度为1-256字节。 | 可选 | 关键资产别名，每条关键资产的唯一索引。 |
| ASSET\_TAG\_ACCESSIBILITY | 类型为uint32\_t，取值范围详见[Asset\_Accessibility](../harmonyos-references/capi-asset-type-h.md#asset_accessibility)。 | 可选 | 基于锁屏状态的访问控制。 |
| ASSET\_TAG\_REQUIRE\_PASSWORD\_SET | 类型为bool。 | 可选 | 是否仅在设置了锁屏密码的情况下，可访问关键资产。为true时表示查询仅用户设置了锁屏密码才允许访问的关键资产；为false时表示查询无论用户是否设置锁屏密码，均可访问的关键资产。 |
| ASSET\_TAG\_AUTH\_TYPE | 类型为uint32\_t，取值范围详见[Asset\_AuthType](../harmonyos-references/capi-asset-type-h.md#asset_authtype)。 | 可选 | 访问关键资产所需的用户认证类型。 |
| ASSET\_TAG\_SYNC\_TYPE | 类型为uint32\_t，取值范围详见[Asset\_SyncType](../harmonyos-references/capi-asset-type-h.md#asset_synctype)。 | 可选 | 关键资产支持的同步类型。 |
| ASSET\_TAG\_IS\_PERSISTENT | 类型为bool。 | 可选 | 在应用卸载时是否需要保留关键资产。为true时表示查询应用卸载后会被保留的关键资产；为false时表示查询应用卸载后会被删除的关键资产。 |
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
| ASSET\_TAG\_RETURN\_TYPE | 类型为uint32\_t，取值范围详见[Asset\_ReturnType](../harmonyos-references/capi-asset-type-h.md#asset_returntype)。 | 可选 | 关键资产查询返回的结果类型。 |
| ASSET\_TAG\_RETURN\_LIMIT | 类型为uint32\_t。 | 可选 | 关键资产查询返回的结果数量。 |
| ASSET\_TAG\_RETURN\_OFFSET | 类型为uint32\_t，取值范围：1-65536。 | 可选 | 关键资产查询返回的结果偏移量。  **说明：** 用于分批查询场景，指定从第几个开始返回。 |
| ASSET\_TAG\_RETURN\_ORDERED\_BY | 类型为uint32\_t，取值范围：ASSET\_TAG\_DATA\_LABEL\_xxx。 | 可选 | 关键资产查询返回的结果排序依据，仅支持按照附属信息排序。  **说明：** 默认按照关键资产新增的顺序返回。 |
| ASSET\_TAG\_REQUIRE\_ATTR\_ENCRYPTED14+ | 类型为bool。 | 可选 | 是否查询业务自定义附属信息被加密的数据。为true时表示查询业务自定义附属信息加密存储的数据，为false时表示查询业务自定义附属信息不加密存储的数据。默认值为false。 |
| ASSET\_TAG\_GROUP\_ID18+ | 类型为uint8[]，长度为7-127字节。 | 可选 | 待查询的关键资产所属群组，默认查询不属于任何群组的关键资产。 |

## 约束和限制

批量查询出的关键资产需要通过IPC通道传输给业务，受IPC缓冲区大小限制，建议对查询超过40条关键资产时，进行分批查询，且每次查询数量不超过40条。

## 代码示例

说明

在查询前，需确保已有关键资产，可参考[指南文档](asset-native-add.md)新增关键资产，否则将抛出NOT\_FOUND错误（错误码24000002）。

### 查询单条关键资产明文

查询别名是demo\_alias的关键资产明文。

在指定群组中查询一条关键资产明文的示例代码详见[查询单条群组关键资产明文](asset-native-group-access-control.md#查询单条群组关键资产明文)。

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
   1. static napi_value QueryAssetPlaintext(napi_env env, napi_callback_info info)
   2. {
   3. const char *aliasStr = "demo_alias";

   5. Asset_Blob alias = {(uint32_t)(strlen(aliasStr)), (uint8_t *)aliasStr};
   6. Asset_Attr attr[] = {
   7. {.tag = ASSET_TAG_ALIAS, .value.blob = alias}, // 指定了关键资产别名，最多查询到一条满足条件的关键资产。
   8. {.tag = ASSET_TAG_RETURN_TYPE, .value.u32 = ASSET_RETURN_ALL}, // 此处表示需要返回关键资产的所有信息，即属性+明文。返回明文需要解密，查询时间较长。
   9. };

   11. Asset_ResultSet resultSet = {0};
   12. int32_t queryResult = OH_Asset_Query(attr, sizeof(attr) / sizeof(attr[0]), &resultSet);
   13. if (queryResult == ASSET_SUCCESS) {
   14. // 解析resultSet。
   15. for (uint32_t i = 0; i < resultSet.count; i++) {
   16. // 解析secret属性：其中data数据对应是secret->blob.data，长度对应是secret->blob.size。
   17. Asset_Attr *secret = OH_Asset_ParseAttr(resultSet.results + i, ASSET_TAG_SECRET);
   18. }
   19. }
   20. OH_Asset_FreeResultSet(&resultSet);

   22. napi_value ret;
   23. napi_create_int32(env, queryResult, &ret);
   24. return ret;
   25. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/AssetStoreKit/AssetStoreNdk/entry/src/main/cpp/napi_init.cpp#L87-L113)

### 查询单条关键资产属性

查询别名是demo\_alias的关键资产属性。

在指定群组中查询一条关键资产属性的示例代码详见[查询单条群组关键资产属性](asset-native-group-access-control.md#查询单条群组关键资产属性)。

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
   1. static napi_value QueryAssetAttribute(napi_env env, napi_callback_info info)
   2. {
   3. const char *aliasStr = "demo_alias";

   5. Asset_Blob alias = { (uint32_t)(strlen(aliasStr)), (uint8_t *)aliasStr };
   6. Asset_Attr attr[] = {
   7. {.tag = ASSET_TAG_ALIAS, .value.blob = alias}, // 指定了关键资产别名，最多查询到一条满足条件的关键资产。
   8. {.tag = ASSET_TAG_RETURN_TYPE, .value.u32 = ASSET_RETURN_ATTRIBUTES}, // 此处表示仅返回关键资产属性。返回属性不需解密，查询时间较短。
   9. };

   11. Asset_ResultSet resultSet = {0};
   12. int32_t queryResult = OH_Asset_Query(attr, sizeof(attr) / sizeof(attr[0]), &resultSet);
   13. if (queryResult == ASSET_SUCCESS) {
   14. // 解析结果。
   15. for (uint32_t i = 0; i < resultSet.count; i++) {
   16. // 解析数据标签：其中数据是label->blob.data，长度对应是label->blob.size。
   17. Asset_Attr *label = OH_Asset_ParseAttr(resultSet.results + i, ASSET_TAG_DATA_LABEL_NORMAL_1);
   18. }
   19. }
   20. OH_Asset_FreeResultSet(&resultSet);

   22. napi_value ret;
   23. napi_create_int32(env, queryResult, &ret);
   24. return ret;
   25. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/AssetStoreKit/AssetStoreNdk/entry/src/main/cpp/napi_init.cpp#L115-L141)

### 批量查询关键资产属性

批量查询标签为demo\_label的关键资产属性，共返回10条符合条件的查询结果，结果按ASSET\_TAG\_DATA\_LABEL\_NORMAL\_1属性内容排序。

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
   1. static napi_value QueryBatchAssetAttributes(napi_env env, napi_callback_info info)
   2. {
   3. const char *labelStr = "demo_label";

   5. Asset_Blob label = {(uint32_t)(strlen(labelStr)), (uint8_t *)labelStr};
   6. Asset_Attr attr[] = {
   7. {.tag = ASSET_TAG_RETURN_TYPE, .value.u32 = ASSET_RETURN_ATTRIBUTES},
   8. {.tag = ASSET_TAG_DATA_LABEL_NORMAL_1, .value.blob = label},
   9. {.tag = ASSET_TAG_RETURN_LIMIT, .value.u32 = 10},
   10. {.tag = ASSET_TAG_RETURN_ORDERED_BY, .value.u32 = ASSET_TAG_DATA_LABEL_NORMAL_1},
   11. };

   13. Asset_ResultSet resultSet = { 0 };
   14. int32_t queryResult = OH_Asset_Query(attr, sizeof(attr) / sizeof(attr[0]), &resultSet);
   15. if (queryResult == ASSET_SUCCESS) {
   16. // 解析结果。
   17. for (uint32_t i = 0; i < resultSet.count; i++) {
   18. // 解析数据别名：其中别名是label->blob.data，长度对应是label->blob.size。
   19. Asset_Attr *alias = OH_Asset_ParseAttr(resultSet.results + i, ASSET_TAG_ALIAS);
   20. }
   21. }
   22. OH_Asset_FreeResultSet(&resultSet);

   24. napi_value ret;
   25. napi_create_int32(env, queryResult, &ret);
   26. return ret;
   27. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/AssetStoreKit/AssetStoreNdk/entry/src/main/cpp/napi_init.cpp#L143-L171)
