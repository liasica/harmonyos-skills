---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-backup-and-restore
title: 数据库备份与恢复 (C/C++)
breadcrumb: 指南 > 应用框架 > ArkData（方舟数据管理） > 数据可靠性与安全性 > 数据库备份与恢复 (C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:74fe48a04459c81a6326c41d03e1f32b5b2b2a917ae3b586b89095f387e4387f
---

## 场景介绍

如果操作或存储的过程中出现问题，开发者可以使用恢复功能，将数据库恢复到之前的状态，重新对数据库进行操作。

在数据库被篡改、删除、或者设备断电场景下，数据库可能会因为数据丢失、数据损坏、脏数据等而不可用，可以通过数据库的备份恢复能力将数据库恢复至可用状态。

当前仅支持使用关系型数据库（C/C++）进行备份与恢复。

## 开发步骤

数据库操作或者存储过程中，有可能会因为各种原因发生非预期的数据库异常的情况，可以根据需要使用关系型数据库的备份能力，以便在数据库异常时，可靠高效地恢复数据保证业务数据正常使用。

1. CMakeLists.txt中添加以下lib。

   ```
   1. libnative_rdb_ndk.z.so
   ```
2. 导入头文件。

   ```
   1. #include <cstring>
   2. #include "database/rdb/relational_store.h"
   3. #include "hilog/log.h"
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/RelationalStore/NativeDataEncryption/entry/src/main/cpp/napi_init.cpp#L18-L20)
3. 调用OH\_Rdb\_Backup接口实现数据库备份。

   ```
   1. OH_Rdb_ConfigV2 *config = OH_Rdb_CreateConfig();
   2. OH_Rdb_SetDatabaseDir(config, "/data/storage/el2/database");
   3. OH_Rdb_SetArea(config, RDB_SECURITY_AREA_EL2);
   4. OH_Rdb_SetStoreName(config, "RdbTest.db");
   5. OH_Rdb_SetSecurityLevel(config, OH_Rdb_SecurityLevel::S3);
   6. OH_Rdb_SetBundleName(config, "com.example.nativedemo");
   7. int errCode = 0;
   8. OH_Rdb_Store *store = OH_Rdb_CreateOrOpen(config, &errCode);
   9. // 备份数据库
   10. int result = OH_Rdb_Backup(store, "/data/storage/el2/database/RdbTest_bak.db");
   11. OH_Rdb_CloseStore(store);
   12. store = nullptr;
   13. OH_Rdb_DestroyConfig(config);
   14. config = nullptr;
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/RelationalStore/NativeDataEncryption/entry/src/main/cpp/napi_init.cpp#L107-L122)
4. 调用OH\_Rdb\_Restore接口实现数据库恢复。

   ```
   1. OH_Rdb_ConfigV2 *config = OH_Rdb_CreateConfig();
   2. OH_Rdb_SetDatabaseDir(config, "/data/storage/el2/database");
   3. OH_Rdb_SetArea(config, RDB_SECURITY_AREA_EL2);
   4. OH_Rdb_SetStoreName(config, "RdbRestoreTest.db");
   5. OH_Rdb_SetSecurityLevel(config, OH_Rdb_SecurityLevel::S3);
   6. OH_Rdb_SetBundleName(config, "com.example.nativedemo");
   7. int errCode = 0;
   8. OH_Rdb_Store *store = OH_Rdb_CreateOrOpen(config, &errCode);
   9. // 恢复数据库
   10. int result2 =
   11. OH_Rdb_Restore(store, "/data/storage/el2/database/RdbTest_bak.db");
   12. OH_Rdb_CloseStore(store);
   13. store = nullptr;
   14. OH_Rdb_DestroyConfig(config);
   15. config = nullptr;
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkData/RelationalStore/NativeDataEncryption/entry/src/main/cpp/napi_init.cpp#L132-L148)
5. 调用OH\_Rdb\_RegisterCorruptedHandler接口注册数据库异常处理。

   从API version 22开始，支持注册数据库异常处理，开发者可根据需要调用OH\_Rdb\_RegisterCorruptedHandler接口注册数据库异常处理。

   ```
   1. // 数据库异常后处理的回调函数。
   2. // context为OH_Rdb_RegisterCorruptedHandler调用时传入的指针，生命周期由业务自身管理
   3. // config为OH_Rdb_RegisterCorruptedHandler调用时拷贝的临时变量，不可在回调函数外部使用
   4. // store为发生异常的DB句柄，如果DB无法打开则为空指针，注意判空。该指针由系统产生，回调函数结束后即刻释放，不可在回调函数外部使用
   5. void CorruptedHandler(void *context, OH_Rdb_ConfigV2 *config, OH_Rdb_Store *store)
   6. {
   7. const char* restorePath = "/data/storage/el2/database/RdbTest_bak.db";
   8. // store为空代表非DB文件或者DB文件彻底异常无法打开
   9. if (store == nullptr) {
   10. OH_Rdb_DeleteStoreV2(config);
   11. // 重新创建数据库，如果有备库可以重建后调用恢复接口
   12. return;
   13. }
   14. // 通过store句柄使用备库进行数据库恢复
   15. int errCode = OH_Rdb_Restore(store, restorePath);
   16. // restore在有其它接口占用写链接时会失败，建议等待其它调用结束后再调用
   17. if (errCode != 0) {
   18. OH_LOG_ERROR(LOG_APP, "restore failed! errCode is: %{public}d", errCode);
   19. // 等待其它线程调用结束，进行重试。不建议重试次数过多或等待时间过长，避免占用太多系统资源。
   20. errCode = OH_Rdb_Restore(store, restorePath);
   21. // 或采用标记的方式标记数据库异常，后续在进程重启或业务空闲时进行恢复
   22. }
   23. }
   24. OH_Rdb_ConfigV2* config3 = OH_Rdb_CreateConfig();
   25. OH_Rdb_SetDatabaseDir(config3, "/data/storage/el2/database");
   26. OH_Rdb_SetArea(config3, RDB_SECURITY_AREA_EL2);
   27. OH_Rdb_SetStoreName(config3, "RdbRestoreTest.db");
   28. OH_Rdb_SetSecurityLevel(config3, OH_Rdb_SecurityLevel::S3);
   29. OH_Rdb_SetBundleName(config3, "com.example.nativedemo");
   30. int errCode3 = 0;
   31. OH_Rdb_Store *store3 = OH_Rdb_CreateOrOpen(config3, &errCode3);

   33. // 备份数据库
   34. int result = OH_Rdb_Backup(store3, "/data/storage/el2/database/RdbTest_bak.db");

   36. void *context = nullptr;
   37. Rdb_CorruptedHandler handler = CorruptedHandler;
   38. // 注册数据库异常处理
   39. OH_Rdb_RegisterCorruptedHandler(config3, context, handler);
   ```
6. 调用OH\_Rdb\_UnregisterCorruptedHandler接口取消注册数据库异常处理。

   从API version 22开始，支持取消注册数据库异常处理，开发者可根据需要调用OH\_Rdb\_UnregisterCorruptedHandler接口取消注册数据库异常处理。

   ```
   1. OH_Rdb_ConfigV2* config4 = OH_Rdb_CreateConfig();
   2. OH_Rdb_SetDatabaseDir(config4, "/data/storage/el2/database");
   3. OH_Rdb_SetArea(config4, RDB_SECURITY_AREA_EL2);
   4. OH_Rdb_SetStoreName(config4, "RdbRestoreTest.db");
   5. OH_Rdb_SetSecurityLevel(config4, OH_Rdb_SecurityLevel::S3);
   6. OH_Rdb_SetBundleName(config4, "com.example.nativedemo");
   7. int errCode4 = 0;
   8. OH_Rdb_Store *store4 = OH_Rdb_CreateOrOpen(config4, &errCode4);

   10. void *context = nullptr;
   11. Rdb_CorruptedHandler handler = CorruptedHandler;
   12. // 取消注册数据库异常处理，handler和context必须要和订阅时保持一致，否则取消失败
   13. OH_Rdb_UnregisterCorruptedHandler(config4, context, handler);
   ```
