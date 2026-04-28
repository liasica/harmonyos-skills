---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-receiver-c
title: 使用Image_NativeModule完成图片接收
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(C/C++) > 图片接收 > 使用Image_NativeModule完成图片接收
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:dc826d9eaef807333ce7f307a98d8716628ed5ac4c91ce00cda43c15e31963fb
---

图像接收类，用于获取组件的surfaceId、接收最新的图片、读取下一张图片以及释放ImageReceiver实例。结合camera API实现的相机预览示例代码可参考[预览流二次处理(C/C++)](native-camera-preview-imagereceiver.md)。

说明

ImageReceiver只作为图片的接收方、消费者，在ImageReceiver设置的size、format等属性实际上并不会生效。图片属性需要在发送方、生产者进行设置，可参考[预览(C/C++)](native-camera-preview.md)设置previewProfiles。

## 开发步骤

### 添加依赖

在进行应用开发之前，开发者需要打开native工程的src/main/cpp/CMakeLists.txt，在target\_link\_libraries依赖中添加libohimage.so、libimage\_receiver.so、libnative\_image.so以及日志依赖libhilog\_ndk.z.so。

```
1. target_link_libraries(entry PUBLIC libhilog_ndk.z.so libohimage.so libimage_receiver.so libnative_image.so)
```

### Native接口调用

具体接口说明请参考[Image\_NativeModule](../harmonyos-references/capi-image-nativemodule.md)。

下述代码主要演示了Receiver的初始化、相机预览流的创建以及获取图像的信息和Receiver的释放等相关功能。

说明

部分接口在API version 20以后才支持，需要开发者在进行开发时选择合适的API版本。

1. 导入相关头文件。

   ```
   1. #include <hilog/log.h>
   2. #include "napi/native_api.h"
   3. #include <string>
   4. #include <multimedia/image_framework/image/image_native.h>
   5. #include <multimedia/image_framework/image/image_receiver_native.h>

   7. #include "ohcamera/camera.h"
   8. #include "ohcamera/camera_input.h"
   9. #include "ohcamera/capture_session.h"
   10. #include "ohcamera/photo_output.h"
   11. #include "ohcamera/preview_output.h"
   12. #include "ohcamera/video_output.h"
   13. #include "ohcamera/camera_manager.h"

   15. #include <mutex>
   16. #include <shared_mutex> // C++17以上使用
   17. #include <condition_variable>
   ```

   [loadReceiver.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadReceiver.cpp#L15-L32)
2. 常量定义。

   ```
   1. #undef LOG_DOMAIN
   2. #define LOG_DOMAIN 0x3200

   4. #undef LOG_TAG
   5. #define LOG_TAG "MY_TAG"

   7. #define IMAGE_WIDTH 320
   8. #define IMAGE_HEIGHT 480
   9. #define IMAGE_CAPACITY 2
   ```

   [loadReceiver.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadReceiver.cpp#L34-L44)
3. 定义全局变量。

   ```
   1. static OH_ImageReceiverNative* g_receiver = nullptr;

   3. static std::mutex g_mutex;
   4. static std::shared_mutex shared_receiver_mutex;
   5. static std::condition_variable g_condVar;
   6. static bool g_imageReady = false;
   7. static OH_ImageNative* g_imageInfoResult = nullptr;
   ```

   [loadReceiver.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadReceiver.cpp#L46-L53)
4. 定义一些工具类函数，用来处理napi的返回值和参数类型的转换。

   ```
   1. // 处理napi返回值。
   2. napi_value GetJsResultDemo(napi_env env, int result)
   3. {
   4. napi_value resultNapi = nullptr;
   5. napi_create_int32(env, result, &resultNapi);
   6. return resultNapi;
   7. }

   9. // 将uint64_t转换为一个以null结尾的char数组。
   10. std::unique_ptr<char[]> ConvertUint64ToCharTemp(uint64_t value)
   11. {
   12. std::string strValue = std::to_string(value);
   13. auto charBuffer = std::make_unique<char[]>(strValue.size() + 1);
   14. std::copy(strValue.begin(), strValue.end(), charBuffer.get());
   15. charBuffer[strValue.size()] = '\0';

   17. return charBuffer;
   18. }
   ```

   [loadReceiver.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadReceiver.cpp#L55-L74)
5. 初始化Receiver。

   * 创建并设置ReceiverOptions。

     ```
     1. static Image_ErrorCode CreateAndConfigOptions(OH_ImageReceiverOptions** options)
     2. {
     3. Image_ErrorCode errCode = OH_ImageReceiverOptions_Create(options);
     4. if (errCode != IMAGE_SUCCESS) {
     5. OH_LOG_ERROR(LOG_APP, "Create image receiver options failed, errCode: %{public}d.", errCode);
     6. return errCode;
     7. }
     8. Image_Size imgSize = {IMAGE_WIDTH, IMAGE_HEIGHT};
     9. errCode = OH_ImageReceiverOptions_SetSize(*options, imgSize);
     10. if (errCode != IMAGE_SUCCESS) {
     11. OH_LOG_ERROR(LOG_APP, "Set image receiver options size failed, errCode: %{public}d.", errCode);
     12. OH_ImageReceiverOptions_Release(*options);
     13. return errCode;
     14. }
     15. errCode = OH_ImageReceiverOptions_SetCapacity(*options, IMAGE_CAPACITY);
     16. if (errCode != IMAGE_SUCCESS) {
     17. OH_LOG_ERROR(LOG_APP, "Set image receiver options capacity failed, errCode: %{public}d.", errCode);
     18. OH_ImageReceiverOptions_Release(*options);
     19. return errCode;
     20. }
     21. return IMAGE_SUCCESS;
     22. }
     ```

     [loadReceiver.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadReceiver.cpp#L77-L100)
   * 获取ReceiverOptions。

     ```
     1. static Image_ErrorCode ValidateOptions(OH_ImageReceiverOptions* options)
     2. {
     3. Image_Size imgSizeRead;
     4. Image_ErrorCode errCode = OH_ImageReceiverOptions_GetSize(options, &imgSizeRead);
     5. if (errCode != IMAGE_SUCCESS) {
     6. OH_LOG_ERROR(LOG_APP, "Get image receiver options size failed, errCode: %{public}d.", errCode);
     7. return errCode;
     8. }
     9. if (imgSizeRead.width != IMAGE_WIDTH || imgSizeRead.height != IMAGE_HEIGHT) {
     10. OH_LOG_ERROR(LOG_APP, "Get image receiver options size failed,"
     11. "width: %{public}d, height: %{public}d.", imgSizeRead.width, imgSizeRead.height);
     12. return IMAGE_BAD_PARAMETER;
     13. }
     14. int32_t capacity = 0;
     15. errCode = OH_ImageReceiverOptions_GetCapacity(options, &capacity);
     16. if (errCode != IMAGE_SUCCESS) {
     17. OH_LOG_ERROR(LOG_APP, "Get image receiver options capacity failed, errCode: %{public}d.", errCode);
     18. return errCode;
     19. }
     20. if (capacity != IMAGE_CAPACITY) {
     21. OH_LOG_ERROR(LOG_APP, "Get image receiver options capacity failed, capacity: %{public}d.", capacity);
     22. return IMAGE_BAD_PARAMETER;
     23. }
     24. return IMAGE_SUCCESS;
     25. }
     ```

     [loadReceiver.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadReceiver.cpp#L102-L128)
   * 创建Receiver对象。

     ```
     1. static Image_ErrorCode CreateReceiver(OH_ImageReceiverOptions* options, OH_ImageReceiverNative** receiver)
     2. {
     3. Image_ErrorCode errCode = OH_ImageReceiverNative_Create(options, receiver);
     4. if (errCode != IMAGE_SUCCESS) {
     5. OH_LOG_ERROR(LOG_APP, "Create image receiver failed, errCode: %{public}d.", errCode);
     6. return errCode;
     7. }
     8. return IMAGE_SUCCESS;
     9. }
     ```

     [loadReceiver.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadReceiver.cpp#L130-L140)
   * 定义获取下一张图片的callback函数。

     ```
     1. static void OnCallback(OH_ImageReceiverNative* receiver)
     2. {
     3. OH_LOG_INFO(LOG_APP, "ImageReceiverNativeCTest buffer available.");

     5. // 共享锁（读）
     6. std::shared_lock<std::shared_mutex> lock(shared_receiver_mutex);
     7. OH_ImageNative* image = nullptr;
     8. Image_ErrorCode errCode = OH_ImageReceiverNative_ReadNextImage(receiver, &image);
     9. if (errCode != IMAGE_SUCCESS) {
     10. OH_LOG_ERROR(LOG_APP, "ImageReceiverNativeCTest get image receiver next image failed,"
     11. "errCode: %{public}d.", errCode);
     12. OH_ImageNative_Release(image);
     13. return;
     14. } else {
     15. std::lock_guard<std::mutex> lock(g_mutex);
     16. g_imageInfoResult = image;
     17. g_imageReady = true;
     18. }
     19. g_condVar.notify_one();
     20. }
     ```

     [loadReceiver.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadReceiver.cpp#L142-L161)
   * 注册callback。

     ```
     1. static Image_ErrorCode RegisterCallbackAndQuery(OH_ImageReceiverNative* receiver)
     2. {
     3. uint64_t surfaceID = 0;
     4. Image_ErrorCode errCode = OH_ImageReceiverNative_On(receiver, OnCallback);
     5. if (errCode != IMAGE_SUCCESS) {
     6. OH_LOG_ERROR(LOG_APP, "Image receiver on failed, errCode: %{public}d.", errCode);
     7. return errCode;
     8. }
     9. errCode = OH_ImageReceiverNative_GetReceivingSurfaceId(receiver, &surfaceID);
     10. if (errCode != IMAGE_SUCCESS) {
     11. OH_LOG_ERROR(LOG_APP, "Get image receiver surfaceID failed, errCode: %{public}d.", errCode);
     12. return errCode;
     13. }
     14. OH_LOG_INFO(LOG_APP, "Get image receiver surfaceID: %{public}lu.", surfaceID);
     15. Image_Size imgSizeRead;
     16. errCode = OH_ImageReceiverNative_GetSize(receiver, &imgSizeRead);
     17. if (errCode != IMAGE_SUCCESS) {
     18. OH_LOG_ERROR(LOG_APP, "Get image receiver size failed, errCode: %{public}d.", errCode);
     19. return errCode;
     20. }
     21. OH_LOG_INFO(LOG_APP, "Get image receiver size: width = %{public}d, height = %{public}d.",
     22. imgSizeRead.width, imgSizeRead.height);
     23. int32_t capacity = 0;
     24. errCode = OH_ImageReceiverNative_GetCapacity(receiver, &capacity);
     25. if (errCode != IMAGE_SUCCESS) {
     26. OH_LOG_ERROR(LOG_APP, "Get image receiver capacity failed, errCode: %{public}d.", errCode);
     27. return errCode;
     28. }
     29. OH_LOG_INFO(LOG_APP, "Get image receiver capacity: %{public}d.", capacity);
     30. return IMAGE_SUCCESS;
     31. }
     ```

     [loadReceiver.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadReceiver.cpp#L163-L195)
   * 初始化Receiver的整体流程。

     ```
     1. static napi_value ImageReceiverNativeCTest(napi_env env, napi_callback_info info)
     2. {
     3. if (g_receiver != nullptr) {
     4. OH_ImageReceiverNative_Off(g_receiver);
     5. OH_ImageReceiverNative_Release(g_receiver);
     6. g_receiver = nullptr;
     7. }

     9. OH_ImageReceiverOptions* options = nullptr;
     10. Image_ErrorCode errCode = CreateAndConfigOptions(&options);
     11. if (errCode != IMAGE_SUCCESS) {
     12. OH_LOG_ERROR(LOG_APP, "CreateAndConfigOptions failed errCode=%{public}d", errCode);
     13. return GetJsResultDemo(env, errCode);
     14. }
     15. errCode = ValidateOptions(options);
     16. if (errCode != IMAGE_SUCCESS) {
     17. OH_LOG_ERROR(LOG_APP, "ValidateOptions failed errCode=%{public}d", errCode);
     18. OH_ImageReceiverOptions_Release(options);
     19. return GetJsResultDemo(env, errCode);
     20. }
     21. errCode = CreateReceiver(options, &g_receiver);
     22. if (errCode != IMAGE_SUCCESS) {
     23. OH_LOG_ERROR(LOG_APP, "CreateReceiver failed errCode=%{public}d", errCode);
     24. OH_ImageReceiverOptions_Release(options);
     25. return GetJsResultDemo(env, errCode);
     26. }
     27. errCode = RegisterCallbackAndQuery(g_receiver);
     28. if (errCode != IMAGE_SUCCESS) {
     29. OH_LOG_ERROR(LOG_APP, "RegisterCallbackAndQuery failed errCode=%{public}d", errCode);
     30. OH_ImageReceiverOptions_Release(options);
     31. OH_ImageReceiverNative_Release(g_receiver);
     32. g_receiver = nullptr;
     33. return GetJsResultDemo(env, errCode);
     34. }
     35. OH_LOG_INFO(LOG_APP, "ImageReceiverNativeCTest create and config success.");
     36. OH_ImageReceiverOptions_Release(options);
     37. return GetJsResultDemo(env, IMAGE_SUCCESS);
     38. }
     ```

     [loadReceiver.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadReceiver.cpp#L197-L236)
6. 调用相机拍照流进行拍照，触发回调。

   * 创建一个CameraManager实例。

     ```
     1. Camera_ErrorCode InitCameraManagerAndInput(Camera_Manager*& cameraManager,
     2. Camera_Device*& cameras,
     3. uint32_t& size,
     4. Camera_Input*& cameraInput)
     5. {
     6. cameraManager = nullptr;
     7. cameras = nullptr;
     8. size = 0;
     9. cameraInput = nullptr;
     10. Camera_ErrorCode ret = OH_Camera_GetCameraManager(&cameraManager);
     11. if (cameraManager == nullptr || ret != CAMERA_OK) {
     12. OH_LOG_ERROR(LOG_APP, "OH_Camera_GetCameraManager failed.");
     13. return ret;
     14. }
     15. ret = OH_CameraManager_GetSupportedCameras(cameraManager, &cameras, &size);
     16. if (cameras == nullptr || size < 1 || ret != CAMERA_OK) {
     17. OH_LOG_ERROR(LOG_APP, "OH_CameraManager_GetSupportedCameras failed.");
     18. return ret;
     19. }

     21. for (uint32_t i = 0; i < size; ++i) {
     22. OH_LOG_INFO(LOG_APP, "Camera[%{public}u]: id=%{public}s, position=%{public}d, type=%{public}d, "
     23. "connectionType=%{public}d", i, cameras[i].cameraId, cameras[i].cameraPosition, cameras[i].cameraType,
     24. cameras[i].connectionType);
     25. }

     27. ret = OH_CameraManager_CreateCameraInput(cameraManager, &cameras[0], &cameraInput);
     28. if (cameraInput == nullptr || ret != CAMERA_OK) {
     29. OH_LOG_ERROR(LOG_APP, "OH_CameraManager_CreateCameraInput failed.ret:%{public}d", ret);
     30. return ret;
     31. }
     32. return CAMERA_OK;
     33. }
     ```

     [loadReceiver.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadReceiver.cpp#L239-L273)
   * 获取相机输出能力。

     ```
     1. Camera_ErrorCode GetCameraOutputCapability(Camera_Manager* cameraManager,
     2. Camera_Device* cameras,
     3. uint32_t cameraDeviceIndex,
     4. Camera_OutputCapability*& capability)
     5. {
     6. capability = nullptr;
     7. Camera_ErrorCode ret = OH_CameraManager_GetSupportedCameraOutputCapability(cameraManager,
     8. &cameras[cameraDeviceIndex],
     9. &capability);
     10. if (capability == nullptr || ret != CAMERA_OK) {
     11. OH_LOG_ERROR(LOG_APP, "OH_CameraManager_GetSupportedCameraOutputCapability failed.");
     12. }
     13. return ret;
     14. }
     ```

     [loadReceiver.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadReceiver.cpp#L275-L290)
   * 创建相机捕获会话，用于捕获相机拍摄的照片。

     ```
     1. Camera_CaptureSession* CreateAndStartSession(Camera_Manager* cameraManager, Camera_Input* cameraInput, int sessionMode)
     2. {
     3. Camera_CaptureSession* captureSession = nullptr;
     4. Camera_ErrorCode ret = OH_CameraManager_CreateCaptureSession(cameraManager, &captureSession);
     5. if (captureSession == nullptr || ret != CAMERA_OK) {
     6. OH_LOG_ERROR(LOG_APP, "OH_CameraManager_CreateCaptureSession failed.");
     7. return nullptr;
     8. }
     9. ret = OH_CaptureSession_SetSessionMode(captureSession, static_cast<Camera_SceneMode>(sessionMode));
     10. if (ret != CAMERA_OK) {
     11. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_SetSessionMode failed.");
     12. return nullptr;
     13. }
     14. ret = OH_CaptureSession_BeginConfig(captureSession);
     15. if (ret != CAMERA_OK) {
     16. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_BeginConfig failed.");
     17. return nullptr;
     18. }
     19. ret = OH_CaptureSession_AddInput(captureSession, cameraInput);
     20. if (ret != CAMERA_OK) {
     21. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddInput failed.");
     22. return nullptr;
     23. }
     24. return captureSession;
     25. }
     ```

     [loadReceiver.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadReceiver.cpp#L292-L318)
   * 开启捕获会话。

     ```
     1. static Camera_ErrorCode StartCaptureSession(Camera_Manager* mgr, Camera_Input* input,
     2. Camera_PreviewOutput* previewOutput,
     3. Camera_CaptureSession** sessionOut)
     4. {
     5. *sessionOut = CreateAndStartSession(mgr, input, NORMAL_PHOTO);
     6. if (*sessionOut == nullptr) {
     7. OH_LOG_ERROR(LOG_APP, "CreateAndStartSession failed.");
     8. return CAMERA_INVALID_ARGUMENT;
     9. }

     11. Camera_ErrorCode ret = OH_CaptureSession_AddPreviewOutput(*sessionOut, previewOutput);
     12. if (ret != CAMERA_OK) {
     13. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddPreviewOutput failed.");
     14. return ret;
     15. }

     17. ret = OH_CaptureSession_CommitConfig(*sessionOut);
     18. if (ret != CAMERA_OK) {
     19. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_CommitConfig failed.");
     20. return ret;
     21. }

     23. ret = OH_CaptureSession_Start(*sessionOut);
     24. if (ret != CAMERA_OK) {
     25. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_Start failed.");
     26. }

     28. return ret;
     29. }
     ```

     [loadReceiver.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadReceiver.cpp#L320-L350)
   * 创建相机拍照流。

     ```
     1. Camera_ErrorCode StartTakePhoto(char* str)
     2. {
     3. char* photoSurfaceId = str;
     4. Camera_Manager* cameraManager = nullptr;
     5. Camera_Device* cameras = nullptr;
     6. uint32_t size = 0;
     7. Camera_Input* cameraInput = nullptr;
     8. Camera_ErrorCode ret = InitCameraManagerAndInput(cameraManager, cameras, size, cameraInput);
     9. if (ret != CAMERA_OK) return ret;

     11. Camera_OutputCapability* cameraOutputCapability = nullptr;
     12. ret = GetCameraOutputCapability(cameraManager, cameras, 0, cameraOutputCapability);
     13. if (ret != CAMERA_OK) return ret;

     15. const Camera_Profile* photoProfile = cameraOutputCapability->previewProfiles[0];
     16. Camera_PreviewOutput* previewOutput = nullptr;
     17. ret = OH_CameraManager_CreatePreviewOutput(cameraManager, photoProfile, photoSurfaceId, &previewOutput);
     18. if (photoProfile == nullptr || previewOutput == nullptr || ret != CAMERA_OK) {
     19. OH_LOG_ERROR(LOG_APP, "OH_CameraManager_CreatePreviewOutput failed.");
     20. return ret;
     21. }

     23. ret = OH_CameraInput_Open(cameraInput);
     24. if (ret != CAMERA_OK) {
     25. OH_LOG_ERROR(LOG_APP, "OH_CameraInput_open failed.");
     26. return ret;
     27. }

     29. Camera_CaptureSession* captureSession = nullptr;
     30. ret = StartCaptureSession(cameraManager, cameraInput, previewOutput, &captureSession);
     31. if (ret != CAMERA_OK) {
     32. OH_LOG_ERROR(LOG_APP, "StartCaptureSession failed.");
     33. return ret;
     34. }

     36. return CAMERA_OK;
     37. }
     ```

     [loadReceiver.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadReceiver.cpp#L352-L390)
   * 调用相机拍照的整体流程。

     ```
     1. static napi_value TakePhoto(napi_env env, napi_callback_info info)
     2. {
     3. if (g_receiver == nullptr) {
     4. OH_LOG_ERROR(LOG_APP, "ImageReceiver not initialized.");
     5. return GetJsResultDemo(env, IMAGE_BAD_PARAMETER);
     6. }
     7. uint64_t surfaceId = 0;
     8. Image_ErrorCode errCode = OH_ImageReceiverNative_GetReceivingSurfaceId(g_receiver, &surfaceId);
     9. if (errCode != IMAGE_SUCCESS) {
     10. OH_LOG_ERROR(LOG_APP, "Get surfaceId failed.");
     11. return GetJsResultDemo(env, errCode);
     12. }

     14. auto surfaceId_c = ConvertUint64ToCharTemp(surfaceId);
     15. Camera_ErrorCode photoRet = StartTakePhoto(surfaceId_c.get());
     16. return GetJsResultDemo(env, photoRet);
     17. }
     ```

     [loadReceiver.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadReceiver.cpp#L392-L410)
7. 获取Receiver接收到的图片信息。

   * 等待OnCallback回调通知。

     ```
     1. // 同步等待。
     2. static OH_ImageNative* NotifyJsImageInfoSync()
     3. {
     4. std::unique_lock<std::mutex> lock(g_mutex);
     5. g_imageReady = false;
     6. g_imageInfoResult = nullptr;

     8. // 等待OnCallback回调通知。
     9. bool ret = g_condVar.wait_for(lock, std::chrono::seconds(1), [] {
     10. OH_LOG_INFO(LOG_APP, "NotifyJsImageInfoSync: wait_for wakeup, g_imageReady=%{public}d", g_imageReady);
     11. return g_imageReady;
     12. });
     13. if (!ret) {
     14. OH_LOG_ERROR(LOG_APP, "NotifyJsImageInfoSync: wait_for timeout.");
     15. return nullptr;
     16. }
     17. return g_imageInfoResult;
     18. }
     ```

     [loadReceiver.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadReceiver.cpp#L413-L432)
   * 获取图片大小。

     ```
     1. // 获取图片大小。
     2. static napi_value GetImageSizeInfo(napi_env env, OH_ImageNative* image)
     3. {
     4. OH_LOG_INFO(LOG_APP, "GetImageSizeInfo: enter, image=%{public}p", image);

     6. Image_Size imgSizeRead;
     7. Image_ErrorCode errCode = OH_ImageNative_GetImageSize(image, &imgSizeRead);
     8. OH_LOG_INFO(LOG_APP, "GetImageSizeInfo: GetImageSize errCode=%{public}d, width=%{public}d, height=%{public}d",
     9. errCode, imgSizeRead.width, imgSizeRead.height);

     11. if (errCode == IMAGE_SUCCESS) {
     12. napi_value resultObj;
     13. napi_create_object(env, &resultObj);

     15. napi_value width;
     16. napi_value height;
     17. napi_create_int32(env, imgSizeRead.width, &width);
     18. napi_create_int32(env, imgSizeRead.height, &height);

     20. napi_set_named_property(env, resultObj, "width", width);
     21. napi_set_named_property(env, resultObj, "height", height);

     23. OH_LOG_INFO(LOG_APP, "GetImageSizeInfo: exit");
     24. return resultObj;
     25. }

     27. OH_LOG_ERROR(LOG_APP, "GetImageSizeInfo: Failed to get image size");
     28. return nullptr;
     29. }
     ```

     [loadReceiver.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadReceiver.cpp#L434-L464)
   * 获取组件类型。

     ```
     1. // 获取组件类型。
     2. static size_t GetComponentTypeSize(OH_ImageNative* image, size_t& componentTypeSize)
     3. {
     4. OH_LOG_INFO(LOG_APP, "GetComponentTypeSize: enter, image=%{public}p", image);
     5. // 获取组件类型的大小。
     6. Image_ErrorCode errCode = OH_ImageNative_GetComponentTypes(image, nullptr, &componentTypeSize);
     7. OH_LOG_INFO(LOG_APP, "GetComponentTypeSize: GetComponentTypes (query size) errCode=%{public}d,"
     8. "componentTypeSize=%{public}zu", errCode, componentTypeSize);
     9. return componentTypeSize;
     10. }
     ```

     [loadReceiver.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadReceiver.cpp#L466-L477)
   * 获取组件信息。

     ```
     1. // 获取组件信息。
     2. static napi_value GetComponentInfo(napi_env env, size_t componentTypeSize, OH_ImageNative* image, napi_value resultObj)
     3. {
     4. if (componentTypeSize > 0) {
     5. uint32_t* components = new uint32_t[componentTypeSize];
     6. Image_ErrorCode errCode = OH_ImageNative_GetComponentTypes(image, &components, &componentTypeSize);
     7. OH_LOG_INFO(LOG_APP, "GetImageInfoObject: GetComponentTypes (get types) errCode=%{public}d,"
     8. "firstComponent=%{public}u", errCode, componentTypeSize > 0 ? components[0] : 0);
     9. if (errCode != IMAGE_SUCCESS) {
     10. OH_LOG_ERROR(LOG_APP, "GetImageInfoObject: GetComponentTypes (get types) failed");
     11. delete [] components;
     12. return resultObj;
     13. }

     15. OH_NativeBuffer* nativeBuffer = nullptr;
     16. errCode = OH_ImageNative_GetByteBuffer(image, components[0], &nativeBuffer);
     17. if (errCode == IMAGE_SUCCESS) {
     18. OH_LOG_INFO(LOG_APP, "Get native buffer success.");
     19. }

     21. size_t nativeBufferSize = 0;
     22. errCode = OH_ImageNative_GetBufferSize(image, components[0], &nativeBufferSize);
     23. OH_LOG_INFO(LOG_APP, "GetImageInfoObject: GetBufferSize errCode=%{public}d, nativeBufferSize=%{public}zu",
     24. errCode, nativeBufferSize);
     25. if (errCode == IMAGE_SUCCESS) {
     26. napi_value bufSize;
     27. napi_create_int32(env, static_cast<int32_t>(nativeBufferSize), &bufSize);
     28. napi_set_named_property(env, resultObj, "bufferSize", bufSize);
     29. }

     31. int32_t rowStride = 0;
     32. errCode = OH_ImageNative_GetRowStride(image, components[0], &rowStride);
     33. OH_LOG_INFO(LOG_APP, "GetImageInfoObject: GetRowStride errCode=%{public}d,"
     34. "rowStride=%{public}d", errCode, rowStride);
     35. if (errCode == IMAGE_SUCCESS) {
     36. napi_value jsRowStride;
     37. napi_create_int32(env, rowStride, &jsRowStride);
     38. napi_set_named_property(env, resultObj, "rowStride", jsRowStride);
     39. }

     41. int32_t pixelStride = 0;
     42. errCode = OH_ImageNative_GetPixelStride(image, components[0], &pixelStride);
     43. OH_LOG_INFO(LOG_APP, "GetImageInfoObject: GetPixelStride errCode=%{public}d, pixelStride=%{public}d",
     44. errCode, pixelStride);
     45. if (errCode == IMAGE_SUCCESS) {
     46. napi_value jsPixelStride;
     47. napi_create_int32(env, pixelStride, &jsPixelStride);
     48. napi_set_named_property(env, resultObj, "pixelStride", jsPixelStride);
     49. }
     50. delete [] components;
     51. }
     52. return resultObj;
     53. }
     ```

     [loadReceiver.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadReceiver.cpp#L479-L533)
   * 获取图片属性并封装为napi对象。

     ```
     1. // 获取图像属性并封装为napi对象。
     2. static napi_value GetImageInfoObject(napi_env env, OH_ImageNative* image)
     3. {
     4. OH_LOG_INFO(LOG_APP, "GetImageInfoObject: enter, image=%{public}p", image);
     5. napi_value resultObj;
     6. napi_create_object(env, &resultObj);
     7. resultObj = GetImageSizeInfo(env, image);

     9. size_t componentTypeSize = 0;
     10. componentTypeSize = GetComponentTypeSize(image, componentTypeSize);
     11. if (componentTypeSize > 0) {
     12. resultObj = GetComponentInfo(env, componentTypeSize, image, resultObj);
     13. }

     15. int64_t timestamp = 0;
     16. Image_ErrorCode errCode = OH_ImageNative_GetTimestamp(image, &timestamp);
     17. OH_LOG_INFO(LOG_APP, "GetImageInfoObject: GetTimestamp errCode=%{public}d, timestamp=%{public}ld",
     18. errCode, timestamp);
     19. if (errCode == IMAGE_SUCCESS) {
     20. napi_value jsTimestamp;
     21. napi_create_int64(env, timestamp, &jsTimestamp);
     22. napi_set_named_property(env, resultObj, "timestamp", jsTimestamp);
     23. }

     25. OH_LOG_INFO(LOG_APP, "GetImageInfoObject: exit");
     26. return resultObj;
     27. }
     ```

     [loadReceiver.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadReceiver.cpp#L535-L563)
   * 获取ReceiverImageInfo的整体流程。

     ```
     1. static napi_value GetReceiverImageInfo(napi_env env, napi_callback_info info)
     2. {
     3. OH_ImageNative* image = NotifyJsImageInfoSync();
     4. if (!image) {
     5. napi_value undefined;
     6. napi_get_undefined(env, &undefined);
     7. return undefined;
     8. }
     9. napi_value resultObj = GetImageInfoObject(env, image);
     10. OH_ImageNative_Release(image);
     11. return resultObj;
     12. }
     ```

     [loadReceiver.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadReceiver.cpp#L565-L578)
8. 释放receiver。

   ```
   1. static napi_value ReleaseImageReceiver(napi_env env, napi_callback_info info)
   2. {
   3. if (g_receiver == nullptr) {
   4. OH_LOG_INFO(LOG_APP, "No image receiver to release.");
   5. return nullptr;
   6. }

   8. Image_ErrorCode errCode = OH_ImageReceiverNative_Off(g_receiver);
   9. if (errCode != IMAGE_SUCCESS) {
   10. OH_LOG_ERROR(LOG_APP, "ImageReceiverNativeCTest image receiver off failed, errCode: %{public}d.", errCode);
   11. }

   13. // 独占锁（写）
   14. std::unique_lock<std::shared_mutex> lock(shared_receiver_mutex);
   15. errCode = OH_ImageReceiverNative_Release(g_receiver);
   16. if (errCode != IMAGE_SUCCESS) {
   17. OH_LOG_ERROR(LOG_APP, "Release image receiver failed, errCode: %{public}d.", errCode);
   18. }

   20. g_receiver = nullptr;
   21. return GetJsResultDemo(env, errCode);
   22. }
   ```

   [loadReceiver.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Image/ImageNativeSample/entry/src/main/cpp/loadReceiver.cpp#L581-L600)
