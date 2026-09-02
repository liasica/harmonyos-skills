---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-36
title: 横竖屏切换时，如何防止画布被清空
breadcrumb: FAQ > 图形开发 > 2D图形（ArkGraphics 2D） > 横竖屏切换时，如何防止画布被清空
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:46+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ac0b2fa1975ab0cc568c66031d602faa5ff5363094f38e89ceca53fce167df75
---

## 问题现象

横竖屏切换时，画布中的内容被清空。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/b6xSu_oWSdKeBodxAm9X7g/zh-cn_image_0000002658792623.png "点击放大")

## 背景知识

* [Canvas.onReady](../harmonyos-references/ts-components-canvas-canvas.md#onready)：Canvas组件初始化完成或者发生大小变化时的事件回调，当该事件被触发时画布被清空。
* [CanvasRenderingContext2D.getImageData](../harmonyos-references/js-components-canvas-canvasrenderingcontext2d.md#getimagedata)：以当前Canvas指定区域内的像素创建ImageData对象。
* [CanvasRenderingContext2D.putImageData](../harmonyos-references/js-components-canvas-canvasrenderingcontext2d.md#putimagedata)：使用ImageData数据填充新的矩形区域。

## 问题定位

1. 横竖屏切换时，输出如下日志，画布大小发生改变，触发重置。

   ```shell
   C01406/com.example/OHOS::RS      com.example      I     RSCanvasDrawingNode::ResetSurface id:271995983888411 width:2760 height:1256
   C01406/com.example/OHOS::RS      com.example      I     RSCanvasDrawingNode::ResetSurface id:271995983888411 width:1256 height:2760
   ```
2. 画布重置后会触发onReady，需要排查onReady中是否有恢复画布的逻辑。

## 分析结论

横竖屏切换时画布的大小会发生改变，当画布的大小发生改变时，画布中的内容会被清空，所以需要在onReady方法中实现恢复画布的逻辑，而该应用未实现。

## 修改建议

恢复画布样例如下。

```ts
import common from '@ohos.app.ability.common';
import window from '@ohos.window';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct CanvasExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private imageData?: ImageData = undefined;
  private canvasWidth: number = 0;
  private canvasHeight: number = 0;

  aboutToAppear(): void {
    // 设置屏幕自动旋转
    (this.getUIContext().getHostContext() as common.UIAbilityContext).windowStage.getMainWindow().then((win) => {
        win.setPreferredOrientation(window.Orientation.AUTO_ROTATION).then(() => {
          console.info('Succeeded in setting the window orientation.');
        }).catch((err: BusinessError) => {
          console.error(`Failed to set the window orientation. Cause code: ${err.code}, message: ${err.message}`);
        });
    }).catch((err: BusinessError) => {
      console.error(`Failed to get the main window. Cause code: ${err.code}, message: ${err.message}`);
    });
  }

  aboutToDisappear(): void {
    // 设置屏幕竖屏
    (this.getUIContext().getHostContext() as common.UIAbilityContext).windowStage.getMainWindow().then((win) => {
      win.setPreferredOrientation(window.Orientation.PORTRAIT).then(() => {
        console.info('Succeeded in setting the window orientation.');
      }).catch((err: BusinessError) => {
        console.error(`Failed to set the window orientation. Cause code: ${err.code}, message: ${err.message}`);
      });
    }).catch((err: BusinessError) => {
      console.error(`Failed to get the main window. Cause code: ${err.code}, message: ${err.message}`);
    });
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#f1f3f5')
        .onReady(() => {
          this.canvasWidth = this.context.width;
          this.canvasHeight = this.context.height;
          // 恢复画布
          if (this.imageData) {
            this.context.putImageData(this.imageData, 0, 0);
          }
        })
        .onTouch((event: TouchEvent) => {
          if (event.type === TouchType.Down) {
            this.context.moveTo(event.touches[0].displayX, event.touches[0].displayY);
          }
          if (event.type === TouchType.Move) {
            this.context.lineTo(event.touches[0].displayX, event.touches[0].displayY);
            this.context.stroke();
          }
          // 当手指抬起时，保存画布内容
          if (event.type === TouchType.Up) {
            this.imageData = this.context.getImageData(0, 0, this.canvasWidth, this.canvasHeight);
          }
        })
    }
    .width('100%')
    .height('100%')
  }
}
```
