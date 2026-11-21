---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-layered-process
title: （推荐）分层图标处理
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 图标处理 > （推荐）分层图标处理
category: harmonyos-guides
scraped_at: 2026-11-21T09:11:25+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:9e994ca8ef4274540dd8c2af913774638985bba94a454305189efa4054804e54
---

## 场景介绍

从5.0.0(12)版本开始， Hds支持分层图标处理能力。

适用于图标为分层资源，且图标展示风格要与华为HarmonyOS Design System设计风格一致的应用场景。以下是一些典型的应用场景：

* 展示带图标的应用列表：可调用UI Design Kit批量处理分层图标的接口获取处理后的应用图标。
* 展示应用详情：可调用UI Design Kit处理单个分层图标的接口获取处理后的应用图标。
* 展示跟随在线主题的应用图标：可调用UI Design Kit处理分层图标的接口获取主题换肤后的应用图标。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/mw9CXpIvSLC1sttHPptmPg/zh-cn_image_0000002821837221.png?HW-CC-KV=V1&HW-CC-Date=20261121T011125Z&HW-CC-Expire=31536000000&HW-CC-Sign=824AE57D391CEF3E051C1A6E09C3A12D5FDD84852AA6A15369D44DE81BC5F247)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/A2-STuGFS22Xs4V7Z7GR0g/zh-cn_image_0000002821757223.png?HW-CC-KV=V1&HW-CC-Date=20261121T011125Z&HW-CC-Expire=31536000000&HW-CC-Sign=8749AF4258FB87F3AC62FAF018E7DEE50DB078D3D13D797852635CF19B23FF51)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/mbhS1_gISg6v-P5rUfFfIw/zh-cn_image_0000002793037286.png?HW-CC-KV=V1&HW-CC-Date=20261121T011125Z&HW-CC-Expire=31536000000&HW-CC-Sign=6B4F1CA71254D58B90EE574772C18FAB7B3642507A3E6F34FF6AD520729ADD7D)

## 约束条件

分层图标处理支持Phone、Tablet、PC/2in1设备，并且从5.1.1(19)版本开始，新增支持TV设备。

## 开发步骤

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/kI_PuVDmT1qFZuRyhbUAxw/zh-cn_image_0000002792877316.png?HW-CC-KV=V1&HW-CC-Date=20261121T011125Z&HW-CC-Expire=31536000000&HW-CC-Sign=D6CF28FCA8BD991F18A9FDACFA6F4CE464B65A16B080A0054AC46A14A96A24F9)

1. 设置分层图标，将前景资源和背景资源放至entry/src/main/resources/base/media文件中，并在该目录下创建一个json文件（例如：drawable.json）：

   ```json
   {
     "layered-image":
     {
       "background" : "$media:background",
       "foreground" : "$media:foreground"
     }
   }
   ```
2. 将图标处理的相关类添加至工程。

   ```typescript
   import { LayeredDrawableDescriptor } from '@kit.ArkUI';
   import { hdsDrawable } from '@kit.UIDesignKit';
   import { image } from '@kit.ImageKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { resourceManager } from '@kit.LocalizationKit';
   import { common } from '@kit.AbilityKit';
   ```
3. 简单配置页面的布局，调用[分层图标接口](../harmonyos-references/ui-design-hdsdrawable.md#hdsdrawablegethdslayeredicon)获取处理后的图标信息，也可以调用[异步批量处理接口](../harmonyos-references/ui-design-hdsdrawable.md#hdsdrawablegethdslayeredicons)。

   ```typescript
   @Entry
   @Component
   struct Index{
     bundleName: string = 'com.example.uidesignsample';
     resManager: resourceManager.ResourceManager | undefined = undefined;
     layeredDrawableDescriptor: LayeredDrawableDescriptor | undefined = undefined;
     @State layeredIconsResult: Array<hdsDrawable.ProcessedIcon> = [];

     build() {
       Column() {
         Column() {
           Text('getHdsLayeredIcon')
             .fontWeight(FontWeight.Bold)
             .fontSize(16)
             .margin(5)

           Image(this.getHdsLayeredIcon())
             .width(48)
             .height(48)
         }
         .margin(20)

         Text('getHdsLayeredIcons')
           .fontWeight(FontWeight.Bold)
           .fontSize(16)
           .margin(5)

         List() {
           ForEach(this.layeredIconsResult,
             (item: hdsDrawable.ProcessedIcon, index?: number) => {
               ListItem() {
                 Column() {
                   Text(item.bundleName)
                     .fontWeight(FontWeight.Medium)
                     .fontSize(16)
                     .margin(5)

                   Image(item.pixelMap)
                     .width(48)
                     .height(48)
                 }
                 .margin(15)
               }
               .width('100%')
             }, (item: hdsDrawable.ProcessedIcon) => item.toString())
         }
         .scrollBar(BarState.On)
         .height('60%')
       }
       .height('100%')
       .width('100%')
     }

     aboutToAppear(): void {
       // 获取资源管理器
       this.resManager = (this.getUIContext().getHostContext() as common.UIAbilityContext)?.resourceManager;
       if (!this.resManager) {
         return;
       }
       // 通过资源管理获取原始分层图标信息
       this.layeredDrawableDescriptor = (this.resManager.getDrawableDescriptor($r('app.media.drawable')
         .id)) as LayeredDrawableDescriptor;
       this.getHdsLayeredIcons();
     }

     private getHdsLayeredIcon(): image.PixelMap | null {
       try {
         // 调用HDS分层图标接口处理图标
         return hdsDrawable.getHdsLayeredIcon(this.bundleName, this.layeredDrawableDescriptor, 48, true);
       } catch (err) {
         let message = (err as BusinessError).message;
         let code = (err as BusinessError).code;
         console.error(`getHdsLayeredIcon failed, code: ${code}, message: ${message}`);
         return null;
       }
     }

     private getHdsLayeredIcons(): void {
       if (!this.layeredDrawableDescriptor) {
         console.error(`getHdsLayeredIcons layeredDrawableDescriptor is undefined.`);
         return;
       }

       // 构造批量接口传参
       let options: hdsDrawable.Options = {
         size: 48,
         hasBorder: true,
         parallelNumber: 4
       };

       let layeredIcons: hdsDrawable.LayeredIcon[] = [];
       for (let i = 0; i < 10; i++) {
         layeredIcons.push({
           bundleName: `${this.bundleName}-${i}`,
           layeredDrawableDescriptor: this.layeredDrawableDescriptor
         });
       }

       try {
         // 调用HDS批量分层接口处理图标
         hdsDrawable.getHdsLayeredIcons(layeredIcons, options)
           .then((data: Array<hdsDrawable.ProcessedIcon>) => {
             console.info(`getHdsLayeredIcons data size: ${data.length}`);
             this.layeredIconsResult = data;
           })
           .catch((err: BusinessError) => {
             console.error(`getHdsLayeredIcons return error, code: ${err.code}, msg: ${err.message}`);
           });
       } catch (err) {
         let message = (err as BusinessError).message;
         let code = (err as BusinessError).code;
         console.error(`getHdsLayeredIcons failed, code: ${code}, message: ${message}`);
       }
     }
   }
   ```
