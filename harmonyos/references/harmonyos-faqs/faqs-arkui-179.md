---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-179
title: 自定义组件间如何实现从底部滑入滑出的效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 自定义组件间如何实现从底部滑入滑出的效果
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:46+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:3118669a4c8fa3a89e695d5504ab1a92c8334e18eded74de7b8ac2d5c253f82c
---

**问题现象**

页面底部默认显示自定义组件A。点击组件A，A消失，自定义组件B从底部出现。点击组件B，B消失，A从底部出现。如何实现这个效果？

**解决措施**

使用transition产生组件转场动画。参数type用于设置组件变化场景，包括新增和删除；参数translate用于设置转场时的平移效果。注意，transition需要配合animateTo才能生效，动效的时长、曲线和延时需跟随animateTo中的配置。参考代码如下：

```
1. @Entry
2. @Component
3. struct ComponentTransition {
4. @State flag: boolean = true;

6. build() {
7. Stack({ alignContent: Alignment.Bottom }) {
8. if (this.flag) {
9. ComponentChild1({ flag: $flag })
10. .transition({ type: TransitionType.Insert,translate: { x: 0, y: 200 } })
11. }
12. if (!this.flag) {
13. ComponentChild2({ flag: $flag })
14. .transition({ type: TransitionType.Insert, translate: { x: 0, y: 200 } })
15. }
16. }.height('100%').width('100%')
17. }
18. }

20. @Component
21. struct ComponentChild1 {
22. @Link flag: boolean

24. build() {
25. Column() {
26. Image($r('app.media.ic_banner01'))// path: resources\base\media
27. .width('100%')
28. .height(200)
29. .onClick(() => {
30. this.getUIContext().animateTo({ duration: 1000 }, () => {
31. this.flag = !this.flag;
32. })
33. })
34. }
35. }
36. }

38. @Component
39. struct ComponentChild2 {
40. @Link flag: boolean

42. build() {
43. Column() {
44. Image($r('app.media.ic_banner02'))// path: resources\base\media
45. .width('100%')
46. .height(200)
47. .onClick(() => {
48. this.getUIContext().animateTo({ duration: 1000 }, () => {
49. this.flag = !this.flag;
50. })
51. })
52. }
53. }
54. }
```

[BottomSlideAndOut.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/BottomSlideAndOut.ets#L21-L74)

**参考链接**

[组件内转场](../harmonyos-references/ts-transition-animation-component.md)
