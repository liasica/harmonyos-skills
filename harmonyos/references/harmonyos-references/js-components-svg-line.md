---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-line
title: line
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > svg组件 > line
category: harmonyos-references
scraped_at: 2026-04-29T13:53:37+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5bd5563459d553d3362d274b7372783e3ed0f65e441f8dea7feae89cb5a2a2c8
---

说明

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

绘制线条。

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
| x1 | <length>|<percentage> | - | 否 | 设置线条起点的x轴坐标。支持属性动画。 |
| y1 | <length>|<percentage> | - | 否 | 设置线条起点的y轴坐标。支持属性动画。 |
| x2 | <length>|<percentage> | - | 否 | 设置线条终点的x轴坐标。支持属性动画。 |
| y2 | <length>|<percentage> | - | 否 | 设置线条终点的y轴坐标。支持属性动画。 |

## 示例

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <svg width="400" height="400">
4. <line x1="10" x2="300" y1="50" y2="50" stroke-width="4" fill="white" stroke="blue"></line>
5. <line x1="10" x2="300" y1="100" y2="100" stroke-width="4" fill="white" stroke="blue"></line>
6. <line x1="10" x2="300" y1="150" y2="150" stroke-width="10" stroke="red" stroke-dasharray="5 3"
7. stroke-dashoffset="3"></line>
8. <!--round：在路径的末端延伸半个圆，直径等于线宽-->
9. <line x1="10" x2="300" y1="200" y2="200" stroke-width="10" stroke="black" stroke-linecap="round"></line>
10. <!--butt：不在路径两端扩展-->
11. <line x1="10" x2="300" y1="220" y2="220" stroke-width="10" stroke="black" stroke-linecap="butt"></line>
12. <!-- square：在路径的末端延伸一个矩形，宽度等于线宽的一半，高度等于线宽 -->
13. <line x1="10" x2="300" y1="240" y2="240" stroke-width="10" stroke="black" stroke-linecap="square"></line>
14. </svg>
15. </div>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/cnCeVJ1CTICZLO1LhZR_RA/zh-cn_image_0000002589326635.png?HW-CC-KV=V1&HW-CC-Date=20260429T055336Z&HW-CC-Expire=86400&HW-CC-Sign=03EDA40DB2E3816AC1DE5F4FB3486E76A8F7EDF2F7E29834239BD3F9BED404B4)
