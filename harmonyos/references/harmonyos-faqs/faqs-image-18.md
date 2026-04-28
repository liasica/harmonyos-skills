---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-18
title: 如何将C++侧接收的PixelMap转换成cv::mat格式
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 如何将C++侧接收的PixelMap转换成cv::mat格式
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:32+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:183986dd064605ad7885bcc1d97a2e4aba7d953b8372d428f4f02eab5b58e7f1
---

**解决措施：**

将PixelMap转换成cv::mat有两种方法：

* 将PixelMap的arraybuffer转换成cv::mat。
* 使用OH\_PixelMap\_AccessPixels获取PixelMap的内存地址，将这个内存地址中的数据转换为cv::mat。

上述两种方法都需确保PixelMap的格式与OpenCV中Mat的格式一致，否则会导致色彩偏差。

示例代码如下：

ArkTS侧传递参数：

```
1. import cPixelMapToMat from 'libcpixelmaptomat.so';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { image } from '@kit.ImageKit';

5. @Entry
6. @Component
7. struct Index {
8. @State pixelMap: image.PixelMap | undefined = undefined

10. async arrayBufferToMat() {
11. if (this.pixelMap == undefined || this.pixelMap){
12. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
13. let resourceManager = context.resourceManager
14. let imageArray = await resourceManager.getMediaContent($r('app.media.sample10'));
15. let pixelBuffer = new Uint8Array(imageArray).buffer as Object as ArrayBuffer
16. console.info("pixelBuffer length: " + pixelBuffer.byteLength);
17. let imageResource = image.createImageSource(pixelBuffer);
18. let opts: image.DecodingOptions = {
19. editable: true,
20. desiredPixelFormat: image.PixelMapFormat.RGBA_8888
21. }
22. this.pixelMap = await imageResource.createPixelMap(opts);
23. }

25. const readBuffer: ArrayBuffer = new ArrayBuffer(this.pixelMap.getPixelBytesNumber()); // Obtain the array buffer of the pixelmap
26. console.info("readBuffer length: " + readBuffer.byteLength);
27. this.pixelMap.readPixelsToBuffer(readBuffer).then(() => {
28. console.info("No Error!")
29. }).catch((err: BusinessError) => {
30. console.error("Error! " + err.message)
31. })
32. const dir = getContext(this).filesDir;
33. console.info('save path: ' + dir);
34. cPixelMapToMat.arrayBufferToMat(this.pixelMap, readBuffer, dir);
35. }

37. async accessToMat(){
38. if (this.pixelMap == undefined || this.pixelMap) {
39. let resourceManager = getContext(this).resourceManager
40. let imageArray = await resourceManager.getMediaContent($r('app.media.sample14'));
41. let pixelBuffer = new Uint8Array(imageArray).buffer as Object as ArrayBuffer
42. console.info("pixelBuffer length: " + pixelBuffer.byteLength);
43. let imageResource = image.createImageSource(pixelBuffer);
44. let opts: image.DecodingOptions = {
45. editable: true,
46. desiredPixelFormat: image.PixelMapFormat.RGBA_8888
47. }
48. this.pixelMap = await imageResource.createPixelMap(opts);
49. }

51. const dir = getContext(this).filesDir;
52. console.info('save path: ' + dir);
53. cPixelMapToMat.accessToMat(this.pixelMap, dir);
54. }

56. build() {
57. Row() {
58. Column() {
59. Image(this.pixelMap)
60. .width(200)
61. .height(200)
62. Button('ArrayBufferToMat')
63. .onClick(() => {
64. this.arrayBufferToMat();
65. })

67. Button('AccessToMat')
68. .onClick(() => {
69. this.accessToMat();
70. })
71. }
72. .width('100%')
73. }
74. .height('100%')
75. }
76. }
```

[Index.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ImageKit/CPixelMapToMat/src/main/ets/pages/Index.ets#L21-L96)

方案一：将arraybuffer转换成cv::mat代码如下：

```
1. #include "napi/native_api.h"
2. #include <multimedia/image_framework/image_mdk.h>
3. #include <multimedia/image_framework/image_mdk_common.h>
4. #include <multimedia/image_framework/image_pixel_map_mdk.h>
5. #include <multimedia/image_framework/image_pixel_map_napi.h>
6. #include "hilog/log.h"
7. #include <opencv2/opencv.hpp>
8. #include <bits/alltypes.h>

10. static napi_value ArrayBufferToMat(napi_env env, napi_callback_info info) {
11. size_t argc = 3;
12. napi_value args[3] = {nullptr};
13. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

15. napi_value error;
16. napi_create_int32(env, -1, &error);

18. // Initialize PixelMap object data
19. NativePixelMap *native = OH_PixelMap_InitNativePixelMap(env, args[0]);
20. if (native == nullptr) {
21. return error;
22. }
23. // Obtaining Image Information
24. struct OhosPixelMapInfos pixelMapInfos;
25. if (OH_PixelMap_GetImageInfo(native, &pixelMapInfos) != IMAGE_RESULT_SUCCESS) {
26. OH_LOG_Print(LOG_APP, LOG_ERROR, 0xFF00, "Test", "Pure : -1");
27. return error;
28. }
29. // Obtains the buffer
30. napi_value buffer = args[1];
31. napi_valuetype valueType;
32. napi_typeof(env, buffer, &valueType);
33. if (valueType == napi_object) {
34. bool isArrayBuffer = false;
35. napi_is_arraybuffer(env, buffer, &isArrayBuffer);
36. if (!isArrayBuffer) {
37. napi_throw_error(env, "EINVAL", "Error");
38. }
39. }

41. void *data = nullptr;
42. size_t byteLength = 0;
43. napi_get_arraybuffer_info(env, buffer, &data, &byteLength);
44. int32_t *saveBuffer = (int32_t *)(data);

46. // Convert to Mat
47. cv::Mat originMat(pixelMapInfos.height, pixelMapInfos.width, CV_8UC4, saveBuffer);
48. if (!originMat.data) {
49. OH_LOG_Print(LOG_APP, LOG_ERROR, 0xFF00, "Read Image", "Pure : -1");
50. return error;
51. }

53. // openCV defaults to BGRA or BGR. If the pixelmap is not created in one of these formats, a format conversion is required
54. cv::Mat saveMat;
55. cv::cvtColor(originMat, saveMat, cv::COLOR_BGRA2RGBA);
56. char pathArray[1024];
57. size_t length;
58. napi_get_value_string_utf8(env, args[2], pathArray, 1024, &length);
59. std::string path(pathArray);
60. path += "/buffer.jpg";
61. if (!cv::imwrite(path, saveMat)) {
62. OH_LOG_Print(LOG_APP, LOG_ERROR, 0xFF00, "Write Image", "Pure : -1");
63. return error;
64. }

66. napi_value res;
67. napi_create_int32(env, 1, &res);
68. return res;
69. }
```

[napi\_init.cpp](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ImageKit/CPixelMapToMat/src/main/cpp/napi_init.cpp#L21-L89)

方案二：使用OH\_PixelMap\_AccessPixels获取PixelMap的内存地址，将这个内存地址中的数据转换为cv::mat的代码如下：

```
1. static napi_value AccessToMat(napi_env env, napi_callback_info info) {
2. size_t argc = 2;
3. napi_value args[2] = {nullptr};
4. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

6. napi_value error;
7. napi_create_int32(env, -1, &error);

9. NativePixelMap *native = OH_PixelMap_InitNativePixelMap(env, args[0]);
10. if (native == nullptr) {
11. return error;
12. }
13. struct OhosPixelMapInfos pixelMapInfos;
14. if (OH_PixelMap_GetImageInfo(native, &pixelMapInfos) != IMAGE_RESULT_SUCCESS) {
15. OH_LOG_Print(LOG_APP, LOG_ERROR, 0xFF00, "Test", "Pure : -1");
16. return error;
17. }

19. void *pixel;
20. // Obtain the memory address of the NativePixelMap object and lock the memory
21. OH_PixelMap_AccessPixels(native, &pixel);

23. // Convert to Mat, pay attention to alignment, so rowSize needs to be passed in
24. cv::Mat originMat(pixelMapInfos.height, pixelMapInfos.width, CV_8UC4, pixel, pixelMapInfos.rowSize);
25. if (!originMat.data) {
26. OH_LOG_Print(LOG_APP, LOG_ERROR, 0xFF00, "Read Image", "Pure : -1");
27. return error;
28. }

30. // openCV defaults to BGRA or BGR. If the pixelmap is not created in one of these formats, a format conversion is required
31. cv::Mat saveMat;
32. cv::cvtColor(originMat, saveMat, cv::COLOR_BGRA2RGBA);
33. char pathArray[1024];
34. size_t length;
35. napi_get_value_string_utf8(env, args[1], pathArray, 1024, &length);
36. std::string path(pathArray);
37. path += "/access.jpg";
38. if (!cv::imwrite(path, saveMat)) {
39. OH_LOG_Print(LOG_APP, LOG_ERROR, 0xFF00, "Write Image", "Pure : -1");
40. return error;
41. }

43. napi_value res;
44. napi_create_int32(env, 1, &res);
45. return res;
46. }
```

[napi\_init.cpp](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ImageKit/CPixelMapToMat/src/main/cpp/napi_init.cpp#L93-L138)

在HarmonyOS开发中，针对图库支持硬解码的操作，需要指定图像的内存空间大小。OH\_PixelMap\_AccessPixels() 获取图片的内存地址并锁定该内存。实际图像的大小需要按 lineStride 对齐。因此，在构造成 mat 时，需指定 lineStride 对齐。lineStride即 rowSize。可以使用 OH\_GetImageInfo 获取 imageInfo，其中包含 width、height 和 rowSize 等信息。
