---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-22
title: 如何在Native侧访问应用包内Rawfile资源
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何在Native侧访问应用包内Rawfile资源
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:32+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:e36275bb3bddd4243ec460e05c4955b55ee7dc6aac57d4840757519d10f38f7c
---

**解决措施**

使用Native Rawfile接口操作Rawfile目录和文件，可以访问应用包内的资源。

参考以下代码。

1. 在src/main/cpp/CMakeLists.txt文件中，添加依赖资源librawfile.z.so。

   target\_link\_libraries(nativeaccessres PUBLIC libace\_napi.z.so libhilog\_ndk.z.so librawfile.z.so)
2. 在index.d.ts文件中声明getRawFileContent。

   ```
   1. import { resourceManager } from "@kit.LocalizationKit";
   2. export const getRawFileContent: (resMgr: resourceManager.ResourceManager, path: string) => Uint8Array;
   ```

   [Index.d.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/NativeAccessRes/src/main/cpp/types/libnativeaccessres/Index.d.ts#L19-L20)
3. 在napi\_init.cpp文件中实现功能代码。

   ```
   1. #include <memory>
   2. #include "string"
   3. #include "napi/native_api.h"
   4. #include <rawfile/raw_file.h>
   5. #include <rawfile/raw_file_manager.h>
   6. #include "hilog/log.h"

   8. const int GLOBAL_RESMGR = 0xFF00;
   9. const char *TAG = "[Sample_rawfile]";

   11. namespace {
   12. napi_value CreateJsArrayValue(napi_env env, std::unique_ptr<uint8_t[]> &data, long length)
   13. {
   14. napi_value buffer;
   15. napi_status status = napi_create_external_arraybuffer(
   16. env, data.get(), length,
   17. [](napi_env env, void *data, void *hint) {
   18. delete[] static_cast<char *>(data);
   19. },
   20. nullptr, &buffer);
   21. if (status != napi_ok) {
   22. OH_LOG_Print(LOG_APP, LOG_ERROR, GLOBAL_RESMGR, TAG, "Failed to create external array buffer");
   23. return nullptr;
   24. }
   25. napi_value result = nullptr;
   26. status = napi_create_typedarray(env, napi_uint8_array, length, buffer, 0, &result);
   27. if (status != napi_ok) {
   28. OH_LOG_Print(LOG_APP, LOG_ERROR, GLOBAL_RESMGR, TAG, "Failed to create media typed array");
   29. return nullptr;
   30. }
   31. data.release();
   32. return result;
   33. }
   34. }

   37. static napi_value GetRawFileContent(napi_env env, napi_callback_info info)
   38. {
   39. OH_LOG_Print(LOG_APP, LOG_ERROR, GLOBAL_RESMGR, TAG, "GetFileContent Begin");
   40. size_t requireArgc = 3;
   41. size_t argc = 2;
   42. napi_value argv[2] = { nullptr };
   43. // Obtain parameter information
   44. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);

   46. // Argv [0] is the first parameter of the function, Js resource object, and OH_ ResourceManagerial is converted to a Native object.
   47. NativeResourceManager *mNativeResMgr = OH_ResourceManager_InitNativeResourceManager(env, argv[0]);
   48. size_t strSize;
   49. char strBuf[256];
   50. napi_get_value_string_utf8(env, argv[1], strBuf, sizeof(strBuf), &strSize);
   51. std::string filename(strBuf, strSize);

   53. // Get rawfile pointer object
   54. RawFile *rawFile = OH_ResourceManager_OpenRawFile(mNativeResMgr, filename.c_str());
   55. if (rawFile != nullptr) {
   56. OH_LOG_Print(LOG_APP, LOG_ERROR, GLOBAL_RESMGR, TAG, "OH_ResourceManager_OpenRawFile success");
   57. }
   58. // Get rawfile size and request memory
   59. long len = OH_ResourceManager_GetRawFileSize(rawFile);
   60. std::unique_ptr<uint8_t[]> data= std::make_unique<uint8_t[]>(len);

   62. // Read all contents of rawfile at once
   63. int res = OH_ResourceManager_ReadRawFile(rawFile, data.get(), len);

   65. // Close open pointer objects
   66. OH_ResourceManager_CloseRawFile(rawFile);
   67. OH_ResourceManager_ReleaseNativeResourceManager(mNativeResMgr);
   68. // Convert to JS object
   69. return CreateJsArrayValue(env, data, len);
   70. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/NativeAccessRes/src/main/cpp/napi_init.cpp#L21-L90)
4. 在ArkTS侧调用时，需要传入资源对象。

   ```
   1. import testNapi from 'libnativeaccessres.so'  // Import so

   3. @Entry
   4. @Component
   5. struct Index {
   6. @State message: string = 'Native Access Resource';
   7. private resMgr = this.getUIContext().getHostContext()!.resourceManager;  // Retrieve the resource objects of this application package
   8. build() {
   9. Row() {
   10. Column() {
   11. Text(this.message)
   12. .fontSize(50)
   13. .fontWeight(FontWeight.Bold)
   14. .onClick(() => {
   15. let rawfileContext = testNapi.getRawFileContent(this.resMgr, 'rawfile.txt');
   16. console.log("rawfileContext" + rawfileContext);
   17. })
   18. }
   19. .width('100%')
   20. }
   21. .height('100%')
   22. }
   23. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/Ndk2/NativeAccessRes/src/main/ets/pages/Index.ets#L19-L41)

参考链接

[Rawfile开发指导](../harmonyos-guides/rawfile-guidelines.md)
