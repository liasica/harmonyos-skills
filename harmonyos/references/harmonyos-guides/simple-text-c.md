---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/simple-text-c
title: 简单文本绘制与显示（C/C++）
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 文本 > 文本绘制与显示 > 简单文本绘制与显示（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-29T13:36:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:505d6b6a676ccae45c08f2ec15cbe92028a381c64c2907d88605e14782d18be0
---

## 场景介绍

在一个简单的用户界面中，可能只需要展示几行静态文本，例如标签、按钮上的文字、菜单项或状态栏中的提示信息。此时，开发者只需要选择合适的字体、大小和颜色即可完成渲染。

## 接口说明

| 接口定义 | 描述 |
| --- | --- |
| OH\_Drawing\_TextStyle\* OH\_Drawing\_CreateTextStyle(void) | 创建指向OH\_Drawing\_TextStyle对象的指针。 |
| void OH\_Drawing\_SetTextStyleFontSize(OH\_Drawing\_TextStyle\* style, double fontSize) | 设置字号。 |
| void OH\_Drawing\_SetTextStyleFontWeight(OH\_Drawing\_TextStyle\* style, int fontWeight) | 设置字重。目前只有系统默认字体支持字重的调节，其他字体设置字重值小于semi-bold时字体粗细无变化，当设置字重值大于等于semi-bold时可能会触发伪加粗效果。 |

## 开发步骤

1. 创建Canvas画布对象，画布Canvas对象创建方法具体可见[画布的获取与绘制结果的显示](canvas-get-result-draw-c.md)。
2. 初始化段落样式，设置文本对齐方式为居中对齐。

   ```
   1. // 创建一个 TypographyStyle 创建 Typography 时需要使用
   2. OH_Drawing_TypographyStyle *typoStyle = OH_Drawing_CreateTypographyStyle();
   3. // 设置文本对齐方式为居中
   4. OH_Drawing_SetTypographyTextAlign(typoStyle, TEXT_ALIGN_CENTER);
   ```

   [sample\_bitmap.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/NDKDrawingSimpleText/entry/src/main/cpp/samples/sample_bitmap.cpp#L165-L170)
3. 初始化文本样式，此处设置字体颜色为纯黑色，字体大小为60，字重为400。

   ```
   1. // 设置文字颜色、大小、字重，不设置 TextStyle 会使用 TypographyStyle 中的默认 TextStyle
   2. OH_Drawing_TextStyle *txtStyle = OH_Drawing_CreateTextStyle();
   3. OH_Drawing_SetTextStyleColor(txtStyle, OH_Drawing_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
   4. OH_Drawing_SetTextStyleFontSize(txtStyle, 60);
   5. OH_Drawing_SetTextStyleFontWeight(txtStyle, FONT_WEIGHT_400);
   ```

   [sample\_bitmap.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/NDKDrawingSimpleText/entry/src/main/cpp/samples/sample_bitmap.cpp#L172-L178)
4. 初始化段落对象，并添加文本。

   ```
   1. // 创建 FontCollection，FontCollection 用于管理字体匹配逻辑
   2. OH_Drawing_FontCollection *fc = OH_Drawing_CreateFontCollection();
   3. // 使用 FontCollection 和 之前创建的 TypographyStyle 创建 TypographyCreate。TypographyCreate 用于创建 Typography
   4. OH_Drawing_TypographyCreate *handler = OH_Drawing_CreateTypographyHandler(typoStyle, fc);

   6. // 将之前创建的 TextStyle 加入 handler 中
   7. OH_Drawing_TypographyHandlerPushTextStyle(handler, txtStyle);
   8. // 设置文本内容，并将文本添加到 handler 中
   9. const char *text = "Hello World Drawing\n";
   10. OH_Drawing_TypographyHandlerAddText(handler, text);

   12. OH_Drawing_Typography *typography = OH_Drawing_CreateTypography(handler);
   ```

   [sample\_bitmap.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/NDKDrawingSimpleText/entry/src/main/cpp/samples/sample_bitmap.cpp#L180-L193)
5. 排版段落并进行文本绘制。

   ```
   1. // 设置页面最大宽度
   2. double maxWidth = width_;
   3. OH_Drawing_TypographyLayout(typography, maxWidth);
   4. // 将文本绘制到画布上
   5. OH_Drawing_TypographyPaint(typography, cCanvas_, 0, 100);
   ```

   [sample\_bitmap.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/NDKDrawingSimpleText/entry/src/main/cpp/samples/sample_bitmap.cpp#L195-L201)
6. 释放内存

   ```
   1. // 释放内存
   2. OH_Drawing_DestroyTypographyStyle(typoStyle);
   3. OH_Drawing_DestroyTextStyle(txtStyle);
   4. OH_Drawing_DestroyFontCollection(fc);
   5. OH_Drawing_DestroyTypographyHandler(handler);
   6. OH_Drawing_DestroyTypography(typography);
   ```

   [sample\_bitmap.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/NDKDrawingSimpleText/entry/src/main/cpp/samples/sample_bitmap.cpp#L203-L210)

## 效果展示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/uw9VCROoRWmWhwm87hHp7w/zh-cn_image_0000002589244995.png?HW-CC-KV=V1&HW-CC-Date=20260429T053615Z&HW-CC-Expire=86400&HW-CC-Sign=CC228E7068A6959658B455F4B1EE85D9AC742D7399BFAEDC74A10C5AA7112A4C)
