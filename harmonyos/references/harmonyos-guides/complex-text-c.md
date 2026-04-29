---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/complex-text-c
title: 复杂文本绘制与显示（C/C++）
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 文本 > 文本绘制与显示 > 复杂文本绘制与显示（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-29T13:36:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:00307ff61cada568608b46ec332cda1d004f452fafe0ee413384af4685cf923c
---

在进行文本绘制时，可以通过选择合适的字体、大小和颜色完成简单文本的绘制与显示；此外，还支持通过设置其他丰富的样式、语言、段落等进行复杂文本的绘制。

复杂文本绘制主要包含以下几个场景：

* 多语言文本绘制与显示
* 多行文本绘制与显示
* 多样式文本绘制与显示
* 样式的拷贝、绘制与显示

## 多语言文本绘制与显示

多语言支持是全球化应用的基础。多语言文本绘制需要支持不同语言的字符集及其独特的显示需求，例如右到左语言（如阿拉伯语）或竖排文本（如中文）。开发者需要理解不同语言的渲染特性，确保文本的正确显示。

在多语言文本使用的场景下，主要通过指定TextStyle文本样式中的**locale**字段来实现，可直接通过locale字段的值优先匹配对应字体，跳过遍历列表匹配字体的过程，从而降低匹配时间和内存使用。

### 接口说明

| 接口定义 | 描述 |
| --- | --- |
| void OH\_Drawing\_SetTypographyTextLocale(OH\_Drawing\_TypographyStyle\* style, const char\* locale) | 设置指定排版样式的语言环境。 |

### 开发步骤

画布Canvas对象具体可见[画布的获取与绘制结果的显示](canvas-get-result-draw-c.md)。

```
1. // 创建一个 TypographyStyle，创建 TypographyCreate 时需要使用
2. OH_Drawing_TypographyStyle *typoStyle = OH_Drawing_CreateTypographyStyle();
3. // 设置文本对齐方式为居中
4. OH_Drawing_SetTypographyTextAlign(typoStyle, TEXT_ALIGN_CENTER);
5. // 设置 locale 为中文
6. OH_Drawing_SetTypographyTextLocale(typoStyle, "zh-Hans");

8. // 设置文字颜色、大小、字重，不设置 TextStyle 会使用 TypographyStyle 中的默认 TextStyle
9. OH_Drawing_TextStyle *txtStyle = OH_Drawing_CreateTextStyle();
10. OH_Drawing_SetTextStyleColor(txtStyle, OH_Drawing_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
11. OH_Drawing_SetTextStyleFontSize(txtStyle, DIV_TEN(width_));
12. OH_Drawing_SetTextStyleFontWeight(txtStyle, FONT_WEIGHT_400);

14. // 创建 FontCollection，FontCollection 用于管理字体匹配逻辑
15. OH_Drawing_FontCollection *fc = OH_Drawing_CreateSharedFontCollection();
16. // 使用 FontCollection 和 之前创建的 TypographyStyle 创建 TypographyCreate。TypographyCreate 用于创建 Typography
17. OH_Drawing_TypographyCreate *handler = OH_Drawing_CreateTypographyHandler(typoStyle, fc);

19. // 将之前创建的 TextStyle 加入 handler 中
20. OH_Drawing_TypographyHandlerPushTextStyle(handler, txtStyle);
21. // 设置文本内容，并将文本添加到 handler 中
22. const char *text = "你好，中文\n";
23. OH_Drawing_TypographyHandlerAddText(handler, text);

25. // 通过 handler 创建一个 Typography
26. OH_Drawing_Typography *typography = OH_Drawing_CreateTypography(handler);
27. // 设置页面最大宽度
28. double maxWidth = width_;
29. OH_Drawing_TypographyLayout(typography, maxWidth);
30. // 将文本绘制到画布上
31. OH_Drawing_TypographyPaint(typography, cCanvas_, 0, DIV_TEN(width_));

33. // 释放内存
34. OH_Drawing_DestroyTypographyStyle(typoStyle);
35. OH_Drawing_DestroyTextStyle(txtStyle);
36. OH_Drawing_DestroyFontCollection(fc);
37. OH_Drawing_DestroyTypographyHandler(handler);
38. OH_Drawing_DestroyTypography(typography);
```

[draw\_text\_impl.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/NDKComplexText1/entry/src/main/cpp/samples/draw_text_impl.cpp#L45-L84)

### 效果展示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/UVONzMPKQMWHPvQ1A_DOHg/zh-cn_image_0000002558765190.png?HW-CC-KV=V1&HW-CC-Date=20260429T053615Z&HW-CC-Expire=86400&HW-CC-Sign=95E1BF26C11A5CDF59D35CAAA8BDC306AD7E00EDD5E61B837E88C05154CC24CE)

## 多行文本绘制与显示

多行文本相对于单行文本比较复杂，一般针对多行文本，需要进行文本排版、断词策略设置、文本对齐方式、最大行数限制等，主要通过设置段落样式实现。

### 接口说明

| 接口定义 | 描述 |
| --- | --- |
| void OH\_Drawing\_SetTypographyTextAlign(OH\_Drawing\_TypographyStyle\* style, int align) | 设置文本对齐方式。 |
| void OH\_Drawing\_SetTypographyTextWordBreakType(OH\_Drawing\_TypographyStyle\* style, int wordBreakType) | 设置单词的断词方式。 |
| void OH\_Drawing\_SetTypographyTextMaxLines(OH\_Drawing\_TypographyStyle\* style, int lineNumber) | 设置文本最大行数。 |

### 开发步骤

以下以断行策略为 BREAK\_ALL 的场景为例，其余策略同理。

```
1. // 创建 FontCollection，FontCollection 用于管理字体匹配逻辑
2. OH_Drawing_FontCollection *fc = OH_Drawing_CreateSharedFontCollection();

4. // 设置文字颜色、大小、字重，不设置 TextStyle 会使用 TypographyStyle 中的默认 TextStyle
5. OH_Drawing_TextStyle *txtStyle = OH_Drawing_CreateTextStyle();
6. OH_Drawing_SetTextStyleColor(txtStyle, OH_Drawing_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
7. OH_Drawing_SetTextStyleFontSize(txtStyle, DIV_TWENTY(width_));
8. OH_Drawing_SetTextStyleFontWeight(txtStyle, FONT_WEIGHT_400);

10. // 设置文本内容
11. const char *text =
12. "Nunc quis augue viverra, venenatis arcu eu, gravida odio. Integer posuere nisi quis ex pretium, a dapibus "
13. "nisl gravida. Mauris lacinia accumsan enim, non tempus ligula. Mauris iaculis dui eu nisi tristique, in porta "
14. "urna varius. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Mauris "
15. "congue nibh mi, vel ultrices ex volutpat et. Aliquam consectetur odio in libero tristique, a mattis ex "
16. "mollis. Praesent et nisl iaculis, facilisis metus nec, faucibus lacus. Duis nec dolor at nibh eleifend "
17. "tempus. Nunc et enim interdum, commodo eros ac, pretium sapien. Pellentesque laoreet orci a nunc pharetra "
18. "pharetra.";

20. // 创建一个断词策略为 BREAK_ALL 的 TypographyStyle
21. OH_Drawing_TypographyStyle *typoStyle = OH_Drawing_CreateTypographyStyle();
22. // 设置文本对齐方式为居中
23. OH_Drawing_SetTypographyTextAlign(typoStyle, TEXT_ALIGN_CENTER);
24. // 设置断词策略为 WORD_BREAK_TYPE_BREAK_ALL
25. OH_Drawing_SetTypographyTextWordBreakType(typoStyle, OH_Drawing_WordBreakType::WORD_BREAK_TYPE_BREAK_ALL);
26. // 设置最大行数为 10，行数大于 10 的部分不显示
27. OH_Drawing_SetTypographyTextMaxLines(typoStyle, 10);

29. // 使用之前创建的 FontCollection 和 TypographyStyle 创建 TypographyCreate。TypographyCreate 用于创建 Typography
30. OH_Drawing_TypographyCreate *handler = OH_Drawing_CreateTypographyHandler(typoStyle, fc);
31. // 将之前创建的 TextStyle 加入 handler
32. OH_Drawing_TypographyHandlerPushTextStyle(handler, txtStyle);
33. // 将文本添加到 handler 中
34. OH_Drawing_TypographyHandlerAddText(handler, text);

36. OH_Drawing_Typography *typography = OH_Drawing_CreateTypography(handler);
37. // 设置页面最大宽度
38. double maxWidth = width_;
39. OH_Drawing_TypographyLayout(typography, maxWidth);
40. // 将文本绘制到画布上
41. OH_Drawing_TypographyPaint(typography, cCanvas_, 0, DIV_TEN(width_));

43. // 释放内存
44. OH_Drawing_DestroyFontCollection(fc);
45. OH_Drawing_DestroyTextStyle(txtStyle);
46. OH_Drawing_DestroyTypographyStyle(typoStyle);
47. OH_Drawing_DestroyTypographyHandler(handler);
48. OH_Drawing_DestroyTypography(typography);
```

[draw\_text\_impl.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/NDKComplexText1/entry/src/main/cpp/samples/draw_text_impl.cpp#L89-L138)

| BREAK\_ALL | BREAK\_WORD |
| --- | --- |
|  |  |

| BREAK\_HYPHEN（locale：未设置） | BREAK\_HYPHEN（locale：en-gb） | BREAK\_HYPHEN（locale：en-us） |
| --- | --- | --- |
|  |  |  |

## 多样式文本绘制与显示

除基本文字、排版属性之外，针对应用中不同文本的设计，开发者可能需要设置使用不同的绘制样式或能力，以凸显对应文本的独特表现或风格，此时可以结合使用多种绘制样式进行文本的渲染。

当前支持的多样式绘制及各绘制样式侧重效果如下：

* **装饰线样式绘制：** 主要通过不同的线条样式对文本进行装饰，可以使文本更加突出，富有表现力。
* **字体特性绘制：** 主要通过字体的变化，包括粗细、斜体等特性来改变文本的外观，增强文本的可读性和美观性。
* **可变字体绘制：** 对应提供文本在不同的显示环境和设备上灵活调整的能力，可满足更为精细的视觉效果。
* **文本阴影绘制：** 主要通过在文本周围添加阴影效果，以提升文本的层次感和立体感，从而使文本更具吸引力。
* **占位符绘制：** 可以在不确定文本内容时保持文本布局的稳定性，使得文本显示更为流畅和自然。
* **自动间距绘制：** 可以在一些字符混排切换的地方自动添加额外间距，提升阅读体验。
* **渐变色绘制：** 可以为文字提供颜色渐变效果，增强文字表现力。
* **垂直对齐：** 调整文本在垂直方向排版位置，提升排版质量。
* **上下标：** 可以将任意字符处理成上标或下标，更精准表达文本含义。
* **高对比度文字绘制：** 主要通过将深色文字变黑、浅色文字变白，增强文本的对比效果。
* **行高调整：** 调整行高可改变文本行的垂直间距，使行间距更松散或更紧凑，显著改善文本垂直截断问题，提高可读性。
* **行间距调整：** 通过调整行间距的方式可以实现行高调整一样的效果，优化阅读体验。

### 装饰线

**装饰线**是指在文本上方、下方或中间添加的装饰性线条，当前支持上划线、下划线、删除线。

可以通过添加文本装饰线，提升文本的视觉效果和可读性。

使用装饰线需要初始化装饰线样式对象，并添加到文本样式中，从而在文本绘制时生效。

| 接口定义 | 描述 |
| --- | --- |
| void OH\_Drawing\_SetTextStyleDecoration(OH\_Drawing\_TextStyle\* style, int decoration) | 设置指定文本样式中的装饰线类型，只能设置一个装饰线类型，添加多个需要使用OH\_Drawing\_AddTextStyleDecoration。 |
| void OH\_Drawing\_SetTextStyleDecorationStyle(OH\_Drawing\_TextStyle\* style, int decorationStyle) | 设置指定文本样式中的装饰线样式。 |
| void OH\_Drawing\_SetTextStyleDecorationColor(OH\_Drawing\_TextStyle\* style, uint32\_t color) | 设置指定文本样式中的装饰线颜色。 |

示例及示意效果如下所示：

```
1. // 创建一个TypographyStyle创建Typography时需要使用
2. OH_Drawing_TypographyStyle *typoStyle = OH_Drawing_CreateTypographyStyle();
3. // 设置文本对齐方式为居中
4. OH_Drawing_SetTypographyTextAlign(typoStyle, TEXT_ALIGN_CENTER);
5. // 设置文本内容
6. const char *text = "Hello World Drawing\n";

8. // 设置文字颜色、大小、字重，不设置 TextStyle 会使用 TypographyStyle 中的默认 TextStyle
9. OH_Drawing_TextStyle *txtStyleWithDeco = OH_Drawing_CreateTextStyle();
10. OH_Drawing_SetTextStyleColor(txtStyleWithDeco, OH_Drawing_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
11. OH_Drawing_SetTextStyleFontSize(txtStyleWithDeco, DIV_TEN(width_));
12. OH_Drawing_SetTextStyleFontWeight(txtStyleWithDeco, FONT_WEIGHT_400);
13. // 设置装饰线为 LINE_THROUGH
14. OH_Drawing_SetTextStyleDecoration(txtStyleWithDeco, TEXT_DECORATION_LINE_THROUGH);
15. // 设置装饰线样式为 WAVY
16. OH_Drawing_SetTextStyleDecorationStyle(txtStyleWithDeco, TEXT_DECORATION_STYLE_WAVY);
17. // 设置装饰线颜色
18. OH_Drawing_SetTextStyleDecorationColor(txtStyleWithDeco, OH_Drawing_ColorSetArgb(0xFF, 0x6F, 0xFF, 0xFF));

20. // 创建一个不带装饰线的 TextStyle 用于对比
21. OH_Drawing_TextStyle *txtStyleNoDeco = OH_Drawing_CreateTextStyle();
22. // 设置文字颜色、大小、字重，不设置 TextStyle 会使用 TypographyStyle 中的默认 TextStyle
23. OH_Drawing_SetTextStyleColor(txtStyleNoDeco, OH_Drawing_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
24. OH_Drawing_SetTextStyleFontSize(txtStyleNoDeco, DIV_TEN(width_));
25. OH_Drawing_SetTextStyleFontWeight(txtStyleNoDeco, FONT_WEIGHT_400);

27. // 创建 FontCollection，FontCollection 用于管理字体匹配逻辑
28. OH_Drawing_FontCollection *fc = OH_Drawing_CreateSharedFontCollection();
29. // 使用 FontCollection 和 之前创建的 TypographyStyle 创建 TypographyCreate。TypographyCreate 用于创建 Typography
30. OH_Drawing_TypographyCreate *handler = OH_Drawing_CreateTypographyHandler(typoStyle, fc);

32. // 加入带有装饰线的文本样式
33. OH_Drawing_TypographyHandlerPushTextStyle(handler, txtStyleWithDeco);
34. // 将文本添加到 handler 中
35. OH_Drawing_TypographyHandlerAddText(handler, text);

37. // 后续加入的不带装饰线的文本样式
38. OH_Drawing_TypographyHandlerPushTextStyle(handler, txtStyleNoDeco);
39. // 将文本添加到 handler 中
40. OH_Drawing_TypographyHandlerAddText(handler, text);

42. OH_Drawing_Typography *typography = OH_Drawing_CreateTypography(handler);
43. // 设置页面最大宽度
44. double maxWidth = width_;
45. OH_Drawing_TypographyLayout(typography, maxWidth);
46. // 将文本绘制到画布上
47. OH_Drawing_TypographyPaint(typography, cCanvas_, 0, DIV_TEN(width_));

49. // 释放内存
50. OH_Drawing_DestroyTypographyStyle(typoStyle);
51. OH_Drawing_DestroyTextStyle(txtStyleWithDeco);
52. OH_Drawing_DestroyTextStyle(txtStyleNoDeco);
53. OH_Drawing_DestroyFontCollection(fc);
54. OH_Drawing_DestroyTypographyHandler(handler);
55. OH_Drawing_DestroyTypography(typography);
```

[draw\_text\_impl.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/NDKComplexText1/entry/src/main/cpp/samples/draw_text_impl.cpp#L366-L422)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/M7YpYDYXTU2BuNcmMxSY6w/zh-cn_image_0000002589325063.png?HW-CC-KV=V1&HW-CC-Date=20260429T053615Z&HW-CC-Expire=86400&HW-CC-Sign=014F34D7EE24248226CEFC1D8F730D5B4B89F1494612BDFD6C2BCC87AEB5F5E1)

### 字体特征

**字体特征**绘制专注于在文本渲染过程中对字体特性（如粗体、斜体、字体变种等）的处理，允许字体在不同的排版场景下表现出不同的效果，可用于增强文本的表现力，使其更符合设计和阅读需求。

常见的**FontFeature**包含有liga、frac、case等，需要对应的ttf文件支持才能正常使能。

| 接口定义 | 描述 |
| --- | --- |
| void OH\_Drawing\_TextStyleAddFontFeature(OH\_Drawing\_TextStyle\* style, const char\* tag, int value) | 设置文本样式中指定字体特征是否启用。 |

示例及示意效果如下所示：

```
1. // 创建一个 TypographyStyle，创建 TypographyCreate 时需要使用
2. OH_Drawing_TypographyStyle *typoStyle = OH_Drawing_CreateTypographyStyle();
3. // 设置文本对齐方式为居中
4. OH_Drawing_SetTypographyTextAlign(typoStyle, TEXT_ALIGN_CENTER);
5. // 设置文本内容
6. const char *text = "1/2 1/3 1/4\n";

8. // 设置文字颜色、大小、字重，不设置TextStyle无法绘制出文本
9. OH_Drawing_TextStyle *txtStyleWithFeature = OH_Drawing_CreateTextStyle();
10. OH_Drawing_SetTextStyleColor(txtStyleWithFeature, OH_Drawing_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
11. OH_Drawing_SetTextStyleFontSize(txtStyleWithFeature, DIV_TEN(width_));
12. OH_Drawing_SetTextStyleFontWeight(txtStyleWithFeature, FONT_WEIGHT_900);
13. // 设置启用frac font feature，此功能将斜线分隔的数字替换为普通（对角线）分数。
14. OH_Drawing_TextStyleAddFontFeature(txtStyleWithFeature, "frac", 1);

16. // 创建一个不带字体特征的 TextStyle 用于对比
17. OH_Drawing_TextStyle *txtStyleNoFeature = OH_Drawing_CreateTextStyle();
18. // 设置文字颜色、大小、字重。不设置 TextStyle 无法绘制出文本
19. OH_Drawing_SetTextStyleColor(txtStyleNoFeature, OH_Drawing_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
20. OH_Drawing_SetTextStyleFontSize(txtStyleNoFeature, DIV_TEN(width_));
21. OH_Drawing_SetTextStyleFontWeight(txtStyleNoFeature, FONT_WEIGHT_900);

23. // 创建 FontCollection，FontCollection 用于管理字体匹配逻辑
24. OH_Drawing_FontCollection *fc = OH_Drawing_CreateSharedFontCollection();
25. // 使用 FontCollection 和 之前创建的 TypographyStyle 创建 TypographyCreate。TypographyCreate 用于创建 Typography
26. OH_Drawing_TypographyCreate *handler = OH_Drawing_CreateTypographyHandler(typoStyle, fc);

28. // 加入带有字体特征的文本样式
29. OH_Drawing_TypographyHandlerPushTextStyle(handler, txtStyleWithFeature);
30. // 将文本添加到 handler 中
31. OH_Drawing_TypographyHandlerAddText(handler, text);
32. // 销毁之前创建的 TextStyle
33. OH_Drawing_TypographyHandlerPopTextStyle(handler);

35. // 后续加入的不带字体特征的文本样式
36. OH_Drawing_TypographyHandlerPushTextStyle(handler, txtStyleNoFeature);
37. // 将文本添加到 handler 中
38. OH_Drawing_TypographyHandlerAddText(handler, text);
39. // 销毁之前创建的 TextStyle
40. OH_Drawing_TypographyHandlerPopTextStyle(handler);

42. OH_Drawing_Typography *typography = OH_Drawing_CreateTypography(handler);
43. // 设置页面最大宽度
44. double maxWidth = width_;
45. OH_Drawing_TypographyLayout(typography, maxWidth);
46. // 将文本绘制到画布上
47. OH_Drawing_TypographyPaint(typography, cCanvas_, 0, DIV_TEN(width_));

49. // 释放内存
50. OH_Drawing_DestroyTypographyStyle(typoStyle);
51. OH_Drawing_DestroyTextStyle(txtStyleWithFeature);
52. OH_Drawing_DestroyTextStyle(txtStyleNoFeature);
53. OH_Drawing_DestroyFontCollection(fc);
54. OH_Drawing_DestroyTypographyHandler(handler);
55. OH_Drawing_DestroyTypography(typography);
```

[draw\_text\_impl.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/NDKComplexText1/entry/src/main/cpp/samples/draw_text_impl.cpp#L427-L483)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/es8PQxOsR2yNR3zON3SZUw/zh-cn_image_0000002589244999.png?HW-CC-KV=V1&HW-CC-Date=20260429T053615Z&HW-CC-Expire=86400&HW-CC-Sign=0943BFA3BF9506A3E086453642E7E57F9767A3ACB5A21E6A96BDEF77FFB76A4D)

### 可变字体

**可变字体**是一种在一个字体文件中包含多个字形变体的字体格式，允许在一个字体文件内灵活地调整字体的各种属性（如字重、字宽、斜体等）。

与传统字体文件（每种变体需要一个独立的文件）不同，可变字体在一个字体文件中包含多个变体轴，可通过使用可变字体实现文本渲染绘制时的平滑过渡。

| 接口定义 | 描述 |
| --- | --- |
| void OH\_Drawing\_TextStyleAddFontVariation(OH\_Drawing\_TextStyle\* style, const char\* axis, const float value) | 添加可变字体属性。对应的字体文件（.ttf文件）需要支持可变调节，此接口才能生效。当对应的字体不支持可变调节时，此接口调用不生效。 |

示例及示意效果如下所示：

```
1. // 创建一个 TypographyStyle 创建 Typography 时需要使用
2. OH_Drawing_TypographyStyle *typoStyle = OH_Drawing_CreateTypographyStyle();
3. // 设置文本对齐方式为居中
4. OH_Drawing_SetTypographyTextAlign(typoStyle, TEXT_ALIGN_CENTER);
5. // 设置文字内容
6. const char *text = "Hello World Drawing\n";

8. OH_Drawing_TextStyle *txtStyleWithVar = OH_Drawing_CreateTextStyle();
9. // 设置可变字体的字重为800，在字体文件支持的情况下，还可以设置"slnt", "wdth"
10. OH_Drawing_TextStyleAddFontVariation(txtStyleWithVar, "wght", 800);
11. // 设置文字颜色、大小、字重，不设置 TextStyle 会使用 TypographyStyle 中的默认 TextStyle
12. OH_Drawing_SetTextStyleColor(txtStyleWithVar, OH_Drawing_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
13. OH_Drawing_SetTextStyleFontSize(txtStyleWithVar, DIV_TEN(width_));
14. // 此处设置字重不生效，将被可变字体的字重覆盖
15. OH_Drawing_SetTextStyleFontWeight(txtStyleWithVar, FONT_WEIGHT_400);

17. // 创建一个不带可变字体的 TextStyle 用于对比
18. OH_Drawing_TextStyle *txtStyleNoVar = OH_Drawing_CreateTextStyle();
19. // 设置文字颜色、大小、字重，不设置 TextStyle 会使用 TypographyStyle 中的默认 TextStyle
20. OH_Drawing_SetTextStyleColor(txtStyleNoVar, OH_Drawing_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
21. OH_Drawing_SetTextStyleFontSize(txtStyleNoVar, DIV_TEN(width_));
22. OH_Drawing_SetTextStyleFontWeight(txtStyleNoVar, FONT_WEIGHT_400);

24. // 创建 FontCollection，FontCollection 用于管理字体匹配逻辑
25. OH_Drawing_FontCollection *fc = OH_Drawing_CreateSharedFontCollection();
26. // 使用 FontCollection 和 之前创建的 TypographyStyle 创建 TypographyCreate。TypographyCreate 用于创建 Typography
27. OH_Drawing_TypographyCreate *handler = OH_Drawing_CreateTypographyHandler(typoStyle, fc);

29. // 加入带有可变字体的文本样式
30. OH_Drawing_TypographyHandlerPushTextStyle(handler, txtStyleWithVar);
31. // 将文本添加到 handler 中
32. OH_Drawing_TypographyHandlerAddText(handler, text);
33. // 弹出之前创建的 TextStyle
34. OH_Drawing_TypographyHandlerPopTextStyle(handler);

36. // 后续加入的不带可变字体的文本样式
37. OH_Drawing_TypographyHandlerPushTextStyle(handler, txtStyleNoVar);
38. // 将文本添加到 handler 中
39. OH_Drawing_TypographyHandlerAddText(handler, text);
40. // 弹出之前创建的 TextStyle
41. OH_Drawing_TypographyHandlerPopTextStyle(handler);

43. OH_Drawing_Typography *typography = OH_Drawing_CreateTypography(handler);
44. // 设置页面最大宽度
45. double maxWidth = width_;
46. OH_Drawing_TypographyLayout(typography, maxWidth);
47. // 将文本绘制到画布上
48. OH_Drawing_TypographyPaint(typography, cCanvas_, 0, DIV_TEN(width_));

50. // 释放内存
51. OH_Drawing_DestroyTypographyStyle(typoStyle);
52. OH_Drawing_DestroyTextStyle(txtStyleWithVar);
53. OH_Drawing_DestroyTextStyle(txtStyleNoVar);
54. OH_Drawing_DestroyFontCollection(fc);
55. OH_Drawing_DestroyTypographyHandler(handler);
56. OH_Drawing_DestroyTypography(typography);
```

[draw\_text\_impl.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/NDKComplexText1/entry/src/main/cpp/samples/draw_text_impl.cpp#L489-L546)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/rsxVTtgATKORudukziQBuA/zh-cn_image_0000002558765194.png?HW-CC-KV=V1&HW-CC-Date=20260429T053615Z&HW-CC-Expire=86400&HW-CC-Sign=F934FD5921D70E9A071DE5EF94657BEAD9B662C8EFA5C9FD42C2FC2865459995)

### 文本阴影

**文本阴影**为文本提供了深度感，使得文本在背景上更具立体感。通常用于提升文本的视觉吸引力或增强可读性，尤其是在色彩对比度较低的场景下。

其中，TextShadow有三个属性，分别为阴影颜色color、阴影基于当前文本的偏移位置point、阴影半径blurRadius。

使用阴影效果需要在文本样式中设置对应的阴影效果数组，从而在文本绘制时生效。

| 接口定义 | 描述 |
| --- | --- |
| OH\_Drawing\_Point\* OH\_Drawing\_PointCreate(float x, float y) | 用于创建一个坐标点对象。 |
| OH\_Drawing\_TextShadow\* OH\_Drawing\_CreateTextShadow(void) | 创建指向字体阴影对象的指针。 |
| void OH\_Drawing\_SetTextShadow(OH\_Drawing\_TextShadow\* shadow, uint32\_t color, OH\_Drawing\_Point\* offset, double blurRadius) | 设置字体阴影对象的参数。 |
| void OH\_Drawing\_TextStyleAddShadow(OH\_Drawing\_TextStyle\* style, const OH\_Drawing\_TextShadow\* shadow) | 字体阴影容器中添加字体阴影元素。 |
| void OH\_Drawing\_DestroyTextShadow(OH\_Drawing\_TextShadow\* shadow) | 释放被字体阴影对象占据的内存。 |

示例及示意效果如下所示：

```
1. // 创建一个 TypographyStyle 创建 Typography 时需要使用
2. OH_Drawing_TypographyStyle *typoStyle = OH_Drawing_CreateTypographyStyle();
3. // 设置文本对齐方式为居中
4. OH_Drawing_SetTypographyTextAlign(typoStyle, TEXT_ALIGN_CENTER);
5. // 设置文本内容
6. const char *text = "Hello World Drawing\n";

8. // 设置文字颜色、大小、字重，不设置 TextStyle 会使用 TypographyStyle 中的默认 TextStyle
9. OH_Drawing_TextStyle *txtStyleWithShadow = OH_Drawing_CreateTextStyle();
10. OH_Drawing_SetTextStyleColor(txtStyleWithShadow, OH_Drawing_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
11. OH_Drawing_SetTextStyleFontSize(txtStyleWithShadow, DIV_TEN(width_));
12. OH_Drawing_SetTextStyleFontWeight(txtStyleWithShadow, FONT_WEIGHT_400);
13. // 设置阴影偏移量
14. OH_Drawing_Point *offset = OH_Drawing_PointCreate(1, 1);
15. OH_Drawing_TextShadow *shadow = OH_Drawing_CreateTextShadow();
16. double radius = 10.0;
17. // 为 TextShadow 设置样式
18. OH_Drawing_SetTextShadow(shadow, OH_Drawing_ColorSetArgb(0xFF, 0x00, 0x00, 0x00), offset, radius);
19. // 将 TextShadow 加入 TextStyle
20. OH_Drawing_TextStyleAddShadow(txtStyleWithShadow, shadow);

22. // 创建一个不带阴影的 TextStyle 用于对比
23. OH_Drawing_TextStyle *txtStyleNoShadow = OH_Drawing_CreateTextStyle();
24. // 设置文字颜色、大小、字重，不设置 TextStyle 会使用 TypographyStyle 中的默认 TextStyle
25. OH_Drawing_SetTextStyleColor(txtStyleNoShadow, OH_Drawing_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
26. OH_Drawing_SetTextStyleFontSize(txtStyleNoShadow, DIV_TEN(width_));
27. OH_Drawing_SetTextStyleFontWeight(txtStyleNoShadow, FONT_WEIGHT_400);

29. // 创建 FontCollection，FontCollection 用于管理字体匹配逻辑
30. OH_Drawing_FontCollection *fc = OH_Drawing_CreateSharedFontCollection();
31. // 使用 FontCollection 和 之前创建的 TypographyStyle 创建 TypographyCreate。TypographyCreate 用于创建 Typography
32. OH_Drawing_TypographyCreate *handler = OH_Drawing_CreateTypographyHandler(typoStyle, fc);

34. // 加入带有阴影的文本样式
35. OH_Drawing_TypographyHandlerPushTextStyle(handler, txtStyleWithShadow);
36. // 将文本添加到 handler 中
37. OH_Drawing_TypographyHandlerAddText(handler, text);

39. // 后续加入的不带阴影的文本样式
40. OH_Drawing_TypographyHandlerPushTextStyle(handler, txtStyleNoShadow);
41. // 将文本添加到 handler 中
42. OH_Drawing_TypographyHandlerAddText(handler, text);

44. OH_Drawing_Typography *typography = OH_Drawing_CreateTypography(handler);
45. // 设置页面最大宽度
46. double maxWidth = width_;
47. OH_Drawing_TypographyLayout(typography, maxWidth);
48. // 将文本绘制到画布上
49. OH_Drawing_TypographyPaint(typography, cCanvas_, 0, DIV_TEN(width_));

51. // 释放内存
52. OH_Drawing_DestroyTypographyStyle(typoStyle);
53. OH_Drawing_DestroyTextStyle(txtStyleWithShadow);
54. OH_Drawing_PointDestroy(offset);
55. OH_Drawing_DestroyTextShadow(shadow);
56. OH_Drawing_DestroyTextStyle(txtStyleNoShadow);
57. OH_Drawing_DestroyFontCollection(fc);
58. OH_Drawing_DestroyTypographyHandler(handler);
59. OH_Drawing_DestroyTypography(typography);
```

[draw\_text\_impl.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/NDKComplexText1/entry/src/main/cpp/samples/draw_text_impl.cpp#L551-L611)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/AKa064mCReWiBvfjZRuk8g/zh-cn_image_0000002558605538.png?HW-CC-KV=V1&HW-CC-Date=20260429T053615Z&HW-CC-Expire=86400&HW-CC-Sign=8CB19FDA71A2AB6A6A880BB46A7A04F1EC83FED41CA4BB976F59387FAA752EB6)

### 占位符

占位符绘制用于处理文本中占位符符号的渲染。

占位符也是用来实现图文混排的关键，是指在实际图像或内容注册之前，用来预先提供或替代某个位置的视觉元素。

| 接口定义 | 描述 |
| --- | --- |
| void OH\_Drawing\_TypographyHandlerAddPlaceholder(OH\_Drawing\_TypographyCreate\* handler, OH\_Drawing\_PlaceholderSpan\* span) | 设置占位符。 |

示例及示意效果如下所示：

```
1. // 设置页面最大宽度
2. double maxWidth = width_;
3. // 创建 FontCollection，FontCollection 用于管理字体匹配逻辑
4. OH_Drawing_FontCollection *fc = OH_Drawing_CreateSharedFontCollection();

6. // 设置文字颜色、大小、字重，不设置 TextStyle 会使用 TypographyStyle 中的默认 TextStyle
7. OH_Drawing_TextStyle *txtStyle = OH_Drawing_CreateTextStyle();
8. OH_Drawing_SetTextStyleColor(txtStyle, OH_Drawing_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
9. OH_Drawing_SetTextStyleFontSize(txtStyle, DIV_TEN(width_));
10. OH_Drawing_SetTextStyleFontWeight(txtStyle, FONT_WEIGHT_400);

12. // 设置文本内容
13. const char *text = "Hello World Drawing\n";

15. // 创建一个 TypographyStyle 创建 Typography 时需要使用
16. OH_Drawing_TypographyStyle *typoStyle = OH_Drawing_CreateTypographyStyle();
17. // 设置文本对齐方式为居中
18. OH_Drawing_SetTypographyTextAlign(typoStyle, TEXT_ALIGN_CENTER);

20. // 使用 FontCollection 和 之前创建的 TypographyStyle 创建 TypographyCreate。TypographyCreate 用于创建 Typography
21. OH_Drawing_TypographyCreate *handlerWithPlaceholder = OH_Drawing_CreateTypographyHandler(typoStyle, fc);
22. // 创建一个 placeholder，并且初始化其成员变量
23. OH_Drawing_PlaceholderSpan placeholder;
24. placeholder.width = DIV_TEN(width_);
25. placeholder.height = DIV_FIVE(width_);
26. placeholder.alignment = ALIGNMENT_ABOVE_BASELINE; // 基线对齐策略
27. placeholder.baseline = TEXT_BASELINE_ALPHABETIC;  // 使用的文本基线类型
28. placeholder.baselineOffset = 0.0; // 相比基线的偏移量。只有对齐策略是 OFFSET_AT_BASELINE 时生效

30. // 将 placeholder 放在开头
31. OH_Drawing_TypographyHandlerAddPlaceholder(handlerWithPlaceholder, &placeholder);

33. // 将之前创建的 TextStyle 加入 handler
34. OH_Drawing_TypographyHandlerPushTextStyle(handlerWithPlaceholder, txtStyle);
35. // 将文本添加到 handler 中
36. OH_Drawing_TypographyHandlerAddText(handlerWithPlaceholder, text);

38. OH_Drawing_Typography *typographyWithPlaceholder = OH_Drawing_CreateTypography(handlerWithPlaceholder);
39. OH_Drawing_TypographyLayout(typographyWithPlaceholder, maxWidth);
40. // 将文本绘制到画布上
41. OH_Drawing_TypographyPaint(typographyWithPlaceholder, cCanvas_, 0, DIV_TEN(width_));

43. // 创建 OH_Drawing_TypographyCreate
44. OH_Drawing_TypographyCreate *handlerNoPlaceholder = OH_Drawing_CreateTypographyHandler(typoStyle, fc);
45. // 将之前创建的 TextStyle 加入 handler
46. OH_Drawing_TypographyHandlerPushTextStyle(handlerNoPlaceholder, txtStyle);
47. // 将文本添加到 handler 中
48. OH_Drawing_TypographyHandlerAddText(handlerNoPlaceholder, text);

50. OH_Drawing_Typography *typographyNoPlaceholder = OH_Drawing_CreateTypography(handlerNoPlaceholder);

52. OH_Drawing_TypographyLayout(typographyNoPlaceholder, maxWidth);
53. // 将文本绘制到画布上
54. OH_Drawing_TypographyPaint(typographyNoPlaceholder, cCanvas_, 0, DIV_TWO(width_));

56. // 释放内存
57. OH_Drawing_DestroyFontCollection(fc);
58. OH_Drawing_DestroyTextStyle(txtStyle);
59. OH_Drawing_DestroyTypographyStyle(typoStyle);
60. OH_Drawing_DestroyTypographyHandler(handlerWithPlaceholder);
61. OH_Drawing_DestroyTypographyHandler(handlerNoPlaceholder);
62. OH_Drawing_DestroyTypography(typographyWithPlaceholder);
63. OH_Drawing_DestroyTypography(typographyNoPlaceholder);
```

[draw\_text\_impl.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/NDKComplexText1/entry/src/main/cpp/samples/draw_text_impl.cpp#L616-L680)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/D41FZSV_T5qRr79vsIiEHw/zh-cn_image_0000002589325065.png?HW-CC-KV=V1&HW-CC-Date=20260429T053615Z&HW-CC-Expire=86400&HW-CC-Sign=2BF5DA04B1D7B12057F71F9703D93D49A312C3FDD765DE41EF8A3859AD3E067F)

### 自动间距

使能自动间距，则会在文本排版时自动调整CJK（中文字符、日文字符、韩文字符）与西文（拉丁字母、西里尔字母、希腊字母）、CJK与数字、CJK与版权符号、版权符号与数字、版权符号与西文之间的间距。例如，在中英文混排场景中，使能自动间距即可在中英文切换的地方自动添加额外间距，提升阅读体验。

| 接口定义 | 描述 |
| --- | --- |
| void OH\_Drawing\_SetTypographyTextAutoSpace(OH\_Drawing\_TypographyStyle \*style, bool enableAutoSpace) | 设置文本排版时是否使能自动间距。默认不使能自动间距，一旦使能则会自动调整CJK（中文字符、日文字符、韩文字符）与西文（拉丁字母、西里尔字母、希腊字母）、CJK与数字、CJK与版权符号、版权符号与数字、版权符号与西文之间的间距。 |

示例及示意效果如下所示：

```
1. // 创建一个TypographyStyle创建Typography时需要使用
2. OH_Drawing_TypographyStyle *typoStyle = OH_Drawing_CreateTypographyStyle();
3. // 设置使能自动间距，默认为false
4. OH_Drawing_SetTypographyTextAutoSpace(typoStyle, true);
5. // 设置文字内容
6. const char *text = "test测试©test©测。";

8. OH_Drawing_TextStyle *txtStyle = OH_Drawing_CreateTextStyle();
9. // 设置文字颜色、大小、字重，不设置TextStyle会使用TypographyStyle中的默认TextStyle
10. OH_Drawing_SetTextStyleColor(txtStyle, OH_Drawing_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
11. OH_Drawing_SetTextStyleFontSize(txtStyle, DIV_TEN(width_));

13. // 创建FontCollection，FontCollection用于管理字体匹配逻辑
14. OH_Drawing_FontCollection *fc = OH_Drawing_CreateSharedFontCollection();
15. // 使用FontCollection和之前创建的TypographyStyle创建TypographyCreate。TypographyCreate用于创建Typography
16. OH_Drawing_TypographyCreate *handler = OH_Drawing_CreateTypographyHandler(typoStyle, fc);

18. // 将文本样式添加到handler中
19. OH_Drawing_TypographyHandlerPushTextStyle(handler, txtStyle);
20. // 将文本添加到handler中
21. OH_Drawing_TypographyHandlerAddText(handler, text);
22. // 创建段落
23. OH_Drawing_Typography *typography = OH_Drawing_CreateTypography(handler);
24. // 设置页面最大宽度
25. double maxWidth = width_;
26. // 将段落按照排版宽度进行排版
27. OH_Drawing_TypographyLayout(typography, maxWidth);
28. // 将文本绘制到画布上
29. OH_Drawing_TypographyPaint(typography, cCanvas_, 0, DIV_TEN(width_));

31. // 设置使能自动间距，用于对比
32. OH_Drawing_SetTypographyTextAutoSpace(typoStyle, false);

34. // 使用FontCollection和之前创建的TypographyStyle创建TypographyCreate。TypographyCreate用于创建Typography
35. OH_Drawing_TypographyCreate *handlerWithoutAutoSpace = OH_Drawing_CreateTypographyHandler(typoStyle, fc);

37. // 将文本样式添加到handlerWithoutAutoSpace中
38. OH_Drawing_TypographyHandlerPushTextStyle(handlerWithoutAutoSpace, txtStyle);
39. // 将文本添加到handlerWithoutAutoSpace中
40. OH_Drawing_TypographyHandlerAddText(handlerWithoutAutoSpace, text);
41. // 创建段落
42. OH_Drawing_Typography *typographyWithoutAutoSpace = OH_Drawing_CreateTypography(handlerWithoutAutoSpace);
43. // 将段落按照排版宽度进行排版
44. OH_Drawing_TypographyLayout(typographyWithoutAutoSpace, maxWidth);
45. // 将文本绘制到画布上
46. OH_Drawing_TypographyPaint(typographyWithoutAutoSpace, cCanvas_, 0, DIV_FOUR(width_));

48. // 释放内存
49. OH_Drawing_DestroyTypographyStyle(typoStyle);
50. OH_Drawing_DestroyTextStyle(txtStyle);
51. OH_Drawing_DestroyFontCollection(fc);
52. OH_Drawing_DestroyTypographyHandler(handler);
53. OH_Drawing_DestroyTypographyHandler(handlerWithoutAutoSpace);
54. OH_Drawing_DestroyTypography(typography);
55. OH_Drawing_DestroyTypography(typographyWithoutAutoSpace);
```

[draw\_text\_impl.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/NDKComplexText1/entry/src/main/cpp/samples/draw_text_impl.cpp#L685-L741)

| 段落样式设置（自动间距） | 示意效果 |
| --- | --- |
| 不使能自动间距 |  |
| 使能自动间距 |  |

### 渐变色

**渐变色**是一种在文字设计中广泛应用的视觉效果，通过在文字的不同部分应用不同的颜色，从而创造出从一种颜色平滑过渡到另一种颜色的效果。可以通过着色器实现文字渐变的效果，着色器的更多介绍请参考[着色器效果](complex-drawing-effect-c.md#着色器效果)。

| 接口定义 | 描述 |
| --- | --- |
| void OH\_Drawing\_SetTextStyleForegroundBrush(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_Brush\* foregroundBrush) | 添加前景画刷，渐变着色器属性依附于前景画刷中。 |

示例及效果如下所示：

```
1. OH_Drawing_TypographyStyle *typoStyle = OH_Drawing_CreateTypographyStyle();
2. OH_Drawing_TextStyle *txtStyle = OH_Drawing_CreateTextStyle();
3. // 设置文字大小
4. OH_Drawing_SetTextStyleFontSize(txtStyle, DIV_TEN(width_));
5. // 创建着色器对象，并设置颜色、变化起始点与结束点
6. OH_Drawing_Point *startPt = OH_Drawing_PointCreate(0, 0);
7. // 结束点位于(900, 900)
8. OH_Drawing_Point *endPt = OH_Drawing_PointCreate(900, 900);
9. uint32_t colors[] = {0xFFFFFF00, 0xFFFF0000, 0xFF0000FF};
10. float pos[] = {0.0f, 0.5f, 1.0f};
11. // pos数组长度为3
12. OH_Drawing_ShaderEffect *colorShaderEffect =
13. OH_Drawing_ShaderEffectCreateLinearGradient(startPt, endPt, colors, pos, 3, OH_Drawing_TileMode::CLAMP);
14. // 创建画刷对象,并将着色器添加到画刷
15. OH_Drawing_Brush *brush = OH_Drawing_BrushCreate();
16. OH_Drawing_BrushSetShaderEffect(brush, colorShaderEffect);
17. // 将画刷添加到文本样式中
18. OH_Drawing_SetTextStyleForegroundBrush(txtStyle, brush);
19. // 创建排版对象，并绘制
20. OH_Drawing_FontCollection *fc = OH_Drawing_CreateSharedFontCollection();
21. OH_Drawing_TypographyCreate *handler = OH_Drawing_CreateTypographyHandler(typoStyle, fc);
22. OH_Drawing_TypographyHandlerPushTextStyle(handler, txtStyle);
23. const char *text = "Hello World";
24. OH_Drawing_TypographyHandlerAddText(handler, text);
25. OH_Drawing_Typography *typography = OH_Drawing_CreateTypography(handler);
26. // 设置页面最大宽度
27. double maxWidth = width_;
28. // 将段落按照排版宽度进行排版
29. OH_Drawing_TypographyLayout(typography, maxWidth);
30. OH_Drawing_TypographyPaint(typography, cCanvas_, 0, DIV_TEN(width_));

32. // 释放对象
33. OH_Drawing_DestroyFontCollection(fc);
34. OH_Drawing_ShaderEffectDestroy(colorShaderEffect);
35. OH_Drawing_BrushDestroy(brush);
36. OH_Drawing_DestroyTextStyle(txtStyle);
37. OH_Drawing_DestroyTypographyStyle(typoStyle);
38. OH_Drawing_DestroyTypographyHandler(handler);
39. OH_Drawing_DestroyTypography(typography);
```

[draw\_text\_impl.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/NDKComplexText1/entry/src/main/cpp/samples/draw_text_impl.cpp#L746-L786)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/M1rB0tPYQoKbkcP6D6SD0A/zh-cn_image_0000002558605540.png?HW-CC-KV=V1&HW-CC-Date=20260429T053615Z&HW-CC-Expire=86400&HW-CC-Sign=EBC25059F0DC3B78ACE37B13F0B95D65FD0CF6B1A258856F72D60CBADCB1FD00)

### 垂直对齐

**垂直对齐**用于调整文本在一行中垂直方向的排版位置。开启行高缩放或行内存在不同字号文本混排时使能垂直对齐，可以让文本实现顶部对齐、居中对齐、底部对齐或基线对齐（默认）。

| 接口定义 | 描述 |
| --- | --- |
| void OH\_Drawing\_SetTypographyVerticalAlignment(OH\_Drawing\_TypographyStyle\* style, OH\_Drawing\_TextVerticalAlignment align) | 设置文本垂直方向排版方式。 |

示例及效果如下所示：

```
1. OH_Drawing_TypographyStyle *typoStyle = OH_Drawing_CreateTypographyStyle();
2. OH_Drawing_TextStyle *txtStyle = OH_Drawing_CreateTextStyle();
3. // 设置垂直对齐方式
4. OH_Drawing_SetTypographyVerticalAlignment(typoStyle,
5. OH_Drawing_TextVerticalAlignment::TEXT_VERTICAL_ALIGNMENT_CENTER);
6. // 设置文字大小
7. OH_Drawing_SetTextStyleFontSize(txtStyle, DIV_TEN(width_));
8. // 设置文字颜色
9. OH_Drawing_SetTextStyleColor(txtStyle, OH_Drawing_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
10. // 创建排版对象，并绘制
11. OH_Drawing_FontCollection *fc = OH_Drawing_CreateSharedFontCollection();
12. OH_Drawing_TypographyCreate *handler = OH_Drawing_CreateTypographyHandler(typoStyle, fc);
13. OH_Drawing_TypographyHandlerPushTextStyle(handler, txtStyle);
14. const char *text = "VerticalAlignment-center";
15. OH_Drawing_TypographyHandlerAddText(handler, text);
16. OH_Drawing_Typography *typography = OH_Drawing_CreateTypography(handler);
17. // 设置页面最大宽度
18. double maxWidth = width_;
19. // 将段落按照排版宽度进行排版
20. OH_Drawing_TypographyLayout(typography, maxWidth);
21. OH_Drawing_TypographyPaint(typography, cCanvas_, 0, DIV_TEN(width_));

23. // 释放对象
24. OH_Drawing_DestroyFontCollection(fc);
25. OH_Drawing_DestroyTextStyle(txtStyle);
26. OH_Drawing_DestroyTypographyStyle(typoStyle);
27. OH_Drawing_DestroyTypographyHandler(handler);
28. OH_Drawing_DestroyTypography(typography);
```

[draw\_text\_impl.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/NDKComplexText1/entry/src/main/cpp/samples/draw_text_impl.cpp#L791-L820)

效果如下（黑框仅为展示文本绘制区域，实际不绘制）：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/0CfrR__bR9ancTAA9hXKnA/zh-cn_image_0000002589325053.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053615Z&HW-CC-Expire=86400&HW-CC-Sign=B159D8F1B8AB4B48F00D80613B3AF836AABA3F2766EBE884BDFACBB086EF9548)

### 上下标

**上下标**能将文本作为上标或下标参与排版。一般用于数学公式、化学式等场景。

| 接口定义 | 描述 |
| --- | --- |
| void OH\_Drawing\_SetTextStyleBadgeType(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_TextBadgeType textBadgeType) | 使能上下标样式。 |

示例及效果如下所示：

```
1. OH_Drawing_TypographyStyle *typoStyle = OH_Drawing_CreateTypographyStyle();
2. OH_Drawing_TextStyle *txtStyle = OH_Drawing_CreateTextStyle();
3. OH_Drawing_TextStyle *badgeTxtStyle = OH_Drawing_CreateTextStyle();
4. // 设置文字大小
5. OH_Drawing_SetTextStyleFontSize(txtStyle, DIV_TWENTY(width_));
6. OH_Drawing_SetTextStyleFontSize(badgeTxtStyle, DIV_TWENTY(width_));
7. // 设置文字颜色
8. OH_Drawing_SetTextStyleColor(txtStyle, OH_Drawing_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
9. OH_Drawing_SetTextStyleColor(badgeTxtStyle, OH_Drawing_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
10. // 使能文本上标
11. OH_Drawing_SetTextStyleBadgeType(badgeTxtStyle, OH_Drawing_TextBadgeType::TEXT_SUPERSCRIPT);
12. // 创建排版对象，并绘制
13. OH_Drawing_FontCollection *fc = OH_Drawing_CreateSharedFontCollection();
14. OH_Drawing_TypographyCreate *handler = OH_Drawing_CreateTypographyHandler(typoStyle, fc);
15. OH_Drawing_TypographyHandlerPushTextStyle(handler, txtStyle);
16. const char *text = "Mass-energy equivalence: E=mc";
17. OH_Drawing_TypographyHandlerAddText(handler, text);
18. OH_Drawing_TypographyHandlerPushTextStyle(handler, badgeTxtStyle);
19. const char *badgeText = "2";
20. OH_Drawing_TypographyHandlerAddText(handler, badgeText);
21. OH_Drawing_Typography *typography = OH_Drawing_CreateTypography(handler);
22. // 设置页面最大宽度
23. double maxWidth = width_;
24. // 将段落按照排版宽度进行排版
25. OH_Drawing_TypographyLayout(typography, maxWidth);
26. OH_Drawing_TypographyPaint(typography, cCanvas_, 0, DIV_TEN(width_));

28. // 释放对象
29. OH_Drawing_DestroyFontCollection(fc);
30. OH_Drawing_DestroyTextStyle(txtStyle);
31. OH_Drawing_DestroyTextStyle(badgeTxtStyle);
32. OH_Drawing_DestroyTypographyStyle(typoStyle);
33. OH_Drawing_DestroyTypographyHandler(handler);
34. OH_Drawing_DestroyTypography(typography);
```

[draw\_text\_impl.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/NDKComplexText1/entry/src/main/cpp/samples/draw_text_impl.cpp#L825-L860)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/kdSwhN59Q0ScR6OExYCAug/zh-cn_image_0000002558605528.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053615Z&HW-CC-Expire=86400&HW-CC-Sign=31AAE82620A361472E960B5417F5C4F34D9C903EDCF8E0BCCFAA0A5F826F1538)

### 高对比度

高对比度可将深色文字变黑、浅色文字变白。开发者可选择开启或关闭应用的高对比度文字渲染，或遵循系统设置中的高对比度文字配置。

| 接口定义 | 描述 |
| --- | --- |
| void OH\_Drawing\_SetTextHighContrast(OH\_Drawing\_TextHighContrast action) | 设置文字渲染高对比度模式。模式具体可参考[OH\_Drawing\_TextHighContrast](../harmonyos-references/capi-drawing-text-global-h.md#oh_drawing_texthighcontrast)。 |

示例及示意效果如下所示：

```
1. // 开启APP的文字渲染高对比模式，该模式的优先级要高于系统设置中的高对比度文字配置
2. OH_Drawing_SetTextHighContrast(TEXT_APP_ENABLE_HIGH_CONTRAST);
3. // 创建一个 TypographyStyle，创建 Typography 时需要使用
4. OH_Drawing_TypographyStyle *typoStyle = OH_Drawing_CreateTypographyStyle();

6. // 设置文字颜色、大小，不设置 TextStyle 会使用 TypographyStyle 中的默认 TextStyle
7. OH_Drawing_TextStyle *txtStyle = OH_Drawing_CreateTextStyle();
8. OH_Drawing_SetTextStyleColor(txtStyle, OH_Drawing_ColorSetArgb(0xFF, 0x6F, 0xFF, 0xFF));
9. OH_Drawing_SetTextStyleFontSize(txtStyle, DIV_TEN(width_));

11. // 创建 FontCollection，FontCollection 用于管理字体匹配逻辑
12. OH_Drawing_FontCollection *fc = OH_Drawing_CreateSharedFontCollection();
13. // 使用 FontCollection 和 之前创建的 TypographyStyle 创建 TypographyCreate
14. OH_Drawing_TypographyCreate *handler = OH_Drawing_CreateTypographyHandler(typoStyle, fc);

16. // 将之前创建的 TextStyle 加入 handler 中
17. OH_Drawing_TypographyHandlerPushTextStyle(handler, txtStyle);
18. // 设置文本内容，并将文本添加到 handler 中
19. const char *text = "Hello World Drawing\n";
20. OH_Drawing_TypographyHandlerAddText(handler, text);

22. OH_Drawing_Typography *typography = OH_Drawing_CreateTypography(handler);
23. // 设置页面最大宽度
24. double maxWidth = width_;
25. // 将段落按照排版宽度进行排版
26. OH_Drawing_TypographyLayout(typography, maxWidth);
27. // 将文本绘制到画布上
28. OH_Drawing_TypographyPaint(typography, cCanvas_, 0, DIV_TEN(width_));

30. // 释放内存
31. OH_Drawing_DestroyTypographyStyle(typoStyle);
32. OH_Drawing_DestroyTextStyle(txtStyle);
33. OH_Drawing_DestroyFontCollection(fc);
34. OH_Drawing_DestroyTypographyHandler(handler);
35. OH_Drawing_DestroyTypography(typography);
```

[draw\_text\_impl.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/NDKComplexText1/entry/src/main/cpp/samples/draw_text_impl.cpp#L865-L901)

| 高对比度设置 | 示意效果 |
| --- | --- |
| 不开启高对比度 |  |
| 开启高对比度 |  |

### 行高调整

调整行高可以改变文本行的垂直间距，行间距将变得更松散或更紧凑，可以显著改善文本垂直方向截断问题，使文本更易读。

当前行高调整方式包括两种：设置行高上限/下限和使用行高缩放系数。

**行高调整（方式一）**

从API version 21开始，支持为文本行设置行高上限与下限。

| 接口定义 | 描述 |
| --- | --- |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_SetTextStyleAttributeDouble(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_TextStyleAttributeId id, double value)](../harmonyos-references/capi-drawing-text-typography-h.md#oh_drawing_settextstyleattributedouble) | 传入id为OH\_Drawing\_TextStyleAttributeId::TEXT\_STYLE\_ATTR\_D\_LINE\_HEIGHT\_MAXIMUM，设置行高上限。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_SetTextStyleAttributeDouble(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_TextStyleAttributeId id, double value)](../harmonyos-references/capi-drawing-text-typography-h.md#oh_drawing_settextstyleattributedouble) | 传入id为OH\_Drawing\_TextStyleAttributeId::TEXT\_STYLE\_ATTR\_D\_LINE\_HEIGHT\_MINIMUM，设置行高下限。 |

示例及效果如下所示：

```
1. OH_Drawing_TypographyStyle *typoStyle = OH_Drawing_CreateTypographyStyle();
2. OH_Drawing_TextStyle *txtStyle = OH_Drawing_CreateTextStyle();
3. // 设置文字大小为50
4. OH_Drawing_SetTextStyleFontSize(txtStyle, 50);
5. // 设置文字颜色
6. OH_Drawing_SetTextStyleColor(txtStyle, OH_Drawing_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
7. OH_Drawing_SetTextStyleAttributeDouble(txtStyle,
8. OH_Drawing_TextStyleAttributeId::TEXT_STYLE_ATTR_D_LINE_HEIGHT_MAXIMUM, 65); // 设置行高上限为65
9. OH_Drawing_SetTextStyleAttributeDouble(txtStyle,
10. OH_Drawing_TextStyleAttributeId::TEXT_STYLE_ATTR_D_LINE_HEIGHT_MINIMUM, 65); // 设置行高下限为65
11. // 创建排版对象，并绘制
12. OH_Drawing_FontCollection *fc = OH_Drawing_CreateSharedFontCollection();
13. OH_Drawing_TypographyCreate *handler = OH_Drawing_CreateTypographyHandler(typoStyle, fc);
14. OH_Drawing_TypographyHandlerPushTextStyle(handler, txtStyle);
15. const char *text = "Hello World!";
16. OH_Drawing_TypographyHandlerAddText(handler, text);
17. OH_Drawing_Typography *typography = OH_Drawing_CreateTypography(handler);
18. // 排版宽度为1000
19. OH_Drawing_TypographyLayout(typography, 1000);
20. OH_Drawing_TypographyPaint(typography, cCanvas_, 0, 0);

22. // 释放对象
23. OH_Drawing_DestroyFontCollection(fc);
24. OH_Drawing_DestroyTextStyle(txtStyle);
25. OH_Drawing_DestroyTypographyStyle(typoStyle);
26. OH_Drawing_DestroyTypographyHandler(handler);
27. OH_Drawing_DestroyTypography(typography);
```

[draw\_text\_impl.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/NDKComplexText1/entry/src/main/cpp/samples/draw_text_impl.cpp#L998-L1026)

具体效果如下所示：

| 行高上限值 | 行高下限值 | 示意效果（黑框仅为展示文本绘制区域，实际不绘制） |
| --- | --- | --- |
| 65 | 65 |  |
| 200 | 200 |  |

**行高调整（方式二）**

设置行高缩放系数。

| 接口定义 | 描述 |
| --- | --- |
| [void OH\_Drawing\_SetTextStyleFontHeight(OH\_Drawing\_TextStyle\* style, double fontHeight)](../harmonyos-references/capi-drawing-text-typography-h.md#oh_drawing_settextstylefontheight) | 使能行高缩放。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_SetTextStyleAttributeInt(OH\_Drawing\_TextStyle\* style, OH\_Drawing\_TextStyleAttributeId id)](../harmonyos-references/capi-drawing-text-typography-h.md#oh_drawing_settextstyleattributeint) | 传入id为OH\_Drawing\_TextStyleAttributeId::TEXT\_STYLE\_ATTR\_I\_LINE\_HEIGHT\_STYLE，使能行高缩放样式。 |

示例及效果如下所示：

```
1. OH_Drawing_TypographyStyle *typoStyle = OH_Drawing_CreateTypographyStyle();
2. OH_Drawing_TextStyle *txtStyle = OH_Drawing_CreateTextStyle();
3. // 设置文字大小为50
4. OH_Drawing_SetTextStyleFontSize(txtStyle, 50);
5. // 设置文字颜色
6. OH_Drawing_SetTextStyleColor(txtStyle, OH_Drawing_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
7. // 设置行高缩放系数为1.5
8. OH_Drawing_SetTextStyleFontHeight(txtStyle, 1.5);
9. // 设置行高缩放样式（1代表行高缩放以字形高度作为缩放基数）
10. OH_Drawing_SetTextStyleAttributeInt(txtStyle,
11. OH_Drawing_TextStyleAttributeId::TEXT_STYLE_ATTR_I_LINE_HEIGHT_STYLE, 1);
12. // 创建排版对象，并绘制
13. OH_Drawing_FontCollection *fc = OH_Drawing_CreateSharedFontCollection();
14. OH_Drawing_TypographyCreate *handler = OH_Drawing_CreateTypographyHandler(typoStyle, fc);
15. OH_Drawing_TypographyHandlerPushTextStyle(handler, txtStyle);
16. const char *text = "Hello World!";
17. OH_Drawing_TypographyHandlerAddText(handler, text);
18. OH_Drawing_Typography *typography = OH_Drawing_CreateTypography(handler);
19. // 排版宽度为1000
20. OH_Drawing_TypographyLayout(typography, 1000);
21. OH_Drawing_TypographyPaint(typography, cCanvas_, 0, 0);

23. // 释放对象
24. OH_Drawing_DestroyFontCollection(fc);
25. OH_Drawing_DestroyTextStyle(txtStyle);
26. OH_Drawing_DestroyTypographyStyle(typoStyle);
27. OH_Drawing_DestroyTypographyHandler(handler);
28. OH_Drawing_DestroyTypography(typography);
```

[draw\_text\_impl.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/NDKComplexText1/entry/src/main/cpp/samples/draw_text_impl.cpp#L1031-L1060)

具体效果如下所示：

| 行高缩放样式 | 示意效果（黑框仅为展示文本绘制区域，实际不绘制） |
| --- | --- |
| TEXT\_LINE\_HEIGHT\_BY\_FONT\_SIZE |  |
| TEXT\_LINE\_HEIGHT\_BY\_FONT\_HEIGHT |  |

### 行间距调整

从API version 21开始，支持设置行间距可以改善文本行之间的距离，提高阅读体验。

| 接口定义 | 描述 |
| --- | --- |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_SetTypographyStyleAttributeDouble(OH\_Drawing\_TypographyStyle\* style, OH\_Drawing\_TypographyStyleAttributeId id, double value)](../harmonyos-references/capi-drawing-text-typography-h.md#oh_drawing_settypographystyleattributedouble) | 传入id为OH\_Drawing\_TypographyStyleAttributeId::TYPOGRAPHY\_STYLE\_ATTR\_D\_LINE\_SPACING，设置行间距。 |

示例及效果如下所示：

```
1. OH_Drawing_TypographyStyle *typoStyle = OH_Drawing_CreateTypographyStyle();
2. OH_Drawing_SetTypographyStyleAttributeDouble(typoStyle,
3. OH_Drawing_TypographyStyleAttributeId::TYPOGRAPHY_STYLE_ATTR_D_LINE_SPACING, 100); // 设置行间距为100
4. OH_Drawing_TextStyle *txtStyle = OH_Drawing_CreateTextStyle();
5. // 设置文字大小为50
6. OH_Drawing_SetTextStyleFontSize(txtStyle, 50);
7. // 设置文字颜色
8. OH_Drawing_SetTextStyleColor(txtStyle, OH_Drawing_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
9. // 创建排版对象，并绘制
10. OH_Drawing_FontCollection *fc = OH_Drawing_CreateSharedFontCollection();
11. OH_Drawing_TypographyCreate *handler = OH_Drawing_CreateTypographyHandler(typoStyle, fc);
12. OH_Drawing_TypographyHandlerPushTextStyle(handler, txtStyle);
13. const char *text = "Hello World!";
14. OH_Drawing_TypographyHandlerAddText(handler, text);
15. OH_Drawing_Typography *typography = OH_Drawing_CreateTypography(handler);
16. // 排版宽度为200
17. OH_Drawing_TypographyLayout(typography, 200);
18. OH_Drawing_TypographyPaint(typography, cCanvas_, 0, 0);

20. // 释放对象
21. OH_Drawing_DestroyFontCollection(fc);
22. OH_Drawing_DestroyTextStyle(txtStyle);
23. OH_Drawing_DestroyTypographyStyle(typoStyle);
24. OH_Drawing_DestroyTypographyHandler(handler);
25. OH_Drawing_DestroyTypography(typography);
```

[draw\_text\_impl.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/NDKComplexText1/entry/src/main/cpp/samples/draw_text_impl.cpp#L1065-L1091)

具体效果如下所示：

| 上升部下降部开关 | 示意效果（黑框仅为展示文本绘制区域，实际不绘制） |
| --- | --- |
| TEXT\_HEIGHT\_DISABLE\_ALL |  |
| TEXT\_HEIGHT\_ALL |  |

## 样式的拷贝、绘制与显示

支持拷贝文本样式、段落样式、阴影样式，以便快速复制相关样式作用到不同文字上。

| 接口定义 | 描述 |
| --- | --- |
| OH\_Drawing\_TypographyStyle\* OH\_Drawing\_CopyTypographyStyle(OH\_Drawing\_TypographyStyle\* style) | 创建一个段落样式的对象副本，用于拷贝一个已有的段落样式对象。 |
| OH\_Drawing\_TextStyle\* OH\_Drawing\_CopyTextStyle(OH\_Drawing\_TextStyle\* style) | 创建一个文本样式的对象副本，用于拷贝一个已有的文本样式对象。 |
| OH\_Drawing\_TextShadow\* OH\_Drawing\_CopyTextShadow(OH\_Drawing\_TextShadow\* shadow) | 创建一个文本阴影的对象副本，用于拷贝一个已有的文本阴影对象。 |

示例及示意效果如下所示：

```
1. // 创建一个TypographyStyle，其中创建Typography时需要使用
2. OH_Drawing_TypographyStyle *typoStyle = OH_Drawing_CreateTypographyStyle();
3. // 配置段落样式包括：使能自动间距、最大行数、省略号样式、省略号文本、对齐方式
4. // 使能自动间距
5. OH_Drawing_SetTypographyTextAutoSpace(typoStyle, true);
6. // 设置段落最大行数为3行
7. OH_Drawing_SetTypographyTextMaxLines(typoStyle, 3);
8. // 设置省略号模式为尾部省略号
9. OH_Drawing_SetTypographyTextEllipsisModal(typoStyle, ELLIPSIS_MODAL_TAIL);
10. // 设置省略号文本
11. OH_Drawing_SetTypographyTextEllipsis(typoStyle, "...");
12. // 设置对齐方式为居中对齐
13. OH_Drawing_SetTypographyTextAlign(typoStyle, TEXT_ALIGN_CENTER);

15. OH_Drawing_TextStyle *txtStyle = OH_Drawing_CreateTextStyle();
16. // 设置文字颜色、大小、字重，不设置TextStyle会使用TypographyStyle中的默认TextStyle
17. OH_Drawing_SetTextStyleColor(txtStyle, OH_Drawing_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
18. OH_Drawing_SetTextStyleFontSize(txtStyle, DIV_TEN(width_));
19. // 设置文本的装饰线
20. // 添加下划线
21. OH_Drawing_SetTextStyleDecoration(txtStyle, TEXT_DECORATION_UNDERLINE);
22. // 设置装饰线样式为波浪线样式
23. OH_Drawing_SetTextStyleDecorationStyle(txtStyle, TEXT_DECORATION_STYLE_WAVY);
24. // 设置下划线粗细
25. OH_Drawing_SetTextStyleDecorationThicknessScale(txtStyle, 1);
26. // 设置下划线颜色为蓝色
27. OH_Drawing_SetTextStyleDecorationColor(txtStyle, OH_Drawing_ColorSetArgb(0xFF, 0x00, 0x00, 0xFF));

29. // 设置阴影的颜色、偏移量、模糊半径
30. // 创建阴影对象
31. OH_Drawing_TextShadow *shadow = OH_Drawing_CreateTextShadow();
32. // 设置阴影偏移量为(5, 5)
33. OH_Drawing_Point *offset = OH_Drawing_PointCreate(5, 5);
34. // 定义阴影模糊半径为4
35. double blurRadius = 4;
36. OH_Drawing_SetTextShadow(shadow, OH_Drawing_ColorSetArgb(0xFF, 0xFF, 0x00, 0xFF), offset, blurRadius);

38. // 拷贝阴影对象
39. OH_Drawing_TextShadow *shadowCopy = OH_Drawing_CopyTextShadow(shadow);
40. // 将拷贝出的阴影添加到文本样式中
41. OH_Drawing_TextStyleAddShadow(txtStyle, shadowCopy);

43. // 创建FontCollection，FontCollection用于管理字体匹配逻辑
44. OH_Drawing_FontCollection *fc = OH_Drawing_CreateSharedFontCollection();

46. // 使用FontCollection和之前创建的TypographyStyle创建TypographyCreate。TypographyCreate用于创建Typography
47. OH_Drawing_TypographyCreate *handler = OH_Drawing_CreateTypographyHandler(typoStyle, fc);
48. // 将段落一文本样式添加到handler中
49. OH_Drawing_TypographyHandlerPushTextStyle(handler, txtStyle);
50. // 将段落一文本添加到handler中
51. const char *text = "The text style, paragraph style, and text shadow of the copied text will be exactly the same "
52. "as those of the original text.";
53. OH_Drawing_TypographyHandlerAddText(handler, text);
54. // 创建段落一，并将段落一按照排版宽度进行排版
55. OH_Drawing_Typography *typography = OH_Drawing_CreateTypography(handler);
56. double maxWidth = width_;
57. OH_Drawing_TypographyLayout(typography, maxWidth);
58. OH_Drawing_TypographyPaint(typography, cCanvas_, 0, DIV_TEN(width_));

60. // 生成第二段文本，其中，文本样式和段落样式均由第一段文本拷贝而来
61. // 复制文本样式
62. OH_Drawing_TextStyle *textStyleCopy = OH_Drawing_CopyTextStyle(txtStyle);
63. // 复制段落样式
64. OH_Drawing_TypographyStyle *typographyStyleCopy = OH_Drawing_CopyTypographyStyle(typoStyle);

66. // 使用复制的样式创建段落二，后续可以观察段落一和段落二是否绘制效果一致
67. OH_Drawing_TypographyCreate *handlerCopy = OH_Drawing_CreateTypographyHandler(typographyStyleCopy, fc);
68. OH_Drawing_TypographyHandlerPushTextStyle(handlerCopy, textStyleCopy);
69. OH_Drawing_TypographyHandlerAddText(handlerCopy, text);
70. OH_Drawing_Typography *typographyCopy = OH_Drawing_CreateTypography(handlerCopy);
71. OH_Drawing_TypographyLayout(typographyCopy, maxWidth);
72. OH_Drawing_TypographyPaint(typographyCopy, cCanvas_, 0, DIV_TWO(width_));

74. // 释放内存
75. OH_Drawing_DestroyFontCollection(fc);
76. OH_Drawing_DestroyTypographyStyle(typoStyle);
77. OH_Drawing_DestroyTextStyle(txtStyle);
78. OH_Drawing_DestroyTypographyHandler(handler);
79. OH_Drawing_DestroyTypography(typography);
80. // 拷贝的段落样式也需要释放内存
81. OH_Drawing_DestroyTypographyStyle(typographyStyleCopy);
82. // 拷贝的文本样式也需要释放内存
83. OH_Drawing_DestroyTextStyle(textStyleCopy);
84. OH_Drawing_DestroyTypographyHandler(handlerCopy);
85. OH_Drawing_DestroyTypography(typographyCopy);
```

[draw\_text\_impl.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/NDKComplexText1/entry/src/main/cpp/samples/draw_text_impl.cpp#L907-L993)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/mR1Up08eQHelfTV7acJk3w/zh-cn_image_0000002558765198.png?HW-CC-KV=V1&HW-CC-Date=20260429T053615Z&HW-CC-Expire=86400&HW-CC-Sign=F67253680C5E805200AAAD8909EECDB50B5AEF395AC2B9B17A12407972B5B508)
