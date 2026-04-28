---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/system-font-c
title: 系统字体的信息获取和使用（C/C++）
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 文本 > 字体管理 > 系统字体的信息获取和使用（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:531333219901cbefe379baee1a9a15c8bfe1ae082db526689cd60e8790c47e1d
---

## 场景介绍

系统字体是指操作系统预设的字体，用于在没有指定自定义字体时显示文本，确保文本的可读性和一致性。默认的系统字体为“HarmonyOS Sans”。

**使用系统字体**的情况通常是在应用未注册自定义字体，或在没有显式指定文本样式时，系统会使用默认的系统字体。另外，系统字体有多种，开发者可以先获取系统字体的配置信息，并根据信息中的字体家族名来进行系统字体的切换和使用。

**禁用系统字体**的情况通常发生在开发者希望确保应用中仅使用自定义字体，而不受操作系统默认字体影响的场景。当自定义字体不存在时，不禁用系统字体，系统则会自动回退到默认字体。通过禁用系统字体，开发者可以在任何场景避免字体回退为系统默认字体，确保文本渲染符合设计预期，从而统一应用的视觉风格。

## 接口说明

以下是系统字体相关的常用接口和结构体，详细接口说明请参考[Drawing](../harmonyos-references/capi-drawing.md)。

| 接口名 | 描述 |
| --- | --- |
| OH\_Drawing\_FontConfigInfo\* OH\_Drawing\_GetSystemFontConfigInfo(OH\_Drawing\_FontConfigInfoErrorCode\*) | 获取系统字体配置信息，返回系统字体配置信息结构体OH\_Drawing\_FontConfigInfo。 |
| void OH\_Drawing\_DestroySystemFontConfigInfo(OH\_Drawing\_FontConfigInfo\*) | 释放系统字体配置信息占用的内存。 |
| OH\_Drawing\_FontCollection\* OH\_Drawing\_CreateSharedFontCollection(void) | 创建可共享的字体集对象OH\_Drawing\_FontCollection。 |
| OH\_Drawing\_TextStyle\* OH\_Drawing\_CreateTextStyle(void) | 创建指向OH\_Drawing\_TextStyle对象的指针，用于设置文本样式。 |
| OH\_Drawing\_SetTextStyleFontFamilies (OH\_Drawing\_TextStyle \*, int, const char \*fontFamilies[]) | 设置指定文本样式的字体家族类型。 |
| void OH\_Drawing\_DisableFontCollectionSystemFont(OH\_Drawing\_FontCollection\* fontCollection) | 禁用系统字体。 |

| 结构体名 | 描述 |
| --- | --- |
| OH\_Drawing\_FontConfigInfo | 系统字体配置信息结构体。 |
| OH\_Drawing\_FontGenericInfo | 系统所支持的通用字体集信息结构体。 |
| OH\_Drawing\_FontFallbackGroup | 备用字体集信息结构体。 |

## 获取系统字体信息

1. 在工程的src/main/cpp/CMakeLists.txt文件中添加以下lib。

   ```
   1. libnative_drawing.so
   ```
2. 导入依赖的相关头文件。

   ```
   1. #include <native_drawing/drawing_font_collection.h>
   2. #include <native_drawing/drawing_text_typography.h>
   3. #include <native_drawing/drawing_register_font.h>
   4. #include <hilog/log.h>
   ```
3. 获取系统字体的配置信息，可以通过返回的状态码确定获取信息是否成功，状态码的包含的具体情况和对应含义可见[OH\_Drawing\_FontConfigInfoErrorCode](../harmonyos-references/capi-drawing-text-typography-h.md#oh_drawing_fontconfiginfoerrorcode)。

   ```
   1. OH_Drawing_FontConfigInfoErrorCode fontConfigInfoErrorCode;  // 用于接收错误代码
   2. OH_Drawing_FontConfigInfo* fontConfigInfo = OH_Drawing_GetSystemFontConfigInfo(&fontConfigInfoErrorCode);
   3. if(fontConfigInfoErrorCode != SUCCESS_FONT_CONFIG_INFO) {
   4. OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_DOMAIN, "PrintSysFontMetrics", "获取系统信息失败，错误代码为： %{public}d", fontConfigInfoErrorCode);
   5. }
   ```

   [sample\_bitmap.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/NDKThemFontAndCustomFontText/entry/src/main/cpp/samples/sample_bitmap.cpp#L242-L248)
4. 系统字体的配置信息[OH\_Drawing\_FontConfigInfo](../harmonyos-references/capi-drawing-oh-drawing-fontconfiginfo.md)包含以下几类信息：

   * 系统字体文件路径数量。
   * 通用字体集列表数量。
   * 备用字体集列表数量。
   * 系统字体文件路径列表。
   * 通用字体集列表，具体信息可见[OH\_Drawing\_FontGenericInfo](../harmonyos-references/capi-drawing-oh-drawing-fontgenericinfo.md)结构体。
   * 备用字体集列表，具体信息可见[OH\_Drawing\_FontFallbackGroup](../harmonyos-references/capi-drawing-oh-drawing-fontfallbackgroup.md)结构体。

   以下示例展示系统字体的一些具体配置信息的获取：

   ```
   1. // 获取系统字体配置信息示例
   2. if (fontConfigInfo != nullptr) {
   3. // 获取字体文件路径数量，打印日志
   4. size_t fontDirCount = fontConfigInfo->fontDirSize;
   5. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_DOMAIN, "PrintSysFontMetrics", "字体文件路径数量为: %{public}zu\n", fontDirCount);
   6. // 遍历字体文件路径列表，打印日志
   7. for (size_t i = 0; i < fontDirCount; ++i) {
   8. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_DOMAIN, "PrintSysFontMetrics", "字体文件路径为: %{public}s\n",
   9. fontConfigInfo->fontDirSet[i]);
   10. }
   11. // 获取通用字体集数量，打印日志
   12. size_t genericCount = fontConfigInfo->fontGenericInfoSize;
   13. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_DOMAIN, "PrintSysFontMetrics", "通用字体集数量为: %{public}zu\n", genericCount);
   14. // 遍历获取每个通用字体集中的字体家族名（例如 HarmonyOS Sans），打印日志
   15. for (size_t i = 0; i < genericCount; ++i) {
   16. OH_Drawing_FontGenericInfo &genericInfo = fontConfigInfo->fontGenericInfoSet[i];
   17. OH_LOG_Print(LOG_APP, LOG_INFO, LOG_DOMAIN, "PrintSysFontMetrics",
   18. "获取第%{public}zu个通用字体集中的字体家族名为: %{public}s", i, genericInfo.familyName);
   19. }
   20. }
   ```

   [sample\_bitmap.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/NDKThemFontAndCustomFontText/entry/src/main/cpp/samples/sample_bitmap.cpp#L250-L271)

   以下打印的示例为应用设备系统对应的部分系统字体配置信息情况，不同设备系统配置信息可能不同，此处仅示意。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/C7aFt9yMTQaNxXLy9oddBQ/zh-cn_image_0000002583478675.png?HW-CC-KV=V1&HW-CC-Date=20260427T234714Z&HW-CC-Expire=86400&HW-CC-Sign=41328E758011E8975C7E49D1892F4652E01ACA7BD7A2C7E306FE3F0B0BC53802)
5. 如若后续不再需要系统字体的系统配置信息时，则释放其占用的内存。

   ```
   1. OH_Drawing_DestroySystemFontConfigInfo(fontConfigInfo);
   ```

## 使用或切换系统字体

系统字体可以有多种，可以先获取系统字体配置信息，再根据其中的字体家族名来进行系统字体的切换和使用。

如果不指定使用任何字体时，会使用系统默认字体“HarmonyOS Sans”显示文本。

1. 在工程的src/main/cpp/CMakeLists.txt文件中添加以下lib。

   ```
   1. libnative_drawing.so
   ```
2. 导入依赖的相关头文件。

   ```
   1. #include <native_drawing/drawing_font_collection.h>
   2. #include <native_drawing/drawing_text_typography.h>
   3. #include <native_drawing/drawing_register_font.h>
   4. #include <hilog/log.h>
   ```
3. 创建字体管理器，建议优先使用OH\_Drawing\_CreateSharedFontCollection创建可共享的字体集对象。

   说明

   使用OH\_Drawing\_CreateFontCollection和OH\_Drawing\_CreateSharedFontCollection均可创建字体管理器OH\_Drawing\_FontCollection对象，但前者创建的字体集指针对象只能被一个段落生成器OH\_Drawing\_TypographyCreate对象使用，无法被多个段落生成器OH\_Drawing\_TypographyCreate对象共享使用。如需在多个段落生成器OH\_Drawing\_TypographyCreate对象间共享使用，请使用后者创建可共享的字体集对象。

   ```
   1. OH_Drawing_FontCollection *fontCollection = OH_Drawing_CreateSharedFontCollection();
   ```

   [sample\_bitmap.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/NDKThemFontAndCustomFontText/entry/src/main/cpp/samples/sample_bitmap.cpp#L276-L278)
4. 创建一个文本样式对象，即OH\_Drawing\_TextStyle对象，用于设置文本样式。

   ```
   1. OH_Drawing_TextStyle *textStyle = OH_Drawing_CreateTextStyle();
   ```

   [sample\_bitmap.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/NDKThemFontAndCustomFontText/entry/src/main/cpp/samples/sample_bitmap.cpp#L279-L281)
5. [获取系统字体信息](system-font-c.md#获取系统字体信息)，获取系统字体的字体家族名，并在文本样式中设置为该系统字体。

   ```
   1. // 情况一：设置系统字体为"HarmonyOS Sans Condensed"
   2. const char *myFontFamilies[] = {"HarmonyOS Sans Condensed"};
   3. OH_Drawing_SetTextStyleFontFamilies(textStyle, 1, myFontFamilies);

   5. // 情况二：不手动设置，此时使用的是系统默认字体"HarmonyOS Sans"
   6. // const char* myFontFamilies[] = {"HarmonyOS Sans Condensed"};
   7. // OH_Drawing_SetTextStyleFontFamilies(textStyle, 1, myFontFamilies);
   ```

   [sample\_bitmap.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/NDKThemFontAndCustomFontText/entry/src/main/cpp/samples/sample_bitmap.cpp#L283-L291)
6. 生成最终段落文本，以便实现最终的文本绘制和显示。

   ```
   1. // 设置其他文本样式
   2. OH_Drawing_SetTextStyleColor(textStyle, OH_Drawing_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
   3. // 设置字体大小为70.0
   4. OH_Drawing_SetTextStyleFontSize(textStyle, 70.0);
   5. // 创建一个段落样式对象，以设置排版风格
   6. OH_Drawing_TypographyStyle *typographyStyle = OH_Drawing_CreateTypographyStyle();
   7. OH_Drawing_SetTypographyTextAlign(typographyStyle, TEXT_ALIGN_LEFT); // 设置段落样式为左对齐
   8. // 创建一个段落生成器
   9. OH_Drawing_TypographyCreate *handler = OH_Drawing_CreateTypographyHandler(typographyStyle, fontCollection);
   10. // 在段落生成器中设置文本样式
   11. OH_Drawing_TypographyHandlerPushTextStyle(handler, textStyle);
   12. // 在段落生成器中设置文本内容
   13. const char *text = "Hello World. 你好世界。\n以上文字使用了系统字体";
   14. OH_Drawing_TypographyHandlerAddText(handler, text);
   15. // 通过段落生成器生成段落
   16. OH_Drawing_Typography *typography = OH_Drawing_CreateTypography(handler);
   17. // 设置页面最大宽度
   18. double maxWidth = width_;
   19. OH_Drawing_TypographyLayout(typography, maxWidth);
   20. // 将文本绘制到画布(0,height_/2.0)上
   21. OH_Drawing_TypographyPaint(typography, cCanvas_, 0, height_ / 2.0);
   ```

   [sample\_bitmap.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/NDKThemFontAndCustomFontText/entry/src/main/cpp/samples/sample_bitmap.cpp#L293-L315)

## 禁用系统字体

当自定义字体不存在时，不禁用系统字体，系统则会自动回退到默认字体。通过禁用系统字体，开发者可以在任何场景避免字体回退为系统默认字体，确保文本渲染符合设计预期，从而统一应用的视觉风格。

在一些应用场景中，开发者可能希望只使用自定义字体来确保字体一致性或提供更具个性化的用户体验。此时，开发者可以通过禁用系统字体，确保应用只使用注册的自定义字体，而不依赖于系统字体。

说明

禁用系统字体后，请确保注册使用自定义字体，否则文本将无法正常显示。

1. 确保已成功注册自定义字体，用于保证禁用系统字体后文本的正常显示，具体可见[自定义字体的注册和使用](custom-font-c.md)。
2. 在工程的src/main/cpp/CMakeLists.txt文件中添加以下lib。

   ```
   1. libnative_drawing.so
   ```
3. 导入依赖的相关头文件。

   ```
   1. #include <native_drawing/drawing_font_collection.h>
   2. #include <native_drawing/drawing_text_typography.h>
   3. #include <native_drawing/drawing_register_font.h>
   4. #include <hilog/log.h>
   ```
4. 创建字体管理器，建议优先使用OH\_Drawing\_CreateSharedFontCollection创建可共享的字体集对象。

   ```
   1. OH_Drawing_FontCollection *fontCollection = OH_Drawing_CreateSharedFontCollection();
   ```

   [sample\_bitmap.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/NDKThemFontAndCustomFontText/entry/src/main/cpp/samples/sample_bitmap.cpp#L328-L330)
5. 禁用系统字体。

   ```
   1. OH_Drawing_DisableFontCollectionSystemFont(fontCollection);
   ```

   [sample\_bitmap.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/NDKThemFontAndCustomFontText/entry/src/main/cpp/samples/sample_bitmap.cpp#L332-L334)
6. 创建文本样式对象，使用注册成功的自定义字体。

   注意

   若不设置字体，文本会默认使用系统字体，而系统字体禁用后若不设置使用自定义字体，文本将无法正常显示。

   ```
   1. OH_Drawing_TextStyle *textStyle = OH_Drawing_CreateTextStyle();
   2. // 禁用系统字体后的几种情况如下：
   3. // 情况一：如果此时设置使用了自定义字体，文本会正常显示
   4. // 该路径是待注册的自定义字体文件在应用设备下的路径，确保该自定义字体文件已正确放置在该路径下
   5. // 后续使用自定义字体时，需使用到该字体家族名
   6. const char* fontFamily = "HarmonyOS_Sans";
   7. const char* fontPath = "/system/fonts/HarmonyOS_Sans.ttf";
   8. // 返回0为成功，1为文件不存在，2为打开文件失败，3为读取文件失败，4为寻找文件失败，5为获取大小失败，9文件损坏
   9. int errorCode = OH_Drawing_RegisterFont(fontCollection, fontFamily, fontPath);
   10. DRAWING_LOGI("errorCode = %{public}d", errorCode);
   11. const char *myFontFamilies[] = {"HarmonyOS_Sans"}; // 确保已成功注册自定义字体，填入自定义字体的字体家族名
   12. OH_Drawing_SetTextStyleFontFamilies(textStyle, 1, myFontFamilies);

   14. // 情况二：如果此时使用了系统字体，文本将无法显示
   15. // const char *myFontFamilies[] = {"HarmonyOS_Sans"};
   16. // OH_Drawing_SetTextStyleFontFamilies(textStyle, 1, myFontFamilies);

   18. // 情况三：如果此时不设置使用字体，文本会默认使用系统默认字体，而此时系统字体已被禁用，因此文本将无法显示
   19. // const char *myFontFamilies[] = {"HarmonyOS_Sans"};
   20. // OH_Drawing_SetTextStyleFontFamilies(textStyle, 1, myFontFamilies);
   ```

   [sample\_bitmap.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/NDKThemFontAndCustomFontText/entry/src/main/cpp/samples/sample_bitmap.cpp#L337-L358)
7. 生成最终的段落文本，以便实现最终的文本绘制和显示。

   ```
   1. // 设置其他文本样式
   2. OH_Drawing_SetTextStyleColor(textStyle, OH_Drawing_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
   3. // 设置字体大小为30.0
   4. OH_Drawing_SetTextStyleFontSize(textStyle, 30.0);
   5. // 创建一个段落样式对象，以设置排版风格
   6. OH_Drawing_TypographyStyle *typographyStyle = OH_Drawing_CreateTypographyStyle();
   7. OH_Drawing_SetTypographyTextAlign(typographyStyle, TEXT_ALIGN_LEFT); // 设置段落样式为左对齐
   8. // 创建一个段落生成器
   9. OH_Drawing_TypographyCreate *handler = OH_Drawing_CreateTypographyHandler(typographyStyle, fontCollection);
   10. // 在段落生成器中设置文本样式
   11. OH_Drawing_TypographyHandlerPushTextStyle(handler, textStyle);
   12. // 在段落生成器中设置文本内容
   13. const char *text = "Hello World.\n以上文字使用了自定义字体";
   14. OH_Drawing_TypographyHandlerAddText(handler, text);
   15. // 通过段落生成器生成段落
   16. OH_Drawing_Typography *typography = OH_Drawing_CreateTypography(handler);

   18. // 设置页面最大宽度
   19. double maxWidth = width_;
   20. OH_Drawing_TypographyLayout(typography, maxWidth);
   21. // 将文本绘制到画布(width_/5.0,height_/2.0)上
   22. OH_Drawing_TypographyPaint(typography, cCanvas_, width_ / 5.0, height_ / 2.0);
   ```

   [sample\_bitmap.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/NDKThemFontAndCustomFontText/entry/src/main/cpp/samples/sample_bitmap.cpp#L360-L383)
