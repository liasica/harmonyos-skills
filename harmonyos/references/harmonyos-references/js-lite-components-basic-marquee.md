---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-basic-marquee
title: marquee
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Lite） > 基础组件 > marquee
category: harmonyos-references
scraped_at: 2026-04-29T13:53:52+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c6d58057469a491800c79c44636317309d1606b74c1b40185be0ad65c1715a20
---

跑马灯组件，用于展示一段单行滚动的文字。

说明

该组件从API version 4 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearableLite Wearable

不支持。

## 属性

PhonePC/2in1TabletTVWearableLite Wearable

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| scrollamount | number | 6 | 否 | 跑马灯每次滚动时移动的最大长度。 |
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
| color | <color> | #ffffff | 否 | 设置跑马灯中文字的文本颜色。 |
| font-size | <length> | 30 | 否 | 设置跑马灯中文字的文本尺寸。 |
| font-family | string | SourceHanSansSC-Regular | 否 | 字体。目前仅支持SourceHanSansSC-Regular 字体。 |
| width | <length> | <percentage>5+ | - | 否 | 设置组件自身的宽度。  未设置时组件宽度默认为0。 |
| height | <length> | <percentage>5+ | - | 否 | 设置组件自身的高度。  未设置时组件高度默认为0。 |
| padding | <length> | 0 | 否 | 使用简写属性设置所有的内边距属性。  该属性可以有1到4个值：  - 指定一个值时，该值指定四个边的内边距。  - 指定两个值时，第一个值指定上下两边的内边距，第二个指定左右两边的内边距。  - 指定三个值时，第一个指定上边的内边距，第二个指定左右两边的内边距，第三个指定下边的内边距。  - 指定四个值时分别为上、右、下、左边的内边距（顺时针顺序）。 |
| padding-[left|top|right|bottom] | <length> | 0 | 否 | 设置左、上、右、下内边距属性。 |
| margin | <length> | <percentage>5+ | 0 | 否 | 使用简写属性设置所有的外边距属性，该属性可以有1到4个值。  - 只有一个值时，这个值会被指定给全部的四个边。  - 两个值时，第一个值被匹配给上和下，第二个值被匹配给左和右。  - 三个值时，第一个值被匹配给上； 第二个值被匹配给左和右；第三个值被匹配给下。  - 四个值时，会依次按上、右、下、左的顺序匹配 (即顺时针顺序)。 |
| margin-[left|top|right|bottom] | <length> | <percentage>5+ | 0 | 否 | 设置左、上、右、下外边距属性。 |
| border-width | <length> | 0 | 否 | 使用简写属性设置元素的所有边框宽度。 |
| border-color | <color> | black | 否 | 使用简写属性设置元素的所有边框颜色。 |
| border-radius | <length> | - | 否 | border-radius属性是设置元素的外边框圆角半径。 |
| background-color | <color> | - | 否 | 设置背景颜色。 |
| opacity5+ | number | 1 | 否 | 元素的透明度，取值范围为0到1，1表示为不透明，0表示为完全透明。 |
| display | string | flex | 否 | 确定一个元素所产生的框的类型，可选值为：  - flex：弹性布局。  - none：不渲染此元素。 |
| [left|top] | <length> | <percentage>6+ | - | 否 | left|top确定元素的偏移位置。  - left属性规定元素的左边缘。该属性定义了定位元素左外边距边界与其包含块左边界之间的偏移。  - top属性规定元素的顶部边缘。该属性定义了一个定位元素的上外边距边界与其包含块上边界之间的偏移。 |

## 示例

PhonePC/2in1TabletTVWearableLite Wearable

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <marquee class="customMarquee" scrollamount="{{scrollAmount}}">{{marqueeCustomData}}</marquee>
4. <text class="text" onclick="addSpeed">speed+</text>
5. <text class="text" onclick="downSpeed">speed-</text>
6. <text class="text" onclick="changeData">changeData</text>
7. </div>
```

```
1. /* xxx.css */
2. .container {
3. flex-direction: column;
4. width: 100%;
5. height: 100%;
6. flex-direction: column;
7. align-items: center;
8. }
9. .customMarquee {
10. width: 50%;
11. height: 80px;
12. padding: 10px;
13. margin: 20px;
14. border-width: 4px;
15. border-color: #ffffff;
16. border-radius: 20px;
17. font-size: 38px;
18. }
19. .text {
20. font-size: 30px;
21. text-align: center;
22. width: 30%;
23. height: 10%;
24. margin-top: 5%;
25. background-color: #f2f2f2;
26. border-radius: 40px;
27. color: #0d81f2;
28. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. scrollAmount: 30,
5. marqueeCustomData: 'Custom marquee Custom marquee Custom marquee'
6. },
7. addSpeed() {
8. this.scrollAmount++;
9. },
10. downSpeed() {
11. this.scrollAmount--;
12. },
13. changeData() {
14. this.marqueeCustomData = 'Change Data Change Data Change Data';
15. }
16. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/vPwFqs8HSSSS5x1NqBZv0g/zh-cn_image_0000002589326805.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055351Z&HW-CC-Expire=86400&HW-CC-Sign=3A929862C036B1B485D64DD6AAE9086C0C21AAE734FA1B751695DA06384E461D)
