---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-26
title: AVScreenCapture录屏获取到的视频数据无法正常显示
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > AVScreenCapture录屏获取到的视频数据无法正常显示
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:44+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5b528d83e848ec19f3bf10c58d9289cba6f7f5e7bc5cb1d55dd814abccd7a1a8
---

## 问题现象

使用AVScreenCapture模块进行屏幕录制，在录屏结束获取完数据之后视频数据无法正常显示。核心代码如下：

```cpp
OH_VideoCaptureInfo videocapinfo = {
  .videoFrameWidth = 720, 
  .videoFrameHeight = 1280,
  .videoSource = OH_VIDEO_SOURCE_SURFACE_RGBA
};
```

问题显示如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/6JfZxv8NStum0iy4C_UWlw/zh-cn_image_0000002628552652.png "点击放大")

## 背景知识

* [AVScreenCapture](../harmonyos-guides/media-kit-intro.md#avscreencapture)：主要工作是捕获音频信号、视频信号，并通过音视频编码将屏幕信息保存到文件中，帮助开发者轻松实现屏幕录制功能，主要包括录屏存文件和录屏取码流两套接口，它允许调用者指定屏幕录制的编码格式、封装格式和文件路径等参数。
  + [使用AVScreenCapture录屏取码流(C/C++)](../harmonyos-guides/using-avscreencapture-for-buffer.md)：开发者可以调用录屏（AVScreenCapture）模块的C API接口，完成屏幕录制，采集设备内、麦克风等的音视频源数据。当开发直播、办公等应用时，可以调用录屏模块获取音视频原始码流，然后通过流的方式流转到其他模块处理，达成直播时共享桌面的场景。
  + [使用AVScreenCapture录屏写文件(C/C++)](../harmonyos-guides/using-avscreencapture-for-file.md)：开发者可以调用录屏（AVScreenCapture）模块的C API接口，完成屏幕录制，采集设备内、麦克风等的音视频源数据。可以调用录屏模块获取音视频文件，然后通过文件的形式流转到其他模块进行播放或处理，达成文件形式分享屏幕内容的场景。
* [视频编码](../harmonyos-guides/video-encoding.md)：可通过调用该模块的Native API接口，完成视频编码，即将未压缩的视频数据压缩成视频码流。在视频编码过程中，编码器会通过算法将图像划分为多个小块，然后逐块进行压缩处理。根据视频编码方式的不同，最大块（即宏块）大小也不同，当前系统支持的视频编码格式有HEVC(H.265)和AVC(H.264)两种，两者区别可参见下表：

  |  | H.265 | H.264 |
  | --- | --- | --- |
  | 宏块大小 | 64x64（帧宽高均为64的整数倍） | 16x16（帧宽高均为16的整数倍） |
  | 编码效率 | 压缩率高，节省带宽和存储 | 相对较低 |
  | 画面质量 | 画面质量更好，低码率情况下优势明显 | 相对较差 |
  | 硬件要求 | 硬件要求高，老设备可能不支持 | 几乎所有视频播放设备都能支持 |
  | 计算复杂度 | 编码算法复杂，编解码所需时间和资源消耗都更高 | 复杂度较低，编解码速度较快 |
  | 适用场景 | 4K、8K超高清视频、流媒体服务、视频存储等领域 | 网络视频、监控系统、视频会议等对实时性要求高、设备性能有限的场景 |

## 问题定位

1. debug发现OH\_AVBuffer\_GetAddr(buffer)里面实际有录屏的数据，并且日志里面也没有报错信息。这说明录屏过程并没有问题，可能是录屏数据在编解码/渲染显示的过程中出现了异常。
2. 排查代码时发现，代码里通过OH\_VideoCodecFormat指定了视频编码格式为OH\_H265，而录屏的帧宽高为720x1280，帧宽度并不是64的整数倍，不符合H.265的分辨率大小要求。

## 分析结论

采用H.265格式给视频编码时，算法会将帧画面划分为64x64大小的块，后续帧内/帧间预测时的残差块的大小也与之相同。而录屏时设定的帧宽度并非64的整数倍，因此使得视频画面在编解码过程中产生画面异常。

## 修改建议

将视频的宽度和高度设置为64的倍数，例如768\*1280，以此来适应视频编码的标准。

完整示例代码可以参考[AVScreenCapture录屏完整示例](../harmonyos-guides/using-avscreencapture-for-file.md#完整示例)。

## 常见FAQ

Q：使用AVScreenCapture录屏取码流，出现Native层数据持续增长，调用释放资源的接口，应在什么时机进行资源释放？

A：可以在内录和外录代码处释放buffer。

Q：使用AVScreenCapture录屏取码流过程中，在屏幕旋转的情况下如何动态调整编码器宽高？

A：编码器不支持动态设置宽高，需要先停止再重新进行配置。但是在屏幕旋转过程中，编码器适配屏幕宽高的场景，可以采用如下方式处理：录制开始时是1920×1080的，录制过程中屏幕旋转切换成1080×1920，最开始可以创建一个1920×1920的编码器，这样就不用过程中动态修改编码器宽高。

Q：想通过OH\_AVScreenCapture\_SetStateCallback()方法来设置状态变更处理函数，但是不知道各个状态切换的时机。

A：通过[OH\_AVScreenCapture\_SetStateCallback()](../harmonyos-references/capi-native-avscreen-capture-h.md#oh_avscreencapture_setstatecallback)设置回调成功后，在启动录屏时将通过隐私弹窗方式征求用户同意。之后在录屏过程中，每当OH\_AVScreenCapture实例状态发生改变即会调用该回调函数。OH\_AVScreenCapture实例状态含义及触发时机见下表：

| 状态 | 含义 | 触发时机 |
| --- | --- | --- |
| OH\_SCREEN\_CAPTURE\_STATE\_CANCELED | 已取消录屏 | 用户拒绝录屏隐私弹窗时 |
| OH\_SCREEN\_CAPTURE\_STATE\_STOPPED\_BY\_USER | 已停止录屏 | 用户手动点击结束时 |
| OH\_SCREEN\_CAPTURE\_STATE\_MIC\_UNAVAILABLE | 麦克风不可用 | 麦克风不可用导致启动录屏失败时 |
| OH\_SCREEN\_CAPTURE\_STATE\_STARTED | 已开始录屏 | 启动录屏成功后 |
| OH\_SCREEN\_CAPTURE\_STATE\_INTERRUPTED\_BY\_OTHER | 录屏被其他录屏中断 | 录屏被其他录屏中断时 |
| OH\_SCREEN\_CAPTURE\_STATE\_STOPPED\_BY\_CALL | 录屏被通话中断 | 录屏被通话中断时 |
| OH\_SCREEN\_CAPTURE\_STATE\_MIC\_MUTED\_BY\_USER | 麦克风被静音 | 麦克风被静音时 |
| OH\_SCREEN\_CAPTURE\_STATE\_MIC\_UNMUTED\_BY\_USER | 麦克风被取消静音 | 麦克风被取消静音时 |
| OH\_SCREEN\_CAPTURE\_STATE\_ENTER\_PRIVATE\_SCENE | 进入隐私弹窗 | 进入隐私弹窗时 |
| OH\_SCREEN\_CAPTURE\_STATE\_EXIT\_PRIVATE\_SCENE | 隐私弹窗退出 | 隐私弹窗退出时 |
| OH\_SCREEN\_CAPTURE\_STATE\_STOPPED\_BY\_USER\_SWITCHES | 系统用户切换，录屏中断 | 系统用户切换时 |

Q：使用OH\_ORIGINAL\_STREAM方式录制屏幕，屏幕正常录制，但OnBufferAvailable回调的数据写到Muxer中封装为MP4格式，文件无法正常播放。

A：检查发现代码录制屏幕数据能够直接播放，且使用中AVMuxer对已编码数据封装正常，确定录制和封装两边单独的功能都没有问题。后查看代码发现流程直接将OH\_ORIGINAL\_STREAM方式录制屏幕的未编码直接放入AVMuxer进行封装。

方案一：修改OH\_AVScreenCaptureConfig参数，将dataType配置为OH\_CAPTURE\_FILE模式，直接MP4文件，详细流程可参考[使用AVScreenCapture录屏写文件](../harmonyos-guides/using-avscreencapture-for-file.md)。

方案二：OH\_AVScreenCaptureConfig的参数dataType依旧为OH\_ORIGINAL\_STREAM模式，此时流程结束后返回的buffer为原始码流，需要编码后才能放入Muxer中进行封装。编码可参考[视频编码](../harmonyos-guides/video-encoding.md)。
