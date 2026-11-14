---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-polyline
title: polyline
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > svg组件 > polyline
category: harmonyos-references
scraped_at: 2026-11-14T08:50:32+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a5914d20f3234666511853827fd3fcabdebb891ebd0490dc138b8e483203bc5b
---

**说明** 

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

绘制折线。

## 权限列表

无

## 子组件

支持[animate](js-components-svg-animate.md)、[animateMotion](js-components-svg-animatemotion.md)、[animateTransform](js-components-svg-animatetransform.md)。

## 属性

支持Svg组件[通用属性](js-components-svg-common-attributes.md)和以下属性。

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| id | string | - | 否 | 组件的唯一标识。 |
| points | string | - | 否 | 设置折线的多个坐标点。  格式为[x1,y1 x2,y2 x3,y3]。  支持属性动画，如果属性动画里设置的动效变化值的坐标个数与原始points的格式不一样，则无效。 |

## 示例

```html
<!-- xxx.hml -->
<div class="container">
  <svg fill="white" stroke="blue" width="400" height="400">
    <polyline points="10,110 60,35 60,85 110,10" fill="red"></polyline>
    <polyline points="10,200 60,125 60,175 110,100" stroke-dasharray="10 5" stroke-dashoffset="3"></polyline>
  </svg>
</div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/HxzZ6L0UQ5qIjg-Fsvmvig/zh-cn_image_0000002817428899.png?HW-CC-KV=V1&HW-CC-Date=20261114T004829Z&HW-CC-Expire=31536000000&HW-CC-Sign=9545FAD8107714F7F74A8B001FB36D876CCFF1597FEC00D6F93AD38C458D4E96)
