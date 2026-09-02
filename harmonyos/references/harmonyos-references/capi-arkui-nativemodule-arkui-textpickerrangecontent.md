---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-textpickerrangecontent
title: ARKUI_TextPickerRangeContent
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ARKUI_TextPickerRangeContent
category: harmonyos-references
scraped_at: 2026-09-02T15:01:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:cbfa4abbd03f023cbc4306f7094fdb7c90ece32fd98ad1df36cf0331602e91d6
---

```c
typedef struct {...} ARKUI_TextPickerRangeContent
```

## 概述

定义单列滑动数据选择器支持的图片资源结构体。该结构体用于在TextPicker组件中同时显示图片和文本内容，适用于需要在单列滑动选择器中展示图标和文本组合的场景。支持自定义图标路径和文本内容，每项可设置独立的图标和文本或仅设置其中之一，帮助开发者实现灵活的图文选择器配置。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [picker.h](capi-picker-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| const char\* icon | 图标路径。以\0结尾的C字符串。可为NULL。未通过API设置时，字段保持默认值nullptr；通过[OH\_ArkUI\_TextPickerRangeContentArray\_SetIconAtIndex](capi-picker-h.md#oh_arkui_textpickerrangecontentarray_seticonatindex)设置为nullptr时不生效（API会忽略此设置）。空字符串""合法，表示不显示图标。具体路径用于显示自定义图标（当需要图标提示时选择），空字符串用于明确不显示图标（当仅显示文本时选择），NULL为默认值（应通过Set方法设置为具体值或空字符串，不建议保留NULL）。路径格式为应用内资源路径，例如"/common/hello.png"，与ArkTS [TextPickerRangeContent](ts-basic-components-textpicker.md#textpickerrangecontent10对象说明)一致；亦支持URI。图片格式未做专门限制，通过ImageSourceInfo加载，与[Image](ts-basic-components-image.md)组件支持的格式一致（如png、jpg、webp等）。显示尺寸固定为24vp × 24vp，不可通过本结构体配置。源码中未规定文件大小上限。 |
| const char\* text | 文本内容。以\0结尾的C字符串。可为NULL，默认为nullptr；通过[OH\_ArkUI\_TextPickerRangeContentArray\_SetTextAtIndex](capi-picker-h.md#oh_arkui_textpickerrangecontentarray_settextatindex)传入nullptr时不生效。空字符串""合法，表示不显示文本。具体文本内容用于显示提示信息（当需要文本说明时选择），空字符串用于明确不显示文本（当仅显示图标时选择），NULL为默认值（应通过Set方法设置为具体值或空字符串，不建议保留NULL）。若未通过Set方法设置，则默认显示为空字符串，与ArkTS文档一致。 |

**说明** 

* 每一项至少提供icon、text其中之一，可为仅icon、仅text或两者同时设置。
* 当文本长度大于列宽时，text内容会被截断显示。
* 建议使用[OH\_ArkUI\_TextPickerRangeContentArray\_Create](capi-picker-h.md#oh_arkui_textpickerrangecontentarray_create)创建数组后，通过[OH\_ArkUI\_TextPickerRangeContentArray\_SetIconAtIndex](capi-picker-h.md#oh_arkui_textpickerrangecontentarray_seticonatindex)和[OH\_ArkUI\_TextPickerRangeContentArray\_SetTextAtIndex](capi-picker-h.md#oh_arkui_textpickerrangecontentarray_settextatindex)设置各位置数据，以确保数据结构正确性，不建议手动拼装原始结构体。如果手动拼装结构体或未使用Create方法初始化，可能导致数组对象未正确初始化、内存管理异常或类型不匹配等问题。
* 在[NODE\_TEXT\_PICKER\_OPTION\_RANGE](capi-native-node-h-nodeattributetype-informationselection.md#node_text_picker_option_range)中配合rangeType为ARKUI\_TEXTPICKER\_RANGETYPE\_RANGE\_CONTENT（取值为2）时使用本结构体。
