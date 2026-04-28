---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-26
title: 如何解决List组件在不设置高度的情况下滑动不到底的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何解决List组件在不设置高度的情况下滑动不到底的问题
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:04+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:356d87e8dfd8d1d8588ff1d04c7a16bf402171595c5cc5d367b411fd94c8b659
---

**原因**

当List组件中的子项数量较多时，如果同级存在其他组件，会挤压List组件的布局空间，导致显示异常。

**解决措施**

给List组件设置layoutWeight()属性。layoutWeight()使子元素自适应占满父容器的剩余空间。当父容器尺寸确定时，设置了layoutWeight的子元素在主轴布局中的尺寸将按照权重分配，忽略其本身的尺寸设置。可参考如下代码：

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ListExample {
5. @State arr: string[] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'];
6. scroller: Scroller = new Scroller();

8. build() {
9. Column() {
10. RichText('')
11. .width('90%')
12. .height(300)
13. .backgroundColor(0XBDDB69)
14. List({ space: 22, initialIndex: 0, scroller: this.scroller }) {
15. ForEach(this.arr, (item: string) => {
16. ListItem() {
17. Text(item)
18. .width('100%')
19. .height(100)
20. .fontSize(16)
21. .textAlign(TextAlign.Center)
22. .borderRadius(10)
23. .backgroundColor(0xFFFFFF)
24. }
25. }, (item: string) => item)
26. }
27. .layoutWeight(1) // Adaptive occupancy of remaining space
28. .listDirection(Axis.Vertical) // Arrangement direction
29. .divider({ strokeWidth: 2, color: 0xFFFFFF, startMargin: 20, endMargin: 20 }) // The boundary line between each row
30. .edgeEffect(EdgeEffect.Spring) // Sliding to the edge has no effect
31. .scrollBar(BarState.Off) // Set scrollbar
32. .margin({ top: 20 })
33. .width('90%')
34. }
35. .width('100%')
36. .height('100%')
37. .backgroundColor(0xDCDCDC)
38. }
39. }
```

[ListDoesNotSetHeight.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ListDoesNotSetHeight.ets#L21-L59)

效果如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/Ya7R8uEfRo6wVBFpQuJfpg/zh-cn_image_0000002194158648.png?HW-CC-KV=V1&HW-CC-Date=20260428T002503Z&HW-CC-Expire=86400&HW-CC-Sign=41B382A45F454F318E3DE278C2E830FB4C21A2D5980B592CCF110DFE866F5933 "点击放大")
