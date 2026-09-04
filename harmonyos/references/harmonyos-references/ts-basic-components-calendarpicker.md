---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-calendarpicker
title: CalendarPicker
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 按钮与选择 > CalendarPicker
category: harmonyos-references
scraped_at: 2026-09-05T06:17:13+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:15be0ebf4c8c2b9c7c8d823a80a345ebb53286954a2456629d3b4f8c931783c5
---

日历选择器组件，提供下拉日历弹窗，用户可快速选择日期。适用于需要用户选择具体日期的场景，如预订系统、日程安排、日期筛选等，提供直观的日历视图，提升用户日期输入体验。

**说明** 

* 该组件从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 该组件从API版本26.0.0开始支持[WithTheme](ts-container-with-theme.md)。

## 子组件

无

## 接口

CalendarPicker(options?: CalendarOptions)

日历选择器。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [CalendarOptions](ts-basic-components-calendarpicker.md#calendaroptions对象说明) | 否 | 配置日历选择器组件的参数。未设置该参数时使用默认配置。 |

## 属性

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### edgeAlign

edgeAlign(alignType: CalendarAlign, offset?: Offset)

设置选择器与入口组件的对齐方式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| alignType | [CalendarAlign](ts-basic-components-calendarpicker.md#calendaralign枚举说明) | 是 | 对齐方式的类型。  默认值：CalendarAlign.END |
| offset | [Offset](ts-types.md#offset) | 否 | 按照对齐方式对齐后，选择器相对入口组件的偏移量。  默认值：{dx: 0, dy: 0}  单位：vp |

### edgeAlign18+

edgeAlign(alignType: Optional<CalendarAlign>, offset?: Offset)

设置选择器与入口组件的对齐方式。与[edgeAlign](ts-basic-components-calendarpicker.md#edgealign)相比，alignType参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| alignType | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[CalendarAlign](ts-basic-components-calendarpicker.md#calendaralign枚举说明)> | 是 | 对齐方式的类型。  默认值：CalendarAlign.END  当alignType的值为undefined时，使用默认值。 |
| offset | [Offset](ts-types.md#offset) | 否 | 按照对齐方式对齐后，选择器相对入口组件的偏移量。  默认值：{dx: 0, dy: 0}  单位：vp |

### textStyle

textStyle(value: PickerTextStyle)

设置入口区的文本颜色、字号、字体粗细。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PickerTextStyle](ts-picker-common.md#pickertextstyle对象说明) | 是 | 设置入口区的文本颜色、字号、字体粗细。  默认值：  {  color: '#ff182431',  font: {  size: '16fp',  weight: FontWeight.Regular  }  } |

### textStyle18+

textStyle(style: Optional<PickerTextStyle>)

设置入口区的文本颜色、字号、字体粗细。与[textStyle](ts-basic-components-calendarpicker.md#textstyle)相比，style参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[PickerTextStyle](ts-picker-common.md#pickertextstyle对象说明)> | 是 | 设置入口区的文本颜色、字号、字体粗细。  默认值：  {  color: '#ff182431',  font: {  size: '16fp',  weight: FontWeight.Regular  }  }  当style的值为undefined时，使用默认值。 |

### markToday19+

markToday(enabled: boolean)

设置日历选择器中系统当前日期是否保持高亮显示。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 设置日历选择器中系统当前日期是否保持高亮显示。  - true：系统当前日期在日历选择器内保持高亮显示。  - false：系统当前日期在日历选择器内不保持高亮显示。  默认值：false |

## 事件

除支持[通用事件](ts-component-general-events.md)，还支持以下事件：

### onChange

onChange(callback: Callback<Date>)

选择日期时触发该事件。不能通过双向绑定的状态变量触发。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](ts-types.md#callback12)<Date> | 是 | 日期选择时触发的回调函数。回调参数为Date类型的选中日期值，开发者可在回调函数中获取用户选中的日期并进行相应处理。 |

### onChange18+

onChange(callback: Optional<Callback<Date>>)

选择日期时触发该事件。不能通过双向绑定的状态变量触发。与[onChange](ts-basic-components-calendarpicker.md#onchange)相比，callback参数新增了对undefined类型的支持。

**说明** 

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[Callback](ts-types.md#callback12)<Date>> | 是 | 日期选择时触发的回调函数，回调参数为选中的日期值。  当callback的值为undefined时，不使用回调函数。 |

## CalendarOptions对象说明

日历选择器组件的参数说明。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| hintRadius | number | [Resource](ts-types.md#resource) | 否 | 是 | 设置日期选中态底板样式。  取值范围：[0.0, 16.0]  单位：vp  默认值：16.0，即底板样式为圆形。  **说明：**  当hintRadius为0.0时表示底板样式为直角矩形；当hintRadius为(0.0, 16.0)时，底板样式为圆角矩形；当hintRadius为16.0时，底板样式为圆形；当hintRadius为负数或大于16.0时，恢复为默认值16.0。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| selected | Date | 否 | 是 | 设置选中项的日期。当需要预设选中日期时传入此参数，不需要预设时使用当前系统日期。选中的日期未设置或日期格式不符合规范则为默认值。选中日期与start、end参数的配合关系见[start和end设置规则](ts-basic-components-calendarpicker.md#start和end设置规则)。  默认值：当前系统日期。  取值范围：[Date('0001-01-01'), Date('5000-12-31')]  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| start18+ | Date | 否 | 是 | 设置开始日期。  默认值：Date('0001-01-01')  取值范围：[Date('0001-01-01'), Date('5000-12-31')]  **说明：** 若start日期晚于end日期，则start日期、end日期都设置无效，选中日期为默认值。详见[start和end设置规则](ts-basic-components-calendarpicker.md#start和end设置规则)。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| end18+ | Date | 否 | 是 | 设置结束日期。  默认值：Date('5000-12-31')  取值范围：[Date('0001-01-01'), Date('5000-12-31')]  **说明：** 若start日期晚于end日期，则start日期、end日期都设置无效，选中日期为默认值。详见[start和end设置规则](ts-basic-components-calendarpicker.md#start和end设置规则)。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| disabledDateRange19+ | [DateRange](ts-picker-common.md#daterange19对象说明)[] | 否 | 是 | 设置禁用日期区间。不传此参数时不禁用任何日期。  **说明：**  1. 若日期区间内的开始日期或结束日期未设置或设置为异常值，则该日期区间无效。  2. 若在日期区间内，结束日期早于开始日期，则该日期区间无效。  3. 当在入口区选定某日期，通过上下箭头调整日期进行增加或减少操作时，若遇到禁用日期，系统将自动跳过整个禁用区间。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |

### start和end设置规则

| 场景 | 说明 |
| --- | --- |
| start日期晚于end日期 | start日期、end日期都设置无效，选中日期为默认值 |
| 选中日期早于start日期 | 选中日期为start日期 |
| 选中日期晚于end日期 | 选中日期为end日期 |
| start日期晚于当前系统日期，选中日期未设置 | 选中日期为start日期 |
| end日期早于当前系统日期，选中日期未设置 | 选中日期为end日期 |
| 日期格式不符合规范，如1999-13-32 | start日期或end日期设置无效，选中日期取默认值 |

## CalendarAlign枚举说明

对齐方式类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| START | 0 | 设置选择器与入口组件的对齐方式为左对齐。 |
| CENTER | 1 | 设置选择器与入口组件的对齐方式为居中对齐。 |
| END | 2 | 设置选择器与入口组件的对齐方式为右对齐。 |

## 示例

### 示例1（设置下拉日历弹窗）

该示例通过calendarPicker实现了日历选择器组件，提供下拉日历弹窗。

```ts
// xxx.ets
@Entry
@Component
struct CalendarPickerExample {
  private selectedDate: Date = new Date('2024-03-05');

  build() {
    Column() {
      Column() {
        CalendarPicker({ hintRadius: 10, selected: this.selectedDate })
          .edgeAlign(CalendarAlign.END)
          .textStyle({ color: '#ff182431', font: { size: 20, weight: FontWeight.Normal } })
          .margin(10)
          .onChange((value) => {
            console.info(`CalendarPicker onChange: ${value.toString()}`);
          })
      }.alignItems(HorizontalAlign.End).width("100%")

      Text('日历日期选择器').fontSize(30)
    }.width('100%').margin({ top: 350 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/4FxQOEeyQ_a26a3dJNNX1w/zh-cn_image_0000002712406072.gif)

### 示例2（设置开始日期和结束日期）

该示例通过start和end设置日历选择器的开始日期和结束日期。

从API version 18开始，[CalendarOptions](ts-basic-components-calendarpicker.md#calendaroptions对象说明)中新增了start、end属性。

```ts
// xxx.ets
@Entry
@Component
struct CalendarPickerExample {
  private selectedDate: Date = new Date('2025-01-15');
  private startDate: Date = new Date('2025-01-05');
  private endDate: Date = new Date('2025-01-25');

  build() {
    Column() {
      Column() {
        CalendarPicker({ hintRadius: 10, selected: this.selectedDate, start: this.startDate, end: this.endDate })
          .edgeAlign(CalendarAlign.END)
          .textStyle({ color: '#ff182431', font: { size: 20, weight: FontWeight.Normal } })
          .margin(10)
          .onChange((value) => {
            console.info(`CalendarPicker onChange: ${value.toString()}`);
          })
      }.alignItems(HorizontalAlign.End).width("100%")
    }.width('100%').margin({ top: 350 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/02_Fh0j2RcCaNz5peBOM2w/zh-cn_image_0000002742125021.png)

### 示例3（设置日历选择器在系统当前日期时，保持高亮显示和禁用日期区间）

该示例通过markToday设置日历选择器在系统当前日期时，开启保持高亮显示，同时，通过disabledDateRange设置日历选择器的禁用日期区间。

从API version 19开始，新增了[markToday](ts-basic-components-calendarpicker.md#marktoday19)接口，[CalendarOptions](ts-basic-components-calendarpicker.md#calendaroptions对象说明)中新增了disabledDateRange属性。

```ts
// xxx.ets
@Entry
@Component
struct CalendarPickerExample {
  private disabledDateRange: DateRange[] = [
    { start: new Date('2025-01-01'), end: new Date('2025-01-02') },
    { start: new Date('2025-01-09'), end: new Date('2025-01-10') },
    { start: new Date('2025-01-15'), end: new Date('2025-01-16') },
    { start: new Date('2025-01-19'), end: new Date('2025-01-19') },
    { start: new Date('2025-01-22'), end: new Date('2025-01-25') }
  ];

  build() {
    Column() {
      CalendarPicker({ disabledDateRange: this.disabledDateRange })
        .margin(10)
        .markToday(true)
        .onChange((value) => {
          console.info(`CalendarPicker onChange: ${value.toString()}`);
        })
    }.alignItems(HorizontalAlign.End).width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/wEzcNsC7Q4O16CMGqiVyDA/zh-cn_image_0000002712246114.gif)
