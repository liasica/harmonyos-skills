---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1042
title: 如何实现圆形转盘的效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现圆形转盘的效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:06+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8cfdd6ce2e109b6248197121162de5f8e989140037c24f5cc1a16c4bf872a9ba
---

## 问题现象

如何实现一个圆形转盘，可以通过单指在上面拖动让其旋转？

## 背景知识

* ArkTS组件提供[onTouch](../harmonyos-references/ts-universal-events-touch.md#ontouch)触摸事件，当手指在组件按下、滑动或抬起时触发。通过回调可以获取到触摸的坐标。
* [rotate](../harmonyos-references/ts-universal-attributes-transformation.md#rotate)可以使组件绕（x, y, z）指定的矢量作为旋转轴进行旋转。x、y、z的默认值分别为0、0、1，使用默认值时为平面上的旋转。

## 解决方案

按压组件后让组件随着手指拖动自旋转，实现步骤如下：

1. 通过每次滑动时获取的坐标点，得到初始位置点p1和滑动后的更新位置点p2，通过两点与圆心p0处的向量得到初始点的角度和更新点的角度，二者相减得到变更的角度值。

   ```ts
   // 计算两个点关于圆心点的角度差
   function calculateAngleBetweenPoints(p0: Position = { x: 0, y: 0 }, p1: Position = { x: 0, y: 0 },
     p2: Position = { x: 0, y: 0 }): number {
     const startY = Number(p1.y) - Number(p0.y);
     const startX = Number(p1.x) - Number(p0.x);
     // 通过反正切函数得到的弧度值
     const startRadians: number = Math.atan2(startY, startX);
     // 相对于正x轴,角度范围是0到360度
     const startDeg = atanToDegrees(startRadians);
     const endY = Number(p2.y) - Number(p0.y);
     const endX = Number(p2.x) - Number(p0.x);
     const endRadians: number = Math.atan2(endY, endX);
     const endDeg = atanToDegrees(endRadians);
     return endDeg - startDeg;
   }
   ```
2. 明确onTouch触摸回调逻辑，每次更新坐标时，上一次的更新角度即为下一次的起始角度，一次坐标变更时，起始角度+更新角度即为本次旋转的角度。

   ```ts
   .onTouch((event: TouchEvent) => {
     if (event.type === TouchType.Down) {
       this.upRotates = 0;
       this.startRotates = this.rotateAngle;
       this.starPosition = { x: event.touches[0].windowX, y: event.touches[0].windowY };
     } else if (event.type === TouchType.Move) {
       this.updatePosition = { x: event.touches[0].windowX, y: event.touches[0].windowY };
       // 手指移动时的角度
       this.upRotates = calculateAngleBetweenPoints(this.circleCenterPoint, this.starPosition, this.updatePosition);
     }
     this.rotateAngle = this.upRotates + this.startRotates;
   });
   ```

完整代码如下：

```ts
import display from '@ohos.display';

// 反正切结果转化成角度
function atanToDegrees(atanResult: number) {
  const degrees = atanResult * (180 / Math.PI);
  return degrees < 0 ? degrees + 360 : degrees;
}

// 计算两个点关于圆心点的角度差
function calculateAngleBetweenPoints(p0: Position = { x: 0, y: 0 }, p1: Position = { x: 0, y: 0 },
  p2: Position = { x: 0, y: 0 }): number {
  const startY = Number(p1.y) - Number(p0.y);
  const startX = Number(p1.x) - Number(p0.x);
  // 通过反正切函数得到的弧度值
  const startRadians: number = Math.atan2(startY, startX);
  // 相对于正x轴,角度范围是0到360度
  const startDeg = atanToDegrees(startRadians);
  const endY = Number(p2.y) - Number(p0.y);
  const endX = Number(p2.x) - Number(p0.x);
  const endRadians: number = Math.atan2(endY, endX);
  const endDeg = atanToDegrees(endRadians);
  return endDeg - startDeg;
}

@Entry
@Component
struct RotatableDisc {
  @State startRotates: number = 0;
  @State upRotates: number = 0;
  @State rotateAngle: number = 0;
  @State starPosition: Position = {};
  @State updatePosition: Position = {};
  // 图片中心点坐标
  @State circleCenterPoint: Position = {};
  private screenH: number = 0;
  private screenW: number = 0;

  aboutToAppear(): void {
    let displayClass: display.Display | null = null;
    displayClass = display.getDefaultDisplaySync();
    this.screenH = this.getUIContext().px2vp(displayClass.height);
    this.screenW = this.getUIContext().px2vp(displayClass.width);
    // 计算圆心点坐标，可根据实际需求修改
    this.circleCenterPoint = { x: this.screenW / 2, y: this.screenH / 2 };
  }

  build() {
    Column() {
      Image($r('app.media.startIcon'))
        .width(300)
        .height(300)
        .objectFit(ImageFit.Contain)
        .borderRadius(150)
        .rotate({
          centerX: '50%',
          centerY: '50%',
          angle: this.rotateAngle
        })
        .onTouch((event: TouchEvent) => {
          if (event.type === TouchType.Down) {
            this.upRotates = 0;
            this.startRotates = this.rotateAngle;
            this.starPosition = { x: event.touches[0].windowX, y: event.touches[0].windowY };
          } else if (event.type === TouchType.Move) {
            this.updatePosition = { x: event.touches[0].windowX, y: event.touches[0].windowY };
            // 手指移动时的角度
            this.upRotates = calculateAngleBetweenPoints(this.circleCenterPoint, this.starPosition, this.updatePosition);
          }
          this.rotateAngle = this.upRotates + this.startRotates;
        });
    }
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%');
  }
}
```

效果图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/MumUuP1RT9yKwFFTfcFnJg/zh-cn_image_0000002658804819.png "点击放大")
