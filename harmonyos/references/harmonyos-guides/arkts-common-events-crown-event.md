---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-events-crown-event
title: 支持表冠输入事件
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 添加交互响应 > 输入设备与事件 > 支持表冠输入事件
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e58bc5a7b3829db9d4625bf38b15616513dd4406e39f2273698a6cf452dd234e
---

表冠事件从API version 18开始支持，是指通过旋转表冠触发的事件，通过硬件采样频率上报旋转角度的变化。

表冠事件分发依赖于应用内组件焦点，只有拥有焦点的组件才能接收到该事件。因此，接收此事件的组件应正确管理其焦点状态，并通过[onFocus](../harmonyos-references/ts-universal-focus-event.md#onfocus)和[onBlur](../harmonyos-references/ts-universal-focus-event.md#onblur)接口监听自身焦点状态变化。当正在接收表冠事件的组件失焦时，接下来的表冠事件都不会再发送给这个组件。

目前，系统中一些组件已默认支持与表冠的交互，例如，旋转手表表冠后，滚动条会根据表冠的旋转方向滚动。

当前，默认支持表冠事件的组件包括： [Slider](../harmonyos-references/ts-basic-components-slider.md)、[DatePicker](../harmonyos-references/ts-basic-components-datepicker.md)、[TextPicker](../harmonyos-references/ts-basic-components-textpicker.md)、 [TimePicker](../harmonyos-references/ts-basic-components-timepicker.md)、[Scroll](../harmonyos-references/ts-container-scroll.md)、[List](../harmonyos-references/ts-container-list.md)、[Grid](../harmonyos-references/ts-container-grid.md)、[WaterFlow](../harmonyos-references/ts-container-waterflow.md)、[ArcList](../harmonyos-references/ts-container-arclist.md)、[Refresh](../harmonyos-references/ts-container-refresh.md)和[Swiper](../harmonyos-references/ts-container-swiper.md)。

此外，应用也可以自行通过[onDigitalCrown](../harmonyos-references/ts-universal-events-crown.md#ondigitalcrown)接口感知表冠事件的上报。

其中，event参数提供表冠事件的时间戳、旋转角速度、旋转角度和[表冠动作](../harmonyos-references/ts-appendix-enums.md#crownaction18)信息。

说明

* 当前仅Wearable设备支持表冠事件。
* 组件对表冠事件的接收受自身获焦状态影响，接收到BEGIN后，如果失焦，则无法继续再接收到后续的UPDATE和END。

当组件需要获取旋转角度等信息时，可以通过onDigitalCrown接收表冠事件来获得上报信息。以下以Text组件为例，介绍表冠事件开发的基本步骤及开发过程中需要注意的事项。

1. 组件获焦

   确保接收事件的组件获焦，可以通过使用[focusable](../harmonyos-references/ts-universal-attributes-focus.md#focusable)、[defaultFocus](../harmonyos-references/ts-universal-attributes-focus.md#defaultfocus9)、[focusOnTouch](../harmonyos-references/ts-universal-attributes-focus.md#focusontouch9)等方法来实现。如需更详细的焦点控制信息，请参考[焦点控制](../harmonyos-references/ts-universal-attributes-focus.md)文档。

   ```
   1. Text(this.message)
   2. .fontSize(20)
   3. .fontColor(Color.White)
   4. .backgroundColor("#262626")
   5. .textAlign(TextAlign.Center)
   6. .focusable(true)
   7. .focusOnTouch(true)
   8. .defaultFocus(true)
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/CrownEventsProject/entry/src/main/ets/pages/Index.ets#L28-L37)
2. 注册事件回调

   接收表冠事件需要注册表冠事件回调，当触发表冠事件时会执行回调函数。

   ```
   1. .onDigitalCrown((event: CrownEvent) => {
   2. // ···
   3. })
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/CrownEventsProject/entry/src/main/ets/pages/Index.ets#L42-L54)
3. 事件字段的含义

   表冠事件提供了时间戳，旋转角速度，旋转角度和表冠动作。此外表冠事件会触发事件冒泡，可通过[stopPropagation](../harmonyos-references/ts-universal-events-crown.md#crownevent对象说明)阻止事件冒泡。

   ```
   1. event.stopPropagation();
   2. this.message = "CrownEvent\n\n" + JSON.stringify(event);
   3. hilog.debug(0x0000, 'Tag',
   4. "action:%{public}d, angularVelocity:%{public}f, degree:%{public}f, timestamp:%{public}f",
   5. event.action, event.angularVelocity, event.degree, event.timestamp);
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/CrownEventsProject/entry/src/main/ets/pages/Index.ets#L45-L51)

**完整示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. @State message: string = 'onDigitalCrown';

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
26. hilog.debug(0x0000, 'Tag',
27. "action:%{public}d, angularVelocity:%{public}f, degree:%{public}f, timestamp:%{public}f",
28. event.action, event.angularVelocity, event.degree, event.timestamp);
29. })
30. }.width("100%").height("100%")
31. }.width("100%").height("100%")
32. }
33. }
34. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/HiZ5a24UTRW3jNhRvfWjnA/zh-cn_image_0000002589244253.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052804Z&HW-CC-Expire=86400&HW-CC-Sign=10000F3B4CEC77AB499149995C0EEC99B3ED98B6B62CE3ECE91598503E0F0013)
