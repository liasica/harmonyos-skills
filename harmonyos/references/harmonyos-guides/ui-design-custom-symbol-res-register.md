---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-custom-symbol-res-register
title: 应用加载自定义Symbol
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 应用加载自定义Symbol
category: harmonyos-guides
scraped_at: 2026-11-21T09:11:25+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:25d05831d6820c858272165a163758dd73431856536422778201148fb277f3db
---

## 场景介绍

从5.1.1 (19)版本开始，新增支持资源注册。

适用于需要快速定制应用内[Symbol图标](../harmonyos-references/ui-design-symbolregister.md)，不想强依赖于系统版本中预制的系统Symbol图标资源。

## 约束条件

资源注册支持Phone、Tablet、PC/2in1设备。

## 开发步骤

1. 将Symbol图标资源（TTF文件，设计规范参见[图标设计文档](../design-guides/system-icons-0000001929854962.md#section26702397263)）与动效参数资源（JSON文件）放入entry/src/main/resources/rawfile目录下，可在此目录下新建子目录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/YNx8VFwfRKCeLRqKbOCzpg/zh-cn_image_0000002792877334.png?HW-CC-KV=V1&HW-CC-Date=20261121T011125Z&HW-CC-Expire=31536000000&HW-CC-Sign=E5A548E0B71DE490EDD6195FB3CBB32B2969C1719EC4B101EC2947663BD1E236)
2. 多语言场景，在entry/src/main/resources目录中对应语言目录下的string.json文件中配置对应的Symbol图标Unicode值。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/NoT-XnJrRJWdMe4VUTCeCQ/zh-cn_image_0000002821837241.png?HW-CC-KV=V1&HW-CC-Date=20261121T011125Z&HW-CC-Expire=31536000000&HW-CC-Sign=C1418AF2F82E99BA1C883824A422BCCE3E795FB21D3113A04231B9AC8D62264B)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/1KIIeqnwQKqd9iTuIzxqug/zh-cn_image_0000002821757243.png?HW-CC-KV=V1&HW-CC-Date=20261121T011125Z&HW-CC-Expire=31536000000&HW-CC-Sign=E7C66AB69419D75AB0664FA308408479CA94DAFBE20A1E66DB991B67E7A95A87)
