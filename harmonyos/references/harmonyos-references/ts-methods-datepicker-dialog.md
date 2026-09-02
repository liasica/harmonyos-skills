---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-datepicker-dialog
title: 日期滑动选择器弹窗 (DatePickerDialog)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 弹窗 > 日期滑动选择器弹窗 (DatePickerDialog)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1b823a06a0c9512ed7398cbb104620fab26677a8c595bf6c972f4e8357babd88
---

根据指定的日期范围创建日期滑动选择器并展示在弹窗上。该组件适用于需要用户快速选择日期的应用场景，如日程安排、活动安排、生日设置等。使用该组件可以简化开发流程，提供统一的日期选择用户体验，并支持多种自定义选项以满足不同需求。

**说明** 

* 该组件从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块功能依赖UI的执行上下文，不可在[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的地方使用，参见[UIContext](arkts-apis-uicontext-uicontext.md)说明。
* 本模块不支持深浅色模式热更新，如果需要进行深浅色模式切换，请重新打开弹窗。
* 最大显示行数在横、竖屏模式下存在差异。竖屏时默认为5行，横屏时依赖系统配置，未配置时默认显示为3行。可通过如下资源引用查看具体配置值$r('sys.float.ohos\_id\_picker\_show\_count\_landscape')。

## DatePickerDialog

### show(deprecated)

static show(options?: DatePickerDialogOptions)

定义日期滑动选择器弹窗并弹出。

**说明** 

从API version 8开始支持，从API version 18开始废弃，建议使用[showDatePickerDialog](arkts-apis-uicontext-uicontext.md#showdatepickerdialog)替代。showDatePickerDialog需先获取[UIContext](arkts-apis-uicontext-uicontext.md)实例后再进行调用。

从API version 10开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[showDatePickerDialog](arkts-apis-uicontext-uicontext.md#showdatepickerdialog)来明确UI的执行上下文。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [DatePickerDialogOptions](ts-methods-datepicker-dialog.md#datepickerdialogoptions对象说明) | 否 | 配置日期选择器弹窗的参数，缺省时不弹出弹窗。 |

## DatePickerDialogOptions对象说明

日期选择器弹窗选项。

继承自[DatePickerOptions](ts-basic-components-datepicker.md#datepickeroptions对象说明)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| lunar | boolean | 否 | 是 | 日期是否显示为农历。  - true：显示为农历。  - false：不显示为农历。  默认值：false  **说明：**  仅在简体中文和繁体中文语言环境下生效，其他语言环境下设置该属性无效果。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| showTime10+ | boolean | 否 | 是 | 是否在弹窗内展示时间选择器。  - true：展示时间选择器。  - false：不展示时间选择器。  默认值：false  **说明：**  1. 当showTime为true时，点击弹窗的标题日期可以在"日期选择器"和"日期选择器+时间选择器"两个页面中切换。  2. 当showTime为true时，mode参数不生效，此时纯日期选择页面固定显示年、月、日三列。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| useMilitaryTime10+ | boolean | 否 | 是 | 弹窗内展示的时间选择器是否为24小时制，仅当showTime为true时生效。  - true：显示24小时制。  - false：显示12小时制。  默认值：false  **说明：**  当展示的时间选择器为12小时制时，上午和下午的标识不会根据小时数自动切换。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| lunarSwitch10+ | boolean | 否 | 是 | 是否展示切换农历的开关。  - true：展示切换农历的开关。  - false：不展示切换农历的开关。  默认值：false  **说明：**  开关打开后，仅在简体中文和繁体中文环境下生效，在其他语言环境农历不生效，因此建议在其他语言环境设置为不展示开关。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| lunarSwitchStyle14+ | [LunarSwitchStyle](ts-methods-datepicker-dialog.md#lunarswitchstyle14对象说明) | 否 | 是 | 设置农历开关的颜色样式。仅当lunarSwitch为true时生效。  默认值：{  selectedColor: $r('sys.color.ohos\_id\_color\_text\_primary\_actived'),  unselectedColor: $r('sys.color.ohos\_id\_color\_switch\_outline\_off'),  strokeColor: Color.White  }  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| disappearTextStyle10+ | [PickerTextStyle](ts-picker-common.md#pickertextstyle对象说明) | 否 | 是 | 设置边缘项（以选中项为基准向上或向下的第二项）的文本颜色、字号、字体粗细。  默认值：  {  color: '#ff182431',  font: {  size: '14fp',  weight: FontWeight.Regular  }  }  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| textStyle10+ | [PickerTextStyle](ts-picker-common.md#pickertextstyle对象说明) | 否 | 是 | 设置待选项（以选中项为基准向上或向下的第一项）的文本颜色、字号、字体粗细。  默认值：  {  color: '#ff182431',  font: {  size: '16fp',  weight: FontWeight.Regular  }  }  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| selectedTextStyle10+ | [PickerTextStyle](ts-picker-common.md#pickertextstyle对象说明) | 否 | 是 | 设置选中项的文本颜色、字号、字体粗细。  默认值：  {  color: '#ff007dff',  font: {  size: '20fp',  weight: FontWeight.Medium  }  }  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| acceptButtonStyle12+ | [PickerDialogButtonStyle](ts-picker-common.md#pickerdialogbuttonstyle12对象说明) | 否 | 是 | 设置确认按钮显示样式、重要程度、角色、背景色、圆角、文本颜色、字号、字体粗细、字体样式、字体列表、按钮是否默认响应Enter键。当需要自定义确认按钮外观或行为时传入此参数。不传入时使用系统默认按钮样式。  **说明：**  1.acceptButtonStyle与cancelButtonStyle中最多只能有一个primary字段配置为true，如果同时设置为true，则primary字段不生效，保持默认值false。  2.按钮高度默认40vp，在关怀模式-大字体场景下高度不变，即使按钮样式设置为圆角矩形[ROUNDED\_RECTANGLE](ts-basic-components-button.md#buttontype枚举说明)，呈现效果依然是胶囊型按钮[Capsule](ts-basic-components-button.md#buttontype枚举说明)。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| cancelButtonStyle12+ | [PickerDialogButtonStyle](ts-picker-common.md#pickerdialogbuttonstyle12对象说明) | 否 | 是 | 设置取消按钮显示样式、重要程度、角色、背景色、圆角、文本颜色、字号、字体粗细、字体样式、字体列表、按钮是否默认响应Enter键。当需要自定义取消按钮外观或行为时传入此参数。不传入时使用系统默认按钮样式。  **说明：**  1.acceptButtonStyle与cancelButtonStyle中最多只能有一个primary字段配置为true，如果同时设置为true，则primary字段不生效，保持默认值false。  2.按钮高度默认40vp，在关怀模式-大字体场景下高度不变，即使按钮样式设置为圆角矩形[ROUNDED\_RECTANGLE](ts-basic-components-button.md#buttontype枚举说明)，呈现效果依然是胶囊型按钮[Capsule](ts-basic-components-button.md#buttontype枚举说明)。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| alignment10+ | [DialogAlignment](ts-methods-alert-dialog-box.md#dialogalignment枚举说明) | 否 | 是 | 弹窗在竖直方向上的对齐方式。  默认值：DialogAlignment.Default  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| offset10+ | [Offset](ts-types.md#offset) | 否 | 是 | 弹窗相对alignment所在位置的偏移量。当需要微调弹窗位置时设置此参数（如与alignment配合实现精确位置控制），不设置时弹窗按alignment对齐位置显示。  默认值：{ dx: 0 , dy: 0 }  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| maskRect10+ | [Rectangle](ts-methods-alert-dialog-box.md#rectangle8类型说明) | 否 | 是 | 弹窗遮蔽层区域，在遮蔽层区域内的事件不透传，在遮蔽层区域外的事件透传。  默认值：{ x: 0, y: 0, width: '100%', height: '100%' }  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| onAccept(deprecated) | (value: [DatePickerResult](ts-basic-components-datepicker.md#datepickerresult对象说明)) => void | 否 | 是 | 点击弹窗中的“确定”按钮时触发该回调。回调参数value为当前选中的日期，包含年、月、日信息。  **说明：**  从API version 8开始支持，从API version 10开始废弃。建议使用onDateAccept。 |
| onCancel | [VoidCallback](ts-types.md#voidcallback12) | 否 | 是 | 点击弹窗中的“取消”按钮时触发该回调。回调签名：() => void，无参数和返回值。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| onChange(deprecated) | (value: [DatePickerResult](ts-basic-components-datepicker.md#datepickerresult对象说明)) => void | 否 | 是 | 滑动弹窗中的滑动选择器使当前选中项改变时触发该回调。回调参数value为当前选中的日期，包含年、月、日信息。  **说明：**  从API version 8开始支持，从API version 10开始废弃。建议使用onDateChange。 |
| onDateAccept10+ | [Callback](ts-types.md#callback12)<Date> | 否 | 是 | 点击弹窗中的“确定”按钮时触发该回调。回调签名：(value: Date) => void，其中value为用户选择的日期，包含年月日信息；当showTime为true时，还包含时和分信息。开发者可在此回调中保存用户选择的日期或执行后续业务逻辑。  **说明：**  当showTime设置为true时，value中时和分为选择器选择的时和分。否则，value中时和分为系统时间的时和分。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| onDateChange10+ | [Callback](ts-types.md#callback12)<Date> | 否 | 是 | 滑动弹窗中的日期使当前选中项改变时触发该回调。回调签名：(value: Date) => void，其中value为当前选中的日期，包含年月日信息；当showTime为true时，还包含时和分信息。此回调在用户滑动选择器过程中实时触发，与onDateAccept仅在点击确定后触发的时机不同。  **说明：**  当showTime设置为true时，value中时和分为选择器选择的时和分。否则，value中时和分为系统时间的时和分。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| backgroundColor11+ | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 弹窗背板颜色。  默认值：Color.Transparent  **说明：**  当设置了backgroundColor为非透明色时，backgroundBlurStyle需要设置为BlurStyle.NONE，否则显示的颜色将不符合预期效果。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundBlurStyle11+ | [BlurStyle](ts-universal-attributes-background.md#blurstyle9) | 否 | 是 | 弹窗背板模糊材质。  默认值：BlurStyle.COMPONENT\_ULTRA\_THICK  **说明：**  设置为BlurStyle.NONE即可关闭背景虚化。当设置了backgroundBlurStyle为非NONE值时，则不要设置backgroundColor，否则显示的颜色将不符合预期效果。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| backgroundBlurStyleOptions19+ | [BackgroundBlurStyleOptions](ts-universal-attributes-background.md#backgroundblurstyleoptions10对象说明) | 否 | 是 | 背景模糊效果参数，用于自定义弹窗背景模糊的显示样式，支持配置颜色模式、自适应颜色、缩放比例等属性，实现不同的背景模糊视觉效果。默认值请参考BackgroundBlurStyleOptions类型说明。  **说明：**  未设置时沿用backgroundBlurStyle的默认效果（BlurStyle.COMPONENT\_ULTRA\_THICK）。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| backgroundEffect19+ | [BackgroundEffectOptions](ts-universal-attributes-background.md#backgroundeffectoptions11) | 否 | 是 | 背景效果参数，用于自定义弹窗背景的显示效果，支持配置模糊半径、饱和度、亮度、颜色等属性，实现不同的背景视觉效果。默认值请参考BackgroundEffectOptions类型说明。  **说明：**  未设置时不生效，此时弹窗背景模糊效果由backgroundBlurStyle决定；设置后将覆盖backgroundBlurStyle的效果。从API版本26.0.0开始，设置systemMaterial后backgroundEffect与backgroundBlurStyle均不生效。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |
| onDidAppear12+ | [VoidCallback](ts-types.md#voidcallback12) | 否 | 是 | 弹窗弹出后的事件回调。  **说明：**  1.正常时序依次为：onWillAppear>>onDidAppear>>(onDateAccept/onCancel/onDateChange)>>onWillDisappear>>onDidDisappear。  2.在onDidAppear内设置改变弹窗显示效果的回调事件，再次调用showDatePickerDialog时生效。  3.快速连续触发弹出与关闭时，存在onWillDisappear在onDidAppear前生效。  4. 当弹窗入场动效未完成时关闭弹窗，该回调不会触发。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onDidDisappear12+ | [VoidCallback](ts-types.md#voidcallback12) | 否 | 是 | 弹窗消失后的事件回调。  **说明：**  1.正常时序依次为：onWillAppear>>onDidAppear>>(onDateAccept/onCancel/onDateChange)>>onWillDisappear>>onDidDisappear。  2.快速连续触发弹出与关闭时，存在onWillDisappear在onDidAppear前生效。  3. 当弹窗入场动效未完成时关闭弹窗，该回调不会触发。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onWillAppear12+ | [VoidCallback](ts-types.md#voidcallback12) | 否 | 是 | 弹窗显示动效前的事件回调。  **说明：**  1.正常时序依次为：onWillAppear>>onDidAppear>>(onDateAccept/onCancel/onDateChange)>>onWillDisappear>>onDidDisappear。  2.在onWillAppear内设置改变弹窗显示效果的回调事件，再次调用showDatePickerDialog时生效。  3.快速连续触发弹出与关闭时，存在onWillDisappear在onDidAppear前生效。  4. 当弹窗入场动效未完成时关闭弹窗，onDidAppear和后续回调不会触发。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onWillDisappear12+ | [VoidCallback](ts-types.md#voidcallback12) | 否 | 是 | 弹窗退出动效前的事件回调。  **说明：**  1.正常时序依次为：onWillAppear>>onDidAppear>>(onDateAccept/onCancel/onDateChange)>>onWillDisappear>>onDidDisappear。  2.快速连续触发弹出与关闭时，存在onWillDisappear在onDidAppear前生效。  3. 当弹窗入场动效未完成时关闭弹窗，该回调不会触发。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| shadow12+ | [ShadowOptions](ts-universal-attributes-image-effect.md#shadowoptions对象说明) | [ShadowStyle](ts-universal-attributes-image-effect.md#shadowstyle10枚举说明) | 否 | 是 | 设置弹窗背板的阴影。  当设备为2in1时，默认场景下获焦阴影值为ShadowStyle.OUTER\_FLOATING\_MD，失焦为ShadowStyle.OUTER\_FLOATING\_SM。其他设备默认无阴影。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| dateTimeOptions12+ | [DateTimeOptions](js-apis-intl.md#datetimeoptionsdeprecated) | 否 | 是 | 设置时分是否显示前导0，目前只支持设置hour和minute参数，仅当showTime为true时生效。  默认值：  hour: 24小时制默认为"2-digit"，设置hour是否按照2位数字显示，如果实际数值小于10，则会补充前导0并显示，即为"0X"；12小时制默认为"numeric"，即没有前导0。可选值为"numeric"或"2-digit"，传入其他值时按默认值处理。  minute: 默认为"2-digit"，设置minute是否按照2位数字显示，如果实际数值小于10，则会补充前导0并显示，即为"0X"。可选值为"numeric"或"2-digit"，传入其他值时按默认值处理。  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| enableHoverMode14+ | boolean | 否 | 是 | 是否响应悬停态。悬停态指折叠屏等设备处于悬停折叠状态时的交互模式，而非鼠标悬停。  - true：响应悬停态。  - false：不响应悬停态。  默认值：false  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| hoverModeArea14+ | [HoverModeAreaType](ts-universal-attributes-sheet-transition.md#hovermodeareatype14) | 否 | 是 | 设置悬停态下弹窗默认展示区域，仅在enableHoverMode为true时生效。  默认值：HoverModeAreaType.BOTTOM\_SCREEN  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| enableHapticFeedback18+ | boolean | 否 | 是 | 设置是否开启触控反馈。  - true：开启触控反馈（当需要为用户提供操作反馈时选择）。  - false：不开启触控反馈（当不需要触控反馈或设备不支持时选择）。  默认值：true  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。  **说明：**  1. 设置为true后，其生效情况取决于系统的硬件是否支持。  2. 开启触控反馈时，需要在工程的src/main/module.json5文件的"module"内配置requestPermissions字段开启振动权限，配置如下：  "requestPermissions": [{"name": "ohos.permission.VIBRATE"}] |
| canLoop20+ | boolean | 否 | 是 | 设置是否可循环滚动。  - true：可循环，年份随着月份的循环滚动进行联动加减，月份随着日的循环滚动进行联动加减。  - false：不可循环，年、月、日到达本列的顶部或底部时，无法再进行滚动，年、月、日之间也无法再联动加减。  默认值：true  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| systemMaterial | [SystemUiMaterial](ts-universal-attributes-image-effect.md#systemuimaterial) | 否 | 是 | 设置弹窗的系统材质。  **说明：**  - 默认值为ImmersiveOptions的style为ImmersiveStyle.ULTRA\_THICK的ImmersiveMaterial对象，设置undefined时与默认值保持一致。不同的材质具有不同的效果。关于ImmersiveMaterial的详细说明，请参考[SystemUiMaterial](ts-universal-attributes-image-effect.md#systemuimaterial)类型定义。  - 该接口影响背景色[backgroundColor](ts-universal-attributes-background.md#backgroundcolor)、背景模糊[backgroundBlurStyle](ts-universal-attributes-background.md#backgroundblurstyle9)、背景模糊效果[backgroundBlurStyleOptions](ts-universal-attributes-background.md#backgroundblurstyleoptions10对象说明)、背景效果[backgroundEffect](ts-universal-attributes-background.md#backgroundeffect11)、边框颜色[borderColor](ts-universal-attributes-border.md#bordercolor)、边框宽度[borderWidth](ts-universal-attributes-border.md#borderwidth)、阴影[shadow](ts-universal-attributes-image-effect.md#shadow)，当设置系统材质时，上述接口不生效。  **起始版本：** 26.0.0  **模型约束：** 此接口仅可在Stage模型下使用。  **元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。 |

## LunarSwitchStyle14+对象说明

定义了DatePickerDialog组件中农历切换开关的样式。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| selectedColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 设置开关开启时开关的背景颜色。  默认值：$r('sys.color.ohos\_id\_color\_text\_primary\_actived')。 |
| unselectedColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 设置开关未开启时开关的边框颜色。  默认值：$r('sys.color.ohos\_id\_color\_switch\_outline\_off')。 |
| strokeColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 设置开关内部图标颜色。  默认值：Color.White。 |

## 示例

**说明** 

推荐通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[showDatePickerDialog](arkts-apis-uicontext-uicontext.md#showdatepickerdialog)来明确UI的执行上下文。

### 示例1（设置显示时间）

该示例通过showTime、useMilitaryTime、dateTimeOptions设置显示时间。

```ts
// xxx.ets
@Entry
@Component
struct DatePickerDialogExample {
  selectedDate: Date = new Date('2010-01-01');

  build() {
    Column() {
      Button('DatePickerDialog')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showDatePickerDialog({
            start: new Date('2000-01-01'),
            end: new Date('2100-12-31'),
            selected: this.selectedDate,
            showTime: true,
            useMilitaryTime: false,
            dateTimeOptions: { hour: 'numeric', minute: '2-digit' },
            onDateAccept: (value: Date) => {
              // 保存按下确定按钮时的日期，这样当弹窗再次弹出时显示选中的是上一次确定的日期
              this.selectedDate = value;
              console.info('DatePickerDialog:onDateAccept()' + value.toString());
            },
            onCancel: () => {
              console.info('DatePickerDialog:onCancel()');
            },
            onDateChange: (value: Date) => {
              console.info('DatePickerDialog:onDateChange()' + value.toString());
            },
            onDidAppear: () => {
              console.info('DatePickerDialog:onDidAppear()');
            },
            onDidDisappear: () => {
              console.info('DatePickerDialog:onDidDisappear()');
            },
            onWillAppear: () => {
              console.info('DatePickerDialog:onWillAppear()');
            },
            onWillDisappear: () => {
              console.info('DatePickerDialog:onWillDisappear()');
            }
          })
        })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/sr0Iu14TSDucBnr9zM3PxQ/zh-cn_image_0000002736315323.gif)

### 示例2（自定义样式）

该示例通过配置disappearTextStyle、textStyle、selectedTextStyle、acceptButtonStyle、cancelButtonStyle实现了自定义文本以及按钮样式。

```ts
// xxx.ets
@Entry
@Component
struct DatePickerDialogExample {
  selectedDate: Date = new Date('2010-01-01');

  build() {
    Column() {
      Button('DatePickerDialog')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showDatePickerDialog({
            start: new Date('2000-01-01'),
            end: new Date('2100-12-31'),
            selected: this.selectedDate,
            disappearTextStyle: { color: '#297bec', font: { size: '20fp', weight: FontWeight.Bold } },
            textStyle: { color: Color.Black, font: { size: '18fp', weight: FontWeight.Normal } },
            selectedTextStyle: { color: Color.Blue, font: { size: '26fp', weight: FontWeight.Regular } },
            acceptButtonStyle: {
              type: ButtonType.Normal,
              style: ButtonStyleMode.NORMAL,
              role: ButtonRole.NORMAL,
              fontColor: 'rgb(81, 81, 216)',
              fontSize: '26fp',
              fontWeight: FontWeight.Bolder,
              fontStyle: FontStyle.Normal,
              fontFamily: 'sans-serif',
              backgroundColor: '#A6ACAF',
              borderRadius: 20
            },
            cancelButtonStyle: {
              type: ButtonType.Normal,
              style: ButtonStyleMode.NORMAL,
              role: ButtonRole.NORMAL,
              fontColor: Color.Blue,
              fontSize: '16fp',
              fontWeight: FontWeight.Normal,
              fontStyle: FontStyle.Italic,
              fontFamily: 'sans-serif',
              backgroundColor: '#50182431',
              borderRadius: 10
            },
            onDateAccept: (value: Date) => {
              // 保存按下确定按钮时的日期，这样当弹窗再次弹出时显示选中的是上一次确定的日期
              this.selectedDate = value;
              console.info('DatePickerDialog:onDateAccept()' + value.toString());
            },
            onCancel: () => {
              console.info('DatePickerDialog:onCancel()');
            },
            onDateChange: (value: Date) => {
              console.info('DatePickerDialog:onDateChange()' + value.toString());
            },
            onDidAppear: () => {
              console.info('DatePickerDialog:onDidAppear()');
            },
            onDidDisappear: () => {
              console.info('DatePickerDialog:onDidDisappear()');
            },
            onWillAppear: () => {
              console.info('DatePickerDialog:onWillAppear()');
            },
            onWillDisappear: () => {
              console.info('DatePickerDialog:onWillDisappear()');
            }
          });
        })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/Pk47JR6ZSjCKhmnYMuXE7Q/zh-cn_image_0000002706676284.png)

**说明** 

如需完全自定义实现日期滑动选择器弹窗，可以通过先使用[自定义弹窗 (CustomDialog)](ts-methods-custom-dialog-box.md)，然后使用[DatePicker](ts-basic-components-datepicker.md)组件来实现。

### 示例3（悬停态弹窗）

该示例展示了在折叠屏悬停态下设置弹窗布局区域的效果。

```ts
@Entry
@Component
struct DatePickerDialogExample {
  selectedDate: Date = new Date('2010-01-01');

  build() {
    Column() {
      Button('DatePickerDialog')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showDatePickerDialog({
            start: new Date('2000-01-01'),
            end: new Date('2100-12-31'),
            selected: this.selectedDate,
            showTime: true,
            useMilitaryTime: false,
            disappearTextStyle: { color: Color.Pink, font: { size: '22fp', weight: FontWeight.Bold }},
            textStyle: { color: '#ff00ff00', font: { size: '18fp', weight: FontWeight.Normal }},
            selectedTextStyle: { color: '#ff182431', font: { size: '14fp', weight: FontWeight.Regular }},
            onDateAccept: (value: Date) => {
              // 保存按下确定按钮时的日期，这样当弹窗再次弹出时显示选中的是上一次确定的日期
              this.selectedDate = value;
              console.info('DatePickerDialog:onDateAccept()' + value.toString());
            },
            onCancel: () => {
              console.info('DatePickerDialog:onCancel()');
            },
            onDateChange: (value: Date) => {
              console.info('DatePickerDialog:onDateChange()' + value.toString());
            },
            onDidAppear: () => {
              console.info('DatePickerDialog:onDidAppear()');
            },
            onDidDisappear: () => {
              console.info('DatePickerDialog:onDidDisappear()');
            },
            onWillAppear: () => {
              console.info('DatePickerDialog:onWillAppear()');
            },
            onWillDisappear: () => {
              console.info('DatePickerDialog:onWillDisappear()');
            },
            enableHoverMode: true,
            hoverModeArea: HoverModeAreaType.TOP_SCREEN
          });
        })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/sNPR8daqTX2dYInATRZSQw/zh-cn_image_0000002736435371.gif)

### 示例4（设置弹窗位置）

该示例通过alignment、offset设置弹窗的位置。

```ts
// xxx.ets
@Entry
@Component
struct DatePickerDialogExample {
  selectedDate: Date = new Date('2010-01-01');

  build() {
    Column() {
      Button('DatePickerDialog')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showDatePickerDialog({
            start: new Date('2000-01-01'),
            end: new Date('2100-12-31'),
            selected: this.selectedDate,
            alignment: DialogAlignment.Center,
            offset: { dx: 20, dy: 0 },
            onDateAccept: (value: Date) => {
              // 保存按下确定按钮时的日期，这样当弹窗再次弹出时显示选中的是上一次确定的日期
              this.selectedDate = value;
              console.info('DatePickerDialog:onDateAccept()' + value.toString());
            }
          });
        })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/lIjLHXDvS1GwiKWgE6NvuQ/zh-cn_image_0000002706836220.png)

### 示例5（设置遮蔽区）

该示例通过maskRect设置遮蔽区。

```ts
// xxx.ets
@Entry
@Component
struct DatePickerDialogExample {
  selectedDate: Date = new Date('2010-01-01');

  build() {
    Column() {
      Button('DatePickerDialog')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showDatePickerDialog({
            start: new Date('2000-01-01'),
            end: new Date('2100-12-31'),
            selected: this.selectedDate,
            maskRect: {
              x: 30,
              y: 60,
              width: '100%',
              height: '60%'
            },
            onDateAccept: (value: Date) => {
              // 保存按下确定按钮时的日期，这样当弹窗再次弹出时显示选中的是上一次确定的日期
              this.selectedDate = value;
              console.info('DatePickerDialog:onDateAccept()' + value.toString());
            }
          });
        })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/m5nuF-BbQNuMRb-Sf0Xx0Q/zh-cn_image_0000002736315325.png)

### 示例6（设置弹窗背板）

该示例通过backgroundColor、backgroundBlurStyle、shadow设置弹窗背板。

```ts
// xxx.ets
@Entry
@Component
struct DatePickerDialogExample {
  selectedDate: Date = new Date('2010-01-01');

  build() {
    Column() {
      Button('DatePickerDialog')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showDatePickerDialog({
            start: new Date('2000-01-01'),
            end: new Date('2100-12-31'),
            selected: this.selectedDate,
            backgroundColor: 'rgb(204, 226, 251)',
            backgroundBlurStyle: BlurStyle.NONE,
            shadow: ShadowStyle.OUTER_FLOATING_SM,
            onDateAccept: (value: Date) => {
              // 保存按下确定按钮时的日期，这样当弹窗再次弹出时显示选中的是上一次确定的日期
              this.selectedDate = value;
              console.info('DatePickerDialog:onDateAccept()' + value.toString());
            }
          });
        })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/T_-DDXz1R7SDbO9fXCiFIQ/zh-cn_image_0000002706676286.png)

### 示例7（设置公历农历）

该示例通过lunar、lunarSwitch设置弹窗显示公历或农历。

```ts
// xxx.ets
@Entry
@Component
struct DatePickerDialogExample {
  selectedDate: Date = new Date('2010-11-09');

  build() {
    Column() {
      Button('DatePickerDialog')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showDatePickerDialog({
            start: new Date('2000-01-01'),
            end: new Date('2100-12-31'),
            selected: this.selectedDate,
            lunar: false,
            onDateAccept: (value: Date) => {
              // 保存按下确定按钮时的日期，这样当弹窗再次弹出时显示选中的是上一次确定的日期
              this.selectedDate = value;
              console.info('DatePickerDialog:onDateAccept()' + value.toString());
            }
          });
        })

      Button('Lunar DatePickerDialog')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showDatePickerDialog({
            start: new Date('2000-01-01'),
            end: new Date('2100-12-31'),
            selected: this.selectedDate,
            lunar: true,
            lunarSwitch: true,
            onDateAccept: (value: Date) => {
              this.selectedDate = value;
              console.info('DatePickerDialog:onDateAccept()' + value.toString());
            }
          });
        })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/8cYXb20BSWymMicUPbXPOw/zh-cn_image_0000002736435373.gif)

### 示例8（设置显示月、日列）

该示例通过配置mode参数实现显示月、日两列。

```ts
// xxx.ets
@Entry
@Component
struct DatePickerDialogExample {
  selectedDate: Date = new Date('2010-10-13');

  build() {
    Column() {
      Button('DatePickerDialog')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showDatePickerDialog({
            start: new Date('2000-01-01'),
            end: new Date('2100-12-31'),
            selected: this.selectedDate,
            mode: DatePickerMode.MONTH_AND_DAY,
            onDateAccept: (value: Date) => {
              // 保存按下确定按钮时的日期，这样当弹窗再次弹出时显示选中的是上一次确定的日期
              this.selectedDate = value;
              console.info('DatePickerDialog:onDateAccept()' + value.toString());
            }
          });
        })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/kpA8dtOyQmaM0TCQw-aCCQ/zh-cn_image_0000002706836222.gif)

### 示例9（设置循环滚动）

从API version 20开始，可以通过配置canLoop参数设置是否循环滚动。

```ts
// xxx.ets
@Entry
@Component
struct DatePickerDialogExample {
  @State isLoop: boolean = true;
  selectedDate: Date = new Date('2009-12-31');

  build() {
    Column() {
      Button('DatePickerDialog')
        .margin(20)
        .onClick(() => {
          this.getUIContext().showDatePickerDialog({
            start: new Date('2000-01-01'),
            end: new Date('2100-12-31'),
            selected: this.selectedDate,
            canLoop: this.isLoop,
            onDateAccept: (value: Date) => {
              // 保存按下确定按钮时的日期，这样当弹窗再次弹出时显示选中的是上一次确定的日期
              this.selectedDate = value;
              console.info('DatePickerDialog:onDateAccept()' + value.toString());
            }
          });
        })

      Row() {
        Text('循环滚动').fontSize(20)
        Toggle({ type: ToggleType.Switch, isOn: true })
          .onChange((isOn: boolean) => {
            this.isLoop = isOn;
          })
      }.position({ x: '60%', y: '40%' })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/vRA5BmKtSBeW3GNQ0QjRiA/zh-cn_image_0000002736315327.gif)

### 示例10（自定义背景模糊效果参数）

从API version 19开始，可以通过配置[backgroundBlurStyleOptions](ts-methods-datepicker-dialog.md#datepickerdialogoptions对象说明)，实现自定义背景模糊效果。

```ts
@Entry
@Component
struct DatePickerDialogExample {
  selectedDate: Date = new Date('2010-01-01');

  build() {
    Stack({ alignContent: Alignment.Top }) {
      // $r('app.media.bg')需要替换为开发者所需的图像资源文件。
      Image($r('app.media.bg'))
      Column() {
        Button('DatePickerDialog')
          .margin(20)
          .onClick(() => {
            this.getUIContext().showDatePickerDialog({
              start: new Date('2000-01-01'),
              end: new Date('2100-12-31'),
              selected: this.selectedDate,
              backgroundColor: undefined,
              backgroundBlurStyle: BlurStyle.Thin,
              backgroundBlurStyleOptions: {
                colorMode: ThemeColorMode.LIGHT,
                adaptiveColor: AdaptiveColor.AVERAGE,
                scale: 1,
                blurOptions: { grayscale: [20, 20] },
              },
            });
          })
      }.width('100%')
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/Wj85HqYvTeWafqu-mMSQ0Q/zh-cn_image_0000002706676288.png)

### 示例11（自定义背景效果参数）

从API version 19开始，该示例通过配置[backgroundEffect](ts-methods-datepicker-dialog.md#datepickerdialogoptions对象说明)，实现自定义背景效果。

```ts
@Entry
@Component
struct DatePickerDialogExample {
  selectedDate: Date = new Date('2010-01-01');

  build() {
    Stack({ alignContent: Alignment.Top }) {
      // $r('app.media.bg')需要替换为开发者所需的图像资源文件。
      Image($r('app.media.bg'))
      Column() {
        Button('DatePickerDialog')
          .margin(20)
          .onClick(() => {
            this.getUIContext().showDatePickerDialog({
              start: new Date('2000-01-01'),
              end: new Date('2100-12-31'),
              selected: this.selectedDate,
              backgroundColor: undefined,
              backgroundBlurStyle: BlurStyle.Thin,
              backgroundEffect: {
                radius: 60,
                saturation: 0,
                brightness: 1,
                color: Color.White,
                blurOptions: { grayscale: [20, 20] }
              },
            });
          })
      }.width('100%')
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/BQ-q3k2wQ6yTFLha49ojVQ/zh-cn_image_0000002736435375.png)

### 示例12（设置系统材质）

该示例通过配置[systemMaterial](ts-methods-datepicker-dialog.md#datepickerdialogoptions对象说明)，实现系统材质效果。

从API版本26.0.0开始，在DatePickerDialogOptions中新增了systemMaterial属性。

```ts
import { uiMaterial } from '@kit.ArkUI';

@Entry
@Component
struct DatePickerDialogExample {
  selectedDate: Date = new Date('2010-01-01');

  build() {
    Stack({ alignContent: Alignment.Top }) {
      Column() {
        Button('DatePickerDialog')
          .margin(20)
          .onClick(() => {
            this.getUIContext().showDatePickerDialog({
              selected: this.selectedDate,
              systemMaterial: new uiMaterial.ImmersiveMaterial({ style: uiMaterial.ImmersiveStyle.ULTRA_THICK })
            });
          })
      }.width('100%')
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/-kCrCBGSRnOdHXfvvXiWMQ/zh-cn_image_0000002706836224.png)
