---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/system-font-arkts
title: 系统字体的信息获取和使用（ArkTS）
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 文本 > 字体管理 > 系统字体的信息获取和使用（ArkTS）
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:06+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:75eb435e0d42871bf82f874e0d749f3cb525d2f0f1647f170856297cd99da283
---

## 场景介绍

系统字体是指操作系统预设的字体，用于在没有指定自定义字体时显示文本，确保文本的可读性和一致性。

**使用系统字体**的情况通常是在应用未注册自定义字体，或在没有显式指定文本样式时，系统会使用默认的系统字体。另外，系统字体有多种，开发者可以先获取系统字体的配置信息，并根据信息中的字体家族名来进行系统字体的切换和使用。

当前ArkTS侧暂不支持禁用系统字体，Native侧支持禁用系统字体。

## 接口说明

以下是系统字体相关的常用接口和结构体，ArkTS侧对外接口由ArkUI提供，详细接口说明请见[@ohos.font](../harmonyos-references/js-apis-font.md)。

| 接口名 | 描述 |
| --- | --- |
| getUIFontConfig(): UIFontConfig | 获取系统字体配置。 |

## 获取系统字体信息

1. 导入依赖的相关模块。

   ```ts
   import { font } from '@kit.ArkUI'
   ```
2. 获取系统字体信息。

   ```typescript
   let fontConfig = font.getUIFontConfig();
   ```
3. 在获取系统字体信息之后通过日志打印字体信息。

   ```typescript
   console.info('sysFontMfg::font-dir -----------' + String(fontConfig.fontDir.length));
   for (let i = 0; i < fontConfig.fontDir.length; i++) {
     console.info(fontConfig.fontDir[i]);
   }
   console.info('sysFontMfg::generic-------------' + String(fontConfig.generic.length));
   for (let i = 0; i < fontConfig.generic.length; i++) {
     console.info('sysFontMfg::family:' + fontConfig.generic[i].family);
     for (let j = 0; j < fontConfig.generic[i].alias.length; j++) {
       console.info(fontConfig.generic[i].alias[j].name + ' ' + fontConfig.generic[i].alias[j].weight);
     }
   }
   console.info('sysFontMfg::fallback------------' + String(fontConfig.fallbackGroups.length));
   for (let i = 0; i < fontConfig.fallbackGroups.length; i++) {
     console.info('sysFontMfg::fontSetName:' + fontConfig.fallbackGroups[i].fontSetName);
     for (let j = 0; j < fontConfig.fallbackGroups[i].fallback.length; j++) {
       console.info('sysFontMfg::language:' + fontConfig.fallbackGroups[i].fallback[j].language + ' family:' +
         fontConfig.fallbackGroups[i].fallback[j].family);
     }
   }
   ```

以下打印的示例为应用设备系统对应的部分系统字体配置信息情况，不同设备系统配置信息可能不同，此处仅示意。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/Cuh4TWCOQyaqtWMzuDAUWw/zh-cn_image_0000002788307778.png?HW-CC-KV=V1&HW-CC-Date=20261114T004623Z&HW-CC-Expire=31536000000&HW-CC-Sign=1E404F25C890A5A7B7B5E80A279CA3BE72780FA722643DC1230D280DA16D2DB1)

## 使用或切换系统字体

系统字体可以有多种，可以先获取系统字体配置信息，再根据其中的字体家族名（即TextStyle中的fontFamilies）来进行系统字体的切换和使用。

如果不指定使用任何字体时，会使用系统默认字体“HarmonyOS Sans”显示文本。

1. 导入依赖的相关模块。

   ```ts
   import { text } from '@kit.ArkGraphics2D';
   ```
2. 创建textStyle1，指定fontFamilies为“HarmonyOS Sans SC”，默认中文字体为“HarmonyOS Sans SC”。

   ```typescript
   let textStyle1: text.TextStyle = {
     color: { alpha: 255, red: 255, green: 0, blue: 0 },
     fontSize: 100,
     fontFamilies: ['HarmonyOS Sans SC']
   };
   ```
3. 创建textStyle2，指定fontFamilies为“HarmonyOS Sans TC”（该两种字体易于观察同一文字字型差异）。

   ```typescript
   let textStyle2: text.TextStyle = {
     color: { alpha: 255, red: 255, green: 0, blue: 0 },
     fontSize: 100,
     fontFamilies: ['HarmonyOS Sans TC']
   };
   ```
4. 创建段落生成器。

   ```typescript
   // 创建一个段落样式对象，以设置排版风格
   let myParagraphStyle: text.ParagraphStyle = {
     textStyle: textStyle1,
     align: text.TextAlign.JUSTIFY,
     wordBreak: text.WordBreak.NORMAL
   };
   // 获取全局字体集实例
   let fontCollection = text.FontCollection.getGlobalInstance();
   // 创建一个段落生成器
   let paragraphBuilder = new text.ParagraphBuilder(myParagraphStyle, fontCollection);
   ```
5. 先后将textStyle1和textStyle2添加到段落样式中并添加文字。

   ```typescript
   let str: string = '模块描述\n';
   // 添加第一种文本样式和对应文本内容
   paragraphBuilder.pushStyle(textStyle1);
   paragraphBuilder.addText(str);
   // 添加第二种文本样式和对应文本内容
   paragraphBuilder.pushStyle(textStyle2);
   paragraphBuilder.addText(str);
   ```
6. 生成段落，用于后续绘制使用。

   ```typescript
   let paragraph = paragraphBuilder.build();
   ```

效果展示如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/-VqrCND5QV6Xr5SgaN19dA/zh-cn_image_0000002817427141.png?HW-CC-KV=V1&HW-CC-Date=20261114T004623Z&HW-CC-Expire=31536000000&HW-CC-Sign=C7035372C5788A07361651B7C293B5C6897185150DDA64381451FB349DB88AA5)
