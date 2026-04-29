---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-manage-keyboard
title: 管理软键盘
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用文本 > 管理软键盘
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f75f46f0448bb296a6fbfdf13560a8ad2b073dfa3488e2e879afc4d6c86d4447
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/W0X5wXy7Ryq_FJL_RVfabA/zh-cn_image_0000002589244149.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052745Z&HW-CC-Expire=86400&HW-CC-Sign=7CEE195F19102A2134CDD31A0B2FD8BC6A77023D4A60DE4DA4ABAA423C075765)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/rwkUJr91Qr2zpQVv8Xlfug/zh-cn_image_0000002558764342.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052745Z&HW-CC-Expire=86400&HW-CC-Sign=2AB634B52199093CBFD70D6EB2502DE94EC513CE4DF71D05A056D4FCEFB9FA1E)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/NS8slKqKRUaYul-gcBipZQ/zh-cn_image_0000002558604686.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052745Z&HW-CC-Expire=86400&HW-CC-Sign=7A06D608C74143D2A304F1ADA57EE412397C29C5471E435439DABAF680018D65)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/8M4cMkqcRDaO3zUvKwVaeA/zh-cn_image_0000002589324211.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052745Z&HW-CC-Expire=86400&HW-CC-Sign=BE2AD5012702C048A386D9F0EF56B410351037A5F58433DC55E7A15005FEF43B)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/F-rXNLtmRkW23Oyr1lImaw/zh-cn_image_0000002589244151.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052745Z&HW-CC-Expire=86400&HW-CC-Sign=0609ACEDDE03FC8CA795479BFDF9D96F9C49493F1AA55BBCC1659982F76F7E5F)

### 接收侧滑手势

下面的动图展示了“用户侧滑时软键盘收起”的场景。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/EnVw1GpySd6UNud_dYoYYw/zh-cn_image_0000002558764344.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052745Z&HW-CC-Expire=86400&HW-CC-Sign=2E1608AFA464D028A82E39EC21C49F51545F2A13BD046C2D199BD3F3736D02DC)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/VIa_Wp9sT26adhcEVRxSrg/zh-cn_image_0000002558604688.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052745Z&HW-CC-Expire=86400&HW-CC-Sign=EEBC9DF273B489CEF6D595990ACE50029DD5CE3DF1A16E19B42EE8BD3BADBD47)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/qVNjvRrCSNSkq5GijSQbIA/zh-cn_image_0000002589324213.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052745Z&HW-CC-Expire=86400&HW-CC-Sign=A4C820A0E176E280F678AC6F389F40F5DBE1DD28D2BF5709FF5DA8B05574B45C)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/5ZglLD7JTBa7x9fh8sr4kg/zh-cn_image_0000002589244153.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052745Z&HW-CC-Expire=86400&HW-CC-Sign=5F8FEDA57128DD02A00296A5657CA598138F5B3F945A441A7C5F534F5916886A)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/bt1MX6ypSYiI5c2KnNsjdA/zh-cn_image_0000002558764346.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052745Z&HW-CC-Expire=86400&HW-CC-Sign=B6D03272C98B25D90AD064F10C1538C2B14FFBD02984704D50889CF36D04AAD0)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/yg_khP3MQ-WtTsWlWYaq7A/zh-cn_image_0000002558604690.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052745Z&HW-CC-Expire=86400&HW-CC-Sign=7169B486B607ED8CB25935B877B16DEC31923D8130CBFA29FBB162CBCEA239C5)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/RUth11S9Qm-jhwJWeNUpNw/zh-cn_image_0000002589324215.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052745Z&HW-CC-Expire=86400&HW-CC-Sign=47DD6E306329D10DAE3EC93C015293DF8072F2BBB6E65634F6FCE63F01306F45)
