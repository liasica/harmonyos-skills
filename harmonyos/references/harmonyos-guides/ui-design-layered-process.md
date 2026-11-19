---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-layered-process
title: （推荐）分层图标处理
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 图标处理 > （推荐）分层图标处理
category: harmonyos-guides
scraped_at: 2026-11-19T09:47:59+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:78b93c9d5b4ede8fbb427452b49b284db2a552f3d6df314ed0f083068ca31076
---

## 场景介绍

从5.0.0(12)版本开始， Hds支持分层图标处理能力。

适用于图标为分层资源，且图标展示风格要与华为HarmonyOS Design System设计风格一致的应用场景。以下是一些典型的应用场景：

* 展示带图标的应用列表：可调用UI Design Kit批量处理分层图标的接口获取处理后的应用图标。
* 展示应用详情：可调用UI Design Kit处理单个分层图标的接口获取处理后的应用图标。
* 展示跟随在线主题的应用图标：可调用UI Design Kit处理分层图标的接口获取主题换肤后的应用图标。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/zQsMOI9LRmWyW9Vuod-Vfw/zh-cn_image_0000002791725634.png?HW-CC-KV=V1&HW-CC-Date=20261119T014707Z&HW-CC-Expire=31536000000&HW-CC-Sign=4CD3C27CC9745DFDF3FBA0B2575F679EAC422B3D17EA013AF1133C0EFECA4141)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/3z5burueTpycaqsuVIix9w/zh-cn_image_0000002791565662.png?HW-CC-KV=V1&HW-CC-Date=20261119T014707Z&HW-CC-Expire=31536000000&HW-CC-Sign=98E8257A5A92EF6F686A59C4041B6D2123B670BE404EDEF950EBC823F72640DA)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/vHV2w5t3Rki30_eGkQoOHw/zh-cn_image_0000002820525615.png?HW-CC-KV=V1&HW-CC-Date=20261119T014707Z&HW-CC-Expire=31536000000&HW-CC-Sign=AC29A825CE575BB6A247901183FD956C76560492CC99A3DDDBA4107ED025D62F)

## 约束条件

分层图标处理支持Phone、Tablet、PC/2in1设备，并且从5.1.1(19)版本开始，新增支持TV设备。

## 开发步骤

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/8aElA3EmSEaZadI-r0WFNA/zh-cn_image_0000002820405615.png?HW-CC-KV=V1&HW-CC-Date=20261119T014707Z&HW-CC-Expire=31536000000&HW-CC-Sign=F2C07640A6FE5AB696D38058FF9366E76A27E82A0A3871F0F83788B0C8504910)

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
