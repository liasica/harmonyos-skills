---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-focus_axis
title: 焦点轴事件
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用事件 > 基础输入事件 > 焦点轴事件
category: harmonyos-references
scraped_at: 2026-04-28T08:00:54+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:6eb4b8e3e5dde04b42734ae88ff7db7b762b46359361fd8eb8122aa73b25e153
---

焦点轴事件是指在与游戏手柄交互时，通过十字按键或者操作杆上报的轴事件，此轴事件通过获得焦点的组件分发并回调给应用。若组件默认可获焦，如Button，则不需要额外设置属性。若组件在默认情况下不可获焦，如Text和Image，可以通过将[focusable](ts-universal-attributes-focus.md#focusable)属性设置为true来启用焦点轴事件。

说明

本模块首批接口从API version 15开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## onFocusAxisEvent

PhonePC/2in1TabletTVWearable

onFocusAxisEvent(event: Callback<FocusAxisEvent>): T

给组件绑定焦点轴事件回调。绑定该方法的组件获焦后，游戏手柄上的摇杆、十字键等的操作会触发该回调。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | Callback<[FocusAxisEvent](ts-universal-events-focus_axis.md#focusaxisevent对象说明)> | 是 | 焦点轴事件回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## FocusAxisEvent对象说明

PhonePC/2in1TabletTVWearable

焦点轴事件的对象说明，继承于[BaseEvent](ts-gesture-customize-judge.md#baseevent8)。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| axisMap | Map<[AxisModel](ts-appendix-enums.md#axismodel15), number> | 否 | 否 | 焦点轴事件的轴值表。 |
| stopPropagation | Callback<void> | 否 | 否 | 阻塞[事件冒泡](../harmonyos-guides/arkts-interaction-basic-principles.md#事件冒泡)传递。 |

## 示例

PhonePC/2in1TabletTVWearable

该示例通过按钮设置了焦点轴事件，当按钮获得焦点时，操控游戏手柄的十字按键或者操作杆将触发onFocusAxisEvent回调。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct FocusAxisEventExample {
5. @State text: string = ''
6. @State axisValue: string = ''

8. aboutToAppear(): void {
9. this.getUIContext().getFocusController().activate(true)
10. }

12. aboutToDisappear(): void {
13. this.getUIContext().getFocusController().activate(false)
14. }

16. build() {
17. Column() {
18. Button('FocusAxisEvent')
19. .defaultFocus(true)
20. .onFocusAxisEvent((event: FocusAxisEvent) => {
21. let absX = event.axisMap.get(AxisModel.ABS_X);
22. let absY = event.axisMap.get(AxisModel.ABS_Y);
23. let absZ = event.axisMap.get(AxisModel.ABS_Z);
24. let absRz = event.axisMap.get(AxisModel.ABS_RZ);
25. let absGas = event.axisMap.get(AxisModel.ABS_GAS);
26. let absBrake = event.axisMap.get(AxisModel.ABS_BRAKE);
27. let absHat0X = event.axisMap.get(AxisModel.ABS_HAT0X);
28. let absHat0Y = event.axisMap.get(AxisModel.ABS_HAT0Y);
29. this.axisValue =
30. 'absX: ' + absX + '; absY: ' + absY + '; absZ: ' + absZ + '; absRz: ' + absRz + '; absGas: ' + absGas +
31. '; absBrake: ' + absBrake + '; absHat0X: ' + absHat0X + '; absHat0Y: ' + absHat0Y;
32. this.text = JSON.stringify(event);
33. })
34. Text(this.axisValue).padding(15)
35. Text(this.text).padding(15)
36. }.height(300).width('100%').padding(35)
37. }
38. }
```

游戏手柄摇杆移动时：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/0ZFHP-b5R1G7rd7vtvsewQ/zh-cn_image_0000002552799816.png?HW-CC-KV=V1&HW-CC-Date=20260428T000053Z&HW-CC-Expire=86400&HW-CC-Sign=AE8A3CEBAFAEE115608BAEE2CD7CE2E85853DBDC24F9D9614DF8938D3A9F2B0B)
