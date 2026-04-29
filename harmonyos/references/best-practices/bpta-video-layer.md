---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-video-layer
title: 视频场景图层低功耗建议
breadcrumb: 最佳实践 > 功耗 > 应用功耗优化 > 前台任务低功耗 > 前台资源合理使用 > 视频场景图层低功耗建议
category: best-practices
scraped_at: 2026-04-29T14:13:51+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:c83ca06446e662bbfecb11da4592ba4b203168b25474e412fa8aa1d4bbdf1311
---

## 建议

* 图层合成包括硬件合成和GPU合成两种方式。硬件合成的功耗比GPU合成低20mA以上。图层数量过多会增加合成负载，超过硬件合成能力时将使用GPU合成，导致功耗增加。因此，建议应用控制图层数量以避免使用GPU合成。
* 图层个数限制：三方应用的图层个数，无弹幕时建议不超过2个图层，有弹幕时建议不超过3个图层。

## 开发步骤

应用使用XComponent组件时，有Surface和Texture两种模式。Surface模式会由一个XComponent组件创建一个独立的Surface图层。根据不同的播放场景，XComponent组件的使用数量也有所不同。在视频/小视频场景中，无弹幕全屏视频播放时，要求一个界面内的Surface模式的XComponent组件数量≤2；而在弹幕全屏视频播放时，由于弹幕功能需要额外Surface图层渲染弹幕内容，该限制放宽至一个界面内的Surface模式的XComponent组件数量≤3。

```
1. XComponent({ id: 'XComponentId', type: 'surface', libraryname: 'entry' })
2. .width(360)
3. .height(360)
```

[VideoSceneLayers.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/RationalUseOfFrontEndResources/entry/src/main/ets/pages/VideoSceneLayers.ets#L26-L28)

## 调测验证

图层抓取命令为**hdc shell hidumper -s 10 -a allInfo。**图层的信息如下，通过查看LayerInfo中的Surface个数，可以得出图层个数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/vpGvTA5LT7Soj0MOnoM43g/zh-cn_image_0000002229336393.png?HW-CC-KV=V1&HW-CC-Date=20260429T061350Z&HW-CC-Expire=86400&HW-CC-Sign=165B27BA27B7F66D4DAE879B7044FEFDD98CCCF602398CE33A5C6337B71F3B15 "点击放大")

上图所示为一个没有弹幕的视频场景，共有4个图层，其中系统的图层2个（RCDTopSurfaceNode和RCDBottomSurfaceNode），三方应用图层2个，符合三方应用图层个数要求。
