---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-277
title: 如何将ListItem的swipeAction滑动效果恢复到初始状态
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何将ListItem的swipeAction滑动效果恢复到初始状态
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:12+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:bbd948ed093237024cfd14840f3b1339a8ef8c0fd15a45053a0e344b377f0f01
---

使用 ListScroller 提供的 closeAllSwipeActions() 方法恢复滑动效果，示例代码如下：

```
1. @Component
2. export struct SwiperActionRecover {
3. @State arr: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
4. private scrollerForList: ListScroller = new ListScroller();

6. @Builder
7. itemEnd() {
8. Row() {
9. Button('Delete')
10. Button('Set')
11. .onClick(() => {
12. this.scrollerForList.closeAllSwipeActions(); // This is the key line of code
13. })
14. }
15. .justifyContent(FlexAlign.SpaceEvenly)
16. }

18. build() {
19. Column() {
20. List({ space: 5, scroller: this.scrollerForList }) {
21. ForEach(this.arr, (item: number) => {
22. ListItem() {
23. Text('item' + item)
24. .width('100%')
25. .height(100)
26. .textAlign(TextAlign.Center)
27. .borderRadius(10)
28. .backgroundColor(0xFFFFFF)
29. }
30. .transition({
31. type: TransitionType.Delete,
32. opacity: 0
33. })
34. .swipeAction({
35. end: {
36. builder: () => {
37. this.itemEnd();
38. },
39. onAction: () => {
40. this.getUIContext().animateTo({ duration: 1000 }, () => {
41. let index = this.arr.indexOf(item);
42. this.arr.splice(index, 1);
43. });
44. },
45. actionAreaDistance: 56
46. }
47. })
48. }, (item: string) => item)
49. }
50. }
51. .padding(20)
52. .backgroundColor(0xDCDCDC)
53. .width('100%')
54. .height('100%')
55. }
56. }
```

[SwipeActionToNotSlide.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/SwipeActionToNotSlide.ets#L21-L76)
