---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-357
title: 状态栏与页面内容发生重叠，如何解决
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 状态栏与页面内容发生重叠，如何解决
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:31+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b009f13fb4c849b317eec55dcc2dc9be04b7defb6d7e27ff45ae0dc40343afce
---

**问题描述**

状态栏与页面内容发生重叠问题存在以下两种场景：

1. 状态栏应该隐藏，实际上未隐藏，例如图片预览场景。
2. 界面布局内容未对状态栏进行避让。

**问题一解决措施：**

1. 调用setWindowLayoutFullScreen()接口设置窗口全屏。
2. 获取并缓存窗口对象，可参考：[Interface (Window)](../harmonyos-references/arkts-apis-window-window.md)。
3. 在点击进入图片预览页时，使用窗口对象调用[setSpecificSystemBarEnabled()](../harmonyos-references/arkts-apis-window-window.md#setspecificsystembarenabled11)接口设置状态栏为隐藏状态。
4. 点击蒙层退出预览时，使用窗口对象调用[setSpecificSystemBarEnabled()](../harmonyos-references/arkts-apis-window-window.md#setspecificsystembarenabled11)接口设置状态栏为显示状态。

参考代码：

设置全屏模式，缓存窗口对象

```
1. // EntryAbility.ets

4. onWindowStageCreate(windowStage: window.WindowStage): void {
5. // Main window is created, set main page for this ability
6. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

9. windowStage.loadContent('pages/ImagePreview', (err) => {
10. if (err.code) {
11. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
12. return;
13. }
14. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');

17. let windowClass: window.Window = windowStage.getMainWindowSync(); // Get the main window of the application
18. // 1. Set the window to full screen
19. let isLayoutFullScreen = true;
20. windowClass.setWindowLayoutFullScreen(isLayoutFullScreen);
21. // 2. Cache window object
22. AppStorage.setOrCreate('windowClass', windowClass);
23. });
24. }
```

[EntryAbilityOverlap\_One.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/entryability/EntryAbilityOverlap_One.ets#L29-L52)

```
1. import { window } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct ImagePreviewExample {
7. windowClass: window.Window = AppStorage.get<window.Window>('windowClass') as window.Window;
8. @State visible: Visibility = Visibility.None;
9. @State scaleValue: number = 1;
10. @State pinchValue: number = 1;
11. @State pinchX: number = 0;
12. @State pinchY: number = 0;
13. @State count: number = 0;
14. @State offsetX: number = 0;
15. @State offsetY: number = 0;
16. @State positionX: number = 0;
17. @State positionY: number = 0;

20. build() {
21. Stack() {
22. Row() {
23. Column() {
24. Image($r('app.media.startIcon'))
25. .width(100)
26. .height(100)
27. .onClick(() => {
28. if (this.visible === Visibility.Visible) {
29. this.visible = Visibility.None;
30. } else {
31. this.visible = Visibility.Visible;
32. this.windowClass.setSpecificSystemBarEnabled('status', false);
33. }
34. })
35. }
36. .width('100%')
37. .justifyContent(FlexAlign.Center)
38. .alignItems(HorizontalAlign.Center)
39. }
40. .height('100%')

43. Text('')
44. .onClick(() => {
45. if (this.visible === Visibility.Visible) {
46. this.windowClass.setSpecificSystemBarEnabled('status', true);
47. this.visible = Visibility.None;
48. } else {
49. this.visible = Visibility.Visible;
50. }
51. })
52. .width('100%')
53. .height('100%')
54. .opacity(0.16)// transparency
55. .backgroundColor(Color.Black)
56. .visibility(this.visible)

59. Column() {
60. Image($r('app.media.startIcon'))
61. .width(300)
62. .height(300)
63. .draggable(false)
64. .visibility(this.visible)
65. .scale({
66. x: this.scaleValue,
67. y: this.scaleValue,
68. z: 1
69. })
70. .translate({
71. x: this.offsetX,
72. y: this.offsetY,
73. z: 0
74. })
75. .gesture(
76. GestureGroup(GestureMode.Parallel,
77. PinchGesture({ fingers: 2 })
78. .onActionUpdate((event?: GestureEvent) => {
79. if (event) {
80. this.scaleValue = this.pinchValue * event.scale;
81. this.pinchX = event.pinchCenterX;
82. this.pinchY = event.pinchCenterY;
83. }
84. })
85. .onActionEnd(() => {
86. this.pinchValue = this.scaleValue;
87. }),
88. PanGesture()
89. .onActionUpdate((event?: GestureEvent) => {
90. if (event) {
91. this.offsetX = this.positionX + event.offsetX;
92. this.offsetY = this.positionY + event.offsetY;
93. }
94. })
95. .onActionEnd(() => {
96. this.positionX = this.offsetX;
97. this.positionY = this.offsetY;
98. })
99. )
100. )
101. }
102. }
103. .backgroundColor(Color.White)
104. .height('100%')
105. .width('100%')
106. }
107. }
```

[ResolveOverlapBetweenStatusBarAndPage\_One.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ResolveOverlapBetweenStatusBarAndPage_One.ets#L21-L127)

**问题二解决措施：**

1. 调用[setWindowLayoutFullScreen()](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)接口设置窗口全屏。
2. 使用[getWindowAvoidArea()](../harmonyos-references/js-apis-arkui-uiextension.md#getwindowavoidarea)接口获取布局遮挡区域（例如状态栏、导航条）。
3. 在布局中对具体控件进行布局调整，以避免遮挡，例如为顶部组件增加相应高度或设置 margin 和 padding 边距。

参考代码

```
1. // EntryAbility.ets

4. onWindowStageCreate(windowStage: window.WindowStage): void {
5. // Main window is created, set main page for this ability
6. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

9. windowStage.loadContent('pages/AvoidStatusBar', (err) => {
10. if (err.code) {
11. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
12. return;
13. }
14. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');

17. let windowClass: window.Window = windowStage.getMainWindowSync(); // Get the main window of the application
18. // 1. Set the window to full screen
19. let isLayoutFullScreen = true;
20. windowClass.setWindowLayoutFullScreen(isLayoutFullScreen);
21. // 2. Cache window object
22. AppStorage.setOrCreate('windowClass', windowClass);

25. // 3. Obtain layout to avoid obstructed areas
26. let type = window.AvoidAreaType.TYPE_SYSTEM;
27. let avoidArea = windowClass.getWindowAvoidArea(type);
28. let statusBar =windowClass.getUIContext().px2vp( avoidArea.topRect.height); // Get the height of the status bar
29. AppStorage.setOrCreate('statusBar', statusBar);
30. });
31. }
```

[EntryAbilityOverlap\_Two.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/entryability/EntryAbilityOverlap_Two.ets#L29-L59)

```
1. @Entry
2. @Component
3. struct AvoidStatusBar {
4. statusBar: number = AppStorage.get<number>('statusBar') as number;

7. build() {

10. Column() {
11. Row() {
12. Text('ROW1')
13. .fontSize(40)
14. }
15. .backgroundColor(Color.Orange)
16. .padding(20)

19. Row() {
20. Text('ROW2')
21. .fontSize(40)
22. }
23. .backgroundColor(Color.Orange)
24. .padding(20)

27. Row() {
28. Text('ROW3')
29. .fontSize(40)
30. }
31. .backgroundColor(Color.Orange)
32. .padding(20)

35. Row() {
36. Text('ROW4')
37. .fontSize(40)
38. }
39. .backgroundColor(Color.Orange)
40. .padding(20)

43. Row() {
44. Text('ROW5')
45. .fontSize(40)
46. }
47. .backgroundColor(Color.Orange)
48. .padding(20)

51. Row() {
52. Text('ROW6')
53. .fontSize(40)
54. }
55. .backgroundColor(Color.Orange)
56. .padding(20)
57. }
58. .width('100%')
59. .height('100%')
60. .alignItems(HorizontalAlign.Center)
61. .justifyContent(FlexAlign.SpaceBetween)
62. .padding({ top: this.statusBar }) // The specific value of the margin or padding here should be consistent with the height of the status bar area in practice
63. .backgroundColor('#008000')
64. }
65. }
```

[ResolveOverlapBetweenStatusBarAndPage\_Two.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ResolveOverlapBetweenStatusBarAndPage_Two.ets#L21-L85)
