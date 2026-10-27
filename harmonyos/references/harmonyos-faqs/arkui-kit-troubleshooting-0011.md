---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-kit-troubleshooting-0011
title: ArkWeb多组件拖拽手势冲突问题定位
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 故障排查 > ArkWeb多组件拖拽手势冲突问题定位
category: harmonyos-faqs
scraped_at: 2026-10-28T07:47:00+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:b0862db70bf8bbd3f1a7a2a6ecb3db6b3dba715db0a8fc90bd124c742a77c7fb
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/YYCo0rW7QXeSLTrVtJ4JgQ/zh-cn_image_0000002802039471.png "点击放大")

## 定位过程

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/XoRR1r5RQIeiri_eHnUFsQ/zh-cn_image_0000002772839716.png "点击放大")
