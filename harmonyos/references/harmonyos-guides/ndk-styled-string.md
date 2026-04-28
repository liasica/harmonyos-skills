---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-styled-string
title: Text组件的文本绘制与显示
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (基于NDK构建UI) > 使用文本 > Text组件的文本绘制与显示
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:95072568682a1a1abb99e87df618b6ed9a650739de489f2ed40dc66b657aa6a4
---

部分框架或应用具备自研的文字排版能力，在移植时，这些能力会被对接到[方舟2D图形服务的文本引擎](complex-text-c.md)。为了避免开发者重复开发文本组件，Text组件提供了接口[NODE\_TEXT\_CONTENT\_WITH\_STYLED\_STRING](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)，可以直接渲染方舟文本引擎生成的文本。

以下场景基于[接入ArkTS页面章节](ndk-access-the-arkts-page.md)，阐述了如何创建字体引擎文本，并利用[Text组件](../harmonyos-references/capi-native-node-h.md#arkui_nodetype)进行渲染显示。

说明

涉及字体引擎的接口，需在CMakeLists.txt中添加target\_link\_libraries(entry PUBLIC libnative\_drawing.so)，否则链接阶段会报错。

下图展示了 NODE\_TEXT\_CONTENT\_WITH\_STYLED\_STRING 接口的主要使用流程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/KegUbg0nQs6JzROQ0JXTZw/zh-cn_image_0000002552958066.png?HW-CC-KV=V1&HW-CC-Date=20260427T234015Z&HW-CC-Expire=86400&HW-CC-Sign=138CFB5CEEA0AE23EB2C20186061369326B6AA1875AC02F91870270C1840DF37)

## 创建Text组件

创建文本组件时，无需配置文字颜色、字体大小等样式属性，因为这些属性通过字体引擎接口设置。但仍需设置基础的[通用属性](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)，如宽度和高度。如果不指定，组件自动适应文本的宽度和高度。

```
1. ArkUI_NativeNodeAPI_1 *nodeApi = reinterpret_cast<ArkUI_NativeNodeAPI_1 *>(
2. OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_NODE, "ArkUI_NativeNodeAPI_1"));
3. if (nodeApi == nullptr) {
4. return;
5. }
6. // ···
7. // 创建Text组件
8. ArkUI_NodeHandle text = nodeApi->createNode(ARKUI_NODE_TEXT);
9. ArkUI_NumberValue textWidth[] = {{.f32 = 300}};
10. ArkUI_AttributeItem textWidthItem = {.value = textWidth, .size = 1};
11. nodeApi->setAttribute(text, NODE_WIDTH, &textWidthItem);
12. ArkUI_NumberValue textHeight[] = {{.f32 = 100}};
13. ArkUI_AttributeItem textHeightItem = {.value = textHeight, .size = 1};
14. nodeApi->setAttribute(text, NODE_HEIGHT, &textHeightItem);
```

[manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/StyledStringNDK/entry/src/main/cpp/manager.cpp#L47-L68)

## 设置段落与文本样式

* 设置段落样式

  段落样式定义了一段文字的整体属性，例如最大显示行数、文字方向等。以下代码示例设置了文字居中，最大行数限制为10。

  说明

  OH\_Drawing\_前缀的接口由方舟字体引擎提供，参考[简单文本绘制与显示（C/C++)](simple-text-c.md)、[复杂文本绘制与显示（C/C++）](complex-text-c.md)。

  ```
  1. OH_Drawing_TypographyStyle *typographyStyle = OH_Drawing_CreateTypographyStyle();
  2. OH_Drawing_SetTypographyTextAlign(typographyStyle, OH_Drawing_TextAlign::TEXT_ALIGN_CENTER);
  3. OH_Drawing_SetTypographyTextMaxLines(typographyStyle, NUM_10);
  ```
* 设置文本样式

  不同内容的文本可以设置不同的文本样式，但必须按照以下三个接口的逻辑调用顺序进行设置，否则将无法生效。

  1. [OH\_ArkUI\_StyledString\_PushTextStyle](../harmonyos-references/capi-styled-string-h.md#oh_arkui_styledstring_pushtextstyle)：将文字样式推入栈中。
  2. [OH\_ArkUI\_StyledString\_AddText](../harmonyos-references/capi-styled-string-h.md#oh_arkui_styledstring_addtext)：添加要修改样式的文字内容。
  3. [OH\_ArkUI\_StyledString\_PopTextStyle](../harmonyos-references/capi-styled-string-h.md#oh_arkui_styledstring_poptextstyle)：将文字样式弹出栈。

  说明

  OH\_ArkUI\_StyledString\_前缀的接口由Text组件提供。

  OH\_Drawing\_前缀的接口由方舟字体引擎提供，参考[简单文本绘制与显示（C/C++)](simple-text-c.md)、[复杂文本绘制与显示（C/C++）](complex-text-c.md)。

  [OH\_Drawing\_CreateTextStyle](../harmonyos-references/capi-drawing-text-typography-h.md#oh_drawing_createtextstyle)创建文本样式。设置“Hello”字体大小28px，颜色为0xFF707070。设置“World!”字体大小为28px，颜色为0xFF2787D9。

  ```
  1. ArkUI_StyledString *styledString = OH_ArkUI_StyledString_Create(typographyStyle, OH_Drawing_CreateFontCollection());
  2. // 创建文本样式，设置字体和颜色。
  3. OH_Drawing_TextStyle *textStyle = OH_Drawing_CreateTextStyle();
  4. OH_Drawing_SetTextStyleFontSize(textStyle, NUM_28);
  5. OH_Drawing_SetTextStyleColor(textStyle, OH_Drawing_ColorSetArgb(0xFF, 0x70, 0x70, 0x70));
  6. // 文本样式的设置顺序push -> add -> pop.
  7. OH_ArkUI_StyledString_PushTextStyle(styledString, textStyle);
  8. OH_ArkUI_StyledString_AddText(styledString, "Hello");
  9. OH_ArkUI_StyledString_PopTextStyle(styledString);
  10. // ···
  11. // 设置不同样式的文字
  12. OH_Drawing_TextStyle *worldTextStyle = OH_Drawing_CreateTextStyle();
  13. OH_Drawing_SetTextStyleFontSize(worldTextStyle, NUM_28);
  14. OH_Drawing_SetTextStyleColor(worldTextStyle, OH_Drawing_ColorSetArgb(0xFF, 0x27, 0x87, 0xD9));
  15. OH_ArkUI_StyledString_PushTextStyle(styledString, worldTextStyle);
  16. OH_ArkUI_StyledString_AddText(styledString, "World!");
  17. OH_ArkUI_StyledString_PopTextStyle(styledString);
  ```

## 添加占位

占位保留指定大小的空白区域，此区域不绘制文字，但参与布局测量，影响文字排版。

行高是文字高度与占位高度中的较大值。

以下示例展示在Hello与World!中间插入占位。

```
1. OH_Drawing_TextStyle *textStyle = OH_Drawing_CreateTextStyle();
2. OH_Drawing_SetTextStyleFontSize(textStyle, NUM_28);
3. OH_Drawing_SetTextStyleColor(textStyle, OH_Drawing_ColorSetArgb(0xFF, 0x70, 0x70, 0x70));
4. // 文本样式的设置顺序push -> add -> pop.
5. OH_ArkUI_StyledString_PushTextStyle(styledString, textStyle);
6. OH_ArkUI_StyledString_AddText(styledString, "Hello");
7. OH_ArkUI_StyledString_PopTextStyle(styledString);
8. // 添加占位，此区域内不会绘制文字，可以在此位置挂载Image组件实现图文混排。
9. OH_Drawing_PlaceholderSpan placeHolder{.width = 100, .height = 100};
10. OH_ArkUI_StyledString_AddPlaceholder(styledString, &placeHolder);
11. // 设置不同样式的文字
12. OH_Drawing_TextStyle *worldTextStyle = OH_Drawing_CreateTextStyle();
13. OH_Drawing_SetTextStyleFontSize(worldTextStyle, NUM_28);
14. OH_Drawing_SetTextStyleColor(worldTextStyle, OH_Drawing_ColorSetArgb(0xFF, 0x27, 0x87, 0xD9));
15. OH_ArkUI_StyledString_PushTextStyle(styledString, worldTextStyle);
16. OH_ArkUI_StyledString_AddText(styledString, "World!");
17. OH_ArkUI_StyledString_PopTextStyle(styledString);
```

[manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/StyledStringNDK/entry/src/main/cpp/manager.cpp#L83-L103)

## 文本布局与绘制

* 文本布局

  文字样式和内容设置完成后，调用字体引擎接口[OH\_Drawing\_TypographyLayout](../harmonyos-references/capi-drawing-text-typography-h.md#oh_drawing_typographylayout)对文本进行布局，传入最大宽度。超过此宽度的文字会自动换行。

  说明

  未经过布局的文本无法显示。

  ```
  1. OH_Drawing_Typography *typography = OH_ArkUI_StyledString_CreateTypography(styledString);
  2. // 字体引擎布局方法，需传入一个宽度，此宽度需与Text组件宽度匹配。
  3. // 布局宽度 = Text组件宽度 - (左padding + 右padding)
  4. OH_Drawing_TypographyLayout(typography, NUM_400);
  ```

  [manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/StyledStringNDK/entry/src/main/cpp/manager.cpp#L106-L111)
* 文本绘制

  文本绘制由字体引擎与图形交互完成，无需额外设置。Text组件会在ArkUI渲染机制下，在组件触发绘制时调用字体引擎绘制接口。此处仅需将已创建的StyledString对象传递给已创建的Text组件。

  ```
  1. ArkUI_AttributeItem styledStringItem = {.object = styledString};
  2. // 布局完成后，通过NODE_TEXT_CONTENT_WITH_STYLED_STRING设置给Text组件。
  3. nodeApi->setAttribute(text, NODE_TEXT_CONTENT_WITH_STYLED_STRING, &styledStringItem);
  ```

  [manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/StyledStringNDK/entry/src/main/cpp/manager.cpp#L112-L116)

## 销毁对象

Text组件不对本文涉及的任何对象的生命周期进行管理，需由开发者自行负责。字体引擎接口均配有相应的销毁方法。

OH\_Drawing\_DestroyTextStyle(OH\_Drawing\_TextStyle \*style)：销毁文本样式对象。

OH\_Drawing\_DestroyTypographyStyle(OH\_Drawing\_TypographyStyle \*style)：销毁段落样式对象。

当Text组件仍在界面上显示时，此时释放会导致文字无法绘制。在实际业务场景下需确保Text组件不再使用时才释放。

相关字体引擎销毁的接口请参考[OH\_Drawing\_DestroyTextStyle](../harmonyos-references/capi-drawing-text-typography-h.md#oh_drawing_destroytextstyle) 和 [OH\_Drawing\_DestroyTypographyStyle](../harmonyos-references/capi-drawing-text-typography-h.md#oh_drawing_destroytypographystyle)。

Text组件提供[OH\_ArkUI\_StyledString\_Destroy](../harmonyos-references/capi-styled-string-h.md#oh_arkui_styledstring_destroy)，用于销毁属性字符串对象。

## 完整示例

本篇示例仅提供核心接口的调用方法，完整的示例工程请参考[StyledStringNDK](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/StyledStringNDK)。

```
1. #include "manager.h"
2. #include <sstream>
3. #include <arkui/native_interface.h>
4. #include <arkui/styled_string.h>
5. // ···
6. #include <native_drawing/drawing_font_collection.h>
7. #include <native_drawing/drawing_text_declaration.h>

9. namespace NativeNode::Manager {
10. constexpr int32_t NUM_10 = 10;
11. constexpr int32_t NUM_28 = 28;
12. constexpr int32_t NUM_400 = 400;
13. // ···
14. void NodeManager::CreateNativeNode()
15. {
16. // ···
17. ArkUI_NativeNodeAPI_1 *nodeApi = reinterpret_cast<ArkUI_NativeNodeAPI_1 *>(
18. OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_NODE, "ArkUI_NativeNodeAPI_1"));
19. if (nodeApi == nullptr) {
20. return;
21. }
22. // 创建一个Column容器组件
23. ArkUI_NodeHandle column = nodeApi->createNode(ARKUI_NODE_COLUMN);
24. ArkUI_NumberValue colWidth[] = {{.f32 = 300}};
25. ArkUI_AttributeItem widthItem = {.value = colWidth, .size = 1};
26. nodeApi->setAttribute(column, NODE_WIDTH, &widthItem);
27. // 创建Text组件
28. ArkUI_NodeHandle text = nodeApi->createNode(ARKUI_NODE_TEXT);
29. ArkUI_NumberValue textWidth[] = {{.f32 = 300}};
30. ArkUI_AttributeItem textWidthItem = {.value = textWidth, .size = 1};
31. nodeApi->setAttribute(text, NODE_WIDTH, &textWidthItem);
32. ArkUI_NumberValue textHeight[] = {{.f32 = 100}};
33. ArkUI_AttributeItem textHeightItem = {.value = textHeight, .size = 1};
34. nodeApi->setAttribute(text, NODE_HEIGHT, &textHeightItem);
35. ArkUI_NumberValue borderWidth[] = {{.f32 = 1}};
36. ArkUI_AttributeItem borderWidthItem = {.value = borderWidth, .size = 1};
37. nodeApi->setAttribute(text, NODE_BORDER_WIDTH, &borderWidthItem);

39. // OH_Drawing_开头的API是字体引擎提供的，typographyStyle表示段落样式。
40. OH_Drawing_TypographyStyle *typographyStyle = OH_Drawing_CreateTypographyStyle();
41. OH_Drawing_SetTypographyTextAlign(typographyStyle, OH_Drawing_TextAlign::TEXT_ALIGN_CENTER);
42. OH_Drawing_SetTypographyTextMaxLines(typographyStyle, NUM_10);
43. // 创建 ArkUI_StyledString。
44. ArkUI_StyledString *styledString = OH_ArkUI_StyledString_Create(typographyStyle, OH_Drawing_CreateFontCollection());
45. // 创建文本样式，设置字体和颜色。
46. OH_Drawing_TextStyle *textStyle = OH_Drawing_CreateTextStyle();
47. OH_Drawing_SetTextStyleFontSize(textStyle, NUM_28);
48. OH_Drawing_SetTextStyleColor(textStyle, OH_Drawing_ColorSetArgb(0xFF, 0x70, 0x70, 0x70));
49. // 文本样式的设置顺序push -> add -> pop.
50. OH_ArkUI_StyledString_PushTextStyle(styledString, textStyle);
51. OH_ArkUI_StyledString_AddText(styledString, "Hello");
52. OH_ArkUI_StyledString_PopTextStyle(styledString);
53. // 添加占位，此区域内不会绘制文字，可以在此位置挂载Image组件实现图文混排。
54. OH_Drawing_PlaceholderSpan placeHolder{.width = 100, .height = 100};
55. OH_ArkUI_StyledString_AddPlaceholder(styledString, &placeHolder);
56. // 设置不同样式的文字
57. OH_Drawing_TextStyle *worldTextStyle = OH_Drawing_CreateTextStyle();
58. OH_Drawing_SetTextStyleFontSize(worldTextStyle, NUM_28);
59. OH_Drawing_SetTextStyleColor(worldTextStyle, OH_Drawing_ColorSetArgb(0xFF, 0x27, 0x87, 0xD9));
60. OH_ArkUI_StyledString_PushTextStyle(styledString, worldTextStyle);
61. OH_ArkUI_StyledString_AddText(styledString, "World!");
62. OH_ArkUI_StyledString_PopTextStyle(styledString);
63. // 依赖StyledString对象创建字体引擎的Typography，此时它已经包含了设置的文本及其样式。
64. OH_Drawing_Typography *typography = OH_ArkUI_StyledString_CreateTypography(styledString);
65. // 字体引擎布局方法，需传入一个宽度，此宽度需与Text组件宽度匹配。
66. // 布局宽度 = Text组件宽度 - (左padding + 右padding)
67. OH_Drawing_TypographyLayout(typography, NUM_400);
68. ArkUI_AttributeItem styledStringItem = {.object = styledString};
69. // 布局完成后，通过NODE_TEXT_CONTENT_WITH_STYLED_STRING设置给Text组件。
70. nodeApi->setAttribute(text, NODE_TEXT_CONTENT_WITH_STYLED_STRING, &styledStringItem);

72. // 资源释放，应用侧可以自由决定何时释放。
73. OH_ArkUI_StyledString_Destroy(styledString);
74. // Text作为Column子组件
75. nodeApi->addChild(column, text);
76. // Column作为XComponent子组件
77. OH_NativeXComponent_AttachNativeRootNode(xComponent_, column);
78. }
79. } // namespace NativeNode::Manager
```

[manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/StyledStringNDK/entry/src/main/cpp/manager.cpp#L15-L126)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/ZBtc2vr5SRmOLMiNEJaErA/zh-cn_image_0000002583478067.png?HW-CC-KV=V1&HW-CC-Date=20260427T234015Z&HW-CC-Expire=86400&HW-CC-Sign=CD4EE16477F20CD265111C7A2BD5DAC21AB1E8D02014B1CE4541B2EBAE74BC69)
