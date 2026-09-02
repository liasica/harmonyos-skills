---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-285
title: 跳转页面如何实现页面级别的透明效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 跳转页面如何实现页面级别的透明效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5af9d19da016ddac21f71c6a7ec3e47ccc38c700845cd88914b570aa5e8b4cb1
---

推荐使用的是Navigation跳转方式，可以将NavDestination设置mode为NavDestinationMode.DIALOG弹窗类型，此时整个NavDestination页面默认透明显示，具体可以参考：[页面显示类型](../harmonyos-guides/arkts-navigation-navdestination.md#页面显示类型)中的弹窗类型。示例代码如下：

```typescript
@Component
export struct TransparentPage {
  @Provide('NavPathStack') pageStack: NavPathStack = new NavPathStack();

  @Builder
  pageMapBuilder(name: string) {
    if (name === 'DialogPage') {
      DialogPage()
    }
  }

  build() {
    Navigation(this.pageStack) {
      Button('Push DialogPage')
        .margin(20)
        .width('80%')
        .onClick(() => {
          this.pageStack.pushPathByName('DialogPage', '');
        })
    }
    .mode(NavigationMode.Stack)
    .title('Main')
    .navDestination(this.pageMapBuilder)
  }
}

@Component
export struct DialogPage {
  @Consume('NavPathStack') pageStack: NavPathStack;

  build() {
    NavDestination() {
      Stack({ alignContent: Alignment.Center }) {
        Column() {
          Text("Dialog NavDestination")
            .fontSize(20)
            .margin({ bottom: 100 })
          Button("Close")
            .onClick(() => {
              this.pageStack?.pop() ?? console.warn("Navigation stack is empty");
            })
            .width('30%')
        }
        .justifyContent(FlexAlign.Center)
        .borderRadius(10)
        .height('30%')
        .width('80%')
      }
      .height("100%")
      .width('100%')
    }
    .hideTitleBar(true)
    .mode(NavDestinationMode.DIALOG)
  }
}
```
