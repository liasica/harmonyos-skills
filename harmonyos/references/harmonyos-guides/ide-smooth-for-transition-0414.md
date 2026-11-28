---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-smooth-for-transition-0414
title: 转场操作流畅
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 附录 > 体检规则 > 转场操作流畅
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:41+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:1398cbef74e11bfab5fac11bfb0d6181c967734a8c2b8ff220d03d7435ebb4b2
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/-jdiba5mTGafp7lbEVglKw/zh-cn_image_0000002808766611.png?HW-CC-KV=V1&HW-CC-Date=20261128T023440Z&HW-CC-Expire=31536000000&HW-CC-Sign=9EE618D824FB23B220FEC92E698DE0D96AC2EBE81A5FE849E54A8BBF094F7E7F)

* 总时长(s)：【最后一个“H:Waiting for Present Fence xxxx” 时间（如图标记2）】 - 【第一个“H:Waiting for Present Fence xxxx” 时间（如图标记1）】。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/lb3Ma89mQ8CJ43F32rv7ew/zh-cn_image_0000002808886687.png?HW-CC-KV=V1&HW-CC-Date=20261128T023440Z&HW-CC-Expire=31536000000&HW-CC-Sign=72412F229CEC2C85DDB482CE7B4C1B50A17885975D2BC2076A357A9F2C6D158F)

* 每帧时长(ms)：1000ms / 刷新率。
* 刷新率：在泳道范围内查找关键词H:RSHardwareThread::CommitAndReleaseLayers rate，如下图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/ZX4KNak-R1idP93DM6sAKQ/zh-cn_image_0000002779407048.png?HW-CC-KV=V1&HW-CC-Date=20261128T023440Z&HW-CC-Expire=31536000000&HW-CC-Sign=8360F3BB1A4AFCC183D9BBA73227FD7B3F7B538505E9BE125ABC6F3E8046FB87)

* 每帧渲染实际耗时(ms)：【下一个H:Waiting for Present Fence xxxx的起始时间】 - 【当前H:Waiting for Present Fence xxxx的起始时间】如下图 【标记2 - 标记1】。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/m2YtGSc1TQ67GGdwkAXGuA/zh-cn_image_0000002779407050.png?HW-CC-KV=V1&HW-CC-Date=20261128T023440Z&HW-CC-Expire=31536000000&HW-CC-Sign=A55E13EEAAE0EBEB6A3AF0C41062FDD62A03003AFFDF6FCC036C13DB58F8F988)

* 每帧丢帧时间(ms)：max（【每帧渲染实际耗时(ms)】- 【每帧时长(ms)】 \* 1.5, 0）；即每帧耗时大于标准耗时1.5倍时则判定为丢帧。

## 计算逻辑

卡顿率=所有【每帧丢帧时间(ms)】/ 总时长(s)，卡顿率小于等于0ms/s。
