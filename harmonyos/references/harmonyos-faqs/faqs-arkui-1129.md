---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1129
title: 如何实现手势控制多个Canvas图形的关联滑动与缩放效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现手势控制多个Canvas图形的关联滑动与缩放效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:17+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c3d3691e6031e422921d5ef83c872d8096ad105d3fc26d9983cd526a13f49958
---

## 问题现象

在大型的选座场景中，例如演唱会、大型歌剧院等场合，由于座位数量多，手机屏幕全部显示时，座位显示过小，需要放大和滑动座位进行选座，希望实现座位导航条显示在屏幕左侧且上下滑动和放大跟随座位图变化，从而在放大时起到定位的作用。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/112Ys7phThW56Z0wb2XSoA/zh-cn_image_0000002628409522.png "点击放大")

## 背景知识

* [Canvas](../harmonyos-references/ts-components-canvas-canvas.md)：提供画布组件，用于自定义绘制图形。
* [PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)是滑动手势事件，当滑动的最小距离达到设定的最小值时触发滑动手势事件。
* [PinchGesture](../harmonyos-references/ts-basic-gestures-pinchgesture.md)用于触发捏合手势，最少需要2指，最多5指，最小识别距离为5vp。

## 解决方案

1. 绘制索引导航条时，将座位表的y轴偏移量和缩放比例进行关联，实现y方向的大小和位置一致的同时实现缩放比例一致。
2. 手势成功识别后，根据手势位置及缩放比例实时重绘座位表和索引导航条。

完整示例参考如下：

```ts
@Entry
@Component
struct GestureIdentity {
  // 用来配置CanvasRenderingContext2D对象和OffscreenCanvasRenderingContext2D对象的参数，包括是否开启抗锯齿。true表明开启抗锯齿
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  // 拖动手势信息
  @State offsetX: number = 0;
  @State offsetY: number = 0;
  @State positionX: number = 0;
  @State positionY: number = 0;
  private panOption: PanGestureOptions = new PanGestureOptions({ direction: PanDirection.All });
  // 座位信息
  @State seatArr: number[][] = [
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
  ];
  listWidth: number = 30;
  private seatSpacing: number = 10;
  seatWidth: number = 30;
  seatHeight: number = 30;
  fontSize: number = 14;
  // 捏合手势信息
  @State scaleValue: number = 1;
  @State pinchValue: number = 1;
  @State pinchX: number = 0;
  @State pinchY: number = 0;

  drawCanvas() {
    this.context.reset();
    let w = this.seatWidth * this.scaleValue; // 最新座位宽度
    let h = this.seatHeight * this.scaleValue; // 最新座位高度
    let newSeatSpacing = this.seatSpacing * this.scaleValue;
    // 座位图
    for (let i = 0; i < this.seatArr.length; i++) {
      // 内循环遍历每一行中的每一个元素
      for (let j = 0; j < this.seatArr[i].length; j++) {
        this.context.fillStyle = '#0097D4';
        const seatStatus = this.seatArr[i][j];
        // 设置座位的颜色
        if (seatStatus === 0) {
          this.context.fillStyle = 'green'; // 空闲座位
        } else if (seatStatus === 1) {
          this.context.fillStyle = 'blue'; // 已选择座位
        } else {
          this.context.fillStyle = 'gray'; // 已售座位
        }
        let x = this.offsetX + w + (w + newSeatSpacing) * i;
        let y = this.offsetY + (h + newSeatSpacing) * j;
        this.context.fillRect(x, y, w, h);
      }
    }
    // 索引图
    this.context.fillStyle = 'rgba(0,0,0,0.3)';
    this.context.font = `${this.fontSize}vp sans-serif`;
    this.context.textAlign = 'center';
    for (let i = 0; i < this.seatArr.length; i++) {
      // 第一个
      if (i === 0) {
        // 椭圆+矩形
        this.context.beginPath();
        this.context.ellipse(this.listWidth / 2, this.offsetY + h / 2, this.listWidth / 2, h / 2, 0, 0, Math.PI, true);
        this.context.fill();
        this.context.fillRect(0, this.offsetY + h / 2, this.listWidth,
          h / 2 + newSeatSpacing);
        this.context.fillText(`${i + 1}`, (this.listWidth - this.fontSize) / 2 + 5,
          this.offsetY + (h + newSeatSpacing) * i + (h + newSeatSpacing) / 2);
      } else if (i === this.seatArr.length - 1) {
        // 最后一行行号
        this.context.fillRect(0, this.offsetY + (h + newSeatSpacing) * i, this.listWidth,
          h / 2);
        this.context.beginPath();
        this.context.ellipse(this.listWidth / 2, this.offsetY + (h + newSeatSpacing) * i + h / 2, this.listWidth / 2,
          h / 2, 0, 0, Math.PI, false);
        this.context.fill();
        this.context.fillText(`${i + 1}`, (this.listWidth - this.fontSize) / 2 + 5,
          this.offsetY + (h + newSeatSpacing) * i + (h + newSeatSpacing) / 2);
      } else {
        // 中间行号
        this.context.fillRect(0, this.offsetY + (h + newSeatSpacing) * i, this.listWidth,
          h + newSeatSpacing);
        this.context.fillText(`${i + 1}`, (this.listWidth - this.fontSize) / 2 + 5,
          this.offsetY + (h + newSeatSpacing) * i + (h + newSeatSpacing) / 2);
      }
    }
  }

  build() {
    Column() {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor(Color.White)
        .onReady(() => {
          this.drawCanvas();
        }) // 以下组合手势为顺序识别，当长按手势事件未正常触发时不会触发拖动手势事件
        .gesture(
          GestureGroup(GestureMode.Exclusive,
            // 捏合手势
            PinchGesture({ fingers: 2 })
              .onActionStart(() => {
              })

              .onActionUpdate((event: GestureEvent) => {
                if (event) {
                  this.scaleValue = this.pinchValue * event.scale;
                  this.pinchX = event.pinchCenterX;
                  this.pinchY = event.pinchCenterY;
                  this.drawCanvas(); // 重绘制
                }
                console.info(event.toString());
              })
              .onActionEnd(() => {
                this.pinchValue = this.scaleValue;
              }),
            // 拖动手势事件
            PanGesture(this.panOption)
              .onActionStart(() => {
              })
              .onActionUpdate((event: GestureEvent) => {
                if (event) {
                  this.offsetX = this.positionX + event.offsetX;
                  this.offsetY = this.positionY + event.offsetY;
                  this.drawCanvas(); // 重绘制
                }
                console.info(event.toString());
              })
              .onActionEnd(() => {
                this.positionX = this.offsetX;
                this.positionY = this.offsetY;
              }),
          )
        );
    }
    .width('100%')
    .height('100%');
  }
}
```
