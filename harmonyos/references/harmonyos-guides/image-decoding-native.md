---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-decoding-native
title: 图片解码
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(依赖JS对象)(不再推荐) > 图片解码
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:206e45a1d2333368e3c969580eff1204a1f02af769326bce16eeec90decedee8
---

说明

当前开发指导使用的接口为[Image](../harmonyos-references/capi-image.md)模块下的C API，可完成图片编解码，图片接收器，处理图像数据等功能。这部分API在API version 11之前发布，在后续的版本不再增加新功能，**不再推荐使用**。

开发者可使用[Image\_NativeModule](../harmonyos-references/capi-image-nativemodule.md)模块下的C API，不仅提供上述图片框架基础功能，还可以完成多图编解码等新特性，相关开发指导请参考[图片开发指导(C/C++)](image-source-c.md)节点下的内容。这部分API从API version 12开始支持，并将持续演进，**推荐开发者使用**。

两套C API不建议同时使用，在部分场景下存在不兼容的问题。

将所支持格式的图片文件解码成PixelMap，以便在应用或系统中进行图片显示或[图片处理](image-transformation.md)。当前支持的图片文件格式包括JPEG、PNG、GIF、WebP、BMP、SVG、ICO、DNG、HEIC、WBMP23+、HEIFS23+、TIFF23+。部分格式的解码能力依赖于具体的设备硬件，建议在调用前使用[image.getImageSourceSupportedFormats20+](../harmonyos-references/arkts-apis-image-f.md#imagegetimagesourcesupportedformats20)接口，动态查询当前设备上的解码能力。

## 开发步骤

图片解码相关API的详细介绍请参见：[图片解码接口文档](../harmonyos-references/capi-image-source-mdk-h.md)。

### 添加依赖

在进行应用开发之前，开发者需要打开native工程的src/main/cpp/CMakeLists.txt，在target\_link\_libraries依赖中添加libace\_napi.z.so、libpixelmap\_ndk.z.so、libimage\_source\_ndk.z.so、librawfile.z.so以及日志依赖libhilog\_ndk.z.so。

```
1. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so libpixelmap_ndk.z.so libimage_source_ndk.z.so librawfile.z.so)
```

### 添加接口映射

打开src/main/cpp/hello.cpp文件，在Init函数中添加getSyncPixelMap函数接口映射，作用是以同步的方式生成PixelMap，具体代码如下：

```
1. EXTERN_C_START
2. static napi_value Init(napi_env env, napi_value exports)
3. {
4. napi_property_descriptor desc[] = {
5. { "getSyncPixelMap", nullptr, getSyncPixelMap, nullptr, nullptr, nullptr, napi_default, nullptr },
6. };

8. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
9. return exports;
10. }
11. EXTERN_C_END
```

### JS侧调用

1. 打开src\main\cpp\types\libentry\index.d.ts（其中libentry根据工程名生成），导入如下引用文件：

   ```
   1. import { image } from '@kit.ImageKit';
   2. import { resourceManager } from '@kit.LocalizationKit';

   4. // 同步调用，入参为资源管理器和图片资源名称，返回PixelMap。
   5. export const getSyncPixelMap: (resMgr: resourceManager.ResourceManager, src: string) => image.PixelMap;
   ```
2. 准备图片资源文件，本示例文件名为example.jpg，导入到src\main\resources\rawfile\ 路径下。
3. 打开src\main\ets\pages\index.ets，导入"libentry.so（根据工程名生成）"，调用Native接口，传入JS的资源对象。示例如下：

   ```
   1. import testNapi from 'libentry.so';
   2. import { image } from '@kit.ImageKit';
   3. import { common } from '@kit.AbilityKit';
   4. @Entry
   5. @Component
   6. struct Index {
   7. @State pixelMap : PixelMap | undefined = undefined;
   8. aboutToAppear() {
   9. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
   10. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   11. // 调用自定义的getSyncPixelMap接口，获取pixelMap。
   12. this.pixelMap = testNapi.getSyncPixelMap(context.resourceManager, "example.jpg");
   13. }

   15. build() {
   16. Row() {
   17. Column() {
   18. Image(this.pixelMap)
   19. .width(100)
   20. .height(100)
   21. }
   22. .width('100%')
   23. }
   24. .height('100%')
   25. }
   26. }
   ```

### Native接口调用

具体接口说明请参考[Image](../harmonyos-references/capi-image.md)。

在hello.cpp文件中获取JS的资源对象，并转为Native的资源对象，即可调用Native接口，调用方式示例代码如下：

**添加引用文件**

```
1. // 引入图片框架、raw文件、raw文件管理和日志打印头文件。
2. #include <cstdlib>
3. #include <cstring>
4. #include <multimedia/image_framework/image_source_mdk.h>
5. #include <multimedia/image_framework/image_pixel_map_mdk.h>
6. #include <rawfile/raw_file.h>
7. #include <rawfile/raw_file_manager.h>
8. #include <hilog/log.h>

10. static napi_value getSyncPixelMap(napi_env env, napi_callback_info info)
11. {
12. size_t argc = 2;
13. napi_value args[2] = {nullptr};

15. napi_get_cb_info(env, info, &argc, args , nullptr, nullptr);

17. napi_valuetype srcType;
18. napi_typeof(env, args[0], &srcType);

20. // 入参args[0]是资源管理器，用来初始化native层的资源管理器。
21. NativeResourceManager *mNativeResMgr = OH_ResourceManager_InitNativeResourceManager(env, args[0]);

23. size_t strSize;
24. char srcBuf[2048];
25. // 入参args[1]是文件名称。
26. napi_get_value_string_utf8(env, args[1], srcBuf, sizeof(srcBuf), &strSize);

28. // 用资源管理器打开Raw文件。
29. RawFile * rawFile = OH_ResourceManager_OpenRawFile(mNativeResMgr, srcBuf);
30. if (rawFile != NULL) {
31. // 获取文件大小，并读取数据。
32. long len = OH_ResourceManager_GetRawFileSize(rawFile);
33. uint8_t * data = static_cast<uint8_t *>(malloc(len));
34. int res = OH_ResourceManager_ReadRawFile(rawFile, data, len);

36. OhosImageSource imageSource_c;
37. imageSource_c.buffer = data;
38. imageSource_c.bufferSize = len;

40. OhosImageSourceOps ops{};
41. napi_value imageSource;
42. napi_value pixelMap;

44. // 用读取到的Raw数据创建ImageSource。
45. int32_t ret = OH_ImageSource_Create(env, &imageSource_c, &ops, &imageSource);

47. // 初始化native层的ImageSource。
48. ImageSourceNative * imageSourceNative_c = OH_ImageSource_InitNative(env, imageSource);
49. OhosImageDecodingOps decodingOps{};
50. // 创建pixelMap。
51. OH_ImageSource_CreatePixelMap(imageSourceNative_c, &decodingOps, &pixelMap);

53. // 下列方法,为gif等动图格式提供。
54. // napi_value pixelMapList;
55. // OH_ImageSource_CreatePixelMapList(imageSourceNative_c, &decodingOps, &pixelMapList);
56. // OhosImageSourceDelayTimeList list{};
57. // OH_ImageSource_GetDelayTime(imageSourceNative_c, &list);
58. // uint32_t count;
59. // OH_ImageSource_GetFrameCount(imageSourceNative_c, &count);

61. OhosImageSourceInfo info{};
62. // 读取图片宽高。
63. OH_ImageSource_GetImageInfo(imageSourceNative_c, 0, &info);
64. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00, "[decode]", "imageInfo width:%{public}d , height:%{public}d", info.size.width, info.size.height);

66. // 读取ImageSource的ImageWidth配置参数并打印日志。
67. OhosImageSourceProperty target;
68. char exifKey_c[] = "ImageWidth";
69. target.size = strlen(exifKey_c);
70. target.value = exifKey_c;

72. OhosImageSourceProperty response{};
73. response.size = 20;
74. response.value = static_cast<char *>(malloc(20));
75. OH_ImageSource_GetImageProperty(imageSourceNative_c, &target, &response);
76. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00, "[decode]", "ImageProperty width after modify:%{public}s", response.value);

78. // 处理完毕，释放native层资源。
79. OH_ImageSource_Release(imageSourceNative_c);
80. OH_ResourceManager_CloseRawFile(rawFile);
81. return pixelMap;
82. }
83. OH_ResourceManager_ReleaseNativeResourceManager(mNativeResMgr);
84. return nullptr;
85. }
```

图片框架支持增量式解码，使用方法如下：

```
1. // 引入图片框架、raw文件、raw文件管理和日志打印头文件。
2. #include <cstdlib>
3. #include <cstring>
4. #include <multimedia/image_framework/image_source_mdk.h>
5. #include <multimedia/image_framework/image_pixel_map_mdk.h>
6. #include <rawfile/raw_file.h>
7. #include <rawfile/raw_file_manager.h>
8. #include <hilog/log.h>

10. static napi_value getSyncPixelMap(napi_env env, napi_callback_info info)
11. {
12. size_t argc = 2;
13. napi_value args[2] = {nullptr};

15. napi_get_cb_info(env, info, &argc, args , nullptr, nullptr);

17. napi_valuetype srcType;
18. napi_typeof(env, args[0], &srcType);

20. // 入参args[0]是资源管理器，用来初始化native层的资源管理器。
21. NativeResourceManager * mNativeResMgr = OH_ResourceManager_InitNativeResourceManager(env, args[0]);

23. size_t strSize;
24. char srcBuf[2048];
25. // 入参args[1]是文件名称。
26. napi_get_value_string_utf8(env, args[1], srcBuf, sizeof(srcBuf), &strSize);

28. // 用资源管理器打开Raw文件。
29. RawFile * rawFile = OH_ResourceManager_OpenRawFile(mNativeResMgr, srcBuf);
30. if (rawFile != NULL) {
31. // 获取文件大小，若大于2048字节，则增量式解码，否则直接全部解码。
32. long len = OH_ResourceManager_GetRawFileSize(rawFile);
33. if (len > 2048) {
34. uint8_t * data = static_cast<uint8_t *>(malloc(len));
35. // 读取文件全部数据。
36. int res = OH_ResourceManager_ReadRawFile(rawFile, data, len);

38. uint8_t * holderdata = static_cast<uint8_t *>(malloc(len));

40. OhosImageSource imageSource_c;
41. // imageSource_c的buffer分配了空间，但是数据是空的。
42. imageSource_c.buffer = holderdata;
43. imageSource_c.bufferSize = len;
44. OhosImageSourceOps ops{};
45. napi_value imageSource;
46. // 初始化增量ImageSource。
47. OH_ImageSource_CreateIncremental(env, &imageSource_c, &ops, &imageSource);

49. // 初始化native层的ImageSource。
50. ImageSourceNative * imageSourceNative_c = OH_ImageSource_InitNative(env, imageSource);

52. // 以下模拟分片加载场景，分两次加载分片。第一次加载2048字节，第二次加载剩余的数据。
53. OhosImageSourceUpdateData firstData{};
54. firstData.buffer = data; // 图片数据。
55. firstData.bufferSize = len; // 图片数据总大小。
56. firstData.isCompleted = false;
57. firstData.offset = 0; // 第一次重头开始加载。
58. firstData.updateLength = 2048; // 第一次加载了2048字节。
59. OH_ImageSource_UpdateData(imageSourceNative_c, &firstData);

61. OhosImageSourceUpdateData secondData{};
62. secondData.buffer = data;
63. secondData.bufferSize = len;
64. secondData.isCompleted = true; // 最后一次加载，要标记加载完成。
65. secondData.offset = 2048; // 已经加载过2048字节了，第二次偏移已经加载的量。
66. secondData.updateLength = len - 2048; // 第二次加载剩余的数据。
67. OH_ImageSource_UpdateData(imageSourceNative_c, &secondData);

69. napi_value pixelMap;
70. OhosImageDecodingOps decodingOps{};
71. decodingOps.index = 0;
72. // 创建pixelMap。
73. OH_ImageSource_CreatePixelMap(imageSourceNative_c, &decodingOps, &pixelMap);

75. // 处理完毕，释放native层资源。
76. OH_ImageSource_Release(imageSourceNative_c);
77. OH_ResourceManager_CloseRawFile(rawFile);
78. return pixelMap;
79. }
80. // 读取Raw文件全部数据。
81. uint8_t * data = static_cast<uint8_t *>(malloc(len));
82. int res = OH_ResourceManager_ReadRawFile(rawFile, data, len);

84. OhosImageSource imageSource_c;
85. imageSource_c.buffer = data;
86. imageSource_c.bufferSize = len;

88. OhosImageSourceOps ops{};
89. napi_value imageSource;
90. napi_value pixelMap;

92. // 用读取到的Raw数据创建ImageSource。
93. int32_t ret = OH_ImageSource_Create(env, &imageSource_c, &ops, &imageSource);

95. // 初始化native层的ImageSource。
96. ImageSourceNative * imageSourceNative_c = OH_ImageSource_InitNative(env, imageSource);
97. OhosImageDecodingOps decodingOps{};

99. // 创建pixelMap。
100. OH_ImageSource_CreatePixelMap(imageSourceNative_c, &decodingOps, &pixelMap);

102. // 处理完毕，释放native层资源。
103. OH_ImageSource_Release(imageSourceNative_c);
104. OH_ResourceManager_CloseRawFile(rawFile);
105. return pixelMap;
106. }
107. OH_ResourceManager_ReleaseNativeResourceManager(mNativeResMgr);
108. return nullptr;
109. }
```
