---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-smooth-for-transition-0414
title: 转场操作流畅
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 附录 > 体检规则 > 转场操作流畅
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:01+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:1d2ae30ec7a6b0669af6616791130b306a09ed73046692139d09442c58bea5a0
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/r631iMtQRe2yU2CkLa8U5Q/zh-cn_image_0000002808766611.png?HW-CC-KV=V1&HW-CC-Date=20261114T004901Z&HW-CC-Expire=31536000000&HW-CC-Sign=8734A232CA42ED4DB122E13AE1B0EDCC1AF3E29E08316A74649B6ED4715DB1DB)

* 总时长(s)：【最后一个“H:Waiting for Present Fence xxxx” 时间（如图标记2）】 - 【第一个“H:Waiting for Present Fence xxxx” 时间（如图标记1）】。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/EZ58CkzRSTOb5hfrY2FNeg/zh-cn_image_0000002808886687.png?HW-CC-KV=V1&HW-CC-Date=20261114T004901Z&HW-CC-Expire=31536000000&HW-CC-Sign=A3E37A5BDC1874C0C1400FCD5AB679C51FB13DB035A19F31CB703AA1798C4F2B)

* 每帧时长(ms)：1000ms / 刷新率。
* 刷新率：在泳道范围内查找关键词H:RSHardwareThread::CommitAndReleaseLayers rate，如下图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/enuBfZrrQ9et_p_w6jvq4w/zh-cn_image_0000002779407048.png?HW-CC-KV=V1&HW-CC-Date=20261114T004901Z&HW-CC-Expire=31536000000&HW-CC-Sign=CB68C2AC29992B85BF742436D4C7711B23BCBFE9ACB870F6D8862B0A9489F558)

* 每帧渲染实际耗时(ms)：【下一个H:Waiting for Present Fence xxxx的起始时间】 - 【当前H:Waiting for Present Fence xxxx的起始时间】如下图 【标记2 - 标记1】。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/D_CYHXAzTN-KwGBi-rd-sg/zh-cn_image_0000002779407050.png?HW-CC-KV=V1&HW-CC-Date=20261114T004901Z&HW-CC-Expire=31536000000&HW-CC-Sign=08D2024F42C572DDC75C32D063403179C71081246133987C4AFF65584868A370)

* 每帧丢帧时间(ms)：max（【每帧渲染实际耗时(ms)】- 【每帧时长(ms)】 \* 1.5, 0）；即每帧耗时大于标准耗时1.5倍时则判定为丢帧。

## 计算逻辑

卡顿率=所有【每帧丢帧时间(ms)】/ 总时长(s)，卡顿率小于等于0ms/s。
