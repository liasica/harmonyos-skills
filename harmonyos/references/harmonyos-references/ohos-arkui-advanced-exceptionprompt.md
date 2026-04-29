---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-exceptionprompt
title: ExceptionPrompt
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 系统预置UI组件库 > ExceptionPrompt
category: harmonyos-references
scraped_at: 2026-04-29T13:52:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b36db8046816cd4595bb77460c48a4daed9f42b0158f3b25fc84d388294989e3
---

异常提示，适用于有异常需要提示异常内容的情况。

说明

* 该组件从API version 11开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件仅可在Stage模型下使用。
* 如果ExceptionPrompt设置[通用属性](ts-component-general-attributes.md)和[通用事件](ts-component-general-events.md)，编译工具链会额外生成节点\_\_Common\_\_，并将通用属性或通用事件挂载在\_\_Common\_\_上，而不是直接应用到ExceptionPrompt本身。这可能导致开发者设置的通用属性或通用事件不生效或不符合预期，因此，不建议ExceptionPrompt设置通用属性和通用事件。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { ExceptionPrompt, PromptOptions, MarginType } from '@kit.ArkUI';
```

## 子组件

PhonePC/2in1TabletTVWearable

无

## ExceptionPrompt

PhonePC/2in1TabletTVWearable

ExceptionPrompt({ options: PromptOptions, onTipClick?: ()=>void, onActionTextClick?: ()=>void })

**装饰器类型：**@Component

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| options | [PromptOptions](ohos-arkui-advanced-exceptionprompt.md#promptoptions) | 是 | @Prop | 指定当前异常提示的配置信息。 |
| onTipClick | ()=>void | 否 | - | 点击左侧提示文本的回调函数，缺省时不执行任何操作。 |
| onActionTextClick | ()=>void | 否 | - | 点击右侧图标按钮的回调函数。缺省时不执行任何操作。 |

## PromptOptions

PhonePC/2in1TabletTVWearable

PromptOptions定义options的类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| icon | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 指定当前异常提示的异常图标样式。  默认不设置或设置为undefined，异常图标不显示。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| symbolStyle18+ | [SymbolGlyphModifier](universal-attributes-attribute-symbolglyphmodifier.md#symbolglyphmodifier) | 否 | 是 | 指定当前异常提示的异常Symbol图标样式，优先级大于icon。  默认不设置或设置为undefined，Symbol图标不显示。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| tip | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 指定当前异常提示的文字提示内容。  支持默认内置四种状态文字资源如下：  1.无网络状态：显示网络未连接：引用ohos\_network\_not\_connected。  2.网络差状态：显示网络连接不稳定，请点击重试：引用ohos\_network\_connected\_unstable。  3.连不上服务器状态：显示无法连接到服务器，请点击重试：引用ohos\_unstable\_connect\_server。  4.有网但是获取不到内容状态：显示无法获取位置，请点击重试：引用ohos\_custom\_network\_tips\_left。  默认不设置或设置为undefined，文字提示内容不显示。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| marginType | [MarginType](ohos-arkui-advanced-exceptionprompt.md#margintype) | 否 | 否 | 指定当前异常提示的边距样式。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| actionText | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 指定当前异常提示的右侧图标按钮的文字内容。  默认不设置或设置为undefined，文字内容不显示。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| marginTop | [Dimension](ts-types.md#dimension10) | 否 | 否 | 指定当前异常提示的距离顶部的位置。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| isShown | boolean | 否 | 是 | 指定当前异常提示的显隐状态。  true：显示状态。  false：隐藏状态。  默认值：false  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## MarginType

PhonePC/2in1TabletTVWearable

MarginType定义marginType的类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT\_MARGIN | 0 | 默认边距：  边距1：引用ohos\_id\_card\_margin\_start。  边距2：引用ohos\_id\_card\_margin\_end。 |
| FIT\_MARGIN | 1 | 可适配边距：  边距1：引用ohos\_id\_max\_padding\_start。  边距2：引用ohos\_id\_max\_padding\_end。 |

## 事件

PhonePC/2in1TabletTVWearable

不支持[通用事件](ts-component-general-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置异常提示）

该示例展示了如何设置异常提示的异常图标、异常提示的文字、边距样式和右侧图标按钮的文字内容。

```
1. import { ExceptionPrompt, PromptOptions, MarginType } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. @State options: PromptOptions = {
7. icon: $r('sys.media.ohos_ic_public_fail'),
8. tip: '异常提示',
9. marginType: MarginType.DEFAULT_MARGIN,
10. actionText: '设置网络',
11. marginTop: 80,
12. isShown: true,
13. }

15. build() {
16. Column() {
17. ExceptionPrompt({
18. options: this.options,
19. onTipClick: () => {
20. // 单击左侧的文本切换到连接状态
21. },
22. onActionTextClick: () => {
23. // 点击“设置网络”按钮，打开设置网络弹窗界面
24. },
25. })
26. }
27. }
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/ixB-LDJhRqWlIhtLYyp99w/zh-cn_image_0000002589326499.png?HW-CC-KV=V1&HW-CC-Date=20260429T055258Z&HW-CC-Expire=86400&HW-CC-Sign=24E9224EBB73D0A41422333FCA4E60792C072C41188C61DFB10034EAE99D2B75)

### 示例2（设置弹窗类型的异常提示）

该示例使用自定义弹窗设置弹窗类型的异常提示。

```
1. import { ExceptionPrompt, PromptOptions, MarginType } from '@kit.ArkUI';

3. @CustomDialog
4. struct CustomDialogExample {
5. @Link textValue: string;
6. @Link inputValue: string;
7. @State options: PromptOptions = {
8. icon: $r('sys.media.ohos_ic_public_fail'),
9. tip: '异常提示！',
10. marginType: MarginType.DEFAULT_MARGIN,
11. actionText: '设置',
12. marginTop: 5,
13. isShown: true,
14. };
15. cancel: () => void = () => {
16. };
17. confirm: () => void = () => {
18. };
19. controller?: CustomDialogController;

21. // 若尝试在CustomDialog中传入多个其他的Controller，以实现在CustomDialog中打开另一个或另一些CustomDialog，
22. // 那么此处需要将指向自己的controller放在最后
23. build() {
24. Column() {
25. ExceptionPrompt({
26. options: this.options,
27. })
28. TextInput({ placeholder: '', text: this.textValue }).margin({ top: 70 }).height(60).width('90%')
29. .onChange((value: string) => {
30. this.textValue = value;
31. })
32. Text('Whether to change a text?').fontSize(16).margin({ bottom: 10 })
33. Flex({ justifyContent: FlexAlign.SpaceAround }) {
34. Button('cancel')
35. .onClick(() => {
36. this.controller?.close();
37. this.cancel();
38. }).backgroundColor(0xffffff).fontColor(Color.Black)
39. Button('confirm')
40. .onClick(() => {
41. this.inputValue = this.textValue;
42. this.controller?.close();
43. this.confirm();
44. }).backgroundColor(0xffffff).fontColor(Color.Red)
45. }.margin({ bottom: 10 })
46. }
47. }
48. }

50. @Entry
51. @Component
52. struct Index1 {
53. @State ButtonText: string = '';
54. @State MAP_HEIGHT: string = '30%';
55. @State duration: number = 2500;
56. @State tips: string = '';
57. @State actionText: string = '';
58. controller: TextInputController = new TextInputController();
59. cancel: () => void = () => {
60. };
61. confirm: () => void = () => {
62. };
63. @State options: PromptOptions = {
64. icon: $r('sys.media.ohos_ic_public_fail'),
65. tip: '',
66. marginType: MarginType.DEFAULT_MARGIN,
67. actionText: '',
68. marginTop: 80,
69. isShown: true,
70. }
71. @State textValue: string = '';
72. @State inputValue: string = 'click me';
73. dialogController: CustomDialogController | undefined = new CustomDialogController({
74. builder: CustomDialogExample({
75. cancel: this.onCancel,
76. confirm: this.onAccept,
77. textValue: $textValue,
78. inputValue: $inputValue,
79. }),
80. cancel: this.existApp,
81. autoCancel: true,
82. alignment: DialogAlignment.Bottom,
83. offset: { dx: 0, dy: -20 },
84. gridCount: 4,
85. customStyle: false,
86. })

88. aboutToDisappear() {
89. this.dialogController = undefined; // 将dialogController置空
90. }

92. onCancel() {
93. console.info('Callback when the first button is clicked');
94. }

96. onAccept() {
97. console.info('Callback when the second button is clicked');
98. }

100. existApp() {
101. console.info('Click the callback in the blank area');
102. }

104. build() {
105. Column() {
106. Button('Click Me')
107. .width('30%')
108. .margin({ top: 420 })
109. .zIndex(999)
110. .onClick(() => {
111. if (this.dialogController != undefined) {
112. this.dialogController.open();
113. }
114. })
115. }
116. .height('100%')
117. .width('100%')
118. }
119. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/LpZwV_yESTKNpP2cupvJMA/zh-cn_image_0000002589246441.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055258Z&HW-CC-Expire=86400&HW-CC-Sign=4503FC89D0A3F7E3B06236D0BA56A9F410150127A72426EB1E19DF5095D3B736)

### 示例3（设置Symbol类型图标）

从API version 18开始，该示例通过设置PromptOptions的属性symbolStyle，展示了自定义Symbol类型图标。

```
1. import { ExceptionPrompt, MarginType, SymbolGlyphModifier } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. build() {
7. Column() {
8. ExceptionPrompt({
9. options: {
10. icon: $r('sys.symbol.house'),
11. tip: '异常提示',
12. marginType: MarginType.DEFAULT_MARGIN,
13. actionText: '设置网络',
14. marginTop: 80,
15. isShown: true,
16. },
17. })
18. ExceptionPrompt({
19. options: {
20. icon: $r('sys.symbol.house'),
21. symbolStyle: new SymbolGlyphModifier($r('sys.symbol.bell')).fontColor([Color.Red]),
22. tip: '异常提示',
23. marginType: MarginType.DEFAULT_MARGIN,
24. actionText: '设置网络',
25. marginTop: 200,
26. isShown: true,
27. },
28. })
29. }
30. }
31. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/pKyjW0o9SbO7JCasR8zVGw/zh-cn_image_0000002558766634.png?HW-CC-KV=V1&HW-CC-Date=20260429T055258Z&HW-CC-Expire=86400&HW-CC-Sign=447386897A80130DB163A13C715388FF60384B50AF6E1685A9C6BDC6563B84F6)
