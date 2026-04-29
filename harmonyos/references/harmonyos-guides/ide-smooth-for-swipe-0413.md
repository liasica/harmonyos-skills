---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-smooth-for-swipe-0413
title: 滑动过程流畅
breadcrumb: 指南 > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 附录 > 体检规则 > 滑动过程流畅
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:04+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:498321bc89be96aaa79c4d29c7160f1c0384d60c96ee81be07131390f1b8e288
---

## 规则详情

应用的滑动过程卡顿率≤ 5ms/s；满帧30FPS的游戏类、地图类和视频类的应用帧率应≥ 29FPS。

## 检测逻辑

* 开始时间：以APP\_LIST\_FLING滑动泳道为例，泳道的起点（如图标记1）。
* 结束时间：以APP\_LIST\_FLING滑动泳道为例，泳道的终点（如图标记2）。

  其他滑动泳道标记如下：

  H:APP\_SWIPER\_SCROLL

  H:WEB\_LIST\_FLING

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/dNWF6HH3T7Gb79z5zA5nDg/zh-cn_image_0000002561752629.png?HW-CC-KV=V1&HW-CC-Date=20260429T054703Z&HW-CC-Expire=86400&HW-CC-Sign=3F1ABDDF774F4C4473D2D7FB4DB8895EB33BE16FAE1790CE7732AB10432BD193)

* 查找滑动泳道：H:APP\_LIST\_FLING，如果是web页面，找H:WEB\_LIST\_FLING。
* 刷新率：查找关键词H:RSHardwareThread::CommitAndReleaseLayers rate，如下图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/Q2Ol7GYKSqqNbLstf4r5Zw/zh-cn_image_0000002530912686.png?HW-CC-KV=V1&HW-CC-Date=20260429T054703Z&HW-CC-Expire=86400&HW-CC-Sign=1713BEB8B00BF4C5F6AFC11E776E4B06CAEB891019B3695BB55040E21C01EF95)
* 每帧标准时长(ms)：1000ms/刷新率。

  总时长(s)：在以上泳道时间范围内，总时长 =【最后一个“H:Waiting for Present Fence xxxx” 时间（如图标记2）】 - 【第一个“H:Waiting for Present Fence xxxx” 时间（如图标记1）】。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/xkwZThl0RWqvPZwP19qWDw/zh-cn_image_0000002561832607.png?HW-CC-KV=V1&HW-CC-Date=20260429T054703Z&HW-CC-Expire=86400&HW-CC-Sign=99CA6B97D5FCDE041033C50DA6C79C51FA8FC06846A2AE84B4C9B2F44D44017F)
* 实际每帧时长：【下一个H:Waiting for Present Fence xxxx的起始时间（如图标记2）】 - 【当前H:Waiting for Present Fence xxxx的起始时间（如图标记1）】。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/79JI2tXiR6GHFJWdXisw4A/zh-cn_image_0000002530752684.png?HW-CC-KV=V1&HW-CC-Date=20260429T054703Z&HW-CC-Expire=86400&HW-CC-Sign=DDF6446C132D80BC699E92AB92A4606B4F95168E1D97B5F56D97E8812E9C9FE3)

  每帧丢帧时间(ms)：max（【Waiting for Present Fence实际时长(ms)】- 【每帧时长(ms)】 \* 1.5 , 0）；即每帧耗时大于标准耗时1.5倍时则判定为丢帧。

## 计算逻辑

卡顿率(即流畅度) = 【每帧丢帧时间累计总和(ms)】/ 总时长(s)，须小于等于5ms/s。
