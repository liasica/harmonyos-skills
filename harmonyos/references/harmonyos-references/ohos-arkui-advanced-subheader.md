---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-subheader
title: SubHeader
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 系统预置UI组件库 > SubHeader
category: harmonyos-references
scraped_at: 2026-04-29T13:53:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1599ccdd91dcac9acea36cc86f49460b5210a602eacc09cc4d249a9210c98114
---

子标题，用于列表项或内容项顶部，将该列表或内容划分为一个区块，子标题名称用来概括该区块内容。

说明

* 该组件从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件仅可在Stage模型下使用。
* 如果SubHeader设置[通用属性](ts-component-general-attributes.md)和[通用事件](ts-component-general-events.md)，编译工具链会额外生成节点\_\_Common\_\_，并将通用属性或通用事件挂载在\_\_Common\_\_上，而不是直接应用到SubHeader本身。这可能导致开发者设置的通用属性或通用事件不生效或不符合预期，因此，不建议SubHeader设置通用属性和通用事件。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { SubHeader } from '@kit.ArkUI';
```

## 子组件

PhonePC/2in1TabletTVWearable

无

说明

不支持设置文本相关。

## SubHeader

PhonePC/2in1TabletTVWearable

SubHeader({icon?: ResourceStr, iconSymbolOptions?: SymbolOptions, primaryTitle?: ResourceStr, secondaryTitle?: ResourceStr, select?: SelectOptions, operationType?: OperationType, operationItem?: Array<OperationOption>, operationSymbolOptions?: Array<SymbolOptions>, primaryTitleModifier?: TextModifier, secondaryTitleModifier?: TextModifier, titleBuilder?: () => void, contentMargin?: LocalizedMargin, contentPadding?: LocalizedPadding})

**装饰器类型：**@Component

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| icon | [ResourceStr](ts-types.md#resourcestr) | 否 | @Prop | 图标设置项。  默认值：undefined，表示不显示图标。  当使用secondaryTitle属性时，设置icon属性才会生效。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| iconSymbolOptions12+ | [SymbolOptions](ohos-arkui-advanced-subheader.md#symboloptions12) | 否 | - | icon为[SymbolGlyph](ts-basic-components-symbolglyph.md)时的设置项。  默认值：undefined，表示不显示图标。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| primaryTitle | [ResourceStr](ts-types.md#resourcestr) | 否 | @Prop | 标题内容。  默认值：undefined，表示不显示标题。  当同时使用primaryTitle、secondaryTitle、icon属性时，设置primaryTitle属性不生效。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| secondaryTitle | [ResourceStr](ts-types.md#resourcestr) | 否 | @Prop | 副标题内容。  默认值：undefined，表示不显示副标题。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| select | [SelectOptions](ohos-arkui-advanced-subheader.md#selectoptions) | 否 | - | select内容以及事件。  默认值：undefined，表示不显示下拉框。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| operationType | [OperationType](ohos-arkui-advanced-subheader.md#operationtype) | 否 | @Prop | 操作区（右侧）元素样式。  默认值：OperationType.BUTTON  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| operationItem | Array<[OperationOption](ohos-arkui-advanced-subheader.md#operationoption)> | 否 | - | 操作区（右侧）的设置项。  默认值：undefined，表示不显示操作区。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| operationSymbolOptions12+ | Array<[SymbolOptions](ohos-arkui-advanced-subheader.md#symboloptions12)> | 否 | - | operationType为OperationType.ICON\_GROUP，  operationItem设置多个图标，图标为[SymbolGlyph](ts-basic-components-symbolglyph.md)时的设置项。  默认值：undefined，表示不设置Symbol图标。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| primaryTitleModifier12+ | [TextModifier](ts-universal-attributes-attribute-modifier.md#自定义modifier) | 否 | - | 设置标题文本属性，如设置标题颜色、字体大小、字重等。  默认值：undefined，表示使用系统默认样式。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| secondaryTitleModifier12+ | [TextModifier](ts-universal-attributes-attribute-modifier.md#自定义modifier) | 否 | - | 设置副标题文本属性，如设置标题颜色、字体大小、字重等。  默认值：undefined，表示使用系统默认样式。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| titleBuilder12+ | () => void | 否 | @BuilderParam | 自定义标题区内容  默认值：undefined，表示不采用自定义标题定义标题。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| contentMargin12+ | [LocalizedMargin](ts-types.md#localizedmargin12) | 否 | @Prop | 子标题外边距，不支持设置负数。  默认值：  {start: LengthMetrics.resource(  $r('sys.float.margin\_left')),  end: LengthMetrics.resource(  $r('sys.float.margin\_right'))}  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| contentPadding12+ | [LocalizedPadding](ts-types.md#localizedpadding12) | 否 | @Prop | 子标题内边距。  默认值：  左侧为副标题或副标题加图标时：  {start: LengthMetrics.vp(12), end: LengthMetrics.vp(12)}。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| titleAccessibilityText23+ | [ResourceStr](ts-types.md#resourcestr) | 否 | @Prop | 设置标题自定义朗读内容。  默认值：undefined  值为undefined时，默认朗读组件显示的标题内容。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |

## OperationType

PhonePC/2in1TabletTVWearable

定义子标题操作区的元素样式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TEXT\_ARROW | 0 | 文本按钮（带右箭头）。 |
| BUTTON | 1 | 文本按钮（不带右箭头）。 |
| ICON\_GROUP | 2 | 图标按钮（最多支持配置三张图标）。 |
| LOADING | 3 | 加载动画。 |

## SelectOptions

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | Array<[SelectOption](ts-basic-components-select.md#selectoption对象说明)> | 否 | 否 | 下拉选项内容。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| selected | number | 否 | 是 | 设置下拉菜单初始选项的索引。  取值范围：大于等于-1。  第一项的索引为0。  当不设置selected属性时，默认选择值为-1，菜单项不选中。  若设置数值小于-1，按不选中处理。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| value | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 设置下拉按钮本身的文本内容。  默认值：空字符串。  **说明**：如果文本大于列宽时，文本被截断。从API version 20开始，支持Resource类型。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| onSelect | (index: number, value?: string) => void | 否 | 是 | 下拉菜单选中某一项的回调。  - index：选中项的索引。  - value：选中项的值。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| defaultFocus18+ | boolean | 否 | 是 | 下拉按钮是否为默认焦点。  true：下拉按钮是默认焦点。  false：下拉按钮不是默认焦点。  默认值：false  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

## OperationOption

PhonePC/2in1TabletTVWearable

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 文本内容。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| action | ()=>void | 否 | 是 | 子标题右侧按钮点击事件。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| accessibilityLevel18+ | string | 否 | 是 | 子标题右侧按钮无障碍重要性。用于控制当前项是否可被无障碍辅助服务所识别。  支持的值为：  "auto"：当前组件会转换"yes"。  "yes"：当前组件可被无障碍辅助服务所识别。  "no"：当前组件不可被无障碍辅助服务所识别。  "no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。  默认值："auto"  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| accessibilityText18+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 子标题右侧按钮的无障碍文本属性。当组件不包含文本属性时，屏幕朗读选中此组件时不播报，使用者无法清楚地知道当前选中了什么组件。为了解决此场景，开发人员可为不包含文字信息的组件设置无障碍文本，当屏幕朗读选中此组件时播报无障碍文本的内容，帮助屏幕朗读的使用者清楚地知道自己选中了什么组件。  默认值：类型为TEXT\_ARROW和BUTTON时默认值为当前项value属性内容，其他类型默认值为“ ”。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| accessibilityDescription18+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 子标题右侧按钮的无障碍描述。此描述用于向用户详细解释当前组件，开发人员应为组件的这一属性提供较为详尽的文本说明，以协助用户理解即将执行的操作及其可能产生的后果。特别是当这些后果无法仅从组件的属性和无障碍文本中直接获知时。如果组件同时具备文本属性和无障碍说明属性，当组件被选中时，系统将首先播报组件的文本属性，随后播报无障碍说明属性的内容。  默认值：类型为LOADING时，默认值为“正在加载”，其他类型默认值为“单指双击即可执行”。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| defaultFocus18+ | boolean | 否 | 是 | 子标题右侧按钮是否为默认焦点。  true：子标题右侧按钮是默认焦点。  false：子标题右侧按钮不是默认焦点。  默认值：false  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

## SymbolOptions12+

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fontColor | Array<[ResourceColor](ts-types.md#resourcecolor)> | 否 | 是 | 设置[SymbolGlyph](ts-basic-components-symbolglyph.md)颜色。  默认值：不同渲染策略下默认值不同。 |
| fontSize | number | string | [Resource](ts-types.md#resource) | 否 | 是 | 设置[SymbolGlyph](ts-basic-components-symbolglyph.md)大小。  number类型取值范围：大于等于0。  设置string类型时，支持number类型取值的字符串形式，可以附带单位，例如："10"，"10fp"。  默认值：系统默认值。 |
| fontWeight | number | [FontWeight](ts-appendix-enums.md#fontweight) | string | 否 | 是 | 设置[SymbolGlyph](ts-basic-components-symbolglyph.md)粗细。  number类型取值[100,900]，取值间隔为100，默认为400，取值越大，字体越粗。  string类型仅支持number类型取值的字符串形式，例如“400”，以及“bold”、“bolder”、“lighter”、“regular” 、“medium”分别对应FontWeight中相应的枚举值。  默认值：FontWeight.Normal |
| renderingStrategy | [SymbolRenderingStrategy](ts-basic-components-symbolglyph.md#symbolrenderingstrategy11枚举说明) | 否 | 是 | 设置[SymbolGlyph](ts-basic-components-symbolglyph.md)渲染策略。  默认值：SymbolRenderingStrategy.SINGLE  **说明：**  $r('sys.symbol.ohos\_\*')中引用的资源仅ohos\_trash\_circle、ohos\_folder\_badge\_plus、ohos\_lungs支持分层与多色模式。 |
| effectStrategy | [SymbolEffectStrategy](ts-basic-components-symbolglyph.md#symboleffectstrategy11枚举说明) | 否 | 是 | 设置[SymbolGlyph](ts-basic-components-symbolglyph.md)动效策略。  默认值：SymbolEffectStrategy.NONE  **说明：**  $r('sys.symbol.ohos\_\*')中引用的资源仅ohos\_wifi支持层级动效模式。 |

## 事件

PhonePC/2in1TabletTVWearable

不支持[通用事件](ts-component-general-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（效率型子标题）

该示例主要演示子标题左侧为icon、secondaryTitle，右侧operationType为按钮类型。

```
1. import { Prompt, OperationType, SubHeader } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct SubHeaderExample {
6. build() {
7. Column() {
8. SubHeader({
9. icon: $r('sys.media.ohos_ic_public_email'),
10. secondaryTitle: '二级标题',
11. operationType: OperationType.BUTTON,
12. operationItem: [{
13. value: '操作',
14. action: () => {
15. Prompt.showToast({ message: 'demo' });
16. }
17. }]
18. })
19. }
20. }
21. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/GnbvgwKZTt62uJ0KXBL4ww/zh-cn_image_0000002589326523.png?HW-CC-KV=V1&HW-CC-Date=20260429T055304Z&HW-CC-Expire=86400&HW-CC-Sign=418907F47556976D39BBA50F3AF1868EFF54C2C00A2E37267CB80C8CCB639283)

### 示例2（双行文本内容型子标题）

该示例主要演示子标题左侧为primaryTitle、secondaryTitle，右侧operationType类型为TEXT\_ARROW。

```
1. import { Prompt, OperationType, SubHeader } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct SubHeaderExample {
6. build() {
7. Column() {
8. SubHeader({
9. primaryTitle: '一级标题',
10. secondaryTitle: '二级标题',
11. operationType: OperationType.TEXT_ARROW,
12. operationItem: [{
13. value: '更多',
14. action: () => {
15. Prompt.showToast({ message: 'demo' });
16. }
17. }]
18. })
19. }
20. }
21. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/8vGJwMFJTF-O0D4kgUpIHg/zh-cn_image_0000002589246465.png?HW-CC-KV=V1&HW-CC-Date=20260429T055304Z&HW-CC-Expire=86400&HW-CC-Sign=D69166B9FF7120FA4C6D90A282211C1F11856D35480E2D570CC87F526FB5886F)

### 示例3（spinner型内容型子标题）

该示例主要演示子标题左侧为select，右侧operationType类型为ICON\_GROUP。

```
1. import { Prompt, OperationType, SubHeader } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct SubHeaderExample {
6. build() {
7. Column() {
8. SubHeader({
9. // 左侧为select选择器
10. select: {
11. options: [{ value: 'aaa' }, { value: 'bbb' }, { value: 'ccc' }],
12. value: 'selectDemo',
13. selected: 2,
14. onSelect: () => {
15. Prompt.showToast({ message: 'demo' });
16. }
17. },
18. operationType: OperationType.ICON_GROUP,
19. // 右侧为三个icon图标
20. operationItem: [{
21. value: $r('sys.media.ohos_ic_public_email'),
22. action: () => {
23. Prompt.showToast({ message: 'demo' })
24. }
25. }, {
26. value: $r('sys.media.ohos_ic_public_email'),
27. action: () => {
28. Prompt.showToast({ message: 'demo' });
29. }
30. }, {
31. value: $r('sys.media.ohos_ic_public_email'),
32. action: () => {
33. Prompt.showToast({ message: 'demo' });
34. }
35. }]
36. })
37. }
38. }
39. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/Yyh4ZAYVThOHnTiBRgXxmg/zh-cn_image_0000002558766658.png?HW-CC-KV=V1&HW-CC-Date=20260429T055304Z&HW-CC-Expire=86400&HW-CC-Sign=8E835B5FC4C0893B88BF9028685C898DC4059BCEE7224AC3E9A31FB484D5C457)

### 示例4（设置左侧symbol图标）

该示例主要演示子标题左侧icon设置symbol图标。

```
1. import { Prompt, OperationType, SubHeader } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct SubHeaderExample {
6. build() {
7. Column() {
8. SubHeader({
9. // 设置icon为symbol图标
10. icon: $r('sys.symbol.ohos_wifi'),
11. iconSymbolOptions: {
12. effectStrategy: SymbolEffectStrategy.HIERARCHICAL,
13. },
14. secondaryTitle: '标题',
15. operationType: OperationType.BUTTON,
16. operationItem: [{
17. value: '操作',
18. action: () => {
19. Prompt.showToast({ message: 'demo' });
20. }
21. }]
22. })
23. }
24. }
25. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/RoGL5PlbT8mKsMJ8BQWnKA/zh-cn_image_0000002558606998.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055304Z&HW-CC-Expire=86400&HW-CC-Sign=F52DDC57AFF7514C4EE0D952E70AC0D7EC6760EEFD3471F158BD8520DEBDC2CA)

### 示例5（设置右侧symbol图标）

该示例主要演示子标题operationType设置为OperationType.ICON\_GROUP，operationItem的value设置为symbol图标。

```
1. import { Prompt, OperationType, SubHeader } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct SubHeaderExample {
6. build() {
7. Column() {
8. SubHeader({
9. // 设置左侧select
10. select: {
11. options: [{ value: 'aaa' }, { value: 'bbb' }, { value: 'ccc' }],
12. value: 'selectDemo',
13. selected: 2,
14. onSelect: () => {
15. Prompt.showToast({ message: 'demo' });
16. }
17. },
18. operationType: OperationType.ICON_GROUP,
19. // 设置右侧icon
20. operationItem: [{
21. value: $r('sys.symbol.ohos_lungs'),
22. action: () => {
23. Prompt.showToast({ message: 'icon1' });
24. }
25. }, {
26. value: $r('sys.symbol.ohos_lungs'),
27. action: () => {
28. Prompt.showToast({ message: 'icon2' });
29. }
30. }, {
31. value: $r('sys.symbol.ohos_lungs'),
32. action: () => {
33. Prompt.showToast({ message: 'icon3' });
34. }
35. }],
36. // 设置右侧icon图标symbol样式
37. operationSymbolOptions: [{
38. fontWeight: FontWeight.Lighter,
39. }, {
40. renderingStrategy: SymbolRenderingStrategy.MULTIPLE_COLOR,
41. fontColor: [Color.Blue, Color.Grey, Color.Green],
42. }, {
43. renderingStrategy: SymbolRenderingStrategy.MULTIPLE_OPACITY,
44. fontColor: [Color.Blue, Color.Grey, Color.Green],
45. }]
46. })
47. }
48. }
49. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/bm_hYnqMSEGNu-QbAZ-lXg/zh-cn_image_0000002589326525.png?HW-CC-KV=V1&HW-CC-Date=20260429T055304Z&HW-CC-Expire=86400&HW-CC-Sign=7F3EF25330E3EF213EFA0725402C0CC565509E63A1E1880F6CE0BC811574BAC4)

### 示例6（自定义标题内容）

该示例主要演示SubHeader设置titleBuilder自定义标题内容的效果。

```
1. import { Prompt, OperationType, SubHeader } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct SubHeaderExample {
6. // 自定义左侧标题
7. @Builder
8. TitleBuilder(): void {
9. Text('自定义标题')
10. .fontSize(24)
11. .fontColor(Color.Blue)
12. .fontWeight(FontWeight.Bold)
13. }

15. build() {
16. Column() {
17. SubHeader({
18. // 调用TitleBuilder
19. titleBuilder: () => {
20. this.TitleBuilder();
21. },
22. primaryTitle: '一级标题',
23. secondaryTitle: '二级标题',
24. icon: $r('sys.symbol.ohos_star'),
25. operationType: OperationType.TEXT_ARROW,
26. operationItem: [{
27. value: '更多信息',
28. action: () => {
29. Prompt.showToast({ message: 'demo' });
30. }
31. }]
32. })
33. }
34. }
35. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/qy1Ui4FKT7iV8ARNA-M_Iw/zh-cn_image_0000002589246467.png?HW-CC-KV=V1&HW-CC-Date=20260429T055304Z&HW-CC-Expire=86400&HW-CC-Sign=D11B261BC1B4388FB2A06F27D37CFA52F6387CF64CACAE97EEC477AA7C765403)

### 示例7（自定义标题样式）

该示例主要演示SubHeader设置标题和副标题字体样式以及标题内外边距的效果。

```
1. import { Prompt, OperationType, SubHeader, LengthMetrics, TextModifier } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct SubHeaderExample {
6. // 设置主副标题文本颜色
7. @State primaryModifier: TextModifier = new TextModifier().fontColor(Color.Blue);
8. @State secondaryModifier: TextModifier = new TextModifier().fontColor(Color.Blue);

10. build() {
11. Column() {
12. SubHeader({
13. primaryTitle: 'primaryTitle',
14. secondaryTitle: 'secondaryTitle',
15. primaryTitleModifier: this.primaryModifier,
16. secondaryTitleModifier: this.secondaryModifier,
17. operationType: OperationType.TEXT_ARROW,
18. operationItem: [{
19. value: '更多信息',
20. action: () => {
21. Prompt.showToast({ message: 'demo' });
22. }
23. }],
24. // 标题内外间距
25. contentMargin: { start: LengthMetrics.vp(20), end: LengthMetrics.vp(20) },
26. contentPadding: { start: LengthMetrics.vp(20), end: LengthMetrics.vp(20) }
27. })
28. }
29. }
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/Zg0qUjalSlCNwlaDIpswLA/zh-cn_image_0000002558766660.png?HW-CC-KV=V1&HW-CC-Date=20260429T055304Z&HW-CC-Expire=86400&HW-CC-Sign=002F4E1A8B4D57CF3443B1C573043D8560A6BAA89AA84A79FC2A0722A046B948)

### 示例8（右侧按钮自定义播报）

从API version 18开始，该示例通过设置SubHeader的右侧按钮属性accessibilityText、accessibilityDescription、accessibilityLevel自定义屏幕朗读播报文本。

```
1. import { Prompt, OperationType, SubHeader } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct SubHeaderExample {
6. build() {
7. Column() {
8. Divider().color('grey').width('100%').height('2vp')
9. SubHeader({
10. // 图标+二级标题, 右侧button
11. icon: $r('sys.media.ohos_ic_public_email'),
12. secondaryTitle: '二级标题',
13. operationType: OperationType.BUTTON,
14. operationItem: [{
15. value: '操作',
16. action: () => {
17. Prompt.showToast({ message: 'demo' })
18. }
19. }]
20. })
21. Divider().color('grey').width('100%').height('2vp')
22. SubHeader({
23. // 右侧text_arrow
24. primaryTitle: '一级标题',
25. secondaryTitle: '二级标题',
26. operationType: OperationType.TEXT_ARROW,
27. operationItem: [{
28. value: '更多',
29. action: () => {
30. Prompt.showToast({ message: 'demo' })
31. }
32. }]
33. })
34. Divider().color('grey').width('100%').height('2vp')
35. SubHeader({
36. // 左侧select 右侧是icon_(依次获焦)
37. select: {
38. options: [{ value: 'aaa' }, { value: 'bbb' }, { value: 'ccc' }],
39. value: 'selectDemo',
40. selected: 0,
41. onSelect: (index: number, value?: string) => {
42. console.info(`SubHeader onSelect index : ${index}, value: ${value}`);
43. }
44. },
45. operationType: OperationType.ICON_GROUP,
46. operationItem: [{
47. value: $r('sys.media.ohos_ic_public_email'),
48. accessibilityText: '图标1',
49. accessibilityLevel: 'yes',
50. }, {
51. value: $r('sys.media.ohos_ic_public_email'),
52. accessibilityText: '图标2',
53. accessibilityLevel: 'no',
54. }, {
55. value: $r('sys.media.ohos_ic_public_email'),
56. accessibilityText: '图标3',
57. accessibilityDescription: '点击操作图标3',
58. }]
59. })
60. Divider().color('grey').width('100%').height('2vp')
61. }
62. }
63. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/mNlXWZs_T-20kU0juBV95w/zh-cn_image_0000002558607000.png?HW-CC-KV=V1&HW-CC-Date=20260429T055304Z&HW-CC-Expire=86400&HW-CC-Sign=34CD00BFB269EB04F3411E52099E6495DEDE5DF9F60D34EF6D8ED08728844C68)

### 示例9（右侧按钮设置默认获焦）

在获焦状态下，该示例通过设置SubHeader的右侧按钮属性defaultFocus使其默认获焦。

从API version 18开始，在[OperationOption](ohos-arkui-advanced-subheader.md#operationoption)中新增defaultFocus接口。

```
1. import { Prompt, OperationType, SubHeader } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct SubHeaderExample {
6. build() {
7. Column() {
8. SubHeader({
9. // 图标+二级标题, 右侧button
10. icon: $r('sys.media.ohos_ic_public_email'),
11. secondaryTitle: '二级标题',
12. operationType: OperationType.BUTTON,
13. operationItem: [{
14. value: '操作',
15. defaultFocus: true,
16. action: () => {
17. Prompt.showToast({ message: 'demo' })
18. }
19. }]
20. })
21. }
22. }
23. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/0HwwGdGsTESvpWUK0-BWlw/zh-cn_image_0000002589326527.png?HW-CC-KV=V1&HW-CC-Date=20260429T055304Z&HW-CC-Expire=86400&HW-CC-Sign=28AAA6908161957223695A7D255C002BE132DDC7CBFD7D2C38A7B4952D2A90B4)
