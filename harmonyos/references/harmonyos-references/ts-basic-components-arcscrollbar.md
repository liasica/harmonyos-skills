---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-arcscrollbar
title: ArcScrollBar
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 滚动与滑动 > ArcScrollBar
category: harmonyos-references
scraped_at: 2026-04-28T08:01:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:20b0057990544e5491839e6d80e8bcb3ca891a5e8cdbf906fabdc672cff5988c
---

弧形滚动条组件ArcScrollBar，用于配合可滚动组件使用，如[ArcList](ts-container-arclist.md)、[List](ts-container-list.md)、[Grid](ts-container-grid.md)、[Scroll](ts-container-scroll.md)、[WaterFlow](ts-container-waterflow.md)。

说明

* 该组件从API version 18开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* ArcScrollBar不设置宽高时，采用父组件[LayoutConstraint](js-apis-arkui-framenode.md#layoutconstraint12)中的maxSize作为宽高。如果ArcScrollBar的父组件存在可滚动组件，如[ArcList](ts-container-arclist.md)、[List](ts-container-list.md)、[Grid](ts-container-grid.md)、[Scroll](ts-container-scroll.md)、[WaterFlow](ts-container-waterflow.md)，建议设置ArcScrollBar宽高，否则ArcScrollBar的宽高可能为无穷大。
* 该组件支持在Phone、PC/2in1、Tablet、TV、Wearable设备上使用。API version 22及以前版本，在Phone、PC/2in1、Tablet、TV上使用会编译告警，但可以正常运行。

## 子组件

PhonePC/2in1TabletTVWearable

不包含子组件。

## 接口

PhonePC/2in1TabletTVWearable

ArcScrollBar(options: ArcScrollBarOptions)

ArcScrollBar的构造函数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ArcScrollBarOptions](ts-basic-components-arcscrollbar.md#arcscrollbaroptions) | 是 | 滚动条组件参数。 |

## ArcScrollBarOptions

PhonePC/2in1TabletTVWearable

ArcScrollBar的构造函数参数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scroller | [Scroller](ts-container-scroll.md#scroller) | 否 | 否 | 可滚动组件的控制器，用于与可滚动组件进行绑定。 |
| state | [BarState](ts-appendix-enums.md#barstate) | 否 | 是 | 滚动条状态。  默认值：BarState.Auto |

说明

ArcScrollBar与可滚动组件需通过scroller进行绑定后方能实现联动，且ArcScrollBar与可滚动组件仅限于一对一的绑定方式。

## 示例

PhonePC/2in1TabletTVWearable

该示例通过ArcScrollBar与[Scroll](ts-container-scroll.md)组件联动，设置了弧形外置滚动条。

```
1. import { ArcScrollBar } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct ArcScrollBarExample {
6. private scroller: Scroller = new Scroller();
7. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

9. build() {
10. Stack({ alignContent: Alignment.Center }) {
11. Scroll(this.scroller) {
12. Flex({ direction: FlexDirection.Column }) {
13. ForEach(this.arr, (item: number) => {
14. Row() {
15. Text(item.toString())
16. .width('80%')
17. .height(60)
18. .backgroundColor('#3366CC')
19. .borderRadius(15)
20. .fontSize(16)
21. .textAlign(TextAlign.Center)
22. .margin({ top: 5 })
23. }
24. }, (item: number) => item.toString())
25. }.margin({ right: 15 })
26. }
27. .width('90%')
28. .scrollBar(BarState.Off)

30. ArcScrollBar({ scroller: this.scroller, state: BarState.Auto })
31. }
32. .width('100%')
33. .height('100%')
34. }
35. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/4KXUmn0vRFCG_VYs-YwBZg/zh-cn_image_0000002583479659.png?HW-CC-KV=V1&HW-CC-Date=20260428T000135Z&HW-CC-Expire=86400&HW-CC-Sign=A9419D5900C12E5C1271B9487D45940D87AF5A6902AB5633B6739DCA7F9D85CC)
