---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avcodec-8
title: 视频画面模糊，清晰度低
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频编解码（AVCodec） > 视频画面模糊，清晰度低
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:45+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:234d6e292fb6e214f7933e636ed795f96b58672a73ceb917f01384b01db02b69
---

## 问题现象

应用播放器播放视频时出现视频模糊、分辨率低或视频通话时画面模糊等视频清晰度低问题。

## 背景知识

* [AVPlayer](../harmonyos-guides/media-kit-intro.md#avplayer)：功能较完善的音视频播放ArkTS/JS API，集成了流媒体和本地资源解析，媒体资源解封装，视频解码和渲染功能，适用于对媒体资源进行端到端播放的场景，可直接播放mp4、mkv等格式的视频文件。
* [视频解码](../harmonyos-guides/video-decoding.md)：视频类应用（比如视频通话、视频播放器等）将视频码流通过视频解码器解码，解码后的图像数据可以送到视频显示设备显示。
* 编解码器运行错误时返回的错误码请参考[OH\_AVCodecOnError()](../harmonyos-references/capi-native-avcodec-base-h.md#oh_avcodeconerror)。

## 问题定位

1. 本地播放该视频，查看该视频是否模糊。
2. 检查网络状况是否正常可用。
   * 通过系统日志中的WifiFrameWork：SignalPoll字段查看wifi状态，主要定位以下关键字。

     ```screen
     rtRate // 重传率，重传率rtRate>=0.2时报文重传率高，卡顿明显无法上网。
     chload // 通道占用比，可用于表征WiFi信道的繁忙度。chload越高代表网络状态越差,，chload 500以上为中网，会卡顿，800以上不可上网
     rssi // -30表示信号很强，-80表示信号很弱
     noise // -80为干扰环境，到-60以上就是强干扰
     isSpeedOk // 网速质量，rx_speed上传速度，tx_speed下载速度，单位b/s，isSpeedOk false是指上传小于24KB，或者下载小于32KB
     其中rtRate、rssi、isSpeedOk只要有1项较差就说明网络质量不好
     ```
   * 通过系统日志中的应用包名/NETSTACK可以看到应用发起http网络请求时的耗时情况，主要定位以下关键字。

     ```screen
     size：上传或者下载的数据大小（byte）。
     dns：域名解析耗时，单位：ms。
     connect:TCP握手耗时，单位：ms。
     tls：TLS握手（加密鉴权）耗时，单位：ms。
     firstSend：从加密鉴权结束到传输即将开始的耗时，单位：ms。
     firstRecv：从传输开始到第一个字节被接收的耗时，单位：ms。
     total：总耗时，单位：ms。
     分析问题时首先确认total值在问题反馈的总耗时占比是否较多，如总耗时达到秒级，对用户体验就会有较大影响，然后看耗时主要集中在dns、connect、tls、firstSend、firstRecv哪一部分，size值是否过大。
     ```
3. 日志中全局搜索关键字AV\_ERR，查看是否出现AV\_ERR\_VIDEO\_UNSUPPORTED\_COLOR\_SPACE\_CONVERSION、AV\_ERROR\_INPUT\_DATA\_ERROR等字段。

## 分析结论

* 若视频本地播放时的清晰度低，则为视频资源本身清晰度低所导致。
* 若网络环境较差，则为网络环境所导致的视频清晰度低。
* 若日志出现包含AV\_ERR的字段，则为视频编解码异常。

## 修改建议

* 若为视频资源本身清晰度低所导致的视频清晰度低，建议更换清晰度高的视频资源。
* 若为网络环境所导致的视频清晰度低，建议在播放视频过程中提高网络质量。若当前网络质量、网速都处于较高水平，会逐渐提高视频通话的分辨率和码率。
* 若为视频编解码异常所导致的视频清晰度低，建议参考[视频编码](../harmonyos-guides/video-encoding.md)和[视频解码](../harmonyos-guides/video-decoding.md)文档修改相关代码。
