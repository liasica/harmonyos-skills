---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-native-group-access-control
title: 管理群组关键资产(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Asset Store Kit（关键资产存储服务） > Asset Store Kit开发指导(C/C++) > 管理群组关键资产(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6da144201fcff9d7b6afb98508f69dfa626acdbc73c545d5dde20f94bdf803ed
---

以下为管理群组关键资产使用示例，请先查看开发指导：

* [新增关键资产(C/C++)](asset-native-add.md)
* [删除关键资产(C/C++)](asset-native-remove.md)
* [更新关键资产(C/C++)](asset-native-update.md)
* [查询关键资产(C/C++)](asset-native-query.md)

## 前置条件

在应用配置文件app.json5中，配置群组ID，如：demo\_group\_id。群组支持配置多个群组ID。

```json5
{
  "app": {
    // 其他配置项此处省略。
    "assetAccessGroups": [
      "demo_group_id",
      // "another_group_id",
      // ...
    ]
  }
}
```

引用头文件。

```
#include "napi/native_api.h"
#include <string.h>
#include "asset/asset_api.h"
```

## 新增群组关键资产

在群组中新增密码为demo\_pwd、别名为demo\_alias、附属信息为demo\_label的关键资产。

```
static napi_value AddGroupAsset(napi_env env, napi_callback_info info)
{
    const char *secretStr = "demo_pwd";
    const char *aliasStr = "demo_alias";
    const char *labelStr = "demo_label";
    const char *groupIdStr = "demo_group_id";

    Asset_Blob secret = {(uint32_t)(strlen(secretStr)), (uint8_t *)secretStr};
    Asset_Blob alias = {(uint32_t)(strlen(aliasStr)), (uint8_t *)aliasStr};
    Asset_Blob label = {(uint32_t)(strlen(labelStr)), (uint8_t *)labelStr};
    Asset_Blob group_id = { (uint32_t)(strlen(groupIdStr)), (uint8_t *)groupIdStr};
    Asset_Attr attr[] = {
        {.tag = ASSET_TAG_SECRET, .value.blob = secret},
        {.tag = ASSET_TAG_ALIAS, .value.blob = alias},
        {.tag = ASSET_TAG_DATA_LABEL_NORMAL_1, .value.blob = label},
        {.tag = ASSET_TAG_GROUP_ID, .value.blob = group_id},
    };

    int32_t addResult = OH_Asset_Add(attr, sizeof(attr) / sizeof(attr[0]));
    napi_value ret;
    napi_create_int32(env, addResult, &ret);
    return ret;
}
```

## 删除群组关键资产

在群组中删除别名为demo\_alias的关键资产。

```
static napi_value RemoveGroupAsset(napi_env env, napi_callback_info info)
{
    const char *aliasStr = "demo_alias";
    const char *groupIdStr = "demo_group_id";

    Asset_Blob alias = {(uint32_t)(strlen(aliasStr)), (uint8_t *)aliasStr};
    Asset_Blob group_id = {(uint32_t)(strlen(groupIdStr)), (uint8_t *)groupIdStr};
    Asset_Attr attr[] = {
        {.tag = ASSET_TAG_ALIAS, .value.blob = alias}, // 此处指定别名删除单条群组关键资产，也可不指定别名删除多条群组关键资产。
        {.tag = ASSET_TAG_GROUP_ID, .value.blob = group_id},
    };

    int32_t removeResult = OH_Asset_Remove(attr, sizeof(attr) / sizeof(attr[0]));
    napi_value ret;
    napi_create_int32(env, removeResult, &ret);
    return ret;
}
```

## 更新群组关键资产

在群组中更新别名为demo\_alias的关键资产，将关键资产的明文更新为demo\_pwd\_new，附属信息更新为demo\_label\_new。

```
static napi_value UpdateGroupAsset(napi_env env, napi_callback_info info)
{
    const char *aliasStr = "demo_alias";
    const char *secretStr = "demo_pwd_new";
    const char *labelStr = "demo_label_new";
    const char *groupIdStr = "demo_group_id";

    Asset_Blob alias = {(uint32_t)(strlen(aliasStr)), (uint8_t *)aliasStr};
    Asset_Blob new_secret = {(uint32_t)(strlen(secretStr)), (uint8_t *)secretStr};
    Asset_Blob new_label = {(uint32_t)(strlen(labelStr)), (uint8_t *)labelStr};
    Asset_Blob group_id = {(uint32_t)(strlen(groupIdStr)), (uint8_t *)groupIdStr};
    Asset_Attr query[] = {
        {.tag = ASSET_TAG_ALIAS, .value.blob = alias},
        {.tag = ASSET_TAG_GROUP_ID, .value.blob = group_id},
    };
    Asset_Attr attributesToUpdate[] = {
        {.tag = ASSET_TAG_SECRET, .value.blob = new_secret},
        {.tag = ASSET_TAG_DATA_LABEL_NORMAL_1, .value.blob = new_label},
    };

    int32_t updateResult = OH_Asset_Update(query, sizeof(query) / sizeof(query[0]), attributesToUpdate,
                                           sizeof(attributesToUpdate) / sizeof(attributesToUpdate[0]));
    napi_value ret;
    napi_create_int32(env, updateResult, &ret);
    return ret;
}
```

## 查询单条群组关键资产明文

在群组中查询别名为demo\_alias的关键资产明文。

```
static napi_value QueryGroupAssetPlaintext(napi_env env, napi_callback_info info)
{
    const char *aliasStr = "demo_alias";
    const char *groupIdStr = "demo_group_id";
    
    Asset_Blob alias = { (uint32_t)(strlen(aliasStr)), (uint8_t *)aliasStr };
    Asset_Blob group_id = { (uint32_t)(strlen(groupIdStr)), (uint8_t *)groupIdStr };
    Asset_Attr attr[] = {
        {.tag = ASSET_TAG_ALIAS, .value.blob = alias}, // 指定了群组关键资产别名，最多查询到一条满足条件的群组关键资产。
        {.tag = ASSET_TAG_RETURN_TYPE, .value.u32 = ASSET_RETURN_ALL}, // 此处表示需要返回群组关键资产的所有信息，即属性+明文。
        {.tag = ASSET_TAG_GROUP_ID, .value.blob = group_id},
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

## 查询单条群组关键资产属性

查询别名为demo\_alias的关键资产属性。

```
static napi_value QueryGroupAssetAttribute(napi_env env, napi_callback_info info)
{
    const char *aliasStr = "demo_alias";
    const char *groupIdStr = "demo_group_id";
    
    Asset_Blob alias = {(uint32_t)(strlen(aliasStr)), (uint8_t *)aliasStr};
    Asset_Blob group_id = {(uint32_t)(strlen(groupIdStr)), (uint8_t *)groupIdStr};
    Asset_Attr attr[] = {
        {.tag = ASSET_TAG_ALIAS, .value.blob = alias}, // 指定了群组关键资产别名，最多查询到一条满足条件的群组关键资产。
        {.tag = ASSET_TAG_RETURN_TYPE, .value.u32 = ASSET_RETURN_ATTRIBUTES}, // 此处表示仅返回群组关键资产属性，不包含群组关键资产明文。
        {.tag = ASSET_TAG_GROUP_ID, .value.blob = group_id},
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
