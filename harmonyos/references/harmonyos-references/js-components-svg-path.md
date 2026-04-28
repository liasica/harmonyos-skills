---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-path
title: path
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > svg组件 > path
category: harmonyos-references
scraped_at: 2026-04-28T08:03:16+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b72dc9e4ba5ba870065b2aeef753ace9f4ec6dd42b0a9b0569281a04303f4e9c
---

说明

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

绘制路径。

## 权限列表

PhonePC/2in1TabletTVWearable

无

## 子组件

PhonePC/2in1TabletTVWearable

支持[animate](js-components-svg-animate.md)、[animateMotion](js-components-svg-animatemotion.md)、[animateTransform](js-components-svg-animatetransform.md)。

## 属性

PhonePC/2in1TabletTVWearable

支持Svg组件[通用属性](js-components-svg-common-attributes.md)和以下属性，设置的通用属性会传递给子组件。

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| id | string | - | 否 | 组件的唯一标识。 |
| d | string | - | 否 | 设置路径的形状。包含一组字符指令，大写字母为绝对路径，小写字符为相对路径。  字母指令表示的意义如下：  - M/m = moveto  - L/l = lineto  - H/h = horizontal lineto  - V/v = vertical lineto  - C/c = curveto  - S/s = smooth curveto  - Q/q = quadratic Bezier curve  - T/t = smooth quadratic Bezier curveto  - A/a = elliptical Arc  - Z/z = closepath |

## 示例

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <svg width="400" height="400">
4. <path d="M 10,30 A 20,20 0,0,1 50,30 A 20,20 0,0,1 90,30 Q 90,60 50,90 Q 10,60 10,30 z"
5. stroke="blue" stroke-width="3" fill="red">
6. </path>
7. </svg>
8. </div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/wBUb9KIiSMGyQjVUpZveRg/zh-cn_image_0000002552960242.png?HW-CC-KV=V1&HW-CC-Date=20260428T000315Z&HW-CC-Expire=86400&HW-CC-Sign=843C3CF3A8710275611EE6BC09C9D5D392249D34727487DE65483F7962A6B2C5)
