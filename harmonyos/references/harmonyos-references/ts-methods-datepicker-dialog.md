---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-datepicker-dialog
title: 日期滑动选择器弹窗 (DatePickerDialog)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 弹窗 > 日期滑动选择器弹窗 (DatePickerDialog)
category: harmonyos-references
scraped_at: 2026-04-28T08:02:23+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:9b270dce37b7e5de2eac3f5687e9d5972cac848037433cc68a4e4a720a088c3a
---

根据指定的日期范围创建日期滑动选择器并展示在弹窗上。

说明

* 该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本模块功能依赖UI的执行上下文，不可在[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的地方使用，参见[UIContext](arkts-apis-uicontext-uicontext.md)说明。
* 本模块不支持深浅色模式热更新，如果需要进行深浅色模式切换，请重新打开弹窗。
* 最大显示行数在横、竖屏模式下存在差异。竖屏时默认为5行，横屏时依赖系统配置，未配置时默认显示为3行。可通过如下参数查看具体配置值$r('sys.float.ohos\_id\_picker\_show\_count\_landscape')。

## DatePickerDialog

PhonePC/2in1TabletTVWearable

### show(deprecated)

PhonePC/2in1TabletTVWearable

static show(options?: DatePickerDialogOptions)

定义日期滑动选择器弹窗并弹出。

说明

从API version 8开始支持，从API version 18开始废弃，建议使用[showDatePickerDialog](arkts-apis-uicontext-uicontext.md#showdatepickerdialog)替代。showDatePickerDialog需先获取[UIContext](arkts-apis-uicontext-uicontext.md)实例后再进行调用。

从API version 10开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[showDatePickerDialog](arkts-apis-uicontext-uicontext.md#showdatepickerdialog)来明确UI的执行上下文。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [DatePickerDialogOptions](ts-methods-datepicker-dialog.md#datepickerdialogoptions对象说明) | 否 | 配置日期选择器弹窗的参数。 |

## DatePickerDialogOptions对象说明

PhonePC/2in1TabletTVWearable

日期选择器弹窗选项。

继承自[DatePickerOptions](ts-basic-components-datepicker.md#datepickeroptions对象说明)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| lunar | boolean | 否 | 是 | 日期是否显示为农历。  - true：显示为农历。  - false：不显示为农历。  默认值：false  **说明：**  仅在简体中文和繁体中文语言环境下生效，其他语言环境下设置该属性无效果。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| showTime10+ | boolean | 否 | 是 | 是否在弹窗内展示时间选择器。  - true：展示时间选择器。  - false：不展示时间选择器。  默认值：false  **说明：**  1. 当showTime为true时，点击弹窗的标题日期可以在"日期选择器"和"日期选择器+时间选择器"两个页面中切换。  2. 当showTime为true时，mode参数不生效，"日期选择器"页面显示默认年、月、日三列。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| useMilitaryTime10+ | boolean | 否 | 是 | 弹窗内展示的时间选择器是否为24小时制，仅当showTime为true时生效。  - true：显示24小时制。  - false：显示12小时制。  默认值：false  **说明：**  当展示的时间选择器为12小时制时，上午和下午的标识不会根据小时数自动切换。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| lunarSwitch10+ | boolean | 否 | 是 | 是否展示切换农历的开关。  - true：展示切换农历的开关。  - false：不展示切换农历的开关。  默认值：false  **说明：**  开关打开后，仅在简体中文和繁体中文环境下生效，在其他语言环境农历不生效。因此建议在其他语言环境设置为不展示开关。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| lunarSwitchStyle14+ | [LunarSwitchStyle](ts-methods-datepicker-dialog.md#lunarswitchstyle14对象说明) | 否 | 是 | 设置农历开关的颜色样式。  默认值：{  selectedColor: $r('sys.color.ohos\_id\_color\_text\_primary\_actived'),  unselectedColor: $r('sys.color.ohos\_id\_color\_switch\_outline\_off'),  strokeColor: Color.White  }  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| disappearTextStyle10+ | [PickerTextStyle](ts-picker-common.md#pickertextstyle对象说明) | 否 | 是 | 设置边缘项（以选中项为基准向上或向下的第二项）的文本颜色、字号、字体粗细。  默认值：  {  color: '#ff182431',  font: {  size: '14fp',  weight: FontWeight.Regular  }  }  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| textStyle10+ | [PickerTextStyle](ts-picker-common.md#pickertextstyle对象说明) | 否 | 是 | 设置待选项（以选中项为基准向上或向下的第一项）的文本颜色、字号、字体粗细。  默认值：  {  color: '#ff182431',  font: {  size: '16fp',  weight: FontWeight.Regular  }  }  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| selectedTextStyle10+ | [PickerTextStyle](ts-picker-common.md#pickertextstyle对象说明) | 否 | 是 | 设置选中项的文本颜色、字号、字体粗细。  默认值：  {  color: '#ff007dff',  font: {  size: '20fp',  weight: FontWeight.Medium  }  }  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| acceptButtonStyle12+ | [PickerDialogButtonStyle](ts-picker-common.md#pickerdialogbuttonstyle12对象说明) | 否 | 是 | 设置确认按钮显示样式、样式和重要程度、角色、背景色、圆角、文本颜色、字号、字体粗细、字体样式、字体列表、按钮是否默认响应Enter键。  **说明：**  1.acceptButtonStyle与cancelButtonStyle中最多只能有一个primary字段配置为true，如果同时设置为true，则primary字段不生效，保持默认值false。  2.按钮高度默认40vp，在关怀模式-大字体场景下高度不变，即使按钮样式设置为圆角矩形[ROUNDED\_RECTANGLE](ts-basic-components-button.md#buttontype枚举说明)，呈现效果依然是胶囊型按钮[Capsule](ts-basic-components-button.md#buttontype枚举说明)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| cancelButtonStyle12+ | [PickerDialogButtonStyle](ts-picker-common.md#pickerdialogbuttonstyle12对象说明) | 否 | 是 | 设置取消按钮显示样式、样式和重要程度、角色、背景色、圆角、文本颜色、字号、字体粗细、字体样式、字体列表、按钮是否默认响应Enter键。  **说明：**  1.acceptButtonStyle与cancelButtonStyle中最多只能有一个primary字段配置为true，如果同时设置为true，则primary字段不生效，保持默认值false。  2.按钮高度默认40vp，在关怀模式-大字体场景下高度不变，即使按钮样式设置为圆角矩形[ROUNDED\_RECTANGLE](ts-basic-components-button.md#buttontype枚举说明)，呈现效果依然是胶囊型按钮[Capsule](ts-basic-components-button.md#buttontype枚举说明)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| alignment10+ | [DialogAlignment](ts-methods-alert-dialog-box.md#dialogalignment枚举说明) | 否 | 是 | 弹窗在竖直方向上的对齐方式。  默认值：DialogAlignment.Default  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| offset10+ | [Offset](ts-types.md#offset) | 否 | 是 | 弹窗相对alignment所在位置的偏移量。  默认值：{ dx: 0 , dy: 0 }  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| maskRect10+ | [Rectangle](ts-methods-alert-dialog-box.md#rectangle8类型说明) | 否 | 是 | 弹窗遮蔽层区域，在遮蔽层区域内的事件不透传，在遮蔽层区域外的事件透传。  默认值：{ x: 0, y: 0, width: '100%', height: '100%' }  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| onAccept(deprecated) | (value: [DatePickerResult](ts-basic-components-datepicker.md#datepickerresult对象说明)) => void | 否 | 是 | 点击弹窗中的“确定”按钮时触发该回调。  **说明：**  从API version 8 开始支持，从 API version 10 开始废弃。建议使用onDateAccept。 |
| onCancel | [VoidCallback](ts-types.md#voidcallback12) | 否 | 是 | 点击弹窗中的“取消”按钮时触发该回调。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| onChange(deprecated) | (value: [DatePickerResult](ts-basic-components-datepicker.md#datepickerresult对象说明)) => void | 否 | 是 | 滑动弹窗中的滑动选择器使当前选中项改变时触发该回调。  **说明：**  从API version 8 开始支持，从 API version 10 开始废弃。建议使用onDateChange。 |
| onDateAccept10+ | [Callback](ts-types.md#callback12)<Date> | 否 | 是 | 点击弹窗中的“确定”按钮时触发该回调。  **说明：**  当showTime设置为true时，回调接口返回值value中时和分为选择器选择的时和分。否则，返回值value中时和分为系统时间的时和分。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| onDateChange10+ | [Callback](ts-types.md#callback12)<Date> | 否 | 是 | 滑动弹窗中的日期使当前选中项改变时触发该回调。  **说明：**  当showTime设置为true时，回调接口返回值value中时和分为选择器选择的时和分。否则，返回值value中时和分为系统时间的时和分。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| backgroundColor11+ | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 弹窗背板颜色。  默认值：Color.Transparent  **说明：**  当设置了backgroundColor为非透明色时，backgroundBlurStyle需要设置为BlurStyle.NONE，否则显示的颜色将不符合预期效果。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundBlurStyle11+ | [BlurStyle](ts-universal-attributes-background.md#blurstyle9) | 否 | 是 | 弹窗背板模糊材质。  默认值：BlurStyle.COMPONENT\_ULTRA\_THICK  **说明：**  设置为BlurStyle.NONE关闭背景虚化。设置backgroundBlurStyle为非NONE值时，不要设置backgroundColor，否则显示的颜色将不符合预期效果。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundBlurStyleOptions19+ | [BackgroundBlurStyleOptions](ts-universal-attributes-background.md#backgroundblurstyleoptions10对象说明) | 否 | 是 | 背景模糊效果。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| backgroundEffect19+ | [BackgroundEffectOptions](ts-universal-attributes-background.md#backgroundeffectoptions11) | 否 | 是 | 背景效果参数。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| onDidAppear12+ | [VoidCallback](ts-types.md#voidcallback12) | 否 | 是 | 弹窗弹出后的事件回调。  **说明：**  1.正常时序为：onWillAppear>>onDidAppear>>(onDateAccept/onCancel/onDateChange)>>onWillDisappear>>onDidDisappear。  2.在onDidAppear内设置改变弹窗显示效果的回调事件。二次弹出生效。  3.快速点击弹出，消失弹窗时，存在onWillDisappear在onDidAppear前生效。  4. 当弹窗入场动效未完成时关闭弹窗，该回调不会触发。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onDidDisappear12+ | [VoidCallback](ts-types.md#voidcallback12) | 否 | 是 | 弹窗消失后的事件回调。  **说明：**  1.正常时序为：onWillAppear>>onDidAppear>>(onDateAccept/onCancel/onDateChange)>>onWillDisappear>>onDidDisappear。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onWillAppear12+ | [VoidCallback](ts-types.md#voidcallback12) | 否 | 是 | 弹窗显示动效前的事件回调。  **说明：**  1.正常时序为：onWillAppear>>onDidAppear>>(onDateAccept/onCancel/onDateChange)>>onWillDisappear>>onDidDisappear。  2.在onWillAppear内设置改变弹窗显示效果的回调事件。二次弹出生效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onWillDisappear12+ | [VoidCallback](ts-types.md#voidcallback12) | 否 | 是 | 弹窗退出动效前的事件回调。  **说明：**  1.正常时序为：onWillAppear>>onDidAppear>>(onDateAccept/onCancel/onDateChange)>>onWillDisappear>>onDidDisappear。  2.快速点击弹出，消失弹窗时，存在onWillDisappear在onDidAppear前生效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| shadow12+ | [ShadowOptions](ts-universal-attributes-image-effect.md#shadowoptions对象说明) | [ShadowStyle](ts-universal-attributes-image-effect.md#shadowstyle10枚举说明) | 否 | 是 | 设置弹窗背板的阴影。  当设备为2in1时，默认场景下获焦阴影值为ShadowStyle.OUTER\_FLOATING\_MD，失焦为ShadowStyle.OUTER\_FLOATING\_SM。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| dateTimeOptions12+ | [DateTimeOptions](js-apis-intl.md#datetimeoptionsdeprecated) | 否 | 是 | 设置时分是否显示前导0，目前只支持设置hour和minute参数。  默认值：  hour: 24小时制默认为"2-digit"，设置hour是否按照2位数字显示，如果实际数值小于10，则会补充前导0并显示，即为"0X"；12小时制默认为"numeric"，即没有前导0。  minute: 默认为"2-digit"，设置minute是否按照2位数字显示，如果实际数值小于10，则会补充前导0并显示，即为"0X"。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| enableHoverMode14+ | boolean | 否 | 是 | 是否响应悬停态。  - true：响应悬停态。  - false：不响应悬停态。  默认值：false  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| hoverModeArea14+ | [HoverModeAreaType](ts-universal-attributes-sheet-transition.md#hovermodeareatype14) | 否 | 是 | 悬停态下弹窗默认展示区域。  默认值：HoverModeAreaType.BOTTOM\_SCREEN  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| enableHapticFeedback18+ | boolean | 否 | 是 | 设置是否开启触控反馈。  - true：开启触控反馈。  - false：不开启触控反馈。  默认值：true  **元服务API**： 从API version 18开始，该接口支持在元服务中使用。  **说明**：  1. 设置为true后，其生效情况取决于系统的硬件是否支持。  2. 开启触控反馈时，需要在工程的src/main/module.json5文件的"module"内配置requestPermissions字段开启振动权限，配置如下：  "requestPermissions": [{"name": "ohos.permission.VIBRATE"}] |
| canLoop20+ | boolean | 否 | 是 | 设置是否可循环滚动。  默认值：true  **说明：**  true：可循环，年份随着月份的循环滚动进行联动加减，月份随着日的循环滚动进行联动加减。  false：不可循环，年、月、日到达本列的顶部或底部时，无法再进行滚动，年、月、日之间也无法再联动加减。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## LunarSwitchStyle14+对象说明

PhonePC/2in1TabletTVWearable

定义了DatePickerDialog组件中农历切换开关的样式。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| selectedColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 设置开关开启时开关的背景颜色。  默认值：$r('sys.color.ohos\_id\_color\_text\_primary\_actived')。 |
| unselectedColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 设置开关未开启时开关的边框颜色。  默认值：$r('sys.color.ohos\_id\_color\_switch\_outline\_off')。 |
| strokeColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 设置开关内部图标颜色。  默认值：Color.White。 |

## 示例

PhonePC/2in1TabletTVWearable

说明

推荐通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[showDatePickerDialog](arkts-apis-uicontext-uicontext.md#showdatepickerdialog)来明确UI的执行上下文。

### 示例1（设置显示时间）

该示例通过showTime、useMilitaryTime、dateTimeOptions设置显示时间。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct DatePickerDialogExample {
5. selectedDate: Date = new Date('2010-01-01');

7. build() {
8. Column() {
9. Button('DatePickerDialog')
10. .margin(20)
11. .onClick(() => {
12. this.getUIContext().showDatePickerDialog({
13. start: new Date('2000-01-01'),
14. end: new Date('2100-12-31'),
15. selected: this.selectedDate,
16. showTime: true,
17. useMilitaryTime: false,
18. dateTimeOptions: { hour: "numeric", minute: "2-digit" },
19. onDateAccept: (value: Date) => {
20. // 保存按下确定按钮时的日期，这样当弹窗再次弹出时显示选中的是上一次确定的日期
21. this.selectedDate = value;
22. console.info('DatePickerDialog:onDateAccept()' + value.toString());
23. },
24. onCancel: () => {
25. console.info('DatePickerDialog:onCancel()');
26. },
27. onDateChange: (value: Date) => {
28. console.info('DatePickerDialog:onDateChange()' + value.toString());
29. },
30. onDidAppear: () => {
31. console.info('DatePickerDialog:onDidAppear()');
32. },
33. onDidDisappear: () => {
34. console.info('DatePickerDialog:onDidDisappear()');
35. },
36. onWillAppear: () => {
37. console.info('DatePickerDialog:onWillAppear()');
38. },
39. onWillDisappear: () => {
40. console.info('DatePickerDialog:onWillDisappear()');
41. }
42. })
43. })
44. }.width('100%')
45. }
46. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/F_aKbS0-THyuW9qs-q3dSQ/zh-cn_image_0000002552960052.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000220Z&HW-CC-Expire=86400&HW-CC-Sign=3CAE600E342B1177BD822A7CF91BC882A18CADFE172A84702575AE2F8193BA77)

### 示例2（自定义样式）

该示例通过配置disappearTextStyle、textStyle、selectedTextStyle、acceptButtonStyle、cancelButtonStyle实现了自定义文本以及按钮样式。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct DatePickerDialogExample {
5. selectedDate: Date = new Date('2010-01-01');

7. build() {
8. Column() {
9. Button('DatePickerDialog')
10. .margin(20)
11. .onClick(() => {
12. this.getUIContext().showDatePickerDialog({
13. start: new Date('2000-01-01'),
14. end: new Date('2100-12-31'),
15. selected: this.selectedDate,
16. disappearTextStyle: { color: '#297bec', font: { size: '20fp', weight: FontWeight.Bold } },
17. textStyle: { color: Color.Black, font: { size: '18fp', weight: FontWeight.Normal } },
18. selectedTextStyle: { color: Color.Blue, font: { size: '26fp', weight: FontWeight.Regular } },
19. acceptButtonStyle: {
20. type: ButtonType.Normal,
21. style: ButtonStyleMode.NORMAL,
22. role: ButtonRole.NORMAL,
23. fontColor: 'rgb(81, 81, 216)',
24. fontSize: '26fp',
25. fontWeight: FontWeight.Bolder,
26. fontStyle: FontStyle.Normal,
27. fontFamily: 'sans-serif',
28. backgroundColor: '#A6ACAF',
29. borderRadius: 20
30. },
31. cancelButtonStyle: {
32. type: ButtonType.Normal,
33. style: ButtonStyleMode.NORMAL,
34. role: ButtonRole.NORMAL,
35. fontColor: Color.Blue,
36. fontSize: '16fp',
37. fontWeight: FontWeight.Normal,
38. fontStyle: FontStyle.Italic,
39. fontFamily: 'sans-serif',
40. backgroundColor: '#50182431',
41. borderRadius: 10
42. },
43. onDateAccept: (value: Date) => {
44. // 保存按下确定按钮时的日期，这样当弹窗再次弹出时显示选中的是上一次确定的日期
45. this.selectedDate = value;
46. console.info('DatePickerDialog:onDateAccept()' + value.toString());
47. },
48. onCancel: () => {
49. console.info('DatePickerDialog:onCancel()');
50. },
51. onDateChange: (value: Date) => {
52. console.info('DatePickerDialog:onDateChange()' + value.toString());
53. },
54. onDidAppear: () => {
55. console.info('DatePickerDialog:onDidAppear()');
56. },
57. onDidDisappear: () => {
58. console.info('DatePickerDialog:onDidDisappear()');
59. },
60. onWillAppear: () => {
61. console.info('DatePickerDialog:onWillAppear()');
62. },
63. onWillDisappear: () => {
64. console.info('DatePickerDialog:onWillDisappear()');
65. }
66. });
67. })
68. }.width('100%')
69. }
70. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/PUXtrDUhSBSJaVKGlrnbYg/zh-cn_image_0000002583480053.png?HW-CC-KV=V1&HW-CC-Date=20260428T000220Z&HW-CC-Expire=86400&HW-CC-Sign=0923D93F8B84F35123B8C2F790B0D6ECEE2E318DC22FA761396FFCF38441AD99)

说明

如需完全自定义实现日期滑动选择器弹窗，可以通过先使用[自定义弹窗 (CustomDialog)](ts-methods-custom-dialog-box.md)，然后使用[DatePicker](ts-basic-components-datepicker.md)组件来实现。

### 示例3（悬停态弹窗）

该示例展示了在折叠屏悬停态下设置dialog布局区域的效果。

```
1. @Entry
2. @Component
3. struct DatePickerDialogExample {
4. selectedDate: Date = new Date('2010-01-01');

6. build() {
7. Column() {
8. Button('DatePickerDialog')
9. .margin(20)
10. .onClick(() => {
11. this.getUIContext().showDatePickerDialog({
12. start: new Date('2000-01-01'),
13. end: new Date('2100-12-31'),
14. selected: this.selectedDate,
15. showTime: true,
16. useMilitaryTime: false,
17. disappearTextStyle: { color: Color.Pink, font: { size: '22fp', weight: FontWeight.Bold }},
18. textStyle: { color: '#ff00ff00', font: { size: '18fp', weight: FontWeight.Normal }},
19. selectedTextStyle: { color: '#ff182431', font: { size: '14fp', weight: FontWeight.Regular }},
20. onDateAccept: (value: Date) => {
21. // 保存按下确定按钮时的日期，这样当弹窗再次弹出时显示选中的是上一次确定的日期
22. this.selectedDate = value;
23. console.info('DatePickerDialog:onDateAccept()' + value.toString());
24. },
25. onCancel: () => {
26. console.info('DatePickerDialog:onCancel()');
27. },
28. onDateChange: (value: Date) => {
29. console.info('DatePickerDialog:onDateChange()' + value.toString());
30. },
31. onDidAppear: () => {
32. console.info('DatePickerDialog:onDidAppear()');
33. },
34. onDidDisappear: () => {
35. console.info('DatePickerDialog:onDidDisappear()');
36. },
37. onWillAppear: () => {
38. console.info('DatePickerDialog:onWillAppear()');
39. },
40. onWillDisappear: () => {
41. console.info('DatePickerDialog:onWillDisappear()');
42. },
43. enableHoverMode: true,
44. hoverModeArea: HoverModeAreaType.TOP_SCREEN
45. });
46. })
47. }.width('100%')
48. }
49. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/ogCc1Kn2Qv6w8mcdiP54-A/zh-cn_image_0000002552800404.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000220Z&HW-CC-Expire=86400&HW-CC-Sign=D8C22A98326F6C49724563F3124A7FCC50A4F592EC790DCA21A43550130D0897)

### 示例4（设置弹窗位置）

该示例通过alignment、offset设置弹窗的位置。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct DatePickerDialogExample {
5. selectedDate: Date = new Date('2010-01-01');

7. build() {
8. Column() {
9. Button('DatePickerDialog')
10. .margin(20)
11. .onClick(() => {
12. this.getUIContext().showDatePickerDialog({
13. start: new Date('2000-01-01'),
14. end: new Date('2100-12-31'),
15. selected: this.selectedDate,
16. alignment: DialogAlignment.Center,
17. offset: { dx: 20, dy: 0 },
18. onDateAccept: (value: Date) => {
19. // 保存按下确定按钮时的日期，这样当弹窗再次弹出时显示选中的是上一次确定的日期
20. this.selectedDate = value;
21. console.info('DatePickerDialog:onDateAccept()' + value.toString());
22. }
23. });
24. })
25. }.width('100%')
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/tAs6XTz0RJGgZr52bRL4_g/zh-cn_image_0000002583440099.png?HW-CC-KV=V1&HW-CC-Date=20260428T000220Z&HW-CC-Expire=86400&HW-CC-Sign=01FAFC7C8B9BA14F44F3F883C21D64ACF56D86FCC87EED12D927D2D4990457B5)

### 示例5（设置遮蔽区）

该示例通过maskRect设置遮蔽区。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct DatePickerDialogExample {
5. selectedDate: Date = new Date('2010-01-01');

7. build() {
8. Column() {
9. Button('DatePickerDialog')
10. .margin(20)
11. .onClick(() => {
12. this.getUIContext().showDatePickerDialog({
13. start: new Date('2000-01-01'),
14. end: new Date('2100-12-31'),
15. selected: this.selectedDate,
16. maskRect: {
17. x: 30,
18. y: 60,
19. width: '100%',
20. height: '60%'
21. },
22. onDateAccept: (value: Date) => {
23. // 保存按下确定按钮时的日期，这样当弹窗再次弹出时显示选中的是上一次确定的日期
24. this.selectedDate = value;
25. console.info('DatePickerDialog:onDateAccept()' + value.toString());
26. }
27. });
28. })
29. }.width('100%')
30. }
31. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/BJbI__joT2Sv5VC2kzuvSw/zh-cn_image_0000002552960054.png?HW-CC-KV=V1&HW-CC-Date=20260428T000220Z&HW-CC-Expire=86400&HW-CC-Sign=773E1113AFF382DB16F1DDB1557A83EEC909864012F428645A2F6521693B3C03)

### 示例6（设置弹窗背板）

该示例通过backgroundColor、backgroundBlurStyle、shadow设置弹窗背板。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct DatePickerDialogExample {
5. selectedDate: Date = new Date('2010-01-01');

7. build() {
8. Column() {
9. Button('DatePickerDialog')
10. .margin(20)
11. .onClick(() => {
12. this.getUIContext().showDatePickerDialog({
13. start: new Date('2000-01-01'),
14. end: new Date('2100-12-31'),
15. selected: this.selectedDate,
16. backgroundColor: 'rgb(204, 226, 251)',
17. backgroundBlurStyle: BlurStyle.NONE,
18. shadow: ShadowStyle.OUTER_FLOATING_SM,
19. onDateAccept: (value: Date) => {
20. // 保存按下确定按钮时的日期，这样当弹窗再次弹出时显示选中的是上一次确定的日期
21. this.selectedDate = value;
22. console.info('DatePickerDialog:onDateAccept()' + value.toString());
23. }
24. });
25. })
26. }.width('100%')
27. }
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/frX77MB5SBSl0MEMz6VpkA/zh-cn_image_0000002583480055.png?HW-CC-KV=V1&HW-CC-Date=20260428T000220Z&HW-CC-Expire=86400&HW-CC-Sign=035248663C72B4EDCB0075FAE60CC49F30D232263D70FDEC7ED8B11C2C632AB9)

### 示例7（设置公历农历）

该示例通过lunar、lunarSwitch设置弹窗显示公历或农历。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct DatePickerDialogExample {
5. selectedDate: Date = new Date('2010-11-09');

7. build() {
8. Column() {
9. Button('DatePickerDialog')
10. .margin(20)
11. .onClick(() => {
12. this.getUIContext().showDatePickerDialog({
13. start: new Date('2000-01-01'),
14. end: new Date('2100-12-31'),
15. selected: this.selectedDate,
16. lunar: false,
17. onDateAccept: (value: Date) => {
18. // 保存按下确定按钮时的日期，这样当弹窗再次弹出时显示选中的是上一次确定的日期
19. this.selectedDate = value;
20. console.info('DatePickerDialog:onDateAccept()' + value.toString());
21. }
22. });
23. })

25. Button('Lunar DatePickerDialog')
26. .margin(20)
27. .onClick(() => {
28. this.getUIContext().showDatePickerDialog({
29. start: new Date('2000-01-01'),
30. end: new Date('2100-12-31'),
31. selected: this.selectedDate,
32. lunar: true,
33. lunarSwitch: true,
34. onDateAccept: (value: Date) => {
35. this.selectedDate = value;
36. console.info('DatePickerDialog:onDateAccept()' + value.toString());
37. }
38. });
39. })
40. }.width('100%')
41. }
42. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/kAl0KJeORw-oxOEYk2oT1Q/zh-cn_image_0000002552800406.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000220Z&HW-CC-Expire=86400&HW-CC-Sign=15D9EFAA338C71982A3D841F01F478D130BB98AC2C5BD546BA36C96705E4844F)

### 示例8（设置显示月、日列）

该示例通过配置mode参数实现显示月、日两列。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct DatePickerDialogExample {
5. selectedDate: Date = new Date('2010-10-13');

7. build() {
8. Column() {
9. Button('DatePickerDialog')
10. .margin(20)
11. .onClick(() => {
12. this.getUIContext().showDatePickerDialog({
13. start: new Date('2000-01-01'),
14. end: new Date('2100-12-31'),
15. selected: this.selectedDate,
16. mode: DatePickerMode.MONTH_AND_DAY,
17. onDateAccept: (value: Date) => {
18. // 保存按下确定按钮时的日期，这样当弹窗再次弹出时显示选中的是上一次确定的日期
19. this.selectedDate = value;
20. console.info('DatePickerDialog:onDateAccept()' + value.toString());
21. }
22. });
23. })
24. }.width('100%')
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/Ma9iOJJfRZSvtb_WQUtEXQ/zh-cn_image_0000002583440101.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000220Z&HW-CC-Expire=86400&HW-CC-Sign=46778E5167520088DB79527C31EBC5B9370530B87B711B58841CA2058BCE7E10)

### 示例9（设置循环滚动）

从API version 20开始，可以通过配置canLoop参数设置是否循环滚动。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct DatePickerDialogExample {
5. @State isLoop: boolean = true;
6. selectedDate: Date = new Date('2009-12-31');

8. build() {
9. Column() {
10. Button('DatePickerDialog')
11. .margin(20)
12. .onClick(() => {
13. this.getUIContext().showDatePickerDialog({
14. start: new Date('2000-01-01'),
15. end: new Date('2100-12-31'),
16. selected: this.selectedDate,
17. canLoop: this.isLoop,
18. onDateAccept: (value: Date) => {
19. // 保存按下确定按钮时的日期，这样当弹窗再次弹出时显示选中的是上一次确定的日期
20. this.selectedDate = value;
21. console.info('DatePickerDialog:onDateAccept()' + value.toString());
22. }
23. });
24. })

26. Row() {
27. Text('循环滚动').fontSize(20)
28. Toggle({ type: ToggleType.Switch, isOn: true })
29. .onChange((isOn: boolean) => {
30. this.isLoop = isOn;
31. })
32. }.position({ x: '60%', y: '40%' })
33. }.width('100%')
34. }
35. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/rPIfrfm4To-4q1Rmjfda1Q/zh-cn_image_0000002552960056.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000220Z&HW-CC-Expire=86400&HW-CC-Sign=21FD4A980891024C1A4B9ECCC4E9E52343983A5DA44F7FFC17A872D6D74291D9)

### 示例10（自定义背景模糊效果参数）

从API version 19开始，可以通过配置[backgroundBlurStyleOptions](ts-methods-datepicker-dialog.md#datepickerdialogoptions对象说明)，实现自定义背景模糊效果。

```
1. @Entry
2. @Component
3. struct DatePickerDialogExample {
4. selectedDate: Date = new Date('2010-01-01');

6. build() {
7. Stack({ alignContent: Alignment.Top }) {
8. Image($r('app.media.bg'))
9. Column() {
10. Button('DatePickerDialog')
11. .margin(20)
12. .onClick(() => {
13. this.getUIContext().showDatePickerDialog({
14. start: new Date('2000-01-01'),
15. end: new Date('2100-12-31'),
16. selected: this.selectedDate,
17. backgroundColor: undefined,
18. backgroundBlurStyle: BlurStyle.Thin,
19. backgroundBlurStyleOptions: {
20. colorMode: ThemeColorMode.LIGHT,
21. adaptiveColor: AdaptiveColor.AVERAGE,
22. scale: 1,
23. blurOptions: { grayscale: [20, 20] },
24. },
25. });
26. })
27. }.width('100%')
28. }
29. }
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/WgHFGCAgRviStvjO-fOVAQ/zh-cn_image_0000002583480057.png?HW-CC-KV=V1&HW-CC-Date=20260428T000220Z&HW-CC-Expire=86400&HW-CC-Sign=E8226B835FAED7492F8909C4AECCA9E35BB27751F276FB95FAA97C042DA108B3)

### 示例11（自定义背景效果参数）

从API version 19开始，该示例通过配置[backgroundEffect](ts-methods-datepicker-dialog.md#datepickerdialogoptions对象说明)，实现自定义背景效果。

```
1. @Entry
2. @Component
3. struct DatePickerDialogExample {
4. selectedDate: Date = new Date('2010-01-01');

6. build() {
7. Stack({ alignContent: Alignment.Top }) {
8. // $r('app.media.bg')需要替换为开发者所需的图像资源文件。
9. Image($r('app.media.bg'))
10. Column() {
11. Button('DatePickerDialog')
12. .margin(20)
13. .onClick(() => {
14. this.getUIContext().showDatePickerDialog({
15. start: new Date('2000-01-01'),
16. end: new Date('2100-12-31'),
17. selected: this.selectedDate,
18. backgroundColor: undefined,
19. backgroundBlurStyle: BlurStyle.Thin,
20. backgroundEffect: {
21. radius: 60,
22. saturation: 0,
23. brightness: 1,
24. color: Color.White,
25. blurOptions: { grayscale: [20, 20] }
26. },
27. });
28. })
29. }.width('100%')
30. }
31. }
32. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/EVCgLLQyTd6YhWTvJezq9w/zh-cn_image_0000002552800408.png?HW-CC-KV=V1&HW-CC-Date=20260428T000220Z&HW-CC-Expire=86400&HW-CC-Sign=E7E2EB188AF66B2305107465544EBB89852F8DA4584A01E55F6B1D94CAD057EC)
