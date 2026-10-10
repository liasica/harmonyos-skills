---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-smooth-for-transition-0414
title: 转场操作流畅
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 附录 > 体检规则 > 转场操作流畅
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:05+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:a911c61d5cf6a828f1278003c74a629263d2bb37cf1672ba2b4cbf75c87b3a12
---

## 规则详情

应用内转场过程卡顿率≤0ms/s；滑动过程卡顿率：动效时间内累计丢帧时间/动效时长。

## 检测逻辑

* 开始时间：以ABILITY\_OR\_PAGE\_SWITCH转场泳道为例，泳道的起点（如图标记1）。
* 结束时间：以ABILITY\_OR\_PAGE\_SWITCH转场泳道为例，泳道的终点（如图标记2）。

  其他转场泳道标记如下：

  H:APP\_TRANSITION\_FROM\_OTHER\_APP

  H:APP\_TRANSITION\_TO\_OTHER\_APP

  H:APP\_SWIPER\_NO\_ANIMATION\_SWITCH

  H:APP\_TABS\_NO\_ANIMATION\_SWITCH

  H:APP\_TABS\_FLING

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/4hPer2maTvW1c7G04Pqlgg/zh-cn_image_0000002701663344.png)

* 总时长(s)：【最后一个“H:Waiting for Present Fence xxxx” 时间（如图标记2）】 - 【第一个“H:Waiting for Present Fence xxxx” 时间（如图标记1）】。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/GHzFzmPnRQC4FvYxnDArgw/zh-cn_image_0000002701823252.png)

* 每帧时长(ms)：1000ms / 刷新率。
* 刷新率：在泳道范围内查找关键词H:RSHardwareThread::CommitAndReleaseLayers rate，如下图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/thb2ef2ESAyu7OrRY833Hg/zh-cn_image_0000002701823256.png)

* 每帧渲染实际耗时(ms)：【下一个H:Waiting for Present Fence xxxx的起始时间】 - 【当前H:Waiting for Present Fence xxxx的起始时间】如下图 【标记2 - 标记1】。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/AveJkk1PRlusoPAG0kIbCA/zh-cn_image_0000002731382561.png)

* 每帧丢帧时间(ms)：max（【每帧渲染实际耗时(ms)】- 【每帧时长(ms)】 \* 1.5, 0）；即每帧耗时大于标准耗时1.5倍时则判定为丢帧。

## 计算逻辑

卡顿率=所有【每帧丢帧时间(ms)】/ 总时长(s)，卡顿率小于等于0ms/s。
