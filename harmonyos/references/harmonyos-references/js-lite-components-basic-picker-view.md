---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-basic-picker-view
title: picker-view
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Lite） > 基础组件 > picker-view
category: harmonyos-references
scraped_at: 2026-04-28T08:03:29+08:00
doc_updated_at: 2026-04-02
content_hash: sha256:a46b394e9b79d1fa676cd6f5365e89f14dd215a420da7136d43c0e0f5a49522a
---

嵌入页面的滑动选择器。

说明

该组件从API version 4 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearableLite Wearable

不支持。

## 属性

PhonePC/2in1TabletTVWearableLite Wearable

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| type | string | text | 否 | 设置滑动选择器的类型，该属性不支持动态修改，可选项有：  - text：文本选择器。  - time：时间选择器。 |
| id | string | - | 否 | 组件的唯一标识。 |
| style | string | - | 否 | 组件的样式声明。 |
| class | string | - | 否 | 组件的样式类，用于引用样式表。 |
| ref | string | - | 否 | 用来指定指向子元素的引用信息，该引用将注册到父组件的$refs 属性对象上。 |

文本选择器：type=text

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| range | Array | - | 否 | 设置文本选择器的取值范围。  使用时需要使用数据绑定的方式，如range = {{data}}，js中声明相应变量：data：["15", "20", "25"]。 |
| selected | number | 0 | 否 | 设置文本选择器的默认选择值，该值需要为range的索引。 |

时间选择器：type=time

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| selected | string | 00:00 | 否 | 设置时间选择器的默认取值，格式为 HH:mm； |

## 事件

PhonePC/2in1TabletTVWearableLite Wearable

type=text：

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| change | { newValue: newValue, newSelected: newSelected } | 文本选择器选定值后触发该事件。 |

type=time：

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| change | { hour: hour, minute: minute} | 时间选择器选定值后触发该事件。 |

## 样式

PhonePC/2in1TabletTVWearableLite Wearable

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| color | <color> | #808080 | 否 | 候选项字体颜色。 |
| font-size | <length> | 30px | 否 | 候选项字体尺寸，类型length，单位px。 |
| selected-color | <color> | #ffffff | 否 | 选中项字体颜色。 |
| selected-font-size | <length> | 38px | 否 | 选中项字体尺寸，类型length，单位px。 |
| selected-font-family | string | HYQiHei-65S | 否 | 选中项字体类型。 |
| font-family | string | HYQiHei-65S | 否 | 选项字体类型。 |
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
| display | string | flex | 否 | 确定一个元素所产生的框的类型，可选值为：  - flex：弹性布局。  - none：不渲染此元素。 |
| [left|top] | <length> | <percentage>6+ | - | 否 | left|top确定元素的偏移位置。  - left属性规定元素的左边缘。该属性定义了定位元素左外边距边界与其包含块左边界之间的偏移。  - top属性规定元素的顶部边缘。该属性定义了一个定位元素的上外边距边界与其包含块上边界之间的偏移。 |

## 方法

PhonePC/2in1TabletTVWearableLite Wearable

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| rotation | { focus: boolean } | 控制picker-view是否请求旋转表冠的焦点。设置focus参数为true，picker-view将获取旋转表冠的焦点，允许用户通过旋转表冠来滚动选择器中的选项；设置为false将释放旋转表冠的焦点。该功能仅在picker-view为单列时生效，对于多列picker-view，需通过用户点击来获取焦点以支持旋转表冠操作。 |

## 示例

PhonePC/2in1TabletTVWearableLite Wearable

```
1. <!-- xxx.hml -->
2. <div class="container" @swipe="handleSwipe">
3. <text class="title">
4. Selected：{{time}}
5. </text>
6. <picker-view class="time-picker" type="time" selected="{{defaultTime}}" @change="handleChange"></picker-view>
7. </div>
```

```
1. /* xxx.css */
2. .container {
3. flex-direction: column;
4. justify-content: center;
5. align-items: center;
6. left: 0px;
7. top: 0px;
8. width: 454px;
9. height: 454px;
10. }
11. .title {
12. font-size: 30px;
13. text-align: center;
14. }
15. .time-picker {
16. width: 500px;
17. height: 400px;
18. margin-top: 20px;
19. }
```

```
1. /* xxx.js */
2. export default {
3. data: {
4. defaultTime: "",
5. time: "",
6. },
7. onInit() {
8. this.defaultTime = this.now();
9. },
10. handleChange(data) {
11. this.time = this.concat(data.hour, data.minute);
12. },
13. now() {
14. const date = new Date();
15. const hours = date.getHours();
16. const minutes = date.getMinutes();
17. return this.concat(hours, minutes);
18. },

20. fill(value) {
21. return (value > 9 ? "" : "0") + value;
22. },

24. concat(hours, minutes) {
25. return `${this.fill(hours)}:${this.fill(minutes)}`;
26. },
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/aVqFUEmgS22ibtawGQ4aRg/zh-cn_image_0000002552800762.png?HW-CC-KV=V1&HW-CC-Date=20260428T000327Z&HW-CC-Expire=86400&HW-CC-Sign=E8E2A06FC351AF5CA1DA2B4D52AF51124A573BAC111062A90186E719FE211A98)
