---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/system-font-arkts
title: 系统字体的信息获取和使用（ArkTS）
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 文本 > 字体管理 > 系统字体的信息获取和使用（ArkTS）
category: harmonyos-guides
scraped_at: 2026-04-29T13:36:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bc59057aa0ebb1b6bdd373e2540323eeb5980dbae3df8460f097afc5ca26bd75
---

## 场景介绍

系统字体是指操作系统预设的字体，用于在没有指定自定义字体时显示文本，确保文本的可读性和一致性。

**使用系统字体**的情况通常是在应用未注册自定义字体，或在没有显式指定文本样式时，系统会使用默认的系统字体。另外，系统字体有多种，开发者可以先获取系统字体的配置信息，并根据信息中的字体家族名来进行系统字体的切换和使用。

当前ArkTS侧暂不支持禁用系统字体，Native侧支持禁用系统字体。

## 接口说明

以下是系统字体相关的常用接口和结构体，ArkTS侧对外接口由ArkUI提供，详细接口说明请见[@ohos.font](../harmonyos-references/js-apis-font.md)。

| 接口名 | 描述 |
| --- | --- |
| getUIFontConfig() : UIFontConfig | 获取系统字体配置。 |

## 获取系统字体信息

1. 导入依赖的相关模块。

   ```
   1. import { font } from '@kit.ArkUI'
   ```
2. 获取系统字体信息。

   ```
   1. let fontConfig = font.getUIFontConfig();
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/SystemFontInfoGet/entry/src/main/ets/pages/Index.ets#L140-L142)
3. 在获取系统字体信息之后通过日志打印字体信息。

   ```
   1. console.info('sysFontMfg::font-dir -----------' + String(fontConfig.fontDir.length));
   2. for (let i = 0; i < fontConfig.fontDir.length; i++) {
   3. console.info(fontConfig.fontDir[i]);
   4. }
   5. console.info('sysFontMfg::generic-------------' + String(fontConfig.generic.length));
   6. for (let i = 0; i < fontConfig.generic.length; i++) {
   7. console.info('sysFontMfg::family:' + fontConfig.generic[i].family);
   8. for (let j = 0; j < fontConfig.generic[i].alias.length; j++) {
   9. console.info(fontConfig.generic[i].alias[j].name + ' ' + fontConfig.generic[i].alias[j].weight);
   10. }
   11. }
   12. console.info('sysFontMfg::fallback------------' + String(fontConfig.fallbackGroups.length));
   13. for (let i = 0; i < fontConfig.fallbackGroups.length; i++) {
   14. console.info('sysFontMfg::fontSetName:' + fontConfig.fallbackGroups[i].fontSetName);
   15. for (let j = 0; j < fontConfig.fallbackGroups[i].fallback.length; j++) {
   16. console.info('sysFontMfg::language:' + fontConfig.fallbackGroups[i].fallback[j].language + ' family:' +
   17. fontConfig.fallbackGroups[i].fallback[j].family);
   18. }
   19. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/SystemFontInfoGet/entry/src/main/ets/pages/Index.ets#L144-L164)

以下打印的示例为应用设备系统对应的部分系统字体配置信息情况，不同设备系统配置信息可能不同，此处仅示意。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/xmewWXtRRneGK_9bD8M0qA/zh-cn_image_0000002558605516.png?HW-CC-KV=V1&HW-CC-Date=20260429T053613Z&HW-CC-Expire=86400&HW-CC-Sign=07635E23EE53C9A42AD247F842FD5F212E6FFD2EEBC2847CB18D32DBC8224342)

## 使用或切换系统字体

系统字体可以有多种，可以先获取系统字体配置信息，再根据其中的字体家族名（即TextStyle中的fontFamilies）来进行系统字体的切换和使用。

如果不指定使用任何字体时，会使用系统默认字体“HarmonyOS Sans”显示文本。

1. 导入依赖的相关模块。

   ```
   1. import { text } from '@kit.ArkGraphics2D';
   ```
2. 创建textStyle1，指定fontFamilies为“HarmonyOS Sans SC”，默认中文字体为“HarmonyOS Sans SC”。

   ```
   1. let textStyle1: text.TextStyle = {
   2. color: { alpha: 255, red: 255, green: 0, blue: 0 },
   3. fontSize: 100,
   4. fontFamilies: ['HarmonyOS Sans SC']
   5. };
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/SystemFontInfoGet/entry/src/main/ets/pages/Index.ets#L28-L34)
3. 创建textStyle2，指定fontFamilies为“HarmonyOS Sans TC”（该两种字体易于观察同一文字字型差异）。

   ```
   1. let textStyle2: text.TextStyle = {
   2. color: { alpha: 255, red: 255, green: 0, blue: 0 },
   3. fontSize: 100,
   4. fontFamilies: ['HarmonyOS Sans TC']
   5. };
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/SystemFontInfoGet/entry/src/main/ets/pages/Index.ets#L36-L42)
4. 创建段落生成器。

   ```
   1. // 创建一个段落样式对象，以设置排版风格
   2. let myParagraphStyle: text.ParagraphStyle = {
   3. textStyle: textStyle1,
   4. align: 3,
   5. wordBreak: text.WordBreak.NORMAL
   6. };
   7. // 获取全局字体集实例
   8. let fontCollection = text.FontCollection.getGlobalInstance(); //获取Arkui全局FC
   9. // 创建一个段落生成器
   10. let ParagraphGraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/SystemFontInfoGet/entry/src/main/ets/pages/Index.ets#L44-L55)
5. 先后将textStyle1和textStyle2添加到段落样式中并添加文字。

   ```
   1. let str:string = '模块描述\n';
   2. // 添加第一种文本样式和对应文本内容
   3. ParagraphGraphBuilder.pushStyle(textStyle1);
   4. ParagraphGraphBuilder.addText(str);
   5. // 添加第二种文本样式和对应文本内容
   6. ParagraphGraphBuilder.pushStyle(textStyle2);
   7. ParagraphGraphBuilder.addText(str);
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/SystemFontInfoGet/entry/src/main/ets/pages/Index.ets#L57-L65)
6. 生成段落，用于后续绘制使用。

   ```
   1. let paragraph = ParagraphGraphBuilder.build();
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/TextEngine/SystemFontInfoGet/entry/src/main/ets/pages/Index.ets#L68-L70)

效果展示如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/2KAFCNA8TTKsXgGQQCv6EQ/zh-cn_image_0000002589325043.png?HW-CC-KV=V1&HW-CC-Date=20260429T053613Z&HW-CC-Expire=86400&HW-CC-Sign=FC13EF8875AFC9BFD86078A51823FFFBA9BAC9AA404BEBB03AC6E22F6204A0C5)
