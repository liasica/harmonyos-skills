---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-environment-guidelines
title: 获取用户目录环境(C/C++)
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 用户文件 > 获取用户目录环境(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:16+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:34f55948662d42ea5ad6bf9fff49d7769bd357554f21cedf829b30bbad8f113c
---

## 场景介绍

[Environment](../harmonyos-references/capi-oh-environment-h.md)提供了获取公共文件用户目录路径的能力，以支持三方应用在公共文件用户目录下进行文件访问操作。

## 约束限制

* 使用此接口，需确认设备具有以下系统能力：SystemCapability.FileManagement.File.Environment.FolderObtain。
* 此接口仅用作公共沙箱目录路径的获取接口，操作对应的公共目录及其子目录需获取通过弹窗授权方式向用户申请授予对应目录的权限，具体参考[访问控制-向用户申请授权](request-user-authorization.md)。

## 接口说明

接口的详细说明，请参考[oh\_environment.h](../harmonyos-references/capi-oh-environment-h.md)。

| 接口名称 | 描述 |
| --- | --- |
| FileManagement\_ErrCode OH\_Environment\_GetUserDownloadDir (char \*\*result) | 获取用户Download目录沙箱路径。只支持2in1设备。 |
| FileManagement\_ErrCode OH\_Environment\_GetUserDesktopDir (char \*\*result) | 获取用户Desktop目录沙箱路径。只支持2in1设备。 |
| FileManagement\_ErrCode OH\_Environment\_GetUserDocumentDir (char \*\*result) | 获取用户Document目录沙箱路径。只支持2in1设备。 |

## 开发步骤

**在CMake脚本中链接动态库**

CMakeLists.txt中添加以下lib。

```
1. target_link_libraries(sample PUBLIC libohenvironment.so libhilog_ndk.z.so)
```

**添加头文件**

```
1. #include <cstdlib>
2. #include <filemanagement/environment/oh_environment.h>
3. #include <filemanagement/fileio/oh_fileio.h>
4. #include <hilog/log.h>
```

1. 调用OH\_Environment\_GetUserDownloadDir接口获取用户Download目录沙箱路径，在接口中使用malloc申请的内存需要在使用完后释放因此需要free对应的内存。示例代码如下所示：

   ```
   1. void GetUserDownloadDirPathExample()
   2. {
   3. char *downloadPath = nullptr;
   4. FileManagement_ErrCode ret = OH_Environment_GetUserDownloadDir(&downloadPath);
   5. if (ret == 0) {
   6. OH_LOG_INFO(LOG_APP, "Succeeded in getting user download directory, path=%{public}s", downloadPath);
   7. free(downloadPath);
   8. } else {
   9. OH_LOG_ERROR(LOG_APP, "Failed to get download path, error code is %{public}d", ret);
   10. }
   11. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/CoreFile/NDKEnvironmentSample/entry/src/main/cpp/napi_init.cpp#L124-L136)
2. 调用OH\_Environment\_GetUserDesktopDir接口获取用户Desktop目录沙箱路径，在接口中使用malloc申请的内存需要在使用完后释放因此需要free对应的内存。示例代码如下所示：

   ```
   1. void GetUserDesktopDirPathExample()
   2. {
   3. char *desktopPath = nullptr;
   4. FileManagement_ErrCode ret = OH_Environment_GetUserDesktopDir(&desktopPath);
   5. if (ret == 0) {
   6. OH_LOG_INFO(LOG_APP, "Succeeded in getting user desktop directory, path=%{public}s", desktopPath);
   7. free(desktopPath);
   8. } else {
   9. OH_LOG_ERROR(LOG_APP, "Failed to get user desktop path, error code is %{public}d", ret);
   10. }
   11. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/CoreFile/NDKEnvironmentSample/entry/src/main/cpp/napi_init.cpp#L144-L156)
3. 调用OH\_Environment\_GetUserDocumentDir接口获取用户Document目录沙箱路径，在接口中使用malloc申请的内存需要在使用完后释放因此需要free对应的内存。示例代码如下所示：

   ```
   1. void GetUserDocumentDirPathExample()
   2. {
   3. char *documentPath = nullptr;
   4. FileManagement_ErrCode ret = OH_Environment_GetUserDocumentDir(&documentPath);
   5. if (ret == 0) {
   6. OH_LOG_INFO(LOG_APP, "Succeeded in getting user document directory, path=%{public}s", documentPath);
   7. free(documentPath);
   8. } else {
   9. OH_LOG_ERROR(LOG_APP, "Failed to get user document path, error code is %{public}d", ret);
   10. }
   11. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/CoreFile/NDKEnvironmentSample/entry/src/main/cpp/napi_init.cpp#L163-L175)
4. 调用OH\_Environment\_GetUserDocumentDir接口获取用户Document目录沙箱路径，使用stat函数判断Document目录空间大小。示例代码如下所示：

   使用前需要引入如下头文件：

   ```
   1. #include <sys/stat.h>
   ```

   ```
   1. void GetUserDownloadDirSizeExample()
   2. {
   3. char *documentPath = nullptr;
   4. FileManagement_ErrCode ret = OH_Environment_GetUserDocumentDir(&documentPath);
   5. if (ret == 0) {
   6. OH_LOG_INFO(LOG_APP, "Succeeded in getting user document directory, path=%{public}s", documentPath);
   7. struct stat fileStat;
   8. int result = stat(documentPath, &fileStat);
   9. if (result == 0) {
   10. OH_LOG_INFO(LOG_APP, "Succeeded in getting file info. document Size=%{public}ld", fileStat.st_size);
   11. } else {
   12. OH_LOG_ERROR(LOG_APP, "Failed to stat user document directory, error code is %{public}d", result);
   13. }
   14. free(documentPath);
   15. } else {
   16. OH_LOG_ERROR(LOG_APP, "Failed to get user document directory, error code is %{public}d", ret);
   17. }
   18. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/CoreFile/NDKEnvironmentSample/entry/src/main/cpp/napi_init.cpp#L183-L202)
