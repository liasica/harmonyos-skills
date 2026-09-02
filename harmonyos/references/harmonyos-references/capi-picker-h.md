---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-picker-h
title: picker.h
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > picker.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:20+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:cf4b65a8af6c0275b586312d741ab3b8ad03dcc59239fa7038a3d2f99e80304b
---

## 概述

为NativeNode API提供Picker节点类型定义，支持日期选择器、文本选择器等多种类型的选择器组件，适用于需要在原生层实现滚动选择功能的场景，提供了丰富的样式配置和数据联动能力，帮助开发者灵活构建各类选择交互。

**引用文件：** <arkui/node\_attributes/picker.h>

**库：** libace\_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**相关示例：** [NativeTypeSample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeType/native_type_sample)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ARKUI\_TextPickerRangeContent](capi-arkui-nativemodule-arkui-textpickerrangecontent.md) | ARKUI\_TextPickerRangeContent | 定义单列滑动数据选择器支持的图片资源结构体。 |
| [ARKUI\_TextPickerCascadeRangeContent](capi-arkui-nativemodule-arkui-textpickercascaderangecontent.md) | ARKUI\_TextPickerCascadeRangeContent | 定义多列联动滑动数据选择器的结构体。 |
| [ArkUI\_PickerIndicatorBackground](capi-arkui-nativemodule-arkui-pickerindicatorbackground.md) | ArkUI\_PickerIndicatorBackground | 背景样式指示器的样式参数。 |
| [ArkUI\_PickerIndicatorDivider](capi-arkui-nativemodule-arkui-pickerindicatordivider.md) | ArkUI\_PickerIndicatorDivider | 分割线样式指示器的样式参数。 |
| [ArkUI\_PickerIndicatorStyle](capi-arkui-nativemodule-arkui-pickerindicatorstyle.md) | ArkUI\_PickerIndicatorStyle | 选中项指示器的样式。 |
| [ArkUI\_TextPickerRangeContentArray](capi-arkui-nativemodule-arkui-textpickerrangecontentarray.md) | ArkUI\_TextPickerRangeContentArray | 定义文本选择器的数据选择列表。 |
| [ArkUI\_TextCascadePickerRangeContentArray](capi-arkui-nativemodule-arkui-textcascadepickerrangecontentarray.md) | ArkUI\_TextCascadePickerRangeContentArray | 定义多列联动数据选择器的列表。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [ArkUI\_DatePickerMode](capi-picker-h.md#arkui_datepickermode) | ArkUI\_DatePickerMode | 定义日期选择器列显示模式的枚举值。 |
| [ArkUI\_TextPickerRangeType](capi-picker-h.md#arkui_textpickerrangetype) | ArkUI\_TextPickerRangeType | 定义滑动选择文本选择器输入类型。 |
| [ArkUI\_CalendarAlignment](capi-picker-h.md#arkui_calendaralignment) | ArkUI\_CalendarAlignment | 日历选择器与入口组件对齐方式。 |
| [ArkUI\_PickerIndicatorType](capi-picker-h.md#arkui_pickerindicatortype) | ArkUI\_PickerIndicatorType | 选择器的选中指示器类型。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [ArkUI\_TextPickerRangeContentArray\* OH\_ArkUI\_TextPickerRangeContentArray\_Create(int32\_t length)](capi-picker-h.md#oh_arkui_textpickerrangecontentarray_create) | 创建TextPickerRangeContent数组的对象，用于构建单列滑动数据选择器的数据列表，常见于日期选择、时间选择、列表选择等场景。创建后必须在使用完毕后调用OH\_ArkUI\_TextPickerRangeContentArray\_Destroy释放资源，否则会导致内存泄漏。 |
| [void OH\_ArkUI\_TextPickerRangeContentArray\_SetIconAtIndex(ArkUI\_TextPickerRangeContentArray\* handle, char\* icon, int32\_t index)](capi-picker-h.md#oh_arkui_textpickerrangecontentarray_seticonatindex) | 设置TextPickerRangeContent数组指定位置的icon数据，用于在单列文本选择器中设置带图标的选项，常见于图文混排列表、带图标提示的选项列表等场景。 |
| [void OH\_ArkUI\_TextPickerRangeContentArray\_SetTextAtIndex(ArkUI\_TextPickerRangeContentArray\* handle, char\* text, int32\_t index)](capi-picker-h.md#oh_arkui_textpickerrangecontentarray_settextatindex) | 设置TextPickerRangeContent数组指定位置的text数据，用于在数据选择器中设置文本内容，是构建选择器选项的必备步骤。 |
| [void OH\_ArkUI\_TextPickerRangeContentArray\_Destroy(ArkUI\_TextPickerRangeContentArray\* handle)](capi-picker-h.md#oh_arkui_textpickerrangecontentarray_destroy) | 销毁TextPickerRangeContent数组对象。此方法必须与OH\_ArkUI\_TextPickerRangeContentArray\_Create配对使用，用于释放创建的数组对象资源。 |
| [ArkUI\_TextCascadePickerRangeContentArray\* OH\_ArkUI\_TextCascadePickerRangeContentArray\_Create(int32\_t length)](capi-picker-h.md#oh_arkui_textcascadepickerrangecontentarray_create) | 创建TextCascadePickerRangeContent数组对象，用于构建多列联动数据选择器，常见于年月日联动选择、省市区三级联动选择等场景。创建后必须在使用完毕后调用OH\_ArkUI\_TextCascadePickerRangeContentArray\_Destroy释放资源，否则会导致内存泄漏。 |
| [void OH\_ArkUI\_TextCascadePickerRangeContentArray\_SetTextAtIndex (ArkUI\_TextCascadePickerRangeContentArray\* handle, char\* text, int32\_t index)](capi-picker-h.md#oh_arkui_textcascadepickerrangecontentarray_settextatindex) | 设置TextCascadePickerRangeContent数组指定位置的text数据，用于设置多列联动选择器的文本内容。 |
| [void OH\_ArkUI\_TextCascadePickerRangeContentArray\_SetChildAtIndex (ArkUI\_TextCascadePickerRangeContentArray\* handle, ArkUI\_TextCascadePickerRangeContentArray\* child, int32\_t index)](capi-picker-h.md#oh_arkui_textcascadepickerrangecontentarray_setchildatindex) | 设置TextCascadePickerRangeContent数组指定位置的child数据，用于设置多列联动选择器的子级数据，实现联动效果。 |
| [void OH\_ArkUI\_TextCascadePickerRangeContentArray\_Destroy (ArkUI\_TextCascadePickerRangeContentArray\* handle)](capi-picker-h.md#oh_arkui_textcascadepickerrangecontentarray_destroy) | 销毁TextCascadePickerRangeContent数组对象。此方法必须与OH\_ArkUI\_TextCascadePickerRangeContentArray\_Create配对使用，用于释放创建的数组对象资源。 |
| [ArkUI\_PickerIndicatorStyle\* OH\_ArkUI\_PickerIndicatorStyle\_Create(ArkUI\_PickerIndicatorType type)](capi-picker-h.md#oh_arkui_pickerindicatorstyle_create) | 创建选中项指示器的样式实例，用于高亮显示用户当前选中的选项，提升用户交互体验。创建后必须在使用完毕后调用OH\_ArkUI\_PickerIndicatorStyle\_Dispose释放资源，否则会导致内存泄漏。 |
| [void OH\_ArkUI\_PickerIndicatorStyle\_Dispose(ArkUI\_PickerIndicatorStyle\* style)](capi-picker-h.md#oh_arkui_pickerindicatorstyle_dispose) | 销毁选中项指示器的样式实例。此方法必须与OH\_ArkUI\_PickerIndicatorStyle\_Create配对使用，用于释放创建的样式实例资源。 |

## 枚举类型说明

### ArkUI\_DatePickerMode

```c
enum ArkUI_DatePickerMode
```

**描述**

定义日期选择器列显示模式的枚举值。

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_DATEPICKER\_MODE\_DATE = 0 | 默认值。日期列显示年、月、日三列，适用于需要完整日期信息的场景，如出生日期选择、预约日期选择等。 |
| ARKUI\_DATEPICKER\_YEAR\_AND\_MONTH = 1 | 日期列显示年、月二列，适用于只需年月信息的场景，如信用卡有效期选择、合同期限选择等。 |
| ARKUI\_DATEPICKER\_MONTH\_AND\_DAY = 2 | 日期列显示月、日二列，适用于只需月日信息的场景，如生日选择（不关注年份）、纪念日选择等。 |

### ArkUI\_TextPickerRangeType

```c
enum ArkUI_TextPickerRangeType
```

**描述**

定义滑动选择文本选择器输入类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_TEXTPICKER\_RANGETYPE\_SINGLE = 0 | 单列数据选择器，适用于单列数据选择场景，如性别选择、学历选择等。 |
| ARKUI\_TEXTPICKER\_RANGETYPE\_MULTI = 1 | 多列数据选择器，适用于多列独立数据选择场景，如时间选择（时、分、秒）、日期选择（年、月、日）等。 |
| ARKUI\_TEXTPICKER\_RANGETYPE\_RANGE\_CONTENT = 2 | 支持图片资源的单列数据选择器，适用于带图标的单列数据选择场景，如城市选择（带国旗图标）、产品分类选择等。 |
| ARKUI\_TEXTPICKER\_RANGETYPE\_CASCADE\_RANGE\_CONTENT = 3 | 支持联动的多列数据选择器，适用于多列联动数据选择场景，如省市区三级联动选择、年月日联动选择等。 |

### ArkUI\_CalendarAlignment

```c
enum ArkUI_CalendarAlignment
```

**描述**

日历选择器与入口组件对齐方式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_CALENDAR\_ALIGNMENT\_START = 0 | 设置选择器与入口组件的对齐方式为左对齐。 |
| ARKUI\_CALENDAR\_ALIGNMENT\_CENTER = 1 | 设置选择器与入口组件的对齐方式为居中对齐。 |
| ARKUI\_CALENDAR\_ALIGNMENT\_END = 2 | 设置选择器与入口组件的对齐方式为右对齐。 |

### ArkUI\_PickerIndicatorType

```c
enum ArkUI_PickerIndicatorType
```

**描述**

选择器的选中指示器类型。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| ARKUI\_PICKER\_INDICATOR\_BACKGROUND = 0 | 背景样式，适用于需要突出选中项的场景，如深色主题选择器、需要强调选中项的表单选择等。 |
| ARKUI\_PICKER\_INDICATOR\_DIVIDER = 1 | 分割线样式，适用于需要简洁风格的场景，如轻量级选择器、分割线风格UI设计等。 |

## 函数说明

### OH\_ArkUI\_TextPickerRangeContentArray\_Create()

```c
ArkUI_TextPickerRangeContentArray* OH_ArkUI_TextPickerRangeContentArray_Create(int32_t length)
```

**描述**

创建[ArkUI\_TextPickerRangeContentArray](capi-arkui-nativemodule-arkui-textpickerrangecontentarray.md)数组的对象，用于构建单列滑动数据选择器的数据列表，常见于日期选择、时间选择、列表选择等场景。创建后必须在使用完毕后调用OH\_ArkUI\_TextPickerRangeContentArray\_Destroy释放资源，否则会导致内存泄漏。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t length | 指定ArkUI\_TextPickerRangeContentArray数组的长度。取值必须大于0；传入非正整数或创建失败时返回空指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_TextPickerRangeContentArray](capi-arkui-nativemodule-arkui-textpickerrangecontentarray.md)\* | 返回指向ArkUI\_TextPickerRangeContentArray数组对象的指针（数组长度由length参数指定）。如果返回空指针，表示创建失败。 |

### OH\_ArkUI\_TextPickerRangeContentArray\_SetIconAtIndex()

```c
void OH_ArkUI_TextPickerRangeContentArray_SetIconAtIndex(ArkUI_TextPickerRangeContentArray* handle, char* icon, int32_t index)
```

**描述**

设置ArkUI\_TextPickerRangeContentArray数组指定位置的icon数据，用于在单列文本选择器中设置带图标的选项，常见于图文混排列表、带图标提示的选项列表等场景。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextPickerRangeContentArray](capi-arkui-nativemodule-arkui-textpickerrangecontentarray.md)\* handle | 指向ArkUI\_TextPickerRangeContentArray数组的指针，需先通过OH\_ArkUI\_TextPickerRangeContentArray\_Create创建。 |
| char\* icon | 图标路径，支持相对路径或绝对路径。相对路径相对于应用资源目录。路径必须指向有效的图标资源文件。 |
| int32\_t index | 数组索引，取值范围为[0, 数组长度-1]，从0开始。超出范围时不生效。 |

### OH\_ArkUI\_TextPickerRangeContentArray\_SetTextAtIndex()

```c
void OH_ArkUI_TextPickerRangeContentArray_SetTextAtIndex(ArkUI_TextPickerRangeContentArray* handle, char* text, int32_t index)
```

**描述**

设置ArkUI\_TextPickerRangeContentArray数组指定位置的text数据，用于在数据选择器中设置文本内容，是构建选择器选项的必备步骤。常见于日期选择器设置日期文本、城市选择器设置城市名称、产品分类选择器设置分类名称等场景。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextPickerRangeContentArray](capi-arkui-nativemodule-arkui-textpickerrangecontentarray.md)\* handle | 指向ArkUI\_TextPickerRangeContentArray数组的指针，需先通过OH\_ArkUI\_TextPickerRangeContentArray\_Create创建。 |
| char\* text | 文本内容。 |
| int32\_t index | 数组索引，取值范围为[0, 数组长度-1]，从0开始。超出范围时不生效。 |

### OH\_ArkUI\_TextPickerRangeContentArray\_Destroy()

```c
void OH_ArkUI_TextPickerRangeContentArray_Destroy(ArkUI_TextPickerRangeContentArray* handle)
```

**描述**

销毁ArkUI\_TextPickerRangeContentArray数组对象。此方法必须与OH\_ArkUI\_TextPickerRangeContentArray\_Create配对使用，用于释放创建的数组对象资源。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextPickerRangeContentArray](capi-arkui-nativemodule-arkui-textpickerrangecontentarray.md)\* handle | 指向ArkUI\_TextPickerRangeContentArray数组的指针。 |

### OH\_ArkUI\_TextCascadePickerRangeContentArray\_Create()

```c
ArkUI_TextCascadePickerRangeContentArray* OH_ArkUI_TextCascadePickerRangeContentArray_Create(int32_t length)
```

**描述**

创建[ArkUI\_TextCascadePickerRangeContentArray](capi-arkui-nativemodule-arkui-textcascadepickerrangecontentarray.md)数组对象，用于构建多列联动数据选择器，常见于年月日联动选择、省市区三级联动选择等场景。创建后必须在使用完毕后调用OH\_ArkUI\_TextCascadePickerRangeContentArray\_Destroy释放资源，否则会导致内存泄漏。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t length | 指定ArkUI\_TextCascadePickerRangeContentArray数组的长度。取值必须大于0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_TextCascadePickerRangeContentArray](capi-arkui-nativemodule-arkui-textcascadepickerrangecontentarray.md)\* | 返回指向ArkUI\_TextCascadePickerRangeContentArray数组对象的指针（数组长度由length参数指定）。如果返回空指针，表示创建失败。 |

### OH\_ArkUI\_TextCascadePickerRangeContentArray\_SetTextAtIndex()

```c
void OH_ArkUI_TextCascadePickerRangeContentArray_SetTextAtIndex(ArkUI_TextCascadePickerRangeContentArray* handle, char* text, int32_t index)
```

**描述**

设置ArkUI\_TextCascadePickerRangeContentArray数组指定位置的text数据，用于设置多列联动选择器的文本内容。常见于省市区三级联动选择器设置省份名称、年月日联动选择器设置年份、品牌车型联动选择器设置品牌名称等场景。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextCascadePickerRangeContentArray](capi-arkui-nativemodule-arkui-textcascadepickerrangecontentarray.md)\* handle | 指向ArkUI\_TextCascadePickerRangeContentArray数组的指针，需先通过OH\_ArkUI\_TextCascadePickerRangeContentArray\_Create创建。 |
| char\* text | 文本内容。 |
| int32\_t index | 数组索引，取值范围为[0, 数组长度-1]，从0开始。超出范围时不生效。 |

### OH\_ArkUI\_TextCascadePickerRangeContentArray\_SetChildAtIndex()

```c
void OH_ArkUI_TextCascadePickerRangeContentArray_SetChildAtIndex(ArkUI_TextCascadePickerRangeContentArray* handle, ArkUI_TextCascadePickerRangeContentArray* child, int32_t index)
```

**描述**

设置ArkUI\_TextCascadePickerRangeContentArray数组指定位置的child数据，用于设置多列联动选择器的子级数据，实现联动效果。常见于省市区三级联动选择器设置省份对应的市级数据、年月日联动选择器设置月份对应的日期数据、品牌车型联动选择器设置品牌对应的车型列表等场景。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextCascadePickerRangeContentArray](capi-arkui-nativemodule-arkui-textcascadepickerrangecontentarray.md)\* handle | 指向ArkUI\_TextCascadePickerRangeContentArray数组的指针，需先通过OH\_ArkUI\_TextCascadePickerRangeContentArray\_Create创建。 |
| [ArkUI\_TextCascadePickerRangeContentArray](capi-arkui-nativemodule-arkui-textcascadepickerrangecontentarray.md)\* child | 指向级联选择器指定位置子级数据列表的指针，需先通过OH\_ArkUI\_TextCascadePickerRangeContentArray\_Create创建。 |
| int32\_t index | 数组索引，取值范围为[0, 数组长度-1]，从0开始。超出范围时不生效。 |

### OH\_ArkUI\_TextCascadePickerRangeContentArray\_Destroy()

```c
void OH_ArkUI_TextCascadePickerRangeContentArray_Destroy(ArkUI_TextCascadePickerRangeContentArray* handle)
```

**描述**

销毁ArkUI\_TextCascadePickerRangeContentArray数组对象。此方法必须与OH\_ArkUI\_TextCascadePickerRangeContentArray\_Create配对使用，用于释放创建的数组对象资源。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_TextCascadePickerRangeContentArray](capi-arkui-nativemodule-arkui-textcascadepickerrangecontentarray.md)\* handle | 指向ArkUI\_TextCascadePickerRangeContentArray数组的指针。 |

### OH\_ArkUI\_PickerIndicatorStyle\_Create()

```c
ArkUI_PickerIndicatorStyle* OH_ArkUI_PickerIndicatorStyle_Create(ArkUI_PickerIndicatorType type)
```

**描述**

创建选中项指示器的样式实例，用于高亮显示用户当前选中的选项，提升用户交互体验。创建后必须在使用完毕后调用OH\_ArkUI\_PickerIndicatorStyle\_Dispose释放资源，否则会导致内存泄漏。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PickerIndicatorType](capi-picker-h.md#arkui_pickerindicatortype) type | 选择器选中项指示器类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [ArkUI\_PickerIndicatorStyle](capi-arkui-nativemodule-arkui-pickerindicatorstyle.md)\* | ArkUI\_PickerIndicatorStyle实例的指针。如果返回空指针，表示创建失败，失败原因可能是地址空间已满或类型不支持。 |

### OH\_ArkUI\_PickerIndicatorStyle\_Dispose()

```c
void OH_ArkUI_PickerIndicatorStyle_Dispose(ArkUI_PickerIndicatorStyle* style)
```

**描述**

销毁选中项指示器的样式实例。此方法必须与OH\_ArkUI\_PickerIndicatorStyle\_Create配对使用，用于释放创建的样式实例资源。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [ArkUI\_PickerIndicatorStyle](capi-arkui-nativemodule-arkui-pickerindicatorstyle.md)\* style | 要销毁的[ArkUI\_PickerIndicatorStyle](capi-arkui-nativemodule-arkui-pickerindicatorstyle.md)实例。 |
