---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h-nodeattributetype-textinputcategory
title: ArkUI_NodeAttributeType（文本输入类组件相关属性）
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 头文件 > native_node.h > ArkUI_NodeAttributeType（文本输入类组件相关属性）
category: harmonyos-references
scraped_at: 2026-09-02T14:51:46+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:12ee39d0959fd7d1e16eb5dec0cb9e9699aedd3976a221f12fae58341fee53b2
---

```c
enum ArkUI_NodeAttributeType
```

## 概述

定义ArkUI在Native侧可以设置的文本输入类组件相关属性样式集合，包含TextInput、TextArea组件属性设置。该属性集合支持光标样式、占位文本、输入过滤、自动填充、文本选中、计数器等多种样式与交互配置，适用于表单输入、搜索框、密码输入、多行文本编辑等场景，便于开发者统一管理文本输入组件的外观与行为。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_node.h](capi-native-node-h.md)

## NODE\_TEXT\_INPUT\_PLACEHOLDER

```c
NODE_TEXT_INPUT_PLACEHOLDER = MAX_NODE_SCOPE_NUM * ARKUI_NODE_TEXT_INPUT = 7000
```

单行文本输入框的默认提示文本内容属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 默认提示文本的内容。当需要在输入框显示提示信息引导用户输入时设置此属性，例如“请输入用户名”、“请输入密码”等。不设置时输入框无提示文本。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 默认提示文本的内容。 |

## NODE\_TEXT\_INPUT\_TEXT

```c
NODE_TEXT_INPUT_TEXT = 7001
```

单行文本输入框的默认文本内容属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 输入框的默认文本内容，用于设置输入框初始显示的文本。当需要在输入框中预置文本时设置此属性，例如表单默认值、编辑初始内容等。不设置时输入框为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 默认文本的内容。 |

## NODE\_TEXT\_INPUT\_CARET\_COLOR

```c
NODE_TEXT_INPUT_CARET_COLOR = 7002
```

光标颜色属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 光标颜色数值，0xARGB格式，形如 0xFFFF0000 表示红色。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 光标颜色数值，0xARGB格式。 |

## NODE\_TEXT\_INPUT\_CARET\_STYLE

```c
NODE_TEXT_INPUT_CARET_STYLE = 7003
```

光标风格属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 光标宽度数值，单位为vp。取值范围：[0, +∞)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 光标宽度数值，单位为vp。 |

## NODE\_TEXT\_INPUT\_SHOW\_UNDERLINE

```c
NODE_TEXT_INPUT_SHOW_UNDERLINE = 7004
```

单行文本输入框下划线属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 0表示不展示下划线，1表示展示下划线。默认值0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 0表示不展示下划线，1表示展示下划线。 |

## NODE\_TEXT\_INPUT\_MAX\_LENGTH

```c
NODE_TEXT_INPUT_MAX_LENGTH = 7005
```

输入框支持的最大文本数属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 最大文本数，无单位。取值范围：[0, +∞)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 最大文本数，无单位。 |

## NODE\_TEXT\_INPUT\_ENTER\_KEY\_TYPE

```c
NODE_TEXT_INPUT_ENTER_KEY_TYPE = 7006
```

回车键类型属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 回车键类型，具体枚举值请参考[ArkUI\_EnterKeyType](capi-text-common-h.md#arkui_enterkeytype)。默认值ARKUI\_ENTER\_KEY\_TYPE\_DONE，显示为完成样式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 回车键类型枚举[ArkUI\_EnterKeyType](capi-text-common-h.md#arkui_enterkeytype)，用于确定输入框回车键的显示样式。 |

## NODE\_TEXT\_INPUT\_PLACEHOLDER\_COLOR

```c
NODE_TEXT_INPUT_PLACEHOLDER_COLOR = 7007
```

无输入时默认提示文本的颜色属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 颜色数值，0xARGB格式，形如 0xFFFF0000 表示红色。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 颜色数值，0xARGB格式。 |

## NODE\_TEXT\_INPUT\_PLACEHOLDER\_FONT

```c
NODE_TEXT_INPUT_PLACEHOLDER_FONT = 7008
```

无输入时默认提示文本的字体配置（包括大小、字重、样式、字体族）属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0]?.f32 | 可选字体大小数值，默认值16.0，单位为fp。取值范围：[0, +∞)。传入负数时不生效。 |
| .value[1]?.i32 | 可选字体样式，具体枚举值请参考[ArkUI\_FontStyle](capi-text-h.md#arkui_fontstyle)。默认值为ARKUI\_FONT\_STYLE\_NORMAL，表示标准字体样式。 |
| .value[2]?.i32 | 可选字体粗细样式，具体枚举值请参考[ArkUI\_FontWeight](capi-text-h.md#arkui_fontweight)。默认值ARKUI\_FONT\_WEIGHT\_NORMAL，表示正常字体粗细。 |
| ?.string | 字体族内容，多个字体族之间使用英文逗号(,)分隔，形如“字体族1,字体族2”。不传入时使用系统默认字体族。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 字体大小数值，单位为fp。 |
| .value[1].i32 | 字体样式[ArkUI\_FontStyle](capi-text-h.md#arkui_fontstyle)。 |
| .value[2].i32 | 字体粗细样式[ArkUI\_FontWeight](capi-text-h.md#arkui_fontweight)。 |
| .string | 字体族内容，多个字体族之间使用英文逗号(,)分隔。 |

## NODE\_TEXT\_INPUT\_ENABLE\_KEYBOARD\_ON\_FOCUS

```c
NODE_TEXT_INPUT_ENABLE_KEYBOARD_ON_FOCUS = 7009
```

聚焦时是否绑定输入法属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 0表示聚焦不拉起输入法，1表示拉起，默认值为1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 0表示聚焦不拉起输入法，1表示拉起。 |

## NODE\_TEXT\_INPUT\_TYPE

```c
NODE_TEXT_INPUT_TYPE = 7010
```

输入框的类型属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 输入框类型，具体枚举值请参考[ArkUI\_TextInputType](capi-text-input-h.md#arkui_textinputtype)。默认值为ARKUI\_TEXTINPUT\_TYPE\_NORMAL，表示基本输入模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 输入框类型枚举[ArkUI\_TextInputType](capi-text-input-h.md#arkui_textinputtype)，用于确定输入框的输入内容和键盘样式。 |

## NODE\_TEXT\_INPUT\_SELECTED\_BACKGROUND\_COLOR

```c
NODE_TEXT_INPUT_SELECTED_BACKGROUND_COLOR = 7011
```

输入框文本选中时的背景色属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 颜色数值，0xARGB格式，形如 0xFFFF0000 表示红色。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 颜色数值，0xARGB格式。 |

## NODE\_TEXT\_INPUT\_SHOW\_PASSWORD\_ICON

```c
NODE_TEXT_INPUT_SHOW_PASSWORD_ICON = 7012
```

密码输入模式时是否显示末尾图标属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 0表示不显示图标，1表示显示图标，默认值为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 0表示不显示图标，1表示显示图标。 |

## NODE\_TEXT\_INPUT\_EDITING

```c
NODE_TEXT_INPUT_EDITING = 7013
```

控制单行文本输入框编辑态属性，支持属性设置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 0表示退出编辑态，1表示维持现状。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 0表示退出编辑态，1表示维持现状。 |

## NODE\_TEXT\_INPUT\_CANCEL\_BUTTON

```c
NODE_TEXT_INPUT_CANCEL_BUTTON = 7014
```

单行文本右侧清除按钮样式属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 按钮样式，具体枚举值请参考[ArkUI\_CancelButtonStyle](capi-text-input-h.md#arkui_cancelbuttonstyle)。默认值为ARKUI\_CANCELBUTTON\_STYLE\_INPUT，表示清除按钮输入样式。 |
| .value[1]?.f32 | 图标大小数值，单位为vp。取值范围：[0, +∞)。传入负数时不生效。不传入时使用系统默认图标大小。 |
| .value[2]?.u32 | 按钮图标颜色数值，0xARGB格式，形如 0xFFFF0000 表示红色。不传入时使用系统默认图标颜色。 |
| ?.string | 按钮图标地址，入参内容为图片本地地址，例如 /pages/icon.png。不传入时使用系统默认清除图标。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 按钮样式[ArkUI\_CancelButtonStyle](capi-text-input-h.md#arkui_cancelbuttonstyle)。 |
| .value[1].f32 | 图标大小数值，单位为vp。 |
| .value[2].u32 | 按钮图标颜色数值，0xARGB格式。 |
| .string | 按钮图标地址。 |

## NODE\_TEXT\_INPUT\_TEXT\_SELECTION

```c
NODE_TEXT_INPUT_TEXT_SELECTION = 7015
```

组件在获焦状态下，设置文本选中并高亮的区域，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 选中文本的起始位置，取值范围[0, 文本长度]，需小于终止位置才生效。 |
| .value[1].i32 | 选中文本的终止位置，取值范围[0, 文本长度]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 选中文本的起始位置。 |
| .value[1].i32 | 选中文本的终止位置。 |

## NODE\_TEXT\_INPUT\_UNDERLINE\_COLOR

```c
NODE_TEXT_INPUT_UNDERLINE_COLOR = 7016
```

开启下划线时，支持配置下划线颜色。需先设置NODE\_TEXT\_INPUT\_SHOW\_UNDERLINE属性为1以开启下划线后，本属性设置才生效。主题配置的默认下划线颜色为0x33182431，表示深灰色，不透明度为20%。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | typing下划线颜色，必填，表示键入时的下划线颜色，0xARGB类型。 |
| .value[1].u32 | normal下划线颜色，必填，表示非特殊状态时下划线颜色，0xARGB类型。 |
| .value[2].u32 | error下划线颜色，必填，表示错误时下划线颜色，0xARGB类型。 |
| .value[3].u32 | disable下划线颜色，必填，表示禁用时下划线颜色，0xARGB类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | typing下划线颜色，表示键入时的下划线颜色，0xARGB类型。 |
| .value[1].u32 | normal下划线颜色，表示非特殊状态时下划线颜色，0xARGB类型。 |
| .value[2].u32 | error下划线颜色，表示错误时下划线颜色，0xARGB类型。 |
| .value[3].u32 | disable下划线颜色，表示禁用时下划线颜色，0xARGB类型。 |

## NODE\_TEXT\_INPUT\_ENABLE\_AUTO\_FILL

```c
NODE_TEXT_INPUT_ENABLE_AUTO_FILL = 7017
```

设置是否启用自动填充。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否启用自动填充，默认值1。  0表示不启用，1表示启用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否启用自动填充。1表示启用，0表示不启用。 |

## NODE\_TEXT\_INPUT\_CONTENT\_TYPE

```c
NODE_TEXT_INPUT_CONTENT_TYPE = 7018
```

自动填充类型。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 参数类型[ArkUI\_TextInputContentType](capi-text-input-h.md#arkui_textinputcontenttype)，用于自动填充场景指定内容类型。具体枚举值及适用场景请参考[ArkUI\_TextInputContentType](capi-text-input-h.md#arkui_textinputcontenttype)枚举说明。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 自动填充内容类型枚举[ArkUI\_TextInputContentType](capi-text-input-h.md#arkui_textinputcontenttype)，用于确定自动填充的内容类型。 |

## NODE\_TEXT\_INPUT\_PASSWORD\_RULES

```c
NODE_TEXT_INPUT_PASSWORD_RULES = 7019
```

定义生成密码的规则。在触发自动填充时，所设置的密码规则会透传给密码保险箱，用于新密码的生成。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 定义生成密码的规则，用于在触发自动填充时透传给密码保险箱以控制新密码的生成。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 定义生成密码的规则。 |

## NODE\_TEXT\_INPUT\_SELECT\_ALL

```c
NODE_TEXT_INPUT_SELECT_ALL = 7020
```

设置初始状态时是否全选文本。不支持内联模式。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否全选文本，默认值：0。  1表示会全选文本，0表示不会全选文本。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否全选文本。1表示会全选文本，0表示不会全选文本。 |

## NODE\_TEXT\_INPUT\_INPUT\_FILTER

```c
NODE_TEXT_INPUT_INPUT_FILTER = 7021
```

通过正则表达式设置输入过滤器。匹配表达式的输入允许显示，不匹配的输入将被过滤。单字符输入场景仅支持单字符匹配，多字符输入场景支持字符串匹配，例如粘贴。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 正则表达式，用于过滤用户输入内容。匹配表达式的输入允许显示，不匹配的输入将被过滤。当需要限制用户只能输入特定格式的字符时设置此属性，例如"^[a-zA-Z]+$"表示只允许字母，"^[0-9]+$"表示只允许数字。不设置时允许所有字符输入。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 正则表达式。 |

## NODE\_TEXT\_INPUT\_STYLE

```c
NODE_TEXT_INPUT_STYLE = 7022
```

设置输入框为默认风格或内联输入风格。内联输入风格是一种无边框的嵌入式输入样式，输入框直接融入页面内容中。内联输入风格只支持输入框类型的枚举[ArkUI\_TextInputType](capi-text-input-h.md#arkui_textinputtype)设置为ARKUI\_TEXTINPUT\_TYPE\_NORMAL。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 参数类型[ArkUI\_TextInputStyle](capi-text-input-h.md#arkui_textinputstyle)。内联输入风格只支持输入框类型[ArkUI\_TextInputType](capi-text-input-h.md#arkui_textinputtype)设置为ARKUI\_TEXTINPUT\_TYPE\_NORMAL。默认值为ARKUI\_TEXTINPUT\_STYLE\_DEFAULT。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 输入框样式枚举[ArkUI\_TextInputStyle](capi-text-input-h.md#arkui_textinputstyle)，用于确定输入框的显示样式。 |

## NODE\_TEXT\_INPUT\_CARET\_OFFSET

```c
NODE_TEXT_INPUT_CARET_OFFSET = 7023
```

设置或获取光标所在位置信息。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

设置输入光标的位置。

返回当前光标所在位置信息。在当前帧更新光标位置同时调用该接口，该接口不生效。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 从字符串开始到光标所在位置的字符长度，取值范围[0, 文本长度]。超出范围时自动修正为边界值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 光标所在位置的索引值。 |
| .value[1].f32 | 光标相对输入框的x坐标值，单位为px。 |
| .value[2].f32 | 光标相对输入框的y坐标值，单位为px。 |

## NODE\_TEXT\_INPUT\_CONTENT\_RECT

```c
NODE_TEXT_INPUT_CONTENT_RECT = 7024
```

获取已编辑文本内容区域相对组件的位置和大小。

作为属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 水平方向横坐标，单位为px。 |
| .value[1].f32 | 竖直方向纵坐标，单位为px。 |
| .value[2].f32 | 内容宽度大小，单位为px。 |
| .value[3].f32 | 内容高度大小，单位为px。 |

## NODE\_TEXT\_INPUT\_CONTENT\_LINE\_COUNT

```c
NODE_TEXT_INPUT_CONTENT_LINE_COUNT = 7025
```

获取已编辑文本内容的行数。

作为属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 已编辑文本内容行数。 |

## NODE\_TEXT\_INPUT\_SELECTION\_MENU\_HIDDEN

```c
NODE_TEXT_INPUT_SELECTION_MENU_HIDDEN = 7026
```

设置长按、双击输入框或者右键输入框时，是否不弹出文本选择菜单，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 长按、双击输入框或者右键输入框时，是否不弹出文本选择菜单。默认值0。  设置为1时，单击输入框光标、长按输入框、双击输入框、三击输入框或者右键输入框，隐藏系统文本选择菜单。  设置为0时，显示系统文本选择菜单。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 长按、双击输入框或者右键输入框时，是否不弹出文本选择菜单。1表示不弹出菜单，0表示弹出菜单。 |

## NODE\_TEXT\_INPUT\_BLUR\_ON\_SUBMIT

```c
NODE_TEXT_INPUT_BLUR_ON_SUBMIT = 7027
```

设置输入框在submit状态下，触发回车键是否失焦。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 触发回车键后是否失焦。默认值1。  0表示不失焦，1表示失焦。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 触发回车键后是否失焦。1表示失焦，0表示不失焦。 |

## NODE\_TEXT\_INPUT\_CUSTOM\_KEYBOARD

```c
NODE_TEXT_INPUT_CUSTOM_KEYBOARD = 7028
```

设置自定义键盘。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 自定义键盘，参数类型[ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)。 |
| .value[0]?.i32 | 设置自定义键盘是否支持避让功能，默认值0。  1表示支持避让，0表示不支持避让。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .object | 自定义键盘，参数类型[ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)。 |
| .value[0].i32 | 设置自定义键盘是否支持避让功能。0表示不支持避让，1表示支持避让。 |

## NODE\_TEXT\_INPUT\_WORD\_BREAK

```c
NODE_TEXT_INPUT_WORD_BREAK = 7029
```

文本断行规则属性，仅在内联输入风格编辑态生效，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 参数类型[ArkUI\_WordBreak](capi-text-common-h.md#arkui_wordbreak)。仅在内联输入风格编辑态生效。默认值ARKUI\_WORD\_BREAK\_BREAK\_WORD。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 文本断行规则枚举[ArkUI\_WordBreak](capi-text-common-h.md#arkui_wordbreak)，用于确定文本的断行方式。 |

## NODE\_TEXT\_INPUT\_SHOW\_KEYBOARD\_ON\_FOCUS

```c
NODE_TEXT_INPUT_SHOW_KEYBOARD_ON_FOCUS = 7030
```

设置输入框获取焦点时是否弹出键盘，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否弹出键盘。默认值1。  0表示获取焦点时不弹出键盘，1表示获取焦点时弹出键盘。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否弹出键盘。1表示弹出键盘，0表示不弹出键盘。 |

## NODE\_TEXT\_INPUT\_NUMBER\_OF\_LINES

```c
NODE_TEXT_INPUT_NUMBER_OF_LINES = 7031
```

设置该属性后，通过该属性计算[TextInput](ts-basic-components-textinput.md)组件的高度。 例如：设置numberOfLines为3时，组件将默认显示足够容纳3行文本内容的高度。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 设置行数，取值范围[1, +∞)，用于通过该属性计算TextInput组件的高度。例如：设置为3时，组件将默认显示足够容纳3行文本内容的高度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 设置numberOfLines的值。 |

## NODE\_TEXT\_INPUT\_LETTER\_SPACING

```c
NODE_TEXT_INPUT_LETTER_SPACING = 7032
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

```c
NODE_TEXT_INPUT_ENABLE_PREVIEW_TEXT = 7033
```

设置[TextInput](ts-basic-components-textinput.md)组件是否开启输入预上屏。接口支持设置，重置以及获取该属性。

“预上屏”描述的是一种文字暂存状态。需要在输入法中开启预上屏功能，在输入文本过程中，未确认输入候选词时，文本框中显示标记文本。例如，通过拼音输入中文时，未确定候选词之前，在输入框中显示拼音字母，该状态称为文字预上屏。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 设置是否开启输入预上屏。默认值1。  0表示不开启输入预上屏，1表示开启输入预上屏。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 获取是否开启输入预上屏。0表示不开启输入预上屏，1表示开启输入预上屏。 |

## NODE\_TEXT\_INPUT\_HALF\_LEADING

```c
NODE_TEXT_INPUT_HALF_LEADING = 7034
```

设置文本将行间距平分至行的顶部与底部。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 设置文本是否将行间距平分至行的顶部与底部。默认值0。  1表示将行间距平分至行的顶部与底部，0表示不平分。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 文本行间距是否平分至行的顶部与底部。1表示平分，0表示不平分。 |

## NODE\_TEXT\_INPUT\_KEYBOARD\_APPEARANCE

```c
NODE_TEXT_INPUT_KEYBOARD_APPEARANCE = 7035
```

设置输入框拉起的键盘样式。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 键盘样式，参数类型[ArkUI\_KeyboardAppearance](capi-text-common-h.md#arkui_keyboardappearance)。具体枚举值请参考ArkUI\_KeyboardAppearance枚举说明。默认值ARKUI\_KEYBOARD\_APPEARANCE\_NONE\_IMMERSIVE，不使用沉浸式样式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 键盘样式，参数类型[ArkUI\_KeyboardAppearance](capi-text-common-h.md#arkui_keyboardappearance)。具体枚举值请参考ArkUI\_KeyboardAppearance枚举说明。默认值ARKUI\_KEYBOARD\_APPEARANCE\_NONE\_IMMERSIVE。 |

## NODE\_TEXT\_INPUT\_ENABLE\_FILL\_ANIMATION

```c
NODE_TEXT_INPUT_ENABLE_FILL_ANIMATION = 7036
```

设置是否启用自动填充动效。仅当输入框类型[ArkUI\_TextInputType](capi-text-input-h.md#arkui_textinputtype)设置为ARKUI\_TEXTINPUT\_TYPE\_PASSWORD、ARKUI\_TEXTINPUT\_TYPE\_NUMBER\_PASSWORD或ARKUI\_TEXTINPUT\_TYPE\_NEW\_PASSWORD时，该动效才生效。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否启用自动填充动效。启用之后，仅输入框类型的枚举[ArkUI\_TextInputType](capi-text-input-h.md#arkui_textinputtype)设置为ARKUI\_TEXTINPUT\_TYPE\_PASSWORD、ARKUI\_TEXTINPUT\_TYPE\_NUMBER\_PASSWORD或ARKUI\_TEXTINPUT\_TYPE\_NEW\_PASSWORD的输入框在进行自动填充时动效可生效。  1表示启用，0表示不启用。  默认值1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否启用自动填充动效。0表示不启用，1表示启用。启用之后，仅输入框类型的枚举[ArkUI\_TextInputType](capi-text-input-h.md#arkui_textinputtype)设置为ARKUI\_TEXTINPUT\_TYPE\_PASSWORD、ARKUI\_TEXTINPUT\_TYPE\_NUMBER\_PASSWORD或ARKUI\_TEXTINPUT\_TYPE\_NEW\_PASSWORD的输入框在进行自动填充时动效可生效。 |

## NODE\_TEXT\_INPUT\_LINE\_HEIGHT

```c
NODE_TEXT_INPUT_LINE_HEIGHT = 7037
```

设置输入框文本行高，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 文本行高，单位fp。默认值是自适应字体大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 文本行高，单位fp。 |

## NODE\_TEXT\_INPUT\_ENABLE\_SELECTED\_DATA\_DETECTOR

```c
NODE_TEXT_INPUT_ENABLE_SELECTED_DATA_DETECTOR = 7038
```

开启选中词文本识别，支持识别选中文本中的电话号码、邮箱地址、网址链接等实体信息，便于用户快捷拨打电话、发送邮件或打开链接。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 开启选中词文本识别，1表示开启识别，0表示关闭识别。默认值：1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否开启选中词文本识别。1表示已开启识别，0表示已关闭识别。 |

## NODE\_TEXT\_INPUT\_SHOW\_COUNTER

```c
NODE_TEXT_INPUT_SHOW_COUNTER = 7040
```

设置输入的字符数超过阈值时是否显示计数器并设置计数器样式，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否开启计数器。值为1表示开启计数器，值为0表示不开启计数器。 |
| .value[1]?.f32 | 可输入字符数占最大字符限制的百分比值，超过此值时显示计数器，取值范围[1, 100]，小数时向下取整，若超出取值范围，则接口属性设置不生效。默认值-1，即始终显示计数器。 |
| .value[2]?.i32 | 输入字符超出限制时高亮边框，1表示高亮边框，0表示不高亮边框。默认值1。 |
| .object | 计数器配置，配置属性为文本输入框未达到最大字符数时计数器的颜色以及超出最大字符数时计数器的颜色。参数类型为 [ArkUI\_ShowCounterConfig](capi-arkui-nativemodule-arkui-textshowcounterconfig.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否开启计数器。0表示不开启计数器，1表示开启计数器。 |
| .value[1].f32 | 可输入字符数占最大字符限制的百分比值，超过此值时显示计数器，取值范围[1, 100]。 |
| .value[2].i32 | 输入字符超出限制时高亮边框。0表示不高亮边框，1表示高亮边框。 |
| .object | 计数器配置，配置属性为文本输入框未达到最大字符数时计数器的颜色以及超出最大字符数时计数器的颜色。参数类型为[ArkUI\_ShowCounterConfig](capi-arkui-nativemodule-arkui-textshowcounterconfig.md)。 |

## NODE\_TEXT\_INPUT\_TEXT\_CONTENT\_CONTROLLER\_BASE

```c
NODE_TEXT_INPUT_TEXT_CONTENT_CONTROLLER_BASE = 7041
```

用于设置或获取文本输入控制器。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 文本内容基础控制器。参数类型为[ArkUI\_TextContentBaseController](capi-arkui-nativemodule-arkui-textcontentbasecontroller.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .object | 文本内容基础控制器。参数类型为[ArkUI\_TextContentBaseController](capi-arkui-nativemodule-arkui-textcontentbasecontroller.md)。 |

## NODE\_TEXT\_INPUT\_ELLIPSIS\_MODE

```c
NODE_TEXT_INPUT_ELLIPSIS_MODE = 7042
```

设置单行文本输入框中文本省略位置，支持属性设置，属性重置，属性获取接口。

此属性存在以下配置依赖：

* 此属性只有在NODE\_TEXT\_INPUT\_TEXT\_OVERFLOW设置为ARKUI\_TEXT\_OVERFLOW\_ELLIPSIS时才生效
* 当TEXT\_OVERFLOW设置为ARKUI\_TEXT\_OVERFLOW\_CLIP时，ELLIPSIS\_MODE的设置不会生效
* 建议先设置TEXT\_OVERFLOW为ELLIPSIS，再设置ELLIPSIS\_MODE指定省略位置

  作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 参数类型[ArkUI\_EllipsisMode](capi-text-common-h.md#arkui_ellipsismode)。具体枚举值请参考ArkUI\_EllipsisMode枚举说明。默认值为ARKUI\_ELLIPSIS\_MODE\_END。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 文本省略位置枚举[ArkUI\_EllipsisMode](capi-text-common-h.md#arkui_ellipsismode)，用于确定文本超长时的省略位置。 |

## NODE\_TEXT\_INPUT\_ORPHAN\_CHAR\_OPTIMIZATION

```c
NODE_TEXT_INPUT_ORPHAN_CHAR_OPTIMIZATION = 7043
```

设置TextInput文本排版时是否使能孤字优化。使能后通过更高效地处理孤立字符（段落尾行首字符）来改善文本布局，调整换行点以尽可能避免孤立字符。

注意：该特性需在[ArkUI\_WordBreak](capi-text-common-h.md#arkui_wordbreak)属性为非ARKUI\_WORD\_BREAK\_BREAK\_ALL时生效。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否使能孤字优化。该特性需在[ArkUI\_WordBreak](capi-text-common-h.md#arkui_wordbreak)属性为非ARKUI\_WORD\_BREAK\_BREAK\_ALL时生效。1表示使能，0表示不使能。默认值0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否使能孤字优化。0表示不使能，1表示使能。 |

## NODE\_TEXT\_INPUT\_COMPRESS\_LEADING\_PUNCTUATION

```c
NODE_TEXT_INPUT_COMPRESS_LEADING_PUNCTUATION = 7044
```

设置输入字符行首标点压缩开关，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否打开行首标点压缩开关。  1表示开启行首标点压缩，0表示关闭行首标点压缩。默认值0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否打开行首标点压缩开关。0表示关闭行首标点压缩，1表示开启行首标点压缩。 |

## NODE\_TEXT\_INPUT\_INCLUDE\_FONT\_PADDING

```c
NODE_TEXT_INPUT_INCLUDE_FONT_PADDING = 7045
```

设置单行输入框内文字是否在首行顶部和尾行底部增加间距以避免文字截断。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 设置输入框内文字是否在首行顶部和尾行底部增加间距以避免文字截断。1表示开启增加间距，0表示关闭增加间距。默认值：0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否在首行顶部和尾行底部增加间距。0表示不增加间距，1表示增加间距。 |

## NODE\_TEXT\_INPUT\_FALLBACK\_LINE\_SPACING

```c
NODE_TEXT_INPUT_FALLBACK_LINE_SPACING = 7046
```

针对多行文本显示场景，支持行高基于文字实际高度自适应。此接口仅当行高小于文字实际高度时生效。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 支持行高基于文字实际高度自适应。此接口仅当行高小于文字实际高度时生效。1表示开启自适应，0表示关闭自适应。默认值：0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否开启行高基于文字实际高度自适应。0表示关闭自适应，1表示开启自适应。 |

## NODE\_TEXT\_INPUT\_DIRECTION

```c
NODE_TEXT_INPUT_DIRECTION = 7047
```

单行输入框的文本排版方向。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 表示文本的排版方向，取[ArkUI\_TextDirection](capi-text-common-h.md#arkui_textdirection)枚举值。默认值为ARKUI\_TEXT\_DIRECTION\_DEFAULT。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 表示文本的排版方向，对应取值及含义请参考[ArkUI\_TextDirection](capi-text-common-h.md#arkui_textdirection)枚举值。 |

## NODE\_TEXT\_INPUT\_SELECTED\_DRAG\_PREVIEW\_STYLE

```c
NODE_TEXT_INPUT_SELECTED_DRAG_PREVIEW_STYLE = 7048
```

用于设置文本输入框内文本选中状态下的拖拽预览样式。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 文本选中状态下的拖拽预览样式。参数类型为[ArkUI\_SelectedDragPreviewStyle](capi-arkui-nativemodule-arkui-textselecteddragpreviewstyle.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .object | 文本选中状态下的拖拽预览样式。参数类型为[ArkUI\_SelectedDragPreviewStyle](capi-arkui-nativemodule-arkui-textselecteddragpreviewstyle.md)。 |

## NODE\_TEXT\_INPUT\_LINEAR\_GRADIENT

```c
NODE_TEXT_INPUT_LINEAR_GRADIENT = 7051
```

设置文本输入框内文本线性渐变效果，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 线性渐变的起始角度，单位为deg。当线性渐变的方向为[ArkUI\_LinearGradientDirection](capi-native-type-visual-h.md#arkui_lineargradientdirection)的ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_CUSTOM时，线性渐变的起始角度属性生效，否则按线性渐变的方向属性为主要布局方式。取值范围为(-∞,+∞)，0点方向顺时针旋转为正向角度，当超过360时，是按照360取余处理，默认值：180。 |
| .value[1].i32 | 线性渐变的方向，取值为[ArkUI\_LinearGradientDirection](capi-native-type-visual-h.md#arkui_lineargradientdirection)枚举。设置除ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_CUSTOM之外的方向后，起始角度不生效。默认值：ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_LEFT\_BOTTOM。 |
| .value[2].i32 | 渐变的颜色是否重复着色，0表示不重复着色，1表示重复着色。默认值：0。 |
| .object | 指定位置处的渐变色颜色，参数类型为[ArkUI\_ColorStop](capi-arkui-nativemodule-arkui-colorstop.md)。  - colors：渐变色颜色数组，元素为0xARGB格式，形如0xFFFF0000表示红色。  - stops：指定颜色所处位置的数组，取值范围[0,1.0]，0表示容器开始处，1.0表示结尾处。建议递增设置。  - size：颜色个数，若小于colors数组长度则仅生效前size个颜色。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 线性渐变的起始角度，单位为deg。当线性渐变的方向为[ArkUI\_LinearGradientDirection](capi-native-type-visual-h.md#arkui_lineargradientdirection)的ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_CUSTOM时，线性渐变的起始角度为设置值，其他情况均为默认值0。 |
| .value[1].i32 | 线性渐变的方向。对应取值及含义请参考[ArkUI\_LinearGradientDirection](capi-native-type-visual-h.md#arkui_lineargradientdirection)。 |
| .value[2].i32 | 渐变的颜色是否重复着色，0表示不重复着色，1表示重复着色。默认值：0。 |
| .object | 指定位置处的渐变色颜色。参数类型为[ArkUI\_ColorStop](capi-arkui-nativemodule-arkui-colorstop.md)。  colors：渐变色颜色数组，数组元素为0xARGB格式，形如0xFFFF0000表示红色。  stops：stops表示指定颜色所处位置的数组，数组元素取值范围为[0,1.0]，0表示需要设置渐变色的容器的开始处，1.0表示容器的结尾处。  size：生效后渐变色的颜色个数。 |

## NODE\_TEXT\_INPUT\_RADIAL\_GRADIENT

```c
NODE_TEXT_INPUT_RADIAL_GRADIENT = 7052
```

设置文本输入框的文本径向渐变效果，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0]?.f32 | 径向渐变的中心点X轴坐标，即相对于当前文本输入框左上角的X轴坐标，单位为vp。默认值为文本输入框宽度的一半。 |
| .value[1]?.f32 | 径向渐变的中心点Y轴坐标，即相对于当前文本输入框左上角的Y轴坐标，单位为vp。默认值为文本输入框高度的一半。 |
| .value[2]?.f32 | 径向渐变的半径，单位为vp。取值范围[0, +∞)，默认值0。传入负数时不生效。 |
| .value[3]?.i32 | 渐变的颜色是否重复着色，0表示不重复着色，1表示重复着色。默认值：0。 |
| .object | 指定位置处的渐变色颜色。参数类型为[ArkUI\_ColorStop](capi-arkui-nativemodule-arkui-colorstop.md)。  colors：渐变色数组，元素为0xARGB格式，形如0xFFFF0000表示红色。  stops：指定颜色所处位置的数组，取值范围[0,1.0]，0表示容器开始处，1.0表示结尾处。建议递增设置，若后一元素小于前一元素，则按等于前一元素的值处理。  size：颜色个数，若小于colors数组长度则仅生效前size个颜色，不建议设置异常值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0]?.f32 | 径向渐变的中心点X轴坐标，即相对于当前文本输入框左上角的X轴坐标，单位为vp。 |
| .value[1]?.f32 | 径向渐变的中心点Y轴坐标，即相对于当前文本输入框左上角的Y轴坐标，单位为vp。 |
| .value[2]?.f32 | 径向渐变的半径，单位为vp，默认值0。 |
| .value[3]?.i32 | 渐变的颜色是否重复着色，0表示不重复着色，1表示重复着色。默认值：0。 |
| .object | 指定位置处的渐变色颜色。参数类型为[ArkUI\_ColorStop](capi-arkui-nativemodule-arkui-colorstop.md)。  colors：渐变色颜色数组，数组元素为0xARGB格式，形如0xFFFF0000表示红色。  stops：stops表示指定颜色所处位置的数组，数组元素取值范围为[0,1.0]，0表示需要设置渐变色的容器的开始处，1.0表示容器的结尾处。  size：生效后渐变色的颜色个数。 |

## NODE\_TEXT\_INPUT\_TEXT\_OVERFLOW

```c
NODE_TEXT_INPUT_TEXT_OVERFLOW = 7049
```

单行文本输入框中文本超长时的显示方式属性，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 表示文本超长时的显示方式[ArkUI\_TextOverflow](capi-text-common-h.md#arkui_textoverflow)。内联模式非编辑态下默认值为ARKUI\_TEXT\_OVERFLOW\_ELLIPSIS，内联模式编辑态下默认值为ARKUI\_TEXT\_OVERFLOW\_CLIP。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 表示文本超长时的显示方式[ArkUI\_TextOverflow](capi-text-common-h.md#arkui_textoverflow)。 |

## NODE\_TEXT\_INPUT\_DECORATION

```c
NODE_TEXT_INPUT_DECORATION = 7050
```

定义单行输入框的文本装饰线样式与颜色，支持属性设置、属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 装饰样式配置项，为可选参数。参数类型为[OH\_ArkUI\_DecorationStyleOptions](capi-arkui-nativemodule-oh-arkui-decorationstyleoptions.md)。不传入时不添加装饰线。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .object | 装饰样式配置项。参数类型为[OH\_ArkUI\_DecorationStyleOptions](capi-arkui-nativemodule-oh-arkui-decorationstyleoptions.md)。 |

## NODE\_TEXT\_INPUT\_PUNCTUATION\_OVERFLOW

```c
NODE_TEXT_INPUT_PUNCTUATION_OVERFLOW = 7053
```

设置TextInput组件是否启用行尾标点符号悬挂，支持属性设置，属性重置和属性获取。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否启用行尾标点符号悬挂。1表示启用标点符号悬挂，0表示不启用标点符号悬挂。默认值为0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否启用行尾标点符号悬挂。0表示不启用标点符号悬挂，1表示启用标点符号悬挂。 |

## NODE\_TEXT\_AREA\_PLACEHOLDER

```c
NODE_TEXT_AREA_PLACEHOLDER = MAX_NODE_SCOPE_NUM * ARKUI_NODE_TEXT_AREA = 8000
```

多行文本输入框的默认提示文本内容属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 默认提示文本的内容。当需要在输入框显示提示信息引导用户输入时设置此属性，例如“请输入用户名”、“请输入内容”等。不设置时输入框无提示文本。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 默认提示文本的内容。 |

## NODE\_TEXT\_AREA\_TEXT

```c
NODE_TEXT_AREA_TEXT = 8001
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

```c
NODE_TEXT_AREA_MAX_LENGTH = 8002
```

输入框支持的最大文本数属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 最大文本数数值。取值范围[0, +∞)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 最大文本数的数字。 |

## NODE\_TEXT\_AREA\_PLACEHOLDER\_COLOR

```c
NODE_TEXT_AREA_PLACEHOLDER_COLOR = 8003
```

无输入时默认提示文本的颜色属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 颜色数值，0xARGB格式，形如 0xFFFF0000 表示红色。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 颜色数值，0xARGB格式。 |

## NODE\_TEXT\_AREA\_PLACEHOLDER\_FONT

```c
NODE_TEXT_AREA_PLACEHOLDER_FONT = 8004
```

无输入时默认提示文本的字体配置（包括大小、字重、样式、字体列表）属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0]?.f32 | 可选字体大小数值，默认值16.0，单位为fp。取值范围[0, +∞)。 |
| .value[1]?.i32 | 可选字体样式[ArkUI\_FontStyle](capi-text-h.md#arkui_fontstyle)。具体样式值请参考ArkUI\_FontStyle枚举。默认值为ARKUI\_FONT\_STYLE\_NORMAL，表示标准字体样式。 |
| .value[2]?.i32 | 可选字体粗细样式[ArkUI\_FontWeight](capi-text-h.md#arkui_fontweight)。具体字重值请参考ArkUI\_FontWeight枚举。默认值为ARKUI\_FONT\_WEIGHT\_NORMAL，表示正常字体粗细。 |
| ?.string | 字体族内容，多个字体族之间使用英文逗号(,)分隔，形如“字体族1,字体族2”。不传入时使用系统默认字体族。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 字体大小数值，单位为fp。 |
| .value[1].i32 | 字体样式[ArkUI\_FontStyle](capi-text-h.md#arkui_fontstyle)。 |
| .value[2].i32 | 字体粗细样式[ArkUI\_FontWeight](capi-text-h.md#arkui_fontweight)。 |
| .string | 字体族内容，多个字体族之间使用英文逗号(,)分隔。 |

## NODE\_TEXT\_AREA\_CARET\_COLOR

```c
NODE_TEXT_AREA_CARET_COLOR = 8005
```

光标颜色属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 光标颜色数值，0xARGB格式，形如 0xFFFF0000 表示红色。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 光标颜色数值，0xARGB格式。 |

## NODE\_TEXT\_AREA\_EDITING

```c
NODE_TEXT_AREA_EDITING = 8006
```

控制多行文本输入框编辑态属性，支持属性设置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 0表示退出编辑态，1表示维持现状。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 0表示退出编辑态，1表示维持现状。 |

## NODE\_TEXT\_AREA\_TYPE

```c
NODE_TEXT_AREA_TYPE = 8007
```

输入框的类型属性，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 输入框类型枚举[ArkUI\_TextAreaType](capi-text-area-h.md#arkui_textareatype)。具体值请参考ArkUI\_TextAreaType枚举。默认值为ARKUI\_TEXTAREA\_TYPE\_NORMAL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 输入框类型枚举[ArkUI\_TextAreaType](capi-text-area-h.md#arkui_textareatype)，用于确定多行文本输入框的类型。 |

## NODE\_TEXT\_AREA\_SHOW\_COUNTER

```c
NODE_TEXT_AREA_SHOW_COUNTER = 8008
```

设置输入的字符数超过阈值时是否显示计数器并设置计数器样式，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否开启计数器，值为1时为开启。默认值0。 |
| .value[1]?.f32 | 可输入字符数占最大字符限制的百分比值，超过此值时显示计数器，取值范围[1, 100]，小数时向下取整，若超出取值范围，则接口属性设置不生效。默认值-1，即始终显示计数器。 |
| .value[2]?.i32 | 输入字符超出限制时是否高亮边框。1表示高亮边框，0表示不高亮边框。默认值1。 |
| .object | 计数器配置，配置属性为文本输入框未达到最大字符数时计数器的颜色以及超出最大字符数时计数器的颜色。参数类型为[ArkUI\_ShowCounterConfig](capi-arkui-nativemodule-arkui-textshowcounterconfig.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否开启计数器。0表示不开启计数器，1表示开启计数器。 |
| .value[1].f32 | 可输入字符数占最大字符限制的百分比值，超过此值时显示计数器，取值范围[1, 100]。 |
| .value[2].i32 | 输入字符超出限制时是否高亮边框。0表示不高亮边框，1表示高亮边框。 |
| .object | 计数器配置，配置属性为文本输入框未达到最大字符数时计数器的颜色以及超出最大字符数时计数器的颜色。参数类型为[ArkUI\_ShowCounterConfig](capi-arkui-nativemodule-arkui-textshowcounterconfig.md)。 |

## NODE\_TEXT\_AREA\_SELECTION\_MENU\_HIDDEN

```c
NODE_TEXT_AREA_SELECTION_MENU_HIDDEN = 8009
```

设置长按、双击输入框或者右键输入框时，是否不弹出文本选择菜单，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 长按、双击输入框或者右键输入框时，是否不弹出文本选择菜单。  设置为1时，单击输入框光标、长按输入框、双击输入框、三击输入框或者右键输入框，隐藏系统文本选择菜单。  设置为0时，显示系统文本选择菜单。  默认值0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 长按、双击输入框或者右键输入框时，是否不弹出文本选择菜单。0表示显示系统文本选择菜单，1表示隐藏系统文本选择菜单。 |

## NODE\_TEXT\_AREA\_BLUR\_ON\_SUBMIT

```c
NODE_TEXT_AREA_BLUR_ON_SUBMIT = 8010
```

设置多行输入框在submit状态下，触发回车键是否失焦。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 触发回车键后是否失焦。  0表示触发回车键后不失焦，1表示触发回车键后失焦。  默认值0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 触发回车键后是否失焦。0表示触发回车键后不失焦，1表示触发回车键后失焦。 |

## NODE\_TEXT\_AREA\_INPUT\_FILTER

```c
NODE_TEXT_AREA_INPUT_FILTER = 8011
```

通过正则表达式设置输入过滤器。匹配表达式的输入允许显示，不匹配的输入将被过滤。单字符输入场景仅支持单字符匹配，多字符输入场景支持字符串匹配，例如粘贴。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .string | 正则表达式，用于过滤用户输入内容。匹配表达式的输入允许显示，不匹配的输入将被过滤。当需要限制用户只能输入特定格式的字符时设置此属性，例如“^[a-zA-Z]+$”表示只允许字母，“^[0-9]+$”表示只允许数字。不设置时允许所有字符输入。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .string | 正则表达式。 |

## NODE\_TEXT\_AREA\_SELECTED\_BACKGROUND\_COLOR

```c
NODE_TEXT_AREA_SELECTED_BACKGROUND_COLOR = 8012
```

设置文本选中底板颜色，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].u32 | 颜色数值，0xARGB格式，形如 0xFFFF0000 表示红色。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].u32 | 颜色数值，0xARGB格式。 |

## NODE\_TEXT\_AREA\_ENTER\_KEY\_TYPE

```c
NODE_TEXT_AREA_ENTER_KEY_TYPE = 8013
```

设置输入法回车键类型，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 回车键类型，具体枚举值参考[ArkUI\_EnterKeyType](capi-text-common-h.md#arkui_enterkeytype)。默认值ARKUI\_ENTER\_KEY\_TYPE\_DONE，显示为完成样式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 回车键类型枚举[ArkUI\_EnterKeyType](capi-text-common-h.md#arkui_enterkeytype)，用于确定输入框回车键的显示样式。 |

## NODE\_TEXT\_AREA\_ENABLE\_KEYBOARD\_ON\_FOCUS

```c
NODE_TEXT_AREA_ENABLE_KEYBOARD_ON_FOCUS = 8014
```

设置TextArea通过点击以外的方式获焦时，是否绑定输入法，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 0表示聚焦不拉起输入法，1表示拉起。默认值为1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 0表示聚焦不拉起输入法，1表示拉起。 |

## NODE\_TEXT\_AREA\_CARET\_OFFSET

```c
NODE_TEXT_AREA_CARET_OFFSET = 8015
```

设置或获取光标所在位置信息。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

设置输入光标的位置。

返回当前光标所在位置信息。在当前帧更新光标位置同时调用该接口，该接口不生效。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 从字符串开始到光标所在位置的字符长度，取值范围[0, 文本长度]。超出范围时自动修正为边界值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 光标所在位置的索引值。 |
| .value[1].f32 | 光标相对输入框的x坐标值，单位为px。 |
| .value[2].f32 | 光标相对输入框的y坐标值，单位为px。 |

## NODE\_TEXT\_AREA\_CONTENT\_RECT

```c
NODE_TEXT_AREA_CONTENT_RECT = 8016
```

获取已编辑文本内容区域相对组件的位置和大小。

作为属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 水平方向横坐标，单位为px。 |
| .value[1].f32 | 竖直方向纵坐标，单位为px。 |
| .value[2].f32 | 内容宽度大小，单位为px。 |
| .value[3].f32 | 内容高度大小，单位为px。 |

## NODE\_TEXT\_AREA\_CONTENT\_LINE\_COUNT

```c
NODE_TEXT_AREA_CONTENT_LINE_COUNT = 8017
```

获取已编辑文本内容的行数。

作为属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 已编辑文本内容行数。 |

## NODE\_TEXT\_AREA\_TEXT\_SELECTION

```c
NODE_TEXT_AREA_TEXT_SELECTION = 8018
```

组件在获焦状态下，调用该接口设置文本选择区域并高亮显示，且只有在selectionStart小于selectionEnd时，文字才会被选取、高亮显示。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 选中文本的起始位置，取值范围[0, 文本长度]，需小于终止位置才生效。 |
| .value[1].i32 | 选中文本的终止位置，取值范围[0, 文本长度]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 选中文本的起始位置。 |
| .value[1].i32 | 选中文本的终止位置。 |

## NODE\_TEXT\_AREA\_ENABLE\_AUTO\_FILL

```c
NODE_TEXT_AREA_ENABLE_AUTO_FILL = 8019
```

设置是否启用自动填充。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否启用自动填充。  1表示启用，0表示不启用。  默认值1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否启用自动填充。1表示已启用，0表示未启用。 |

## NODE\_TEXT\_AREA\_CONTENT\_TYPE

```c
NODE_TEXT_AREA_CONTENT_TYPE = 8020
```

自动填充类型。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 参数类型[ArkUI\_TextInputContentType](capi-text-input-h.md#arkui_textinputcontenttype)。用于指定自动填充的内容类型，以便系统提供更准确的自动填充建议。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 参数类型[ArkUI\_TextInputContentType](capi-text-input-h.md#arkui_textinputcontenttype)。用于指定自动填充的内容类型，以便系统提供更准确的自动填充建议。 |

## NODE\_TEXT\_AREA\_SHOW\_KEYBOARD\_ON\_FOCUS

```c
NODE_TEXT_AREA_SHOW_KEYBOARD_ON_FOCUS = 8021
```

设置输入框获取焦点时是否弹出键盘，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 获取焦点时是否弹出键盘。  1表示弹出键盘，0表示不弹出键盘。  默认值1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 获取焦点时是否弹出键盘。1表示弹出键盘，0表示不弹出键盘。 |

## NODE\_TEXT\_AREA\_NUMBER\_OF\_LINES

```c
NODE_TEXT_AREA_NUMBER_OF_LINES = 8022
```

设置该属性后，通过该属性计算TextArea组件的高度。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 设置行数，取值范围[1, +∞)。用于通过该属性计算TextArea组件的高度。例如：设置为3时，组件将默认显示足够容纳3行文本内容的高度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 设置numberOfLines的值。 |

## NODE\_TEXT\_AREA\_LETTER\_SPACING

```c
NODE_TEXT_AREA_LETTER_SPACING = 8023
```

设置该属性后，通过该属性调整TextArea组件的字符间距。接口支持设置，重置以及获取该属性。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 设置[letterSpacing](ts-basic-components-text.md#letterspacing)的值，取值范围(-∞, +∞)，单位为fp。当取值为负值时，文字会被压缩。负值过小时会将组件内容区大小压缩为0，导致内容无法显示。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 获取[letterSpacing](ts-basic-components-text.md#letterspacing)的值，取值范围(-∞, +∞)，单位为fp。 |

## NODE\_TEXT\_AREA\_ENABLE\_PREVIEW\_TEXT

```c
NODE_TEXT_AREA_ENABLE_PREVIEW_TEXT = 8024
```

设置TextArea组件是否开启输入预上屏。接口支持设置，重置以及获取该属性。

“预上屏”描述的是一种文字暂存状态。需要在输入法中开启预上屏功能，在输入文本过程中，未确认输入候选词时，文本框中显示标记文本。例如，通过拼音输入中文时，未确定候选词之前，在输入框中显示拼音字母，该状态称为文字预上屏。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 设置是否开启输入预上屏。  0表示不开启输入预上屏，1表示开启输入预上屏。  默认值1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否开启输入预上屏。1表示已开启，0表示未开启。 |

## NODE\_TEXT\_AREA\_HALF\_LEADING

```c
NODE_TEXT_AREA_HALF_LEADING = 8025
```

设置文本将行间距平分至行的顶部与底部。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 设置文本是否将行间距平分至行的顶部与底部。  1表示将行间距平分至行的顶部与底部，0表示不平分。  默认值0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 文本行间距是否平分至行的顶部与底部。1表示平分，0表示不平分。 |

## NODE\_TEXT\_AREA\_KEYBOARD\_APPEARANCE

```c
NODE_TEXT_AREA_KEYBOARD_APPEARANCE = 8026
```

设置输入框拉起的键盘样式。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 键盘样式，参数类型[ArkUI\_KeyboardAppearance](capi-text-common-h.md#arkui_keyboardappearance)。具体枚举值请参考ArkUI\_KeyboardAppearance枚举说明。默认值ARKUI\_KEYBOARD\_APPEARANCE\_NONE\_IMMERSIVE。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 键盘样式，参数类型[ArkUI\_KeyboardAppearance](capi-text-common-h.md#arkui_keyboardappearance)。 |

## NODE\_TEXT\_AREA\_MAX\_LINES

```c
NODE_TEXT_AREA_MAX_LINES = 8027
```

设置输入框内联模式编辑态时文本可显示的最大行数，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 内联输入风格编辑态时文本可显示的最大行数。取值范围[1, +∞)。  内联模式下，默认值是3，非内联模式下，默认值是+∞，不限制最大行数。  不传入该参数时，使用默认值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 最大行数。 |

## NODE\_TEXT\_AREA\_LINE\_SPACING

```c
NODE_TEXT_AREA_LINE_SPACING = 8028
```

设置输入框文本的行间距，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 文本的行间距，取值范围[0, +∞)，单位为fp。默认值是0。超出范围时自动修正为边界值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 文本的行间距，单位fp。 |

## NODE\_TEXT\_AREA\_MIN\_LINES

```c
NODE_TEXT_AREA_MIN_LINES = 8029
```

设置节点的最小行数。支持属性设置、属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 最小行数，取值范围[1, +∞)。传入0或负数时参数不生效。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 最小行数，取值范围[1, +∞)。 |

## NODE\_TEXT\_AREA\_MAX\_LINES\_WITH\_SCROLL

```c
NODE_TEXT_AREA_MAX_LINES_WITH_SCROLL = 8030
```

设置支持滚动时节点的最大行数。支持属性设置、属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 支持滚动时的最大行数。取值范围[1, +∞)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 支持滚动时的最大行数。取值范围[1, +∞)。 |

## NODE\_TEXT\_AREA\_LINE\_HEIGHT

```c
NODE_TEXT_AREA_LINE_HEIGHT = 8031
```

设置输入框文本行高，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 文本行高。默认值是自适应字体大小，单位fp。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 文本行高，单位fp。 |

## NODE\_TEXT\_AREA\_BAR\_STATE

```c
NODE_TEXT_AREA_BAR_STATE = 8032
```

定义文本输入框滚动条状态。支持属性设置、属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 文本控制滚动条状态，具体枚举值请参考[ArkUI\_BarState](capi-scroll-h.md#arkui_barstate)。默认值为ARKUI\_BAR\_STATE\_AUTO，按需显示滚动条（在触摸时显示滚动条，2秒后自动消失）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 文本控制滚动条状态。参数类型为[ArkUI\_BarState](capi-scroll-h.md#arkui_barstate)。 |

## NODE\_TEXT\_AREA\_ENABLE\_SELECTED\_DATA\_DETECTOR

```c
NODE_TEXT_AREA_ENABLE_SELECTED_DATA_DETECTOR = 8033
```

开启选中词文本识别，支持识别选中文本中的电话号码、邮箱地址、网址链接等实体信息，便于用户快捷拨打电话、发送邮件或打开链接。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 开启选中词文本识别。1表示开启识别，0表示关闭识别。默认值：1。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否开启选中词文本识别。0表示关闭识别，1表示开启识别。 |

## NODE\_TEXT\_AREA\_SCROLL\_BAR\_COLOR

```c
NODE_TEXT_AREA_SCROLL_BAR_COLOR = 8035
```

设置输入框滚动条颜色，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .data[0].u32 | 滚动条颜色数值，0xARGB格式。默认值：0x66182431，显示为灰色。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .data[0].u32 | 滚动条颜色数值，0xARGB格式。 |

## NODE\_TEXT\_AREA\_CUSTOM\_KEYBOARD

```c
NODE_TEXT_AREA_CUSTOM_KEYBOARD = 8036
```

设置文本输入框的自定义键盘。支持属性设置、属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 自定义键盘，参数类型[ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)。 |
| .value[0]?.i32 | 设置自定义键盘是否支持避让功能。  1表示支持避让，0表示不支持避让。  默认值：0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .object | 自定义键盘，参数类型[ArkUI\_NodeHandle](capi-arkui-nativemodule-arkui-node8h.md)。 |
| .value[0].i32 | 自定义键盘是否支持避让功能。1表示支持避让，0表示不支持避让。 |

## NODE\_TEXT\_AREA\_TEXT\_CONTENT\_CONTROLLER\_BASE

```c
NODE_TEXT_AREA_TEXT_CONTENT_CONTROLLER_BASE = 8037
```

用于设置或获取文本区域控制器。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 文本内容基础控制器，参数类型为[ArkUI\_TextContentBaseController](capi-arkui-nativemodule-arkui-textcontentbasecontroller.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .object | 文本内容基础控制器，参数类型为[ArkUI\_TextContentBaseController](capi-arkui-nativemodule-arkui-textcontentbasecontroller.md)。 |

## NODE\_TEXT\_AREA\_ELLIPSIS\_MODE

```c
NODE_TEXT_AREA_ELLIPSIS_MODE = 8038
```

设置多行文本输入框中文本省略位置，支持属性设置，属性重置，属性获取接口。

此属性存在以下配置依赖：

* 此属性只有在NODE\_TEXT\_AREA\_TEXT\_OVERFLOW设置为ARKUI\_TEXT\_OVERFLOW\_ELLIPSIS时才生效
* 当TEXT\_OVERFLOW设置为ARKUI\_TEXT\_OVERFLOW\_CLIP时，ELLIPSIS\_MODE的设置不会生效
* 建议先设置TEXT\_OVERFLOW为ELLIPSIS，再设置ELLIPSIS\_MODE指定省略位置

  作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 参数类型[ArkUI\_EllipsisMode](capi-text-common-h.md#arkui_ellipsismode)。具体枚举值请参考ArkUI\_EllipsisMode枚举说明。默认值为ARKUI\_ELLIPSIS\_MODE\_END。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 文本省略位置枚举[ArkUI\_EllipsisMode](capi-text-common-h.md#arkui_ellipsismode)，用于确定文本超长时的省略位置。 |

## NODE\_TEXT\_AREA\_ORPHAN\_CHAR\_OPTIMIZATION

```c
NODE_TEXT_AREA_ORPHAN_CHAR_OPTIMIZATION = 8039
```

设置TextArea文本排版时是否使能孤字优化，设置后通过更高效地处理孤立字符（段落尾行首字符）来改善文本布局。使能后，它会调整换行点以尽可能避免孤立字符。孤字优化特性需在[ArkUI\_WordBreak](capi-text-common-h.md#arkui_wordbreak)属性为非ARKUI\_WORD\_BREAK\_BREAK\_ALL时生效。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否使能孤字优化。该特性需在[ArkUI\_WordBreak](capi-text-common-h.md#arkui_wordbreak)属性为非ARKUI\_WORD\_BREAK\_BREAK\_ALL时生效。1表示使能，0表示不使能。默认值0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否使能孤字优化。1表示已使能，0表示未使能。 |

## NODE\_TEXT\_AREA\_COMPRESS\_LEADING\_PUNCTUATION

```c
NODE_TEXT_AREA_COMPRESS_LEADING_PUNCTUATION = 8040
```

设置输入字符行首标点压缩开关，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否打开行首标点压缩开关。  1表示开启行首标点压缩，0表示关闭行首标点压缩。默认值0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 行首标点压缩开关状态。1表示已开启，0表示已关闭。 |

## NODE\_TEXT\_AREA\_INCLUDE\_FONT\_PADDING

```c
NODE_TEXT_AREA_INCLUDE_FONT_PADDING = 8041
```

设置多行输入框内文字是否在首行和尾行增加间距以避免文字截断。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 设置输入框内文字是否在首行和尾行增加间距以避免文字截断。1表示开启增加间距，0表示关闭增加间距。默认值0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 输入框内文字是否在首行和尾行增加间距。0表示不增加间距，1表示增加间距。 |

## NODE\_TEXT\_AREA\_FALLBACK\_LINE\_SPACING

```c
NODE_TEXT_AREA_FALLBACK_LINE_SPACING = 8042
```

针对多行文本显示场景，支持行高基于文字实际高度自适应。此接口仅当行高小于文字实际高度时生效。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 支持行高基于文字实际高度自适应。此接口仅当行高小于文字实际高度时生效。1表示开启自适应，0表示关闭自适应。默认值0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否开启行高基于文字实际高度自适应。0表示关闭自适应，1表示开启自适应。 |

## NODE\_TEXT\_AREA\_HORIZONTAL\_SCROLLING

```c
NODE_TEXT_AREA_HORIZONTAL_SCROLLING = 8043
```

设置多行输入框在文本宽度超过输入框内容区宽度时是否启用水平滚动。默认不启用水平滚动，文本会被输入框自动换行。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否启用水平滚动。1表示启用水平滚动，0表示不启用水平滚动。默认值0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否启用水平滚动。1表示已启用，0表示未启用。 |

## NODE\_TEXT\_AREA\_DIRECTION

```c
NODE_TEXT_AREA_DIRECTION = 8044
```

多行输入框的文本排版方向。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 表示文本的排版方向，取[ArkUI\_TextDirection](capi-text-common-h.md#arkui_textdirection)枚举值。默认值为ARKUI\_TEXT\_DIRECTION\_DEFAULT。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 表示文本的排版方向，对应取值及含义请参考[ArkUI\_TextDirection](capi-text-common-h.md#arkui_textdirection)枚举值。 |

## NODE\_TEXT\_AREA\_SELECTED\_DRAG\_PREVIEW\_STYLE

```c
NODE_TEXT_AREA_SELECTED_DRAG_PREVIEW_STYLE = 8045
```

用于设置多行文本输入框内文本选中状态下的拖拽预览样式。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 文本选中状态下的拖拽预览样式。参数类型为[ArkUI\_SelectedDragPreviewStyle](capi-arkui-nativemodule-arkui-textselecteddragpreviewstyle.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .object | 文本选中状态下的拖拽预览样式。参数类型为[ArkUI\_SelectedDragPreviewStyle](capi-arkui-nativemodule-arkui-textselecteddragpreviewstyle.md)。 |

## NODE\_TEXT\_AREA\_TEXT\_OVERFLOW

```c
NODE_TEXT_AREA_TEXT_OVERFLOW = 8046
```

多行文本输入框中文本超长时的显示方式属性，支持属性设置，属性重置，属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 表示文本超长时的显示方式[ArkUI\_TextOverflow](capi-text-common-h.md#arkui_textoverflow)。默认值为ARKUI\_TEXT\_OVERFLOW\_CLIP。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 表示文本超长时的显示方式[ArkUI\_TextOverflow](capi-text-common-h.md#arkui_textoverflow)。 |

## NODE\_TEXT\_AREA\_DECORATION

```c
NODE_TEXT_AREA_DECORATION = 8047
```

定义多行输入框的文本装饰线样式与颜色，支持属性设置、属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .object | 装饰样式配置项，为可选参数。参数类型为[OH\_ArkUI\_DecorationStyleOptions](capi-arkui-nativemodule-oh-arkui-decorationstyleoptions.md)。不传入时不添加装饰线。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .object | 装饰样式配置项。参数类型为[OH\_ArkUI\_DecorationStyleOptions](capi-arkui-nativemodule-oh-arkui-decorationstyleoptions.md)。 |

## NODE\_TEXT\_AREA\_LINEAR\_GRADIENT

```c
NODE_TEXT_AREA_LINEAR_GRADIENT = 8048
```

设置多行文本输入框的文本线性渐变效果，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].f32 | 线性渐变的起始角度，单位为deg。当线性渐变的方向为[ArkUI\_LinearGradientDirection](capi-native-type-visual-h.md#arkui_lineargradientdirection)的ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_CUSTOM时，线性渐变的起始角度属性生效，否则按线性渐变的方向属性为主要布局方式。取值范围为(-∞,+∞)，0点方向顺时针旋转为正向角度，当超过360时，是按照360取余处理，默认值：180。 |
| .value[1].i32 | 线性渐变的方向。取值为[ArkUI\_LinearGradientDirection](capi-native-type-visual-h.md#arkui_lineargradientdirection)中的枚举。设置除[ArkUI\_LinearGradientDirection](capi-native-type-visual-h.md#arkui_lineargradientdirection)的ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_CUSTOM之外的线性渐变方向后，线性渐变的起始角度不生效。默认值：[ArkUI\_LinearGradientDirection](capi-native-type-visual-h.md#arkui_lineargradientdirection)的ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_LEFT\_BOTTOM |
| .value[2].i32 | 渐变的颜色是否重复着色，0表示不重复着色，1表示重复着色。默认值：0。 |
| .object | 指定位置处的渐变色颜色。参数类型为[ArkUI\_ColorStop](capi-arkui-nativemodule-arkui-colorstop.md)。  colors：渐变色颜色数组，数组元素为0xARGB格式，形如0xFFFF0000表示红色。  stops：stops表示指定颜色所处位置的数组，数组元素取值范围为[0,1.0]，0表示需要设置渐变色的容器的开始处，1.0表示容器的结尾处。想要实现多个颜色渐变效果时，数组元素建议递增设置，如后一个数组元素比前一个数组元素小的话，按照等于前一个数组元素的值处理。  size：颜色个数，若小于colors数组长度则仅生效前size个颜色，不建议设置大于colors数组长度或小于等于0的值以及异常值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].f32 | 线性渐变的起始角度，单位为deg。当线性渐变的方向为[ArkUI\_LinearGradientDirection](capi-native-type-visual-h.md#arkui_lineargradientdirection)的ARKUI\_LINEAR\_GRADIENT\_DIRECTION\_CUSTOM时，线性渐变的起始角度为设置值，其他情况均为默认值0。 |
| .value[1].i32 | 线性渐变的方向。对应取值及含义请参考[ArkUI\_LinearGradientDirection](capi-native-type-visual-h.md#arkui_lineargradientdirection)。 |
| .value[2].i32 | 渐变的颜色是否重复着色，0表示不重复着色，1表示重复着色。默认值：0。 |
| .object | 指定位置处的渐变色颜色。参数类型为[ArkUI\_ColorStop](capi-arkui-nativemodule-arkui-colorstop.md)。  colors：渐变色颜色数组，数组元素为0xARGB格式，形如0xFFFF0000表示红色。  stops：stops表示指定颜色所处位置的数组，数组元素取值范围为[0,1.0]，0表示需要设置渐变色的容器的开始处，1.0表示容器的结尾处。  size：生效后渐变色的颜色个数。 |

## NODE\_TEXT\_AREA\_RADIAL\_GRADIENT

```c
NODE_TEXT_AREA_RADIAL_GRADIENT = 8049
```

设置多行文本输入框的文本径向渐变效果，支持属性设置，属性重置和属性获取接口。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0]?.f32 | 径向渐变的中心点X轴坐标，即相对于当前多行输入框左上角的X轴坐标，单位为vp。默认值为多行输入框宽度的一半。 |
| .value[1]?.f32 | 径向渐变的中心点Y轴坐标，即相对于当前多行输入框左上角的Y轴坐标，单位为vp。默认值为多行输入框高度的一半。 |
| .value[2]?.f32 | 径向渐变的半径，取值范围[0, +∞)，默认值0。传入负数时不生效。 |
| .value[3]?.i32 | 渐变的颜色是否重复着色，0表示不重复着色，1表示重复着色。默认值：0。 |
| .object | 指定位置处的渐变色颜色。参数类型为[ArkUI\_ColorStop](capi-arkui-nativemodule-arkui-colorstop.md)。  colors：渐变色颜色数组，数组元素为0xARGB格式，形如0xFFFF0000表示红色。  stops：stops表示指定颜色所处位置的数组，数组元素取值范围为[0,1.0]，0表示需要设置渐变色的容器的开始处，1.0表示容器的结尾处。想要实现多个颜色渐变效果时，数组元素建议递增设置，如后一个数组元素比前一个数组元素小的话，按照等于前一个数组元素的值处理。  size：颜色个数，若小于colors数组长度则仅生效前size个颜色，不建议设置大于colors数组长度或小于等于0的值以及异常值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0]?.f32 | 径向渐变的中心点X轴坐标，即相对于当前多行输入框左上角的X轴坐标，单位为vp。 |
| .value[1]?.f32 | 径向渐变的中心点Y轴坐标，即相对于当前多行输入框左上角的Y轴坐标，单位为vp。 |
| .value[2]?.f32 | 径向渐变的半径，单位为vp，默认值0。 |
| .value[3]?.i32 | 渐变的颜色是否重复着色，0表示不重复着色，1表示重复着色。默认值：0。 |
| .object | 指定位置处的渐变色颜色。参数类型为[ArkUI\_ColorStop](capi-arkui-nativemodule-arkui-colorstop.md)。  colors：渐变色颜色数组，数组元素为0xARGB格式，形如0xFFFF0000表示红色。  stops：stops表示指定颜色所处位置的数组，数组元素取值范围为[0,1.0]，0表示需要设置渐变色的容器的开始处，1.0表示容器的结尾处。  size：生效后渐变色的颜色个数。 |

## NODE\_TEXT\_AREA\_PUNCTUATION\_OVERFLOW

```c
NODE_TEXT_AREA_PUNCTUATION_OVERFLOW = 8050
```

设置TextArea组件是否启用行尾标点符号悬挂，支持属性设置，属性重置和属性获取。

作为属性设置方法参数、属性获取方法返回值[ArkUI\_AttributeItem](capi-arkui-nativemodule-arkui-attributeitem.md)格式如下。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| .value[0].i32 | 是否启用行尾标点符号悬挂。1表示启用标点符号悬挂，0表示不启用标点符号悬挂。默认值0。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| .value[0].i32 | 是否启用行尾标点符号悬挂。1表示已启用，0表示未启用。 |
