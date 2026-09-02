---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-751
title: List嵌套Canvas滑动抖动问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > List嵌套Canvas滑动抖动问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:22+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:50cc830bec0052d99a4890bdec7985e87a85f13ea233f9e5eec56f2b526f5160
---

## 问题现象

在List组件中嵌套Canvas，滑动页面会出现轻微抖动。

问题代码示例参考如下：

```screen
import { display } from '@kit.ArkUI'

@ComponentV2
@Entry
export struct CanvasInListComponent {
  // 动画
  @Local radianTest: number = 0
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600)
  canvasTest = (): void => {
    let offContext = this.offCanvas.getContext('2d', this.settings)
    offContext.lineCap = 'round'
    offContext.lineWidth = 14
    offContext.beginPath()
    offContext.arc(
      (this.getUIContext().px2vp(display.getDefaultDisplaySync().width) - 2 * 14) / 2.0,
      180,
      100,
      (225 - 90) * Math.PI / 180,
      (135 - 90) * Math.PI / 180
    )
    offContext.strokeStyle = '#EAF2FF'
    offContext.stroke()
    offContext.beginPath()
    offContext.arc(
      (this.getUIContext().px2vp(display.getDefaultDisplaySync().width) - 2 * 14) / 2.0,
      180,
      100,
      (225 - 90) * (Math.PI / 180),
      this.radianTest === 0 ? (135 - 90) * (Math.PI / 180) : (135 - 270 * (1 - this.radianTest) - 90) * (Math.PI / 180)
    )
    offContext.strokeStyle = '#337DFF'
    offContext.stroke()
    let image = this.offCanvas.transferToImageBitmap()
    this.context.transferFromImageBitmap(image)
    // 使用setTimeout模拟帧刷新
    setTimeout(() => {
      this.radianTest = Number(this.radianTest + 0.005)
      if (this.radianTest > 1) {
        this.radianTest = 0
      } else {
        this.canvasTest()
      }
    }, 10)
  }

  build() {
    List() {
      ForEach([1, 2, 3, 4, 5, 6, 7, 8, 9], (item: number) => {
        ListItem() {
          Row() {
            Text(item.toString())
          }
          .height(200)
        }
      })
      ListItem() {
        Canvas(this.context)
          .width('100%')
          .height(300)
          .onReady(this.canvasTest)
          .position({ x: 0, y: 0 })
      }
      .onClick(() => {
        this.canvasTest()
      })
    }
    .width('100%')
    .height('100%')
    .alignListItem(ListItemAlign.Center)
  }
}
```

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/a4_jAgGCSFKGgxrNR84sUA/zh-cn_image_0000002628555364.gif "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/dCYy0T8YRiaNJ-0UcJZ4Gg/zh-cn_image_0000002628395470.gif "点击放大")

## 背景知识

* 采用了[List](../harmonyos-guides/arkts-layout-development-create-list.md)布局，当列表项达到一定数量，内容超过屏幕大小时，可以自动提供滚动功能。
* [Canvas](../harmonyos-references/ts-components-canvas-canvas.md)画布组件用于自定义绘制图形。
* 绘制方法采用了[OffscreenCanvasRenderingContext2D](../harmonyos-references/ts-offscreencanvasrenderingcontext2d.md)离屏绘制：离屏绘制使用CPU进行绘制，绘制速度较慢，对绘制速度有要求的场景应避免使用离屏绘制。

## 问题定位

1. 通过抓取性能Trace图，观察到在橙色标记的时间段内，存在多个方法执行耗时超出预期的情况。其中，Canvas的FireReadyEvent方法出现在关键路径上，表明当前帧的绘制任务未能按时完成，导致渲染延迟，从而引发界面卡顿。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/KATGwxH4TECVXj27EpWyFg/zh-cn_image_0000002658914687.png)
2. 分析onReady中绘制方法：排查到使用了OffscreenCanvasRenderingContext2D方法，根据背景知识了解到离屏绘制的绘制速度较慢，尝试修改为在屏绘制，抖动消失。

## 分析结论

Canvas采用了离屏绘制，使用CPU进行绘制，绘制速度较慢，导致List滑动阻塞。

## 修改建议

将Canvas绘制方法修改为在屏绘制。

完整示例参考如下：

```screen
import { display } from '@kit.ArkUI';

@ComponentV2
@Entry
struct DrawWithScreen {
  // 动画
  @Local radianTest: number = 0;
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);
  canvasTest = (): void => {
    // 原先的离屏绘制改为在屏绘制
    let ctx = this.context;
    ctx.reset();
    ctx.lineCap = 'round';
    ctx.lineWidth = 14;
    ctx.beginPath();
    ctx.arc(
      (this.getUIContext().px2vp(display.getDefaultDisplaySync().width) - 2 * 14) / 2.0,
      180,
      100,
      (225 - 90) * Math.PI / 180,
      (135 - 90) * Math.PI / 180
    );
    ctx.strokeStyle = '#EAF2FF';
    ctx.stroke();
    ctx.beginPath();
    ctx.arc(
      (this.getUIContext().px2vp(display.getDefaultDisplaySync().width) - 2 * 14) / 2.0,
      180,
      100,
      (225 - 90) * (Math.PI / 180),
      this.radianTest === 0 ? (135 - 90) * (Math.PI / 180) : (135 - 270 * (1 - this.radianTest) - 90) * (Math.PI / 180),
    );
    ctx.strokeStyle = '#337DFF';
    ctx.stroke();
    // 使用setTimeout模拟帧刷新
    setTimeout(() => {
      this.radianTest = Number(this.radianTest + 0.05);
      if (this.radianTest > 1) {
        this.radianTest = 0;
      } else {
        this.canvasTest();
      }
    }, 20);
  };

  build() {
    List() {
      ForEach([1, 2, 3, 4, 5, 6, 7, 8, 9], (item: number) => {
        ListItem() {
          Row() {
            Text(item.toString());
          }
          .height(200);
        };
      });
      ListItem() {
        Canvas(this.context)
          .width('100%')
          .height(300)
          .onReady(this.canvasTest)
          .position({ x: 0, y: 0 });
      }
      .onClick(() => {
        this.canvasTest();
      });
    }
    .width('100%')
    .height('100%')
    .alignListItem(ListItemAlign.Center);
  }
}
```
