---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-348
title: 如何实现List的折叠动画效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现List的折叠动画效果
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:29+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:623639e7bfed4c1c2894beb8367db874eb4422a1743d004cc987104a55f7fbda
---

可以使用显式动画animateTo结合条件渲染if控制 ListItem内容区域的展开和收起，示例代码如下：

```
1. @Entry
2. @Component
3. struct ListCollapseExpand {
4. private numberList: number[] = [0, 1, 2, 3, 4, 5, 6];
5. @State isContentShow: boolean = true;
6. @State selectItem: number = 0;

8. build() {
9. Column() {
10. List({ initialIndex: 0 }) {
11. ForEach(this.numberList, (item: number, index: number) => {
12. ListItem() {
13. Column() {
14. Row() {
15. Text(item.toString())
16. Button(this.isContentShow && this.selectItem === item ? 'Collapse' : 'Expand')
17. .onClick(() => {
18. this.getUIContext().animateTo({
19. duration: 300,
20. onFinish: () => {
21. console.info('animation end');
22. }
23. }, () => {
24. this.isContentShow = !this.isContentShow;
25. this.selectItem = item;
26. })
27. })
28. }
29. .width('100%')
30. .justifyContent(FlexAlign.SpaceBetween)

32. // Display the content area only when the current item is selected and is in an expanded state.
33. if (this.isContentShow && this.selectItem === item) {
34. Text('This is the content area')
35. .backgroundColor(Color.Gray)
36. .width('100%')
37. .height(100)
38. }
39. }
40. .backgroundColor(0xFFFFFF)
41. .width('100%')
42. .padding({
43. top: 12,
44. bottom: 12
45. })
46. .margin({ top: 10 })
47. }
48. }, (item: string) => item.toString())
49. }
50. .scrollBar(BarState.Off)
51. .height('100%')
52. .width('100%')
53. }
54. .backgroundColor(0xF1F3F5)
55. .padding(12)
56. }
57. }
```

[ListFoldAnimationEffect.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ListFoldAnimationEffect.ets#L21-L78)
