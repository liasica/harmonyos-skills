---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-smooth-for-swipe-0413
title: 滑动过程流畅
breadcrumb: 指南 > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 附录 > 体检规则 > 滑动过程流畅
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b34ee790fc92d4acb884c8f856076ed7866b69e1feddd4e2ab72e5308bea2e13
---

## 规则详情

应用的滑动过程卡顿率≤ 5ms/s；满帧30FPS的游戏类、地图类和视频类的应用帧率应≥ 29FPS。

## 检测逻辑

* 开始时间：以APP\_LIST\_FLING滑动泳道为例，泳道的起点（如图标记1）。
* 结束时间：以APP\_LIST\_FLING滑动泳道为例，泳道的终点（如图标记2）。

  其他滑动泳道标记如下：

  H:APP\_SWIPER\_SCROLL

  H:WEB\_LIST\_FLING

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/jptDY9qzQ62bwEM5fDRm-w/zh-cn_image_0000002561752629.png?HW-CC-KV=V1&HW-CC-Date=20260427T235704Z&HW-CC-Expire=86400&HW-CC-Sign=D060AE354822AD13A38570F815365D3AE348028F68C4097618B699F7EDDE117F)

* 查找滑动泳道：H:APP\_LIST\_FLING，如果是web页面，找H:WEB\_LIST\_FLING。
* 刷新率：查找关键词H:RSHardwareThread::CommitAndReleaseLayers rate，如下图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/FLGAvs52RnealWyhO3IvTg/zh-cn_image_0000002530912686.png?HW-CC-KV=V1&HW-CC-Date=20260427T235704Z&HW-CC-Expire=86400&HW-CC-Sign=07594A7D067A3C5197867C0790CD50BF424B34AF8712340C536FEC874707856C)
* 每帧标准时长(ms)：1000ms/刷新率。

  总时长(s)：在以上泳道时间范围内，总时长 =【最后一个“H:Waiting for Present Fence xxxx” 时间（如图标记2）】 - 【第一个“H:Waiting for Present Fence xxxx” 时间（如图标记1）】。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/RX_nk9b8Sh6Ctw-rnfADrw/zh-cn_image_0000002561832607.png?HW-CC-KV=V1&HW-CC-Date=20260427T235704Z&HW-CC-Expire=86400&HW-CC-Sign=9253730061BD939136F2CD48302516C0BA2D26F01ACC6E7F20B5446C0B2DCF8D)
* 实际每帧时长：【下一个H:Waiting for Present Fence xxxx的起始时间（如图标记2）】 - 【当前H:Waiting for Present Fence xxxx的起始时间（如图标记1）】。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/eRox86epQduszNuLog15WA/zh-cn_image_0000002530752684.png?HW-CC-KV=V1&HW-CC-Date=20260427T235704Z&HW-CC-Expire=86400&HW-CC-Sign=70737A44E1A9CB81D800F76985DAC777DCCAC7BCEEADB050594477BD1979C101)

  每帧丢帧时间(ms)：max（【Waiting for Present Fence实际时长(ms)】- 【每帧时长(ms)】 \* 1.5 , 0）；即每帧耗时大于标准耗时1.5倍时则判定为丢帧。

## 计算逻辑

卡顿率(即流畅度) = 【每帧丢帧时间累计总和(ms)】/ 总时长(s)，须小于等于5ms/s。
