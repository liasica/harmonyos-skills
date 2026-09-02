---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1497
title: 如何实现页面内容随着侧边栏弹出平移
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现页面内容随着侧边栏弹出平移
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:11+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5fbf2fd087dcaef758fe45f16eb6948c9b2f76ca5d29be1b2f06bc8e130c440e
---

## 问题现象

希望实现页面内容随着侧边栏弹出平移，侧边栏跟随手指滑动，松手后如有收起趋势，侧边栏将自动收起。

## 背景知识

* [组件内转场 (transition)](../harmonyos-references/ts-transition-animation-component.md)主要通过transition属性配置转场参数，在组件插入和删除时显示过渡动效，主要用于容器组件中的子组件插入和删除时，提升用户体验。
* [PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)滑动手势事件，当滑动的最小距离达到设定的最小值时触发滑动手势事件。

## 解决方案

可以通过Stack布局将底层主界面、灰色半透明蒙层、侧边栏界面依次堆叠，然后通过组件内转场中的TransitionEffect.move实现底层主界面的平移，通过PanGesture手势实现滑动效果，示例代码如下：

```ts
import { window } from "@kit.ArkUI";

// 侧边栏容器
@Component
export struct SideBar {
  build() {
    Column() {
      Text('Side Bar')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
        })
    }
    .justifyContent(FlexAlign.Center)
    .backgroundColor('#F1F3F5')
    .height('100%')
    .width('100%')
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
  }
}

@Entry
@Component
struct Index {
  private windowClass: window.Window | undefined = undefined;
  @State showSideBar: boolean = false; // 显示侧边栏
  isLeft: boolean = false; // 设置左侧弹出或右侧弹出
  sideBarWidth = 290; // 设置侧边栏宽度
  duration = 250; // 设置侧边栏动画时长
  @State xValue: number = 0; // 底层主界面距离边缘距离
  maxX: number = this.sideBarWidth; // 最大距离值
  minX: number = 0; // 最小距离值

  aboutToAppear(): void {
    // 获取窗口实例
    window.getLastWindow(this.getUIContext().getHostContext(),
      (err, windowObj) => {
        if (err.code) {
          console.error(`Failed to getLastWindow. Code：${err.code}，message：${err.message}`);
        }
        this.windowClass = windowObj;
        this.windowClass.setWindowLayoutFullScreen(true); // 设置窗口全屏
        this.windowClass.setWindowSystemBarEnable(['status', 'navigation']);
      });
  }

  build() {
    // 底层主界面
    Stack({ alignContent: this.isLeft ? Alignment.TopStart : Alignment.TopEnd }) {
      Column() {
        Text('Open Side')
          .fontSize(30)
          .onClick(() => {
            this.getUIContext().animateTo({
              duration: this.duration,
              curve: Curve.EaseOut,
            }, () => {
              this.showSideBar = true;
              this.xValue = this.sideBarWidth;
            });
          })
      }
      .justifyContent(FlexAlign.Center)
      .margin({
        right: !this.isLeft ? this.xValue : 0,
        left: this.isLeft ? this.xValue : 0,
      })
      .height('100%')
      .width('100%')

      // 灰色半透明蒙层
      if (this.showSideBar) {
        Column()
          .backgroundColor('#000')
          .opacity(0.4)
          .height('100%')
          .width('100%')
          .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
          .onClick(() => {
            this.getUIContext().animateTo({
              duration: this.duration,
              curve: Curve.EaseOut,
            }, () => {
              this.showSideBar = false;
              this.xValue = 0;
            });
          })
      }

      // 侧边栏
      if (this.showSideBar) {
        Column() {
          SideBar()
        }
        .margin({
          left: this.isLeft ? this.xValue - this.sideBarWidth : 0,
          right: !this.isLeft ? this.xValue - this.sideBarWidth : 0,
        })
        .width(this.sideBarWidth)
        .visibility(this.showSideBar ? Visibility.Visible : Visibility.Hidden)
        .transition(TransitionEffect.OPACITY.animation({ duration: this.duration, curve: Curve.EaseInOut })
          .combine(TransitionEffect.move(this.isLeft ? TransitionEdge.START : TransitionEdge.END)))
        .gesture(PanGesture(new PanGestureOptions({ direction: PanDirection.Left | PanDirection.Right }))
        // 滑动手势
          .onActionUpdate((event: GestureEvent) => {
            if (event) {
              let a = this.isLeft ? this.maxX + event.offsetX : this.maxX - event.offsetX;
              if (this.xValue >= this.maxX) { // 如果xValue大于最大值，将最大值赋给xValue
                // 当前值为手势起始位置加上偏移量
                this.xValue = a >= this.maxX ? this.maxX : a;
              } else if (this.xValue <= this.minX) { // 如果xValue小于最小值，将最小值赋给xValue
                // 当前值为手势起始位置加上偏移量
                this.xValue = a <= this.minX ? this.minX : a;
              } else { // 区间内直接赋值
                this.xValue = a;
              }
            }
          })
          .onActionEnd((event: GestureEvent) => {
            if (event.velocityX > 0) {
              // 滑动方向向右
              this.getUIContext().animateTo({
                duration: 250,
                curve: Curve.EaseOut,
              }, () => {
                this.xValue = this.isLeft ? this.maxX : this.minX;
                this.showSideBar = this.isLeft ? true : false;
              });
            } else {
              // 滑动方向向左
              this.getUIContext().animateTo({
                duration: 250,
                curve: Curve.EaseOut,
              }, () => {
                this.xValue = this.isLeft ? this.minX : this.maxX;
                this.showSideBar = this.isLeft ? false : true;
              });
            }
          })
        )
      }
    }
    .height('100%')
    .width('100%')
  }
}
```

通过设置isLeft可以控制左侧弹出或者右侧弹出。

效果如下：

| 左侧弹出 | 右侧弹出 |
| --- | --- |
|  |  |
