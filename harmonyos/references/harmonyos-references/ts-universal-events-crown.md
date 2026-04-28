---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-crown
title: 表冠事件
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用事件 > 基础输入事件 > 表冠事件
category: harmonyos-references
scraped_at: 2026-04-28T08:00:54+08:00
doc_updated_at: 2026-04-02
content_hash: sha256:f1d88ede1fd5a6b9efd3d3ded4cf4fc307ee720d451546ed46bfc2450d3ae162
---

指旋转表冠时触发的事件，事件的分发依赖于应用焦点，开发者可以通过[焦点事件](ts-universal-focus-event.md)自定义事件处理。

说明

* 本模块首批接口从API version 18开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 手动旋转表冠以触发其存在默认的交互逻辑，例如旋转手表的表冠后，滚动条会根据旋转表冠的旋转方向进行滚动。
* 组件收到表冠事件的前提是该组件获焦，焦点控制可以通过[focusable](ts-universal-attributes-focus.md#focusable)、[defaultFocus](ts-universal-attributes-focus.md#defaultfocus9)、[focusOnTouch](ts-universal-attributes-focus.md#focusontouch9)进行管理。
* 仅穿戴设备支持该事件。
* 默认支持表冠事件的组件: [Slider](ts-basic-components-slider.md)、[DatePicker](ts-basic-components-datepicker.md)、[TextPicker](ts-basic-components-textpicker.md)、 [TimePicker](ts-basic-components-timepicker.md)、[Scroll](ts-container-scroll.md)、[List](ts-container-list.md)、[Grid](ts-container-grid.md)、[WaterFlow](ts-container-waterflow.md)、[ArcList](ts-container-arclist.md)、[Refresh](ts-container-refresh.md)和[ArcSwiper](ts-container-arcswiper.md)。

## onDigitalCrown

PhonePC/2in1TabletTVWearable

onDigitalCrown(handler: Optional<Callback<CrownEvent>>): T

组件获焦以后旋转表冠时触发该回调。

说明

该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | Optional<Callback<[CrownEvent](ts-universal-events-crown.md#crownevent对象说明)>> | 是 | 获得[CrownEvent](ts-universal-events-crown.md#crownevent对象说明)对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## CrownEvent对象说明

PhonePC/2in1TabletTVWearable

组件接收表冠事件的数据结构。内容包括时间戳、旋转角速度、旋转角度、表冠动作和阻止事件冒泡。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| timestamp | number | 否 | 否 | 时间戳。 |
| angularVelocity | number | 否 | 否 | 旋转角速度，每秒转的角度(°/s)。 |
| degree | number | 否 | 否 | 相对旋转角度。  单位：度。  取值范围:[-360, 360]。 |
| action | [CrownAction](ts-appendix-enums.md#crownaction18) | 否 | 否 | 表冠动作。 |
| stopPropagation | Callback<void> | 否 | 否 | 阻止[事件冒泡](../harmonyos-guides/arkts-interaction-basic-principles.md#事件冒泡)。 |

## 示例

PhonePC/2in1TabletTVWearable

该示例实现了组件注册表冠事件，接收表冠事件数据上报内容。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct CityList {
5. @State message: string = "onDigitalCrown";

7. build() {
8. Column() {
9. Row() {
10. Stack() {
11. Text(this.message)
12. .fontSize(20)
13. .fontColor(Color.White)
14. .backgroundColor("#262626")
15. .textAlign(TextAlign.Center)
16. .focusable(true)
17. .focusOnTouch(true)
18. .defaultFocus(true)
19. .borderWidth(2)
20. .width(223)
21. .height(223)
22. .borderRadius(110)
23. .onDigitalCrown((event: CrownEvent) => {
24. event.stopPropagation();
25. this.message = "CrownEvent\n\n" + JSON.stringify(event);
26. console.info(`action: ${event.action}, angularVelocity: ${event.angularVelocity}, degree: ${event.degree}, timestamp: ${event.timestamp}`);
27. })
28. }.width("100%").height("100%")
29. }.width("100%").height("100%")
30. }
31. }
32. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/gXQsb8xTSiOPLfi44aisBw/zh-cn_image_0000002583477955.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000053Z&HW-CC-Expire=86400&HW-CC-Sign=4459A918CEAEA8B078C1781E7CF015E610926D02BBFF9F796E1AA8559B4541DD)
