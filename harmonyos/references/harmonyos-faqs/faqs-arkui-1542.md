---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1542
title: 实现Canvas的橡皮擦效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 实现Canvas的橡皮擦效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:20+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:a0c398b347ef11c48343e91ca1f20b726bcc5e69ab53177d13b8a612bad6f245
---

## 问题现象

Canvas如何实现橡皮擦效果，清除已绘制的路径？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/GDfTUwKhT_-nfIh38qa89w/zh-cn_image_0000002628769120.png "点击放大")

## 背景知识

* [Canvas](../harmonyos-references/ts-components-canvas-canvas.md)：提供画布组件，用于自定义绘制图形。
* [globalCompositeOperation](../harmonyos-references/ts-components-canvas-common-property.md#globalcompositeoperation)：通过设置不同合成模式，决定新绘制的图形与现有画布内容的叠加效果。
* [clearRect](../atomic-ascf/apis-canvas-rendering-context-2d.md#canvasrenderingcontext2dclearrect)：删除指定区域内的绘制内容。
* [onReady](../harmonyos-references/ts-components-canvas-canvas.md#onready)：Canvas组件初始化完成或者发生大小变化时的事件回调，支持attributeModifier动态设置属性方法。
* [onTouch](../harmonyos-references/ts-universal-events-touch.md#ontouch)：手指触摸动作触发该回调。

## 解决方案

基于图层叠加实现橡皮擦效果，思路如下：

1. 用Canvas创建画布，设置属性，如宽高，背景等，并在onReady回调里完成画笔线宽，颜色，绘制路径等初始化。
2. 在onTouch回调里，根据TouchEvent的枚举类型，在枚举类型为Down时记录绘制路径，Move时实现路径绘制。
3. 使用globalCompositeOperation设置图层叠加模式，设置画笔大小，实现橡皮擦效果。

完整示例参考如下：

```screen
@Entry
@Component
struct CanvasDemo {
  @State paintSize: number = 5; // 当前画笔大小
  @State paintColor: Color = Color.Black; // 当前画笔颜色
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  canvasContext: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  tempPath: Path2D = new Path2D();
  @State pathArray: Array<Path2D | undefined> = []; // 所有画图路径信息
  @State text: string = '';
  @State eventType: string = '';

  build() {
    Column({ space: 7 }) {
      Row() {
        Button('橡皮擦')
          .onClick(() => {
            this.canvasContext.globalCompositeOperation = 'destination-out';
            this.paintSize = 150;
          })
        Button('画笔')
          .onClick(() => {
            this.canvasContext.globalCompositeOperation = 'source-over';
            this.paintSize = 5;
          })

        Button('清屏')
          .onClick(() => {
            this.canvasContext.clearRect(0, 0, 360, 720);
          })
      }
      .margin({ top: 25 })
      .width('100%')
      .justifyContent(FlexAlign.SpaceEvenly)

      Stack({ alignContent: Alignment.Top }) {
        Canvas(this.canvasContext)
          .width('100%')
          .height('100%')
          .backgroundColor('#bacaf3')
          .onReady(() => {
            this.pathArray = [];
            this.canvasContext.strokeStyle = this.paintColor;
            this.canvasContext.lineWidth = this.paintSize;
            this.canvasContext.stroke(this.tempPath);
            for (let index = 0; index < this.pathArray.length; index++) {
              this.canvasContext.stroke(this.pathArray[index]);
            }
          })
          .onTouch((event?: TouchEvent) => {
            if (event) {
              if (event.type === TouchType.Down) {
                this.eventType = 'Down';
                this.canvasContext.beginPath();
                this.tempPath = new Path2D();
                this.pathArray.push(this.tempPath);
                this.tempPath.moveTo(event.touches[0].x, event.touches[0].y);
                this.canvasContext.moveTo(event.touches[0].x, event.touches[0].y);
              }
              if (event.type === TouchType.Up) {
                this.eventType = 'Up';
              }
              if (event.type === TouchType.Move) {
                this.eventType = 'Move';
                this.tempPath.lineTo(event.touches[0].x, event.touches[0].y);
                this.canvasContext.stroke(this.tempPath);
              }
              this.text = 'TouchType:' + this.eventType + '\n touch point and touch element:\nx: ' +
              event.touches[0].x + '\n' + 'y: ' + event.touches[0].y + '\nwidth:' + event.target.area.width +
                '\nheight:' + event.target.area.height + '\npathArray size:' +
              this.pathArray.length;
            }
          })
        Text(this.text);
      }
    }
  }
}
```
