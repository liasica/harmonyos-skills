---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-23
title: 如何在Native侧跨模块访问资源
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何在Native侧跨模块访问资源
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:33+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a9dc0786fd54c2f16e2f8caa1bbeac5565855ff3d9653cf77b35d2a5b80256a4
---

**解决措施**

可以通过createModuleContext(moduleName)接口创建同应用中不同模块的上下文。获取到resourceManager对象后，使用 Native Rawfile 接口在 Native 侧操作 Rawfile 目录和文件，实现跨模块资源访问。

具体使用方式可参考以下代码：

1. 在CMakeLists.txt中添加librawfile.z.so依赖。

   target\_link\_libraries(nativecrossmoduleaccessres PUBLIC libace\_napi.z.so libhilog\_ndk.z.so librawfile.z.so)
2. 在src/main/cpp/types/libentry/index.d.ts文件中，声明应用侧函数getRawFileContent。

   ```
   1. import { resourceManager } from "@kit.LocalizationKit";
   2. export const getRawFileContent: (resMgr: resourceManager.ResourceManager, path: string) => Uint8Array;
   ```

   [Index.d.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/NativeCrossModuleAccessRes/src/main/cpp/types/libnativecrossmoduleaccessres/Index.d.ts#L20-L21)
3. 在napi\_init.cpp中实现功能代码。

   ```
   1. #include <memory>
   2. #include "string"
   3. #include "napi/native_api.h"
   4. #include <rawfile/raw_file.h>
   5. #include <rawfile/raw_file_manager.h>
   6. #include "hilog/log.h"

   8. const int GLOBAL_RESMGR = 0xFF00;
   9. const char *TAG = "[Sample_rawfile]";
   10. namespace {
   11. napi_value CreateJsArrayValue(napi_env env, std::unique_ptr<uint8_t[]> &data, long length)
   12. {
   13. napi_value buffer;
   14. napi_status status = napi_create_external_arraybuffer(
   15. env, data.get(), length,
   16. [](napi_env env, void *data, void *hint) {
   17. delete[] static_cast<char *>(data);
   18. },
   19. nullptr, &buffer);
   20. if (status != napi_ok) {
   21. OH_LOG_Print(LOG_APP, LOG_ERROR, GLOBAL_RESMGR, TAG, "Failed to create external array buffer");
   22. return nullptr;
   23. }
   24. napi_value result = nullptr;
   25. status = napi_create_typedarray(env, napi_uint8_array, length, buffer, 0, &result);
   26. if (status != napi_ok) {
   27. OH_LOG_Print(LOG_APP, LOG_ERROR, GLOBAL_RESMGR, TAG, "Failed to create media typed array");
   28. return nullptr;
   29. }
   30. data.release();
   31. return result;
   32. }
   33. }
   34. static napi_value GetRawFileContent(napi_env env, napi_callback_info info)
   35. {
   36. OH_LOG_Print(LOG_APP, LOG_ERROR, GLOBAL_RESMGR, TAG, "GetFileContent Begin");
   37. size_t requireArgc = 3;
   38. size_t argc = 2;
   39. napi_value argv[2] = { nullptr };
   40. // Obtain parameter information
   41. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
   42. // argv[0] is the first parameter of the function, the js resource object. OH_ResourceManager_InitNativeResourceManager convert to Native object.
   43. NativeResourceManager *mNativeResMgr = OH_ResourceManager_InitNativeResourceManager(env, argv[0]);
   44. size_t strSize;
   45. char strBuf[256];
   46. napi_get_value_string_utf8(env, argv[1], strBuf, sizeof(strBuf), &strSize);
   47. std::string filename(strBuf, strSize);
   48. // Get rawfile pointer object
   49. RawFile *rawFile = OH_ResourceManager_OpenRawFile(mNativeResMgr, filename.c_str());
   50. if (rawFile != nullptr) {
   51. OH_LOG_Print(LOG_APP, LOG_ERROR, GLOBAL_RESMGR, TAG, "OH_ResourceManager_OpenRawFile success");
   52. }
   53. // Obtain the size of the rawfile and allocate memory
   54. long len = OH_ResourceManager_GetRawFileSize(rawFile);
   55. std::unique_ptr<uint8_t[]> data= std::make_unique<uint8_t[]>(len);
   56. // Read the entire content of the rawfile one-off
   57. int res = OH_ResourceManager_ReadRawFile(rawFile, data.get(), len);
   58. // Close the open pointer object
   59. OH_ResourceManager_CloseRawFile(rawFile);
   60. OH_ResourceManager_ReleaseNativeResourceManager(mNativeResMgr);
   61. // Convert to js object
   62. return CreateJsArrayValue(env, data, len);
   63. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/NativeCrossModuleAccessRes/src/main/cpp/napi_init.cpp#L21-L83)
4. 在ArkTS侧调用，传入资源对象。

   ```
   1. import { application } from '@kit.AbilityKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import testNapi from 'libnativecrossmoduleaccessres.so';

   5. @Entry
   6. @Component
   7. struct Index {
   8. @State message: string = 'Native Cross Module Access Resource';

   10. build() {
   11. Row() {
   12. Column() {
   13. Text(this.message)
   14. .fontSize(50)
   15. .fontWeight(FontWeight.Bold)
   16. .onClick(() => {
   17. application.createModuleContext(this.getUIContext().getHostContext(), 'NativeAccessRes')
   18. .then((data: Context) => {
   19. if (data) {
   20. let rawfileContext: Uint8Array = testNapi.getRawFileContent(data.resourceManager, 'rawfile.txt');
   21. console.log("rawfileContext" + rawfileContext);
   22. }
   23. })
   24. .catch((error: BusinessError) => {
   25. let code: number = (error as BusinessError).code;
   26. let message: string = (error as BusinessError).message;
   27. console.error(`createModuleContext failed, error.code: ${code}, error.message: ${message}`);
   28. })
   29. })
   30. }
   31. .width('100%')
   32. }
   33. .height('100%')
   34. }
   35. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/NativeCrossModuleAccessRes/src/main/ets/pages/Index.ets#L19-L54)

参考链接：

[Rawfile开发指导](../harmonyos-guides/rawfile-guidelines.md)
