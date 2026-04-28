---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-241
title: 如何让Grid组件在高度不确定的情况下，实现自适应高度
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何让Grid组件在高度不确定的情况下，实现自适应高度
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:02+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:193a1c55ffed4f1f806d67ebc71a31db78c688e5e39e4fefe0e48042b57ec903
---

**问题现象**

页面中使用Grid组件，因为GridItem数量不固定，且不允许滚动，理想中Grid组件高度会被GridItem内容自动撑起，实际体验中发现：

1. Grid必须显式设置固定height属性，这种由于GridItem数量不固定，且不允许出现滚动，不满足需求；

2. 设置maxCount属性后，可以实现高度被撑起，但与文档的解释好像不符，且GridItem数量不固定，所以也不满足需求；

3. Grid的height设置为auto时也不会被自动撑起。

**可能原因**

Grid不会自适应子节点的高度，不设置高度就是和父组件一样高。

**解决措施**

目前有两个替代方案：

1.使用list替代，设置其lanes属性进行分列。

2.可以动态计算GridItem高度，然后给Grid的height设置高度。

参考代码如下：

```
1. interface Item {
2. text: string
3. img: Resource
4. }

6. @Entry
7. @Component
8. struct Index {
9. data: Item[] = [
10. { text: 'aaa', img: $r('app.media.app_icon') },
11. { text: 'bbb', img: $r('app.media.app_icon') },
12. { text: 'ccc', img: $r('app.media.app_icon') },
13. { text: 'ddd', img: $r('app.media.app_icon') },
14. { text: 'eee', img: $r('app.media.app_icon') },
15. { text: 'fff', img: $r('app.media.app_icon') },
16. { text: 'ggg', img: $r('app.media.app_icon') },
17. { text: 'hhh', img: $r('app.media.app_icon') },
18. { text: 'jjj', img: $r('app.media.app_icon') },
19. { text: 'kkk', img: $r('app.media.app_icon') }]
20. // Calculate the number of rows in the grid
21. getCategoryRowCount() {
22. return Math.ceil(this.data.length / 4);
23. }
24. // Calculate the height of the grid based on the height of the item
25. getCategoryViewHeight() {
26. return `${68.33 * this.getCategoryRowCount()}vp`;
27. }

29. build() {
30. Column() {
31. Grid() {
32. ForEach(this.data, (item: Item) => {
33. GridItem() {
34. Column() {
35. Image(item.img)
36. .width(40)
37. .height(40)
38. Text(item.text)
39. .margin({ top: 2 })
40. .fontSize(14)
41. .textAlign(TextAlign.Center)
42. }
43. }
44. }, (item: Item) => item.text)
45. }
46. .height(this.getCategoryViewHeight())
47. .columnsTemplate('1fr 1fr 1fr 1fr')
48. .columnsGap(10)
49. .rowsGap(10)
50. .margin({ top: 10 })
51. }
52. .padding(10)
53. .width('100%')
54. }
55. }
```

[RealizeAdaptiveHeight.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/RealizeAdaptiveHeight.ets#L21-L75)
