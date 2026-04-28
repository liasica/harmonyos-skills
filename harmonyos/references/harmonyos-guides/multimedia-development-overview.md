---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multimedia-development-overview
title: 媒体开发概览
breadcrumb: 指南 > 媒体 > 媒体开发概览
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:29+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:dd4e3a54e9dd97d92d5462fd142a59baa4f4b8f4991a77349bdaf6fc49622a85
---

HarmonyOS提供丰富的一站式媒体业务开放能力，开发者能够在系统上快速开发主流的媒体业务，满足常规高频使用场景，并提供优秀的性能表现。

## 媒体系统架构

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/qOqMdpQnQPiSVZKwnpl9ag/zh-cn_image_0000002552958526.png?HW-CC-KV=V1&HW-CC-Date=20260427T234528Z&HW-CC-Expire=86400&HW-CC-Sign=6445948438E70122487F84627B36990FB7A57B14DB5C8604D08F95CC503D65FB)

媒体系统架构提供用户视觉、听觉信息的处理能力，例如音视频信息的采集、编码存储、解码播放等。操作系统实现中，根据不同的媒体信息处理内容，将媒体划分为不同的模块，包括音频、视频、图片等。

媒体系统面向应用开发提供音视频应用、图库应用、相机应用的编程框架接口；面向设备开发提供对接不同硬件芯片的适配加速功能；中间以服务形式提供媒体核心功能和管理机制。

* 音频服务（Audio Kit）：提供场景化音频播放和录制接口，助力开发者快速构建音频高清采集及沉浸式播放能力。
* 音视频编解码服务（AVCodec Kit）：提供音视频编解码、媒体文件解析、封装及媒体数据输入等原子能力。
* 音视频播控服务（AVSession Kit）：提供系统级音视频管控服务，统一管理系统中所有音视频行为。
* 相机服务（Camera Kit）：提供场景化相机控制管理接口，实现预览图像显示、拍照图片保存及视频录制功能。
* 数字版权保护服务（DRM Kit）：提供DRM加密音视频解密，支持设备DRM证书管理、许可证管理及内容解密功能。
* 图片处理服务（Image Kit）：提供全面图片处理能力，帮助开发者实现图片的解码、编码、编辑、元数据处理和图片接收等功能。
* 媒体服务（Media Kit）：提供端到端播放原始媒体资源，音视频录制与屏幕录制，获取媒体资源元数据、缩略图，视频转码等功能。
* 媒体文件管理服务（Media Library Kit）：提供管理相册和媒体文件的能力，包括照片和视频。
* 铃声服务（Ringtone Kit）：提供铃声设置功能，为用户提供简单一致、安全高品质的铃声设置体验。
* 统一扫码服务（Scan Kit）：提供系统级的扫码服务。

## 媒体应用开发综述

### 相机预览

相机预览是启动相机后实时的图像显示，通常在拍照和录像前执行。

**指南**

* [预览(ArkTS)](camera-preview.md)
* [双路预览(ArkTS)](camera-dual-channel-preview.md)
* [动态调整预览帧率(ArkTS)](camera-framerate.md)
* [适配相机旋转角度(ArkTS)](camera-rotation-angle-adaptation.md)
* [预览(C/C++)](native-camera-preview.md)
* [预览流二次处理(C/C++)](native-camera-preview-imagereceiver.md)
* [动态调整预览帧率(C/C++)](camera-setframerate-native.md)
* [适配相机旋转角度(C/C++)](camera-rotation-angle-adaptation-native.md)

**API参考**

* ArkTS API：[camera](../harmonyos-references/js-apis-camera.md)
* C API：[OH\_Camera](../harmonyos-references/capi-oh-camera.md)

**最佳实践**

* [相机预览花屏解决方案](../best-practices/bpta-deal-stride-solution.md)

### 相机拍照

拍照是相机的最重要功能之一，Camera Kit提供多种拍照方式，开发者可以直接拉起系统相机拍照、采用系统预配置简化应用开发流程，或是根据开放接口开发一个专业的相机应用。

**指南**

* [通过系统相机拍照和录像(CameraPicker)](camera-picker.md)
* [拍照(ArkTS)](camera-shooting.md)
* [分段式拍照(ArkTS)](camera-deferred-capture.md)
* [动态照片拍摄(ArkTS)](camera-moving-photo.md)
* [使用相机预配置(ArkTS)](camera-preconfig.md)
* [HDR Vivid相机拍照(ArkTS)](camera-hdr-shooting.md)
* [适配相机旋转角度(ArkTS)](camera-rotation-angle-adaptation.md)
* [拍照(C/C++)](native-camera-shooting.md)
* [分段式拍照(C/C++)](native-camera-deferred-capture.md)
* [使用相机预配置(C/C++)](camera-preconfig-native.md)
* [适配相机旋转角度(C/C++)](camera-rotation-angle-adaptation-native.md)

**API参考**

* ArkTS API：[camera](../harmonyos-references/js-apis-camera.md)
* ArkTS组件：[cameraPicker](../harmonyos-references/js-apis-camerapicker.md)
* C API：[OH\_Camera](../harmonyos-references/capi-oh-camera.md)

**最佳实践**

* [相机分段式拍照性能优化实践](../best-practices/bpta-camera-shot2see.md)

**示例代码**

* [基于系统相机实现拍照功能](https://gitcode.com/HarmonyOS_Samples/camera-picker)
* [实现相机数据采集保存功能](https://gitcode.com/HarmonyOS_Samples/camera)
* [实现相机数据采集保存功能（C++）](https://gitcode.com/HarmonyOS_Samples/camera-data-collection)

### 视频播放

AVPlayer提供功能齐全的一体化播放能力，支持多种音视频格式和流媒体协议。应用使用AVPlayer不仅可以实现基础的播放控制，还可以通过外挂字幕、画中画、自定义UI控件、内容版权保护等功能，为用户提供优良的影音体验。

**指南**

* [AVPlayer简介（含支持的格式与协议）](media-kit-intro.md#avplayer)
* [使用AVPlayer播放视频(ArkTS)](video-playback.md)
* [使用AVPlayer设置播放URL(ArkTS)](playback-url-setting-method.md)
* [使用AVPlayer播放流媒体(ArkTS)](streaming-media-playback-development-guide.md)
* [使用AVPlayer添加视频外挂字幕(ArkTS)](video-subtitle.md)
* [使用AVPlayer播放视频(C/C++)](using-ndk-avplayer-for-video-playback.md)
* [HDR Vivid视频播放](hdr-vivid-video-player.md)
* [接入Background Tasks Kit长时任务实现后台播放](continuous-task.md)
* [应用接入AVSession](avsession-access-scene.md)
* [应用接入播控自检](playback-control-access-selfcheck.md)
* [基于AVPlayer播放DRM节目(ArkTS)](drm-avplayer-arkts-integration.md)
* [视频转码(ArkTS)](media-transcoder-arkts.md)
* [在应用程序中使用画中画功能](window-pipwindow.md)

**API参考**

* ArkTS API：[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)
* C API：[AVPlayer](../harmonyos-references/capi-avplayer.md)

**最佳实践**

* [在线视频播放卡顿优化实践](../best-practices/bpta-online-video-playback-lags-practice.md)
* [音画同步最佳实践](../best-practices/bpta-audio-video-synchronization.md)
* [基于系统能力获取视频缩略图](../best-practices/bpta-video-thumbnail.md)

**示例代码**

* [实现视频播放功能](https://gitcode.com/HarmonyOS_Samples/video-play)
* [实现视频边缓存边播放功能](https://gitcode.com/HarmonyOS_Samples/video-cache)
* [实现视频流畅播放且支持后台与焦点打断功能](https://gitcode.com/HarmonyOS_Samples/video-player)
* [基于系统能力获取视频缩略图](https://gitcode.com/HarmonyOS_Samples/VideoThumbnail)
* [实现流畅切换短视频](https://gitcode.com/HarmonyOS_Samples/SmoothSwitchShortVideos)
* [实现音画同步播放效果](https://gitcode.com/HarmonyOS_Samples/AudioToVideoSync)

**设计体验**

* [播控中心](../design-guides/broadcasting-control-0000001957017133.md)
* [画中画](../design-guides/pip-0000001927422624.md)

### 视频录制

AVRecorder提供音视频录制的能力，AVScreenCapture提供屏幕录制的能力，支持多源输入，可灵活配置录制参数，帮助开发者轻松实现音视频录制功能。

**指南**

* [AVRecorder简介（含支持的格式）](media-kit-intro.md#avrecorder)
* [使用AVRecorder录制视频(ArkTS)](video-recording.md)
* [AVScreenCapture简介（含支持的格式）](media-kit-intro.md#avscreencapture)
* [使用AVScreenCaptureRecorder录屏写文件(ArkTS)](using-avscreencapture-arkts.md)
* [使用AVScreenCapture录屏取码流(C/C++)](using-avscreencapture-for-buffer.md)
* [使用AVScreenCapture录屏写文件(C/C++)](using-avscreencapture-for-file.md)
* [HDR Vivid相机录像](camera-hdr-recording.md)
* [HDR Vivid视频录制](hdr-vivid-video-recorder.md)
* [使用Camera Kit录像(ArkTS)](camera-recording.md)

**API参考**

* ArkTS API：[AVRecorder](../harmonyos-references/arkts-apis-media-avrecorder.md)
* C API：[AVRecorder](../harmonyos-references/capi-avrecorder.md)
* ArkTS API：[AVScreenCaptureRecorder](../harmonyos-references/arkts-apis-media-avscreencapturerecorder.md)
* C API：[AVScreenCapture](../harmonyos-references/capi-avscreencapture.md)

**示例代码**

* [基于CameraKit通过AVRecorder录像](https://gitcode.com/HarmonyOS_Samples/camera-kit-avrecorder)

### 视频投播

使用媒体播控，可以简单高效地将音视频投放到其他HarmonyOS设备上播放，如在手机上播放的音视频，可以投到2in1设备上继续播放。

**指南**

* [使用通话设备切换组件](using-switch-call-devices.md)
* [投播组件开发指导](distributed-playback-guide.md)
* [扩展屏投播开发指导](avsession-extended-screen.md)

**API参考**

* ArkTS API：[avsession](../harmonyos-references/js-apis-avsession.md)
* ArkTS组件：[AVCastPicker](../harmonyos-references/ohos-multimedia-avcastpicker.md)

**示例代码**

* [实现视频投播功能](https://gitcode.com/HarmonyOS_Samples/VideoCast)

### 音频播放

开发者可以使用AVPlayer播放媒体资源，如mp4/mp3/mkv/mpeg-ts等，也可以使用AudioRenderer播放PCM音频数据。

**AVPlayer指南**

* [使用AVPlayer播放音频(ArkTS)](using-avplayer-for-playback.md)
* [使用AVPlayer设置播放URL(ArkTS)](playback-url-setting-method.md)
* [使用AVPlayer播放流媒体(ArkTS)](streaming-media-playback-development-guide.md)
* [使用SoundPool播放短音频(ArkTS)](using-soundpool-for-playback.md)
* [使用AVPlayer播放音频(C/C++)](using-ndk-avplayer-for-playback.md)

**AVPlayer API参考**

* ArkTS API：[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)
* C API：[AVPlayer](../harmonyos-references/capi-avplayer.md)

**AudioRenderer指南**

* [使用AudioRenderer开发音频播放功能](using-audiorenderer-for-playback.md)
* [响应音频流输出设备变更](audio-output-device-change.md)
* [使用OHAudio开发音频播放功能(C/C++)](using-ohaudio-for-playback.md)
* [使用AudioHaptic开发音振协同播放功能](using-audiohaptic-for-playback.md)

**AudioRenderer API参考**

* ArkTS API：[AudioRenderer](../harmonyos-references/arkts-apis-audio-audiorenderer.md)
* ArkTS API：[audioHaptic](../harmonyos-references/js-apis-audiohaptic.md)
* C API：[OHAudio](../harmonyos-references/capi-ohaudio.md)

**通用指南**

* [接入Background Tasks Kit长时任务实现后台播放](continuous-task.md)
* [应用接入AVSession](avsession-access-scene.md)
* [应用接入播控自检](playback-control-access-selfcheck.md)
* [使用合适的音频流类型](using-right-streamusage-and-sourcetype.md)
* [音频焦点和音频会话介绍](audio-playback-concurrency.md)
* [使用AudioSession管理应用音频焦点(ArkTS)](audio-session-management.md)
* [使用AudioSession管理应用音频焦点(C/C++)](using-ohaudio-for-session.md)

**最佳实践**

* [音频焦点管理解决方案](../best-practices/bpta-audio-focus-management.md)
* [音乐服务卡片](../best-practices/bpta-music-card.md)

**示例代码**

* [实现音频应用作为媒体会话提供方接入媒体会话](https://gitcode.com/HarmonyOS_Samples/media-provider)
* [实现音频低时延录制与播放](https://gitcode.com/HarmonyOS_Samples/audio-native)
* [基于AudioRenderer的音频播控和多场景交互](https://gitcode.com/HarmonyOS_Samples/audio-interaction)

**设计体验**

* [播控中心](../design-guides/broadcasting-control-0000001957017133.md)

### 音频采集

AudioCapture提供了音频采集能力，为开发者提供PCM原始数据。

**指南**

* [使用AudioCapturer开发音频录制功能](using-audiocapturer-for-recording.md)
* [使用OHAudio开发音频录制功能(C/C++)](using-ohaudio-for-recording.md)

**API参考**

* ArkTS API：[AudioCapturer](../harmonyos-references/arkts-apis-audio-audiocapturer.md)
* C API：[OHAudio](../harmonyos-references/capi-ohaudio.md)

**示例代码**

* [实现音频低时延录制与播放](https://gitcode.com/HarmonyOS_Samples/audio-native)
* [基于AudioRenderer的音频播控和多场景交互](https://gitcode.com/HarmonyOS_Samples/audio-interaction)

### 音频录制

AVRecorder提供音频录制的能力，帮助开发者录制纯音频文件。

**指南**

* [使用AVRecorder录制音频(ArkTS)](using-avrecorder-for-recording.md)

**API参考**

* ArkTS API：[AVRecorder](../harmonyos-references/arkts-apis-media-avrecorder.md)
* C API：[AVRecorder](../harmonyos-references/capi-avrecorder.md)

### 媒体资源的选择和保存

**指南**

* [使用Picker选择媒体库资源](photoaccesshelper-photoviewpicker.md)
* [使用PhotoPicker组件访问图片/视频](component-guidelines-photoviewpicker.md)
* [保存媒体库资源](photoaccesshelper-savebutton.md)

**API参考**

* ArkTS API：[photoAccessHelper](../harmonyos-references/js-apis-photoaccesshelper.md)
* ArkTS组件：[AlbumPickerComponent](../harmonyos-references/ohos-file-albumpickercomponent.md)
* ArkTS组件：[PhotoPickerComponent](../harmonyos-references/ohos-file-photopickercomponent.md)
* ArkTS组件：[RecentPhotoComponent](../harmonyos-references/ohos-file-recentphotocomponent.md)

**最佳实践**

* [图片获取与保存实践](../best-practices/bpta-image_get_and_save.md)

**示例代码**

* [实现图片获取与保存功能](https://gitcode.com/HarmonyOS_Samples/ImageGetAndSave)
* [基于PhotoPicker实现图片推荐功能](https://gitcode.com/HarmonyOS_Samples/SmartPhotoPicker)

### 隐私安全

在进行媒体应用开发过程中，应用需要访问个人数据（如用户照片、视频、音频文件等）和设备数据（如相机、麦克风等）。这些资源受系统保护，使用时需通过Picker或申请相关权限。

**访问个人数据**

* [使用Picker选择媒体库资源](photoaccesshelper-photoviewpicker.md)
* [保存资源到媒体库](photoaccesshelper-savebutton.md)
* [选择音频类文件](select-user-file.md#选择音频类文件)
* [保存音频类文件](save-user-file.md#保存音频类文件)

应用需要克隆、备份或同步图片/视频类文件时，可[申请受限权限读写媒体库](photoaccesshelper-preparation.md#申请相册管理模块功能相关权限)。

**访问设备数据**

麦克风权限ohos.permission.MICROPHONE、相机权限ohos.permission.CAMERA、媒体地理位置信息权限ohos.permission.MEDIA\_LOCATION，均为用户授权权限，申请方式见[向用户申请授权](request-user-authorization.md)。

## 更多资源

**Audio Kit**

| 分类 | 资源链接 |
| --- | --- |
| 音频焦点 | - 开发指南：[使用合适的音频流类型](using-right-streamusage-and-sourcetype.md)  - 开发指南：[音频焦点和音频会话](audio-playback-concurrency.md)  - ArkTS API参考：[AudioSession](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md)  - ArkTS API参考：[StreamUsage](../harmonyos-references/arkts-apis-audio-e.md#streamusage) |
| 音频通话 | - 开发指南：[使用AudioRenderer播放对端的通话声音](audio-call-development.md#使用audiorenderer播放对端的通话声音)  - 开发指南：[使用AudioCapturer录制本端的通话声音](audio-call-development.md#使用audiocapturer录制本端的通话声音) |
| 更多 | [Audio Kit开发指南](audio-kit.md)  [Audio Kit API参考](../harmonyos-references/audio-api.md) |

**AVCodec Kit**

| 分类 | 资源链接 |
| --- | --- |
| 音频编解码 | - 开发指南：[音频编码](audio-encoding.md)  - 开发指南：[音频解码](audio-decoding.md)  - 示例代码：[AudioEncoder（音频编码）](https://gitcode.com/HarmonyOS_Samples/AVCodecVideo/blob/master/entry/src/main/cpp/capbilities/AudioEncoder.cpp)  - 示例代码：[AudioDecoder（音频解码）](https://gitcode.com/HarmonyOS_Samples/AVCodecVideo/blob/master/entry/src/main/cpp/capbilities/AudioDecoder.cpp)  - C API参考：[AudioCodec（音频编解码）](../harmonyos-references/capi-native-avcodec-audiocodec-h.md) |
| 视频编解码 | - 开发指南：[视频编码](video-encoding.md)  - 示例代码：[VideoEncoder（视频编码）](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/BasicFeature/Media/AVCodec/entry/src/main/cpp/capbilities/video_encoder.cpp)  - C API参考：[VideoEncoder（视频编码）](../harmonyos-references/capi-native-avcodec-videoencoder-h.md)  - 开发指南：[视频解码](video-decoding.md)  - 示例代码：[VideoDecoder（视频解码）](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/BasicFeature/Media/AVCodec/entry/src/main/cpp/capbilities/video_decoder.cpp)  - C API参考：[VideoDecoder（视频解码）](../harmonyos-references/capi-native-avcodec-videodecoder-h.md) |
| 更多 | [AVCodec Kit开发指南](avcodec-kit.md)  [AVCodec Kit API参考](../harmonyos-references/avcodec-api.md) |

**AVSession Kit**

| 分类 | 资源链接 |
| --- | --- |
| 本地媒体会话 | - ArkTS API参考：[媒体会话管理](../harmonyos-references/js-apis-avsession.md)  - 开发指南：[应用接入AVSession场景介绍](avsession-access-scene.md)  - 示例代码：[基于AVPlayer实现播放接入](https://gitcode.com/HarmonyOS_Samples/media-provider)  - 示例代码：[基于AudioRenderer实现播放接入](https://gitcode.com/HarmonyOS_Samples/audio-interaction) |
| 更多 | [AVSession Kit开发指南](avsession-kit.md)  [AVSession Kit API参考](../harmonyos-references/avsession-api.md) |

**Camera Kit**

| 分类 | 资源链接 |
| --- | --- |
| 视频录制 | - ArkTS API参考：[Camera API(相机管理)](../harmonyos-references/js-apis-camera.md)  - 开发指南：[录像(ArkTS)](camera-recording.md)  - 开发指南：[录像(C/C++)](native-camera-recording.md)  - 示例实现：[录像实践(ArkTS)](camera-recording-case.md) |
| 安全相机 | - ArkTS API参考：[SecureSession](../harmonyos-references/arkts-apis-camera-securesession.md)  - 开发指南：[安全相机(ArkTS)](camera-secure-photo.md) |
| 更多 | [Camera Kit开发指南](camera-kit.md)  [Camera Kit API参考](../harmonyos-references/camera-api.md) |

**DRM Kit**

| 分类 | 资源链接 |
| --- | --- |
| AVPlayer播放DRM节目 | - ArkTS API参考：[DRM](../harmonyos-references/js-apis-drm.md)  - 开发指南：[数字版权保护(ArkTS)](drm-arkts-dev-guide.md)  - 示例实现：[基于AVPlayer播放DRM节目(ArkTS)](drm-avplayer-arkts-integration.md) |
| AVCodec播放DRM节目 | - C API参考：[数字版权保护API(C/C++)](../harmonyos-references/capi-drm.md)  - 开发指南：[数字版权保护(C/C++)](drm-c-dev-guide.md)  - 示例实现：[基于AVCodec播放DRM节目(C/C++)](drm-avcodec-integration.md) |
| 更多 | [DRM Kit开发指南](drm-kit.md)  [DRM Kit API参考](../harmonyos-references/drm-api.md) |

**Image Kit**

| 分类 | 资源链接 |
| --- | --- |
| 图片解码 | 支持HEIF、JPEG、PNG、WebP、GIF、BMP、SVG、ICO、DNG格式图片的解码。  - ArkTS指南：[使用ImageSource完成图片解码](image-decoding.md)  - C/C++指南：[使用Image\_NativeModule完成图片解码](image-source-c.md)  支持自定义申请内存类型，优化解码效率。  - ArkTS指南：[申请图片解码内存(ArkTS)](image-allocator-type.md)  - C/C++指南：[申请图片解码内存(C/C++)](image-allocator-type-c.md) |
| 图片编码 | 支持编码为HEIF、JPEG、PNG、WebP、GIF格式图片。  - ArkTS指南：[使用ImagePacker完成图片编码](image-encoding.md)  - C/C++指南：[使用Image\_NativeModule完成图片编码](image-packer-c.md) |
| 图片接收 | 支持作为消费者接收和处理图片。  - ArkTS指南：[使用ImageReceiver完成图片接收](image-receiver.md)  - C/C++指南：[使用Image\_NativeModule完成图片接收](image-receiver-c.md) |
| 图片编辑和处理 | 支持裁剪、缩放、偏移、旋转、翻转、设置透明度等图像变换，以及对图片部分区域做像素数据写入的位图操作。  - ArkTS指南：[使用PixelMap完成图像变换](image-transformation.md)  - ArkTS指南：[使用PixelMap完成位图操作](image-pixelmap-operation.md)  - C/C++指南：[使用Image\_NativeModule完成位图操作](pixelmap-c.md)  支持读取和编辑图片的EXIF信息。  - ArkTS指南：[编辑图片EXIF信息](image-tool.md)  - C/C++指南：[使用Image\_NativeModule编辑图片EXIF信息](image-tool-c.md)  支持为图片添加个性化的滤镜效果。  - C/C++指南：[使用ImageEffect编辑图片](image-effect-guidelines.md)  支持对图片做清晰度增强、色彩空间转换、HDR效果转换。  - C/C++指南：[图片缩放](image-scaling.md)  - C/C++指南：[图片色彩空间转换](image-csc.md)  - C/C++指南：[图片动态元数据生成](image-dynamic-metadata-generation.md)  - C/C++指南：[单层HDR图片转换双层](hdr-single-to-dual.md)  - C/C++指南：[双层HDR图片转换单层](hdr-dual-to-single.md) |
| 更多 | [Image Kit开发指南](image-kit.md)  [Image Kit API参考](../harmonyos-references/image-api.md) |

**Media Kit**

| 分类 | 资源链接 |
| --- | --- |
| 视频转码 | - ArkTS API参考：[AVTranscoder](../harmonyos-references/arkts-apis-media-avtranscoder.md)  - 开发指南：[使用AVTranscoder实现视频转码(ArkTS)](using-avtranscoder-for-transcodering.md)  - 开发指南：[创建异步线程执行AVTranscoder视频转码(ArkTS)](avtranscoder-practice.md) |
| 元数据 | - ArkTS API参考：[AVMetadataExtractor](../harmonyos-references/arkts-apis-media-avmetadataextractor.md)  - C API参考：[AVMetadataExtractor](../harmonyos-references/capi-avmetadataextractor.md)  - 开发指南：[使用AVMetadataExtractor提取音视频元数据信息(ArkTS)](avmetadataextractor.md)  - 开发指南：[使用AVMetadataExtractor获取元数据(C/C++)](using-ndk-avmetadataextractor-for-media.md) |
| 缩略图 | - ArkTS API参考：[AVImageGenerator](../harmonyos-references/arkts-apis-media-avimagegenerator.md)  - C API参考：[AVImageGenerator](../harmonyos-references/capi-avimagegenerator.md)  - 开发指南：[使用AVImageGenerator提取视频指定时间图像(ArkTS)](avimagegenerator.md)  - 开发指南：[使用AVImageGenerator获取视频帧(C/C++)](using-ndk-avimagegenerator-for-video.md)  - 最佳实践：[基于系统能力获取视频缩略图](../best-practices/bpta-video-thumbnail.md) |
| 更多 | [Media Kit开发指南](media-kit.md)  [Media Kit API参考](../harmonyos-references/media-api.md) |

**Media Library Kit**

| 分类 | 资源链接 |
| --- | --- |
| 管理动态照片 | - 指南：[访问和管理动态照片资源](photoaccesshelper-movingphoto.md)  - 指南：[使用MovingPhotoView播放动态照片](movingphotoview-guidelines.md) |
| 更多 | [Media Library Kit开发指南](medialibrary-kit.md)  [Media Library Kit API参考](../harmonyos-references/media-library-api.md) |

**Ringtone Kit**

| 分类 | 资源链接 |
| --- | --- |
| 铃声设置服务 | - ArkTS API参考：[铃声服务](../harmonyos-references/ringtone-ringtone.md)  - 指南：[设置铃声](ringtone-preparations.md) |

**Scan Kit**

| 分类 | 资源链接 |
| --- | --- |
| 默认界面扫码 | - ArkTS API参考：[默认界面扫码](../harmonyos-references/scan-scanbarcode-api.md)  - 指南：[默认界面扫码](scan-scanbarcode.md) |
| 自定义界面扫码 | - ArkTS API参考：[自定义界面扫码](../harmonyos-references/scan-customscan-api.md)  - 指南：[自定义界面扫码](scan-customscan.md) |
| 图像识码 | - ArkTS API参考：[图像识码](../harmonyos-references/scan-imagedecode.md)  - 指南：[识别本地图片](scan-detectbarcode.md)  - 指南：[识别图像数据](scan-decodeimage.md) |
| 码图生成 | - ArkTS API参考：[码图生成](../harmonyos-references/scan-generatebarcode.md)  - 指南：[通过文本生成码图](scan-barcodegenerate.md)  - 指南：[通过字节数组生成码图](scan-generatearray.md) |
