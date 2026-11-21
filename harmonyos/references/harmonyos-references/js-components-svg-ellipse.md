---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-ellipse
title: ellipse
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > svg组件 > ellipse
category: harmonyos-references
scraped_at: 2026-11-21T09:14:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f16955b726c478e69d31eac65cba79c9418acebb0e3bcef7de579640dc3d8cb6
---

**说明** 

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

椭圆形状。

## 权限列表

无

## 子组件

支持[animate](js-components-svg-animate.md)、[animateMotion](js-components-svg-animatemotion.md)、[animateTransform](js-components-svg-animatetransform.md)。

## 属性

支持Svg组件[通用属性](js-components-svg-common-attributes.md)和以下属性。

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| id | string | - | 否 | 组件的唯一标识。 |
| cx | <length>|<percentage> | 0 | 否 | 设置椭圆中心的x轴坐标。支持属性动画。 |
| cy | <length>|<percentage> | 0 | 否 | 设置椭圆中心的y轴坐标。支持属性动画。 |
| rx | <length>|<percentage> | 0 | 否 | 设置椭圆x轴的半径。支持属性动画。 |
| ry | <length>|<percentage> | 0 | 否 | 设置椭圆y轴的半径。支持属性动画。 |

## 示例

```html
<!-- xxx.hml -->
<div class="container">
  <svg fill="white" width="400" height="400">
    <ellipse cx="60" cy="200" rx="50" ry="100" stroke-width="4" fill="red" stroke="blue"></ellipse>
    <ellipse cx="220" cy="200" rx="100" ry="50" stroke-width="5" stroke="red" stroke-dasharray="10 5" stroke-dashoffset="3"></ellipse>
  </svg>
</div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/YK_LoIvISS6z-Q_tLOv1bA/zh-cn_image_0000002821839453.png?HW-CC-KV=V1&HW-CC-Date=20261121T011321Z&HW-CC-Expire=31536000000&HW-CC-Sign=6210FF6CF2AF0AE8EE3ADDDB31189ADA4151EB1896F7D0E3C46884D1634DC83E)
