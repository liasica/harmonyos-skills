---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-23
title: 如何在Native侧跨模块访问资源
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何在Native侧跨模块访问资源
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:965435e28aced6ceddc791a1a7eb2e72d21bc18d28cddcb6835a3cb42373247a
---

**解决措施**

可以通过createModuleContext(moduleName)接口创建同应用中不同模块的上下文。获取到resourceManager对象后，使用 Native Rawfile 接口在 Native 侧操作 Rawfile 目录和文件，实现跨模块资源访问。

具体使用方式可参考以下代码：

1. 在CMakeLists.txt中添加librawfile.z.so依赖。

   target\_link\_libraries(nativecrossmoduleaccessres PUBLIC libace\_napi.z.so libhilog\_ndk.z.so librawfile.z.so)
2. 在src/main/cpp/types/libentry/index.d.ts文件中，声明应用侧函数getRawFileContent。

   ```ts
   import { resourceManager } from "@kit.LocalizationKit";
   export const getRawFileContent: (resMgr: resourceManager.ResourceManager, path: string) => Uint8Array;
   ```
3. 在napi\_init.cpp中实现功能代码。

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
       // argv[0] is the first parameter of the function, the js resource object. OH_ResourceManager_InitNativeResourceManager convert to Native object. 
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
       // Obtain the size of the rawfile and allocate memory 
       long len = OH_ResourceManager_GetRawFileSize(rawFile); 
       std::unique_ptr<uint8_t[]> data= std::make_unique<uint8_t[]>(len); 
       // Read the entire content of the rawfile one-off 
       int res = OH_ResourceManager_ReadRawFile(rawFile, data.get(), len); 
       // Close the open pointer object  
       OH_ResourceManager_CloseRawFile(rawFile); 
       OH_ResourceManager_ReleaseNativeResourceManager(mNativeResMgr); 
       // Convert to js object  
       return CreateJsArrayValue(env, data, len);
   }
   ```
4. 在ArkTS侧调用，传入资源对象。

   ```ts
   import { application } from '@kit.AbilityKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import testNapi from 'libnativecrossmoduleaccessres.so';

   @Entry
   @Component
   struct Index {
     @State message: string = 'Native Cross Module Access Resource';

     build() {
       Row() {
         Column() {
           Text(this.message)
             .fontSize(50)
             .fontWeight(FontWeight.Bold)
             .onClick(() => {
               application.createModuleContext(this.getUIContext().getHostContext(), 'NativeAccessRes')
                 .then((data: Context) => {
                   if (data) {
                     let rawfileContext: Uint8Array = testNapi.getRawFileContent(data.resourceManager, 'rawfile.txt');
                     console.log("rawfileContext" + rawfileContext);
                   }
                 })
                 .catch((error: BusinessError) => {
                   let code: number = (error as BusinessError).code;
                   let message: string = (error as BusinessError).message;
                   console.error(`createModuleContext failed, error.code: ${code}, error.message: ${message}`);
                 })
             })
         }
         .width('100%')
       }
       .height('100%')
     }
   }
   ```

参考链接：

[Rawfile开发指导](../harmonyos-guides/rawfile-guidelines.md)
