---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-environment-guidelines
title: 获取用户目录环境(C/C++)
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 用户文件 > 获取用户目录环境(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7f2aeba435f62b3b7f0711929735821c722e5056dedd4b2d53ab6c8236f9a1b5
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
| FileManagement\_ErrCode OH\_Environment\_GetUserDownloadDir (char \*\*result) | 获取用户Download目录沙箱路径。支持2in1设备。  从API版本26.0.0开始，支持tablet设备。 |
| FileManagement\_ErrCode OH\_Environment\_GetUserDesktopDir (char \*\*result) | 获取用户Desktop目录沙箱路径。支持2in1设备。  从API版本26.0.0开始，支持tablet设备。 |
| FileManagement\_ErrCode OH\_Environment\_GetUserDocumentDir (char \*\*result) | 获取用户Document目录沙箱路径。支持2in1设备。  从API版本26.0.0开始，支持tablet设备。 |

## 开发步骤

**在CMake脚本中链接动态库**

CMakeLists.txt中添加以下lib。

```txt
target_link_libraries(sample PUBLIC libohenvironment.so libhilog_ndk.z.so)
```

**添加头文件**

```
#include <cstdlib>
#include <filemanagement/environment/oh_environment.h>
#include <filemanagement/fileio/oh_fileio.h>
#include <hilog/log.h>
```

1. 调用OH\_Environment\_GetUserDownloadDir接口获取用户Download目录沙箱路径，在接口中使用malloc申请的内存需要在使用完后释放因此需要free对应的内存。示例代码如下所示：

   ```
   void GetUserDownloadDirPathExample()
   {
       char *downloadPath = nullptr;
       FileManagement_ErrCode ret = OH_Environment_GetUserDownloadDir(&downloadPath);
       if (ret == 0) {
           OH_LOG_INFO(LOG_APP, "Succeeded in getting user download directory, path=%{public}s", downloadPath);
           free(downloadPath);
       } else {
           OH_LOG_ERROR(LOG_APP, "Failed to get download path, error code is %{public}d", ret);
       }
   }
   ```
2. 调用OH\_Environment\_GetUserDesktopDir接口获取用户Desktop目录沙箱路径，在接口中使用malloc申请的内存需要在使用完后释放因此需要free对应的内存。示例代码如下所示：

   ```
   void GetUserDesktopDirPathExample()
   {
       char *desktopPath = nullptr;
       FileManagement_ErrCode ret = OH_Environment_GetUserDesktopDir(&desktopPath);
       if (ret == 0) {
           OH_LOG_INFO(LOG_APP, "Succeeded in getting user desktop directory, path=%{public}s", desktopPath);
           free(desktopPath);
       } else {
           OH_LOG_ERROR(LOG_APP, "Failed to get user desktop path, error code is %{public}d", ret);
       }
   }
   ```
3. 调用OH\_Environment\_GetUserDocumentDir接口获取用户Document目录沙箱路径，在接口中使用malloc申请的内存需要在使用完后释放因此需要free对应的内存。示例代码如下所示：

   ```
   void GetUserDocumentDirPathExample()
   {
       char *documentPath = nullptr;
       FileManagement_ErrCode ret = OH_Environment_GetUserDocumentDir(&documentPath);
       if (ret == 0) {
           OH_LOG_INFO(LOG_APP, "Succeeded in getting user document directory, path=%{public}s", documentPath);
           free(documentPath);
       } else {
           OH_LOG_ERROR(LOG_APP, "Failed to get user document path, error code is %{public}d", ret);
       }
   }
   ```
4. 调用OH\_Environment\_GetUserDocumentDir接口获取用户Document目录沙箱路径，使用stat函数判断Document目录空间大小。示例代码如下所示：

   使用前需要引入如下头文件：

   ```
   #include <sys/stat.h>
   ```

   ```
   void GetUserDownloadDirSizeExample()
   {
       char *documentPath = nullptr;
       FileManagement_ErrCode ret = OH_Environment_GetUserDocumentDir(&documentPath);
       if (ret == 0) {
           OH_LOG_INFO(LOG_APP, "Succeeded in getting user document directory, path=%{public}s", documentPath);
           struct stat fileStat;
           int result = stat(documentPath, &fileStat);
           if (result == 0) {
               OH_LOG_INFO(LOG_APP, "Succeeded in getting file info. document Size=%{public}ld", fileStat.st_size);
           } else {
               OH_LOG_ERROR(LOG_APP, "Failed to stat user document directory, error code is %{public}d", result);
           }
           free(documentPath);
       } else {
           OH_LOG_ERROR(LOG_APP, "Failed to get user document directory, error code is %{public}d", ret);
       }
   }
   ```
