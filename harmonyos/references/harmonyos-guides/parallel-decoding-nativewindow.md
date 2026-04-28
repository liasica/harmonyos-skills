---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/parallel-decoding-nativewindow
title: 创建视频解码器和NativeWindow初始化并行
breadcrumb: 指南 > 媒体 > AVCodec Kit（音视频编解码服务） > 音视频编解码 > 创建视频解码器和NativeWindow初始化并行
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:45+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:620063409ccb1187966462a8f2d8ba5a246c1c12bf9ef1908eab96b5020f8d8a
---

## 场景介绍

为了解码Surface模式的正常创建，在XComponent尚未创建或OpenGL后处理（NativeImage）尚未初始化的情况下，可以创建一个空的surface，以确保视频解码器能够正常创建和运行。

## 开发步骤

以下步骤描述了在surface的消费端没有创建之前，如何并行创建视频解码器和NativeWindow，让视频解码器正常创建执行。

**添加动态链接库**

```
1. target_link_libraries(sample PUBLIC libnative_image.so)
2. target_link_libraries(sample PUBLIC libnative_window.so)
3. target_link_libraries(sample PUBLIC libnative_buffer.so)
4. target_link_libraries(sample PUBLIC libnative_media_vdec.so)
```

说明

上述'sample'字样仅为示例，此处由开发者根据实际工程目录自定义。

**头文件**

```
1. #include <iostream>
2. #include <string>
3. #include <native_image/native_image.h>
4. #include <native_window/external_window.h>
5. #include <native_buffer/native_buffer.h>
6. #include <multimedia/player_framework/native_avcodec_videodecoder.h>
```

1. 创建OH\_NativeImage实例。

   ```
   1. // 创建NativeImage实例，作为surface的消费者。
   2. OH_NativeImage* image = OH_ConsumerSurface_Create();
   ```
2. 获取对应的数据生产者端NativeWindow。

   ```
   1. // 获取生产者NativeWindow。
   2. OHNativeWindow* nativeImageWindow = OH_NativeImage_AcquireNativeWindow(image);
   ```
3. 设置NativeWindow的宽高。

   ```
   1. int code = SET_BUFFER_GEOMETRY;
   2. int32_t width = 800;
   3. int32_t height = 600;
   4. int32_t ret = OH_NativeWindow_NativeWindowHandleOpt(nativeImageWindow, code, width, height);
   5. if (ret != AV_ERR_OK) {
   6. // 异常处理。
   7. }
   ```
4. 注册NativeImage的回调函数。

   注册OH\_NativeImage的监听者OH\_OnFrameAvailableListener，包括：

   * context 用户自定义的上下文信息；
   * onFrameAvailable 有buffer可获取触发时的回调函数。

   ```
   1. // onFrameAvailable实现。
   2. static void onFrameAvailable()
   3. {
   4. OHNativeWindowBuffer *buffer = nullptr;
   5. int fenceFd;
   6. // 通过消费端的OH_NativeImage获取一个OHNativeWindowBuffer。
   7. OH_NativeImage_AcquireNativeWindowBuffer(image, &buffer, &fenceFd);
   8. // 通过OH_NativeImage实例将OHNativeWindowBuffer归还到buffer队列中。
   9. OH_NativeImage_ReleaseNativeWindowBuffer(image, buffer, fenceFd);
   10. }

   12. static void context()
   13. {
   14. // 开发者自定义的上下文信息。
   15. }

   17. // 设置回调监听者。
   18. OH_OnFrameAvailableListener listener = {&onFrameAvailable, &context};
   19. // 设置帧可用回调。
   20. ret = OH_NativeImage_SetOnFrameAvailableListener(image, listener);
   21. if (ret != AV_ERR_OK) {
   22. // 异常处理。
   23. }
   ```

   说明

   在此示例中，回调函数的实现仅仅是将buffer取出来并释放，开发者可以根据业务需求自行拓展。
5. 配置解码器。

   具体开发指导请参考[视频解码Surface模式](video-decoding.md#surface模式)“步骤-5：调用OH\_VideoDecoder\_Configure()配置解码器”。
6. 设置surface。

   在应用业务真正的surface消费端创建成功之前，可以先使用上面临时创建的消费端连接解码器。

   示例中的变量说明如下：

   * videoDec：视频解码器实例的指针。创建方式可参考[视频解码Surface模式](video-decoding.md#surface模式)“步骤-2：创建解码器实例对象”。

   ```
   1. ret = OH_VideoDecoder_SetSurface(videoDec, nativeImageWindow);
   2. if (ret != AV_ERR_OK) {
   3. // 异常处理。
   4. }
   ```
7. 启动解码器。

   具体开发指导请参考[视频解码Surface模式](video-decoding.md#surface模式)“步骤-8：调用OH\_VideoDecoder\_Start()启动解码器”。
8. 设置surface。

   在应用业务真正的surface消费端创建成功后，可以调用OH\_VideoDecoder\_SetSurface接口，将解码输出重定向到新的surface上。

   本例中的nativeWindow，有两种方式获取：

   1. 如果解码后直接显示，则从XComponent组件获取，获取方式请参考 [XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)；
   2. 如果解码后接OpenGL后处理，则从NativeImage获取，获取方式请参考 [NativeImage](native-image-guidelines.md)。

   ```
   1. ret = OH_VideoDecoder_SetSurface(videoDec, nativeWindow);
   2. if (ret != AV_ERR_OK) {
   3. // 异常处理。
   4. }
   ```
9. 销毁OH\_NativeImage实例。

   在调用OH\_VideoDecoder\_Destroy接口后，调用OH\_NativeImage\_Destroy接口销毁OH\_NativeImage实例。

   ```
   1. // 销毁OH_NativeImage实例。
   2. OH_NativeImage_Destroy(&image);
   ```
