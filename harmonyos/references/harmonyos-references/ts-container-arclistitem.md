---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclistitem
title: ArcListItem
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 滚动与滑动 > ArcListItem
category: harmonyos-references
scraped_at: 2026-04-29T13:51:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:99fad9422f49b0a8f724174b42aea363a50ec56591cf27831a98d07869a2d682
---

用来展示列表具体子组件，必须配合[ArcList](ts-container-arclist.md)来使用。

说明

* 该组件从API version 18开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件的父组件只能是[ArcList](ts-container-arclist.md)。
* 当ArcListItem配合[LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)使用时，ArcListItem子组件在ArcListItem创建时创建。配合[if/else](../harmonyos-guides/arkts-rendering-control-ifelse.md)、[ForEach](../harmonyos-guides/arkts-rendering-control-foreach.md)使用时，或父组件为[ArcList](ts-container-arclist.md)时，ArcListItem子组件在ArcListItem布局时创建。
* 该组件支持在Phone、PC/2in1、Tablet、TV、Wearable设备上使用。API version 22及以前版本，在Phone、PC/2in1、Tablet、TV上使用会编译告警，但可以正常运行。

## 导入模块

PhonePC/2in1TabletTVWearable

说明

* ArcListItemAttribute是用于配置ArcListItem组件属性的关键接口。API version 21及之前版本，导入ArcListItem组件后需要开发者手动导入ArcListItemAttribute，否则会编译报错。从API version 22开始，编译工具链识别到导入ArcListItem组件后，会自动导入ArcListItemAttribute，无需开发者手动导入ArcListItemAttribute。
* 如果开发者手动导入ArcListItemAttribute，DevEco Studio会显示置灰，API version 21及之前版本删除会编译报错，从API version 22开始，删除对功能无影响。

API version 21及之前版本：

```
1. import { ArcListItem, ArcListItemAttribute } from '@kit.ArkUI';
```

API version 22及之后版本：

```
1. import { ArcListItem } from '@kit.ArkUI';
```

## 子组件

PhonePC/2in1TabletTVWearable

可以包含单个子组件。

## 接口

PhonePC/2in1TabletTVWearable

ArcListItem()

创建弧形列表子组件。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### autoScale

PhonePC/2in1TabletTVWearable

autoScale(enable: Optional<boolean>)

用于设置ArcListItem是否支持自动缩放显示。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | ArcListItem是否支持自动缩放显示，true表示支持自动缩放显示，false表示不支持自动缩放显示。  默认值：true，支持自动缩放显示。 |

### swipeAction

PhonePC/2in1TabletTVWearable

swipeAction(options: Optional<SwipeActionOptions>)

用于设置ArcListItem的划出组件。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[SwipeActionOptions](ts-container-listitem.md#swipeactionoptions9对象说明)> | 是 | ArcListItem的划出组件。 |

## 示例

PhonePC/2in1TabletTVWearable

该示例展示了子项关闭自动缩放和开启自动缩放后的对比效果。

```
1. // xxx.ets
2. import { LengthMetrics, CircleShape } from '@kit.ArkUI';
3. // 从API version 22开始，无需手动导入ArcListAttribute和ArcListItemAttribute。具体请参考ArcList、ArcListItem的导入模块说明。
4. import { ArcList, ArcListItem, ArcListAttribute, ArcListItemAttribute } from '@kit.ArkUI';

6. @Entry
7. @Component
8. struct ArcListItemExample {
9. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
10. private watchSize: string = '466px'; // 手表默认宽高：466*466
11. private itemSize: string = '414px'; // item宽度

13. @Builder
14. buildList() {
15. Stack() {
16. Column() {
17. }
18. .width(this.watchSize)
19. .height(this.watchSize)
20. .clipShape(new CircleShape({ width: '100%', height: '100%' }))
21. .backgroundColor(0x707070)

23. ArcList({ initialIndex: 3}) {
24. ForEach(this.arr, (item: number) => {
25. ArcListItem() {
26. Button('' + item, { type: ButtonType.Capsule })
27. .width(this.itemSize)
28. .height('70px')
29. .fontSize('40px')
30. .backgroundColor(0x17A98D)
31. }
32. .autoScale(item % 3 == 0 || item % 5 == 0)
33. }, (item: number) => item.toString())
34. }
35. .space(LengthMetrics.px(10))
36. .borderRadius(this.watchSize)
37. }
38. .width(this.watchSize)
39. .height(this.watchSize)
40. }

42. build() {
43. Column() {
44. this.buildList();
45. }
46. .width('100%')
47. .height('100%')
48. .alignItems(HorizontalAlign.Center)
49. .justifyContent(FlexAlign.Center)
50. }
51. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/xbAfXOhESueHZsouYU7Iow/zh-cn_image_0000002589326009.png?HW-CC-KV=V1&HW-CC-Date=20260429T055142Z&HW-CC-Expire=86400&HW-CC-Sign=8812DC0ED0AB6F56432D20725F05E834A50FFC2775932265CA0D817B9A72B1DE)
