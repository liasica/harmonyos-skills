---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-smooth-for-swipe-0413
title: 滑动过程流畅
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 附录 > 体检规则 > 滑动过程流畅
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:32+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:7d261dc40144a2d7cc8c2736cd417e5e574908dd5da08a7776b99b57476c6941
---

## 规则详情

应用的滑动过程卡顿率≤5ms/s；满帧30FPS的游戏类、地图类和视频类的应用帧率应≥29FPS。

## 检测逻辑

* 开始时间：以APP\_LIST\_FLING滑动泳道为例，泳道的起点（如图标记1）。
* 结束时间：以APP\_LIST\_FLING滑动泳道为例，泳道的终点（如图标记2）。

  其他滑动泳道标记如下：

  H:APP\_SWIPER\_SCROLL

  H:WEB\_LIST\_FLING

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/vkKrziIWRpiB8jup8qljMQ/zh-cn_image_0000002779406434.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=726B671A8B6B27676595AB1CE29CF11F2B075AD666E84B7F8E930AC7B3EBFB1C)

* 查找滑动泳道：H:APP\_LIST\_FLING，如果是web页面，找H:WEB\_LIST\_FLING。
* 刷新率：查找关键词H:RSHardwareThread::CommitAndReleaseLayers rate，如下图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/YAZc43_0SFSRw6jHles0Yg/zh-cn_image_0000002779566412.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=4E1B0FAF8814C621E5DAA592194E8F7D594C1CA1F8BF3B6A217776152E2DD4DB)
* 每帧标准时长(ms)：1000ms/刷新率。

  总时长(s)：在以上泳道时间范围内，总时长 =【最后一个“H:Waiting for Present Fence xxxx” 时间（如图标记2）】 - 【第一个“H:Waiting for Present Fence xxxx” 时间（如图标记1）】。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/kdkAMv6jS9CWkCft5wWT6g/zh-cn_image_0000002779566408.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=1BD054023834B4E35AE219C099A8E10E99B494CDABA6378D7551A6FC72B91FE9)
* 实际每帧时长：【下一个H:Waiting for Present Fence xxxx的起始时间（如图标记2）】 - 【当前H:Waiting for Present Fence xxxx的起始时间（如图标记1）】。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/T04jA1u7S2q6IJWnIyIkgw/zh-cn_image_0000002779406430.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=9E2EFB1B7B7B787FCF03F2987755008D4170990E1C85E9577F635107E2A08FC7)

  每帧丢帧时间(ms)：max（【Waiting for Present Fence实际时长(ms)】- 【每帧时长(ms)】 \* 1.5 , 0）；即每帧耗时大于标准耗时1.5倍时则判定为丢帧。

## 计算逻辑

卡顿率(即流畅度) = 【每帧丢帧时间累计总和(ms)】/ 总时长(s)，须小于等于5ms/s。
