---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-normal-process
title: 单层图标处理
breadcrumb: 指南 > 应用框架 > UI Design Kit（UI设计套件） > 图标处理 > 单层图标处理
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:58+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:080e3d333ea656ba8e2dd9c1f5c0215180e71d3efa67c22c6b36a83cd00115e4
---

## 场景介绍

从5.0.0(12)版本开始， Hds支持单层图标处理能力。

适用于图标为单层资源，且图标展示风格要与华为HarmonyOS Design System设计风格一致的应用场景，典型应用场景可参考分层图标[场景介绍](ui-design-layered-process.md#场景介绍)。

## 约束条件

单层图标处理支持Phone、Tablet、PC/2in1设备，并且从5.1.1(19)版本开始，新增支持TV设备。

## 开发步骤

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/zRgzd11aR_G8-x0TNFlmug/zh-cn_image_0000002706834226.png)

1. 在entry/src/main/resources/base/media下，配置一张图片资源normal\_icon.png。
2. 将图标处理的相关类添加至工程。

   ```typescript
   import { LayeredDrawableDescriptor, DrawableDescriptor } from '@kit.ArkUI';
   import { hdsDrawable } from '@kit.UIDesignKit';
   import { image } from '@kit.ImageKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { resourceManager } from '@kit.LocalizationKit';
   import { common } from '@kit.AbilityKit';
   ```
3. 简单配置页面的布局，调用[单层图标接口](../harmonyos-references/ui-design-hdsdrawable.md#hdsdrawablegethdsicon)获取处理后的图标信息，也可以调用[异步批量处理接口](../harmonyos-references/ui-design-hdsdrawable.md#hdsdrawablegethdsicons)。

   ```typescript
   @Entry
   @Component
   struct Index{
     bundleName: string = 'com.example.uidesignsample';
     resManager: resourceManager.ResourceManager | undefined = undefined;
     layeredDrawableDescriptor: LayeredDrawableDescriptor | undefined = undefined;
     drawableDescriptor: DrawableDescriptor | undefined = undefined;
     @State iconsResult: Array<hdsDrawable.ProcessedIcon> = [];

     build() {
       Column() {
         Column() {
           Text('getHdsIcon')
             .fontWeight(FontWeight.Bold)
             .fontSize(16)
             .margin(5)

           Image(this.getHdsIcon())
             .width(48)
             .height(48)
         }
         .margin(20)

         Text('getHdsIcons')
           .fontWeight(FontWeight.Bold)
           .fontSize(16)
           .margin(5)

         List() {
           ForEach(this.iconsResult,
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

       // 通过资源管理获取分层图标信息
       this.layeredDrawableDescriptor = (this.resManager.getDrawableDescriptor($r('app.media.drawable').id)) as LayeredDrawableDescriptor;

       // 通过资源管理获取单层图标信息
       this.drawableDescriptor =
         (this.resManager?.getDrawableDescriptor($r('app.media.normal_icon').id)) as DrawableDescriptor;

       this.getHdsIcons();
     }

     private getHdsIcon(): image.PixelMap | null {
       try {
         // 调用HDS单层图标接口
         return hdsDrawable.getHdsIcon(this.bundleName, this.drawableDescriptor?.getPixelMap(), 48,
           this.layeredDrawableDescriptor?.getMask().getPixelMap(), true);
       } catch (err) {
         let message = (err as BusinessError).message;
         let code = (err as BusinessError).code;
         console.error(`getHdsIcon failed, code: ${code}, message: ${message}`);
         return null;
       }
     }

     getHdsIcons(): void {
       if (!this.drawableDescriptor) {
         console.error(`getHdsIcons drawableDescriptor is undefined.`);
         return;
       }

       if (!this.layeredDrawableDescriptor) {
         console.error(`getHdsIcons layeredDrawableDescriptor is undefined.`);
         return;
       }

       // 构造批量接口传参
       let options: hdsDrawable.Options = {
         size: 48,
         hasBorder: true,
         parallelNumber: 4
       };

       let icons: hdsDrawable.Icon[] = [];
       for (let i = 0; i < 10; i++) {
         icons.push({
           bundleName: `${this.bundleName}-${i}`,
           pixelMap: this.drawableDescriptor.getPixelMap()
         })
       }

       try {
         // 调用HDS单层批量接口处理图标
         hdsDrawable.getHdsIcons(icons, this.layeredDrawableDescriptor.getMask().getPixelMap(), options)
           .then((data: hdsDrawable.ProcessedIcon[]) => {
             console.info(`getHdsIcons data size: ${data.length}`);
             this.iconsResult = data;
           })
           .catch((err: BusinessError) => {
             console.error(`getHdsIcons error, code: ${err.code}, msg: ${err.message}`);
           });
       } catch (err) {
         let message = (err as BusinessError).message;
         let code = (err as BusinessError).code;
         console.error(`getHdsIcons callback failed: ${message}, code: ${code}`);
       }
     }
   }
   ```
