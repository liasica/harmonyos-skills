---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-fileshare-guidelines
title: 授权持久化(C/C++)
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 用户文件 > 选择与保存用户文件 > 授权持久化(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d024547026121248e20a19c809215eba8ae7ce68dee789dea2ea629d6bea713b
---

## 场景介绍

应用通过Picker获取临时授权，临时授权在应用退出后或者设备重启后会清除。如果应用重启或者设备重启后需要直接访问之前已访问过的文件，则对文件进行[持久化授权](file-persistpermission.md#场景介绍)。FileShare提供了支持基于uri的文件及目录授予持久化权限、权限激活、权限查询等方法。

## 接口说明

接口的详细介绍请参见[oh\_file\_uri.h](../harmonyos-references/capi-oh-file-share-h.md)。

| 接口名称 | 描述 |
| --- | --- |
| OH\_FileShare\_PersistPermission(const FileShare\_PolicyInfo \*policies, unsigned int policyNum, FileShare\_PolicyErrorResult \*\*result, unsigned int \*resultNum) | 对所选择的多个文件或目录uri持久化授权。 |
| OH\_FileShare\_RevokePermission(const FileShare\_PolicyInfo \*policies, unsigned int policyNum, FileShare\_PolicyErrorResult \*\*result, unsigned int \*resultNum) | 对所选择的多个文件或目录uri取消持久化授权。 |
| OH\_FileShare\_ActivatePermission(const FileShare\_PolicyInfo \*policies, unsigned int policyNum, FileShare\_PolicyErrorResult \*\*result, unsigned int \*resultNum) | 使能多个已经持久化授权过的文件或目录uri。 |
| OH\_FileShare\_DeactivatePermission(const FileShare\_PolicyInfo \*policies, unsigned int policyNum, FileShare\_PolicyErrorResult \*\*result, unsigned int \*resultNum) | 取消使能授权过的多个文件或目录uri。 |
| OH\_FileShare\_CheckPersistentPermission(const FileShare\_PolicyInfo \*policies, unsigned int policyNum, bool \*\*result, unsigned int \*resultNum) | 校验所选择的多个文件或目录uri的持久化权限结果。 |
| OH\_FileShare\_ReleasePolicyErrorResult(FileShare\_PolicyErrorResult \*errorResult, unsigned int resultNum) | 释放FileShare\_PolicyErrorResult内存。 |

## 约束与限制

* 使用文件分享的相关接口，需确认设备具有以下系统能力：SystemCapability.FileManagement.AppFileService.FolderAuthorization。
* 在调用文件分享的相关接口前，需要申请权限："[ohos.permission.FILE\_ACCESS\_PERSIST](restricted-permissions.md#ohospermissionfile_access_persist)"，申请方式请参考[选择申请权限的方式](determine-application-mode.md)。

## 开发步骤

以下步骤描述了如何使用FileShare提供的Native API接口。

**添加动态链接库**

CMakeLists.txt中添加以下lib。

```
1. target_link_libraries(sample PUBLIC libohfileshare.so)
```

**头文件**

```
1. #include <filemanagement/fileshare/oh_file_share.h>
2. #include <iostream>
```

1. 创建FileShare\_PolicyInfo实例,调用OH\_FileShare\_PersistPermission接口，设置uri的持久化授权，接口入参policyNum最大上限为500。

   ```
   1. static const uint32_t policyNum = 2;
   2. char strTestPath1[] = "file://com.example.fileshare/data/storage/el2/base/files/test1.txt";
   3. char strTestPath2[] = "file://com.example.fileshare/data/storage/el2/base/files/test2.txt";
   4. FileShare_PolicyInfo policy[policyNum] = {
   5. {strTestPath1, static_cast<unsigned int>(strlen(strTestPath1)), FileShare_OperationMode::READ_MODE},
   6. {strTestPath2, static_cast<unsigned int>(strlen(strTestPath2)), FileShare_OperationMode::WRITE_MODE}};
   7. FileShare_PolicyErrorResult* result = nullptr;
   8. uint32_t resultNum = 0;
   9. napi_value napiResult;
   10. std::string resultStr;
   11. auto ret = OH_FileShare_PersistPermission(policy, policyNum, &result, &resultNum);
   12. if (ret != ERR_OK) {
   13. if (ret == ERR_EPERM && result != nullptr) {
   14. for (uint32_t i = 0; i < resultNum; i++) {
   15. std::cout << "error uri: " <<  result[i].uri << std::endl;
   16. std::cout << "error code: " <<  result[i].code << std::endl;
   17. std::cout << "error message: " << result[i].message << std::endl;
   18. // ...
   19. }
   20. }
   21. }
   22. OH_FileShare_ReleasePolicyErrorResult(result, resultNum);
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/CoreFile/UserFile/FileShareDevelopment_C/entry/src/main/cpp/napi_init.cpp#L23-L56)
2. 调用OH\_FileShare\_ActivatePermission接口，激活已授权过的uri，接口入参policyNum最大上限为500。

   ```
   1. auto ret = OH_FileShare_ActivatePermission(policy, policyNum, &result, &resultNum);
   2. if (ret != ERR_OK) {
   3. if (ret == ERR_EPERM && result != nullptr) {
   4. for (uint32_t i = 0; i < resultNum; i++) {
   5. std::cout << "error uri: " <<  result[i].uri << std::endl;
   6. std::cout << "error code: " <<  result[i].code << std::endl;
   7. std::cout << "error message: " << result[i].message << std::endl;
   8. // ...
   9. }
   10. }
   11. }
   12. OH_FileShare_ReleasePolicyErrorResult(result, resultNum);
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/CoreFile/UserFile/FileShareDevelopment_C/entry/src/main/cpp/napi_init.cpp#L76-L99)
3. 调用OH\_FileShare\_DeactivatePermission接口，停止已启用授权过uri的访问权限，接口入参policyNum最大上限为500。

   ```
   1. auto ret = OH_FileShare_DeactivatePermission(policy, policyNum, &result, &resultNum);
   2. if (ret != ERR_OK) {
   3. if (ret == ERR_EPERM && result != nullptr) {
   4. for (uint32_t i = 0; i < resultNum; i++) {
   5. std::cout << "error uri: " <<  result[i].uri << std::endl;
   6. std::cout << "error code: " <<  result[i].code << std::endl;
   7. std::cout << "error message: " << result[i].message << std::endl;
   8. // ...
   9. }
   10. }
   11. }
   12. OH_FileShare_ReleasePolicyErrorResult(result, resultNum);
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/CoreFile/UserFile/FileShareDevelopment_C/entry/src/main/cpp/napi_init.cpp#L119-L142)
4. 调用OH\_FileShare\_RevokePermission接口，撤销已经授权的uri持久化权限，接口入参policyNum最大上限为500。

   ```
   1. auto ret = OH_FileShare_RevokePermission(policy, policyNum, &result, &resultNum);
   2. if (ret != ERR_OK) {
   3. if (ret == ERR_EPERM && result != nullptr) {
   4. for (uint32_t i = 0; i < resultNum; i++) {
   5. std::cout << "error uri: " <<  result[i].uri << std::endl;
   6. std::cout << "error code: " <<  result[i].code << std::endl;
   7. std::cout << "error message: " << result[i].message << std::endl;
   8. // ...
   9. }
   10. }
   11. }
   12. OH_FileShare_ReleasePolicyErrorResult(result, resultNum);
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/CoreFile/UserFile/FileShareDevelopment_C/entry/src/main/cpp/napi_init.cpp#L162-L185)
5. 调用OH\_FileShare\_CheckPersistentPermission接口，检查uri持久化权限，接口入参policyNum最大上限为500。

   ```
   1. bool *result = nullptr;
   2. auto ret = OH_FileShare_CheckPersistentPermission(policy, policyNum, &result, &resultNum);
   3. if (ret != ERR_OK) {
   4. if (ret == ERR_EPERM && result != nullptr) {
   5. for (uint32_t i = 0; i < resultNum && resultNum <= policyNum; i++) {
   6. std::cout << "uri: " <<  policy[i].uri << std::endl;
   7. std::cout << "result: " <<  result[i] << std::endl;
   8. // ...
   9. }
   10. }
   11. }
   12. std::cout << "retCode: " <<  ret << std::endl;
   13. free(result);
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/CoreFile/UserFile/FileShareDevelopment_C/entry/src/main/cpp/napi_init.cpp#L204-L225)
