---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-effect-guidelines
title: 使用ImageEffect编辑图片
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(C/C++) > 图片编辑和处理 > 使用ImageEffect编辑图片
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:20+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:e6ed0d22509fd99d91238035b91af0bf00177acf13201410352d8789ce69b52f
---

## 场景介绍

ImageEffect提供了一系列接口用于图像的编辑。开发者可以通过ImageEffect接口处理不同图像输入类型Pixelmap、NativeWindow、NativeBuffer或Uri，获得滤镜处理效果。

针对ImageEffect，常见的开发场景如下：

* 通过ImageEffect提供的Native API接口添加滤镜或滤镜链，设置输入图像，最终生效滤镜效果。
* 通过注册自定义滤镜，实现开发者的定制化滤镜效果。
* 通过EffectFilter提供的Native API接口快速实现单个滤镜的处理效果。

## 接口说明

详细的接口说明请参考[ImageEffect](../harmonyos-references/capi-imageeffect.md)。

## 开发步骤

**添加动态链接库**

CMakeLists.txt中添加以下lib。

```
1. target_link_libraries(entry PUBLIC
2. libace_ndk.z.so
3. libimage_effect.so
4. libpixelmap.so
5. libnative_window.so
6. libnative_buffer.so
7. )
```

根据处理的图像类型添加对应动态链接库：Pixelmap(libpixelmap.so)、NativeWindow(libnative\_window.so)、NativeBuffer(libnative\_buffer.so)

**添加头文件**

```
1. #include <hilog/log.h>
2. #include <multimedia/image_effect/image_effect.h>
3. #include <multimedia/image_effect/image_effect_filter.h>
4. #include <multimedia/image_effect/image_effect_errors.h>
```

### 通过ImageEffect提供的接口生效图像效果

1. 创建ImageEffect实例。

   ```
   1. // 创建imageEffect实例，“ImageEdit”是imageEffect实例别名。
   2. OH_ImageEffect *imageEffect = OH_ImageEffect_Create("ImageEdit");
   ```
2. 添加EffectFilter滤镜。

   ```
   1. // 添加滤镜，获取OH_EffectFilter实例。多次调用该接口可以添加多个滤镜，组成滤镜链。
   2. OH_EffectFilter *filter = OH_ImageEffect_AddFilter(imageEffect, OH_EFFECT_BRIGHTNESS_FILTER);
   3. if (filter == nullptr) {
   4. OH_LOG_ERROR(LOG_APP, "OH_ImageEffect_AddFilter fail!");
   5. return;
   6. }
   7. // 设置滤镜参数, 例如：滤镜强度设置为50。
   8. ImageEffect_Any value = { .dataType = ImageEffect_DataType::EFFECT_DATA_TYPE_FLOAT, .dataValue.floatValue = 50.f };
   9. ImageEffect_ErrorCode errorCode = OH_EffectFilter_SetValue(filter, OH_EFFECT_FILTER_INTENSITY_KEY, &value);
   ```
3. 设置处理数据。

   **场景一：设置OH\_PixelmapNative输入类型。**

   OH\_PixelmapNative的具体使用方法请参考[Pixelmap开发指导](image-pixelmap-operation-native.md)。

   ```
   1. // 设置输入的Pixelmap。
   2. errorCode = OH_ImageEffect_SetInputPixelmap(imageEffect, inputPixelmap);
   3. if (errorCode != ImageEffect_ErrorCode::EFFECT_SUCCESS) {
   4. OH_LOG_ERROR(LOG_APP, "OH_ImageEffect_SetInputPixelmap fail!");
   5. return;
   6. }

   8. // 设置输出的Pixelmap（可选），不调用该接口时会在输入Pixelmap上直接生效滤镜效果。
   9. errorCode = OH_ImageEffect_SetOutputPixelmap(imageEffect, outputPixelmap);
   10. if (errorCode != ImageEffect_ErrorCode::EFFECT_SUCCESS) {
   11. OH_LOG_ERROR(LOG_APP, "OH_ImageEffect_SetOutputPixelmap fail!");
   12. return;
   13. }
   ```

   **场景二：设置OH\_NativeBuffer输入类型。**

   OH\_NativeBuffer的具体使用方法请参考[NativeBuffer开发指导](native-buffer-guidelines.md)。

   ```
   1. // 设置输入的NativeBuffer。
   2. errorCode = OH_ImageEffect_SetInputNativeBuffer(imageEffect, inputNativeBuffer);
   3. if (errorCode != ImageEffect_ErrorCode::EFFECT_SUCCESS) {
   4. OH_LOG_ERROR(LOG_APP, "OH_ImageEffect_SetInputNativeBuffer fail!");
   5. return;
   6. }

   8. // 设置输出的NativeBuffer（可选），不调用该接口时会在输入NativeBuffer上直接生效滤镜效果。
   9. errorCode = OH_ImageEffect_SetOutputNativeBuffer(imageEffect, outputNativeBuffer);
   10. if (errorCode != ImageEffect_ErrorCode::EFFECT_SUCCESS) {
   11. OH_LOG_ERROR(LOG_APP, "OH_ImageEffect_SetOutputNativeBuffer fail!");
   12. return;
   13. }
   ```

   **场景三：设置URI输入类型。**

   ```
   1. // 设置输入的URI。
   2. errorCode = OH_ImageEffect_SetInputUri(imageEffect, inputUri);
   3. if (errorCode != ImageEffect_ErrorCode::EFFECT_SUCCESS) {
   4. OH_LOG_ERROR(LOG_APP, "OH_ImageEffect_SetInputUri fail!");
   5. return;
   6. }
   7. // 设置输出的URI（可选），不调用该接口时会在输入URI上直接生效滤镜效果。
   8. errorCode = OH_ImageEffect_SetOutputUri(imageEffect, outputUri);
   9. if (errorCode != ImageEffect_ErrorCode::EFFECT_SUCCESS) {
   10. OH_LOG_ERROR(LOG_APP, "OH_ImageEffect_SetOutputUri fail!");
   11. return;
   12. }
   ```

   **场景四：设置纹理输入类型。**

   纹理输入场景是使用硬件GPU渲染的高性能场景，此场景下，应用需要提供合法的OpenGL上下文环境，并在正确的环境下，设置参数以及进行渲染操作。

   ```
   1. // 设置输入的纹理ID。
   2. errorCode = OH_ImageEffect_SetInputTextureId(imageEffect, inputTex, ColorSpaceName::SRGB);
   3. if (errorCode != ImageEffect_ErrorCode::EFFECT_SUCCESS) {
   4. OH_LOG_ERROR(LOG_APP, "OH_ImageEffect_SetInputTextureId fail!");
   5. return;
   6. }

   8. // 设置输出的纹理ID, 注意不能与输入是同一块纹理，否则可能产生渲染异常。
   9. errorCode = OH_ImageEffect_SetOutputTextureId(imageEffect, outputTex);
   10. if (errorCode != ImageEffect_ErrorCode::EFFECT_SUCCESS) {
   11. OH_LOG_ERROR(LOG_APP, "OH_ImageEffect_SetOutputTextureId fail!");
   12. return;
   13. }
   ```

   **场景五：设置OHNativeWindow输入类型。**

   以相机预览场景为例来说明OHNativeWindow输入场景。XComponent组件为相机预览流提供的SurfaceId，可在native c++层将SurfaceId转换成OHNativeWindow，下面提供一份代码示例。

   XComponent模块的具体使用方法请参考[XComponent组件参考](../harmonyos-references/ts-basic-components-xcomponent.md)。

   NativeWindow模块的具体使用方法请参考[OHNativeWindow](../harmonyos-references/capi-nativewindow.md)。

   Camera的具体使用方法请参考[Camera预览参考](native-camera-preview.md)。

   (1) 在xxx.ets中添加一个XComponent组件。

   ```
   1. XComponent({
   2. id: 'xcomponentId',
   3. type: 'surface',
   4. controller: this.mXComponentController,
   5. libraryname: 'entry'
   6. })
   7. .onLoad(() => {
   8. // 获取XComponent的SurfaceId。
   9. this.mSurfaceId = this.mXComponentController.getXComponentSurfaceId()

   11. // 调用native接口获取输入SurfaceId。
   12. this.mSurfaceId = imageEffect.getSurfaceId(this.mSurfaceId)

   14. // 调用相机接口启动预览，将获取到的输入SurfaceId传递给相机框架。
   15. // ...
   16. })
   17. .width('100%')
   18. .height('100%')
   ```

   (2) imageEffect.getSurfaceId的native c++层具体实现。

   ```
   1. // 根据SurfaceId创建NativeWindow，注意创建出来的NativeWindow在使用结束后需要主动调用OH_NativeWindow_DestroyNativeWindow进行释放。
   2. uint64_t outputSurfaceId;
   3. std::istrstream iss(outputSurfaceIdStr);
   4. issue >> outputSurfaceId;
   5. OHNativeWindow *outputNativeWindow = nullptr;
   6. int32_t res = OH_NativeWindow_CreateNativeWindowFromSurfaceId(outputSurfaceId, &outputNativeWindow);
   7. if (res != 0) {
   8. OH_LOG_ERROR(LOG_APP, "OH_NativeWindow_CreateNativeWindowFromSurfaceId fail!");
   9. return;
   10. }

   12. // 设置输出显示的Surface。
   13. ImageEffect_ErrorCode errorCode = OH_ImageEffect_SetOutputSurface(imageEffect, outputNativeWindow);
   14. if (errorCode != ImageEffect_ErrorCode::EFFECT_SUCCESS) {
   15. OH_LOG_ERROR(LOG_APP, "OH_ImageEffect_SetOutputSurface fail!");
   16. return;
   17. }
   18. // 获取输入的Surface。注意获取的inputNativeWindow在使用结束后需要主动调用OH_NativeWindow_DestroyNativeWindow进行释放。
   19. OHNativeWindow *inputNativeWindow = nullptr;
   20. errorCode = OH_ImageEffect_GetInputSurface(imageEffect, &inputNativeWindow);
   21. if (errorCode != ImageEffect_ErrorCode::EFFECT_SUCCESS) {
   22. OH_LOG_ERROR(LOG_APP, "OH_ImageEffect_GetInputSurface fail!");
   23. return;
   24. }

   26. // 从获取到输入的NativeWindow中获取SurfaceId。
   27. uint64_t inputSurfaceId = 0;
   28. res = OH_NativeWindow_GetSurfaceId(inputNativeWindow, &inputSurfaceId);
   29. if (res != 0) {
   30. OH_LOG_ERROR(LOG_APP, "OH_NativeWindow_GetSurfaceId fail!");
   31. return;
   32. }

   34. // 将SurfaceId转成字符串进行返回。
   35. std::string inputSurfaceIdStr = std::to_string(inputSurfaceId);
   ```
4. 启动效果器。

   ```
   1. // 执行生效滤镜效果。
   2. errorCode = OH_ImageEffect_Start(imageEffect);
   3. if (errorCode != ImageEffect_ErrorCode::EFFECT_SUCCESS) {
   4. OH_LOG_ERROR(LOG_APP, "OH_ImageEffect_Start fail!");
   5. return;
   6. }
   ```
5. 停止生效效果（可选，仅在输入Surface场景下才有效）。

   ```
   1. // 停止生效滤镜效果。
   2. errorCode = OH_ImageEffect_Stop(imageEffect);
   3. if (errorCode != ImageEffect_ErrorCode::EFFECT_SUCCESS) {
   4. OH_LOG_ERROR(LOG_APP, "OH_ImageEffect_Stop fail!");
   5. return;
   6. }
   ```
6. 序列化效果器（可选）。

   ```
   1. char *info = nullptr;
   2. errorCode = OH_ImageEffect_Save(imageEffect, &info);
   3. if (errorCode != ImageEffect_ErrorCode::EFFECT_SUCCESS) {
   4. OH_LOG_ERROR(LOG_APP, "OH_ImageEffect_Save fail!");
   5. return;
   6. }
   ```
7. 销毁效果器实例。

   ```
   1. // 释放imageEffect实例资源。
   2. errorCode = OH_ImageEffect_Release(imageEffect);
   3. if (errorCode != ImageEffect_ErrorCode::EFFECT_SUCCESS) {
   4. OH_LOG_ERROR(LOG_APP, "OH_ImageEffect_Release fail!");
   5. return;
   6. }
   ```

### 自定义滤镜

以下步骤描述了如何实现并注册自定义滤镜接口：

1. 定义 ImageEffect\_FilterDelegate。

   ```
   1. // 图像信息结构体。
   2. struct EffectBufferInfo {
   3. void *addr = nullptr;
   4. int32_t width = 0;
   5. int32_t height = 0;
   6. int32_t rowSize = 0;
   7. ImageEffect_Format format = ImageEffect_Format::EFFECT_PIXEL_FORMAT_UNKNOWN;
   8. };

   10. // 自定义滤镜具体实现。
   11. ImageEffect_FilterDelegate filterDelegate = {
   12. .setValue = [](OH_EffectFilter *filter, const char *key, const ImageEffect_Any *value) {
   13. // 参数校验，校验成功时返回true，否则返回false。
   14. // ...
   15. return true;
   16. },
   17. .render = [](OH_EffectFilter *filter, OH_EffectBufferInfo *info, OH_EffectFilterDelegate_PushData pushData) {
   18. return Render(filter, info, pushData);
   19. },
   20. .save = [](OH_EffectFilter *filter, char **info) {
   21. // 获取自定义所设置的滤镜参数，其中"Brightness"为自定义滤镜的Key，由开发者自己任意指定。
   22. ImageEffect_Any value;
   23. ImageEffect_ErrorCode errorCode = OH_EffectFilter_GetValue(filter, "Brightness", &value);
   24. if (errorCode != ImageEffect_ErrorCode::EFFECT_SUCCESS) {
   25. OH_LOG_ERROR(LOG_APP, "OH_EffectFilter_GetValue fail!");
   26. return false;
   27. }

   29. // 生成键值对信息。
   30. json values;
   31. values["Brightness"] = value.dataValue.floatValue;
   32. json root;
   33. root["name"] = "CustomBrightness";
   34. root["values"] = values;

   36. // 将json对象转成字符串infoStr。
   37. // ...

   39. // 对*info赋值序列化字符串地址。
   40. *info = infoStr;
   41. return true;
   42. },
   43. .restore = [](const char *info) {
   44. // 创建OH_EffectFilter实例，其中"CustomBrightness"为自定义滤镜的滤镜名。
   45. OH_EffectFilter *filter = OH_EffectFilter_Create("CustomBrightness");
   46. // 解析json字符串info获取key和value。
   47. // ...

   49. // 设置滤镜参数, value为info中按json解析出来的参数。
   50. ImageEffect_ErrorCode errorCode = OH_EffectFilter_SetValue(filter, "Brightness", &value);

   52. // ...
   53. return filter;
   54. }
   55. };
   ```

   其中Render接口的实现分两种场景。

   **场景一：自定义算法可以直接修改info中的像素数据（比如：亮度调节滤镜）。**

   ```
   1. bool Render(OH_EffectFilter *filter, OH_EffectBufferInfo *info, OH_EffectFilterDelegate_PushData pushData)
   2. {
   3. // 获取图像信息具体参数。
   4. EffectBufferInfo inputBufferInfo;
   5. OH_EffectBufferInfo_GetAddr(info, &inputBufferInfo.addr);
   6. OH_EffectBufferInfo_GetWidth(info, &inputBufferInfo.width);
   7. OH_EffectBufferInfo_GetHeight(info, &inputBufferInfo.height);
   8. OH_EffectBufferInfo_GetRowSize(info, &inputBufferInfo.rowSize);
   9. OH_EffectBufferInfo_GetEffectFormat(info, &inputBufferInfo.format);

   11. // 调用自定义滤镜算法。
   12. ApplyCustomAlgo(inputBufferInfo);

   14. // 编辑完成后调用pushData直接传递原图。
   15. pushData(filter, info);
   16. return true;
   17. }
   ```

   **场景二：自定义算法不能直接修改info中的像素数据（比如：裁剪滤镜）。**

   ```
   1. bool Render(OH_EffectFilter *filter, OH_EffectBufferInfo *info, OH_EffectFilterDelegate_PushData pushData)
   2. {
   3. // 获取图像信息具体参数。
   4. EffectBufferInfo inputBufferInfo;
   5. OH_EffectBufferInfo_GetAddr(info, &inputBufferInfo.addr);
   6. OH_EffectBufferInfo_GetWidth(info, &inputBufferInfo.width);
   7. OH_EffectBufferInfo_GetHeight(info, &inputBufferInfo.height);
   8. OH_EffectBufferInfo_GetRowSize(info, &inputBufferInfo.rowSize);
   9. OH_EffectBufferInfo_GetEffectFormat(info, &inputBufferInfo.format);

   11. // 创建输出像素信息。
   12. EffectBufferInfo outputBufferInfo = CreateOutputBufferInfo(inputBufferInfo);

   14. // 调用自定义滤镜算法。
   15. ApplyCustomAlgo(inputBufferInfo, outputBufferInfo);

   17. // 生成outputOhInfo。
   18. OH_EffectBufferInfo *outputOhInfo = OH_EffectBufferInfo_Create();
   19. OH_EffectBufferInfo_SetAddr(outputOhInfo, outputBufferInfo.addr);
   20. OH_EffectBufferInfo_SetWidth(outputOhInfo, outputBufferInfo.width);
   21. OH_EffectBufferInfo_SetHeight(outputOhInfo, outputBufferInfo.height);
   22. OH_EffectBufferInfo_SetRowSize(outputOhInfo, outputBufferInfo.rowSize);
   23. OH_EffectBufferInfo_SetEffectFormat(outputOhInfo, outputBufferInfo.format);

   25. // 编辑完成后调用pushData传递outputOhInfo。
   26. pushData(filter, outputOhInfo);

   28. // 释放资源。
   29. OH_EffectBufferInfo_Release(outputOhInfo);
   30. ReleaseOutputBuffer(outputBufferInfo.addr);

   32. return true;
   33. }
   ```
2. 生成自定义滤镜信息。

   ```
   1. // 创建OH_EffectFilterInfo实例。
   2. OH_EffectFilterInfo *customFilterInfo = OH_EffectFilterInfo_Create();
   3. if (customFilterInfo ==nullptr) {
   4. OH_LOG_ERROR(LOG_APP, "OH_EffectFilter_GetValue fail!");
   5. return;
   6. }

   8. // 设置自定义滤镜滤镜名。
   9. OH_EffectFilterInfo_SetFilterName(customFilterInfo, "CustomBrightness");

   11. // 设置自定义滤镜所支持的内存类型。
   12. ImageEffect_BufferType bufferTypeArray[] = { ImageEffect_BufferType::EFFECT_BUFFER_TYPE_PIXEL };
   13. OH_EffectFilterInfo_SetSupportedBufferTypes(customFilterInfo, sizeof(bufferTypeArray) / sizeof(ImageEffect_BufferType), bufferTypeArray);

   15. // 设置自定义滤镜所支持的像素格式。
   16. ImageEffect_Format formatArray[] = { ImageEffect_Format::EFFECT_PIXEL_FORMAT_RGBA8888 };
   17. OH_EffectFilterInfo_SetSupportedFormats(customFilterInfo, sizeof(formatArray) / sizeof(ImageEffect_Format), formatArray);
   ```
3. 将 ImageEffect\_FilterDelegate 注册到效果器。

   ```
   1. // 注册自定义滤镜。
   2. ImageEffect_ErrorCode errorCode = OH_EffectFilter_Register(customFilterInfo, &filterDelegate);
   3. if (errorCode != ImageEffect_ErrorCode::EFFECT_SUCCESS) {
   4. OH_LOG_ERROR(LOG_APP, "OH_EffectFilter_Register fail!");
   5. return;
   6. }
   ```

### EffectFilter快速实现单个滤镜的处理效果

1. 创建滤镜。

   ```
   1. // 创建滤镜。比如：创建对比度效果器。
   2. OH_EffectFilter *filter = OH_EffectFilter_Create(OH_EFFECT_CONTRAST_FILTER);
   ```
2. 设置滤镜参数。

   ```
   1. // 设置滤镜参数, 滤镜强度设置为50。
   2. ImageEffect_Any value = {.dataType = ImageEffect_DataType::EFFECT_DATA_TYPE_FLOAT, .dataValue.floatValue = 50.f};
   3. ImageEffect_ErrorCode errorCode = OH_EffectFilter_SetValue(filter, OH_EFFECT_FILTER_INTENSITY_KEY, &value);
   4. if (errorCode != ImageEffect_ErrorCode::EFFECT_SUCCESS) {
   5. OH_LOG_ERROR(LOG_APP, "OH_EffectFilter_SetValue fail!");
   6. return;
   7. }
   ```
3. 生效滤镜。

   ```
   1. // 生效滤镜效果。
   2. errorCode = OH_EffectFilter_Render(filter, inputPixelmap, outputPixelmap);
   ```
4. 销毁滤镜实例。

   ```
   1. // 销毁滤镜实例。
   2. errorCode = OH_EffectFilter_Release(filter);
   ```

### 查询能力

* 根据滤镜名查询滤镜信息。

  ```
  1. // 创建OH_EffectFilterInfo实例。
  2. OH_EffectFilterInfo *filterInfo = OH_EffectFilterInfo_Create();
  3. if (filterInfo == nullptr) {
  4. OH_LOG_ERROR(LOG_APP, "OH_EffectFilterInfo_Create fail!");
  5. return;
  6. }

  8. // 根据滤镜名查询滤镜能力信息。
  9. ImageEffect_ErrorCode errorCode = OH_EffectFilter_LookupFilterInfo(OH_EFFECT_BRIGHTNESS_FILTER, filterInfo);
  10. if (errorCode != ImageEffect_ErrorCode::EFFECT_SUCCESS) {
  11. OH_LOG_ERROR(LOG_APP, "OH_EffectFilter_LookupFilterInfo fail!");
  12. return;
  13. }

  15. // 从滤镜能力信息中获取滤镜名。
  16. char *name = nullptr;
  17. OH_EffectFilterInfo_GetFilterName(filterInfo, &name);

  19. // 获取支持的内存类型。
  20. uint32_t supportedBufferTypesCnt = 0;
  21. ImageEffect_BufferType *bufferTypeArray = nullptr;
  22. OH_EffectFilterInfo_GetSupportedBufferTypes(filterInfo, &supportedBufferTypesCnt, &bufferTypeArray);

  24. // 获取支持的像素类型信息。
  25. uint32_t supportedFormatsCnt = 0;
  26. ImageEffect_Format *formatArray = nullptr;
  27. OH_EffectFilterInfo_GetSupportedFormats(filterInfo, supportedFormatsCnt, &formatArray);

  29. // 销毁OH_EffectFilterInfo实例。
  30. OH_EffectFilterInfo_Release(filterInfo);
  ```
* 根据条件查询满足条件的滤镜。

  ```
  1. // 查询所有的Filter，需要主动进行资源释放。
  2. ImageEffect_FilterNames *filterNames = OH_EffectFilter_LookupFilters("Default");

  4. // ...

  6. // 释放FilterNames虚拟内存资源。
  7. OH_EffectFilter_ReleaseFilterNames();
  ```
