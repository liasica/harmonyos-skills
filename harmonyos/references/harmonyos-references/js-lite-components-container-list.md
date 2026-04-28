---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-container-list
title: list
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > 兼容JS的类Web开发范式（ArkUI.Lite） > 容器组件 > list
category: harmonyos-references
scraped_at: 2026-04-28T08:03:26+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:90f7bd6fe465725f1d93841bd6a28f466cf28bc4d23d433e425794e806e90c6f
---

列表包含一系列相同宽度的列表项。适合连续、多行呈现同类数据，例如图片和文本。

说明

该组件从API version 4 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearableLite Wearable

仅支持<[list-item](js-lite-components-container-list-item.md)>。

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
| scrollend | - | 列表滑动已经结束。 |
| click | - | 点击动作触发该事件。 |
| longpress | - | 长按动作触发该事件。 |
| swipe5+ | [SwipeEvent](js-lite-common-events.md) | 组件上快速滑动后触发。 |
| scrolltop8+ | - | 当前列表已滑动到顶部位置。 |
| scrollbottom8+ | - | 当前列表已滑动到底部位置。 |

## 样式

PhonePC/2in1TabletTVWearableLite Wearable

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| flex-direction | string | column | 否 | 设置flex容器主轴的方向，指定flex项如何放置在flex容器中，可选值为：  - column：主轴为纵向。  - row：主轴为横向。  其他组件默认值为row，在list组件中默认值为column。轻量级智能穿戴设备不支持动态修改。 |
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
| [left|top] | <length> | <percentage>6+ | - | 否 | left|top规定元素的偏移位置。  - left属性规定元素的左边缘。该属性定义了定位元素左外边距边界与其包含块左边界之间的偏移。  - top属性规定元素的顶部边缘。该属性定义了一个定位元素的上外边距边界与其包含块上边界之间的偏移。 |

## 方法

PhonePC/2in1TabletTVWearableLite Wearable

| 名称 | 参数 | 描述 |
| --- | --- | --- |
| scrollTo | { index: number(指定位置) } | list滑动到指定index的item位置。 |
| rotation | { focus: boolean } | 控制list是否请求旋转表冠的焦点。设置focus参数为true，list将获取旋转表冠的焦点，允许用户通过旋转表冠来滚动选择器中的选项；设置为false将释放旋转表冠的焦点。 |

## 示例

PhonePC/2in1TabletTVWearableLite Wearable

```
1. <!-- index.hml -->
2. <div class="container">
3. <list class="todo-wrapper" ref="listObj">
4. <list-item for="{{todolist}}" class="todo-item">
5. <div style="flex-direction: column;align-items: center;justify-content: center;">
6. <text class="todo-title">{{$item.title}}</text>
7. <text class="todo-title">{{$item.date}}</text>
8. </div>
9. </list-item>
10. </list>
11. </div>
```

```
1. // index.js
2. export default {
3. data: {
4. todolist: [{
5. title: '刷题',
6. date: '2021-12-31 10:00:00',
7. }, {
8. title: '看电影',
9. date: '2021-12-31 20:00:00',
10. }
11. , {
12. title: '看书',
13. date: '2021-12-31 21:00:00',
14. },
15. {
16. title: '洗澡',
17. date: '2021-12-31 22:00:00',
18. },
19. {
20. title: '睡觉',
21. date: '2021-12-31 23:00:00',
22. }],
23. },
24. onShow() {
25. this.$refs.listObj.rotation({focus: true})
26. }
27. }
```

```
1. /* index.css */
2. .container {
3. display: flex;
4. justify-content: center;
5. align-items: center;
6. left: 0px;
7. top: 0px;
8. width: 454px;
9. height: 454px;
10. }
11. .todo-wrapper {
12. width: 454px;
13. height: 500px;
14. }
15. .todo-item {
16. width: 454px;
17. height: 80px;
18. flex-direction: column;
19. }
20. .todo-title {
21. width: 454px;
22. height: 40px;
23. text-align: center;
24. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/lQMkpf_xS3euny6o2v8kOA/zh-cn_image_0000002583440451.png?HW-CC-KV=V1&HW-CC-Date=20260428T000325Z&HW-CC-Expire=86400&HW-CC-Sign=158110ABAD84BAD8AABA0B4F967A94FE3E998F0901CD813830EF40FBED18011A)
