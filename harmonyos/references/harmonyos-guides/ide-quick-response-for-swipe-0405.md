---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-quick-response-for-swipe-0405
title: 滑动操作响应快
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 附录 > 体检规则 > 滑动操作响应快
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:32+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:c9a206fa7df63867501af86eba715b81a51444d593431b6e3e59e0428d31f831
---

## 规则详情

应用内滑动操作响应时延应≤80ms；时间起点：手指滑动；时间终点：界面发生变化。

## 检测逻辑

* 开始时间：滑动开始点，Y坐标开始变化的第一个点，如图标记1；关键字：H:DispatchTouchEvent，其中type=2。
* 结束时间：滑动泳道H:APP\_LIST\_FLING的开始点，如图标记2。

  如图展示的是H:APP\_LIST\_FLING泳道，其他滑动类泳道标记如下：

  H:APP\_SWIPER\_SCROLL

  H:APP\_TABS\_SCROLL

  H:WEB\_LIST\_FLING
* 备注：由于trace的响应时延小于用户实际感知的时延，所以目前滑动类算法会补偿30ms。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/FBP4iIHkRJG7RrApL7d7yw/zh-cn_image_0000002808886905.png?HW-CC-KV=V1&HW-CC-Date=20261124T044232Z&HW-CC-Expire=31536000000&HW-CC-Sign=138F29D18A6F745F90008089AD30D4A4A6199C5A44DB8704CB900D7EECAFFA38)

## 计算逻辑

时延=结束时间-开始时间，小于等于80ms。
