---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1186
title: 如何通过手势实现组件惯性滚动动画
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何通过手势实现组件惯性滚动动画
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:26+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5f109701fc190e64f42b98af507fab72de597b51dfe7dc31fc26849007537b06
---

## 问题现象

如何通过PanGesture手势实现自定义组件带有惯性的滑动动画？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/EEkT65slSCSOMCaqHHdR6g/zh-cn_image_0000002658952169.png "点击放大")

## 背景知识

* [GestureGroup](../harmonyos-references/ts-combined-gestures.md#接口)：手势识别组合，即多种手势组合为复合手势，支持连续识别、并行识别和互斥识别。
* [PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)：滑动手势事件，当滑动的最小距离达到设定的最小值时触发滑动手势事件。
* [SwipeGesture](../harmonyos-references/ts-basic-gestures-swipegesture.md)：用于触发滑动事件，滑动速度大于100vp/s时可识别成功。
* [animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)：提供全局animateTo显式动画接口来指定由于闭包代码导致的状态变化插入过渡动效。

## 解决方案

1. 通过PanGesture、SwipeGesture等处理手势事件和animateTo方法配合实现。
2. 使用PanGesture拖动组件平移，在onActionStart回调中标记手势开始，在onActionUpdate回调中实时更新组件位置，并在onActionEnd回调中记录结束时组件最终位置同时标记手势结束。
3. 当手指抬起时触发SwipeGesture手势事件中的animateTo动画，计算滑动过程中组件的偏移量，将两者相加得出组件停止状态下的最终坐标位置，从而实现惯性滚动效果。

```ts
@Entry
@Component
struct PanGestureExample {
  @State offsetX: number = 0;
  @State offsetY: number = 0;
  @State positionX: number = 0;
  @State positionY: number = 0;
  private panOption: PanGestureOptions = new PanGestureOptions({ direction: PanDirection.All });
  @State isEnd: boolean = false; // 标记手势是否结束
  uiContext: UIContext | undefined = undefined;

  aboutToAppear() {
    this.uiContext = this.getUIContext();
    if (!this.uiContext) {
      console.warn('no uiContext');
      return;
    }
  }

  build() {
    Column() {
      Text('文本滑动');
    }
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center)
    .height(60)
    .width(150)
    .backgroundColor('#f1f3f5')
    .borderRadius(12)
    .margin(30)
    .translate({ x: this.offsetX, y: this.offsetY, z: 0 }) // 以组件左上角为坐标原点进行移动
    .gesture(

      GestureGroup(GestureMode.Parallel,
        // 平移手势
        PanGesture(this.panOption) // 手势识别成功的回调
          .onActionStart(() => {
            // 手势开始
            this.isEnd = false;
            console.info('Pan start');
          }) // 手势移动过程中回调
          .onActionUpdate((event?: GestureEvent) => {
            if (event) {
              // 最后的位置加上偏移量
              this.offsetX = this.positionX + event.offsetX;
              this.offsetY = this.positionY + event.offsetY;
            }
          }) // 手势识别成功，手指抬起后触发回调
          .onActionEnd((event) => {
            this.positionX = this.positionX + event.offsetX;
            this.positionY = this.positionY + event.offsetY;
            // 手势结束
            this.isEnd = true;
          }),
        // 滑动手势
        SwipeGesture({ speed: 10 }) // 滑动手势识别成功回调
          .onAction((event) => {
            // 计算惯性滑动的速度
            let speedY = event.speed * Math.sin(Math.sin(event.angle * Math.PI / 180));
            let speedX = event.speed * Math.sin(Math.sin((90 - event.angle) * Math.PI / 180));
            if (this.isEnd) {
              // 设置滑动动画
              this.uiContext?.animateTo({
                duration: 1000,
                curve: Curve.LinearOutSlowIn,
                iterations: 1,
                playMode: PlayMode.Normal,
                onFinish: () => {
                  console.info('play end');
                }
              }, () => {
                this.offsetY = this.offsetY + speedY * 0.1;
                this.positionY = this.positionY + speedY * 0.1;
                this.offsetX = this.offsetX + speedX * 0.1;
                this.positionX = this.positionX + speedX * 0.1;
              });
            }
          })
      )
    );
  }
}
```
