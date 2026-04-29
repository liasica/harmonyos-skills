---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-image-to-video-synthesis
title: 图片合成视频开发实践
breadcrumb: 最佳实践 > 媒体 > 音频和视频 > 图片合成视频开发实践
category: best-practices
scraped_at: 2026-04-29T14:11:41+08:00
doc_updated_at: 2026-04-01
content_hash: sha256:d343a5a559281bfae61a6421a419bc0a58d10347f2e6d106cc1b7564fd7f2213
---

## 概述

在个人相册制作、电商产品展示、理财销售回放等多个场景中，都需要将图片合成视频。开发者通过调用Image Kit、视频编码、媒体数据封装提供的接口，可以实现图片合成视频的功能。

* [Image Kit](../harmonyos-guides/image-overview.md)提供图片的解码、编码、编辑、元数据处理等功能。
* [视频编码](../harmonyos-guides/video-encoding.md)可将未压缩的视频数据压缩为视频码流，如H.264、H.265。
* [媒体数据封装](../harmonyos-guides/audio-video-muxer.md)可完成媒体文件的封装，将编码后的音视频数据，按一定的格式写入媒体文件中。

本文以图库图片合成视频场景为例，介绍图片解码、图片数据编码、视频生成的主要步骤，并给出开发过程中常见问题的分析思路和解决方案。

## 图库图片合成视频

### 场景描述

以将图库中的图片转换为MP4文件为例，本场景展示使用图片和编解码的基础能力来实现图片合成视频的功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/xgC0AOLHQ7ydMSvoHepNyw/zh-cn_image_0000002529433631.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061138Z&HW-CC-Expire=86400&HW-CC-Sign=ACF9738E8179B5BE5C0D3B5C8A33C8C5E57F5381EA3B0BF09C896AF87D0EED4B "点击放大")

### 实现原理

[Image Kit](../harmonyos-guides/image-overview.md)中的[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)是用于读取或写入图像数据以及获取图像信息的图像像素类。在图片合成视频的过程中，首先将图片解码为PixelMap，然后使用[Buffer模式](../harmonyos-guides/video-encoding.md#buffer模式)编码，将PixelMap中保存的图像数据复制到编码器的输入buffer中，未压缩的YUV输出成已压缩的视频码流H.264，编码完成后封装成视频文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/3XUtnc3-RnCYucFz1E-nVQ/zh-cn_image_0000002497593680.png?HW-CC-KV=V1&HW-CC-Date=20260429T061138Z&HW-CC-Expire=86400&HW-CC-Sign=D86A8FEE70C38AD43FDBDBA42A904FC191962540A8A9BAF631BDB4D0AB75A014)

如果需要使用[Surface模式](../harmonyos-guides/video-encoding.md#surface模式)编码，将图片解码成PixelMap后，需要先从编码器的NativeWindow申请buffer，然后将PixelMap中保存的图像数据复制到申请的buffer中并提交buffer，编码完成后再封装为视频文件，具体实现可以参考[NativeWindow开发指导 (C/C++)](../harmonyos-guides/native-window-guidelines.md)。

### 开发步骤

1. 使用[PhotoViewPicker](../harmonyos-references/arkts-apis-photoaccesshelper-photoviewpicker.md)从图库中选择图片，数量不少于两张。当选择数量不足两张时，将弹出提示框。

   ```
   1. // Use photoAccessHelper to pull up the gallery and select images.
   2. let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
   3. photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
   4. let photoPicker = new photoAccessHelper.PhotoViewPicker();
   5. photoPicker.select(photoSelectOptions)
   6. .then(async (PhotoSelectResult: photoAccessHelper.PhotoSelectResult) => {
   7. this.imageUri = PhotoSelectResult.photoUris;
   8. if (this.imageUri.length < 2) {
   9. this.showToast($r('app.string.Please_select_at_least_two_images'), 2000);
   10. return;
   11. } else {
   12. this.dialogController.open();
   13. await this.processImages();
   14. this.synthesis();
   15. }
   16. })
   17. .catch((err: BusinessError) => {
   18. hilog.error(0x0000, TAG, `PhotoViewPicker.select failed, error: ${err.code}, ${err.message}`);
   19. });
   ```

   [Index.ets](https://gitcode.com/harmonyos_samples/ImageToVideo/blob/master/entry/src/main/ets/pages/Index.ets#L158-L176)
2. 遍历处理从图库选择的图片。

   （1）读取图片数据并创建ImageSource。

   （2）配置图片解码参数，使用[imageSource.createPixelMap()](../harmonyos-references/arkts-apis-image-imagesource.md#createpixelmap7)获取解码后的PixelMap。

   （3）将PixelMap保存到队列中。

   ```
   1. // Decode the image and pass it to the native.
   2. async processImages() {
   3. for (let i = 0; i < this.imageUri.length; i++) {
   4. // Read image file data.
   5. let imgData: ArrayBuffer | undefined;
   6. let imgFile: fileIo.File | undefined;
   7. try {
   8. imgFile = fileIo.openSync(this.imageUri[i], fileIo.OpenMode.READ_ONLY);
   9. let stat: fileIo.Stat = fileIo.statSync(imgFile.fd);
   10. imgData = new ArrayBuffer(stat.size);
   11. fileIo.readSync(imgFile.fd, imgData);
   12. } catch (err) {
   13. hilog.error(0x0000, 'testTag', `failed to open uri. code=${err.code},message=${err.message}`);
   14. } finally {
   15. if (imgFile) {
   16. try {
   17. fileIo.closeSync(imgFile);
   18. } catch (err) {
   19. hilog.error(0x0000, 'testTag', `failed to close fileIo. code=${err.code},message=${err.message}`);
   20. }
   21. }
   22. }
   23. // Decoding images.
   24. let imageSource: image.ImageSource | undefined;
   25. let pixelMap: image.PixelMap | undefined;
   26. try {
   27. imageSource = image.createImageSource(imgData);
   28. // Set the decoding bitmap size to be consistent with the first image.
   29. if (this.imageWidth === 0 && this.imageHeight === 0) {
   30. let imageInfo: image.ImageInfo = imageSource.getImageInfoSync();
   31. this.imageWidth = imageInfo.size.width;
   32. this.imageHeight = imageInfo.size.height;
   33. }
   34. let decodingOptions: image.DecodingOptions = {
   35. editable: true,
   36. desiredPixelFormat: image.PixelMapFormat.NV12,
   37. desiredSize: { width: this.imageWidth, height: this.imageHeight }
   38. }
   39. pixelMap = await imageSource.createPixelMap(decodingOptions);
   40. transcoding.pushPixelMap(pixelMap);
   41. } catch (err) {
   42. hilog.error(0x0000, 'testTag', `failed to add pictures. code=${err.code},message=${err.message}`);
   43. } finally {
   44. if (imageSource) {
   45. imageSource.release();
   46. }
   47. if (pixelMap) {
   48. pixelMap.release();
   49. }
   50. }
   51. }
   52. }
   ```

   [Index.ets](https://gitcode.com/harmonyos_samples/ImageToVideo/blob/master/entry/src/main/ets/pages/Index.ets#L221-L273)
3. 创建编码器和封装器。

   （1）初始化视频编码环境。

   ```
   1. // Initialize the encoder environment, create and configure the muxer.
   2. int32_t Transcoding::InitEncoder() {
   3. CHECK_AND_RETURN_RET_LOG(!isStarted_, AVCODEC_SAMPLE_ERR_ERROR, "Already started.");
   4. CHECK_AND_RETURN_RET_LOG(muxer_ == nullptr && videoEncoder_ == nullptr, AVCODEC_SAMPLE_ERR_ERROR,
   5. "Already started.");

   7. videoEncoder_ = std::make_unique<VideoEncoder>();
   8. muxer_ = std::make_unique<Muxer>();

   10. int32_t ret = muxer_->Create(sampleInfo_.outputFd);
   11. CHECK_AND_RETURN_RET_LOG(ret == AVCODEC_SAMPLE_ERR_OK, ret, "Create muxer with fd(%{public}d) failed",
   12. sampleInfo_.outputFd);
   13. ret = muxer_->Config(sampleInfo_);

   15. CHECK_AND_RETURN_RET_LOG(ret == AVCODEC_SAMPLE_ERR_OK, ret, "Create audio encoder failed");

   17. ret = CreateVideoEncoder();
   18. CHECK_AND_RETURN_RET_LOG(ret == AVCODEC_SAMPLE_ERR_OK, ret, "Create video encoder failed");

   20. AVCODEC_SAMPLE_LOGI("Succeed");
   21. return AVCODEC_SAMPLE_ERR_OK;
   22. }
   ```

   [Transcoding.cpp](https://gitcode.com/harmonyos_samples/ImageToVideo/blob/master/entry/src/main/cpp/transcoding/Transcoding.cpp#L69-L90)

   （2）创建封装器。

   ```
   1. int32_t Muxer::Create(int32_t fd) {
   2. muxer_ = OH_AVMuxer_Create(fd, AV_OUTPUT_FORMAT_MPEG_4);
   3. CHECK_AND_RETURN_RET_LOG(muxer_ != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "Muxer create failed, fd: %{public}d", fd);
   4. return AVCODEC_SAMPLE_ERR_OK;
   5. }
   ```

   [Muxer.cpp](https://gitcode.com/harmonyos_samples/ImageToVideo/blob/master/entry/src/main/cpp/capbilities/Muxer.cpp#L31-L35)

   （3）创建编码器。

   ```
   1. // Create and configure encoder.
   2. int32_t Transcoding::CreateVideoEncoder() {
   3. int32_t ret = videoEncoder_->Create(sampleInfo_.outputVideoCodecMime);
   4. CHECK_AND_RETURN_RET_LOG(ret == AVCODEC_SAMPLE_ERR_OK, ret, "Create video encoder failed");

   6. videoEncContext_ = new CodecUserData;
   7. ret = videoEncoder_->Config(sampleInfo_, videoEncContext_);
   8. CHECK_AND_RETURN_RET_LOG(ret == AVCODEC_SAMPLE_ERR_OK, ret, "Encoder config failed");

   10. return AVCODEC_SAMPLE_ERR_OK;
   11. }
   ```

   [Transcoding.cpp](https://gitcode.com/harmonyos_samples/ImageToVideo/blob/master/entry/src/main/cpp/transcoding/Transcoding.cpp#L55-L65)
4. 对图片进行编码和封装。

   （1）启动编码器和封装器，启动编码输入输出处理线程。

   ```
   1. // Start the encoder, create input and output thread.
   2. int32_t Transcoding::Start() {
   3. std::unique_lock<std::mutex> lock(mutex_);
   4. int32_t ret;
   5. CHECK_AND_RETURN_RET_LOG(!isStarted_, AVCODEC_SAMPLE_ERR_ERROR, "Already started.");
   6. if (videoEncContext_) {
   7. CHECK_AND_RETURN_RET_LOG(videoEncoder_ != nullptr && muxer_ != nullptr, AVCODEC_SAMPLE_ERR_ERROR,
   8. "Already started.");
   9. int32_t ret = muxer_->Start();
   10. CHECK_AND_RETURN_RET_LOG(ret == AVCODEC_SAMPLE_ERR_OK, ret, "Muxer start failed");
   11. ret = videoEncoder_->Start();
   12. isStarted_ = true;
   13. CHECK_AND_RETURN_RET_LOG(ret == AVCODEC_SAMPLE_ERR_OK, ret, "Encoder start failed");
   14. videoEncInputThread_ = std::make_unique<std::thread>(&Transcoding::VideoEncInputThread, this);
   15. videoEncOutputThread_ = std::make_unique<std::thread>(&Transcoding::VideoEncOutputThread, this);
   16. if (videoEncInputThread_ == nullptr || videoEncOutputThread_ == nullptr) {
   17. AVCODEC_SAMPLE_LOGE("Create thread failed");
   18. StartRelease();
   19. return AVCODEC_SAMPLE_ERR_ERROR;
   20. }
   21. }
   22. if (isReleased_) {
   23. isReleased_ = false;
   24. videoEncContext_->outputFrameCount = 0;
   25. }
   26. AVCODEC_SAMPLE_LOGI("Succeed");
   27. doneCond_.notify_all();
   28. return AVCODEC_SAMPLE_ERR_OK;
   29. }
   ```

   [Transcoding.cpp](https://gitcode.com/harmonyos_samples/ImageToVideo/blob/master/entry/src/main/cpp/transcoding/Transcoding.cpp#L94-L122)

   （2）编码器输入线程从PixelMap队列中取出待编码数据，然后复制到编码器输入队列中。

   ```
   1. // Encoding input thread.
   2. void Transcoding::VideoEncInputThread() {
   3. while (true) {
   4. OH_LOG_ERROR(LOG_APP, "do VideoEncInputThread while");
   5. std::unique_lock<std::mutex> lock(videoEncContext_->outputMutex);
   6. bool condRet = videoEncContext_->inputCond.wait_for(
   7. lock, 5s, [this]() { return !isStarted_ || !videoEncContext_->inputBufferInfoQueue.empty(); });
   8. CHECK_AND_BREAK_LOG(isStarted_, "Work done, thread out");
   9. CHECK_AND_CONTINUE_LOG(!videoEncContext_->inputBufferInfoQueue.empty(),
   10. "Buffer queue is empty, continue, cond ret: %{public}d", condRet);
   11. // get Buffer from inputBufferInfoQueue.
   12. CodecBufferInfo bufferInfo = videoEncContext_->inputBufferInfoQueue.front();
   13. videoEncContext_->inputBufferInfoQueue.pop();
   14. videoEncContext_->inputFrameCount++;
   15. lock.unlock();
   16. if (!pictures.empty()) {
   17. // Get the data of the current frame.
   18. OH_PixelmapNative *currentFrame = pictures.front();
   19. pictures.pop();
   20. CopyStrideYUV420SP(bufferInfo, currentFrame);
   21. } else {
   22. bufferInfo.attr.size = 0;
   23. bufferInfo.attr.offset = 0;
   24. bufferInfo.attr.pts = 0;
   25. bufferInfo.attr.flags = AVCODEC_BUFFER_FLAGS_EOS;
   26. }
   27. int32_t ret = videoEncoder_->PushInputBuffer(bufferInfo);
   28. CHECK_AND_BREAK_LOG(ret == AVCODEC_SAMPLE_ERR_OK, "Push data failed, thread out");
   29. AVCODEC_SAMPLE_LOGW(
   30. "Out bufferInfo flags: %{public}u, offset: %{public}d, pts: %{public}u, size: %{public}" PRId64,
   31. bufferInfo.attr.flags, bufferInfo.attr.offset, bufferInfo.attr.pts, bufferInfo.attr.size);
   32. if (bufferInfo.attr.flags & AVCODEC_BUFFER_FLAGS_EOS) {
   33. AVCODEC_SAMPLE_LOGW("VideoDecOutputThread Catch EOS, thread out" PRId64);
   34. break;
   35. }
   36. }
   37. }
   ```

   [Transcoding.cpp](https://gitcode.com/harmonyos_samples/ImageToVideo/blob/master/entry/src/main/cpp/transcoding/Transcoding.cpp#L221-L257)

   （3）编码器输出线程从编码器输出队列中取出已编码的数据送入封装器。

   ```
   1. // Encoding output thread.
   2. void Transcoding::VideoEncOutputThread() {
   3. while (true) {
   4. std::unique_lock<std::mutex> lock(videoEncContext_->outputMutex);
   5. bool condRet = videoEncContext_->outputCond.wait_for(
   6. lock, 5s, [this]() { return !isStarted_ || !videoEncContext_->outputBufferInfoQueue.empty(); });
   7. CHECK_AND_BREAK_LOG(isStarted_, "Work done, thread out");
   8. CHECK_AND_CONTINUE_LOG(!videoEncContext_->outputBufferInfoQueue.empty(),
   9. "Buffer queue is empty, continue, cond ret: %{public}d", condRet);

   11. CodecBufferInfo bufferInfo = videoEncContext_->outputBufferInfoQueue.front();
   12. videoEncContext_->outputBufferInfoQueue.pop();
   13. CHECK_AND_BREAK_LOG(!(bufferInfo.attr.flags & AVCODEC_BUFFER_FLAGS_EOS),
   14. "VideoEncOutputThread  Catch EOS, thread out");
   15. lock.unlock();
   16. if ((bufferInfo.attr.flags & AVCODEC_BUFFER_FLAGS_SYNC_FRAME) ||
   17. (bufferInfo.attr.flags == AVCODEC_BUFFER_FLAGS_NONE)) {
   18. videoEncContext_->outputFrameCount++;
   19. bufferInfo.attr.pts = videoEncContext_->outputFrameCount * MICROSECOND / sampleInfo_.outputFrameRate;
   20. } else {
   21. bufferInfo.attr.pts = 0;
   22. }
   23. AVCODEC_SAMPLE_LOGW("Out buffer count: %{public}u, size: %{public}d, flag: %{public}u, pts: %{public}" PRId64,
   24. videoEncContext_->outputFrameCount, bufferInfo.attr.size, bufferInfo.attr.flags,
   25. bufferInfo.attr.pts);
   26. muxer_->WriteSample(muxer_->GetVideoTrackId(), reinterpret_cast<OH_AVBuffer *>(bufferInfo.buffer),
   27. bufferInfo.attr);
   28. int32_t ret = videoEncoder_->FreeOutputBuffer(bufferInfo.bufferIndex);
   29. CHECK_AND_BREAK_LOG(ret == AVCODEC_SAMPLE_ERR_OK, "Encoder output thread out");
   30. CHECK_AND_BREAK_LOG(videoEncContext_->outputFrameCount != sampleInfo_.imgCount, "Encoder output thread out");
   31. }
   32. AVCODEC_SAMPLE_LOGI("Exit, frame count: %{public}u", videoEncContext_->outputFrameCount);
   33. StartRelease();
   34. }
   ```

   [Transcoding.cpp](https://gitcode.com/harmonyos_samples/ImageToVideo/blob/master/entry/src/main/cpp/transcoding/Transcoding.cpp#L261-L294)
5. 所有图片都处理完成后，使用[Video](../harmonyos-references/ts-media-components-video.md)组件播放合成后的视频。

   ```
   1. // Play videos using the Video component.
   2. Video({
   3. src: this.videoSrc,
   4. controller: this.controller
   5. })
   6. .width('100%')
   7. .height('100%')
   8. .autoPlay(true)
   9. .controls(false)
   10. .objectFit(1)
   11. .zIndex(0)
   12. .onPrepared((event) => {
   13. if (event) {
   14. this.durationTime = event.duration;
   15. }
   16. })
   17. .onUpdate((event) => {
   18. if (event) {
   19. this.currentTime = event.time;
   20. }
   21. })
   22. .onFinish(() => {
   23. this.isStart = !this.isStart;
   24. })
   25. .transition(TransitionEffect.OPACITY.animation({ duration: 1000, curve: Curve.Sharp }))
   ```

   [Index.ets](https://gitcode.com/harmonyos_samples/ImageToVideo/blob/master/entry/src/main/ets/pages/Index.ets#L81-L105)
6. 使用[SaveButton](../harmonyos-references/ts-security-components-savebutton.md)安全控件，将视频保存到图库。

   （1）创建安全控件按钮。

   ```
   1. // Use SaveButton Component to Save Video.
   2. SaveButton({ text: SaveDescription.SAVE_TO_GALLERY })
   3. .width('100%')
   4. .height(40)
   5. .backgroundColor(this.showVideo ? 'rgba(10,89,247)' : 'rgba(10,89,247,0.4)')
   6. .onClick(async (event, result: SaveButtonOnClickResult) => {
   7. if (!this.showVideo) {
   8. return;
   9. }
   10. if (result === SaveButtonOnClickResult.SUCCESS) {
   11. try {
   12. this.saveVideo();
   13. this.showToast($r('app.string.Save_Success'));
   14. } catch (err) {
   15. hilog.error(0x0000, TAG, 'createAsset failed, error: ' + JSON.stringify(err));
   16. }
   17. } else {
   18. hilog.error(0x0000, TAG, 'SaveButtonOnClickResult create asset failed.');
   19. }
   20. })
   ```

   [Index.ets](https://gitcode.com/harmonyos_samples/ImageToVideo/blob/master/entry/src/main/ets/pages/Index.ets#L192-L211)

   （2）调用[MediaAssetChangeRequest.createImageAssetRequest()](../harmonyos-references/kts-apis-photoaccesshelper-mediaassetchangerequest.md#createimageassetrequest11)和[PhotoAccessHelper.applyChanges()](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#applychanges11)接口，将视频保存到图库。

   ```
   1. // Save videos using photoAccessHelper.
   2. saveVideo() {
   3. let context = this.getUIContext().getHostContext();
   4. let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
   5. let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest | undefined;
   6. try {
   7. assetChangeRequest =
   8. photoAccessHelper.MediaAssetChangeRequest.createVideoAssetRequest(context, this.videoSrc);
   9. } catch (error) {
   10. let err = error as BusinessError;
   11. hilog.error(0x0000, 'openSync', `openSync failed. code =${err.code}, message =${err.message}`);
   12. }
   13. phAccessHelper.applyChanges(assetChangeRequest).then(() => {
   14. hilog.info(0x0000, 'testTag', '%{public}s', 'apply Changes successfully');
   15. }).catch((err: BusinessError) => {
   16. hilog.error(0x0000, 'testTag', `apply Changes failed. code=${err.code},message=${err.message}`);
   17. });
   18. }
   ```

   [Index.ets](https://gitcode.com/harmonyos_samples/ImageToVideo/blob/master/entry/src/main/ets/pages/Index.ets#L300-L318)

## 常见问题

### 合成后的视频出现花屏

**问题根因**

buffer复制时没有考虑跨距的问题。视频编码需要注意宽高对齐，处理对应的跨距。

**解决方案**

将图片数据复制到编码器的输入buffer时，应依据编码器的跨距值进行复制，跨距值可通过接口[OH\_VideoEncoder\_GetInputDescription()](../harmonyos-references/capi-native-avcodec-videoencoder-h.md#oh_videoencoder_getinputdescription)获取。

1. 获取编码器的跨距值。

   ```
   1. // Add the index and pointer of the input buffer to the inputBufferInfoQueue.
   2. void SampleCallback::OnNeedInputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData) {
   3. if (userData == nullptr) {
   4. return;
   5. }
   6. CodecUserData *codecUserData = static_cast<CodecUserData *>(userData);
   7. // Process the first frame and obtain the width, height, and stride of the image.
   8. if (codecUserData->isEncFirstFrame) {
   9. OH_AVFormat *format = OH_VideoEncoder_GetInputDescription(codec);
   10. OH_AVFormat_GetIntValue(format, OH_MD_KEY_VIDEO_PIC_WIDTH, &codecUserData->width);
   11. OH_AVFormat_GetIntValue(format, OH_MD_KEY_VIDEO_PIC_HEIGHT, &codecUserData->height);
   12. OH_AVFormat_GetIntValue(format, OH_MD_KEY_VIDEO_STRIDE, &codecUserData->widthStride);
   13. OH_AVFormat_GetIntValue(format, OH_MD_KEY_VIDEO_SLICE_HEIGHT, &codecUserData->heightStride);
   14. OH_AVFormat_Destroy(format);
   15. codecUserData->isEncFirstFrame = false;
   16. }
   17. std::unique_lock<std::mutex> lock(codecUserData->inputMutex);
   18. codecUserData->inputBufferInfoQueue.emplace(index, buffer);
   19. codecUserData->inputCond.notify_all();
   20. }
   ```

   [SampleCallback.cpp](https://gitcode.com/harmonyos_samples/ImageToVideo/blob/master/entry/src/main/cpp/common/SampleCallback.cpp#L40-L59)
2. 按照编码器的跨距值进行复制。

   ```
   1. // Copy the YUV 420SP format image data into the buffer while considering the stride of the image.
   2. void Transcoding::CopyStrideYUV420SP(CodecBufferInfo &bufferInfo, OH_PixelmapNative *pixelmap) {
   3. // Obtain the info of the Pixelmap.
   4. OH_Pixelmap_ImageInfo *imageInfo = nullptr;
   5. OH_PixelmapImageInfo_Create(&imageInfo);
   6. OH_PixelmapNative_GetImageInfo(pixelmap, imageInfo);
   7. uint32_t width;
   8. uint32_t height;
   9. OH_PixelmapImageInfo_GetWidth(imageInfo, &width);
   10. OH_PixelmapImageInfo_GetHeight(imageInfo, &height);
   11. OH_PixelmapImageInfo_Release(imageInfo);

   13. // Read the data of the current frame to oneFrameData.
   14. size_t bufferSize = width * height * 3 / 2;
   15. uint8_t *oneFrameData = new uint8_t[bufferSize];
   16. OH_PixelmapNative_ReadPixels(pixelmap, oneFrameData, &bufferSize);
   17. uint8_t *inputBufferAddr = OH_AVBuffer_GetAddr(reinterpret_cast<OH_AVBuffer *>(bufferInfo.buffer));
   18. // handle Stride.
   19. uint8_t *dst = inputBufferAddr;
   20. uint8_t *src = oneFrameData;
   21. uint32_t srcHeight = height;
   22. int32_t videoStrideWidth = videoEncContext_->widthStride;
   23. int32_t videoStrideHeight = videoEncContext_->heightStride;
   24. // Y -> Copy the source data of region Y to the target data of another region.
   25. for (int32_t i = 0; i < srcHeight; ++i) {
   26. std::memcpy(dst, src, width);
   27. dst += videoStrideWidth;
   28. src += width;
   29. }
   30. // padding -> Update pointers to both the data source and target data, with pointers moving down one
   31. // padding.
   32. dst += (videoStrideHeight - height) * videoStrideWidth;
   33. srcHeight >>= 1;
   34. // UV -> Copy the source data of the UV area to the target data of another area.
   35. for (int32_t i = 0; i < srcHeight; ++i) {
   36. std::memcpy(dst, src, width);
   37. dst += videoStrideWidth;
   38. src += width;
   39. }
   40. bufferInfo.attr.size = videoStrideWidth * videoStrideHeight * 3 / 2;
   41. bufferInfo.attr.flags = AVCODEC_BUFFER_FLAGS_NONE;
   42. delete[] oneFrameData;
   43. }
   ```

   [Transcoding.cpp](https://gitcode.com/harmonyos_samples/ImageToVideo/blob/master/entry/src/main/cpp/transcoding/Transcoding.cpp#L175-L217)

## 示例代码

* [实现图片合成视频功能](https://gitcode.com/harmonyos_samples/ImageToVideo/tree/master)
