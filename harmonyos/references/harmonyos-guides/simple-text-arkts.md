---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/simple-text-arkts
title: 简单文本绘制与显示（ArkTS）
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 文本 > 文本绘制与显示 > 简单文本绘制与显示（ArkTS）
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0769703bc91ce29721f31215c4eb7a37168d5bf942dfddf2de57fca250e5976a
---

## 场景介绍

在一个简单的用户界面中，可能只需要展示几行静态文本，例如标签、按钮上的文字、菜单项或状态栏中的提示信息。此时，开发者只需要选择合适的字体、大小和颜色即可完成渲染。

## 相关属性

此场景示例，涉及到的文本样式属性如下，具体及更多文本样式可参考[TextStyle](../harmonyos-references/js-apis-graphics-text.md#textstyle)。

* color：字体颜色，默认为白色。请注意与画布颜色进行区分，以保证文本的正常显示。
* fontSize：字体大小，浮点数，默认为14.0，单位为物理像素px。

## 开发步骤

1. 通过context获取到Canvas画布对象。

   ```
   1. let canvas = context.canvas;
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/SimpleTextDrawing/entry/src/main/ets/pages/Index.ets#L26-L28)
2. 初始化文本样式，此处设置字体颜色为红色，字体大小为50。

   ```
   1. // 获取文本样式
   2. let myTextStyle: text.TextStyle = {
   3. // 文本颜色
   4. color: {
   5. alpha: 255,
   6. red: 255,
   7. green: 0,
   8. blue: 0
   9. },
   10. // 文本大小
   11. fontSize: 100
   12. };
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/SimpleTextDrawing/entry/src/main/ets/pages/Index.ets#L29-L42)
3. 初始化段落样式。

   ```
   1. let myParagraphStyle: text.ParagraphStyle = {
   2. textStyle: myTextStyle,
   3. };
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/SimpleTextDrawing/entry/src/main/ets/pages/Index.ets#L44-L48)
4. 初始化段落对象，并添加文本。

   ```
   1. let fontCollection = text.FontCollection.getGlobalInstance();
   2. let ParagraphGraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
   3. // 更新文本样式
   4. ParagraphGraphBuilder.pushStyle(myTextStyle);
   5. // 添加文本
   6. ParagraphGraphBuilder.addText("Hello World");
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/SimpleTextDrawing/entry/src/main/ets/pages/Index.ets#L49-L56)
5. 排版段落并进行文本绘制。

   ```
   1. // 生成段落
   2. let paragraph = ParagraphGraphBuilder.build();
   3. // 布局
   4. paragraph.layoutSync(1250);
   5. // 绘制文本
   6. paragraph.paint(canvas, 0, 100);
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/SimpleTextDrawing/entry/src/main/ets/pages/Index.ets#L58-L65)

## 效果展示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/iM-jeO9zRHa4aZ1DBaeuLA/zh-cn_image_0000002552799026.png?HW-CC-KV=V1&HW-CC-Date=20260427T234715Z&HW-CC-Expire=86400&HW-CC-Sign=308FE3EDFBBAE4BFBD0E92BB83A9E7583190812D7BA14560E91AD6B978D5D824)
