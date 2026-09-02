---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-841
title: 如何实现组件平移、缩放和旋转操作
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现组件平移、缩放和旋转操作
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:42+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e4a494d67e985b573e93eea6503175e7d03b4cbccc609ed766a8bba6dcf62470
---

## 问题现象

点击一个组件的右下角，如何实现组件跟随手指移动进行平移、缩放和旋转操作？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/0x-p5IVjREifyuDkhnZCXQ/zh-cn_image_0000002658797915.gif "点击放大")

## 背景知识

* 通用属性[transform](../harmonyos-references/ts-universal-attributes-transformation.md#transform)可以设置组件的变换矩阵。
* [PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md#pangesture-1)滑动手势事件，当滑动的最小距离达到设定的最小值时触发滑动手势事件。
* [@ohos.matrix4](../harmonyos-references/js-apis-matrix4.md)模块提供矩阵变换功能，支持对图形进行平移、旋转和缩放等。

## 解决方案

实现思路：

* 旋转和缩放部分。

  使用矩阵实现，通过构建一个以组件中心为原点的坐标系，初始坐标是从中心指向边框右下角。手指移动时，在初始坐标基础上增加手指移动的向量，即可得到当前手指相对于组件中心为原点的坐标系的坐标。从而可以计算到原点的距离和旋转的角度，该距离除以初始距离即为缩放比例，该角度减去初始角度即为旋转角度。

  **说明** 

  每次计算当前手指相对于中心的坐标时，需要使用初始坐标加上手指偏移距离得到的坐标进行上一次旋转缩放的矩阵映射，否则会有偏差。
* 平移部分。

  使用offset实现，记录上一次移动的终点位置，再加上本次手指移动的距离，即可实现平移。

  **说明** 

  由于平移的手势绑定在旋转缩放的组件上，所以直接使用会有偏差，必须对该坐标也进行一次相同的旋转缩放映射。

完整示例参考如下：

```ts
import { matrix4 } from '@kit.ArkUI';

@Entry
@ComponentV2
struct ImageMovePage {
  // 声明平移矩阵
  @Local matrix: matrix4.Matrix4Transit = matrix4.identity().copy();
  // 声明手势前的矩阵
  private rotateAndScaleMatrix: matrix4.Matrix4Transit = matrix4.identity().copy();
  // 声明初始位置坐标
  private initStackX: number = 0;
  private initStackY: number = 0;
  // 声明初始宽高
  private initStackWidth: number = 0;
  private initStackHeight: number = 0;
  // 声明中心点坐标
  private initCenterX: number = 0;
  private initCenterY: number = 0;
  // 声明初始半径
  private initR: number = 0;
  // 声明初始角度
  private initAngle: number = 0;
  // 声明手势开始时的坐标
  private startStackX: number = 0;
  private startStackY: number = 0;
  // 声明当前位置
  @Local currentX: number = 0;
  @Local currentY: number = 0;
  // 声明当前中心点坐标
  @Local currentCenterX: number = 0;
  @Local currentCenterY: number = 0;
  // 声明缩放比例
  @Local stackScale: number = 1;
  // 声明当前旋转角度
  @Local stackRotate: number = 0;
  // 声明移动时手指的初始坐标
  private initFingerX: number = -1;
  private initFingerY: number = -1;
  private lastFingerX: number = 0;
  private lastFingerY: number = 0;

  // 在即将出现时初始化数据
  aboutToAppear(): void {
    this.init();
  }

  // 初始化方法：获取初始位置
  init() {
    let observer = this.getUIContext().getUIInspector().createComponentObserver('target');
    observer.on('layout', () => {
      let node = this.getUIContext().getAttachedFrameNodeById('target');
      if (node) {
        let position = node.getPositionToParent();
        this.initStackX = position.x;
        this.initStackY = position.y;
        let size = node.getMeasuredSize();
        this.initStackWidth = this.getUIContext().px2vp(size.width);
        this.initStackHeight = this.getUIContext().px2vp(size.height);
        this.initCenterX = this.initStackX + (this.initStackWidth >> 1);
        this.initCenterY = this.initStackY + (this.initStackHeight >> 1);
        this.initR = Math.sqrt((this.initStackWidth >> 1) * (this.initStackWidth >> 1) +
          (this.initStackHeight >> 1) * (this.initStackHeight >> 1));
        this.initAngle = Math.atan2((this.initStackHeight), (this.initStackWidth)) * 180 / Math.PI;
      }
      console.info(`x: ${this.initStackX}, y: ${this.initStackY}`);
      console.info(`width: ${this.initStackWidth}, height: ${this.initStackHeight}`);
      console.info(`centerX: ${this.initCenterX}, centerY: ${this.initCenterY}`);
      console.info(`initR: ${this.initR}, angle: ${this.initAngle}`);
      observer.off('layout');
    });
  }

  build() {
    NavDestination() {
      Stack() {
        Stack() {
          Stack({ alignContent: Alignment.BottomEnd }) {
            Text('harmonyos')
              .width(80)
              .height(80)
              .borderWidth(1)
              .borderColor('#0A59F7')
              .fontColor('#0A59F7');

            Text()
              .width(10)
              .height(10)
              .backgroundColor('#0A59F7');
            // 手势识别
            Text()
              .width(10)
              .height(10)
              .backgroundColor('#0A59F7')
              .gesture(
                PanGesture()
                  .onActionStart(event => {
                    console.info(`event: ${event}`);
                    // 记录上一次的矩阵
                    this.rotateAndScaleMatrix = this.matrix.copy();
                    // 获取手指位置
                    this.initFingerX = (this.initStackWidth >> 1);
                    this.initFingerY = (this.initStackHeight >> 1);
                  })
                  .onActionUpdate(event => {
                    // 获取当前坐标手指
                    let currentFingerX: number = this.initFingerX + event.offsetX;
                    let currentFingerY: number = this.initFingerY + event.offsetY;
                    // 映射手指坐标
                    let point = this.rotateAndScaleMatrix.copy().transformPoint([currentFingerX, currentFingerY]);
                    currentFingerX = point[0];
                    currentFingerY = point[1];
                    console.info(`event.offsetX: ${currentFingerX}, event.offsetY: ${currentFingerY}`);
                    // 获取半径
                    let r: number = Math.sqrt(currentFingerX * currentFingerX + currentFingerY * currentFingerY);
                    console.info(`半径r: ${r}, 初始半径：${this.initR}, 比率： ${r / this.initR}`);
                    // 获取cos和sin，判断象限
                    this.stackScale = (r / this.initR);
                    // 声明角度
                    let theta: number = Math.atan2(currentFingerY, currentFingerX) * 180 / Math.PI - this.initAngle;
                    // 判断象限
                    this.stackRotate = theta;
                    this.matrix = matrix4.identity().copy()
                      .scale({ x: r / this.initR, y: r / this.initR })
                      .rotate({ z: 1, angle: theta });
                  })
                  .onActionEnd(event => {
                    this.lastFingerX = this.initFingerX + event.offsetX;
                    this.lastFingerY = this.initFingerY + event.offsetY;
                    console.info(`旋转角度: ${this.stackRotate}, 缩放比例: ${this.stackScale}`);
                  })
              );
          }
          .transform(this.matrix)
          .gesture(
            PanGesture()
              .onActionStart(() => {
                this.startStackX = this.currentX;
                this.startStackY = this.currentY;
              })
              .onActionUpdate(event => {
                // 获取手指位置
                let point = this.matrix.copy().transformPoint([event.offsetX, event.offsetY]);
                this.currentX = this.startStackX + point[0];
                this.currentY = this.startStackY + point[1];
              })
              .onActionEnd(() => {
                console.info(`currentX: ${this.currentX}, currentY: ${this.currentY}`);
              })
          );
        }
        .id('target')
        .offset({ x: this.currentX, y: this.currentY });
      }
      .height('100%')
      .backgroundColor('#F1F3F5')
      .width('100%')
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
    };
  }
}
```
