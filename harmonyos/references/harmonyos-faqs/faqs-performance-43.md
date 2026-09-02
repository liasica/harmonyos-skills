---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-43
title: 点击视频播放按钮后长时间初始化
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 点击视频播放按钮后长时间初始化
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f3fd456a864046df130d696158061b5c42076281189da5727b51984049e037e6
---

## 问题现象

点击视频播放按钮，视频长时间处于初始化状态，无法操作滑动进度条等。

## 背景知识

* **ArkUI Inspector**：

  ArkUI Inspector是DevEco Studio提供的[布局分析](../harmonyos-guides/ide-arkui-inspector.md)工具，可用于查看应用在真机上的UI显示效果，能够快速分析定位状态变量、组件嵌套层次、UI界面布局存在的问题等。
* **DevEco Profiler Frame分析**：

  [Frame分析](../harmonyos-guides/ide-insight-session-frame.md)：开发应用或元服务过程中，如果发现有表单滑动不顺畅、页面交互延迟、动效不流畅等卡顿现象时，可以使用DevEco Profiler提供的Frame场景分析能力，录制卡顿过程中的关键数据进行分析，从而识别出导致卡顿丢帧的原因所在。
* **ffmpeg（解封装）初始化**：

  解封装初始化分两块：TypeFound（嗅探容器格式解析）和setDatasource(文件属性解析)。其中嗅探阶段耗时只与数据输入速率有关，重点分析对象是setDatasource阶段耗时。
* **setDatasource耗时**：
  + 数据申请耗时：初始化数据量大：mp4等自带详细帧box信息的格式在读头信息时天生会比其他格式需要的数据量大；画质较高的资源初始化所需要的数据量一般也会比画质较低的视频的大。网络环境差：网络差的情况下所需要读到单位长度的耗时就会更多。
  + 单纯解封装解析耗时：仅限于个别资源在本地播放时必现起播慢的情况下需排查单纯解封装解析耗时。

## 问题定位

1. 使用ArkUI Inspector可以看到视频初始化过程中的加载组件名为LoadingProgress。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/2Jh4XjoPRK-X86grdXxLug/zh-cn_image_0000002658914511.png)
2. 使用DevEco Profiler Frame模板抓取从点击播放按钮到视频开始播放的Trace，搜索关键字H:DispatchTouchEvent XXX type=1作为起始时间。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/nKJ86OTuSUqAdQtt4JIGgg/zh-cn_image_0000002628395280.png "点击放大")

   搜索最后一次关于LoadingProgress渲染的Trace点H:FrameNode[LoadingProgress]作为结束时间。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/b8TMnXBSR2adE0jjlUly2g/zh-cn_image_0000002658794555.png "点击放大")

   可以看到在此时间范围内应用包名主线程并无耗时过长的Trace点，可以排除应用主线程阻塞导致的耗时。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/cacTeu5KQeCO-FcX_NqgAQ/zh-cn_image_0000002628555192.png "点击放大")
3. 查看media\_service泳道中PlayerEngine子泳道，可以明显看到16s多的耗时点，耗时主要集中在H:ffmpeg\_init，ffmpeg\_init是应用对资源进行解封装初始化。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/zcbxg9NbRhSeqKThBtUi-g/zh-cn_image_0000002658914513.png "点击放大")
4. 根据背景知识中对解封装初始耗时原因的介绍，重点分析数据申请耗时。因为在不同网络环境下可复现问题，故排除网络环境差导致的耗时问题。

   在HiLog中搜索content-type|content-range：

   ```txt
   8179: 07-17 10:55:46.645  1541 34079 I C02B23/media_service/HiStreamer: (HandleContentType(), 873): content-type:  video/mp4
   8182: 07-17 10:55:46.645  1541 34079 I C02B23/media_service/HiStreamer: (HandleRange(), 935): content-range:  bytes 0-8191/11319147656
   ```

   根据搜索结果content-type:video/mp4、content-range:bytes 0-8191/11319147656可知资源是11G左右大小的mp4，对头部数据要求很大。

   在HiLog中搜索http buffer is enough|NotifyInitializationCompleted：

   ```txt
   25604: 07-17 10:56:03.157  1541 34079 I C02B23/media_service/HiStreamer: (HandleBuffering(), 288): HTTP Buffer is enough, bufferSize:15284 waterLineAbove: 4096 avgDownloadSpeed: 21132934.131737
   25629: 07-17 10:56:03.166  1541 34079 I C02B23/media_service/HiStreamer: (HandleBuffering(), 288): HTTP Buffer is enough, bufferSize:6404 waterLineAbove: 4096 avgDownloadSpeed: 21132934.131737
   25679: 07-17 10:56:03.177  1541 34079 I C02B23/media_service/HiStreamer: (HandleBuffering(), 288): HTTP Buffer is enough, bufferSize:12204 waterLineAbove: 4096 avgDownloadSpeed: 21132934.131737
   25693: 07-17 10:56:03.187  1541 34079 I C02B23/media_service/HiStreamer: (HandleBuffering(), 288): HTTP Buffer is enough, bufferSize:7744 waterLineAbove: 4096 avgDownloadSpeed: 21132934.131737
   25701: 07-17 10:56:03.214  1541 34079 I C02B23/media_service/HiStreamer: (HandleBuffering(), 288): HTTP Buffer is enough, bufferSize:19424 waterLineAbove: 4096 avgDownloadSpeed: 21132934.131737
   26349: 07-17 10:56:04.310  1541 34074 I C02B3A/media_service/FfmpegDemuxerPlugin: (NotifyInitializationCompleted(), 1024): Large init size 41152121
   ```

   根据搜索结果，Large init size 41152121是指需加载41152121bytes的头部数据才会开始播放，avgDownloadSpeed: 21132934.131737是指下载速度大约为21132934bps换算后是2.5M/s左右，根据资源大小和下载速度可以计算得出头部数据下载时间在16s左右，因此会长时间处于初始化阶段。

## 分析结论

资源文件是过大的mp4，因此初始化阶段的头部数据很大，下载耗时，故长时间初始化。

## 修改建议

1. 适当调整视频分辨率和码率，对视频进行压缩处理，具体可参考[视频压缩处理](../architecture-guides/video_compress_demo-0000002248722292.md)。
2. 长视频分割为多段时长适中的视频，减少初始化阶段数据下载量。
