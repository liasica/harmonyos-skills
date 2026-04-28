---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-quick-response-for-swipe-0405
title: 滑动操作响应快
breadcrumb: 指南 > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 附录 > 体检规则 > 滑动操作响应快
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3b355657ff97f7efb2a9d6d978ee70919533999a980f637bdaf6ca11061d8d30
---

## 规则详情

应用内滑动操作响应时延应≤ 80毫秒；时间起点：手指滑动；时间终点：界面发生变化。

## 检测逻辑

* 开始时间：滑动开始点，Y坐标开始变化的第一个点，如图标记1；关键字：H:DispatchTouchEvent，其中type=2。
* 结束时间：滑动泳道H:APP\_LIST\_FLING的开始点，如图标记2。

  如图展示的是H:APP\_LIST\_FLING泳道，其他滑动类泳道标记如下：

  H:APP\_SWIPER\_SCROLL

  H:APP\_TABS\_SCROLL

  H:WEB\_LIST\_FLING
* 备注：由于trace的响应时延小于用户实际感知的时延，所以目前滑动类算法会补偿30ms。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/3uSp0SOBSOK0hPk5LMhDYQ/zh-cn_image_0000002561833679.png?HW-CC-KV=V1&HW-CC-Date=20260427T235704Z&HW-CC-Expire=86400&HW-CC-Sign=3739CC4C30E70E47C27D1BCBAD801DE1AEA78079C75662FA98CE77AA6352FA5D)

## 计算逻辑

时延=结束时间-开始时间，小于等于80ms。
