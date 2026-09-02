---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/request-dir-permission
title: 获取并使用公共目录
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 用户文件 > 获取并使用公共目录
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:24+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8cc998b6880f9a332e21ee4c2aad5d210c20f751242c7f49a011023c59534a18
---

## 通过 ArkTS 接口获取并访问公共目录

目录环境能力接口（[ohos.file.environment](../harmonyos-references/js-apis-file-environment.md)）提供获取公共目录路径的能力，支持三方应用在公共文件用户目录下进行文件访问操作。

**约束限制**

* 使用此方式，需确认设备具有以下系统能力：SystemCapability.FileManagement.File.Environment.FolderObtain，当前支持2in1设备。

  从API版本26.0.0开始，支持tablet设备。

  ```ts
  if (!canIUse('SystemCapability.FileManagement.File.Environment.FolderObtain')) {
      console.error('this api is not supported on this device');
      return;
  }
  ```
* 公共目录获取接口仅用于获取公共目录路径，不对公共目录访问权限进行校验。若需访问公共目录需申请对应的公共目录访问权限。三方应用需要访问公共目录时，需向用户申请授予[Download目录权限](permissions-for-all-user.md#ohospermissionread_write_download_directory)、[Documents目录权限](permissions-for-all-user.md#ohospermissionread_write_documents_directory)或[Desktop目录权限](restricted-permissions.md#ohospermissionread_write_desktop_directory)，具体参考[访问控制-向用户申请授权](request-user-authorization.md)。

### 示例

1. 获取公共目录路径。

   ```ts
   import { BusinessError } from '@kit.BasicServicesKit';
   import { Environment } from '@kit.CoreFileKit';
   ```

   ```typescript
   function getUserDirExample() {
     try {
       const downloadPath = Environment.getUserDownloadDir();
       console.info(`Succeeded in getting user download dir: ${downloadPath}`);
       const documentsPath = Environment.getUserDocumentDir();
       console.info(`Succeeded in getting user document dir: ${documentsPath}`);
     } catch (error) {
       const err: BusinessError = error as BusinessError;
       console.error(`Failed to get user dir. Code: ${err.code}, message: ${err.message}`);
     }
   }
   ```
2. 以Download目录为例，访问Download目录下的文件。

   ```ts
   import { BusinessError } from '@kit.BasicServicesKit';
   import { Environment } from '@kit.CoreFileKit';
   import { fileIo } from '@kit.CoreFileKit';
   import { common } from '@kit.AbilityKit';

   // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
   let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   ```

   ```typescript
   function readUserDownloadDirExample(context: common.UIAbilityContext) {
     try {
       // 获取 Download 目录
       const downloadPath = Environment.getUserDownloadDir();
       console.info(`Succeeded in getting user download dir: ${downloadPath}`);
       const dirPath = context.filesDir;
       // 查看 Download 目录下的文件并拷贝到沙箱目录中
       let fileList: string[] = fileIo.listFileSync(downloadPath);
       fileList.forEach((file, index) => {
         console.info(`${downloadPath} ${index}: ${file}`);
         if (fileIo.statSync(`${downloadPath}/${file}`).isFile()) {
           fileIo.copyFileSync(`${downloadPath}/${file}`, `${dirPath}/${file}`);
         }
       });
       // 查看沙箱目录下对应的文件
       fileList = fileIo.listFileSync(dirPath);
       fileList.forEach((file, index) => {
         console.info(`Succeeded in listing file, ${dirPath} ${index}: ${file}`);
       });
     } catch (error) {
       const err: BusinessError = error as BusinessError;
       console.error(`Failed to read user download dir. Code: ${err.code}, message: ${err.message}`);
     }
   }
   ```
3. 以Download目录为例，保存文件到Download目录。

   ```ts
   import { BusinessError } from '@kit.BasicServicesKit';
   import { Environment } from '@kit.CoreFileKit';
   import { fileIo } from '@kit.CoreFileKit';
   ```

   ```typescript
   function writeUserDownloadDirExample() {
     // 检查是否具有 READ_WRITE_DOWNLOAD_DIRECTORY 权限，无权限则需要向用户申请授予权限。
     try {
       // 获取 Download 目录
       const downloadPath = Environment.getUserDownloadDir();
       console.info(`Succeeded in getting user download dir: ${downloadPath}`);
       // 保存 temp.txt 到 Download 目录下
       const file = fileIo.openSync(`${downloadPath}/temp.txt`, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
       fileIo.writeSync(file.fd, 'write a message');
       fileIo.closeSync(file);
     } catch (error) {
       const err: BusinessError = error as BusinessError;
       console.error(`Failed to write user download dir. Code: ${err.code}, message: ${err.message}`);
     }
   }
   ```

## 通过 C/C++ 接口获取并使用公共目录

除了通过ArkTS访问公共目录的方式，也可通过C/C++接口进行目录访问，具体可以参考 [oh\_environment.h](../harmonyos-references/capi-oh-environment-h.md)。

**约束限制**

* 使用此接口，需确认设备具有以下系统能力：SystemCapability.FileManagement.File.Environment.FolderObtain。
* 三方应用需要访问公共目录时，需通过弹窗授权向用户申请授予Download目录权限、Documents目录权限或Desktop目录权限，具体参考[访问控制-向用户申请授权](request-user-authorization.md)。

### 接口说明

接口的详细说明，请参考[oh\_environment.h](../harmonyos-references/capi-oh-environment-h.md)。

| 接口名称 | 描述 |
| --- | --- |
| FileManagement\_ErrCode OH\_Environment\_GetUserDownloadDir (char \*\*result) | 获取用户Download目录沙箱路径。支持2in1设备。  从API版本26.0.0开始，支持tablet设备 |
| FileManagement\_ErrCode OH\_Environment\_GetUserDesktopDir (char \*\*result) | 获取用户Desktop目录沙箱路径。支持2in1设备。  从API版本26.0.0开始，支持tablet设备 |
| FileManagement\_ErrCode OH\_Environment\_GetUserDocumentDir (char \*\*result) | 获取用户Document目录沙箱路径。支持2in1设备。  从API版本26.0.0开始，支持tablet设备 |

### 开发步骤

**在CMake脚本中链接动态库**

CMakeLists.txt中添加以下lib。

```txt
target_link_libraries(sample PUBLIC libohenvironment.so libhilog_ndk.z.so)
```

**添加头文件**

```
#include <filemanagement/environment/oh_environment.h>
#include <filemanagement/fileio/oh_fileio.h>
#include <hilog/log.h>
```

1. 调用OH\_Environment\_GetUserDownloadDir接口获取用户Download目录沙箱路径，在接口中使用malloc申请的内存需要在使用完后释放因此需要free对应的内存。示例代码如下所示：

   ```
   #include <cstdlib>
   ```

   ```
   void GetUserDownloadDirExample()
   {
       char *downloadPath = nullptr;
       FileManagement_ErrCode ret = OH_Environment_GetUserDownloadDir(&downloadPath);
       if (ret == 0) {
           OH_LOG_INFO(LOG_APP, "Succeeded in getting user download directory, download path=%{public}s", downloadPath);
           free(downloadPath);
       } else {
           OH_LOG_ERROR(LOG_APP, "Failed to get download path, error code is %{public}d", ret);
       }
   }
   ```
2. 调用OH\_Environment\_GetUserDownloadDir接口获取用户Download目录沙箱路径，并查看Download目录下的文件。示例代码如下所示：

   ```
   #include <cstdlib>
   #include <dirent.h>
   ```

   ```
   void ScanUserDownloadDirPathExample()
   {
       // 获取 download 路径
       char *downloadPath = nullptr;
       FileManagement_ErrCode ret = OH_Environment_GetUserDownloadDir(&downloadPath);
       if (ret == 0) {
           OH_LOG_INFO(LOG_APP, "Succeeded in scanning user download directory, path=%{public}s", downloadPath);
       } else {
           OH_LOG_ERROR(LOG_APP, "Failed to get download path, error code is %{public}d", ret);
           return;
       }
       // 查看文件夹下的文件
       struct dirent **namelist = nullptr;
       int num = scandir(downloadPath, &namelist, nullptr, nullptr);
       if (num < 0) {
           free(downloadPath);
           OH_LOG_ERROR(LOG_APP, "Failed to scan directory");
           return;
       }

       for (int i = 0; i < num; i++) {
           OH_LOG_INFO(LOG_APP, "Succeeded in scanning directory, file name is %{public}s", namelist[i]->d_name);
       }
       free(downloadPath);
       for (int i = 0; i < num; i++) {
           free(namelist[i]);
       }
       free(namelist);
   }
   ```
3. 调用OH\_Environment\_GetUserDownloadDir接口获取用户Download目录沙箱路径，并保存temp.txt到Download目录下。示例代码如下所示：

   ```
   #include <fstream>
   ```

   ```
   void WriteUserDownloadDirPathExample()
   {
       // 获取 download 路径
       char *downloadPath = nullptr;
       FileManagement_ErrCode ret = OH_Environment_GetUserDownloadDir(&downloadPath);
       if (ret == 0) {
           OH_LOG_INFO(LOG_APP, "Succeeded in getting user download directory, path=%{public}s", downloadPath);
       } else {
           OH_LOG_ERROR(LOG_APP, "Failed to get download path, error code is %{public}d", ret);
           return;
       }
       // 保存文件到 download 目录下
       std::string filePath = std::string(downloadPath) + "/temp.txt";
       free(downloadPath);

       std::ofstream outfile;
       outfile.open(filePath.c_str());
       if (!outfile) {
           OH_LOG_ERROR(LOG_APP, "Failed to open file");
           return;
       }
       std::string msg = "Write a message";
       outfile.write(msg.c_str(), msg.size());
       outfile.close();
   }
   ```
