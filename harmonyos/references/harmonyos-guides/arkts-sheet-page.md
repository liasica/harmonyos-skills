---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sheet-page
title: 绑定半模态页面（bindSheet）
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用弹窗 > 绑定模态页面 > 绑定半模态页面（bindSheet）
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bc005ea3b8549f2910e8acaa4a3917fd2a3a7949c003727e30718cfeef8e2907
---

[半模态页面（bindSheet）](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)默认是模态形式的非全屏弹窗式交互页面，允许部分底层父视图可见，帮助用户在与半模态交互时保留其父视图环境。

半模态页面适用于展示简单的任务或信息面板，例如，个人信息、文本简介、分享面板、创建日程、添加内容等。若需展示可能影响父视图的半模态页面，半模态支持配置为非模态交互形式。

半模态在不同宽度的设备上存在不同的形态能力，开发者对不同宽度的设备上有不同的形态诉求请参考([preferType](../harmonyos-references/ts-universal-attributes-sheet-transition.md#sheetoptions))属性。可以使用bindSheet构建半模态转场效果，详见[模态转场](arkts-modal-transition.md#使用bindsheet构建半模态转场效果)。对于复杂或者冗长的用户流程，建议考虑其他的转场方式替代半模态。如[全模态转场](arkts-contentcover-page.md)和[Navigation转场](arkts-navigation-animation.md)。

## 使用约束

* 半模态内嵌[UIExtension](../harmonyos-references/js-apis-arkui-uiextension.md)时，不支持再在UIExtension内拉起半模态/弹窗。
* 若无二次确认或者自定义关闭行为的场景，不建议使用[shouldDismiss/onWillDismiss](../harmonyos-references/ts-universal-attributes-sheet-transition.md#sheetoptions)接口。

## 生命周期

半模态页面提供了生命周期函数，用于通知用户该弹窗的生命周期状态。生命周期的触发顺序依次为：onWillAppear -> onAppear -> onWillDisappear -> onDisappear。

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| onWillAppear | () => void | 半模态页面显示（动画开始前）回调函数。 |
| onAppear | () => void | 半模态页面显示（动画结束后）回调函数。 |
| onWillDisappear | () => void | 半模态页面回退（动画开始前）回调函数。 |
| onDisappear | () => void | 半模态页面回退（动画结束后）回调函数。 |

## 使用嵌套滚动交互

在半模态面板内容区域滑动时的操作优先级：

1. 内容处于最顶部（内容不可滚动时以此状态处理）

   上滑时，优先向上扩展面板挡位，如无挡位可扩展，则滚动内容

   下滑时，优先向下收缩面板挡位，如无挡位可收缩，则关闭面板
2. 内容处于中间位置（可上下滚动）

   上/下滑时，优先滚动内容，直至页面内容到达底部/顶部
3. 内容处于底部位置（内容可滚动时）

   上滑时，呈现内容区域回弹效果，不切换挡位

   下滑时，滚动内容直到到达顶部

半模态上述交互默认的嵌套模式为：{Forward：PARENT\_FIRST，Backward：SELF\_FIRST}

如果开发者希望在面板内容的builder中定义滚动容器，如List、Scroll，并结合半模态的上述交互能力，那么需要在垂直方向上为滚动容器设置嵌套滚动属性。

```
1. .nestedScroll({
2. // 可滚动组件往末尾端滚动时的嵌套滚动选项，手势向上
3. scrollForward: NestedScrollMode.PARENT_FIRST,
4. // 可滚动组件往起始端滚动时的嵌套滚动选项，手势向下
5. scrollBackward: NestedScrollMode.SELF_FIRST,
6. })
```

完整示例代码如下：

```
1. @Entry
2. @Component
3. struct SheetDemo {
4. @State isShowSheet: boolean = false;
5. private items: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

7. @Builder
8. SheetBuilder() {
9. Column() {
10. // 第一步：自定义滚动容器
11. List({ space: '10vp' }) {
12. ForEach(this.items, (item: number) => {
13. ListItem() {
14. Text(String(item)).fontSize(16).fontWeight(FontWeight.Bold)
15. }.width('90%').height('80vp').backgroundColor('#ff53ecd9').borderRadius(10)
16. })
17. }
18. .alignListItem(ListItemAlign.Center)
19. .margin({ top: '10vp' })
20. .width('100%')
21. .height('900px')
22. // 第二步：设置滚动组件的嵌套滚动属性
23. .nestedScroll({
24. scrollForward: NestedScrollMode.PARENT_FIRST,
25. scrollBackward: NestedScrollMode.SELF_FIRST,
26. })

28. // 请将$r('app.string.tSheetBuilder_text1')替换为实际资源文件，在本示例中该资源文件的value值为"非滚动区域"
29. Text($r('app.string.tSheetBuilder_text1'))
30. .width('100%')
31. .backgroundColor(Color.Gray)
32. .layoutWeight(1)
33. .textAlign(TextAlign.Center)
34. .align(Alignment.Top)
35. }.width('100%').height('100%')
36. }

38. build() {
39. Column() {
40. Button('Open Sheet').width('90%').height('80vp')
41. .onClick(() => {
42. this.isShowSheet = !this.isShowSheet;
43. })
44. .bindSheet($$this.isShowSheet, this.SheetBuilder(), {
45. detents: [SheetSize.MEDIUM, SheetSize.LARGE, 600],
46. preferType: SheetType.BOTTOM,
47. // 请将$r('app.string.tSheetBuilder_text2')替换为实际资源文件，在本示例中该资源文件的value值为"嵌套滚动场景"
48. title: { title: $r('app.string.tSheetBuilder_text2') },
49. })
50. }.width('100%').height('100%')
51. .justifyContent(FlexAlign.Center)
52. }
53. }
```

[SheetDemo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BindSheet/entry/src/main/ets/pages/bindSheet/template10/SheetDemo.ets#L16-L72)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/zm51GTLlSZOd8L8SfsqmVw/zh-cn_image_0000002583477923.png?HW-CC-KV=V1&HW-CC-Date=20260427T233946Z&HW-CC-Expire=86400&HW-CC-Sign=99C1692647FE393C8E19FFB78167AD36655786C21C0A3BAF7B09A95D17020745)

## 二次确认能力

推荐使用onWillDismiss接口，此接口支持在回调中处理二次确认，或自定义关闭行为。

说明

声明onWillDismiss接口后，半模态页面的所有关闭操作，包括侧滑、点击关闭按钮、点击蒙层和下拉关闭，都需通过调用dismiss方法来实现。若未实现此逻辑，半模态页面将无法响应上述关闭操作。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const TAG = '[Sample_SupportingAgingFriendly]';
4. const DOMAIN = 0xF811;
5. const BUNDLE = 'SupportingAgingFriendly_';

7. @Entry
8. @Component
9. struct OnWillDismiss_Dismiss {
10. @State isShow: Boolean = false;

12. @Builder
13. myBuilder() {
14. Column() {
15. Button('Button')
16. }
17. }

19. build() {
20. Button('OpenBindSheet')
21. .onClick(() => {
22. this.isShow = true
23. })
24. .margin(120)
25. .bindSheet($$this.isShow, this.myBuilder(), {
26. height: SheetSize.MEDIUM,
27. blurStyle: BlurStyle.Thick,
28. dragBar: true,
29. detents: [SheetSize.MEDIUM, SheetSize.LARGE],
30. title: { title: 'title', subtitle: 'subtitle' },
31. enableOutsideInteractive: false,
32. onWillDismiss: ((dismissSheetAction: DismissSheetAction) => {
33. // 第二步：确认二次回调交互能力，此处用AlertDialog提示 "是否需要关闭半模态"
34. this.getUIContext().showAlertDialog(
35. {
36. // 请将$r('app.string.bindContentCover_label2')替换为实际资源文件，在本示例中该资源文件的value值为"示例2（自定义转场动画）"
37. message: $r('app.string.bindContentCover_label2'),
38. autoCancel: true,
39. alignment: DialogAlignment.Bottom,
40. gridCount: 4,
41. offset: { dx: 0, dy: -20 },
42. primaryButton: {
43. value: 'cancel',
44. action: () => {
45. hilog.info(DOMAIN, TAG, 'Callback when the cancel button is clicked');
46. }
47. },
48. secondaryButton: {
49. enabled: true,
50. defaultFocus: true,
51. style: DialogButtonStyle.HIGHLIGHT,
52. value: 'ok',
53. // 第三步：确认关闭半模态逻辑所在，此处为AlertDialog的Button回调
54. action: () => {
55. // 第四步：上述第三步逻辑触发的时候，调用dismiss()关闭半模态
56. dismissSheetAction.dismiss();
57. hilog.info(DOMAIN, TAG, 'Callback when the ok button is clicked');
58. }
59. },
60. cancel: () => {
61. hilog.info(DOMAIN, TAG, BUNDLE + 'onWillDismiss_Dismiss:' + 'AlertDialog Closed callbacks');
62. }
63. }
64. )
65. })
66. })
67. }
68. }
```

[OnWillDismiss\_Dismiss.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BindSheet/entry/src/main/ets/pages/bindSheet/template11/OnWillDismiss_Dismiss.ets#L16-L86)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/NZZT2-_lTUeXHodtB9mFVA/zh-cn_image_0000002552798274.png?HW-CC-KV=V1&HW-CC-Date=20260427T233946Z&HW-CC-Expire=86400&HW-CC-Sign=2ECA19C61EDCEB114CF9ACD24D3042D59BCFCDF1A8F42ECA7D4CF292D7AC8CE9)

## 屏蔽部分关闭行为

由于声明了onWillDismiss接口，半模态的关闭行为都需要dismiss处理。可以通过if等逻辑自定义处理关闭逻辑。

下述示例显示半模态页面只在下滑的时候关闭。

```
1. onWillDismiss: ((DismissSheetAction: DismissSheetAction) => {
2. if (DismissSheetAction.reason === DismissReason.SLIDE_DOWN) {
3. DismissSheetAction.dismiss();// 注册dismiss行为
4. }
5. }),
```

同理可以结合onWillSpringBackWhenDismiss接口实现更好的下滑体验。

类比onWillDismiss，在声明了onWillSpringBackWhenDismiss后，半模态下滑时的回弹操作需要使用 SpringBackAction.springBack()处理，无此逻辑则不会回弹。

具体代码如下，在半模态下滑的时候无需回弹。

```
1. onWillDismiss: ((DismissSheetAction: DismissSheetAction) => {
2. if (DismissSheetAction.reason === DismissReason.SLIDE_DOWN) {
3. DismissSheetAction.dismiss();// 注册dismiss行为
4. }
5. }),

7. onWillSpringBackWhenDismiss: ((SpringBackAction: SpringBackAction) => {
8. // 没有注册springBack，下拉半模态页面无回弹行为
9. }),
```

## 半模态支持避让中轴

半模态从API version 14开始支持中轴避让，当前在2in1设备默认开启（仅窗口处于瀑布模式时产生避让）中轴避让能力，且在2in1设备默认避让区域为上半屏。开发者可以通过[SheetOptions](../harmonyos-references/ts-universal-attributes-sheet-transition.md#sheetoptions)的enableHoverMode主动设置是否避让中轴，及[SheetOptions](../harmonyos-references/ts-universal-attributes-sheet-transition.md#sheetoptions)的hoverModeArea设置避让中轴后显示区域。

* 半模态中轴避让不支持控件子窗能力，[SheetOptions](../harmonyos-references/ts-universal-attributes-sheet-transition.md#sheetoptions)中的showInSubWindow为true的场景。
* 2in1设备上需同时满足窗口处于瀑布模式才会产生避让。

完整示例代码如下：

```
1. @Entry
2. @Component
3. struct SheetTransitionExample {
4. @State isShow: boolean = false;
5. @State enableHoverMode: boolean = true;
6. @State hoverModeArea: HoverModeAreaType = HoverModeAreaType.TOP_SCREEN;

8. @Builder
9. myBuilder() {
10. Column() {
11. // 请将$r('app.string.bindSheetCmd_label10')替换为实际资源文件，在本示例中该资源文件的value值为"enableHoverMode切换"
12. Button($r('app.string.bindSheetCmd_label10'))
13. .margin(10)
14. .fontSize(20)
15. .onClick(() => {
16. this.enableHoverMode = !this.enableHoverMode;
17. })

19. // 请将$r('app.string.bindSheetCmd_label11')替换为实际资源文件，在本示例中该资源文件的value值为"hoverModeArea切换"
20. Button($r('app.string.bindSheetCmd_label11'))
21. .margin(10)
22. .fontSize(20)
23. .onClick(() => {
24. this.hoverModeArea = this.hoverModeArea === HoverModeAreaType.TOP_SCREEN ?
25. HoverModeAreaType.BOTTOM_SCREEN : HoverModeAreaType.TOP_SCREEN;
26. })

28. Button('close modal')
29. .margin(10)
30. .fontSize(20)
31. .onClick(() => {
32. this.isShow = false;
33. })
34. }
35. .width('100%')
36. .height('100%')
37. }

39. build() {
40. Column() {
41. // 请将$r('app.string.bindSheetCmd_label9')替换为实际资源文件，在本示例中该资源文件的value值为"拉起半模态"
42. Button($r('app.string.bindSheetCmd_label9'))
43. .onClick(() => {
44. this.isShow = true;
45. })
46. .fontSize(20)
47. .margin(10)
48. .bindSheet($$this.isShow, this.myBuilder(), {
49. height: 300,
50. backgroundColor: Color.Green,
51. preferType: SheetType.CENTER,
52. enableHoverMode: this.enableHoverMode,
53. hoverModeArea: this.hoverModeArea
54. })
55. }
56. .justifyContent(FlexAlign.Center)
57. .width('100%')
58. .height('100%')
59. }
60. }
```

[SheetTransitionExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BindSheet/entry/src/main/ets/pages/bindSheet/template12/SheetTransitionExample.ets#L16-L79)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/lJ2y1MHUQ_y0TThtvnbiLQ/zh-cn_image_0000002583437969.png?HW-CC-KV=V1&HW-CC-Date=20260427T233946Z&HW-CC-Expire=86400&HW-CC-Sign=B272794DC0368119C2EDABFEEB793B11FD3CEC4134F5D3D8FAC728525195A718)
