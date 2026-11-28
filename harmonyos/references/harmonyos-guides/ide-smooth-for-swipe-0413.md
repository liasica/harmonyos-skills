---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-smooth-for-swipe-0413
title: 滑动过程流畅
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 附录 > 体检规则 > 滑动过程流畅
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:41+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:aaa991409b827e8a0500fb2bbe90132479e425ab9e378c8f76f6899307657f2e
---

## 规则详情

应用的滑动过程卡顿率≤5ms/s；满帧30FPS的游戏类、地图类和视频类的应用帧率应≥29FPS。

## 检测逻辑

* 开始时间：以APP\_LIST\_FLING滑动泳道为例，泳道的起点（如图标记1）。
* 结束时间：以APP\_LIST\_FLING滑动泳道为例，泳道的终点（如图标记2）。

  其他滑动泳道标记如下：

  H:APP\_SWIPER\_SCROLL

  H:WEB\_LIST\_FLING

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/Toda453HTAe7RiT00qFEPA/zh-cn_image_0000002779406434.png?HW-CC-KV=V1&HW-CC-Date=20261128T023440Z&HW-CC-Expire=31536000000&HW-CC-Sign=EC5BE28B293C16E5611EB14767788B983D93430603002679DEB5ACDE80D0F183)

* 查找滑动泳道：H:APP\_LIST\_FLING，如果是web页面，找H:WEB\_LIST\_FLING。
* 刷新率：查找关键词H:RSHardwareThread::CommitAndReleaseLayers rate，如下图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/BMGfX2gDRXeLQHNPusqflA/zh-cn_image_0000002779566412.png?HW-CC-KV=V1&HW-CC-Date=20261128T023440Z&HW-CC-Expire=31536000000&HW-CC-Sign=FD46FFDA743854C9274442CAC18B84EC1A6E21914CE9A39A589A244CB8EF97AB)
* 每帧标准时长(ms)：1000ms/刷新率。

  总时长(s)：在以上泳道时间范围内，总时长 =【最后一个“H:Waiting for Present Fence xxxx” 时间（如图标记2）】 - 【第一个“H:Waiting for Present Fence xxxx” 时间（如图标记1）】。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/U8pV753yQqKrbk4ndMqAIA/zh-cn_image_0000002779566408.png?HW-CC-KV=V1&HW-CC-Date=20261128T023440Z&HW-CC-Expire=31536000000&HW-CC-Sign=F50E3AFDC857DCFC443718BB7DBED384D01DBA076ADE532B6EBB289FC239C3A7)
* 实际每帧时长：【下一个H:Waiting for Present Fence xxxx的起始时间（如图标记2）】 - 【当前H:Waiting for Present Fence xxxx的起始时间（如图标记1）】。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/yl02sbfXQV-_YICL0qmudQ/zh-cn_image_0000002779406430.png?HW-CC-KV=V1&HW-CC-Date=20261128T023440Z&HW-CC-Expire=31536000000&HW-CC-Sign=8CE9130E00F7192321D1A0A530D477B8EFFBA1BFBD265B8A5350041526841371)

  每帧丢帧时间(ms)：max（【Waiting for Present Fence实际时长(ms)】- 【每帧时长(ms)】 \* 1.5 , 0）；即每帧耗时大于标准耗时1.5倍时则判定为丢帧。

## 计算逻辑

卡顿率(即流畅度) = 【每帧丢帧时间累计总和(ms)】/ 总时长(s)，须小于等于5ms/s。
