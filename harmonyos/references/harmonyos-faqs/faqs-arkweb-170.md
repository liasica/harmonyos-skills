---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-170
title: Scroll内Web嵌套其他组件时滑动优先级设置
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Scroll内Web嵌套其他组件时滑动优先级设置
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:33+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:eab1f3bdaa2e89e55a36780ab6af3516a8507e3b276bfef0eed3ec3d533bd8da
---

## 问题现象

Scroll内Web组件头尾存在其他组件时，头部组件只有在Web内容滑动至顶部时才显示，尾部组件只有在Web内容滑动至底部时才显示。

## 背景知识

* [onVisibleAreaChange](../harmonyos-references/ts-universal-component-visible-area-change-event.md#onvisibleareachange)：组件可见区域变化时触发该回调。
* [nestedScroll](../harmonyos-references/ts-container-scrollable-common.md#nestedscroll11)设置前后两个方向的嵌套滚动模式，实现与父组件的滚动联动。

## 解决方案

通过给头尾组件设置onVisibleAreaChange可见区域变化回调：当头部组件或尾部组件可见时，设置Web的滑动优先级为父组件先滚动；当头部组件或尾部组件不可见时，设置Web的滑动优先级为自身先滚动。

```ts
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct ScrollerDemo {
  scroller: Scroller = new Scroller();
  controller: webview.WebviewController = new webview.WebviewController();
  @State scrollMode: NestedScrollMode = NestedScrollMode.PARENT_FIRST;

  build() {
    Scroll(this.scroller) {
      Column() {
        Column() {
          Text('标题')
            .fontSize(16)
            .fontWeight(600)
            .lineHeight(23)
            .textAlign(TextAlign.Start)
            .width('90%')
        }
        .width('100%').alignItems(HorizontalAlign.Start).margin({ top: 20, bottom: 24 })
        // 判断可见区域变化
        .onVisibleAreaChange([0.0, 1.0], (isExpanding: boolean, currentRatio: number) => {
          if (isExpanding && currentRatio > 0.0) {
            // 可见时，设置Web的滑动优先级为父组件先滚动
            this.scrollMode = NestedScrollMode.PARENT_FIRST;
          }

          if (!isExpanding && currentRatio <= 0.0) {
            // 不可见时，设置Web的滑动优先级为自身先滚动
            this.scrollMode = NestedScrollMode.SELF_FIRST;
          }
        })

        Web({
          // 此处'www.example.com'仅作示例。
          src: 'www.example.com',
          controller: this.controller
        })
          .fileAccess(false)
          .geolocationAccess(false)
          .domStorageAccess(true)
          .javaScriptAccess(true)
          .zoomAccess(false)
          .height('100%')
          .nestedScroll({
            scrollForward: this.scrollMode,
            scrollBackward: this.scrollMode
          })

        Row() {
          Text(`阅读量：  12345`).textAlign(TextAlign.End)
        }.height(40).alignItems(VerticalAlign.Center)
        // 判断可见区域变化
        .onVisibleAreaChange([0.0, 1.0], (isExpanding: boolean, currentRatio: number) => {
          if (isExpanding && currentRatio > 0.0) {
            // 可见时，设置Web的滑动优先级为父组件先滚动
            this.scrollMode = NestedScrollMode.PARENT_FIRST;
          }

          if (!isExpanding && currentRatio <= 0.0) {
            // 不可见时，设置Web的滑动优先级为自身先滚动
            this.scrollMode = NestedScrollMode.SELF_FIRST;
          }
        })
      }
    }
    .width('100%')
    .layoutWeight(1)
    .padding({
      left: 14,
      right: 14
    })
    .scrollBar(BarState.Off)
  }
}
```
