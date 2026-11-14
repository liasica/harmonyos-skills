---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-custom-symbol-res-register
title: 应用加载自定义Symbol
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 应用加载自定义Symbol
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:21+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:9adc5ca2d94fa9cabc38247cef55f2ff4aca6e6f0821b25aae1571597adc7213
---

## 场景介绍

从5.1.1 (19)版本开始，新增支持资源注册。

适用于需要快速定制应用内[Symbol图标](../harmonyos-references/ui-design-symbolregister.md)，不想强依赖于系统版本中预制的系统Symbol图标资源。

## 约束条件

资源注册支持Phone、Tablet、PC/2in1设备。

## 开发步骤

1. 将Symbol图标资源（TTF文件，设计规范参见[图标设计文档](../design-guides/system-icons-0000001929854962.md#section26702397263)）与动效参数资源（JSON文件）放入entry/src/main/resources/rawfile目录下，可在此目录下新建子目录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/eQFf0LdxQbmEYxz1ahGkfw/zh-cn_image_0000002788307354.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=728476AE09DA2490893EBFF92A67439F52A757285A0D209E1EC6551B0A007040)
2. 多语言场景，在entry/src/main/resources目录中对应语言目录下的string.json文件中配置对应的Symbol图标Unicode值。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/AK-peHhlRXietvGGS1cEIg/zh-cn_image_0000002817426717.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=86335569188410CEA42D8FCB644298975026DD7ACB85B680E48A99FC5A58C031)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/bSQX0j_eQYGW9InHQQtp6Q/zh-cn_image_0000002788467298.png?HW-CC-KV=V1&HW-CC-Date=20261114T004721Z&HW-CC-Expire=31536000000&HW-CC-Sign=924F8225CEE46119D613D712E2FFCF3D2FBE754CEC212C313E95052ECDCDBDCC)
