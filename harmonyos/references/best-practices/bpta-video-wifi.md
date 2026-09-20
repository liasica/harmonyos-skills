---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-video-wifi
title: 视频场景Wi-Fi加载低功耗建议
breadcrumb: 最佳实践 > 功耗 > 应用功耗优化 > 前台任务低功耗 > 前台资源合理使用 > 视频场景Wi-Fi加载低功耗建议
category: best-practices
scraped_at: 2026-09-21T06:25:48+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:fc73b80630e7c257a27239c142354c50ab032093443a5b6c5b9e48472ecb4865
---

## 建议

视频场景数据缓存下载方式：建议每20s下载一次，每次下载3到5s，以避免小流量持续下载导致Wi-Fi功耗增加。

## 开发步骤

调用系统的setHandoverCb()接口，实现聚合方式缓存视频，具体的接口调用方法如下：

1.监听系统接管状态，要注册系统handover起始回调，接收变化通知，包含接管start回调及接管结束回调。

setHandoverCb(HandoverStartCb startCb, HandoverCompleteCb completeCb);

2.当应用需要短时间使用网络链路，需要反馈期望使用网络的earliestBegin时间及最晚忍受时间，系统会参考多个应用的时间进行拉齐，统一在一段时间内恢复网络的正常使用。transDesc中包含期望的最早时间和可以忍受的最晚时间。

setTransDesc(transDesc);

3.当应用有优先级不高且不影响基本功能的业务时，比如上传log等，应用可以在发送数据的请求中标识该请求，系统会进行统一调度。out中传入系统自主控制delegation的标志位。

send(out);

## 调测验证

相同大小的文件下载存在两种方式：按聚合方式下载和小流量持续下载。数据包与时间的关系如下：

1. 按聚合方式下载时，例如每20s下载一次，每次下载3到5s，Wi-Fi器件在大部分时间处于idle状态，实测Wi-Fi功耗为35mA。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/C_gJ3H4KRtq_AGXkn8XDHw/zh-cn_image_0000002193850568.png "点击放大")
2. 当以小流量持续下载时，例如每1s下载一次，Wi-Fi器件的空闲时间会减少。实测结果显示，小流量持续下载的Wi-Fi功耗为55mA，而聚合下载的功耗为35mA。因此，建议应用采用聚合方式下载，以避免小流量持续下载导致的高Wi-Fi功耗。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/oebB0WHwRlub8s4JdTUAHQ/zh-cn_image_0000002193850572.png "点击放大")
