---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/rawfile-guidelines
title: Rawfile开发指导
breadcrumb: 指南 > NDK开发 > 代码开发 > 资源管理 > Rawfile开发指导
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:48+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:179129b1ca934c9dcb4e57fa045f78a706bf3edcd79087e54983a52392f5cdb6
---

## 场景介绍

开发者可以通过本指导了解在HarmonyOS应用中，如何使用Native Rawfile接口操作Rawfile目录和文件。功能包括文件列表遍历、文件打开、搜索、读取和关闭Rawfile。

64后缀相关接口属于新增接口，新接口支持打开更大的rawfile文件(超过2G建议使用)，具体请参考：[Rawfile接口介绍](../harmonyos-references/capi-rawfile.md)。64相关的开发步骤和非64一致，将非64接口替换为64接口即可，例如：OH\_ResourceManager\_OpenRawFile替换为OH\_ResourceManager\_OpenRawFile64。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| NativeResourceManager \*OH\_ResourceManager\_InitNativeResourceManager(napi\_env env, napi\_value jsResMgr) | 初始化native resource manager。 |
| RawDir \*OH\_ResourceManager\_OpenRawDir(const NativeResourceManager \*mgr, const char \*dirName) | 打开指定rawfile目录。 |
| int OH\_ResourceManager\_GetRawFileCount(RawDir \*rawDir) | 获取指定rawfile目录下的rawfile文件数量。 |
| const char \*OH\_ResourceManager\_GetRawFileName(RawDir \*rawDir, int index) | 获取rawfile名字。 |
| RawFile \*OH\_ResourceManager\_OpenRawFile(const NativeResourceManager \*mgr, const char \*fileName) | 打开指定rawfile文件。 |
| long OH\_ResourceManager\_GetRawFileSize(RawFile \*rawFile) | 获取rawfile文件大小。 |
| int OH\_ResourceManager\_ReadRawFile(const RawFile \*rawFile, void \*buf, size\_t length) | 读取rawfile文件内容。 |
| void OH\_ResourceManager\_CloseRawFile(RawFile \*rawFile) | 释放rawfile文件相关资源。 |
| void OH\_ResourceManager\_CloseRawDir(RawDir \*rawDir) | 释放rawfile目录相关资源。 |
| bool OH\_ResourceManager\_GetRawFileDescriptor(const RawFile \*rawFile, RawFileDescriptor &descriptor) | 获取rawfile的fd。 |
| void OH\_ResourceManager\_ReleaseNativeResourceManager(NativeResourceManager \*resMgr) | 释放native resource manager相关资源。 |
| bool OH\_ResourceManager\_IsRawDir(const NativeResourceManager \*mgr, const char \*path) | 判断路径是否是rawfile下的目录。 |

详细的接口说明请参考[rawfile](../harmonyos-references/capi-rawfile.md)。

## 开发步骤

以ArkTS侧获取rawfile文件列表、获取rawfile文件内容、获取rawfile描述符（fd, offset, length）、判断是否是rawfile下的目录四种调用方式为例。

**1. 创建工程**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/8wyXrNlETqmsydDzi3b_IQ/zh-cn_image_0000002712405670.png)

**2. 添加依赖**

创建完成后，DevEco Studio会在工程中生成cpp目录，目录下有libentry/index.d.ts、hello.cpp、CMakeLists.txt等文件。

1. 打开src/main/cpp/CMakeLists.txt，在target\_link\_libraries依赖中添加rawfile依赖librawfile.z.so以及日志依赖libhilog\_ndk.z.so。

   ```
   target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so librawfile.z.so)
   ```
2. 打开src/main/cpp/types/libentry/index.d.ts文件，在此文件中声明ArkTS侧接口getFileList、getRawFileContent、getRawFileDescriptor、isRawDir。

   ```typescript
   import { resourceManager } from '@kit.LocalizationKit';
   export const getFileList: (resMgr: resourceManager.ResourceManager, path: string) => Array<String>;
   export const getRawFileContent: (resMgr: resourceManager.ResourceManager, path: string) => Uint8Array;
   export const getRawFileDescriptor: (resMgr: resourceManager.ResourceManager, path: string) => resourceManager.RawFileDescriptor;
   export const isRawDir: (resMgr: resourceManager.ResourceManager, path: string) => boolean;
   ```

**3. 修改源文件**

1. 打开src/main/cpp/hello.cpp文件，在Init方法中添加ArkTS接口与C++接口的映射。ArkTS侧接口getFileList、getRawFileContent、getRawFileDescriptor、isRawDir，映射C++接口分别为GetFileList、GetRawFileContent、GetRawFileDescriptor、IsRawDir。

   ```
   EXTERN_C_START
   static napi_value Init(napi_env env, napi_value exports)
   {
       napi_property_descriptor desc[] = {
           { "getFileList", nullptr, GetFileList, nullptr, nullptr, nullptr, napi_default, nullptr },
           { "getRawFileContent", nullptr, GetRawFileContent, nullptr, nullptr, nullptr, napi_default, nullptr },
           { "getRawFileDescriptor", nullptr, GetRawFileDescriptor, nullptr, nullptr, nullptr, napi_default, nullptr },
           { "isRawDir", nullptr, IsRawDir, nullptr, nullptr, nullptr, napi_default, nullptr }
       };

       napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
       return exports;
   }
   EXTERN_C_END
   ```
2. 在src/main/cpp/目录下创建hello.h文件，在hello.h文件中增加对应的四个方法，如下所示：

   ```c
   #ifndef RAWFILE_HELLO_H
   #define RAWFILE_HELLO_H

   #include <js_native_api.h>
   #include <js_native_api_types.h>
   #include <string>
   #include <vector>
   #include <cstdlib>
   #include "napi/native_api.h"

   napi_value GetFileList(napi_env env, napi_callback_info info);
   napi_value GetRawFileContent(napi_env env, napi_callback_info info);
   napi_value GetRawFileDescriptor(napi_env env, napi_callback_info info);
   napi_value IsRawDir(napi_env env, napi_callback_info info);

   #endif // RAWFILE_HELLO_H
   ```
3. 在hello.cpp文件中实现上述四个方法。通过env和info获取Js的资源管理对象，并转换为Native的资源管理对象，即可调用Native资源管理对象的接口，示例代码如下：

   导入头文件

   ```
   #include "hello.h"
   #include "rawfile/raw_file_manager.h"
   #include "rawfile/raw_file.h"
   #include "rawfile/raw_dir.h"
   #include "hilog/log.h"
   ```

   声明hilog日志打印的DOMAIN和TAG常量

   ```
   const int GLOBAL_RESMGR = 0xFF00;
   const char *TAG = "[Sample_rawfile]";
   ```

   示例：

   ```
   // 示例一：获取rawfile文件列表 GetFileList
   napi_value GetFileList(napi_env env, napi_callback_info info)
   {
       OH_LOG_Print(LOG_APP, LOG_INFO, GLOBAL_RESMGR, TAG, "NDKTest GetFileList Begin");
       size_t argc = 2;
       napi_value argv[2] = { nullptr };
       // 获取参数信息
       napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);

       // argv[0]即为函数第一个参数Js资源对象，OH_ResourceManager_InitNativeResourceManager转为Native对象
       NativeResourceManager *mNativeResMgr = OH_ResourceManager_InitNativeResourceManager(env, argv[0]);

       // 获取函数argv[1]，此为rawfile相对路径
       size_t strSize;
       char strBuf[256];
       napi_get_value_string_utf8(env, argv[1], strBuf, sizeof(strBuf), &strSize);
       std::string dirName(strBuf, strSize);

       // 获取对应的rawDir指针对象
       RawDir* rawDir = OH_ResourceManager_OpenRawDir(mNativeResMgr, dirName.c_str());

       // 获取rawDir下文件及文件夹数量
       int count = OH_ResourceManager_GetRawFileCount(rawDir);

       // 遍历获取文件名称，并保存
       std::vector<std::string> tempArray;
       for (int i = 0; i < count; i++) {
           std::string filename = OH_ResourceManager_GetRawFileName(rawDir, i);
           tempArray.emplace_back(filename);
       }

       // 转为js数组
       napi_value fileList;
       napi_create_array(env, &fileList);
       for (size_t i = 0; i < tempArray.size(); i++) {
           napi_value jsString;
           napi_create_string_utf8(env, tempArray[i].c_str(), NAPI_AUTO_LENGTH, &jsString);
           napi_set_element(env, fileList, i, jsString);
       }

       // 关闭打开的指针对象
       OH_ResourceManager_CloseRawDir(rawDir);
       OH_ResourceManager_ReleaseNativeResourceManager(mNativeResMgr);
       return fileList;
   }
   ```

   ```
   // 示例二：获取rawfile文件内容 GetRawFileContent
   napi_value CreateJsArrayValue(napi_env env, std::unique_ptr<uint8_t[]> &data, long length)
   {
       // 创建js外部ArrayBuffer
       napi_value buffer;
       napi_status status = napi_create_external_arraybuffer(env, data.get(), length,
           [](napi_env env, void *data, void *hint) {
               delete[] static_cast<char*>(data);
           }, nullptr, &buffer);
       // 检测ArrayBuffer是否创建成功
       if (status != napi_ok) {
           OH_LOG_Print(LOG_APP, LOG_ERROR, GLOBAL_RESMGR, TAG, "Failed to create external array buffer");
           return nullptr;
       }
       // 创建js TypedArray  将ArrayBuffer绑定到TypedArray
       napi_value result = nullptr;
       status = napi_create_typedarray(env, napi_uint8_array, length, buffer, 0, &result);
       if (status != napi_ok) {
           OH_LOG_Print(LOG_APP, LOG_ERROR, GLOBAL_RESMGR, TAG, "Failed to create media typed array");
           return nullptr;
       }
       data.release();
       return result;
   }

   napi_value GetRawFileContent(napi_env env, napi_callback_info info)
   {
       OH_LOG_Print(LOG_APP, LOG_INFO, GLOBAL_RESMGR, TAG, "GetFileContent Begin");
       size_t argc = 2;
       napi_value argv[2] = { nullptr };
       // 获取参数信息
       napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);

       // argv[0]即为函数第一个参数Js资源对象，OH_ResourceManager_InitNativeResourceManager转为Native对象
       NativeResourceManager *mNativeResMgr = OH_ResourceManager_InitNativeResourceManager(env, argv[0]);
       size_t strSize;
       char strBuf[256];
       napi_get_value_string_utf8(env, argv[1], strBuf, sizeof(strBuf), &strSize);
       std::string filename(strBuf, strSize);

       // 获取rawfile指针对象
       RawFile *rawFile = OH_ResourceManager_OpenRawFile(mNativeResMgr, filename.c_str());
       if (rawFile != nullptr) {
           OH_LOG_Print(LOG_APP, LOG_INFO, GLOBAL_RESMGR, TAG, "OH_ResourceManager_OpenRawFile success");
       }
       // 获取rawfile大小并申请内存
       long len = OH_ResourceManager_GetRawFileSize(rawFile);
       std::unique_ptr<uint8_t[]> data = std::make_unique<uint8_t[]>(len);

       // 一次性读取rawfile全部内容
       int res = OH_ResourceManager_ReadRawFile(rawFile, data.get(), len);

       // 关闭打开的指针对象
       OH_ResourceManager_CloseRawFile(rawFile);
       OH_ResourceManager_ReleaseNativeResourceManager(mNativeResMgr);
       // 转为js对象
       return CreateJsArrayValue(env, data, len);
   }
   ```

   ```
   // 示例三：获取rawfile文件描述符 GetRawFileDescriptor
   // 定义一个函数，将RawFileDescriptor转为js对象
   napi_value createJsFileDescriptor(napi_env env, RawFileDescriptor& descriptor)
   {
       // 创建js对象
       napi_value result;
       napi_status status = napi_create_object(env, &result);
       if (status != napi_ok) {
           return result;
       }

       // 将文件描述符fd存入到result对象中
       napi_value fd;
       status = napi_create_int32(env, descriptor.fd, &fd);
       if (status != napi_ok) {
           return result;
       }
       status = napi_set_named_property(env, result, "fd", fd);
       if (status != napi_ok) {
           return result;
       }

       // 将文件偏移量offset存入到result对象中
       napi_value offset;
       status = napi_create_int64(env, descriptor.start, &offset);
       if (status != napi_ok) {
           return result;
       }
       status = napi_set_named_property(env, result, "offset", offset);
       if (status != napi_ok) {
           return result;
       }

       // 将文件长度length存入到result对象中
       napi_value length;
       status = napi_create_int64(env, descriptor.length, &length);
       if (status != napi_ok) {
           return result;
       }
       status = napi_set_named_property(env, result, "length", length);
       if (status != napi_ok) {
           return result;
       }
       return result;
   }

   napi_value GetRawFileDescriptor(napi_env env, napi_callback_info info)
   {
       OH_LOG_Print(LOG_APP, LOG_INFO, GLOBAL_RESMGR, TAG, "NDKTest GetRawFileDescriptor Begin");
       size_t argc = 2;
       napi_value argv[2] = { nullptr };
       // 获取参数信息
       napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);

       // argv[0]即为函数第一个参数Js资源对象，OH_ResourceManager_InitNativeResourceManager转为Native对象
       NativeResourceManager *mNativeResMgr = OH_ResourceManager_InitNativeResourceManager(env, argv[0]);
       size_t strSize;
       char strBuf[256];
       napi_get_value_string_utf8(env, argv[1], strBuf, sizeof(strBuf), &strSize);
       std::string filename(strBuf, strSize);
       // 获取rawfile指针对象
       RawFile *rawFile = OH_ResourceManager_OpenRawFile(mNativeResMgr, filename.c_str());
       if (rawFile != nullptr) {
           OH_LOG_Print(LOG_APP, LOG_INFO, GLOBAL_RESMGR, TAG, "OH_ResourceManager_OpenRawFile success");
       }
       // 获取rawfile的描述符RawFileDescriptor {fd, offset, length}
       RawFileDescriptor descriptor;
       OH_ResourceManager_GetRawFileDescriptor(rawFile, descriptor);
       // 关闭打开的指针对象
       OH_ResourceManager_CloseRawFile(rawFile);
       OH_ResourceManager_ReleaseNativeResourceManager(mNativeResMgr);
       // 转为js对象
       return createJsFileDescriptor(env, descriptor);
   }
   ```

   ```
   // 示例四：判断路径是否是rawfile下的目录 IsRawDir
   napi_value CreateJsBool(napi_env env, bool &bValue)
   {
       napi_value jsValue = nullptr;
       if (napi_get_boolean(env, bValue, &jsValue) != napi_ok) {
           return nullptr;
       }
       return jsValue;
   }

   napi_value IsRawDir(napi_env env, napi_callback_info info)
   {
       OH_LOG_Print(LOG_APP, LOG_INFO, GLOBAL_RESMGR, TAG, "NDKTest IsRawDir Begin");
       size_t argc = 2;
       napi_value argv[2] = { nullptr };
       // 获取参数信息
       napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);

       // argv[0]即为函数第一个参数Js资源对象，OH_ResourceManager_InitNativeResourceManager转为Native对象
       NativeResourceManager *mNativeResMgr = OH_ResourceManager_InitNativeResourceManager(env, argv[0]);

       napi_valuetype fileNameType;
       napi_typeof(env, argv[1], &fileNameType);
       if (fileNameType == napi_undefined || fileNameType == napi_null) {
           OH_LOG_Print(LOG_APP, LOG_ERROR, GLOBAL_RESMGR, TAG, "NDKTest file name is null");
           bool temp = false;
           return CreateJsBool(env, temp);
       }
       size_t strSize;
       char strBuf[256];
       napi_get_value_string_utf8(env, argv[1], strBuf, sizeof(strBuf), &strSize);
       std::string filename(strBuf, strSize);
       // 判断是否是rawfile下的目录
       bool result = OH_ResourceManager_IsRawDir(mNativeResMgr, filename.c_str());
       OH_ResourceManager_ReleaseNativeResourceManager(mNativeResMgr);
       return CreateJsBool(env, result);
   }
   ```

**4. ArkTS侧调用**

1. 打开src\main\ets\pages\index.ets, 导入"libentry.so"。
2. 资源获取包括获取本应用包资源、应用内跨包资源、跨应用包资源。

   通过context.resourceManager获取本应用包resourceManager对象。

   通过context.createModuleContext().resourceManager获取应用内跨包resourceManager对象。

   Context的更多使用信息请参考[应用上下文Context](application-context-stage.md)。
3. 调用src/main/cpp/types/libentry/index.d.ts中声明的接口，如getFileList，传入js的资源管理对象以及rawfile文件夹的相对路径。

   获取本应用包资源resourceManager对象的示例如下：

   ```typescript
   import { util } from '@kit.ArkTS';
   import { resourceManager } from '@kit.LocalizationKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import testNapi from 'libentry.so'; // 导入so

   const DOMAIN = 0x0000;
   const TAG = '[Sample_rawfile]';

   @Entry
   @Component
   struct Index {
     @State message: string = 'Hello World';
     private resMgr = this.getUIContext().getHostContext()?.resourceManager; // 获取本应用包的资源对象
     @State rawfileListMsg: string = 'FileList = ';
     @State retMsg: string = 'isRawDir = ';
     @State rawfileContentMsg: string = 'RawFileContent = ';
     @State rawfileDescriptorMsg: string = 'RawFileDescriptor.length = ';

     build() {
       Row() {
         Column() {
           Text(this.message)
             .id('hello_world')
             .fontSize(30)
             .fontWeight(FontWeight.Bold)
             .onClick(async () => {
               // 传入资源管理对象，以及访问的rawfile文件夹名称
               let rawFileList: Array<String> = testNapi.getFileList(this.resMgr, '');
               this.rawfileListMsg = 'FileList = ' + rawFileList;
               hilog.info(DOMAIN, TAG, this.rawfileListMsg);

               // 'sub_rawfile'仅作示例，请替换为实际使用的资源
               let ret: boolean = testNapi.isRawDir(this.resMgr, 'sub_rawfile');
               this.retMsg = 'isRawDir = ' + ret;
               hilog.info(DOMAIN, TAG, this.retMsg);

               // 传入资源管理对象，以及访问的rawfile文件夹名称
               // 'rawfile1.txt'仅作示例，请替换为实际使用的资源
               let rawfileArray: Uint8Array = testNapi.getRawFileContent(this.resMgr, 'rawfile1.txt');
               // 将Uint8Array转为字符串
               let textDecoder: util.TextDecoder = new util.TextDecoder();
               let rawfileContent: string = textDecoder.decodeToString(rawfileArray);
               this.rawfileContentMsg = 'RawFileContent = ' + rawfileContent;
               hilog.info(DOMAIN, TAG, this.rawfileContentMsg);

               // 传入资源管理对象，以及访问的rawfile文件名称
               // 'rawfile1.txt'仅作示例，请替换为实际使用的资源
               let rawfileDescriptor: resourceManager.RawFileDescriptor =
                 testNapi.getRawFileDescriptor(this.resMgr, 'rawfile1.txt');
               this.rawfileDescriptorMsg = 'RawFileDescriptor.length = ' + rawfileDescriptor.length;
               hilog.info(DOMAIN, TAG, this.rawfileDescriptorMsg);
             })
           Text(this.rawfileListMsg).id('get_file_list').fontSize(30);
           Text(this.retMsg).id('is_raw_dir').fontSize(30);
           Text(this.rawfileContentMsg).id('get_raw_file_content').fontSize(30);
           Text(this.rawfileDescriptorMsg).id('get_raw_file_descriptor').fontSize(30);
         }
         .width('100%')
       }
       .height('100%')
     }
   }
   ```
