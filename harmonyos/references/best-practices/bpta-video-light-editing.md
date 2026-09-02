---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-video-light-editing
title: 视频轻编辑开发实践
breadcrumb: 最佳实践 > 行业场景解决方案 > 影音娱乐 > 视频轻编辑开发实践
category: best-practices
scraped_at: 2026-09-02T15:03:20+08:00
doc_updated_at: 2026-08-17
content_hash: sha256:f3b9ff55bcdb930b7c3fe5437c248b56589a7663973220ed4d968dddb17f5792
---

## 概述

在短视频社交、生活记录及轻量内容创作等场景中，用户需在移动端完成全链路操作，流程包括：选视频、预览、加贴纸/文字/配乐、裁剪、导出分享。视频轻编辑强调编辑的实时性，HarmonyOS视频编辑SDK基于[Pipeline](bpta-maleoon-gpu-best-practices.md#section10631102319132)并行、自适应高频编解码、GPU高效渲染，提升音视频编辑的效率。本文将基于媒体能力，重点介绍以下视频轻编辑的典型场景：

* [视频编辑预览](bpta-video-light-editing.md#section16868173694413)
* [视频添加文字](bpta-video-light-editing.md#section1957241019189)
* [视频添加图片](bpta-video-light-editing.md#section1420112811191)
* [视频添加背景音乐](bpta-video-light-editing.md#section4265113218192)
* [音频格式转换和混音](bpta-video-light-editing.md#section101747111207)
* [视频分辨率调整](bpta-video-light-editing.md#section145221012192014)
* [视频格式转码](bpta-video-light-editing.md#section1087321362015)
* [视频裁剪](bpta-video-light-editing.md#section1554110107507)
* [视频编辑保存导出](bpta-video-light-editing.md#section18709135205117)

## 视频编辑预览

### 场景描述

视频编辑预览是视频编辑的核心功能之一，允许用户在编辑过程中实时查看视频效果。用户可以通过拉起图库选择单个视频文件后进入编辑页，编辑页上方约70%区域为视频预览区，下方30%为编辑操作区。视频导入后自动播放，预览过程中支持播放、循环播放等操作，同时支持在视频上方叠加贴纸和文字等元素。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/wNnuEOUWRSKYDUERY4CeMA/zh-cn_image_0000002680339558.gif "点击放大")

### 实现原理

预览阶段采用解码直出+UI叠加的轻量方案，不经过IGLRenderEngine，与导出侧InSurface/OutSurface链路形成对照，从而在编辑过程中保持较低延迟。调用时序图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/d0SsR6i9SGul_ZE6OM0t3w/zh-cn_image_0000002710019335.png "点击放大")

### 开发步骤

1. 点击选择视频按钮，通过InitEditor()初始化编辑器。

   ```typescript
   Button() {
     Text($r('app.string.select_video'))
       .fontSize(16)
       .fontColor(Color.White)
       .fontWeight(FontWeight.Bold)
   }
   .type(ButtonType.Capsule)
   .backgroundColor('#007DFF')
   .height(40)
   .width('100%')

   .onClick(() => {
     sdk.InitEditor();
     this.selectVideo();
   })
   ```

   ```cpp
   static napi_value InitEditor(napi_env env, [[maybe_unused]] napi_callback_info info)
   {
       Interface::InitEditor();
       return ToJsUndefined(env);
   }
   ```
2. 使用[Class(PhotoViewPicker)](../harmonyos-references/arkts-apis-photoaccesshelper-photoviewpicker.md)从图库中选择视频，选择视频后，将视频参数videoUri和fd通过sdk.SetVideo()传给Native侧，同步初始化VideoAsset（时长、分辨率等），供后续裁剪与导出使用。

   ```typescript
   async selectVideo() {
     try {
       let options: photoAccessHelper.PhotoSelectOptions = {
         MIMEType: photoAccessHelper.PhotoViewMIMETypes.VIDEO_TYPE,
         isEditSupported: false,
         maxSelectNumber: 1,
         isPhotoTakingSupported: false,
         isSearchSupported: true,
         isOriginalSupported: true
       };
       let photoPicker = new photoAccessHelper.PhotoViewPicker();
       photoPicker.select(options).then((selectResult: photoAccessHelper.PhotoSelectResult) => {
         Logger.info(TAG, 'select video success');
         if (selectResult.photoUris.length == 0) {
           Logger.info(TAG, 'no photo are selected.');
         } else {
           selectResult.photoUris.forEach((uri) => {
             this.videoUri = uri;
             this.file = fs.openSync(this.videoUri);
             this.fd = this.file.fd;
             let res: number = sdk.SetVideo(this.videoUri, this.fd);
             if (res === 0) {
               let videoAsset: VideoAsset = {
                 videoUri: this.videoUri,
                 fd: this.fd,
                 screenWidth: this.screenWidth,
                 screenHeight: this.screenHeight
               };
               this.getUIContext().getRouter().replaceUrl({ url: 'pages/VideoEdit', params: videoAsset })
                 .catch((error: BusinessError) => {
                   Logger.error(`replaceUrl failed, code is ${error.code}, message is ${error.message}`);
                 })
             } else {
               this.isSuccessful = 1;
             }
           });
         }
       }).catch((err: BusinessError) => {
         Logger.error(TAG, `PhotoPicker,select failed with err: ${err.code},${err.message}`);
       });
     } catch (error) {
       let err: BusinessError = error as BusinessError;
       Logger.error(TAG, `PhotoPicker,select failed with err: ${err.code},${err.message}`);
     }
   }
   ```
3. 创建XComponent渲染组件，通过XComponent组件进行实时预览播放。

   ```typescript
   XComponent({
     id: '',
     type: XComponentType.SURFACE,
     libraryname: 'veditor',
     controller: this.xComponentController
   })
     .onLoad(() => {
       this.testFetchFrameByTime();
       // The width of the container for XComponent
       let containerWidth = this.getUIContext().vp2px(this.params.screenWidth as number);
       let containerHeight = this.getUIContext().vp2px((this.params.screenHeight as number) * 0.7);
       // Calculate the height based on the width of the container and the aspect ratio of the video
       sdk.SetCanvasSize(containerHeight, containerWidth);
       const videoInfo: Point[] | undefined = sdk.GetDrawableArea();
       if (videoInfo !== undefined) {
         const videoX = videoInfo[0]?.x;
         const videoY = videoInfo[0]?.y;
         const videoWidth = videoInfo[1]?.x - videoInfo[0]?.x;
         const videoHeight = videoInfo[3]?.y - videoInfo[0]?.y;
         // Calculate the video boundaries and save them
         // Update video boundary information
         this.state.videoRect = {
           x: videoX,
           y: videoY,
           width: videoWidth,
           height: videoHeight
         };
         this.xComponentController.setXComponentSurfaceRect({
           offsetX: (containerWidth + 1 - videoWidth) / 2,
           offsetY: (containerHeight + 1 - videoHeight) / 2, // Centered video
           surfaceWidth: videoWidth,
           surfaceHeight: videoHeight
         });
         this.state.surfaceID = this.xComponentController.getXComponentSurfaceId();
         sdk.Play();
       }
     })
   ```
4. 初始化预览引擎。

   ```cpp
   VEditorStatus Editor::PreparePreviewEngine(int32_t fd)
   {
       LOGI("Editor::PreparePreviewEngine.");
       LOGD("Editor::PreparePreviewEngine fd is %{public}d.", fd);
       std::shared_ptr<VideoAsset> mainVideo = m_timeline->GetMainVideo();
       if (!mainVideo) {
           LOGE("Editor::PreparePreviewEngine no mainVideo.");
           return VEditorStatus::STATUS_ERROR;
       }
       // Create Decoder
       std::shared_ptr<IAVDecoderEngine> decoderEngine = IAVDecoderEngine::Create(fd, previewDecoderCallback);
       if (!decoderEngine) {
           LOGE("Editor::PreparePreviewEngine Create preview decoder engine failed.");
           return VEditorStatus::STATUS_ERROR;
       }
       m_previewEngine = decoderEngine;
       return VEditorStatus::STATUS_OK;
   }
   ```
5. 通过SetPreviewWindow()设置预览窗口并启动播放。

   ```cpp
   void Editor::SetPreviewWindow(OHNativeWindow *window)
   {
       LOGI("Editor::SetPreviewWindow.");
       if (!window || !m_previewEngine) {
           LOGE("Editor::SetPreviewWindow window or engine is nullptr .");
           return;
       }
       m_previewWindow = window;
       m_previewEngine->SetVideoOutputWindow(m_previewWindow);
       m_previewEngine->Init();
           
       OH_AVFormat *format = m_previewEngine->GetVideoFormat();
       if (!format) {
           LOGE("Editor::SetPreviewWindow no Video format.");
           return;
       }
       
       int64_t originalDuration = m_previewEngine->GetVideoDuration();
       if (originalDuration <= 0) {
           LOGE("Editor::SetPreviewWindow get video duration failed.");
           return;
       }
       
       int32_t width = 0;
       int32_t height = 0;
       int32_t rotation = 0;
       OH_AVFormat_GetIntValue(format, OH_MD_KEY_HEIGHT, &height);
       OH_AVFormat_GetIntValue(format, OH_MD_KEY_WIDTH, &width);
       OH_AVFormat_GetIntValue(format, OH_MD_KEY_ROTATION, &rotation);
       
       std::shared_ptr<VideoAsset> mainVideo = m_timeline->GetMainVideo();
       if (!mainVideo) {
           LOGE("Editor::SetPreviewWindow no mainVideo.");
           return;
       }
       mainVideo->SetWidth(width);
       LOGD("Editor::SetPreviewWindow Set video width %{public}d.", width);
       mainVideo->SetHeight(height);
       LOGD("Editor::SetPreviewWindow Set video height %{public}d.", height);
       mainVideo->SetRotation(rotation);
       LOGD("Editor::SetPreviewWindow Set rotation is %{public}d.", rotation);
       mainVideo->SetOriginalDuration(static_cast<uint64_t>(originalDuration));
       LOGD("Editor::SetPreviewWindow Set original video duration %{public}ld.", originalDuration);
   }
   ```
6. 处理循环播放，定义previewDecoderCallback()函数，它有两个回调函数：
   * 第一个回调函数在每次解码器生成一个新的帧时调用，参数是pts（时间戳us）。
   * 第二个回调函数在解码器状态改变时调用，参数是CodecStatus。如果CodecStatus是END\_OF\_STREAM，表示视频流已经结束，此时会启动一个新的线程调用Editor::GetInstance().PlayFromStart()来重新开始播放。

   ```cpp
   static std::shared_ptr<LambdaAVDecoderCallback> previewDecoderCallback = std::make_shared<LambdaAVDecoderCallback>(
       [](uint64_t pts) { Editor::GetInstance().OnPlay(pts); },
       [](CodecStatus status) {
           if (status == CodecStatus::END_OF_STREAM) {
               std::thread t([]() { Editor::GetInstance().PlayFromStart(); });
               t.detach();
           }
       });
   ```

   处理播放器的播放事件，更新播放状态。pts是当前帧的时间戳，m\_firstFrame是一个布尔变量，用于标记是否是第一帧。

   * 如果m\_firstFrame为false，表示这是第一帧，会创建并复制视频格式信息，并将m\_firstFrame设置为true。
   * 检查当前帧的时间戳pts是否接近视频的结束位置。如果pts+60000大于或等于结束位置，表示视频即将结束，此时会启动一个新的线程来重新开始播放。

   ```cpp
   void Editor::OnPlay(int64_t pts)
   {
       if (!m_firstFrame) {
           LOGI("Editor::OnPlay get VideoFormat");
           if (m_inVideoFormat) {
               OH_AVFormat_Destroy(m_inVideoFormat);
           }
           m_inVideoFormat = OH_AVFormat_Create();
           if (m_inVideoFormat && m_previewEngine) {
               OH_AVFormat_Copy(m_inVideoFormat, m_previewEngine->GetVideoFormat());
           }

           m_firstFrame = true;
       }
       if (m_timeline && (pts + END_POSITION_THRESHOLD_US) >= m_timeline->GetVideoEndPos()) {
           LOGI("Editor::OnPlay Trigger onPlay play from start. pts is %{public}ld, end pos is %{public}ld.", pts,
                m_timeline->GetVideoEndPos());
           std::thread t([this]() { PlayFromStart(); });
           t.detach();
       }
   }
   ```

## 视频添加文字

### 场景描述

用户点击按钮，显示文本输入面板，输入文字后点击添加按钮。文字显示在视频预览区上方，系统将文字渲染为图片，然后作为贴纸叠加到视频，支持单指移动、双指缩放与旋转，与贴纸共用手势逻辑。可叠加多段文字，按添加顺序决定层级。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/p4IcmzRzSBW3xOlnT-QKyw/zh-cn_image_0000002680179682.gif "点击放大")

### 实现原理

文字在预览与导出两端采用不同渲染路径、同一数据模型的策略：预览由ArkUI直接绘制，导出前将文字栅格化为PNG图像，复用贴纸/Image资产管线进入渲染引擎合成。调用时序（预览添加）图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/C99wjF7DSNOasSSVxsJ5_A/zh-cn_image_0000002709859481.png "点击放大")

导出合成的调用时序如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/T9cLG8Q6Qjys0pYD4h3nrg/zh-cn_image_0000002680339560.png "点击放大")

### 开发步骤

1. 创建文字输入面板inputTextPanel，使用TextInput组件接收用户输入的文字，点击添加按钮将文字inputText添加至TextInputCanvas画布中。

   ```typescript
   @Builder
   inputTextPanel() {
     Column() {
       Row() {
         // Input box
         TextInput({ text: this.state.inputText, placeholder: $r('app.string.input_text') })
           .defaultFocus(true)
           .id('inputTextPanel')
           .onChange(value => this.state.inputText = value)
           .width('calc(70% - 16vp)')
           .height(40)
           .backgroundColor('#333333')
           .placeholderColor('#AAAAAA')
           .fontColor('#FFFFFF')
           .borderRadius(40)
           .padding({ left: 16 })
           .margin({ right: 10 })

         Button($r('app.string.add'))
           .width('calc(30% - 16vp)')
           .height(40)
           .backgroundColor('#333333')
           .fontColor('#FFFFFF')
           .borderRadius(40)
           .fontSize(16)
           .shadow({ radius: 4, color: '#00000033' })
           .hoverEffect(HoverEffect.Scale)
           .onClick(() => {
             this.state.isShowWordPanel = false;
             this.state.isFinish = true;
           })
       }
       .padding({
         left: 16,
         right: 16
       })
     }
     .visibility(this.state.isShowWordPanel ? Visibility.Visible : Visibility.None)
     .width('100%')
     .height(40)
     .offset({ y: 100 })
   }
   ```

   ```typescript
   TextInputCanvas({
     inputText: this.state.inputText,
     isFinish: this.state.isFinish,
     maxWidth: this.getUIContext().px2vp(this.state.videoRect.width),
     setImageURI: (filepath: string, wordUri: string) => {
       this.state.imgUri = filepath;
       this.state.wordUri = wordUri;
       this.state.isWordFile = true;
       this.state.wordFilePaths.push(filepath);
     }
   }).offset({ y: -100 })
     .visibility(this.state.isShowWordPanel ? Visibility.Visible : Visibility.None);
   ```
2. 使用Canvas组件绘制文字，设置文字的字体大小、样式、颜色等。

   ```typescript
   Canvas(this.context)
     .width(this.canvasWidth)
     .height(this.canvasHeight)
     .onReady(() => {
       this.updateCanvasAndDraw();
     })
   ```

   ```typescript
   updateCanvasAndDraw() {
     if (!this.context) {
       return;
     }
     const context = this.context;
     context.font = TEXT_FONT;
     context.fillStyle = '#FF5722'; // Text color
     context.textAlign = 'left';
     context.textBaseline = 'top';

     const maxCanvasWidth = this.getMaxCanvasWidth();
     const lines = this.wrapText(this.inputText, maxCanvasWidth);
     let maxLineWidth = 0;
     let lineHeight = 0;
     lines.forEach((line: string) => {
       const metrics = context.measureText(line);
       maxLineWidth = Math.max(maxLineWidth, metrics.width);
       lineHeight = Math.max(lineHeight, metrics.height);
     });
     this.canvasWidth = Math.max(CANVAS_PADDING * 2,
       Math.min(maxCanvasWidth, maxLineWidth + CANVAS_PADDING * 2));
     this.canvasHeight = Math.max(CANVAS_PADDING * 2,
       lines.length * lineHeight + CANVAS_PADDING * 2);

     context.clearRect(0, 0, this.canvasWidth, this.canvasHeight);
     lines.forEach((line: string, index: number) => {
       context.fillText(line, CANVAS_PADDING, CANVAS_PADDING + index * lineHeight);
     });
   }

   getMaxCanvasWidth(): number {
     const screenWidthPx = display.getDefaultDisplaySync().width;
     const screenWidthVp = this.getUIContext().px2vp(screenWidthPx);
     const limitWidth = this.maxWidth > 0 ? this.maxWidth : screenWidthVp;
     return Math.max(1, Math.min(limitWidth, screenWidthVp) - SCREEN_MARGIN);
   }

   wrapText(text: string, maxWidth: number): string[] {
     const lines: string[] = [];
     let currentLine = '';
     for (let i = 0; i < text.length; i++) {
       const char = text[i];
       if (char === '\n') {
         lines.push(currentLine);
         currentLine = '';
         continue;
       }
       const testLine = currentLine + char;
       if (this.context.measureText(testLine).width > maxWidth) {
         lines.push(currentLine);
         currentLine = char;
       } else {
         currentLine = testLine;
       }
     }
     if (currentLine) {
       lines.push(currentLine);
     }
     return lines;
   }
   ```
3. 使用Canvas的[toDataURL()](../harmonyos-references/js-components-canvas-canvas.md#todataurl6)将绘制的内容转换为图片。

   ```typescript
   // The canvas is converted to PixelMap and saved.
   async canvasToPixelMap() {
     if (!this.context) {
       return;
     }
     try {
       const dataUrl = this.context.toDataURL('image/png');
       // Parse base64 data
       const base64Data = dataUrl.split(',')[1]
       const buffer = await this.base64ToArrayBuffer(base64Data);
       let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
       // Obtain the system timestamp
       let timestamp = Date.now();
       const filePath = context.filesDir + '/canvas_image' + timestamp + '.png';
       // Write to file
       const file = await fileIo.open(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
       await fileIo.write(file.fd, buffer);
       await fileIo.close(file.fd);
       this.setImageURI(filePath, dataUrl);
     } catch (err) {
       Logger.error(`save fail, error code : ${err?.code}, message: ${err?.message}`);
     }
   }
   ```
4. 将文字图片作为贴纸添加到视频预览界面中。

   ```typescript
   // Draw the sticker
   @Monitor('state.imgUri')
   buildSticker() {
     // Cancel the previously selected status of the stickers
     this.state.stickers.forEach(sticker => sticker.isSelected = false);
     if (this.state.imgUri !== '') {
       let imageClass: TImageInfo = sdk.AddImage(this.state.imgUri, this.state.isWordFile);
       sdk.MoveImage(imageClass.imageId, this.getUIContext().vp2px(this.params.screenWidth as number) / 2,
         this.getUIContext().vp2px(this.params.screenHeight as number * 0.7) / 2);
       let newSticker = new Sticker(imageClass.imageId, this.state.isWordFile ? this.state.wordUri : this.state.imgUri,
         this.state.startOffsetX, this.state.startOffsetY, 1, 0, true, imageClass.width,
         imageClass.height, this.getUIContext().vp2px(this.params.screenWidth as number) / 2,
         this.getUIContext().vp2px(this.params.screenHeight as number * 0.7) / 2);
       this.state.stickers.push(newSticker);
       this.state.selectedStickerId = newSticker.id;
       this.state.imgUri = '';
       this.state.isWordFile = false;
     }
   }
   ```

## 视频添加图片

### 场景描述

用户点击按钮，从图库选择单张图片作为贴纸叠加到视频上。贴纸支持单指拖动、双指缩放与旋转，用户可以添加多个贴纸，按添加顺序叠放层级。贴纸位置限制在视频可视区域内，可以删除不需要的贴纸。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/8DMc2H_WQFWbh-GfSns1DA/zh-cn_image_0000002710019337.gif "点击放大")

### 实现原理

图片与文字共用ImageAsset数据结构与NAPI接口，预览由Image组件叠加，导出由IGLRenderEngine + ImageManager在GPU侧合成。预览添加与手势的调用时序如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/gKaG0imHRO2MpclggFsZew/zh-cn_image_0000002680179684.png "点击放大")

导出合成调用时序如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/R3ReyvlMQf69jV-1-ksB6A/zh-cn_image_0000002709859483.png "点击放大")

色彩空间要求：

* 渲染模块直接支持P3与SRGB色彩空间的图像。
* P3图片须保证OH\_NativeBuffer携带OH\_COLORSPACE\_DISPLAY\_P3\_SRGB，否则需预先转换。
* 图像输出会统一转换到与视频一致的色彩格式（BT.709 Limited Range）。

### 开发步骤

1. 点击按钮拉起图库，选择单张图片。

   ```typescript
   // Select the stickers
   selectImage() {
     if (this.state.isExporting) {
       return;
     }
     try {
       let options: photoAccessHelper.PhotoSelectOptions = {
         MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
         isEditSupported: false,
         maxSelectNumber: 1,
         isPhotoTakingSupported: false,
         isSearchSupported: true,
         isOriginalSupported: true,
       };
       let photoPicker = new photoAccessHelper.PhotoViewPicker();
       photoPicker.select(options).then((selectResult: photoAccessHelper.PhotoSelectResult) => {
         if (selectResult.photoUris.length > 0) {
           const selectedUri = selectResult.photoUris[0];
           // URI, Trigger sticker addition
           this.state.imgUri = selectedUri;
         }
       })
         .catch((err: BusinessError) => {
           Logger.error(TAG, `Image selection failed: ${err.code}, ${err.message}`);
         });
     } catch (error) {
       let err: BusinessError = error as BusinessError;
       Logger.error(TAG, `Image selector error: ${err.code}, ${err.message}`);
     }
   }
   ```
2. 获取到图片的uri、fd后，通过AddImage()传给后端。

   ```typescript
   // Draw the sticker
   @Monitor('state.imgUri')
   buildSticker() {
     // Cancel the previously selected status of the stickers
     this.state.stickers.forEach(sticker => sticker.isSelected = false);
     if (this.state.imgUri !== '') {
       let imageClass: TImageInfo = sdk.AddImage(this.state.imgUri, this.state.isWordFile);
       sdk.MoveImage(imageClass.imageId, this.getUIContext().vp2px(this.params.screenWidth as number) / 2,
         this.getUIContext().vp2px(this.params.screenHeight as number * 0.7) / 2);
       let newSticker = new Sticker(imageClass.imageId, this.state.isWordFile ? this.state.wordUri : this.state.imgUri,
         this.state.startOffsetX, this.state.startOffsetY, 1, 0, true, imageClass.width,
         imageClass.height, this.getUIContext().vp2px(this.params.screenWidth as number) / 2,
         this.getUIContext().vp2px(this.params.screenHeight as number * 0.7) / 2);
       this.state.stickers.push(newSticker);
       this.state.selectedStickerId = newSticker.id;
       this.state.imgUri = '';
       this.state.isWordFile = false;
     }
   }
   ```
3. C++后端添加图片，后端传回图片的长度、宽度和id。

   ```cpp
   std::tuple<std::string, int32_t, int32_t> Interface::AddImage(const std::string& path, bool isPath)
   {
       LOGI("Interface::AddImage. path=%{public}s.", path.c_str());

       if (path.empty()) {
           LOGE("Interface::AddImage. path is empty.");
           return {"", 0, 0};
       }

       std::string fullPath = path;
       if (!isPath) {
           fullPath = UriToPath(path);
           LOGI("Interface::AddImage. true path=%{public}s.", fullPath.c_str());
       }

       std::shared_ptr<Timeline> timeline = Editor::GetInstance().GetTimeline();
       if (timeline == nullptr) {
           LOGE("Interface::AddImage. timeline is nullptr.");
           return {"", 0, 0};
       }

       std::string imageId = timeline->AddImage(fullPath);
       if (imageId.empty()) {
           LOGE("Interface::AddImage. failed to add image.");
           return {"", 0, 0};
       }

       std::shared_ptr<ImageAsset> image = timeline->GetImage(imageId);
       if (image == nullptr) {
           LOGE("Interface::AddImage. image is nullptr.");
           return {"", 0, 0};
       }

       image->PrepareImageInfo();
       LOGI("Interface::AddImage. height=%{public}d, width = %{public}d.", image->GetHeight(), image->GetWidth());
       return {imageId, image->GetHeight(), image->GetWidth()};
   }
   ```
4. 初始化贴纸信息，调用StickerManage组件打印贴纸，缩放比例初始值为100%，层级按添加顺序递增。

   ```typescript
   // The main body of the sticker
   Image(this.sticker.uri)
     .objectFit(ImageFit.Contain)
     .width(this.getUIContext().px2vp(this.sticker.width))
     .height(this.getUIContext().px2vp(this.sticker.height))
     .position(
       { x: this.stickerX - this.getUIContext().px2vp(this.sticker.width / 2),
         y: this.stickerY - this.getUIContext().px2vp(this.sticker.height / 2) })
     .rotate({ angle: this.rotateEndAngle })
     .scale({ x: this.pinchValue, y: this.pinchValue, z: 1 })
     .stickerGestureGroup(this)
     .outline({
       width: 4,
       color: this.sticker.isSelected ? Color.White : 0x33EEEEEE,
       radius: 2
     })
     .onClick((event: ClickEvent) => {
       this.sticker.isSelected = true;
     })
     .zIndex(2)
     .visibility(this.remove ? Visibility.None : Visibility.Visible)
   ```
5. 贴纸的手势操作有三个功能，移动（单指）、缩放和旋转（双指），每个手势有三种状态，start、update和end。在end状态会更新贴纸的位置、缩放和旋转角度，并传输给后端。

   ```typescript
   @Extend(Image)
   function stickerGestureGroup(stickerManage: StickerManage) {
     .gesture(GestureGroup(GestureMode.Exclusive,
       TapGesture({ count: 1 })
         .onAction((event: GestureEvent) => {
           if (event.fingerList?.[0]) {
             stickerManage.currentLocalX = event.fingerList?.[0]?.localX;
             stickerManage.currentLocalY = event.fingerList?.[0]?.localY;
             stickerManage.sticker.isSelected = !stickerManage.sticker.isSelected;
           }
         }),
       GestureGroup(GestureMode.Parallel,
         PanGesture({ fingers: 1 })
           .onActionStart((event: GestureEvent) => {
             stickerManage.panStart(event);
           })
           .onActionUpdate((event: GestureEvent) => {
             stickerManage.panUpdate(event);
           })
           .onActionEnd((event: GestureEvent) => {
             stickerManage.panEnd();
           })
           .onActionCancel(() => {
             stickerManage.panEnd();
           }),

         PinchGesture({ fingers: 2 })
           .onActionStart((event: GestureEvent) => {
             stickerManage.pinchStart(event);
           })
           .onActionUpdate((event: GestureEvent) => {
             stickerManage.pinchUpdate(event);
           })
           .onActionEnd((event: GestureEvent) => {
             stickerManage.pinchEnd();
           })
           .onActionCancel(() => {
           }),
         RotationGesture({ fingers: 2 })
           .onActionStart((event: GestureEvent) => {
             stickerManage.rotateStart();
           })
           .onActionUpdate((event: GestureEvent) => {
             stickerManage.rotateUpdate(event);
           })
           .onActionEnd((event: GestureEvent) => {
             stickerManage.rotateEnd();
           })
           .onActionCancel(() => {
             stickerManage.rotateEnd();
           })
       )
     ))
   }
   ```
6. 使用deleteSticker()方法，通过贴纸的id删除指定的贴纸。

   ```typescript
   // Delete the specified sticker
   deleteSticker(id: string) {
     if (this.state.isExporting) {
       return;
     }
     this.state.stickers = this.state.stickers.filter(sticker => sticker.id !== id);
     if (this.state.selectedStickerId === id) {
       this.state.selectedStickerId = '';
       sdk.RemoveImage(id);
     }
   }
   ```

## 视频添加背景音乐

### 场景描述

在短视频编辑场景中，用户通常希望对视频的音频进行灵活控制：一方面可以选择保留或移除视频原声，另一方面可以叠加新的背景音乐。例如，为一段旅行视频配上轻快的配乐并关闭原声，或在保留环境音的同时叠加一段舒缓的背景音乐。用户可以从音频库选择音频文件，添加后会立即播放音乐。在导出时，音乐起点会与视频裁剪点对齐，音乐时长大于视频时长时进行裁剪，小于视频时长时循环填充。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/1za8XPhiRy-jTNX50Mn3hQ/zh-cn_image_0000002680339562.gif "点击放大")

### 实现原理

音频解码模块采用双层引擎架构：外层AVDecoderEngine持有两个内层解码引擎实例，分别负责视频原声和配乐的解封装解码。原声控制与配乐叠加的能力分别通过不同的接口与数据通路实现。

**原声控制**

预览与导出采用不同的原声控制策略：

* **预览**：原声静音时仅将音频渲染器的音量设为0，解码任务继续运行。恢复原声时音频进度与画面保持同步，响应即时。
* **导出**：移除原声时不启动音频解码线程，跳过原声解码，节省计算开销；同时在混音阶段标记原声数据为静音，确保不会误取。

**配乐叠加**

添加配乐时，创建独立的配乐解码引擎（仅解码音频轨，不涉及视频处理）。配乐的生命周期与预览/导出阶段紧密关联：

* **预览**：配乐解码引擎创建后立即启动解码。解码输出线程在收到EOS后自动Seek到起始位置并继续解码，实现循环播放。删除配乐时停止并销毁配乐解码引擎。
* **导出**：配乐解码引擎在导出准备阶段创建，通过设置播放时长限制配乐解码范围，当解码位置超过视频裁剪时长时停止送帧。

**数据通路**

预览与导出阶段，音频数据走不同的输出通路：

* **预览通路**：两路音频各自通过独立的音频渲染器播放，不经过混音，最终由系统进行混音和播放。
* **导出通路**：两路音频均通过回调送入格式转换与混音流程，处理后的PCM数据写入缓冲队列，供编码引擎消费。

预览时序（原声控制 + 配乐叠加）如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/AMRcQZbDQQyWJDsfAGr7cw/zh-cn_image_0000002710019339.png "点击放大")

导出时序（原声控制 + 配乐叠加）如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/uquDPSsVSGa3iCPDC51vLA/zh-cn_image_0000002680179686.png "点击放大")

### 开发步骤

1. 点击按钮拉起音频库，支持选择不同音频进行替换。获取到音频uri、fd，通过sdk.SetBgAudio(audioUri, audioInfo.fd)传给后端。

   ```typescript
   // Select audio
   async audioPicker() {
     if (this.state.isExporting) {
       return;
     }
     try {
       let audioPicker = new picker.AudioViewPicker();
       audioPicker.select((err: BusinessError, audioSelectResult: string[]) => {
         if (err) {
           Logger.error(TAG,
             `AudioViewPicker.select failed with err: , code is ${err?.code}, message is ${err?.message}`);
           return;
         }
         if (audioSelectResult && audioSelectResult.length > 0) {
           const audioUri = audioSelectResult[0];
           this.getAudioInfo(audioUri).then(audioInfo => {
             this.state.selectedAudio = audioInfo;
             sdk.SetBgAudio(audioUri, audioInfo.fd);
           });
         }
       });
     } catch (error) {
       let err: BusinessError = error as BusinessError;
       Logger.error(TAG, `AudioViewPicker.select failed with err: , code is ${error.code}, message is ${error.message}`);
     }
   }
   ```
2. 添加音频到预览解码引擎，C++后端设置背景音乐。

   ```cpp
   void Interface::SetBgAudio(const std::string& path, int32_t fd)
   {
       LOGI("Interface::SetBgAudio. path=%{public}s.", path.c_str());

       if (fd < 0) {
           LOGE("Interface::SetBgAudio. invalid fd.");
           return;
       }

       std::string fullPath = UriToPath(path);
       LOGD("Interface::SetBgAudio. true path is %{public}s.", fullPath.c_str());

       std::shared_ptr<Timeline> timeline = Editor::GetInstance().GetTimeline();
       if (timeline == nullptr) {
           LOGE("Interface::SetBgAudio. timeline is nullptr.");
           close(fd);
           return;
       }
       timeline->SetBgAudio(fullPath);

       std::shared_ptr<IAVDecoderEngine> previewEngine = Editor::GetInstance().GetPreviewEngine();
       if (previewEngine == nullptr) {
           LOGE("Interface::SetBgAudio. decoderEngine is nullptr.");
           close(fd);
           return;
       }
       previewEngine->AddAudio(fd);
       LOGI("Interface::SetBgAudio. bgAudio fd is %{public}d", fd);
       Editor::GetInstance().TrackFd(fd);
   }
   ```
3. 通过AVDecoderEngine::AddAudio(int fd)将音乐文件添加到解码引擎中。

   ```cpp
   int32_t AVDecoderEngine::AddAudio(int fd)
   {
       musicDecoderEngine_ = std::make_shared<AVDecoderEngineImpl>(fd, std::weak_ptr<AVDecodeCallback>{}, true);
       int32_t ret;
       if (avDataDuration_ != -1) {
           ret = musicDecoderEngine_->SetPlayDuration(avDataDuration_);
           CHECK_AND_RETURN_RET_LOG(ret == AV_OK, ret, "music decoder set duration failed");
       }
       ret = musicDecoderEngine_->Init();
       CHECK_AND_RETURN_RET_LOG(ret == AV_OK, ret, "music decoder init failed");
       if (isAvDecodingStarted_) {
           ret = musicDecoderEngine_->Start();
           CHECK_AND_RETURN_RET_LOG(ret == AV_OK, ret, "music decoder start failed");
           isMusicDecodingStarted_.store(true);
       }
       return AV_OK;
   }
   ```
4. 通过UnsetBgAudio()删除背景音乐。

   ```cpp
   void Interface::UnsetBgAudio()
   {
       LOGI("Interface::UnsetBgAudio.");

       std::shared_ptr<Timeline> timeline = Editor::GetInstance().GetTimeline();
       if (timeline == nullptr) {
           LOGE("Interface::UnsetBgAudio. timeline is nullptr.");
           return;
       }
       timeline->UnsetBgAudio();

       std::shared_ptr<IAVDecoderEngine> previewEngine = Editor::GetInstance().GetPreviewEngine();
       if (previewEngine == nullptr) {
           LOGE("Interface::UnsetBgAudio. decoderEngine is nullptr.");
           return;
       }
       previewEngine->DeleteAudio(0);
   }
   ```

## 音频格式转换和混音

### 场景描述

视频原声与背景音乐的源格式往往不一致，例如采样率可能是44100Hz或48000Hz等，声道数可能是单声道或立体声等，而编码器要求输入统一的PCM格式。因此导出时需要将两路音频分别重采样至固定采样率、转换位深与声道数，再按需混音为一条立体声音轨，最终编码为AAC写入MP4文件。

具体而言，格式转换包含以下三个环节：

* **重采样**：将不同采样率的音频统一至44100Hz，使用基于多相滤波器的重采样算法，保证音频质量。
* **位深转换**：重采样器工作在浮点域，需在重采样前后进行16-bit整数与浮点数之间的转换，并处理溢出防护。
* **声道变换**：将任意声道数的音频统一为立体声（2通道），单声道复制为双声道，多声道取前两通道。

混音则将格式统一后的原声与配乐PCM逐采样相加，饱和截断后输出。

### 实现原理

导出场景下，AVDecoderEngine作为音频处理的中枢，接收两路解码回调数据，依次执行声道变换、重采样与混音，最终通过缓冲队列送入编码引擎。处理流程为：解码输出 → 声道变换 → 重采样 → 混音 → 编码输入。

**声道变换**

声道变换在解码输出回调中完成，将任意声道数的PCM数据统一为立体声（2通道），确保后续重采样与混音的输入格式一致：

* 单声道：将每个采样复制到左右两个通道。
* 立体声：直接透传，无需变换。
* 多声道（>=2）：取前两个通道作为左右声道，丢弃其余通道。

**重采样**

重采样基于多相滤波器的单级重采样器实现，支持任意采样率到44100Hz的转换。流程如下：

1. 初始化：分别为视频原声和配乐创建重采样器实例，指定输入/输出采样率、通道数与质量参数。
2. 采样率更新：当解码器回调通知实际采样率时，动态更新重采样器参数并重新计算输入帧长。
3. 分块处理：每40ms的音频数据在44100Hz的采样率下，立体声通道的输出帧长为每秒3528个采样点（44100×40ms×2通道/1000）。

**位深转换**

重采样器工作在浮点域，而解码器输出与编码器输入均为16-bit整数，因此每次重采样前后需要做位深转换：

* 入重采样前：将16-bit整数映射到 [-1.0, 1.0] 浮点区间。
* 出重采样后：将浮点值映射回16-bit整数。映射前先将值裁剪到略小于[-1.0, 1.0]的安全区间，避免浮点精度导致溢出。

**混音**

混音在两路音频均完成重采样后执行，以编码器帧长（2048个采样点）为单位从重采样后的队列中取数据进行混合：

* 移除原声时，仅输出配乐PCM。
* 无配乐时，仅输出原声PCM。
* 原声与配乐并存时，逐采样相加，结果裁剪至INT16范围（饱和截断）。

混音后的PCM数据写入缓冲队列，由编码引擎消费并编码为AAC（44100Hz、立体声、96kbps）后封装入MP4。

**尾部排空**

当任一解码器完成时，等待两路均完成后执行排空：先将残留数据补零对齐后送入重采样器，再将重采样后不足一帧的剩余数据直接拼入混音队列，确保无数据丢失。

### 开发步骤

1. 音频数据准备，确保所有音频数据的格式一致。如果格式不一致，需要进行格式转换和重采样。

   ```cpp
   void OnAVDataReady(std::shared_ptr<PcmData> pcmData) override;
   void OnMusicDataReady(std::shared_ptr<PcmData> pcmData) override;
   void OnAVSamplingRateChanged(const int32_t samplingRate) override;
   void OnMusicSamplingRateChanged(const int32_t samplingRate) override;
   ```
2. 音频重采样处理，确保所有音频数据在时间上对齐。如果数据长度不一致，需要进行填充或裁剪。

   ```cpp
   int32_t ProResampler::Process(const float *inBuffer, uint32_t inFrameSize, float *outBuffer, uint32_t outFrameSize)
   {
       CHECK_AND_RETURN_RET_LOG(state_ != nullptr, RESAMPLER_ERR_ALLOC_FAILED,
           "ProResampler Process: resampler is %{public}s", ErrCodeToString(RESAMPLER_ERR_ALLOC_FAILED).c_str());

       uint32_t expectedOutFrameSize = outFrameSize;
       std::vector<float> tmpOutBuf(expectedOutFrameSize * channels_, 0.0f);
       int32_t ret =
           SingleStagePolyphaseResamplerProcess(state_, inBuffer, &inFrameSize, tmpOutBuf.data(), &outFrameSize);
       CHECK_AND_RETURN_RET_LOG(ret == RESAMPLER_ERR_SUCCESS, ret, "ProResampler process failed with error %{public}s",
           ErrCodeToString(ret).c_str());

       if (outFrameSize > expectedOutFrameSize) {
           return RESAMPLER_ERR_OVERFLOW;
       }

       uint32_t fillSize = expectedOutFrameSize - outFrameSize;
       size_t outBufferSize = expectedOutFrameSize * channels_ * sizeof(float);
       errno_t err = memset_s(outBuffer, outBufferSize, 0, fillSize * channels_ * sizeof(float));
       if (err != EOK) {
           return RESAMPLER_ERR_OVERFLOW;
       }

       ret = memcpy_s(outBuffer + fillSize * channels_, outBufferSize - fillSize * channels_ * sizeof(float),
                      tmpOutBuf.data(), outFrameSize * channels_ * sizeof(float));
       if (ret != EOK) {
           return RESAMPLER_ERR_OVERFLOW;
       }
       return RESAMPLER_ERR_SUCCESS;
   }
   ```
3. 通过AVDecoderEngine::MixAudioData()进行混音处理，当isAudioDataMute\_ 为true，表示移除原声后，仅输出配乐PCM；当musicDecoderEngine\_ 为空（nullptr），表示无配乐时，仅输出原声PCM；否则，原声与配乐并存时，逐采样相加，结果裁剪至INT16范围（饱和截断）。

   ```cpp
   void AVDecoderEngine::MixAudioData()
   {
       while ((isAudioDataMute_ || avDataQueueAfterResample_.size() >= CODEC_FRAME_LENGTH) &&
           (!musicDecoderEngine_ || musicDataQueueAfterResample_.size() >= CODEC_FRAME_LENGTH)) {
           // only use data from music data
           if (isAudioDataMute_) {
               mixDataQueue_.insert(mixDataQueue_.end(),
                   musicDataQueueAfterResample_.begin(), musicDataQueueAfterResample_.begin() + CODEC_FRAME_LENGTH);
               musicDataQueueAfterResample_.erase(musicDataQueueAfterResample_.begin(),
                   musicDataQueueAfterResample_.begin() + CODEC_FRAME_LENGTH);
               SendAudioData();
               continue;
           }
           // only use data from av data
           if (!musicDecoderEngine_) {
               mixDataQueue_.insert(mixDataQueue_.end(),
                   avDataQueueAfterResample_.begin(), avDataQueueAfterResample_.begin() + CODEC_FRAME_LENGTH);
               avDataQueueAfterResample_.erase(avDataQueueAfterResample_.begin(),
                   avDataQueueAfterResample_.begin() + CODEC_FRAME_LENGTH);
               SendAudioData();
               continue;
           }
           // mix data from av data and music data
           std::copy(avDataQueueAfterResample_.begin(), avDataQueueAfterResample_.begin() + CODEC_FRAME_LENGTH,
               avDataBuffer_.begin());
           avDataQueueAfterResample_.erase(avDataQueueAfterResample_.begin(),
               avDataQueueAfterResample_.begin() + CODEC_FRAME_LENGTH);
           std::copy(musicDataQueueAfterResample_.begin(), musicDataQueueAfterResample_.begin() + CODEC_FRAME_LENGTH,
               musicDataBuffer_.begin());
           musicDataQueueAfterResample_.erase(musicDataQueueAfterResample_.begin(),
               musicDataQueueAfterResample_.begin() + CODEC_FRAME_LENGTH);

           for (int32_t i = 0; i < CODEC_FRAME_LENGTH; ++i) {
               int32_t result = static_cast<int32_t>(avDataBuffer_[i]) + static_cast<int32_t>(musicDataBuffer_[i]);
               if (result > INT16_MAX) {
                   tempOutBuffer_[i] = INT16_MAX;
               } else if (result < INT16_MIN) {
                   tempOutBuffer_[i] = INT16_MIN;
               } else {
                   tempOutBuffer_[i] = static_cast<int16_t>(result);
               }
           }
           mixDataQueue_.insert(mixDataQueue_.end(), tempOutBuffer_.begin(), tempOutBuffer_.begin() + CODEC_FRAME_LENGTH);
           SendAudioData();
       }
   }
   ```
4. 通过SendAudioData()将混音后的PCM数据写入缓冲队列，由编码引擎消费并编码为AAC（44100Hz，立体声，96kbps）后封装入MP4。

   ```cpp
   void AVDecoderEngine::SendAudioData()
   {
       while (mixDataQueue_.size() >= CODEC_FRAME_LENGTH) {
           std::shared_ptr<PcmData> pcmData = std::make_shared<PcmData>();
           pcmData->data.resize(CODEC_FRAME_SIZE);
           uint8_t *dest = pcmData->data.data();
           for (int32_t i = 0; i < CODEC_FRAME_LENGTH; ++i) {
               auto data = mixDataQueue_.front();
               mixDataQueue_.pop_front();
               memcpy_s(dest + i * sizeof(int16_t), sizeof(int16_t), &data, sizeof(int16_t));
           }
           pcmData->dataSize = CODEC_FRAME_SIZE;
           if (pcmBufferQueue_) {
               pcmBufferQueue_->Enqueue(pcmData);
           }
       }
   }
   ```

## 视频分辨率调整

### 场景描述

视频分辨率调整功能用于在导出视频时控制输出分辨率。视频导入阶段输入分辨率最大支持4K，导出阶段自动调整输出分辨率，不提供UI手动选择，输出分辨率固定为720P。

### 实现原理

调整编码器参数和渲染输出Surface的几何尺寸，以确保解码、渲染和编码三端的分辨率一致。同时，需要实现码率自适应，根据分辨率和帧率动态调整码率。

| 帧率 | 720p 基准码率 |
| --- | --- |
| 30 fps | 1 Mbps |
| 60 fps | 1.4 Mbps |
| 其他 | 以30fps为基准，按分辨率与帧率比例缩放，限制在0.8×~1.5×范围内 |

**调整策略**

1. 读取源视频宽高，若旋转元数据为90°/270°则先交换宽高。
2. 若min(width, height) < 720：输出分辨率 = 输入分辨率。
3. 否则：短边固定为720，长边按宽高比计算，并对长边做偶数化处理（满足部分编码器对齐要求）。

**渲染侧联动：**

* 通过OH\_AVFormat\_SetIntValue设置OH\_MD\_KEY\_WIDTH、OH\_MD\_KEY\_HEIGHT。
* 对编码器输入窗口执行设置缓冲区宽度和高度的操作。
* 同步调用IGLRenderEngine::SetViewParams设置视口宽高，供叠加图像坐标计算使用。

### 开发步骤

1. 获取视频分辨率信息，若旋转元数据为90°/270° 则先交换宽高。

   ```cpp
   uint32_t inputWidth;
   uint32_t inputHeight;
   if (mainVideo->GetRotation() == ROTATION_90 || mainVideo->GetRotation() == ROTATION_270) {
       inputWidth = mainVideo->GetHeight();
       inputHeight = mainVideo->GetWidth();
   } else {
       inputWidth = mainVideo->GetWidth();
       inputHeight = mainVideo->GetHeight();
   }
   LOGI("Editor::PrepareExportEngine input video width is %{public}d, height is %{public}d", inputWidth, inputHeight);
   ```
2. 判断是否需要缩放。

   ```cpp
   if (std::min(inputHeight, inputWidth) < LIMIT_PIX) {
       outputWidth = inputWidth;
       outputHeight = inputHeight;
       LOGI("Editor::PrepareExportEngine use original resolution.");
   } else {
       std::tie(outputWidth, outputHeight) = ConvertToLimit(inputWidth, inputHeight, LIMIT_PIX);
       LOGI("Editor::PrepareExportEngine convert resolution to 720P.");
   }
   ```
3. 若min(width, height)<720：输出分辨率 = 输入分辨率。否则：短边固定为720，长边按宽高比计算，并对长边做偶数化处理（满足部分编码器对齐要求）。

   ```cpp
   std::pair<uint32_t, uint32_t> ConvertToLimit(uint32_t inputWidth, uint32_t inputHeight, uint32_t limitPix)
   {
       if (inputWidth == 0 || inputHeight == 0 || limitPix == 0) {
           LOGE("input invalid");
           return {0, 0};
       }
       
       float aspectRatio = static_cast<float>(inputWidth) / inputHeight;
       uint32_t shortSide = limitPix;
       uint32_t longSide;
       
       if (inputHeight < inputWidth) {
           longSide = static_cast<uint32_t>(std::round(aspectRatio * shortSide));
       } else {
           longSide = static_cast<uint32_t>(std::round(shortSide / aspectRatio));
       }
       
       const uint32_t evenAlignment = 2;
       if (longSide % evenAlignment != 0) {
           longSide += 1;
       }
           
       if (inputWidth > inputHeight) {
           return {longSide, shortSide};
       } else {
           return {shortSide, longSide};
       }
   }
   ```
4. 设置输出分辨率。

   ```cpp
   CHECK_AND_RETURN_RET_LOG(OH_AVFormat_SetIntValue(exportFormat, OH_MD_KEY_WIDTH, static_cast<int>(outputWidth)),
                            VEditorStatus::STATUS_ERROR, "ConfigExportFormat failed");
   CHECK_AND_RETURN_RET_LOG(OH_AVFormat_SetIntValue(exportFormat, OH_MD_KEY_HEIGHT, static_cast<int>(outputHeight)),
                            VEditorStatus::STATUS_ERROR, "ConfigExportFormat failed");
   ```
5. 根据分辨率计算码率。

   ```cpp
   VEditorStatus Editor::CalculateBitrate(int64_t& bitrate, uint32_t outputWidth, uint32_t outputHeight, double framerate)
   {
       const int pix720 = 921600;
       const int pix1080 = 2574720;
       const int pix1440 = 3684400;
       const int pix4k = 8294400;
       const int bit720 = 1400000;
       const int bit1080 = 2600000;
       const int bit1440 = 4900000;
       const int bit4k = 5600000;
       
       double scaleRate = 1.0;
       const double baseFR = 30.0;
       
       int pixOut = outputHeight * outputWidth;
       if (pixOut <= pix720) {
           scaleRate = static_cast<double>(pixOut) / pix720;
           scaleRate = scaleRate * (framerate / baseFR);
           bitrate = static_cast<int64_t>(bit720 * scaleRate);
       } else if (pixOut <= pix1080) {
           scaleRate = static_cast<double>(pixOut) / pix1080;
           scaleRate = scaleRate * (framerate / baseFR);
           bitrate = static_cast<int64_t>(bit1080 * scaleRate);
       } else if (pixOut <= pix1440) {
           scaleRate = static_cast<double>(pixOut) / pix1440;
           scaleRate = scaleRate * (framerate / baseFR);
           bitrate = static_cast<int64_t>(bit1440 * scaleRate);
       } else if (pixOut <= pix4k) {
           scaleRate = static_cast<double>(pixOut) / pix4k;
           scaleRate = scaleRate * (framerate / baseFR);
           bitrate = static_cast<int64_t>(bit4k * scaleRate);
       } else {
           LOGE("Resolution is bigger than 4k");
           return VEditorStatus::STATUS_ERROR;
       }
       LOGI("Editor out video FrameRate:%{public}f,BitRate:%{public}lld", framerate, static_cast<long long>(bitrate));
       return VEditorStatus::STATUS_OK;
   }
   ```

## 视频格式转码

### 场景描述

视频格式转码功能负责将原始视频转换为标准的输出格式。系统会将视频编码为H.265格式，音频编码为AAC格式，并封装为MP4格式，同时会设置合适的色彩空间、码率等参数。用户从图库导入MP4或标准流MKV视频进行编辑，若导入格式不支持，页面提示格式不支持。

### 实现原理

转码贯穿解封装、解码、HDR处理（可选）、渲染合成、编码、封装全链路，是导出管线的核心能力之一。

**输入支持：**

* 容器：MP4、MKV（标准流）。
* 视频编码：由解封装器读取轨信息，经OH\_VideoDecoder\_CreateByMime创建对应解码器。
* HDR素材：可选经VideoProcess做HDR → SDR转换后再进入渲染。

**色彩空间转换（Render 模块）：**

| 方向 | 说明 |
| --- | --- |
| 视频输入 | 支持BT.601 / BT.709的Full Range与Limited Range四种组合（SetInVideoFormat） |
| 视频输出 | 渲染引擎统一输出BT.709 Limited Range |

**旋转处理：**

* 源视频旋转元数据通过输入Surface的SET\_TRANSFORM在首帧前设置，渲染引擎处理该旋转信息。
* 封装时OH\_MD\_KEY\_ROTATION置为0，避免播放器二次旋转。

**输出规格：**

* 视频编码：HEVC。
* 音频编码：AAC。
* 容器：MP4。

### 开发步骤

1. 设置视频编码参数。

   ```cpp
   CHECK_AND_RETURN_RET_LOG(OH_AVFormat_Copy(exportFormat, m_inVideoFormat), VEditorStatus::STATUS_ERROR,
                            "ConfigExportFormat failed");
   CHECK_AND_RETURN_RET_LOG(OH_AVFormat_SetStringValue(exportFormat, OH_MD_KEY_CODEC_MIME, "video/hevc"),
                            VEditorStatus::STATUS_ERROR, "ConfigExportFormat failed");
   CHECK_AND_RETURN_RET_LOG(OH_AVFormat_SetIntValue(exportFormat, OH_MD_KEY_WIDTH, static_cast<int>(outputWidth)),
                            VEditorStatus::STATUS_ERROR, "ConfigExportFormat failed");
   CHECK_AND_RETURN_RET_LOG(OH_AVFormat_SetIntValue(exportFormat, OH_MD_KEY_HEIGHT, static_cast<int>(outputHeight)),
                            VEditorStatus::STATUS_ERROR, "ConfigExportFormat failed");
   CHECK_AND_RETURN_RET_LOG(OH_AVFormat_SetIntValue(exportFormat, OH_MD_KEY_ROTATION, 0), VEditorStatus::STATUS_ERROR,
                            "ConfigExportFormat failed");
   CHECK_AND_RETURN_RET_LOG(
       OH_AVFormat_SetIntValue(exportFormat, OH_MD_KEY_COLOR_PRIMARIES, OH_ColorPrimary::COLOR_PRIMARY_BT709),
       VEditorStatus::STATUS_ERROR, "ConfigExportFormat failed");
   CHECK_AND_RETURN_RET_LOG(OH_AVFormat_SetIntValue(exportFormat, OH_MD_KEY_MATRIX_COEFFICIENTS,
                                                    OH_MatrixCoefficient::MATRIX_COEFFICIENT_BT709),
                            VEditorStatus::STATUS_ERROR, "ConfigExportFormat failed");
   CHECK_AND_RETURN_RET_LOG(OH_AVFormat_SetIntValue(exportFormat, OH_MD_KEY_TRANSFER_CHARACTERISTICS,
                                                    OH_TransferCharacteristic::TRANSFER_CHARACTERISTIC_BT709),
                            VEditorStatus::STATUS_ERROR, "ConfigExportFormat failed");
   CHECK_AND_RETURN_RET_LOG(OH_AVFormat_SetIntValue(exportFormat, OH_MD_KEY_RANGE_FLAG, false),
                            VEditorStatus::STATUS_ERROR, "ConfigExportFormat failed");
   ```
2. 设置音频编码参数。

   ```cpp
   OH_AVFormat_SetIntValue(encodeParam.audioTrunkFormat, OH_MD_KEY_AUD_SAMPLE_RATE, DEFAULT_AUDIO_SAMPLE_RATE);
   OH_AVFormat_SetIntValue(encodeParam.audioTrunkFormat, OH_MD_KEY_AUDIO_SAMPLE_FORMAT,
                           OH_BitsPerSample::SAMPLE_S16LE);
   OH_AVFormat_SetIntValue(encodeParam.audioTrunkFormat, OH_MD_KEY_AUD_CHANNEL_COUNT, DEFAULT_AUDIO_CHANNEL_COUNT);
   OH_AVFormat_SetLongValue(encodeParam.audioTrunkFormat, OH_MD_KEY_CHANNEL_LAYOUT,
                            OH_AudioChannelLayout::CH_LAYOUT_STEREO);
   OH_AVFormat_SetStringValue(encodeParam.audioTrunkFormat, OH_MD_KEY_CODEC_MIME, OH_AVCODEC_MIMETYPE_AUDIO_AAC);
   OH_AVFormat_SetLongValue(encodeParam.audioTrunkFormat, OH_MD_KEY_BITRATE, DEFAULT_AUDIO_BITRATE);
   ```
3. 创建编码引擎。

   ```cpp
   // Create decoder for export
   std::shared_ptr<IAVDecoderEngine> decoderEngine = IAVDecoderEngine::Create(fdVideo, exportDecoderCallback);
   if (!decoderEngine) {
       LOGE("Editor::PrepareExportEngine Create export decoder engine failed.");
       return VEditorStatus::STATUS_ERROR;
   }

   int32_t status = decoderEngine->SetVideoOutputWindow(m_renderEngine->GetInSurface());
   if (status == AVError::AV_ERROR) {
       LOGE("Editor::PrepareExportEngine Set decoder output window failed.");
       return VEditorStatus::STATUS_ERROR;
   }

   decoderEngine->SetHighPerformance(true);
   status = decoderEngine->Init();
   if (status == AVError::AV_ERROR) {
       LOGE("Editor::PrepareExportEngine Init decoder failed.");
       return VEditorStatus::STATUS_ERROR;
   }
   ```
4. 启动编码引擎。

   ```cpp
   status = m_encoderEngine->Start();
   if (status == AVError::AV_ERROR) {
       LOGE("Editor::Export encoder engine start failed.");
       return VEditorStatus::STATUS_ERROR;
   }
   ```

## 视频裁剪

### 场景描述

视频裁剪功能允许用户通过拖动把手来裁剪视频的时长。拖动左把手设置视频从开头裁剪的长度，拖动右把手设置从尾部裁剪的长度。预览时视频从裁剪起点到裁剪终点循环播放，导出时视频从裁剪起点导出至裁剪终点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/MkDxRXBdTb6g9HmSiha6vg/zh-cn_image_0000002709859485.gif "点击放大")

### 实现原理

裁剪功能采用实时预览设计，前端通过手势拖拽事件计算视频裁剪的起始点和结束点，然后调用后端接口设置裁剪参数trimIn和trimOut。后端根据裁剪参数更新视频资产的起始位置startPos和结束位置endPos，预览时从startPos开始播放，播放至endPos时循环。

### 开发步骤

1. 定义视频裁剪界面的布局，包括前全局把手、中间边框和后全局把手。

   ```typescript
   Row() {
     // Front global handle
     Row() {
       Row()
         .margin({ left: HANDLER_WIDTH })
         .height(60)
         .width('100%')
         .backgroundColor(0xA0000000)
     }
     .layoutWeight(1)
     .height(60)

     Row() {
       Blank()
         .width(3)
         .height(24.8)
         .backgroundColor(Color.Black)
         .borderRadius(3)
     }
     .height(60)
     .width(HANDLER_WIDTH)
     .backgroundColor(Color.White)
     .borderRadius({ topLeft: 8, bottomLeft: 8 })
     .direction(Direction.Ltr)
     .handler(this, true)
   }.width(this.state.trimIn + HANDLER_WIDTH)
   .margin({ left: HANDLER_WIDTH })
   .direction(Direction.Ltr)
   ```
2. 在视频裁剪时，监听并处理手势拖拽相关的交互事件，包括拖拽开始dragStart()、拖拽中dragMoving()和拖拽结束dragEnd()。拖拽结束后，将裁剪参数curTrimInValue和curTrimOutValue通过SetTrim()传递给后端。

   ```typescript
   // Drag and drop start
   dragStart(isLeft: boolean, windowX: number) {
     sdk.Pause();
     this.state.isDragMoving = true;
     this.state.dragLeft = isLeft;
     this.state.dragTrimValue = isLeft ? this.state.trimIn : this.state.trimOut;
     this.state.dragStartPos = windowX;
     this.changeTrimType(isLeft);
     this.state.curDuration = this.state.newDuration - this.state.curTrimInValue - this.state.curTrimOutValue;
   }

   // Change position to time
   toTime(vp: number, roundValue = true): number {
     return roundValue ? Math.round(vp) : vp;
   }

   // Minimum trim length in pixels, ensuring the selected segment is at least 1 second
   minTrimPixelValue(): number {
     if (this.state.duration <= 0 || this.state.newDuration <= 0) {
       return MIN_TRIM_VALUE;
     }
     const minOneSecondPixels = (US_PER_SECOND / this.state.newDuration) * this.state.duration;
     return Math.max(MIN_TRIM_VALUE, minOneSecondPixels + 1);
   }

   // Dragging in progress
   dragMoving(windowX: number) {
     this.state.isSeekMoving = true;
     sdk.Pause();
     let deltaX = windowX - this.state.dragStartPos;
     let minTrimPixels = this.minTrimPixelValue();
     if (this.state.dragLeft) {
       let newTrimin = this.state.dragTrimValue + this.toTime(deltaX);
       let maxValue = Math.max(0, this.state.duration - this.state.trimOut - minTrimPixels);
       newTrimin = newTrimin < 0 ? 0 : (newTrimin > maxValue ? maxValue : newTrimin);
       this.state.trimIn = newTrimin;
       this.state.curTrimInValue = (newTrimin / this.state.duration) * this.state.newDuration;
       this.state.curDuration = this.state.newDuration - this.state.curTrimInValue - this.state.curTrimOutValue;
     } else {
       let newTrimOut = this.state.dragTrimValue - this.toTime(deltaX);
       let maxValue = Math.max(0, this.state.duration - this.state.trimIn - minTrimPixels);
       newTrimOut = newTrimOut < 0 ? 0 : (newTrimOut > maxValue ? maxValue : newTrimOut);
       this.state.trimOut = newTrimOut;
       this.state.curTrimOutValue = (newTrimOut / this.state.duration) * this.state.newDuration;
       this.state.curDuration = this.state.newDuration - this.state.curTrimInValue - this.state.curTrimOutValue;
     }
   }

   // Drag operation completed
   dragEnd() {
     this.state.isSeekMoving = false;
     this.state.isDragMoving = false;
     this.report(this.state.trimType, true);
     sdk.SetTrim(this.state.curTrimInValue, this.state.curTrimOutValue);
     sdk.PlayFromStart();
     this.state.curDuration = this.state.newDuration - this.state.curTrimInValue - this.state.curTrimOutValue;
   }
   ```
3. C++后端设置参数对视频进行裁剪。

   ```cpp
   void Interface::SetTrim(uint64_t trimIn, uint64_t trimOut)
   {
       LOGI("Interface::SetTrim. TrimIn %{public}lu, TrimOut %{public}lu", trimIn, trimOut);
       
       std::shared_ptr<Timeline> timeline = Editor::GetInstance().GetTimeline();
       if (!timeline) {
           LOGE("Interface::SetTrim. timeline is nullptr.");
           return;
       }

       std::shared_ptr<VideoAsset> mainVideo = timeline->GetMainVideo();
       if (!mainVideo) {
           LOGE("Interface::SetTrim. mainVideo is nullptr");
           return;
       }

       mainVideo->SetTrim(trimIn, trimOut);
   }
   ```

## 视频编辑保存导出

### 场景描述

视频编辑保存和导出功能是视频编辑器的最终输出环节。用户完成所有编辑操作后，点击"完成"按钮触发导出流程。界面显示半透明蒙层与进度条，暂停视频、原声与配乐播放，系统会将所有编辑效果（贴纸、文字、背景音乐、裁剪等）合成为一个新的视频文件，并保存到系统相册。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/ZDtQaZ2xQX6wG6Q77uGE_A/zh-cn_image_0000002680339564.gif "点击放大")

### 实现原理

导出是预览与导出双管线中计算量最大的阶段，涉及渲染引擎、编解码引擎的创建、串联与生命周期管理。引擎创建顺序（依赖关系）如下：

1. 渲染引擎：无前置依赖，可在用户点击导出前预创建IGLRenderEngine::Create()。
2. 解码引擎：需渲染引擎GetInSurface()作为视频输出窗口。
3. 编码引擎：初始化后提供GetVideoInputWindow()作为渲染引擎输出Surface。

因此PrepareExportEngine中的配置顺序为：Render（Create + SetViewParams + SetOutSurface + SetInVideoFormat）→ Encoder（Init + GetVideoInputWindow）→ Decoder（SetVideoOutputWindow + Init + AddAudio + AddImage）。调用时序（用户触发导出）如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/ekkQ_vMCQ367mfxWmO8K-Q/zh-cn_image_0000002710019341.png "点击放大")

调用时序（引擎预配置PrepareExportEngine）如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/9WOCM1TESX-qahEvnoB_hQ/zh-cn_image_0000002680179688.png "点击放大")

**启动顺序：** Render → Encoder → Decoder（与创建配置顺序不同，启动时先就绪下游再启动上游送帧）。

**进度与结束通知：**

* NAPI层Export注册napi\_threadsafe\_function，解码/编码回调中OnExport(pts)计算进度并回调UI（过滤 >100% 的非法值）。
* 导出结束由解码帧计数与编码帧计数比较判定；SendEOS须在独立线程调用，避免在编码器回调中直接调用导致死锁。
* 不裁剪直接导出时，借助解码器EOS回调辅助确定真实帧数，防止最后一帧PTS与duration不匹配导致卡死。

**文件保存：**

1. 导出文件写入应用沙箱路径：cacheDir/merge\_{timestamp}.mp4。
2. UI收到结束回调后，调用phAccessHelper的[showAssetsCreationDialog](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#showassetscreationdialog12)推入图库（需申请[ohos.permission.WRITE\_MEDIA](../harmonyos-guides/permissions-for-all-user.md#ohospermissionwrite_media)权限）。
3. 调用sdk.DestroyEditor()释放引擎资源。

### 开发步骤

1. 点击导出按钮触发导出流程，并显示导出进度exportProgress。

   ```typescript
   Button($r('app.string.completed'))
     .width(80)
     .height(40)
     .backgroundColor('#007DFF')
     .offset({
       x: -36,
       y: -5
     })
     .borderRadius(40)
     .type(ButtonType.Normal)
     .onClick(() => {
       this.state.exportProgress = 0;
       this.state.isExporting = true;
       this.outputFilePath = `${this.getUIContext()?.getHostContext()?.cacheDir}/merge_${new Date().getTime()}.mp4`;
       sdk.Export(this.outputFilePath,
         (progress: number) => {
           this.state.isExporting = true;
           this.state.exportProgress = progress;
           // Export will be completed when the progress reaches 100%.
         }, this.completeCallback()).catch((error: BusinessError) => {
         this.state.isExporting = false;
         Logger.error(TAG, `Export failed, code is ${error.code}, message is ${error.message}`);
       });
     })
     .enabled(!this.state.isExporting) // Exporting is currently disabled.
   ```

   导出过程中，显示半透明黑色背景，阻止下层交互，通过Progress组件展示当前导出进度。

   ```typescript
   @Builder
   ExportMaskLayer() {
     if (this.state.isExporting) {
       Stack() {
         // Translucent black background, preventing interaction at the lower level
         Column()
           .width('100%')
           .height('100%')
           .backgroundColor('rgba(0, 0, 0, 0.7)')
           .onClick(() => {
           }) // Prevent click-through

         // Progress display
         Column() {
           Text($r('app.string.export_video'))
             .fontSize(18)
             .fontColor(Color.White)
             .margin({ bottom: 20 })
           Progress({
             value: Math.min(this.state.exportProgress, 100),
             total: 100,
             type: ProgressType.Linear
           })
             .width(300)
             .height(8)
             .color('#007AFF')
           Text(`${this.state.exportProgress}%`)
             .fontSize(24)
             .fontWeight(FontWeight.Bold)
             .fontColor(Color.White)
             .margin({ top: 20 })
         }
       }
       .zIndex(10) // The highest level
       .width('100%')
       .height('100%')
     }
   }
   ```
2. C++后端准备导出引擎。

   ```cpp
   VEditorStatus Editor::PrepareExportEngine(std::string savePath)
   {
       LOGI("Editor::PrepareExportEngine");
       if (m_isExportReady) {
           LOGI("Editor::PrepareExportEngine already prepared");
           return VEditorStatus::STATUS_OK;
       }
       isDecoderStopped = false;
       decoderFrameCount = 0;
       encoderFrameCount = 0;
       if (!m_inVideoFormat) {
           LOGE("Editor::PrepareExportEngine export format is nullptr.");
           return VEditorStatus::STATUS_ERROR;
       }
       
       std::shared_ptr<VideoAsset> mainVideo = m_timeline->GetMainVideo();
       if (!mainVideo) {
           LOGE("Editor::PrepareExportEngine no main video.");
           return VEditorStatus::STATUS_ERROR;
       }
          
       if (CreateDecoder(mainVideo) != VEditorStatus::STATUS_OK) {
           return VEditorStatus::STATUS_ERROR;
       }
       
       uint32_t outputWidth;
       uint32_t outputHeight;
       CalculateOutputResolution(mainVideo, outputWidth, outputHeight);
           
       if (CreateEncoder(savePath, outputWidth, outputHeight) != VEditorStatus::STATUS_OK) {
           return VEditorStatus::STATUS_ERROR;
       }
    
       if (ConfigureRender() != VEditorStatus::STATUS_OK) {
           return VEditorStatus::STATUS_ERROR;
       }

       if (ConfigureAudioBufferQueue() != VEditorStatus::STATUS_OK) {
           return VEditorStatus::STATUS_ERROR;
       }
       
       m_isExportReady = true;
       return VEditorStatus::STATUS_OK;
   }
   ```
3. 调用Editor::Export()启动导出，包括启动渲染引擎、启动编码引擎、启动解码引擎等。

   ```cpp
   VEditorStatus Editor::Export()
   {
       LOGI("Editor::Export.");
       if (!m_isExportReady) {
           LOGE("Editor::Export export is not ready");
           return VEditorStatus::STATUS_ERROR;
       }
       
       LOGI("Editor::Export render engine start.");
       if (!m_renderEngine) {
           LOGE("Editor::Export m_renderEngine is nullptr");
           return VEditorStatus::STATUS_ERROR;
       }
       int32_t status = m_renderEngine->Start();
       if (status == AVError::AV_ERROR) {
           LOGE("Editor::Export render engine start failed.");
           return VEditorStatus::STATUS_ERROR;
       }
       
       LOGI("Editor::Export encoder engine start.");
       if (!m_encoderEngine) {
           LOGE("Editor::Export m_encoderEngine is nullptr");
           return VEditorStatus::STATUS_ERROR;
       }
       status = m_encoderEngine->Start();
       if (status == AVError::AV_ERROR) {
           LOGE("Editor::Export encoder engine start failed.");
           return VEditorStatus::STATUS_ERROR;
       }
       return StartExportEngine();
   }
   ```
4. 通知前端刷新导出的进度。同时，判断视频导出是否结束，并在满足条件时发送EOS（End of Stream）信号，停止导出引擎，并调用回调函数。

   ```cpp
   void Editor::OnExport(int64_t pts)
   {
       auto mainVideo = m_timeline->GetMainVideo();
       if (!mainVideo) {
           LOGE("Editor::OnExport main video is nullptr.");
           return;
       }
       auto duration = mainVideo->GetDuration();
       LOGD("Editor::OnExport pts is %{public}ld, duration is %{public}ld.", pts, duration);
       float progress = static_cast<float>(pts) / static_cast<float>(duration);
       if (m_exportSendProgress && progress > m_progress + 0.01f) {
           m_progress = progress;
           LOGD("Editor::OnExport progress is %{public}f.", progress);
           napi_call_threadsafe_function(m_exportSendProgress, &m_progress, napi_tsfn_nonblocking);
       }
       
       if (isDecoderStopped && encoderFrameCount + EOS_BUFFER_FRAMES >= decoderFrameCount) {
           LOGI("Editor::OnExport decoder stopped and encoder received enough frames %{public}zu. Encoder pts is "
                "%{public}ld", encoderFrameCount.load(), pts);
           NotifyExportFinished();
       }
   }
   ```
5. 通过showAssetsCreationDialog将视频文件保存到相册。

   ```typescript
   // Save video
   async saveFile() {
     try {
       let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
       let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
       let srcFileUris: string[] = [this.outputFilePath];
       let photoCreationConfigs: photoAccessHelper.PhotoCreationConfig[] = [
         {
           title: `VID_${new Date().getTime()}`,
           fileNameExtension: 'mp4',
           photoType: photoAccessHelper.PhotoType.VIDEO,
           subtype: photoAccessHelper.PhotoSubtype.DEFAULT,
         }
       ];
       let desFileUris: string[] = await phAccessHelper.showAssetsCreationDialog(srcFileUris, photoCreationConfigs);
       if (!desFileUris || desFileUris.length === 0) {
         Logger.error(TAG, 'saveFile failed: user cancelled or no URI returned');
         return;
       }
       let srcFile = fs.openSync(this.outputFilePath, fs.OpenMode.READ_ONLY);
       let desFile = fs.openSync(desFileUris[0], fs.OpenMode.WRITE_ONLY);
       fs.copyFileSync(srcFile.fd, desFile.fd);
       fs.closeSync(srcFile);
       fs.closeSync(desFile);
     } catch (error) {
       Logger.error(TAG, `saveFile failed, code is ${error.code}, message is ${error.message}`);
     } finally {
       try {
         fs.unlink(this.outputFilePath);
       } catch (error) {
         Logger.error(TAG, `unlink failed, code is ${error.code}, message is ${error.message}`);
       }
     }
   }
   ```
6. 当导出流程完成时，调用DestroyEditor()释放引擎资源，删除应用沙箱目录的文件路径和对应的文件。

   ```typescript
   // Exit the program directly after the export is completed.
   private completeCallback(): CallableFunction {
     clearInterval(this.state.exportInterval);
     return () => {
       this.state.isExporting = false;
       this.saveFile()
         .then(() => {
           sdk.DestroyEditor();
           //Delete the text and images in the application sandbox directory
           if (this.state.wordFilePaths.length > 0) {
             this.state.wordFilePaths.forEach(file => {
               try {
                 fs.unlink(file);
                 Logger.info('delete success!')
               } catch (err) {
                 Logger.error(TAG, `delete failed, code is ${err?.code}, message is ${err?.message}`);
               }
             })
           }
           this.getUIContext().getRouter().replaceUrl({ url: 'pages/Index' });
         });
     }
   }
   ```

## 示例代码

* [实现视频轻编辑功能](https://gitcode.com/HarmonyOS_Samples/VideoLightEditing)
