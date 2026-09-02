---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-339
title: 如何解决Web页上下滑动时会误触发tab页翻页手势及tab页切换时Web组件还可以上下滚动问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决Web页上下滑动时会误触发tab页翻页手势及tab页切换时Web组件还可以上下滚动问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:872d548c7bb81ff056f0dba613b2b50d81f8d4603192de182cf23d3591572706
---

**问题现象**

Tabs组件嵌套Web组件在滚动场景中可能出现以下问题：

1. 在Web页面上下滑动时，可能会误触发标签页的翻页手势。
2. 切换tab页时，Web组件仍可上下滚动。

**解决措施**

1. 可以通过给**Web组件**设置嵌套滚动[nestedScroll](../harmonyos-references/arkts-basic-components-web-attributes.md#nestedscroll11)属性解决。
2. 可以通过给**Web组件**设置网页是否允许滚动[setScrollable](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#setscrollable12)属性解决。

示例代码如下：

```ts
import { webview } from '@kit.ArkWeb';

@Component
@Entry
struct TabWebScroll {
  @State isScrollEnabled: boolean = true; // Control the sliding page for page switching
  private tabsController = new TabsController();
  private currentIndex: number = 0;// Track currently active tab index
  private webviewController: webview.WebviewController = new webview.WebviewController();

  build() {
    Tabs({ barPosition: BarPosition.End, controller: this.tabsController }) {
      TabContent() {
        Web({ src: 'https://developer.huawei.com/consumer/cn/', controller: this.webviewController })
          .nestedScroll({
            // Set nested scrolling
            scrollForward: NestedScrollMode.PARENT_FIRST,
            scrollBackward: NestedScrollMode.SELF_FIRST
          })
      }
      .tabBar(this.tabBuilder('home page', 0))

      TabContent() {
        Column() {
          Text('find')
        }
        .width('100%')
        .height('100%')
      }
      .tabBar(this.tabBuilder('find', 1))

      TabContent() {
        Column() {
          Text('recommend')
        }
        .width('100%')
        .height('100%')
      }
      .tabBar(this.tabBuilder('recommend', 2))

      TabContent() {
        Column() {
          Text('my')
        }
        .width('100%')
        .height('100%')
      }
      .tabBar(this.tabBuilder('my', 3))
    }
    .onChange((index: number) => {
      this.currentIndex = index;
    })
    .scrollable(this.isScrollEnabled)
    .onAnimationEnd(() => {
      // Trigger this callback when the animation ends, and set the web component to slide
      this.webviewController?.setScrollable(true);
    })
    .onGestureSwipe(() => {
      // During the sliding process on the page, this callback is triggered frame by frame. When switching between tab pages, the web page cannot slide up or down
      this.webviewController?.setScrollable(false);
    })
  }

  @Builder
  tabBuilder(title: string, targetIndex: number) {
    Column() {
      Text(title)
        .fontColor(this.currentIndex === targetIndex ? '#1698CE' : '#6B6B6B')
    }
    .width('100%')
    .height(50)
    .justifyContent(FlexAlign.Center)
  }
}
```
