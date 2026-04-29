---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-container-list
title: list
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > JS组件 > JS服务卡片UI组件 > 容器组件 > list
category: harmonyos-references
scraped_at: 2026-04-29T13:53:59+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:b958a30dea2e10fe5ccda08db8e5be6cdc53c60849ecef3e80cf7e496ea82b63
---

列表包含一系列相同宽度的列表项。适合连续、多行呈现同类数据，例如图片和文本。

说明

从API version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

针对卡片场景，建议开发者控制list中的子节点list-item的数量（建议30条以内）以便获得更好的卡片交互体验。

## 子组件

PhonePC/2in1TabletTVWearable

仅支持<[list-item](js-service-widget-container-list-item.md)>子组件。

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](js-service-widget-common-attributes.md)外，还支持如下属性：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| cachedcount | number | 0 | 否 | 长列表延迟加载时list-item最少缓存数量。 |
| scrollbar | string | off | 否 | 侧边滑动栏的显示模式（当前只支持纵向）：  - off：不显示。  - auto：按需显示(触摸时显示，2s后消失)。  - on：常驻显示。 |
| scrolleffect | string | spring | 否 | 滑动效果，目前支持如下滑动效果：  - spring：弹性物理动效，滑动到边缘后可以根据初始速度或通过触摸事件继续滑动一段距离，松开后回弹。  - fade：渐隐物理动效，滑动到边缘后展示一个波浪形的渐隐，根据速度和滑动距离的变化渐隐也会发生一定的变化。  - no：滑动到边缘后无效果。 |
| divider | boolean | false | 否 | item是否自带分隔线。  其样式参考[样式列表](js-service-widget-container-list.md#样式)的divider-color、divider-height、divider-length、divider-origin。  - false：item不自带分隔线。  - true：item自带分隔线。 |
| shapemode | string | default | 否 | 侧边滑动栏的形状类型。  - default：不指定，跟随主题。  - rect：矩形。  - round：圆形。 |
| updateeffect | boolean | false | 否 | 用于设置当list内部的item发生删除或新增时是否支持动效。  - false：新增删除item时无过渡动效。  - true：新增删除item时有过渡动效。 |
| initialindex | number | 0 | 否 | 用于设置当前List初次加载时视口起始位置显示的item，默认为0，即显示第一个item，如设置的序号超过了最后一个item的序号，则设置不生效，当同时设置了initialoffset属性时，当前属性不生效。 |
| initialoffset | <length> | 0 | 否 | 用于设置当前List初次加载时视口的起始偏移量，偏移量无法超过当前List可滑动的范围，如果超过会被截断为可滑动范围的极限值。 |
| selected | string | - | 否 | 指定当前列表中被选中激活的项，可选值为list-item的section属性值。 |

## 样式

PhonePC/2in1TabletTVWearable

除支持[通用样式](js-service-widget-common-styles.md)外，还支持如下样式：

| 名称 | 类型 | 默认值 | 必填 | 描述 |
| --- | --- | --- | --- | --- |
| divider-color | <color> | transparent | 否 | item分隔线颜色，仅当list的divider属性为true时生效。 |
| divider-height | <length> | 1 | 否 | item分隔线高度，仅当list的divider属性为true时生效。 |
| divider-length | <length> | 主轴宽度 | 否 | item分隔线长度，不设置时最大长度为主轴宽度，具体长度取决于divider-origin，仅当list的divider属性为true时生效。 |
| divider-origin | <length> | 0 | 否 | item分隔线相对于item主轴起点位置的偏移量，仅当list的divider属性为true时生效。 |
| flex-direction | string | column | 否 | 设置flex容器主轴的方向，指定flex项如何放置在flex容器中，可选值为：  - column：主轴为纵向。  - row：主轴为横向。  其他组件默认值为row，在list组件中默认值为column。 |
| columns | number | 1 | 否 | list交叉轴方向的显示列数，默认为1列。  设置多列时，在list交叉轴上进行均分，每一列大小相同。 |
| align-items | string | stretch | 否 | list每一列交叉轴上的对齐格式，可选值为：  - stretch：弹性元素被在交叉轴方向被拉伸到与容器相同的高度或宽度。  - flex-start：元素向交叉轴起点对齐。  - flex-end：元素向交叉轴终点对齐。  - center：元素在交叉轴居中。  align-items样式作用在每一列的子元素上，列与列之间采用均分方式布局。 |
| item-extent | <length> | <percentage> | - | 否 | 设置内部item为固定大小，设置为百分比格式时，指相对于list的视口主轴方向长度的百分比。 |
| fade-color | <color> | grey | 否 | 设置渐隐物理动效的颜色。当滑动效果设置为渐隐物理动效时生效。 |
| scrollbar-color | <color> | - | 否 | 设置滚动条的颜色。 |
| scrollbar-width | <length> | - | 否 | 设置滚动条的宽度。 |
| scrollbar-offset | <length> | 0 | 否 | 设置滚动条距离List默认位置的偏移量，只支持正数，默认位置在List右边缘，可以通过这个偏移量调整滚动条的水平位置，如果滚动条绘制在list外部，而list父组件有裁剪，会导致滚动条被裁剪。 |

## 事件

PhonePC/2in1TabletTVWearable

支持[通用事件](js-service-widget-common-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

```
1. <!-- index.html -->
2. <div class="container">
3. <list class="todo-wrapper">
4. <list-item for="{{todolist}}" class="todo-item">
5. <text class="todo-title">{{$item.title}}</text>
6. <text class="todo-title">{{$item.date}}</text>
7. </list-item>
8. </list>
9. </div>
```

```
1. {
2. "data": {
3. "todolist": [{
4. "title": "work",
5. "date": "2021-12-31 10:00:00"
6. }, {
7. "title": "watch movie",
8. "date": "2021-12-31 20:00:00"
9. }]
10. }
11. }
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
13. height: 300px;
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

**4\*4卡片**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/pk-JIlNGTsmh1dibNDyYjA/zh-cn_image_0000002558766952.png?HW-CC-KV=V1&HW-CC-Date=20260429T055358Z&HW-CC-Expire=86400&HW-CC-Sign=598B45B98603448226E92680B1DEB40A28267A38B80142FDF37055146CF9E132)
