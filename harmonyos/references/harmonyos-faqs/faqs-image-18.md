---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-18
title: 如何将C++侧接收的PixelMap转换成cv::mat格式
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 如何将C++侧接收的PixelMap转换成cv::mat格式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:42+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:317b55427a2b24aaa52250e39eb4fe5bdd1a826eb1cf630209c03b5ba70e7232
---

## 解决措施

将PixelMap转换成cv::mat有两种方法：

* 将PixelMap的arraybuffer转换成cv::mat。
* 使用OH\_PixelMap\_AccessPixels获取PixelMap的内存地址，将这个内存地址中的数据转换为cv::mat。

上述两种方法都需确保PixelMap的格式与OpenCV中Mat的格式一致，否则会导致色彩偏差。

示例代码如下：

ArkTS侧传递参数：

```ts
import cPixelMapToMat from 'libcpixelmaptomat.so';
import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

@Entry
@Component
struct Index {
  @State pixelMap: image.PixelMap | undefined = undefined

  async arrayBufferToMat() {
    if (this.pixelMap == undefined || this.pixelMap){
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      let resourceManager = context.resourceManager
      let imageArray = await resourceManager.getMediaContent($r('app.media.sample10'));
      let pixelBuffer = new Uint8Array(imageArray).buffer as Object as ArrayBuffer
      console.info("pixelBuffer length: " + pixelBuffer.byteLength);
      let imageResource = image.createImageSource(pixelBuffer);
      let opts: image.DecodingOptions = {
        editable: true,
        desiredPixelFormat: image.PixelMapFormat.RGBA_8888
      }
      this.pixelMap = await imageResource.createPixelMap(opts);
    }

    const readBuffer: ArrayBuffer = new ArrayBuffer(this.pixelMap.getPixelBytesNumber()); // Obtain the array buffer of the pixelmap
    console.info("readBuffer length: " + readBuffer.byteLength);
    this.pixelMap.readPixelsToBuffer(readBuffer).then(() => {
      console.info("No Error!")
    }).catch((err: BusinessError) => {
      console.error("Error! " + err.message)
    })
    const dir = getContext(this).filesDir;
    console.info('save path: ' + dir);
    cPixelMapToMat.arrayBufferToMat(this.pixelMap, readBuffer, dir);
  }

  async accessToMat(){
    if (this.pixelMap == undefined || this.pixelMap) {
      let resourceManager = getContext(this).resourceManager
      let imageArray = await resourceManager.getMediaContent($r('app.media.sample14'));
      let pixelBuffer = new Uint8Array(imageArray).buffer as Object as ArrayBuffer
      console.info("pixelBuffer length: " + pixelBuffer.byteLength);
      let imageResource = image.createImageSource(pixelBuffer);
      let opts: image.DecodingOptions = {
        editable: true,
        desiredPixelFormat: image.PixelMapFormat.RGBA_8888
      }
      this.pixelMap = await imageResource.createPixelMap(opts);
    }

    const dir = getContext(this).filesDir;
    console.info('save path: ' + dir);
    cPixelMapToMat.accessToMat(this.pixelMap, dir);
  }

  build() {
    Row() {
      Column() {
        Image(this.pixelMap)
          .width(200)
          .height(200)
        Button('ArrayBufferToMat')
          .onClick(() => {
            this.arrayBufferToMat();
          })

        Button('AccessToMat')
          .onClick(() => {
            this.accessToMat();
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

* 方案一：将arraybuffer转换成cv::mat代码如下：

  ```cpp
  #include "napi/native_api.h"
  #include <multimedia/image_framework/image_mdk.h>
  #include <multimedia/image_framework/image_mdk_common.h>
  #include <multimedia/image_framework/image_pixel_map_mdk.h>
  #include <multimedia/image_framework/image_pixel_map_napi.h>
  #include "hilog/log.h"
  #include <opencv2/opencv.hpp>
  #include <bits/alltypes.h>

  static napi_value ArrayBufferToMat(napi_env env, napi_callback_info info) {
      size_t argc = 3;
      napi_value args[3] = {nullptr};
      napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

      napi_value error;
      napi_create_int32(env, -1, &error);

      // Initialize PixelMap object data 
      NativePixelMap *native = OH_PixelMap_InitNativePixelMap(env, args[0]);
      if (native == nullptr) {
          return error;
      }
      // Obtaining Image Information
      struct OhosPixelMapInfos pixelMapInfos;
      if (OH_PixelMap_GetImageInfo(native, &pixelMapInfos) != IMAGE_RESULT_SUCCESS) {
          OH_LOG_Print(LOG_APP, LOG_ERROR, 0xFF00, "Test", "Pure : -1");
          return error;
      }
      // Obtains the buffer
      napi_value buffer = args[1];
      napi_valuetype valueType;
      napi_typeof(env, buffer, &valueType);
      if (valueType == napi_object) {
          bool isArrayBuffer = false;
          napi_is_arraybuffer(env, buffer, &isArrayBuffer);
          if (!isArrayBuffer) {
              napi_throw_error(env, "EINVAL", "Error");
          }
      }

      void *data = nullptr;
      size_t byteLength = 0;
      napi_get_arraybuffer_info(env, buffer, &data, &byteLength);
      int32_t *saveBuffer = (int32_t *)(data);

      // Convert to Mat
      cv::Mat originMat(pixelMapInfos.height, pixelMapInfos.width, CV_8UC4, saveBuffer);
      if (!originMat.data) {
          OH_LOG_Print(LOG_APP, LOG_ERROR, 0xFF00, "Read Image", "Pure : -1");
          return error;
      }

      // openCV defaults to BGRA or BGR. If the pixelmap is not created in one of these formats, a format conversion is required
      cv::Mat saveMat;
      cv::cvtColor(originMat, saveMat, cv::COLOR_BGRA2RGBA);
      char pathArray[1024];
      size_t length;
      napi_get_value_string_utf8(env, args[2], pathArray, 1024, &length);
      std::string path(pathArray);
      path += "/buffer.jpg";
      if (!cv::imwrite(path, saveMat)) {
          OH_LOG_Print(LOG_APP, LOG_ERROR, 0xFF00, "Write Image", "Pure : -1");
          return error;
      }

      napi_value res;
      napi_create_int32(env, 1, &res);
      return res;
  }
  ```
* 方案二：使用OH\_PixelMap\_AccessPixels获取PixelMap的内存地址，将这个内存地址中的数据转换为cv::mat的代码如下：

  ```cpp
  static napi_value AccessToMat(napi_env env, napi_callback_info info) {
      size_t argc = 2;
      napi_value args[2] = {nullptr};
      napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

      napi_value error;
      napi_create_int32(env, -1, &error);

      NativePixelMap *native = OH_PixelMap_InitNativePixelMap(env, args[0]);
      if (native == nullptr) {
          return error;
      }
      struct OhosPixelMapInfos pixelMapInfos;
      if (OH_PixelMap_GetImageInfo(native, &pixelMapInfos) != IMAGE_RESULT_SUCCESS) {
          OH_LOG_Print(LOG_APP, LOG_ERROR, 0xFF00, "Test", "Pure : -1");
          return error;
      }

      void *pixel;
      // Obtain the memory address of the NativePixelMap object and lock the memory
      OH_PixelMap_AccessPixels(native, &pixel);

      // Convert to Mat, pay attention to alignment, so rowSize needs to be passed in
      cv::Mat originMat(pixelMapInfos.height, pixelMapInfos.width, CV_8UC4, pixel, pixelMapInfos.rowSize);
      if (!originMat.data) {
          OH_LOG_Print(LOG_APP, LOG_ERROR, 0xFF00, "Read Image", "Pure : -1");
          return error;
      }

      // openCV defaults to BGRA or BGR. If the pixelmap is not created in one of these formats, a format conversion is required
      cv::Mat saveMat;
      cv::cvtColor(originMat, saveMat, cv::COLOR_BGRA2RGBA);
      char pathArray[1024];
      size_t length;
      napi_get_value_string_utf8(env, args[1], pathArray, 1024, &length);
      std::string path(pathArray);
      path += "/access.jpg";
      if (!cv::imwrite(path, saveMat)) {
          OH_LOG_Print(LOG_APP, LOG_ERROR, 0xFF00, "Write Image", "Pure : -1");
          return error;
      }

      napi_value res;
      napi_create_int32(env, 1, &res);
      return res;
  }
  ```

在HarmonyOS开发中，针对图库支持硬解码的操作，需要指定图像的内存空间大小。OH\_PixelMap\_AccessPixels() 获取图片的内存地址并锁定该内存。实际图像的大小需要按 lineStride 对齐。因此，在构造成 mat 时，需指定 lineStride 对齐。lineStride即 rowSize。可以使用 OH\_GetImageInfo 获取 imageInfo，其中包含 width、height 和 rowSize 等信息。
