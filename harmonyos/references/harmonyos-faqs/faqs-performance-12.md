---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-12
title: ArkUI页面的视频加载缓慢
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > ArkUI页面的视频加载缓慢
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:118d2eb6b24239a217d88b885ea45748760f76b77e4f6767211660b74ec4c0b9
---

## 问题现象

打开应用中视频观看时，需要等待一段时间后视频才开始播放。

## 背景知识

* [Video](../harmonyos-references/ts-media-components-video.md)：可用于播放视频文件的组件。
* 视频码率：在单位时间内，视频文件传输的数据量，也叫视频的数据速率，通常用bps（位每秒）、Kbps（千位每秒）或Mbps（兆位每秒）来表示。
* 视频起播水线：为了保证视频流畅播放设置的缓冲区阈值。当视频缓冲区的已下载数据量达到起播水线值时，才会开始播放视频，有助于减少视频播放初期可能出现的卡顿现象。起播水线取值与下载速率与视频码率有关，如果下载速率大于或等于视频码率，起播水线取值为0.3\*码率，如果下载速率小于视频码率，起播水线取值为5\*码率，具体可看[缓冲区工作过程](../harmonyos-guides/online-video-playback-lags-optimize.md#缓冲区工作过程)。
* ArkUI Inspector：DevEco Studio提供的[布局分析](../harmonyos-guides/ide-arkui-inspector.md)工具，可用于查看应用在真机上的UI显示效果，能够快速分析定位状态变量、组件嵌套层次、UI界面布局存在的问题等。
* DevEco Profiler：集成在DevEco Studio中的性能调优工具，提供场景化的性能调优功能体验，可以检测应用的性能指标、录制Trace信息，通过分析Trace数据能够发现代码中的性能瓶颈，进而优化性能，相关内容可看[DevEco Profiler调优工具简介](../harmonyos-guides/ide-profiler.md)。

  视频加载关键Trace点如下：

  | Trace关键字 | 描述 | 泳道/线程 |
  | --- | --- | --- |
  | H:DispatchTouchEvent xxx type=1 | 应用收到手指离开屏幕的事件 | 应用主进程 |
  | H:Create[组件名][self:组件id] | 组件创建 | 应用主进程 |
  | H:PlayerServer::PrepareAsync | 系统播放器服务准备播放 | media\_service进程的H:PlayerServer::PrepareAsync泳道 |
  | H:PlayerServer::Play | 系统播放器服务启动播放 | media\_service进程的H:PlayerServer::Play泳道 |
  | H:HiPlayerImpl::PrepareAsync | 播放器引擎实例初始化，准备播放。与H:PlayerServer::PrepareAsync对应，分析H:PlayerServer::PrepareAsync具体耗时情况需要分析该Trace关键字，如下图所示 | media\_service进程的PlayerEngine线程 |
  | H:HiPlayerImpl::Play | 播放器引擎实例启动播放。与H:PlayerServer::Play对应，分析H:PlayerServer::Play具体耗时情况需要分析该Trace关键字，如下图所示 | media\_service进程的PlayerEngine线程 |
  | H:HttpRequest | http请求 | 应用进程的H:HttpRequest泳道 |

## 问题定位

以某应用视频加载时间长问题为例，定位过程如下：

1. 使用ArkUI Inspector抓取应用页面布局，得知应用使用Video组件进行视频播放。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/2ACrCZ1IShWfQkYjRssVfQ/zh-cn_image_0000002628395104.png "点击放大")
2. 使用Profiler Frame抓取视频加载播放过程的应用Trace信息，然后搜索应用收到手指离开屏幕的事件、Video组件创建、播放器准备、播放器播放相关Trace点。
   * 应用收到手指离开屏幕：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/f6152ko8Shyu09GgYK76JA/zh-cn_image_0000002658914323.png "点击放大")
   * Video组件创建：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/-2Z2-1fWThWA_CeJgWkohQ/zh-cn_image_0000002658794371.png "点击放大")
   * 播放器准备：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/LbnVnNESRsuA6EWVEcc0OQ/zh-cn_image_0000002628555006.png "点击放大")
   * 播放器播放：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/wv_O0GxtRKGF8TP33e3wBA/zh-cn_image_0000002628395106.png "点击放大")

3. 计算上述Trace关键字之间的时间，分析其中耗时最多的部分，具体情况如下：
   * 耗时主要集中在从应用收到手指离开屏幕事件到Video组件创建阶段，如下表所示。

     | 应用收到手指离开屏幕事件到Video组件创建 | Video组件创建到播放器准备 | 播放器准备耗时 | 播放器播放耗时 |
     | --- | --- | --- | --- |
     | 10s | 41ms | 314ms | 25ms |

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/Z50GyKK1RG6kkQWsCO6_xA/zh-cn_image_0000002658914325.png "点击放大")

     查看上图中应用收到手指离开屏幕事件到Video组件创建阶段，应用主线程并无长时间Running的情况，在Video组件创建前可以看到状态变量有刷新，怀疑应用刷新该状态变量后会触发Video组件创建，而状态变量刷新可能与http请求有关。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/AUON1SnTRdywDq3zBk6e4A/zh-cn_image_0000002658794373.png "点击放大")

     排查应用H:HttpRequest泳道信息发现应用有进行http请求，耗时接近10s，由此可知应用在加载视频前会进行http请求，从服务器获取数据后刷新组件的状态变量，创建Video组件开始播放视频。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/5-L6Y5iqQLqip7oa2rKUEw/zh-cn_image_0000002628555008.png "点击放大")

     搜索应用包名/NETSTACK日志关键字，查看http请求时的相关耗时参数，发现此处http请求耗时集中在firstRecv部分，应用服务器响应应用请求时，处理耗时较多。

     ```txt
     04-22 21:36:54.839 22080 22716 I C015B0/com.example.myapplication/NETSTACK: [http_exec.cpp:418] taskid=-2147483621, size:40791, dns:0.100, connect:0.000, tls:0.000, firstSend:0.230, firstRecv:9672.959, total:9965.226, redirect:0.000, errCode:0, RespCode:200, httpVer:3, method:GET, osErr:0
     ```
   * 耗时主要集中在播放器准备，如下表所示，需要通过日志分析视频数据下载情况。

     | 应用收到手指离开屏幕事件到Video组件创建 | Video组件创建到播放器准备 | 播放器准备耗时 | 播放器播放耗时 |
     | --- | --- | --- | --- |
     | 394ms | 18.1ms | 12.4s | 44.4ms |

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/QcbN3H_BQhKFJBkaC0ei3w/zh-cn_image_0000002628395108.png "点击放大")

     在日志中搜索BUFFERING\_START PAUSE|BUFFERING\_END PLAYING|HTTP Buffer is enough|bitrate =找到视频缓冲的起始点、结束点、起播水线、数据下载速度和视频码率，如下图中看到视频缓冲的时间为11.415s（BUFFERING\_START PAUSE和BUFFERING\_END PLAYING时间间隔），起播水线为5773077字节，下载速度为4209738bit/s，视频码率为9236923bps。

     ```txt
     07-14 14:15:02.080  1707  3269 I C02B32/av_codec_service/HCODEC: [44][dec.avc][Initialized][Configure 104] bitrate = 9236923 | codec_config, bufferSize = 52 | codec_mime = video/avc | frame_rate = 30.000000 | height = 1080 | language = und | rotation_angle = 0 | track_index = 0 | track_start_time = 0 | track_type = 1 | video_delay = 1 | video_encoder_enable_surface_input_call ...
     07-14 14:15:02.097  1436 24011 I C02B22/media_service/HiPlayer: #2180 BUFFERING_START PAUSE
     07-14 14:15:13.512  1436 24017 I C02B23/media_service/HiStreamer: (HandleBuffering(), 289): HTTP Buffer is enough, bufferSize:5773623 waterLineAbove: 5773077 avgDownloadSpeed: 4209738.819320
     07-14 14:15:13.512  1436 24011 I C02B22/media_service/HiPlayer: #2171 BUFFERING_END PLAYING
     ```

     由于视频码率大于下载速率，起播水线取值为5\*9236923/8=5773076.875字节，与日志中看见的一致，由于视频码率较大，超过当前网络下载速率，视频缓冲到起播水线需要时间，导致视频加载慢。

## 分析结论

视频加载慢的原因有：

* 应用在视频播放前发送http请求访问服务器获取数据，服务器端业务逻辑处理耗时较长，导致应用侧收到数据较慢，视频延迟一段时间后才能播放。
* 视频码率较大，超过当前网络下载速率，视频缓冲到起播水线需要时间，导致视频加载慢。

## 修改建议

* 优化服务器侧处理逻辑。
* 使用码率较小的视频资源，增加视频加载中提示，或使用[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)实现视频播放，通过[setMediaSource](../harmonyos-references/arkts-apis-media-avplayer.md#setmediasource12)方法调整PlaybackStrategy中的preferredBufferDurationForPlaying参数去设置起播缓冲水线值。
