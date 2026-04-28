---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/rawfile-guidelines
title: Rawfile开发指导
breadcrumb: 指南 > NDK开发 > 代码开发 > 资源管理 > Rawfile开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9ba10574f0cbd85a81a2c60f3c30d1f0e23bbc2f6f239c3faabb06c312a28f99
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/Uvh8hZffS1et1HDspnRJhg/zh-cn_image_0000002552799738.png?HW-CC-KV=V1&HW-CC-Date=20260427T235428Z&HW-CC-Expire=86400&HW-CC-Sign=CECF7B898BCE786BFE33D1E6134E1FF1E6C05290FC992EB682EFEA5CAE016C60)

**2. 添加依赖**

创建完成后，DevEco Studio会在工程中生成cpp目录，目录下有libentry/index.d.ts、hello.cpp、CMakeLists.txt等文件。

1. 打开src/main/cpp/CMakeLists.txt，在target\_link\_libraries依赖中添加rawfile依赖librawfile.z.so以及日志依赖libhilog\_ndk.z.so。

   ```
   1. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so librawfile.z.so)
   ```
2. 打开src/main/cpp/types/libentry/index.d.ts文件，在此文件中声明ArkTS侧接口getFileList、getRawFileContent、getRawFileDescriptor、isRawDir。

   ```
   1. import { resourceManager } from '@kit.LocalizationKit';
   2. export const getFileList: (resMgr: resourceManager.ResourceManager, path: string) => Array<String>;
   3. export const getRawFileContent: (resMgr: resourceManager.ResourceManager, path: string) => Uint8Array;
   4. export const getRawFileDescriptor: (resMgr: resourceManager.ResourceManager, path: string) => resourceManager.RawFileDescriptor;
   5. export const isRawDir: (resMgr: resourceManager.ResourceManager, path: string) => boolean;
   ```

   [Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ResourceManagement/RawFile/entry/src/main/cpp/types/libentry/Index.d.ts#L16-L22)

**3. 修改源文件**

1. 打开src/main/cpp/hello.cpp文件，在Init方法中添加ArkTS接口与C++接口的映射。ArkTS侧接口getFileList、getRawFileContent、getRawFileDescriptor、isRawDir，映射C++接口分别为GetFileList、GetRawFileContent、GetRawFileDescriptor、IsRawDir。

   ```
   1. EXTERN_C_START
   2. static napi_value Init(napi_env env, napi_value exports)
   3. {
   4. napi_property_descriptor desc[] = {
   5. { "getFileList", nullptr, GetFileList, nullptr, nullptr, nullptr, napi_default, nullptr },
   6. { "getRawFileContent", nullptr, GetRawFileContent, nullptr, nullptr, nullptr, napi_default, nullptr },
   7. { "getRawFileDescriptor", nullptr, GetRawFileDescriptor, nullptr, nullptr, nullptr, napi_default, nullptr },
   8. { "isRawDir", nullptr, IsRawDir, nullptr, nullptr, nullptr, napi_default, nullptr }
   9. };

   11. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   12. return exports;
   13. }
   14. EXTERN_C_END
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ResourceManagement/RawFile/entry/src/main/cpp/hello.cpp#L255-L270)
2. 在src/main/cpp/目录下创建hello.h文件，在hello.h文件中增加对应的四个方法，如下所示：

   ```
   1. #ifndef RAWFILE_HELLO_H
   2. #define RAWFILE_HELLO_H

   4. #include <js_native_api.h>
   5. #include <js_native_api_types.h>
   6. #include <string>
   7. #include <vector>
   8. #include <cstdlib>
   9. #include "napi/native_api.h"

   11. napi_value GetFileList(napi_env env, napi_callback_info info);
   12. napi_value GetRawFileContent(napi_env env, napi_callback_info info);
   13. napi_value GetRawFileDescriptor(napi_env env, napi_callback_info info);
   14. napi_value IsRawDir(napi_env env, napi_callback_info info);

   16. #endif // RAWFILE_HELLO_H
   ```

   [hello.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ResourceManagement/RawFile/entry/src/main/cpp/hello.h#L16-L33)
3. 在hello.cpp文件中实现上述四个方法。通过env和info获取Js的资源管理对象，并转换为Native的资源管理对象，即可调用Native资源管理对象的接口，示例代码如下：

   导入头文件

   ```
   1. #include "hello.h"
   2. #include "rawfile/raw_file_manager.h"
   3. #include "rawfile/raw_file.h"
   4. #include "rawfile/raw_dir.h"
   5. #include "hilog/log.h"
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ResourceManagement/RawFile/entry/src/main/cpp/hello.cpp#L16-L22)

   声明hilog日志打印的DOMAIN和TAG常量

   ```
   1. const int GLOBAL_RESMGR = 0xFF00;
   2. const char *TAG = "[Sample_rawfile]";
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ResourceManagement/RawFile/entry/src/main/cpp/hello.cpp#L24-L27)

   示例：

   ```
   1. // 示例一：获取rawfile文件列表 GetFileList
   2. napi_value GetFileList(napi_env env, napi_callback_info info)
   3. {
   4. OH_LOG_Print(LOG_APP, LOG_INFO, GLOBAL_RESMGR, TAG, "NDKTest GetFileList Begin");
   5. size_t argc = 2;
   6. napi_value argv[2] = { nullptr };
   7. // 获取参数信息
   8. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);

   10. // argv[0]即为函数第一个参数Js资源对象，OH_ResourceManager_InitNativeResourceManager转为Native对象
   11. NativeResourceManager *mNativeResMgr = OH_ResourceManager_InitNativeResourceManager(env, argv[0]);

   13. // 获取函数argv[1]，此为rawfile相对路径
   14. size_t strSize;
   15. char strBuf[256];
   16. napi_get_value_string_utf8(env, argv[1], strBuf, sizeof(strBuf), &strSize);
   17. std::string dirName(strBuf, strSize);

   19. // 获取对应的rawDir指针对象
   20. RawDir* rawDir = OH_ResourceManager_OpenRawDir(mNativeResMgr, dirName.c_str());

   22. // 获取rawDir下文件及文件夹数量
   23. int count = OH_ResourceManager_GetRawFileCount(rawDir);

   25. // 遍历获取文件名称，并保存
   26. std::vector<std::string> tempArray;
   27. for (int i = 0; i < count; i++) {
   28. std::string filename = OH_ResourceManager_GetRawFileName(rawDir, i);
   29. tempArray.emplace_back(filename);
   30. }

   32. // 转为js数组
   33. napi_value fileList;
   34. napi_create_array(env, &fileList);
   35. for (size_t i = 0; i < tempArray.size(); i++) {
   36. napi_value jsString;
   37. napi_create_string_utf8(env, tempArray[i].c_str(), NAPI_AUTO_LENGTH, &jsString);
   38. napi_set_element(env, fileList, i, jsString);
   39. }

   41. // 关闭打开的指针对象
   42. OH_ResourceManager_CloseRawDir(rawDir);
   43. OH_ResourceManager_ReleaseNativeResourceManager(mNativeResMgr);
   44. return fileList;
   45. }
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ResourceManagement/RawFile/entry/src/main/cpp/hello.cpp#L29-L75)

   ```
   1. // 示例二：获取rawfile文件内容 GetRawFileContent
   2. napi_value CreateJsArrayValue(napi_env env, std::unique_ptr<uint8_t[]> &data, long length)
   3. {
   4. // 创建js外部ArrayBuffer
   5. napi_value buffer;
   6. napi_status status = napi_create_external_arraybuffer(env, data.get(), length,
   7. [](napi_env env, void *data, void *hint) {
   8. delete[] static_cast<char*>(data);
   9. }, nullptr, &buffer);
   10. // 检测ArrayBuffer是否创建成功
   11. if (status != napi_ok) {
   12. OH_LOG_Print(LOG_APP, LOG_ERROR, GLOBAL_RESMGR, TAG, "Failed to create external array buffer");
   13. return nullptr;
   14. }
   15. // 创建js TypedArray  将ArrayBuffer绑定到TypedArray
   16. napi_value result = nullptr;
   17. status = napi_create_typedarray(env, napi_uint8_array, length, buffer, 0, &result);
   18. if (status != napi_ok) {
   19. OH_LOG_Print(LOG_APP, LOG_ERROR, GLOBAL_RESMGR, TAG, "Failed to create media typed array");
   20. return nullptr;
   21. }
   22. data.release();
   23. return result;
   24. }

   26. napi_value GetRawFileContent(napi_env env, napi_callback_info info)
   27. {
   28. OH_LOG_Print(LOG_APP, LOG_INFO, GLOBAL_RESMGR, TAG, "GetFileContent Begin");
   29. size_t argc = 2;
   30. napi_value argv[2] = { nullptr };
   31. // 获取参数信息
   32. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);

   34. // argv[0]即为函数第一个参数Js资源对象，OH_ResourceManager_InitNativeResourceManager转为Native对象
   35. NativeResourceManager *mNativeResMgr = OH_ResourceManager_InitNativeResourceManager(env, argv[0]);
   36. size_t strSize;
   37. char strBuf[256];
   38. napi_get_value_string_utf8(env, argv[1], strBuf, sizeof(strBuf), &strSize);
   39. std::string filename(strBuf, strSize);

   41. // 获取rawfile指针对象
   42. RawFile *rawFile = OH_ResourceManager_OpenRawFile(mNativeResMgr, filename.c_str());
   43. if (rawFile != nullptr) {
   44. OH_LOG_Print(LOG_APP, LOG_INFO, GLOBAL_RESMGR, TAG, "OH_ResourceManager_OpenRawFile success");
   45. }
   46. // 获取rawfile大小并申请内存
   47. long len = OH_ResourceManager_GetRawFileSize(rawFile);
   48. std::unique_ptr<uint8_t[]> data = std::make_unique<uint8_t[]>(len);

   50. // 一次性读取rawfile全部内容
   51. int res = OH_ResourceManager_ReadRawFile(rawFile, data.get(), len);

   53. // 关闭打开的指针对象
   54. OH_ResourceManager_CloseRawFile(rawFile);
   55. OH_ResourceManager_ReleaseNativeResourceManager(mNativeResMgr);
   56. // 转为js对象
   57. return CreateJsArrayValue(env, data, len);
   58. }
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ResourceManagement/RawFile/entry/src/main/cpp/hello.cpp#L77-L136)

   ```
   1. // 示例三：获取rawfile文件描述符 GetRawFileDescriptor
   2. // 定义一个函数，将RawFileDescriptor转为js对象
   3. napi_value createJsFileDescriptor(napi_env env, RawFileDescriptor& descriptor)
   4. {
   5. // 创建js对象
   6. napi_value result;
   7. napi_status status = napi_create_object(env, &result);
   8. if (status != napi_ok) {
   9. return result;
   10. }

   12. // 将文件描述符fd存入到result对象中
   13. napi_value fd;
   14. status = napi_create_int32(env, descriptor.fd, &fd);
   15. if (status != napi_ok) {
   16. return result;
   17. }
   18. status = napi_set_named_property(env, result, "fd", fd);
   19. if (status != napi_ok) {
   20. return result;
   21. }

   23. // 将文件偏移量offset存入到result对象中
   24. napi_value offset;
   25. status = napi_create_int64(env, descriptor.start, &offset);
   26. if (status != napi_ok) {
   27. return result;
   28. }
   29. status = napi_set_named_property(env, result, "offset", offset);
   30. if (status != napi_ok) {
   31. return result;
   32. }

   34. // 将文件长度length存入到result对象中
   35. napi_value length;
   36. status = napi_create_int64(env, descriptor.length, &length);
   37. if (status != napi_ok) {
   38. return result;
   39. }
   40. status = napi_set_named_property(env, result, "length", length);
   41. if (status != napi_ok) {
   42. return result;
   43. }
   44. return result;
   45. }

   47. napi_value GetRawFileDescriptor(napi_env env, napi_callback_info info)
   48. {
   49. OH_LOG_Print(LOG_APP, LOG_INFO, GLOBAL_RESMGR, TAG, "NDKTest GetRawFileDescriptor Begin");
   50. size_t argc = 2;
   51. napi_value argv[2] = { nullptr };
   52. // 获取参数信息
   53. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);

   55. // argv[0]即为函数第一个参数Js资源对象，OH_ResourceManager_InitNativeResourceManager转为Native对象
   56. NativeResourceManager *mNativeResMgr = OH_ResourceManager_InitNativeResourceManager(env, argv[0]);
   57. size_t strSize;
   58. char strBuf[256];
   59. napi_get_value_string_utf8(env, argv[1], strBuf, sizeof(strBuf), &strSize);
   60. std::string filename(strBuf, strSize);
   61. // 获取rawfile指针对象
   62. RawFile *rawFile = OH_ResourceManager_OpenRawFile(mNativeResMgr, filename.c_str());
   63. if (rawFile != nullptr) {
   64. OH_LOG_Print(LOG_APP, LOG_INFO, GLOBAL_RESMGR, TAG, "OH_ResourceManager_OpenRawFile success");
   65. }
   66. // 获取rawfile的描述符RawFileDescriptor {fd, offset, length}
   67. RawFileDescriptor descriptor;
   68. OH_ResourceManager_GetRawFileDescriptor(rawFile, descriptor);
   69. // 关闭打开的指针对象
   70. OH_ResourceManager_CloseRawFile(rawFile);
   71. OH_ResourceManager_ReleaseNativeResourceManager(mNativeResMgr);
   72. // 转为js对象
   73. return createJsFileDescriptor(env, descriptor);
   74. }
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ResourceManagement/RawFile/entry/src/main/cpp/hello.cpp#L138-L213)

   ```
   1. // 示例四：判断路径是否是rawfile下的目录 IsRawDir
   2. napi_value CreateJsBool(napi_env env, bool &bValue)
   3. {
   4. napi_value jsValue = nullptr;
   5. if (napi_get_boolean(env, bValue, &jsValue) != napi_ok) {
   6. return nullptr;
   7. }
   8. return jsValue;
   9. }

   11. napi_value IsRawDir(napi_env env, napi_callback_info info)
   12. {
   13. OH_LOG_Print(LOG_APP, LOG_INFO, GLOBAL_RESMGR, TAG, "NDKTest IsRawDir Begin");
   14. size_t argc = 2;
   15. napi_value argv[2] = { nullptr };
   16. // 获取参数信息
   17. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);

   19. // argv[0]即为函数第一个参数Js资源对象，OH_ResourceManager_InitNativeResourceManager转为Native对象
   20. NativeResourceManager *mNativeResMgr = OH_ResourceManager_InitNativeResourceManager(env, argv[0]);

   22. napi_valuetype fileNameType;
   23. napi_typeof(env, argv[1], &fileNameType);
   24. if (fileNameType == napi_undefined || fileNameType == napi_null) {
   25. OH_LOG_Print(LOG_APP, LOG_ERROR, GLOBAL_RESMGR, TAG, "NDKTest file name is null");
   26. bool temp = false;
   27. return CreateJsBool(env, temp);
   28. }
   29. size_t strSize;
   30. char strBuf[256];
   31. napi_get_value_string_utf8(env, argv[1], strBuf, sizeof(strBuf), &strSize);
   32. std::string filename(strBuf, strSize);
   33. // 判断是否是rawfile下的目录
   34. bool result = OH_ResourceManager_IsRawDir(mNativeResMgr, filename.c_str());
   35. OH_ResourceManager_ReleaseNativeResourceManager(mNativeResMgr);
   36. return CreateJsBool(env, result);
   37. }
   ```

   [hello.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ResourceManagement/RawFile/entry/src/main/cpp/hello.cpp#L215-L253)

**4. ArkTS侧调用**

1. 打开src\main\ets\pages\index.ets, 导入"libentry.so"。
2. 资源获取包括获取本应用包资源、应用内跨包资源、跨应用包资源。

   通过context.resourceManager获取本应用包resourceManager对象。

   通过context.createModuleContext().resourceManager获取应用内跨包resourceManager对象。

   Context的更多使用信息请参考[应用上下文Context](application-context-stage.md)。
3. 调用src/main/cpp/types/libentry/index.d.ts中声明的接口，如getFileList，传入js的资源管理对象以及rawfile文件夹的相对路径。

   获取本应用包资源resourceManager对象的示例如下：

   ```
   1. import { util } from '@kit.ArkTS';
   2. import { resourceManager } from '@kit.LocalizationKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   4. import testNapi from 'libentry.so'; // 导入so

   6. const DOMAIN = 0x0000;
   7. const TAG = '[Sample_rawfile]';

   9. @Entry
   10. @Component
   11. struct Index {
   12. @State message: string = 'Hello World';
   13. private resMgr = this.getUIContext().getHostContext()?.resourceManager; // 获取本应用包的资源对象
   14. @State rawfileListMsg: string = 'FileList = ';
   15. @State retMsg: string = 'isRawDir = ';
   16. @State rawfileContentMsg: string = 'RawFileContent = ';
   17. @State rawfileDescriptorMsg: string = 'RawFileDescriptor.length = ';

   19. build() {
   20. Row() {
   21. Column() {
   22. Text(this.message)
   23. .id('hello_world')
   24. .fontSize(30)
   25. .fontWeight(FontWeight.Bold)
   26. .onClick(async () => {
   27. // 传入资源管理对象，以及访问的rawfile文件夹名称
   28. let rawFileList: Array<String> = testNapi.getFileList(this.resMgr, '');
   29. this.rawfileListMsg = 'FileList = ' + rawFileList;
   30. hilog.info(DOMAIN, TAG, this.rawfileListMsg);

   32. // 'sub_rawfile'仅作示例，请替换为实际使用的资源
   33. let ret: boolean = testNapi.isRawDir(this.resMgr, 'sub_rawfile');
   34. this.retMsg = 'isRawDir = ' + ret;
   35. hilog.info(DOMAIN, TAG, this.retMsg);

   37. // 传入资源管理对象，以及访问的rawfile文件夹名称
   38. // 'rawfile1.txt'仅作示例，请替换为实际使用的资源
   39. let rawfileArray: Uint8Array = testNapi.getRawFileContent(this.resMgr, 'rawfile1.txt');
   40. // 将Uint8Array转为字符串
   41. let textDecoder: util.TextDecoder = new util.TextDecoder();
   42. let rawfileContent: string = textDecoder.decodeToString(rawfileArray);
   43. this.rawfileContentMsg = 'RawFileContent = ' + rawfileContent;
   44. hilog.info(DOMAIN, TAG, this.rawfileContentMsg);

   46. // 传入资源管理对象，以及访问的rawfile文件名称
   47. // 'rawfile1.txt'仅作示例，请替换为实际使用的资源
   48. let rawfileDescriptor: resourceManager.RawFileDescriptor =
   49. testNapi.getRawFileDescriptor(this.resMgr, 'rawfile1.txt');
   50. this.rawfileDescriptorMsg = 'RawFileDescriptor.length = ' + rawfileDescriptor.length;
   51. hilog.info(DOMAIN, TAG, this.rawfileDescriptorMsg);
   52. })
   53. Text(this.rawfileListMsg).id('get_file_list').fontSize(30);
   54. Text(this.retMsg).id('is_raw_dir').fontSize(30);
   55. Text(this.rawfileContentMsg).id('get_raw_file_content').fontSize(30);
   56. Text(this.rawfileDescriptorMsg).id('get_raw_file_descriptor').fontSize(30);
   57. }
   58. .width('100%')
   59. }
   60. .height('100%')
   61. }
   62. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ResourceManagement/RawFile/entry/src/main/ets/pages/Index.ets#L15-L79)
