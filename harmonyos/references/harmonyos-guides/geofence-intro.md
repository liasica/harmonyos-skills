---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/geofence-intro
title: 地理围栏简介
breadcrumb: 指南 > 应用服务 > Location Kit（位置服务） > 地理围栏开发指导 > 地理围栏简介
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:87805196b7e372083bb89efcfd57c65f21881c77d42eb1b8d8e721e6101cd3ca
---

地理围栏（GeoFence）是一种基于地理位置的技术，它允许开发者设定特定的地理区域，在用户进入、离开或驻留在这个特定区域的时候，可以把该地理围栏事件（进入/离开/驻留）通知应用，应用在接收到这些事件时完成后面的业务逻辑，以达到提醒用户的目的。

HarmonyOS支持2种类型的地理围栏：端侧围栏和云侧围栏。端侧围栏是指由开发者来管理围栏的生命周期，比如创建围栏，删除围栏；云侧围栏是指开发者直接使用华为云侧的公共围栏。端侧围栏比较适合于开发者要使用自己的个性化围栏场景，云侧围栏比较适合于开发者要使用公共围栏的场景。
