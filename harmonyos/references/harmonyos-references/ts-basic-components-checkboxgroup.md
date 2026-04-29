---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-checkboxgroup
title: CheckboxGroup
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 按钮与选择 > CheckboxGroup
category: harmonyos-references
scraped_at: 2026-04-29T13:51:59+08:00
doc_updated_at: 2026-04-08
content_hash: sha256:c048b915d92e4d4b058e30f1883a97afa9ef7245707917a42d4be40e0df1228b
---

多选框群组，用于控制多选框全选或者不全选状态。

说明

该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

无

## 接口

PhonePC/2in1TabletTVWearable

CheckboxGroup(options?: CheckboxGroupOptions)

创建多选框群组，用于控制群组内Checkbox的全选或取消全选状态，具有相同group值的Checkbox和CheckboxGroup属于同一群组。

在结合带缓存功能的组件使用时（如[List](ts-container-list.md)），未被创建的Checkbox选中状态需要应用手动控制。详细示例请参考[示例4](ts-basic-components-checkboxgroup.md#示例4设置全选)。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [CheckboxGroupOptions](ts-basic-components-checkboxgroup.md#checkboxgroupoptions对象说明) | 否 | 配置多选框群组参数。  未设置时，按照CheckboxGroupOptions中各参数的默认值配置。 |

## CheckboxGroupOptions对象说明

PhonePC/2in1TabletTVWearable

多选框群组的信息。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| group | string | 否 | 是 | 群组名称。  默认值：undefined，默认状态下管理[CheckboxOptions](ts-basic-components-checkbox.md#checkboxoptions对象说明)属性group信息为undefined的节点。  **说明：**  具有相同群组名称的多个CheckboxGroup，仅第一个CheckboxGroup生效。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### selectAll

PhonePC/2in1TabletTVWearable

selectAll(value: boolean)

设置是否全选。若同组的[Checkbox](ts-basic-components-checkbox.md)显式设置了select属性，则Checkbox的优先级高。

在与带有缓存功能的组件（如[List](ts-container-list.md)）配合使用时，未创建的Checkbox选中状态需由开发者控制。

从API version 10开始，该属性支持[$$](../harmonyos-guides/arkts-two-way-sync.md)双向绑定变量。

从API version 18开始，该属性支持[!!](../harmonyos-guides/arkts-new-binding.md#系统组件参数双向绑定)双向绑定变量。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否全选。  默认值：false  值为true时，多选框群组将全部被选中；值为false时，多选框群组将全部取消选中。 |

### selectAll18+

PhonePC/2in1TabletTVWearable

selectAll(isAllSelected: Optional<boolean>)

设置是否全选。若同组的[Checkbox](ts-basic-components-checkbox.md)显式设置了select属性，则Checkbox的优先级高。与[selectAll](ts-basic-components-checkboxgroup.md#selectall)相比，isAllSelected参数新增了对undefined类型的支持。

在与带有缓存功能的组件（如[List](ts-container-list.md)）配合使用时，未创建的Checkbox选中状态需由开发者控制。

该属性支持[$$](../harmonyos-guides/arkts-two-way-sync.md)、[!!](../harmonyos-guides/arkts-new-binding.md#系统组件参数双向绑定)双向绑定变量。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isAllSelected | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 是否全选。  当isAllSelected的值为undefined时取默认值false。  值为true时，多选框群组将全部被选中；值为false时，多选框群组将全部取消选中。 |

### selectedColor

PhonePC/2in1TabletTVWearable

selectedColor(value: ResourceColor)

设置被选中或部分选中状态的颜色。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 被选中或部分选中状态的颜色。  默认值：$r('sys.color.ohos\_id\_color\_text\_primary\_activated')  异常值按照默认值处理。 |

### selectedColor18+

PhonePC/2in1TabletTVWearable

selectedColor(resColor: Optional<ResourceColor>)

设置被选中或部分选中状态的颜色。与[selectedColor](ts-basic-components-checkboxgroup.md#selectedcolor)相比，resColor参数新增了对undefined类型的支持。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resColor | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[ResourceColor](ts-types.md#resourcecolor)> | 是 | 被选中或部分选中状态的颜色。  当resColor的值为undefined时，默认值：$r('sys.color.ohos\_id\_color\_text\_primary\_activated')  异常值按照默认值处理。 |

### unselectedColor10+

PhonePC/2in1TabletTVWearable

unselectedColor(value: ResourceColor)

设置非选中状态边框颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 非选中状态边框颜色。  默认值：$r('sys.color.ohos\_id\_color\_switch\_outline\_off')。 |

### unselectedColor18+

PhonePC/2in1TabletTVWearable

unselectedColor(resColor: Optional<ResourceColor>)

设置非选中状态边框颜色。与[unselectedColor](ts-basic-components-checkboxgroup.md#unselectedcolor10)10+相比，resColor参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resColor | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[ResourceColor](ts-types.md#resourcecolor)> | 是 | 非选中状态边框颜色。  当resColor的值为undefined时，默认值：$r('sys.color.ohos\_id\_color\_switch\_outline\_off')。 |

### mark10+

PhonePC/2in1TabletTVWearable

mark(value: MarkStyle)

设置多选框内部图标样式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [MarkStyle](ts-types.md#markstyle10对象说明) | 是 | 多选框内部图标样式。 |

### mark18+

PhonePC/2in1TabletTVWearable

mark(style: Optional<MarkStyle>)

设置多选框内部图标样式。与[mark](ts-basic-components-checkboxgroup.md#mark10)10+相比，style参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[MarkStyle](ts-types.md#markstyle10对象说明)> | 是 | 多选框内部图标样式。  当style的值为undefined时，维持上次取值。 |

### checkboxShape12+

PhonePC/2in1TabletTVWearable

checkboxShape(value: CheckBoxShape)

设置CheckboxGroup组件形状，包括圆形和圆角方形。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [CheckBoxShape](ts-appendix-enums.md#checkboxshape11) | 是 | 设置CheckboxGroup组件形状，包括圆形和圆角方形。  默认值：CheckBoxShape.CIRCLE  **说明：**  CheckboxGroup组件将按照设置的形状显示。  CheckboxGroup内所有未单独设置shape类型的Checkbox，其形状将与CheckboxGroup保持一致。  CheckboxGroup内已单独设置shape类型的Checkbox，其形状将优先于CheckboxGroup的设置，按照自身设置显示。 |

### checkboxShape18+

PhonePC/2in1TabletTVWearable

checkboxShape(shape: Optional<CheckBoxShape>)

设置CheckboxGroup组件形状，包括圆形和圆角方形。与[checkboxShape](ts-basic-components-checkboxgroup.md#checkboxshape12)12+相比，shape参数新增了对undefined类型的支持。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| shape | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[CheckBoxShape](ts-appendix-enums.md#checkboxshape11)> | 是 | 设置CheckboxGroup组件形状，包括圆形和圆角方形。  当shape的值为undefined时，默认值为CheckBoxShape.CIRCLE。  **说明：**  CheckboxGroup组件将按照设置的形状显示。  CheckboxGroup内所有未单独设置shape类型的Checkbox，其形状将与CheckboxGroup保持一致。  CheckboxGroup内已单独设置shape类型的Checkbox，其形状将优先于CheckboxGroup的设置，按照自身设置显示。 |

### contentModifier21+

PhonePC/2in1TabletTVWearable

contentModifier(modifier: Optional<ContentModifier<CheckBoxGroupConfiguration>>)

定制CheckboxGroup内容区的方法。设置该属性时，其他属性设置会失效。

说明

该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [Optional](ts-universal-attributes-custom-property.md#optionalt)<ContentModifier<[CheckBoxGroupConfiguration](ts-basic-components-checkboxgroup.md#checkboxgroupconfiguration21对象说明)>> | 是 | 在CheckboxGroup组件上，定制内容区的方法。  modifier：内容修改器，开发者需要自定义类以实现ContentModifier接口。  当modifier的值为undefined时，不使用内容修改器。 |

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](ts-component-general-events.md)外，还支持以下事件：

### onChange

PhonePC/2in1TabletTVWearable

onChange(callback: OnCheckboxGroupChangeCallback)

CheckboxGroup的选中状态或群组内的Checkbox的选中状态发生变化时，触发回调。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnCheckboxGroupChangeCallback](ts-basic-components-checkboxgroup.md#oncheckboxgroupchangecallback18) | 是 | 多选框群组的信息。 |

### onChange18+

PhonePC/2in1TabletTVWearable

onChange(callback: Optional<OnCheckboxGroupChangeCallback>)

CheckboxGroup的选中状态或群组内的Checkbox的选中状态发生变化时，触发回调。与[onChange](ts-basic-components-checkboxgroup.md#onchange)相比，callback参数新增了对undefined类型的支持。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[OnCheckboxGroupChangeCallback](ts-basic-components-checkboxgroup.md#oncheckboxgroupchangecallback18)> | 是 | 多选框群组的信息。  当callback的值为undefined时，不使用回调函数。 |

## OnCheckboxGroupChangeCallback18+

PhonePC/2in1TabletTVWearable

type OnCheckboxGroupChangeCallback = (value: CheckboxGroupResult) => void

多选框群组的信息。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [CheckboxGroupResult](ts-basic-components-checkboxgroup.md#checkboxgroupresult对象说明) | 是 | 多选框群组的信息。 |

## CheckboxGroupResult对象说明

PhonePC/2in1TabletTVWearable

多选框群组的名称和状态。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | Array<string> | 否 | 否 | 群组内所有被选中的多选框名称。 |
| status | [SelectStatus](ts-basic-components-checkboxgroup.md#selectstatus枚举说明) | 否 | 否 | 选中状态。 |

## SelectStatus枚举说明

PhonePC/2in1TabletTVWearable

多选框群组的选中状态。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| All | 0 | 群组多选择框全部选择。 |
| Part | 1 | 群组多选择框部分选择。 |
| None | 2 | 群组多选择框全部没有选择。 |

## CheckBoxGroupConfiguration21+对象说明

PhonePC/2in1TabletTVWearable

开发者必须自定义此类以实现ContentModifier接口，使用方法见[contentModifier](ts-basic-components-checkboxgroup.md#contentmodifier21)。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 当前多选框群组名称。 |
| status | [SelectStatus](ts-basic-components-checkboxgroup.md#selectstatus枚举说明) | 否 | 否 | 表示多选框群组的选中状态。 |
| triggerChange | Callback<boolean> | 否 | 否 | 触发多选框群组选中状态变化。true表示从部分选中或未选中变为全部选中，false表示从全部选中或部分选中变为全部未选中。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置多选框群组）

该示例用于控制多选框全选或者不全选状态。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct CheckboxExample {
5. build() {
6. Scroll() {
7. Column() {
8. // 全选按钮
9. Flex({ justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
10. CheckboxGroup({ group: 'checkboxGroup' })
11. .checkboxShape(CheckBoxShape.ROUNDED_SQUARE)
12. .selectedColor('#007DFF')
13. .onChange((itemName: CheckboxGroupResult) => {
14. console.info("checkbox group content" + JSON.stringify(itemName));
15. })
16. Text('Select All').fontSize(14).lineHeight(20).fontColor('#182431').fontWeight(500)
17. }

19. // 选项1
20. Flex({ justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
21. Checkbox({ name: 'checkbox1', group: 'checkboxGroup' })
22. .selectedColor('#007DFF')
23. .shape(CheckBoxShape.ROUNDED_SQUARE)
24. .onChange((value: boolean) => {
25. console.info('Checkbox1 change is' + value);
26. })
27. Text('Checkbox1').fontSize(14).lineHeight(20).fontColor('#182431').fontWeight(500)
28. }.margin({ left: 36 })

30. // 选项2
31. Flex({ justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
32. Checkbox({ name: 'checkbox2', group: 'checkboxGroup' })
33. .selectedColor('#007DFF')
34. .shape(CheckBoxShape.ROUNDED_SQUARE)
35. .onChange((value: boolean) => {
36. console.info('Checkbox2 change is' + value);
37. })
38. Text('Checkbox2').fontSize(14).lineHeight(20).fontColor('#182431').fontWeight(500)
39. }.margin({ left: 36 })

41. // 选项3
42. Flex({ justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
43. Checkbox({ name: 'checkbox3', group: 'checkboxGroup' })
44. .selectedColor('#007DFF')
45. .shape(CheckBoxShape.ROUNDED_SQUARE)
46. .onChange((value: boolean) => {
47. console.info('Checkbox3 change is' + value);
48. })
49. Text('Checkbox3').fontSize(14).lineHeight(20).fontColor('#182431').fontWeight(500)
50. }.margin({ left: 36 })
51. }
52. }
53. }
54. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/885_XCUaQyKTu1bbHQbaRg/zh-cn_image_0000002558606564.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055156Z&HW-CC-Expire=86400&HW-CC-Sign=39CE9BF255603BC3CBC5ABD47489A5BA41EED2EE862E726728B439679779D82D)

### 示例2（自定义勾选样式）

该示例通过配置mark实现自定义多选框群组的勾选样式。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {

6. build() {
7. Row() {
8. Column() {
9. Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
10. CheckboxGroup({ group: 'checkboxGroup' })
11. .checkboxShape(CheckBoxShape.ROUNDED_SQUARE)
12. .selectedColor(Color.Orange)
13. .onChange((itemName: CheckboxGroupResult) => {
14. console.info("checkbox group content" + JSON.stringify(itemName));
15. })
16. .mark({
17. strokeColor:Color.Black,
18. size: 40,
19. strokeWidth: 5
20. })
21. .unselectedColor(Color.Red)
22. .width(30)
23. .height(30)
24. Text('Select All').fontSize(20)
25. }.margin({right:15})
26. Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
27. Checkbox({ name: 'checkbox1', group: 'checkboxGroup' })
28. .selectedColor(0x39a2db)
29. .shape(CheckBoxShape.ROUNDED_SQUARE)
30. .onChange((value: boolean) => {
31. console.info('Checkbox1 change is'+ value);
32. })
33. .mark({
34. strokeColor:Color.Black,
35. size: 50,
36. strokeWidth: 5
37. })
38. .unselectedColor(Color.Red)
39. .width(30)
40. .height(30)
41. Text('Checkbox1').fontSize(20)
42. }
43. Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
44. Checkbox({ name: 'checkbox2', group: 'checkboxGroup' })
45. .selectedColor(0x39a2db)
46. .shape(CheckBoxShape.ROUNDED_SQUARE)
47. .onChange((value: boolean) => {
48. console.info('Checkbox2 change is' + value);
49. })
50. .width(30)
51. .height(30)
52. Text('Checkbox2').fontSize(20)
53. }
54. Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
55. Checkbox({ name: 'checkbox3', group: 'checkboxGroup' })
56. .selectedColor(0x39a2db)
57. .shape(CheckBoxShape.ROUNDED_SQUARE)
58. .onChange((value: boolean) => {
59. console.info('Checkbox3 change is' + value);
60. })
61. .width(30)
62. .height(30)
63. Text('Checkbox3').fontSize(20)
64. }
65. }
66. .width('100%')
67. }
68. .height('100%')
69. }
70. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/Vgzdc1HqQ0-XJ_HzHUQxzA/zh-cn_image_0000002589326091.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055156Z&HW-CC-Expire=86400&HW-CC-Sign=865FB59F86ECB1A5DF1E33222ECD642303CBA2FA02D9D24E84840D91FE232830)

### 示例3（自定义多选框样式）

从API version 21开始，该示例通过[contentModifier](ts-basic-components-checkboxgroup.md#contentmodifier21)属性实现了自定义复选框群组样式的功能。自定义样式实现了一个五边形复选框群组，如果全部选中，内部会出现红色三角图案，标题会显示全选字样；如果部分选中，三角图案显示蓝色，标题会显示部分选中字样；如果未选中，三角图案消失，标题会显示未选中。

```
1. // xxx.ets
2. class MyCheckboxGroupStyle implements ContentModifier<CheckBoxGroupConfiguration> {
3. selectedColor: Color = Color.Black;

5. constructor(selectedColor: Color) {
6. this.selectedColor = selectedColor;
7. }

9. applyContent(): WrappedBuilder<[CheckBoxGroupConfiguration]> {
10. return wrapBuilder(buildCheckboxgroup);
11. }
12. }
13. let statusString: string[] = ['全选', '部分选中', '全不选'];
14. @Builder
15. function buildCheckboxgroup(config: CheckBoxGroupConfiguration) {
16. Column({ space: 10 }) {
17. Text(config.name + " " + statusString[config.status ]).margin({ right: 70, top: 50 })
18. Text(config.enabled ? "enabled true" : "enabled false").margin({ right: 110 })
19. Shape() {
20. Path()
21. .width(100)
22. .height(100)
23. .commands('M100 0 L0 100 L50 200 L150 200 L200 100 Z')
24. .fillOpacity(0)
25. .strokeWidth(3)
26. .onClick(() => {
27. console.info('checkboxgroup status ', statusString[config.status])
28. if (config.status === SelectStatus.All ||  config.status === SelectStatus.Part) {
29. config.triggerChange(false);
30. console.info('checkboxgroup not selected')
31. } else {
32. config.triggerChange(true);
33. console.info('checkboxgroup selected')
34. }
35. })
36. .opacity(config.enabled ? 1 : 0.1)
37. Path()
38. .width(10)
39. .height(10)
40. .commands('M50 0 L100 100 L0 100 Z')
41. .visibility(config.status === SelectStatus.All ? Visibility.Visible : Visibility.Hidden)
42. .fill(config.status === SelectStatus.All ? (config.contentModifier as MyCheckboxGroupStyle).selectedColor : Color.Black)
43. .stroke((config.contentModifier as MyCheckboxGroupStyle).selectedColor)
44. .margin({ left: 10, top: 10 })
45. .opacity(config.enabled ? 1 : 0.1)
46. Path()
47. .width(10)
48. .height(10)
49. .commands('M50 0 L100 100 L0 100 Z')
50. .visibility(config.status === SelectStatus.Part ? Visibility.Visible : Visibility.Hidden)
51. .fill(config.status === SelectStatus.Part ? Color.Blue : Color.Black)
52. .stroke((config.contentModifier as MyCheckboxGroupStyle).selectedColor)
53. .margin({ left: 10, top: 10 })
54. .opacity(config.enabled ? 1 : 0.1)
55. }
56. .width(300)
57. .height(200)
58. .viewPort({
59. x: 0,
60. y: 0,
61. width: 310,
62. height: 310
63. })
64. .strokeLineJoin(LineJoinStyle.Miter)
65. .strokeMiterLimit(5)
66. .margin({ left: 50 })
67. }
68. }

70. @Entry
71. @Component
72. struct Index {
73. @State checkboxEnabled: boolean = true;

75. build() {
76. Column({ space: 100 }) {
77. CheckboxGroup({  group: 'checkboxGroup' })
78. .contentModifier(new MyCheckboxGroupStyle(Color.Red))
79. .onChange((itemName: CheckboxGroupResult) => {
80. console.info(" CheckboxGroup onChange: " + JSON.stringify(itemName));
81. })
82. .enabled(this.checkboxEnabled)

84. Row() {
85. Toggle({ type: ToggleType.Switch, isOn: true }).onChange((value: boolean) => {
86. if (value) {
87. this.checkboxEnabled = true;
88. } else {
89. this.checkboxEnabled = false;
90. }
91. })
92. }.position({ x: 50, y: 130 })
93. Row() {
94. Checkbox({ name: '复选框1', group: 'checkboxGroup' })
95. .onChange((value: boolean) => {
96. console.info('复选框1 change to ' + value);
97. })
98. Text('复选框1').fontSize(20)
99. }
100. .position({ x: 50, y: 230 })
101. Row() {
102. Checkbox({ name: '复选框2', group: 'checkboxGroup' })
103. .onChange((value: boolean) => {
104. console.info('复选框2 change to ' + value);
105. })
106. Text('复选框2').fontSize(20)
107. }
108. .position({ x: 50, y: 260 })
109. }.margin({ top: 30 })
110. }
111. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/kmjofPQ_RHS-vNUMuZCMcg/zh-cn_image_0000002589246033.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055156Z&HW-CC-Expire=86400&HW-CC-Sign=D3CF42687378DE9FA117050B1E1C7E37BD4DFF88D35A3B33B10D5B2AAA9142E5)

### 示例4（设置全选）

该示例实现了在结合带缓存功能的组件使用时(如List)，未被创建的Checkbox全选的功能。

```
1. class BasicDataSource implements IDataSource {
2. private listeners: DataChangeListener[] = [];
3. private originDataArray: checkboxItemData[] = [];

5. public totalCount(): number {
6. return this.originDataArray.length;
7. }

9. public getData(index: number): checkboxItemData {
10. return this.originDataArray[index];
11. }

13. registerDataChangeListener(listener: DataChangeListener): void {
14. if (this.listeners.indexOf(listener) < 0) {
15. console.info('add listener');
16. this.listeners.push(listener);
17. }
18. }

20. unregisterDataChangeListener(listener: DataChangeListener): void {
21. const pos = this.listeners.indexOf(listener);
22. if (pos >= 0) {
23. console.info('remove listener');
24. this.listeners.splice(pos, 1);
25. }
26. }

28. notifyDataReload(): void {
29. this.listeners.forEach(listener => {
30. listener.onDataReloaded();
31. });
32. }

34. notifyDataAdd(index: number): void {
35. this.listeners.forEach(listener => {
36. listener.onDataAdd(index);
37. });
38. }

40. notifyDataChange(index: number): void {
41. this.listeners.forEach(listener => {
42. listener.onDataChange(index);
43. });
44. }

46. notifyDataDelete(index: number): void {
47. this.listeners.forEach(listener => {
48. listener.onDataDelete(index);
49. });
50. }

52. notifyDataMove(from: number, to: number): void {
53. this.listeners.forEach(listener => {
54. listener.onDataMove(from, to);
55. });
56. }

58. notifyDatasetChange(operations: DataOperation[]): void {
59. this.listeners.forEach(listener => {
60. listener.onDatasetChange(operations);
61. });
62. }
63. }

65. interface checkboxItemData {
66. isCheck: boolean;
67. itemName: string;
68. }

71. class MyDataSource extends BasicDataSource {
72. private dataArray: checkboxItemData[] = [];

74. public totalCount(): number {
75. return this.dataArray.length;
76. }

78. public getData(index: number): checkboxItemData {
79. return this.dataArray[index];
80. }

82. public pushData(data: checkboxItemData): void {
83. this.dataArray.push(data);
84. this.notifyDataAdd(this.dataArray.length - 1);
85. }

87. public operateData(isSelect: boolean): void {
88. this.dataArray.forEach((item) => {
89. item.isCheck = isSelect
90. })

92. this.notifyDataReload()
93. }

95. public operateItem(isSelect: boolean, index: number): void {
96. this.dataArray[index].isCheck = isSelect
97. this.notifyDataChange(index)
98. }

100. public getDataSource(): checkboxItemData[] {
101. return this.dataArray
102. }
103. }

105. @Entry
106. @Component
107. struct MyComponent {
108. private data: MyDataSource = new MyDataSource();

110. aboutToAppear() {
111. for (let i = 0; i <= 100; i++) {
112. this.data.pushData({ isCheck: false, itemName: `checkbox ${i}` });
113. }
114. }

116. @State isSelectAll: boolean = false

118. build() {
119. Column() {
120. Flex({ justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
121. CheckboxGroup({ group: "group" })
122. .selectAll(this.isSelectAll)
123. .hitTestBehavior(HitTestMode.None)
124. Text("全选").fontSize(25)
125. }.onClick(() => {
126. this.isSelectAll = !this.isSelectAll
127. this.data.operateData(this.isSelectAll)
128. }).padding({ left: 10 })

130. List({ space: 3 }) {
131. LazyForEach(this.data, (item: checkboxItemData, index: number) => {
132. ListItem() {
133. Row() {
134. Checkbox({ name: `checkbox-${item}` })
135. .select(item.isCheck)
136. .onChange((value: boolean) => {
137. this.data.operateItem(value, index)
138. let dataSource = this.data.getDataSource()
139. this.isSelectAll = dataSource.every((item) => item.isCheck === true)
140. })
141. Text(item.itemName).fontSize(20)
142. }.margin({ left: 10, right: 10 })
143. }

145. }, (item: checkboxItemData) => item.itemName + item.isCheck)
146. }.cachedCount(5)
147. }
148. }
149. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/bJQ6npmISZqXK5HNk8_1Dw/zh-cn_image_0000002558766224.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055156Z&HW-CC-Expire=86400&HW-CC-Sign=9AB7F7D23C482294CE18CC7FB8FEAB36925FE3ECF8903A1B1CA6E375ADA2D0D2)
