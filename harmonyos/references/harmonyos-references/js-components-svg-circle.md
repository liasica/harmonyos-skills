---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-circle
title: circle
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > svg组件 > circle
category: harmonyos-references
scraped_at: 2026-11-21T09:14:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:faba77bf66e1e3340bb9df3d25b6616aaacaa49c5903dc88b1a73772560ff7c2
---

**说明** 

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

圆形形状。

## 权限列表

无

## 子组件

支持[animate](js-components-svg-animate.md)、[animateMotion](js-components-svg-animatemotion.md)、[animateTransform](js-components-svg-animatetransform.md)。

## 属性

支持Svg组件[通用属性](js-components-svg-common-attributes.md)和以下属性。

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| id | string | - | 否 | 组件的唯一标识。 |
| cx | <length>|<percentage> | 0 | 否 | 设置圆心的x轴坐标。支持属性动画。 |
| cy | <length>|<percentage> | 0 | 否 | 设置圆心的y轴坐标。支持属性动画。 |
| r | <length>|<percentage> | 0 | 否 | 设置圆的半径。支持属性动画。 |

## 示例

```html
<!-- xxx.hml -->
<div class="container">
  <svg fill="white" width="400" height="400">
    <circle cx="60" cy="200" r="50" stroke-width="4" fill="red" stroke="blue"></circle>
    <circle cx="180" cy="200" r="50" stroke-width="10" stroke="red" stroke-dasharray="10 5" stroke-dashoffset="3"></circle>
  </svg>
</div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/mLJJlzy7Sxaswtckowdj5A/zh-cn_image_0000002792879546.png?HW-CC-KV=V1&HW-CC-Date=20261121T011423Z&HW-CC-Expire=31536000000&HW-CC-Sign=A9BCD182D679A6E12ACE02082E6347B4A4C31778F8F4D8E7FA318A4D3E6DC1DC)
