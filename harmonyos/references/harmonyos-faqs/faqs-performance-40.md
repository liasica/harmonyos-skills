---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-40
title: 下拉页面列表刷新卡顿，延迟一段时间后突然回跳
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 下拉页面列表刷新卡顿，延迟一段时间后突然回跳
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:324fd22d8bea3bc13bb37710fbfba3efeace7c7c2e018331a00502bd721b4678
---

## 问题现象

下拉页面刷新列表时存在卡顿问题，延迟一段时间后列表突然回跳，不流畅。

## 背景知识

* [Image](../harmonyos-references/ts-basic-components-image.md)：图片组件，常用于在应用中显示图片。图片组件在加载图片时默认是异步加载方式，可通过[syncLoad](../harmonyos-references/ts-basic-components-image.md#syncload8)设置成同步加载方式。由于同步加载是在主线程上执行，建议在加载尺寸较小的本地图片时使用，如尺寸较大或网络图片则采用异步加载方式。
* ArkUI Inspector：DevEco Studio提供的[布局分析](../harmonyos-guides/ide-arkui-inspector.md)工具。开发者可以借助它预览真机或模拟器中的UI效果，快速定位布局层级问题，也可以观察组件属性、不同组件之间的关系等。
* DevEco Profiler：集成在DevEco Studio中的性能调优工具，提供场景化的性能调优功能体验，可以检测应用的性能指标、录制Trace信息，通过分析Trace数据能够发现代码中的性能瓶颈，进而优化性能。更多详细内容可看[使用Profiler进行性能调优](../harmonyos-guides/ide-profiler-introduction.md)。

  常见Trace关键字：

  | 关键字 | 说明 |
  | --- | --- |
  | H:touchEventDispatch | 屏幕触摸事件 |
  | H:APP\_LIST\_FLING | 列表滑动 |
  | H:APP\_SWIPER\_FLING | 手指离开屏幕后的滑动 |
  | H:HttpRequestInner | http请求 |
  | H:PerformDownload https://xxx.png | 下载网络图片 |

## 问题定位

1. 使用DevEco Profiler Frame分析工具抓取该过程的Trace信息，通过Trace关键字H:touchEventDispatch和H:APP\_LIST\_FLING找到下拉列表后手指离开屏幕的时间点，通过Trace关键字H:APP\_SWIPER\_FLING找到列表开始上移的时间点，从下图中可看到两者时间间隔2.9s，同时可看到在该过程应用接收Vsync信号处理时耗时较长，导致长时间未渲染绘制，因此出现卡顿延迟的现象。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/KMfQb_fzSHC0q8A55i6zhg/zh-cn_image_0000002658794551.png "点击放大")
2. 查看应用接收Vsync信号处理部分的Trace信息，发现应用主线程有下载多张网络图片，总耗时达到2.5s左右，推测应用采用了同步加载方式，导致界面刷新时耗时较长。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/eWyyZw00T9eUVffaIjB4Xg/zh-cn_image_0000002628555188.png "点击放大")
3. 使用ArkUI Inspector抓取页面组件树，查看Image组件的syncLoad参数值为true，确认是同步加载方式。

## 分析结论

下拉页面列表刷新时，由于页面图片采用同步加载方式，在主线程执行网络图片下载操作，导致页面刷新耗时较长，进而引起卡顿、延迟一段时间后上移的现象。

## 修改建议

Image组件取消使用同步加载方式加载图片。

* 将Image组件的syncLoad属性值设置为false。
* 去掉Image组件的syncLoad属性值设置。
