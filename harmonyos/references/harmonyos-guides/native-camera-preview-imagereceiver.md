---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-preview-imagereceiver
title: 预览流二次处理(C/C++)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(C/C++) > 预览流二次处理(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8d81540bd958e9fb38fe6702ec5af73ec444c45b3666a5e781b77aed31395228
---

通过ImageReceiver创建预览输出，获取预览流实时数据，以供后续进行图像二次处理，比如应用可以对其添加滤镜算法等。

## 开发步骤

详细的API说明请参考[OH\_Camera](../harmonyos-references/capi-oh-camera.md)。

1. 导入NDK接口，接口中提供了相机相关的属性和方法，导入方法如下。

   ```
   1. #include <cstdint>
   2. #include <cstdlib>
   3. #include "hilog/log.h"
   4. #include <memory>
   5. #include <new>
   6. #include <multimedia/image_framework/image/image_native.h>
   7. #include <multimedia/image_framework/image/image_receiver_native.h>
   8. #include "ohcamera/camera.h"
   9. #include "ohcamera/camera_input.h"
   10. #include "ohcamera/camera_device.h"
   11. #include "ohcamera/capture_session.h"
   12. #include "ohcamera/photo_output.h"
   13. #include "ohcamera/preview_output.h"
   14. #include "ohcamera/video_output.h"
   15. #include "ohcamera/camera_manager.h"

   17. #include <multimedia/media_library/media_asset_manager_capi.h>
   18. #include <multimedia/media_library/media_asset_change_request_capi.h>
   19. #include <multimedia/media_library/media_access_helper_capi.h>
   20. #include <multimedia/image_framework/image/image_packer_native.h>
   ```

   [camera\_manager.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/NDKPreviewImageSample/entry/src/main/cpp/camera_manager.h#L19-L40)
2. 在CMake脚本中链接相关动态库。

   ```
   1. target_link_libraries(entry PUBLIC
   2. libace_napi.z.so
   3. libhilog_ndk.z.so
   4. libohimage.so
   5. libimage_receiver.so
   6. libnative_image.so
   7. libohcamera.so
   8. libnative_buffer.so
   9. )
   ```
3. 初始化图片接收器[ImageReceiver](image-receiver-c.md)实例，获取SurfaceId。

   通过image的OH\_ImageReceiverNative\_Create方法创建OH\_ImageReceiverNative实例，再通过实例的OH\_ImageReceiverNative\_GetReceivingSurfaceId方法获取SurfaceId。

   ```
   1. void InitImageReceiver(uint64_t &receiverSurfaceID)
   2. {
   3. OH_ImageReceiverOptions *options = nullptr;
   4. // 注意捕获错误码处理异常及对象判空，当前示例仅展示调用流程。
   5. // 设置图片参数。
   6. Image_ErrorCode errCode = OH_ImageReceiverOptions_Create(&options);
   7. if (errCode != IMAGE_SUCCESS || options == nullptr) {
   8. OH_LOG_ERROR(LOG_APP, "OH_ImageReceiverOptions_Create call failed");
   9. return;
   10. }
   11. Image_Size imgSize;
   12. imgSize.width = PREVIEW_WIDTH; // 创建预览流的宽。
   13. imgSize.height = PREVIEW_HEIGHT; // 创建预览流的高。
   14. int32_t capacity = 8; // BufferQueue里最大Image数量，推荐填写8。
   15. errCode = OH_ImageReceiverOptions_SetSize(options, imgSize);
   16. if (errCode != IMAGE_SUCCESS) {
   17. OH_LOG_ERROR(LOG_APP, "OH_ImageReceiverOptions_SetSize call failed");
   18. }
   19. errCode = OH_ImageReceiverOptions_SetCapacity(options, capacity);
   20. if (errCode != IMAGE_SUCCESS) {
   21. OH_LOG_ERROR(LOG_APP, "OH_ImageReceiverOptions_SetCapacity call failed");
   22. }
   23. // 创建OH_ImageReceiverNative对象。
   24. OH_ImageReceiverNative *receiver = nullptr;
   25. errCode = OH_ImageReceiverNative_Create(options, &receiver);
   26. if (errCode != IMAGE_SUCCESS || receiver == nullptr) {
   27. OH_LOG_ERROR(LOG_APP, "OH_ImageReceiverNative_Create call failed");
   28. return;
   29. }

   31. errCode = OH_ImageReceiverNative_On(receiver, CallbackReadNextImage);
   32. if (errCode != IMAGE_SUCCESS) {
   33. OH_LOG_ERROR(LOG_APP, "%{public}s image receiver on failed, errCode: %{public}d.", __func__, errCode);
   34. OH_ImageReceiverOptions_Release(options);
   35. OH_ImageReceiverNative_Release(receiver);
   36. return;
   37. }
   38. // 获取OH_ImageReceiverNative对象的SurfaceId。
   39. errCode = OH_ImageReceiverNative_GetReceivingSurfaceId(receiver, &receiverSurfaceID);
   40. if (errCode != IMAGE_SUCCESS) {
   41. OH_LOG_ERROR(LOG_APP, "OH_ImageReceiverNative_GetReceivingSurfaceId call failed");
   42. } else {
   43. OH_LOG_INFO(LOG_APP, "receiver surfaceID:%{public}lu", receiverSurfaceID);
   44. }
   45. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/NDKPreviewImageSample/entry/src/main/cpp/napi_init.cpp#L177-L223)
4. 通过上一步获取到的SurfaceId创建预览流（在创建预览流之前需要将SurfaceId类型转成char \*），参考[预览(C/C++)](native-camera-preview.md)步骤4。
5. 创建会话，使能会话，参考[会话管理(C/C++)](native-camera-session-management.md)。
6. 注册ImageReceiver图片接收器的回调，监听获取每帧上报图像内容。

   ```
   1. void copyBuffer(OH_NativeBuffer *srcBuffer, size_t srcSize, OHNativeWindowBuffer *dstBuffer)
   2. {
   3. OH_LOG_INFO(LOG_APP, "ImageReceiverNativeCTest %{public}s IN", __func__);
   4. void *srcVir = nullptr;
   5. OH_NativeBuffer_Map(srcBuffer, &srcVir);
   6. BufferHandle *bufferHandle = OH_NativeWindow_GetBufferHandleFromNative(dstBuffer);
   7. OH_LOG_INFO(LOG_APP,
   8. "ImageReceiverNativeCTest %{public}s bufferHandle info fd= %{public}d , width= %{public}d, "
   9. "height=%{public}d, stride= %{public}d, size= %{public}d, format= %{public}d, usage= %{public}lu",
   10. __func__, bufferHandle->fd, bufferHandle->width, bufferHandle->height, bufferHandle->stride, bufferHandle->size,
   11. bufferHandle->format, bufferHandle->usage);

   13. void *mappedAddr =
   14. mmap(bufferHandle->virAddr, bufferHandle->size, PROT_READ | PROT_WRITE, MAP_SHARED, bufferHandle->fd, 0);
   15. std::memcpy(static_cast<unsigned char *>(mappedAddr), static_cast<unsigned char *>(srcVir), srcSize);
   16. munmap(mappedAddr, bufferHandle->size);

   18. OH_NativeBuffer_Unmap(srcBuffer);
   19. OH_LOG_INFO(LOG_APP, "ImageReceiverNativeCTest %{public}s SUCCESS", __func__);
   20. }

   22. void ShowImage(OH_ImageNative *image)
   23. {
   24. OH_LOG_INFO(LOG_APP, "ImageReceiverNativeCTest %{public}s IN", __func__);
   25. uint64_t xComponentSurfaceId = std::stoull(g_xComponentSurfaceIdSlave);
   26. OH_LOG_ERROR(LOG_APP, "ImageReceiverNativeCTest %{public}s XComponentId is : %{public}lu.", __func__,
   27. xComponentSurfaceId);
   28. OHNativeWindow *nativeWindow = nullptr;
   29. int32_t res = OH_NativeWindow_CreateNativeWindowFromSurfaceId(xComponentSurfaceId, &nativeWindow);
   30. if (res != 0) {
   31. OH_LOG_ERROR(LOG_APP,
   32. "ShowImage CreateNativeWindowFromSurfaceId failed, errCode: %{public}d.", res);
   33. return;
   34. }

   36. // 关键：调整nativeWindow大小及format，需要与image的大小、format保持一致。
   37. res = OH_NativeWindow_NativeWindowHandleOpt(nativeWindow, SET_BUFFER_GEOMETRY, g_imageWidth, g_imageHeight);
   38. res = OH_NativeWindow_NativeWindowHandleOpt(nativeWindow, SET_FORMAT, NATIVEBUFFER_PIXEL_FMT_YCRCB_420_SP); // NV21
   39. // 设置旋转角度，后置默认旋转90，则需要将nativeWindow旋转270度，前置默认270，则需要将nativeWindow旋转90度。
   40. if (g_isFront) {
   41. res = OH_NativeWindow_NativeWindowHandleOpt(nativeWindow, SET_TRANSFORM, NATIVEBUFFER_FLIP_V_ROT90);
   42. } else {
   43. res = OH_NativeWindow_NativeWindowHandleOpt(nativeWindow, SET_TRANSFORM, NATIVEBUFFER_ROTATE_270);
   44. }

   46. OH_NativeBuffer *imageBuffer = nullptr;
   47. Image_ErrorCode errCode = OH_ImageNative_GetByteBuffer(image, g_jpegComponent, &imageBuffer);
   48. if (errCode != IMAGE_SUCCESS) {
   49. OH_LOG_ERROR(LOG_APP, "ShowImage GetByteBuffer failed, errCode: %{public}d.", errCode);
   50. return;
   51. }
   52. Image_Size imgSize = {};
   53. OH_ImageNative_GetImageSize(image, &imgSize);
   54. OH_LOG_INFO(LOG_APP, "ImageReceiverNativeCTest %{public}s imgSize is : %{public}u, %{public}u.", __func__,
   55. imgSize.width, imgSize.height);
   56. size_t bufSize = 0;
   57. OH_ImageNative_GetBufferSize(image, g_jpegComponent, &bufSize);

   59. OHNativeWindowBuffer *nativeWindowBuffer = nullptr;
   60. int fenceFd = -1;
   61. res = OH_NativeWindow_NativeWindowRequestBuffer(nativeWindow, &nativeWindowBuffer, &fenceFd);
   62. if (res != 0) {
   63. OH_LOG_ERROR(LOG_APP, "ShowImage RequestBuffer failed, errCode: %{public}d.", res);
   64. return;
   65. }

   67. // 将image数据拷贝到nativeWindowBuffer上。
   68. copyBuffer(imageBuffer, bufSize, nativeWindowBuffer);

   70. Region region1{};
   71. res = OH_NativeWindow_NativeWindowFlushBuffer(nativeWindow, nativeWindowBuffer, fenceFd, region1);
   72. if (res != 0) {
   73. OH_LOG_ERROR(LOG_APP, "ShowImage FlushBuffer failed, errCode: %{public}d.", res);
   74. return;
   75. }
   76. OH_LOG_INFO(LOG_APP, "ImageReceiverNativeCTest %{public}s SUCCESS", __func__);
   77. }

   79. static void CallbackReadNextImage(OH_ImageReceiverNative *receiver)
   80. {
   81. OH_LOG_INFO(LOG_APP, "CallbackReadNextImage %{public}s IN", __func__);
   82. // 读取OH_ImageReceiverNative下一张图片对象。
   83. OH_ImageNative *image = nullptr;
   84. Image_ErrorCode errCode = OH_ImageReceiverNative_ReadNextImage(receiver, &image);
   85. if (errCode != IMAGE_SUCCESS) {
   86. OH_LOG_ERROR(LOG_APP,
   87. "CallbackReadNextImage %{public}s get image receiver next image failed, errCode: %{public}d.", __func__,
   88. errCode);
   89. return;
   90. }

   92. ShowImage(image);

   94. // 释放OH_ImageNative实例。
   95. errCode = OH_ImageNative_Release(image);
   96. if (errCode != IMAGE_SUCCESS) {
   97. OH_LOG_ERROR(LOG_APP, "CallbackReadNextImage %{public}s release image native failed, errCode: %{public}d.",
   98. __func__, errCode);
   99. }
   100. OH_LOG_INFO(LOG_APP, "CallbackReadNextImage %{public}s SUCCESS", __func__);
   101. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/NDKPreviewImageSample/entry/src/main/cpp/napi_init.cpp#L73-L175)
