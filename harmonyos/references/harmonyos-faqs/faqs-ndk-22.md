---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-22
title: 如何在Native侧访问应用包内Rawfile资源
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何在Native侧访问应用包内Rawfile资源
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7e16632821226f6cf9e41fdbdd63b70138fe3966e35336972007981dd772eeae
---

**解决措施**

使用Native Rawfile接口操作Rawfile目录和文件，可以访问应用包内的资源。

参考以下代码。

1. 在src/main/cpp/CMakeLists.txt文件中，添加依赖资源librawfile.z.so。

   target\_link\_libraries(nativeaccessres PUBLIC libace\_napi.z.so libhilog\_ndk.z.so librawfile.z.so)
2. 在index.d.ts文件中声明getRawFileContent。

   ```ts
   import { resourceManager } from "@kit.LocalizationKit";
   export const getRawFileContent: (resMgr: resourceManager.ResourceManager, path: string) => Uint8Array;
   ```
3. 在napi\_init.cpp文件中实现功能代码。

   ```cpp
   #include <memory>
   #include "string"
   #include "napi/native_api.h"
   #include <rawfile/raw_file.h>
   #include <rawfile/raw_file_manager.h>
   #include "hilog/log.h"

   const int GLOBAL_RESMGR = 0xFF00;
   const char *TAG = "[Sample_rawfile]";

   namespace {
       napi_value CreateJsArrayValue(napi_env env, std::unique_ptr<uint8_t[]> &data, long length)
       {
           napi_value buffer;
           napi_status status = napi_create_external_arraybuffer(
               env, data.get(), length,
               [](napi_env env, void *data, void *hint) {
                   delete[] static_cast<char *>(data);
               },
               nullptr, &buffer);
           if (status != napi_ok) {
               OH_LOG_Print(LOG_APP, LOG_ERROR, GLOBAL_RESMGR, TAG, "Failed to create external array buffer");
               return nullptr;
           }
           napi_value result = nullptr;
           status = napi_create_typedarray(env, napi_uint8_array, length, buffer, 0, &result);
           if (status != napi_ok) {
               OH_LOG_Print(LOG_APP, LOG_ERROR, GLOBAL_RESMGR, TAG, "Failed to create media typed array");
               return nullptr;
           }
           data.release();
           return result;
       }
   }

   static napi_value GetRawFileContent(napi_env env, napi_callback_info info)
   {
       OH_LOG_Print(LOG_APP, LOG_ERROR, GLOBAL_RESMGR, TAG, "GetFileContent Begin");
       size_t requireArgc = 3;
       size_t argc = 2;
       napi_value argv[2] = { nullptr };
       // Obtain parameter information
       napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);

       // Argv [0] is the first parameter of the function, Js resource object, and OH_ ResourceManagerial is converted to a Native object.
       NativeResourceManager *mNativeResMgr = OH_ResourceManager_InitNativeResourceManager(env, argv[0]);
       size_t strSize;
       char strBuf[256];
       napi_get_value_string_utf8(env, argv[1], strBuf, sizeof(strBuf), &strSize);
       std::string filename(strBuf, strSize);

       // Get rawfile pointer object
       RawFile *rawFile = OH_ResourceManager_OpenRawFile(mNativeResMgr, filename.c_str());
       if (rawFile != nullptr) {
           OH_LOG_Print(LOG_APP, LOG_ERROR, GLOBAL_RESMGR, TAG, "OH_ResourceManager_OpenRawFile success");
       }
       // Get rawfile size and request memory
       long len = OH_ResourceManager_GetRawFileSize(rawFile);
       std::unique_ptr<uint8_t[]> data= std::make_unique<uint8_t[]>(len);

       // Read all contents of rawfile at once
       int res = OH_ResourceManager_ReadRawFile(rawFile, data.get(), len);

       // Close open pointer objects
       OH_ResourceManager_CloseRawFile(rawFile);
       OH_ResourceManager_ReleaseNativeResourceManager(mNativeResMgr);
       // Convert to JS object
       return CreateJsArrayValue(env, data, len);
   }
   ```
4. 在ArkTS侧调用时，需要传入资源对象。

   ```ts
   import testNapi from 'libnativeaccessres.so'  // Import so

   @Entry
   @Component
   struct Index {
     @State message: string = 'Native Access Resource';
     private resMgr = this.getUIContext().getHostContext()!.resourceManager;  // Retrieve the resource objects of this application package
     build() {
       Row() {
         Column() {
           Text(this.message)
             .fontSize(50)
             .fontWeight(FontWeight.Bold)
             .onClick(() => {
               let rawfileContext = testNapi.getRawFileContent(this.resMgr, 'rawfile.txt');
               console.log("rawfileContext" + rawfileContext);
             })
         }
         .width('100%')
       }
       .height('100%')
     }
   }
   ```

参考链接

[Rawfile开发指导](../harmonyos-guides/rawfile-guidelines.md)
