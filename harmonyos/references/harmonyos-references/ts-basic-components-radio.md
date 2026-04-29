---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-radio
title: Radio
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 按钮与选择 > Radio
category: harmonyos-references
scraped_at: 2026-04-29T13:52:01+08:00
doc_updated_at: 2026-04-08
content_hash: sha256:04066c78714bfa25157301f9d59a2055403f8b627fdddd7e60d030c5ecfc0100
---

单选框，提供相应的用户交互选择项。

说明

API version 12开始，Radio选中默认样式由RadioIndicatorType.DOT变为RadioIndicatorType.TICK。

该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

无

## 接口

PhonePC/2in1TabletTVWearable

Radio(options: RadioOptions)

创建单选框组件。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [RadioOptions](ts-basic-components-radio.md#radiooptions对象说明) | 是 | 配置单选框的参数。 |

## RadioOptions对象说明

PhonePC/2in1TabletTVWearable

单选框的信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | string | 否 | 否 | 当前单选框的值。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| group | string | 否 | 否 | 当前单选框的所属群组名称，相同group的Radio只能有一个被选中。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| indicatorType12+ | [RadioIndicatorType](ts-basic-components-radio.md#radioindicatortype12枚举说明) | 否 | 是 | 配置单选框的选中样式。未设置时按照RadioIndicatorType.TICK进行显示。  **卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| indicatorBuilder12+ | [CustomBuilder](ts-types.md#custombuilder8) | 否 | 是 | 配置单选框的选中样式为自定义组件。自定义组件与Radio组件为中心点对齐显示。indicatorBuilder设置为undefined时，按照RadioIndicatorType.TICK进行显示。  **卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## RadioIndicatorType12+枚举说明

PhonePC/2in1TabletTVWearable

单选框的样式。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TICK | 0 | 选中样式为系统默认TICK图标。 |
| DOT | 1 | 选中样式为系统默认DOT图标。 |
| CUSTOM | 2 | 选中样式为indicatorBuilder中的内容。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### checked

PhonePC/2in1TabletTVWearable

checked(value: boolean)

设置单选框的选中状态。

从API version 10开始，该属性支持[$$](../harmonyos-guides/arkts-two-way-sync.md)双向绑定变量。

从API version 18开始，该属性支持[!!](../harmonyos-guides/arkts-new-binding.md#系统组件参数双向绑定)双向绑定变量。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 单选框的选中状态。  默认值：false  值为true时，单选框被选中。值为false时，单选框不被选中。 |

### checked18+

PhonePC/2in1TabletTVWearable

checked(isChecked: Optional<boolean>)

设置单选框的选中状态。与[checked](ts-basic-components-radio.md#checked)相比，isChecked参数新增了对undefined类型的支持。

该属性支持[$$](../harmonyos-guides/arkts-two-way-sync.md)、[!!](../harmonyos-guides/arkts-new-binding.md#系统组件参数双向绑定)双向绑定变量。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isChecked | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 单选框的选中状态。  当isChecked的值为undefined时取默认值false。  值为true时，单选框被选中。值为false时，单选框不被选中。 |

### radioStyle10+

PhonePC/2in1TabletTVWearable

radioStyle(value?: RadioStyle)

设置单选框选中状态和非选中状态的样式。

从API version 10开始，该接口支持在ArkTS组件中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [RadioStyle](ts-basic-components-radio.md#radiostyle10对象说明) | 否 | 单选框选中状态和非选中状态的样式。  未设置时，则按照RadioStyle中各参数的默认值配置。 |

### contentModifier12+

PhonePC/2in1TabletTVWearable

contentModifier(modifier: ContentModifier<RadioConfiguration>)

定制Radio内容区的方法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [ContentModifier<RadioConfiguration>](ts-basic-components-radio.md#radioconfiguration12对象说明) | 是 | 在Radio组件上，定制内容区的方法。  modifier：内容修改器，开发者需要自定义class实现ContentModifier接口。 |

### contentModifier18+

PhonePC/2in1TabletTVWearable

contentModifier(modifier: Optional<ContentModifier<RadioConfiguration>>)

定制Radio内容区的方法。与[contentModifier](ts-basic-components-radio.md#contentmodifier12)12+相比，modifier参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[ContentModifier<RadioConfiguration>](ts-basic-components-radio.md#radioconfiguration12对象说明)> | 是 | 在Radio组件上，定制内容区的方法。  modifier：内容修改器，开发者需要自定义class实现ContentModifier接口。  当modifier的值为undefined时，不使用内容修改器。 |

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](ts-component-general-events.md)外，还支持以下事件：

### onChange

PhonePC/2in1TabletTVWearable

onChange(callback: (isChecked: boolean) => void)

单选框选中状态改变时触发的回调。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isChecked | boolean | 是 | 单选框选中状态改变时触发该回调。  值为true时，表示从未选中变为选中。值为false时，表示从选中变为未选中。 |

### onChange18+

PhonePC/2in1TabletTVWearable

onChange(callback: Optional<OnRadioChangeCallback>)

单选框选中状态改变时触发的回调。与[onChange](ts-basic-components-radio.md#onchange)相比，callback参数新增了对undefined类型的支持。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[OnRadioChangeCallback](ts-basic-components-radio.md#onradiochangecallback18)> | 是 | 单选框选中状态改变时触发该回调。  当callback的值为undefined时，不使用回调函数。 |

## OnRadioChangeCallback18+

PhonePC/2in1TabletTVWearable

type OnRadioChangeCallback = (isChecked: boolean) => void

单选框选中状态改变时触发的回调函数类型定义。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isChecked | boolean | 是 | 单选框的状态。  值为true时，表示从未选中变为选中。值为false时，表示从选中变为未选中。 |

## RadioStyle10+对象说明

PhonePC/2in1TabletTVWearable

单选框的颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| checkedBackgroundColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 开启状态底板颜色。  默认值：$r('sys.color.ohos\_id\_color\_text\_primary\_activated') |
| uncheckedBorderColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 关闭状态描边颜色。  默认值：$r('sys.color.ohos\_id\_color\_switch\_outline\_off') |
| indicatorColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 开启状态内部圆饼颜色。从API version 12开始，indicatorType设置为RadioIndicatorType.TICK和RadioIndicatorType.DOT时，支持修改内部颜色。indicatorType设置为RadioIndicatorType.CUSTOM时，不支持修改内部颜色。  默认值：$r('sys.color.ohos\_id\_color\_foreground\_contrary') |

## RadioConfiguration12+对象说明

PhonePC/2in1TabletTVWearable

开发者需要自定义class实现ContentModifier接口。继承自[CommonConfiguration](ts-universal-attributes-content-modifier.md#commonconfigurationt)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | string | 否 | 否 | 当前单选框的值。 |
| checked | boolean | 否 | 否 | 设置单选框的选中状态。  默认值：false  值为true时，单选框被选中。值为false时，单选框不被选中。 |
| triggerChange | Callback<boolean> | 否 | 否 | 触发单选框选中状态变化。  值为true时，表示从未选中变为选中。值为false时，表示从选中变为未选中。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1 （设置底板颜色）

该示例通过配置checkedBackgroundColor实现自定义单选框的底板颜色。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct RadioExample {
5. build() {
6. Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
7. Column() {
8. Text('Radio1')
9. Radio({ value: 'Radio1', group: 'radioGroup' }).checked(true)
10. .radioStyle({
11. checkedBackgroundColor: Color.Pink
12. })
13. .height(50)
14. .width(50)
15. .onChange((isChecked: boolean) => {
16. console.info('Radio1 status is ' + isChecked);
17. })
18. }
19. Column() {
20. Text('Radio2')
21. Radio({ value: 'Radio2', group: 'radioGroup' }).checked(false)
22. .radioStyle({
23. checkedBackgroundColor: Color.Pink
24. })
25. .height(50)
26. .width(50)
27. .onChange((isChecked: boolean) => {
28. console.info('Radio2 status is ' + isChecked);
29. })
30. }
31. Column() {
32. Text('Radio3')
33. Radio({ value: 'Radio3', group: 'radioGroup' }).checked(false)
34. .radioStyle({
35. checkedBackgroundColor: Color.Pink
36. })
37. .height(50)
38. .width(50)
39. .onChange((isChecked: boolean) => {
40. console.info('Radio3 status is ' + isChecked);
41. })
42. }
43. }.padding({ top: 30 })
44. }
45. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/NJD0SrVtRIGnZpe3RZxBQA/zh-cn_image_0000002589326109.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055158Z&HW-CC-Expire=86400&HW-CC-Sign=3360AD2F0E1C4E9AEDD7282EA1A04F5BC0DB85852A27D0BB6B082AC6099E6522)

### 示例2 （设置选中样式）

该示例通过配置indicatorType、indicatorBuilder实现自定义选中样式。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct RadioExample {
5. @Builder
6. indicatorBuilder() {
7. // $r('app.media.star')需要替换为开发者所需的图像资源文件。
8. Image($r("app.media.star"))
9. }
10. build() {
11. Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
12. Column() {
13. Text('Radio1')
14. Radio({ value: 'Radio1', group: 'radioGroup',
15. indicatorType:RadioIndicatorType.TICK
16. }).checked(true)
17. .height(50)
18. .width(80)
19. .onChange((isChecked: boolean) => {
20. console.info('Radio1 status is ' + isChecked);
21. })
22. }
23. Column() {
24. Text('Radio2')
25. Radio({ value: 'Radio2', group: 'radioGroup',
26. indicatorType:RadioIndicatorType.DOT
27. }).checked(false)
28. .height(50)
29. .width(80)
30. .onChange((isChecked: boolean) => {
31. console.info('Radio2 status is ' + isChecked);
32. })
33. }
34. Column() {
35. Text('Radio3')
36. Radio({ value: 'Radio3', group: 'radioGroup',
37. indicatorType:RadioIndicatorType.CUSTOM,
38. indicatorBuilder:()=>{this.indicatorBuilder()}
39. }).checked(false)
40. .height(50)
41. .width(80)
42. .onChange((isChecked: boolean) => {
43. console.info('Radio3 status is ' + isChecked);
44. })
45. }
46. }.padding({ top: 30 })
47. }
48. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/doerMF6XQy2vqxGqc-ZYTw/zh-cn_image_0000002589246051.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055158Z&HW-CC-Expire=86400&HW-CC-Sign=337BC233EF5128C0A747974C2429F9A32F84A0CB7B351DDE7B4E8EF074FE01AD)

### 示例3（设置自定义样式）

该示例通过contentModifier实现自定义单选框样式。

```
1. class MyRadioStyle implements ContentModifier<RadioConfiguration> {
2. type: number = 0;
3. selectedColor: ResourceColor = Color.Black;

5. constructor(numberType: number, colorType: ResourceColor) {
6. this.type = numberType;
7. this.selectedColor = colorType;
8. }

10. applyContent(): WrappedBuilder<[RadioConfiguration]> {
11. return wrapBuilder(buildRadio);
12. }
13. }

15. @Builder
16. function buildRadio(config: RadioConfiguration) {
17. Row({ space: 30 }) {
18. Circle({ width: 50, height: 50 })
19. .stroke(Color.Black)
20. .fill(config.checked ? (config.contentModifier as MyRadioStyle).selectedColor : Color.White)
21. Button(config.checked ? "off" : "on")
22. .width(100)
23. .type(config.checked ? (config.contentModifier as MyRadioStyle).type : ButtonType.Normal)
24. .backgroundColor('#2787D9')
25. .onClick(() => {
26. if (config.checked) {
27. config.triggerChange(false);
28. } else {
29. config.triggerChange(true);
30. }
31. })
32. }
33. }

35. @Entry
36. @Component
37. struct refreshExample {
38. build() {
39. Column({ space: 50 }) {
40. Row() {
41. Radio({ value: 'Radio1', group: 'radioGroup' })
42. .contentModifier(new MyRadioStyle(1, '#004AAF'))
43. .checked(false)
44. .width(300)
45. .height(100)
46. }

48. Row() {
49. Radio({ value: 'Radio2', group: 'radioGroup' })
50. .checked(true)
51. .width(300)
52. .height(60)
53. .contentModifier(new MyRadioStyle(2, '#004AAF'))
54. }
55. }
56. }
57. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/_yCISxXkRXKd0lodUstF-Q/zh-cn_image_0000002558766242.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055158Z&HW-CC-Expire=86400&HW-CC-Sign=E67BD41302BD308CCC2CDA8D6A29B1A1C2750667394CCEC0972D39EF9E52BD45)
