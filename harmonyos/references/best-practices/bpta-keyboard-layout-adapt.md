---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-keyboard-layout-adapt
title: 软键盘布局适配
breadcrumb: 最佳实践 > 应用框架 > 输入法 > 软键盘布局适配
category: best-practices
scraped_at: 2026-04-29T14:11:02+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:87e38d626d02efa444d497617824bbeb017cf2f25ef0f05e4656996cfba17c58
---

## 概述

软键盘是用户进行交互的重要途径之一，同时软键盘的弹出和收起，可能会影响到正在显示的UI元素，影响用户体验，出现如下常见的软键盘布局适配问题：

* 重要信息被软键盘遮挡：当软键盘弹出时，输入框或其它重要UI元素可能会被键盘遮挡，导致用户无法看到或访问它们。
* 软键盘弹出导致布局错位：内容可能会不恰当上移，影响用户体验。
* 软键盘弹出导致弹窗过度上抬：弹窗被键盘上顶，造成不好的体验。

本文将介绍以下知识帮助开发者了解软键盘的弹出和收起的控制、避让机制以及软键盘常见问题的解决方法。

## 软键盘的弹出收起和监听

用户点击输入框时，软键盘默认弹出。但在特定场景下，需要对软键盘的弹出和收起进行控制，如点击空白区域收起软键盘，进入页面时输入框主动获焦。开发者还需根据软键盘状态和高度调整页面布局。

### 主动获焦弹出软键盘

有时候进入页面，希望页面中的输入框能主动获焦并且弹出软键盘，方便用户直接输入，例如，点击应用首页的搜索框，进入应用搜索页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/YEd5SU0WRtuef3ZdOS8-oA/zh-cn_image_0000002345807137.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061100Z&HW-CC-Expire=86400&HW-CC-Sign=D4187EEC97E5574E28178690BD1A78C6A4129A086168740BCC8CE5DDD35FE4F0 "点击放大")

可以通过将输入框的defaultFocus设置为true来实现。

```
1. TextInput()
2. .defaultFocus(true)
```

[ExamplePage.ets](https://gitcode.com/harmonyos_samples/keyboard/blob/master/entry/src/main/ets/pages/ExamplePage.ets#L31-L32)

### 代码控制弹出软键盘

开发者可以使用FocusController的[requestFocus()](../harmonyos-references/arkts-apis-uicontext-focuscontroller.md#requestfocus12)方法，通过组件的id将焦点转移到组件树对应的实体节点，并且弹出软键盘。例如，表情面板切换到文本输入时，点击表情图标拉起系统软键盘，便于用户直接输入。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/dztQmQYrQMuHWazoRNoVUA/zh-cn_image_0000002349352709.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061100Z&HW-CC-Expire=86400&HW-CC-Sign=55D4F31FD71EA5631AE57C8F5E2E87DB70B8F656A35FC03EA42F10E19F3C7EA0 "点击放大")

示例如下：

```
1. TextInput({ placeholder: 'Please enter a contact name' })
2. .id('input1')

4. Button('login')
5. .onClick(() => {
6. this.getUIContext().getFocusController().requestFocus('input1');
7. })
```

[ExamplePage.ets](https://gitcode.com/harmonyos_samples/keyboard/blob/master/entry/src/main/ets/pages/ExamplePage.ets#L35-L41)

注意

使用requestFocus需要保证TextInput组件已经挂载完成，应避免在组件未创建的情况下使用。

### 代码控制收起软键盘

通过全局的焦点控制对象FocusController的[clearFocus](../harmonyos-references/arkts-apis-uicontext-focuscontroller.md#clearfocus12)方法，软键盘收起，例如在下面的搜索页面中，点击搜索按钮时软键盘收起。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/BT60at9LQ0CZIK2FQcXeBg/zh-cn_image_0000002315512768.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061100Z&HW-CC-Expire=86400&HW-CC-Sign=5D2D148F241537A364BEDB41DF77E5B03A597EF2460C6D4CEF765E4D653F9492 "点击放大")

示例代码如下：

```
1. Button('Search')
2. .onClick(() => {
3. this.getUIContext().getFocusController().clearFocus();
4. })
```

[ExamplePage.ets](https://gitcode.com/harmonyos_samples/keyboard/blob/master/entry/src/main/ets/pages/ExamplePage.ets#L44-L47)

此外，开发者可调用[stopEditing()](../harmonyos-references/ts-basic-components-textinput.md#stopediting10)方法来关闭键盘，该方法需为输入框单独绑定一个TextInputController对象。在存在多个输入框的场景下，需要绑定多个TextInputController对象，使用起来较为繁琐，推荐改用clearFocus()方法来解除焦点。

```
1. @Component
2. struct StopEditingCpt {
3. private controller: TextInputController = new TextInputController();

5. build() {
6. Column() {
7. TextInput({ placeholder: 'Input', controller: this.controller })

9. Button('Search')
10. .onClick(() => {
11. this.controller.stopEditing();
12. })
13. }
14. }
15. }
```

[ExamplePage.ets](https://gitcode.com/harmonyos_samples/keyboard/blob/master/entry/src/main/ets/pages/ExamplePage.ets#L65-L79)

### 监听获取软键盘高度

开发者可以通过获取软键盘高度、监听软键盘的弹出和收起状态，调整组件位置以适配界面或显示隐藏某些组件。通过[window](../harmonyos-references/js-apis-window.md)模块的[on('keyboardHeightChange')](../harmonyos-references/arkts-apis-window-window.md#onkeyboardheightchange7)方法开启软键盘高度变化的监听，实时获取软键盘高度。例如下面这个示例软键盘弹起后显示表情栏，软键盘收起后隐藏表情栏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/zojzLEneR52miMJeeAoBbQ/zh-cn_image_0000002312007956.png?HW-CC-KV=V1&HW-CC-Date=20260429T061100Z&HW-CC-Expire=86400&HW-CC-Sign=2B72BC67994ED48A56D0D252098808EE32AAADF6CB87879F6BCE22945C66E213 "点击放大")

上面效果图的实现示例代码如下，通过[on('keyboardHeightChange')](../harmonyos-references/arkts-apis-window-window.md#onkeyboardheightchange7)方法实时获取软键盘高度（返回值为整数，单位为px），并赋值给变量keyboardHeight。当keyboardHeight为0的时候表示软键盘处于收起状态，此时隐藏表情栏；keyboardHeight不为0的时候表示软键盘处于弹出状态，此时显示表情栏。

```
1. import { window } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. @Entry
6. @Component
7. struct GetKeyboardHeightDemo {
8. @State keyboardHeight: number = 0; // Soft keyboard height

10. aboutToAppear(): void {
11. try {
12. window.getLastWindow(this.getUIContext().getHostContext()).then(currentWindow => {
13. currentWindow.on('keyboardHeightChange', (data: number) => {
14. this.keyboardHeight = this.getUIContext().px2vp(data);
15. })
16. })
17. } catch (error) {
18. let err = error as BusinessError;
19. hilog.error(0x0000, 'GetKeyboardHeightDemo',
20. `getLastWindow failed, error code=${err.code}, message=${err.message}`);
21. }
22. }

24. build() {
25. Column() {
26. // ...
27. TextInput()

29. if (this.keyboardHeight > 0) {
30. Row() { // Emoji
31. // ...
32. }

34. // ...
35. }
36. }
37. }
38. }
```

[GetKeyboardHeightDemo.ets](https://gitcode.com/harmonyos_samples/keyboard/blob/master/entry/src/main/ets/pages/GetKeyboardHeightDemo.ets#L17-L68)

### 监听获取安全区域高度

通过[window](../harmonyos-references/arkts-apis-window.md)模块的[on('avoidAreaChange')](../harmonyos-references/arkts-apis-window-window.md#onavoidareachange9)方法开启当前窗口系统规避区变化的监听，获取内容可视区域大小，同时也可以监听软键盘的弹出收起。根据软键盘弹出后的可视区域大小，动态调整布局中组件的高度以适配界面。具体运用可以参考[软键盘避让常见问题](bpta-keyboard-layout-adapt.md#section085404710246)中**通过监听软键盘弹出，实现软键盘避让**示例。

```
1. import { KeyboardAvoidMode, window } from '@kit.ArkUI';
2. import { UIAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

6. @Entry
7. @Component
8. struct GetSafeAreaHeightDemo {
9. @State screenHeight: number = 0; // The height of the safe area
10. @State isKeyBoardHidden: boolean = false; // Whether the soft keyboard is hidden

12. aboutToAppear(): void {
13. try {
14. window.getLastWindow(this.getUIContext().getHostContext()).then(currentWindow => {
15. let property = currentWindow.getWindowProperties();
16. let avoidArea = currentWindow.getWindowAvoidArea(window.AvoidAreaType.TYPE_KEYBOARD);
17. // Initialize the display area height
18. this.screenHeight = this.getUIContext()
19. .px2vp(property.windowRect.height - avoidArea.topRect.height - avoidArea.bottomRect.height);
20. // Enables the monitoring of changes in the avoidance zone of the current window
21. currentWindow.on('avoidAreaChange', data => {
22. if (data.type !== window.AvoidAreaType.TYPE_KEYBOARD) {
23. return;
24. }
25. if (data.area.bottomRect.height <= 0) {
26. this.isKeyBoardHidden = true;
27. } else {
28. this.isKeyBoardHidden = false;
29. }
30. this.screenHeight = this.getUIContext()
31. .px2vp(property.windowRect.height - data.area.topRect.height - data.area.bottomRect.height);
32. hilog.info(0x0000, 'GetSafeAreaHeightDemo', `screen height is: ${this.screenHeight}`);
33. })
34. })
35. } catch (error) {
36. let err = error as BusinessError;
37. hilog.error(0x0000, 'GetSafeAreaHeightDemo',
38. `getLastWindow failed, error code=${err.code}, message=${err.message}`);
39. }
40. }

42. build() {
43. Column() {
44. TextInput()
45. }
46. }
47. }
```

[GetSafeAreaHeightDemo.ets](https://gitcode.com/harmonyos_samples/keyboard/blob/master/entry/src/main/ets/pages/GetSafeAreaHeightDemo.ets#L17-L64)

## 软键盘避让机制

解决软键盘的界面适配问题，首先需要了解在HarmonyOS系统中软键盘的避让机制是怎么样的。

### 软键盘默认避让效果

为了确保输入框不被软键盘挡住，系统默认提供了输入框避让软键盘的能力，结合下面这个输入框列表，介绍软键盘避让的主要表现形式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/av9-wptgTgac0wyoKyba0A/zh-cn_image_0000002345807161.png?HW-CC-KV=V1&HW-CC-Date=20260429T061100Z&HW-CC-Expire=86400&HW-CC-Sign=A0057606D1F3BA2E46496B4C3FC12317EFD52D8A2BE40102358CE5213EFE22D9 "点击放大")

默认情况下，系统针对输入框位置，执行安全避让策略，保证输入框不会被软键盘遮挡：

* 如果当前输入框不会被软键盘遮挡，则不上抬组件，如图所示点击输入框1，组件不会上抬。
* 当前输入框会被软键盘遮挡，则上抬组件至刚好在软键盘上方显示完整的输入框，输入框上方的组件会跟着抬起，下方的组件不会露出。

**表1** 默认避让规格

| 描述 | * 如果当前输入框不会被软键盘遮挡，则不上抬组件，如图所示点击输入框1，组件不会上抬。 | 如果当前输入框会被软键盘遮挡，则上抬组件至刚好在软键盘上方显示完整的输入框，输入框上方的组件会跟着抬起，下方的组件不会露出，可以看到输入框11下方的输入框12不会露出。 |
| --- | --- | --- |
| **效果图** |  |  |

**弹窗内输入框避让规则**

弹窗避让可以通过BaseDialogOptions，设置弹窗的避让模式KeyboardAvoidMode，当设置为默认避让Default模式时，如果软键盘弹出会覆盖输入框，弹窗整体会上抬，并且为了UX美观，会存在默认的间隔，默认大小为16vp。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/JtEjuP2AReyxrP5A4BDJ0w/zh-cn_image_0000002312007964.png?HW-CC-KV=V1&HW-CC-Date=20260429T061100Z&HW-CC-Expire=86400&HW-CC-Sign=F931CB50838CC6C7E020EBF1E4A05821B1D36D565DC4FF8BDF8300FE5E79D38B "点击放大")

系统默认的软键盘避让形式仅能确保输入框不被遮挡，但输入框下方的组件可能会被软键盘遮挡。要解决此问题，需要了解软键盘的避让模式。

### 软键盘避让模式

当用户在输入时，为了确保输入框不会被键盘遮挡，系统提供了避让模式来解决这一问题。开发者可以通过[setKeyboardAvoidMode](../harmonyos-references/ts-universal-attributes-expand-safe-area.md#setkeyboardavoidmode11)控制虚拟键盘抬起时页面的避让模式，键盘抬起时默认页面避让模式为上抬模式，下面列举了几种常见的避让模式。

* 上抬模式（KeyboardAvoidMode.OFFSET）：为了避让软键盘，Page内容会整体上抬。如下示例代码，软键盘弹出时，页面整体上抬：

  ```
  1. import { KeyboardAvoidMode, window } from '@kit.ArkUI';
  2. import { UIAbility } from '@kit.AbilityKit';

  4. export default class EntryAbility extends UIAbility {
  5. onWindowStageCreate(windowStage: window.WindowStage): void {
  6. windowStage.loadContent('pages/GetSafeAreaHeightDemo', (err) => {
  7. // Lift up mode
  8. windowStage.getMainWindowSync().getUIContext().setKeyboardAvoidMode(KeyboardAvoidMode.OFFSET);
  9. });
  10. }
  11. }
  ```

  [GetSafeAreaHeightDemoMode.ets](https://gitcode.com/harmonyos_samples/keyboard/blob/master/entry/src/main/ets/pages/GetSafeAreaHeightDemoMode.ets#L17-L28)

  示意效果如下，上抬整个页面实现软键盘避让：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/-jU0YugRSBKFypTWVpTw_g/zh-cn_image_0000002345807165.png?HW-CC-KV=V1&HW-CC-Date=20260429T061100Z&HW-CC-Expire=86400&HW-CC-Sign=53DC4A1AF1A5BEE60E75BC1C903A9EBB320A4366B4A6F7F5E2A7921C37FE9BA0 "点击放大")
* 压缩模式（KeyboardAvoidMode.RESIZE）：当软键盘高度改变时，调整Page大小。Page下设置百分比宽高的组件会跟随压缩，直接设置宽高的组件保持固定大小。设置KeyboardAvoidMode.RESIZE时，expandSafeArea([SafeAreaType.KEYBOARD],[SafeAreaEdge.BOTTOM])不生效。

  ```
  1. export default class EntryAbility extends UIAbility {
  2. onWindowStageCreate(windowStage: window.WindowStage): void {
  3. windowStage.loadContent('pages/GetSafeAreaHeightDemo', (err) => {
  4. // Compression mode
  5. windowStage.getMainWindowSync().getUIContext().setKeyboardAvoidMode(KeyboardAvoidMode.RESIZE);
  6. });
  7. }
  8. }
  ```

  [ExamplePage.ets](https://gitcode.com/harmonyos_samples/keyboard/blob/master/entry/src/main/ets/pages/ExamplePage.ets#L54-L61)

  示意效果如下，通过压缩内容区域高度实现软键盘避让：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/ddILJ9dsTcGHI_pxnLo0Dw/zh-cn_image_0000002311848196.png?HW-CC-KV=V1&HW-CC-Date=20260429T061100Z&HW-CC-Expire=86400&HW-CC-Sign=9426E2C74CDAB1818ECB0AB96E14006BB6200C39CE138001857525C0FF9CC8A4 "点击放大")
* 不避让模式（KeyboardAvoidMode.NONE）：软键盘将直接覆盖页面UI，不会触发界面布局调整。例如在全屏沉浸式场景（游戏/视频播放器等），为保障用户体验的完整性，开发者可以使用KeyboardAvoidMode.NONE模式。

  ```
  1. aboutToAppear(): void {
  2. this.getUIContext().setKeyboardAvoidMode(KeyboardAvoidMode.NONE);
  3. }
  ```

  [ExamplePage.ets](https://gitcode.com/harmonyos_samples/keyboard/blob/master/entry/src/main/ets/pages/ExamplePage.ets#L23-L25)

**光标避让**

上抬模式和压缩模式还包括KeyboardAvoidMode.OFFSET\_WITH\_CARET和KeyboardAvoidMode.RESIZE\_WITH\_CARET两种。当输入框的光标位置发生变化时，系统会自动触发相应的界面避让行为，确保光标始终处于可视区域内，具体可以参考[光标避让](../harmonyos-guides/arkts-common-components-text-input.md#光标避让)。

**弹窗类组件避让模式**

弹窗类组件（如Dialog、Popup、Menu、BindSheet等）避让模式有KeyboardAvoidMode.DEFAULT（避让）和KeyboardAvoidMode**.**NONE（不避让）两种，通过[BaseDialogOptions](../harmonyos-references/js-apis-promptaction.md#basedialogoptions11)中的keyboardAvoidMode属性，灵活控制是否避让软键盘。

若未指定弹窗避让模式，则其避让行为受页面避让模式影响。例如当通过setKeyboardAvoidMode()方法设置页面避让模式为KeyboardAvoidMode**.**NONE时，则弹窗也不会避让软键盘。

```
1. this.getUIContext().getPromptAction().openCustomDialog({
2. builder: () => {
3. this.customDialogBuilder();
4. },
5. alignment: DialogAlignment.Bottom,
6. width: '100%',
7. // Set not avoid keyboard
8. keyboardAvoidMode: KeyboardAvoidMode.NONE,
9. });
```

[CustomDialogAvoid.ets](https://gitcode.com/harmonyos_samples/keyboard/blob/master/entry/src/main/ets/pages/CustomDialogAvoid.ets#L46-L54)

### 设置组件不避让软键盘

前面介绍了避让模式，组件会为了避让软键盘而移动。有时希望组件不避让软键盘，例如在上抬模式下，希望顶部标题栏不移动。这种需求如何实现？这就需要了解[安全区域](../harmonyos-references/ts-universal-attributes-expand-safe-area.md)和[expandSafeArea](../harmonyos-references/ts-universal-attributes-expand-safe-area.md#expandsafearea)属性了。

通过[expandSafeArea](../harmonyos-references/ts-universal-attributes-expand-safe-area.md#expandsafearea)属性支持组件不改变布局情况下扩展其绘制区域至安全区外，当设置expandSafeArea属性type为SafeAreaType.KEYBOARD的时候，即expandSafeArea([SafeAreaType.KEYBOARD])，系统会将软键盘区域视作安全区，从而不会避让软键盘。如果开发者希望某些组件不避让软键盘，可以给组件设置expandSafeArea属性。组件避让软键盘的示例效果如下，软键盘弹出时页面整体上抬，自定义标题栏固定不动，具体实现可以参考[软键盘弹出导致布局错位](bpta-keyboard-layout-adapt.md#section20196428133211)的示例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/Nkw-9P4fRsCUsGmHeNLOAA/zh-cn_image_0000002345926957.png?HW-CC-KV=V1&HW-CC-Date=20260429T061100Z&HW-CC-Expire=86400&HW-CC-Sign=243C91FF53BBF257F31BE36DEDC0E9084BC76062CC919A9602F5D832EC81AD91 "点击放大")

## 软键盘避让常见问题

下面列举常见的软键盘适配问题，帮助开发者了解软键盘的适配方法。

### 重要信息被软键盘遮挡

例如下面这个电子邮件示例，内容包括标题栏、内容区域和底部操作栏。点击输入内容的输入框时，软键盘会遮挡底部操作栏，影响用户体验。具体如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/2SXNyTEbQFuoFEwga8cLsQ/zh-cn_image_0000002312007968.png?HW-CC-KV=V1&HW-CC-Date=20260429T061100Z&HW-CC-Expire=86400&HW-CC-Sign=4FE102A5A8E018EF203D75E14B503E3BCD59E3E91499754D14FD47349C124397 "点击放大")

对应的示例代码如下，其中标题栏和底部操作栏都是固定的高度56，内容区域高度是非固定高度layoutWeight(1)，自适应高度。

```
1. @Component
2. export struct MailPage {
3. // ...

5. build() {
6. Column() {
7. this.NavigationTitle()
8. this.EmailContent()
9. this.BottomToolbar()
10. }
11. // ...
12. }

14. @Builder
15. NavigationTitle() {
16. Row() {
17. // ...
18. }
19. .width('100%')
20. .height("56vp")
21. // ...
22. }

24. @Builder
25. BottomToolbar() {
26. Row({ space: 12 }) {
27. // ...
28. }
29. .width('100%')
30. .height("56vp")
31. // ...
32. }

34. @Builder
35. EmailContent() {
36. Column() {
37. // ...
38. }
39. .width('100%')
40. .layoutWeight(1)
41. // ...
42. }
43. }
```

[MailPage.ets](https://gitcode.com/harmonyos_samples/keyboard/blob/master/entry/src/main/ets/pages/MailPage.ets#L20-L178)

开发者可以通过设置软键盘的避让模式为KeyboardAvoidMode.RESIZE（压缩模式），来解决底部操作栏被遮挡的问题，设置该属性后，软键盘的避让会通过压缩内容区域的高度来实现。示例代码如下：

```
1. aboutToAppear(): void {
2. this.getUIContext().setKeyboardAvoidMode(KeyboardAvoidMode.RESIZE);
3. }

5. aboutToDisappear(): void {
6. this.getUIContext().setKeyboardAvoidMode(KeyboardAvoidMode.OFFSET);
7. }
```

[MailPage.ets](https://gitcode.com/harmonyos_samples/keyboard/blob/master/entry/src/main/ets/pages/MailPage.ets#L24-L30)

需要注意的是内容区域高度的设置需要用百分比的方式实现，效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/L_RyI7j8Qt64rBmgNo6eTg/zh-cn_image_0000002345807169.png?HW-CC-KV=V1&HW-CC-Date=20260429T061100Z&HW-CC-Expire=86400&HW-CC-Sign=EEACD75CBD324EB022FF4E9B99951E096757B1701426BDDC26A543330DA926CB "点击放大")

**通过监听软键盘弹出，实现软键盘避让**

上面这个示例开发者还可以通过window模块的[getWindowAvoidArea](../harmonyos-references/arkts-apis-window-window.md#getwindowavoidarea9)方法，监听获取软键盘弹出，获取安全显示区域高度动态设置页面高度。示例代码如下：

```
1. import { CommonConstants as Const } from '../common/constants/CommonConstants';
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

6. @Entry
7. @Component
8. struct MailHomePage2 {
9. @State message: string = 'Hello World';
10. @State screenHeight: number = 0;
11. @State isKeyBoardHidden: boolean = false;

13. aboutToAppear(): void {
14. try {
15. window.getLastWindow(this.getUIContext().getHostContext()).then(currentWindow => {
16. let property = currentWindow.getWindowProperties();
17. let avoidArea = currentWindow.getWindowAvoidArea(window.AvoidAreaType.TYPE_SYSTEM);
18. // Initialize the display area height
19. this.screenHeight = this.getUIContext().px2vp(property.windowRect.height - avoidArea.topRect.height - avoidArea.bottomRect.height);
20. // Monitor the ejection and retraction of the soft keyboard
21. currentWindow.on('avoidAreaChange', async data => {
22. if (data.type !== window.AvoidAreaType.TYPE_KEYBOARD) {
23. return;
24. }
25. if (data.area.bottomRect.height <= 0) {
26. this.isKeyBoardHidden = true;
27. } else {
28. this.isKeyBoardHidden = false;
29. }
30. this.screenHeight = this.getUIContext().px2vp(property.windowRect.height - avoidArea.topRect.height - data.area.bottomRect.height);
31. })
32. })
33. } catch (error) {
34. let err = error as BusinessError;
35. hilog.error(0x0000, 'MailHomePage2', `getLastWindow failed, error code=${err.code}, message=${err.message}`);
36. }
37. }

39. build() {
40. Column() {
41. this.NavigationTitle()
42. this.EmailContent()
43. this.BottomToolbar()
44. }
45. .width('100%')
46. .height(this.screenHeight) // Dynamically sets the viewport height
47. .expandSafeArea([SafeAreaType.KEYBOARD])
48. .backgroundColor('#F1F3F5')
49. }
50. // ...
51. }
```

[MailHomePage2.ets](https://gitcode.com/harmonyos_samples/keyboard/blob/master/entry/src/main/ets/pages/MailHomePage2.ets#L17-L186)

当系统的避让机制无法满足开发者需求时，开发者可以监听软键盘弹出，根据获取的安全区域或软键盘高度，调整布局大小和位置以避让软键盘。

### 软键盘弹出导致布局错位

**内容向上滚动避让，顶部固定**

例如下面这样的一个聊天界面，顶部是一个自定义的标题，下方为可滚动聊天消息区域，底部是消息输入框，示例代码如下：

```
1. @Entry
2. @Component
3. export struct ContactPage {
4. // ...

6. build() {
7. Row() {
8. Column() {
9. Row() {
10. // ...
11. }
12. // ...
13. .height('12%')
14. // ...
15. .expandSafeArea([SafeAreaType.KEYBOARD])
16. .zIndex(1)
17. // ...

19. List() {
20. // ...
21. }
22. .height('76%')
23. // ...

25. Column() {
26. // ...
27. }
28. .height('12%')
29. // ...
30. }
31. .width('100%')
32. // ...
33. }
34. .height('100%')
35. }
36. }
```

[ContactPage.ets](https://gitcode.com/harmonyos_samples/keyboard/blob/master/entry/src/main/ets/pages/ContactPage.ets#L20-L201)

由于软键盘避让默认为上抬模式，会将整个页面向上抬起，因此标题也会被顶上去，如图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/kzgh3OwDQai6DlrKzmpEFg/zh-cn_image_0000002311848204.png?HW-CC-KV=V1&HW-CC-Date=20260429T061100Z&HW-CC-Expire=86400&HW-CC-Sign=02134F040808A559DF4E838344A6EC2D27CC84CB2795E2C6F1937E3D737D236A "点击放大")

现在需求是希望顶部标题固定，点击底部输入框软键盘弹起的时候，标题不上抬，只有内容区域上抬。效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/MSrNcd2lRTWZ_QicdaILFg/zh-cn_image_0000002345926969.png?HW-CC-KV=V1&HW-CC-Date=20260429T061100Z&HW-CC-Expire=86400&HW-CC-Sign=12E17B06D5B3D0E38EE311C7D89B4359370AC19772E44E01F7776D5ABB98B893 "点击放大")

想要顶部标题不被软键盘向上抬，需要给对应的组件设置 .expandSafeArea([SafeAreaType.KEYBOARD])属性，使标题组件不避让键盘，示例代码如下：

```
1. @Entry
2. @Component
3. export struct ContactPage {
4. // ...

6. build() {
7. Row() {
8. Column() {
9. Row() {
10. // ...
11. }
12. // ...
13. .height('12%')
14. // ...
15. .expandSafeArea([SafeAreaType.KEYBOARD])
16. .zIndex(1)
17. // ...

19. List() {
20. // ...
21. }
22. .height('76%')
23. // ...

25. Column() {
26. // ...
27. }
28. .height('12%')
29. // ...
30. }
31. .width('100%')
32. // ...
33. }
34. .height('100%')
35. }
36. }
```

[ContactPage.ets](https://gitcode.com/harmonyos_samples/keyboard/blob/master/entry/src/main/ets/pages/ContactPage.ets#L20-L201)

具体实现可以参考Sample代码[Keyboard](https://gitcode.com/harmonyos_samples/keyboard)。

### 软键盘弹出导致弹窗过度上抬

**自定义弹窗被键盘顶起** **，影响用户体验**

在软键盘系统避让机制中介绍过，弹窗为避让软键盘会整体向上抬，这样可能会影响用户体验。比如下面这个评论列表的弹窗，使用@CustomDialog实现的，示例代码如下：

```
1. @CustomDialog
2. struct CommentDialog {
3. listData: string[] = ['comments1', 'comments2', 'comments3', 'comments4', 'comments5', 'comments6', 'comments7', 'comments8'];
4. controller?: CustomDialogController;

7. build() {
8. Column() {
9. Text('comments')
10. .fontSize(20)
11. .fontWeight(FontWeight.Medium)

14. List() {
15. ForEach(this.listData, (item: string) => {
16. ListItem() {
17. Text(item)
18. .height(80)
19. .fontSize(20)
20. }
21. }, (item: string) => item)
22. }
23. .scrollBar(BarState.Off)
24. .width('100%')
25. .layoutWeight(1)

28. TextInput({ placeholder: 'Please input content' })
29. .height(40)
30. .width('100%')
31. }
32. .padding(12)
33. }
34. }

37. @Entry
38. @Component
39. struct CustomDialogDemo {
40. dialogController: CustomDialogController | null = new CustomDialogController({
41. builder: CommentDialog(),
42. alignment: DialogAlignment.Bottom,
43. cornerRadius: 0,
44. width: '100%',
45. height: '80%'
46. })

49. build() {
50. Column() {
51. Button('click me')
52. .onClick(() => {
53. if (this.dialogController !== null) {
54. this.dialogController.open();
55. }
56. })
57. }
58. .height('100%')
59. .width('100%')
60. .justifyContent(FlexAlign.Center)
61. }
62. }
```

[CommentDialog.ets](https://gitcode.com/harmonyos_samples/keyboard/blob/master/entry/src/main/ets/view/dialog/CommentDialog.ets#L2-L63)

当用户点击弹窗底部的输入框的时候，弹窗会整体上抬，输入框上抬的距离也过多。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/QzILrWvVQsuFXCuqjeRMJw/zh-cn_image_0000002312007980.png?HW-CC-KV=V1&HW-CC-Date=20260429T061100Z&HW-CC-Expire=86400&HW-CC-Sign=22C80626917303D7D6029C3AA7A42AC56413AED78CED21BAFA2F95526BC5E9E9 "点击放大")

为了解决以上问题，可以使用[Navigation.Dialog](../harmonyos-guides/arkts-navigation-navigation.md#页面显示类型)，通过设置NavDestination的mode为NavDestinationMode.DIALOG弹窗类型，此时整个NavDestination默认透明显示，示例代码如下：

```
1. @Entry
2. @Component
3. struct NavDestinationModeDemo {
4. @Provide('NavPathStack') pageStack: NavPathStack = new NavPathStack()

6. @Builder
7. PagesMap(name: string) {
8. if (name === 'DialogPage') {
9. DialogPage()
10. }
11. }

13. build() {
14. Navigation(this.pageStack) {
15. Column() {
16. Button('click me')
17. .onClick(() => {
18. this.pageStack.pushPathByName('DialogPage', '');
19. })
20. }
21. .height('100%')
22. .width('100%')
23. .justifyContent(FlexAlign.Center)
24. }
25. .mode(NavigationMode.Stack)
26. .navDestination(this.PagesMap)
27. }
28. }

30. @Component
31. export struct DialogPage {
32. @Consume('NavPathStack') pageStack: NavPathStack;
33. listData: string[] = ['评论1', '评论2', '评论3', '评论4', '评论5', '评论6', '评论7', '评论8'];

35. build() {
36. NavDestination() {
37. Stack({ alignContent: Alignment.Bottom }) {
38. Column() {
39. Text('评论')
40. .fontSize(20)
41. .fontWeight(FontWeight.Medium)

43. List() {
44. ForEach(this.listData, (item: string) => {
45. ListItem() {
46. Text(item)
47. .height(80)
48. .fontSize(20)
49. }
50. }, (item: string) => item)
51. }
52. .scrollBar(BarState.Off)
53. .width('100%')
54. .layoutWeight(1)

56. TextInput({ placeholder: 'Please input content' })
57. .height(40)
58. .width('100%')
59. }
60. .backgroundColor(Color.White)
61. .height('75%')
62. .width('100%')
63. .padding(12)
64. }
65. .height('100%')
66. .width('100%')
67. }
68. .backgroundColor('rgba(0,0,0,0.2)')
69. .hideTitleBar(true)
70. .mode(NavDestinationMode.DIALOG)
71. }
72. }
```

[NavDestinationModeDemo.ets](https://gitcode.com/harmonyos_samples/keyboard/blob/master/entry/src/main/ets/pages/NavDestinationModeDemo.ets#L17-L88)

还需设置软键盘避让模式为压缩模式，示例代码如下：

```
1. import { UIAbility } from "@kit.AbilityKit";
2. import { window, KeyboardAvoidMode } from "@kit.ArkUI";

4. export default class EntryAbility extends UIAbility {
5. onWindowStageCreate(windowStage: window.WindowStage): void {
6. windowStage.loadContent('pages/GetSafeAreaHeightDemo', (err) => {
7. // Compression mode
8. windowStage.getMainWindowSync().getUIContext().setKeyboardAvoidMode(KeyboardAvoidMode.RESIZE);
9. });
10. }
11. }
```

[ExamplePageMode.ets](https://gitcode.com/harmonyos_samples/keyboard/blob/master/entry/src/main/ets/pages/ExamplePageMode.ets#L17-L28)

运行效果如下，点击输入框后，内容区域会进行压缩，弹窗整体不会发生上抬。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/N8BTx_nDQv-iSxEotKbIUg/zh-cn_image_0000002345807177.png?HW-CC-KV=V1&HW-CC-Date=20260429T061100Z&HW-CC-Expire=86400&HW-CC-Sign=C7895039C8B6CA61BAD065E14ACDB7114EAA16BD02D8544514E7CE1FEAA3383D "点击放大")

关于评论回复场景的实现，可以参考：[评论回复弹窗](bpta-comment-reply-pop-up-window.md)。

### 设置软键盘和弹窗组件距离

弹窗类组件默认避让模式下，软键盘弹起之后弹窗组件之间16vp间隔，开发者可以通过弹窗参数[BaseDialogOptions](../harmonyos-references/js-apis-promptaction.md#basedialogoptions11)中keyboardAvoidDistance，调整弹窗组件与软键盘之间的避让距离。设置软键盘间距时，需要将keyboardAvoidMode值设为KeyboardAvoidMode.DEFAULT。

```
1. this.getUIContext().getPromptAction().openCustomDialog({
2. builder: () => {
3. this.customDialogBuilder();
4. },
5. alignment: DialogAlignment.Bottom,
6. width: '100%',
7. // Set the distance between the soft keyboard and custom dialog to 0
8. keyboardAvoidDistance:LengthMetrics.vp(0)
9. });
```

[CustomDialogAvoid.ets](https://gitcode.com/harmonyos_samples/keyboard/blob/master/entry/src/main/ets/pages/CustomDialogAvoid.ets#L61-L69)

### Web组件内容输入框

针对由Web组件内容输入组件拉起软键盘以及避让软键盘的内容，可以参考：[Web组件对接软键盘](../harmonyos-guides/web-docking-softkeyboard.md)。

## 示例代码

* [实现软键盘弹出功能](https://gitcode.com/harmonyos_samples/keyboard)
