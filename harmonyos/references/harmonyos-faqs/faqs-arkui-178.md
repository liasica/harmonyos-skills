---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-178
title: 如何实现上下切换的页面间跳转动画
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现上下切换的页面间跳转动画
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:50be04228a81fce872400751b18a13de777e75cc647c573ed963351e251b3928
---

使用pageTransition函数实现页面转场效果。通过PageTransitionEnter和PageTransitionExit指定页面进入和退出的动画效果。将slide属性设置为SlideEffect.Bottom，页面入场时从下方滑入，出场时滑出到下方，从而实现上下切换效果。参考代码如下：

```ts
// Index.ets
@Entry
@Component
struct PageTransition1 {
  pageInfos: NavPathStack = new NavPathStack();

  build() {
    Stack({ alignContent: Alignment.Bottom }) {
      Navigation(this.pageInfos) {
        Image($r('app.media.ic_banner01')).width('100%').height(200) // The image is stored in the media folder
      }
    }.height('100%').width('100%')
  }

  pageTransition() {
    PageTransitionEnter({ duration: 500, curve: Curve.Linear }).slide(SlideEffect.Bottom)
    PageTransitionExit({ duration: 500, curve: Curve.Ease }).slide(SlideEffect.Bottom)
  }
}
```

```ts
// Page1.ets
@Entry
@Component
struct PageTransition2 {
  pageInfos: NavPathStack = new NavPathStack();

  build() {
    Stack({ alignContent: Alignment.Bottom }) {
      Navigation(this.pageInfos) {
        Image($r('app.media.ic_banner02')).width('100%').height(200) // The image is stored in the media folder
      }
    }.height('100%').width('100%')
  }

  pageTransition() {
    PageTransitionEnter({ duration: 500, curve: Curve.Linear }).slide(SlideEffect.Bottom)
    PageTransitionExit({ duration: 500, curve: Curve.Ease }).slide(SlideEffect.Bottom)
  }
}
```

**参考链接**

[页面间转场](../harmonyos-references/ts-page-transition-animation.md)
