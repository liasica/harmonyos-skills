---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/-native-node-h-nodeattributetype-textinputcategory
title: ArkUI_NodeAttributeType（文本输入类组件相关属性）
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > native_node.h > ArkUI_NodeAttributeType（文本输入类组件相关属性）
category: harmonyos-references
scraped_at: 2026-04-29T13:54:16+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:5011089d3e60e0290404aa8686436653cd90de637cdeee3cac25de46f1cdcf7a
---

```
1. enum ArkUI_NodeAttributeType
```

## 概述

定义ArkUI在Native侧可以设置的文本输入类组件相关属性样式集合，包含TextInput、TextArea组件属性设置。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_node.h](capi-native-node-h.md)

## NODE\_TEXT\_INPUT\_PLACEHOLDER

```
1. NODE_TEXT_INPUT_PLACEHOLDER = MAX_NODE_SCOPE_NUM * ARKUI_NODE_TEXT_INPUT = 7000
```

单行文本输入框的默认提示文本内容属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 默认提示文本的内容。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 默认提示文本的内容。 |

## NODE\_TEXT\_INPUT\_TEXT

```
1. NODE_TEXT_INPUT_TEXT = 7001
```

单行文本输入框的默认文本内容属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 默认文本的内容。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 默认文本的内容。 |

## NODE\_TEXT\_INPUT\_CARET\_COLOR

```
1. NODE_TEXT_INPUT_CARET_COLOR = 7002
```

光标颜色属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 光标颜色数值，0xargb格式，形如 0xFFFF0000 表示红色。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 光标颜色数值，0xargb格式。 |

## NODE\_TEXT\_INPUT\_CARET\_STYLE

```
1. NODE_TEXT_INPUT_CARET_STYLE = 7003
```

光标风格属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 光标宽度数值，单位为vp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 光标宽度数值，单位为vp。 |

## NODE\_TEXT\_INPUT\_SHOW\_UNDERLINE

```
1. NODE_TEXT_INPUT_SHOW_UNDERLINE = 7004
```

单行文本输入框下划线属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | false表示不展示下划线，true表示展示下划线。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 0表示不展示下划线，1表示展示下划线。 |

## NODE\_TEXT\_INPUT\_MAX\_LENGTH

```
1. NODE_TEXT_INPUT_MAX_LENGTH = 7005
```

输入框支持的最大文本数属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 最大文本数的数字，无单位。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 最大文本数的数字。 |

## NODE\_TEXT\_INPUT\_ENTER\_KEY\_TYPE

```
1. NODE_TEXT_INPUT_ENTER_KEY_TYPE = 7006
```

回车键类型属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 回车键类型枚举[ArkUI\_EnterKeyType](capi-native-type-h.md#arkui_enterkeytype)，默认值为ARKUI\_ENTER\_KEY\_TYPE\_DONE。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 回车键类型枚举[ArkUI\_EnterKeyType](capi-native-type-h.md#arkui_enterkeytype)。 |

## NODE\_TEXT\_INPUT\_PLACEHOLDER\_COLOR

```
1. NODE_TEXT_INPUT_PLACEHOLDER_COLOR = 7007
```

无输入时默认提示文本的颜色属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 颜色数值，0xargb格式，形如 0xFFFF0000 表示红色。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 颜色数值，0xargb格式。 |

## NODE\_TEXT\_INPUT\_PLACEHOLDER\_FONT

```
1. NODE_TEXT_INPUT_PLACEHOLDER_FONT = 7008
```

无输入时默认提示文本的字体配置（包括大小、字重、样式、字体列表）属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0]?.f32 | 可选字体大小数值，默认值16.0，单位为fp。 |
| .value[1]?.i32 | 可选字体样式[ArkUI\_FontStyle](capi-native-type-h.md#arkui_fontstyle)，默认值为ARKUI\_FONT\_STYLE\_NORMAL。 |
| .value[2]?.i32 | 可选字体粗细样式[ArkUI\_FontWeight](capi-native-type-h.md#arkui_fontweight)，默认值为ARKUI\_FONT\_WEIGHT\_NORMAL。 |
| ?.string | 字体族内容，多个字体族之间使用逗号分隔，形如“字重；字体族1，字体族2”。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 字体大小数值，单位为fp。 |
| .value[1].i32 | 字体样式[ArkUI\_FontStyle](capi-native-type-h.md#arkui_fontstyle)。 |
| .value[2].i32 | 字体粗细样式[ArkUI\_FontWeight](capi-native-type-h.md#arkui_fontweight)。 |
| .string | 字体族内容，多个字体族之间使用逗号分隔。 |

## NODE\_TEXT\_INPUT\_ENABLE\_KEYBOARD\_ON\_FOCUS

```
1. NODE_TEXT_INPUT_ENABLE_KEYBOARD_ON_FOCUS = 7009
```

聚焦时是否绑定输入法属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | false表示聚焦不拉起输入法，true表示拉起。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 0表示聚焦不拉起输入法，1表示拉起。 |

## NODE\_TEXT\_INPUT\_TYPE

```
1. NODE_TEXT_INPUT_TYPE = 7010
```

输入框的类型属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 输入框类型枚举[ArkUI\_TextInputType](capi-native-type-h.md#arkui_textinputtype)，默认值为ARKUI\_TEXTINPUT\_TYPE\_NORMAL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 输入框类型枚举[ArkUI\_TextInputType](capi-native-type-h.md#arkui_textinputtype)。 |

## NODE\_TEXT\_INPUT\_SELECTED\_BACKGROUND\_COLOR

```
1. NODE_TEXT_INPUT_SELECTED_BACKGROUND_COLOR = 7011
```

输入框文本选中时的背景色属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 颜色数值，0xargb格式，形如 0xFFFF0000 表示红色。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 颜色数值，0xargb格式。 |

## NODE\_TEXT\_INPUT\_SHOW\_PASSWORD\_ICON

```
1. NODE_TEXT_INPUT_SHOW_PASSWORD_ICON = 7012
```

密码输入模式时是否显示末尾图标属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | false表示不显示图标，true表示显示图标，默认值为false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 0表示不显示图标，1表示显示图标。 |

## NODE\_TEXT\_INPUT\_EDITING

```
1. NODE_TEXT_INPUT_EDITING = 7013
```

控制单行文本输入框编辑态属性，支持属性设置。

作为属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | false表示退出编辑态，true表示维持现状。  属性获取方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式： |
| .value[0].i32 | false表示退出编辑态，true表示维持现状。 |

## NODE\_TEXT\_INPUT\_CANCEL\_BUTTON

```
1. NODE_TEXT_INPUT_CANCEL_BUTTON = 7014
```

单行文本右侧清除按钮样式属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 按钮样式[ArkUI\_CancelButtonStyle](capi-native-type-h.md#arkui_cancelbuttonstyle)，默认值为ARKUI\_CANCELBUTTON\_STYLE\_INPUT。 |
| .value[1]?.f32 | 图标大小数值，单位为vp。 |
| .value[2]?.u32 | 按钮图标颜色数值，0xargb格式，形如 0xFFFF0000 表示红色。 |
| ?.string | 按钮图标地址，入参内容为图片本地地址，例如 /pages/icon.png。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 按钮样式[ArkUI\_CancelButtonStyle](capi-native-type-h.md#arkui_cancelbuttonstyle)。 |
| .value[1].f32 | 图标大小数值，单位为vp。 |
| .value[2].u32 | 按钮图标颜色数值，0xargb格式。 |
| .string | 按钮图标地址。 |

## NODE\_TEXT\_INPUT\_TEXT\_SELECTION

```
1. NODE_TEXT_INPUT_TEXT_SELECTION = 7015
```

单行文本设置文本选中并高亮的区域，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 选中文本的起始位置。 |
| .value[1].i32 | 选中文本的终止位置。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 选中文本的起始位置。 |
| .value[1].i32 | 选中文本的终止位置。 |

## NODE\_TEXT\_INPUT\_UNDERLINE\_COLOR

```
1. NODE_TEXT_INPUT_UNDERLINE_COLOR = 7016
```

开启下划线时，支持配置下划线颜色。主题配置的默认下划线颜色为'0x33182431'。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | typing，必填，键入时下划线颜色，0xargb类型。 |
| .value[1].u32 | normal，必填，非特殊状态时下划线颜色，0xargb类型。 |
| .value[2].u32 | error，必填，错误时下划线颜色，0xargb类型。 |
| .value[3].u32 | disable，必填，禁用时下划线颜色，0xargb类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | typing，键入时下划线颜色，0xargb类型。 |
| .value[1].u32 | normal，非特殊状态时下划线颜色，0xargb类型。 |
| .value[2].u32 | error，错误时下划线颜色，0xargb类型。 |
| .value[3].u32 | disable，禁用时下划线颜色，0xargb类型。 |

## NODE\_TEXT\_INPUT\_ENABLE\_AUTO\_FILL

```
1. NODE_TEXT_INPUT_ENABLE_AUTO_FILL = 7017
```

设置是否启用自动填充。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否启用自动填充，默认值true。  true表示启用，false表示不启用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否启用自动填充。 |

## NODE\_TEXT\_INPUT\_CONTENT\_TYPE

```
1. NODE_TEXT_INPUT_CONTENT_TYPE = 7018
```

自动填充类型。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 参数类型[ArkUI\_TextInputContentType](capi-native-type-h.md#arkui_textinputcontenttype)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 参数类型[ArkUI\_TextInputContentType](capi-native-type-h.md#arkui_textinputcontenttype)。 |

## NODE\_TEXT\_INPUT\_PASSWORD\_RULES

```
1. NODE_TEXT_INPUT_PASSWORD_RULES = 7019
```

定义生成密码的规则。在触发自动填充时，所设置的密码规则会透传给密码保险箱，用于新密码的生成。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 定义生成密码的规则。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 定义生成密码的规则。 |

## NODE\_TEXT\_INPUT\_SELECT\_ALL

```
1. NODE_TEXT_INPUT_SELECT_ALL = 7020
```

设置当初始状态，是否全选文本。不支持内联模式。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否全选文本，默认值：false。  true表示会全选文本，false表示不会全选文本。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否全选文本。 |

## NODE\_TEXT\_INPUT\_INPUT\_FILTER

```
1. NODE_TEXT_INPUT_INPUT_FILTER = 7021
```

通过正则表达式设置输入过滤器。匹配表达式的输入允许显示，不匹配的输入将被过滤。单字符输入场景仅支持单字符匹配，多字符输入场景支持字符串匹配，例如粘贴。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 正则表达式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 正则表达式。 |

## NODE\_TEXT\_INPUT\_STYLE

```
1. NODE_TEXT_INPUT_STYLE = 7022
```

设置输入框为默认风格或内联输入风格。内联输入风格只支持输入框类型的枚举[ArkUI\_TextInputType](capi-native-type-h.md#arkui_textinputtype)设置为ARKUI\_TEXTINPUT\_TYPE\_NORMAL。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 参数类型[ArkUI\_TextInputStyle](capi-native-type-h.md#arkui_textinputstyle)。默认值为ARKUI\_TEXTINPUT\_STYLE\_DEFAULT。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 参数类型[ArkUI\_TextInputStyle](capi-native-type-h.md#arkui_textinputstyle)。 |

## NODE\_TEXT\_INPUT\_CARET\_OFFSET

```
1. NODE_TEXT_INPUT_CARET_OFFSET = 7023
```

设置或获取光标所在位置信息。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

设置输入光标的位置。

返回当前光标所在位置信息。在当前帧更新光标位置同时调用该接口，该接口不生效。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 从字符串开始到光标所在位置的字符长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 光标所在位置的索引值。 |
| .value[1].f32 | 光标相对输入框的x坐标位值。 |
| .value[2].f32 | 光标相对输入框的y坐标位值。 |

## NODE\_TEXT\_INPUT\_CONTENT\_RECT

```
1. NODE_TEXT_INPUT_CONTENT_RECT = 7024
```

获取已编辑文本内容区域相对组件的位置和大小。

作为属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 水平方向横坐标。 |
| .value[1].f32 | 竖直方向纵坐标。 |
| .value[2].f32 | 内容宽度大小。 |
| .value[3].f32 | 内容高度大小。 |

## NODE\_TEXT\_INPUT\_CONTENT\_LINE\_COUNT

```
1. NODE_TEXT_INPUT_CONTENT_LINE_COUNT = 7025
```

获取已编辑文本内容的行数。

作为属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 已编辑文本内容行数。 |

## NODE\_TEXT\_INPUT\_SELECTION\_MENU\_HIDDEN

```
1. NODE_TEXT_INPUT_SELECTION_MENU_HIDDEN = 7026
```

设置长按、双击输入框或者右键输入框时，是否不弹出文本选择菜单，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 长按、双击输入框或者右键输入框时，是否不弹出文本选择菜单。默认值false。  设置为true时，单击输入框光标、长按输入框、双击输入框、三击输入框或者右键输入框，隐藏系统文本选择菜单。  设置为false时，显示系统文本选择菜单。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 长按、双击输入框或者右键输入框时，是否不弹出文本选择菜单。 |

## NODE\_TEXT\_INPUT\_BLUR\_ON\_SUBMIT

```
1. NODE_TEXT_INPUT_BLUR_ON_SUBMIT = 7027
```

设置输入框在submit状态下，触发回车键是否失焦。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否失焦。默认值true。  false表示触发回车键后不失焦，true表示触发回车键后失焦。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否失焦。 |

## NODE\_TEXT\_INPUT\_CUSTOM\_KEYBOARD

```
1. NODE_TEXT_INPUT_CUSTOM_KEYBOARD = 7028
```

设置自定义键盘。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 自定义键盘，参数类型[ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)。 |
| .value[0]?.i32 | 设置自定义键盘是否支持避让功能，默认值false。  true表示支持避让，false表示不支持避让。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .object | 自定义键盘，参数类型[ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)。 |
| .value[0].i32 | 设置自定义键盘是否支持避让功能。 |

## NODE\_TEXT\_INPUT\_WORD\_BREAK

```
1. NODE_TEXT_INPUT_WORD_BREAK = 7029
```

文本断行规则属性，仅在内联输入风格编辑态生效，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 参数类型[ArkUI\_WordBreak](capi-native-type-h.md#arkui_wordbreak)。默认值ARKUI\_WORD\_BREAK\_BREAK\_WORD。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 参数类型[ArkUI\_WordBreak](capi-native-type-h.md#arkui_wordbreak)。 |

## NODE\_TEXT\_INPUT\_SHOW\_KEYBOARD\_ON\_FOCUS

```
1. NODE_TEXT_INPUT_SHOW_KEYBOARD_ON_FOCUS = 7030
```

设置输入框获取焦点时是否弹出键盘，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否弹出键盘。false表示获取焦点时不弹出键盘，true表示获取焦点时弹出键盘。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否弹出键盘。 |

## NODE\_TEXT\_INPUT\_NUMBER\_OF\_LINES

```
1. NODE_TEXT_INPUT_NUMBER_OF_LINES = 7031
```

设置该属性后，通过该属性计算[TextInput](ts-basic-components-textinput.md)组件的高度。 例如：设置numberOfLines为3时，组件将默认显示足够容纳3行文本内容的高度。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 设置numberOfLines的值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 设置numberOfLines的值。 |

## NODE\_TEXT\_INPUT\_LETTER\_SPACING

```
1. NODE_TEXT_INPUT_LETTER_SPACING = 7032
```

设置该属性后，通过该属性调整[TextInput](ts-basic-components-textinput.md)组件的字符间距。接口支持设置，重置以及获取该属性。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 设置[letterSpacing](ts-basic-components-text.md#letterspacing)的值，默认单位fp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 获取letterSpacing的值，默认单位fp。 |

## NODE\_TEXT\_INPUT\_ENABLE\_PREVIEW\_TEXT

```
1. NODE_TEXT_INPUT_ENABLE_PREVIEW_TEXT = 7033
```

设置[TextInput](ts-basic-components-textinput.md)组件是否开启输入预上屏。接口支持设置，重置以及获取该属性。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 设置是否开启输入预上屏。默认值true。  false表示不开启输入预上屏，true表示开启输入预上屏。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 获取是否开启输入预上屏。 |

## NODE\_TEXT\_INPUT\_HALF\_LEADING

```
1. NODE_TEXT_INPUT_HALF_LEADING = 7034
```

设置文本将行间距平分至行的顶部与底部。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 设置文本是否将行间距平分至行的顶部与底部。默认值false。  true表示将行间距平分至行的顶部与底部，false表示不平分。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 设置文本是否将行间距平分至行的顶部与底部。 |

## NODE\_TEXT\_INPUT\_KEYBOARD\_APPEARANCE

```
1. NODE_TEXT_INPUT_KEYBOARD_APPEARANCE = 7035
```

设置输入框拉起的键盘样式。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 键盘样式，参数类型[ArkUI\_KeyboardAppearance](capi-native-type-h.md#arkui_keyboardappearance)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 键盘样式，参数类型[ArkUI\_KeyboardAppearance](capi-native-type-h.md#arkui_keyboardappearance)。默认值ARKUI\_KEYBOARD\_APPEARANCE\_NONE\_IMMERSIVE。 |

## NODE\_TEXT\_INPUT\_ENABLE\_FILL\_ANIMATION

```
1. NODE_TEXT_INPUT_ENABLE_FILL_ANIMATION = 7036
```

设置是否启用自动填充动效。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否启用自动填充动效。  true表示启用，false表示不启用。  默认值true。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否启用自动填充动效。启用之后，仅输入框类型的枚举[ArkUI\_TextInputType](capi-native-type-h.md#arkui_textinputtype)设置为ARKUI\_TEXTINPUT\_TYPE\_PASSWORD、ARKUI\_TEXTINPUT\_TYPE\_NUMBER\_PASSWORD或ARKUI\_TEXTINPUT\_TYPE\_NEW\_PASSWORD的输入框在进行自动填充时动效可生效。 |

## NODE\_TEXT\_INPUT\_LINE\_HEIGHT

```
1. NODE_TEXT_INPUT_LINE_HEIGHT = 7037
```

设置输入框文本的高度，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 文本的高度的数字。默认值是自适应字体大小。设置为undefined时，文本的高度设置为5。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 文本的高度的数字。 |

## NODE\_TEXT\_INPUT\_ENABLE\_SELECTED\_DATA\_DETECTOR

```
1. NODE_TEXT_INPUT_ENABLE_SELECTED_DATA_DETECTOR = 7038
```

开启选中词文本识别。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 开启选中词文本识别，true表示开启识别，false表示关闭识别。默认值：true。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否开启选中词文本识别。 |

## NODE\_TEXT\_INPUT\_SHOW\_COUNTER

```
1. NODE_TEXT_INPUT_SHOW_COUNTER = 7040
```

设置输入的字符数超过阈值时是否显示计数器并设置计数器样式，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否开启计数器。值为true表示开启计数器，值为false表示不开启计数器。 |
| .value[1]?.f32 | 可输入字符数占最大字符限制的百分比值，超过此值时显示计数器，取值范围[1, 100]，小数时向下取整，若超出取值范围，则接口属性设置不生效。 |
| .value[2]?.i32 | 输入字符超出限制时高亮边框，true表示高亮边框，false表示为不高亮边框。 |
| .object | 计数器配置，配置属性为文本输入框未达到最大字符数时计数器的颜色以及超出最大字符数时计数器的颜色。参数类型为 [ArkUI\_ShowCounterConfig](api-arkui-nativemodule-arkui-textshowcounterconfig.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否开启计数器。 |
| .value[1].f32 | 可输入字符数占最大字符限制的百分比值，超过此值时显示计数器，取值范围[1, 100]。 |
| .value[2].i32 | 输入字符超出限制时高亮边框，true表示高亮边框，false表示为不高亮边框，默认高亮。 |
| .object | 计数器配置，配置属性为文本输入框未达到最大字符数时计数器的颜色以及超出最大字符数时计数器的颜色。参数类型为[ArkUI\_ShowCounterConfig](api-arkui-nativemodule-arkui-textshowcounterconfig.md)。 |

## NODE\_TEXT\_INPUT\_TEXT\_CONTENT\_CONTROLLER\_BASE

```
1. NODE_TEXT_INPUT_TEXT_CONTENT_CONTROLLER_BASE = 7041
```

用于设置或获取文本输入控制器。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 文本内容基础控制器。参数类型为[ArkUI\_TextContentBaseController](arkui-nativemodule-arkui-textcontentbasecontroller.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .object | 文本内容基础控制器。参数类型为[ArkUI\_TextContentBaseController](arkui-nativemodule-arkui-textcontentbasecontroller.md)。 |

## NODE\_TEXT\_INPUT\_COMPRESS\_LEADING\_PUNCTUATION

```
1. NODE_TEXT_INPUT_COMPRESS_LEADING_PUNCTUATION = 7044
```

设置输入字符行首标点压缩开关，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否打开行首标点压缩开关。  true表示开启行首标点压缩，false表示关闭行首标点压缩。默认值false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否打开行首标点压缩开关。 |

## NODE\_TEXT\_INPUT\_INCLUDE\_FONT\_PADDING

```
1. NODE_TEXT_INPUT_INCLUDE_FONT_PADDING = 7045
```

设置单行输入框内文字是否在首行顶部和尾行底部增加间距以避免文字截断。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 设置输入框内文字是否在首行顶部和尾行底部增加间距以避免文字截断。true表示开启增加间距，false表示关闭增加间距。默认值：false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否在首行顶部和尾行底部增加间距。true表示增加间距，false表示不增加间距。 |

## NODE\_TEXT\_INPUT\_FALLBACK\_LINE\_SPACING

```
1. NODE_TEXT_INPUT_FALLBACK_LINE_SPACING = 7046
```

针对多行文字叠加，支持行高基于文字实际高度自适应。此接口仅当行高小于文字实际高度时生效。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 支持行高基于文字实际高度自适应。true表示开启自适应，false表示关闭自适应。默认值：false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否开启行高基于文字实际高度自适应。true表示开启自适应，false表示关闭自适应。 |

## NODE\_TEXT\_INPUT\_DIRECTION

```
1. NODE_TEXT_INPUT_DIRECTION = 7047
```

单行输入框的文本排版方向。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 表示文本的排版方向，取[ArkUI\_TextDirection](capi-native-type-h.md#arkui_textdirection)枚举值。默认值为ARKUI\_TEXT\_DIRECTION\_DEFAULT。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 表示文本的排版方向，对应取值及含义请参考[ArkUI\_TextDirection](capi-native-type-h.md#arkui_textdirection)枚举值。 |

## NODE\_TEXT\_INPUT\_SELECTED\_DRAG\_PREVIEW\_STYLE

```
1. NODE_TEXT_INPUT_SELECTED_DRAG_PREVIEW_STYLE = 7048
```

用于设置文本输入框内文本选中状态下的拖拽预览样式。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 文本选中状态下的拖拽预览样式。参数类型为[ArkUI\_SelectedDragPreviewStyle](ui-nativemodule-arkui-textselecteddragpreviewstyle.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .object | 文本选中状态下的拖拽预览样式。参数类型为[ArkUI\_SelectedDragPreviewStyle](ui-nativemodule-arkui-textselecteddragpreviewstyle.md)。 |

## NODE\_TEXT\_AREA\_PLACEHOLDER

```
1. NODE_TEXT_AREA_PLACEHOLDER = MAX_NODE_SCOPE_NUM * ARKUI_NODE_TEXT_AREA = 8000
```

多行文本输入框的默认提示文本内容属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 默认提示文本的内容。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 默认提示文本的内容。 |

## NODE\_TEXT\_AREA\_TEXT

```
1. NODE_TEXT_AREA_TEXT = 8001
```

多行文本输入框的默认文本内容属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 默认文本的内容。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 默认文本的内容。 |

## NODE\_TEXT\_AREA\_MAX\_LENGTH

```
1. NODE_TEXT_AREA_MAX_LENGTH = 8002
```

输入框支持的最大文本数属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 最大文本数的数字。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 最大文本数的数字。 |

## NODE\_TEXT\_AREA\_PLACEHOLDER\_COLOR

```
1. NODE_TEXT_AREA_PLACEHOLDER_COLOR = 8003
```

无输入时默认提示文本的颜色属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 颜色数值，0xargb格式，形如 0xFFFF0000 表示红色。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 颜色数值，0xargb格式。 |

## NODE\_TEXT\_AREA\_PLACEHOLDER\_FONT

```
1. NODE_TEXT_AREA_PLACEHOLDER_FONT = 8004
```

无输入时默认提示文本的字体配置（包括大小、字重、样式、字体列表）属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0]?.f32 | 可选字体大小数值，默认值16.0，单位为fp。 |
| .value[1]?.i32 | 可选字体样式[ArkUI\_FontStyle](capi-native-type-h.md#arkui_fontstyle)，默认值为ARKUI\_FONT\_STYLE\_NORMAL。 |
| .value[2]?.i32 | 可选字体粗细样式[ArkUI\_FontWeight](capi-native-type-h.md#arkui_fontweight)，默认值为ARKUI\_FONT\_WEIGHT\_NORMAL。 |
| ?.string | 字体族内容，多个字体族之间使用逗号分隔，形如“字重；字体族1，字体族2”。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 字体大小数值，单位为fp。 |
| .value[1].i32 | 字体样式[ArkUI\_FontStyle](capi-native-type-h.md#arkui_fontstyle)。 |
| .value[2].i32 | 字体粗细样式[ArkUI\_FontWeight](capi-native-type-h.md#arkui_fontweight)。 |
| .string | 字体族内容，多个字体族之间使用逗号分隔。 |

## NODE\_TEXT\_AREA\_CARET\_COLOR

```
1. NODE_TEXT_AREA_CARET_COLOR = 8005
```

光标颜色属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 背景色数值，0xargb格式，形如 0xFFFF0000 表示红色。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 背景色数值，0xargb格式。 |

## NODE\_TEXT\_AREA\_EDITING

```
1. NODE_TEXT_AREA_EDITING = 8006
```

控制多行文本输入框编辑态属性，支持属性设置，属性获取接口。

作为属性设置方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | false表示退出编辑态，true表示维持现状。  属性获取方法参数[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式： |
| .value[0].i32 | false表示退出编辑态，true表示维持现状。 |

## NODE\_TEXT\_AREA\_TYPE

```
1. NODE_TEXT_AREA_TYPE = 8007
```

输入框的类型属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 输入框类型枚举[ArkUI\_TextAreaType](capi-native-type-h.md#arkui_textareatype)，默认值为ARKUI\_TEXTAREA\_TYPE\_NORMAL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 输入框类型枚举[ArkUI\_TextAreaType](capi-native-type-h.md#arkui_textareatype)。 |

## NODE\_TEXT\_AREA\_SHOW\_COUNTER

```
1. NODE_TEXT_AREA_SHOW_COUNTER = 8008
```

设置输入的字符数超过阈值时是否显示计数器并设置计数器样式，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否开启计数器，值为true时为开启。默认值false。 |
| .value[1]?.f32 | 可输入字符数占最大字符限制的百分比值，超过此值时显示计数器，取值范围[1, 100]，小数时向下取整，若超出取值范围，则接口属性设置不生效。 |
| .value[2]?.i32 | 输入字符超出限制时是否高亮边框。true表示高亮边框，false表示不高亮边框。默认值true。 |
| .object | 计数器配置，配置属性为文本输入框未达到最大字符数时计数器的颜色以及超出最大字符数时计数器的颜色。参数类型为[ArkUI\_ShowCounterConfig](api-arkui-nativemodule-arkui-textshowcounterconfig.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否开启计数器，值为true时开启。 |
| .value[1].f32 | 可输入字符数占最大字符限制的百分比值，超过此值时显示计数器，取值范围[1, 100]。 |
| .value[2].i32 | 输入字符超出限制时是否高亮边框，值为true时高亮边框。 |
| .object | 计数器配置，配置属性为文本输入框未达到最大字符数时计数器的颜色以及超出最大字符数时计数器的颜色。参数类型为[ArkUI\_ShowCounterConfig](api-arkui-nativemodule-arkui-textshowcounterconfig.md)。 |

## NODE\_TEXT\_AREA\_SELECTION\_MENU\_HIDDEN

```
1. NODE_TEXT_AREA_SELECTION_MENU_HIDDEN = 8009
```

设置长按、双击输入框或者右键输入框时，是否不弹出文本选择菜单，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 长按、双击输入框或者右键输入框时，是否不弹出文本选择菜单。默认值false。  设置为true时，单击输入框光标、长按输入框、双击输入框、三击输入框或者右键输入框，隐藏系统文本选择菜单。  设置为false时，显示系统文本选择菜单。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 长按、双击输入框或者右键输入框时，是否不弹出文本选择菜单。 |

## NODE\_TEXT\_AREA\_BLUR\_ON\_SUBMIT

```
1. NODE_TEXT_AREA_BLUR_ON_SUBMIT = 8010
```

设置多行输入框在submit状态下，触发回车键是否失焦。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否失焦。false表示触发回车键后不失焦，true表示触发回车键后失焦。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否失焦。 |

## NODE\_TEXT\_AREA\_INPUT\_FILTER

```
1. NODE_TEXT_AREA_INPUT_FILTER = 8011
```

通过正则表达式设置输入过滤器。匹配表达式的输入允许显示，不匹配的输入将被过滤。单字符输入场景仅支持单字符匹配，多字符输入场景支持字符串匹配，例如粘贴。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 正则表达式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 正则表达式。 |

## NODE\_TEXT\_AREA\_SELECTED\_BACKGROUND\_COLOR

```
1. NODE_TEXT_AREA_SELECTED_BACKGROUND_COLOR = 8012
```

设置文本选中底板颜色，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 颜色数值，0xargb格式，形如 0xFFFF0000 表示红色。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 颜色数值，0xargb格式。 |

## NODE\_TEXT\_AREA\_ENTER\_KEY\_TYPE

```
1. NODE_TEXT_AREA_ENTER_KEY_TYPE = 8013
```

设置输入法回车键类型，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 回车键类型枚举[ArkUI\_EnterKeyType](capi-native-type-h.md#arkui_enterkeytype)，默认值为ARKUI\_ENTER\_KEY\_TYPE\_DONE。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 回车键类型枚举[ArkUI\_EnterKeyType](capi-native-type-h.md#arkui_enterkeytype)。 |

## NODE\_TEXT\_AREA\_ENABLE\_KEYBOARD\_ON\_FOCUS

```
1. NODE_TEXT_AREA_ENABLE_KEYBOARD_ON_FOCUS = 8014
```

设置TextArea通过点击以外的方式获焦时，是否绑定输入法，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | false表示聚焦不拉起输入法，true表示拉起，默认值为true。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 0表示聚焦不拉起输入法，1表示拉起。 |

## NODE\_TEXT\_AREA\_CARET\_OFFSET

```
1. NODE_TEXT_AREA_CARET_OFFSET = 8015
```

设置或获取光标所在位置信息。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

设置输入光标的位置。

返回当前光标所在位置信息。在当前帧更新光标位置同时调用该接口，该接口不生效。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 从字符串开始到光标所在位置的字符长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 光标所在位置的索引值。 |
| .value[1].f32 | 光标相对输入框的x坐标位值。 |
| .value[2].f32 | 光标相对输入框的y坐标位值。 |

## NODE\_TEXT\_AREA\_CONTENT\_RECT

```
1. NODE_TEXT_AREA_CONTENT_RECT = 8016
```

获取已编辑文本内容区域相对组件的位置和大小。

作为属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 水平方向横坐标。 |
| .value[1].f32 | 竖直方向纵坐标。 |
| .value[2].f32 | 内容宽度大小。 |
| .value[3].f32 | 内容高度大小。 |

## NODE\_TEXT\_AREA\_CONTENT\_LINE\_COUNT

```
1. NODE_TEXT_AREA_CONTENT_LINE_COUNT = 8017
```

获取已编辑文本内容的行数。

作为属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 已编辑文本内容行数。 |

## NODE\_TEXT\_AREA\_TEXT\_SELECTION

```
1. NODE_TEXT_AREA_TEXT_SELECTION = 8018
```

组件在获焦状态下，调用该接口设置文本选择区域并高亮显示，且只有在selectionStart小于selectionEnd时，文字才会被选取、高亮显示。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 选中文本的起始位置。 |
| .value[1].i32 | 选中文本的终止位置。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 选中文本的起始位置。 |
| .value[1].i32 | 选中文本的终止位置。 |

## NODE\_TEXT\_AREA\_ENABLE\_AUTO\_FILL

```
1. NODE_TEXT_AREA_ENABLE_AUTO_FILL = 8019
```

设置是否启用自动填充。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否启用自动填充，默认值true。  true表示启用，false表示不启用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否启用自动填充。 |

## NODE\_TEXT\_AREA\_CONTENT\_TYPE

```
1. NODE_TEXT_AREA_CONTENT_TYPE = 8020
```

自动填充类型。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 参数类型[ArkUI\_TextInputContentType](capi-native-type-h.md#arkui_textinputcontenttype)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 参数类型[ArkUI\_TextInputContentType](capi-native-type-h.md#arkui_textinputcontenttype)。 |

## NODE\_TEXT\_AREA\_SHOW\_KEYBOARD\_ON\_FOCUS

```
1. NODE_TEXT_AREA_SHOW_KEYBOARD_ON_FOCUS = 8021
```

设置输入框获取焦点时是否弹出键盘，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否弹出键盘。默认值true。  false表示获取焦点时不弹出键盘，true表示获取焦点时弹出键盘。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否弹出键盘。 |

## NODE\_TEXT\_AREA\_NUMBER\_OF\_LINES

```
1. NODE_TEXT_AREA_NUMBER_OF_LINES = 8022
```

设置该属性后，通过该属性计算TextArea组件的高度。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 设置numberOfLines的值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 设置numberOfLines的值。 |

## NODE\_TEXT\_AREA\_LETTER\_SPACING

```
1. NODE_TEXT_AREA_LETTER_SPACING = 8023
```

设置该属性后，通过该属性调整TextArea组件的字符间距。接口支持设置，重置以及获取该属性。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 设置[letterSpacing](ts-basic-components-text.md#letterspacing)的值，默认单位fp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 获取[letterSpacing](ts-basic-components-text.md#letterspacing)的值，默认单位fp。 |

## NODE\_TEXT\_AREA\_ENABLE\_PREVIEW\_TEXT

```
1. NODE_TEXT_AREA_ENABLE_PREVIEW_TEXT = 8024
```

设置TextArea组件是否开启输入预上屏。接口支持设置，重置以及获取该属性。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 设置是否开启输入预上屏。false表示不开启输入预上屏，true表示开启输入预上屏。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 获取是否开启输入预上屏。 |

## NODE\_TEXT\_AREA\_HALF\_LEADING

```
1. NODE_TEXT_AREA_HALF_LEADING = 8025
```

设置文本将行间距平分至行的顶部与底部。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 设置文本是否将行间距平分至行的顶部与底部。默认值false。  true表示将行间距平分至行的顶部与底部，false表示不平分。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 设置文本是否将行间距平分至行的顶部与底部。 |

## NODE\_TEXT\_AREA\_KEYBOARD\_APPEARANCE

```
1. NODE_TEXT_AREA_KEYBOARD_APPEARANCE = 8026
```

设置输入框拉起的键盘样式。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 键盘样式，参数类型[ArkUI\_KeyboardAppearance](capi-native-type-h.md#arkui_keyboardappearance)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 键盘样式，参数类型[ArkUI\_KeyboardAppearance](capi-native-type-h.md#arkui_keyboardappearance)。 |

## NODE\_TEXT\_AREA\_MAX\_LINES

```
1. NODE_TEXT_AREA_MAX_LINES = 8027
```

设置输入框内联模式编辑态时文本可显示的最大行数，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 内联输入风格编辑态时文本可显示的最大行数。内联模式下，默认值是3，  非内联模式下，默认值是+∞，不限制最大行数。设置为undefined时，最大行数设置为5。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 最大行数的数字。 |

## NODE\_TEXT\_AREA\_LINE\_SPACING

```
1. NODE_TEXT_AREA_LINE_SPACING = 8028
```

设置输入框文本的行间距，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 文本的行间距的数字。默认值是0，单位fp。设置为undefined时，行间距设置为5。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 文本的行间距的数字，单位fp。 |

## NODE\_TEXT\_AREA\_MIN\_LINES

```
1. NODE_TEXT_AREA_MIN_LINES = 8029
```

设置节点的最小行数。支持属性设置、属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 最小行数的数字。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 最小行数的数字。 |

## NODE\_TEXT\_AREA\_MAX\_LINES\_WITH\_SCROLL

```
1. NODE_TEXT_AREA_MAX_LINES_WITH_SCROLL = 8030
```

设置支持滚动时节点的最大行数。支持属性设置、属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 支持滚动时的最大行数的数字。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 支持滚动时的最大行数的数字。 |

## NODE\_TEXT\_AREA\_LINE\_HEIGHT

```
1. NODE_TEXT_AREA_LINE_HEIGHT = 8031
```

设置输入框文本的高度，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 文本的高度的数字。默认值是自适应字体大小，单位fp。设置为undefined时，文本的高度设置为5。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 文本的高度的数字，单位fp。 |

## NODE\_TEXT\_AREA\_BAR\_STATE

```
1. NODE_TEXT_AREA_BAR_STATE = 8032
```

定义文本输入框滚动条状态。支持属性设置、属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 文本控制滚动条状态。参数类型为[ArkUI\_BarState](capi-native-type-h.md#arkui_barstate)。默认值为ARKUI\_BAR\_STATE\_AUTO。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 文本控制滚动条状态。参数类型为[ArkUI\_BarState](capi-native-type-h.md#arkui_barstate)。 |

## NODE\_TEXT\_AREA\_ENABLE\_SELECTED\_DATA\_DETECTOR

```
1. NODE_TEXT_AREA_ENABLE_SELECTED_DATA_DETECTOR = 8033
```

开启选中词文本识别。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 开启选中词文本识别，true表示开启识别，false表示关闭识别。默认值：true。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否开启选中词文本识别。 |

## NODE\_TEXT\_AREA\_SCROLL\_BAR\_COLOR

```
1. NODE_TEXT_AREA_SCROLL_BAR_COLOR = 8035
```

设置输入框滚动条颜色，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 滚动条颜色数值。0xargb类型。默认值：0x66182431，显示为灰色。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 滚动条颜色数值。 |

## NODE\_TEXT\_AREA\_CUSTOM\_KEYBOARD

```
1. NODE_TEXT_AREA_CUSTOM_KEYBOARD = 8036
```

设置文本输入框的自定义键盘。支持属性设置、属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 自定义键盘，参数类型[ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)。 |
| .value[0]?.i32 | 设置自定义键盘是否支持避让功能。  true表示支持避让，false表示不支持避让。  默认值：false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .object | 自定义键盘，参数类型[ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)。 |
| .value[0].i32 | 设置自定义键盘是否支持避让功能。 |

## NODE\_TEXT\_AREA\_TEXT\_CONTENT\_CONTROLLER\_BASE

```
1. NODE_TEXT_AREA_TEXT_CONTENT_CONTROLLER_BASE = 8037
```

用于设置或获取文本区域控制器。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 文本内容基础控制器，参数类型为[ArkUI\_TextContentBaseController](arkui-nativemodule-arkui-textcontentbasecontroller.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .object | 文本内容基础控制器，参数类型为[ArkUI\_TextContentBaseController](arkui-nativemodule-arkui-textcontentbasecontroller.md)。 |

## NODE\_TEXT\_AREA\_COMPRESS\_LEADING\_PUNCTUATION

```
1. NODE_TEXT_AREA_COMPRESS_LEADING_PUNCTUATION = 8040
```

设置输入字符行首标点压缩开关，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否打开行首标点压缩开关。  true表示开启行首标点压缩，false表示关闭行首标点压缩。默认值false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否打开行首标点压缩开关。 |

## NODE\_TEXT\_AREA\_INCLUDE\_FONT\_PADDING

```
1. NODE_TEXT_AREA_INCLUDE_FONT_PADDING = 8041
```

设置多行输入框内文字是否在首行和尾行增加间距以避免文字截断。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 设置输入框内文字是否在首行和尾行增加间距以避免文字截断。true表示开启增加间距，false表示关闭增加间距。默认值：false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 输入框内文字是否在首行和尾行增加间距。true表示增加间距，false表示不增加间距。 |

## NODE\_TEXT\_AREA\_FALLBACK\_LINE\_SPACING

```
1. NODE_TEXT_AREA_FALLBACK_LINE_SPACING = 8042
```

针对多行文字叠加，支持行高基于文字实际高度自适应。此接口仅当行高小于文字实际高度时生效。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 支持行高基于文字实际高度自适应。true表示开启自适应，false表示关闭自适应。默认值：false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否开启行高基于文字实际高度自适应。true表示开启自适应，false表示关闭自适应。 |

## NODE\_TEXT\_AREA\_DIRECTION

```
1. NODE_TEXT_AREA_DIRECTION = 8044
```

多行输入框的文本排版方向。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 表示文本的排版方向，取[ArkUI\_TextDirection](capi-native-type-h.md#arkui_textdirection)枚举值。默认值为ARKUI\_TEXT\_DIRECTION\_DEFAULT。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 表示文本的排版方向，对应取值及含义请参考[ArkUI\_TextDirection](capi-native-type-h.md#arkui_textdirection)枚举值。 |

## NODE\_TEXT\_AREA\_SELECTED\_DRAG\_PREVIEW\_STYLE

```
1. NODE_TEXT_AREA_SELECTED_DRAG_PREVIEW_STYLE = 8045
```

用于设置多行文本输入框内文本选中状态下的拖拽预览样式。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 文本选中状态下的拖拽预览样式。参数类型为[ArkUI\_SelectedDragPreviewStyle](ui-nativemodule-arkui-textselecteddragpreviewstyle.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .object | 文本选中状态下的拖拽预览样式。参数类型为[ArkUI\_SelectedDragPreviewStyle](ui-nativemodule-arkui-textselecteddragpreviewstyle.md)。 |
