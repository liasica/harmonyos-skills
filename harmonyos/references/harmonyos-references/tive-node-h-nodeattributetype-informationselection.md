---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/tive-node-h-nodeattributetype-informationselection
title: ArkUI_NodeAttributeType（信息选择类组件相关属性）
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > native_node.h > ArkUI_NodeAttributeType（信息选择类组件相关属性）
category: harmonyos-references
scraped_at: 2026-04-29T13:54:15+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:15b1800bb19249b0337348fe903306d1e7f1a18ebf96aa71d3db45953b1796e8
---

```
1. enum ArkUI_NodeAttributeType
```

## 概述

定义ArkUI在Native侧可以设置信息选择类组件相关属性样式集合，包含DatePicker、TimePicker、TextPicker、CalendarPicker等组件属性设置。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_node.h](capi-native-node-h.md)

## NODE\_DATE\_PICKER\_LUNAR

```
1. NODE_DATE_PICKER_LUNAR = MAX_NODE_SCOPE_NUM * ARKUI_NODE_DATE_PICKER = 13000
```

设置日期选择器组件的日期是否显示农历，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否显示农历，默认值false。false表示不展示农历，true表示展示农历。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否显示农历。 |

## NODE\_DATE\_PICKER\_START

```
1. NODE_DATE_PICKER_START = 13001
```

设置日期选择器组件选择器的起始日期，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 日期，默认值"1970-1-1"。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 日期。 |

## NODE\_DATE\_PICKER\_END

```
1. NODE_DATE_PICKER_END = 13002
```

设置日期选择器组件选择器的结束日期，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 日期，默认值"2100-12-31"。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 日期。 |

## NODE\_DATE\_PICKER\_SELECTED

```
1. NODE_DATE_PICKER_SELECTED = 13003
```

设置日期选择器组件选中项的日期，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 日期，默认值"2024-01-22"。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 日期。 |

## NODE\_DATE\_PICKER\_DISAPPEAR\_TEXT\_STYLE

```
1. NODE_DATE_PICKER_DISAPPEAR_TEXT_STYLE = 13004
```

设置日期选择器组件的所有选项中最上和最下两个选项的文本颜色、字号、字体粗细，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 入参5个，格式为字符串，以 ';' 分割：  入参1： 文本颜色，#argb类型。  入参2： 文本大小，数字类型，单位fp。  入参3： 文本粗细，字符串枚举("bold", "normal", "bolder", "lighter", "medium", "regular")。  入参4： 文本字体列表，使用 ',' 进行分割。  入参5： 文本样式，字符串枚举("normal", "italic")。  如 "#ff182431;14;normal;Arial,HarmonyOS Sans;normal" 。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 参数5个，格式为字符串，以 ';' 分割：  参数1： 文本颜色，#argb类型。  参数2： 文本大小，数字类型，单位fp。  参数3： 文本粗细，字符串枚举("bold", "normal", "bolder", "lighter", "medium", "regular")。  参数4： 文本字体列表，使用 ',' 进行分割。  参数5： 文本样式，字符串枚举("normal", "italic")。  如 "#ff182431;14;normal;Arial,HarmonyOS Sans;normal" 。 |

## NODE\_DATE\_PICKER\_TEXT\_STYLE

```
1. NODE_DATE_PICKER_TEXT_STYLE = 13005
```

设置日期选择器组件的所有选项中除了最上、最下及选中项以外的文本颜色、字号、字体粗细，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 入参5个，格式为字符串，以 ';' 分割：  入参1： 文本颜色，#argb类型。  入参2： 文本大小，数字类型，单位fp。  入参3： 文本粗细，字符串枚举("bold", "normal", "bolder", "lighter", "medium", "regular")。  入参4： 文本字体列表，使用 ',' 进行分割。  入参5： 文本样式，字符串枚举("normal", "italic")。  如 "#ff182431;14;normal;Arial,HarmonyOS Sans;normal" 。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 参数5个，格式为字符串，以 ';' 分割：  参数1： 文本颜色，#argb类型。  参数2： 文本大小，数字类型，单位fp。  参数3： 文本粗细，字符串枚举("bold", "normal", "bolder", "lighter", "medium", "regular")。  参数4： 文本字体列表，使用 ',' 进行分割。  参数5： 文本样式，字符串枚举("normal", "italic")。  如 "#ff182431;14;normal;Arial,HarmonyOS Sans;normal" 。 |

## NODE\_DATE\_PICKER\_SELECTED\_TEXT\_STYLE

```
1. NODE_DATE_PICKER_SELECTED_TEXT_STYLE = 13006
```

设置日期选择器组件的选中项的文本颜色、字号、字体粗细，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 入参5个，格式为字符串，以 ';' 分割：  入参1： 文本颜色，#argb类型。  入参2： 文本大小，数字类型，单位fp。  入参3： 文本粗细，字符串枚举("bold", "normal", "bolder", "lighter", "medium", "regular")。  入参4： 文本字体列表，使用 ',' 进行分割。  入参5： 文本样式，字符串枚举("normal", "italic")。  如 "#ff182431;14;normal;Arial,HarmonyOS Sans;normal" 。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 参数5个，格式为字符串，以 ';' 分割：  参数1： 文本颜色，#argb类型。  参数2： 文本大小，数字类型，单位fp。  参数3： 文本粗细，字符串枚举("bold", "normal", "bolder", "lighter", "medium", "regular")。  参数4： 文本字体列表，使用 ',' 进行分割。  参数5： 文本样式，字符串枚举("normal", "italic")。  如 "#ff182431;14;normal;Arial,HarmonyOS Sans;normal" 。 |

## NODE\_DATE\_PICKER\_MODE

```
1. NODE_DATE_PICKER_MODE = 13007
```

设置要显示的日期选项列。DatePicker显示不同样式的日期列，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 显示的日期列类型。参数类型[ArkUI\_DatePickerMode](capi-native-type-h.md#arkui_datepickermode)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 显示的日期列类型。参数类型[ArkUI\_DatePickerMode](capi-native-type-h.md#arkui_datepickermode)。 |

## NODE\_DATE\_PICKER\_ENABLE\_HAPTIC\_FEEDBACK

```
1. NODE_DATE_PICKER_ENABLE_HAPTIC_FEEDBACK = 13008
```

设置是否开启触控反馈。支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 是否开启触控反馈。默认值：true，true表示开启触控反馈，false则表示不开启触控反馈。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 是否开启触控反馈。 |

## NODE\_DATE\_PICKER\_CAN\_LOOP

```
1. NODE_DATE_PICKER_CAN_LOOP = 13009
```

Picker组件可循环滚动属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | false表示不可循环，true表示可循环。默认值：true，设置异常值时使用默认值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 0表示不可循环，1表示可循环。  说明：可循环情况下，年份随着月份的循环滚动进行联动加减，月份随着日的循环滚动进行联动加减。  不可循环情况下，年/月/日到达本列的顶部或底部时，无法再进行滚动，年/月/日之间也无法再联动加减。 |

## NODE\_TIME\_PICKER\_SELECTED

```
1. NODE_TIME_PICKER_SELECTED = MAX_NODE_SCOPE_NUM * ARKUI_NODE_TIME_PICKER = 14000
```

设置时间选择器组件的选中项时间，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 时间。默认值：当前系统时间。格式：仅支持时、分输入（例：23:59/23-59）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 时间。默认值：当前系统时间。格式：时、分、秒（例：23,59,1）。 |

## NODE\_TIME\_PICKER\_USE\_MILITARY\_TIME

```
1. NODE_TIME_PICKER_USE_MILITARY_TIME = 14001
```

设置时间选择组件展示时间是否为24小时制，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否为24小时制，默认值：false。false表示展示时间为12小时制，true表示展示时间为24小时制。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否为24小时制。 |

## NODE\_TIME\_PICKER\_DISAPPEAR\_TEXT\_STYLE

```
1. NODE_TIME_PICKER_DISAPPEAR_TEXT_STYLE = 14002
```

设置边缘项（以选中项为基准向上或向下的第二项）的文本样式，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 入参5个，格式为字符串，以 ';' 分割：  入参1： 文本颜色，#argb类型。  入参2： 文本大小，数字类型，单位fp。  入参3： 文本粗细，字符串枚举("bold", "normal", "bolder", "lighter", "medium", "regular")。  入参4： 文本字体列表，使用 ',' 进行分割。  入参5： 文本样式，字符串枚举("normal", "italic")。  如 "#ff182431;14;normal;Arial,HarmonyOS Sans;normal" 。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 参数5个，格式为字符串，以 ';' 分割：  参数1： 文本颜色，#argb类型。  参数2： 文本大小，数字类型，单位fp。  参数3： 文本粗细，字符串枚举("bold", "normal", "bolder", "lighter", "medium", "regular")。  参数4： 文本字体列表，使用 ',' 进行分割。  参数5： 文本样式，字符串枚举("normal", "italic")。  如 "#ff182431;14;normal;Arial,HarmonyOS Sans;normal" 。 |

## NODE\_TIME\_PICKER\_TEXT\_STYLE

```
1. NODE_TIME_PICKER_TEXT_STYLE = 14003
```

设置设置边缘项（以选中项为基准向上或向下的第二项）的文本样式，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 入参5个，格式为字符串，以 ';' 分割：  入参1： 文本颜色，#argb类型。  入参2： 文本大小，数字类型，单位fp。  入参3： 文本粗细，字符串枚举("bold", "normal", "bolder", "lighter", "medium", "regular")。  入参4： 文本字体列表，使用 ',' 进行分割。  入参5： 文本样式，字符串枚举("normal", "italic")。  如 "#ff182431;14;normal;Arial,HarmonyOS Sans;normal" 。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 参数5个，格式为字符串，以 ';' 分割：  参数1： 文本颜色，#argb类型。  参数2： 文本大小，数字类型，单位fp。  参数3： 文本粗细，字符串枚举("bold", "normal", "bolder", "lighter", "medium", "regular")。  参数4： 文本字体列表，使用 ',' 进行分割。  参数5： 文本样式，字符串枚举("normal", "italic")。  如 "#ff182431;14;normal;Arial,HarmonyOS Sans;normal" 。 |

## NODE\_TIME\_PICKER\_SELECTED\_TEXT\_STYLE

```
1. NODE_TIME_PICKER_SELECTED_TEXT_STYLE = 14004
```

设置时间选择组件选中项的文本颜色、字号、字体粗细，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 入参5个，格式为字符串，以 ';' 分割：  入参1： 文本颜色，#argb类型。  入参2： 文本大小，数字类型，单位fp。  入参3： 文本粗细，字符串枚举("bold", "normal", "bolder", "lighter", "medium", "regular")。  入参4： 文本字体列表，使用 ',' 进行分割。  入参5： 文本样式，字符串枚举("normal", "italic")。  如 "#ff182431;14;normal;Arial,HarmonyOS Sans;normal" 。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 参数5个，格式为字符串，以 ';' 分割：  参数1： 文本颜色，#argb类型。  参数2： 文本大小，数字类型，单位fp。  参数3： 文本粗细，字符串枚举("bold", "normal", "bolder", "lighter", "medium", "regular")。  参数4： 文本字体列表，使用 ',' 进行分割。  参数5： 文本样式，字符串枚举("normal", "italic")。  如 "#ff182431;14;normal;Arial,HarmonyOS Sans;normal" 。 |

## NODE\_TIME\_PICKER\_START

```
1. NODE_TIME_PICKER_START = 14005
```

设置时间选择器组件的起始时间，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 时间。默认值："0:0:0"。格式：仅支持时、分输入（例：12:59/12-59）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 时间。默认值："0:0:0"。格式：时、分、秒（例：12:59:0）。 |

## NODE\_TIME\_PICKER\_END

```
1. NODE_TIME_PICKER_END = 14006
```

设置时间选择器组件的结束日期，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 时间。默认值："23:59:59"。格式：仅支持时、分输入（例：23:59/23-59）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 时间。默认值："23:59:59"。格式：时、分、秒（例：23:59:0）。 |

## NODE\_TIME\_PICKER\_ENABLE\_CASCADE

```
1. NODE_TIME_PICKER_ENABLE_CASCADE = 14007
```

在设置12小时制时，上午和下午的标识会根据小时数自动切换，支持属性设置、重置和获取。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 在12小时制时，设置上午和下午的标识是否会根据小时数自动切换，默认值：false。false表示不自动切换，true表示自动切换。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 在12小时制时，设置上午和下午的标识是否会根据小时数自动切换。 |

## NODE\_TEXT\_PICKER\_OPTION\_RANGE

```
1. NODE_TEXT_PICKER_OPTION_RANGE = MAX_NODE_SCOPE_NUM * ARKUI_NODE_TEXT_PICKER = 15000
```

设置滑动选择文本选择器的选择列表，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 使用的选择器类型[ArkUI\_TextPickerRangeType](capi-native-type-h.md#arkui_textpickerrangetype)，默认值为ARKUI\_TEXTPICKER\_RANGETYPE\_SINGLE。 |
| ?.string | 针对不同选择器类型有如下输入范式：  1：单列选择器，入参格式为用分号分隔的一组字符串；  2：多列选择器，支持多对纯文本字符串对，多对之间使用分号分隔，每对内部使用逗号分隔。 |
| ?.object | 针对不同选择器类型有如下输入范式：  1：单列支持图片的选择器，输入结构体为[ARKUI\_TextPickerRangeContentArray](kui-nativemodule-arkui-textpickerrangecontentarray.md)；  2：多列联动选择器，输入结构体为[ARKUI\_TextCascadePickerRangeContentArray](ivemodule-arkui-textcascadepickerrangecontentarray.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 使用的选择器类型[ArkUI\_TextPickerRangeType](capi-native-type-h.md#arkui_textpickerrangetype)。 |
| ?.string | 针对不同选择器类型有如下输出范式：  1：单列选择器，输出格式为用分号分隔的一组字符串；  2：多列选择器，输出多对纯文本字符串对，多对之间使用分号分隔，每对内部使用逗号分隔。 |

## NODE\_TEXT\_PICKER\_OPTION\_SELECTED

```
1. NODE_TEXT_PICKER_OPTION_SELECTED = 15001
```

设置滑动选择文本内容的组件默认选中项在数组中的索引值，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 索引值，如存在多个索引值则逐个添加。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 索引值，如存在多个索引值则逐个添加。 |

## NODE\_TEXT\_PICKER\_OPTION\_VALUE

```
1. NODE_TEXT_PICKER_OPTION_VALUE = 15002
```

设置滑动选择文本内容的组件默认选中项的值，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 选中项的值，如存在多个值则逐个添加，用分号分隔。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 选中项的值，如存在多个值则逐个添加，用分号分隔。 |

## NODE\_TEXT\_PICKER\_DISAPPEAR\_TEXT\_STYLE

```
1. NODE_TEXT_PICKER_DISAPPEAR_TEXT_STYLE = 15003
```

设置滑动选择文本内容的组件所有选项中最上和最下两个选项的文本颜色、字号、字体粗细，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 入参5个，格式为字符串，以 ';' 分割：  入参1： 文本颜色，#argb类型  入参2： 文本大小，数字类型，单位fp  入参3： 文本粗细，字符串枚举("bold", "normal", "bolder", "lighter", "medium", "regular")  入参4： 文本字体列表，使用 ',' 进行分割  入参5： 文本样式，字符串枚举("normal", "italic")  如 "#ff182431;14;normal;Arial,HarmonyOS Sans;normal" 。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 参数5个，格式为字符串，以 ';' 分割：  参数1： 文本颜色，#argb类型  参数2： 文本大小，数字类型，单位fp  参数3： 文本粗细，字符串枚举("bold", "normal", "bolder", "lighter", "medium", "regular")  参数4： 文本字体列表，使用 ',' 进行分割  参数5： 文本样式，字符串枚举("normal", "italic")  如 "#ff182431;14;normal;Arial,HarmonyOS Sans;normal" 。 |

## NODE\_TEXT\_PICKER\_TEXT\_STYLE

```
1. NODE_TEXT_PICKER_TEXT_STYLE = 15004
```

设置滑动选择文本内容的组件所有选项中除了最上、最下及选中项以外的文本颜色、字号、字体粗细，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 入参5个，格式为字符串，以 ';' 分割：  入参1： 文本颜色，#argb类型。  入参2： 文本大小，数字类型，单位fp。  入参3： 文本粗细，字符串枚举("bold", "normal", "bolder", "lighter", "medium", "regular")。  入参4： 文本字体列表，使用 ',' 进行分割。  入参5： 文本样式，字符串枚举("normal", "italic")。  如 "#ff182431;14;normal;Arial,HarmonyOS Sans;normal" 。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 参数5个，格式为字符串，以 ';' 分割：  参数1： 文本颜色，#argb类型。  参数2： 文本大小，数字类型，单位fp。  参数3： 文本粗细，字符串枚举("bold", "normal", "bolder", "lighter", "medium", "regular")。  参数4： 文本字体列表，使用 ',' 进行分割。  参数5： 文本样式，字符串枚举("normal", "italic")。  如 "#ff182431;14;normal;Arial,HarmonyOS Sans;normal" 。 |

## NODE\_TEXT\_PICKER\_SELECTED\_TEXT\_STYLE

```
1. NODE_TEXT_PICKER_SELECTED_TEXT_STYLE = 15005
```

设置滑动选择文本内容的组件选中项的文本颜色、字号、字体粗细，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 入参5个，格式为字符串，以 ';' 分割：  入参1： 文本颜色，#argb类型；  入参2： 文本大小，数字类型，单位fp；  入参3： 文本粗细，字符串枚举("bold", "normal", "bolder", "lighter", "medium", "regular")；  入参4： 文本字体列表，使用 ',' 进行分割；  入参5： 文本样式，字符串枚举("normal", "italic")；  如 "#ff182431;14;normal;Arial,HarmonyOS Sans;normal" 。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 参数5个，格式为字符串，以 ';' 分割：  参数1： 文本颜色，#argb类型；  参数2： 文本大小，数字类型，单位fp；  参数3： 文本粗细，字符串枚举("bold", "normal", "bolder", "lighter", "medium", "regular")；  参数4： 文本字体列表，使用 ',' 进行分割；  参数5： 文本样式，字符串枚举("normal", "italic")；  如 "#ff182431;14;normal;Arial,HarmonyOS Sans;normal" 。 |

## NODE\_TEXT\_PICKER\_SELECTED\_INDEX

```
1. NODE_TEXT_PICKER_SELECTED_INDEX = 15006
```

设置滑动选择文本内容的组件默认选中项在数组中的索引值，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0...].i32 | 默认选中项在数组中的索引值数组。 |

## NODE\_TEXT\_PICKER\_CAN\_LOOP

```
1. NODE_TEXT_PICKER_CAN_LOOP = 15007
```

Picker组件可循环滚动属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | false表示不可循环，true表示可循环。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 0表示不可循环，1表示可循环。 |

## NODE\_TEXT\_PICKER\_DEFAULT\_PICKER\_ITEM\_HEIGHT

```
1. NODE_TEXT_PICKER_DEFAULT_PICKER_ITEM_HEIGHT = 15008
```

Picker各选择项的高度属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 子项高度属性，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 子项高度属性，单位为vp。 |

## NODE\_TEXT\_PICKER\_COLUMN\_WIDTHS

```
1. NODE_TEXT_PICKER_COLUMN_WIDTHS = 15009
```

设置每一个选择项列宽，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 设置的第1个选择项列宽，为总宽度的百分比。默认情况下，所有选择项的列宽相等。 |
| .value[1]?.f32 | 设置的第2个选择项列宽，为总宽度的百分比。默认情况下，所有选择项的列宽相等。 |
| .value[2]?.f32 | 设置的第3个选择项列宽，为总宽度的百分比。默认情况下，所有选择项的列宽相等。  ...。 |
| .value[n]?.f32 | 设置的第n+1个选择项列宽，为总宽度的百分比。默认情况下，所有选择项的列宽相等。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 第1列宽度，总宽度的百分比。 |
| .value[1].f32 | 第2列宽度，总宽度的百分比。 |
| .value[2].f32 | 第3列宽度，总宽度的百分比。  ...。 |
| .value[n].f32 | 第n+1列宽度，总宽度的百分比。 |

## NODE\_TEXT\_PICKER\_ENABLE\_HAPTIC\_FEEDBACK

```
1. NODE_TEXT_PICKER_ENABLE_HAPTIC_FEEDBACK = 15010
```

设置是否开启触控反馈。支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 是否开启触控反馈。默认值：true，true表示开启触控反馈，false则表示不开启触控反馈。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 是否开启触控反馈。 |

## NODE\_TEXT\_PICKER\_SELECTED\_BACKGROUND\_STYLE

```
1. NODE_TEXT_PICKER_SELECTED_BACKGROUND_STYLE = 15011
```

设置选中项的背景颜色和边框圆角。支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 背景颜色，采用 0xARGB 格式，例如，**0xFF1122FF**。 |
| .value[1].f32 | 四个角的圆角半径，单位为VP。 |
| .value[1].f32 | 左上角的圆角半径，单位为VP。 |
| .value[2].f32 | 右上角的圆角半径，单位为VP。 |
| .value[3].f32 | 左下角的圆角半径，单位为VP。 |
| .value[4].f32 | 右下角的圆角半径，单位为VP。  默认值：背景颜色：0x0C182431；圆角半径：24.0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 背景颜色，采用 0xARGB 格式，例如，**0xFF1122FF**。 |
| .value[1].f32 | 左上角的圆角半径，单位为VP。 |
| .value[2].f32 | 右上角的圆角半径，单位为VP。 |
| .value[3].f32 | 左下角的圆角半径，单位为VP。 |
| .value[4].f32 | 右下角的圆角半径，单位为VP。 |

## NODE\_PICKER\_OPTION\_SELECTED\_INDEX

```
1. NODE_PICKER_OPTION_SELECTED_INDEX = MAX_NODE_SCOPE_NUM * ARKUI_NODE_PICKER
```

定义选择器数据选择范围内默认选中项的索引。支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 索引值。默认值：0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 索引值。 |

## NODE\_PICKER\_ENABLE\_HAPTIC\_FEEDBACK

```
1. NODE_PICKER_ENABLE_HAPTIC_FEEDBACK = 1018001
```

定义是否启用触感反馈。支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否启用触感反馈。true表示启用反馈，false表示不启用。默认值：true。开启后，是否存在触控反馈取决于系统硬件支持情况。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否启用反馈。 |

## NODE\_PICKER\_CAN\_LOOP

```
1. NODE_PICKER_CAN_LOOP = 1018002
```

定义选择器是否支持滚动循环。支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否支持滚动循环。true表示支持滚动循环，false表示不支持。默认值：true。  如果子组件的个数小于8个，无论设置为true还是false，都不会循环滚动。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否支持滚动循环。值为true表示支持滚动循环，false表示不支持。 |

## NODE\_PICKER\_SELECTION\_INDICATOR

```
1. NODE_PICKER_SELECTION_INDICATOR = 1018003
```

设置选择指示器的类型和参数。支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 参数类型为[ArkUI\_PickerIndicatorStyle](capi-arkui-nativemodule-arkui-pickerindicatorstyle.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .object | 参数类型为[ArkUI\_PickerIndicatorStyle](capi-arkui-nativemodule-arkui-pickerindicatorstyle.md)。 |

## NODE\_CALENDAR\_PICKER\_HINT\_RADIUS

```
1. NODE_CALENDAR_PICKER_HINT_RADIUS = MAX_NODE_SCOPE_NUM * ARKUI_NODE_CALENDAR_PICKER = 16000
```

设置日历选中态底板圆角半径的参数，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 日历选中态底板圆角半径，默认值：16.0，单位为vp，表示底板样式为圆形。当输入参数为0.0时表示底板样式为直角矩形；当输入参数为(0.0, 16.0)时，底板样式为圆角矩形；当输入参数为负数或大于16.0时，恢复成默认值16.0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 日历选中态底板圆角半径，默认值：16.0，单位为vp，表示底板样式为圆形。取值范围[0.0, 16.0]，其中取值为0.0表示底板样式为直角矩形。 |

## NODE\_CALENDAR\_PICKER\_SELECTED\_DATE

```
1. NODE_CALENDAR_PICKER_SELECTED_DATE = 16001
```

设置日历选择选中日期的参数，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 选中的年。 |
| .value[1].u32 | 选中的月。 |
| .value[2].u32 | 选中的日。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 选中的年。 |
| .value[1].u32 | 选中的月。 |
| .value[2].u32 | 选中的日。 |

## NODE\_CALENDAR\_PICKER\_EDGE\_ALIGNMENT

```
1. NODE_CALENDAR_PICKER_EDGE_ALIGNMENT = 16002
```

设置日历选择器与入口组件的对齐方式，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 对齐方式类型，参数类型[ArkUI\_CalendarAlignment](capi-native-type-h.md#arkui_calendaralignment)。 |
| .value[1]?.f32 | 按照对齐方式对齐后，选择器相对入口组件的x轴方向相对偏移。 |
| .value[2]?.f32 | 按照对齐方式对齐后，选择器相对入口组件的y轴方向相对偏移。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 对齐方式类型，参数类型[ArkUI\_CalendarAlignment](capi-native-type-h.md#arkui_calendaralignment)。 |
| .value[1].f32 | 按照对齐方式对齐后，选择器相对入口组件的x轴方向相对偏移。 |
| .value[2].f32 | 按照对齐方式对齐后，选择器相对入口组件的y轴方向相对偏移。 |

## NODE\_CALENDAR\_PICKER\_TEXT\_STYLE

```
1. NODE_CALENDAR_PICKER_TEXT_STYLE = 16003
```

设置日历选择器入口区的文本颜色、字号、字体粗细。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0]?.u32 | 入口区的文本颜色。 |
| .value[1]?.f32 | 入口区的文本字号，单位为fp。 |
| .value[2]?.i32 | 入口区的文本字体粗细，参数类型[ArkUI\_FontWeight](capi-native-type-h.md#arkui_fontweight)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 入口区的文本颜色。 |
| .value[1].f32 | 入口区的文本字号，单位为fp。 |
| .value[2].i32 | 入口区的文本字体粗细，参数类型[ArkUI\_FontWeight](capi-native-type-h.md#arkui_fontweight)。 |

## NODE\_CALENDAR\_PICKER\_START

```
1. NODE_CALENDAR_PICKER_START = 16004
```

设置日历选择器的开始日期，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 日期。值的格式如 "1970-1-1"。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 日期。 |

## NODE\_CALENDAR\_PICKER\_END

```
1. NODE_CALENDAR_PICKER_END = 16005
```

设置日历选择器的结束日期，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 日期。值的格式如 "2100-12-31"。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 日期。 |

## NODE\_CALENDAR\_PICKER\_DISABLED\_DATE\_RANGE

```
1. NODE_CALENDAR_PICKER_DISABLED_DATE_RANGE = 16006
```

设置日历选择器的禁用日期区间，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 禁用日期区间字符串。禁用日期区间："第一个区间开始日期,第一个区间结束日期,第二个区间开始日期,第二个区间结束日期,...,第n个区间开始日期,第n个区间结束日期"。  设置的禁用日期区间格式："1910-01-01,1910-12-31,2020-01-01,2020-12-31"。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 禁用日期区间字符串。 |

## NODE\_CALENDAR\_PICKER\_MARK\_TODAY

```
1. NODE_CALENDAR_PICKER_MARK_TODAY = 16007
```

设置日历选择器在系统当前日期时，是否保持高亮显示，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 日历选择器在系统当前日期时，是否保持高亮显示，默认值：false。false表示不保持高亮显示，true表示保持高亮显示。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 日历选择器在系统当前日期时，是否保持高亮显示。 |
