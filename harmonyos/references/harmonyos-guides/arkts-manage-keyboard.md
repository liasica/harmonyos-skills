---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-manage-keyboard
title: 管理软键盘
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用文本 > 管理软键盘
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bc9d3c604de70cd22c186407b2505e0a8c77c59dc8cf91a1ebfc111c8ae533b8
---

软键盘是用户交互的重要途径，提供文本输入功能。本文介绍在使用系统输入框组件（[TextInput](../harmonyos-references/ts-basic-components-textinput.md)、[TextArea](../harmonyos-references/ts-basic-components-textarea.md)、[Search](../harmonyos-references/ts-basic-components-search.md)、[RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)）时，如何控制软键盘的弹出和收起。

## 弹出软键盘

默认情况下，当焦点转移到输入框时，软键盘将自动弹出。

焦点转移到输入框的方法主要有：

1. 人机交互获得焦点，例如：单击、双击、长按输入框。
2. 通过代码设置焦点，例如：使用[requestFocus](../harmonyos-references/ts-universal-attributes-focus.md#requestfocus9)或[defaultFocus](../harmonyos-references/ts-universal-attributes-focus.md#defaultfocus9)方法，将焦点转移到输入框。
3. 使用外接键盘的按键走焦，例如：Tab键、Shift+Tab键、方向键，按下后可以转移焦点。外接键盘时输入框获焦，不会弹出系统软键盘，会显示物理键盘悬浮栏。

软键盘分为系统软键盘和自定义键盘。输入框的[enableKeyboardOnFocus](../harmonyos-references/ts-basic-components-textarea.md#enablekeyboardonfocus10)属性会影响系统软键盘弹出。当enableKeyboardOnFocus属性设置为false时，只有通过点击、按键走焦才能弹出系统软键盘。enableKeyboardOnFocus属性对自定义键盘的弹出无影响。外接物理键盘会阻止弹出系统软键盘，对自定义键盘无影响。

### 人机交互获得焦点

以下示例展示了单击、双击和长按输入框时，软键盘弹出效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/wvPqSKYjS8iiqzrPimPFVA/zh-cn_image_0000002583477851.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233935Z&HW-CC-Expire=86400&HW-CC-Sign=193EF29F158F400D4A33F0E0E964EA4E0311718ECEE3AE62B878E2FEE6F6CD46)

### 通过代码请求焦点

可以通过代码控制将焦点转移到输入框，包括使用[defaultFocus](../harmonyos-references/ts-universal-attributes-focus.md#defaultfocus9)和[requestFocus](../harmonyos-references/ts-universal-attributes-focus.md#requestfocus9)方法。更多细节请参见[支持焦点处理](arkts-common-events-focus-event.md)。

以下示例展示了点击按钮时，焦点转移到输入框并弹出软键盘的方法。

```
1. @Entry
2. @Component
3. struct demo {
4. controller: TextInputController = new TextInputController();
5. @State inputValue: string = "";

7. build() {
8. Column({ space: 20 }) {
9. Button('输入框请求焦点').onClick(() => {
10. this.getUIContext().getFocusController().requestFocus("textInput1")
11. })
12. TextInput({ controller: this.controller, text: this.inputValue })
13. .id("textInput1")
14. }
15. .height('100%')
16. .width('80%')
17. .margin('10%')
18. .justifyContent(FlexAlign.Center)
19. }
20. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/6eGc7P9ITW2Nsv8bGxkTsQ/zh-cn_image_0000002552798202.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233935Z&HW-CC-Expire=86400&HW-CC-Sign=E89F02816E2EA59AFE15AA4C7B5B3193332DCC6E85C1F3CB0A15CA3A018EB42A)

### 使用外接键盘的按键走焦

外接物理键盘时，按下物理键盘的Tab键、Shift+Tab键、方向键可以转移焦点。按键走焦到输入框时，显示物理键盘悬浮栏。更多细节请参见[支持焦点处理](arkts-common-events-focus-event.md#走焦规范)。

以下示例展示了外接键盘时，多次按下Tab键，焦点转移到TextInput并弹出软键盘的场景。当按下Tab键时，焦点在页面中的三个组件之间转移，可以从Text的蓝色边框或者TextInput中闪烁的光标观察到焦点转移。当TextInput获焦时，显示光标，同时显示物理键盘悬浮栏。

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. Column({ space: 20 }) {
6. Text('Text.focusable(true)')
7. .focusable(true)

9. TextInput({ placeholder: "TextInput" })

11. TextInput({ placeholder: "TextInput" })
12. }
13. .height('100%')
14. .width('80%')
15. .margin('10%')
16. .justifyContent(FlexAlign.Center)
17. }
18. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/973j3U4aSwiv-nEd0Ah46w/zh-cn_image_0000002583437897.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233935Z&HW-CC-Expire=86400&HW-CC-Sign=51577BCAC2BF03EFC3B9207F20CC4040EBB457EF7B158874F538378745F0A1FB)

## 收起软键盘

当输入框获得焦点时，软键盘会弹出；然而，当输入框失焦时，软键盘不会自动收起，而是由下一个获得焦点的组件决定是否收起软键盘。如果该组件需要使用软键盘，软键盘将继续显示；如果该组件不需要软键盘，则软键盘将被收起。通常情况下，除输入框外的其他组件不需要软键盘。

收起软键盘的常见场景如下所示，下列场景都会将焦点转移到不需要软键盘的组件上并收起软键盘。

1. 用户主动点击软键盘的关闭按钮。
2. 用户正在拖拽文本。
3. 输入框接收到了侧滑手势。
4. 页面发生切换。
5. 通过输入框的[TextInputController](../harmonyos-references/ts-basic-components-textinput.md#textinputcontroller8)退出编辑态。
6. 焦点从输入框转移到另一个不需要软键盘的组件。

### 点击软键盘的关闭按钮

软键盘自带关闭按钮，用户点击该按钮时，软键盘将被收起。

以下示例展示了用户主动点击软键盘关闭按钮的场景。

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. Column({ space: 20 }) {
6. Blank()
7. .height(350)
8. Flex({ direction: FlexDirection.Row }) {
9. TextInput({ placeholder: 'TextInput' })
10. }
11. .width(250)
12. }
13. .height('100%')
14. .width('90%')
15. .padding('5%')
16. }
17. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/2TrapQsiSSey2nLZY3qEwg/zh-cn_image_0000002552957852.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233935Z&HW-CC-Expire=86400&HW-CC-Sign=133100E95A6102E0DC2D73C015B4EAB01C72F9F3E57229F6F977DA826FE61316)

### 拖拽文本

用户主动拖拽输入框的文本，开始拖拽时，软键盘将收起。更多细节请参见[支持统一拖拽](arkts-common-events-drag-event.md)。

以下示例展示了用户主动拖拽文本时，软键盘被收起的场景。

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. Column({ space: 20 }) {
6. Blank()
7. .height(350)
8. Flex({ direction: FlexDirection.Row }) {
9. TextInput({ text: '用户主动拖拽文本' })
10. .selectAll(true)
11. .defaultFocus(true)
12. }
13. .width(250)
14. }
15. .height('100%')
16. .width('90%')
17. .padding('5%')
18. }
19. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/lKL39VEjTo2SZP2QL--o7Q/zh-cn_image_0000002583477853.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233935Z&HW-CC-Expire=86400&HW-CC-Sign=82D93A92AA19C86A2AE1F0EA46D8093B63B8BDFE8C821EB18698C0CDD607801C)

### 接收侧滑手势

下面的动图展示了“用户侧滑时软键盘收起”的场景。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/2XhK8dCnS96IZ5scpE25WA/zh-cn_image_0000002552798204.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233935Z&HW-CC-Expire=86400&HW-CC-Sign=C4921215C39E53A4DF919CB7646988995A7D8E3E6FCFEB682839E55BA181B5DB)

### 页面发生切换

以下示例展示了页面切换过程中，软键盘收起的场景。

页面跳转写法请参考[Navigation页面路由](arkts-navigation-jump.md)。

跳转前的页面

```
1. // Index.ets
2. @Entry
3. @Component
4. struct Index {
5. // 创建一个导航控制器对象并传入Navigation
6. pathStack: NavPathStack = new NavPathStack()

8. build() {
9. Navigation(this.pathStack) {
10. Column({ space: 30 }) {
11. Blank().height(150)
12. TextInput({ placeholder: 'TextInput' })
13. Button('跳转到下一个页面')
14. .onClick(() => {
15. this.pathStack.pushPath({ name: 'demo_text_1' })
16. })
17. }
18. .height('100%')
19. .width('80%')
20. .margin('10%')
21. }
22. .title('用Navigation实现页面跳转')
23. }
24. }
```

跳转后的页面

```
1. // demo_text_1.ets
2. @Builder
3. export function demo_text_1_Builder() {
4. demo_text_1()
5. }

7. @Component
8. struct demo_text_1 {
9. pathStack: NavPathStack = new NavPathStack()
10. // 跳转后的页面
11. build() {
12. NavDestination() {
13. Column({ space: 20 }) {
14. Text('跳转后的页面没有需要键盘的组件')
15. }
16. .width('100%')
17. .height('100%')
18. .justifyContent(FlexAlign.Center)
19. }
20. .onReady((context: NavDestinationContext) => {
21. this.pathStack = context.pathStack
22. })
23. }
24. }
```

系统路由表配置

在跳转目标模块的配置文件module.json5添加路由表配置

```
1. {
2. "module": {
3. // ...
4. "routerMap": "$profile:route_map",
5. // ...
6. }
7. }
```

在工程resources/base/profile中创建route\_map.json文件。添加如下配置信息。

```
1. // route_map.json
2. {
3. "routerMap": [
4. {
5. "name": "demo_text_1",
6. "pageSourceFile": "src/main/ets/pages/demo_text_1.ets",
7. "buildFunction": "demo_text_1_Builder"
8. }
9. ]
10. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/SEoDdBv8RjScZXrpzigLXA/zh-cn_image_0000002583437899.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233935Z&HW-CC-Expire=86400&HW-CC-Sign=D550737201469ECA3180B3826B8E66FD6AE6708957CF0C5F13FC0AAD2E5FDFC8)

### 通过输入框的controller退出编辑态

通过输入框的[TextInputController](../harmonyos-references/ts-basic-components-textinput.md#textinputcontroller8)调用[stopEditing](../harmonyos-references/ts-basic-components-textinput.md#stopediting10)方法后，软键盘会自动收起。

以下示例展示了如何通过[TextInputController](../harmonyos-references/ts-basic-components-textinput.md#textinputcontroller8)收起软键盘。

```
1. struct textInputControllerCloseKeyboard {
2. controller: TextInputController = new TextInputController();
3. @State inputValue: string = '';

5. build() {
6. NavDestination() {
7. Column({ space: 30 }) {
8. // 请将$r('app.string.close_keyboard')替换为实际资源文件，在本示例中该资源文件的value值为"close keyboard"
9. Button($r('app.string.close_keyboard')).onClick(() => {
10. this.controller.stopEditing()
11. })
12. TextInput({ controller: this.controller, text: this.inputValue })
13. }
14. .width('80%')
15. .height('100%')
16. .margin('10%')
17. .justifyContent(FlexAlign.Center)
18. }
19. }
20. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/SCQfkyMERsiyHZ5Xc8z99Q/zh-cn_image_0000002552957854.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233935Z&HW-CC-Expire=86400&HW-CC-Sign=BECB4E89C336AECE215FA0EB73CC354C2E6F8136630C95DAA06BA0EF16B901D3)

### 焦点转移到不需要软键盘的组件

焦点转移到不需要软键盘的组件时，软键盘会自动收起。

代码控制焦点转移的方法，包括[requestFocus](../harmonyos-references/ts-universal-attributes-focus.md#requestfocus9)、[clearFocus](../harmonyos-references/arkts-apis-uicontext-focuscontroller.md#clearfocus12)。更多细节请参见[支持焦点处理](arkts-common-events-focus-event.md)。

与通过输入框的controller退出编辑态方法相比，焦点转移到不需要软键盘的组件方法的优势在于，页面包含多个输入框时，开发者无需为每个输入框设置controller、再通过controller收起软键盘。

以下示例展示了点击按钮时，调用[requestFocus](../harmonyos-references/ts-universal-attributes-focus.md#requestfocus9)方法，焦点从输入框转移到按钮上，软键盘收起的场景。

```
1. struct requestFocusCloseKeyBoard {
2. controller: TextInputController = new TextInputController();
3. @State inputValue: string = '';

5. build() {
6. NavDestination() {
7. Column({ space: 20 }) {
8. // 请将$r('app.string.button_get_focus')替换为实际资源文件，在本示例中该资源文件的value值为"按钮获得焦点"
9. Button($r('app.string.button_get_focus')).onClick(() => {
10. this.getUIContext().getFocusController().requestFocus('button')
11. }).id('button')
12. TextInput({ controller: this.controller, text: this.inputValue })
13. }
14. .justifyContent(FlexAlign.Center)
15. .height('100%')
16. .width('80%')
17. .margin('10%')
18. }
19. }
20. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/fNiWlG57Sd2SUH-Y2R1uoQ/zh-cn_image_0000002583477855.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233935Z&HW-CC-Expire=86400&HW-CC-Sign=31E423D50C3FAFADB2267AB88533F89A8DA44965926506573F453C62F8FD4136)

以下示例展示了滚动容器在开始滚动时收起键盘的场景。[List](../harmonyos-references/ts-container-list.md)开始滚动时，调用[clearFocus](../harmonyos-references/arkts-apis-uicontext-focuscontroller.md#clearfocus12)方法清理焦点，焦点转移到页面根容器节点，页面根容器节点不需要软键盘，从而收起软键盘。

```
1. @Entry
2. @Component
3. struct Index {
4. private arr: number[] = Array.from<number, number>(
5. { length: 100 } as ArrayLike<number>,
6. (_, i: number) => i + 1
7. );

9. build() {
10. Column() {
11. List({ space: 20, initialIndex: 0 }) {
12. ForEach(this.arr, (item: number, index?: number) => {
13. ListItem() {
14. Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Center }) {
15. TextInput({ placeholder: 'TextInput ' + item })
16. }
17. }
18. }, (item: string) => item)
19. }
20. .onScrollStart(() => {
21. // List开始滚动时清理焦点，达成收起键盘的目的
22. this.getUIContext().getFocusController().clearFocus()
23. })
24. .width('80%')
25. .height('80%')
26. .margin('10%')
27. }
28. .justifyContent(FlexAlign.Center)
29. }
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/uCGJ6nOPQOuOSvIEfPRaTA/zh-cn_image_0000002552798206.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233935Z&HW-CC-Expire=86400&HW-CC-Sign=9D436EF27B8D45C915A9D6C7C780650C640AB11E255941DFE08C626A231A8A48)

## 常见问题

在软键盘的实际应用中，开发者可能会遇到一些特殊的使用场景或个性化需求。本节将针对这些常见问题提供相应的解决方案，帮助开发者更好地控制软键盘的行为。

### 获得焦点时阻止弹出软键盘

**问题现象**

如何实现点击输入框时，不弹出软键盘？

**原因分析**

默认情况下，点击输入框后，输入框获得焦点，会自动弹出系统软键盘。通过[customKeyboard](../harmonyos-references/ts-basic-components-textinput.md#customkeyboard10)设置自定义键盘之后，输入框获焦时不会弹出系统软键盘，改为弹出自定义键盘。

**解决措施**

设置自定义键盘后，系统键盘不会弹出。利用此特性，设置一个空的自定义键盘，实现“点击输入框时不显示软键盘”的效果。

示例如下，单击输入框，拉起空的自定义键盘。

```
1. @Entry
2. @Component
3. struct demo {
4. controller: TextInputController = new TextInputController();
5. @State inputValue: string = "";

7. // 自定义键盘组件
8. @Builder
9. CustomKeyboardBuilder() {
10. Column() {
11. }
12. }

14. build() {
15. Column() {
16. TextInput({ placeholder: 'TextInput', controller: this.controller, text: this.inputValue })// 绑定自定义键盘
17. .customKeyboard(this.CustomKeyboardBuilder())
18. }
19. .justifyContent(FlexAlign.Center)
20. .width('80%')
21. .margin('10%')
22. .height('100%')
23. }
24. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/mvVBHaOeSJSWfFTIwJYCFw/zh-cn_image_0000002583437901.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233935Z&HW-CC-Expire=86400&HW-CC-Sign=59DE10DB322E0361C82ECD8186ED8B6111B983BF30AE7F2110C4564F4E6820C3)

### 点击发送按钮后不收起键盘

**问题现象**

如何实现点击软键盘发送按钮之后，软键盘不收起？

**原因分析**

软键盘的[enterKeyType](../harmonyos-references/ts-basic-components-textarea.md#enterkeytype11)可以设置输入法回车键类型，包括发送样式。按下发送按钮实际上是按下回车键，非TV设备按下回车键时，输入框默认会失焦并且收起键盘。

**解决措施**

软键盘的[enterKeyType](../harmonyos-references/ts-basic-components-textarea.md#enterkeytype11)可以设置输入法回车键类型。除EnterKeyType.NEW\_LINE外，enterKeyType设置其他的枚举值时，按下软键盘输入法回车键都会触发[onSubmit](../harmonyos-references/ts-basic-components-textarea.md#onsubmit14)事件。可以在TextArea的onSubmit回调中，通过调用[keepEditableState](../harmonyos-references/ts-basic-components-textinput.md#keepeditablestate11)接口保持输入框编辑态，使得点击回车键后不收起键盘。

示例如下，软键盘的回车键显示为发送样式。按下发送之后，键盘不会收起。

```
1. @Entry
2. @Component
3. struct demo {
4. build() {
5. Column({ space: 20 }) {
6. TextArea({ placeholder: '点击发送收起键盘' })
7. .enterKeyType(EnterKeyType.Send)

9. TextArea({ placeholder: 'onSubmit中设置keepEditableState，点击发送不收起键盘' })
10. .enterKeyType(EnterKeyType.Send)
11. .onSubmit((enterKey: EnterKeyType, event: SubmitEvent) => {
12. // 调用keepEditableState方法，输入框保持编辑态
13. event.keepEditableState();
14. })
15. }
16. .justifyContent(FlexAlign.Center)
17. .height('100%')
18. .width('80%')
19. .margin('10%')
20. }
21. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/i4yZyXtxT6uH11NWpC-Daw/zh-cn_image_0000002552957856.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233935Z&HW-CC-Expire=86400&HW-CC-Sign=A80661E333BF9219BE6BE6D3A831FE8207983ED424F14C8AF802792CD800EB18)
