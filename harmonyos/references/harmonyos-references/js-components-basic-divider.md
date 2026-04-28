---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-divider
title: divider
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Full） > 基础组件 > divider
category: harmonyos-references
scraped_at: 2026-04-28T08:03:00+08:00
doc_updated_at: 2026-03-30
content_hash: sha256:cdb7799be148e61f252e52da01224654683425c76a91a9bbf219fbc75fe34b88
---

说明

从API version 4开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

提供分隔器组件，分隔不同内容块/内容元素。可用于列表或界面布局。

## 权限列表

PhonePC/2in1TabletTVWearable

无

## 子组件

PhonePC/2in1TabletTVWearable

不支持。

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](js-components-common-attributes.md)外，还支持如下属性：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| vertical | boolean | false | 否 | 使用水平分割线还是垂直分割线，默认使用水平分割线。 |

说明

不支持focusable、disabled属性。

## 样式

PhonePC/2in1TabletTVWearable

仅支持如下样式：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| margin | <length> | 0 | 否 | 使用简写属性设置所有的外边距属性，该属性可以有1到4个值。 |
| margin-[left|top|right|bottom] | <length> | 0 | 否 | 使用简写属性设置左、上、右、下外边距属性，类型length，单位px，默认值0。 |
| color | <color> | #08000000 | 否 | 设置分割线颜色。 |
| stroke-width | <length> | 1 | 否 | 设置分割线宽度。 |
| display | string | flex | 否 | 确定分割线所产生的框的类型。值flex/none，默认值flex。 |
| visibility | string | visible | 否 | 是否显示分割线。不可见的框会占用布局。visible代表显示元素，hidden代表不显示元素。 |
| line-cap | string | butt | 否 | 设置分割线条的端点样式，默认为butt，可选值为：  - butt：分割线两端为平行线；  - round：分割线两端额外添加半圆，额外增加一个线宽的分割线长度；  - square：分割线两端额外添加半方形，额外增加一个线宽的分割线长度； |
| flex | number | - | 否 | 规定了分割线如何适应父组件中的可用空间，用来设置组件的flex-grow。  仅父容器为<div>、<list-item>、<tabs>时生效。 |
| flex-grow | number | 0 | 否 | 设置分割线的伸展因子，指定父组件容器主轴方向上剩余空间（容器本身大小减去所有flex项加起来的大小）的分配系数，0为不伸展。  仅父容器为<div>、<list-item>、<tabs>时生效。 |
| flex-shrink | number | 1 | 否 | 设置分割线的收缩因子，flex元素仅在默认宽度之和大于容器的时候才会发生收缩，0为不收缩。  仅父容器为<div>、<list-item>、<tabs>时生效。 |
| flex-basis | <length> | - | 否 | 设置分割线在主轴方向上的初始大小。  仅父容器为<div>、<list-item>、<tabs>时生效。 |

## 事件

PhonePC/2in1TabletTVWearable

不支持。

## 方法

PhonePC/2in1TabletTVWearable

不支持。

## 示例

PhonePC/2in1TabletTVWearable

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <div class="content">
4. <divider class="divider" vertical="false"></divider>
5. </div>
6. </div>
```

```
1. /* xxx.css */
2. .container {
3. margin: 20px;
4. flex-direction:column;
5. width:100%;
6. height:100%;
7. align-items:center;
8. }
9. .content{
10. width:80%;
11. height:40%;
12. border:1px solid #000000;
13. align-items: center;
14. justify-content: center;
15. flex-direction:column;
16. }
17. .divider {
18. margin: 10px;
19. color: #ff0000ff;
20. stroke-width: 3px;
21. line-cap: round;
22. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/PZCn39U1QjShT11yxzm1gw/zh-cn_image_0000002552800540.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T000259Z&HW-CC-Expire=86400&HW-CC-Sign=CB02C54C785D71508A6997C8B3AF157016234DED8E910099DCFA58A74C807655)
