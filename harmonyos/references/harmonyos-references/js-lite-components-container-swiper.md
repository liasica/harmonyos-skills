---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-container-swiper
title: swiper
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Lite） > 容器组件 > swiper
category: harmonyos-references
scraped_at: 2026-04-29T13:53:51+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:e47257f7711ed24a20db0b5d17e78e9e7dec7618f42a03ce7647b4ead3c4b17b
---

滑动容器，提供切换子组件显示的能力。

说明

该组件从API version 4 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearableLite Wearable

支持除<list>之外的子组件。

## 属性

PhonePC/2in1TabletTVWearableLite Wearable

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| index | number | 0 | 否 | 当前在容器中显示的子组件的索引值。 |
| loop | boolean | true | 否 | 是否开启循环轮播。true为开启循环，false为不开启循环。 |
| duration | number | - | 否 | 子组件切换的动画时长。 |
| vertical | boolean | false | 否 | 是否为纵向滑动，纵向滑动时采用纵向的指示器。true为纵向滑动，false为水平滑动。  不支持动态修改。 |
| id | string | - | 否 | 组件的唯一标识。 |
| style | string | - | 否 | 组件的样式声明。 |
| class | string | - | 否 | 组件的样式类，用于引用样式表。 |
| ref | string | - | 否 | 用来指定指向子元素的引用信息，该引用将注册到父组件的$refs 属性对象上。 |

## 事件

PhonePC/2in1TabletTVWearableLite Wearable

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| change | { index: currentIndex } | 当前显示的组件索引变化时触发该事件。 |
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

## 方法

PhonePC/2in1TabletTVWearableLite Wearable

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| rotation | { focus: boolean } | 控制swiper是否请求旋转表冠的焦点。设置focus参数为true，swiper将获取旋转表冠的焦点，允许用户通过旋转表冠来滚动选择器中的选项；设置为false将释放旋转表冠的焦点。 |

## 示例

PhonePC/2in1TabletTVWearableLite Wearable

```
1. <!-- xxx.hml -->
2. <swiper class="container" index="{{index}}" ref="swiperObj">
3. <div class="swiper-item primary-item">
4. <text>1</text>
5. </div>
6. <div class="swiper-item warning-item">
7. <text>2</text>
8. </div>
9. <div class="swiper-item success-item">
10. <text>3</text>
11. </div>
12. </swiper>
```

```
1. /* xxx.css */
2. .container {
3. left: 0px;
4. top: 0px;
5. width: 454px;
6. height: 454px;
7. }
8. .swiper-item {
9. width: 454px;
10. height: 454px;
11. justify-content: center;
12. align-items: center;
13. }
14. .primary-item {
15. background-color: #007dff;
16. }
17. .warning-item {
18. background-color: #ff7500;
19. }
20. .success-item {
21. background-color: #41ba41;
22. }
```

```
1. /* xxx.js */
2. export default {
3. data: {
4. index: 1
5. },
6. onShow() {
7. this.$refs.swiperObj.rotation({focus: true});
8. }
9. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/MaUUcKjAR9ev2PwM4pgFAA/zh-cn_image_0000002589326801.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055349Z&HW-CC-Expire=86400&HW-CC-Sign=93E9968D7A7CF3E66AA805F5B077AAE3A5921CF5DA37BC77AC4CE6C7882A2E40)
