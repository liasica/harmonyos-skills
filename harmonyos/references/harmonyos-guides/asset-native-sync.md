---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-native-sync
title: 同步（备份恢复）关键资产(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Asset Store Kit（关键资产存储服务） > Asset Store Kit开发指导(C/C++) > 同步（备份恢复）关键资产(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:946362393df1820444f1aa95856020df0e100b23bfbbc6a717a2d690f2536fe3
---

## 添加依赖

在CMake脚本中链接相关动态库。

```
1. target_link_libraries(entry PUBLIC libasset_ndk.z.so)
```

引用头文件。

```
1. #include "napi/native_api.h"
2. #include <string.h>
3. #include "asset/asset_api.h"
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/AssetStoreKit/AssetStoreNdk/entry/src/main/cpp/napi_init.cpp#L16-L20)

## 新增支持同步的关键资产

新增密码demo\_pwd（别名demo\_alias），附属信息为demo\_label，支持同步的关键资产。

```
1. static napi_value AddSyncAsset(napi_env env, napi_callback_info info)
2. {
3. char *secretStr = "demo_pwd";
4. char *aliasStr = "demo_alias";
5. char *labelStr = "demo_label";

7. Asset_Blob secret = {(uint32_t)(strlen(secretStr)), (uint8_t *)secretStr};
8. Asset_Blob alias = {(uint32_t)(strlen(aliasStr)), (uint8_t *)aliasStr};
9. Asset_Blob label = {(uint32_t)(strlen(labelStr)), (uint8_t *)labelStr};
10. Asset_Attr attr[] = {
11. {.tag = ASSET_TAG_SECRET, .value.blob = secret},
12. {.tag = ASSET_TAG_ALIAS, .value.blob = alias},
13. {.tag = ASSET_TAG_DATA_LABEL_NORMAL_1, .value.blob = label},
14. {.tag = ASSET_TAG_SYNC_TYPE, .value.u32 = ASSET_SYNC_TYPE_TRUSTED_DEVICE}, // 需指定在可信设备间同步（如新旧设备间克隆）。
15. };

17. int32_t addResult = OH_Asset_Add(attr, sizeof(attr) / sizeof(attr[0]));
18. napi_value ret;
19. napi_create_int32(env, addResult, &ret);
20. return ret;
21. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/AssetStoreKit/AssetStoreNdk/entry/src/main/cpp/napi_init.cpp#L310-L332)

## 接入备份恢复扩展能力

为触发应用数据备份恢复，需要[应用接入数据备份恢复](app-file-backup-extension.md)。

## 查询关键资产同步结果

### 接口介绍

通过API文档查看查询关键资产同步结果接口OH\_Asset\_QuerySyncResult。

在查询关键资产时，关键资产属性的内容参数如下表所示。

| 属性名称（Asset\_Tag） | 属性内容（Asset\_Value） | 是否必选 | 说明 |
| --- | --- | --- | --- |
| ASSET\_TAG\_REQUIRE\_ATTR\_ENCRYPTED14+ | 类型为bool。 | 是 | 是否查询业务自定义附属信息被加密的关键资产同步结果。true表示查询业务自定义附属信息加密存储的关键资产同步结果，false表示查询业务自定义附属信息不加密存储的关键资产同步结果。默认值为false。 |
| ASSET\_TAG\_GROUP\_ID18+ | 类型为uint8[]，长度为7-127字节。 | 是 | 待查询的关键资产所属群组，默认查询不属于任何群组的关键资产同步结果。 |

### 代码示例

```
1. static napi_value QuerySyncResult(napi_env env, napi_callback_info info)
2. {
3. Asset_SyncResult syncResult = {0};
4. int32_t queryResult = OH_Asset_QuerySyncResult(NULL, 0, &syncResult);
5. napi_value ret;
6. napi_create_int32(env, queryResult, &ret);
7. return ret;
8. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/AssetStoreKit/AssetStoreNdk/entry/src/main/cpp/napi_init.cpp#L334-L343)

## 约束和限制

在可信设备间同步过程中，新旧设备的关键资产均需处于可访问的状态，否则可能出现关键资产无法同步的情况。

* 仅设置密码时可访问的关键资产，如果新旧设备中任意一台设备未设置锁屏密码，则无法同步成功。
* 仅屏幕处于解锁状态时可访问的关键资产，如果新旧设备中任意一台设备的屏幕未处于解锁状态，则无法同步成功。
* 仅用户认证通过后可访问的关键资产，如果旧设备未设置锁屏密码，则无法同步成功。
