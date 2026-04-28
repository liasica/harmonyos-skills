---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-transformation-native
title: 图像变换
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(依赖JS对象)(不再推荐) > 图像变换
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:23+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:a32c8002f131a75bf392d041ead50723a999f5ae4ecbfcbd7512c03094207c65
---

说明

当前开发指导使用的接口为[Image](../harmonyos-references/capi-image.md)模块下的C API，可完成图片编解码，图片接收器，处理图像数据等功能。这部分API在API version 11之前发布，在后续的版本不再增加新功能，**不再推荐使用**。

开发者可使用[Image\_NativeModule](../harmonyos-references/capi-image-nativemodule.md)模块下的C API，不仅提供上述图片框架基础功能，还可以完成多图编解码等新特性，相关开发指导请参考[图片开发指导(C/C++)](image-source-c.md)节点下的内容。这部分API从API version 12开始支持，并将持续演进，**推荐开发者使用**。

两套C API不建议同时使用，在部分场景下存在不兼容的问题。

开发者可以通过本指导了解如何使用Native Image的接口完成图像变换。

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
5. { "testGetImageInfo", nullptr, TestGetImageInfo, nullptr, nullptr, nullptr, napi_default, nullptr },
6. { "testAccessPixels", nullptr, TestAccessPixels, nullptr, nullptr, nullptr, napi_default, nullptr },
7. { "testUnAccessPixels", nullptr, TestUnAccessPixels, nullptr, nullptr, nullptr, napi_default, nullptr },
8. };

10. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
11. return exports;
12. }
13. EXTERN_C_END
```

**Native接口调用**

具体接口说明请参考[Image](../harmonyos-references/capi-image.md)。

在hello.cpp文件中获取JS的资源对象，并转为Native的资源对象，即可调用Native接口，调用方式示例代码如下：

打开src/main/cpp/hello.cpp，添加引用文件。

```
1. #include<multimedia/image_framework/image_pixel_map_napi.h>
```

1. 获取**PixelMap**的信息，并记录信息到**OhosPixelMapInfo**结构中。

   ```
   1. static napi_value TestGetImageInfo(napi_env env, napi_callback_info info)
   2. {
   3. napi_value result = nullptr;
   4. napi_get_undefined(env, &result);

   6. napi_value thisVar = nullptr;
   7. napi_value argValue[1] = {0};
   8. size_t argCount = 1;

   10. napi_get_cb_info(env, info, &argCount, argValue, &thisVar, nullptr);

   12. OHOS::Media::OhosPixelMapInfo pixelMapInfo;
   13. OHOS::Media::OH_GetImageInfo(env, argValue[0], &pixelMapInfo);
   14. return result;
   15. }
   ```
2. 获取**PixelMap**对象数据的内存地址，并锁定该内存。

   ```
   1. static napi_value TestAccessPixels(napi_env env, napi_callback_info info)
   2. {
   3. napi_value result = nullptr;
   4. napi_get_undefined(env, &result);

   6. napi_value thisVar = nullptr;
   7. napi_value argValue[1] = {0};
   8. size_t argCount = 1;

   10. napi_get_cb_info(env, info, &argCount, argValue, &thisVar, nullptr);

   12. void* addrPtr = nullptr;
   13. OHOS::Media::OH_AccessPixels(env, argValue[0], &addrPtr);
   14. return result;
   15. }
   ```
3. 释放**PixelMap**对象数据的内存锁。

   ```
   1. static napi_value TestUnAccessPixels(napi_env env, napi_callback_info info)
   2. {
   3. napi_value result = nullptr;
   4. napi_get_undefined(env, &result);

   6. napi_value thisVar = nullptr;
   7. napi_value argValue[1] = {0};
   8. size_t argCount = 1;

   10. napi_get_cb_info(env, info, &argCount, argValue, &thisVar, nullptr);

   12. OHOS::Media::OH_UnAccessPixels(env, argValue[0]);
   13. return result;
   14. }
   ```

**JS侧调用**

1. 打开src\main\cpp\types\libentry\index.d.ts(其中libentry根据工程名生成)，导入如下引用文件：

   ```
   1. import { image } from '@kit.ImageKit';
   2. export const add:(a: number, b: number) => image.PixelMap;
   3. export const transform: (a: image.PixelMap) => image.PixelMap;
   4. export const testGetImageInfo: (a: image.PixelMap) => image.PixelMap;
   5. export const testAccessPixels: (a: image.PixelMap) => image.PixelMap;
   6. export const testUnAccessPixels: (a: image.PixelMap) => image.PixelMap;
   ```
2. 打开src\main\ets\pages\index.ets, 导入"libentry.so"(根据工程名生成)；调用Native接口，传入JS的资源对象。示例如下：

   ```
   1. import testNapi from 'libentry.so';
   2. import { image } from '@kit.ImageKit';

   4. @Entry
   5. @Component
   6. struct Index {
   7. @State message: string = 'IMAGE';
   8. @State _PixelMap : image.PixelMap | undefined = undefined;

   10. build() {
   11. Row() {
   12. Column() {
   13. Button(this.message)
   14. .fontSize(50)
   15. .fontWeight(FontWeight.Bold)
   16. .onClick(() => {
   17. const color : ArrayBuffer = new ArrayBuffer(96);
   18. let opts: image.InitializationOptions = { alphaType: 0, editable: true, pixelFormat: 4, scaleMode: 1, size: { height: 4, width: 6 } };
   19. image.createPixelMap(color, opts)
   20. .then( (pixelmap : image.PixelMap) => {
   21. this._PixelMap = pixelmap;
   22. testNapi.testGetImageInfo(this._PixelMap);
   23. console.info("Test GetImageInfo success");

   25. testNapi.testAccessPixels(this._PixelMap);
   26. console.info("Test AccessPixels success");

   28. testNapi.testUnAccessPixels(this._PixelMap);
   29. console.info("Test UnAccessPixels success");
   30. })
   31. })
   32. }
   33. .width('100%')
   34. }
   35. .height('100%')
   36. }
   37. }
   ```
