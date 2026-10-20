---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/avcodec-kit-troubleshooting-0001
title: 视频播放画面异常常见问题定位
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频编解码（AVCodec） > 故障排查 > 视频播放画面异常常见问题定位
category: harmonyos-faqs
scraped_at: 2026-10-21T07:12:20+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:1e4aab200afd5969c0e65120aa2889f577c2bc0f8c1f23f9b21129178b9b162d
---

## 视频播放花屏

### 问题现象

视频在播放过程中出现画面异常，表现为色彩失真、条纹、闪烁或马赛克等现象。

### 定位过程

1. 视频播放花屏排查流程图如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/wnpQUhRTSGqPz0dwlQG45g/zh-cn_image_0000002765034374.png "点击放大")
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

     ```txt
     - 查看应用是否使用了编解码器，全局搜索OH_VideoEncoder_Create，查看创建编码器时的设置。
     ```

     ```cpp
     int32_t VideoEncoder::Create(const std::string &videoCodecMime)
     {
         encoder_ = OH_VideoEncoder_CreateByMime(videoCodecMime.c_str());
         CHECK_AND_RETURN_RET_LOG(encoder_ != nullptr, AVCODEC_SAMPLE_ERR_ERROR, "Create failed");
         return AVCODEC_SAMPLE_ERR_OK;
     }
     ```
   * 检查视频编码器有没有做stride和视频宽高不一致时的处理。

     ```cpp
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

### 分析结论

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

### 修改建议

* 若网络环境较差，建议用户选择网络较好的环境。
* 若为视频资源本身的问题，建议更换视频资源。
* 若视频编解码异常导致的视频花屏，建议参考[视频编码](../harmonyos-guides/video-encoding.md)和[视频解码](../harmonyos-guides/video-decoding.md)文档修改。

## Native音视频编解码常见错误

### 问题现象

视频编码器触发OH\_AVCodecOnError回调函数，错误码AV\_ERR\_INPUT\_DATA\_ERROR = 10。

### 定位过程

DevEco Studio本地搜索OH\_AVErrCode关键字，查看错误码AV\_ERR\_INPUT\_DATA\_ERROR = 10含义，确认为输入数据错误。

### 分析结论

错误码AV\_ERR\_INPUT\_DATA\_ERROR错误可能原因：

* 运行过程中surfacebuffer宽、高超出OH\_VideoEncoder\_Configure接口配置的宽、高，会触发AV\_ERR\_INPUT\_DATA\_ERROR报错，如：传参时，误将surface宽高传入顺序颠倒，使得surface宽高和编码器宽高相反。
* 配置信息与输入数据比特不一致，会触发AV\_ERR\_INPUT\_DATA\_ERROR报错。如：编码输入数据为8bit而配置为10bit，或编码输入数据为10bit而配置为8bit。
* 配置了不支持的pixelformat，会触发AV\_ERR\_INPUT\_DATA\_ERROR报错。如：配置了[视频像素格式枚举值OH\_AVPixelFormat](../harmonyos-references/capi-native-avformat-h.md#oh_avpixelformat)中不存在的格式。

### 修改建议

参考[使用AVCodec实现视频编解码](https://gitcode.com/HarmonyOS_Samples/AVCodecVideo)为编解码中的配置项设置正确的参数。
