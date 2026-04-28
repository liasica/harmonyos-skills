---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-receiver-native
title: 图片接收
breadcrumb: 指南 > 媒体 > Image Kit（图片处理服务） > 图片开发指导(依赖JS对象)(不再推荐) > 图片接收
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:23+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:04a6b7f505cd1c3f84e28c0dcd338d925593cebabef661088d603a784d069efa
---

说明

当前开发指导使用的接口为[Image](../harmonyos-references/capi-image.md)模块下的C API，可完成图片编解码，图片接收器，处理图像数据等功能。这部分API在API version 11之前发布，在后续的版本不再增加新功能，**不再推荐使用**。

开发者可使用[Image\_NativeModule](../harmonyos-references/capi-image-nativemodule.md)模块下的C API，不仅提供上述图片框架基础功能，还可以完成多图编解码等新特性，相关开发指导请参考[图片开发指导(C/C++)](image-source-c.md)节点下的内容。这部分API从API version 12开始支持，并将持续演进，**推荐开发者使用**。

两套C API不建议同时使用，在部分场景下存在不兼容的问题。

图片接收类，用于获取组件surface id，接收最新的图片和读取下一张图片，以及释放ImageReceiver实例。

## 开发步骤

### 添加依赖

在进行应用开发之前，开发者需要打开native工程的src/main/cpp/CMakeLists.txt，在target\_link\_libraries依赖中添加libace\_napi.z.so、libimage\_ndk.z.so、libimage\_receiver\_ndk.z.so、libnative\_image.so以及日志依赖libhilog\_ndk.z.so。

```
1. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so libimage_ndk.z.so libimage_receiver_ndk.z.so libnative_image.so)
```

### 添加接口映射

打开src/main/cpp/hello.cpp文件，在Init函数中添加接口映射如下：

```
1. EXTERN_C_START
2. static napi_value Init(napi_env env, napi_value exports)
3. {
4. napi_property_descriptor desc[] = {
5. { "createFromReceiver", nullptr, createFromReceiver, nullptr, nullptr, nullptr, napi_default, nullptr },
6. };

8. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
9. return exports;
10. }
11. EXTERN_C_END
```

### 添加权限申请

此处通过camera图片获取输入数据，需要申请权限ohos.permission.CAMERA，申请方式请参考[向用户申请授权](request-user-authorization.md)。

### JS侧调用

1. 打开src\main\cpp\types\libentry\index.d.ts（其中libentry根据工程名生成），导入如下引用文件：

   ```
   1. import { image } from '@kit.ImageKit';

   3. export const createFromReceiver: (a: image.ImageReceiver) => image.Image;
   ```
2. 打开src\main\ets\pages\index.ets，导入"libentry.so（根据工程名生成）"，调用Native接口，传入JS的资源对象。示例如下：

   ```
   1. import testNapi from 'libentry.so';
   2. import { image } from '@kit.ImageKit';
   3. import { common, abilityAccessCtrl } from '@kit.AbilityKit';
   4. import { camera } from '@kit.CameraKit';

   6. @Entry
   7. @Component
   8. struct Index {
   9. private receiver: image.ImageReceiver | undefined = undefined;
   10. func (){
   11. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   12. abilityAccessCtrl.createAtManager().requestPermissionsFromUser(context,['ohos.permission.CAMERA']).then(async () => {
   13. let cameraManager = await camera.getCameraManager(context);
   14. // 获取支持的相机设备对象。
   15. let cameraDevices: Array<camera.CameraDevice> = cameraManager.getSupportedCameras();
   16. if (cameraDevices.length <= 0) {
   17. return;
   18. }
   19. // 获取对应相机设备的profiles。
   20. let profiles: camera.CameraOutputCapability = cameraManager.getSupportedOutputCapability(cameraDevices[0], camera.SceneMode.NORMAL_PHOTO);
   21. let previewProfiles: Array<camera.Profile> = profiles.previewProfiles;
   22. if (previewProfiles.length <= 0) {
   23. return;
   24. }
   25. let profileObj = previewProfiles[0];
   26. this.receiver = image.createImageReceiver({width:profileObj.size.width, height:profileObj.size.height}, image.ImageFormat.JPEG, 8);
   27. let receiverSurfaceId: string = await this.receiver.getReceivingSurfaceId();
   28. // 创建预览流输出对象。
   29. let previewOutput: camera.PreviewOutput = cameraManager.createPreviewOutput(profileObj,receiverSurfaceId);
   30. let cameraInput : camera.CameraInput = cameraManager.createCameraInput(cameraDevices[0]);
   31. // 打开相机。
   32. await cameraInput.open();
   33. // 会话流程。
   34. let session : camera.PhotoSession = cameraManager.createSession(camera.SceneMode.NORMAL_PHOTO) as camera.PhotoSession;
   35. // 配置会话。
   36. session.beginConfig();
   37. // 把cameraInput加入到会话。
   38. session.addInput(cameraInput);
   39. // 把预览流加入到会话。
   40. session.addOutput(previewOutput);
   41. // 提交配置信息。
   42. await session.commitConfig();
   43. // 会话开始。
   44. await session.start();

   46. this.receiver.on('imageArrival', () => {
   47. let img : image.Image = testNapi.createFromReceiver(this.receiver);
   48. img.release();
   49. })

   51. });
   52. }

   54. build() {
   55. Row() {
   56. Column() {
   57. Button("start")
   58. .width(100)
   59. .height(100)
   60. .onClick(() => {
   61. console.info("button click in");
   62. if (this.receiver == undefined) {
   63. this.func();
   64. }
   65. })
   66. }
   67. .width('100%')
   68. }
   69. .height('100%')
   70. }
   71. }
   ```

### Native接口调用

具体接口说明请参考[Image](../harmonyos-references/capi-image.md)。

在hello.cpp文件中获取JS的资源对象，并转为Native的资源对象，即可调用Native接口，调用方式示例代码如下：

**添加引用文件**

```
1. #include <multimedia/image_framework/image_mdk.h>
2. #include <multimedia/image_framework/image_receiver_mdk.h>
3. #include <malloc.h>
4. #include <hilog/log.h>

6. static napi_value createFromReceiver(napi_env env, napi_callback_info info)
7. {
8. size_t argc = 1;
9. napi_value args[2] = {nullptr};
10. napi_get_cb_info(env, info, &argc, args , nullptr, nullptr);
11. napi_valuetype valuetype0;
12. napi_typeof(env, args[0], &valuetype0);
13. napi_ref reference;
14. napi_create_reference(env, args[0], 1 ,&reference);
15. napi_value imgReceiver_js;
16. napi_get_reference_value(env, reference, &imgReceiver_js);

18. ImageReceiverNative * imgReceiver_c = OH_Image_Receiver_InitImageReceiverNative(env, imgReceiver_js);

20. int32_t capacity;
21. OH_Image_Receiver_GetCapacity(imgReceiver_c, &capacity);
22. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00, "[receiver]", "capacity: %{public}d", capacity);
23. int32_t format;
24. OH_Image_Receiver_GetFormat(imgReceiver_c, &format);
25. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00, "[receiver]", "format: %{public}d", format);
26. char * surfaceId = static_cast<char *>(malloc(sizeof(char)));
27. OH_Image_Receiver_GetReceivingSurfaceId(imgReceiver_c, surfaceId, sizeof(char));
28. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00, "[receiver]", "surfaceId: %{public}c", surfaceId[0]);
29. OhosImageSize size;
30. OH_Image_Receiver_GetSize(imgReceiver_c, &size);
31. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00, "[receiver]", "OH_Image_Receiver_GetSize  width: %{public}d, height:%{public}d", size.width, size.height);

33. napi_value nextImage;
34. // 或调用 OH_Image_Receiver_ReadNextImage(imgReceiver_c, &nextImage);
35. OH_Image_Receiver_ReadLatestImage(imgReceiver_c, &nextImage);

37. ImageNative * nextImage_native = OH_Image_InitImageNative(env, nextImage);

39. OhosImageSize imageSize;
40. OH_Image_Size(nextImage_native, &imageSize);
41. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00, "[receiver]", "OH_Image_Size  width: %{public}d, height:%{public}d", imageSize.width, imageSize.height);

43. OhosImageComponent imgComponent;
44. OH_Image_GetComponent(nextImage_native, 4, &imgComponent); // 4=jpeg

46. uint8_t *img_buffer = imgComponent.byteBuffer;

48. OH_Image_Release(nextImage_native);
49. OH_Image_Receiver_Release(imgReceiver_c);
50. return nextImage;
51. }
```
