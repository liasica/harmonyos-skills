---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-rect
title: rect
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > svg组件 > rect
category: harmonyos-references
scraped_at: 2026-04-28T08:03:15+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:6840cc407e74ae877cef378b8b126dce1985623df63a15e458033a194011e8f5
---

说明

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

用于绘制矩形、圆角矩形。

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
| width | <length>|<percentage> | 0 | 否 | 设置矩形的宽度。支持属性动画。 |
| height | <length>|<percentage> | 0 | 否 | 设置矩形的高度。支持属性动画。 |
| x | <length>|<percentage> | 0 | 否 | 设置矩形左上角x轴坐标。支持属性动画。 |
| y | <length>|<percentage> | 0 | 否 | 设置矩形左上角y轴坐标。支持属性动画。 |
| rx | <length>|<percentage> | 0 | 否 | 设置矩形圆角x方向半径。支持属性动画。 |
| ry | <length>|<percentage> | 0 | 否 | 设置矩形圆角y方向半径。支持属性动画。 |

## 示例

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <svg fill="white" width="400" height="400">
4. <rect width="100" height="100" x="10" y="20" stroke-width="4" stroke="blue" id="rectId"></rect>
5. <rect width="100" height="100" x="150" y="20" stroke-width="4" stroke="blue" rx="10" ry="10"></rect>
6. <rect width="100" height="100" x="10" y="130" stroke-width="10" fill="red" stroke="blue" rx="10" ry="10"></rect>
7. <rect width="100" height="100" x="150" y="130" stroke-width="10" stroke="red" rx="10" ry="10" stroke-dasharray="5 3" stroke-dashoffset="3"></rect>
8. <rect width="100" height="100" x="20" y="270" stroke-width="4" stroke="blue" transform="rotate(-10)"></rect>
9. </svg>
10. </div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/ifSTBtAnRM-ObKIrrcYDfg/zh-cn_image_0000002583480241.png?HW-CC-KV=V1&HW-CC-Date=20260428T000314Z&HW-CC-Expire=86400&HW-CC-Sign=0111B2E072E7EFC2D9708412ACF36C85EB8411C71733796448D167A7F0CC33DD)
