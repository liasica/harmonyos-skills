---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-polygon
title: polygon
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > svg组件 > polygon
category: harmonyos-references
scraped_at: 2026-04-28T08:03:17+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:82312c5da2194d65e938ba0aaa14a41967b83cd310992794c498cb6928f49f93
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/yxEYNnkAQ6ePB7nTvADhrg/zh-cn_image_0000002583440289.png?HW-CC-KV=V1&HW-CC-Date=20260428T000316Z&HW-CC-Expire=86400&HW-CC-Sign=AE062E886E2E9B72A325FF7015AE2321D6F004160E313BC310CAA2ED1770C543)
