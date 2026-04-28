---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-atomicservice-interstitialdialogaction
title: InterstitialDialogAction
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > AtomicService > InterstitialDialogAction
category: harmonyos-references
scraped_at: 2026-04-28T08:02:27+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:98dbccca11950dfadf58329e65136138e2b3058d3bbd3c91dfa8711e6211fa32
---

InterstitialDialogAction弹框在元服务中用于在保持当前的上下文环境时，临时展示用户需关注的信息或待处理的操作，用户点击弹框的不同区域可以触发相应的动作。

说明

该组件从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { InterstitialDialogAction, IconStyle, TitlePosition, BottomOffset } from '@kit.ArkUI';
```

## 子组件

PhonePC/2in1TabletTVWearable

无

## 属性

PhonePC/2in1TabletTVWearable

不支持[通用属性](ts-component-general-attributes.md)

## InterstitialDialogAction

PhonePC/2in1TabletTVWearable

对自定义弹框进行封装，用于在保持当前的上下文环境时，临时展示用户需关注的信息或待处理的操作。使用示例参见[示例](ohos-atomicservice-interstitialdialogaction.md#示例)。

### constructor

PhonePC/2in1TabletTVWearable

constructor(dialogOptions: DialogOptions)

InterstitialDialogAction的构造函数

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dialogOptions | [DialogOptions](ohos-atomicservice-interstitialdialogaction.md#dialogoptions) | 是 | 设置弹框特有的属性。 |

### openDialog

PhonePC/2in1TabletTVWearable

openDialog(): void

打开弹框。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### closeDialog

PhonePC/2in1TabletTVWearable

closeDialog(): void

关闭弹框。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## DialogOptions

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

设置弹框特有的属性以及提供给用户自定义的点击触发动作。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uiContext | [UIContext](arkts-apis-uicontext-uicontext.md) | 否 | 否 | UI上下文实例。 |
| bottomOffsetType | [BottomOffset](ohos-atomicservice-interstitialdialogaction.md#bottomoffset) | 否 | 是 | 弹框距离底部偏移类型。默认值为[BottomOffset](ohos-atomicservice-interstitialdialogaction.md#bottomoffset).OFFSET\_FOR\_BAR。 |
| title | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 弹框标题文本。默认为空字符串。 |
| subtitle | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 弹框副标题文本。默认为空字符串。 |
| titleColor | [ResourceStr](ts-types.md#resourcestr) | [Color](ts-appendix-enums.md#color) | 否 | 是 | 弹框标题文本颜色。默认为$r('sys.color.ohos\_id\_color\_text\_primary\_contrary')。 |
| subtitleColor | [ResourceStr](ts-types.md#resourcestr) | [Color](ts-appendix-enums.md#color) | 否 | 是 | 弹框副标题文本颜色。默认为$r('sys.color.ohos\_id\_color\_text\_secondary\_contrary')。 |
| backgroundImage | [Resource](ts-types.md#resource) | 否 | 是 | 弹框背景图片。默认为纯色背景，颜色值为#EBEEF5。 |
| foregroundImage | [Resource](ts-types.md#resource) | 否 | 是 | 弹框前景图片。默认为空，即不显示前景图片。 |
| iconStyle | [IconStyle](ohos-atomicservice-interstitialdialogaction.md#iconstyle) | 否 | 是 | 关闭按钮图标的样式（亮调或者暗调）。  默认值：[IconStyle](ohos-atomicservice-interstitialdialogaction.md#iconstyle).Light |
| titlePosition | [TitlePosition](ohos-atomicservice-interstitialdialogaction.md#titleposition) | 否 | 是 | 标题在弹框中的位置，在副标题的上方或者在副标题的下方。  默认值：[TitlePosition](ohos-atomicservice-interstitialdialogaction.md#titleposition).Top |
| onDialogClick | Callback<void> | 否 | 是 | 点击弹框任意位置后触发的用户自定义动作。默认为“执行关闭弹框的函数”，即仅关闭弹框。 |
| onDialogClose | Callback<void> | 否 | 是 | 点击关闭按钮后触发的用户自定义动作。默认为“执行关闭弹框的函数”，即仅关闭弹框。 |

## IconStyle

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

设置关闭按钮的色调样式，默认设置关闭按钮为亮色调。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DARK | 0 | 设置关闭按钮为暗色调。 |
| LIGHT | 1 | 设置关闭按钮为亮色调。  默认值。 |

## TitlePosition

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

设置主副标题之间的上下相对位置，默认设置为主标题在副标题之上。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TOP | 0 | 设置主标题位于副标题之上。  默认值。 |
| BOTTOM | 1 | 设置副标题位于主标题之上。 |

## BottomOffset

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

设置不同情景模式下弹框距离底部的距离，判断依据为是否存在菜单栏，默认显示为不存在菜单栏情况下的距离。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OFFSET\_FOR\_BAR | 0 | 存在菜单栏情况下与窗口底部的距离。  默认值，设置后弹框距离底部88vp。 |
| OFFSET\_FOR\_NONE | 1 | 不存在菜单栏情况下与窗口底部的距离。  设置后弹框距离底部44vp。 |

## 事件

PhonePC/2in1TabletTVWearable

不支持[通用事件](ts-component-general-events.md)

## 示例

PhonePC/2in1TabletTVWearable

### 示例1

为可选属性设置相应值，用两种不同参数类型分别为主标题、副标题设置颜色值，关闭按钮设置为暗色调，主副标题相对位置设置为主标题在副标题上方，底部距离类型设置为不存在菜单栏情况下的距离。

```
1. // ../entryability/EntryAbility
2. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { window } from '@kit.ArkUI';
5. import { BusinessError } from '@kit.BasicServicesKit';

7. let dialogUIContext: UIContext | null = null;

9. export function getDialogUIContext(): UIContext | null {
10. return dialogUIContext;
11. }

13. export default class EntryAbility extends UIAbility {
14. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
15. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
16. }

18. onDestroy(): void {
19. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
20. }

22. onWindowStageCreate(windowStage: window.WindowStage): void {
23. // Main window is created, set main page for this ability
24. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

26. windowStage.loadContent('pages/Index', (err) => {
27. if (err.code) {
28. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
29. return;
30. }
31. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
32. });

34. let windowClass: window.Window | undefined = undefined;
35. windowStage.getMainWindow((err: BusinessError, data) => {
36. let errCode: number = err.code;
37. if (errCode) {
38. console.error('Failed to obtain the main window. Cause: ' + JSON.stringify(err));
39. return;
40. }
41. windowClass = data;
42. console.info('Succeeded in obtaining the main window. Data: ' + JSON.stringify(data));
43. dialogUIContext = windowClass.getUIContext();
44. })

46. //获取窗口
47. windowStage.getMainWindow((err, data) => {
48. if (err.code) {
49. console.error('Failed to obtain the main window. Cause: ' + JSON.stringify(err));
50. return;
51. }
52. windowClass = data;
53. console.info('Succeeded in obtaining the main window. Data: ' + JSON.stringify(data));
54. //设置窗口全屏
55. windowClass.setWindowLayoutFullScreen(false)
56. })
57. }

59. onWindowStageDestroy(): void {
60. // Main window is destroyed, release UI related resources
61. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
62. }

64. onForeground(): void {
65. // Ability has brought to foreground
66. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
67. }

69. onBackground(): void {
70. // Ability has back to background
71. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
72. }
73. }
```

```
1. // Index.ets
2. import { getDialogUIContext } from '../entryability/EntryAbility';
3. import { UIContext, InterstitialDialogAction, IconStyle, TitlePosition, BottomOffset } from '@kit.ArkUI';

5. @Entry
6. @Component
7. struct Index {
8. build() {
9. Row() {
10. Column() {
11. Text("show dialog")
12. .fontSize(50)
13. .fontWeight(FontWeight.Bold)
14. .onClick(() => {
15. let ctx: UIContext | null = getDialogUIContext();
16. let interstitialDialogAction: InterstitialDialogAction = new InterstitialDialogAction({
17. uiContext: ctx as UIContext,
18. title: "主标题",
19. subtitle: "副标题",
20. titleColor: 'rgb(255, 192, 0)',
21. subtitleColor: Color.Red,
22. backgroundImage: $r('app.media.testBackgroundImg'),
23. foregroundImage: $r('app.media.testForegroundImg'),
24. iconStyle: IconStyle.DARK,
25. titlePosition: TitlePosition.TOP,
26. bottomOffsetType: BottomOffset.OFFSET_FOR_NONE,
27. onDialogClick: () => { console.info('outer dialog click action') },
28. onDialogClose: () => { console.info('outer close action') }
29. });
30. interstitialDialogAction.openDialog();
31. })
32. }
33. .width('100%')
34. }
35. .height('100%')
36. .backgroundColor('rgba(0, 0, 0, 0.1)')
37. }
38. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/EBmJyuUqQQ2r6dQ5yj0HNQ/zh-cn_image_0000002583440133.png?HW-CC-KV=V1&HW-CC-Date=20260428T000226Z&HW-CC-Expire=86400&HW-CC-Sign=4D88EE5311D81495D1B95B0F4449CB781102E07B43F5C4FC90EE423A0ABF897F)

### 示例2

为可选属性设置相应值，用两种不同参数类型分别为主标题，副标题设置颜色值，关闭按钮设置为亮色调，主副标题相对位置设置为主标题在副标题下方，底部距离类型设置为存在菜单栏情况下的距离。

```
1. // ../entryability/EntryAbility
2. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { window } from '@kit.ArkUI';
5. import { BusinessError } from '@kit.BasicServicesKit';

7. let dialogUIContext: UIContext | null = null;

9. export function getDialogUIContext(): UIContext | null {
10. if (getDialogUIContext === null) {
11. hilog.info(0x0000, 'testTag', '%{public}s', 'getDialogUIContext is null');
12. }
13. return dialogUIContext;
14. }

16. export default class EntryAbility extends UIAbility {
17. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
18. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
19. }

21. onDestroy(): void {
22. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
23. }

25. onWindowStageCreate(windowStage: window.WindowStage): void {
26. // Main window is created, set main page for this ability
27. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

29. windowStage.loadContent('pages/Index', (err) => {
30. if (err.code) {
31. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
32. return;
33. }
34. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
35. });

37. let windowClass: window.Window | undefined = undefined;
38. windowStage.getMainWindow((err: BusinessError, data) => {
39. let errCode: number = err.code;
40. if (errCode) {
41. console.error('Failed to obtain the main window. Cause: ' + JSON.stringify(err));
42. return;
43. }
44. windowClass = data;
45. console.info('Succeeded in obtaining the main window. Data: ' + JSON.stringify(data));
46. dialogUIContext = windowClass.getUIContext();
47. })

49. //获取窗口
50. windowStage.getMainWindow((err, data) => {
51. if (err.code) {
52. console.error('Failed to obtain the main window. Cause: ' + JSON.stringify(err));
53. return;
54. }
55. windowClass = data;
56. console.info('Succeeded in obtaining the main window. Data: ' + JSON.stringify(data));
57. //设置窗口全屏
58. windowClass.setWindowLayoutFullScreen(false)
59. })
60. }

62. onWindowStageDestroy(): void {
63. // Main window is destroyed, release UI related resources
64. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
65. }

67. onForeground(): void {
68. // Ability has brought to foreground
69. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
70. }

72. onBackground(): void {
73. // Ability has back to background
74. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
75. }
76. }
```

```
1. // Index.ets
2. import { getDialogUIContext } from '../entryability/EntryAbility';
3. import { UIContext, InterstitialDialogAction, IconStyle, TitlePosition, BottomOffset } from '@kit.ArkUI';

5. @Entry
6. @Component
7. struct Index {
8. build() {
9. Row() {
10. Column() {
11. Text("show dialog")
12. .fontSize(50)
13. .fontWeight(FontWeight.Bold)
14. .onClick(() => {
15. let ctx: UIContext | null = getDialogUIContext();
16. let interstitialDialogAction: InterstitialDialogAction = new InterstitialDialogAction({
17. uiContext: ctx as UIContext,
18. title: "主标题",
19. subtitle: "副标题",
20. titleColor: 'rgb(255, 192, 0)',
21. subtitleColor: Color.Red,
22. backgroundImage: $r('app.media.testBackgroundImg'),
23. foregroundImage: $r('app.media.testForegroundImg'),
24. iconStyle: IconStyle.LIGHT,
25. titlePosition: TitlePosition.BOTTOM,
26. bottomOffsetType: BottomOffset.OFFSET_FOR_BAR,
27. onDialogClick: () => { console.info('outer dialog click action') },
28. onDialogClose: () => { console.info('outer close action') }
29. });
30. interstitialDialogAction.openDialog();
31. })
32. }
33. .width('100%')
34. }
35. .height('100%')
36. .backgroundColor('rgba(0, 0, 0, 0.1)')
37. }
38. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/vrDep2MsRJ-7oIZysiulGA/zh-cn_image_0000002552960088.png?HW-CC-KV=V1&HW-CC-Date=20260428T000226Z&HW-CC-Expire=86400&HW-CC-Sign=94CC4E05355B5F51F560DDBA08C5369276800B934A4FDC7F9E32BB0500D64EC9)
