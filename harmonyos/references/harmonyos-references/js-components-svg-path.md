---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-path
title: path
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > svg组件 > path
category: harmonyos-references
scraped_at: 2026-09-05T06:17:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ab27718f8ef81bdd56a3f8a5e1961735639eda7fcc68f1531a7d47b188f46009
---

**说明** 

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

绘制路径。

## 权限列表

无

## 子组件

支持[animate](js-components-svg-animate.md)、[animateMotion](js-components-svg-animatemotion.md)、[animateTransform](js-components-svg-animatetransform.md)。

## 属性

支持Svg组件[通用属性](js-components-svg-common-attributes.md)和以下属性，设置的通用属性会传递给子组件。

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| id | string | - | 否 | 组件的唯一标识。 |
| d | string | - | 否 | 设置路径的形状。包含一组字符指令，大写字母为绝对路径，小写字符为相对路径。  字母指令表示的意义如下：  - M/m = moveto  - L/l = lineto  - H/h = horizontal lineto  - V/v = vertical lineto  - C/c = curveto  - S/s = smooth curveto  - Q/q = quadratic Bezier curve  - T/t = smooth quadratic Bezier curveto  - A/a = elliptical Arc  - Z/z = closepath |

## 示例

```html
<!-- xxx.hml -->
<div class="container">
    <svg width="400" height="400">
        <path d="M 10,30 A 20,20 0,0,1 50,30 A 20,20 0,0,1 90,30 Q 90,60 50,90 Q 10,60 10,30 z"
          stroke="blue" stroke-width="3" fill="red">
        </path>
    </svg>
</div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/K7HP7PRdQaSiZDZwD9QvKw/zh-cn_image_0000002712406704.png)
