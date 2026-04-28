---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-animate
title: animate
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > svg组件 > animate
category: harmonyos-references
scraped_at: 2026-04-28T08:03:18+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:0bb3ccdc56c70c65b413dbbde45369839db3011063478ad2e5667f58e26991c2
---

说明

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

设置svg组件的属性动画。

## 权限列表

PhonePC/2in1TabletTVWearable

无

## 子组件

PhonePC/2in1TabletTVWearable

不支持。

## 属性

PhonePC/2in1TabletTVWearable

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| id | string | - | 否 | 组件的唯一标识。 |
| attributeName | string | - | 否 | 设置需要进行动效的属性名。 |
| begin | <time> | 0 | 否 | 设置动效的延迟时间。  支持输入ms(毫秒)、s（秒）、m（分），默认为s(秒)，其他格式不支持。 |
| dur | <time> | 0 | 否 | 设置动效持续时间，如果dur没设置，按照end-begin的结果作为持续时间，小于等于0时，动效不触发。  支持输入ms(毫秒)、s（秒）、m（分），默认为s(秒)，其他格式不支持。 |
| end | <time> | 0 | 否 | 设置动效多久时间后结束。支持输入ms(毫秒)、s（秒）、m（分），默认为s(秒)，其他格式不支持。 |
| repeatCount | <number | indefinite> | 1 | 否 | 设置动画播放的次数，默认无限次播放(indefinite)，可通过设置为数值1仅播放一次。 |
| fill | <freeze | remove> | remove | 否 | 设置动画结束时的状态。 |
| calcMode | <discrete | linear | paced | spline> | linear | 否 | 设置动画的插值模式。  discrete：阶跃，from值直接跳转到to的值；  linear：线性；  paced：线性，设置此项后keyTimes和keyPoints值无效；  spline：自定义贝塞尔曲线，spline点定义在keyTimes属性中，每个时间间隔控制点由keySplines定义。 |
| keyTimes | string | - | 否 | 设置关键帧动画的开始时间，值为0~1之间的数值用分号隔开，比如0;0.3;0.8;1。keyTimes、keySplines、values组合设置关键帧动画。keyTimes和values的个数保持一致。keySplines个数为keyTimes个数减一。 |
| keySplines | string | - | 否 | 与keyTimes相关联的一组贝塞尔控制点。定义每个关键帧的贝塞尔曲线，曲线之间用分号隔开。曲线内的两个控制点格式为x1 y1 x2 y2。比如0.5 0 0.5 1; 0.5 0 0.5 1;0.5 0 0.5 1 |
| by | number | - | 否 | 在动画中对某一指定属性，添加相对偏移值，from默认为原属性值。 |
| from | string | - | 否 | 设置需要进行动画的属性的开始值。  如果已经设置了values属性，则from失效。 |
| to | string | - | 否 | 设置需要进行动画的属性的结束值。  如果已经设置了values属性，则to都失效。 |
| values | string | - | 否 | 设置一组动画的变化值。格式为value1;value2;value3。 |

## 示例

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <svg width="400" height="400">
4. <rect x="20" y="20" width="100" height="100" fill="red" rx="0" ry="20">
5. <animate attributeName="rx" values="0;10;30;0" keyTimes="0;0.25;0.75;1" keySplines="0.5 0 0.5 1; 0.5 0 0.5 1; 0.5 0 0.5 1" dur="1000" repeatCount="indefinite">
6. </animate>
7. </rect>
8. </svg>
9. </div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/FxwoMTUWToKtS5HNIOZtwg/zh-cn_image_0000002583480253.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000316Z&HW-CC-Expire=86400&HW-CC-Sign=67A6A05ADBFE574A23F7AE440C44B00C12666958A975EAAA12A07D79BD11D679)

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <svg width="400" height="400">
4. <rect x="20" y="20" width="100" height="100" fill="red" rx="0" ry="20">
5. <animate attributeName="fill" from="red" to="blue" dur="1000" repeatCount="indefinite"></animate>
6. <animate attributeName="height" from="50" to="150" begin="500" end="1000" repeatCount="indefinite">  </animate>
7. </rect>
8. </svg>
9. </div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/pPuRMWfISpmRtLdP0B5oaA/zh-cn_image_0000002552800604.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000316Z&HW-CC-Expire=86400&HW-CC-Sign=ACAD4CE55F0F1ABDE067EB49985A41FEA7A5B0186085D693C42C940C583A27E7)

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <svg width="400" height="400">
4. <rect x="20" y="20" width="100" height="100" fill="red" rx="0" ry="20">
5. <animate attributeName="rx" values="0;30" dur="1000" repeatCount="indefinite" fill="freeze" calcMode="linear"></animate>
6. </rect>
7. </svg>
8. </div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/p-_WWSMnTBC6vjMau7gHUQ/zh-cn_image_0000002583440299.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000316Z&HW-CC-Expire=86400&HW-CC-Sign=E18A7F42F5EC51A75756238CC423D9BBF86661D421FED7D822C18FA4563CC0EB)

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <svg fill="white" width="600" height="600">
4. <circle cx="60" cy="70" r="50" stroke-width="4" fill="white" stroke="blue">
5. <animate attributeName="r" from="0" to="50" dur="2000" repeatCount="indefinite"></animate>
6. <animate attributeName="cx" from="60" to="200" dur="2000" repeatCount="indefinite"></animate>
7. </circle>
8. <circle cx="60" cy="200" r="50" stroke-width="4" fill="white" stroke="blue">
9. <animate attributeName="stroke-width" from="4" to="10" calcMode="discrete" dur="2000" repeatCount="indefinite"></animate>
10. <animate attributeName="stroke" values="red;blue" dur="2000" repeatCount="indefinite"></animate>
11. </circle>
12. <circle cx="180" cy="200" r="50" stroke-width="10" stroke="red" stroke-dasharray="60 10" stroke-dashoffset="3">
13. <animate attributeName="stroke-opacity" from="1.0" to="0.5" dur="2000" repeatCount="indefinite"></animate>
14. <animate attributeName="stroke-dashoffset" values="30;0;30" dur="500" repeatCount="indefinite"></animate>
15. <animate attributeName="cx" from="180" to="400" dur="2000" repeatCount="indefinite"></animate>
16. </circle>
17. <circle cx="180" cy="200" r="5" fill="blue">
18. <animate attributeName="cx" from="180" to="400" dur="2000" repeatCount="indefinite"></animate>
19. </circle>
20. <circle cx="60" cy="380" r="50"  fill="blue">
21. <animate attributeName="fill" values="red;blue" dur="2000" repeatCount="indefinite"></animate>
22. </circle>
23. <circle cx="180" cy="380" r="50"  fill="blue">
24. <animate attributeName="fill-opacity" from="1.0" to="0.5" dur="2000" repeatCount="indefinite"></animate>
25. </circle>
26. </svg>
27. </div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/1DVVncDCRhOi37UJMxrAsg/zh-cn_image_0000002552960254.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000316Z&HW-CC-Expire=86400&HW-CC-Sign=0DFAAC936F3495F90F286BC42AC4E74D82CFC083DB665A08104ABCB9283A6CA6)
