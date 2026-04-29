---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-data-overview
title: 数据开放总览
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > 数据开放总览
category: harmonyos-guides
scraped_at: 2026-04-29T13:38:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:aa8b63b6a51f19efecc14005df6dd5122250197b7671f5fd3a0ce187019d1f5e
---

当前提供如下Health Service Kit数据，开发者可申请对应数据权限进行应用开发。开放等级中，![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/S2orkmqgRX-O2XEjg_bH5g/zh-cn_image_0000002589325277.png?HW-CC-KV=V1&HW-CC-Date=20260429T053817Z&HW-CC-Expire=86400&HW-CC-Sign=DC9CA5A18B11F2ED2842A34C4DA901164E8C03D3B8344476C9DED4AD16D06E7C)表示该数据权限为高阶数据，暂不对个人开发者开放。如需使用，请使用企业账号重新注册并申请权限；![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/cDv0O7_bQvOQGx1-C7rICg/zh-cn_image_0000002589245213.png?HW-CC-KV=V1&HW-CC-Date=20260429T053817Z&HW-CC-Expire=86400&HW-CC-Sign=CBCC4CA2FEBD778C9CEEF289CB6F33521119940AC2D206690CA41B84D9A4F993)表示该数据权限为基础数据，个人及企业开发者均可申请查询/使用。

说明

* 数据及时性体验依赖用户使用方式，若穿戴设备未连接至手机蓝牙、华为运动健康App未设置后台保活等情况下，将无法保证数据及时性体验。开发者需考虑数据及时性体验各类极端情况，综合判断合适的数据使用场景，确保给用户提供的产品/服务的稳定性，保证用户体验。
* 相关数据类型对应权限参考[权限说明](health-permission-description.md)。

**表1** **采样数据**

| 数据子类 | 数据项 | 开放等级 | 数据及时性 | 支持读 | 支持写 |
| --- | --- | --- | --- | --- | --- |
| [日常活动](health-daily-activities.md) | 步数、热量、距离等日常活动数据 |  | 小时级 | Y | Y |
| [心率](health-heart-rate.md) | 动态心率、静息心率、心率变异性 |  | 小时级 | Y | Y |
| [血氧](health-blood-oxygen.md) | 瞬时血氧饱和度 |  | 小时级 | Y | Y |
| [压力](health-pressure.md) | 压力得分 |  | 小时级 | Y | Y |
| [体温](health-body-temperature.md) | 体温、皮肤体温 |  | 分钟级 | Y | Y |
| [血压](health-blood-pressure.md) | 收缩压、舒张压、脉搏等 |  | 分钟级 | Y | Y |
| [体重](health-weight.md) | 体重、体脂、BMI等 |  | 分钟级 | Y | Y |
| [身高](health-height.md) | 身高 |  | 分钟级 | Y | Y |
| [情绪](health-emotion.md) | 情绪数据 |  | 小时级 | Y | Y |

**表2** **健康记录和锻炼记录**

| 数据子类 | 数据项 | 开放等级 | 数据及时性 | 支持读 | 支持写 |
| --- | --- | --- | --- | --- | --- |
| [睡眠](health-sleeprecord.md) | 睡眠分期采样数据、睡眠记录 |  | 分钟级 | Y | Y |
| [锻炼记录数据](health-exercisesequence-summary.md) | 跑步、骑行、健走、跳绳、跑步机等运动和健身类型 |  | 分钟级 | Y | Y |
