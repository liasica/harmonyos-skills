---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/simple-text-c
title: 简单文本绘制与显示（C/C++）
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 文本 > 文本绘制与显示 > 简单文本绘制与显示（C/C++）
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8de2604a7702b1ca6cab9ed6d072efa44ac751a00bb6c43806cbc32661dc5d7a
---

## 场景介绍

在一个简单的用户界面中，可能只需要展示几行静态文本，例如标签、按钮上的文字、菜单项或状态栏中的提示信息。此时，开发者只需要选择合适的字体、大小和颜色即可完成渲染。

## 接口说明

简单文本绘制的相关接口如下所示，详细接口说明请参考[drawing\_text\_typography.h](../harmonyos-references/capi-drawing-text-typography-h.md)。

| 接口定义 | 描述 |
| --- | --- |
| OH\_Drawing\_TextStyle\* OH\_Drawing\_CreateTextStyle(void) | 创建指向OH\_Drawing\_TextStyle对象的指针。 |
| void OH\_Drawing\_SetTextStyleFontSize(OH\_Drawing\_TextStyle\* style, double fontSize) | 设置字号。 |
| void OH\_Drawing\_SetTextStyleFontWeight(OH\_Drawing\_TextStyle\* style, int fontWeight) | 设置字重。 |

## 开发步骤

1. 创建Canvas画布对象，画布Canvas对象创建方法具体可见[画布的获取与绘制结果的显示](canvas-get-result-draw-c.md)。
2. 初始化段落样式，设置文本对齐方式为居中对齐。

   ```
   // 创建一个 TypographyStyle 创建 Typography 时需要使用
   OH_Drawing_TypographyStyle *typoStyle = OH_Drawing_CreateTypographyStyle();
   // 设置文本对齐方式为居中
   OH_Drawing_SetTypographyTextAlign(typoStyle, TEXT_ALIGN_CENTER);
   ```
3. 初始化文本样式，此处设置字体颜色为纯黑色，字体大小为60，字重为400。

   ```
   // 设置文字颜色、大小、字重，不设置 TextStyle 会使用 TypographyStyle 中的默认 TextStyle
   OH_Drawing_TextStyle *txtStyle = OH_Drawing_CreateTextStyle();
   OH_Drawing_SetTextStyleColor(txtStyle, OH_Drawing_ColorSetArgb(0xFF, 0x00, 0x00, 0x00));
   OH_Drawing_SetTextStyleFontSize(txtStyle, 60);
   OH_Drawing_SetTextStyleFontWeight(txtStyle, FONT_WEIGHT_400);
   ```
4. 初始化段落对象，并添加文本。

   ```
   // 创建 FontCollection，FontCollection 用于管理字体匹配逻辑
   OH_Drawing_FontCollection *fc = OH_Drawing_CreateFontCollection();
   // 使用 FontCollection 和 之前创建的 TypographyStyle 创建 TypographyCreate。TypographyCreate 用于创建 Typography
   OH_Drawing_TypographyCreate *handler = OH_Drawing_CreateTypographyHandler(typoStyle, fc);

   // 将之前创建的 TextStyle 加入 handler 中
   OH_Drawing_TypographyHandlerPushTextStyle(handler, txtStyle);
   // 设置文本内容，并将文本添加到 handler 中
   const char *text = "Hello World Drawing\n";
   OH_Drawing_TypographyHandlerAddText(handler, text);

   OH_Drawing_Typography *typography = OH_Drawing_CreateTypography(handler);
   ```
5. 排版段落并进行文本绘制。

   ```
   // 设置页面最大宽度
   double maxWidth = width_;
   OH_Drawing_TypographyLayout(typography, maxWidth);
   // 将文本绘制到画布上
   OH_Drawing_TypographyPaint(typography, cCanvas_, 0, 100);
   ```
6. 释放内存

   ```
   // 释放内存
   OH_Drawing_DestroyTypographyStyle(typoStyle);
   OH_Drawing_DestroyTextStyle(txtStyle);
   OH_Drawing_DestroyFontCollection(fc);
   OH_Drawing_DestroyTypographyHandler(handler);
   OH_Drawing_DestroyTypography(typography);
   ```

## 效果展示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/SP_cqlh0RFSZlIP6H2EFxw/zh-cn_image_0000002742003883.png)
