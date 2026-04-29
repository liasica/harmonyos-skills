---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-polygon
title: polygon
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > svg组件 > polygon
category: harmonyos-references
scraped_at: 2026-04-29T13:53:37+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:23431ff178023f8cb311da8ffa8c86e172cc2033c21b007794172e81843207c3
---

说明

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

绘制多边形。

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
| points | string | - | 否 | 设置多边形的多个坐标点。  格式为[x1,y1 x2,y2 x3,y3]。  支持属性动画，如果属性动画里设置的动效变化值的坐标个数与原始points的格式不一样，则无效。 |

## 示例

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <svg fill="white" stroke="blue" width="400" height="400">
4. <polygon points="10,110 60,35 60,85 110,10" fill="red"></polygon>
5. <polygon points="10,200 60,125 60,175 110,100" stroke-dasharray="10 5" stroke-dashoffset="3"></polygon>
6. </svg>
7. </div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/hsTqt3zLTIy18qAaqN5LNw/zh-cn_image_0000002558766770.png?HW-CC-KV=V1&HW-CC-Date=20260429T055336Z&HW-CC-Expire=86400&HW-CC-Sign=47DFC85E48331142226E504590E3A25F233B9E00D1CE1A1986A0EE24C13ABE0A)
