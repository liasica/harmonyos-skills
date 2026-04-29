---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-343
title: 如何实现直播评论场景中顶部渐变遮罩效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现直播评论场景中顶部渐变遮罩效果
category: harmonyos-faqs
scraped_at: 2026-04-29T14:17:26+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:54b4572457a1c3dd195c1dac396e5f42cf5b41f3b171fad1161cb79286ecdb93
---

1. 开发者可使用overlay在当前组件上添加遮罩。
2. 通过linearGradient可设置颜色渐变效果。
3. 使用blendMode让当前浮层与List混合。

代码示例如下：

```
1. @Entry
2. @Component
3. struct MaskDemo {
4. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

6. @Builder
7. createOverlayBuilder() {
8. Stack()
9. .height('100%')
10. .width('100%')
11. .linearGradient({
12. direction: GradientDirection.Bottom, // Gradient direction
13. colors: [['#00FFFFFF', 0.0], ['#FFFFFFFF',
14. 0.3]] // When the proportion of elements at the end of the array is less than 1, it satisfies the repeated shading effect
15. })
16. .blendMode(BlendMode.DST_IN, BlendApplyType.OFFSCREEN)// Implement a top gradient mask effect using the DST_IN blending mode.
17. .hitTestBehavior(HitTestMode.None)
18. }

20. build() {
21. Column() {
22. List({ space: 20, initialIndex: 0 }) {
23. ForEach(this.arr, (item: number) => {
24. ListItem() {
25. Text(item.toString())
26. .width('100%')
27. .height(100)
28. .fontSize(16)
29. .textAlign(TextAlign.Center)
30. .borderRadius(10)
31. .backgroundColor(0xFFFFFF)
32. }
33. .onClick(() => {
34. console.log('is click');
35. })
36. }, (item: string) => item)
37. }
38. .width('90%')
39. .height('100%')
40. .scrollBar(BarState.Off)
41. .overlay(this.createOverlayBuilder())
42. .blendMode(BlendMode.SRC_OVER, BlendApplyType.OFFSCREEN)
43. }
44. .width('100%')
45. .height('100%')
46. .backgroundColor(0xDCDCDC)
47. }
48. }
```

[GradientMaskForLiveCommentScene.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/GradientMaskForLiveCommentScene.ets#L21-L69)

实现效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/xiyMlsvrRfGO7aXLFq2T1g/zh-cn_image_0000002229604397.png?HW-CC-KV=V1&HW-CC-Date=20260429T061725Z&HW-CC-Expire=86400&HW-CC-Sign=58A8AA88654DB9E0681DAD1BEACA3C658CF8ECE20085F14C3425344AA8D1DC86)
