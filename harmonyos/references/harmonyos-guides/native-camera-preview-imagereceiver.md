---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-preview-imagereceiver
title: 预览流二次处理(C/C++)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(C/C++) > 预览流二次处理(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:16+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7999de3f848589dfc2c2df9223e84a1e9c28f6e6bce2ff40789e59fe255168ae
---

通过ImageReceiver创建预览输出，获取预览流实时数据，以供后续进行图像二次处理，比如应用可以对其添加滤镜算法等。

## 开发步骤

详细的API说明请参考[OH\_Camera](../harmonyos-references/capi-oh-camera.md)。

1. 导入NDK接口，接口中提供了相机相关的属性和方法，导入方法如下。

   ```c
   #include <cstdint>
   #include <cstdlib>
   #include "hilog/log.h"
   #include <memory>
   #include <new>
   #include <map>
   #include <multimedia/image_framework/image/image_native.h>
   #include <multimedia/image_framework/image/image_receiver_native.h>
   #include "ohcamera/camera.h"
   #include "ohcamera/camera_input.h"
   #include "ohcamera/camera_device.h"
   #include "ohcamera/capture_session.h"
   #include "ohcamera/photo_output.h"
   #include "ohcamera/preview_output.h"
   #include "ohcamera/video_output.h"
   #include "ohcamera/camera_manager.h"

   #include <multimedia/media_library/media_asset_manager_capi.h>
   #include <multimedia/media_library/media_asset_change_request_capi.h>
   #include <multimedia/media_library/media_access_helper_capi.h>
   #include <multimedia/image_framework/image/image_packer_native.h>
   ```
2. 在CMake脚本中链接相关动态库。

   ```txt
   target_link_libraries(entry PUBLIC
       libace_napi.z.so
       libhilog_ndk.z.so
       libohimage.so
       libimage_receiver.so
       libnative_image.so
       libohcamera.so
       libnative_buffer.so
   )
   ```
3. 初始化图片接收器[ImageReceiver](image-receiver-c.md)实例，获取SurfaceId。

   通过image的OH\_ImageReceiverNative\_Create方法创建OH\_ImageReceiverNative实例，再通过实例的OH\_ImageReceiverNative\_GetReceivingSurfaceId方法获取SurfaceId。

   ```
   void InitImageReceiver(uint64_t &receiverSurfaceID)
   {
       OH_ImageReceiverOptions *options = nullptr;
       // 注意捕获错误码处理异常及对象判空，当前示例仅展示调用流程。
       // 设置图片参数。
       Image_ErrorCode errCode = OH_ImageReceiverOptions_Create(&options);
       if (errCode != IMAGE_SUCCESS || options == nullptr) {
           OH_LOG_ERROR(LOG_APP, "OH_ImageReceiverOptions_Create call failed");
           return;
       }
       Image_Size imgSize;
       imgSize.width = PREVIEW_WIDTH; // 创建预览流的宽。
       imgSize.height = PREVIEW_HEIGHT; // 创建预览流的高。
       int32_t capacity = 8; // BufferQueue里最大Image数量，推荐填写8。
       errCode = OH_ImageReceiverOptions_SetSize(options, imgSize);
       if (errCode != IMAGE_SUCCESS) {
           OH_LOG_ERROR(LOG_APP, "OH_ImageReceiverOptions_SetSize call failed");
       }
       errCode = OH_ImageReceiverOptions_SetCapacity(options, capacity);
       if (errCode != IMAGE_SUCCESS) {
           OH_LOG_ERROR(LOG_APP, "OH_ImageReceiverOptions_SetCapacity call failed");
       }
       // 创建OH_ImageReceiverNative对象。
       OH_ImageReceiverNative *receiver = nullptr;
       errCode = OH_ImageReceiverNative_Create(options, &receiver);
       if (errCode != IMAGE_SUCCESS || receiver == nullptr) {
           OH_LOG_ERROR(LOG_APP, "OH_ImageReceiverNative_Create call failed");
           return;
       }

       errCode = OH_ImageReceiverNative_On(receiver, CallbackReadNextImage);
       if (errCode != IMAGE_SUCCESS) {
           OH_LOG_ERROR(LOG_APP, "%{public}s image receiver on failed, errCode: %{public}d.", __func__, errCode);
           OH_ImageReceiverOptions_Release(options);
           OH_ImageReceiverNative_Release(receiver);
           return;
       }
       // 获取OH_ImageReceiverNative对象的SurfaceId。
       errCode = OH_ImageReceiverNative_GetReceivingSurfaceId(receiver, &receiverSurfaceID);
       if (errCode != IMAGE_SUCCESS) {
           OH_LOG_ERROR(LOG_APP, "OH_ImageReceiverNative_GetReceivingSurfaceId call failed");
       } else {
           OH_LOG_INFO(LOG_APP, "receiver surfaceID:%{public}lu", receiverSurfaceID);
       }
   }
   ```
4. 通过上一步获取到的SurfaceId创建预览流（在创建预览流之前需要将SurfaceId类型转成char \*），参考[预览(C/C++)](native-camera-preview.md)步骤4。
5. 创建会话，使能会话，参考[会话管理(C/C++)](native-camera-session-management.md)。
6. 注册ImageReceiver图片接收器的回调，监听获取每帧上报图像内容。

   ```
   void copyBuffer(OH_NativeBuffer *srcBuffer, size_t srcSize, OHNativeWindowBuffer *dstBuffer)
   {
       OH_LOG_INFO(LOG_APP, "ImageReceiverNativeCTest %{public}s IN", __func__);
       void *srcVir = nullptr;
       OH_NativeBuffer_Map(srcBuffer, &srcVir);
       BufferHandle *bufferHandle = OH_NativeWindow_GetBufferHandleFromNative(dstBuffer);
       OH_LOG_INFO(LOG_APP,
           "ImageReceiverNativeCTest %{public}s bufferHandle info fd= %{public}d , width= %{public}d, "
           "height=%{public}d, stride= %{public}d, size= %{public}d, format= %{public}d, usage= %{public}lu",
           __func__, bufferHandle->fd, bufferHandle->width, bufferHandle->height, bufferHandle->stride, bufferHandle->size,
           bufferHandle->format, bufferHandle->usage);

       void *mappedAddr =
           mmap(bufferHandle->virAddr, bufferHandle->size, PROT_READ | PROT_WRITE, MAP_SHARED, bufferHandle->fd, 0);
       std::memcpy(static_cast<unsigned char *>(mappedAddr), static_cast<unsigned char *>(srcVir), srcSize);
       munmap(mappedAddr, bufferHandle->size);

       OH_NativeBuffer_Unmap(srcBuffer);
       OH_LOG_INFO(LOG_APP, "ImageReceiverNativeCTest %{public}s SUCCESS", __func__);
   }

   void ShowImage(OH_ImageNative *image)
   {
       OH_LOG_INFO(LOG_APP, "ImageReceiverNativeCTest %{public}s IN", __func__);
       uint64_t xComponentSurfaceId = std::stoull(g_xComponentSurfaceIdSlave);
       OH_LOG_ERROR(LOG_APP, "ImageReceiverNativeCTest %{public}s XComponentId is : %{public}lu.", __func__,
           xComponentSurfaceId);
       OHNativeWindow *nativeWindow = nullptr;
       int32_t res = OH_NativeWindow_CreateNativeWindowFromSurfaceId(xComponentSurfaceId, &nativeWindow);
       if (res != 0) {
           OH_LOG_ERROR(LOG_APP,
               "ShowImage CreateNativeWindowFromSurfaceId failed, errCode: %{public}d.", res);
           return;
       }

       // 关键：调整nativeWindow大小及format，需要与image的大小、format保持一致。
       res = OH_NativeWindow_NativeWindowHandleOpt(nativeWindow, SET_BUFFER_GEOMETRY, g_imageWidth, g_imageHeight);
       res = OH_NativeWindow_NativeWindowHandleOpt(nativeWindow, SET_FORMAT, NATIVEBUFFER_PIXEL_FMT_YCRCB_420_SP); // NV21
       
       int32_t displayRotation = g_ndkCamera->GetDefaultDisplayRotation();
       int32_t previewRotation = static_cast<int32_t>(g_ndkCamera->GetPreviewRotation(displayRotation));
       if (g_isFront && (displayRotation == ROTATION_90 || displayRotation == ROTATION_270)) {
           previewRotation = (previewRotation + ROTATION_180) % ROTATION_360;
       }
       OH_NativeBuffer_TransformType transformType = g_ndkCamera->GetNativeBufferTransformType(previewRotation, g_isFront);
       res = OH_NativeWindow_NativeWindowHandleOpt(nativeWindow, SET_TRANSFORM, transformType);

       OH_NativeBuffer *imageBuffer = nullptr;
       Image_ErrorCode errCode = OH_ImageNative_GetByteBuffer(image, g_jpegComponent, &imageBuffer);
       if (errCode != IMAGE_SUCCESS) {
           OH_LOG_ERROR(LOG_APP, "ShowImage GetByteBuffer failed, errCode: %{public}d.", errCode);
           return;
       }
       Image_Size imgSize = {};
       OH_ImageNative_GetImageSize(image, &imgSize);
       OH_LOG_INFO(LOG_APP, "ImageReceiverNativeCTest %{public}s imgSize is : %{public}u, %{public}u.", __func__,
           imgSize.width, imgSize.height);
       size_t bufSize = 0;
       OH_ImageNative_GetBufferSize(image, g_jpegComponent, &bufSize);

       OHNativeWindowBuffer *nativeWindowBuffer = nullptr;
       int fenceFd = -1;
       res = OH_NativeWindow_NativeWindowRequestBuffer(nativeWindow, &nativeWindowBuffer, &fenceFd);
       if (res != 0) {
           OH_LOG_ERROR(LOG_APP, "ShowImage RequestBuffer failed, errCode: %{public}d.", res);
           return;
       }

       // 将image数据拷贝到nativeWindowBuffer上。
       copyBuffer(imageBuffer, bufSize, nativeWindowBuffer);

       Region region1{};
       res = OH_NativeWindow_NativeWindowFlushBuffer(nativeWindow, nativeWindowBuffer, fenceFd, region1);
       if (res != 0) {
           OH_LOG_ERROR(LOG_APP, "ShowImage FlushBuffer failed, errCode: %{public}d.", res);
           return;
       }
       OH_LOG_INFO(LOG_APP, "ImageReceiverNativeCTest %{public}s SUCCESS", __func__);
   }

   static void CallbackReadNextImage(OH_ImageReceiverNative *receiver)
   {
       OH_LOG_INFO(LOG_APP, "CallbackReadNextImage %{public}s IN", __func__);
       // 读取OH_ImageReceiverNative下一张图片对象。
       OH_ImageNative *image = nullptr;
       Image_ErrorCode errCode = OH_ImageReceiverNative_ReadNextImage(receiver, &image);
       if (errCode != IMAGE_SUCCESS) {
           OH_LOG_ERROR(LOG_APP,
               "CallbackReadNextImage %{public}s get image receiver next image failed, errCode: %{public}d.", __func__,
               errCode);
           return;
       }

       ShowImage(image);

       // 释放OH_ImageNative实例。
       errCode = OH_ImageNative_Release(image);
       if (errCode != IMAGE_SUCCESS) {
           OH_LOG_ERROR(LOG_APP, "CallbackReadNextImage %{public}s release image native failed, errCode: %{public}d.",
               __func__, errCode);
       }
       OH_LOG_INFO(LOG_APP, "CallbackReadNextImage %{public}s SUCCESS", __func__);
   }
   ```
