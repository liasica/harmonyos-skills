---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-video-render
title: 渲染视频画面
breadcrumb: 最佳实践 > 媒体 > 音频和视频 > 渲染视频画面
category: best-practices
scraped_at: 2026-04-28T08:20:44+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:06df4bd45e157c635f542513ff114f9a7ad493a3217d5e92c42bf1f8136bce38
---

## 概述

渲染视频画面是将原始视频数据（如 YUV、RGB 等格式）转换为可在屏幕上显示的图像，并最终输出到显示设备（如手机屏幕）的过程。此过程是视频解码播放、视频直播、相机预览等场景中的关键环节，决定了画面视觉效果。

本文以视频解码播放为场景案例，介绍了视频在解码后，如何将解码的视频数据渲染送显到设备屏幕上。目前，系统中提供了多种方式渲染视频画面，包括使用XComponent渲染视频画面、使用OpenGL渲染视频画面、使用Vulkan渲染视频画面。这三个方案的优点、缺点和适用场景如下表所示。

|  | 优点 | 缺点 | 使用场景 |
| --- | --- | --- | --- |
| 使用XComponent渲染视频画面 | * 开发门槛不高，可以通过XComponent的NativeWindow直接对接解码器。 * 解码后的YUV视频数据，无需额外进行处理，可以直接提交给XComponent进行渲染显示。 | * 定制化能力弱，无法满足复杂的开发场景。 * 性能优化的空间不多，在较为复杂或高规格的场景中，无法干预渲染流程，导致性能不高。 | 该方案适用于简单的视频播放，不需要对视频画面做复杂的处理。 |
| 使用OpenGL渲染视频画面 | * 可以满足复杂的场景，根据开发者的需求定制化开发。 * OpenGL是跨编程语言和跨平台的应用编程接口，便于应用的开发与迁移。 * 开发门槛适中，生态资料丰富。 | * 需要额外处理视频数据的格式，视频解码后的数据通常需要转化成RGBA的格式。 | 该方案可以满足复杂的开发场景，开发者可以根据实际需求实现，如视频直播、视频弹幕等场景。 |
| 使用Vulkan渲染视频画面 | * 可细粒度控制渲染全流程，优化渲染链路以获得更高性能。 * 可适配复杂的场景。 * Vulkan是跨编程语言和跨平台的应用编程接口，便于应用的开发与迁移。 | * 需要额外处理视频数据的格式，视频解码后的数据通常需要转化成RGBA的格式。 * 开发门槛较高，需要手动管理内存、命令缓冲等，且需要开发的代码量大，出现问题难定位。 | 同上。 |

## 使用XComponent渲染视频画面

### 场景描述

系统提供了AVPlayer、Video组件播放视频文件，其实现方式简单，但支持的文件格式有限。在播放其他格式（如rmvb格式）或有数字版权保护的视频时，AVPlayer、Video组件不能满足开发者的诉求。此时，开发者可以通过AVCodec将视频文件进行解码，然后将解码后的视频数据通过XComponent组件直接进行渲染送显即可。使用XComponent渲染视频画面是简单、常用的方式，开发者可以将解码的YUV视频数据传入给XComponent，无需关注YUV格式转化等问题。

### 实现原理

在使用XComponent渲染视频画面的方案中，需要提前获取XComponent对应的NativeWindow对象，并在创建视频解码器时，将NativeWindow设置给视频解码器。其具体开发流程如下所示。

1. 在XComponent创建时，通过回调函数OnSurfaceCreatedCB获取对应的NativeWindow对象。
2. 初始化视频解码的环境，包括初始化解封装器、初始化解码器。
3. 启动解码器、解码输入子线程、解码输出子线程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/8GvLAZ9iTQujVmSdwDeOaw/zh-cn_image_0000002484614821.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T002040Z&HW-CC-Expire=86400&HW-CC-Sign=0C59C9119159A7408CFFF256A44FBE24E31821783A2F73283A2899C253DF395D "点击放大")
4. 通过OnNeedInputBuffer获取可用的AVBuffer后，在解码输入子线程中，将解封装器读取视频数据填充到AVBuffer中，并提交给解码器进行解码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/2yYOnxY2QsyVVkiSxSkFjQ/zh-cn_image_0000002451534962.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T002040Z&HW-CC-Expire=86400&HW-CC-Sign=F252B3F90F5FFEC228A0736738BD8BA427A2A7222CAEE2E3C3CF4EC019FADBD6 "点击放大")
5. 通过OnNeedOutputBuffer获取解码的视频数据后，在解码输出子线程中，将解码后的视频数据提交给输出Surface（即XComponent的NativeWindow）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/p-VE-aUfQpCVBUDj70dE_A/zh-cn_image_0000002451375366.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T002040Z&HW-CC-Expire=86400&HW-CC-Sign=EF91A2212AE496060114D7FADE338F51D87C7832DE3B7FD1D5CCDF3548AC3516 "点击放大")

### 开发步骤

1. 在XComponent创建时，通过回调函数OnSurfaceCreatedCB获取对应的NativeWindow对象。

   ```
   1. void OnSurfaceCreatedCB(OH_NativeXComponent *component, void *window)
   2. {
   3. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "Callback", "OnSurfaceCreatedCB");
   4. if ((component == nullptr) || (window == nullptr)) {
   5. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "Callback",
   6. "onSurfaceCreatedCB: component or window is null");
   7. return;
   8. }
   9. char idStr[OH_XCOMPONENT_ID_LEN_MAX + 1] = {'\0'};
   10. uint64_t idSize = OH_XCOMPONENT_ID_LEN_MAX + 1;
   11. if (OH_NativeXComponent_GetXComponentId(component, idStr, &idSize) != OH_NATIVEXCOMPONENT_RESULT_SUCCESS) {
   12. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "Callback",
   13. "OnSurfaceCreatedCB:Unable to get XComponent id");
   14. return;
   15. }
   16. std::string id(idStr);
   17. auto render = PluginRender::GetInstance(id);
   18. uint64_t width;
   19. uint64_t height;
   20. int32_t xSize = OH_NativeXComponent_GetXComponentSize(component, window, &width, &height);
   21. if ((xSize != OH_NATIVEXCOMPONENT_RESULT_SUCCESS) || (render == nullptr)) {
   22. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "Callback",
   23. "OnSurfaceCreatedCB: Unable to qet XComponent size");
   24. return;
   25. }
   26. render->nativeWindow = reinterpret_cast<OHNativeWindow *>(window);
   27. (void)OH_NativeWindow_NativeWindowHandleOpt(render->nativeWindow, SET_BUFFER_GEOMETRY, static_cast<int>(width),
   28. static_cast<int>(height));
   29. if (id == "OpenGL") {
   30. render->openGLRenderThread_->UpdateNativeWindow(render->nativeWindow, width, height);
   31. } else if(id == "Vulkan") {
   32. render->vulkanRenderThread_->UpdateNativeWindow(render->nativeWindow, width, height);
   33. }
   34. }
   ```

   [PluginRender.cpp](https://gitcode.com/HarmonyOS_Samples/video-render/blob/master/entry/src/main/cpp/render/src/PluginRender.cpp#L27-L60)
2. 初始化视频解码的环境。

   ```
   1. int32_t Player::Init(SampleInfo &sampleInfo) {
   2. std::unique_lock<std::mutex> lock(mutex_);
   3. if(isStarted_ || (demuxer_ != nullptr && videoDecoder_ != nullptr)) {
   4. OH_LOG_ERROR(LOG_APP, "Already started.");
   5. return AVCODEC_SAMPLE_ERR_ERROR;
   6. }

   8. sampleInfo_ = sampleInfo;

   10. videoDecoder_ = std::make_unique<VideoDecoder>();
   11. demuxer_ = std::make_unique<Demuxer>();
   12. isReleased_ = false;
   13. int32_t ret = demuxer_->Create(sampleInfo_);
   14. if (ret != AVCODEC_SAMPLE_ERR_OK) {
   15. OH_LOG_ERROR(LOG_APP, "Create demuxer failed");
   16. doneCond_.notify_all();
   17. lock.unlock();
   18. StartRelease();
   19. return AVCODEC_SAMPLE_ERR_ERROR;
   20. }

   22. ret = CreateVideoDecoder();
   23. if (ret != AVCODEC_SAMPLE_ERR_OK) {
   24. OH_LOG_ERROR(LOG_APP, "Create video decoder failed");
   25. doneCond_.notify_all();
   26. lock.unlock();
   27. StartRelease();
   28. return AVCODEC_SAMPLE_ERR_ERROR;
   29. }

   31. OH_LOG_INFO(LOG_APP, "Succeed");
   32. return AVCODEC_SAMPLE_ERR_OK;
   33. }
   ```

   [Player.cpp](https://gitcode.com/HarmonyOS_Samples/video-render/blob/master/entry/src/main/cpp/player/src/Player.cpp#L48-L80)

   创建解封装器。

   ```
   1. int32_t Demuxer::Create(SampleInfo &info) {
   2. source_ = OH_AVSource_CreateWithFD(info.inputFd, info.inputFileOffset, info.inputFileSize);
   3. if (source_ == nullptr) {
   4. OH_LOG_ERROR(LOG_APP,
   5. "Create demuxer source failed, fd: %{public}d, offset: %{public}ld, file size: %{public}ld",
   6. info.inputFd, info.inputFileOffset, info.inputFileSize);
   7. return AVCODEC_SAMPLE_ERR_ERROR;
   8. }

   10. demuxer_ = OH_AVDemuxer_CreateWithSource(source_);
   11. if (demuxer_ == nullptr) {
   12. OH_LOG_ERROR(LOG_APP, "Create demuxer failed");
   13. return AVCODEC_SAMPLE_ERR_ERROR;
   14. }

   16. auto sourceFormat = std::shared_ptr<OH_AVFormat>(OH_AVSource_GetSourceFormat(source_), OH_AVFormat_Destroy);
   17. if (sourceFormat == nullptr) {
   18. OH_LOG_ERROR(LOG_APP, "Get source format failed");
   19. return AVCODEC_SAMPLE_ERR_ERROR;
   20. }

   22. int32_t ret = GetTrackInfo(sourceFormat, info);
   23. if (ret != AVCODEC_SAMPLE_ERR_OK) {
   24. OH_LOG_ERROR(LOG_APP, "Get video track info, ret: %{public}d", ret);
   25. return AVCODEC_SAMPLE_ERR_ERROR;
   26. }

   28. return AVCODEC_SAMPLE_ERR_OK;
   29. }
   ```

   [Demuxer.cpp](https://gitcode.com/HarmonyOS_Samples/video-render/blob/master/entry/src/main/cpp/capbilities/src/Demuxer.cpp#L26-L54)

   创建视频解码器。

   ```
   1. int32_t Player::CreateVideoDecoder() {
   2. OH_LOG_INFO(LOG_APP, "video mime:%{public}s", sampleInfo_.videoCodecMime.c_str());
   3. int32_t ret = videoDecoder_->Create(sampleInfo_.videoCodecMime);
   4. if (ret != AVCODEC_SAMPLE_ERR_OK) {
   5. OH_LOG_INFO(LOG_APP, "Create video decoder failed, mime:%{public}s", sampleInfo_.videoCodecMime.c_str());
   6. } else {
   7. videoDecContext_ = new CodecUserData;
   8. ret = videoDecoder_->Config(sampleInfo_, videoDecContext_);
   9. if(!(ret == AVCODEC_SAMPLE_ERR_OK)) {
   10. OH_LOG_ERROR(LOG_APP, "Video Decoder config failed");
   11. return ret;
   12. }
   13. }
   14. return AVCODEC_SAMPLE_ERR_OK;
   15. }
   ```

   [Player.cpp](https://gitcode.com/HarmonyOS_Samples/video-render/blob/master/entry/src/main/cpp/player/src/Player.cpp#L30-L44)

   设置视频解码器的Surface。

   ```
   1. int32_t VideoDecoder::Config(const SampleInfo &sampleInfo, CodecUserData *codecUserData) {
   2. if (decoder_ == nullptr) {
   3. OH_LOG_ERROR(LOG_APP, "Decoder is null");
   4. return AVCODEC_SAMPLE_ERR_ERROR;
   5. }

   7. if (codecUserData == nullptr) {
   8. OH_LOG_ERROR(LOG_APP, "Invalid param: codecUserData");
   9. return AVCODEC_SAMPLE_ERR_ERROR;
   10. }

   12. int32_t ret = Configure(sampleInfo);
   13. if (ret != AVCODEC_SAMPLE_ERR_OK) {
   14. OH_LOG_ERROR(LOG_APP, "Configure failed");
   15. return AVCODEC_SAMPLE_ERR_ERROR;
   16. }

   18. if (sampleInfo.window != nullptr) {
   19. int ret = OH_VideoDecoder_SetSurface(decoder_, sampleInfo.window);
   20. if (ret != AV_ERR_OK) {
   21. OH_LOG_ERROR(LOG_APP, "Set surface failed, ret: %{public}d", ret);
   22. return AVCODEC_SAMPLE_ERR_ERROR;
   23. }
   24. }

   26. ret = SetCallback(codecUserData);
   27. if (ret != AVCODEC_SAMPLE_ERR_OK) {
   28. OH_LOG_ERROR(LOG_APP, "Set callback failed, ret: %{public}d", ret);
   29. return AVCODEC_SAMPLE_ERR_ERROR;
   30. }

   32. ret = OH_VideoDecoder_Prepare(decoder_);
   33. if (ret != AV_ERR_OK) {
   34. OH_LOG_ERROR(LOG_APP, "Prepare failed, ret: %{public}d", ret);
   35. return AVCODEC_SAMPLE_ERR_ERROR;
   36. }

   38. return AVCODEC_SAMPLE_ERR_OK;
   39. }
   ```

   [VideoDecoder.cpp](https://gitcode.com/harmonyos_samples/video-render/blob/master/entry/src/main/cpp/capbilities/src/VideoDecoder.cpp#L81-L119)
3. 启动解码器、解码输入子线程、解码输出子线程。

   ```
   1. int32_t Player::Start() {
   2. std::unique_lock<std::mutex> lock(mutex_);
   3. int32_t ret;
   4. if (isStarted_ || demuxer_ == nullptr) {
   5. OH_LOG_ERROR(LOG_APP, "Already started.");
   6. return AVCODEC_SAMPLE_ERR_ERROR;
   7. }

   9. if (videoDecContext_) {
   10. ret = videoDecoder_->Start();
   11. if (ret != AVCODEC_SAMPLE_ERR_OK) {
   12. OH_LOG_ERROR(LOG_APP, "Video Decoder start failed");
   13. lock.unlock();
   14. StartRelease();
   15. return AVCODEC_SAMPLE_ERR_ERROR;
   16. }
   17. isStarted_ = true;
   18. videoDecInputThread_ = std::make_unique<std::thread>(&Player::VideoDecInputThread, this);
   19. videoDecOutputThread_ = std::make_unique<std::thread>(&Player::VideoDecOutputThread, this);

   21. if (videoDecInputThread_ == nullptr || videoDecOutputThread_ == nullptr) {
   22. OH_LOG_ERROR(LOG_APP, "Create thread failed");
   23. lock.unlock();
   24. StartRelease();
   25. return AVCODEC_SAMPLE_ERR_ERROR;
   26. }
   27. }

   29. OH_LOG_INFO(LOG_APP, "Succeed");
   30. doneCond_.notify_all();
   31. return AVCODEC_SAMPLE_ERR_OK;
   32. }
   ```

   [Player.cpp](https://gitcode.com/harmonyos_samples/video-render/blob/master/entry/src/main/cpp/player/src/Player.cpp#L84-L115)
4. 通过OnNeedInputBuffer获取可用的AVBuffer，将AVBuffer放到队列中，便于后续处理。

   ```
   1. void SampleCallback::OnNeedInputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData) {
   2. if (userData == nullptr) {
   3. return;
   4. }
   5. (void)codec;
   6. CodecUserData *codecUserData = static_cast<CodecUserData *>(userData);
   7. std::unique_lock<std::mutex> lock(codecUserData->inputMutex);
   8. codecUserData->inputBufferInfoQueue.emplace(index, buffer);
   9. codecUserData->inputCond.notify_all();
   10. }
   ```

   [SampleCallback.cpp](https://gitcode.com/harmonyos_samples/video-render/blob/master/entry/src/main/cpp/capbilities/src/SampleCallback.cpp#L32-L41)

   在解码输入子线程中，将解封装器读取视频数据填充到AVBuffer中，并提交给解码器进行解码。

   ```
   1. void Player::VideoDecInputThread() {
   2. while (true) {
   3. if (!isStarted_) {
   4. OH_LOG_ERROR(LOG_APP, "Decoder input thread out");
   5. break;;
   6. }

   8. std::unique_lock<std::mutex> lock(videoDecContext_->inputMutex);
   9. bool condRet = videoDecContext_->inputCond.wait_for(
   10. lock, 5s, [this]() { return !isStarted_ || !videoDecContext_->inputBufferInfoQueue.empty(); });
   11. if (!isStarted_) {
   12. OH_LOG_ERROR(LOG_APP, "Work done, thread out");
   13. break;
   14. }
   15. if (videoDecContext_->inputBufferInfoQueue.empty()) {
   16. OH_LOG_ERROR(LOG_APP, "Buffer queue is empty, continue, cond ret: %{public}d", condRet);
   17. continue;
   18. }

   20. CodecBufferInfo bufferInfo = videoDecContext_->inputBufferInfoQueue.front();
   21. videoDecContext_->inputBufferInfoQueue.pop();
   22. videoDecContext_->inputFrameCount++;
   23. lock.unlock();

   25. demuxer_->ReadSample(demuxer_->GetVideoTrackId(), reinterpret_cast<OH_AVBuffer *>(bufferInfo.buffer),
   26. bufferInfo.attr);

   28. int32_t ret = videoDecoder_->PushInputBuffer(bufferInfo);
   29. if (ret != AVCODEC_SAMPLE_ERR_OK) {
   30. OH_LOG_ERROR(LOG_APP, "Push data failed, thread out");
   31. break;
   32. }

   34. if (bufferInfo.attr.flags & AVCODEC_BUFFER_FLAGS_EOS) {
   35. OH_LOG_ERROR(LOG_APP, "Catch EOS, thread out");
   36. break;
   37. }
   38. }
   39. }
   ```

   [Player.cpp](https://gitcode.com/harmonyos_samples/video-render/blob/master/entry/src/main/cpp/player/src/Player.cpp#L170-L208)
5. 在解码输出子线程中，将解码后的视频数据提交给输出Surface。通过OnNeedOutputBuffer获取解码的视频数据。

   ```
   1. void SampleCallback::OnNewOutputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData) {
   2. if (userData == nullptr) {
   3. return;
   4. }
   5. (void)codec;
   6. CodecUserData *codecUserData = static_cast<CodecUserData *>(userData);
   7. std::unique_lock<std::mutex> lock(codecUserData->outputMutex);
   8. codecUserData->outputBufferInfoQueue.emplace(index, buffer);
   9. codecUserData->outputCond.notify_all();
   10. }
   ```

   [SampleCallback.cpp](https://gitcode.com/harmonyos_samples/video-render/blob/master/entry/src/main/cpp/capbilities/src/SampleCallback.cpp#L45-L54)

   在解码输出子线程中，将解码后的视频数据提交给输出Surface。Surface在已在解码器初始化配置，设置的是XComponent的NativeWindow对象。

   ```
   1. void Player::VideoDecOutputThread() {
   2. sampleInfo_.frameInterval = MICROSECOND / sampleInfo_.frameRate;
   3. while (true) {
   4. thread_local auto lastPushTime = std::chrono::system_clock::now();
   5. if (!isStarted_) {
   6. OH_LOG_ERROR(LOG_APP, "Decoder output thread out");
   7. break;
   8. }
   9. std::unique_lock<std::mutex> lock(videoDecContext_->outputMutex);
   10. bool condRet = videoDecContext_->outputCond.wait_for(
   11. lock, 5s, [this]() { return !isStarted_ || !videoDecContext_->outputBufferInfoQueue.empty(); });
   12. if (!isStarted_) {
   13. OH_LOG_ERROR(LOG_APP, "Decoder output thread out");
   14. break;
   15. }
   16. if (videoDecContext_->outputBufferInfoQueue.empty()) {
   17. OH_LOG_ERROR(LOG_APP, "Buffer queue is empty, continue, cond ret: %{public}d", condRet);
   18. continue;
   19. }

   21. CodecBufferInfo bufferInfo = videoDecContext_->outputBufferInfoQueue.front();
   22. videoDecContext_->outputBufferInfoQueue.pop();
   23. if (bufferInfo.attr.flags & AVCODEC_BUFFER_FLAGS_EOS) {
   24. OH_LOG_ERROR(LOG_APP, "Catch EOS, thread out");
   25. break;
   26. }
   27. videoDecContext_->outputFrameCount++;
   28. OH_LOG_INFO(LOG_APP,"Out buffer count: %{public}u, size: %{public}d, flag: %{public}u, pts: %{public}ld",
   29. videoDecContext_->outputFrameCount, bufferInfo.attr.size, bufferInfo.attr.flags,
   30. bufferInfo.attr.pts);
   31. lock.unlock();

   33. int32_t ret = videoDecoder_->FreeOutputBuffer(bufferInfo.bufferIndex, true);
   34. if (ret != AVCODEC_SAMPLE_ERR_OK) {
   35. OH_LOG_ERROR(LOG_APP, "Decoder output thread out");
   36. break;
   37. }

   39. std::this_thread::sleep_until(lastPushTime + std::chrono::microseconds(sampleInfo_.frameInterval));
   40. lastPushTime = std::chrono::system_clock::now();
   41. }
   42. StartRelease();
   43. }
   ```

   [Player.cpp](https://gitcode.com/harmonyos_samples/video-render/blob/master/entry/src/main/cpp/player/src/Player.cpp#L212-L254)

   通过OH\_VideoDecoder\_RenderOutputBuffer通知解码器将视频数据提交给输出Surface。

   ```
   1. int32_t VideoDecoder::FreeOutputBuffer(uint32_t bufferIndex, bool render) {
   2. if (decoder_ == nullptr) {
   3. OH_LOG_ERROR(LOG_APP, "Decoder is null");
   4. return AVCODEC_SAMPLE_ERR_ERROR;
   5. }

   7. int32_t ret = AVCODEC_SAMPLE_ERR_OK;
   8. if (render) {
   9. ret = OH_VideoDecoder_RenderOutputBuffer(decoder_, bufferIndex);
   10. } else {
   11. ret = OH_VideoDecoder_FreeOutputBuffer(decoder_, bufferIndex);
   12. }
   13. if (ret != AV_ERR_OK) {
   14. OH_LOG_ERROR(LOG_APP, "Free output data failed");
   15. return AVCODEC_SAMPLE_ERR_ERROR;
   16. }
   17. return AVCODEC_SAMPLE_ERR_OK;
   18. }
   ```

   [VideoDecoder.cpp](https://gitcode.com/HarmonyOS_Samples/video-render/blob/master/entry/src/main/cpp/capbilities/src/VideoDecoder.cpp#L153-L170)

## 使用OpenGL渲染视频画面

### 场景描述

OpenGL(Open Graphics Library)是一种跨语言、跨平台的应用程序编程接口（API），用于渲染2D和3D矢量图形。使用XComponent渲染视频画面的实现方案简单，支持的视频格式多，但对视频画面处理不够灵活，例如视频放大、旋转等操作。通过OpenGL，开发者可以根据需求定制实现各种图像处理功能，如视频旋转、视频弹幕等。

### 实现原理

在使用OpenGL渲染视频画面中，需要使用NativeImage对接解码器和OpenGL。开发者需要通过OH\_NativeImage\_AcquireNativeWindow()获取NativeImage的NativeWindow对象，并将NativeImage的NativeWindow对象设置给解码器，以消费解码器生成的视频图像数据。然后，通过OH\_NativeImage\_UpdateSurfaceImage()将NativeImage获取到的视频图像缓存更新到Opengl相关的纹理中。最后，通过eglSwapBuffers将渲染的缓存提交给XComponent的NativeWindow对象。

其具体实现如下所示。

1. 启动渲染子线程，初始化OpenGL环境，包括获取显示设备、初始化EGL环境、创建OpenGL上下文等。
2. 创建NativeImage对象，并根据NativeImage获取NativeWindow对象。
3. 获取XComponent的NativeWindow对象，并根据XComponent的NativeWindow对象创建EGLSurface。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/80_27qPpTKe6q5oSwTNkJw/zh-cn_image_0000002484494809.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T002040Z&HW-CC-Expire=86400&HW-CC-Sign=5F30645DE385F63DC8E763E219C67A4A5EBF83D60BB3F97D9BE8ACD2FAD944B5 "点击放大")
4. 初始化视频解码的环境，包括初始化解封装器、初始化配置解码器。

   说明

   在初始化配置解码器时，与直接使用XComponent渲染的方案不同，解码器设置Surface的入参是NativeImage的NativeWindow对象，而不是XComponent的NativeWindow对象。
5. 启动解码器、解码输入子线程、解码输出子线程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/IvQXR8JXQFOpEr2DDu-fWg/zh-cn_image_0000002484614829.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T002040Z&HW-CC-Expire=86400&HW-CC-Sign=9328EE00409A840FE87AB8353FF60B9E9A8112CC445C5A41768B2D8D6429D8E1 "点击放大")
6. 通过OnNeedInputBuffer获取可用的AVBuffer后，在解码输入子线程中，将解封装器读取视频数据填充到AVBuffer中，并提交给解码器进行解码。
7. 通过OnNeedOutputBuffer获取解码的视频数据后，在解码输出子线程中，将解码后的视频数据提交给输出Surface（当前Surface为NativeImage的NativeWindow对象）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/0EPHBxuaR5q6LXWMuyhz0A/zh-cn_image_0000002451534970.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T002040Z&HW-CC-Expire=86400&HW-CC-Sign=2F15F78625B86BDAAD4A160381166B75E810BBFB80467B8CE7AC85B82AD9A357 "点击放大")
8. 通过NativeImage，将视频图像缓存更新至OpenGL的纹理上。
9. 通过eglSwapBuffers交换前后缓冲区的内容，并将渲染结果显示在屏幕。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/HAHdXjHySZW8Yx06zMPe1A/zh-cn_image_0000002451375374.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T002040Z&HW-CC-Expire=86400&HW-CC-Sign=F73B5F8469FE4CC2FC731F032FBBF378F447DF98293D43EF163B8BEF023A9C73 "点击放大")

### 开发步骤

1. 启动渲染子线程，初始化OpenGL环境。

   ```
   1. void OpenGLRenderThread::ThreadMainLoop()
   2. {
   3. threadId_ = std::this_thread::get_id();
   4. if (!InitRenderContext()) {
   5. return;
   6. }
   7. if (!InitNativeVsync()) {
   8. return;
   9. }
   10. if (!CreateNativeImage()) {
   11. return;
   12. }
   13. while (running_) {
   14. {
   15. std::unique_lock<std::mutex> lock(wakeUpMutex_);
   16. wakeUpCond_.wait(lock, [this]() { return wakeUp_ || vSyncCnt_ > 0 || availableFrameCnt_ > 0; });
   17. wakeUp_ = false;
   18. vSyncCnt_--;
   19. (void)OH_NativeVSync_RequestFrame(nativeVsync_, &OpenGLRenderThread::OnVsync, this);
   20. }

   22. std::vector<RenderTask> tasks;
   23. {
   24. std::unique_lock<std::mutex> lock(taskMutex_);
   25. tasks.swap(tasks_);
   26. }
   27. for (const auto &task : tasks) {
   28. task(*renderContext_);
   29. }

   31. if (availableFrameCnt_ <= 0) {
   32. continue;
   33. }
   34. DrawImage();
   35. availableFrameCnt_--;
   36. }
   37. }
   ```

   [OpenGLRenderThread.cpp](https://gitcode.com/HarmonyOS_Samples/video-render/blob/master/entry/src/main/cpp/render/src/OpenGLRenderThread.cpp#L313-L349)

   初始化OpenGL环境，包括获取Display、EGL初始化、EGL上下文的创建等。

   ```
   1. bool OpenGLRender::Init()
   2. {
   3. if (IsEglContextReady()) {
   4. return true;
   5. }

   7. OH_LOG_Print(LOG_APP, LOG_DEBUG, LOG_PRINT_DOMAIN, "EglRenderContext", "EglRenderContext::Init begin.");
   8. eglDisplay_ = GetPlatformEglDisplay(EGL_PLATFORM_OHOS_KHR, EGL_DEFAULT_DISPLAY, NULL);
   9. if (eglDisplay_ == EGL_NO_DISPLAY) {
   10. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EglRenderContext",
   11. "EglRenderContext::Init: failed to create eglDisplay, error: %{public}s.", GetEglErrorString());
   12. return false;
   13. }

   15. EGLint major;
   16. EGLint minor;
   17. if (eglInitialize(eglDisplay_, &major, &minor) == EGL_FALSE) {
   18. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EglRenderContext",
   19. "EglRenderContext::Init: Failed to initialize EGLDisplay, error: %{public}s.",
   20. GetEglErrorString());
   21. }
   22. SetupEglExtensions();

   24. if (eglBindAPI(EGL_OPENGL_ES_API) == EGL_FALSE) {
   25. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EglRenderContext",
   26. "EglRenderContext::Init: Failed to bind OpenGL ES API, error: %{public}s.", GetEglErrorString());
   27. return false;
   28. }
   29. EGLint count;
   30. EGLint configAttribs[] = { EGL_SURFACE_TYPE,
   31. EGL_WINDOW_BIT,
   32. EGL_RED_SIZE,
   33. 8,
   34. EGL_GREEN_SIZE,
   35. 8,
   36. EGL_BLUE_SIZE,
   37. 8,
   38. EGL_ALPHA_SIZE,
   39. 8,
   40. EGL_RENDERABLE_TYPE,
   41. EGL_OPENGL_ES3_BIT,
   42. EGL_NONE };
   43. if (eglChooseConfig(eglDisplay_, configAttribs, &config_, 1, &count) == EGL_FALSE) {
   44. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EglRenderContext",
   45. "EglRenderContext::Init: Failed to bind choose config, error: %{public}s.", GetEglErrorString());
   46. return false;
   47. }
   48. const EGLint contextAttribs[] = { EGL_CONTEXT_CLIENT_VERSION, 2, EGL_NONE };
   49. eglContext_ = eglCreateContext(eglDisplay_, config_, EGL_NO_CONTEXT, contextAttribs);
   50. if (eglContext_ == EGL_NO_CONTEXT) {
   51. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EglRenderContext",
   52. "EglRenderContext::Init: Failed to bind create context, error: %{public}s.", GetEglErrorString());
   53. return false;
   54. }

   56. OH_LOG_Print(LOG_APP, LOG_DEBUG, LOG_PRINT_DOMAIN, "EglRenderContext", "EglRenderContext::Init end.");
   57. return true;
   58. }
   ```

   [OpenGLRender.cpp](https://gitcode.com/HarmonyOS_Samples/video-render/blob/master/entry/src/main/cpp/render/src/OpenGLRender.cpp#L104-L161)
2. 创建NativeImage对象，然后根据OH\_NativeImage\_AcquireNativeWindow()获取NativeWindow对象，并注册NativeImage的回调方法。

   ```
   1. bool OpenGLRenderThread::CreateNativeImage()
   2. {
   3. nativeImage_ = OH_NativeImage_Create(-1, GL_TEXTURE_EXTERNAL_OES);
   4. if (nativeImage_ == nullptr) {
   5. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "OpenGLRenderThread", "OH_NativeImage_Create failed.");
   6. return false;
   7. }
   8. int ret = 0;
   9. {
   10. std::lock_guard<std::mutex> lock(nativeImageSurfaceIdMutex_);
   11. nativeImageWindow_ = OH_NativeImage_AcquireNativeWindow(nativeImage_);
   12. ret = OH_NativeImage_GetSurfaceId(nativeImage_, &nativeImageSurfaceId_);
   13. }
   14. if (ret != 0) {
   15. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "OpenGLRenderThread",
   16. "OH_NativeImage_GetSurfaceId failed, ret is %{public}d.", ret);
   17. return false;
   18. }

   20. nativeImageFrameAvailableListener_.context = this;
   21. nativeImageFrameAvailableListener_.onFrameAvailable = &OpenGLRenderThread::OnNativeImageFrameAvailable;
   22. ret = OH_NativeImage_SetOnFrameAvailableListener(nativeImage_, nativeImageFrameAvailableListener_);
   23. if (ret != 0) {
   24. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "OpenGLRenderThread",
   25. "OH_NativeImage_SetOnFrameAvailableListener failed, ret is %{public}d.", ret);
   26. return false;
   27. }

   29. return true;
   30. }
   ```

   [OpenGLRenderThread.cpp](https://gitcode.com/harmonyos_samples/video-render/blob/master/entry/src/main/cpp/render/src/OpenGLRenderThread.cpp#L264-L293)
3. 在XComponent的回调函数OnSurfaceCreatedCB中，获取XComponent的NativeWindow对象。

   ```
   1. void OnSurfaceCreatedCB(OH_NativeXComponent *component, void *window)
   2. {
   3. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "Callback", "OnSurfaceCreatedCB");
   4. if ((component == nullptr) || (window == nullptr)) {
   5. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "Callback",
   6. "onSurfaceCreatedCB: component or window is null");
   7. return;
   8. }
   9. char idStr[OH_XCOMPONENT_ID_LEN_MAX + 1] = {'\0'};
   10. uint64_t idSize = OH_XCOMPONENT_ID_LEN_MAX + 1;
   11. if (OH_NativeXComponent_GetXComponentId(component, idStr, &idSize) != OH_NATIVEXCOMPONENT_RESULT_SUCCESS) {
   12. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "Callback",
   13. "OnSurfaceCreatedCB:Unable to get XComponent id");
   14. return;
   15. }
   16. std::string id(idStr);
   17. auto render = PluginRender::GetInstance(id);
   18. uint64_t width;
   19. uint64_t height;
   20. int32_t xSize = OH_NativeXComponent_GetXComponentSize(component, window, &width, &height);
   21. if ((xSize != OH_NATIVEXCOMPONENT_RESULT_SUCCESS) || (render == nullptr)) {
   22. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "Callback",
   23. "OnSurfaceCreatedCB: Unable to qet XComponent size");
   24. return;
   25. }
   26. render->nativeWindow = reinterpret_cast<OHNativeWindow *>(window);
   27. (void)OH_NativeWindow_NativeWindowHandleOpt(render->nativeWindow, SET_BUFFER_GEOMETRY, static_cast<int>(width),
   28. static_cast<int>(height));
   29. if (id == "OpenGL") {
   30. render->openGLRenderThread_->UpdateNativeWindow(render->nativeWindow, width, height);
   31. } else if(id == "Vulkan") {
   32. render->vulkanRenderThread_->UpdateNativeWindow(render->nativeWindow, width, height);
   33. }
   34. }
   ```

   [PluginRender.cpp](https://gitcode.com/HarmonyOS_Samples/video-render/blob/master/entry/src/main/cpp/render/src/PluginRender.cpp#L27-L60)

   根据XComponent的NativeWindow对象，调用eglCreateWindowSurface()创建EGLSurface对象。

   ```
   1. void OpenGLRenderThread::UpdateNativeWindow(void *window, uint64_t width, uint64_t height)
   2. {
   3. OH_LOG_Print(LOG_APP, LOG_DEBUG, LOG_PRINT_DOMAIN, "OpenGLRenderThread", "UpdateNativeWindow.");
   4. auto nativeWindow = reinterpret_cast<OHNativeWindow *>(window);
   5. PostTask([this, nativeWindow, width, height](OpenGLRender &renderContext) {
   6. if (nativeWindow_ != nativeWindow) {
   7. if (nativeWindow_ != nullptr) {
   8. (void)OH_NativeWindow_NativeObjectUnreference(nativeWindow_);
   9. }
   10. nativeWindow_ = nativeWindow;
   11. if (nativeWindow_ != nullptr) {
   12. (void)OH_NativeWindow_NativeObjectReference(nativeWindow_);
   13. }

   15. if (eglSurface_ != EGL_NO_SURFACE) {
   16. renderContext_->DestroyEglSurface(eglSurface_);
   17. eglSurface_ = EGL_NO_SURFACE;
   18. CleanGLResources();
   19. }
   20. }
   21. if (nativeWindow_ != nullptr) {
   22. (void)OH_NativeWindow_NativeWindowHandleOpt(nativeWindow_, SET_BUFFER_GEOMETRY, static_cast<int>(width),
   23. static_cast<int>(height));
   24. if (eglSurface_ == EGL_NO_SURFACE) {
   25. eglSurface_ = renderContext_->CreateEglSurface(static_cast<EGLNativeWindowType>(nativeWindow_));
   26. }
   27. if (eglSurface_ == EGL_NO_SURFACE) {
   28. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "OpenGLRenderThread", "xfl CreateEglSurface failed.");
   29. return;
   30. }
   31. renderContext_->MakeCurrent(eglSurface_);
   32. CreateGLResources();
   33. }
   34. });
   35. }
   ```

   [OpenGLRenderThread.cpp](https://gitcode.com/harmonyos_samples/video-render/blob/master/entry/src/main/cpp/render/src/OpenGLRenderThread.cpp#L129-L163)
4. 初始化视频解码的环境，包括初始化解封装器、初始化解码器。注意，解码器设置的是NativeImage的NativeWindow对象。

   ```
   1. napi_value PluginRender::StartPlayer(napi_env env, napi_callback_info info)
   2. {
   3. SampleInfo sampleInfo;
   4. size_t argc = 4;
   5. napi_value args[4] = {nullptr};
   6. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
   7. napi_get_value_int32(env, args[0], &sampleInfo.inputFd);
   8. napi_get_value_int64(env, args[1], &sampleInfo.inputFileOffset);
   9. napi_get_value_int64(env, args[2], &sampleInfo.inputFileSize);
   10. size_t length = 0;
   11. napi_status status = napi_get_value_string_utf8(env, args[3], nullptr, 0, &length);
   12. char* buf = new char[length + 1];
   13. std::memset(buf, 0, length + 1);
   14. status = napi_get_value_string_utf8(env, args[3], buf, length + 1, &length);
   15. std::string type = buf;
   16. PluginRender *render = PluginRender::GetInstance(type);
   17. if (render != nullptr) {
   18. if (type == "OpenGL") {
   19. sampleInfo.window = render->openGLRenderThread_->GetNativeImageWindow();
   20. } else if (type == "Vulkan") {
   21. sampleInfo.window = render->vulkanRenderThread_->GetNativeImageWindow();
   22. } else {
   23. sampleInfo.window = render->nativeWindow;
   24. }
   25. }
   26. int32_t ret = Player::GetInstance().Init(sampleInfo);
   27. if (ret != AVCODEC_SAMPLE_ERR_OK) {
   28. return nullptr;
   29. }
   30. Player::GetInstance().Start();
   31. return nullptr;
   32. }
   ```

   [PluginRender.cpp](https://gitcode.com/harmonyos_samples/video-render/blob/master/entry/src/main/cpp/render/src/PluginRender.cpp#L154-L185)
5. 启动解码器、解码输入子线程、解码输出子线程。（代码与使用XComponent渲染一致）
6. 通过OnNeedInputBuffer获取可用的AVBuffer后，在解码输入子线程中，将解封装器读取视频数据填充到AVBuffer中，并提交给解码器进行解码。（代码与使用XComponent渲染一致）
7. 通过OnNeedOutputBuffer获取解码的视频数据后，在解码输出子线程中，将解码后的视频数据提交给输出Surface。（代码与使用XComponent渲染一致）
8. 通过OH\_NativeImage\_AttachContext()绑定上下文，再通过OH\_NativeImage\_UpdateSurfaceImage()将视频图像缓存更新至OpenGL的纹理上。

   ```
   1. void OpenGLRenderThread::DrawImage()
   2. {
   3. if (nativeImageTexId_ == 9999) {
   4. glGenTextures(1, &nativeImageTexId_);
   5. glBindTexture(GL_TEXTURE_EXTERNAL_OES, nativeImageTexId_);
   6. // set the texture wrapping parameters
   7. glTexParameteri(GL_TEXTURE_EXTERNAL_OES, GL_TEXTURE_WRAP_S, GL_REPEAT);
   8. glTexParameteri(GL_TEXTURE_EXTERNAL_OES, GL_TEXTURE_WRAP_T, GL_REPEAT);
   9. // set texture filtering parameters
   10. glTexParameteri(GL_TEXTURE_EXTERNAL_OES, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
   11. glTexParameteri(GL_TEXTURE_EXTERNAL_OES, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
   12. }
   13. OH_LOG_Print(LOG_APP, LOG_DEBUG, LOG_PRINT_DOMAIN, "OpenGLRenderThread", "DrawImage.");

   15. if (eglSurface_ == EGL_NO_SURFACE) {
   16. OH_LOG_Print(LOG_APP, LOG_WARN, LOG_PRINT_DOMAIN, "OpenGLRenderThread", "eglSurface_ is EGL_NO_SURFACE");
   17. return;
   18. }

   20. OH_NativeImage_AttachContext(nativeImage_, nativeImageTexId_);

   22. int32_t ret = OH_NativeImage_UpdateSurfaceImage(nativeImage_);
   23. if (ret != 0) {
   24. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "OpenGLRenderThread",
   25. "OH_NativeImage_UpdateSurfaceImage failed, ret: %{public}d, texId: %{public}d", ret,
   26. nativeImageTexId_);
   27. return;
   28. }
   29. OH_LOG_Print(LOG_APP, LOG_DEBUG, LOG_PRINT_DOMAIN, "OpenGLRenderThread", "OH_NativeImage_UpdateSurfaceImage succeed.");

   31. OHNativeWindow *nativeWindow = OH_NativeImage_AcquireNativeWindow(nativeImage_);
   32. int32_t transformTmp = 0;
   33. int code = NativeWindowOperation::GET_TRANSFORM;
   34. OH_NativeWindow_NativeWindowHandleOpt(nativeWindow, code, &transformTmp);

   36. ret = OH_NativeImage_GetTransformMatrix(nativeImage_, matrix_);
   37. if (ret != 0) {
   38. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "OpenGLRenderThread",
   39. "OH_NativeImage_GetTransformMatrix failed, ret: %{public}d", ret);
   40. return;
   41. }

   43. transformTmp = 2;
   44. ComputeTransformByMatrix(transformTmp, matrix_);

   46. DrawVideoImage();
   47. }
   ```

   [OpenGLRenderThread.cpp](https://gitcode.com/harmonyos_samples/video-render/blob/master/entry/src/main/cpp/render/src/OpenGLRenderThread.cpp#L427-L473)
9. 通过eglSwapBuffers将渲染的缓存提交给XComponent的NativeWindow对象进行显示。

   ```
   1. void OpenGLRender::SwapBuffers(EGLSurface surface) const
   2. {
   3. EGLBoolean ret = eglSwapBuffers(eglDisplay_, surface);
   4. if (ret == EGL_FALSE) {
   5. EGLint surfaceId = -1;
   6. eglQuerySurface(eglDisplay_, surface, EGL_CONFIG_ID, &surfaceId);
   7. OH_LOG_Print(
   8. LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "EglRenderContext",
   9. "EglRenderContext::SwapBuffers: Failed to SwapBuffers on EGLSurface %{public}d, error is %{public}s.",
   10. surfaceId, GetEglErrorString());
   11. }
   12. }
   ```

   [OpenGLRender.cpp](https://gitcode.com/harmonyos_samples/video-render/blob/master/entry/src/main/cpp/render/src/OpenGLRender.cpp#L204-L215)

## 使用Vulkan渲染视频画面

### 场景描述

Vulkan是一套用来做2D和3D渲染的图形应用程序接口，能够跨平台高效访问GPU。Vulkan提供了更细粒度的硬件控制，允许开发者更精细地管理资源和状态，从而提高性能和效率。相比之下，OpenGL的一些细节对开发者是隐藏的，在部分情况下会限制性能。在实际开发实现中，Vulkan的门槛远高于OpenGL，需要手动管理内存、渲染流程等。如果开发者对性能较高，且熟悉Vulkan，可以使用Vulkan渲染视频画面。

### 实现原理

NativeImage是提供Surface关联OpenGL外部纹理的模块，表示图形队列的消费者端，有两种方式消费处理数据。第一种是将数据和OpenGL纹理对接，需在OpenGL环境下使用，此方式在使用OpenGL渲染视频画面中介绍过。另一种是开发者自行获取Buffer进行渲染处理，使用Vulkan渲染视频画面采用的是第二种方式。

在将NativeImage的NativeWindow对象设置给解码器后，NativeImage成为了视频解码器的数据消费者。开发者可以使用OH\_NativeImage\_AcquireNativeWindowBuffer()从NativeImage获取NativeWindowBuffer对象，消费使用OHNativeWindowBuffer对象中的视频数据。然后，通过OH\_NativeBuffer\_FromNativeWindowBuffer()方法，将OHNativeWindowBuffer对象转化成NativeBuffer。最后，将NativeBuffer提交给Vulkan，Vulkan根据NativeBuffer创建ImageView对象用于后续的渲染。同时，需要注意的是，解码器解码后的图像格式通常是YUV的格式，开发者需要对数据格式进行转化，才能正常渲染显示。

其具体实现如下所示。

1. 启动渲染子线程，加载Vulkan的动态链接库。
2. 创建NativeImage对象，并根据NativeImage获取NativeWindow对象。
3. 获取XComponent的NativeWindow对象，并根据XComponent的NativeWindow对象创建Vulkan的Surface用于显示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/UDVY3rQxReaMcQcyi4aofA/zh-cn_image_0000002484494813.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T002040Z&HW-CC-Expire=86400&HW-CC-Sign=89F4F024D39F677874AFBA9FEA92EB592773DB28AE83789624EC75D6E584F92C "点击放大")
4. 初始化视频解码的环境，包括初始化解封装器、初始化解码器。

   说明

   在初始化配置解码器时，与直接使用XComponent渲染的方案不同，解码器设置Surface的入参是NativeImage的NativeWindow对象，而不是XComponent的NativeWindow对象。
5. 启动解码器、解码输入子线程、解码输出子线程。
6. 在解码输入子线程中，通过解封装器读取视频数据，并提交给解码器。
7. 通过OnNeedOutputBuffer获取解码的视频数据后，在解码输出子线程中，将解码后的视频数据提交给输出Surface（当前Surface为NativeImage的NativeWindow对象）。
8. 在NativeImage的回调onFrameAvailable()有可用数据后，通过OH\_NativeImage\_AcquireNativeWindowBuffer()获取视频数据，并通过OH\_NativeBuffer\_FromNativeWindowBuffer()转化为NativeBuffer的类型。
9. Vulkan根据NativeBuffer创建对应的ImageView用于采样，同时，创建对应格式的采样器，通过采样器将YUV格式的图像转化成RGBA的图像，最后，通过渲染管道进行显示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/aKXzZVt5QpO0GtcpmBLRQw/zh-cn_image_0000002484614833.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T002040Z&HW-CC-Expire=86400&HW-CC-Sign=FBF03921952F26412AB18DE40265EEA71FBEDE393AD0E6F136F625706845705C "点击放大")

### 开发步骤

1. 启动渲染子线程，加载Vulkan的动态链接库。

   ```
   1. void VulkanRenderThread::ThreadMainLoop() {
   2. threadId_ = std::this_thread::get_id();
   3. if (!InitRenderContext()) {
   4. return;
   5. }
   6. if (!InitNativeVsync()) {
   7. return;
   8. }
   9. if (!CreateNativeImage()) {
   10. return;
   11. }
   12. while (running_) {
   13. {
   14. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "RenderThread", "Waiting for Vsync.");
   15. std::unique_lock<std::mutex> Lock(wakeUpMutex_);
   16. wakeUpCond_.wait(Lock, [this]() { return wakeup_ || vSyncCnt_ > 0 || availableFrameCnt_ > 0; });
   17. wakeup_ = false;
   18. vSyncCnt_--;
   19. (void)OH_NativeVSync_RequestFrame(nativeVsync_, &VulkanRenderThread::OnVsync, this);
   20. }

   22. std::vector<VulkanRenderTask> tasks;
   23. {
   24. std::lock_guard<std::mutex> lock(taskMutex_);
   25. tasks.swap(tasks_);
   26. }
   27. for (const auto &task : tasks) {
   28. task(*vulkanRenderContext_);
   29. }
   30. if (availableFrameCnt_ <= 0) {
   31. continue;
   32. }
   33. DrawImage();
   34. availableFrameCnt_--;
   35. }
   36. }
   ```

   [VulkanRenderThread.cpp](https://gitcode.com/harmonyos_samples/video-render/blob/master/entry/src/main/cpp/render/src/VulkanRenderThread.cpp#L175-L210)

   动态加载libvulkan.so，并加载Vulkan基础函数的指针。

   ```
   1. // Dynamically load Vulkan library and base function pointers
   2. bool LoadVulkanLibrary() {
   3. // Load vulkan library
   4. constexpr char *path = "libvulkan.so";
   5. dlerror();
   6. g_libVulkan = dlopen(path, RTLD_NOW | RTLD_LOCAL);
   7. if (!g_libVulkan) {
   8. OH_LOG_ERROR(LOG_APP, "Failed to load vulkan Library, %{public}s", dlerror());
   9. return false;
   10. }

   12. // // Load base function pointers
   13. vkEnumerateInstanceExtensionProperties = reinterpret_cast<PFN_vkEnumerateInstanceExtensionProperties>(
   14. dlsym(g_libVulkan, "vkEnumerateInstanceExtensionProperties"));
   15. vkEnumerateInstanceLayerProperties = reinterpret_cast<PFN_vkEnumerateInstanceLayerProperties>(
   16. dlsym(g_libVulkan, "vkEnumerateInstanceLayerProperties"));
   17. vkCreateInstance = reinterpret_cast<PFN_vkCreateInstance>(dlsym(g_libVulkan, "vkCreateInstance"));
   18. vkGetInstanceProcAddr = reinterpret_cast<PFN_vkGetInstanceProcAddr>(dlsym(g_libVulkan, "vkGetInstanceProcAddr"));
   19. vkGetDeviceProcAddr = reinterpret_cast<PFN_vkGetDeviceProcAddr>(dlsym(g_libVulkan, "vkGetDeviceProcAddr"));

   21. return true;
   22. }
   ```

   [VulkanUtils.cpp](https://gitcode.com/harmonyos_samples/video-render/blob/master/entry/src/main/cpp/utils/src/VulkanUtils.cpp#L149-L170)
2. 创建NativeImage对象，并根据NativeImage获取NativeWindow对象。

   ```
   1. bool VulkanRenderThread::CreateNativeImage() {
   2. nativeImage_ = OH_NativeImage_Create(-1, GL_TEXTURE_EXTERNAL_OES);
   3. if (nativeImage_ == nullptr) {
   4. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "RenderThread", "OH_NativeImage_Create failed.");
   5. return false;
   6. }
   7. int ret = 0;
   8. {
   9. std::lock_guard<std::mutex> Lock(nativeImageSurfaceIdMutex_);
   10. nativeImageWindow_ = OH_NativeImage_AcquireNativeWindow(nativeImage_);
   11. ret = OH_NativeImage_GetSurfaceId(nativeImage_, &nativeImageSurfaceId_);
   12. }
   13. if (ret != 0) {
   14. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "RenderThread",
   15. "OH_NativeImage_GetSurfaceId failed, ret is %{public}d.", ret);
   16. return false;
   17. }

   19. nativeImageFrameAvailableListener_.context = this;
   20. nativeImageFrameAvailableListener_.onFrameAvailable = &VulkanRenderThread::OnNativeImageFrameAvailable;
   21. ret = OH_NativeImage_SetOnFrameAvailableListener(nativeImage_, nativeImageFrameAvailableListener_);
   22. if (ret != 0) {
   23. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "RenderThread",
   24. "OH_NativeImage_SetonFrameAvailableListener failed, ret is %{public}d.", ret);
   25. return false;
   26. }
   27. return true;
   28. }
   ```

   [VulkanRenderThread.cpp](https://gitcode.com/harmonyos_samples/video-render/blob/master/entry/src/main/cpp/render/src/VulkanRenderThread.cpp#L136-L163)
3. 在获取XComponent的NativeWindow对象后，根据XComponent的NativeWindow对象创建Vulkan的Surface。

   ```
   1. void VulkanRenderThread::UpdateNativeWindow(void *window, uint64_t width, uint64_t height) {
   2. OH_LOG_Print(LOG_APP, LOG_DEBUG, LOG_PRINT_DOMAIN, "RenderThread", "UpdateNativeWindow.");
   3. auto nativeWindow = reinterpret_cast<OHNativeWindow *>(window);
   4. PostTask([this, nativeWindow, width, height](VulkanRender &renderContext) {
   5. if (nativeWindow_ != nativeWindow) {
   6. if (nativeWindow_ != nullptr) {
   7. (void)OH_NativeWindow_NativeObjectUnreference(nativeWindow_);
   8. }
   9. nativeWindow_ = nativeWindow;
   10. if (nativeWindow_ != nullptr) {
   11. (void)OH_NativeWindow_NativeObjectReference(nativeWindow_);
   12. }
   13. }
   14. if (nativeWindow_ != nullptr) {
   15. vulkanRenderContext_->SetupWindow(nativeWindow_);
   16. }
   17. });
   18. }
   ```

   [VulkanRenderThread.cpp](https://gitcode.com/harmonyos_samples/video-render/blob/master/entry/src/main/cpp/render/src/VulkanRenderThread.cpp#L61-L78)

   设置Vulkan的Surface，同时更新初始化Vulkan的上下文，包括Vulkan的实例、选择物理设备、加载Vulkan的方法等。

   ```
   1. void VulkanRender::SetupWindow(NativeWindow *nativeWindow) {
   2. nativeWindow_ = nativeWindow;
   3. CreateInstance();
   4. vkExample::utils::LoadVulkanFunctions(instance);
   5. CreateSurface();
   6. PickPhysicalDevice();
   7. CreateLogicalDevice();
   8. vkExample::utils::LoadVulkanFunctions(device);

   10. createSwapChain();
   11. createRenderPass();
   12. createFrameBuffersAndImages();
   13. createVertexBuffer();
   14. createUniformBuffer();
   15. deviceInfoInitialized = true;
   16. }
   ```

   [VulkanRender.cpp](https://gitcode.com/harmonyos_samples/video-render/blob/master/entry/src/main/cpp/render/src/VulkanRender.cpp#L45-L60)

   通过vkCreateSurfaceOHOS()创建Surface对象。

   ```
   1. bool VulkanRender::CreateSurface() {
   2. VkSurfaceCreateInfoOHOS surfaceCreateInfo{};
   3. surfaceCreateInfo.sType = VK_STRUCTURE_TYPE_SURFACE_CREATE_INFO_OHOS;
   4. if (nativeWindow_ == nullptr) {
   5. OH_LOG_INFO(LOG_APP, "nativeWindow_ is nulptr.Failed to create surface !");
   6. return false;
   7. }
   8. surfaceCreateInfo.window = nativeWindow_;
   9. surfaceCreateInfo.flags = 0;
   10. surfaceCreateInfo.pNext = nullptr;
   11. bool res = CheckResult(vkCreateSurfaceOHOS(instance, &surfaceCreateInfo, nullptr, &surface));
   12. return res;
   13. }
   ```

   [VulkanRender.cpp](https://gitcode.com/HarmonyOS_Samples/video-render/blob/master/entry/src/main/cpp/render/src/VulkanRender.cpp#L119-L131)
4. 初始化视频解码的环境，包括初始化解封装器、初始化解码器。

   ```
   1. napi_value PluginRender::StartPlayer(napi_env env, napi_callback_info info)
   2. {
   3. SampleInfo sampleInfo;
   4. size_t argc = 4;
   5. napi_value args[4] = {nullptr};
   6. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
   7. napi_get_value_int32(env, args[0], &sampleInfo.inputFd);
   8. napi_get_value_int64(env, args[1], &sampleInfo.inputFileOffset);
   9. napi_get_value_int64(env, args[2], &sampleInfo.inputFileSize);
   10. size_t length = 0;
   11. napi_status status = napi_get_value_string_utf8(env, args[3], nullptr, 0, &length);
   12. char* buf = new char[length + 1];
   13. std::memset(buf, 0, length + 1);
   14. status = napi_get_value_string_utf8(env, args[3], buf, length + 1, &length);
   15. std::string type = buf;
   16. PluginRender *render = PluginRender::GetInstance(type);
   17. if (render != nullptr) {
   18. if (type == "OpenGL") {
   19. sampleInfo.window = render->openGLRenderThread_->GetNativeImageWindow();
   20. } else if (type == "Vulkan") {
   21. sampleInfo.window = render->vulkanRenderThread_->GetNativeImageWindow();
   22. } else {
   23. sampleInfo.window = render->nativeWindow;
   24. }
   25. }
   26. int32_t ret = Player::GetInstance().Init(sampleInfo);
   27. if (ret != AVCODEC_SAMPLE_ERR_OK) {
   28. return nullptr;
   29. }
   30. Player::GetInstance().Start();
   31. return nullptr;
   32. }
   ```

   [PluginRender.cpp](https://gitcode.com/harmonyos_samples/video-render/blob/master/entry/src/main/cpp/render/src/PluginRender.cpp#L154-L185)
5. 启动解码器、解码输入子线程、解码输出子线程。（代码与使用XComponent渲染一致）
6. 在解码输入子线程中，通过解封装器读取视频数据，并提交给解码器。（代码与使用XComponent渲染一致）
7. 在解码输出子线程中，将解码后的视频数据提交给输出Surface。（代码与使用XComponent渲染一致）
8. 在NativeImage有可用数据后，通过OH\_NativeImage\_AcquireNativeWindowBuffer()获取视频数据，并通过OH\_NativeBuffer\_FromNativeWindowBuffer()转化为NativeBuffer的类型。

   ```
   1. void VulkanRenderThread::DrawImage() {
   2. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "VulkanRenderThread", "DrawImage.");
   3. int ret;
   4. OHNativeWindowBuffer *inBuffer = nullptr;
   5. OH_NativeBuffer *nativeBuffer = nullptr;
   6. int32_t fenceFd1 = -1;
   7. ret = OH_NativeImage_AcquireNativeWindowBuffer(nativeImage_, &inBuffer, &fenceFd1);
   8. ret = OH_NativeWindow_NativeObjectReference(inBuffer);
   9. ret = OH_NativeBuffer_FromNativeWindowBuffer(inBuffer, &nativeBuffer);
   10. if (nativeBuffer == nullptr) {
   11. OH_NativeWindow_NativeObjectUnreference(inBuffer);
   12. OH_NativeImage_ReleaseNativeWindowBuffer(nativeImage_, inBuffer, -1);
   13. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "VulkanRenderThread", "nativeBuffer is null.");
   14. return;
   15. }
   16. ret = OH_NativeImage_GetTransformMatrix(nativeImage_, matrix_);
   17. int32_t transformTmp = 0;
   18. ComputeTransform(transformTmp, matrix_);
   19. vulkanRenderContext_->hwBufferToTexture(nativeBuffer, matrix_);
   20. vulkanRenderContext_->render();
   21. if (lastInBuffer_ != nullptr) {
   22. OH_NativeWindow_NativeObjectUnreference(lastInBuffer_);
   23. OH_NativeImage_ReleaseNativeWindowBuffer(nativeImage_, lastInBuffer_, -1);
   24. }
   25. lastInBuffer_ = inBuffer;
   26. }
   ```

   [VulkanRenderThread.cpp](https://gitcode.com/harmonyos_samples/video-render/blob/master/entry/src/main/cpp/render/src/VulkanRenderThread.cpp#L286-L311)
9. Vulkan根据NativeBuffer创建对应的ImageView用于渲染显示，同时，创建对应格式的采样器，将YUV格式的图像转化成RGBA的图像，用于正确的渲染显示。

   ```
   1. void VulkanRender::hwBufferToTexture(OH_NativeBuffer *buffer, float transformMatrix[16]) {
   2. OH_LOG_Print(LOG_APP, LOG_INFO, 0xFF00, "VulkanRenderThread", "hwBufferToTexture.");
   3. if (!deviceInfoInitialized) {
   4. return;
   5. }
   6. UniformBufferObject ubo{};
   7. memcpy(ubo.mvp, transformMatrix, sizeof(float) * 16);
   8. memcpy(buffersInfo.uniformBufferMapped, &ubo, sizeof(ubo));
   9. VkNativeBufferFormatPropertiesOHOS nbFormatProps = {
   10. .sType = VK_STRUCTURE_TYPE_NATIVE_BUFFER_FORMAT_PROPERTIES_OHOS,
   11. .pNext = nullptr
   12. };
   13. VkNativeBufferPropertiesOHOS nbProps = {.sType = VK_STRUCTURE_TYPE_NATIVE_BUFFER_PROPERTIES_OHOS,
   14. .pNext = &nbFormatProps};
   15. CheckResult(vkGetNativeBufferPropertiesOHOS(device, buffer, &nbProps));

   17. VkImportNativeBufferInfoOHOS importBufferInfo = {
   18. .sType = VK_STRUCTURE_TYPE_IMPORT_NATIVE_BUFFER_INFO_OHOS,
   19. .pNext = nullptr,
   20. .buffer = buffer
   21. };

   23. VkMemoryDedicatedAllocateInfo dedicatedAllocateInfo = {
   24. .sType = VK_STRUCTURE_TYPE_MEMORY_DEDICATED_ALLOCATE_INFO,
   25. .pNext = &importBufferInfo,
   26. .image = VK_NULL_HANDLE, // wiLl be set later
   27. .buffer = VK_NULL_HANDLE
   28. };

   30. VkPhysicalDeviceMemoryProperties physicalDeviceMemProps;
   31. uint32_t foundTypeIndex = 0;
   32. vkGetPhysicalDeviceMemoryProperties(gpuDevice, &physicalDeviceMemProps);
   33. uint32_t memTypeCnt = physicalDeviceMemProps.memoryTypeCount;
   34. for (uint32_t i = 0; i < memTypeCnt; ++i) {
   35. if (nbProps.memoryTypeBits & (1 << i)) {
   36. const VkPhysicalDeviceMemoryProperties &pdmp = physicalDeviceMemProps;
   37. uint32_t supportedFLags = pdmp.memoryTypes[i].propertyFlags & VK_MEMORY_PROPERTY_DEVICE_LOCAL_BIT;
   38. if (supportedFLags == VK_MEMORY_PROPERTY_DEVICE_LOCAL_BIT) {
   39. foundTypeIndex = i;
   40. break;
   41. }
   42. }
   43. }

   45. VkMemoryAllocateInfo allocInfo{
   46. .sType = VK_STRUCTURE_TYPE_MEMORY_ALLOCATE_INFO,
   47. .pNext = &dedicatedAllocateInfo,
   48. .allocationSize = nbProps.allocationSize,
   49. .memoryTypeIndex = 0 // Memory type assigned in the next step
   50. };

   52. mapMemoryTypeToIndex(nbProps.memoryTypeBits, VK_MEMORY_PROPERTY_DEVICE_LOCAL_BIT, &allocInfo.memoryTypeIndex);
   53. VkExternalFormatOHOS externalFormat;
   54. externalFormat.sType = VK_STRUCTURE_TYPE_EXTERNAL_FORMAT_OHOS;
   55. externalFormat.pNext = nullptr;
   56. externalFormat.externalFormat = 0;
   57. if (nbFormatProps.format == VK_FORMAT_UNDEFINED) {
   58. externalFormat.externalFormat = nbFormatProps.externalFormat;
   59. }

   61. VkExternalMemoryImageCreateInfo externalMemoryImageInfo = {
   62. .sType = VK_STRUCTURE_TYPE_EXTERNAL_MEMORY_IMAGE_CREATE_INFO,
   63. .pNext = &externalFormat,
   64. .handleTypes = VK_EXTERNAL_MEMORY_HANDLE_TYPE_OHOS_NATIVE_BUFFER_BIT_OHOS,
   65. };

   67. VkImageUsageFlags usageFlags = VK_IMAGE_USAGE_SAMPLED_BIT;
   68. if (nbFormatProps.format != VK_FORMAT_UNDEFINED) {
   69. usageFlags = usageFlags | VK_IMAGE_USAGE_TRANSFER_SRC_BIT | VK_IMAGE_USAGE_TRANSFER_DST_BIT |
   70. VK_IMAGE_USAGE_COLOR_ATTACHMENT_BIT | VK_IMAGE_USAGE_INPUT_ATTACHMENT_BIT;
   71. }
   72. OH_NativeBuffer_Config config;
   73. OH_NativeBuffer_GetConfig(buffer, &config);
   74. VkImageCreateInfo image_create_info = {
   75. .sType = VK_STRUCTURE_TYPE_IMAGE_CREATE_INFO,
   76. .pNext = &externalMemoryImageInfo,
   77. .flags = 0,
   78. .imageType = VK_IMAGE_TYPE_2D,
   79. .format = nbFormatProps.format,
   80. .extent = {static_cast<uint32_t>(config.width), static_cast<uint32_t>(config.height), 1},
   81. .mipLevels = 1,
   82. .arrayLayers = 1,
   83. .samples = VK_SAMPLE_COUNT_1_BIT,
   84. .tiling = VK_IMAGE_TILING_OPTIMAL,
   85. .usage = usageFlags,
   86. .sharingMode = VK_SHARING_MODE_EXCLUSIVE,
   87. .queueFamilyIndexCount = 1,
   88. .pQueueFamilyIndices = &queueFamilyIndex_,
   89. // VK_IMAGE_LAYOUT_UNDEFINED is mandatory when using external memory
   90. .initialLayout = VK_IMAGE_LAYOUT_UNDEFINED
   91. };

   93. CheckResult(vkCreateImage(device, &image_create_info, nullptr, &externalTextureImage));
   94. dedicatedAllocateInfo.image = externalTextureImage;
   95. CheckResult(vkAllocateMemory(device, &allocInfo, nullptr, &externalTextureMemory));
   96. CheckResult(vkBindImageMemory(device, externalTextureImage, externalTextureMemory, 0));

   98. VkSamplerYcbcrConversionCreateInfo ycbcrCreateInfo = {
   99. .sType = VK_STRUCTURE_TYPE_SAMPLER_YCBCR_CONVERSION_CREATE_INFO,
   100. .ycbcrRange = nbFormatProps.suggestedYcbcrRange,
   101. .components = nbFormatProps.samplerYcbcrConversionComponents,
   102. .xChromaOffset = nbFormatProps.suggestedXChromaOffset,
   103. .yChromaOffset = nbFormatProps.suggestedYChromaOffset,
   104. .chromaFilter = VK_FILTER_LINEAR,
   105. .forceExplicitReconstruction = false
   106. };

   108. if (nbFormatProps.format == VK_FORMAT_UNDEFINED) {
   109. ycbcrCreateInfo.pNext = &externalFormat;
   110. ycbcrCreateInfo.format = VK_FORMAT_UNDEFINED;
   111. ycbcrCreateInfo.ycbcrModel = nbFormatProps.suggestedYcbcrModel;
   112. }

   114. CheckResult(
   115. vkCreateSamplerYcbcrConversion(device, &ycbcrCreateInfo, nullptr, &externalTextureInfo.ycbcrConversion));

   117. VkSamplerYcbcrConversionInfo convInfoWrap = {
   118. .sType = VK_STRUCTURE_TYPE_SAMPLER_YCBCR_CONVERSION_INFO,
   119. .conversion = externalTextureInfo.ycbcrConversion,
   120. .pNext = nullptr,
   121. };

   123. VkImageViewCreateInfo view = {
   124. .sType = VK_STRUCTURE_TYPE_IMAGE_VIEW_CREATE_INFO,
   125. .pNext = &convInfoWrap,
   126. .flags = 0,
   127. .image = externalTextureImage,
   128. .viewType = VK_IMAGE_VIEW_TYPE_2D,
   129. .format = nbFormatProps.format,
   130. .components =
   131. {
   132. VK_COMPONENT_SWIZZLE_IDENTITY,
   133. VK_COMPONENT_SWIZZLE_IDENTITY,
   134. VK_COMPONENT_SWIZZLE_IDENTITY,
   135. VK_COMPONENT_SWIZZLE_IDENTITY
   136. },
   137. .subresourceRange = {VK_IMAGE_ASPECT_COLOR_BIT, 0, 1, 0, 1},
   138. };
   139. CheckResult(vkCreateImageView(device, &view, nullptr, &externalTextureInfo.view));

   141. // Create sampler
   142. const VkSamplerCreateInfo sampler = {
   143. .sType = VK_STRUCTURE_TYPE_SAMPLER_CREATE_INFO,
   144. .pNext = &convInfoWrap,
   145. .magFilter = VK_FILTER_NEAREST,
   146. .minFilter = VK_FILTER_NEAREST,
   147. .mipmapMode = VK_SAMPLER_MIPMAP_MODE_NEAREST,
   148. .addressModeU = VK_SAMPLER_ADDRESS_MODE_CLAMP_TO_EDGE,
   149. .addressModeV = VK_SAMPLER_ADDRESS_MODE_CLAMP_TO_EDGE,
   150. .addressModeW = VK_SAMPLER_ADDRESS_MODE_CLAMP_TO_EDGE,
   151. .mipLodBias = 0.0f,
   152. .compareEnable = VK_FALSE,
   153. .anisotropyEnable = VK_FALSE,
   154. .maxAnisotropy = 1,
   155. .compareOp = VK_COMPARE_OP_NEVER,
   156. .minLod = 0.0f,
   157. .maxLod = 0.0f,
   158. .borderColor = VK_BORDER_COLOR_FLOAT_OPAQUE_WHITE,
   159. .unnormalizedCoordinates = VK_FALSE
   160. };
   161. CheckResult(vkCreateSampler(device, &sampler, nullptr, &externalTextureInfo.sampler));

   163. createDescriptorSetLayout();
   164. createDescriptorSet();

   166. VkDescriptorImageInfo imageInfo = {
   167. .sampler = externalTextureInfo.sampler,
   168. .imageView = externalTextureInfo.view,
   169. .imageLayout = VK_IMAGE_LAYOUT_SHADER_READ_ONLY_OPTIMAL
   170. };

   172. VkDescriptorBufferInfo bufferInfo = {
   173. .buffer = buffersInfo.uniformBuf, .offset = 0, .range = sizeof(UniformBufferObject)};
   174. VkWriteDescriptorSet bufferWrite = {.sType = VK_STRUCTURE_TYPE_WRITE_DESCRIPTOR_SET,
   175. .dstSet = gfxPipelineInfo.descSet,
   176. .dstBinding = 0,
   177. .dstArrayElement = 0,
   178. .descriptorCount = 1,
   179. .descriptorType = VK_DESCRIPTOR_TYPE_UNIFORM_BUFFER,
   180. .pImageInfo = nullptr,
   181. .pBufferInfo = &bufferInfo,
   182. .pTexelBufferView = nullptr};
   183. VkWriteDescriptorSet imageWrite = {.sType = VK_STRUCTURE_TYPE_WRITE_DESCRIPTOR_SET,
   184. .dstSet = gfxPipelineInfo.descSet,
   185. .dstBinding = 1,
   186. .dstArrayElement = 0,
   187. .descriptorCount = 1,
   188. .descriptorType = VK_DESCRIPTOR_TYPE_COMBINED_IMAGE_SAMPLER,
   189. .pImageInfo = &imageInfo,
   190. .pBufferInfo = nullptr,
   191. .pTexelBufferView = nullptr};
   192. gfxPipelineInfo.descWrites[0] = bufferWrite;
   193. gfxPipelineInfo.descWrites[1] = imageWrite;
   194. vkUpdateDescriptorSets(device, 2, gfxPipelineInfo.descWrites, 0, nullptr);

   196. createGraphicsPipeline();
   197. createOtherStaff();

   199. recordCommandBuffer();
   200. OH_LOG_INFO(LOG_APP, "hwBufferToTexture end");
   201. }
   ```

   [VulkanRender.cpp](https://gitcode.com/HarmonyOS_Samples/video-render/blob/master/entry/src/main/cpp/render/src/VulkanRender.cpp#L796-L996)

## 示例代码

* [渲染视频数据](https://gitcode.com/harmonyos_samples/video-render)
