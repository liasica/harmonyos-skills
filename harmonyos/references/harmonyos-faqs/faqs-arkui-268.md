---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-268
title: List的下拉加载如何回滚到当前展示位置
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > List的下拉加载如何回滚到当前展示位置
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:09+08:00
doc_updated_at: 2026-03-25
content_hash: sha256:cdb28ad9f8b989b0a5ef9fe5e3dbfd004bd4d430b76399269f3c1364434d7aeb
---

**需求描述：**

List组件顶部下拉刷新时，期望数据加载后仍保持刷新前可见的首项元素位置。

**实现方法**：

可以给List添加scroller控制器，通过控制器将列表滚动回刷新前的位置this.scroller.scrollToIndex，示例代码如下：

```
1. @Entry
2. @Component
3. struct RefreshDemo {
4. @State isRefreshing: boolean = false;
5. @State arr: String[] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'];
6. // Used to control the scrolling position of the list and maintain consistency of the view after refreshing
7. private listScroller: Scroller = new Scroller();

9. build() {
10. Column() {
11. Refresh({ refreshing: $$this.isRefreshing }) {
12. List({ scroller: this.listScroller, space: 10 }) {
13. ForEach(this.arr, (item: string) => {
14. ListItem() {
15. Text(item)
16. .width('100%')
17. .height(100)
18. .textAlign(TextAlign.Center)
19. .backgroundColor(Color.Grey)
20. }
21. }, (item: string) => item)
22. }
23. .onScrollIndex((first: number) => {
24. console.info(first.toString());
25. })
26. .width('100%')
27. .height('100%')
28. }
29. .onRefreshing(() => {
30. setTimeout(() => {
31. this.isRefreshing = false;
32. }, 2000)
33. let originalCount = this.arr.length;
34. this.arr.unshift('11');
35. this.arr.unshift('12');
36. this.listScroller.scrollToIndex(this.arr.length - originalCount);
37. })
38. }
39. }
40. }
```

[ListDropdownLoadRollbackCurrentLocation.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ListDropdownLoadRollbackCurrentLocation.ets#L21-L61)
