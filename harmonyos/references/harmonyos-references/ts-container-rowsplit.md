---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-rowsplit
title: RowSplit
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 栅格与分栏 > RowSplit
category: harmonyos-references
scraped_at: 2026-04-29T13:51:41+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1394f890c2e4b1d58c4cc034eb81d6f1036cc3b67a5c257cce42684e2dfc963a
---

将子组件横向布局，并在每个子组件之间插入纵向分割线。

说明

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

可以包含子组件。

RowSplit通过分割线限制子组件的宽度。初始化时，分割线位置根据子组件的宽度来计算。初始化后，动态修改子组件的宽度不生效，分割线位置保持不变，可以通过拖动相邻分割线改变子组件宽度。

初始化后，动态修改[margin](ts-universal-attributes-size.md#margin)、[border](ts-universal-attributes-border.md#border)、[padding](ts-universal-attributes-size.md#padding)通用属性导致子组件宽度大于相邻分割线间距的异常情况下，不支持拖动分割线改变子组件的宽度。

## 接口

PhonePC/2in1TabletTVWearable

RowSplit()

带分割线的子组件横向分隔布局。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

说明

RowSplit组件[形状裁剪](ts-universal-attributes-sharp-clipping.md)的默认值为true。

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

说明

RowSplit的分割线可以改变左右两边子组件的宽度，子组件可改变宽度的范围取决于子组件的最大最小宽度。

## 事件

PhonePC/2in1TabletTVWearable

支持[通用事件](ts-component-general-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

RowSplit的基本用法。设置可拖动的、横向布局的子组件。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct RowSplitExample {
5. build() {
6. Column() {
7. Text('The second line can be dragged').fontSize(9).fontColor(0xCCCCCC).width('90%')
8. RowSplit() {
9. Text('1').width('10%').height(100).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)
10. Text('2').width('10%').height(100).backgroundColor(0xD2B48C).textAlign(TextAlign.Center)
11. Text('3').width('10%').height(100).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)
12. Text('4').width('10%').height(100).backgroundColor(0xD2B48C).textAlign(TextAlign.Center)
13. Text('5').width('10%').height(100).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)
14. }
15. .resizeable(true) // 可拖拽
16. .width('90%').height(100)
17. }.width('100%').margin({ top: 5 })
18. }
19. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/t_5XyXFGQ7Guhnft7gKMWw/zh-cn_image_0000002589245935.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055140Z&HW-CC-Expire=86400&HW-CC-Sign=7AAC7FADD19A94F10999414CFE830D5287365C9C50FF7CC3F8F1FA6740FE6EC3)
