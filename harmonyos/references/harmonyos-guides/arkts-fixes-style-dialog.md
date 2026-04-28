---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-fixes-style-dialog
title: 固定样式弹出框
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用弹窗 > 弹出框 (Dialog) > 固定样式弹出框
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2fbec0dcb9da5487104bcb2ea64023866c0a1c3384256c9481dfd8ab7ca9bf01
---

固定样式弹出框采用固定的布局格式，这使得开发者无需关心具体的显示布局细节，只需输入所需显示的文本内容，从而简化了使用流程，提升了便捷性。

## 使用约束

* 可以通过调用UIContext或getUIContext，在非UI页面或某些异步回调中使用本文中的接口。CalendarPickerDialog当前不支持此操作。
* 操作菜单 (showActionMenu)、对话框 (showDialog)需先使用UIContext中的[getPromptAction()](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getpromptaction)方法获取到PromptAction对象，再通过该对象调用对应方法。
* 列表选择弹出框 (ActionSheet)、警告弹出框 (AlertDialog)、选择器弹出框 (PickerDialog)中除CalendarPickerDialog都需先使用ohos.window中的[getUIContext()](../harmonyos-references/arkts-apis-window-window.md#getuicontext10)方法获取UIContext实例，再通过此实例调用对应方法。或者可以通过自定义组件内置方法[getUIContext()](../harmonyos-references/ts-custom-component-api.md#getuicontext)获取。

操作菜单 (showActionMenu)、对话框 (showDialog)、列表选择弹出框 (ActionSheet)、警告弹出框 (AlertDialog)可以设置isModal为false变成非模态弹窗。

操作菜单 (showActionMenu)、对话框 (showDialog)、列表选择弹出框 (ActionSheet)和警告弹出框 (AlertDialog)不支持设置内容区的字体样式，如字体颜色、大小换行等操作，如需自定义样式，建议使用[不依赖UI组件的全局自定义弹出框](arkts-uicontext-custom-dialog.md)或者[基础自定义弹出框](arkts-common-components-custom-dialog.md)。

## 生命周期

弹出框提供了生命周期函数，用于通知用户该弹出框的生命周期。生命周期的触发时序依次为：onWillAppear -> onDidAppear -> onWillDisappear -> onDidDisappear，也可参照各组件API。

从API version 19开始，对话框（showDialog）、列表选择弹出框（ActionSheet）、警告弹出框（AlertDialog）支持以下生命周期。

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| onWillAppear | Callback<void> | 弹出框显示动效前的事件回调。 |
| onDidAppear | Callback<void> | 弹出框弹出后的事件回调。 |
| onWillDisappear | Callback<void> | 弹出框退出动效前的事件回调。 |
| onDidDisappear | Callback<void> | 弹出框消失后的事件回调。 |

## 操作菜单 (showActionMenu)

操作菜单通过UIContext中的getPromptAction方法获取到PromptAction对象，再通过该对象调用[showActionMenu](../harmonyos-references/arkts-apis-uicontext-promptaction.md#showactionmenu11)接口实现，支持在回调或开发者自定义类中使用。

操作菜单中，title字段的字体最大放大倍数为2。

创建并显示操作菜单后，菜单的响应结果会异步返回选中按钮在buttons数组中的索引。

```
1. import { PromptAction } from '@kit.ArkUI';

3. @Entry
4. @Component
5. export struct ShowActionMenuExample {
6. build() {
7. // ...
8. Column({ space: 12 }) {

10. Column() {
11. Button('ShowActionMenu')
12. .margin(30)
13. .onClick(() => {
14. let uiContext = this.getUIContext();
15. let promptAction: PromptAction = uiContext.getPromptAction();
16. try {
17. promptAction.showActionMenu({
18. title: 'showActionMenu Title Info',
19. buttons: [
20. {
21. text: 'item1',
22. color: '#666666'
23. },
24. {
25. text: 'item2',
26. color: '#000000'
27. },
28. ]
29. })
30. .then(data => {
31. console.info('showActionMenu success, click button: ' + data.index);
32. })
33. .catch((err: Error) => {
34. console.error('showActionMenu error: ' + err);
35. })
36. } catch (error) {
37. }
38. })
39. }.width('100%')
40. }
41. .width('100%')
42. .height('100%')
43. // ...
44. }
45. }
```

[ShowActionMenu.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/fixedstyledialog/ShowActionMenu.ets#L16-L72)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/sdcMxs-dTJq_xCoBCSuH-A/zh-cn_image_0000002552798254.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233942Z&HW-CC-Expire=86400&HW-CC-Sign=63AD1C96BECA96165CCD1C4A6E6F17E1794BCCEFE24FEA495E1F1741EE587595)

## 对话框 (showDialog)

对话框通过UIContext中的getPromptAction方法获取到PromptAction对象，再通过该对象调用[showDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#showdialog)接口实现，支持在回调或开发者自定义类中使用。

对话框中，title字段的字体最大放大倍数为2。

创建并显示对话框，对话框响应后异步返回选中按钮在buttons数组中的索引。

```
1. // xxx.ets
2. import { PromptAction } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. export struct ShowDialogExample {
8. build() {
9. // ...
10. Column({ space: 12 }) {
11. Column() {
12. Button('ShowDialog')
13. .margin(30)
14. .onClick(() => {
15. let uiContext = this.getUIContext();
16. let promptAction: PromptAction = uiContext.getPromptAction();
17. try {
18. promptAction.showDialog({
19. title: 'showDialog Title Info',
20. message: 'Message Info',
21. buttons: [
22. {
23. text: 'button1',
24. color: '#000000'
25. },
26. {
27. text: 'button2',
28. color: '#000000'
29. }
30. ]
31. }, (err, data) => {
32. if (err) {
33. console.error('showDialog err: ' + err);
34. return;
35. }
36. console.info('showDialog success callback, click button: ' + data.index);
37. });
38. } catch (error) {
39. let message = (error as BusinessError).message;
40. let code = (error as BusinessError).code;
41. console.error(`showdialog args error code is ${code}, message is ${message}`);
42. }
43. })
44. }.width('100%')
45. }
46. .width('100%')
47. .height('100%')
48. .padding({ left: 12, right: 12 })
49. // ...
50. }
51. }
```

[ShowDialog.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/fixedstyledialog/ShowDialog.ets#L15-L74)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/Hf5GlKYSSkK_R47mO4AIDA/zh-cn_image_0000002583437949.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233942Z&HW-CC-Expire=86400&HW-CC-Sign=9AEE59A171473FFF84DA6601BD5EB30A1B048F232903912505E26FC41AE19F5E)

## 选择器弹窗 (PickerDialog)

选择器弹窗通常用于在用户进行某些操作（如点击按钮）时显示特定的信息或选项。

### 日历选择器弹窗 (CalendarPickerDialog)

日历选择器弹窗提供日历视图，包含年、月和星期信息，通过[CalendarPickerDialog](../harmonyos-references/ts-methods-calendarpicker-dialog.md)接口实现。开发者可调用show函数，定义并弹出日历选择器弹窗。

日历选择器弹窗的弹出依赖UI的执行上下文，不可在[UI上下文不明确](arkts-global-interface.md#ui上下文不明确)的地方使用，具体约束参见[UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)说明。

通过配置[CalendarDialogOptions](../harmonyos-references/ts-methods-calendarpicker-dialog.md#calendardialogoptions对象说明)中的acceptButtonStyle、cancelButtonStyle属性可以实现自定义按钮样式。

```
1. // xxx.ets

3. @Entry
4. @Component
5. export struct CalendarDialog {
6. private selectedDate: Date = new Date('2024-04-23');

8. build() {
9. NavDestination() {
10. Column({ space: 12 }) {

12. Column() {
13. Button('Show CalendarPicker Dialog')
14. .margin(20)
15. .onClick(() => {
16. console.info('CalendarDialog.show');
17. CalendarPickerDialog.show({
18. selected: this.selectedDate,
19. acceptButtonStyle: {
20. fontColor: '#2787d9',
21. fontSize: '16fp',
22. backgroundColor: '#f7f7f7',
23. borderRadius: 10
24. },
25. cancelButtonStyle: {
26. fontColor: Color.Red,
27. fontSize: '16fp',
28. backgroundColor: '#f7f7f7',
29. borderRadius: 10
30. },
31. onAccept: (date: Date) => {
32. // 当弹出框再次弹出时显示选中的是上一次确定的日期
33. this.selectedDate = date;
34. }
35. })
36. })
37. }.width('100%')

39. }
40. .width('100%')
41. .height('100%')
42. .padding({ left: 12, right: 12 })
43. }
44. // ...
45. // 请将$r('app.string.CustomDialog_calender')替换为实际资源文件，在本示例中该资源文件的value值为"日历选择器弹窗"
46. .title($r('app.string.CustomDialog_calender'))
47. }
48. }
```

[CalendarPickerDialog.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/fixedstyledialog/CalendarPickerDialog.ets#L16-L68)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/Ydcdg1x9RJyM7sJ-m5w4tg/zh-cn_image_0000002552957904.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233942Z&HW-CC-Expire=86400&HW-CC-Sign=4328401C4F1865D26209C0E3CDA795148F10F5E31C683199DE622543443FB806)

### 日期滑动选择器弹窗 (DatePickerDialog)

开发者可以利用指定的日期范围，创建日期滑动选择器弹窗，将日期信息清晰地展示在弹出的窗口上。

日期滑动选择器弹窗通过UIContext中的[showDatePickerDialog](../harmonyos-references/arkts-apis-uicontext-uicontext.md#showdatepickerdialog)接口实现。

弹窗中配置[DatePickerDialogOptions](../harmonyos-references/ts-methods-datepicker-dialog.md#datepickerdialogoptions对象说明)的lunarSwitch、showTime属性为true时，会展示切换农历的开关和时间，当checkbox被选中时，会显示农历。当按下确定按钮时，弹窗会通过onDateAccept返回目前所选中的日期。如需弹窗再次弹出时显示选中的是上一次确定的日期，就要在回调中重新给selectTime进行赋值。

```
1. @Entry
2. @Component
3. export struct DatePickerDialogExample {
4. @State selectTime: Date = new Date('2023-12-25T08:30:00');

6. build() {
7. NavDestination() {
8. Column({ space: 12 }) {

10. Column() {
11. Button('showDatePickerDialog')
12. .margin(30)
13. .onClick(() => {
14. this.getUIContext().showDatePickerDialog({
15. start: new Date('2000-1-1'),
16. end: new Date('2100-12-31'),
17. selected: this.selectTime,
18. lunarSwitch: true,
19. showTime: true,
20. onDateAccept: (value: Date) => {
21. this.selectTime = value;
22. console.info('DatePickerDialog:onAccept()' + JSON.stringify(value));
23. },
24. })
25. })
26. }.width('100%').margin({ top: 5 })

28. }
29. .width('100%')
30. .height('100%')
31. .padding({ left: 12, right: 12 })
32. }
33. // ...
34. }
35. }
```

[DatePickerDialog.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/fixedstyledialog/DatePickerDialog.ets#L16-L57)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/2rieIvw2R6y07OKVCuh3fA/zh-cn_image_0000002583477905.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233942Z&HW-CC-Expire=86400&HW-CC-Sign=4F4A61C698CD0AC89F0C030B50FD767E1D1106A0F5291D51B2F0EEC9F79282C4)

该示例通过配置disappearTextStyle、textStyle、selectedTextStyle、acceptButtonStyle、cancelButtonStyle实现了自定义文本以及按钮样式。

```
1. @Entry
2. @Component
3. export struct DatePickerCustomDialogExample {
4. @State selectTime: Date = new Date('2023-12-25T08:30:00');

6. build() {
7. NavDestination() {
8. Column() {
9. Button('showDatePickerDialog')
10. .margin(30)
11. .onClick(() => {
12. this.getUIContext().showDatePickerDialog({
13. start: new Date('2000-1-1'),
14. end: new Date('2100-12-31'),
15. selected: this.selectTime,
16. textStyle: { color: '#2787d9', font: { size: '14fp', weight: FontWeight.Normal } },
17. selectedTextStyle: { color: '#004aaf', font: { size: '18fp', weight: FontWeight.Regular } },
18. acceptButtonStyle: {
19. fontColor: '#2787d9',
20. fontSize: '16fp',
21. backgroundColor: '#f7f7f7',
22. borderRadius: 10
23. },
24. cancelButtonStyle: {
25. fontColor: Color.Red,
26. fontSize: '16fp',
27. backgroundColor: '#f7f7f7',
28. borderRadius: 10
29. }
30. })
31. })
32. }.width('100%').margin({ top: 5 })
33. }
34. // ...
35. }
36. }
```

[DatePickerCustomDialog.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/fixedstyledialog/DatePickerCustomDialog.ets#L17-L59)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/WXgjPkhmStywyTKnG5WcaA/zh-cn_image_0000002552798256.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233942Z&HW-CC-Expire=86400&HW-CC-Sign=A6479F05A5D5B72999272455D7D6B9C22E97ED4CC1EB7E27DDE2A56629DB3101)

### 时间滑动选择器弹窗 (TimePickerDialog)

开发者可根据24小时的时间区间，创建时间滑动选择器弹窗，将时间信息清晰地展示在弹出的窗口上。

时间滑动选择器弹窗通过UIContext中的[showTimePickerDialog](../harmonyos-references/arkts-apis-uicontext-uicontext.md#showtimepickerdialog)接口实现。

该示例通过配置[disappearTextStyle](../harmonyos-references/ts-basic-components-timepicker.md#disappeartextstyle10)、[textStyle](../harmonyos-references/ts-basic-components-timepicker.md#textstyle10)、[selectedTextStyle](../harmonyos-references/ts-basic-components-timepicker.md#selectedtextstyle10)、[acceptButtonStyle](../harmonyos-references/ts-methods-timepicker-dialog.md#timepickerdialogoptions对象说明)、[cancelButtonStyle](../harmonyos-references/ts-methods-timepicker-dialog.md#timepickerdialogoptions对象说明)实现了自定义文本以及按钮样式。

```
1. // xxx.ets

3. @Entry
4. @Component
5. export struct TimePickerDialogExample {
6. @State selectTime: Date = new Date('2023-12-25T08:30:00');

8. build() {
9. NavDestination() {
10. Column({ space: 12 }) {

12. Column() {
13. Button('showTimePickerDialog')
14. .margin(30)
15. .onClick(() => {
16. this.getUIContext().showTimePickerDialog({
17. selected: this.selectTime,
18. textStyle: { color: '#2787d9', font: { size: '14fp', weight: FontWeight.Normal } },
19. selectedTextStyle: { color: '#004aaf', font: { size: '18fp', weight: FontWeight.Regular } },
20. acceptButtonStyle: {
21. fontColor: '#2787d9',
22. fontSize: '16fp',
23. backgroundColor: '#f7f7f7',
24. borderRadius: 10
25. },
26. cancelButtonStyle: {
27. fontColor: Color.Red,
28. fontSize: '16fp',
29. backgroundColor: '#f7f7f7',
30. borderRadius: 10
31. }
32. })
33. })
34. }.width('100%').margin({ top: 5 })
35. }
36. // ...
37. }
38. // ...
39. }
40. }
```

[TimePickerDialog.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/fixedstyledialog/TimePickerDialog.ets#L16-L65)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/tDQ_1pCMStehJsjf2U63nQ/zh-cn_image_0000002583437951.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233942Z&HW-CC-Expire=86400&HW-CC-Sign=EE43CA2EB5C7EEB56F21168EF2DED1EFD40B9ED94027B33B386A4E8A81575591)

### 文本滑动选择器弹窗 (TextPickerDialog)

开发者可根据指定的选择范围，创建文本滑动选择器弹窗，将文本信息清晰地展示在弹出的窗口上。

文本滑动选择器弹窗通过UIContext中的[showTextPickerDialog](../harmonyos-references/arkts-apis-uicontext-uicontext.md#showtextpickerdialog)接口实现。

该示例通过设置range的参数类型为TextCascadePickerRangeContent[]，实现3列文本选择器弹窗。当按下确定按钮时，弹窗会通过onAccept返回目前所选中文本和索引值。如需弹窗再次弹出时显示选中的是上一次确定的文本，就要在回调中重新给select进行赋值。

```
1. @Entry
2. @Component
3. export struct TextPickerCNDialogExample {
4. private fruits: TextCascadePickerRangeContent[] = [
5. {
6. text: '辽宁省',
7. children: [{ text: '沈阳市', children: [{ text: '沈河区' }, { text: '和平区' }, { text: '浑南区' }] },
8. { text: '大连市', children: [{ text: '中山区' }, { text: '金州区' }, { text: '长海县' }] }]
9. },
10. {
11. text: '吉林省',
12. children: [{ text: '长春市', children: [{ text: '南关区' }, { text: '宽城区' }, { text: '朝阳区' }] },
13. { text: '四平市', children: [{ text: '铁西区' }, { text: '铁东区' }, { text: '梨树县' }] }]
14. },
15. {
16. text: '黑龙江省',
17. children: [{ text: '哈尔滨市', children: [{ text: '道里区' }, { text: '道外区' }, { text: '南岗区' }] },
18. { text: '牡丹江市', children: [{ text: '东安区' }, { text: '西安区' }, { text: '爱民区' }] }]
19. }
20. ];
21. private select: number = 0;

23. build() {
24. // ···
25. Column() {
26. Button('showTextPickerDialog')
27. // ···
28. .margin(30)
29. .onClick(() => {
30. this.getUIContext().showTextPickerDialog({
31. range: this.fruits,
32. selected: this.select,
33. onAccept: (value: TextPickerResult) => {
34. this.select = value.index as number
35. }
36. });
37. })
38. }.width('100%').margin({ top: 5 })
39. // ···
40. }
41. }
```

[TextPickerCNDialog.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/fixedstyledialog/TextPickerCNDialog.ets#L16-L65)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/_VrM5bO2QtSYN44MqvYv-A/zh-cn_image_0000002552957906.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233942Z&HW-CC-Expire=86400&HW-CC-Sign=7889DDCFB0B298CA1F2666B149EE713D6C96F83313477097D003519A568B7E62)

## 列表选择弹窗 (ActionSheet)

列表选择器弹窗适用于呈现多个操作选项，尤其当界面中仅需展示操作列表而无其他内容时。

列表选择器弹窗通过UIContext中的[showActionSheet](../harmonyos-references/arkts-apis-uicontext-uicontext.md#showactionsheet)接口实现。

列表选择弹窗中，title字段的字体最大放大倍数为2。

该示例通过配置width、height、transition等接口，定义了弹窗的样式以及弹出动效。

```
1. @Entry
2. @Component
3. export struct showActionSheetExample {

5. build() {
6. NavDestination() {
7. Column({ space: 12 }) {

9. Column() {
10. Button('showActionSheet')
11. .margin(30)
12. .onClick(() => {
13. this.getUIContext().showActionSheet({
14. title: 'ActionSheet title',
15. message: 'message',
16. autoCancel: false,
17. width: 300,
18. height: 300,
19. cornerRadius: 20,
20. borderWidth: 1,
21. borderStyle: BorderStyle.Solid,
22. borderColor: Color.Blue,
23. backgroundColor: Color.White,
24. transition: TransitionEffect.asymmetric(TransitionEffect.OPACITY
25. .animation({ duration: 3000, curve: Curve.Sharp })
26. .combine(TransitionEffect.scale({ x: 1.5, y: 1.5 })
27. .animation({ duration: 3000, curve: Curve.Sharp })),
28. TransitionEffect.OPACITY.animation({ duration: 100, curve: Curve.Smooth })
29. .combine(TransitionEffect.scale({ x: 0.5, y: 0.5 })
30. .animation({ duration: 100, curve: Curve.Smooth }))),
31. confirm: {
32. value: 'Confirm button',
33. action: () => {
34. console.info('Get Alert Dialog handled');
35. }
36. },
37. alignment: DialogAlignment.Center,
38. sheets: [
39. {
40. title: 'apples',
41. action: () => {
42. }
43. },
44. {
45. title: 'bananas',
46. action: () => {
47. }
48. },
49. {
50. title: 'pears',
51. action: () => {
52. console.info('pears');
53. }
54. }
55. ]
56. })
57. })
58. }.width('100%').margin({ top: 5 })

60. }
61. .width('100%')
62. .height('100%')
63. .padding({ left: 12, right: 12 })
64. }
65. .backgroundColor('#f1f2f3')
66. // 请将$r('app.string.CustomDialog_ActionSheet')替换为实际资源文件，在本示例中该资源文件的value值为"列表选择弹窗"
67. .title($r('app.string.CustomDialog_ActionSheet'))
68. }
69. }
```

[ActionSheet.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/fixedstyledialog/ActionSheet.ets#L16-L86)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/Cfhhq0MiSpeoDUvg_bkMLQ/zh-cn_image_0000002583477907.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233942Z&HW-CC-Expire=86400&HW-CC-Sign=26123E374F5443C959E2CF1D4E1649DFCE9ABA7D16C10049C079B1C7D249C1D6)

## 警告弹窗 (AlertDialog)

向用户提问或得到用户的许可时，使用警告弹窗。

* 警告弹窗用来提示重要信息，但会中断当前任务，尽量提供必要的信息和有用的操作。
* 避免仅使用警告弹窗提供信息，用户不喜欢被信息丰富但不可操作的警告打断。

警告弹窗通过UIContext中的[showAlertDialog](../harmonyos-references/arkts-apis-uicontext-uicontext.md#showalertdialog)接口实现。

警告弹窗中，title和subtitle字段的字体最大放大倍数为2。

该示例通过配置width、height、transition等接口，定义了多个按钮弹窗的样式以及弹出动效。

```
1. import { PromptAction } from '@kit.ArkUI';

3. @Entry
4. @Component
5. export struct showAlertDialogExample {
6. build() {
7. NavDestination() {
8. Column({ space: 12 }) {

10. Column() {
11. Button('showAlertDialog')
12. .margin(30)
13. .onClick(() => {
14. this.getUIContext().showAlertDialog(
15. {
16. title: 'title',
17. message: 'text',
18. autoCancel: true,
19. alignment: DialogAlignment.Center,
20. offset: { dx: 0, dy: -20 },
21. gridCount: 3,
22. transition: TransitionEffect.asymmetric(TransitionEffect.OPACITY
23. .animation({ duration: 3000, curve: Curve.Sharp })
24. .combine(TransitionEffect.scale({ x: 1.5, y: 1.5 })
25. .animation({ duration: 3000, curve: Curve.Sharp })),
26. TransitionEffect.OPACITY.animation({ duration: 100, curve: Curve.Smooth })
27. .combine(TransitionEffect.scale({ x: 0.5, y: 0.5 })
28. .animation({ duration: 100, curve: Curve.Smooth }))),
29. buttons: [{
30. value: 'cancel',
31. action: () => {
32. console.info('Callback when the first button is clicked');
33. }
34. },
35. {
36. enabled: true,
37. defaultFocus: true,
38. style: DialogButtonStyle.HIGHLIGHT,
39. value: 'ok',
40. action: () => {
41. console.info('Callback when the second button is clicked');
42. }
43. }],
44. }
45. )
46. })
47. }.width('100%').margin({ top: 5 })

49. }
50. .width('100%')
51. .height('100%')
52. .padding({ left: 12, right: 12 })
53. }
54. .backgroundColor('#f1f2f3')
55. // 请将$r('app.string.CustomDialog_AlertDialog')替换为实际资源文件，在本示例中该资源文件的value值为"警告弹窗"
56. .title($r('app.string.CustomDialog_AlertDialog'))
57. }
58. }
```

[AlertDialog.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/fixedstyledialog/AlertDialog.ets#L16-L76)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/sEjZt6G7Sy6I2Wkd8h8Xdw/zh-cn_image_0000002552798258.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233942Z&HW-CC-Expire=86400&HW-CC-Sign=58792690D4F08C8F1A4CE4102B992D1F2CD8AA94CAB3988E43A16BC444DC04EF)
