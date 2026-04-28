---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-checkbox
title: Checkbox
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 按钮与选择 > Checkbox
category: harmonyos-references
scraped_at: 2026-04-28T08:01:42+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:8793556d30cf7abb395c83d4695ba3627edd24b318b10bda257a5d8547b21626
---

提供多选框组件，通常用于某选项的打开或关闭。

说明

API version 11开始，Checkbox默认样式由圆角方形变为圆形。

该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

无

## 接口

PhonePC/2in1TabletTVWearable

Checkbox(options?: CheckboxOptions)

多选框组件。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [CheckboxOptions](ts-basic-components-checkbox.md#checkboxoptions对象说明) | 否 | 配置多选框的参数。 |

## CheckboxOptions对象说明

PhonePC/2in1TabletTVWearable

多选框的信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 是 | 指定多选框名称。  默认值：undefined，取值为undefined无效果。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| group | string | 否 | 是 | 用于指定多选框所属群组的名称（即所属CheckboxGroup的名称）。  默认值：undefined，默认状态下配合[CheckboxGroupOptions](ts-basic-components-checkboxgroup.md#checkboxgroupoptions对象说明)属性group信息为undefined的节点使用。  **说明：**  未配合使用[CheckboxGroup](ts-basic-components-checkboxgroup.md)组件时，此值无用。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| indicatorBuilder12+ | [CustomBuilder](ts-types.md#custombuilder8) | 否 | 是 | 配置多选框的选中样式为自定义组件。自定义组件与Checkbox组件为中心点对齐显示。indicatorBuilder设置为undefined/null时，默认为indicatorBuilder未设置状态。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### select

PhonePC/2in1TabletTVWearable

select(value: boolean)

设置多选框选中状态。

从API version 10开始，该属性支持[$$](../harmonyos-guides/arkts-two-way-sync.md)双向绑定变量。

从API version 18开始，该属性支持[!!](../harmonyos-guides/arkts-new-binding.md#系统组件参数双向绑定)双向绑定变量。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 多选框是否选中。  默认值：false  值为true时，多选框被选中。值为false时，多选框未选中。 |

### select18+

PhonePC/2in1TabletTVWearable

select(isSelected: Optional<boolean>)

设置多选框选中状态。与[select](ts-basic-components-checkbox.md#select)相比，isSelected参数新增了对undefined类型的支持。

该属性支持[$$](../harmonyos-guides/arkts-two-way-sync.md)、[!!](../harmonyos-guides/arkts-new-binding.md#系统组件参数双向绑定)双向绑定变量。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isSelected | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 多选框是否选中。  当isSelected的值为undefined时取默认值false。  值为true时，多选框被选中。值为false时，多选框未选中。 |

### selectedColor

PhonePC/2in1TabletTVWearable

selectedColor(value: ResourceColor)

设置多选框选中状态颜色。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 多选框选中状态颜色。  默认值：$r('sys.color.ohos\_id\_color\_text\_primary\_activated')  异常值按照默认值处理。 |

### selectedColor18+

PhonePC/2in1TabletTVWearable

selectedColor(resColor: Optional<ResourceColor>)

设置多选框选中状态颜色。与[selectedColor](ts-basic-components-checkbox.md#selectedcolor)相比，resColor参数新增了对undefined类型的支持。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resColor | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[ResourceColor](ts-types.md#resourcecolor)> | 是 | 多选框选中状态颜色。  当resColor的值为undefined时取默认值$r('sys.color.ohos\_id\_color\_text\_primary\_activated')。  异常值按照默认值处理。 |

### unselectedColor10+

PhonePC/2in1TabletTVWearable

unselectedColor(value: ResourceColor)

设置多选框非选中状态的边框颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 多选框非选中状态边框颜色。  默认值：$r('sys.color.ohos\_id\_color\_switch\_outline\_off') |

### unselectedColor18+

PhonePC/2in1TabletTVWearable

unselectedColor(resColor: Optional<ResourceColor>)

设置多选框非选中状态的边框颜色。与[unselectedColor](ts-basic-components-checkbox.md#unselectedcolor10)10+相比，resColor参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resColor | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[ResourceColor](ts-types.md#resourcecolor)> | 是 | 多选框非选中状态边框颜色。  当resColor的值为undefined时取默认值$r('sys.color.ohos\_id\_color\_switch\_outline\_off') |

### mark10+

PhonePC/2in1TabletTVWearable

mark(value: MarkStyle)

设置多选框内部图标的样式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [MarkStyle](ts-types.md#markstyle10对象说明) | 是 | 多选框内部图标样式。 从API version 12开始，设置了indicatorBuilder时，按照indicatorBuilder中的内容显示。  默认值：{  strokeColor : $r('sys.color.ohos\_id\_color\_foreground\_contrary'),  strokeWidth: $r('sys.float.ohos\_id\_checkbox\_stroke\_width'),  size: '20vp'  } |

### mark18+

PhonePC/2in1TabletTVWearable

mark(style: Optional<MarkStyle>)

设置多选框内部图标的样式。与[mark](ts-basic-components-checkbox.md#mark10)10+相比，style参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[MarkStyle](ts-types.md#markstyle10对象说明)> | 是 | 多选框内部图标样式。 设置了indicatorBuilder时，按照indicatorBuilder中的内容显示。  当style的值为undefined时，默认值：{  strokeColor : $r('sys.color.ohos\_id\_color\_foreground\_contrary'),  strokeWidth: $r('sys.float.ohos\_id\_checkbox\_stroke\_width'),  size: '20vp'  } |

### shape11+

PhonePC/2in1TabletTVWearable

shape(value: CheckBoxShape)

设置Checkbox组件形状，包括圆形和圆角方形。如果想要调整当前Checkbox的样式，需使用[contentModifier](ts-basic-components-checkbox.md#contentmodifier12)属性自定义Checkbox样式。

**卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [CheckBoxShape](ts-appendix-enums.md#checkboxshape11) | 是 | Checkbox组件形状，包括圆形和圆角方形。  默认值：CheckBoxShape.CIRCLE |

### shape18+

PhonePC/2in1TabletTVWearable

shape(shape: Optional<CheckBoxShape>)

设置Checkbox组件形状，包括圆形和圆角方形。与[shape](ts-basic-components-checkbox.md#shape11)11+相比，shape参数新增了对undefined类型的支持。如果想要调整当前Checkbox的样式，需使用[contentModifier](ts-basic-components-checkbox.md#contentmodifier12)属性自定义Checkbox样式。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| shape | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[CheckBoxShape](ts-appendix-enums.md#checkboxshape11)> | 是 | Checkbox组件形状，包括圆形和圆角方形。  当shape的值为undefined时，默认值为CheckBoxShape.CIRCLE。 |

### contentModifier12+

PhonePC/2in1TabletTVWearable

contentModifier(modifier: ContentModifier<CheckBoxConfiguration>)

定制Checkbox内容区的方法。设置该属性时，会导致其他属性设置失效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [ContentModifier](ts-universal-attributes-content-modifier.md#contentmodifiert)[<CheckBoxConfiguration>](ts-basic-components-checkbox.md#checkboxconfiguration12对象说明) | 是 | 在Checkbox组件上，定制内容区的方法。  modifier：内容修改器，开发者需要自定义class实现ContentModifier接口。 |

### contentModifier18+

PhonePC/2in1TabletTVWearable

contentModifier(modifier: Optional<ContentModifier<CheckBoxConfiguration>>)

定制Checkbox内容区的方法。与[contentModifier](ts-basic-components-checkbox.md#contentmodifier12)12+相比，modifier参数新增了对undefined类型的支持。设置该属性时，会导致其他属性设置失效。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[ContentModifier](ts-universal-attributes-content-modifier.md#contentmodifiert)[<CheckBoxConfiguration>](ts-basic-components-checkbox.md#checkboxconfiguration12对象说明)> | 是 | 在Checkbox组件上，定制内容区的方法。  modifier：内容修改器，开发者需要自定义class实现ContentModifier接口。  当modifier的值为undefined时，不使用内容修改器。 |

## 事件

PhonePC/2in1TabletTVWearable

支持[通用事件](ts-component-general-events.md)外，还支持以下事件：

### onChange

PhonePC/2in1TabletTVWearable

onChange(callback: OnCheckboxChangeCallback)

当选中状态发生变化时，触发该回调。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnCheckboxChangeCallback](ts-basic-components-checkbox.md#oncheckboxchangecallback18) | 是 | 返回选中的状态。 |

### onChange18+

PhonePC/2in1TabletTVWearable

onChange(callback: Optional<OnCheckboxChangeCallback>)

当选中状态发生变化时，触发该回调。与[onChange](ts-basic-components-checkbox.md#onchange)相比，callback参数新增了对undefined类型的支持。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[OnCheckboxChangeCallback](ts-basic-components-checkbox.md#oncheckboxchangecallback18)> | 是 | 返回选中的状态。  当callback的值为undefined时，不使用回调函数。 |

## OnCheckboxChangeCallback18+

PhonePC/2in1TabletTVWearable

type OnCheckboxChangeCallback = (value: boolean) => void

选中的状态。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 返回true表示已选中。返回false表示未选中。 |

## CheckBoxConfiguration12+对象说明

PhonePC/2in1TabletTVWearable

开发者需要自定义class实现ContentModifier接口。继承自[CommonConfiguration](ts-universal-attributes-content-modifier.md#commonconfigurationt)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 当前多选框名称。 |
| selected | boolean | 否 | 否 | 指示多选框是否被选中，值为true时，多选框被选中。值为false时，多选框未选中。  如果select属性没有设置默认值是false。  如果设置select属性，此值与设置select属性的值相同。 |
| triggerChange | Callback<boolean> | 否 | 否 | 触发多选框选中状态变化。true表示从未选中变为选中，false表示从选中变为未选中。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置多选框形状）

该示例通过配置CheckBoxShape实现圆形和圆角方形多选框样式。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct CheckboxExample {
5. build() {
6. Flex({ justifyContent: FlexAlign.SpaceEvenly }) {
7. Checkbox({ name: 'checkbox1', group: 'checkboxGroup' })
8. .select(true)
9. .selectedColor(0xed6f21)
10. .shape(CheckBoxShape.CIRCLE)
11. .onChange((value: boolean) => {
12. console.info('Checkbox1 change is' + value);
13. })
14. Checkbox({ name: 'checkbox2', group: 'checkboxGroup' })
15. .select(false)
16. .selectedColor(0x39a2db)
17. .shape(CheckBoxShape.ROUNDED_SQUARE)
18. .onChange((value: boolean) => {
19. console.info('Checkbox2 change is' + value);
20. })
21. }
22. }
23. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/TPUiDBk5Rn2wANka9z3duQ/zh-cn_image_0000002583439743.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000141Z&HW-CC-Expire=86400&HW-CC-Sign=589F74FA486162920712D9EADB2D1AD66C42D0A32427788D2E55BD8FE27A617E)

### 示例2（设置多选框颜色）

该示例通过配置mark实现自定义多选框的颜色。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {

6. build() {
7. Row() {
8. Column() {
9. Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
10. Checkbox({ name: 'checkbox1', group: 'checkboxGroup' })
11. .selectedColor(0x39a2db)
12. .shape(CheckBoxShape.ROUNDED_SQUARE)
13. .onChange((value: boolean) => {
14. console.info('Checkbox1 change is'+ value);
15. })
16. .mark({
17. strokeColor:Color.Black,
18. size: 50,
19. strokeWidth: 5
20. })
21. .unselectedColor(Color.Red)
22. .width(30)
23. .height(30)
24. Text('Checkbox1').fontSize(20)
25. }
26. Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
27. Checkbox({ name: 'checkbox2', group: 'checkboxGroup' })
28. .selectedColor(0x39a2db)
29. .shape(CheckBoxShape.ROUNDED_SQUARE)
30. .onChange((value: boolean) => {
31. console.info('Checkbox2 change is' + value);
32. })
33. .width(30)
34. .height(30)
35. Text('Checkbox2').fontSize(20)
36. }
37. }
38. .width('100%')
39. }
40. .height('100%')
41. }
42. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/wNLe87u5TkGhKzjHbj7lBQ/zh-cn_image_0000002552959698.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000141Z&HW-CC-Expire=86400&HW-CC-Sign=6C539BB3A5F0EE7EAFF82FD2FA0D913D3A221A6692F73A74529CDD267810DF49)

### 示例3（自定义多选框样式）

该示例通过[contentModifier](ts-basic-components-checkbox.md#contentmodifier12)属性实现了自定义多选框样式的功能，自定义样式实现了一个五边形多选框，如果选中，内部会出现红色三角图案，标题会显示选中字样，如果取消选中，红色三角图案消失，标题会显示非选中字样。

```
1. // xxx.ets
2. class MyCheckboxStyle implements ContentModifier<CheckBoxConfiguration> {
3. selectedColor: Color = Color.White;

5. constructor(selectedColor: Color) {
6. this.selectedColor = selectedColor;
7. }

9. applyContent(): WrappedBuilder<[CheckBoxConfiguration]> {
10. return wrapBuilder(buildCheckbox);
11. }
12. }

14. @Builder
15. function buildCheckbox(config: CheckBoxConfiguration) {
16. Column({ space: 10 }) {
17. Text(config.name + (config.selected ? "（ 选中 ）" : "（ 非选中 ）")).margin({ right: 70, top: 50 })
18. Text(config.enabled ? "enabled true" : "enabled false").margin({ right: 110 })
19. Shape() {
20. Path()
21. .width(100)
22. .height(100)
23. .commands('M100 0 L0 100 L50 200 L150 200 L200 100 Z')
24. .fillOpacity(0)
25. .strokeWidth(3)
26. .onClick(() => {
27. if (config.selected) {
28. config.triggerChange(false);
29. } else {
30. config.triggerChange(true);
31. }
32. })
33. .opacity(config.enabled ? 1 : 0.1)
34. Path()
35. .width(10)
36. .height(10)
37. .commands('M50 0 L100 100 L0 100 Z')
38. .visibility(config.selected ? Visibility.Visible : Visibility.Hidden)
39. .fill(config.selected ? (config.contentModifier as MyCheckboxStyle).selectedColor : Color.Black)
40. .stroke((config.contentModifier as MyCheckboxStyle).selectedColor)
41. .margin({ left: 10, top: 10 })
42. .opacity(config.enabled ? 1 : 0.1)
43. }
44. .width(300)
45. .height(200)
46. .viewPort({
47. x: 0,
48. y: 0,
49. width: 310,
50. height: 310
51. })
52. .strokeLineJoin(LineJoinStyle.Miter)
53. .strokeMiterLimit(5)
54. .margin({ left: 50 })
55. }
56. }

58. @Entry
59. @Component
60. struct Index {
61. @State checkboxEnabled: boolean = true;

63. build() {
64. Column({ space: 100 }) {
65. Checkbox({ name: '多选框状态', group: 'checkboxGroup' })
66. .contentModifier(new MyCheckboxStyle(Color.Red))
67. .onChange((value: boolean) => {
68. console.info('Checkbox change is' + value);
69. }).enabled(this.checkboxEnabled)

71. Row() {
72. Toggle({ type: ToggleType.Switch, isOn: true }).onChange((value: boolean) => {
73. if (value) {
74. this.checkboxEnabled = true;
75. } else {
76. this.checkboxEnabled = false;
77. }
78. })
79. }.position({ x: 50, y: 130 })
80. }.margin({ top: 30 })
81. }
82. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/y3IGu4OwTpKZ4nXGJrKkpw/zh-cn_image_0000002583479699.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000141Z&HW-CC-Expire=86400&HW-CC-Sign=7E422569B0CA30480A6DD6E16DE107CE9BAF3F7FAC89E632286E085E466B202E)

### 示例4（设置文本多选框样式）

该示例通过配置indicatorBuilder实现选中样式为Text。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct CheckboxExample {
5. @Builder
6. indicatorBuilder(value: number) {
7. Column(){
8. Text(value > 99 ? '99+': value.toString())
9. .textAlign(TextAlign.Center)
10. .fontSize(value > 99 ?  '16vp': '20vp')
11. .fontWeight(FontWeight.Medium)
12. .fontColor('#ffffffff')
13. }
14. }
15. build() {
16. Row() {
17. Column() {
18. Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center}) {
19. Checkbox({ name: 'checkbox1', group: 'checkboxGroup', indicatorBuilder:()=>{this.indicatorBuilder(9)}})
20. .shape(CheckBoxShape.CIRCLE)
21. .onChange((value: boolean) => {
22. console.info('Checkbox1 change is'+ value);
23. })
24. .mark({
25. strokeColor:Color.Black,
26. size: 50,
27. strokeWidth: 5
28. })
29. .width(30)
30. .height(30)
31. Text('Checkbox1').fontSize(20)
32. }.padding(15)
33. Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
34. Checkbox({ name: 'checkbox2', group: 'checkboxGroup', indicatorBuilder:()=>{this.indicatorBuilder(100)}})
35. .shape(CheckBoxShape.ROUNDED_SQUARE)
36. .onChange((value: boolean) => {
37. console.info('Checkbox2 change is' + value);
38. })
39. .width(30)
40. .height(30)
41. Text('Checkbox2').fontSize(20)
42. }
43. }
44. .width('100%')
45. }
46. .height('100%')
47. }
48. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/jjbKARkqSBaiQJrz0flu6w/zh-cn_image_0000002552800050.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000141Z&HW-CC-Expire=86400&HW-CC-Sign=D0BBB07C08BFF79DF4AB3939BB51635F29F075D0EDD62CE56AB691D00A07D58B)

### 示例5（获取多选框选中信息）

该示例通过选中Checkbox以及CheckboxGroup多选框来获取选中的信息。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct CheckboxExample {
5. @State arrOne: Array<string> = ['1', '2', '3'];
6. @State arrTwo: Array<string> = ['1', '2', '3', '4'];
7. @State arrThree: Array<string> = ['1', '2', '3', '4', '5', '6'];
8. @State selected: boolean = false;
9. @State infoOne: string = '';
10. @State infoTwo: string = '';
11. @State infoThree: string = '';

13. build() {
14. Column() {
15. // 单元项全选按钮
16. Flex({ justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
17. CheckboxGroup({ group: 'checkboxGroupOne' })
18. .selectAll(this.selected)
19. .checkboxShape(CheckBoxShape.ROUNDED_SQUARE)
20. .selectedColor('#007DFF')
21. .onChange((itemName: CheckboxGroupResult) => {
22. this.infoOne = "checkboxGroupOne" + JSON.stringify(itemName);
23. console.info("checkboxGroupOne" + JSON.stringify(itemName));
24. })
25. Text('checkboxGroupOne Select All').fontSize(14).lineHeight(20).fontColor('#182431').fontWeight(500)
26. }

28. // 选项1
29. Flex({ justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
30. Column() {
31. ForEach(this.arrOne, (item: string) => {
32. Row() {
33. Checkbox({ name: 'checkbox' + item, group: 'checkboxGroupOne' })
34. .selectedColor('#007DFF')
35. .shape(CheckBoxShape.ROUNDED_SQUARE)
36. .onChange((value: boolean) => {
37. console.info('Checkbox' + item + 'change is' + value);
38. })
39. .margin({ left: 20 })
40. Text('Checkbox' + item)
41. .fontSize(14)
42. .lineHeight(20)
43. .fontColor('#182431')
44. .fontWeight(500)
45. .margin({ left: 10 })
46. }
47. }, (item: string) => item)
48. }
49. }.margin({ bottom: 15 })

51. Flex({ justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
52. CheckboxGroup({ group: 'checkboxGroupTwo' })
53. .selectAll(this.selected)
54. .checkboxShape(CheckBoxShape.ROUNDED_SQUARE)
55. .selectedColor('#007DFF')
56. .onChange((itemName: CheckboxGroupResult) => {
57. this.infoTwo = "checkboxGroupTwo" + JSON.stringify(itemName);
58. console.info("checkboxGroupTwo" + JSON.stringify(itemName));
59. })
60. Text('checkboxGroupTwo Select All').fontSize(14).lineHeight(20).fontColor('#182431').fontWeight(500)
61. }

63. // 选项2
64. Flex({ justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
65. Column() {
66. ForEach(this.arrTwo, (item: string) => {
67. Row() {
68. Checkbox({ name: 'checkbox' + item, group: 'checkboxGroupTwo' })
69. .selectedColor('#007DFF')
70. .shape(CheckBoxShape.ROUNDED_SQUARE)
71. .onChange((value: boolean) => {
72. console.info('Checkbox' + item + 'change is' + value);
73. })
74. .margin({ left: 20 })
75. Text('Checkbox' + item)
76. .fontSize(14)
77. .lineHeight(20)
78. .fontColor('#182431')
79. .fontWeight(500)
80. .margin({ left: 10 })
81. }
82. }, (item: string) => item)
83. }
84. }.margin({ bottom: 15 })

86. Flex({ justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
87. CheckboxGroup({ group: 'checkboxGroupThree' })
88. .selectAll(this.selected)
89. .checkboxShape(CheckBoxShape.ROUNDED_SQUARE)
90. .selectedColor('#007DFF')
91. .onChange((itemName: CheckboxGroupResult) => {
92. this.infoThree = "checkboxGroupThree" + JSON.stringify(itemName);
93. console.info("checkboxGroupThree" + JSON.stringify(itemName));
94. })
95. Text('checkboxGroupThree Select All').fontSize(14).lineHeight(20).fontColor('#182431').fontWeight(500)
96. }

98. // 选项3
99. Flex({ justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
100. Column() {
101. ForEach(this.arrThree, (item: string) => {
102. Row() {
103. Checkbox({ name: 'checkbox' + item, group: 'checkboxGroupThree' })
104. .selectedColor('#007DFF')
105. .shape(CheckBoxShape.ROUNDED_SQUARE)
106. .onChange((value: boolean) => {
107. console.info('Checkbox' + item + 'change is' + value);
108. })
109. .margin({ left: 20 })
110. Text('Checkbox' + item)
111. .fontSize(14)
112. .lineHeight(20)
113. .fontColor('#182431')
114. .fontWeight(500)
115. .margin({ left: 10 })
116. }
117. }, (item: string) => item)
118. }
119. }.margin({ bottom: 15 })

121. // 全选按钮
122. Flex({ justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
123. Row() {
124. CheckboxGroup({ group: 'checkboxGroup' })
125. .checkboxShape(CheckBoxShape.CIRCLE)
126. .selectedColor('#007DFF')
127. .width(30)
128. .margin({ left: 10 })
129. .onChange(() => {
130. this.selected = !this.selected
131. })
132. Text('Select All')
133. .fontSize(14)
134. .lineHeight(20)
135. .fontColor('#182431')
136. .fontWeight(500)
137. .margin({ left: 10 })
138. }
139. }.margin({ bottom: 15 })

141. // 获取选中信息
142. Button('get selected info')
143. .margin({ top: 10 })
144. .onClick(() => {
145. this.getUIContext().getPromptAction().showToast({
146. message: 'selected info: ' + this.infoOne + '\n' + this.infoTwo + '\n' + this.infoThree
147. })
148. })
149. }.padding(10)
150. }
151. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/dwUs_ZxuTtCGNAp9FrLNJw/zh-cn_image_0000002583439745.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000141Z&HW-CC-Expire=86400&HW-CC-Sign=D6C730D04D8D29B9BF6AF76BE7E453A7C14E73580FBC29367C2B232149A96772)

### 示例6（设置滑动多选）

该示例通过设置手势事件实现Checkbox滑动多选。

```
1. // xxx.ets
2. import { componentUtils, ComponentUtils, UIContext } from '@kit.ArkUI';
3. import { LinkedList } from '@kit.ArkTS';

5. @Entry
6. @Component
7. struct Index {
8. @State isChoosing: boolean = false;
9. @State selectedStart: number = -1;
10. @State @Watch('onSelectedEndChange') selectedEnd: number = -1;
11. selectedPhotos: LinkedList<number> = new LinkedList();
12. @State selectedList: number[] = [];
13. @State image: Resource[] =
14. // $r('app.media.xxx')需要替换为开发者所需的图像资源文件。
15. [$r("app.media.imageOne"), $r('app.media.imageTwo'), $r('app.media.imageThree'), $r('app.media.imageFour')];
16. private selectedState: SelectedState = SelectedState.None;
17. private componentUtils: ComponentUtils = this.getUIContext().getComponentUtils();
18. private listScroller: ListScroller = new ListScroller();
19. private currentOffsetY: number = 0;

21. onChange() {
22. console.info('change successful');
23. }

25. getSpeed(fingerY: number, edge: number) {
26. return 150 * 150 * (fingerY - edge) / 2000 / Math.abs(fingerY - edge);
27. }

29. getIndex(fingerX: number, fingerY: number) {
30. let rect: componentUtils.ComponentInfo | null = null;
31. for (let i = 0; i < 100; i++) {
32. let uiContext: UIContext = this.getUIContext();
33. rect = this.componentUtils.getRectangleById(`stack${i}`);
34. if (rect) {
35. const x1 = uiContext.px2vp(rect.windowOffset.x);
36. const x2 = uiContext.px2vp(rect.windowOffset.x + rect.size.width);
37. const y1 = uiContext.px2vp(rect.windowOffset.y);
38. const y2 = uiContext.px2vp(rect.windowOffset.y + rect.size.height);
39. if (x1 <= fingerX && fingerX < x2 && y1 <= fingerY && fingerY < y2) {
40. return i;
41. }
42. }
43. }
44. return this.selectedEnd;
45. }

47. onSelectedEndChange() {
48. let start: number = -1;
49. let end: number = -1;
50. if (this.selectedEnd > this.selectedStart) {
51. start = this.selectedStart;
52. end = this.selectedEnd;
53. } else {
54. end = this.selectedStart;
55. start = this.selectedEnd;
56. }
57. if (this.selectedState == SelectedState.Selected) {
58. for (let i = start; i <= end; i++) {
59. if (!this.selectedPhotos.has(i)) {
60. this.selectedPhotos.add(i);
61. }
62. }
63. } else if (this.selectedState == SelectedState.Remove) {
64. for (let i = start; i <= end; i++) {
65. if (this.selectedPhotos.has(i)) {
66. this.selectedPhotos.remove(i);
67. }
68. }
69. }
70. this.selectedList = this.selectedPhotos.convertToArray();
71. }

73. scroll(fingerY: number) {
74. if (fingerY > 700 && !this.listScroller.isAtEnd()) {
75. this.listScroller.scrollBy(0, this.getSpeed(fingerY, 700));
76. return;
77. }
78. if (fingerY < 200 && this.currentOffsetY > 0) {
79. this.listScroller.scrollBy(0, this.getSpeed(fingerY, 200));
80. return;
81. }
82. }

84. onPanGestureUpdate(event: GestureEvent) {
85. const fingerInfo = event.fingerList[event.fingerList.length - 1];
86. const fingerX = fingerInfo.globalX;
87. const fingerY = fingerInfo.globalY;
88. this.selectedEnd = this.getIndex(fingerX, fingerY);
89. this.scroll(fingerY);
90. }

92. build() {
93. Column() {
94. if (this.isChoosing) {
95. Row() {
96. Text('取消')
97. .onClick(() => {
98. this.isChoosing = false;
99. this.selectedStart = -1;
100. this.selectedEnd = -1;
101. this.selectedPhotos.clear();
102. this.selectedList = [];
103. })
104. }
105. .width('100%')
106. .justifyContent(FlexAlign.SpaceEvenly)
107. }
108. List({ space: 10, scroller: this.listScroller }) {
109. ForEach(Array.from({ length: 100 }), (item: string, index: number) => {
110. ListItem() {
111. Stack({ alignContent: Alignment.TopEnd }) {
112. Image(this.image[(index % 4)])
113. .width('100%')
114. .draggable(false)
115. Checkbox({ name: index.toString() })
116. .shape(CheckBoxShape.CIRCLE)
117. .visibility(this.isChoosing ? Visibility.Visible : Visibility.None)
118. .select(this.selectedList.includes(index))
119. }
120. .id(`stack${index}`)
121. .width('100%')
122. }
123. .draggable(false)
124. }, (item: string, index: number) => 'listItem' + index)
125. }
126. .id('list')
127. .height('100%')
128. .width('100%')
129. .lanes(4)
130. .alignListItem(ListItemAlign.Center)
131. .onDidScroll(() => {
132. this.currentOffsetY = this.listScroller.currentOffset().yOffset;
133. })
134. .gesture(
135. GestureGroup(GestureMode.Exclusive,
136. GestureGroup(GestureMode.Sequence,
137. LongPressGesture()
138. .onAction(() => {
139. this.isChoosing = true;
140. }),
141. PanGesture()
142. .onActionStart(event => {
143. if (!this.isChoosing) {
144. return;
145. }
146. const fingerInfo = event.fingerList[event.fingerList.length - 1];
147. const fingerX = fingerInfo.globalX;
148. const fingerY = fingerInfo.globalY;
149. this.selectedStart = this.getIndex(fingerX, fingerY);
150. if (this.selectedPhotos.has(this.selectedStart)) {
151. this.selectedState = SelectedState.Remove;
152. } else {
153. this.selectedState = SelectedState.Selected;
154. }
155. })
156. .onActionUpdate(event => {
157. if (!this.isChoosing) {
158. return;
159. }
160. this.onPanGestureUpdate(event);
161. })
162. .onActionEnd(() => {
163. if (!this.isChoosing) {
164. return;
165. }
166. this.selectedState = SelectedState.None;
167. })
168. ),
169. PanGesture()
170. .onActionStart(event => {
171. if (!this.isChoosing) {
172. return;
173. }
174. const fingerInfo = event.fingerList[event.fingerList.length - 1];
175. const fingerX = fingerInfo.globalX;
176. const fingerY = fingerInfo.globalY;
177. this.selectedStart = this.getIndex(fingerX, fingerY);
178. if (this.selectedPhotos.has(this.selectedStart)) {
179. this.selectedState = SelectedState.Remove;
180. } else {
181. this.selectedState = SelectedState.Selected;
182. }
183. })
184. .onActionUpdate(event => {
185. if (!this.isChoosing) {
186. return;
187. }
188. this.onPanGestureUpdate(event);
189. })
190. .onActionEnd(() => {
191. if (!this.isChoosing) {
192. return;
193. }
194. this.selectedState = SelectedState.None;
195. })
196. )
197. )
198. }
199. }
200. }

202. enum SelectedState {
203. None,
204. Selected,
205. Remove
206. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/wafmv1yBTt-9GvZh9Qz27g/zh-cn_image_0000002552959700.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000141Z&HW-CC-Expire=86400&HW-CC-Sign=D9B48D9671A41ED5A1E5853D8EB91684FF07F1FFCE59A65EA8E0BE2CDA842E7B)
