---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textpicker
title: TextPicker
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 按钮与选择 > TextPicker
category: harmonyos-references
scraped_at: 2026-04-29T13:52:01+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:7d204d54c9da3104aaf09d6081d5d9558eff8330c183745b6bfb6ead27bfcaca
---

滑动选择文本、图片或图文混排内容的组件，用户可以按需创建单列数据选择器、多列非联动数据选择器和多列联动数据选择器。

说明

* 该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件不建议开发者在动效过程中修改属性数据。
* 最大显示行数在横、竖屏模式下存在差异。竖屏时默认为5行，横屏时依赖系统配置，未配置时默认显示为3行。可通过如下参数查看具体配置值$r('sys.float.ohos\_id\_picker\_show\_count\_landscape')。
* 多列非联动数据选择器和多列联动数据选择器在下文中统称为多列数据选择器。

## 子组件

PhonePC/2in1TabletTVWearable

无

## 接口

PhonePC/2in1TabletTVWearable

TextPicker(options?: TextPickerOptions)

根据指定的数据列表创建文本选择器。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [TextPickerOptions](ts-basic-components-textpicker.md#textpickeroptions对象说明) | 否 | 配置文本选择器的参数。 |

## TextPickerOptions对象说明

PhonePC/2in1TabletTVWearable

文本选择器的参数说明。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| range | string[] | string[][]10+ | [Resource](ts-types.md#resource) |  [TextPickerRangeContent](ts-basic-components-textpicker.md#textpickerrangecontent10对象说明)[]10+ | [TextCascadePickerRangeContent](ts-basic-components-textpicker.md#textcascadepickerrangecontent10对象说明)[]10+ | 否 | 否 | 选择器的数据选择列表。不可设置为空数组，若设置为空数组，则不显示；若动态变化为空数组，则保持当前正常值显示。  **说明**：  1. 单列数据选择器使用string[]，[Resource](ts-types.md#resource)，[TextPickerRangeContent](ts-basic-components-textpicker.md#textpickerrangecontent10对象说明)[]类型。  2. 多列非联动数据选择器使用string[][]类型。  3. 多列联动数据选择器使用[TextCascadePickerRangeContent](ts-basic-components-textpicker.md#textcascadepickerrangecontent10对象说明)[]类型。  4. Resource类型只支持[strarray.json](../harmonyos-guides/resource-categories-and-access.md#资源组目录)。  5. range的类型及列数不可以动态修改。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| selected | number | number[]10+ | 否 | 是 | 设置选中项在数据选择列表中的索引值，索引从0开始。  默认值：0  **说明**：  1. 单列数据选择器使用number类型。  2. 多列数据选择器使用number[]类型。  3. 从API version 10开始，该参数支持[$$](../harmonyos-guides/arkts-two-way-sync.md)双向绑定变量。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| value | [ResourceStr](ts-types.md#resourcestr) | [ResourceStr](ts-types.md#resourcestr)[] | 否 | 是 | 设置选中项的值，优先级低于selected。  默认值：数据选择列表中第一个元素的值。  **说明**：  1. 从API version 10开始，该参数支持[$$](../harmonyos-guides/arkts-two-way-sync.md)双向绑定变量。  2. 从API version 20开始，支持[Resource](ts-types.md#resource)类型。  3. 只有显示文本列表时该值有效。显示图片或图文混排的列表时，该值无效。  4. 单列数据选择器使用[ResourceStr](ts-types.md#resourcestr)类型。  5. 多列数据选择器使用[ResourceStr](ts-types.md#resourcestr)[]类型。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| columnWidths18+ | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12)[] | 否 | 是 | 设置每一列的列宽。  默认值：每一列的列宽相等，为组件宽度除以列数。  **说明**：  1. 当文本长度大于列宽时，文本被截断。  2. 当设置为异常值时，使用默认值。  3. 支持设置为Undefined和Null，不支持Undefined[]和Null[]。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

## TextPickerRangeContent10+对象说明

PhonePC/2in1TabletTVWearable

单列数据选择器的数据选项内容。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| icon | string | [Resource](ts-types.md#resource) | 否 | 否 | 图片资源。 icon是string类型时，表示图片存放的路径，例如"/common/hello.png"。 |
| text | string | [Resource](ts-types.md#resource) | 否 | 是 | 文本信息。  默认值：空字符串  **说明**：当文本长度大于列宽时，文本被截断。 |

## TextCascadePickerRangeContent10+对象说明

PhonePC/2in1TabletTVWearable

多列联动数据选择器的数据选项内容。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| text | string | [Resource](ts-types.md#resource) | 否 | 否 | 文本信息。  **说明**：当文本长度大于列宽时，文本被截断。 |
| children | [TextCascadePickerRangeContent](ts-basic-components-textpicker.md#textcascadepickerrangecontent10对象说明)[] | 否 | 是 | 联动数据。 |

## DividerOptions12+对象说明

PhonePC/2in1TabletTVWearable

分割线的信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| strokeWidth | [Dimension](ts-types.md#dimension10) | 否 | 是 | 分割线的线宽。  默认值：2.0px  单位：默认为vp，也可指定单位为px。  取值范围：strokeWidth小于0取默认值，最大不得超过列高的一半。不支持“百分比”类型。 |
| startMargin | [Dimension](ts-types.md#dimension10) | 否 | 是 | 分割线与TextPicker侧边起始端的距离。  默认值：0  单位：默认为vp，也可指定单位为px。  取值范围：startMargin小于0时无效，最大值不得超过TextPicker列宽。不支持“百分比”类型。 |
| endMargin | [Dimension](ts-types.md#dimension10) | 否 | 是 | 分割线与TextPicker侧边结束端的距离。  默认值：0  单位：默认为vp，也可指定单位为px。  取值范围：endMargin小于0时无效，最大值不得超过TextPicker列宽。不支持“百分比”类型。 |
| color | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 分割线的颜色。  默认值：'#33000000' |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### defaultPickerItemHeight

PhonePC/2in1TabletTVWearable

defaultPickerItemHeight(value: number | string)

设置选择项的高度。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | 是 | 选择项的高度。  取值范围：  number类型：[0, +∞)，单位为vp。  string类型：仅支持number类型取值的字符串形式，例如"56"。  默认值：选中项56vp，非选中项36vp。  **说明：**  设置该参数后，选中项与非选中项的高度均为所设置的值。 |

### defaultPickerItemHeight18+

PhonePC/2in1TabletTVWearable

defaultPickerItemHeight(height: Optional<number | string>)

设置选择项的高度。与[defaultPickerItemHeight](ts-basic-components-textpicker.md#defaultpickeritemheight)相比，height参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| height | [Optional](ts-universal-attributes-custom-property.md#optionalt)<number | string> | 是 | 选择项的高度。  取值范围：  number类型：[0, +∞)，单位为vp。  string类型：仅支持number类型取值的字符串形式，例如"56"。  默认值：选中项56vp，非选中项36vp。  **说明：**  1. 设置该参数后，选中项与非选中项的高度均为所设置的值。  2. 当height的值为undefined时，维持上次取值。 |

### disappearTextStyle10+

PhonePC/2in1TabletTVWearable

disappearTextStyle(value: PickerTextStyle)

设置边缘项（以选中项为基准向上或向下的第二项）的文本颜色、字号、字体粗细。

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

设置边缘项（以选中项为基准向上或向下的第二项）的文本颜色、字号、字体粗细。与[disappearTextStyle10+](ts-basic-components-textpicker.md#disappeartextstyle10)相比，style参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[PickerTextStyle](ts-picker-common.md#pickertextstyle对象说明)> | 是 | 边缘项的文本颜色、字号、字体粗细。  默认值：  {  color: '#ff182431',  font: {  size: '14fp',  weight: FontWeight.Regular  }  }  当style的值为undefined时，使用默认值。 |

说明

若选中项向上或向下的可视项数低于两项则无对应边缘项。

### disappearTextStyle20+

PhonePC/2in1TabletTVWearable

disappearTextStyle(style: Optional<PickerTextStyle|TextPickerTextStyle>)

设置边缘项（以选中项为基准向上或向下的第二项）的文本颜色、字号、字体粗细、最大字号、最小字号、超长文本截断方式。与[disappearTextStyle](ts-basic-components-textpicker.md#disappeartextstyle18)18+相比，style参数新增了对[TextPickerTextStyle](ts-basic-components-textpicker.md#textpickertextstyle15类型说明)类型的支持。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[PickerTextStyle](ts-picker-common.md#pickertextstyle对象说明)|[TextPickerTextStyle](ts-basic-components-textpicker.md#textpickertextstyle15类型说明)> | 是 | 边缘项的文本颜色、字号、字体粗细、最大字号、最小字号、超长文本截断方式。  默认值：  {  color: '#ff182431',  font: {  size: '14fp',  weight: FontWeight.Regular  },  minFontSize: 0,  maxFontSize: 0,  overflow: TextOverflow.Clip  }  当style的值为undefined时，使用默认值。 |

说明

若选中项向上或向下的可视项数低于两项则无对应边缘项。

### textStyle10+

PhonePC/2in1TabletTVWearable

textStyle(value: PickerTextStyle)

设置待选项（以选中项为基准向上或向下的第一项）的文本颜色、字号、字体粗细。

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

设置待选项（以选中项为基准向上或向下的第一项）的文本颜色、字号、字体粗细。与[textStyle10+](ts-basic-components-textpicker.md#textstyle10)相比，style参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[PickerTextStyle](ts-picker-common.md#pickertextstyle对象说明)> | 是 | 待选项的文本颜色、字号、字体粗细。  默认值：  {  color: '#ff182431',  font: {  size: '16fp',  weight: FontWeight.Regular  }  }  当style的值为undefined时，使用默认值。 |

说明

若选中项向上或向下可视项数低于一项则无对应待选项。

### textStyle20+

PhonePC/2in1TabletTVWearable

textStyle(style: Optional<PickerTextStyle|TextPickerTextStyle>)

设置待选项（以选中项为基准向上或向下的第一项）的文本颜色、字号、字体粗细、最大字号、最小字号、超长文本截断方式。与[textStyle](ts-basic-components-textpicker.md#textstyle18)18+相比，style参数新增了对[TextPickerTextStyle](ts-basic-components-textpicker.md#textpickertextstyle15类型说明)类型的支持。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[PickerTextStyle](ts-picker-common.md#pickertextstyle对象说明)|[TextPickerTextStyle](ts-basic-components-textpicker.md#textpickertextstyle15类型说明)> | 是 | 待选项的文本颜色、字号、字体粗细、最大字号、最小字号、超长文本截断方式。  默认值：  {  color: '#ff182431',  font: {  size: '16fp',  weight: FontWeight.Regular  },  minFontSize: 0,  maxFontSize: 0,  overflow: TextOverflow.Clip  }  当style的值为undefined时，使用默认值。 |

说明

若选中项向上或向下可视项数低于一项则无对应待选项。

### selectedTextStyle10+

PhonePC/2in1TabletTVWearable

selectedTextStyle(value: PickerTextStyle)

设置选中项的文本颜色、字号、字体粗细。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该属性在Wearable设备上使用无效果，在其他设备中可正常生效。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PickerTextStyle](ts-picker-common.md#pickertextstyle对象说明) | 是 | 选中项的文本颜色、字号、字体粗细。  默认值：  {  color: '#ff007dff',  font: {  size: '20fp',  weight: FontWeight.Medium  }  } |

### selectedTextStyle18+

PhonePC/2in1TabletTVWearable

selectedTextStyle(style: Optional<PickerTextStyle>)

设置选中项的文本颜色、字号、字体粗细。与[selectedTextStyle10+](ts-basic-components-textpicker.md#selectedtextstyle10)相比，style参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该属性在Wearable设备上使用无效果，在其他设备中可正常生效。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[PickerTextStyle](ts-picker-common.md#pickertextstyle对象说明)> | 是 | 选中项的文本颜色、字号、字体粗细。  默认值：  {  color: '#ff007dff',  font: {  size: '20fp',  weight: FontWeight.Medium  }  }  当style的值为undefined时，使用默认值。 |

### selectedTextStyle20+

PhonePC/2in1TabletTVWearable

selectedTextStyle(style: Optional<PickerTextStyle|TextPickerTextStyle>)

设置选中项的文本颜色、字号、字体粗细、最大字号、最小字号、超长文本截断方式。与[selectedTextStyle](ts-basic-components-textpicker.md#selectedtextstyle18)18+相比，style参数新增了对[TextPickerTextStyle](ts-basic-components-textpicker.md#textpickertextstyle15类型说明)类型的支持。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该属性在Wearable设备上使用无效果，在其他设备中可正常生效。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[PickerTextStyle](ts-picker-common.md#pickertextstyle对象说明)|[TextPickerTextStyle](ts-basic-components-textpicker.md#textpickertextstyle15类型说明)> | 是 | 选中项的文本颜色、字号、字体粗细、最大字号、最小字号、超长文本截断方式。  默认值：  {  color: '#ff007dff',  font: {  size: '20fp',  weight: FontWeight.Medium  },  minFontSize: 0,  maxFontSize: 0,  overflow: TextOverflow.Clip  }  当style的值为undefined时，使用默认值。 |

### selectedIndex10+

PhonePC/2in1TabletTVWearable

selectedIndex(value: number | number[])

设置选中项在数据选择列表中的索引值，优先级高于[TextPickerOptions](ts-basic-components-textpicker.md#textpickeroptions对象说明)中的"value"属性。单列数据选择器使用number类型。多列数据选择器使用number[]类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | number[] | 是 | 选中项在数据选择列表中的索引值，索引从0开始。  默认值：0  当value的值为负数或者超过数据选择列表的最大索引值时，使用默认值。 |

### selectedIndex18+

PhonePC/2in1TabletTVWearable

selectedIndex(index: Optional<number | number[]>)

设置选中项在数据选择列表中的索引值，优先级高于[TextPickerOptions](ts-basic-components-textpicker.md#textpickeroptions对象说明)中的"value"属性。单列数据选择器使用number类型，多列数据选择器使用number[]类型。与[selectedIndex10+](ts-basic-components-textpicker.md#selectedindex10)相比，index参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | [Optional](ts-universal-attributes-custom-property.md#optionalt)<number | number[]> | 是 | 选中项在数据选择列表中的索引值，索引从0开始。  默认值：0  当index的值为undefined时，使用[TextPickerOptions](ts-basic-components-textpicker.md#textpickeroptions对象说明)中的selected值。  当index的值为负数或者超过数据选择列表的最大索引值时，使用默认值。 |

### canLoop10+

PhonePC/2in1TabletTVWearable

canLoop(value: boolean)

设置是否可循环滚动。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否可循环滚动。  - true：可循环。  - false：不可循环。  默认值：true |

### canLoop18+

PhonePC/2in1TabletTVWearable

canLoop(isLoop: Optional<boolean>)

设置是否可循环滚动。与[canLoop10+](ts-basic-components-textpicker.md#canloop10)相比，isLoop参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isLoop | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 是否可循环滚动。  - true：可循环。  - false：不可循环。  默认值：true  当isLoop的值为undefined时，使用默认值。 |

### divider12+

PhonePC/2in1TabletTVWearable

divider(value: DividerOptions | null)

设置分割线样式，不设置该属性则按“默认值”展示分割线。

[DividerOptions](ts-basic-components-textpicker.md#divideroptions12对象说明)中startMargin + endMargin 超过组件宽度后，startMargin和endMargin会被置0。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [DividerOptions](ts-basic-components-textpicker.md#divideroptions12对象说明) | null | 是 | 默认值：  {  strokeWidth: '2px',  startMargin: 0,  endMargin: 0,  color: '#33000000'  }  1. 当textDivider设置为有效的[DividerOptions](ts-basic-components-textpicker.md#divideroptions12对象说明)时，按设置的样式显示分割线。  2. 当textDivider设置为null时，不显示分割线。 |

### divider18+

PhonePC/2in1TabletTVWearable

divider(textDivider: Optional<DividerOptions | null>)

设置分割线样式，不设置该属性则按“默认值”展示分割线。与[divider12+](ts-basic-components-textpicker.md#divider12)相比，textDivider参数新增了对undefined类型的支持。

[DividerOptions](ts-basic-components-textpicker.md#divideroptions12对象说明)中startMargin + endMargin 超过组件宽度后，startMargin和endMargin会被置0。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| textDivider | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[DividerOptions](ts-basic-components-textpicker.md#divideroptions12对象说明) | null> | 是 | 默认值：  {  strokeWidth: '2px',  startMargin: 0,  endMargin: 0,  color: '#33000000'  }  1. 当textDivider的值为undefined时，使用默认值。  2. 当textDivider设置为有效的[DividerOptions](ts-basic-components-textpicker.md#divideroptions12对象说明)时，按设置的样式显示分割线。  3. 当textDivider设置为null时，不显示分割线。 |

### gradientHeight12+

PhonePC/2in1TabletTVWearable

gradientHeight(value: Dimension)

设置渐隐效果的高度。若未设置该属性，则显示默认渐隐效果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Dimension](ts-types.md#dimension10) | 是 | 内容区上下边缘的渐隐高度。  默认值：36vp  取值范围：[0, +∞)，支持百分比。  **说明：**  1. value设置为百分比时，100%为TextPicker高度的一半。  2. value设置为0时不显示渐隐效果。  3. value设置为数字且超过TextPicker高度的一半时，使用默认值。  4. 当value的值为负数时，使用默认值。 |

### gradientHeight18+

PhonePC/2in1TabletTVWearable

gradientHeight(height: Optional<Dimension>)

设置渐隐效果的高度。若未设置该属性，则显示默认渐隐效果。与[gradientHeight12+](ts-basic-components-textpicker.md#gradientheight12)相比，height参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| height | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[Dimension](ts-types.md#dimension10)> | 是 | 内容区上下边缘的渐隐高度。  默认值：36vp  取值范围：[0, +∞)，支持百分比。  **说明：**  1. height设置为百分比时，100%为TextPicker高度的一半。  2. height设置为0时不显示渐隐效果。  3. height设置为数字且超过TextPicker高度的一半时，使用默认值。  4. 当height的值为undefined或负数时，使用默认值。 |

### disableTextStyleAnimation15+

PhonePC/2in1TabletTVWearable

disableTextStyleAnimation(disabled: boolean)

设置是否关闭滑动过程中文本样式变化的动效。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| disabled | boolean | 是 | 是否关闭滑动过程中文本样式变化的动效。  - true：关闭文本样式变化动效。  - false：不关闭文本样式变化动效。  默认值：false  **说明：**  设置为true时，滑动过程中无字号、字重、字体颜色等变化动效，且文本均显示为[defaultTextStyle](ts-basic-components-textpicker.md#defaulttextstyle15)属性设置的样式。如未设置[defaultTextStyle](ts-basic-components-textpicker.md#defaulttextstyle15)，则显示为[Text](ts-basic-components-text.md)组件默认样式。 |

### defaultTextStyle15+

PhonePC/2in1TabletTVWearable

defaultTextStyle(style: TextPickerTextStyle)

设置关闭滑动过程中文本样式变化的动效时，各个选项的文本样式。仅当[disableTextStyleAnimation](ts-basic-components-textpicker.md#disabletextstyleanimation15)为true时生效。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [TextPickerTextStyle](ts-basic-components-textpicker.md#textpickertextstyle15类型说明) | 是 | 设置关闭滑动过程中文本样式变化的动效时，各个选项的文本样式。  默认值：与[Text](ts-basic-components-text.md)组件默认值相同。 |

开启触控反馈时，需要在工程的src/main/module.json5文件的"module"内配置requestPermissions字段开启振动权限，配置如下：

```
1. "requestPermissions": [
2. {
3. "name": "ohos.permission.VIBRATE",
4. }
5. ]
```

### enableHapticFeedback18+

PhonePC/2in1TabletTVWearable

enableHapticFeedback(enable: Optional<boolean>)

设置是否开启触控反馈。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 设置是否开启触控反馈。  - true：开启触控反馈。  - false：不开启触控反馈。  默认值：true  设置为true后，其生效情况取决于系统的硬件是否支持。 |

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

用于圆形屏幕的穿戴设备。组件响应[表冠事件](ts-universal-events-crown.md)，需要先获取焦点。

### selectedBackgroundStyle20+

PhonePC/2in1TabletTVWearable

selectedBackgroundStyle(style: Optional<PickerBackgroundStyle>)

设置选中项的背景样式。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[PickerBackgroundStyle](ts-basic-components-textpicker.md#pickerbackgroundstyle20)> | 是 | 选中项背景的颜色和边框圆角半径，多列模式时会同时设置所有列的选中项背景的颜色和圆角半径。  默认值：  {  color: $r('sys.color.comp\_background\_tertiary'),  borderRadius: $r('sys.float.corner\_radius\_level12')  } |

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](ts-component-general-events.md)外，还支持以下事件：

### onChange

PhonePC/2in1TabletTVWearable

onChange(callback: (value: string | string[], index: number | number[]) => void)

滑动TextPicker文本内容后，选项归位至选中项位置时，触发该回调。不能通过双向绑定的状态变量触发。当显示文本或图片加文本列表时，value值为选中项中的文本值，当显示图片列表时，value值为空。

回调会在滑动动画结束后触发，如果需要快速获取索引值变化，建议使用[onEnterSelectedArea](ts-basic-components-textpicker.md#onenterselectedarea18)接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | string[]10+ | 是 | 当前选中项的文本。多列数据选择器的value为数组类型。 |
| index | number | number[]10+ | 是 | 当前选中项的索引值，索引从0开始。多列数据选择器的index为数组类型。 |

### onChange18+

PhonePC/2in1TabletTVWearable

onChange(callback: Optional<OnTextPickerChangeCallback>)

滑动TextPicker文本内容后，选项归位至选中项位置时，触发该回调。不能通过双向绑定的状态变量触发。当显示文本或图片加文本列表时，value值为选中项中的文本值，当显示图片列表时，value值为空。与[onChange](ts-basic-components-textpicker.md#onchange)相比，callback参数新增了对undefined类型的支持。

回调会在滑动动画结束后触发，如果需要快速获取索引值变化，建议使用[onEnterSelectedArea](ts-basic-components-textpicker.md#onenterselectedarea18)接口。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[OnTextPickerChangeCallback](ts-basic-components-textpicker.md#ontextpickerchangecallback18)> | 是 | 滑动选中TextPicker文本内容后，触发的回调。  当callback的值为undefined时，不使用回调函数。 |

### onScrollStop14+

PhonePC/2in1TabletTVWearable

onScrollStop(callback: TextPickerScrollStopCallback)

文本选择器的选项列滑动停止时触发该事件。

手指拖动选项列触发的滑动，手指离开屏幕且滑动停止时会触发该事件。

说明

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [TextPickerScrollStopCallback](ts-basic-components-textpicker.md#textpickerscrollstopcallback14) | 是 | 文本选择器的选项列滑动停止时触发该事件。 |

### onScrollStop18+

PhonePC/2in1TabletTVWearable

onScrollStop(callback: Optional<TextPickerScrollStopCallback>)

文本选择器的选项列滑动停止时触发该事件。与[onScrollStop14+](ts-basic-components-textpicker.md#onscrollstop14)相比，callback参数新增了对undefined类型的支持。

手指拖动选项列触发的滑动，手指离开屏幕且滑动停止时会触发该事件。

说明

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[TextPickerScrollStopCallback](ts-basic-components-textpicker.md#textpickerscrollstopcallback14)> | 是 | 文本选择器的选项列滑动停止时触发该事件。  当callback的值为undefined时，不使用回调函数。 |

### onEnterSelectedArea18+

PhonePC/2in1TabletTVWearable

onEnterSelectedArea(callback: TextPickerEnterSelectedAreaCallback)

滑动TextPicker过程中，选项进入分割线区域内（当前列的滑动距离超过选中项高度的一半）时，触发该回调。

说明

* 与[onChange](ts-basic-components-textpicker.md#onchange)事件的差别在于，该事件的触发时机早于[onChange](ts-basic-components-textpicker.md#onchange)事件。
* 在多列联动场景中，不建议使用该回调，由于该回调标识的是滑动过程中选项进入分割线区域内的节点，而跟随变化的选项并不涉及滑动，因此，回调的返回值中，仅当前滑动列的值会正常变化，其余未滑动列的值保持不变。
* 该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [TextPickerEnterSelectedAreaCallback](ts-basic-components-textpicker.md#textpickerenterselectedareacallback18) | 是 | 滑动TextPicker过程中，选项进入分割线区域时触发的回调。 |

### onAccept(deprecated)

PhonePC/2in1TabletTVWearable

onAccept(callback: (value: string, index: number) => void)

点击弹窗中的“确定”按钮时触发该回调。该事件仅在[文本滑动选择器弹窗](ts-methods-textpicker-dialog.md)中生效。

从API version 8开始支持，从API version 10开始废弃，无替代接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 当前选中项的文本。 |
| index | number | 是 | 当前选中项的索引值，索引从0开始。 |

### onCancel(deprecated)

PhonePC/2in1TabletTVWearable

onCancel(callback: () => void)

点击弹窗中的“取消”按钮时触发该回调。该事件仅在[文本滑动选择器弹窗](ts-methods-textpicker-dialog.md)中生效。

从API version 8开始支持，从API version 10开始废弃，无替代接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | () => void | 是 | 点击弹窗中的“取消”按钮时触发该回调。 |

## TextPickerTextStyle15+类型说明

PhonePC/2in1TabletTVWearable

文本样式选项，继承自[PickerTextStyle](ts-picker-common.md#pickertextstyle对象说明)。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| minFontSize | number | string | [Resource](ts-types.md#resource) | 否 | 是 | 文本最小显示字号，与maxFontSize配合使用。当设置minFontSize和maxFontSize时，font中的size将不生效。默认最大行数为1，自适应高度方式为MIN\_FONT\_SIZE\_FIRST。详细规则请参考Text组件的[minFontSize](ts-basic-components-text.md#minfontsize)属性。 |
| maxFontSize | number | string | [Resource](ts-types.md#resource) | 否 | 是 | 文本最大显示字号。详细规则请参考Text组件的[maxFontSize](ts-basic-components-text.md#maxfontsize)属性。 |
| overflow | [TextOverflow](ts-appendix-enums.md#textoverflow) | 否 | 是 | 文本截断方式。当设置为MARQUEE时，该属性不生效。详细规则请参考Text组件的[textOverflow](ts-basic-components-text.md#textoverflow)属性。 |

## OnTextPickerChangeCallback18+

PhonePC/2in1TabletTVWearable

type OnTextPickerChangeCallback = (selectItem: string | string[], index: number | number[]) => void

定义触发onChange事件的回调类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| selectItem | string | string[]10+ | 是 | 当前选中项的文本。多列数据选择器的selectItem为数组类型。  **说明：**  当选择器内容为文本或图文混排时，selectItem值为选中项中的文本值；当选择器内容为图片时，selectItem值为空。 |
| index | number | number[]10+ | 是 | 当前选中项的索引值，索引从0开始。多列数据选择器的index为数组类型。 |

## TextPickerScrollStopCallback14+

PhonePC/2in1TabletTVWearable

type TextPickerScrollStopCallback = (value: string | string[], index: number | number[]) => void

定义触发onScrollStop事件的回调类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | string[] | 是 | 当前选中项的文本。多列数据选择器的value为数组类型。  **说明：**  当选择器内容为文本或图文混排时，value值为选中项中的文本值；当选择器内容为图片时，value值为空。 |
| index | number | number[] | 是 | 当前选中项的索引值，索引从0开始。多列数据选择器的index为数组类型。 |

## TextPickerEnterSelectedAreaCallback18+

PhonePC/2in1TabletTVWearable

type TextPickerEnterSelectedAreaCallback = (value: string | string[], index: number | number[]) => void

定义触发onEnterSelectedArea事件的回调类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | string[] | 是 | 当前选中项的文本。多列数据选择器的value为数组类型。  **说明：**  当选择器内容为文本或图文混排时，value值为选中项中的文本值；当选择器内容为图片时，value值为空。 |
| index | number | number[] | 是 | 当前选中项的索引值，索引从0开始。多列数据选择器的index为数组类型。 |

## PickerBackgroundStyle20+

PhonePC/2in1TabletTVWearable

选择器选中项的背景样式，包括选中项的背景颜色和边框圆角半径。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| color | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 选中项的背景颜色。  默认值：  'sys.color.comp\_background\_tertiary' |
| borderRadius | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | [BorderRadiuses](ts-types.md#borderradiuses9) | [LocalizedBorderRadiuses](ts-types.md#localizedborderradiuses12) | 否 | 是 | 选中项的边框圆角半径。  默认值：{ value:24, unit:LengthUnit.VP }，即四个圆角半径均为24VP。  **说明：**  1. [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12)类型的value参数同时作用于四个圆角半径大小，unit参数用于设置单位。  2. [BorderRadiuses](ts-types.md#borderradiuses9)类型可以设置四个不同值的圆角半径，所有单位固定为VP。  3. [LocalizedBorderRadiuses](ts-types.md#localizedborderradiuses12)类型可以设置四个不同值的圆角半径，并且可以单独设置每个圆角的单位。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置选择器列数）

该示例通过配置range实现单列数据选择器和多列数据选择器，并使用columnWidths调整每一列的宽度。

从API version 18开始，新增了[TextPickerOptions](ts-basic-components-textpicker.md#textpickeroptions对象说明)的columnWidths属性。

```
1. // xxx.ets
2. import { LengthMetrics } from '@kit.ArkUI';

4. class Bottom {
5. bottom: number = 50;
6. }

8. let bott: Bottom = new Bottom();
9. @Entry
10. @Component
11. struct TextPickerExample {
12. private select: number = 1;
13. private apfruits: string[] = ['apple1', 'apple2', 'apple3', 'apple4'];
14. private orfruits: string[] = ['orange1', 'orange2', 'orange3', 'orange4'];
15. private pefruits: string[] = ['peach1', 'peach2', 'peach3', 'peach4'];
16. private multi: string[][] = [this.apfruits, this.orfruits, this.pefruits];
17. private cascade: TextCascadePickerRangeContent[] = [
18. {
19. text: '辽宁省',
20. children: [{ text: '沈阳市', children: [{ text: '沈河区' }, { text: '和平区' }, { text: '浑南区' }] },
21. { text: '大连市', children: [{ text: '中山区' }, { text: '金州区' }, { text: '长海县' }] }]
22. },
23. {
24. text: '吉林省',
25. children: [{ text: '长春市', children: [{ text: '南关区' }, { text: '宽城区' }, { text: '朝阳区' }] },
26. { text: '四平市', children: [{ text: '铁西区' }, { text: '铁东区' }, { text: '梨树县' }] }]
27. },
28. {
29. text: '黑龙江省',
30. children: [{ text: '哈尔滨市', children: [{ text: '道里区' }, { text: '道外区' }, { text: '南岗区' }] },
31. { text: '牡丹江市', children: [{ text: '东安区' }, { text: '西安区' }, { text: '爱民区' }] }]
32. }
33. ];
34. private singleColumnWidths: LengthMetrics[] = [
35. LengthMetrics.percent(50)
36. ];

38. private multipleColumnWidths: LengthMetrics[] = [
39. LengthMetrics.vp(100),
40. LengthMetrics.vp(200),
41. LengthMetrics.vp(100)
42. ];

44. private cascadeColumnWidths: LengthMetrics[] = [
45. LengthMetrics.percent(20),
46. LengthMetrics.percent(30),
47. LengthMetrics.percent(50)
48. ];
49. build() {
50. Column() {

52. TextPicker({ range: this.apfruits, selected: this.select, columnWidths: this.singleColumnWidths })
53. .onChange((value: string | string[], index: number | number[]) => {
54. console.info('Picker item changed, value: ' + value + ', index: ' + index);
55. })
56. .onScrollStop((value: string | string[], index: number | number[]) => {
57. console.info('Picker scroll stopped, value: ' + value + ', index: ' + index);
58. }).margin(bott)
59. .onEnterSelectedArea((value: string | string[], index: number | number[]) => {
60. console.info('Picker item enter selected area, value: ' + value + ', index: ' + index);
61. })

63. TextPicker({ range: this.multi, columnWidths: this.multipleColumnWidths })
64. .onChange((value: string | string[], index: number | number[]) => {
65. console.info('TextPicker 多列:onChange ' + JSON.stringify(value) + ', ' + 'index: ' + JSON.stringify(index));
66. })
67. .onScrollStop((value: string | string[], index: number | number[]) => {
68. console.info('TextPicker 多列:onScrollStop ' + JSON.stringify(value) + ', ' + 'index: ' + JSON.stringify(index));
69. }).margin(bott)
70. .onEnterSelectedArea((value: string | string[], index: number | number[]) => {
71. console.info('TextPicker 多列:onEnterSelectedArea ' + JSON.stringify(value) + ', ' + 'index: ' + JSON.stringify(index));
72. })

74. TextPicker({ range: this.cascade, columnWidths: this.cascadeColumnWidths })
75. .onChange((value: string | string[], index: number | number[]) => {
76. console.info('TextPicker 多列联动:onChange ' + JSON.stringify(value) + ', ' + 'index: ' + JSON.stringify(index));
77. })
78. .onScrollStop((value: string | string[], index: number | number[]) => {
79. console.info('TextPicker 多列联动:onScrollStop ' + JSON.stringify(value) + ', ' + 'index: ' + JSON.stringify(index));
80. })
81. .onEnterSelectedArea((value: string | string[], index: number | number[]) => {
82. console.info('TextPicker 多列联动:onEnterSelectedArea ' + JSON.stringify(value) + ', ' + 'index: ' + JSON.stringify(index));
83. })
84. }
85. }
86. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/_rjVaMpeRcOfXuLBYXsv7Q/zh-cn_image_0000002558766232.png?HW-CC-KV=V1&HW-CC-Date=20260429T055158Z&HW-CC-Expire=86400&HW-CC-Sign=055319C1CF1076722FA396EED5D2EAB66440B40B63BCAB4D2261FC7CE35C7C86)

### 示例2（设置文本样式）

该示例使用[disappearTextStyle](ts-basic-components-textpicker.md#disappeartextstyle10)、[textStyle](ts-basic-components-textpicker.md#textstyle10)、[selectedTextStyle](ts-basic-components-textpicker.md#selectedtextstyle10)设置文本选择器中的文本样式。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextPickerExample {
5. private select: number = 0;
6. private fruits: string[] = ['apple1', 'orange2', 'peach3', 'grape4'];

8. build() {
9. Column() {
10. TextPicker({
11. range: this.fruits,
12. selected: this.select,
13. value: this.fruits[this.select]
14. })
15. .onChange((value: string | string[], index: number | number[]) => {
16. console.info('Picker item changed, value: ' + value + ', index: ' + index);
17. })
18. .onScrollStop((value: string | string[], index: number | number[]) => {
19. console.info('Picker scroll stopped, value: ' + value + ', index: ' + index);
20. })
21. .disappearTextStyle({ color: Color.Red, font: { size: 15, weight: FontWeight.Lighter } })
22. .textStyle({ color: Color.Black, font: { size: 20, weight: FontWeight.Normal } })
23. .selectedTextStyle({ color: Color.Blue, font: { size: 30, weight: FontWeight.Bolder } })
24. .defaultPickerItemHeight(50)
25. .canLoop(false)
26. .selectedIndex(2)
27. }.width('100%').height('100%')
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/PkLFRWRUSDWowQ2S5lBSCw/zh-cn_image_0000002558606574.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055158Z&HW-CC-Expire=86400&HW-CC-Sign=EC8361BF9E16102CC44C6B77F538296B16D8D328A34783CEFA83C17AB009489F)

### 示例3（设置无分割线样式）

该示例通过配置[divider](ts-basic-components-textpicker.md#divider12)为null实现无分割线样式的文本选择器。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextPickerExample {
5. private select: number = 0;
6. private fruits: string[] = ['apple1', 'orange2', 'peach3', 'grape4'];

8. build() {
9. Column() {
10. TextPicker({ range: this.fruits, selected: this.select })
11. .onChange((value: string | string[], index: number | number[]) => {
12. console.info('Picker item changed, value: ' + value + ', index: ' + index);
13. })
14. .onScrollStop((value: string | string[], index: number | number[]) => {
15. console.info('Picker scroll stopped, value: ' + value + ', index: ' + index);
16. })
17. .disappearTextStyle({color: Color.Red, font: {size: 15, weight: FontWeight.Lighter}})
18. .textStyle({color: Color.Black, font: {size: 20, weight: FontWeight.Normal}})
19. .selectedTextStyle({color: Color.Blue, font: {size: 30, weight: FontWeight.Bolder}})
20. .divider(null)
21. }.width('100%').height('100%')
22. }
23. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/j8QnQIAHSOeWscnleGlCKw/zh-cn_image_0000002589326101.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055158Z&HW-CC-Expire=86400&HW-CC-Sign=E9104C7BAB30230FAB5F7A4B77EF6F86CEE862CDBDEC8DE091BC827227894CD1)

### 示例4（设置分割线样式）

该示例通过配置divider的DividerOptions设置文本选择器的分割线样式。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextPickerExample {
5. private select: number = 1;
6. private fruits: string[] = ['apple1', 'orange2', 'peach3', 'grape4'];

8. build() {
9. Column() {
10. TextPicker({ range: this.fruits, selected: this.select })
11. .onChange((value: string | string[], index: number | number[]) => {
12. console.info('Picker item changed, value: ' + value + ', index: ' + index);
13. })
14. .onScrollStop((value: string | string[], index: number | number[]) => {
15. console.info('Picker scroll stopped, value: ' + value + ', index: ' + index);
16. })
17. .disappearTextStyle({color: Color.Red, font: {size: 15, weight: FontWeight.Lighter}})
18. .textStyle({color: Color.Black, font: {size: 20, weight: FontWeight.Normal}})
19. .selectedTextStyle({color: Color.Blue, font: {size: 30, weight: FontWeight.Bolder}})
20. .divider({
21. strokeWidth: 10,
22. color: Color.Red,
23. startMargin: 10,
24. endMargin: 20
25. } as DividerOptions)
26. }.width('100%').height('100%')
27. }
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/cAZfAj-ASD-4FySnSRPBBQ/zh-cn_image_0000002589246043.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055158Z&HW-CC-Expire=86400&HW-CC-Sign=250790DE992382DA95E18811364095393971EA718088517182597B0C1ACF3727)

### 示例5（设置渐隐效果）

该示例通过配置[gradientHeight](ts-basic-components-textpicker.md#gradientheight12)设置文本选择器的渐隐效果高度。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextPickerExample {
5. private select: number = 1;
6. private fruits: string[] = ['apple1', 'orange2', 'peach3', 'grape4'];

8. build() {
9. Column() {
10. TextPicker({ range: this.fruits, selected: this.select })
11. .onChange((value: string | string[], index: number | number[]) => {
12. console.info('Picker item changed, value: ' + value + ', index: ' + index);
13. })
14. .onScrollStop((value: string | string[], index: number | number[]) => {
15. console.info('Picker scroll stopped, value: ' + value + ', index: ' + index);
16. })
17. .disappearTextStyle({color: Color.Red, font: {size: 15, weight: FontWeight.Lighter}})
18. .textStyle({color: Color.Black, font: {size: 20, weight: FontWeight.Normal}})
19. .selectedTextStyle({color: Color.Blue, font: {size: 30, weight: FontWeight.Bolder}})
20. .gradientHeight(100)
21. }.width('100%').height('100%')
22. }
23. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/ravmGtQAT7a0NbmMsrFoxw/zh-cn_image_0000002558766234.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055158Z&HW-CC-Expire=86400&HW-CC-Sign=471942F427E58FF8ED3A714503F1D895AB62E68C6F513FA13451AC92FDADCD0C)

### 示例6（设置选择项高度）

该示例通过配置[defaultPickerItemHeight](ts-basic-components-textpicker.md#defaultpickeritemheight)设置选择项的高度。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextPickerExample {
5. private select: number = 1;
6. private fruits: string[] = ['apple1', 'orange2', 'peach3', 'grape4'];

8. build() {
9. Column() {
10. TextPicker({ range: this.fruits, selected: this.select })
11. .defaultPickerItemHeight(60)
12. .onChange((value: string | string[], index: number | number[]) => {
13. console.info('Picker item changed, value: ' + value + ', index: ' + index);
14. })
15. .onScrollStop((value: string | string[], index: number | number[]) => {
16. console.info('Picker scroll stopped, value: ' + value + ', index: ' + index);
17. })
18. }.width('100%').height('100%')
19. }
20. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/7SerMwviQyqusZBqL_5uiw/zh-cn_image_0000002558606576.png?HW-CC-KV=V1&HW-CC-Date=20260429T055158Z&HW-CC-Expire=86400&HW-CC-Sign=A90B1D61C03BA9730803BC846E44428451DFDB3CB75DB23C22C4BEFFBF17B68C)

### 示例7（设置循环滚动）

该示例通过配置[canLoop](ts-basic-components-textpicker.md#canloop10)设置文本选择器是否循环滚动。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextPickerExample {
5. @State isLoop: boolean = false;
6. private select: number = 1;
7. private fruits: string[] = ['apple1', 'orange2', 'peach3', 'grape4'];

9. build() {
10. Column() {
11. TextPicker({ range: this.fruits, selected: this.select })
12. .onChange((value: string | string[], index: number | number[]) => {
13. console.info('Picker item changed, value: ' + value + ', index: ' + index);
14. })
15. .onScrollStop((value: string | string[], index: number | number[]) => {
16. console.info('Picker scroll stopped, value: ' + value + ', index: ' + index);
17. })
18. .canLoop(this.isLoop)

20. Row() {
21. Text('循环滚动').fontSize(20)

23. Toggle({ type: ToggleType.Switch, isOn: false })
24. .onChange((isOn: boolean) => {
25. this.isLoop = isOn;
26. })
27. }.position({ x: '60%', y: '40%' })

29. }.width('100%')
30. }
31. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/_oopyioKQ3G8wbj0o_cQdQ/zh-cn_image_0000002589326103.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055158Z&HW-CC-Expire=86400&HW-CC-Sign=24DAE92865838620A9B0CF71247DAFFC0558F402A24E32A21A91EED5CB3049B9)

### 示例8（设置选中项索引值）

该示例通过配置[selectedIndex](ts-basic-components-textpicker.md#selectedindex10)设置默认选中项的索引值。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextPickerExample {
5. private fruits: string[] = ['apple1', 'orange2', 'peach3', 'grape4'];

7. build() {
8. Column() {
9. TextPicker({ range: this.fruits, selected: 1 })
10. .selectedIndex(2)
11. .onChange((value: string | string[], index: number | number[]) => {
12. console.info('Picker item changed, value: ' + value + ', index: ' + index);
13. })
14. .onScrollStop((value: string | string[], index: number | number[]) => {
15. console.info('Picker scroll stopped, value: ' + value + ', index: ' + index);
16. })
17. }.width('100%').height('100%')
18. }
19. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/z6DggAtZTeauy7u1ztLy3Q/zh-cn_image_0000002589246045.png?HW-CC-KV=V1&HW-CC-Date=20260429T055158Z&HW-CC-Expire=86400&HW-CC-Sign=37DD195C3529329A9B103404D924CA129704722493E7DD6862388A2D40EF7A7D)

### 示例9（设置关闭文本样式变化动效与对应文本样式）

该示例通过配置[disableTextStyleAnimation](ts-basic-components-textpicker.md#disabletextstyleanimation15)、[defaultTextStyle](ts-basic-components-textpicker.md#defaulttextstyle15)实现关闭文本选择器文本样式变化的动效，并设置文本样式。

从API version 15开始，新增disableTextStyleAnimation、defaultTextStyle接口。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextPickerExample {
5. private select: number = 1;
6. private fruits: string[] = ['AAAAA', 'BBBBBBBBBBBBB', 'CCCC', 'DDDDDDDD', 'EEE'];

8. build() {
9. Column() {
10. TextPicker({
11. range: this.fruits,
12. selected: this.select,
13. value: this.fruits[this.select]
14. })
15. .disableTextStyleAnimation(true)
16. .margin({ bottom: 30 })
17. TextPicker({
18. range: this.fruits,
19. selected: this.select,
20. value: this.fruits[this.select]
21. })
22. .disableTextStyleAnimation(true)
23. .defaultTextStyle({ minFontSize: 18, maxFontSize: 28, overflow: TextOverflow.Ellipsis })
24. }.width('100%').height('100%')
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/3GDUfFCdQqK83HFYZtaUQQ/zh-cn_image_0000002558766236.jpeg?HW-CC-KV=V1&HW-CC-Date=20260429T055158Z&HW-CC-Expire=86400&HW-CC-Sign=38232904F1247BEEFA9F6F2EB379BE81B2BB20827B1BAD054B1088B9664673E6)

### 示例10（设置选中项背景样式）

该示例通过配置[selectedBackgroundStyle](ts-basic-components-textpicker.md#selectedbackgroundstyle20)实现文本选择器选中项的背景样式。

```
1. import { LengthUnit } from '@kit.ArkUI';

3. // xxx.ets
4. @Entry
5. @Component
6. struct TextPickerExample {
7. private showText1: string [] =
8. ['Text1', 'Text1', 'Text1', 'Text1']
9. private showText2: string[] [] =
10. [
11. ['Text2', 'Text2', 'Text2', 'Text2'],
12. ['Text3', 'Text3', 'Text3', 'Text3']
13. ]

15. build() {
16. Column() {
17. Row() {
18. TextPicker({ range: this.showText1 })
19. .selectedBackgroundStyle({
20. color: '#FFD5D5D5',
21. borderRadius: { value: 0, unit: LengthUnit.VP }
22. })
23. Column()
24. .width('10%')
25. TextPicker({ range: this.showText1 })
26. .selectedBackgroundStyle({
27. color: '#FFE3F8F9',
28. borderRadius: {
29. topStart: { value: 5, unit: LengthUnit.VP },
30. topEnd: { value: 10, unit: LengthUnit.VP },
31. bottomStart: { value: 15, unit: LengthUnit.VP },
32. bottomEnd: { value: 20, unit: LengthUnit.VP },
33. }
34. })
35. }

37. Row()
38. .height('10%')
39. Row() {
40. TextPicker({ range: this.showText2 })
41. .selectedBackgroundStyle({
42. borderRadius: {
43. topLeft: 8,
44. topRight: 8,
45. bottomLeft: 8,
46. bottomRight: 8
47. },
48. color: '#FFFFEEF6'
49. })
50. }
51. }.height('100%')
52. }
53. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/amIvKGMXT_26tcP70rm3MQ/zh-cn_image_0000002558606578.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055158Z&HW-CC-Expire=86400&HW-CC-Sign=DD357B715B293FF9B2636B0484EDFC7280350307297BF1E9F2C1D188F70D9C9A)

### 示例11（设置文本的最大字号、最小字号、超长文本截断方式）

该示例通过配置[disappearTextStyle](ts-basic-components-textpicker.md#disappeartextstyle20)、[textStyle](ts-basic-components-textpicker.md#textstyle20)和[selectedTextStyle](ts-basic-components-textpicker.md#selectedtextstyle20)，设置文本的颜色、最大字号、最小字号、超长文本截断方式。

从API version 20开始，新增disappearTextStyle、textStyle和selectedTextStyle接口。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextPickerExample {
5. private rangeValue: string[] = ['AAAAA', 'BBBBBBBBBBBBB', 'CCCC', 'DDDDDDDD', 'EEEEEEEEEEEEEEE'];

7. build() {
8. RelativeContainer() {
9. TextPicker({
10. range: this.rangeValue
11. })
12. .disappearTextStyle({
13. color: '#fff52769',
14. // 设置minFontSize与maxFontSize时，font中的size属性将被忽略。
15. font: { size: 50 },
16. minFontSize: 12,
17. maxFontSize: 18,
18. overflow: TextOverflow.Ellipsis
19. })
20. .textStyle({
21. color: Color.Orange,
22. minFontSize: 12,
23. maxFontSize: 18,
24. overflow: TextOverflow.MARQUEE
25. })
26. .selectedTextStyle({
27. color: '#ff9eea48',
28. minFontSize: 12,
29. maxFontSize: 18,
30. overflow: TextOverflow.Clip
31. })
32. .width('100%')
33. }
34. .height('100%')
35. .width('100%')
36. }
37. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/WqbQveKmRWa_dH3Or5Adyw/zh-cn_image_0000002589326105.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055158Z&HW-CC-Expire=86400&HW-CC-Sign=D74EAB66AE5A2C2F00B58587D2BAD733927935B98B334CCA03278B4263D1AE88)
