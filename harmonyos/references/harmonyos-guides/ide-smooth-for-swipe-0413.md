---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-smooth-for-swipe-0413
title: 滑动过程流畅
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 附录 > 体检规则 > 滑动过程流畅
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:b5c43ee9c8399d7c5eaa8fe78240540675cc8b6d3a81da403e06022b3d6eb6ef
---

## 规则详情

应用的滑动过程卡顿率≤5ms/s；满帧30FPS的游戏类、地图类和视频类的应用帧率应≥29FPS。

## 检测逻辑

* 开始时间：以APP\_LIST\_FLING滑动泳道为例，泳道的起点（如图标记1）。
* 结束时间：以APP\_LIST\_FLING滑动泳道为例，泳道的终点（如图标记2）。

  其他滑动泳道标记如下：

  H:APP\_SWIPER\_SCROLL

  H:WEB\_LIST\_FLING

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/Ai2OAkiqS5yI6wFSokSfZw/zh-cn_image_0000002779406434.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=92502AAC7A51697D6C03E4C73E0A95219F178B9EE43F709957DD2DE91FA77E73)

* 查找滑动泳道：H:APP\_LIST\_FLING，如果是web页面，找H:WEB\_LIST\_FLING。
* 刷新率：查找关键词H:RSHardwareThread::CommitAndReleaseLayers rate，如下图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/PdOrOUm8T7qXkKS1JnrvkQ/zh-cn_image_0000002779566412.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=339B1D370EA16E3323E5F0BC21A165B479B3F3C8D3520C735B7A520759DCFB0F)
* 每帧标准时长(ms)：1000ms/刷新率。

  总时长(s)：在以上泳道时间范围内，总时长 =【最后一个“H:Waiting for Present Fence xxxx” 时间（如图标记2）】 - 【第一个“H:Waiting for Present Fence xxxx” 时间（如图标记1）】。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/HX2o9Oy1QRmXk8V8LJdYKQ/zh-cn_image_0000002779566408.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=765FA60F2AE9CA9090388AAA0E6FB91CF95EF4FF308A756FED91B59CDCF8949D)
* 实际每帧时长：【下一个H:Waiting for Present Fence xxxx的起始时间（如图标记2）】 - 【当前H:Waiting for Present Fence xxxx的起始时间（如图标记1）】。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/B3LmwSwPTa2ieBg3fs0N8Q/zh-cn_image_0000002779406430.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=391AAE2864F2DC300BC91FD7DA719893395D449F04A5D7BB4CCED88F4AB59D8A)

  每帧丢帧时间(ms)：max（【Waiting for Present Fence实际时长(ms)】- 【每帧时长(ms)】 \* 1.5 , 0）；即每帧耗时大于标准耗时1.5倍时则判定为丢帧。

## 计算逻辑

卡顿率(即流畅度) = 【每帧丢帧时间累计总和(ms)】/ 总时长(s)，须小于等于5ms/s。
