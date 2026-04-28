---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-container-stack
title: stack
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Lite） > 容器组件 > stack
category: harmonyos-references
scraped_at: 2026-04-28T08:03:26+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:dc4ad3ff03719857bd6435a58ba5727d87cc876c7b850acb1d3ddad28771b26f
---

堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。

说明

该组件从API version 4 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearableLite Wearable

支持。

## 属性

PhonePC/2in1TabletTVWearableLite Wearable

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| id | string | - | 否 | 组件的唯一标识。 |
| style | string | - | 否 | 组件的样式声明。 |
| class | string | - | 否 | 组件的样式类，用于引用样式表。 |
| ref | string | - | 否 | 用来指定指向子元素的引用信息，该引用将注册到父组件的$refs 属性对象上。 |

## 事件

PhonePC/2in1TabletTVWearableLite Wearable

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| click | - | 点击动作触发该事件。 |
| longpress | - | 长按动作触发该事件。 |
| swipe5+ | [SwipeEvent](js-lite-common-events.md) | 组件上快速滑动后触发。 |

## 样式

PhonePC/2in1TabletTVWearableLite Wearable

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| width | <length> | <percentage>5+ | - | 否 | 设置组件自身的宽度。  未设置时组件宽度默认为0。 |
| height | <length> | <percentage>5+ | - | 否 | 设置组件自身的高度。  未设置时组件高度默认为0。 |
| padding | <length> | 0 | 否 | 使用简写属性设置所有的内边距属性。  该属性可以有1到4个值：  - 指定一个值时，该值指定四个边的内边距。  - 指定两个值时，第一个值指定上下两边的内边距，第二个指定左右两边的内边距。  - 指定三个值时，第一个指定上边的内边距，第二个指定左右两边的内边距，第三个指定下边的内边距。  - 指定四个值时分别为上、右、下、左边的内边距（顺时针顺序）。 |
| padding-[left|top|right|bottom] | <length> | 0 | 否 | 设置左、上、右、下内边距属性。 |
| margin | <length> | <percentage>5+ | 0 | 否 | 使用简写属性设置所有的外边距属性，该属性可以有1到4个值。  - 只有一个值时，这个值会被指定给全部的四个边。  - 两个值时，第一个值被匹配给上和下，第二个值被匹配给左和右。  - 三个值时，第一个值被匹配给上, 第二个值被匹配给左和右，第三个值被匹配给下。  - 四个值时，会依次按上、右、下、左的顺序匹配 (即顺时针顺序)。 |
| margin-[left|top|right|bottom] | <length> | <percentage>5+ | 0 | 否 | 设置左、上、右、下外边距属性。 |
| border-width | <length> | 0 | 否 | 使用简写属性设置元素的所有边框宽度。 |
| border-color | <color> | black | 否 | 使用简写属性设置元素的所有边框颜色。 |
| border-radius | <length> | - | 否 | border-radius属性是设置元素的外边框圆角半径。 |
| background-color | <color> | - | 否 | 设置背景颜色。 |
| opacity5+ | number | 1 | 否 | 元素的透明度，取值范围为0到1，1表示为不透明，0表示为完全透明。 |
| display | string | flex | 否 | 确定一个元素所产生的框的类型，可选值为：  - flex：弹性布局。  - none：不渲染此元素。 |
| [left|top] | <length> | <percentage>6+ | - | 否 | left|top确定元素的偏移位置。  - left属性规定元素的左边缘。该属性定义了定位元素左外边距边界与其包含块左边界之间的偏移。  - top属性规定元素的顶部边缘。该属性定义了一个定位元素的上外边距边界与其包含块上边界之间的偏移。 |

说明

由于绝对定位不支持设置百分比，所以也不支持stack组件的子组件上设置margin。

## 示例

PhonePC/2in1TabletTVWearableLite Wearable

```
1. <!-- xxx.hml -->
2. <stack class="stack-parent">
3. <div class="back-child bd-radius"></div>
4. <div class="positioned-child bd-radius"></div>
5. <div class="front-child bd-radius"></div>
6. </stack>
```

```
1. /* xxx.css */
2. .stack-parent {
3. width: 400px;
4. height: 400px;
5. background-color: #ffffff;
6. border-width: 1px;
7. border-style: solid;
8. }
9. .back-child {
10. width: 300px;
11. height: 300px;
12. background-color: #3f56ea;
13. }
14. .front-child {
15. width: 100px;
16. height: 100px;
17. background-color: #00bfc9;
18. }
19. .positioned-child {
20. width: 100px;
21. height: 100px;
22. left: 50px;
23. top: 50px;
24. background-color: #47cc47;
25. }
26. .bd-radius {
27. border-radius: 16px;
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/lB48jb0eQBSakzGvWAIIuw/zh-cn_image_0000002552960406.png?HW-CC-KV=V1&HW-CC-Date=20260428T000325Z&HW-CC-Expire=86400&HW-CC-Sign=F63DF135679D9B0EEB427C91A14FAA8D974048C71C2CCB8DDF64CA84BE32D132)
