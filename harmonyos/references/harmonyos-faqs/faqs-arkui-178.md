---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-178
title: 如何实现上下切换的页面间跳转动画
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现上下切换的页面间跳转动画
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:46+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a622153aa227c683b5af07cd33c9457c2e709aa93663c0cfc00db7486a4d1ef0
---

使用pageTransition函数实现页面转场效果。通过PageTransitionEnter和PageTransitionExit指定页面进入和退出的动画效果。将slide属性设置为SlideEffect.Bottom，页面入场时从下方滑入，出场时滑出到下方，从而实现上下切换效果。参考代码如下：

```
1. // Index.ets
2. @Entry
3. @Component
4. struct PageTransition1 {
5. pageInfos: NavPathStack = new NavPathStack();

7. build() {
8. Stack({ alignContent: Alignment.Bottom }) {
9. Navigation(this.pageInfos) {
10. Image($r('app.media.ic_banner01')).width('100%').height(200) // The image is stored in the media folder
11. }
12. }.height('100%').width('100%')
13. }

15. pageTransition() {
16. PageTransitionEnter({ duration: 500, curve: Curve.Linear }).slide(SlideEffect.Bottom)
17. PageTransitionExit({ duration: 500, curve: Curve.Ease }).slide(SlideEffect.Bottom)
18. }
19. }
```

[ImplementPageSwitchingAnimation\_One.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ImplementPageSwitchingAnimation_One.ets#L21-L39)

```
1. // Page1.ets
2. @Entry
3. @Component
4. struct PageTransition2 {
5. pageInfos: NavPathStack = new NavPathStack();

7. build() {
8. Stack({ alignContent: Alignment.Bottom }) {
9. Navigation(this.pageInfos) {
10. Image($r('app.media.ic_banner02')).width('100%').height(200) // The image is stored in the media folder
11. }
12. }.height('100%').width('100%')
13. }

15. pageTransition() {
16. PageTransitionEnter({ duration: 500, curve: Curve.Linear }).slide(SlideEffect.Bottom)
17. PageTransitionExit({ duration: 500, curve: Curve.Ease }).slide(SlideEffect.Bottom)
18. }
19. }
```

[ImplementPageSwitchingAnimation\_Two.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ImplementPageSwitchingAnimation_Two.ets#L21-L39)

**参考链接**

[页面间转场](../harmonyos-references/ts-page-transition-animation.md)
