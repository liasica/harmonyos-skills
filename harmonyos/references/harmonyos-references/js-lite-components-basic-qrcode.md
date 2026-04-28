---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-basic-qrcode
title: qrcode
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Lite） > 基础组件 > qrcode
category: harmonyos-references
scraped_at: 2026-04-28T08:03:29+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:944c99af8a27de40c6b635fa06ac4915fea42afb4f75ee3dfc171ef239c65bec
---

生成并显示二维码。

说明

该组件从API version 5 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearableLite Wearable

不支持。

## 属性

PhonePC/2in1TabletTVWearableLite Wearable

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| value | string | - | 是 | 用来生成二维码的内容。最大长度为256。 |
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
| color | <color> | #000000 | 否 | 二维码颜色。 |
| background-color | <color> | #ffffff | 否 | 二维码背景颜色。 |
| width | <length> | <percentage>5+ | - | 否 | 设置组件自身的宽度。  未设置时组件宽度默认为0。 |
| height | <length> | <percentage>5+ | - | 否 | 设置组件自身的高度。  未设置时组件高度默认为0。 |
| padding | <length> | 0 | 否 | 使用简写属性设置所有的内边距属性。  该属性可以有1到4个值：  - 指定一个值时，该值指定四个边的内边距。  - 指定两个值时，第一个值指定上下两边的内边距，第二个指定左右两边的内边距。  - 指定三个值时，第一个指定上边的内边距，第二个指定左右两边的内边距，第三个指定下边的内边距。  - 指定四个值时分别为上、右、下、左边的内边距（顺时针顺序）。 |
| padding-[left|top|right|bottom] | <length> | 0 | 否 | 设置左、上、右、下内边距属性。 |
| margin | <length> | <percentage>5+ | 0 | 否 | 使用简写属性设置所有的外边距属性，该属性可以有1到4个值。  - 只有一个值时，这个值会被指定给全部的四个边。  - 两个值时，第一个值被匹配给上和下，第二个值被匹配给左和右。  - 三个值时，第一个值被匹配给上, 第二个值被匹配给左和右，第三个值被匹配给下。  - 四个值时，会依次按上、右、下、左的顺序匹配 (即顺时针顺序)。 |
| margin-[left|top|right|bottom] | <length> | <percentage>5+ | 0 | 否 | 设置左、上、右、下外边距属性。 |
| border-width | <length> | 0 | 否 | 使用简写属性设置元素的所有边框宽度。 |
| border-color | <color> | black | 否 | 使用简写属性设置元素的所有边框颜色。 |
| border-radius | <length> | - | 否 | border-radius属性是设置元素的外边框圆角半径。 |
| display | string | flex | 否 | 确定一个元素所产生的框的类型，可选值为：  - flex：弹性布局。  - none：不渲染此元素。 |
| [left|top] | <length> | <percentage>6+ | - | 否 | left|top确定元素的偏移位置。  - left属性规定元素的左边缘。该属性定义了定位元素左外边距边界与其包含块左边界之间的偏移。  - top属性规定元素的顶部边缘。该属性定义了一个定位元素的上外边距边界与其包含块上边界之间的偏移。 |

说明

* width和height不一致时，以二者最小值作为二维码的边长。且最终生成的二维码居中显示；
* width和height的最小值为200px。

## 示例

PhonePC/2in1TabletTVWearableLite Wearable

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <qrcode value="{{qr_value}}" class="qrCode" style="color: {{qr_col}};background-color: {{qr_bcol}};"></qrcode>
4. <input type="button" onclick="changeColor" class="button">Color</input>
5. <input type="button" onclick="changeBackgroundColor" class="button">BackgroundColor</input>
6. <input type="button" onclick="changeValue" class="button">Value</input>
7. </div>
```

```
1. /* xxx.css */
2. .container {
3. width: 100%;
4. height: 100%;
5. flex-direction: column;
6. justify-content: center;
7. align-items: center;
8. }
9. .qrCode {
10. width: 200px;
11. height: 200px;
12. }
13. .button {
14. width: 30%;
15. height: 10%;
16. margin-top: 5%;
17. }
```

```
1. // xxx.js
2. export default {
3. data: {
4. qr_col: '#87ceeb',
5. qr_bcol: '#f0ffff',
6. qr_value: 'value'
7. },
8. changeColor() {
9. if (this.qr_col == '#87ceeb') {
10. this.qr_col = '#fa8072';
11. } else {
12. this.qr_col = '#87ceeb';
13. }
14. },
15. changeBackgroundColor() {
16. if (this.qr_bcol == '#f0ffff') {
17. this.qr_bcol = '#ffffe0';
18. } else {
19. this.qr_bcol = '#f0ffff';
20. }
21. },
22. changeValue() {
23. if (this.qr_value == 'value') {
24. this.qr_value = 'change';
25. } else {
26. this.qr_value = 'value';
27. }
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/7G2h1EGEQ4qD0EGXdeovVw/zh-cn_image_0000002552960412.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000328Z&HW-CC-Expire=86400&HW-CC-Sign=FD4BA09623CC1F5FEB2CB7217F02214017A023CD68C7518835024D16BD0361B7)
