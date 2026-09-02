---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-559
title: 如何解决组件消失后滑动手势依然可以触发的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决组件消失后滑动手势依然可以触发的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:01+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:142021a552c896579ce984f372a15197bd26bf3da21daeef5c4ea13202194599
---

## 问题现象

当组件在手势事件触发过程中，设置其Visibility为Visibility.None，组件隐藏后绑定的滑动手势事件依然可以触发。

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/7PS66uoORmefVQRTOdI3hw/zh-cn_image_0000002658911337.png "点击放大")

## 效果预览

当组件消失后，手指滑动不会继续触发组件的手势事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/o7GASUZ4TAuSYXJG0rIcxw/zh-cn_image_0000002628392124.png "点击放大")

## 背景知识

* [PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)用于给组件添加滑动手势事件，通过onActionStart、onActionUpdate、onActionEnd来判断当前手势状态。
* [手势拦截增强](../harmonyos-references/ts-gesture-blocking-enhancement.md)提供开发者拦截组件手势的能力，可以动态控制手势事件的触发。

## 解决方案

当使用Visibility.None将组件隐藏后，组件虽然不占位，但onActionUpdate回调的接口还没有释放，行为上仍在触发。

可使用手势拦截增强，通过[onGestureRecognizerJudgeBegin](../harmonyos-references/ts-gesture-blocking-enhancement.md#ongesturerecognizerjudgebegin13)属性获取当前组件的识别器，当设置Visibility为None的时候通过手势识别器的setEnabled方法设置为false表示当前手势识别器不回调应用事件，从而实现禁止组件的拖拽事件。

```ts
@Entry
@Component
struct PanGestureExample {
  @State offsetX: number = 0;
  @State offsetY: number = 0;
  @State positionX: number = 0;
  @State positionY: number = 0;
  private panOption: PanGestureOptions = new PanGestureOptions({ direction: PanDirection.Left | PanDirection.Right });
  private currentRecognizer: GestureRecognizer = new GestureRecognizer();
  @State flag: boolean = true;

  aboutToAppear(): void {
    // 四秒后隐藏该组件
    setTimeout(() => {
      this.flag = false;
      // 设置当前手势识别器的使能状态
      this.currentRecognizer.setEnabled(false);
    }, 4000);
  }

  build() {
    Column() {
      Text(`offsetX: ${this.offsetX}`)
        .margin(16);
      Column() {
        // ...
      }
      .margin({ left: 16 })
      .height(200)
      .width(300)
      .border({ width: 3 })
      .id('column')
      .visibility(this.flag ? Visibility.Visible : Visibility.None)
      // 以组件左上角为坐标原点进行移动
      .translate({ x: this.offsetX, y: this.offsetY, z: 0 })
      .onGestureRecognizerJudgeBegin((event: BaseGestureEvent, current: GestureRecognizer,
        others: Array<GestureRecognizer>) => {
        if (current) {
          let target = current.getEventTargetInfo();
          if (target) {
            // 通过组件Id与手势类型找到需要控制的组件识别器
            if (target.getId() === 'column' &&
              current.getType() === GestureControl.GestureType.PAN_GESTURE) {
              // 保存当前组件的识别器
              this.currentRecognizer = current;
            }
          }
        }
        console.info('event-', event, others);
        return GestureJudgeResult.CONTINUE;
      })
      // 左右拖动触发该手势事件
      .gesture(
        PanGesture(this.panOption)
          .onActionStart((event: GestureEvent) => {
            if (event) {
            }
          })
          .onActionUpdate((event: GestureEvent) => {
            if (event) {
              // 实现拖拽效果
              this.offsetX = this.positionX + event.offsetX;
              this.offsetY = this.positionY + event.offsetY;
            }
          })
          .onActionEnd((event: GestureEvent) => {
            if (event) {
              this.positionX = this.offsetX;
              this.positionY = this.offsetY;
            }
          })
      );
    }
    .alignItems(HorizontalAlign.Start);
  }
}
```

## 常见FAQ

Q：如何拦截web的手势动作？

A：可以参考手势拦截增强文档中的[示例](../harmonyos-references/ts-gesture-blocking-enhancement.md#示例4手势触发成功时取消子组件上的touch事件)将内层的Scoller容器换成Web即可实现拦截Web手势。
