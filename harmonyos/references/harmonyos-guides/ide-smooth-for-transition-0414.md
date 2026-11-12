---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-smooth-for-transition-0414
title: 转场操作流畅
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 附录 > 体检规则 > 转场操作流畅
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:51604cd265693c1071da8a10031010d1b25bee8fcc44da8605d62960b24d2050
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/n9YNA6qzSBqksb65Vhuy7w/zh-cn_image_0000002808766611.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=D8A14D9C0D694C0AF2F9ED821A4D32B0708186B2DE9076EFBD7CA97BCC6D212F)

* 总时长(s)：【最后一个“H:Waiting for Present Fence xxxx” 时间（如图标记2）】 - 【第一个“H:Waiting for Present Fence xxxx” 时间（如图标记1）】。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/VhSob0LIS6GhIXDMUBvzxQ/zh-cn_image_0000002808886687.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=749C6715B9701B65AC64BFBAEB3840F4DA75B34F6B91B4136D083F630950FE1B)

* 每帧时长(ms)：1000ms / 刷新率。
* 刷新率：在泳道范围内查找关键词H:RSHardwareThread::CommitAndReleaseLayers rate，如下图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/rTKhqJMQRUesKER-f-627A/zh-cn_image_0000002779407048.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=2FC07066C11FD0DFBEB0CB9F092A43E22535F92846ED80092468C8B985DC230F)

* 每帧渲染实际耗时(ms)：【下一个H:Waiting for Present Fence xxxx的起始时间】 - 【当前H:Waiting for Present Fence xxxx的起始时间】如下图 【标记2 - 标记1】。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/Ax3pFHuETBWEDlhRZWmy5w/zh-cn_image_0000002779407050.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=127AE0B99C74DE3FAA59EB304BF3EADD62E9443BF2F3336CCFE768AEC4AA35CD)

* 每帧丢帧时间(ms)：max（【每帧渲染实际耗时(ms)】- 【每帧时长(ms)】 \* 1.5, 0）；即每帧耗时大于标准耗时1.5倍时则判定为丢帧。

## 计算逻辑

卡顿率=所有【每帧丢帧时间(ms)】/ 总时长(s)，卡顿率小于等于0ms/s。
