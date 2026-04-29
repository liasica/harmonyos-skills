---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-ellipse
title: ellipse
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > svg组件 > ellipse
category: harmonyos-references
scraped_at: 2026-04-29T13:53:37+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:0898bf9d670b0946e77b0da1b6330b836030dabf7dbceff8814f7ed17467d3b1
---

说明

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

椭圆形状。

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
| cx | <length>|<percentage> | 0 | 否 | 设置椭圆的x轴坐标。支持属性动画。 |
| cy | <length>|<percentage> | 0 | 否 | 设置椭圆的y轴坐标。支持属性动画。 |
| rx | <length>|<percentage> | 0 | 否 | 设置椭圆x轴的半径。支持属性动画。 |
| ry | <length>|<percentage> | 0 | 否 | 设置椭圆y轴的半径。支持属性动画。 |

## 示例

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <svg fill="white" width="400" height="400">
4. <ellipse cx="60" cy="200" rx="50" ry="100" stroke-width="4" fill="red" stroke="blue"></ellipse>
5. <ellipse cx="220" cy="200" rx="100" ry="50" stroke-width="5" stroke="red" stroke-dasharray="10 5" stroke-dashoffset="3"></ellipse>
6. </svg>
7. </div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/ZZ125QFuTeKIzaWh_p2N-A/zh-cn_image_0000002558766768.png?HW-CC-KV=V1&HW-CC-Date=20260429T055336Z&HW-CC-Expire=86400&HW-CC-Sign=50D428F116DC7F76588777CF9A23DD3D38093671DD0536117493155182BBCA65)
