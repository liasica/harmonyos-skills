---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-21
title: 如何加载和使用自定义字体
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何加载和使用自定义字体
category: harmonyos-faqs
scraped_at: 2026-10-28T07:47:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3d8a0959d7cc4d021a538919a61fd5b403643f08c4e2578222dc58250cd4fa72
---

1. 字体管理中[@ohos.font (注册自定义字体)](../harmonyos-references/js-apis-font.md)。

   **说明** 

   从DevEco Studio 6.0.0 Beta2版本开始，新建工程或模块时，默认创建的模块不会对非resources目录下的资源进行打包，需使能相关开关：模块的build-profile.json5中buildOption > resOptions > copyCodeResource > enable设置为true，详见resOptions中[copyCodeResource](../harmonyos-guides/ide-hvigor-build-profile.md#table1476161719356)相关介绍。
2. 设置对应文本的字体家族。可参考以下代码：

   ```ts
   // xxx.ets
   import { Font } from '@kit.ArkUI';

   @Entry
   @Component
   struct FontExample {
     @State message: string = 'Hello World';

     aboutToAppear() {
       // Register in black font
       let font: Font = this.getUIContext().getFont()
       font.registerFont({
         familyName: 'Condensed_Black', // Registered font name
         familySrc: '/font/Sans_Condensed_Black.ttf' // The font folder is at the same level as the pages directory
       })

       // Register in black oblique font
       font.registerFont({
         familyName: 'Condensed_Black_Italic', // Registered font name
         familySrc: '/font/Sans_Condensed_Black_Italic.ttf' // The font folder is at the same level as the pages directory
       })
     }

     build() {
       Column() {
         Text(this.message)
           .align(Alignment.Center)
           .fontSize(50)
           .fontFamily('Condensed_Black') // Use black font
         Text(this.message)
           .align(Alignment.Center)
           .fontSize(50)
           .fontFamily('Condensed_Black_Italic') // Use black oblique font
         Text(this.message)
           .align(Alignment.Center)
           .fontSize(50)
       }
       .width('100%')
       .margin({ top: 30 })
     }
   }
   ```

效果如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/qFK1Ho_PRpKmXSoR76FNIQ/zh-cn_image_0000002654835219.png "点击放大")
