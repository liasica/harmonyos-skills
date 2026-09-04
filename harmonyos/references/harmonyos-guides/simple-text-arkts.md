---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/simple-text-arkts
title: 简单文本绘制与显示（ArkTS）
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 文本 > 文本绘制与显示 > 简单文本绘制与显示（ArkTS）
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:49e1e3589f93399eb0021161b92297a298dca27ed762767d465a14b34db84b4c
---

## 场景介绍

在一个简单的用户界面中，可能只需要展示几行静态文本，例如标签、按钮上的文字、菜单项或状态栏中的提示信息。此时，开发者只需要选择合适的字体、大小和颜色即可完成渲染。

## 相关属性

此场景示例，涉及到的文本样式属性如下，具体及更多文本样式可参考[TextStyle](../harmonyos-references/js-apis-graphics-text.md#textstyle)。

* color：字体颜色，默认为白色。请注意与画布颜色进行区分，以保证文本的正常显示。
* fontSize：字体大小，浮点数，默认为14.0，单位为物理像素px。

## 开发步骤

1. 通过context获取到Canvas画布对象。

   ```typescript
   let canvas = context.canvas;
   ```
2. 初始化文本样式，此处设置字体颜色为红色，字体大小为100px。

   ```typescript
   // 初始化文本样式
   let myTextStyle: text.TextStyle = {
     // 文本颜色
     color: {
       alpha: 255,
       red: 255,
       green: 0,
       blue: 0
     },
     // 文本大小
     fontSize: 100
   };
   ```
3. 初始化段落样式。

   ```typescript
   let myParagraphStyle: text.ParagraphStyle = {
     textStyle: myTextStyle,
   };
   ```
4. 初始化段落对象，并添加文本。

   ```typescript
   let fontCollection = text.FontCollection.getGlobalInstance();
   let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
   // 更新文本样式
   paragraphBuilder.pushStyle(myTextStyle);
   // 添加文本
   paragraphBuilder.addText("Hello World");
   ```
5. 排版段落并进行文本绘制。

   ```typescript
   // 生成段落
   let paragraph = paragraphBuilder.build();
   // 布局
   paragraph.layoutSync(1250);
   // 绘制文本
   paragraph.paint(canvas, 0, 100);
   ```

## 效果展示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/icWIJG3vQ6ugiaba2L3vqA/zh-cn_image_0000002742003861.png)
