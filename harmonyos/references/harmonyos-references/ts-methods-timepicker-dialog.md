---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-timepicker-dialog
title: 时间滑动选择器弹窗 (TimePickerDialog)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 弹窗 > 时间滑动选择器弹窗 (TimePickerDialog)
category: harmonyos-references
scraped_at: 2026-04-29T13:52:46+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:215800219976833d292071ad4349285843cc4b2ca41d2e72c439eed119d9880e
---

以24小时的时间区间创建时间滑动选择器，展示在弹窗上。

说明

* 该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本模块功能依赖UI的执行上下文，不可在[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的地方使用，参见[UIContext](arkts-apis-uicontext-uicontext.md)说明。
* 本模块不支持深浅色模式热更新，如果需要进行深浅色模式切换，请重新打开弹窗。
* 最大显示行数在横、竖屏模式下存在差异。竖屏时默认为5行，横屏时依赖系统配置，未配置时默认显示为3行。可通过如下参数查看具体配置值$r('sys.float.ohos\_id\_picker\_show\_count\_landscape')。

## TimePickerDialog

PhonePC/2in1TabletTVWearable

### show(deprecated)

PhonePC/2in1TabletTVWearable

static show(options?: TimePickerDialogOptions)

定义时间滑动选择器弹窗并弹出。

说明

从API version 8开始支持，从API version 18开始废弃，建议使用[showTimePickerDialog](arkts-apis-uicontext-uicontext.md#showtimepickerdialog)替代。showTimePickerDialog需先获取[UIContext](arkts-apis-uicontext-uicontext.md)实例后再进行调用。

从API version 10开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[showTimePickerDialog](arkts-apis-uicontext-uicontext.md#showtimepickerdialog)来明确UI的执行上下文。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [TimePickerDialogOptions](ts-methods-timepicker-dialog.md#timepickerdialogoptions对象说明) | 否 | 配置时间选择器弹窗的参数。 |

## TimePickerDialogOptions对象说明

PhonePC/2in1TabletTVWearable

时间选择器弹窗选项。

继承自[TimePickerOptions](ts-basic-components-timepicker.md#timepickeroptions对象说明)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| useMilitaryTime | boolean | 否 | 是 | 时间是否以24小时制展示。  - true：时间以24小时制展示。  - false：时间以12小时制展示。  默认值：false  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| disappearTextStyle10+ | [PickerTextStyle](ts-picker-common.md#pickertextstyle对象说明) | 否 | 是 | 设置边缘项（以选中项为基准向上或向下的第二项）的文本颜色、字号、字体粗细。  默认值：  {  color: '#ff182431',  font: {  size: '14fp',  weight: FontWeight.Regular  }  }  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| textStyle10+ | [PickerTextStyle](ts-picker-common.md#pickertextstyle对象说明) | 否 | 是 | 设置待选项（以选中项为基准向上或向下的第一项）的文本颜色、字号、字体粗细。  默认值：  {  color: '#ff182431',  font: {  size: '16fp',  weight: FontWeight.Regular  }  }  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| selectedTextStyle10+ | [PickerTextStyle](ts-picker-common.md#pickertextstyle对象说明) | 否 | 是 | 设置选中项的文本颜色、字号、字体粗细。  默认值：  {  color: '#ff007dff',  font: {  size: '20fp',  weight: FontWeight.Medium  }  }  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| acceptButtonStyle12+ | [PickerDialogButtonStyle](ts-picker-common.md#pickerdialogbuttonstyle12对象说明) | 否 | 是 | 设置确认按钮显示样式、样式和重要程度、角色、背景色、圆角、文本颜色、字号、字体粗细、字体样式、字体列表、按钮是否默认响应Enter键。  **说明：**  1.acceptButtonStyle与cancelButtonStyle中最多只能有一个primary字段配置为true，如果同时设置为true，则primary字段不生效，保持默认值false。  2.按钮高度默认40vp，在关怀模式-大字体场景下高度不变，即使按钮样式设置为圆角矩形[ROUNDED\_RECTANGLE](ts-basic-components-button.md#buttontype枚举说明)，呈现效果依然是胶囊型按钮[Capsule](ts-basic-components-button.md#buttontype枚举说明)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| cancelButtonStyle12+ | [PickerDialogButtonStyle](ts-picker-common.md#pickerdialogbuttonstyle12对象说明) | 否 | 是 | 设置取消按钮显示样式、样式和重要程度、角色、背景色、圆角、文本颜色、字号、字体粗细、字体样式、字体列表、按钮是否默认响应Enter键。  **说明：**  1.acceptButtonStyle与cancelButtonStyle中最多只能有一个primary字段配置为true，如果同时设置为true，则primary字段不生效，保持默认值false。  2.按钮高度默认40vp，在关怀模式-大字体场景下高度不变，即使按钮样式设置为圆角矩形[ROUNDED\_RECTANGLE](ts-basic-components-button.md#buttontype枚举说明)，呈现效果依然是胶囊型按钮[Capsule](ts-basic-components-button.md#buttontype枚举说明)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| alignment10+ | [DialogAlignment](ts-methods-alert-dialog-box.md#dialogalignment枚举说明) | 否 | 是 | 设置弹窗在垂直方向上的对齐方式。  默认值：DialogAlignment.Default  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| offset10+ | [Offset](ts-types.md#offset) | 否 | 是 | 设置弹窗相对alignment所在位置的偏移量。  默认值：{ dx: 0 , dy: 0 }  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| maskRect10+ | [Rectangle](ts-methods-alert-dialog-box.md#rectangle8类型说明) | 否 | 是 | 弹窗遮蔽层区域，在遮蔽层区域内的事件不透传，在遮蔽层区域外的事件透传。  默认值：{ x: 0, y: 0, width: '100%', height: '100%' }  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| onAccept | (value: [TimePickerResult](ts-basic-components-timepicker.md#timepickerresult对象说明)) => void | 否 | 是 | 点击弹窗中的“确定”按钮时触发该回调。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| onCancel | () => void | 否 | 是 | 点击弹窗中的“取消”按钮时触发该回调。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| onChange | (value: [TimePickerResult](ts-basic-components-timepicker.md#timepickerresult对象说明)) => void | 否 | 是 | 滑动弹窗中的选择器后，选项归位至选中项位置时，触发该回调。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| backgroundColor11+ | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 弹窗背板颜色。  默认值：Color.Transparent  **说明：**  当设置了backgroundColor为非透明色时，backgroundBlurStyle需要设置为BlurStyle.NONE，否则显示的颜色将不符合预期效果。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundBlurStyle11+ | [BlurStyle](ts-universal-attributes-background.md#blurstyle9) | 否 | 是 | 弹窗背板模糊材质。  默认值：BlurStyle.COMPONENT\_ULTRA\_THICK  **说明：**  设置为BlurStyle.NONE即可关闭背景虚化。当设置了backgroundBlurStyle为非NONE值时，则不要设置backgroundColor，否则显示的颜色将不符合预期效果。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundBlurStyleOptions19+ | [BackgroundBlurStyleOptions](ts-universal-attributes-background.md#backgroundblurstyleoptions10对象说明) | 否 | 是 | 背景模糊效果。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| backgroundEffect19+ | [BackgroundEffectOptions](ts-universal-attributes-background.md#backgroundeffectoptions11) | 否 | 是 | 背景效果参数。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| onDidAppear12+ | () => void | 否 | 是 | 弹窗弹出后的事件回调。  **说明：**  1.正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange)>>onWillDisappear>>onDidDisappear。  2.在onDidAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。  3.快速点击弹出，消失弹窗时，存在onWillDisappear在onDidAppear前生效。  4. 当弹窗入场动效未完成时关闭弹窗，该回调不会触发。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onDidDisappear12+ | () => void | 否 | 是 | 弹窗消失后的事件回调。  **说明：**  1.正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange)>>onWillDisappear>>onDidDisappear。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onWillAppear12+ | () => void | 否 | 是 | 弹窗显示动效前的事件回调。  **说明：**  1.正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange)>>onWillDisappear>>onDidDisappear。  2.在onWillAppear内设置改变弹窗显示效果的回调事件，二次弹出生效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onWillDisappear12+ | () => void | 否 | 是 | 弹窗退出动效前的事件回调。  **说明：**  1.正常时序依次为：onWillAppear>>onDidAppear>>(onAccept/onCancel/onChange)>>onWillDisappear>>onDidDisappear。  2.快速点击弹出，消失弹窗时，存在onWillDisappear在onDidAppear前生效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| shadow12+ | [ShadowOptions](ts-universal-attributes-image-effect.md#shadowoptions对象说明) | [ShadowStyle](ts-universal-attributes-image-effect.md#shadowstyle10枚举说明) | 否 | 是 | 设置弹窗背板的阴影。  **说明：**  当设备为2in1时，默认场景下获焦阴影值为ShadowStyle.OUTER\_FLOATING\_MD，失焦为ShadowStyle.OUTER\_FLOATING\_SM。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| dateTimeOptions12+ | [DateTimeOptions](js-apis-intl.md#datetimeoptionsdeprecated) | 否 | 是 | 设置时分是否显示前导0，目前只支持设置hour和minute参数。  默认值：  hour: 24小时制默认为"2-digit"，设置hour是否按照2位数字显示，如果实际数值小于10，则会补充前导0并显示，即为"0X"；12小时制默认为"numeric"，即没有前导0。  minute: 默认为"2-digit"，设置minute是否按照2位数字显示，如果实际数值小于10，则会补充前导0并显示，即为"0X"。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| enableHoverMode14+ | boolean | 否 | 是 | 是否响应悬停态。  - true：响应悬停态。  - false：不响应悬停态。  默认值：false  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| hoverModeArea14+ | [HoverModeAreaType](ts-universal-attributes-sheet-transition.md#hovermodeareatype14) | 否 | 是 | 悬停态下弹窗默认展示区域。  默认值：HoverModeAreaType.BOTTOM\_SCREEN  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| onEnterSelectedArea18+ | Callback<[TimePickerResult](ts-basic-components-timepicker.md#timepickerresult对象说明)> | 否 | 是 | 滑动过程中，选项进入分割线区域内，触发该回调。与onChange事件的差别在于，该事件的触发时机早于onChange事件，当当前滑动列滑动距离超过选中项高度的一半时，选项此时已经进入分割线区域内，会触发该事件。  **说明：**  当enableCascade设置为true时，由于上午/下午列与小时列存在联动关系，不建议使用该回调。该回调标识的是滑动过程中选项进入分割线区域内的节点，而联动变化的选项并不涉及滑动，因此，回调的返回值中，仅当前滑动列的值会正常变化，其余未滑动列的值保持不变。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| enableCascade18+ | boolean | 否 | 是 | 设置上午和下午的标识是否根据小时数自动切换，仅在useMilitaryTime设置为false时生效。  - true：自动切换。  - false：不自动切换。  默认值：false  当enableCascade设置为true时，仅在loop参数同时为true时生效。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| enableHapticFeedback18+ | boolean | 否 | 是 | 设置是否开启触控反馈。  - true：开启触控反馈。  - false：不开启触控反馈。  默认值：true  **说明**：  1. 设置为true后，其生效情况取决于系统的硬件是否支持。  2. 开启触控反馈时，需要在工程的src/main/module.json5文件的"module"内配置requestPermissions字段开启振动权限，配置如下：  "requestPermissions": [{"name": "ohos.permission.VIBRATE"}]  **元服务API**： 从API version 18开始，该接口支持在元服务中使用。 |

## 示例

PhonePC/2in1TabletTVWearable

说明

推荐通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[showTimePickerDialog](arkts-apis-uicontext-uicontext.md#showtimepickerdialog)来明确UI的执行上下文。

### 示例1（设置时间格式）

该示例通过useMilitaryTime、dateTimeOptions、format设置时间格式。

```
1. @Entry
2. @Component
3. struct TimePickerDialogExample {
4. private selectTime: Date = new Date('2020-12-25T08:30:00');

6. build() {
7. Column() {
8. Button('TimePickerDialog 12小时制')
9. .margin(20)
10. .onClick(() => {
11. this.getUIContext().showTimePickerDialog({
12. selected: this.selectTime,
13. format: TimePickerFormat.HOUR_MINUTE,
14. useMilitaryTime: false,
15. dateTimeOptions: { hour: 'numeric', minute: '2-digit' },
16. onAccept: (value: TimePickerResult) => {
17. // 设置selectTime为按下确定按钮时的时间，这样当弹窗再次弹出时显示选中的为上一次确定的时间
18. if (value.hour != undefined && value.minute != undefined) {
19. this.selectTime.setHours(value.hour, value.minute);
20. console.info('TimePickerDialog:onAccept()' + JSON.stringify(value));
21. }
22. },
23. onCancel: () => {
24. console.info('TimePickerDialog:onCancel()');
25. },
26. onChange: (value: TimePickerResult) => {
27. console.info('TimePickerDialog:onChange()' + JSON.stringify(value));
28. },
29. onDidAppear: () => {
30. console.info('TimePickerDialog:onDidAppear()');
31. },
32. onDidDisappear: () => {
33. console.info('TimePickerDialog:onDidDisappear()');
34. },
35. onWillAppear: () => {
36. console.info('TimePickerDialog:onWillAppear()');
37. },
38. onWillDisappear: () => {
39. console.info('TimePickerDialog:onWillDisappear()');
40. }
41. });
42. })
43. Button('TimePickerDialog 24小时制')
44. .margin(20)
45. .onClick(() => {
46. this.getUIContext().showTimePickerDialog({
47. selected: this.selectTime,
48. format: TimePickerFormat.HOUR_MINUTE_SECOND,
49. useMilitaryTime: true,
50. onAccept: (value: TimePickerResult) => {
51. if (value.hour != undefined && value.minute != undefined) {
52. this.selectTime.setHours(value.hour, value.minute);
53. console.info('TimePickerDialog:onAccept()' + JSON.stringify(value));
54. }
55. },
56. })
57. })
58. }.width('100%')
59. }
60. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/APVjSKAwRzOHREmNnm7oMA/zh-cn_image_0000002589246391.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055244Z&HW-CC-Expire=86400&HW-CC-Sign=CF8AE6871E989E4BB1697F58A7010ADB064B7B9076AEAD23A3C270E865E0DC20)

### 示例2（自定义样式）

该示例通过配置disappearTextStyle、textStyle、selectedTextStyle、acceptButtonStyle、cancelButtonStyle实现了自定义文本以及按钮样式。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TimePickerDialogExample {
5. private selectTime: Date = new Date('2020-12-25T08:30:00');

7. build() {
8. Column() {
9. Button('TimePickerDialog 12小时制')
10. .margin(20)
11. .onClick(() => {
12. this.getUIContext().showTimePickerDialog({
13. disappearTextStyle: { color: '#297bec', font: { size: 15, weight: FontWeight.Lighter } },
14. textStyle: { color: Color.Black, font: { size: 20, weight: FontWeight.Normal } },
15. selectedTextStyle: { color: Color.Blue, font: { size: 30, weight: FontWeight.Bolder } },
16. acceptButtonStyle: {
17. type: ButtonType.Normal,
18. style: ButtonStyleMode.NORMAL,
19. role: ButtonRole.NORMAL,
20. fontColor: 'rgb(81, 81, 216)',
21. fontSize: '26fp',
22. fontWeight: FontWeight.Bolder,
23. fontStyle: FontStyle.Normal,
24. fontFamily: 'sans-serif',
25. backgroundColor: '#A6ACAF',
26. borderRadius: 20
27. },
28. cancelButtonStyle: {
29. type: ButtonType.Normal,
30. style: ButtonStyleMode.NORMAL,
31. role: ButtonRole.NORMAL,
32. fontColor: Color.Blue,
33. fontSize: '16fp',
34. fontWeight: FontWeight.Normal,
35. fontStyle: FontStyle.Italic,
36. fontFamily: 'sans-serif',
37. backgroundColor: '#50182431',
38. borderRadius: 10
39. },
40. onAccept: (value: TimePickerResult) => {
41. if (value.hour != undefined && value.minute != undefined) {
42. this.selectTime.setHours(value.hour, value.minute);
43. console.info('TimePickerDialog:onAccept()' + JSON.stringify(value));
44. }
45. }
46. });
47. })
48. }.width('100%')
49. }
50. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/C7cAQ5u8QPmjYZCNnNAC4A/zh-cn_image_0000002558766584.png?HW-CC-KV=V1&HW-CC-Date=20260429T055244Z&HW-CC-Expire=86400&HW-CC-Sign=3536EBD5EC1B8BEBE83DF59431C4A5E9B97D756300922B01A49FD712334FAC49)

### 示例3（悬停态弹窗）

该示例展示了在折叠屏悬停态下设置dialog布局区域的效果。

```
1. @Entry
2. @Component
3. struct TimePickerDialogExample {
4. private selectTime: Date = new Date('2020-12-25T08:30:00');

6. build() {
7. Column() {
8. Button('TimePickerDialog 12小时制')
9. .margin(20)
10. .onClick(() => {
11. this.getUIContext().showTimePickerDialog({
12. selected: this.selectTime,
13. disappearTextStyle: { color: Color.Red, font: { size: 15, weight: FontWeight.Lighter } },
14. textStyle: { color: Color.Black, font: { size: 20, weight: FontWeight.Normal } },
15. selectedTextStyle: { color: Color.Blue, font: { size: 30, weight: FontWeight.Bolder } },
16. onAccept: (value: TimePickerResult) => {
17. // 设置selectTime为按下确定按钮时的时间，这样当弹窗再次弹出时显示选中的为上一次确定的时间
18. if (value.hour != undefined && value.minute != undefined) {
19. this.selectTime.setHours(value.hour, value.minute);
20. console.info('TimePickerDialog:onAccept()' + JSON.stringify(value));
21. }
22. },
23. onCancel: () => {
24. console.info('TimePickerDialog:onCancel()');
25. },
26. onChange: (value: TimePickerResult) => {
27. console.info('TimePickerDialog:onChange()' + JSON.stringify(value));
28. },
29. onDidAppear: () => {
30. console.info('TimePickerDialog:onDidAppear()');
31. },
32. onDidDisappear: () => {
33. console.info('TimePickerDialog:onDidDisappear()');
34. },
35. onWillAppear: () => {
36. console.info('TimePickerDialog:onWillAppear()');
37. },
38. onWillDisappear: () => {
39. console.info('TimePickerDialog:onWillDisappear()');
40. },
41. enableHoverMode: true,
42. hoverModeArea: HoverModeAreaType.TOP_SCREEN
43. });
44. })
45. }.width('100%')
46. }
47. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/TCbD5oUwQASWCHUpzqR5cQ/zh-cn_image_0000002558606924.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055244Z&HW-CC-Expire=86400&HW-CC-Sign=EAAF88890A9DA34C9AB0E2BA9A8107B101CBDD9529D179F4F87123C3654B72E3)

### 示例4（设置弹窗位置）

该示例通过alignment和offset设置弹窗的位置。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TimePickerDialogExample {
5. private selectTime: Date = new Date('2020-12-25T08:30:00');

7. build() {
8. Column() {
9. Button('TimePickerDialog')
10. .margin(20)
11. .onClick(() => {
12. this.getUIContext().showTimePickerDialog({
13. alignment: DialogAlignment.Center,
14. offset: { dx: 20 , dy: 0 },
15. onAccept: (value: TimePickerResult) => {
16. // 设置selectTime为按下确定按钮时的时间，这样当弹窗再次弹出时显示选中的为上一次确定的时间
17. if (value.hour != undefined && value.minute != undefined) {
18. this.selectTime.setHours(value.hour, value.minute);
19. console.info('TimePickerDialog:onAccept()' + JSON.stringify(value));
20. }
21. }
22. });
23. })
24. }.width('100%')
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/Z4G8Tc7CRuuKAeIchwmu0A/zh-cn_image_0000002589326451.png?HW-CC-KV=V1&HW-CC-Date=20260429T055244Z&HW-CC-Expire=86400&HW-CC-Sign=3F7508997268D41A9442ADD10CA213491E74BA9821ED168946EA6A916E2424B8)

### 示例5（设置遮蔽区）

该示例通过maskRect设置遮蔽区。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TimePickerDialogExample {
5. private selectTime: Date = new Date('2020-12-25T08:30:00');

7. build() {
8. Column() {
9. Button('TimePickerDialog')
10. .margin(20)
11. .onClick(() => {
12. this.getUIContext().showTimePickerDialog({
13. maskRect: { x: 30, y: 60, width: '100%', height: '60%' },
14. onAccept: (value: TimePickerResult) => {
15. // 设置selectTime为按下确定按钮时的时间，这样当弹窗再次弹出时显示选中的为上一次确定的时间
16. if (value.hour != undefined && value.minute != undefined) {
17. this.selectTime.setHours(value.hour, value.minute);
18. console.info('TimePickerDialog:onAccept()' + JSON.stringify(value));
19. }
20. }
21. });
22. })
23. }.width('100%')
24. }
25. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/BjCv6Cl-RH2na3y6VSO1DQ/zh-cn_image_0000002589246393.png?HW-CC-KV=V1&HW-CC-Date=20260429T055244Z&HW-CC-Expire=86400&HW-CC-Sign=9BCECB56BAC4D9BF64FBCFA526619B5FB2909406E26D762CC90651B850E3BF3E)

### 示例6（设置弹窗背板）

该示例通过maskRect设置弹窗背板。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TimePickerDialogExample {
5. private selectTime: Date = new Date('2020-12-25T08:30:00');

7. build() {
8. Column() {
9. Button('TimePickerDialog')
10. .margin(20)
11. .onClick(() => {
12. this.getUIContext().showTimePickerDialog({
13. backgroundColor: 'rgb(204, 226, 251)',
14. backgroundBlurStyle: BlurStyle.NONE,
15. shadow: ShadowStyle.OUTER_FLOATING_SM,
16. onAccept: (value: TimePickerResult) => {
17. // 设置selectTime为按下确定按钮时的时间，这样当弹窗再次弹出时显示选中的为上一次确定的时间
18. if (value.hour != undefined && value.minute != undefined) {
19. this.selectTime.setHours(value.hour, value.minute);
20. console.info('TimePickerDialog:onAccept()' + JSON.stringify(value));
21. }
22. }
23. });
24. })
25. }.width('100%')
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/cB03y6xbTNyzaB7vlLx_CQ/zh-cn_image_0000002558766586.png?HW-CC-KV=V1&HW-CC-Date=20260429T055244Z&HW-CC-Expire=86400&HW-CC-Sign=51BBA31EF501C4A6AC54A2DE425E91C9EF200311B3C981234F8D4D78AC779240)

### 示例7（设置时间滑动选择器弹窗的起始时间）

该示例设置TimePickerDialog的起始时间。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TimePickerDialogExample {
5. private selectTime: Date = new Date('2022-07-22T08:50:00');

7. build() {
8. Column() {
9. Button('TimePickerDialog')
10. .margin(20)
11. .onClick(() => {
12. this.getUIContext().showTimePickerDialog({
13. useMilitaryTime: false,
14. selected: this.selectTime,
15. format: TimePickerFormat.HOUR_MINUTE_SECOND,
16. start: new Date('2022-07-22T08:30:00'),
17. onAccept: (value: TimePickerResult) => {
18. // 设置selectTime为按下确定按钮时的时间，这样当弹窗再次弹出时显示选中的为上一次确定的时间
19. if (value.hour != undefined && value.minute != undefined) {
20. this.selectTime.setHours(value.hour, value.minute);
21. console.info('TimePickerDialog:onAccept()' + JSON.stringify(value));
22. }
23. }
24. });
25. })
26. }.width('100%')
27. }
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/B26uoo-US6udfib20onxIA/zh-cn_image_0000002558606926.png?HW-CC-KV=V1&HW-CC-Date=20260429T055244Z&HW-CC-Expire=86400&HW-CC-Sign=F0314FC5A5BD8B0CBD349901E779770F096EF66D60DB7F2C465E4C32F3057EA4)

### 示例8（设置时间滑动选择器弹窗的结束时间）

该示例设置TimePickerDialog的结束时间。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TimePickerDialogExample {
5. private selectTime: Date = new Date('2022-07-22T08:50:00');

7. build() {
8. Column() {
9. Button('TimePickerDialog')
10. .margin(20)
11. .onClick(() => {
12. this.getUIContext().showTimePickerDialog({
13. useMilitaryTime: false,
14. selected: this.selectTime,
15. format: TimePickerFormat.HOUR_MINUTE_SECOND,
16. end: new Date('2022-07-22T15:20:00'),
17. onAccept: (value: TimePickerResult) => {
18. // 设置selectTime为按下确定按钮时的时间，这样当弹窗再次弹出时显示选中的为上一次确定的时间
19. if (value.hour != undefined && value.minute != undefined) {
20. this.selectTime.setHours(value.hour, value.minute);
21. console.info('TimePickerDialog:onAccept()' + JSON.stringify(value));
22. }
23. }
24. });
25. })
26. }.width('100%')
27. }
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/FYdKHltJRlenr993CrSLCQ/zh-cn_image_0000002589326453.png?HW-CC-KV=V1&HW-CC-Date=20260429T055244Z&HW-CC-Expire=86400&HW-CC-Sign=EE49C49C03BF21F615C32B07416C189BD81BCA92A17D98527158DFA7296335DC)

### 示例9（设置上午下午跟随时间联动）

该示例通过配置enableCascade实现12小时制时上午下午跟随时间联动。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TimePickerDialogExample {
5. private selectTime: Date = new Date('2022-07-22T08:00:00');

7. build() {
8. Column() {
9. Button('TimePickerDialog')
10. .margin(20)
11. .onClick(() => {
12. this.getUIContext().showTimePickerDialog({
13. useMilitaryTime: false,
14. selected: this.selectTime,
15. enableCascade:true,
16. onAccept: (value: TimePickerResult) => {
17. // 设置selectTime为按下确定按钮时的时间，这样当弹窗再次弹出时显示选中的为上一次确定的时间
18. if (value.hour != undefined && value.minute != undefined) {
19. this.selectTime.setHours(value.hour, value.minute);
20. console.info('TimePickerDialog:onAccept()' + JSON.stringify(value));
21. }
22. }
23. });
24. })
25. }.width('100%')
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/lo2TNJEPQySXnD9iop1xuQ/zh-cn_image_0000002589246395.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055244Z&HW-CC-Expire=86400&HW-CC-Sign=213483323608812E7B4570D6739DEA18AB5CDB47633E3668B89E78A4A6C39A57)

### 示例10（自定义背景模糊效果参数）

从API version 19开始，该示例通过配置[backgroundBlurStyleOptions](ts-methods-timepicker-dialog.md#timepickerdialogoptions对象说明)，实现自定义背景模糊效果。

```
1. @Entry
2. @Component
3. struct TimePickerDialogExample {
4. build() {
5. Stack({ alignContent: Alignment.Top }) {
6. // $r('app.media.bg')需要替换为开发者所需的图像资源文件。
7. Image($r('app.media.bg'))
8. Column() {
9. Button('TimePickerDialog')
10. .margin(20)
11. .onClick(() => {
12. this.getUIContext().showTimePickerDialog({
13. backgroundColor: undefined,
14. backgroundBlurStyle: BlurStyle.Thin,
15. backgroundBlurStyleOptions: {
16. colorMode: ThemeColorMode.LIGHT,
17. adaptiveColor: AdaptiveColor.AVERAGE,
18. scale: 1,
19. blurOptions: { grayscale: [20, 20] },
20. },
21. });
22. })
23. }.width('100%')
24. }
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/JM_ZPLcaTqCGEo9IYykSyQ/zh-cn_image_0000002558766588.png?HW-CC-KV=V1&HW-CC-Date=20260429T055244Z&HW-CC-Expire=86400&HW-CC-Sign=0646DDBCC1FB165FA12946E7DAB140054095A639EE9B46EB3BD170D26F1D0CD0)

### 示例11（自定义背景效果参数）

从API version 19开始，该示例通过配置[backgroundEffect](ts-methods-timepicker-dialog.md#timepickerdialogoptions对象说明)，实现自定义背景效果。

```
1. @Entry
2. @Component
3. struct TimePickerDialogExample {
4. build() {
5. Stack({ alignContent: Alignment.Top }) {
6. // $r('app.media.bg')需要替换为开发者所需的图像资源文件。
7. Image($r('app.media.bg'))
8. Column() {
9. Button('TimePickerDialog')
10. .margin(20)
11. .onClick(() => {
12. this.getUIContext().showTimePickerDialog({
13. backgroundColor: undefined,
14. backgroundBlurStyle: BlurStyle.Thin,
15. backgroundEffect: {
16. radius: 60,
17. saturation: 0,
18. brightness: 1,
19. color: Color.White,
20. blurOptions: { grayscale: [20, 20] }
21. },
22. });
23. })
24. }.width('100%')
25. }
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/__y_5A-OQtedX_cLMVONFA/zh-cn_image_0000002558606928.png?HW-CC-KV=V1&HW-CC-Date=20260429T055244Z&HW-CC-Expire=86400&HW-CC-Sign=8F7326FA25A58CD70BAE85663ACC58F61573D2ACBD308BA6A3535854E2C073D1)
