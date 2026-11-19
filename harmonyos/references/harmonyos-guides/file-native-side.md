---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/file-native-side
title: Native侧实现文件访问
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 文件基础服务开发实践 > Native侧实现文件访问
category: harmonyos-guides
scraped_at: 2026-11-19T09:47:55+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:6b347ca792cb6a44b6f23b15ee8d24ee61d6d5f679eae1372c2c30b565cad1cc
---

## 概述

在对文件处理性能要求高的场景中，Native侧访问文件处理数据比在ArkTS侧操作文件（详见[应用文件访问(ArkTS)](app-file-access.md)）有更高的效率和更快的响应，例如处理大文件、复杂的文件操作以及实时通信等低时延场景。根据文件位置的不同，应用在Native侧访问文件可以分为以下两种类型：

* 类型一：访问应用沙箱内的文件进行读写操作，主要是通过沙箱路径进行访问。
* 类型二：访问系统公共目录中的文件进行读写操作，可以使用文件picker来获取文件描述符。

本文将针对这两种场景给出具体的实现方案。

## 访问应用沙箱文件

应用沙箱（详见[应用沙箱目录](app-sandbox-directory.md)）是一种以安全防护为目的的隔离机制，避免数据受到恶意路径穿越访问。在这种沙箱的保护机制下，应用可见的目录范围即为“应用沙箱目录”，沙箱中的文件就需要通过沙箱路径去进行访问。Native侧获取沙箱路径的方案有两种：

* 方案一：ArkTS侧获取沙箱路径（详见[获取应用文件路径](application-context-stage.md#获取应用文件路径)）传递给Native侧访问文件。
* 方案二：Native侧直接拼接沙箱路径（详见[应用沙箱路径和真实物理路径的对应关系](app-sandbox-directory.md#应用沙箱路径和真实物理路径的对应关系)）访问文件。

### 方案一：ArkTS侧获取沙箱路径传递给Native侧访问文件

**图 1** ArkTS侧获取沙箱路径传递给Native侧访问文件示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/07NRfPnfSuaZgynf6dpwZA/zh-cn_image_0000002791725542.png?HW-CC-KV=V1&HW-CC-Date=20261119T014704Z&HW-CC-Expire=31536000000&HW-CC-Sign=1F0E57B2D3BACCBED6BC9CE6D9CFE2EE54D57FF1D14DC5FF410BD8669B09C21E)

**实现方案**

这里以访问沙箱文件并写入文本的场景为例，实现方案分为Native侧定义操作文件的方法和ArkTS侧调用该方法两部分。

第一部分：在Native侧定义一个方法，用于接收沙箱路径并将文本写入到文件中。

1. 通过Node-API接口将沙箱路径和要写入文本的内容传递到Native侧。

   ```cpp
   napi_get_value_string_utf8(env, argv[0], pathBuf, sizeof(pathBuf), &pathSize);
   napi_get_value_string_utf8(env, argv[1], contentsBuf, sizeof(contentsBuf), &contentsSize);
   ```
2. 通过指定的路径打开文件。

   ```cpp
   FILE *fp;
   fp = fopen(pathBuf, "w");
   ```
3. 使用C标准库的文件操作函数写入文件。

   ```cpp
   // Write a file using the file operation function of the C standard library.
   fprintf(fp, "%s", contentsBuf);
   ```
4. 完整代码如下所示：

   ```cpp
   // entry/src/main/cpp/FileAccessMethods.cpp
   static napi_value TransferSandboxPath(napi_env env, napi_callback_info info) {
       size_t argc = 2;
       napi_value argv[2] = {nullptr};
       napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
       // Convert the sandbox path and the contents of the text to be written into C-side variables
       // through the Node-API interface.
       size_t pathSize, contentsSize;
       char pathBuf[BUFFER_SIZE], contentsBuf[BUFFER_SIZE];
       napi_get_value_string_utf8(env, argv[0], pathBuf, sizeof(pathBuf), &pathSize);
       napi_get_value_string_utf8(env, argv[1], contentsBuf, sizeof(contentsBuf), &contentsSize);
       // Open the file through the specified path.
       snprintf(pathBuf, sizeof(pathBuf), "%s/TransferSandboxPath.txt", pathBuf);
       FILE *fp;
       fp = fopen(pathBuf, "w");
       if (fp == nullptr) {
           OH_LOG_Print(LOG_APP, LOG_ERROR, DOMAIN, TAG, "Open file error!");
           return nullptr;
       }
       OH_LOG_Print(LOG_APP, LOG_INFO, DOMAIN, TAG, "Open file successfully!");
       // Write a file using the file operation function of the C standard library.
       fprintf(fp, "%s", contentsBuf);
       fclose(fp);
       return nullptr;
   }
   ```
5. 将该C++接口与ArkTS接口进行绑定和映射（详见[Native侧方法的实现](use-napi-process.md#native侧方法的实现)），同时在index.d.ts文件中，提供该接口方法以便于ArkTS侧调用。

   ```ts
   export const transferSandboxPath: (path: string, contents: string) => void;
   ```

第二部分：在Native侧访问沙箱文件写数据的功能实现后，在ArkTS侧调用该方法。

1. 引用Native侧相应的so库。

   ```ts
   import FileAccess from 'libfile_access.so';
   ```
2. 在ArkTS侧获取沙箱路径。

   ```ts
   private sandboxFilesDir: string = this.getUIContext().getHostContext()!.filesDir;
   ```
3. 获取到沙箱路径后，将该路径传递给Native侧，同时传递需要写入的内容。

   ```ts
   FileAccess.transferSandboxPath(this.sandboxFilesDir, content);
   ```

通过上述步骤，实现了在Native侧通过ArkTS侧传递的沙箱路径访问与操作应用沙箱文件的方案。

**效果展示**

**图 2** ArkTS侧传递沙箱路径到Native侧方案效果展示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/Y5vU1oDOQ9q0WixqHEgfEg/zh-cn_image_0000002791565570.png?HW-CC-KV=V1&HW-CC-Date=20261119T014704Z&HW-CC-Expire=31536000000&HW-CC-Sign=1E902BD06E107B1FBACB050261F65DC2E918F7D1BE456A0813D7B66033B66861)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/3LMZXWPjT6i-rSJCv8QW4A/zh-cn_image_0000002820525523.png?HW-CC-KV=V1&HW-CC-Date=20261119T014704Z&HW-CC-Expire=31536000000&HW-CC-Sign=74793CCE3D06D43DD29527CC07164744D542B3431833EB9A989BE8395DC99A9A)

### 方案二：Native侧直接拼接沙箱路径访问文件

**图 3** Native侧直接拼接沙箱路径访问文件示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/1zllWetLTTa0caX6P_Otgg/zh-cn_image_0000002820405523.png?HW-CC-KV=V1&HW-CC-Date=20261119T014704Z&HW-CC-Expire=31536000000&HW-CC-Sign=C3B5DB8C6FFAFE6EB500947E354C69AAC45ACD3ECFB2F360AA898321882C0DB3)

**实现方案**

这里同样以访问沙箱文件并写入文本的场景为例，实现方案分为Native侧定义操作文件的方法和ArkTS侧调用该方法两部分。

第一部分：在Native侧定义一个方法，用于拼接沙箱路径并将文本写入到文件中。

1. 根据实际文件位置拼接沙箱路径（详见[应用沙箱路径和真实物理路径的对应关系](app-sandbox-directory.md#应用沙箱路径和真实物理路径的对应关系)）。

   ```cpp
   char pathBuf[READ_SIZE] = {0};
   strncpy(pathBuf,FILE_PATH,READ_SIZE);
   ```
2. 将要写入文本的内容通过Node-API接口传递到Native侧。

   ```cpp
   napi_get_value_string_utf8(env, argv[0], contentsBuf, sizeof(contentsBuf), &contentsSize);
   ```
3. 通过指定的路径打开文件。

   ```cpp
   // Open the file through the specified path.
   FILE *fp;
   fp = fopen(pathBuf, "w");
   ```
4. 使用C标准库的文件操作函数写入文件。

   ```cpp
   // Write a file using the file operation function of the C standard library.
   fprintf(fp, "%s", contentsBuf);
   ```
5. 完整代码如下所示：

   ```cpp
   static napi_value SplicePath(napi_env env, napi_callback_info info) {
       size_t argc = 1;
       napi_value argv[1] = {nullptr};
       napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
       // Splice the sandbox path according to the actual file location.
       size_t contentsSize;
       char pathBuf[READ_SIZE] = {0};
       strncpy(pathBuf,FILE_PATH,READ_SIZE);
       // Convert the contents of the text to be written into C-side variables through the Node-API interface.
       char contentsBuf[BUFFER_SIZE];
       napi_get_value_string_utf8(env, argv[0], contentsBuf, sizeof(contentsBuf), &contentsSize);
       // Open the file through the specified path.
       FILE *fp;
       fp = fopen(pathBuf, "w");
       if (fp == nullptr) {
           OH_LOG_Print(LOG_APP, LOG_ERROR, DOMAIN, TAG, "Open file error!");
           return nullptr;
       }
       OH_LOG_Print(LOG_APP, LOG_INFO, DOMAIN, TAG, "Open file successfully!");
       // Write a file using the file operation function of the C standard library.
       fprintf(fp, "%s", contentsBuf);
       fclose(fp);
       return nullptr;
   }
   ```
6. 将该C++接口与ArkTS接口进行绑定和映射（详见[Native侧方法的实现](use-napi-process.md#native侧方法的实现)），同时在index.d.ts文件中，提供该接口方法。

   ```ts
   export const splicePath: (contents: string) => void;
   ```

第二部分：Native侧访问沙箱文件写数据的功能实现后，在ArkTS侧调用该方法。

1. 引用Native侧相应的so库。

   ```ts
   import FileAccess from 'libfile_access.so';
   ```
2. 在ArkTS侧调用该接口实现文件写入的操作。

   ```ts
   FileAccess.splicePath(content);
   ```

通过上述步骤，实现了在Native侧通过拼接沙箱路径访问与操作应用沙箱文件的方案。

**效果展示**

**图 4** Native侧拼接沙箱路径方案效果展示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/p-CxolbxRKq_0LemihZR6g/zh-cn_image_0000002791725544.png?HW-CC-KV=V1&HW-CC-Date=20261119T014704Z&HW-CC-Expire=31536000000&HW-CC-Sign=58BD43875476F629C9977727E68F1DB000EC46B5FB27A365CF8CCF947AF4250D)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/klS_yo_ORw-IgVK5kw3O6g/zh-cn_image_0000002791565572.png?HW-CC-KV=V1&HW-CC-Date=20261119T014704Z&HW-CC-Expire=31536000000&HW-CC-Sign=379CF723D92A217F8F6D9BAD8795D471EB9FC6817A68517696C765CD0FF42E60)

## 访问公共目录文件

系统公共目录下储存的是用户文件（详见[用户文件概述](user-file-overview.md)），应用对用户文件的操作需要提前获取用户授权，或由用户操作完成。可以通过系统预置的文件选择器（FilePicker）（详见[选择文档类文件](select-user-file.md#选择文档类文件)）实现该能力，目前主要有创建文件、写入和读取三类操作，创建文件（详见[save](../harmonyos-references/js-apis-file-picker.md#save))可以直接使用picker，针对Native侧，有如下两种场景：

* 场景一：写数据到公共目录文件。
* 场景二：从公共目录文件中读取数据。

### 场景一：写数据到公共目录文件

**场景描述**

ArkTS侧通过文件picker在公共目录下创建文件，并传递文件描述符到Native侧，Native侧通过文件描述符打开文件并将数据写入到文件中。

**图 7** Native侧写入公共目录文件场景示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/LHvQsDtiSEuXnXoR5f4sGA/zh-cn_image_0000002820525525.png?HW-CC-KV=V1&HW-CC-Date=20261119T014704Z&HW-CC-Expire=31536000000&HW-CC-Sign=95F9F59514C55749D2304888AE8ACC1AAC7512E303EA1E37EEC4F45477AF56D8)

**实现方案**

实现方案分为Native侧定义操作文件的方法和ArkTS侧调用该方法两部分。

第一部分：在Native侧定义一个方法，用于接收文件描述符并将数据写入到文件中，注意使用文件描述符操作文件需要引用头文件unistd.h。

1. 将传入的文件描述符和要写入文件的内容通过Node-API接口传递到Native侧。

   ```cpp
   // Convert the incoming file descriptor and the contents to be written into the file into C-side variables.
   napi_get_value_uint32(env, argv[0], &fd);
   napi_get_value_string_utf8(env, argv[1], contentsBuf, sizeof(contentsBuf), &contentsSize);
   ```
2. 使用C标准库的文件操作函数写入文件。

   ```cpp
   // Write a file using the file operation function of the C standard library.
   size_t buffSize = write(fd, contentsBuf, contentsSize);
   ```
3. 根据write函数的返回值判断操作是否成功。

   ```
   std::string res;
   // According to the return value of the write function, judge whether
   // the operation returns the result successfully.
   napi_value contents;
   if (buffSize == -1) {
       res = "Write File Failed!";
       OH_LOG_Print(LOG_APP, LOG_ERROR, DOMAIN, TAG, "%s", res.c_str());
   } else {
       res = "Write File Successfully!!!";
       OH_LOG_Print(LOG_APP, LOG_INFO, DOMAIN, TAG, "%s", res.c_str());
   }
   napi_create_string_utf8(env, res.c_str(), sizeof(res), &contents);
   return contents;
   ```
4. 完整代码如下所示：

   ```
   static napi_value WriteFileUsingPickerFd(napi_env env, napi_callback_info info) {
       size_t argc = 2;
       napi_value argv[2] = {nullptr};
       napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);

       unsigned int fd = -1;
       size_t contentsSize;
       char contentsBuf[BUFFER_SIZE];
       // Convert the incoming file descriptor and the contents to be written into the file into C-side variables.
       napi_get_value_uint32(env, argv[0], &fd);
       napi_get_value_string_utf8(env, argv[1], contentsBuf, sizeof(contentsBuf), &contentsSize);
       ftruncate(fd, 0);
       // Write a file using the file operation function of the C standard library.
       size_t buffSize = write(fd, contentsBuf, contentsSize);
       std::string res;
       // According to the return value of the write function, judge whether
       // the operation returns the result successfully.
       napi_value contents;
       if (buffSize == -1) {
           res = "Write File Failed!";
           OH_LOG_Print(LOG_APP, LOG_ERROR, DOMAIN, TAG, "%s", res.c_str());
       } else {
           res = "Write File Successfully!!!";
           OH_LOG_Print(LOG_APP, LOG_INFO, DOMAIN, TAG, "%s", res.c_str());
       }
       napi_create_string_utf8(env, res.c_str(), sizeof(res), &contents);
       return contents;
   }
   ```
5. 将该C++接口与ArkTS接口进行绑定和映射（详见[Native侧方法的实现](use-napi-process.md#native侧方法的实现)），同时在index.d.ts文件中，提供该接口方法。

   ```ts
   export const writeFileUsingPickerFd: (fd: number, contents: string) => string;
   ```

第二部分：Native侧访问公共目录文件写数据的功能实现后，在ArkTS侧调用该方法。

1. 引用Native侧相应的so库。

   ```ts
   import FileAccess from 'libfile_access.so';
   ```
2. 在ArkTS侧拉起picker选择文件并将文件描述符传入Native接口中。

   ```typescript
   async function WriteFileByPicker(contents: string): Promise<string> {
     // Configure picker Selection Information
     const documentSelectOptions = new picker.DocumentSelectOptions();
     documentSelectOptions.maxSelectNumber = 1;
     documentSelectOptions.fileSuffixFilters = ['.txt'];

     let uris: Array<string> = [];
     const documentViewPicker = new picker.DocumentViewPicker();
     // Pull up the picker selection file
     return await documentViewPicker.select(documentSelectOptions).then((documentSelectResult: Array<string>) => {
       uris = documentSelectResult;
       let uri: string = uris[0];
       let path: string = new fileUri.FileUri(uri).path;
       Logger.info(`Open The File path is [${uri}]`);
       let file = fileIo.openSync(path, fileIo.OpenMode.WRITE_ONLY);
       // Call the native method to write a file
       let res = FileAccess.writeFileUsingPickerFd(file.fd, contents);
       fileIo.closeSync(file.fd);
       return res;
     }).catch((error: BusinessError) => {
       Logger.error(`Open The file failed, error code is [${error.code}], error message is [${error.message}]`);
       return 'Write Failed by Picker';
     })
   }
   ```

通过上述步骤，实现了在Native侧通过ArkTS侧picker传递的文件资源描述符访问公共目录文件并写入内容的方案。

**效果展示**

**图 8** Native侧写公共目录文件场景方案效果展示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/410k1elyQpuKHiv1nK1LKA/zh-cn_image_0000002820405525.png?HW-CC-KV=V1&HW-CC-Date=20261119T014704Z&HW-CC-Expire=31536000000&HW-CC-Sign=007087E7E64F089EF7CE986FEFE7E00BABA947842DA3B7F8163F8ADF65457695)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/xeSgzdQER8ebBcrliC2Csw/zh-cn_image_0000002791725546.png?HW-CC-KV=V1&HW-CC-Date=20261119T014704Z&HW-CC-Expire=31536000000&HW-CC-Sign=B787B3C2FA1E78DF44A5116D1D626876C0CA4B17DA7BB65365EE0F1FB342F4F0)

### 场景二：从公共目录文件中读取数据

**场景描述**

ArkTS侧通过文件picker选择文件，并传递文件描述符到Native侧，Native侧通过文件描述符打开文件并读取文件数据。

**图 9** Native侧读取公共目录文件场景示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/_0ZQ9FBCRyKAaj3oOteYvw/zh-cn_image_0000002791565574.png?HW-CC-KV=V1&HW-CC-Date=20261119T014704Z&HW-CC-Expire=31536000000&HW-CC-Sign=6EF2F86ECE76E5CD82217CE2BFA152C907629ECE8B220B385F302AD78136ECC9)

**实现方案**

实现方案分为Native侧定义操作文件的方法和ArkTS侧调用该方法两部分。

第一部分：在Native侧定义一个方法，用于接收文件描述符并从文件中读取数据，注意使用文件描述符操作文件需要引用头文件unistd.h。

1. 将传入的文件描述符通过Node-API接口传递到Native侧。

   ```cpp
   // Convert the incoming file descriptor into a C-side variable.
   napi_get_value_uint32(env, argv[0], &fd);
   ```
2. 使用C标准库的文件操作函数读取文件。

   ```cpp
   // Use the file operation function of the C standard library to read the file.
   char buff[READ_SIZE];
   size_t buffSize = read(fd, buff, sizeof(buff));
   ```
3. 判断读取是否成功并返回文件内容。

   ```cpp
   // Judge whether the reading is successful or not and return the file content.
   napi_value contents;
   if (buffSize == -1) {
       OH_LOG_Print(LOG_APP, LOG_ERROR, DOMAIN, TAG, "Read File Failed!!!");
   } else {
       OH_LOG_Print(LOG_APP, LOG_INFO, DOMAIN, TAG, "Read File Successfully!!!");
       napi_create_string_utf8(env, buff, buffSize, &contents);
   }
   return contents;
   ```
4. 完整代码如下所示：

   ```cpp
   // entry/src/main/cpp/FileAccessMethods.cpp
   static napi_value ReadFileUsingPickerFd(napi_env env, napi_callback_info info) {
       size_t argc = 1;
       napi_value argv[1] = {nullptr};
       napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);

       unsigned int fd = -1;
       // Convert the incoming file descriptor into a C-side variable.
       napi_get_value_uint32(env, argv[0], &fd);
       // Use the file operation function of the C standard library to read the file.
       char buff[READ_SIZE];
       size_t buffSize = read(fd, buff, sizeof(buff));
       // Judge whether the reading is successful or not and return the file content.
       napi_value contents;
       if (buffSize == -1) {
           OH_LOG_Print(LOG_APP, LOG_ERROR, DOMAIN, TAG, "Read File Failed!!!");
       } else {
           OH_LOG_Print(LOG_APP, LOG_INFO, DOMAIN, TAG, "Read File Successfully!!!");
           napi_create_string_utf8(env, buff, buffSize, &contents);
       }
       return contents;
   }
   ```
5. 将该C++接口与ArkTS接口进行绑定和映射（详见[Native侧方法的实现](use-napi-process.md#native侧方法的实现)），同时在index.d.ts文件中，提供该接口方法。

   ```ts
   export const readFileUsingPickerFd: (fd: number) => string;
   ```

第二部分：Native侧访问公共目录文件读数据的功能实现后，在ArkTS侧调用该方法。

1. 引用Native侧相应的so库。

   ```ts
   import FileAccess from 'libfile_access.so';
   ```
2. 在ArkTS侧拉起picker选择文件并将文件描述符传入Native接口中。

   ```typescript
   async function ReadFileByPicker(): Promise<string> {
     // Configure picker Selection Information
     const documentSelectOptions = new picker.DocumentSelectOptions();
     documentSelectOptions.maxSelectNumber = 1;
     documentSelectOptions.fileSuffixFilters = ['.txt'];
     // Pull up the picker selection file
     let uris: Array<string> = [];
     const documentViewPicker = new picker.DocumentViewPicker();
     return await documentViewPicker.select(documentSelectOptions).then((documentSelectResult: Array<string>) => {
       uris = documentSelectResult;
       let uri: string = uris[0];
       let path: string = new fileUri.FileUri(uri).path;
       Logger.info(`The Opened File path is [${uri}]`);
       let file = fileIo.openSync(path, fileIo.OpenMode.READ_ONLY);
       // Call the native method to read the file.
       let res = FileAccess.readFileUsingPickerFd(file.fd);
       fileIo.closeSync(file.fd);
       return res;
     }).catch((error: BusinessError) => {
       Logger.error(`Open The file failed, error code is [${error.code}], error message is [${error.message}]`);
       return 'Read Failed by Picker!';
     })
   }
   ```

通过上述步骤，实现了在Native侧通过ArkTS侧picker传递的文件资源描述符访问公共目录文件并读取内容的方案。

**效果展示**

**图 10** Native侧读公共目录文件场景方案效果展示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/bcY3NQZvSnaGxLQG-kSSnw/zh-cn_image_0000002820525527.png?HW-CC-KV=V1&HW-CC-Date=20261119T014704Z&HW-CC-Expire=31536000000&HW-CC-Sign=9518F3EF4DFF8AED1BA02875F194916C6674CAEA41E40E5E875F42A9E6530240)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/O1HlCGZrR7-YHSU7wuqpzA/zh-cn_image_0000002820405527.png?HW-CC-KV=V1&HW-CC-Date=20261119T014704Z&HW-CC-Expire=31536000000&HW-CC-Sign=91974C8CA137C18262B499FD0F1040A334B871983FA09309E81AFA5342EEA367)

## 示例代码

[实现Native侧文件访问](https://gitcode.com/harmonyos_samples/NativeFileAccess)
