---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-26
title: 运动轨迹如何分享为图片
breadcrumb: FAQ > 图形开发 > 2D图形（ArkGraphics 2D） > 运动轨迹如何分享为图片
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:46+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:95943d88e3956ecbbf4f084059b0de224854553c87c7f5b5aa45c69bfa252d91
---

## 问题现象

华为运动健康分享运动轨迹为图片的功能使用了什么方法？应用拿到轨迹点坐标，如何绘制轨迹路线并生成图片？

## 背景知识

* [对挂树组件截图](../harmonyos-guides/arkts-uicontext-component-snapshot.md#对挂树组件截图)：对已明确挂树的组件进行截图，可通过get或getSync实现，传入组件标识（需提前通过.id通用属性配置）以指定组件根节点。系统在通过指定的ID查找待截图组件时，仅遍历已挂树的组件，不对cache或离屏组件进行查找。系统以第一个查找到的结果为准，故应用需确保组件标识ID的唯一性。
* [对离线组件截图](../harmonyos-guides/arkts-uicontext-component-snapshot.md#对离线组件截图)：离线组件不参与真实渲染，因此对其截图需要更长的时间，因为系统必须先进行离线构建、布局及资源加载等操作，在这些操作完成前执行的截图所获位图不符合预期。因此，通常需要通过设置delay参数指定足够的时间，确保系统能够完成这些操作。
* [CanvasRenderingContext2D](../harmonyos-references/js-components-canvas-canvasrenderingcontext2d.md)：用于在画布组件上绘制矩形、文本、图片等。
* [OffscreenCanvas](../harmonyos-references/ts-components-offscreencanvas.md)：提供了一个可以在屏幕外渲染的画布，用于绘制自定义图形。
* [packToFile](../harmonyos-references/arkts-apis-image-imagepacker.md#packtofile11-3)：图片编码进文件，通过传入对应的文件路径，编码后的PixelMap数据将直接写入文件。

## 解决方案

获取运动轨迹路线，可以使用Map Kit或Canvas绘制轨迹路线后将图片保存，两种方案的实现参考如下。

* 基于Map Kit实现轨迹绘制：
  1. 基于Map Kit使用[addTraceOverlay](../harmonyos-references/map-map-mapcomponentcontroller.md#addtraceoverlay)将一系列经纬度轨迹点绘制成动态轨迹路线，可参考[移动轨迹追踪](../architecture-guides/map_location-0000002385607421.md)。
  2. 通过[组件截图](../harmonyos-references/js-apis-arkui-componentsnapshot.md)将绘制完成的图片保存，关于组件截图可参考下述代码。

     ```ts
     // Trace是组件id标识，仅作参考，实际请以需要截图的组件为准
     let pixelMap = this.uiContext.getComponentSnapshot().getSync('Trace', { scale: 1, waitUntilRenderFinished: true });
     if (pixelMap !== undefined) {
       this.savePixelToSandbox(pixelMap);
     }
     ```
  3. 获取生成的轨迹图片后，若需将图片保存至图库中，可以将获取的PixelMap存入应用沙箱中，并获取图片的应用沙箱路径使用[安全控件、弹窗授权实现媒体资源保存](faqs-media-library-28.md)。保存至媒体库后，可以通过[系统分享](../harmonyos-references/share-system-share.md)将图片分享至需要的应用中。将PixelMap保存至应用沙箱参考如下：

     ```ts
     async savePixelToSandbox(pixel: image.PixelMap | undefined) {
       let imageFile: fs.File | null = null;
       try {
         let context = this.uiContext.getHostContext();
         let cacheDir = context?.filesDir;
         let filePath = `${cacheDir}` + '/test.png';
         imageFile = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
         // 绘制内容写进图片文件里。
         await image.createImagePacker().packToFile(pixel, imageFile.fd, {
           format: 'image/png',
           quality: 80
         }).then(() => {
           console.info(`Success to save image`);
         }).catch((error: BusinessError) => {
           console.error(`Failed to pack the image to file.code ${error.code},message is ${error.message}`);
         });
       } catch (err) {
         console.error(`Failed to save image: ${err.message}`);
       } finally {
         if (imageFile) {
           fs.closeSync(imageFile);
         }
       }
     }
     ```
* 基于Canvas实现轨迹绘制：
  1. 若需要保存一张透明背景的运动轨迹路线，不显示地图中的其他元素，可以将地图上的经纬度坐标，通过[toScreenLocation](../harmonyos-references/map-map-projection.md#toscreenlocation)转化为屏幕坐标后，使用CanvasRenderingContext2D或OffscreenCanvas绘制轨迹路线，画布绘制自定义轨迹可参考以下代码：

     ```ts
     private onDraw = () => {
       this.context.lineCap = this.lineCap;
       if (this.linesStyle != undefined) {
         // 设置轨迹图的颜色
         this.context.strokeStyle = this.linesStyle;
         this.context.lineWidth = this.axisWidth;
         // 开始绘制，根据坐标自定义路径
         this.context.beginPath();
         this.context.moveTo(30, 30);
         this.context.lineTo(60, 80);
         this.context.lineTo(100, 50);
         this.context.lineTo(200, 320);
         this.context.lineTo(240, 360);
         // 结束绘制轨迹图
         this.context.stroke();
         this.pixelmap = this.context.getPixelMap(0, 0, 400, 400); // 创建PixelMap对象
       }
     };
     ```
  2. 使用Canvas绘制透明背景图片也可以使用组件截图保存所需要的图片（参考Map Kit绘制中的步骤2），若只需获取绘制图片可以使用[getPixelMap](../harmonyos-references/ts-components-canvas-common-method.md#getpixelmap)获取绘制区域：

     ```ts
     this.pixelmap = this.context.getPixelMap(0, 0, 400, 400); // 创建PixelMap对象
     ```
  3. 获取图片保存媒体库后进行分享，参考Map Kit绘制中的步骤3。

  完整示例参考如下：

  ```ts
  import image from '@ohos.multimedia.image';
  import fs from '@ohos.file.fs';
  import { BusinessError } from '@kit.BasicServicesKit';
  @Entry
  @Component
  struct GetTracePixel {
    @State pixelmap: image.PixelMap | undefined = undefined;
    private settings: RenderingContextSettings = new RenderingContextSettings(true);
    private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
    public lineCap: CanvasLineCap = 'round';
    // 绘制轨迹的线条宽度
    public axisWidth: number = 6;
    // 轨迹图样式
    public linesStyle?: string | CanvasGradient | CanvasPattern = '#ff0099ff';
    private uiContext = this.getUIContext();

    async savePixelToSandbox(pixel: image.PixelMap | undefined) {
      let imageFile: fs.File | null = null;
      try {
        let context = this.uiContext.getHostContext();
        let cacheDir = context?.filesDir;
        let filePath = `${cacheDir}` + '/test.png';
        imageFile = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
        // 绘制内容写进图片文件里。
        await image.createImagePacker().packToFile(pixel, imageFile.fd, {
          format: 'image/png',
          quality: 80
        }).then(() => {
          console.info(`Success to save image`);
        }).catch((error: BusinessError) => {
          console.error(`Failed to pack the image to file.code ${error.code},message is ${error.message}`);
        });
      } catch (err) {
        console.error(`Failed to save image: ${err.message}`);
      } finally {
        if (imageFile) {
          fs.closeSync(imageFile);
        }
      }
    }
    build() {
      Column({space:20}) {
        Canvas(this.context)
          .width('70%')
          .height('70%')
          .onReady(this.onDraw)
          .id('Trace');
        Button('保存PixelMap至应用沙箱')
          .onClick(() => {
            if (this.pixelmap !== undefined) {
              this.savePixelToSandbox(this.pixelmap);
            }
          });
        Button('组件截图保存')
          .onClick(() => {
            // Trace是组件id标识，仅作参考，实际请以需要截图的组件为准
            let pixelMap = this.uiContext.getComponentSnapshot().getSync('Trace', { scale: 1, waitUntilRenderFinished: true });
            if (pixelMap !== undefined) {
              this.savePixelToSandbox(pixelMap);
            }
          });
      }
      .width('100%')
      .height('100%');
    }

    private onDraw = () => {
      this.context.lineCap = this.lineCap;
      if (this.linesStyle != undefined) {
        // 设置轨迹图的颜色
        this.context.strokeStyle = this.linesStyle;
        this.context.lineWidth = this.axisWidth;
        // 开始绘制，根据坐标自定义路径
        this.context.beginPath();
        this.context.moveTo(30, 30);
        this.context.lineTo(60, 80);
        this.context.lineTo(100, 50);
        this.context.lineTo(200, 320);
        this.context.lineTo(240, 360);
        // 结束绘制轨迹图
        this.context.stroke();
        this.pixelmap = this.context.getPixelMap(0, 0, 400, 400); // 创建PixelMap对象
      }
    };
  }
  ```

## 总结

将图片运动轨迹保存为图片可参考以下步骤：

1. 使用Map Kit或Canvas绘制轨迹路线。
2. 获取轨迹路线图片，不同组件使用及适用场景参考如下。

| 绘制工具 | 图片获取方式 | 适用场景 |
| --- | --- | --- |
| Map Kit | 屏幕截图。 | 简单的图片截图分享。 |
| Canvas | 屏幕截图，或是获取坐标后绘制。 | 通过坐标绘制动态展示运动轨迹变化后，保存屏幕截图或保存透明背景的运动轨迹图片。 |

3. 将图片保存至应用沙箱中，并通过安全控件等方式将图片保存至媒体库中，使用系统分享能力完成图片分享。
