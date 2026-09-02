---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1446
title: 如何实现List下滑指定距离才展开的效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现List下滑指定距离才展开的效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:22+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:efd798d9f6a9e63e2d90b912d611b1db942e0413aeb8a3295e77d8b639fc5b2d
---

## 问题现象

List组件可以下拉上滑，期望实现以下效果：

1. 组件1默认高度为0，不展示，当组件2下拉时，组件1根据下拉偏移量展示高度，当下拉手势结束时判断偏移量是否超出组件1全部展示高度的一半，如果超出，则组件1全部展示，否则，组件1不展示并触发回弹效果。
2. 当组件1全部展示后，组件2触发上滑时，组件1根据上滑偏移量展示剩余高度，当上滑手势结束时，触发和下拉一致的效果。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/BtsvA1X8Q5WPi6urwhpGnQ/zh-cn_image_0000002628764160.gif "点击放大")

## 背景知识

* [List](../harmonyos-references/ts-container-list.md)：List是用来显示列表的组件，包含一系列相同宽度的列表项，适合连续、多行地呈现同类数据。
* [onTouch](../harmonyos-references/ts-universal-events-touch.md#ontouch)：手指触摸动作触发该回调。鼠标左键按下时对应的事件也会转化成触摸事件并触发该回调。

## 解决方案

可以使用onTouch来监听下拉/上滑手势操作，并通过监听下拉距离用来计算是否展开，具体实现如下：

* 使用onTouch监听触摸事件，根据触摸类型执行相应的操作。当触摸类型为Down时，记录当前触摸位置和图片初始高度。当触摸类型为Move时，根据图片展开状态和触摸移动的距离调整图片高度。当触摸类型为Up时，判断是否需要展开图片，并使用getUIContext().animateTo执行动画，根据图片高度变化展开或收起图片。动画结束后，设置isAnimating为false，表示动画结束。

  ```screen
  .onTouch((event: TouchEvent) => {
    if (!this.isAnimating) { // 非动画中
      const currentY = event.touches[0].y;
      switch (event.type) {
        case TouchType.Down: // 记录当前触摸位置和图片初始高度
          this.touchStartY = currentY;
          this.touchStartHeight = this.imageHeight;
          break;

        case TouchType.Move: // 根据图片展开状态和触摸移动的距离调整图片高度
          const deltaY = currentY - this.touchStartY;
          if (this.isExpanded) {
            if (deltaY >= 0) {
              return;
            } else {
              const newHeight = Math.max(this.touchStartHeight + deltaY, 0);
              if (Math.abs(newHeight - this.imageHeight) > 1) {
                this.imageHeight = newHeight;
              }
            }
          } else {
            if (this.startIndex === 0 && deltaY > 0) {
              const newHeight = Math.min(deltaY, this.maxImageHeight);
              if (Math.abs(newHeight - this.imageHeight) > 1) {
                this.imageHeight = newHeight;
              }
            }
          }
          break;

        case TouchType.Up: // 手指抬起，判断当前组件展开的高度进行完全展开或收起动作
          const movedDistance = Math.abs(currentY - this.touchStartHeight); // 移动距离小于5不做操作
          const isMove = movedDistance > 5;

          if (isMove) {
            this.isAnimating = true;
            this.getUIContext()?.animateTo({
              duration: 400,
              curve: curves.cubicBezierCurve(0.2, 0.8, 0.1, 1.0),
              onFinish: () => {
                this.isAnimating = false;
              }
            }, () => {
              if (this.imageHeight > this.threshold) {
                this.imageHeight = this.maxImageHeight;
                this.isExpanded = true;
              } else {
                this.imageHeight = 0;
                this.isExpanded = false;
              }
            });
          }
          break;
      }
    }
  })
  ```

完整示例参考如下：

```screen
import curves from '@ohos.curves';

@Entry
@Component
struct ListDownDemo {
  @State imageHeight: number = 0; // 图片容器高度
  @State startIndex: number = 0; // 列表起始索引
  @State isExpanded: boolean = false; // 图片展开状态
  private maxImageHeight: number = 240; // 图片最大高度
  private touchStartY: number = 0; // 触摸起始位置
  private threshold: number = 120; // 触发阈值
  private isAnimating: boolean = false; // 是否正在动画中
  private touchStartHeight: number = 0; // 触摸图片起始高度

  build() {
    Column() {
      Column() {
        Text('下拉组件内容区')
          .fontSize(20)
      }
      .width('100%')
      .backgroundColor('#f1f3f5')
      .height(this.imageHeight)
      .clip(true)
      .margin({ bottom: 10 })
      .align(Alignment.Bottom)
      .justifyContent(FlexAlign.End)
      .transition(TransitionEffect.opacity(1).animation({ duration: 200 }))

      List() {
        ForEach([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], (item: number) => {
          ListItem() {
            Row() {
              Column() {
                Text(`组件二内容： ${item} `)
                  .fontSize(14)
                  .opacity(0.7)
              }
              .layoutWeight(1)
              .margin({ right: 10 })
            }
            .padding(8)
            .backgroundColor('#FFFFFF')
            .height(100)
            .margin({
              top: 8,
              bottom: 8,
              left: 16,
              right: 16
            })
            .shadow({
              radius: 4,
              color: '#00000020',
              offsetX: 1,
              offsetY: 1
            })
          }
        })
      }
      .width('100%')
      .height('100%')
      .enableScrollInteraction(this.isExpanded ? false : true)
      .onScrollIndex((start: number) => {
        this.startIndex = start;
      })
      .layoutWeight(1)
      .edgeEffect(EdgeEffect.None)
    }
    .onTouch((event: TouchEvent) => {
      if (!this.isAnimating) { // 非动画中
        const currentY = event.touches[0].y;
        switch (event.type) {
          case TouchType.Down: // 记录当前触摸位置和图片初始高度
            this.touchStartY = currentY;
            this.touchStartHeight = this.imageHeight;
            break;

          case TouchType.Move: // 根据图片展开状态和触摸移动的距离调整图片高度
            const deltaY = currentY - this.touchStartY;
            if (this.isExpanded) {
              if (deltaY >= 0) {
                return;
              } else {
                const newHeight = Math.max(this.touchStartHeight + deltaY, 0);
                if (Math.abs(newHeight - this.imageHeight) > 1) {
                  this.imageHeight = newHeight;
                }
              }
            } else {
              if (this.startIndex === 0 && deltaY > 0) {
                const newHeight = Math.min(deltaY, this.maxImageHeight);
                if (Math.abs(newHeight - this.imageHeight) > 1) {
                  this.imageHeight = newHeight;
                }
              }
            }
            break;

          case TouchType.Up: // 手指抬起，判断当前组件展开的高度进行完全展开或收起动作
            const movedDistance = Math.abs(currentY - this.touchStartHeight); // 移动距离小于5不做操作
            const isMove = movedDistance > 5;

            if (isMove) {
              this.isAnimating = true;
              this.getUIContext()?.animateTo({
                duration: 400,
                curve: curves.cubicBezierCurve(0.2, 0.8, 0.1, 1.0),
                onFinish: () => {
                  this.isAnimating = false;
                }
              }, () => {
                if (this.imageHeight > this.threshold) {
                  this.imageHeight = this.maxImageHeight;
                  this.isExpanded = true;
                } else {
                  this.imageHeight = 0;
                  this.isExpanded = false;
                }
              });
            }
            break;
        }
      }
    })
  }
}
```
