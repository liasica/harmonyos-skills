---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-datepicker
title: DatePicker
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 按钮与选择 > DatePicker
category: harmonyos-references
scraped_at: 2026-04-28T08:01:43+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:20c592c6848a16e144c9977674f613bc0d6aafcdaad6db5c80abc4fe6ba430f2
---

滑动选择日期的组件。

说明

* 该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件不建议开发者在动效过程中修改属性数据。
* 最大显示行数在横、竖屏模式下存在差异。竖屏时默认为5行，横屏时依赖系统配置，未配置时默认显示为3行。可通过如下参数查看具体配置值$r('sys.float.ohos\_id\_picker\_show\_count\_landscape')。

## 子组件

PhonePC/2in1TabletTVWearable

无

## 接口

PhonePC/2in1TabletTVWearable

DatePicker(options?: DatePickerOptions)

根据指定日期范围创建日期选择器。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [DatePickerOptions](ts-basic-components-datepicker.md#datepickeroptions对象说明) | 否 | 配置日期选择器组件的参数。 |

## DatePickerOptions对象说明

PhonePC/2in1TabletTVWearable

日期选择器组件的参数说明。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| start | Date | 否 | 是 | 指定选择器的起始日期。  默认值：Date('1970-1-1')  取值范围：[Date('1900-01-31'), Date('2100-12-31')]  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| end | Date | 否 | 是 | 指定选择器的结束日期。  默认值：Date('2100-12-31')  取值范围：[Date('1900-01-31'), Date('2100-12-31')]  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| selected | Date | 否 | 是 | 设置选中项的日期。  默认值：当前系统日期。  取值范围：[Date('1900-01-31'), Date('2100-12-31')]  从API version 10开始，该参数支持[$$](../harmonyos-guides/arkts-two-way-sync.md)双向绑定变量。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| mode18+ | [DatePickerMode](ts-basic-components-datepicker.md#datepickermode18枚举说明) | 否 | 是 | 设置日期展示模式。  默认值：DatePickerMode.DATE，显示年、月、日三列。  在[DatePickerDialog](ts-methods-datepicker-dialog.md)中，当[DatePickerDialogOptions](ts-methods-datepicker-dialog.md#datepickerdialogoptions对象说明)的showTime设置为true时，此参数不生效，默认显示年、月、日三列。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

说明

* Date的使用请参考[TimePickerOptions](ts-basic-components-timepicker.md#timepickeroptions对象说明)。
* 在DatePicker组件滑动过程中修改DatePickerOptions中的属性，会导致这些属性无法生效。

**起始日期、结束日期和选中日期的异常情形说明：**

| 异常情形 | 对应结果 |
| --- | --- |
| 起始日期晚于结束日期，选中日期未设置。 | 起始日期、结束日期和选中日期都为默认值。 |
| 起始日期晚于结束日期，选中日期早于起始日期默认值。 | 起始日期、结束日期都为默认值，选中日期为起始日期默认值。 |
| 起始日期晚于结束日期，选中日期晚于结束日期默认值。 | 起始日期、结束日期都为默认值，选中日期为结束日期默认值。 |
| 起始日期晚于结束日期，选中日期在起始日期与结束日期默认值范围内。 | 起始日期、结束日期都为默认值，选中日期为设置的值。 |
| 选中日期早于起始日期。 | 选中日期为起始日期。 |
| 选中日期晚于结束日期。 | 选中日期为结束日期。 |
| 起始日期晚于当前系统日期，选中日期未设置。 | 选中日期为起始日期。 |
| 结束日期早于当前系统日期，选中日期未设置。 | 选中日期为结束日期。 |
| 日期格式不符合规范，如‘1999-13-32’。 | 取默认值。 |
| 起始日期或结束日期早于系统有效范围。 | 起始日期或结束日期取起始日期默认值。 |
| 起始日期或结束日期晚于系统有效范围。 | 起始日期或结束日期取结束日期默认值。 |
| 起始日期与结束日期同时早于系统有效范围。 | 起始日期与结束日期取系统有效范围最早日期。 |
| 起始日期与结束日期同时晚于系统有效范围。 | 起始日期与结束日期取系统有效范围最晚日期。 |

说明

先处理起始日期与结束日期的异常情形，再处理选中日期的异常情形。

## DatePickerMode18+枚举说明

PhonePC/2in1TabletTVWearable

设置日期展示模式。

**元服务API：** 从API version 18开始，该类型支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DATE | 0 | 显示年、月、日三列。 |
| YEAR\_AND\_MONTH | 1 | 显示年、月二列。 |
| MONTH\_AND\_DAY | 2 | 显示月、日二列。  在此模式下，年份始终保持不变。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### lunar

PhonePC/2in1TabletTVWearable

lunar(value: boolean)

设置日期是否显示为农历。

说明

仅在简体中文和繁体中文语言环境下生效，其他语言环境下设置该属性无效果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 日期是否显示为农历。  - true：显示为农历。  - false：不显示为农历。  默认值：false |

### lunar18+

PhonePC/2in1TabletTVWearable

lunar(isLunar: Optional<boolean>)

设置弹窗的日期是否显示为农历。与[lunar](ts-basic-components-datepicker.md#lunar)相比，isLunar参数新增了对undefined类型的支持。

说明

仅在简体中文和繁体中文语言环境下生效，其他语言环境下设置该属性无效果。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isLunar | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 日期是否显示为农历。  - true：显示为农历。  - false：不显示为农历。  默认值：false  当isLunar的值为undefined时，使用默认值。 |

### disappearTextStyle10+

PhonePC/2in1TabletTVWearable

disappearTextStyle(value: PickerTextStyle)

设置边缘项（以选中项为基准向上或向下的第二项）的文本样式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PickerTextStyle](ts-picker-common.md#pickertextstyle对象说明) | 是 | 边缘项的文本颜色、字号、字体粗细。  默认值：  {  color: '#ff182431',  font: {  size: '14fp',  weight: FontWeight.Regular  }  } |

说明

若选中项向上或向下的可视项数低于两项则无对应边缘项。

### disappearTextStyle18+

PhonePC/2in1TabletTVWearable

disappearTextStyle(style: Optional<PickerTextStyle>)

设置边缘项（以选中项为基准向上或向下的第二项）的文本样式。与[disappearTextStyle10+](ts-basic-components-datepicker.md#disappeartextstyle10)相比，style参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[PickerTextStyle](ts-picker-common.md#pickertextstyle对象说明)> | 是 | 边缘项的文本颜色、字号、字体粗细。  默认值：  {  color: '#ff182431',  font: {  size: '14fp',  weight: FontWeight.Regular  }  }  当style的值为undefined时，使用默认值。 |

说明

若选中项向上或向下的可视项数低于两项则无对应边缘项。

### textStyle10+

PhonePC/2in1TabletTVWearable

textStyle(value: PickerTextStyle)

设置待选项（以选中项为基准向上或向下的第一项）的文本样式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PickerTextStyle](ts-picker-common.md#pickertextstyle对象说明) | 是 | 待选项的文本颜色、字号、字体粗细。  默认值：  {  color: '#ff182431',  font: {  size: '16fp',  weight: FontWeight.Regular  }  } |

说明

若选中项向上或向下可视项数低于一项则无对应待选项。

### textStyle18+

PhonePC/2in1TabletTVWearable

textStyle(style: Optional<PickerTextStyle>)

设置待选项（以选中项为基准向上或向下的第一项）的文本样式。与[textStyle10+](ts-basic-components-datepicker.md#textstyle10)相比，style参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[PickerTextStyle](ts-picker-common.md#pickertextstyle对象说明)> | 是 | 待选项的文本颜色、字号、字体粗细。  默认值：  {  color: '#ff182431',  font: {  size: '16fp',  weight: FontWeight.Regular  }  }  当style的值为undefined时，使用默认值。 |

说明

若选中项向上或向下可视项数低于一项则无对应待选项。

### selectedTextStyle10+

PhonePC/2in1TabletTVWearable

selectedTextStyle(value: PickerTextStyle)

设置选中项的文本样式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PickerTextStyle](ts-picker-common.md#pickertextstyle对象说明) | 是 | 选中项的文本颜色、字号、字体粗细。  默认值：  {  color: '#ff007dff',  font: {  size: '20fp',  weight: FontWeight.Medium  }  } |

### selectedTextStyle18+

PhonePC/2in1TabletTVWearable

selectedTextStyle(style: Optional<PickerTextStyle>)

设置选中项的文本样式。与[selectedTextStyle10+](ts-basic-components-datepicker.md#selectedtextstyle10)相比，style参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[PickerTextStyle](ts-picker-common.md#pickertextstyle对象说明)> | 是 | 选中项的文本颜色、字号、字体粗细。  默认值：  {  color: '#ff007dff',  font: {  size: '20fp',  weight: FontWeight.Medium  }  }  当style的值为undefined时，使用默认值。 |

### enableHapticFeedback18+

PhonePC/2in1TabletTVWearable

enableHapticFeedback(enable: Optional<boolean>)

设置是否开启触控反馈。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 设置是否开启触控反馈。  - true：开启触控反馈。  - false：不开启触控反馈。  默认值：true  设置为true后，其生效情况取决于系统的硬件是否支持。  当enable的值为undefined时，使用默认值。 |

开启触控反馈时，需要在工程的src/main/module.json5文件的"module"内配置requestPermissions字段开启振动权限，配置如下：

```
1. "requestPermissions": [
2. {
3. "name": "ohos.permission.VIBRATE",
4. }
5. ]
```

### digitalCrownSensitivity18+

PhonePC/2in1TabletTVWearable

digitalCrownSensitivity(sensitivity: Optional<CrownSensitivity>)

设置表冠灵敏度。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sensitivity | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[CrownSensitivity](ts-appendix-enums.md#crownsensitivity18)> | 是 | 表冠响应灵敏度。  默认值：CrownSensitivity.MEDIUM，响应速度适中。 |

说明

用于穿戴设备圆形屏幕使用。组件响应[表冠事件](ts-universal-events-crown.md)，需要先获取焦点。

### canLoop20+

PhonePC/2in1TabletTVWearable

canLoop(isLoop: Optional<boolean>)

设置是否可循环滚动。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isLoop | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 是否可循环滚动。  - true：可循环滚动，年份随着月份的循环滚动进行联动加减，月份随着日的循环滚动进行联动加减。  - false：不可循环滚动，年、月、日到达本列的顶部或底部时，无法再进行滚动，年、月、日之间也无法再联动加减。  默认值：true  当isLoop的值为undefined时，使用默认值。 |

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](ts-component-general-events.md)外，还支持以下事件：

### onChange(deprecated)

PhonePC/2in1TabletTVWearable

onChange(callback: (value: DatePickerResult) => void)

滑动DatePicker文本内容后，选项完全归位至选中项位置时，触发该回调。不能通过双向绑定的状态变量触发。

从API version 8开始支持，从API version 10开始废弃，建议使用[onDateChange](ts-basic-components-datepicker.md#ondatechange10)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | (value: [DatePickerResult](ts-basic-components-datepicker.md#datepickerresult对象说明)) => void | 是 | 返回选中的时间。 |

### onDateChange10+

PhonePC/2in1TabletTVWearable

onDateChange(callback: Callback<Date>)

滑动DatePicker文本内容后，选项完全归位至选中项位置时，触发该回调。不能通过双向绑定的状态变量触发。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](ts-types.md#callback12)<Date> | 是 | 返回选中的时间，年、月、日为选中的日期，时、分取决于当前系统时间的时、分，秒恒为00。 |

### onDateChange18+

PhonePC/2in1TabletTVWearable

onDateChange(callback: Optional<Callback<Date>>)

滑动DatePicker文本内容后，选项完全归位至选中项位置时，触发该回调。不能通过双向绑定的状态变量触发。与[onDateChange10+](ts-basic-components-datepicker.md#ondatechange10)相比，callback参数新增了对undefined类型的支持。

说明

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[Callback](ts-types.md#callback12)<Date>> | 是 | 返回选中的时间，年、月、日为选中的日期，时、分取决于当前系统时间的时、分，秒恒为00。  当callback的值为undefined时，不使用回调函数。 |

## DatePickerResult对象说明

PhonePC/2in1TabletTVWearable

日期选择器返回的时间格式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| year | number | 否 | 是 | 选中日期的年。  取值范围：与设置的start、end有关，如果没有设置start、end，取值范围为[1970, 2100]。 |
| month | number | 否 | 是 | 选中日期的月的索引值，索引从0开始，0表示1月，11表示12月。  取值范围：与设置的start、end有关，如果没有设置start、end，取值范围为[0, 11]。 |
| day | number | 否 | 是 | 选中日期的日。  取值范围：与设置的start、end有关，如果没有设置start、end，取值范围为[1, 31]。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（切换公历农历）

该示例实现了日期选择器组件，点击按钮可以切换公历农历。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct DatePickerExample {
5. @State isLunar: boolean = false;
6. private selectedDate: Date = new Date('2021-08-08');

8. build() {
9. Column() {
10. Button('切换公历农历')
11. .margin({ top: 30, bottom: 30 })
12. .onClick(() => {
13. this.isLunar = !this.isLunar;
14. })
15. DatePicker({
16. start: new Date('1970-1-1'),
17. end: new Date('2100-1-1'),
18. selected: this.selectedDate
19. })
20. .lunar(this.isLunar)
21. .onDateChange((value: Date) => {
22. this.selectedDate = value;
23. console.info('select current date is: ' + value.toString());
24. })

26. }.width('100%')
27. }
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/MqfOtYJRQRu1pWfaoBNxDQ/zh-cn_image_0000002552959708.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000141Z&HW-CC-Expire=86400&HW-CC-Sign=EF4E44CFDC3C4FBC6B5D96D78068AE12C52D1A99901216626D17BA8F68B1A7AE)

### 示例2（设置文本样式）

该示例通过配置[disappearTextStyle](ts-basic-components-datepicker.md#disappeartextstyle10)、[textStyle](ts-basic-components-datepicker.md#textstyle10)、[selectedTextStyle](ts-basic-components-datepicker.md#selectedtextstyle10)设置文本样式。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct DatePickerExample {
5. private selectedDate: Date = new Date('2021-08-08');

7. build() {
8. Column() {
9. DatePicker({
10. start: new Date('1970-1-1'),
11. end: new Date('2100-1-1'),
12. selected: this.selectedDate
13. })
14. .disappearTextStyle({ color: Color.Gray, font: { size: '16fp', weight: FontWeight.Bold } })
15. .textStyle({ color: '#ff182431', font: { size: '18fp', weight: FontWeight.Normal } })
16. .selectedTextStyle({ color: '#ff0000FF', font: { size: '26fp', weight: FontWeight.Regular, family: "HarmonyOS Sans", style: FontStyle.Normal } })
17. .onDateChange((value: Date) => {
18. this.selectedDate = value;
19. console.info('select current date is: ' + value.toString());
20. })

22. }.width('100%')
23. }
24. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/S3NUJJ6hR2Cu4hc81D-NXQ/zh-cn_image_0000002583479709.png?HW-CC-KV=V1&HW-CC-Date=20260428T000141Z&HW-CC-Expire=86400&HW-CC-Sign=9D5404C419C16F390B26F1C5BF1F8BA4A1BE40E9B4C7AA39B8AF343CBD9333BB)

### 示例3（设置显示年、月和月、日列）

该示例通过配置mode参数实现显示年、月和月、日列。

从API version 18开始，新增了[DatePickerOptions](ts-basic-components-datepicker.md#datepickeroptions对象说明)的mode属性。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct DatePickerExample {
5. @State isLunar: boolean = false;
6. private selectedDate: Date = new Date('2025-01-15');
7. @State datePickerModeList: (DatePickerMode)[] = [
8. DatePickerMode.DATE,
9. DatePickerMode.YEAR_AND_MONTH,
10. DatePickerMode.MONTH_AND_DAY,
11. ];
12. @State datePickerModeIndex: number = 0;

14. build() {
15. Column() {
16. Button('切换公历农历')
17. .margin({ top: 30, bottom: 30 })
18. .onClick(() => {
19. this.isLunar = !this.isLunar;
20. })
21. DatePicker({
22. start: new Date('1970-1-1'),
23. end: new Date('2100-1-1'),
24. selected: this.selectedDate,
25. mode:this.datePickerModeList[this.datePickerModeIndex]
26. })
27. .lunar(this.isLunar)
28. .onDateChange((value: Date) => {
29. this.selectedDate = value;
30. console.info('select current date is: ' + value.toString());
31. })

33. Button('mode :' + this.datePickerModeIndex).margin({ top: 20 })
34. .onClick(() => {
35. this.datePickerModeIndex++;
36. if(this.datePickerModeIndex >= this.datePickerModeList.length){
37. this.datePickerModeIndex = 0;
38. }
39. })
40. }.width('100%')
41. }
42. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/F8TP7WuXQE6qfkSy4blyig/zh-cn_image_0000002552800060.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000141Z&HW-CC-Expire=86400&HW-CC-Sign=7658C65648D1B7852EC68A6D2B3EE5EA6835F5EE76E9AF46746E30125BE08684)

### 示例4（设置循环滚动）

从API version 20开始，可以通过配置[canLoop](ts-basic-components-datepicker.md#canloop20)参数设置DatePicker是否循环滚动。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct DatePickerExample {
5. @State isLoop: boolean = true;
6. selectedDate: Date = new Date("2010-1-1");

8. build() {
9. Column() {
10. DatePicker({
11. start: new Date("2000-1-1"),
12. end: new Date("2100-12-31"),
13. selected: this.selectedDate,
14. })
15. .canLoop(this.isLoop)
16. .onDateChange((value: Date) => {
17. console.info("DatePicker:onDateChange()" + value.toString());
18. })

20. Row() {
21. Text('循环滚动').fontSize(20)
22. Toggle({ type: ToggleType.Switch, isOn: true })
23. .onChange((isOn: boolean) => {
24. this.isLoop = isOn;
25. })
26. }.position({ x: '60%', y: '40%' })
27. }.width('100%')
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/4yjWts1BTwaelx946d7vow/zh-cn_image_0000002583439755.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000141Z&HW-CC-Expire=86400&HW-CC-Sign=FFAC82D1DBE22F3969585C42D59665AF8A9174E476B1D604ED7027C36913E784)
