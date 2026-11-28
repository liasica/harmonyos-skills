---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-quick-response-for-click-0403
title: 点击操作响应快
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 开发自测试 > 应用与元服务体检 > 附录 > 体检规则 > 点击操作响应快
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:40+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:978def579c37ec39c15ea0893f7cc3fcfbe22d0cbbef27a7181e63ce07f0ff66
---

## 规则详情

应用内点击操作响应时延应≤100ms；时间起点：点击离手；时间终点：界面发生变化。

## 检测逻辑

* 开始时间：点击离手，如图标记1；关键字：H:DispatchTouchEvent，其中type=1。
* 结束时间：泳道开始时间，如图标记2。

  如图展示的是H:ABILITY\_OR\_PAGE\_SWITCH泳道，其他转场泳道标记如下：

  H:APP\_TRANSITION\_FROM\_OTHER\_APP

  H:APP\_TRANSITION\_TO\_OTHER\_APP

  H:APP\_SWIPER\_NO\_ANIMATION\_SWITCH

  H:APP\_TABS\_NO\_ANIMATION\_SWITCH

  H:APP\_TABS\_FLING
* 备注：由于trace的响应时延小于用户实际感知的时延，所以目前点击类算法会补偿20ms。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/aoV37Fj_Rf2lIXxaLMfe9g/zh-cn_image_0000002779567046.png?HW-CC-KV=V1&HW-CC-Date=20261128T023440Z&HW-CC-Expire=31536000000&HW-CC-Sign=6B7E946875381B6729F242578B1991EAB083C7BAE48B66B396B99F204ED38654)

## 计算逻辑

时延=结束时间 - 开始时间，小于等于100ms。
