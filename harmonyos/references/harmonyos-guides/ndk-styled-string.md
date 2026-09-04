---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-styled-string
title: 使用属性字符串
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (基于NDK构建UI) > 使用文本 > 使用属性字符串
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:05+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:88f57bfbd451ad9fc11f857912c5a838340164515d7ac2c20e7043e40d1066e2
---

部分框架或应用具备自研的文字排版能力，在移植时，其文字排版能力会被对接到[方舟2D图形服务的文本引擎](complex-text-c.md)。为了避免开发者重复开发文本组件，Text组件可以通过[ArkUI\_NodeAttributeType](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)中的NODE\_TEXT\_CONTENT\_WITH\_STYLED\_STRING属性，使用格式化字符串对象设置文本内容属性，直接渲染方舟文本引擎生成的文本。

**说明** 

* 本篇示例仅提供核心接口的调用方法，完整的示例工程请参考[StyledStringSample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/StyledStringSample)。

以下示例代码基于[接入ArkTS页面章节](ndk-access-the-arkts-page.md)，阐述了如何创建StyledString，并利用[ArkUI\_NodeType](../harmonyos-references/capi-native-node-h.md#arkui_nodetype)为ARKUI\_NODE\_TEXT的组件进行渲染显示。

下图展示了 NODE\_TEXT\_CONTENT\_WITH\_STYLED\_STRING 接口的主要使用流程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/MFfbglqJQ2GhZpFGuvfUcw/zh-cn_image_0000002742003087.png)

## 创建StyledString对象

使用[OH\_ArkUI\_StyledString\_Create](../harmonyos-references/capi-styled-string-h.md#oh_arkui_styledstring_create)接口创建StyledString对象，需要传入[段落样式](ndk-styled-string.md#设置段落样式)和字体集合。

```
// 创建StyledString对象
ArkUI_StyledString *styledString = OH_ArkUI_StyledString_Create(typographyStyle, fontCollection);
```

## 通过StyledString设置样式

StyledString支持为文本中的不同部分设置不同的样式，包括段落样式和文本样式。

### 设置段落样式

通过如下接口可以设置StyledString的段落样式属性，包括最大行数、对齐方式等。

**说明** 

StyledString需要依赖OH\_Drawing\_前缀的方舟字体引擎接口进行字体以及段落样式的设置，参考[简单文本绘制与显示（C/C++）](simple-text-c.md)、[复杂文本绘制与显示（C/C++）](complex-text-c.md)。涉及字体引擎的接口，需在CMakeLists.txt中添加target\_link\_libraries(entry PUBLIC libnative\_drawing.so)，否则链接阶段会报错。

**表1** 段落样式设置接口

| 接口 | 描述 |
| --- | --- |
| [OH\_Drawing\_CreateFontCollection](../harmonyos-references/capi-drawing-font-collection-h.md#oh_drawing_createfontcollection) | 创建字体集对象。 |
| [OH\_Drawing\_CreateTypographyStyle](../harmonyos-references/capi-drawing-text-typography-h.md#oh_drawing_createtypographystyle) | 创建段落样式对象。 |
| [OH\_Drawing\_SetTypographyTextAlign](../harmonyos-references/capi-drawing-text-typography-h.md#oh_drawing_settypographytextalign) | 设置文本对齐方式。 |
| [OH\_Drawing\_SetTypographyTextMaxLines](../harmonyos-references/capi-drawing-text-typography-h.md#oh_drawing_settypographytextmaxlines) | 设置文本最大行数。 |

以下代码示例设置了文字居中，最大行数限制为10。

```
// 创建字体集合与段落样式，并设置对齐方式和最大行数
OH_Drawing_FontCollection *fontCollection = OH_Drawing_CreateFontCollection();
OH_Drawing_TypographyStyle *typographyStyle = OH_Drawing_CreateTypographyStyle();
OH_Drawing_SetTypographyTextAlign(typographyStyle, OH_Drawing_TextAlign::TEXT_ALIGN_CENTER);
OH_Drawing_SetTypographyTextMaxLines(typographyStyle, NUM_10);
```

### 设置文本样式

不同内容的文本可以通过StyledString设置不同的文本样式，但必须按照以下三个接口的逻辑调用顺序进行设置，否则将无法生效。

1. [OH\_ArkUI\_StyledString\_PushTextStyle](../harmonyos-references/capi-styled-string-h.md#oh_arkui_styledstring_pushtextstyle)：将文字样式推入栈中。
2. [OH\_ArkUI\_StyledString\_AddText](../harmonyos-references/capi-styled-string-h.md#oh_arkui_styledstring_addtext)：添加要修改样式的文字内容。
3. [OH\_ArkUI\_StyledString\_PopTextStyle](../harmonyos-references/capi-styled-string-h.md#oh_arkui_styledstring_poptextstyle)：将文字样式弹出栈。

**表2** 文本样式设置接口

| 接口 | 描述 |
| --- | --- |
| [OH\_Drawing\_CreateTextStyle](../harmonyos-references/capi-drawing-text-typography-h.md#oh_drawing_createtextstyle) | 创建文本样式对象。 |
| [OH\_Drawing\_SetTextStyleFontSize](../harmonyos-references/capi-drawing-text-typography-h.md#oh_drawing_settextstylefontsize) | 设置字体大小。 |
| [OH\_Drawing\_SetTextStyleColor](../harmonyos-references/capi-drawing-text-typography-h.md#oh_drawing_settextstylecolor) | 设置字体颜色。 |

使用[OH\_Drawing\_CreateTextStyle](../harmonyos-references/capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)创建文本样式。以下示例设置"Hello"字体大小28px，颜色为0xFF707070，显示为灰色；设置"World!"字体大小为28px，颜色为0xFF2787D9，显示为蓝色。

```
// 第一段文本（灰色"Hello"）
OH_Drawing_TextStyle *textStyle = OH_Drawing_CreateTextStyle();
OH_Drawing_SetTextStyleFontSize(textStyle, FONT_SIZE);
OH_Drawing_SetTextStyleColor(textStyle, TEXT_COLOR_GRAY);
OH_ArkUI_StyledString_PushTextStyle(styledString, textStyle);
OH_ArkUI_StyledString_AddText(styledString, "Hello");
OH_ArkUI_StyledString_PopTextStyle(styledString);
```

```
// 第二段文本（蓝色"World!"）
OH_Drawing_TextStyle *worldTextStyle = OH_Drawing_CreateTextStyle();
OH_Drawing_SetTextStyleFontSize(worldTextStyle, FONT_SIZE);
OH_Drawing_SetTextStyleColor(worldTextStyle, TEXT_COLOR_BLUE);
OH_ArkUI_StyledString_PushTextStyle(styledString, worldTextStyle);
OH_ArkUI_StyledString_AddText(styledString, "World!");
OH_ArkUI_StyledString_PopTextStyle(styledString);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/Z2Za7ovYRB2-qsPTLgYnzQ/zh-cn_image_0000002712404100.png)

## 添加占位符

占位符功能主要用于图文混排场景，可以在文本中插入指定大小的空白区域，用于挂载Image组件或其他自定义内容。

使用[OH\_ArkUI\_StyledString\_AddPlaceholder](../harmonyos-references/capi-styled-string-h.md#oh_arkui_styledstring_addplaceholder)接口在文本中插入占位符。

```
// 添加占位符
OH_Drawing_PlaceholderSpan placeHolder{.width = PLACEHOLDER_WIDTH, .height = PLACEHOLDER_HEIGHT};
OH_ArkUI_StyledString_AddPlaceholder(styledString, &placeHolder);
```

## 布局与绘制

StyledString在设置到Text组件之前，需要先完成布局计算，然后再进行渲染。

文字样式和内容设置完成后，调用字体引擎接口[OH\_Drawing\_TypographyLayout](../harmonyos-references/capi-drawing-text-typography-h.md#oh_drawing_typographylayout)对文本进行布局，传入最大宽度。超过此宽度的文字会自动换行。

```
OH_Drawing_Typography *typography = OH_ArkUI_StyledString_CreateTypography(styledString);
OH_Drawing_TypographyLayout(typography, LAYOUT_MAX_WIDTH);
// 布局完成后，将StyledString设置给Text组件
ArkUI_AttributeItem styledStringItem = {.object = styledString};
nodeApi->setAttribute(text, NODE_TEXT_CONTENT_WITH_STYLED_STRING, &styledStringItem);
```

## 序列化与反序列化

从API version 14开始，StyledString提供了序列化和反序列化功能，支持将字节数据反序列化为描述符，或将描述符转换为HTML格式，便于数据的存储、传输和跨平台使用。

**表3** 序列化与反序列化接口

| 接口 | 描述 |
| --- | --- |
| [OH\_ArkUI\_StyledString\_Descriptor\_Create](../harmonyos-references/capi-styled-string-h.md#oh_arkui_styledstring_descriptor_create) | 创建StyledString描述符。 |
| [OH\_ArkUI\_UnmarshallStyledStringDescriptor](../harmonyos-references/capi-styled-string-h.md#oh_arkui_unmarshallstyledstringdescriptor) | 反序列化字节数据到描述符。 |
| [OH\_ArkUI\_ConvertToHtml](../harmonyos-references/capi-styled-string-h.md#oh_arkui_converttohtml) | 将描述符转换为HTML格式。 |
| [OH\_ArkUI\_StyledString\_Descriptor\_Destroy](../harmonyos-references/capi-styled-string-h.md#oh_arkui_styledstring_descriptor_destroy) | 销毁StyledString描述符。 |

以下示例展示了如何创建描述符、反序列化字节数据、转换为HTML并进行验证。

```
static void SerializeAndDeserializeStyledString()
{
    // 准备测试数据
    uint8_t data_bytes[] = {0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08};
    size_t dataSize = sizeof(data_bytes) / sizeof(data_bytes[0]);

    // 创建StyledString描述符
    auto desc = OH_ArkUI_StyledString_Descriptor_Create();
    if (desc == nullptr) {
        OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "styledString", "Create Descriptor failed");
        return;
    }

    // 反序列化字节数据
    auto status = OH_ArkUI_UnmarshallStyledStringDescriptor(data_bytes, dataSize, desc);
    OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "styledString", "Unmarshall status: %{public}d", status);

    // 转换为HTML格式
    const char* html = OH_ArkUI_ConvertToHtml(desc);
    OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "styledString", "html: [%{public}s]", html);
    size_t resultSize = dataSize + 2;
    OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "styledString", "resultSize: %{public}zu", resultSize);
    uint8_t *buf2 = (uint8_t *)malloc(resultSize * sizeof(uint8_t));

    // 验证反序列化后的数据
    if (buf2 != nullptr) {
        if (resultSize >= dataSize) {
            for (size_t i = 0; i < dataSize; i++) {
                buf2[i] = data_bytes[i];
            }
        } else {
            OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_PRINT_DOMAIN, "styledString",
                         "Buf too small: %{public}zu < %{public}zu", resultSize, dataSize);
            free(buf2);
            OH_ArkUI_StyledString_Descriptor_Destroy(desc);
            return;
        }
        bool equal = true;
        for (size_t i = 0; i < dataSize && equal; i++) equal = (data_bytes[i] == buf2[i]);
        OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "styledString",
            "Before: %{public}zu, After: %{public}zu, Equal: %{public}d", dataSize, resultSize, equal);
        free(buf2);
    }

    // 释放描述符
    OH_ArkUI_StyledString_Descriptor_Destroy(desc);
}
```

## 销毁对象

Text组件不对本文涉及的任何对象的生命周期进行管理，需由开发者自行负责。字体引擎接口均配有相应的销毁方法。

OH\_Drawing\_DestroyTextStyle(OH\_Drawing\_TextStyle \*style)：销毁文本样式对象。

OH\_Drawing\_DestroyTypographyStyle(OH\_Drawing\_TypographyStyle \*style)：销毁段落样式对象。

当Text组件仍在界面上显示时，此时释放会导致文字无法绘制。在实际业务场景下需确保Text组件不再使用时才释放。

相关字体引擎销毁的接口请参考[OH\_Drawing\_DestroyTextStyle](../harmonyos-references/capi-drawing-text-typography-h.md#oh_drawing_destroytextstyle) 和 [OH\_Drawing\_DestroyTypographyStyle](../harmonyos-references/capi-drawing-text-typography-h.md#oh_drawing_destroytypographystyle)。

Text组件提供[OH\_ArkUI\_StyledString\_Destroy](../harmonyos-references/capi-styled-string-h.md#oh_arkui_styledstring_destroy)，用于销毁属性字符串对象。
