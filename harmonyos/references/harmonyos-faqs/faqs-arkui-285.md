---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-285
title: 跳转页面如何实现页面级别的透明效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 跳转页面如何实现页面级别的透明效果
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:15+08:00
doc_updated_at: 2026-04-27
content_hash: sha256:26fdc3594523d1f3f681e4127de1088177e8305a11486049a4e63d66252ee244
---

推荐使用的是Navigation跳转方式，可以将NavDestination设置mode为NavDestinationMode.DIALOG弹窗类型，此时整个NavDestination页面默认透明显示，具体可以参考：[页面显示类型](../harmonyos-guides/arkts-navigation-navdestination.md#页面显示类型)中的弹窗类型。示例代码如下：

```
1. @Component
2. export struct TransparentPage {
3. @Provide('NavPathStack') pageStack: NavPathStack = new NavPathStack();

5. @Builder
6. pageMapBuilder(name: string) {
7. if (name === 'DialogPage') {
8. DialogPage()
9. }
10. }

12. build() {
13. Navigation(this.pageStack) {
14. Button('Push DialogPage')
15. .margin(20)
16. .width('80%')
17. .onClick(() => {
18. this.pageStack.pushPathByName('DialogPage', '');
19. })
20. }
21. .mode(NavigationMode.Stack)
22. .title('Main')
23. .navDestination(this.pageMapBuilder)
24. }
25. }

27. @Component
28. export struct DialogPage {
29. @Consume('NavPathStack') pageStack: NavPathStack;

31. build() {
32. NavDestination() {
33. Stack({ alignContent: Alignment.Center }) {
34. Column() {
35. Text("Dialog NavDestination")
36. .fontSize(20)
37. .margin({ bottom: 100 })
38. Button("Close")
39. .onClick(() => {
40. this.pageStack?.pop() ?? console.warn("Navigation stack is empty");
41. })
42. .width('30%')
43. }
44. .justifyContent(FlexAlign.Center)
45. .borderRadius(10)
46. .height('30%')
47. .width('80%')
48. }
49. .height("100%")
50. .width('100%')
51. }
52. .hideTitleBar(true)
53. .mode(NavDestinationMode.DIALOG)
54. }
55. }
```

[RealizePageLevelTransparencyEffect.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/RealizePageLevelTransparencyEffect.ets#L21-L75)
