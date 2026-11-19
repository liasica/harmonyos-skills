---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-custom-symbol-res-register
title: 应用加载自定义Symbol
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 应用加载自定义Symbol
category: harmonyos-guides
scraped_at: 2026-11-19T09:47:59+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:903adc7a4d6a010113004b98b0ed6b172919749a037c8a3442ebbbadaee67600
---

## 场景介绍

从5.1.1 (19)版本开始，新增支持资源注册。

适用于需要快速定制应用内[Symbol图标](../harmonyos-references/ui-design-symbolregister.md)，不想强依赖于系统版本中预制的系统Symbol图标资源。

## 约束条件

资源注册支持Phone、Tablet、PC/2in1设备。

## 开发步骤

1. 将Symbol图标资源（TTF文件，设计规范参见[图标设计文档](../design-guides/system-icons-0000001929854962.md#section26702397263)）与动效参数资源（JSON文件）放入entry/src/main/resources/rawfile目录下，可在此目录下新建子目录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/7o65asP7TdyejxFpCkBxPg/zh-cn_image_0000002820405633.png?HW-CC-KV=V1&HW-CC-Date=20261119T014759Z&HW-CC-Expire=31536000000&HW-CC-Sign=723DC4AF41BA901805DC4FF3F9E76EF699257AA4FED64FA5033C5D7959E17EBD)
2. 多语言场景，在entry/src/main/resources目录中对应语言目录下的string.json文件中配置对应的Symbol图标Unicode值。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/D1kP8EBjRHyRHgYN0D1rKQ/zh-cn_image_0000002791725654.png?HW-CC-KV=V1&HW-CC-Date=20261119T014759Z&HW-CC-Expire=31536000000&HW-CC-Sign=295B0C316A79C6C038FEF2A42D35F1D2D979EFF687CAE1796984C6F2E73FAF66)

   ```json
   {
     "string": [
       {
         "name": "symbol_custom_phone_fill_1",
         "value": "0x100016"
       }
     ]
   }
   ```
3. 导入相关模块。

   ```typescript
   import { symbolRegister } from '@kit.UIDesignKit'
   import { BusinessError } from '@kit.BasicServicesKit'
   ```
4. 在通过SymbolGlyph/SymbolSpan组件展示自定义Symbol图标前，需要注册加载图标资源与动效参数资源。在需要展示自定义Symbol图标的页面通过SymbolGlyph/SymbolSpan组件展示该图标。

   ```typescript
   @Entry
   @Component
   struct Index {
     aboutToAppear(): void {
       try {
         let result = symbolRegister.registerSymbol($rawfile("symbol/symbol_register.ttf"), $rawfile("symbol/symbol_register.json"));
       } catch (error) {
         let err = error as BusinessError;
         console.error("errCode: " + err.code)
         console.error("error: " + err.message);
       }
     }
     build() {
       Column(){
         SymbolGlyph($r('app.string.symbol_custom_phone_fill_1'))
       }
       .width('100%')
       .height('100%')
     }
   }
   ```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/50cjWY0qTgCp72mlZGRsIg/zh-cn_image_0000002791565682.png?HW-CC-KV=V1&HW-CC-Date=20261119T014759Z&HW-CC-Expire=31536000000&HW-CC-Sign=76897A133E6E45830CCB85E2F3A524D7C95432447DAA9286EAA50F8CCF492B35)
