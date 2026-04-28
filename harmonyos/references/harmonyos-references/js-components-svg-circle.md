---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-circle
title: circle
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > svg组件 > circle
category: harmonyos-references
scraped_at: 2026-04-28T08:03:15+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:0bb5eace45dad066662be4dd4103e13a3b170dd14939fe8b0e6a77592962f07f
---

说明

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

圆形形状。

## 权限列表

PhonePC/2in1TabletTVWearable

无

## 子组件

PhonePC/2in1TabletTVWearable

支持[animate](js-components-svg-animate.md)、[animateMotion](js-components-svg-animatemotion.md)、[animateTransform](js-components-svg-animatetransform.md)。

## 属性

PhonePC/2in1TabletTVWearable

支持Svg组件[通用属性](js-components-svg-common-attributes.md)和以下属性。

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| id | string | - | 否 | 组件的唯一标识。 |
| cx | <length>|<percentage> | 0 | 否 | 设置圆心的x轴坐标。支持属性动画。 |
| cy | <length>|<percentage> | 0 | 否 | 设置圆心的y轴坐标。支持属性动画。 |
| r | <length>|<percentage> | 0 | 否 | 设置圆的半径。支持属性动画。 |

## 示例

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <svg fill="white" width="400" height="400">
4. <circle cx="60" cy="200" r="50" stroke-width="4" fill="red" stroke="blue"></circle>
5. <circle cx="180" cy="200" r="50" stroke-width="10" stroke="red" stroke-dasharray="10 5" stroke-dashoffset="3"></circle>
6. </svg>
7. </div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/Y0UUGw_1Q5-3Gadi9oSW5w/zh-cn_image_0000002552800592.png?HW-CC-KV=V1&HW-CC-Date=20260428T000314Z&HW-CC-Expire=86400&HW-CC-Sign=9B4A50DC9490B3F88ECFA3651D7FBCCF160FFC6D67CBCB6B4D536906D7F2F9B4)
