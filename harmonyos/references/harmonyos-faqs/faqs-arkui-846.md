---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-846
title: 如何实现可旋转的弧形图片集
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现可旋转的弧形图片集
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:04+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b81c943eb4492e2e4703669fe65aa01209c4f64e48e17764cbda1ddcdaddae93
---

## 问题现象

如何实现一个类似转盘效果的弧形图片集，要求可以360度旋转。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/-oe0faEeTNqkWXreYGElIw/zh-cn_image_0000002628398640.gif "点击放大")

## 背景知识

* [Image](../harmonyos-references/ts-basic-components-image.md)为图片组件，常用于在应用中显示图片。配合通用属性[rotate](../harmonyos-references/ts-universal-attributes-transformation.md#rotate)可以实现图片的旋转。
* [gesture](../harmonyos-guides/arkts-gesture-events-binding.md#gesture常规手势绑定方法)为通用的一种手势绑定方法，可以将手势绑定到对应的组件上。
* 自定义组件的生命周期[aboutToAppear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoappear)函数在创建自定义组件的新实例后，在执行其build()函数之前执行。允许在aboutToAppear函数中改变状态变量，更改将在后续执行build()函数中生效。

## 解决方案

1. 通过aboutToAppear方法初始化屏幕宽度和图像在圆上的位置坐标。
2. 使用Stack堆叠图像，并为Stack添加手势识别。
3. 自定义getAngle和calculatePointsOnCircle方法分别计算图像的旋转角度和位置坐标。
4. 自定义getScreenWidth方法获取屏幕宽度，用于手势识别的坐标计算。

完整示例参考如下：

```ts
import { display } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct RotatingArcDemo {
  @State stackAngle: number = 0;
  private panOption: PanGestureOptions = new PanGestureOptions({ direction: PanDirection.All });
  imageWidth: number = 100;
  imageHeight: number = 200;
  @State x1: number = 0;
  @State y1: number = 0;
  @State x2: number = 0;
  @State y2: number = 0;
  @State distance: number = 0;
  @State screenWidth: number = 0;
  // imageList图片资源，运行时需替换为实际的资源文件
  private imageList: Array<string> =
    ['app.media.a', 'app.media.b', 'app.media.c', 'app.media.a', 'app.media.b', 'app.media.b', 'app.media.b',
      'app.media.b', 'app.media.b', 'app.media.b', 'app.media.b', 'app.media.b', 'app.media.b', 'app.media.c',
      'app.media.c', 'app.media.c', 'app.media.c'];
  private points: number[][] = [];

  // 通过aboutToAppear方法初始化屏幕宽度和图像在圆上的位置坐标。
  aboutToAppear(): void {
    this.getScreenWidth();
    this.calculatePointsOnCircle(0, 200, 200, this.imageList.length);
  }

  build() {
    NavDestination() {
      Column() {
        Stack() {
          ForEach(this.imageList, (item: string, index: number) => {
            Image($r(item))
              .width(this.imageWidth)
              .height(this.imageHeight)
              .border({ color: '#FFF', width: 2 })
              .position({
                x: this.points[index][0],
                y: this.points[index][1]
              })
              .rotate({ centerX: 100 / 2, centerY: 200 / 2, angle: this.getAngle(index) })
              .zIndex(this.imageList.length - index)
              .id(`${index}`);
          });
        }
        // centerY=图片高度+圆的半径
        .rotate({ angle: this.stackAngle, centerY: 200 + 100 });
      }.height('100%')
      .width('100%')
      .backgroundColor('#ffa7a7a7')
      // 为Stack添加手势识别。
      .gesture(
        PanGesture(this.panOption)
          .onActionStart((event: GestureEvent) => {
            console.info('Pan start', event.offsetX);
            let info = event.fingerList[0];
            this.x1 = this.getUIContext().px2vp(this.screenWidth) / 2 - info.globalX;
            this.y1 = 200 + 100 - info.globalY;
            console.info('Pan start', this.x1, this.y1);
          })
          .onActionEnd((event: GestureEvent) => {
            console.info('Pan end', event.offsetY);
            console.info('Pan end', this.x2, this.y2);
          })
          .onActionUpdate((event: GestureEvent) => {
            console.info(`this.stackAngle: ${this.stackAngle}`);
            if (event) {
              let info = event.fingerList[0];
              this.x2 = this.getUIContext().px2vp(this.screenWidth) / 2 - info.globalX;
              this.y2 = 200 + 100 - info.globalY;
              this.distance = Math.sqrt((event.offsetX) * (event.offsetX) + (event.offsetY) * (event.offsetY));
              if ((this.x1 * this.y2 - this.x2 * this.y1) > 0) {
                this.stackAngle = (this.stackAngle + (this.distance / 60)) % 360;
              } else {
                this.stackAngle = (this.stackAngle - (this.distance / 60)) % 360;
              }
            }
          })
      );
    };
  }

  // 自定义getAngle方法计算图像的旋转角度。
  getAngle(index: number): number {
    let length = this.imageList.length;
    let midIndex = length / 2;
    if (index <= midIndex) {
      console.info(`角度1: ${360 / length * index}`);
      return 360 / length * index;
    } else {
      console.info(`角度2: ${-360 / length * (length - index)}`);
      return -360 / length * (length - index);
    }
  }

  /** 自定义calculatePointsOnCircle方法计算图像的位置坐标。
   * 输入 圆心x，y、 半径、均匀分布的数量
   * 返回一组坐标x=0 / y=200 /r=100
   */
  calculatePointsOnCircle(x: number, y: number, r: number, n: number) {
    const theta = (2 * Math.PI) / n;
    for (let i = 0; i < n; i++) {
      const cx: number = r * Math.cos(i * theta - Math.PI / 2);
      const cy: number = r * Math.sin(i * theta - Math.PI / 2);
      const pointX: number = Math.ceil(x + cx);
      const pointY: number = Math.ceil(y + cy);
      console.info(`坐标 x: ${pointX}, y: ${pointY}`);
      this.points.push([pointX, pointY]);
    }
  }

  // 自定义getScreenWidth方法获取屏幕宽度，用于手势识别的坐标计算。
  getScreenWidth() {
    display.getAllDisplays((err: BusinessError, data: Array<display.Display>) => {
      this.screenWidth = data[0].width;
      console.info(`width: ${this.screenWidth}`);
      const errCode: number = err.code;
      if (errCode) {
        console.error('Failed to obtain all the display objects. Code: ${err.code}, message: ${err.message}');
        return;
      }
      console.info('Succeeded in obtaining all the display objects. Data: ', JSON.stringify(data));
    });
  }
}
```
