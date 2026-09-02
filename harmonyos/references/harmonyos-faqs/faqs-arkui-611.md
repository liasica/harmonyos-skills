---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-611
title: 多组件拖拽手势冲突
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 多组件拖拽手势冲突
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:01+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6f13cd4e2d21e003c004b0b47976994d14c6f59e8a23f4bab5dc971ad00d08c5
---

## 问题现象

在Web组件的上层添加一个视图组件，并给组件添加了拖拽手势。当拖动该视图组件时，Web组件中的内容也跟随滑动。问题代码如下：

```ts
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct Index {
  @State webViewController: webview.WebviewController = new webview.WebviewController;
  @State curX: number = 0;
  @State curY: number = 0;
  posX: number = 0;
  posY: number = 0;

  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      Web({
        controller: this.webViewController,
        src: 'www.example.com' // 运行时替换为实际链接
      });
      RelativeContainer() {
        Column() {
          Text('组件');
        }
        .alignItems(HorizontalAlign.Center)
        .justifyContent(FlexAlign.Center)
        .backgroundColor('#fff1f1f5')
        .borderWidth('3')
        .borderColor('#22000000')
        .position({
          x: this.curX,
          y: this.curY
        })
        .width(100)
        .height(100)
        .borderRadius(12)
        .translate({})
        .gesture(
          PanGesture(new PanGestureOptions({ direction: PanDirection.All, fingers: 1, distance: 1 }))
            .onActionStart((event: GestureEvent) => {
              this.curX = this.posX + event.offsetX;
              this.curY = this.posY + event.offsetY;
            })
            .onActionUpdate((event: GestureEvent) => {
              if (event) {
                this.curX = this.posX + event.offsetX;
                this.curY = this.posY + event.offsetY;
              }
            })
            .onActionEnd((event: GestureEvent) => {
              this.posX = this.curX;
              this.posY = this.curY;
            })
        );
      }.width('100%').height('100%').hitTestBehavior(HitTestMode.Transparent);
    }.width('100%').height('100%');
  }
}
```

问题效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/yPeqzD1WRM-hor2xClrQIQ/zh-cn_image_0000002628392730.png "点击放大")

## 背景知识

* [onTouchIntercept](../harmonyos-references/ts-universal-attributes-on-touch-intercept.md#ontouchintercept)为组件提供自定义的事件拦截能力，开发者可根据事件在控件上按下时发生的位置，输入源等事件信息决定控件上的HitTestMode属性。
* [hitTestBehavior](../harmonyos-references/ts-universal-attributes-hit-test-behavior.md#hittestbehavior)属性用于设置不同的触摸测试响应模式，影响触摸测试收集结果及后续触屏事件分发。

## 问题定位

问题代码中多组件手势冲突，Web组件未对手势进行拦截，因此会默认响应触摸测试。

## 分析结论

Web组件未设置HitTestMode属性，所以会默认响应触摸测试，故当拖动视图组件时，底部的Web组件也会被拖动。

## 修改建议

可以通过onTouchIntercept属性监听Web组件输入源，对hitTestBehavior属性设置不同的触摸测试响应模式，结合bool类型的变量实现只拖动特定组件的效果。

1. 定义bool类型的rowTouchFlag变量，当该值为true时，将Web组件设置为None不响应触摸测试，为false时正常响应。
2. 当拖拽视图组件时，将rowTouchFlag的值设置为true，此时Web组件将不响应触摸，停止移动，当拖拽动作完成时，重新将rowTouchFlag的值设置为false。

具体代码如下：

```ts
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct HitTestModeTouchIDemo {
  @State webViewController: webview.WebviewController = new webview.WebviewController;
  @State curX: number = 0;
  @State curY: number = 0;
  posX: number = 0;
  posY: number = 0;
  @State rowTouchFlag: boolean = false;

  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      Web({
        controller: this.webViewController,
        src: 'www.example.com' // 运行时替换为实际链接
      })
        .fileAccess(false)
        .geolocationAccess(false)
        .onTouchIntercept(() => {
          // 当rowTouchFlag为true时返回HitTestMode.None，此时Web组件不再响应触摸事件
          if (this.rowTouchFlag) {
            return HitTestMode.None;
          }
          return HitTestMode.Default;
        });
      RelativeContainer() {
        Column() {
          Text('组件');
        }
        .alignItems(HorizontalAlign.Center)
        .justifyContent(FlexAlign.Center)
        .backgroundColor('#fff1f1f5')
        .borderWidth('3')
        .borderColor('#22000000')
        .position({
          x: this.curX,
          y: this.curY
        })
        .width(100)
        .height(100)
        .borderRadius(12)
        .translate({})
        .gesture(
          // 使用PanGesture实现单指全方向拖拽，通过onActionUpdate更新方块位置
          PanGesture(new PanGestureOptions({ direction: PanDirection.All, fingers: 1, distance: 1 }))
            .onActionStart((event: GestureEvent) => {
              this.curX = this.posX + event.offsetX;
              this.curY = this.posY + event.offsetY;
            })
            .onActionUpdate((event: GestureEvent) => {
              if (event) {
                this.curX = this.posX + event.offsetX;
                this.curY = this.posY + event.offsetY;
              }
            })
            .onActionEnd(() => {
              this.posX = this.curX;
              this.posY = this.curY;
              this.rowTouchFlag = false;
            })
        )
        .onTouchIntercept(() => {
          this.rowTouchFlag = true;
          return HitTestMode.Default;
        });
      }.width('50%').height('50%').hitTestBehavior(HitTestMode.Transparent);
    }.width('100%').height('100%');
  }
}
```

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/drj2tniwT0WpKolmqFIEhw/zh-cn_image_0000002658792001.png "点击放大")
