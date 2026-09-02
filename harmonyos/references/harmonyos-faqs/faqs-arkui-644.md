---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-644
title: 自定义实现图标拖动效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 自定义实现图标拖动效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:23+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c965d85cef68cc98c897c248f7235e38c05359e8016be240dfff877b47234682
---

## 问题现象

如何实现常见图标拖动效果。长按图标后图标变大，并解锁拖动功能，拖动结束后图标停留在结束位置并缩小为原本大小。

## 背景知识

* [GestureGroup](../harmonyos-references/ts-combined-gestures.md)（组合手势）：手势识别组合，即多种手势组合为复合手势，支持连续识别、并行识别和互斥识别。
* [LongPressGesture](../harmonyos-references/ts-basic-gestures-longpressgesture.md)：用于触发长按手势事件，触发长按手势的最少手指数为1，最短长按时间为500毫秒。
* [PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)：滑动手势事件，当滑动的最小距离达到设定的最小值时触发滑动手势事件。

## 解决方案

想要实现期望效果，单一手势无法完成，需要使用到GestureGroup组合手势并将组合模式设置为GestureMode.Parallel（并发执行手势）。

实现步骤如下：

1. 添加LongPressGesture手势，实现长按动态改变图标大小。

   ```ts
   LongPressGesture({ repeat: true })
     .onAction((event: GestureEvent) => {
       if (event && event.repeat) {
         this.getUIContext()?.animateTo({ curve: curves.springMotion() }, () => {
           this.picSize = 150;
         });
         this.isActive = true;
       };
     })
     .onActionEnd(() => {
       this.getUIContext()?.animateTo({ curve: curves.springMotion() }, () => {
         this.picSize = 100;
       });
       this.isActive = false;
     }),
   ```
2. 添加PanGesture手势，实现拖动图标。

   ```ts
   PanGesture()
     .onActionUpdate((e) => {
       this.offsetX = this.isActive ? e.offsetX : 0;
       this.offsetY = this.isActive ? e.offsetY : 0;
     })
     .onActionEnd(() => {
       this.positionX += this.offsetX;
       this.positionY += this.offsetY;
       this.offsetX = 0;
       this.offsetY = 0;
     })
   ```

完整示例参考如下：

```ts
import { curves, display } from '@kit.ArkUI';

@Entry
@Component
struct DragDemo {
  screenWidth: number = this.getUIContext().px2vp(display.getDefaultDisplaySync().width);
  screenHeight: number = this.getUIContext().px2vp(display.getDefaultDisplaySync().height);
  @State offsetX: number = 0;
  @State offsetY: number = 0;
  @State positionX: number = (this.screenWidth - 100) / 2; // 设置居中
  @State positionY: number = (this.screenHeight - 100) / 2 - 50; // 设置居中
  @State picSize: number = 100;
  @State isActive: boolean = false;

  build() {
    RelativeContainer() {
      Column() {
        // 示例图片，请根据需求选择图片
        Image($r('app.media.startIcon'))
          .draggable(false)
          .width(this.picSize)
          .height(this.picSize)
          .translate({ x: this.positionX + this.offsetX, y: this.positionY + this.offsetY, z: 0 })
          .gesture(
            GestureGroup(GestureMode.Parallel,
              // 添加长按事件，长按后触发图片动效放大，松手后图片动效缩小
              LongPressGesture({ repeat: true })
                .onAction((event: GestureEvent) => {
                  if (event && event.repeat) {
                    this.getUIContext()?.animateTo({ curve: curves.springMotion() }, () => {
                      this.picSize = 150;
                    });
                    this.isActive = true;
                  };
                })
                .onActionEnd(() => {
                  this.getUIContext()?.animateTo({ curve: curves.springMotion() }, () => {
                    this.picSize = 100;
                  });
                  this.isActive = false;
                }),
              // 在长按事件触发后执行拖动事件，根据拖动对图片进行位移
              PanGesture()
                .onActionUpdate((e) => {
                  this.offsetX = this.isActive ? e.offsetX : 0;
                  this.offsetY = this.isActive ? e.offsetY : 0;
                })
                .onActionEnd(() => {
                  this.positionX += this.offsetX;
                  this.positionY += this.offsetY;
                  this.offsetX = 0;
                  this.offsetY = 0;
                })
            )
          );
      }
    }
  }
}
```

实现效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/WFhaqwITTMucjo8_T3h5YA/zh-cn_image_0000002658793779.png "点击放大")
