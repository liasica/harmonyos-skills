---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-local-rec-scene-experience
title: 场景体验
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 位置推荐方案 > 场景体验
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:019c7e8cc13d6e415a9f234dd90d9690e4d2ef0a644901026fce3a9632f303be
---

## 典型场景

华为意图框架位置感知推荐能力主要支持室内位置推荐、室外近场位置推荐、跨域位置推荐等高确定性场景，结合华为智慧决策能力，在小艺建议入口推荐更贴心、更及时、更满足用户诉求的场景卡片。场景示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/Uf81aY4GTlmu82A3QwoPvg/zh-cn_image_0000002552799668.png?HW-CC-KV=V1&HW-CC-Date=20260427T235333Z&HW-CC-Expire=86400&HW-CC-Sign=C4501968504DC974E8A6EA039E1DCEF18D377CA4236B5C997E819F11EB224324)

| 推荐类型 | 能力概述 | 适用场景 |
| --- | --- | --- |
| 室内位置推荐 | 基于：  - WLAN指纹识别  - 基站Cell信息定位  - Beacon定位  用户进入店内、场馆内触发围栏感知，可实现室内精准定位感知能力。 | 适用于室内多楼层、小范围高精度定位场景，如美食门店、博物馆、体育馆、医院科室、银行、政务大厅、地铁站等。 |
| 室外近场位置推荐 | 基于：  - POI多边形围栏  - POI点+半径  - Beacon定位  用户到达指定位置附近或进入区域范围后触发围栏感知。 | 适用于室外区域范围定位分发场景，如商圈、景区、医院、机场、火车站、加油站、停车场等。 |
| 跨域位置推荐 | 主要基于城市、国家级别围栏触发感知，用户跨城、出境触发围栏感知，可实现跨域定位感知能力。 | 适用于跨城、出境定位场景，如到新城市推旅游攻略场景。 |

## 卡片展示效果

基于POI（Point of interest）和Beacon（蓝牙信标设备）触发的位置推荐场景，由近场服务提供模板卡片的配置入口，开发者开通近场服务权限后自行配置。卡片的尺寸样式可参考：[近场服务-POI接入小艺建议场景-创建全网态服务-创建全网态服务](../app/agc-help-xiaoyi-create-formalstate-service-0000002349016144.md)

基于WLAN指纹和Cell触发的位置推荐场景，意图框架提供标准的卡片模板。卡片由华为侧统一配置。

**卡片模板参考：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/k6DGV4yKTwCKisPQJ8wvUg/zh-cn_image_0000002583439363.png?HW-CC-KV=V1&HW-CC-Date=20260427T235333Z&HW-CC-Expire=86400&HW-CC-Sign=96C28F4D3373CDCC07B19CB23E40E553D0C5247587BC611E3E191096B399878D)
