---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-basic-text
title: text
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Lite） > 基础组件 > text
category: harmonyos-references
scraped_at: 2026-04-28T08:03:30+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:236a384f698f67f448cf19e1c5a623816d19375398beab52d63e101d0096f9c8
---

文本，用于呈现一段信息。

说明

该组件从API version 4 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearableLite Wearable

不支持。

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
| color | <color> | #ffffff | 否 | 设置文本的颜色。 |
| font-size | <length> | 30px | 否 | 设置文本的尺寸。 |
| letter-spacing | <length> | 2px | 否 | 设置文本的字符间距。 |
| text-align | string | left | 否 | 设置文本的文本对齐方式，可选值为：  - left：文本左对齐；  - center：文本居中对齐；  - right：文本右对齐； |
| text-overflow | string | clip | 否 | 可选值为：  - clip：将文本根据父容器大小进行裁剪显示；  - ellipsis：根据父容器大小显示，显示不下的文本用省略号代替。 |
| font-family | string | SourceHanSansSC-Regular | 否 | 字体。目前仅支持SourceHanSansSC-Regular 字体。 |
| width | <length> | <percentage>5+ | 0px | 否 | 设置组件自身的宽度。  单位：px  未设置时组件宽度默认为0。 |
| height | <length> | <percentage>5+ | 0px | 否 | 设置组件自身的高度。  单位：px  未设置时组件高度默认为0。 |
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
| line-height10+ | number | 0px | 否 | 设置文本的行高。  单位：px  未设置时文本行高默认为适应性行高。 |

## 示例

PhonePC/2in1TabletTVWearableLite Wearable

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <text class="title">
4. Hello {{ title }}
5. </text>
6. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. justify-content: center;
6. align-items: center;
7. }

9. .title {
10. width: 100px;
11. font-size: 30px;
12. text-align: center;
13. color: red;
14. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. title: ""
5. },
6. onInit() {
7. this.title = "World";
8. }
9. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/-3a8UMRyTEO4Dn4zgpOalw/zh-cn_image_0000002583440459.png?HW-CC-KV=V1&HW-CC-Date=20260428T000329Z&HW-CC-Expire=86400&HW-CC-Sign=8F1777B013CFF1596AB370733E8E9987FFB25D67E32C916E9DA024E2E9E36C9C)
