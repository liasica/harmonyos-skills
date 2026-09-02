---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avcodec-7
title: 视频播放花屏
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频编解码（AVCodec） > 视频播放花屏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:45+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9a464007b0093e8bddb7177355715e9d3f740c3b94b7951e1760b3087cafaceb
---

## 问题现象

视频在播放过程中出现画面异常，表现为色彩失真、条纹、闪烁或马赛克等现象。

## 背景知识

* [AVPlayer](../harmonyos-guides/video-playback.md)：功能较完善的音视频播放ArkTS/JS API，集成了流媒体和本地资源解析、媒体资源解封装、视频解码和渲染功能，适用于对媒体资源进行端到端播放的场景，可直接播放mp4、mkv等格式的视频文件。
* [视频编码](../harmonyos-guides/video-encoding.md)：将未压缩的视频数据压缩成视频码流。
* [视频解码](../harmonyos-guides/video-decoding.md)：将媒体数据解码成YUV文件或送显。
* 视频宽高是指视频帧的实际宽度和高度，以像素为单位。stride（步幅）描述了图片在内存中每一行像素数据的存储宽度，是图片绘制过程中的重要参数，用于正确定位图片数据在内存中的布局。视频编解码器Buffer模式下，若stride和视频宽高未对齐，需要对视频buffer数据进行处理，否则会导致花屏。
* 以NV12图像为例，width、height、wStride和hStride图像排列参考下图：
  + OH\_MD\_KEY\_WIDTH表示width；
  + OH\_MD\_KEY\_HEIGHT表示height；
  + OH\_MD\_KEY\_VIDEO\_STRIDE表示wStride；
  + OH\_MD\_KEY\_VIDEO\_SLICE\_HEIGHT表示hStride。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/0tAkVv83S6u8LayOiHv1IQ/zh-cn_image_0000002628392792.png "点击放大")

## 问题定位

1. 视频播放花屏排查流程图如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/PyR8soMAS5O9l51530G0QQ/zh-cn_image_0000002658792061.png "点击放大")
2. 检查网络状况是否正常，hilog日志中搜索WifiFrameWork: SignalPoll，主要定位以下关键字。

   | 关键字 | 解释 |
   | --- | --- |
   | rtRate | 重传率，rtRate≥0.2时，报文重传率高，卡顿明显，无法上网。 |
   | chload | 通道占用比，可用于表示WiFi信道的繁忙度。chload越高代表网络状态越差，chload 500以上为中等网络，会出现卡顿现象，800以上不可上网。 |
   | rssi | 信号强度，-30表示信号很强，-80表示信号很弱。 |
   | noise | 噪声，-80为干扰环境，-60以上就是强干扰。 |
3. 使用设备自带的播放器播放该视频资源，查看是否有花屏现象。无法获取该视频资源时，可对比其他平台应用同一视频播放时是否存在花屏。
4. 确认应用是否使用AVPlayer和视频编解码器。
   * 在日志中搜索AVPlayer，如果应用有对应的日志，即表示使用了AVPlayer。

     ```txt
     [NtesMediaPlayer]: [NtesMediaPlayer : 10-9 16:52:1:597] Av-immersive0
     AVPlayerNapi: #220 0xAE9290 JsCreateAVPlayer Out
     [NtesMediaPlayer]: [NtesMediaPlayer : 10-9 16:52:1:597] Av-immersive0
     JsWindow: (1849)Window [400, hmos0] get properties end
     AceXcomponent: [(10000:100000:scope)] XComponent[video] triggers onLoal
     [NtesMediaPlayer : 10-9 16:52:1:606] Av-immersive0
     [foldText]: [foldText : 10-9 16:52:1:609] text = xxxxx
     AVPlayerNapi: #61 0x149500 ctor
     HiTraceC: [a92ab2443194d86 0 0] HiTraceBegin name:PlayerImpl flag5:0x00.
     ```
   * 查看应用是否使用了编解码器，全局搜索OH\_VideoEncoder\_Create，查看创建编码器时的设置。

     ```
     int32_t VideoEncoder::Create(const std::string &videoCodecMime)
     {
         encoder_ = OH_VideoEncoder_CreateByMime(videoCodecMime.c_str());
         CHECK_AND_RETURN_RET_LOG(encoder_ != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "Create failed");
         return AVCODEC_SAMPLE_ERR_OK;
     }
     ```
   * 检查视频编码器有没有做stride和视频宽高不一致时的处理。

     ```
     // widthStride:获取到的buffer数据的跨距。
     if (widthStride == width) {
         // 处理文件流得到帧的长度，再将需要编码的数据写入到对应index的buffer中。 
         int32_t frameSize = width * height * 3 / 2; 
         // NV12像素格式下，每帧数据大小的计算公式。
         inputFile->read(reinterpret_cast<char *>(OH_AVBuffer_GetAddr(bufferInfo->buffer)), frameSize); 
     }else {
         // 如果跨距不等于宽，需要开发者按照跨距进行偏移，具体可参考以下示例。
     }
     ```

## 分析结论

| 步骤 | 判断条件 | 判断结果 | 结论 | 建议 |
| --- | --- | --- | --- | --- |
| 1 | 排查日志，在Hilog日志搜索关键字WifiFrameWork: SignalPoll | 网络环境较差 | 网络问题导致 | 增加缓冲或提示用户 |
| 网络环境好 | 非网络问题导致 | 转步骤2 |
| 2 | 检查视频源是否存在花屏问题 | 视频源播放花屏 | 视频源问题 | 修复视频源 |
| 视频源播放正常 | 视频源无问题 | 转步骤3 |
| 3 | 排查代码，检查是否使用了AVPlayer或者看日志，在HiLog日志中搜索关键字AVPlayer | 未使用AVPlayer | 使用了非官方的播放器 | 检查播放视频的代码逻辑 |
| 使用了AVPlayer | 进一步排查使用的视频编解码器 | 转步骤4 |
| 4 | 排查代码，检查是否使用了OH\_VideoEncoder\_Create | 未使用官方的编解码器 | 使用了非官方的编解码器 | 检查视频编解码的代码逻辑 |
| 使用了官方的编解码器 | 进一步排查视频编解码代码逻辑 | 转步骤5 |
| 5 | 排查代码，检查是否有stride和视频宽高的处理 | 没有stride和视频宽高不一致的处理 | 添加stride和视频宽高不一致时的代码逻辑 | 参见修改建议 |

## 修改建议

* 若网络环境较差，建议用户选择网络较好的环境。
* 若为视频资源本身的问题，建议更换视频资源。
* 若视频编解码异常导致的视频花屏，建议参考[视频编码](../harmonyos-guides/video-encoding.md)和[视频解码](../harmonyos-guides/video-decoding.md)文档修改。
