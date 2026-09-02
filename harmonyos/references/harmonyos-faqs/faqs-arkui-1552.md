---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1552
title: 使用matrix4缩放图片后无法平移至边缘如何处理
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 使用matrix4缩放图片后无法平移至边缘如何处理
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:11+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:31884515846311a268197578d34b968f502db0c2ce264c5d4ea16db4b1491fa1
---

## 问题现象

使用matrix4矩阵变换，控制图片进行缩放平移，具体要求如下：

* 图片依照图片中心点进行缩放。
* 图片放大后可平移，且要平移至图片边缘。
* 图片缩小后自动回归原大小并居中。

目前存在图片放大后无法移动至边缘问题，问题代码示例参考如下：

```ts
import Matrix4 from '@ohos.matrix4';

@Entry
@Component
struct Index {
  @State mScale: number = 1.0;
  @State mBaseScale: number = 1.0;
  @State matrix: Matrix4Transit = Matrix4.identity();
  @State offsetX: number = 0;
  @State offsetY: number = 0;
  @State startOffsetX: number = 0;
  @State startOffsetY: number = 0;
  private componentWidth: number = 0;
  private componentHeight: number = 0;
  private MAX_SCALE: number = 5;
  private MIN_SCALE: number = 1;

  handlePinchUpdate(event: PinchGestureEvent) {
    let currentScale: number = this.mBaseScale * event.scale;
    if (currentScale > this.MAX_SCALE) {
      this.mScale = this.MAX_SCALE;
    } else if (currentScale < this.MIN_SCALE) {
      this.mScale = this.MIN_SCALE;
      this.startOffsetX = 0;
      this.startOffsetY = 0;
      this.offsetX = 0;
      this.offsetY = 0;
    } else {
      this.mScale = currentScale;
    }
    this.getUIContext().animateTo({ duration: 100, curve: Curve.EaseOut }, () => {
      this.updateMatrix();
    });
  }

  public updateMatrix(): void {
    this.matrix = Matrix4.identity()
      .translate({ x: this.offsetX, y: this.offsetY })
      .scale({ x: this.mScale, y: this.mScale })
  }

  // 计算最大偏移量
  getMaxOffset(): [number, number] {
    // 内容缩放后的实际尺寸
    const scaledWidth = this.componentWidth * this.mScale;
    const scaledHeight = this.componentHeight * this.mScale;
    // 最大允许偏移量（内容边缘不超出容器）
    const maxX = Math.max(0, (scaledWidth - this.componentWidth) / 2);
    const maxY = Math.max(0, (scaledHeight - this.componentHeight) / 2);
    return [maxX, maxY];
  }

  build() {
    RelativeContainer() {
      Image($r('app.media.startIcon'))
        .objectFit(ImageFit.Contain)
        .transform(this.matrix)
        .onSizeChange((oldValue: SizeOptions, newValue: SizeOptions) => {
          this.componentWidth = newValue.width as number;
          this.componentHeight = newValue.height as number;
        })
        .width('100%')
        .height('100%')
        .transform(this.matrix)
        .gesture(
          GestureGroup(GestureMode.Exclusive, // 互斥模式
            PinchGesture({ fingers: 2, distance: 1 }) // 双指最小5vp触发
              .onActionStart(() => {
                this.mBaseScale = this.mScale;
              })
              .onActionUpdate((event: PinchGestureEvent) => {
                this.handlePinchUpdate(event); // 缩放事件处理
              }),
            PanGesture({ fingers: 1 }) // 单指拖动
              .onActionUpdate((event: PanGestureEvent) => {
                let distanceX: number = this.startOffsetX + event.offsetX;
                let distanceY: number = this.startOffsetY + event.offsetY;
                let maxOffset: [number, number] = this.getMaxOffset(); // 解构元组赋值
                let maxX = maxOffset[0];
                let maxY = maxOffset[1];
                // 水平方向边界约束
                if (maxX > 0) {
                  distanceX = Math.max(-maxX, Math.min(distanceX, maxX));
                } else {
                  distanceX = 0; // 缩放后内容未超出容器，不允许拖拽
                }
                // 垂直方向约束
                if (maxY > 0) {
                  distanceY = Math.max(-maxY, Math.min(distanceY, maxY));
                } else {
                  distanceY = 0;
                }
                this.offsetX = distanceX;
                this.offsetY = distanceY;
                this.updateMatrix();
              })
              .onActionEnd((event: PanGestureEvent) => {
                let distanceX: number = this.startOffsetX + event.offsetX;
                let distanceY: number = this.startOffsetY + event.offsetY;
                let maxOffset: [number, number] = this.getMaxOffset(); // 解构元组赋值
                let maxX = maxOffset[0];
                let maxY = maxOffset[1];
                // 水平方向约束
                if (maxX > 0) {
                  distanceX = Math.max(-maxX, Math.min(distanceX, maxX));
                } else {
                  distanceX = 0; // 缩放后内容未超出容器，不允许拖拽
                }
                // 垂直方向约束
                if (maxY > 0) {
                  distanceY = Math.max(-maxY, Math.min(distanceY, maxY));
                } else {
                  distanceY = 0;
                }
                this.startOffsetX = distanceX;
                this.startOffsetY = distanceY;
              })
          )
        )
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
    }
    .height('100%')
    .width('100%')
    .clip(true)
  }
}
```

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/YtdccrfFRX2bNbgqhbkMcA/zh-cn_image_0000002628609228.gif "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/4VKvpGQKTduWaEqOwWqRJQ/zh-cn_image_0000002628769128.gif "点击放大")

## 背景知识

* 在HarmonyOS系统中，[matrix4](../harmonyos-references/js-apis-matrix4.md)是实现图片变换的核心API，支持平移、旋转和缩放操作。本文中，matrix4用于处理图片的缩放和平移，确保图片响应用户的捏合和滑动手势。
* [PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)和[PinchGesture](../harmonyos-references/ts-basic-gestures-pinchgesture.md)是HarmonyOS系统中的手势API。PanGesture检测滑动操作，将其转化为平移变换；PinchGesture检测捏合操作，将其转化为缩放变换。
* 这些API的结合使用，使图片的缩放和平移操作流畅响应用户交互。通过matrix4、PanGesture和PinchGesture的协同工作，开发者可以实现图片的动态缩放和平移功能，满足用户的多维度操作需求。

## 问题定位

* 目前代码仅在图片放大后，再进行平移的情况下，无法查看到图片边缘。因此可以主要分析图片缩放后的超出部分原图片大小的部分，已经在平移过程中，对数据信息的处理。
* 纵览代码可知，目前程序的主要逻辑为在识别到相关手势的时候，对初始矩阵进行调节。
  + 识别到捏合手势后，通过手势传出的缩放大小进行处理，并限制缩放上下限。达到下限时，将缩放和偏移初始化。
  + 识别到滑动手势后，每次滑动手势更新时进行边界值获取，然后根据滑动值与边界值进行判断后，更新矩阵。
  + 矩阵更新，矩阵每次更新都是依照初始矩阵，并先进行平移然后进行缩放。
* 依照上述结合代码，矩阵更新的平移偏移量都是根据初始矩阵进行变换，因此矩阵的平移都需要进行数值转化，保证是在未缩放情况下的移动距离。

## 分析结论

* 问题根因:
  + 代码中getMaxOffset()为获取最大偏移量，但实际获取的是图片初始长宽的一半作为边界值，本质的边界值应该是放大导致的超出原本图片大小的部分。
* 性能优化:
  + 因为是根据初始化矩阵进行偏移，因此每次都是总偏移量，所以与当前滑动距离无关，仅与滑动初始阶段的缩放量有关，因此相关计算可移至onActionStart。
  + 滑动结束阶段onActionEnd，因为前面每次滑动更新都会进行矩阵变换，因此最后一次没必要进行矩阵变换，仅需记录最终偏移结果即可。

## 修改建议

* 修改最大偏移量计算逻辑。

  ```ts
  // 计算最大偏移量
  getMaxOffset(): [number, number] {
    // 内容缩放后的实际尺寸
    const scaledWidth = (this.getUIContext().vp2px(this.componentWidth) / 2) * (this.mScale - 1) / this.mScale;
    const scaledHeight = (this.getUIContext().vp2px(this.componentHeight) / 2) * (this.mScale - 1) / this.mScale;

    return [scaledWidth + 20, scaledHeight + 20];
  }
  ```
* 修改调用getMaxOffset逻辑，每次拖动调用一次即可，或者迁移至缩放结束回调。

  ```ts
  .onActionStart(() => {
    let maxOffset: [number, number] = this.getMaxOffset(); // 获取当前缩放下的移动阈值
    this.lateralMovementThreshold = maxOffset[0]; // 横向移动阈值
    this.verticalMovementThreshold = maxOffset[1]; // 纵向移动阈值
  })
  ```
* 删除滑动回调结束的冗余代码，仅保留如下内容，用于记录最终偏移量。

  ```ts
  this.startOffsetX = this.offsetX;
  this.startOffsetY = this.offsetY;
  ```

完整示例参考如下：

```ts
import Matrix4 from '@ohos.matrix4';

@Entry
@Component
struct Matrix4Demo {
  @State mScale: number = 1.0;
  @State mBaseScale: number = 1.0;
  @State matrix: Matrix4Transit = Matrix4.identity();
  @State offsetX: number = 0;
  @State offsetY: number = 0;
  @State startOffsetX: number = 0;
  @State startOffsetY: number = 0;
  @State lateralMovementThreshold: number = 0;
  @State verticalMovementThreshold: number = 0;
  private componentWidth: number = 0;
  private componentHeight: number = 0;
  private MAX_SCALE: number = 5;
  private MIN_SCALE: number = 1;

  handlePinchUpdate(event: PinchGestureEvent) {
    let currentScale: number = this.mBaseScale * event.scale;
    if (currentScale > this.MAX_SCALE) {
      this.mScale = this.MAX_SCALE;
    } else if (currentScale < this.MIN_SCALE) {
      this.mScale = this.MIN_SCALE;
      this.startOffsetX = 0;
      this.startOffsetY = 0;
      this.offsetX = 0;
      this.offsetY = 0;
    } else {
      this.mScale = currentScale;
    }

    this.getUIContext().animateTo({ duration: 100, curve: Curve.EaseOut }, () => {
      this.updateMatrix();
    });
  }

  // 更新矩阵
  public updateMatrix(): void {
    this.matrix = Matrix4.identity()
      .translate({ x: this.offsetX, y: this.offsetY })
      .scale({ x: this.mScale, y: this.mScale });
  }

  // 计算最大偏移量
  getMaxOffset(): [number, number] {
    // 内容缩放后的实际尺寸
    const scaledWidth = (this.getUIContext().vp2px(this.componentWidth) / 2) * (this.mScale - 1) / this.mScale;
    const scaledHeight = (this.getUIContext().vp2px(this.componentHeight) / 2) * (this.mScale - 1) / this.mScale;

    return [scaledWidth + 20, scaledHeight + 20];
  }

  build() {
    RelativeContainer() {
      Image($r('app.media.startIcon'))
        .objectFit(ImageFit.Contain)
        .onSizeChange((oldValue: SizeOptions, newValue: SizeOptions) => {
          console.info(`${oldValue}`);
          this.componentWidth = newValue.width as number;
          this.componentHeight = newValue.height as number;
        })
        .width('100%')
        .height('100%')
        .transform(this.matrix)
        .gesture(
          GestureGroup(GestureMode.Exclusive, // 互斥模式
            PinchGesture({ fingers: 2, distance: 1 }) // 双指最小5vp触发
              .onActionStart(() => {
                this.mBaseScale = this.mScale;
              })
              .onActionUpdate((event: PinchGestureEvent) => {
                this.handlePinchUpdate(event); // 缩放事件处理
              }),
            PanGesture({ fingers: 1 }) // 单指拖动
              .onActionStart(() => {
                let maxOffset: [number, number] = this.getMaxOffset(); // 获取当前缩放下的移动阈值
                this.lateralMovementThreshold = maxOffset[0]; // 横向移动阈值
                this.verticalMovementThreshold = maxOffset[1]; // 纵向移动阈值
              })
              .onActionUpdate((event: PanGestureEvent) => {
                let distanceX: number = this.startOffsetX + this.getUIContext().vp2px(event.offsetX / this.mScale);
                let distanceY: number = this.startOffsetY + this.getUIContext().vp2px(event.offsetY / this.mScale);

                // 水平方向边界约束
                this.offsetX = Math.max(-this.lateralMovementThreshold,
                  Math.min(distanceX, this.lateralMovementThreshold));
                // 垂直方向约束
                this.offsetY = Math.max(-this.verticalMovementThreshold,
                  Math.min(distanceY, this.verticalMovementThreshold));

                this.updateMatrix();
              })
              .onActionEnd((event: PanGestureEvent) => {
                console.info(`${event}`);
                this.startOffsetX = this.offsetX;
                this.startOffsetY = this.offsetY;
              })

          )
        )
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        });
    }
    .height('100%')
    .width('100%')
    .clip(true);
  }
}
```
