---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/performance-troubleshootin-0003
title: ArkUI-Canvas组件图片放大卡顿问题定位
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 故障排查 > ArkUI-Canvas组件图片放大卡顿问题定位
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:42+08:00
doc_updated_at: 2026-10-14
content_hash: sha256:53b73be408a109d8ee23500979c67c460d668493611943c043a9a944a4ecdcb2
---

## 问题现象

在浏览图片时，双击图片放大，放大过程中明显感到卡顿不流畅。

## 定位过程

1. 复现问题，找到发生卡顿的问题页面，使用ArkUI Inspector抓取当前页面的组件结构，发现应用使用Canvas组件绘制当前页面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/AsC56S_DS9GXWSoXIVSa2g/zh-cn_image_0000002762688108.png "点击放大")
2. 使用DevEco Profiler中的Frame模板抓取整个复现流程的Trace，由于是双击后放大图片，在应用包名泳道搜索关键字H:DispatchTouchEvent找到第二个type=1的Trace点，此时为双击事件识别成功，可作为问题分析的起点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/e6wumC8ATIa0jOqxridv4A/zh-cn_image_0000002762848058.png "点击放大")
3. 查看render\_service进程中的H:PreferredFrameRate，鼠标悬停可查看此时屏幕刷新率为90Hz。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/hYtDPUC2RTSgpKyXmeEcFQ/zh-cn_image_0000002792206921.png "点击放大")
4. 应用发生卡顿的页面是用[Canvas](../harmonyos-references/ts-components-canvas-canvas.md)组件绘制的，因此搜索关键字H:FrameNode[Canvas][id:xxx]::RenderTask，发现应用侧渲染Canvas组件周期为100ms，换算成刷新率仅为10Hz，远低于当前屏幕刷新率90Hz，因此使用体验非常卡顿。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/yYsNTztsTam2_53g7-BHiA/zh-cn_image_0000002762848074.png "点击放大")

## 分析结论

双击放大图片时，应用组件渲染的频率过低，远小于屏幕刷新率，导致放大过程异常卡顿丢帧问题。

## 修改建议

GPU并行计算能力优于CPU，更适用于绘制图片，建议应用侧参考[GPU后端Canvas的创建与显示](../harmonyos-guides/canvas-get-result-draw-c.md#gpu后端canvas的创建与显示)创建GPU后端Canvas，提高绘制性能，减少卡顿。
