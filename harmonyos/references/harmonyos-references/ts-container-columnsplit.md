---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-columnsplit
title: ColumnSplit
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 栅格与分栏 > ColumnSplit
category: harmonyos-references
scraped_at: 2026-04-29T13:51:41+08:00
doc_updated_at: 2026-04-08
content_hash: sha256:95515aa99073b78822b675f02aba5db3805c992dae80c929bf9ca5036fd227cb
---

将子组件纵向布局，并在每个子组件之间插入横向分割线。

说明

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

可以包含子组件。

ColumnSplit通过分割线限制子组件的高度。初始化时，分割线位置根据子组件的高度来计算。初始化后，动态修改子组件的高度不生效，分割线位置保持不变，可通过拖动相邻分割线改变子组件高度。

初始化后，动态修改[margin](ts-universal-attributes-size.md#margin)、[border](ts-universal-attributes-border.md#border)、[padding](ts-universal-attributes-size.md#padding)通用属性导致子组件尺寸大于相邻分割线间距的异常情况下，不支持拖动分割线改变子组件的高度。

## 接口

PhonePC/2in1TabletTVWearable

ColumnSplit()

带分割线的子组件纵向布局。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

说明

ColumnSplit组件[形状裁剪](ts-universal-attributes-sharp-clipping.md)的默认值为true。

### resizeable

PhonePC/2in1TabletTVWearable

resizeable(value: boolean)

设置分割线是否可拖拽。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 分割线是否可拖拽。设置为true时表示分割线可拖拽，设置为false时表示分割线不可拖拽。  默认值：false  非法值：按默认值处理。 |

### divider10+

PhonePC/2in1TabletTVWearable

divider(value: ColumnSplitDividerStyle | null)

设置分割线的margin。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ColumnSplitDividerStyle](ts-container-columnsplit.md#columnsplitdividerstyle10对象说明) | null | 是 | 分割线的margin，即设置分割线与子组件的距离。  默认值：null。当设置为null时，分割线与子组件的距离为0vp。  非法值：按默认值处理。 |

## ColumnSplitDividerStyle10+对象说明

PhonePC/2in1TabletTVWearable

设置子组件与上下分割线的距离。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| startMargin | [Dimension](ts-types.md#dimension10) | 否 | 是 | 子组件与其上方分割线的距离。  默认值：0vp  非法值：按默认值处理，此时[getInspectorByKey()](ts-universal-attributes-component-id.md#getinspectorbykey9)接口获取到的属性值为undefined。 |
| endMargin | [Dimension](ts-types.md#dimension10) | 否 | 是 | 子组件与其下方分割线的距离。  默认值：0vp  非法值：按默认值处理，此时[getInspectorByKey()](ts-universal-attributes-component-id.md#getinspectorbykey9)接口获取到的属性值为undefined。 |

说明

与[RowSplit](ts-container-rowsplit.md)相同，ColumnSplit的分割线可调整上下两侧子组件的高度，子组件的高度调整范围受其最大最小高度限制。

支持[clip](ts-universal-attributes-sharp-clipping.md#clip12)、[margin](ts-universal-attributes-size.md#margin)等通用属性，未设置clip属性时，其默认值为true。

## 事件

PhonePC/2in1TabletTVWearable

支持[通用事件](ts-component-general-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置可拖动的ColumnSplit组件）

本示例展示如何设置可拖动的ColumnSplit组件及其效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ColumnSplitExample {
5. build() {
6. Column() {
7. Text('The dividing line can be dragged').fontSize(9).fontColor(0xCCCCCC).width('90%')
8. ColumnSplit() {
9. Text('1').width('100%').height(50).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)
10. Text('2').width('100%').height(50).backgroundColor(0xD2B48C).textAlign(TextAlign.Center)
11. Text('3').width('100%').height(50).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)
12. Text('4').width('100%').height(50).backgroundColor(0xD2B48C).textAlign(TextAlign.Center)
13. Text('5').width('100%').height(50).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)
14. }
15. .borderWidth(1)
16. .resizeable(true) // 可拖动
17. .width('90%').height('60%')
18. }.width('100%')
19. }
20. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/KeGMl_zFQ5-ZYgiCX2eHeA/zh-cn_image_0000002558606466.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055140Z&HW-CC-Expire=86400&HW-CC-Sign=1F1ECA4C0EBF90FBA09A911AE4920534AB6328FEC6EA4643E730C42245D0E474)

### 示例2（设置带有间隔的ColumnSplit组件）

本示例展示如何设置带有间隔的ColumnSplit组件及其效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ColumnSplitDividerExample {
5. build() {
6. Column() {
7. Text('The dividing line can be dragged').fontSize(9).fontColor(0xCCCCCC).width('90%')
8. ColumnSplit() {
9. Text('1').width('100%').height(50).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)
10. Text('2').width('100%').height(50).backgroundColor(0xD2B48C).textAlign(TextAlign.Center)
11. Text('3').width('100%').height(50).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)
12. Text('4').width('100%').height(50).backgroundColor(0xD2B48C).textAlign(TextAlign.Center)
13. Text('5').width('100%').height(50).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)
14. }
15. .borderWidth(1)
16. .divider({ startMargin: 5, endMargin: 5 }) // 设置间隔
17. .width('90%')
18. .height('60%')
19. }.width('100%')
20. }
21. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/u577pJwvSQ-FjL1ep_V-AA/zh-cn_image_0000002589325993.png?HW-CC-KV=V1&HW-CC-Date=20260429T055140Z&HW-CC-Expire=86400&HW-CC-Sign=FA99522C0840D51E420CCF711B9D3004640011F66ABE23537257BCA05B513809)
