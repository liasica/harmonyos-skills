---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-971
title: Canvas绘制时如何使fillStyle可以使用Resource颜色资源
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Canvas绘制时如何使fillStyle可以使用Resource颜色资源
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:02+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:36db7cba430741312ab66d0481c5255d7d84978de39b108302d357e2e851998b
---

## 问题现象

在Canvas画布上绘制时，fillStyle用于设置画笔的填充颜色，但fillStyle只接受number或string类型的颜色资源，不接受Resource类型的颜色资源（即$r('xxx')的引用方式），如何使得fillStyle可以使用引用资源的方式设置颜色？

## 背景知识

* [Canvas](../harmonyos-references/ts-components-canvas-canvas.md)是画布组件，规定用于绘制的区域。
* [CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md)是画笔，用于绘制内容到Canvas上。[fillStyle](../harmonyos-references/ts-components-canvas-common-property.md#fillstyle)是CanvasRenderingContext2D的属性，用于设置画笔的颜色。
* [Resource](../harmonyos-references/ts-types.md#resource)是资源引用类型，fillStyle无法接受Resource作为参数类型。
* [getColorSync](../harmonyos-references/js-apis-resource-manager.md#getcolorsync10)是[@ohos.resourceManager (资源管理)](../harmonyos-references/js-apis-resource-manager.md)中的方法，可以将一个Resource类型的颜色资源变成一个number类型。

## 解决方案

1. 在EntryAbility中通过AppStorage存储context，以便调用resourceManager。

   ```ts
   onWindowStageCreate(windowStage: window.WindowStage): void {
     let context = this.context;
     AppStorage.setOrCreate('context', context);
     // Main window is created, set main page for this ability
     hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

     windowStage.loadContent('pages/Index', (err) => {
       if (err.code) {
         hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
         return;
       }
       hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
     });
   }
   ```
2. 通过@ohos.resourceManager (资源管理)的getColorSync方法，将$r('xxx')方式获取的静态颜色资源转变为number类型的颜色值。

   **说明** 

   getColorSync方法不支持dark目录下的深色模式颜色。

   ```ts
   import { common } from '@kit.AbilityKit';

   @Entry
   @Component
   struct FillRect {
     private settings: RenderingContextSettings = new RenderingContextSettings(true);
     private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
     private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

     build() {
       Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
         Canvas(this.context)
           .width('100%')
           .height('100%')
           .onReady(() => {
             let context = AppStorage.get('context') as common.Context;
             let colorNumber = context.resourceManager.getColorSync($r('app.color.test').id);
             let offContext = this.offCanvas.getContext('2d', this.settings);
             offContext.shadowBlur = 30;
             offContext.shadowColor = '#5291FF';
             offContext.fillStyle = colorNumber.toString();
             offContext.fillRect(30, 30, 100, 100);
             let image = this.offCanvas.transferToImageBitmap();
             this.context.transferFromImageBitmap(image);
           });
       }
       .width('100%')
       .height('100%');
     }
   }
   ```

   ```json
   {
     "color": [
       {
         "name": "test",
         "value": "#5291FF"
       }
     ]
   }
   ```
