---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-pixelmap-operation-native
title: 位图操作
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(依赖JS对象)(不再推荐) > 位图操作
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:23+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:d0e4793f89278837cadb63d5c04f7e57d139e51f6dd728492c5ccfa234d02cda
---

说明

当前开发指导使用的接口为[Image](../harmonyos-references/capi-image.md)模块下的C API，可完成图片编解码，图片接收器，处理图像数据等功能。这部分API在API version 11之前发布，在后续的版本不再增加新功能，**不再推荐使用**。

开发者可使用[Image\_NativeModule](../harmonyos-references/capi-image-nativemodule.md)模块下的C API，不仅提供上述图片框架基础功能，还可以完成多图编解码等新特性，相关开发指导请参考[图片开发指导(C/C++)](image-source-c.md)节点下的内容。这部分API从API version 12开始支持，并将持续演进，**推荐开发者使用**。

两套C API不建议同时使用，在部分场景下存在不兼容的问题。

开发者可以通过本指导了解如何使用Native Image的接口完成位图操作。

## 开发步骤

**添加依赖**

在进行应用开发之前，开发者需要打开native工程的src/main/cpp/CMakeLists.txt，在target\_link\_libraries依赖中添加image的libace\_napi.z.so、libpixelmap\_ndk.z.so以及日志依赖libhilog\_ndk.z.so。

```
1. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so libpixelmap_ndk.z.so)
```

**添加接口映射**

打开src/main/cpp/hello.cpp文件，在Init函数中添加接口映射如下：

```
1. EXTERN_C_START
2. static napi_value Init(napi_env env, napi_value exports)
3. {
4. napi_property_descriptor desc[] = {
5. { "createPixelMapTest", nullptr, CreatePixelMapTest, nullptr, nullptr, nullptr, napi_default, nullptr },
6. { "createAlphaPixelMap", nullptr, CreateAlphaPixelMap, nullptr, nullptr, nullptr, napi_default, nullptr },
7. { "transform", nullptr, Transform, nullptr, nullptr, nullptr, napi_default, nullptr },
8. };

10. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
11. return exports;
12. }
13. EXTERN_C_END
```

**Native接口调用**

具体接口说明请参考[Image](../harmonyos-references/capi-image.md)。

在hello.cpp文件中获取JS的资源对象，并转为Native的资源对象，即可调用Native接口，调用方式示例代码如下：

**添加引用文件**

```
1. #include <multimedia/image_framework/image_mdk_common.h>
2. #include <multimedia/image_framework/image_pixel_map_mdk.h>
3. #include <stdlib.h>
```

1. 创建一个 **PixelMap** 对象。

   ```
   1. napi_value CreatePixelMapTest(napi_env env, napi_callback_info info) {
   2. napi_value udfVar = nullptr;
   3. napi_value pixelMap = nullptr;

   5. struct OhosPixelMapCreateOps createOps;
   6. createOps.width = 4;
   7. createOps.height = 6;
   8. createOps.pixelFormat = 4;
   9. createOps.alphaType = 0;
   10. size_t bufferSize = createOps.width * createOps.height * 4;
   11. void *buff = malloc(bufferSize);
   12. if (buff == nullptr) {
   13. return udfVar;
   14. }

   16. char *cc = (char *)buff;
   17. for (int i = 0; i < 96; i++) {
   18. *(cc++) = (char)i;
   19. }
   20. int32_t res = OH_PixelMap_CreatePixelMap(env, createOps, (uint8_t *)buff, bufferSize, &pixelMap);
   21. free(buff);
   22. if (res != IMAGE_RESULT_SUCCESS || pixelMap == nullptr) {
   23. return udfVar;
   24. }
   25. return pixelMap;
   26. }
   ```
2. 根据Alpha通道的信息，来生成一个仅包含Alpha通道信息的 **PixelMap** 对象。

   ```
   1. napi_value CreateAlphaPixelMap(napi_env env, napi_callback_info info) {
   2. napi_value udfVar = nullptr;
   3. napi_value thisVar = nullptr;
   4. napi_value argValue[1] = {0};
   5. size_t argCount = 1;

   7. napi_value alphaPixelMap = nullptr;

   9. napi_get_undefined(env, &udfVar);

   11. if (napi_get_cb_info(env, info, &argCount, argValue, &thisVar, nullptr) != napi_ok || argCount < 1 ||
   12. argValue[0] == nullptr) {
   13. return udfVar;
   14. }
   15. int32_t res = OH_PixelMap_CreateAlphaPixelMap(env, argValue[0], &alphaPixelMap);
   16. if (res != IMAGE_RESULT_SUCCESS || alphaPixelMap == nullptr) {
   17. return udfVar;
   18. }
   19. return alphaPixelMap;
   20. }
   ```
3. 对 **PixelMap** 数据进行处理。

   ```
   1. napi_value Transform(napi_env env, napi_callback_info info) {
   2. napi_value thisVar = nullptr;
   3. napi_value argValue[1] = {0};
   4. size_t argCount = 1;

   6. if (napi_get_cb_info(env, info, &argCount, argValue, &thisVar, nullptr) != napi_ok || argCount < 1 ||
   7. argValue[0] == nullptr) {
   8. return nullptr;
   9. }
   10. napi_value result = nullptr;
   11. napi_get_undefined(env, &result);

   13. // 初始化NativePixelMap对象。
   14. NativePixelMap *native = OH_PixelMap_InitNativePixelMap(env, argValue[0]);
   15. if (native == nullptr) {
   16. return result;
   17. }

   19. // 获取图片信息。
   20. struct OhosPixelMapInfos pixelMapInfo;
   21. OH_PixelMap_GetImageInfo(native, &pixelMapInfo);

   23. // 获取PixelMap对象每行字节数。
   24. int32_t rowBytes;
   25. OH_PixelMap_GetBytesNumberPerRow(native, &rowBytes);

   27. // 获取PixelMap对象是否可编辑的状态。
   28. int32_t editable = 0;
   29. OH_PixelMap_GetIsEditable(native, &editable);

   31. // 获取PixelMap对象是否支持Alpha通道。
   32. int32_t supportAlpha = 0;
   33. OH_PixelMap_IsSupportAlpha(native, &supportAlpha);

   35. // 设置PixelMap对象的Alpha通道。
   36. int32_t alphaAble = 0;
   37. OH_PixelMap_SetAlphaAble(native, alphaAble);

   39. // 获取PixelMap对象像素密度。
   40. int32_t densityG;
   41. OH_PixelMap_GetDensity(native, &densityG);

   43. // 设置PixelMap对象像素密度。
   44. int32_t densityS = 100;
   45. OH_PixelMap_SetDensity(native, densityS);

   47. // 设置PixelMap对象的透明度。
   48. float opacity = 0.5;
   49. OH_PixelMap_SetOpacity(native, opacity);

   51. // 设置缩放比例。
   52. // scaleX: 宽为原来的0.5。
   53. // scaleY: 高为原来的0.5。
   54. float scaleX = 0.5;
   55. float scaleY = 0.5;
   56. OH_PixelMap_Scale(native, scaleX, scaleY);

   58. // 设置偏移。
   59. // translateX: 向下偏移50。
   60. // translateY: 向右偏移50。
   61. float translateX = 50;
   62. float translateY = 50;
   63. OH_PixelMap_Translate(native, translateX, translateY);

   65. // 设置顺时针旋转90度。
   66. float angle = 90;
   67. OH_PixelMap_Rotate(native, angle);

   69. // 设置翻转
   70. // flipX: 水平翻转，0为不翻转，1为翻转。
   71. // flipY: 垂直翻转，0为不翻转，1为翻转。
   72. int32_t flipX = 0;
   73. int32_t flipY = 1;
   74. OH_PixelMap_Flip(native, flipX, flipY);

   76. // 设置裁剪区域。
   77. // cropX: 裁剪起始点横坐标。
   78. // cropY: 裁剪起始点纵坐标。
   79. // cropH: 裁剪高度10，方向为从上往下（裁剪后的图片高度为10）。
   80. // cropW: 裁剪宽度10，方向为从左到右（裁剪后的图片宽度为10）。
   81. int32_t cropX = 1;
   82. int32_t cropY = 1;
   83. int32_t cropW = 10;
   84. int32_t cropH = 10;
   85. OH_PixelMap_Crop(native, cropX, cropY, cropW, cropH);

   87. // 获取PixelMap对象数据的内存地址，并锁定该内存。
   88. void *pixelAddr = nullptr;
   89. OH_PixelMap_AccessPixels(native, &pixelAddr);

   91. // 释放PixelMap对象数据的内存锁。
   92. OH_PixelMap_UnAccessPixels(native);

   94. return result;
   95. }
   ```

**JS侧调用**

1. 打开src\main\cpp\types\libentry\index.d.ts（其中libentry根据工程名生成），导入如下引用文件：

   ```
   1. import { image } from '@kit.ImageKit';

   3. export const createPixelMapTest: () => image.PixelMap;
   4. export const transform: (a: image.PixelMap) => void;
   ```
2. 打开src\main\ets\pages\index.ets, 导入"libentry.so"(根据工程名生成)，调用Native接口，传入JS的资源对象。示例如下：

   ```
   1. import testNapi from 'libentry.so';
   2. import { image } from '@kit.ImageKit';

   4. @Entry
   5. @Component
   6. struct Index {
   7. @State _pixelMap : image.PixelMap | undefined = undefined;

   9. build() {
   10. Row() {
   11. Column() {
   12. Button("PixelMap")
   13. .width(100)
   14. .height(100)
   15. .onClick(() => {
   16. console.info("com.example.native_ndk_api10 button click in");
   17. this._pixelMap = testNapi.createPixelMapTest();
   18. testNapi.transform(this._pixelMap);
   19. })
   20. Image(this._pixelMap)
   21. .width(500)
   22. .height(500)
   23. .objectFit(ImageFit.Cover)
   24. .border({width: 1, color: Color.Blue})
   25. }
   26. .width('100%')
   27. }
   28. .height('100%')
   29. }
   30. }
   ```
