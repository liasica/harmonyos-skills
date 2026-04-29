---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-ui-picker-component
title: UIPickerComponent
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 按钮与选择 > UIPickerComponent
category: harmonyos-references
scraped_at: 2026-04-29T13:51:59+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f88e106266e07cdc964918e498a082f549b2d286986c5b3b1423f04dd2199235
---

UIPickerComponent容器是用于实现用户选择操作的组件。它支持从一组有限的选项中让用户进行单选，可应用于时间选择、日期选择、地区选择、状态选择等多种场景。UIPickerComponent容器的显示效果为立体滚轮样式，支持选项按需定制，包括文本类型、图片类型和图文组合类型。

说明

* 该组件从API version 22开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* UIPickerComponent容器的选项行高固定为40vp，最多可显示7个选项。由于显示效果为立体滚轮样式，因此除选中项外的其他选项会进行不同角度的旋转，实际的可视高度会小于40vp。
* UIPickerComponent容器的[height](ts-universal-attributes-size.md#height)建议设置为200vp。当设置的高度大于等于该建议值时，可完全显示7个选项；小于该建议值时，显示范围会从上下边缘向中间裁剪，可显示的选项数量也会相应减少，始终保持选中项垂直居中。
* 当UIPickerComponent容器未设置[width](ts-universal-attributes-size.md#width)时，取当前视图中可见子组件的最大宽度作为容器宽度。建议为UIPickerComponent容器设置宽度，或为每个子组件设置相同宽度，以避免滑动过程中容器宽度动态发生变化，影响显示效果。
* UIPickerComponent容器的子组件的对齐方式固定为居中对齐，不支持通过[align](ts-universal-attributes-location.md#align)属性改变子组件的对齐方式。
* UIPickerComponent容器当前不支持智能手表设备。

## 子组件

PhonePC/2in1TabletTVWearable

* 支持多个子组件。
* 支持子组件类型：[Text](ts-basic-components-text.md)、[Image](ts-basic-components-image.md)、[Row](ts-container-row.md)和[SymbolGlyph](ts-basic-components-symbolglyph.md)。
* 支持渲染控制类型：[if/else](../harmonyos-guides/arkts-rendering-control-ifelse.md)和[ForEach](../harmonyos-guides/arkts-rendering-control-foreach.md)。

说明

* 开发者在使用Row容器作为子组件时，Row容器中仅支持包含Text、Image、SymbolGlyph基础组件，包含其他容器组件可能会影响显示效果或滑动功能异常。
* 统计子组件的个数时，不包含Row容器内的子组件，Row容器及其子组件共同视为1个子组件。
* 子组件为Text、Image、SymbolGlyph时，[height](ts-universal-attributes-size.md#height)属性不生效，固定为40vp。
* 子组件为Row容器时，Row容器的[height](ts-universal-attributes-size.md#height)属性不生效，固定为40vp，Row容器内的子组件[height](ts-universal-attributes-size.md#height)属性能正常生效，最终显示效果由Row容器决定。
* 图文组合类型选项需要使用Row容器包含图片和文本组件。使用图文组合类型选项时，建议将图片的[height](ts-universal-attributes-size.md#height)设置为40vp及以下，避免图片较大时被裁剪。
* UIPickerComponent容器内所有文本组件（包括Row容器内的文本组件）的fontSize属性默认为20fp。用户设置将覆盖默认值，设置异常值时以文本组件[fontSize](ts-basic-components-text.md#fontsize)处理的结果为准。建议统一设置或不设置fontSize以保证良好的显示效果。

## 接口

PhonePC/2in1TabletTVWearable

UIPickerComponent(options?: UIPickerComponentOptions)

创建UIPickerComponent容器，其选中项由options参数中的selectedIndex属性值决定。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [UIPickerComponentOptions](ts-container-ui-picker-component.md#uipickercomponentoptions对象说明) | 否 | 配置UIPickerComponent容器的参数。 |

## UIPickerComponentOptions对象说明

PhonePC/2in1TabletTVWearable

UIPickerComponent容器的参数说明。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| selectedIndex | number | 否 | 是 | 选中项的索引值。  取值范围：[0, 子组件的个数-1]内的整数。不在取值范围内时，使用默认值；设置小数时，使用向下取整后的整数。  默认值：0  **说明：**  统计子组件的个数时，不包含Row容器内的子组件，Row容器及其子组件共同视为1个子组件。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### canLoop

PhonePC/2in1TabletTVWearable

canLoop(isLoop: Optional<boolean>)

设置选项列是否可循环滚动。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isLoop | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 是否可循环滚动。  - true：可循环滚动。  - false：不可循环滚动。  默认值：true  当isLoop的值为undefined时，使用默认值。  如果子组件的个数小于8个，无论isLoop设置为true还是false，都不会循环滚动。 |

### enableHapticFeedback

PhonePC/2in1TabletTVWearable

enableHapticFeedback(enable: Optional<boolean>)

设置是否开启触控反馈。

开启触控反馈时，需要在工程的src/main/module.json5文件的"module"内配置requestPermissions字段开启振动权限，配置如下：

```
1. "requestPermissions": [
2. {
3. "name": "ohos.permission.VIBRATE",
4. }
5. ]
```

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 设置是否开启触控反馈。  - true：开启触控反馈。  - false：不开启触控反馈。  默认值：true  当enable的值为undefined时，使用默认值。  开启后，是否存在触控反馈取决于系统硬件支持情况。 |

### selectionIndicator

PhonePC/2in1TabletTVWearable

selectionIndicator(style: Optional<PickerIndicatorStyle>)

设置选中项指示器的样式。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[PickerIndicatorStyle](ts-container-ui-picker-component.md#pickerindicatorstyle对象说明)> | 是 | 选中项指示器的样式。  默认值：  {  type: PickerIndicatorType.BACKGROUND,  borderRadius: {  value:12,  unit:LengthUnit.vp  },  backgroundColor: 'sys.color.comp\_background\_tertiary'  }  当style的值为undefined时，使用默认值。 |

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](ts-component-general-events.md)外，还支持以下事件：

### onChange

PhonePC/2in1TabletTVWearable

onChange(callback: Optional<OnUIPickerComponentCallback>)

滑动选择器选项时，若选中项发生变化，触发该事件。

说明

如果某个选项有一半以上的区域进入选中项区域内，则该选项成为选中项。

选中项区域可通过设置[selectionIndicator](ts-container-ui-picker-component.md#selectionindicator)进行标识。如果设置选中项指示器为背景，则背景区域即为选中项区域。如果设置选中项指示器为分割线，则上下分割线的中心线内的区域为选中项区域。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[OnUIPickerComponentCallback](ts-container-ui-picker-component.md#onuipickercomponentcallback)> | 是 | 当选中项发生变化时触发的回调函数。  当callback的值为undefined时，不使用回调函数。 |

### onScrollStop

PhonePC/2in1TabletTVWearable

onScrollStop(callback: Optional<OnUIPickerComponentCallback>)

选择器滑动停止时，触发该事件。选择器滑动停止指某次行为触发的滑动动画完全结束。如果某次滑动动画还未结束时又触发了新的滑动动画，则不属于滑动停止。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[OnUIPickerComponentCallback](ts-container-ui-picker-component.md#onuipickercomponentcallback)> | 是 | 当选择器滑动停止时触发的回调函数。  当callback的值为undefined时，不使用回调函数。 |

## PickerIndicatorStyle对象说明

PhonePC/2in1TabletTVWearable

选中项指示器样式的参数说明。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [PickerIndicatorType](ts-container-ui-picker-component.md#pickerindicatortype枚举说明) | 否 | 否 | 选中项指示器的类型。  默认值：PickerIndicatorType.BACKGROUND  当type的值为小数时，使用向下取整后的整数；当type的值不在PickerIndicatorType枚举范围内时，使用默认值。 |
| strokeWidth | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 分割线的线宽。  默认值：2.0px  单位：与LengthMetrics一致。  取值范围：[0, 选中项高度的一半（即20vp）]。strokeWidth小于0或大于选中项高度的一半时使用默认值。不支持“百分比”类型。  **说明：**  1. 当type为PickerIndicatorType.DIVIDER时生效。  2. 通过LengthMetrics.resource方式设置时，使用非长度属性的值会按照0vp处理。 |
| dividerColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 分割线的颜色。  默认值：'sys.color.comp\_divider'  **说明：**  当type为PickerIndicatorType.DIVIDER时生效。 |
| startMargin | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 分割线与UIPickerComponent容器侧边起始端的距离。  默认值：0  单位：与LengthMetrics一致。  取值范围：startMargin与endMargin之和不得超过UIPickerComponent容器的宽度。设置小于0或startMargin与endMargin之和超过UIPickerComponent容器的宽度时，使用默认值。不支持“百分比”类型。  **说明：**  当type为PickerIndicatorType.DIVIDER时生效。 |
| endMargin | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 分割线与UIPickerComponent容器侧边结束端的距离。  默认值：0  单位：与LengthMetrics一致。  取值范围：startMargin与endMargin之和不得超过UIPickerComponent容器的宽度。设置小于0或startMargin与endMargin之和超过UIPickerComponent容器的宽度时，使用默认值。不支持“百分比”类型。  **说明：**  当type为PickerIndicatorType.DIVIDER时生效。 |
| backgroundColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 选中项背景的颜色。  默认值：'sys.color.comp\_background\_tertiary'  **说明：**  当type为PickerIndicatorType.BACKGROUND时生效。 |
| borderRadius | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | [BorderRadiuses](ts-types.md#borderradiuses9) | [LocalizedBorderRadiuses](ts-types.md#localizedborderradiuses12) | 否 | 是 | 选中项背景的边框圆角半径。  默认值：{ value:12, unit:LengthUnit.vp }，即四个圆角半径均为12vp。  取值范围：取选中项的宽和高之中较小的边长为x，最大不超过x的一半。当取值小于0时，使用默认值；当取值大于最大值时，使用最大值。  **说明：**  1. 当type为PickerIndicatorType.BACKGROUND时生效。  2. [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12)：统一设置四个圆角半径的大小和单位。  3. [BorderRadiuses](ts-types.md#borderradiuses9)：单独设置四个圆角半径的大小（单位为vp）。  4. [LocalizedBorderRadiuses](ts-types.md#localizedborderradiuses12)：单独设置四个圆角半径的大小和单位。 |

## PickerIndicatorType枚举说明

PhonePC/2in1TabletTVWearable

设置选中项指示器的类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 22开始，该类型支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BACKGROUND | 0 | 通过给选中项添加背景，标识选中项。 |
| DIVIDER | 1 | 通过在选中项的上下边缘添加分割线，标识选中项。 |

## OnUIPickerComponentCallback

PhonePC/2in1TabletTVWearable

type OnUIPickerComponentCallback = (selectedIndex: number) => void

定义[onChange](ts-container-ui-picker-component.md#onchange)和[onScrollStop](ts-container-ui-picker-component.md#onscrollstop)事件的回调类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| selectedIndex | number | 是 | 当前选中项的索引值。  取值范围：[0, 子组件的个数-1]内的整数。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（切换循环滚动和开关触控反馈）

从API version 22开始，该示例通过点击按钮的方式实现切换UIPickerComponent容器的循环滚动和开启/关闭触控反馈功能。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct UIPickerComponentAttrsExample {
5. private dataArray: string[] = [];
6. @State loop: boolean = true;
7. @State hapticFeedback: boolean = true;

9. aboutToAppear(): void {
10. // 构造选项数据
11. for (let i = 1; i <= 10; i++) {
12. this.dataArray.push(i.toString())
13. }
14. }

16. build() {
17. Column() {
18. Row() {
19. UIPickerComponent() {
20. ForEach(this.dataArray, (item: string) => {
21. Text(item)
22. })
23. }
24. // 配置选项列表循环
25. .canLoop(this.loop)
26. // 配置触控音振反馈
27. .enableHapticFeedback(this.hapticFeedback)
28. .width('70%')
29. }

31. Column() {
32. Row() {
33. Toggle({ type: ToggleType.Switch, isOn: true })
34. .onChange((isOn: boolean) => {
35. this.loop = isOn;
36. })
37. Text('canLoop').fontSize(20)
38. }
39. .width('70%')

41. Row() {
42. Toggle({ type: ToggleType.Switch, isOn: true })
43. .onChange((isOn: boolean) => {
44. this.hapticFeedback = isOn;
45. })
46. Text('enableHapticFeedback').fontSize(20)
47. }
48. .width('70%')
49. }

51. }
52. .width('100%')
53. }
54. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/cco0on7ASGSSbtOFeOkbFw/zh-cn_image_0000002558606566.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055156Z&HW-CC-Expire=86400&HW-CC-Sign=4C34A62A2C8E3441980B116289C4010F9E9D6710F5E0C15E1FDC35A58D27F208)

### 示例2（设置事件回调）

从API version 22开始，该示例基于状态选择，实现了UIPickerComponent容器的onChange和onScrollStop事件回调。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct UIPickerComponentEventsExample {
5. // 构造状态选项数据
6. private dataArray: string[] = ['待办', '进行中', '已完成'];
7. @State onChangeDesc: string = '';
8. @State onScrollStopDesc: string = '';

10. build() {
11. Column() {
12. Row() {
13. UIPickerComponent() {
14. ForEach(this.dataArray, (item: string) => {
15. Text(item)
16. })
17. }
18. // 配置onChange事件回调
19. .onChange((selectedIndex: number) => {
20. this.onChangeDesc = 'on change: ' + selectedIndex
21. })
22. // 配置onScrollStop事件回调
23. .onScrollStop((selectedIndex: number) => {
24. this.onScrollStopDesc = 'on scroll stop: ' + selectedIndex
25. })
26. .width('70%')
27. }

29. Column() {
30. Text(this.onChangeDesc)
31. Text(this.onScrollStopDesc)
32. }

34. }
35. .width('100%')
36. }
37. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/ssDGVodLSuapy_A3C-bhDQ/zh-cn_image_0000002589326093.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055156Z&HW-CC-Expire=86400&HW-CC-Sign=A206149448F396B0A02A7A7F62EE501B99A58391E8CF9D87DFA68C2F6E181BA3)

### 示例3（设置选中项索引值）

从API version 22开始，该示例实现了设置UIPickerComponent容器的选中项索引值。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct UIPickerComponentSelectedIndexExample {
5. private dataArray: string[] = [];
6. @State selectedIndex: number = 0;

8. aboutToAppear(): void {
9. // 构造选项数据
10. for (let i = 1; i <= 10; i++) {
11. this.dataArray.push(i.toString())
12. }
13. }

15. build() {
16. Column() {
17. Row() {
18. UIPickerComponent({
19. // 配置选中项索引值
20. selectedIndex: this.selectedIndex
21. }) {
22. ForEach(this.dataArray, (item: string) => {
23. Text(item)
24. })
25. }
26. .onChange((selectedIndex: number) => {
27. this.selectedIndex = selectedIndex
28. })
29. .onScrollStop((selectedIndex: number) => {
30. this.selectedIndex = selectedIndex
31. })
32. .width('70%')
33. }

35. Column() {
36. Text('selectedIndex: ' + this.selectedIndex)
37. }

39. }
40. .width('100%')
41. }
42. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/gnuch8VyTKu2rJDJmEQ69A/zh-cn_image_0000002589246035.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055156Z&HW-CC-Expire=86400&HW-CC-Sign=C1EEF0460D8143BEE01B4B3C2508D1F7B2B4836101ECBF6C5D5BAC899C1E30BE)

### 示例4（设置选中项指示器）

从API version 22开始，该示例实现了设置UIPickerComponent容器的选中项指示器。具体包括：在使用背景指示器时，设置背景颜色、背景圆角；在使用分割线指示器时，设置分割线颜色、分割线宽度、起始侧边距、结束侧边距。

```
1. // xxx.ets
2. import { LengthMetrics } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct UIPickerComponentIndicatorExample {
7. private dataArray: string[] = [];
8. @State indicatorType: PickerIndicatorType | undefined = undefined;
9. @State bgColor: Color | undefined = undefined;
10. @State dividerColor: Color | undefined = undefined;
11. @State strokeWidth: LengthMetrics = LengthMetrics.px(2);
12. @State startMargin: LengthMetrics = LengthMetrics.px(2);
13. @State endMargin: LengthMetrics = LengthMetrics.px(2);
14. @State selectIndicator: PickerIndicatorStyle | undefined = undefined;
15. @State bgBorderRadius: LengthMetrics | BorderRadiuses | LocalizedBorderRadiuses | undefined = undefined
16. bgBorderRadiuses1: LengthMetrics = LengthMetrics.vp(10)
17. bgBorderRadiuses2: BorderRadiuses = {
18. topLeft: 10,
19. bottomLeft: 0,
20. topRight: 10,
21. bottomRight: 0,
22. }
23. bgBorderRadiuses3: LocalizedBorderRadiuses = {
24. topStart: LengthMetrics.vp(0),
25. bottomStart: LengthMetrics.vp(10),
26. topEnd: LengthMetrics.vp(0),
27. bottomEnd: LengthMetrics.vp(10)
28. }
29. private controller: TabsController = new TabsController();
30. @State curTabIndex: number = 0;

32. @Builder
33. dividerBuilder() {
34. Column() {
35. Row() {
36. Text('分割线线宽')
37. }.margin(2)

39. Row() {
40. Button('0')
41. .onClick(() => {
42. this.strokeWidth = LengthMetrics.px(0)
43. })
44. .fontSize(12)
45. .height(30)
46. .width(100)
47. .margin(2)
48. Button('10px')
49. .onClick(() => {
50. this.strokeWidth = LengthMetrics.px(10)
51. })
52. .fontSize(12)
53. .height(30)
54. .width(100)
55. .margin(2)
56. Button('10vp')
57. .onClick(() => {
58. this.strokeWidth = LengthMetrics.vp(10)
59. })
60. .fontSize(12)
61. .height(30)
62. .width(100)
63. .margin(2)
64. }

66. Row() {
67. Text('起始侧边距')
68. }.margin(2)

70. Row() {
71. Button('0')
72. .onClick(() => {
73. this.startMargin = LengthMetrics.px(0)
74. })
75. .fontSize(12)
76. .height(30)
77. .width(100)
78. .margin(2)
79. Button('10px')
80. .onClick(() => {
81. this.startMargin = LengthMetrics.px(10)
82. })
83. .fontSize(12)
84. .height(30)
85. .width(100)
86. .margin(2)
87. Button('10vp')
88. .onClick(() => {
89. this.startMargin = LengthMetrics.vp(10)
90. })
91. .fontSize(12)
92. .height(30)
93. .width(100)
94. .margin(2)
95. }

97. Row() {
98. Text('结束侧边距')
99. }.margin(2)

101. Row() {
102. Button('0')
103. .onClick(() => {
104. this.endMargin = LengthMetrics.px(0)
105. })
106. .fontSize(12)
107. .height(30)
108. .width(100)
109. .margin(2)
110. Button('10px')
111. .onClick(() => {
112. this.endMargin = LengthMetrics.px(10)
113. })
114. .fontSize(12)
115. .height(30)
116. .width(100)
117. .margin(2)
118. Button('10vp')
119. .onClick(() => {
120. this.endMargin = LengthMetrics.vp(10)
121. })
122. .fontSize(12)
123. .height(30)
124. .width(100)
125. .margin(2)
126. }

128. Row() {
129. Text('分割线颜色')
130. }

132. Row() {
133. Button('蓝色')
134. .onClick(() => {
135. this.dividerColor = Color.Blue
136. })
137. .fontSize(12)
138. .height(30)
139. .width(73)
140. .margin(2)
141. Button('黑色')
142. .onClick(() => {
143. this.dividerColor = Color.Black
144. })
145. .fontSize(12)
146. .height(30)
147. .width(73)
148. .margin(2)
149. }

151. Row() {
152. Button('不使用自定义设置')
153. .onClick(() => {
154. this.dividerColor = undefined
155. })
156. .fontSize(12)
157. .height(30)
158. .width(150)
159. .margin(2)
160. }
161. }
162. }

164. @Builder
165. backgroundBuilder() {
166. Column() {
167. Row() {
168. Text('圆角设置')
169. }.margin(2)

171. Column() {
172. Button('使用LengthMetrics，实现统一圆角')
173. .onClick(() => {
174. this.bgBorderRadius = this.bgBorderRadiuses1
175. })
176. .fontSize(12)
177. .height(30)
178. .width(300)
179. .margin(2)
180. Button('使用BorderRadiuses，实现上圆下方')
181. .onClick(() => {
182. this.bgBorderRadius = this.bgBorderRadiuses2
183. })
184. .fontSize(12)
185. .height(30)
186. .width(300)
187. .margin(2)
188. Button('使用LocalizedBorderRadiuses，实现上方下圆')
189. .onClick(() => {
190. this.bgBorderRadius = this.bgBorderRadiuses3
191. })
192. .fontSize(12)
193. .height(30)
194. .width(300)
195. .margin(2)
196. }.margin(2)

198. Row() {
199. Text('背景色设置')
200. }.margin(2)

202. Row() {
203. Button('蓝色')
204. .onClick(() => {
205. this.bgColor = Color.Blue
206. })
207. .fontSize(12)
208. .height(30)
209. .width(73)
210. .margin(2)
211. Button('绿色')
212. .onClick(() => {
213. this.bgColor = Color.Green
214. })
215. .fontSize(12)
216. .height(30)
217. .width(73)
218. .margin(2)
219. }

221. Row() {
222. Button('不使用自定义设置')
223. .onClick(() => {
224. this.bgColor = undefined
225. })
226. .fontSize(12)
227. .height(30)
228. .width(150)
229. .margin(2)
230. }
231. }
232. }

234. aboutToAppear(): void {
235. // 构造选项数据
236. for (let i = 1; i <= 10; i++) {
237. this.dataArray.push(i.toString())
238. }
239. }

241. build() {
242. Column() {
243. Row() {
244. UIPickerComponent() {
245. ForEach(this.dataArray, (item: string) => {
246. Text(item)
247. })
248. }
249. // 配置选中项指示器
250. .selectionIndicator({
251. type: this.indicatorType,
252. strokeWidth: this.strokeWidth,
253. dividerColor: this.dividerColor,
254. startMargin: this.startMargin,
255. endMargin: this.endMargin,
256. backgroundColor: this.bgColor,
257. borderRadius: this.bgBorderRadius
258. })
259. .width('70%')
260. }
261. Tabs({ barPosition: BarPosition.Start, index: this.curTabIndex, controller: this.controller }) {
262. TabContent() {
263. this.backgroundBuilder()
264. }.tabBar('背景指示器')

266. TabContent() {
267. this.dividerBuilder()
268. }.tabBar('分割线指示器')
269. }
270. .vertical(false)
271. .barMode(BarMode.Fixed)
272. .barWidth(360)
273. .barHeight(56)
274. .animationDuration(400)
275. .onChange((index: number) => {
276. this.curTabIndex = index
277. if (this.curTabIndex == 1) {
278. this.indicatorType = PickerIndicatorType.DIVIDER
279. } else {
280. this.indicatorType = PickerIndicatorType.BACKGROUND
281. }
282. })
283. .height(LayoutPolicy.wrapContent)
284. .divider({ strokeWidth: 2 })
285. .margin({ top: 20 })
286. .backgroundColor('#F1F3F5')
287. }
288. .width('100%')
289. }
290. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/q6hAHQFoSeawU4LxGOWMQA/zh-cn_image_0000002558766226.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055156Z&HW-CC-Expire=86400&HW-CC-Sign=A125959A14AED4DBDF0C04DDB51720A1F7EF0F7B20A60F87485FFC8C2F7C8B89)

### 示例5（自定义月份选择器）

从API version 22开始，该示例使用UIPickerComponent容器嵌套文本子组件的方式实现月份选择器。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct MonthUIPickerComponentExample {
5. private fontSize: number | string | Resource = '20vp';
6. private monthArray: string[] = [];

8. aboutToAppear(): void {
9. // 构造选项数据
10. for (let i = 1; i <= 12; i++) {
11. this.monthArray.push(i + '月')
12. }
13. }

15. build() {
16. Column() {
17. UIPickerComponent() {
18. ForEach(this.monthArray, (item: string) => {
19. Text(item)
20. .fontSize(this.fontSize)
21. .textAlign(TextAlign.Center)
22. .fontColor(Color.Black)
23. })
24. }
25. .width('70%')
26. // 配置选项列表循环
27. .canLoop(true)
28. // 配置触控音振反馈为关闭
29. .enableHapticFeedback(false)
30. // 配置选中项的指示器标识为分割线
31. .selectionIndicator({ type: PickerIndicatorType.DIVIDER })
32. // 订阅选中项改变事件
33. .onChange((idx: number) => {
34. console.info('UIPickerComponent item changed: ' + this.monthArray[idx])
35. })
36. // 订阅滑动停止事件
37. .onScrollStop((idx: number) => {
38. console.info('UIPickerComponent scroll stopped: ' + this.monthArray[idx])
39. })
40. }
41. .width('100%')
42. }
43. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/2NO8XibiQoG99m7jUVBw7g/zh-cn_image_0000002558606568.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055156Z&HW-CC-Expire=86400&HW-CC-Sign=528886C8B062200C36FFE00A90601F21E5A7C1AF3FD6F2BAB4C3E6F661F368D5)

### 示例6（自定义地区选择器）

从API version 22开始，该示例使用多列UIPickerComponent容器组合实现地区选择器。

```
1. // xxx.ets

3. type RegionDict = Record<string, Record<string, Array<string>>>;
4. // 定义地区字典
5. let regionData: RegionDict = {
6. '辽宁省': {
7. '沈阳市': ['沈河区', '和平区', '浑南区'],
8. '大连市': ['中山区', '金州区', '长海县']
9. },
10. '吉林省': {
11. '长春市': ['南关区', '宽城区', '朝阳区'],
12. '四平市': ['铁西区', '铁东区', '梨树县']
13. },
14. '黑龙江省': {
15. '哈尔滨市': ['道里区', '道外区', '南岗区'],
16. '牡丹江市': ['东安区', '西安区', '爱民区']
17. },
18. };

20. @Entry
21. @Component
22. struct RegionUIPickerComponentExample {
23. @State provinceIndex: number = 0;
24. @State cityIndex: number = 0;
25. @State countyIndex: number = 0;
26. @State provinces: Array<string> = [];
27. @State cities: Array<string> = [];
28. @State counties: Array<string> = [];

30. aboutToAppear(): void {
31. this.provinces = Object.keys(regionData);
32. this.flushCityColumn()
33. }

35. flushCityColumn() {
36. let currentProvince = this.provinces[this.provinceIndex]
37. this.cities = Object.keys(regionData[currentProvince])
38. this.cityIndex = 0
39. this.flushCountyColumn()
40. }

42. flushCountyColumn() {
43. let currentProvince = this.provinces[this.provinceIndex]
44. let currentCity = this.cities[this.cityIndex]
45. this.counties = regionData[currentProvince][currentCity]
46. this.countyIndex = 0
47. }

49. build() {
50. Column() {
51. Row() {
52. // 省级
53. UIPickerComponent({
54. selectedIndex: this.provinceIndex
55. }) {
56. ForEach(this.provinces, (province: string) => {
57. Text(province)
58. })
59. }
60. .onChange((selectedIndex: number) => {
61. this.provinceIndex = selectedIndex
62. this.flushCityColumn()

64. })
65. .onScrollStop((selectedIndex: number) => {
66. this.provinceIndex = selectedIndex
67. })
68. .selectionIndicator({ type: PickerIndicatorType.DIVIDER })
69. .width('25%')

71. // 地级
72. UIPickerComponent({
73. selectedIndex: this.cityIndex
74. }) {
75. ForEach(this.cities, (city: string) => {
76. Text(city)
77. })
78. }
79. .onChange((selectedIndex: number) => {
80. this.cityIndex = selectedIndex
81. this.flushCountyColumn()
82. })
83. .onScrollStop((selectedIndex: number) => {
84. this.cityIndex = selectedIndex
85. })
86. .selectionIndicator({ type: PickerIndicatorType.DIVIDER })
87. .width('25%')

89. // 县级
90. UIPickerComponent({
91. selectedIndex: this.countyIndex
92. }) {
93. ForEach(this.counties, (county: string) => {
94. Text(county)
95. })
96. }
97. .onChange((selectedIndex: number) => {
98. this.countyIndex = selectedIndex
99. })
100. .onScrollStop((selectedIndex: number) => {
101. this.countyIndex = selectedIndex
102. })
103. .selectionIndicator({ type: PickerIndicatorType.DIVIDER })
104. .width('25%')
105. }
106. }
107. .width('100%')
108. }
109. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/okmCn2KnSUGb1ABZlPtuxg/zh-cn_image_0000002589326095.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055156Z&HW-CC-Expire=86400&HW-CC-Sign=82115AC96F90657342C1B9E31F2000FDD598158D59FF146CCDB57D547DA1F903)

### 示例7（自定义选项类型）

从API version 22开始，该示例使用UIPickerComponent容器实现不同选项类型的选择器，包含文本选择器、图片选择器、图文组合选择器。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct UIPickerComponentExample {
5. @State textList: string[] =
6. ['text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'text7', 'text8'];
7. // 以下$r('sys.media.*')资源文件需要替换为开发者所需的图像资源文件。
8. @State imageList: Resource[] =
9. [$r('sys.media.ohos_ic_normal_white_grid_audio'), $r('sys.media.ohos_ic_normal_white_grid_calendar'),
10. $r('sys.media.ohos_ic_normal_white_grid_compress'), $r('sys.media.ohos_ic_normal_white_grid_doc'),
11. $r('sys.media.ohos_ic_normal_white_grid_flac'), $r('sys.media.ohos_ic_normal_white_grid_folder'),
12. $r('sys.media.ohos_ic_normal_white_grid_html'), $r('sys.media.ohos_ic_normal_white_grid_image')];
13. // 以下$r('sys.symbol.*')资源文件需要替换为开发者所需的图像资源文件。
14. @State symbolList: Resource[] =
15. [$r('sys.symbol.calendar_01'), $r('sys.symbol.calendar_02'), $r('sys.symbol.calendar_03'),
16. $r('sys.symbol.calendar_04'), $r('sys.symbol.calendar_05'), $r('sys.symbol.calendar_06'),
17. $r('sys.symbol.calendar_07'), $r('sys.symbol.calendar_08')];
18. private controller: TabsController = new TabsController();
19. @State curTabIndex: number = 0;

21. @Builder
22. ImagePicker() {
23. Column() {
24. UIPickerComponent() {
25. ForEach(this.imageList, (item: Resource) => {
26. Image(item)
27. })
28. }
29. .margin(20)
30. .width(200)
31. }
32. }

34. @Builder
35. TextPicker() {
36. Column() {
37. UIPickerComponent() {
38. ForEach(this.textList, (item: string) => {
39. Text(item)
40. })
41. }
42. .margin(20)
43. .width(200)
44. }
45. }

47. @Builder
48. HybridPicker() {
49. Column() {
50. UIPickerComponent() {
51. ForEach(this.symbolList, (item: Resource, index: number) => {
52. Row() {
53. SymbolGlyph(item)
54. .height('20vp')
55. Text(this.textList[index])
56. }
57. })
58. }
59. .margin(20)
60. .width(200)
61. }
62. }

64. build() {
65. Column() {
66. Tabs({ barPosition: BarPosition.Start, index: this.curTabIndex, controller: this.controller }) {
67. TabContent() {
68. this.TextPicker()
69. }.tabBar('文本选择器')

71. TabContent() {
72. this.ImagePicker()
73. }.tabBar('图片选择器')

75. TabContent() {
76. this.HybridPicker()
77. }.tabBar('图文组合选择器')
78. }
79. .vertical(true)
80. .divider({ strokeWidth: 1 })
81. .barMode(BarMode.Fixed)
82. .barWidth(140)
83. .barHeight(230)
84. .height(230)
85. .animationDuration(400)
86. }
87. }
88. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/krJH3xWXT0GbPQjIWFVKOw/zh-cn_image_0000002589246037.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055156Z&HW-CC-Expire=86400&HW-CC-Sign=3217507FED790CE6011722C523AF7BADF6492A1A9F3CE04F2D43696931415AD1)

### 示例8（自定义时间选择器）

从API version 22开始，该示例实现了一个时间选择器，功能包含设置切换是否循环滚动、切换是否显示秒数、切换是否使用24小时制、切换是否显示前导0，还可按照当前系统语言显示对应语言的内容，并根据语言习惯调整各列的显示顺序。

说明

* 该示例中，时间选择器的各列内容根据系统语言显示对应语言的内容，例如：英文系统显示AM/PM，中文系统显示上午/下午。
* 该示例中，时间选择器的各列根据系统语言调整显示顺序，例如：英文系统显示时/分/秒/AMPM，中文系统显示上下午/时/分/秒。

为实现"上下午"随系统语言切换，需要在工程的resource目录下添加对应语言的翻译，例如：

* 中文（默认）：在resource目录下创建base目录，在base目录下创建element目录，在element目录添加string.json文件（若文件已存在，请在文件中追加以下"name"-"value"键值对，请勿直接覆盖原文件）。文件内容如下：

  ```
  1. {
  2. "string": [
  3. {
  4. "name": "app_name",
  5. "value": "timePicker"
  6. },
  7. {
  8. "name": "am",
  9. "value": "上午"
  10. },
  11. {
  12. "name": "pm",
  13. "value": "下午"
  14. }
  15. ]
  16. }
  ```
* 英文：在resource目录下创建en目录，在en目录下创建element目录，在element目录添加string.json文件（若文件已存在，请在文件中追加以下"name"-"value"键值对，请勿直接覆盖原文件）。文件内容如下：

  ```
  1. {
  2. "string": [
  3. {
  4. "name": "app_name",
  5. "value": "timePicker"
  6. },
  7. {
  8. "name": "am",
  9. "value": "AM"
  10. },
  11. {
  12. "name": "pm",
  13. "value": "PM"
  14. }
  15. ]
  16. }
  ```
* 阿拉伯语：在resource目录下创建ar目录，在ar目录下创建element目录，在element目录下添加string.json文件（若文件已存在，请在文件中追加以下"name"-"value"键值对，请勿直接覆盖原文件）。文件内容如下：

  ```
  1. {
  2. "string": [
  3. {
  4. "name": "app_name",
  5. "value": "timePicker"
  6. },
  7. {
  8. "name": "am",
  9. "value": "ص"
  10. },
  11. {
  12. "name": "pm",
  13. "value": "م"
  14. }
  15. ]
  16. }
  ```
* 其他语言依此类推。

示例代码如下：

```
1. // xxx.ets
2. import { LengthMetrics } from '@kit.ArkUI';
3. import { i18n, intl } from '@kit.LocalizationKit';
4. import { commonEventManager } from '@kit.BasicServicesKit';

6. @Entry
7. @Component
8. struct TimeUIPickerComponentExample {
9. @State showSecond: boolean = false;
10. @State useMilitary: boolean = false;
11. @State zeroPrefix: boolean = true;
12. @State loop: boolean = true;
13. @State amPmAtLast: boolean = false
14. @State isRtl: boolean = false;

16. startBorderStyle: LocalizedBorderRadiuses = {
17. topStart: LengthMetrics.px(40),
18. bottomStart: LengthMetrics.px(40),
19. topEnd: LengthMetrics.px(0),
20. bottomEnd: LengthMetrics.px(0)
21. }
22. centerBorderStyle: LengthMetrics = LengthMetrics.px(0)
23. endBorderStyle: LocalizedBorderRadiuses = {
24. topStart: LengthMetrics.px(0),
25. bottomStart: LengthMetrics.px(0),
26. topEnd: LengthMetrics.px(40),
27. bottomEnd: LengthMetrics.px(40)
28. }
29. @State amPmBorder: LengthMetrics | LocalizedBorderRadiuses = this.startBorderStyle;
30. @State hourBorder: LengthMetrics | LocalizedBorderRadiuses = this.startBorderStyle;
31. @State minBorder: LengthMetrics | LocalizedBorderRadiuses = this.endBorderStyle;
32. @State secBorder: LengthMetrics | LocalizedBorderRadiuses = this.endBorderStyle;

34. @State amPmIndex: number = 0;
35. @State hourIndex: number = 0;
36. @State minIndex: number = 0;
37. @State secIndex: number = 0;

39. @State amPmArr: Array<string| undefined> = []
40. @State hourArr: Array<string> = []
41. @State minSecArr: Array<string> = []

43. @State currentTime: string = '';

45. sysLanguageChanged: boolean = false
46. zero: string = '0'
47. systemLanguage: string = i18n.System.getSystemLanguage();
48. // 使用系统当前区域ID创建NumberFormat对象
49. formatter: intl.NumberFormat = new intl.NumberFormat();

51. aboutToAppear(): void {
52. this.zero = this.formatter.format(0)
53. this.flushAmPmColumn()
54. this.flushHourColumn()
55. this.flushMinSecColumn()
56. this.flushCurrentTime()
57. this.flushBorderStyle()
58. let subscriber: commonEventManager.CommonEventSubscriber;
59. let subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
60. events: [commonEventManager.Support.COMMON_EVENT_LOCALE_CHANGED]
61. };
62. // 创建订阅者，监听系统语言变化
63. commonEventManager.createSubscriber(subscribeInfo)
64. .then((commonEventSubscriber: commonEventManager.CommonEventSubscriber) => {
65. console.info("CreateSubscriber");
66. subscriber = commonEventSubscriber;
67. commonEventManager.subscribe(subscriber, (err, data) => {
68. if (err) {
69. console.error(`Failed to subscribe common event. error code: ${err.code}, message: ${err.message}.`);
70. return;
71. }
72. this.formatter = new intl.NumberFormat();
73. this.zero = this.formatter.format(0)
74. this.sysLanguageChanged = true
75. this.systemLanguage = i18n.System.getSystemLanguage();
76. this.flushAmPmColumn()
77. this.flushHourColumn()
78. this.flushMinSecColumn()
79. this.flushCurrentTime()
80. this.flushBorderStyle()
81. })
82. })
83. .catch((err: BusinessError) => {
84. console.error(`CreateSubscriber failed, code is ${err.code}, message is ${err.message}`);
85. });
86. }

88. onPageShow(): void {
89. if (this.sysLanguageChanged) {
90. this.flushAmPmColumn()
91. this.flushCurrentTime()
92. this.flushBorderStyle()
93. this.sysLanguageChanged = false
94. }
95. }

97. buildColumnOptions(start: number, end: number, isHour: boolean = false) : string[] {
98. let newOptions: string[] = []
99. for (let i = start; i <= end; i++) {
100. if (isHour && i == 0 && !this.useMilitary) {
101. newOptions.push(this.formatter.format(12))
102. continue
103. }
104. if (this.zeroPrefix) {
105. newOptions.push(this.formatTime(i))
106. } else {
107. newOptions.push(this.formatter.format(i))
108. }
109. }
110. return newOptions
111. }

113. flushAmPmColumn() {
114. // 根据语言习惯设置amPm列是否放在最后
115. if (this.systemLanguage.startsWith('en') || this.systemLanguage == 'ug') {
116. this.amPmAtLast = true
117. } else {
118. this.amPmAtLast = false
119. }
120. this.amPmArr[0] = this.getUIContext().getHostContext()?.resourceManager.getStringSync($r('app.string.am').id)
121. this.amPmArr[1] = this.getUIContext().getHostContext()?.resourceManager.getStringSync($r('app.string.pm').id)
122. }

124. flushHourColumn() {
125. if (this.useMilitary) {
126. this.hourArr = this.buildColumnOptions(0, 23)
127. } else {
128. this.hourArr = this.buildColumnOptions(0, 11, true)
129. }
130. }

132. flushMinSecColumn() {
133. this.minSecArr = this.buildColumnOptions(0, 59)
134. }

136. flushBorderStyle() {
137. let realStartBorder = this.startBorderStyle
138. let realEndBorder = this.endBorderStyle
139. // 根据语言习惯设置镜像语言的时间顺序
140. if (this.systemLanguage == 'ar' || this.systemLanguage == 'ug') {
141. this.isRtl = true
142. realStartBorder = this.endBorderStyle
143. realEndBorder = this.startBorderStyle
144. } else {
145. this.isRtl = false
146. }
147. if (!this.useMilitary) {
148. if (this.amPmAtLast) {
149. this.amPmBorder = realEndBorder
150. this.hourBorder = realStartBorder
151. this.minBorder = this.centerBorderStyle
152. this.secBorder = this.centerBorderStyle
153. } else {
154. this.amPmBorder = realStartBorder
155. this.hourBorder = this.centerBorderStyle
156. if (this.showSecond) {
157. this.minBorder = this.centerBorderStyle
158. } else {
159. this.minBorder = realEndBorder
160. }
161. this.secBorder = realEndBorder
162. }
163. } else {
164. this.hourBorder = realStartBorder
165. if (this.showSecond) {
166. this.minBorder = this.centerBorderStyle
167. } else {
168. this.minBorder = realEndBorder
169. }
170. this.secBorder = realEndBorder
171. }
172. }

174. formatTime(time: number): string {
175. if (time < 10) {
176. return this.zero + this.formatter.format(time)
177. }
178. return this.formatter.format(time)
179. }

181. @Builder
182. buildAmPmColumn() {
183. UIPickerComponent({ selectedIndex: this.amPmIndex }) {
184. ForEach(this.amPmArr, (amPm: string) => {
185. Text(amPm)
186. })
187. }
188. .width('200px')
189. .canLoop(this.loop)
190. .selectionIndicator({
191. type: PickerIndicatorType.BACKGROUND,
192. borderRadius: this.amPmBorder
193. })
194. .onChange((selectedIndex: number) => {
195. this.amPmIndex = selectedIndex
196. this.flushCurrentTime()
197. })
198. .onScrollStop((selectedIndex: number) => {
199. this.amPmIndex = selectedIndex
200. this.flushCurrentTime()
201. })
202. }

204. @Builder
205. buildHourColumn() {
206. UIPickerComponent({ selectedIndex: this.hourIndex }) {
207. ForEach(this.hourArr, (hour: string) => {
208. Text(hour)
209. })
210. }
211. .width('200px')
212. .canLoop(this.loop)
213. .selectionIndicator({
214. type: PickerIndicatorType.BACKGROUND,
215. borderRadius: this.hourBorder
216. })
217. .onChange((selectedIndex: number) => {
218. this.hourIndex = selectedIndex
219. this.flushCurrentTime()
220. })
221. .onScrollStop((selectedIndex: number) => {
222. this.hourIndex = selectedIndex
223. this.flushCurrentTime()
224. })
225. }

227. @Builder
228. buildMinColumn() {
229. UIPickerComponent({ selectedIndex: this.minIndex }) {
230. ForEach(this.minSecArr, (min: string) => {
231. Text(min)
232. })
233. }
234. .width('200px')
235. .canLoop(this.loop)
236. .selectionIndicator({
237. type: PickerIndicatorType.BACKGROUND,
238. borderRadius: this.minBorder
239. })
240. .onChange((selectedIndex: number) => {
241. this.minIndex = selectedIndex
242. this.flushCurrentTime()
243. })
244. .onScrollStop((selectedIndex: number) => {
245. this.minIndex = selectedIndex
246. this.flushCurrentTime()
247. })
248. }

250. @Builder
251. buildSecColumn() {
252. UIPickerComponent({ selectedIndex: this.secIndex }) {
253. ForEach(this.minSecArr, (sec: string) => {
254. Text(sec)
255. })
256. }
257. .width('200px')
258. .canLoop(this.loop)
259. .selectionIndicator({
260. type: PickerIndicatorType.BACKGROUND,
261. borderRadius: this.secBorder
262. })
263. .onChange((selectedIndex: number) => {
264. this.secIndex = selectedIndex
265. this.flushCurrentTime()
266. })
267. .onScrollStop((selectedIndex: number) => {
268. this.secIndex = selectedIndex
269. this.flushCurrentTime()
270. })
271. }

273. flushCurrentTime() {
274. this.currentTime = ''
275. if (!this.useMilitary) {
276. this.currentTime += this.amPmArr[this.amPmIndex] + ' '
277. }
278. this.currentTime += this.hourArr[this.hourIndex] + ':' + this.minSecArr[this.minIndex]
279. if (this.showSecond) {
280. this.currentTime += ':' + this.minSecArr[this.secIndex]
281. }
282. }

284. build() {
285. Column() {
286. Row() {
287. // 根据镜像语言显示顺序创建column
288. if (!this.isRtl) {
289. if (!this.useMilitary && !this.amPmAtLast) {
290. this.buildAmPmColumn()
291. this.buildHourColumn()
292. } else {
293. this.buildHourColumn()
294. }
295. this.buildMinColumn()
296. if (this.showSecond) {
297. this.buildSecColumn()
298. }
299. if (!this.useMilitary && this.amPmAtLast) {
300. this.buildAmPmColumn()
301. }
302. } else {
303. if (!this.useMilitary && this.amPmAtLast) {
304. this.buildAmPmColumn()
305. }
306. if (this.showSecond) {
307. this.buildSecColumn()
308. }
309. this.buildMinColumn()
310. if (!this.useMilitary && !this.amPmAtLast) {
311. this.buildHourColumn()
312. this.buildAmPmColumn()
313. } else {
314. this.buildHourColumn()
315. }
316. }
317. }

319. Row() {
320. Text('selected time: ' + this.currentTime)
321. .margin(5)
322. .width("80%")
323. .textAlign(TextAlign.Center)
324. }
325. .border({ width: 1 })
326. .margin(5)

328. Column() {
329. Row() {
330. Toggle({ type: ToggleType.Switch, isOn: true })
331. .onChange((isOn: boolean) => {
332. this.loop = isOn;
333. })
334. Text('loop').fontSize(20)
335. }.width(200).margin(5)
336. Row() {
337. Toggle({ type: ToggleType.Switch, isOn: false })
338. .onChange((isOn: boolean) => {
339. this.showSecond = isOn
340. this.flushCurrentTime()
341. this.flushBorderStyle()
342. })
343. Text('show second').fontSize(20)
344. }.width(200).margin(5)
345. Row() {
346. Toggle({ type: ToggleType.Switch, isOn: false })
347. .onChange((isOn: boolean) => {
348. this.useMilitary = isOn
349. if (this.useMilitary) {
350. if (this.amPmIndex) {
351. this.hourIndex += 12
352. }
353. } else {
354. if (this.hourIndex >= 12) {
355. this.amPmIndex = 1
356. this.hourIndex -= 12
357. } else {
358. this.amPmIndex = 0
359. }
360. }
361. this.flushBorderStyle()
362. this.flushHourColumn()
363. this.flushCurrentTime()
364. })
365. Text('use military').fontSize(20)
366. }.width(200).margin(5)
367. Row() {
368. Toggle({ type: ToggleType.Switch, isOn: true })
369. .onChange((isOn: boolean) => {
370. this.zeroPrefix = isOn
371. this.flushHourColumn()
372. this.flushMinSecColumn()
373. this.flushCurrentTime()
374. })
375. Text('2-digits').fontSize(20)
376. }.width(200).margin(5)
377. }
378. }
379. .width('100%')
380. }
381. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/58Y8XxfsRHenWZQFfDu5zw/zh-cn_image_0000002558766228.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055156Z&HW-CC-Expire=86400&HW-CC-Sign=F76904EA8F82BA228F2A389AA9B2C9E9D0F16F60C13110ACC9F5E79EFD2D9C60)
