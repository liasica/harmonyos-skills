---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/dlp-guidelines-ndk
title: 数据防泄漏服务开发指导(C/C++)
breadcrumb: 指南 > 系统 > 安全 > Data Protection Kit（数据保护服务） > 数据防泄漏服务 > 数据防泄漏服务开发指导(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-29T13:31:20+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:c0eedbf350427c25793a91d7dfc5406db3a84da954a4a2b4257c1e347dd30bac
---

数据防泄漏（Data Loss Prevention，DLP）是系统提供的系统级的数据防泄漏解决方案，提供跨设备的文件的权限管理、加密存储、授权访问等能力。

* 权限管理：查询当前DLP沙箱的权限信息。
* 文件信息获取：获取DLP文件的基本信息，如原始文件名。
* 沙箱环境检测：查询当前应用是否运行在DLP沙箱环境。
* 配置管理：设置、获取和清理沙箱应用配置信息。

## 接口说明

数据防泄漏服务关键接口如下表所示。具体API说明详见[API参考](../harmonyos-references/capi-dlp-permission-api-h.md)

| 名称 | 描述 |
| --- | --- |
| DLP\_ErrCode OH\_DLP\_GetDlpPermissionInfo(DLP\_FileAccess \*dlpFileAccess, uint32\_t \*flags) | 查询当前DLP沙箱的权限信息。 |
| DLP\_ErrCode OH\_DLP\_GetOriginalFileName(const char \*fileName, char \*\*originalFileName) | 获取指定DLP文件名的原始文件名。 |
| DLP\_ErrCode OH\_DLP\_IsInSandbox(bool \*isInSandbox) | 查询当前应用是否运行在DLP沙箱环境。 |
| DLP\_ErrCode OH\_DLP\_SetSandboxAppConfig(const char \*configInfo) | 设置沙箱应用配置信息。 |
| DLP\_ErrCode OH\_DLP\_GetSandboxAppConfig(char \*\*configInfo) | 获取沙箱应用配置信息。 |
| DLP\_ErrCode OH\_DLP\_CleanSandboxAppConfig() | 清理沙箱应用配置信息。 |

## 开发步骤

1. 在CMakeLists.txt中导入数据防泄漏的共享库，并链接该库。

   ```
   1. cmake_minimum_required(VERSION 3.5.0)
   2. project(DlpApiTest)

   4. set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

   6. if(DEFINED PACKAGE_FIND_FILE)
   7. include(${PACKAGE_FIND_FILE})
   8. endif()

   10. include_directories(${NATIVERENDER_ROOT_PATH}
   11. ${NATIVERENDER_ROOT_PATH}/include)

   13. add_library(entry SHARED napi_init.cpp)
   14. target_link_libraries(entry PUBLIC libace_napi.z.so libohdlp_permission.so)
   ```
2. 导入数据防泄漏服务的头文件和NAPI相关头文件。

   ```
   1. #include "napi/native_api.h"
   2. #include <cstdint>
   3. #include <cstdlib>
   4. #include "DataProtectionKit/dlp_permission_api.h"
   ```
3. 查询当前DLP沙箱的权限信息。

   ```
   1. static napi_value GetDlpPermissionInfo(napi_env env, napi_callback_info info)
   2. {
   3. DLP_FileAccess dlpFileAccess = NO_PERMISSION;
   4. uint32_t flags = 0;
   5. DLP_ErrCode ret = OH_DLP_GetDlpPermissionInfo(&dlpFileAccess, &flags);
   6. if (ret == DLP_ErrCode::ERR_OH_SUCCESS) {
   7. napi_value result[2] = {nullptr};
   8. napi_create_int32(env, dlpFileAccess, &result[0]);
   9. napi_create_int32(env, flags, &result[1]);
   10. return result[1];
   11. }
   12. napi_value result = nullptr;
   13. napi_create_int32(env, ret, &result);
   14. return result;
   15. }
   ```
4. 获取指定DLP文件名的原始文件名。

   ```
   1. static napi_value GetOriginalFileName(napi_env env, napi_callback_info info)
   2. {
   3. const char *fileName = "test.txt.dlp";
   4. char *originalFileName = nullptr;
   5. DLP_ErrCode ret = OH_DLP_GetOriginalFileName(fileName, &originalFileName);
   6. if (ret == DLP_ErrCode::ERR_OH_SUCCESS) {
   7. napi_value result = nullptr;
   8. napi_create_string_utf8(env, originalFileName, NAPI_AUTO_LENGTH, &result);
   9. return result;
   10. }
   11. napi_value result = nullptr;
   12. napi_create_int32(env, ret, &result);
   13. free(originalFileName);
   14. return result;
   15. }
   ```
5. 查询当前应用是否运行在DLP沙箱环境。

   ```
   1. static napi_value IsInSandbox(napi_env env, napi_callback_info info)
   2. {
   3. bool isInSandbox = false;
   4. DLP_ErrCode ret = OH_DLP_IsInSandbox(&isInSandbox);
   5. if (ret == DLP_ErrCode::ERR_OH_SUCCESS) {
   6. napi_value result = nullptr;
   7. napi_get_boolean(env, isInSandbox, &result);
   8. return result;
   9. }
   10. napi_value result = nullptr;
   11. napi_create_int32(env, ret, &result);
   12. return result;
   13. }
   ```
6. 设置沙箱应用配置信息。

   ```
   1. static napi_value SetSandboxAppConfig(napi_env env, napi_callback_info info)
   2. {
   3. const char *configInfo = "configInfo";
   4. DLP_ErrCode ret = OH_DLP_SetSandboxAppConfig(configInfo);

   6. napi_value result = nullptr;
   7. napi_create_int32(env, ret, &result);
   8. return result;
   9. }
   ```
7. 获取沙箱应用配置信息。

   ```
   1. static napi_value GetSandboxAppConfig(napi_env env, napi_callback_info info)
   2. {
   3. char *configInfo = nullptr;
   4. DLP_ErrCode ret = OH_DLP_GetSandboxAppConfig(&configInfo);
   5. if (ret == DLP_ErrCode::ERR_OH_SUCCESS) {
   6. napi_value result = nullptr;
   7. napi_create_string_utf8(env, configInfo, NAPI_AUTO_LENGTH, &result);
   8. return result;
   9. }
   10. napi_value result = nullptr;
   11. napi_create_int32(env, ret, &result);
   12. free(configInfo);
   13. return result;
   14. }
   ```
8. 清理沙箱应用配置信息。

   ```
   1. static napi_value CleanSandboxAppConfig(napi_env env, napi_callback_info info)
   2. {
   3. DLP_ErrCode ret = OH_DLP_CleanSandboxAppConfig();

   5. napi_value result = nullptr;
   6. napi_create_int32(env, ret, &result);
   7. return result;
   8. }
   ```
