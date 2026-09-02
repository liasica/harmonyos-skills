---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-native-query
title: 查询关键资产(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Asset Store Kit（关键资产存储服务） > Asset Store Kit开发指导(C/C++) > 查询关键资产(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:28+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2b5e3af01a8aa8f34d9e9c81f308c2cdb94cf4fe680ba4b904338c68674297b3
---

## 接口介绍

开发者可以查阅API文档，获取关键资产查询接口的详细说明：[OH\_Asset\_Query](../harmonyos-references/capi-asset-api-h.md#oh_asset_query)。

在查询关键资产时，关键资产属性的内容参数如下表所示：

**注意** 

下表中“ASSET\_TAG\_ALIAS”和名称包含“ASSET\_TAG\_DATA\_LABEL”的关键资产属性，用于存储业务自定义信息，其内容不会被加密，请勿存放敏感个人数据。

查询关键资产明文ASSET\_TAG\_SECRET需要解密，目前不支持批量查询，查询时间较长，需要将Asset\_ReturnType设置为ASSET\_RETURN\_ALL；只查询其他关键资产属性不需解密，支持批量查询，查询时间较短，需要将Asset\_ReturnType设置为ASSET\_RETURN\_ATTRIBUTES。

| 属性名称（Asset\_Tag） | 属性内容（Asset\_Value） | 是否必选 | 说明 |
| --- | --- | --- | --- |
| ASSET\_TAG\_ALIAS | 类型为uint8[]，长度为1-256字节。 | 可选 | 关键资产别名，每条关键资产的唯一索引。 |
| ASSET\_TAG\_ACCESSIBILITY | 类型为uint32\_t，取值范围详见[Asset\_Accessibility](../harmonyos-references/capi-asset-type-h.md#asset_accessibility)。 | 可选 | 基于锁屏状态的访问控制。 |
| ASSET\_TAG\_REQUIRE\_PASSWORD\_SET | 类型为bool。 | 可选 | 是否仅在设置了锁屏密码的情况下，可访问关键资产。为true时表示查询仅用户设置了锁屏密码才允许访问的关键资产；为false时表示查询无论用户是否设置锁屏密码，均可访问的关键资产。 |
| ASSET\_TAG\_AUTH\_TYPE | 类型为uint32\_t，取值范围详见[Asset\_AuthType](../harmonyos-references/capi-asset-type-h.md#asset_authtype)。 | 可选 | 访问关键资产所需的用户认证类型。 |
| ASSET\_TAG\_SYNC\_TYPE | 类型为uint32\_t，取值范围详见[Asset\_SyncType](../harmonyos-references/capi-asset-type-h.md#asset_synctype)。 | 可选 | 关键资产支持的同步类型。 |
| ASSET\_TAG\_IS\_PERSISTENT | 类型为bool。 | 可选 | 在应用卸载时是否需要保留关键资产。为true时表示查询应用卸载后会被保留的关键资产；为false时表示查询应用卸载后会被删除的关键资产。 |
| ASSET\_TAG\_DATA\_LABEL\_CRITICAL\_1 | 类型为uint8[]，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且有完整性保护。  **说明：** 在API version 12及之前版本，长度为1-512字节。 |
| ASSET\_TAG\_DATA\_LABEL\_CRITICAL\_2 | 类型为uint8[]，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且有完整性保护。  **说明：** 在API version 12及之前版本，长度为1-512字节。 |
| ASSET\_TAG\_DATA\_LABEL\_CRITICAL\_3 | 类型为uint8[]，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且有完整性保护。  **说明：** 在API version 12及之前版本，长度为1-512字节。 |
| ASSET\_TAG\_DATA\_LABEL\_CRITICAL\_4 | 类型为uint8[]，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且有完整性保护。  **说明：** 在API version 12及之前版本，长度为1-512字节。 |
| ASSET\_TAG\_DATA\_LABEL\_NORMAL\_1 | 类型为uint8[]，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且无完整性保护。  **说明：** 在API version 12及之前版本，长度为1-512字节。 |
| ASSET\_TAG\_DATA\_LABEL\_NORMAL\_2 | 类型为uint8[]，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且无完整性保护。  **说明：** 在API version 12及之前版本，长度为1-512字节。 |
| ASSET\_TAG\_DATA\_LABEL\_NORMAL\_3 | 类型为uint8[]，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且无完整性保护。  **说明：** 在API version 12及之前版本，长度为1-512字节。 |
| ASSET\_TAG\_DATA\_LABEL\_NORMAL\_4 | 类型为uint8[]，长度为1-2048字节。 | 可选 | 关键资产附属信息，内容由业务自定义且无完整性保护。  **说明：** 在API version 12及之前版本，长度为1-512字节。 |
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

**说明** 

在查询前，需确保已有关键资产，可参考[指南文档](asset-native-add.md)新增关键资产，否则将抛出NOT\_FOUND错误（错误码24000002）。

### 查询单条关键资产明文

查询别名是demo\_alias的关键资产明文。

在指定群组中查询一条关键资产明文的示例代码详见[查询单条群组关键资产明文](asset-native-group-access-control.md#查询单条群组关键资产明文)。

1. 在CMake脚本中链接相关动态库。

   ```txt
   target_link_libraries(entry PUBLIC libasset_ndk.z.so)
   ```
2. 引用头文件。

   ```
   #include "napi/native_api.h"
   #include <string.h>
   #include "asset/asset_api.h"
   ```
3. 参考如下示例代码，进行业务功能开发。

   ```
   static napi_value QueryAssetPlaintext(napi_env env, napi_callback_info info)
   {
       const char *aliasStr = "demo_alias";
       
       Asset_Blob alias = {(uint32_t)(strlen(aliasStr)), (uint8_t *)aliasStr};
       Asset_Attr attr[] = {
           {.tag = ASSET_TAG_ALIAS, .value.blob = alias}, // 指定了关键资产别名，最多查询到一条满足条件的关键资产。
           {.tag = ASSET_TAG_RETURN_TYPE, .value.u32 = ASSET_RETURN_ALL}, // 此处表示需要返回关键资产的所有信息，即属性+明文。返回明文需要解密，查询时间较长。
       };

       Asset_ResultSet resultSet = {0};
       int32_t queryResult = OH_Asset_Query(attr, sizeof(attr) / sizeof(attr[0]), &resultSet);
       if (queryResult == ASSET_SUCCESS) {
           // 解析resultSet。
           for (uint32_t i = 0; i < resultSet.count; i++) {
               // 解析secret属性：其中data数据对应是secret->blob.data，长度对应是secret->blob.size。
               Asset_Attr *secret = OH_Asset_ParseAttr(resultSet.results + i, ASSET_TAG_SECRET);
           }
       }
       OH_Asset_FreeResultSet(&resultSet);
    
       napi_value ret;
       napi_create_int32(env, queryResult, &ret);
       return ret;
   }
   ```

### 查询单条关键资产属性

查询别名是demo\_alias的关键资产属性。

在指定群组中查询一条关键资产属性的示例代码详见[查询单条群组关键资产属性](asset-native-group-access-control.md#查询单条群组关键资产属性)。

1. 在CMake脚本中链接相关动态库。

   ```txt
   target_link_libraries(entry PUBLIC libasset_ndk.z.so)
   ```
2. 引用头文件。

   ```
   #include "napi/native_api.h"
   #include <string.h>
   #include "asset/asset_api.h"
   ```
3. 参考如下示例代码，进行业务功能开发。

   ```
   static napi_value QueryAssetAttribute(napi_env env, napi_callback_info info)
   {
       const char *aliasStr = "demo_alias";
       
       Asset_Blob alias = { (uint32_t)(strlen(aliasStr)), (uint8_t *)aliasStr };
       Asset_Attr attr[] = {
           {.tag = ASSET_TAG_ALIAS, .value.blob = alias}, // 指定了关键资产别名，最多查询到一条满足条件的关键资产。
           {.tag = ASSET_TAG_RETURN_TYPE, .value.u32 = ASSET_RETURN_ATTRIBUTES}, // 此处表示仅返回关键资产属性。返回属性不需解密，查询时间较短。
       };

       Asset_ResultSet resultSet = {0};
       int32_t queryResult = OH_Asset_Query(attr, sizeof(attr) / sizeof(attr[0]), &resultSet);
       if (queryResult == ASSET_SUCCESS) {
           // 解析结果。
           for (uint32_t i = 0; i < resultSet.count; i++) {
               // 解析数据标签：其中数据是label->blob.data，长度对应是label->blob.size。
               Asset_Attr *label = OH_Asset_ParseAttr(resultSet.results + i, ASSET_TAG_DATA_LABEL_NORMAL_1);
           }
       }
       OH_Asset_FreeResultSet(&resultSet);
    
       napi_value ret;
       napi_create_int32(env, queryResult, &ret);
       return ret;
   }
   ```

### 批量查询关键资产属性

批量查询标签为demo\_label的关键资产属性，共返回10条符合条件的查询结果，结果按ASSET\_TAG\_DATA\_LABEL\_NORMAL\_1属性内容排序。

1. 在CMake脚本中链接相关动态库。

   ```txt
   target_link_libraries(entry PUBLIC libasset_ndk.z.so)
   ```
2. 引用头文件。

   ```
   #include "napi/native_api.h"
   #include <string.h>
   #include "asset/asset_api.h"
   ```
3. 参考如下示例代码，进行业务功能开发。

   ```
   static napi_value QueryBatchAssetAttributes(napi_env env, napi_callback_info info)
   {
       const char *labelStr = "demo_label";
       
       Asset_Blob label = {(uint32_t)(strlen(labelStr)), (uint8_t *)labelStr};
       Asset_Attr attr[] = {
           {.tag = ASSET_TAG_RETURN_TYPE, .value.u32 = ASSET_RETURN_ATTRIBUTES},
           {.tag = ASSET_TAG_DATA_LABEL_NORMAL_1, .value.blob = label},
           {.tag = ASSET_TAG_RETURN_LIMIT, .value.u32 = 10},
           {.tag = ASSET_TAG_RETURN_ORDERED_BY, .value.u32 = ASSET_TAG_DATA_LABEL_NORMAL_1},
       };

       Asset_ResultSet resultSet = { 0 };
       int32_t queryResult = OH_Asset_Query(attr, sizeof(attr) / sizeof(attr[0]), &resultSet);
       if (queryResult == ASSET_SUCCESS) {
           // 解析结果。
           for (uint32_t i = 0; i < resultSet.count; i++) {
               // 解析数据别名：其中别名是label->blob.data，长度对应是label->blob.size。
               Asset_Attr *alias = OH_Asset_ParseAttr(resultSet.results + i, ASSET_TAG_ALIAS);
           }
       }
       OH_Asset_FreeResultSet(&resultSet);
    
       napi_value ret;
       napi_create_int32(env, queryResult, &ret);
       return ret;
   }
   ```
