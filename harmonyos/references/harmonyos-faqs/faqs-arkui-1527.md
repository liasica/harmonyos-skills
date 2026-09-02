---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1527
title: 旋转验证码效果实现
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 旋转验证码效果实现
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:16+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1eae52b7546201c45bf29cc43a269bc0cd7987afed483e499ff5eb42556e72ac
---

## 问题现象

如何实现旋转验证码的效果，具体演示如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/wCpVyOGKStGlOzW7omy5uw/zh-cn_image_0000002658966207.png "点击放大")

## 背景知识

* [rotate](../harmonyos-references/ts-universal-attributes-transformation.md#rotate)是一种组件通用属性，用于设置组件的旋转，使用时传入一个RotationOptions类对象，属性说明如下：

  | 名称 | 说明 |
  | --- | --- |
  | centerX | 表示变换中心点x轴坐标（单位：vp） |
  | centerY | 表示变换中心点y轴坐标（单位：vp） |
  | angle | 表示旋转角度（取值可为string类型，如'90deg'） |
* [onTouch](../harmonyos-references/ts-universal-events-touch.md#ontouch)是一种组件通用事件。当手指在组件上按下、滑动、抬起时会触发该事件。

## 解决方案

1. 给Circle组件添加onTouch事件：
   * 当TouchType为Down时，获取图片初始位置startPosition。
   * 当TouchType为Move时，实时获取组件位置updatePosition，并通过calculateAngleBetweenPoints方法计算图片旋转的角度。
2. 定义变量rotateAngle表示图片旋转的角度值，该变量的值由上述方法获得，并将之赋值给Image的rotate属性即可。

完整示例参考如下：

```typescript
import display from '@ohos.display';
import { promptAction } from '@kit.ArkUI';

@Entry
@Component
struct RotatingCodePage {
  @State startRotates: number = 0;
  @State updateRotates: number = 0;
  @State rotateAngle: number = -90;
  @State startPosition: Position = {};
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
    this.circleCenterPoint = { x: this.screenW / 2, y: this.screenH / 2 };
  }

  build() {
    Column({ space: 20 }) {
      Stack() {
        // 开发者可在这自定义图片
        Image($r('app.media.startIcon'))
          .width(100)
          .height(100)
          .objectFit(ImageFit.Contain)
          .rotate({
            // 设置旋转的中心点为组件的中心
            centerX: '50%',
            centerY: '50%',
            angle: this.rotateAngle
          });

        Circle()
          .width(300)
          .height(300)
          .fillOpacity(0)
          .strokeWidth(2)
          .stroke('#0A59f7')
          .onTouch((event: TouchEvent) => {
            if (event.type === TouchType.Down) {
              this.updateRotates = 0;
              this.startRotates = this.rotateAngle;
              this.startPosition = { x: event.touches[0].windowX, y: event.touches[0].windowY };
            } else if (event.type === TouchType.Move) {
              this.updatePosition = { x: event.touches[0].windowX, y: event.touches[0].windowY };
              // 手指移动时的角度
              this.updateRotates =
                calculateAngleBetweenPoints(this.circleCenterPoint, this.startPosition, this.updatePosition);
            }
            this.rotateAngle = this.updateRotates + this.startRotates;

            if (this.rotateAngle > -2 && this.rotateAngle < 2) {
              promptAction.openToast({
                message: '验证成功'
              });
            }
          });
      }
      .hitTestBehavior(HitTestMode.Transparent);

      Text('长按拖拽画面，使图片正立');
    }
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%');
  }
}

function atanToDegrees(atanResult: number) {
  const degrees = atanResult * (180 / Math.PI);
  return degrees;
}

function calculateAngleBetweenPoints(p0: Position = { x: 0, y: 0 }, p1: Position = { x: 0, y: 0 },
  p2: Position = { x: 0, y: 0 }): number {
  const startY = Number(p1.y) - Number(p0.y);
  const startX = Number(p1.x) - Number(p0.x);
  // 通过反正切函数得到的弧度值
  const startRadians: number = Math.atan2(startY, startX);
  // 相对于正x轴，角度范围是0到360度
  const startDeg = atanToDegrees(startRadians);
  const endY = Number(p2.y) - Number(p0.y);
  const endX = Number(p2.x) - Number(p0.x);
  const endRadians: number = Math.atan2(endY, endX);
  const endDeg = atanToDegrees(endRadians);
  return endDeg - startDeg;
}
```
