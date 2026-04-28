---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-popup-and-menu-components-popup
title: 气泡提示（Popup）
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用弹窗 > 气泡提示 > 气泡提示（Popup）
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cfb8587bcb5fed2377fb89accc4171bd6279b5fcf2fdc290b80c0ff691053eeb
---

Popup属性可绑定在组件上显示气泡弹窗提示，设置弹窗内容、交互逻辑和显示状态。主要用于屏幕录制、信息弹出提醒等显示状态。

气泡分为两种类型，一种是系统提供的气泡[PopupOptions](../harmonyos-references/ts-universal-attributes-popup.md#popupoptions类型说明)，一种是开发者可以自定义的气泡[CustomPopupOptions](../harmonyos-references/ts-universal-attributes-popup.md#custompopupoptions8类型说明)。其中，PopupOptions通过配置primaryButton和secondaryButton来设置带按钮的气泡；CustomPopupOptions通过配置[builder](arkts-builder.md)来设置自定义的气泡。其中系统提供的气泡PopupOptions，字体的最大放大倍数为2。

气泡可以通过配置[mask](../harmonyos-references/ts-universal-attributes-popup.md#popupoptions类型说明)来实现模态和非模态窗口，mask为true或者颜色值的时候，气泡为模态窗口，mask为false时，气泡为非模态窗口。

多个气泡同时弹出时，子窗内显示的气泡比主窗内显示的气泡层级高，所处窗口相同时，后面弹出的气泡层级比先弹出的气泡层级高。

## 文本提示气泡

文本提示气泡常用于展示带有文本的信息提示，适用于无交互的场景。Popup属性需绑定组件，当bindPopup属性的参数show为true时，会弹出气泡提示。

在Button组件上绑定Popup属性，每次点击Button按钮时，handlePopup会切换布尔值。当值为true时，触发bindPopup弹出气泡。

```
1. @Entry
2. @Component
3. export struct TextPopupExample {
4. @State handlePopup: boolean = false;

6. build() {
7. NavDestination() {
8. Column() {
9. Button('PopupOptions')
10. .id('PopupOptions')
11. .margin({ top: 300 })
12. .onClick(() => {
13. this.handlePopup = !this.handlePopup;
14. })
15. .bindPopup(this.handlePopup, {
16. message: 'This is a popup with PopupOptions',
17. })
18. }.width('100%').padding({ top: 5 })
19. }
20. // ...
21. }
22. }
```

[TextPrompts.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/popup/TextPrompts.ets#L16-L42)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/q3dF1EeqTNOHA3hVRtRzyw/zh-cn_image_0000002552798268.png?HW-CC-KV=V1&HW-CC-Date=20260427T233945Z&HW-CC-Expire=86400&HW-CC-Sign=242750FCA60EE9DBEE63046914C58917C6A5A3CD319BF5CE3FBFFBFB2BE423D6)

## 添加气泡状态变化的事件

通过[PopupOptions](../harmonyos-references/ts-universal-attributes-popup.md#popupoptions类型说明)中的onStateChange属性为气泡添加状态变化的事件回调，可以判断气泡的当前显示状态。

```
1. @Entry
2. @Component
3. export struct StatePopupExample {
4. @State handlePopup: boolean = false;

6. build() {
7. NavDestination() {
8. Column() {
9. Button('PopupOptions')
10. .id('PopupOptions')
11. .margin({ top: 300 })
12. .onClick(() => {
13. this.handlePopup = !this.handlePopup;
14. })
15. .bindPopup(this.handlePopup, {
16. message: 'This is a popup with PopupOptions',
17. onStateChange: (e)=> { // 返回当前的气泡状态
18. if (!e.isVisible) {
19. this.handlePopup = false;
20. }
21. }
22. })
23. }.width('100%').padding({ top: 5 })
24. }
25. // ...
26. }
27. }
```

[PopupStateChange.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/popup/PopupStateChange.ets#L16-L47)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/vA95fgp5Qeq-2waraAZHFw/zh-cn_image_0000002583437963.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233945Z&HW-CC-Expire=86400&HW-CC-Sign=1C15BA29273431DE929A6395BFD4E901D562F28DC8B86D96A4402762296E71E1)

## 带按钮的提示气泡

通过[PopupOptions](../harmonyos-references/ts-universal-attributes-popup.md#popupoptions类型说明)中的primaryButton、secondaryButton属性为气泡最多设置两个Button按钮，通过此按钮进行简单的交互，开发者可以通过配置action参数来设置想要触发的操作。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. @Entry
4. @Component
5. export struct ButtonPopupExample {
6. @State handlePopup: boolean = false;

8. build() {
9. NavDestination() {
10. Column() {
11. Button('PopupOptions').margin({ top: 300 })
12. .id('PopupOptions')
13. .onClick(() => {
14. this.handlePopup = !this.handlePopup;
15. })
16. .bindPopup(this.handlePopup, {
17. message: 'This is a popup with PopupOptions',
18. primaryButton: {
19. value: 'Confirm',
20. action: () => {
21. this.handlePopup = !this.handlePopup;
22. hilog.info(0xFF00, 'DialogProject', 'confirm Button click');
23. }
24. },
25. secondaryButton: {
26. value: 'Cancel',
27. action: () => {
28. this.handlePopup = !this.handlePopup;
29. }
30. },
31. onStateChange: (e) => {
32. if (!e.isVisible) {
33. this.handlePopup = false;
34. }
35. }
36. })
37. }.width('100%').padding({ top: 5 })
38. }
39. // ...
40. }
41. }
```

[ButtonPopup.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/popup/ButtonPopup.ets#L16-L61)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/EOYl7eBxTF6vZKSKn_0MqA/zh-cn_image_0000002552957918.jpeg?HW-CC-KV=V1&HW-CC-Date=20260427T233945Z&HW-CC-Expire=86400&HW-CC-Sign=D4F2D4B680CD63D2F5A29D336A800864E1D43E9FA0EBDB4291284F87101C01DB)

## 气泡的动画

通过[PopupOptions](../harmonyos-references/ts-universal-attributes-popup.md#popupoptions类型说明)或[CustomPopupOptions](../harmonyos-references/ts-universal-attributes-popup.md#custompopupoptions8类型说明)中的transition属性，可以控制气泡的进场和出场动画效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. export struct AnimationPopupExample {
5. @State handlePopup: boolean = false;
6. @State customPopup: boolean = false;

8. // popup构造器定义弹框内容
9. @Builder
10. popupBuilder() {
11. Row() {
12. Text('Custom Popup with transitionEffect').fontSize(10)
13. }.height(50).padding(5)
14. }

16. build() {
17. NavDestination() {
18. Flex({ direction: FlexDirection.Column }) {
19. // PopupOptions 类型设置弹框内容
20. Button('PopupOptions')
21. .id('PopupOptions')
22. .onClick(() => {
23. this.handlePopup = !this.handlePopup;
24. })
25. .bindPopup(this.handlePopup, {
26. message: 'This is a popup with transitionEffect',
27. placement: Placement.Top,
28. showInSubWindow: false,
29. onStateChange: (e) => {
30. if (!e.isVisible) {
31. this.handlePopup = false;
32. }
33. },
34. // 设置弹窗显示动效为透明度动效与平移动效的组合效果，无退出动效
35. transition: TransitionEffect.asymmetric(
36. TransitionEffect.OPACITY.animation({ duration: 1000, curve: Curve.Ease }).combine(
37. TransitionEffect.translate({ x: 50, y: 50 })),
38. TransitionEffect.IDENTITY)
39. })
40. .position({ x: 100, y: 150 })

42. // CustomPopupOptions 类型设置弹框内容
43. Button('CustomPopupOptions')
44. .id('CustomPopupOptions')
45. .onClick(() => {
46. this.customPopup = !this.customPopup;
47. })
48. .bindPopup(this.customPopup, {
49. builder: this.popupBuilder,
50. placement: Placement.Top,
51. showInSubWindow: false,
52. onStateChange: (e) => {
53. if (!e.isVisible) {
54. this.customPopup = false;
55. }
56. },
57. // 设置弹窗显示动效与退出动效为缩放动效
58. transition: TransitionEffect.scale({ x: 1, y: 0 }).animation({ duration: 500, curve: Curve.Ease })
59. })
60. .position({ x: 80, y: 300 })
61. }.width('100%').padding({ top: 5 })
62. }
63. // ...
64. }
65. }
```

[PopupAnimation.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/popup/PopupAnimation.ets#L16-L85)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/q1ZWOsMdTa6k9MZB7QhWEg/zh-cn_image_0000002583477919.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233945Z&HW-CC-Expire=86400&HW-CC-Sign=D54EB23033D882F3B7F246C906E952DC82A7176F78AE331BA09028B599D6EAF1)

## 自定义气泡

开发者可以使用[CustomPopupOptions](../harmonyos-references/ts-universal-attributes-popup.md#custompopupoptions8类型说明)的builder创建自定义气泡，@Builder中可以放自定义的内容。除此之外，还可以通过popupColor等参数控制气泡样式。

```
1. // 请将$r('app.media.xxx')替换为实际资源文件
2. @Entry
3. @Component
4. export struct CustomPopupExample {
5. @State customPopup: boolean = false;

7. // popup构造器定义弹框内容
8. @Builder
9. popupBuilder() {
10. Row({ space: 2 }) {
11. Image($r('app.media.app_icon')).width(24).height(24).margin({ left: 5 })
12. Text('This is Custom Popup').fontSize(15)
13. }.width(200).height(50).padding(5)
14. }

16. build() {
17. NavDestination() {
18. Column() {
19. Button('CustomPopupOptions')
20. .id('CustomPopupOptions')
21. .margin({ top: 300 })
22. .onClick(() => {
23. this.customPopup = !this.customPopup;
24. })
25. .bindPopup(this.customPopup, {
26. builder: this.popupBuilder, // 气泡的内容
27. placement: Placement.Bottom, // 气泡的弹出位置
28. popupColor: Color.Pink, // 气泡的背景色
29. backgroundBlurStyle: BlurStyle.NONE,
30. onStateChange: (e) => {
31. if (!e.isVisible) {
32. this.customPopup = false
33. }
34. }
35. })
36. }
37. .height('100%')
38. }
39. // ...
40. }
41. }
```

[CustomPopup.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/popup/CustomPopup.ets#L16-L63)

使用者通过配置placement参数将弹出的气泡放到需要提示的位置。弹窗构造器会触发弹出提示信息，来引导使用者完成操作，也让使用者有更好的UI体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/YMhzAuyiQES0bTSb9s4ocw/zh-cn_image_0000002552798270.jpeg?HW-CC-KV=V1&HW-CC-Date=20260427T233945Z&HW-CC-Expire=86400&HW-CC-Sign=4E14FF87C0BEF83EB9C5999FF1EE2A51CB9202F5D9D4E50E1343F993D2244283)

## 气泡样式

气泡除了可以通过builder实现自定义气泡，还可以通过接口设置气泡的样式和显示效果。

背景颜色：气泡的背景色默认为透明，但是会有一个默认的模糊效果，手机上为COMPONENT\_ULTRA\_THICK。

蒙层样式：气泡默认有蒙层，且蒙层的颜色为透明。

显示大小：气泡大小由内部的builder大小或者message的长度决定的。

显示位置：气泡默认显示在宿主组件的下方，可以通过[PopupOptions](../harmonyos-references/ts-universal-attributes-popup.md#popupoptions类型说明)中的Placement属性来配置其显示位置以及对齐方向。

以下示例通过设置[PopupOptions](../harmonyos-references/ts-universal-attributes-popup.md#popupoptions类型说明)中的popupColor（背景颜色）、mask（蒙层样式）、width（气泡宽度）、placement（显示位置）实现气泡的样式。

```
1. // xxx.ets

3. @Entry
4. @Component
5. export struct StylePopupExample {
6. @State handlePopup: boolean = false;

8. build() {
9. NavDestination() {
10. Column({ space: 100 }) {
11. Button('PopupOptions')
12. .onClick(() => {
13. this.handlePopup = !this.handlePopup;
14. })
15. .bindPopup(this.handlePopup, {
16. width: 200,
17. message: 'This is a popup.',
18. popupColor: Color.Red, // 设置气泡的背景色
19. mask: {
20. color: '#33d9d9d9'
21. },
22. placement: Placement.Top,
23. backgroundBlurStyle: BlurStyle.NONE // 去除背景模糊效果需要关闭气泡的模糊背景
24. })
25. }
26. .width('100%')
27. }
28. // ...
29. }
30. }
```

[PopupStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/popup/PopupStyle.ets#L16-L50)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/fZzyCvA2Sx6hX0p9h-SOaw/zh-cn_image_0000002583437965.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233945Z&HW-CC-Expire=86400&HW-CC-Sign=8FB34E4EB08D1A138C79C090198C4809D5B142344A38F981F2C4A7AB2068EA64)

## 气泡避让软键盘

当软键盘弹出时，气泡默认不会对其避让，可能导致气泡被软键盘覆盖，从API version 15开始，可以设置[CustomPopupOptions](../harmonyos-references/ts-universal-attributes-popup.md#custompopupoptions8类型说明)中keyboardAvoidMode属性的值为KeyboardAvoidMode.DEFAULT，来使气泡避让键盘。这时如果当前没有位置放下气泡时，气泡会从预设位置平移覆盖宿主组件。

```
1. // xxx.ets
2. @Entry
3. @Component
4. export struct AvoidSoftKeyboardPopupExample {
5. @State handlePopup: boolean = false;

7. @Builder
8. popupBuilder() {
9. Column({ space: 2 }) {
10. Text('Custom Popup').fontSize(20)
11. .borderWidth(2)
12. TextInput()
13. }.width(200).padding(5)
14. }

16. build() {
17. NavDestination() {
18. Column({ space: 100 }) {
19. TextInput()
20. Button('PopupOptions')
21. .id('PopupOptions')
22. .onClick(() => {
23. this.handlePopup = !this.handlePopup;
24. })
25. .bindPopup(this.handlePopup!!, {
26. width: 200,
27. builder: this.popupBuilder(),
28. placement: Placement.Bottom,
29. mask: false,
30. autoCancel: false,
31. keyboardAvoidMode: KeyboardAvoidMode.DEFAULT
32. })
33. .position({ x: 100, y: 300 })
34. }
35. .width('100%')
36. }
37. // ...
38. }
39. }
```

[PopupAvoidSoftKeyboard.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/popup/PopupAvoidSoftKeyboard.ets#L16-L59)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/BJSi0rufTKmQxa_UL8CsBA/zh-cn_image_0000002552957920.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233945Z&HW-CC-Expire=86400&HW-CC-Sign=CE4E490D30CA8CC68DA07A265847FD890D30AF4171D3D5E9B6EC257C81F59DF7)

## 设置气泡内的多态效果

目前使用@Builder自定义气泡内容时，默认不支持多态样式，可以使用@Component新建一个组件实现按下气泡中的内容时背景变色。

```
1. // 请将$r('app.media.xxx')替换为实际资源文件
2. @Entry
3. @Component
4. export struct PolymorphicEffectPopupExample {
5. // 请在resources\base\element\string.json文件中配置name为'xxx'，value为非空字符串的资源
6. @State scan: string =
7. this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('Scan_title') as string;
8. @State createGroupChat: string =
9. this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('Create_group_chat') as string;
10. @State electronicWorkCard: string =
11. this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('Electronic_work_card') as string;
12. private menus: Array<string> = [this.scan, this.createGroupChat, this.electronicWorkCard];

14. // popup构造器定义弹框内容
15. @Builder
16. popupItemBuilder(name: string, action: string) {
17. PopupItemChild({ childName: name, childAction: action })
18. }

20. // popup构造器定义弹框内容
21. @Builder
22. popupBuilder() {
23. Column() {
24. ForEach(
25. this.menus,
26. (item: string, index) => {
27. this.popupItemBuilder(item, String(index))
28. },
29. (item: string, index) => {
30. return item
31. })
32. }
33. .padding(8)
34. }

36. @State customPopup: boolean = false;

38. build() {
39. NavDestination() {
40. Column() {
41. Button('click me')
42. .id('click me')
43. .onClick(() => {
44. this.customPopup = !this.customPopup
45. })
46. .bindPopup(
47. this.customPopup,
48. {
49. builder: this.popupBuilder, // 气泡的内容
50. placement: Placement.Bottom, // 气泡的弹出位置
51. popupColor: Color.White, // 气泡的背景色
52. onStateChange: (event) => {
53. if (!event.isVisible) {
54. this.customPopup = false
55. }
56. }
57. })
58. }
59. .width('100%')
60. .justifyContent(FlexAlign.Center)
61. }
62. // ...
63. }
64. }

66. @Component
67. struct PopupItemChild {
68. @Prop childName: string = '';
69. @Prop childAction: string = '';
70. @State selected: string =
71. this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('Selected') as string;

73. build() {
74. Row({ space: 8 }) {
75. Image($r('app.media.startIcon'))
76. .width(24)
77. .height(24)
78. Text(this.childName)
79. .fontSize(16)
80. }
81. .width(130)
82. .height(50)
83. .padding(8)
84. .onClick(() => {
85. this.getUIContext().getPromptAction().showToast({ message: this.selected + this.childName })
86. })
87. .stateStyles({
88. normal: {
89. .backgroundColor(Color.White)
90. },
91. pressed: {
92. .backgroundColor('#d4f1ff')
93. }
94. })
95. }
96. }
```

[PopupPolymorphicEffect.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/popup/PopupPolymorphicEffect.ets#L17-L117)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/8lHc-7z9RFeQgLegwl0Zpg/zh-cn_image_0000002583477921.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233945Z&HW-CC-Expire=86400&HW-CC-Sign=43E551907EBB423625B81422A71C81F32F97CF56284BC80C400ABC6FD7734053)

## 气泡支持避让中轴

从API version 18起，气泡支持中轴避让功能。从API version 20开始，在2in1设备上默认启用（仅在窗口处于瀑布模式时产生避让）。开发者可通过[PopupOptions](../harmonyos-references/ts-universal-attributes-popup.md#popupoptions类型说明)中的enableHoverMode属性，控制气泡是否启用中轴避让。

说明

* 如果气泡的点击位置在中轴区域，则气泡不会避让。
* 2in1设备上需同时满足窗口处于瀑布模式才会产生避让。

```
1. @Entry
2. @Component
3. export struct SupportedAvoidAxisPopupExample {
4. // 请在resources\base\element\string.json文件中配置name为'xxx'，value为非空字符串的资源
5. @State upScreen: string =
6. this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('Upper_half_screen') as string;
7. @State middleAxle: string =
8. this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('Middle_axle') as string;
9. @State lowerScreen: string =
10. this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('Lower_half_screen') as string;
11. @State subwindowDisplay: string =
12. this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('Subwindow_display') as string;
13. @State subwindow: string =
14. this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('Subwindow') as string;
15. @State nonSubwindow: string =
16. this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('Non_Subwindow') as string;
17. @State zone: string =
18. this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('zone') as string;
19. @State hoverModeStart: string =
20. this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('hoverMode_start') as string;

22. @State message: string = 'Hello World';
23. @State index: number = 0;
24. @State arrayStr: Array<string> = [this.upScreen, this.middleAxle, this.lowerScreen];
25. @State enableHoverMode: boolean | undefined = true;
26. @State showInSubwindow: boolean = false;
27. @State placement: Placement | undefined = undefined;
28. @State isShow: boolean = false;

30. build() {
31. NavDestination() {
32. RelativeContainer() {
33. Column() {
34. Button(this.zone + this.arrayStr[this.index])
35. .onClick(() => {
36. if (this.index < 2) {
37. this.index++
38. } else {
39. this.index = 0
40. }
41. })

43. Button(this.subwindowDisplay + (this.showInSubwindow ? this.subwindow : this.nonSubwindow))
44. .onClick(() => {
45. this.showInSubwindow = !this.showInSubwindow
46. })

48. Button(this.hoverModeStart + this.enableHoverMode)
49. .onClick(() => {
50. if (this.enableHoverMode === undefined) {
51. this.enableHoverMode = true
52. } else if (this.enableHoverMode === true) {
53. this.enableHoverMode = false
54. } else {
55. this.enableHoverMode = undefined
56. }
57. })
58. }

60. Row() {
61. Button('Popup')
62. .id('Popup')
63. .fontWeight(FontWeight.Bold)
64. .bindPopup(this.isShow, {
65. message: 'popup',
66. enableHoverMode: this.enableHoverMode,
67. showInSubWindow: this.showInSubwindow,
68. })
69. .onClick(() => {
70. this.isShow = !this.isShow
71. })
72. }
73. .alignRules({
74. center: { anchor: '__container__', align: VerticalAlign.Center },
75. middle: { anchor: '__container__', align: HorizontalAlign.Center }
76. })
77. .margin({
78. top: this.index === 2 ? 330 : this.index === 1 ? 50 : 0,
79. bottom: this.index === 0 ? 330 : 0
80. })
81. }
82. .height('100%')
83. .width('100%')
84. }
85. // ...
86. }
87. }
```

[PopupSupportedAvoidAxis.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/popup/PopupSupportedAvoidAxis.ets#L16-L107)
