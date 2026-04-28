---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-native-group-access-control
title: 管理群组关键资产(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Asset Store Kit（关键资产存储服务） > Asset Store Kit开发指导(C/C++) > 管理群组关键资产(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bc1c07265971efc6522bec6c10f1c22b95a70bd06baf20fcd3612b572d74c0f6
---

以下为管理群组关键资产使用示例，请先查看开发指导：

* [新增关键资产(C/C++)](asset-native-add.md)
* [删除关键资产(C/C++)](asset-native-remove.md)
* [更新关键资产(C/C++)](asset-native-update.md)
* [查询关键资产(C/C++)](asset-native-query.md)

## 前置条件

在应用配置文件app.json5中，配置群组ID，如：demo\_group\_id。群组支持配置多个群组ID。

```
1. {
2. "app": {
3. // 其他配置项此处省略。
4. "assetAccessGroups": [
5. "demo_group_id",
6. // "another_group_id",
7. // ...
8. ]
9. }
10. }
```

引用头文件。

```
1. #include "napi/native_api.h"
2. #include <string.h>
3. #include "asset/asset_api.h"
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/AssetStoreKit/AssetStoreNdk/entry/src/main/cpp/napi_init.cpp#L16-L20)

## 新增群组关键资产

在群组中新增密码为demo\_pwd、别名为demo\_alias、附属信息为demo\_label的关键资产。

```
1. static napi_value AddGroupAsset(napi_env env, napi_callback_info info)
2. {
3. const char *secretStr = "demo_pwd";
4. const char *aliasStr = "demo_alias";
5. const char *labelStr = "demo_label";
6. const char *groupIdStr = "demo_group_id";

8. Asset_Blob secret = {(uint32_t)(strlen(secretStr)), (uint8_t *)secretStr};
9. Asset_Blob alias = {(uint32_t)(strlen(aliasStr)), (uint8_t *)aliasStr};
10. Asset_Blob label = {(uint32_t)(strlen(labelStr)), (uint8_t *)labelStr};
11. Asset_Blob group_id = { (uint32_t)(strlen(groupIdStr)), (uint8_t *)groupIdStr};
12. Asset_Attr attr[] = {
13. {.tag = ASSET_TAG_SECRET, .value.blob = secret},
14. {.tag = ASSET_TAG_ALIAS, .value.blob = alias},
15. {.tag = ASSET_TAG_DATA_LABEL_NORMAL_1, .value.blob = label},
16. {.tag = ASSET_TAG_GROUP_ID, .value.blob = group_id},
17. };

19. int32_t addResult = OH_Asset_Add(attr, sizeof(attr) / sizeof(attr[0]));
20. napi_value ret;
21. napi_create_int32(env, addResult, &ret);
22. return ret;
23. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/AssetStoreKit/AssetStoreNdk/entry/src/main/cpp/napi_init.cpp#L173-L197)

## 删除群组关键资产

在群组中删除别名为demo\_alias的关键资产。

```
1. static napi_value RemoveGroupAsset(napi_env env, napi_callback_info info)
2. {
3. const char *aliasStr = "demo_alias";
4. const char *groupIdStr = "demo_group_id";

6. Asset_Blob alias = {(uint32_t)(strlen(aliasStr)), (uint8_t *)aliasStr};
7. Asset_Blob group_id = {(uint32_t)(strlen(groupIdStr)), (uint8_t *)groupIdStr};
8. Asset_Attr attr[] = {
9. {.tag = ASSET_TAG_ALIAS, .value.blob = alias}, // 此处指定别名删除单条群组关键资产，也可不指定别名删除多条群组关键资产。
10. {.tag = ASSET_TAG_GROUP_ID, .value.blob = group_id},
11. };

13. int32_t removeResult = OH_Asset_Remove(attr, sizeof(attr) / sizeof(attr[0]));
14. napi_value ret;
15. napi_create_int32(env, removeResult, &ret);
16. return ret;
17. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/AssetStoreKit/AssetStoreNdk/entry/src/main/cpp/napi_init.cpp#L199-L217)

## 更新群组关键资产

在群组中更新别名为demo\_alias的关键资产，将关键资产的明文更新为demo\_pwd\_new，附属信息更新为demo\_label\_new。

```
1. static napi_value UpdateGroupAsset(napi_env env, napi_callback_info info)
2. {
3. const char *aliasStr = "demo_alias";
4. const char *secretStr = "demo_pwd_new";
5. const char *labelStr = "demo_label_new";
6. const char *groupIdStr = "demo_group_id";

8. Asset_Blob alias = {(uint32_t)(strlen(aliasStr)), (uint8_t *)aliasStr};
9. Asset_Blob new_secret = {(uint32_t)(strlen(secretStr)), (uint8_t *)secretStr};
10. Asset_Blob new_label = {(uint32_t)(strlen(labelStr)), (uint8_t *)labelStr};
11. Asset_Blob group_id = {(uint32_t)(strlen(groupIdStr)), (uint8_t *)groupIdStr};
12. Asset_Attr query[] = {
13. {.tag = ASSET_TAG_ALIAS, .value.blob = alias},
14. {.tag = ASSET_TAG_GROUP_ID, .value.blob = group_id},
15. };
16. Asset_Attr attributesToUpdate[] = {
17. {.tag = ASSET_TAG_SECRET, .value.blob = new_secret},
18. {.tag = ASSET_TAG_DATA_LABEL_NORMAL_1, .value.blob = new_label},
19. };

21. int32_t updateResult = OH_Asset_Update(query, sizeof(query) / sizeof(query[0]), attributesToUpdate,
22. sizeof(attributesToUpdate) / sizeof(attributesToUpdate[0]));
23. napi_value ret;
24. napi_create_int32(env, updateResult, &ret);
25. return ret;
26. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/AssetStoreKit/AssetStoreNdk/entry/src/main/cpp/napi_init.cpp#L219-L246)

## 查询单条群组关键资产明文

在群组中查询别名为demo\_alias的关键资产明文。

```
1. static napi_value QueryGroupAssetPlaintext(napi_env env, napi_callback_info info)
2. {
3. const char *aliasStr = "demo_alias";
4. const char *groupIdStr = "demo_group_id";

6. Asset_Blob alias = { (uint32_t)(strlen(aliasStr)), (uint8_t *)aliasStr };
7. Asset_Blob group_id = { (uint32_t)(strlen(groupIdStr)), (uint8_t *)groupIdStr };
8. Asset_Attr attr[] = {
9. {.tag = ASSET_TAG_ALIAS, .value.blob = alias}, // 指定了群组关键资产别名，最多查询到一条满足条件的群组关键资产。
10. {.tag = ASSET_TAG_RETURN_TYPE, .value.u32 = ASSET_RETURN_ALL}, // 此处表示需要返回群组关键资产的所有信息，即属性+明文。
11. {.tag = ASSET_TAG_GROUP_ID, .value.blob = group_id},
12. };

14. Asset_ResultSet resultSet = {0};
15. int32_t queryResult = OH_Asset_Query(attr, sizeof(attr) / sizeof(attr[0]), &resultSet);
16. if (queryResult == ASSET_SUCCESS) {
17. // 解析resultSet。
18. for (uint32_t i = 0; i < resultSet.count; i++) {
19. // 解析secret属性：其中data数据对应是secret->blob.data，长度对应是secret->blob.size。
20. Asset_Attr *secret = OH_Asset_ParseAttr(resultSet.results + i, ASSET_TAG_SECRET);
21. }
22. }
23. OH_Asset_FreeResultSet(&resultSet);

25. napi_value ret;
26. napi_create_int32(env, queryResult, &ret);
27. return ret;
28. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/AssetStoreKit/AssetStoreNdk/entry/src/main/cpp/napi_init.cpp#L248-L277)

## 查询单条群组关键资产属性

查询别名为demo\_alias的关键资产属性。

```
1. static napi_value QueryGroupAssetAttribute(napi_env env, napi_callback_info info)
2. {
3. const char *aliasStr = "demo_alias";
4. const char *groupIdStr = "demo_group_id";

6. Asset_Blob alias = {(uint32_t)(strlen(aliasStr)), (uint8_t *)aliasStr};
7. Asset_Blob group_id = {(uint32_t)(strlen(groupIdStr)), (uint8_t *)groupIdStr};
8. Asset_Attr attr[] = {
9. {.tag = ASSET_TAG_ALIAS, .value.blob = alias}, // 指定了群组关键资产别名，最多查询到一条满足条件的群组关键资产。
10. {.tag = ASSET_TAG_RETURN_TYPE, .value.u32 = ASSET_RETURN_ATTRIBUTES}, // 此处表示仅返回群组关键资产属性，不包含群组关键资产明文。
11. {.tag = ASSET_TAG_GROUP_ID, .value.blob = group_id},
12. };

14. Asset_ResultSet resultSet = {0};
15. int32_t queryResult = OH_Asset_Query(attr, sizeof(attr) / sizeof(attr[0]), &resultSet);
16. if (queryResult == ASSET_SUCCESS) {
17. // 解析结果。
18. for (uint32_t i = 0; i < resultSet.count; i++) {
19. // 解析数据标签：其中数据是label->blob.data，长度对应是label->blob.size。
20. Asset_Attr *label = OH_Asset_ParseAttr(resultSet.results + i, ASSET_TAG_DATA_LABEL_NORMAL_1);
21. }
22. }
23. OH_Asset_FreeResultSet(&resultSet);

25. napi_value ret;
26. napi_create_int32(env, queryResult, &ret);
27. return ret;
28. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/AssetStoreKit/AssetStoreNdk/entry/src/main/cpp/napi_init.cpp#L279-L308)
