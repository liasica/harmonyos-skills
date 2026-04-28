---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-386
title: 如何禁用Refresh组件的下拉刷新
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何禁用Refresh组件的下拉刷新
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:42+08:00
doc_updated_at: 2026-03-25
content_hash: sha256:69f33fc2f6a8cb94803eb15fa7eb6393e20161c89c4053a7393a568c079f47e5
---

**问题现象**

在使用Refresh组件时，开发者需要控制Refresh组件的下拉刷新功能，实现临时禁用或者开启下拉刷新。

**解决措施**

可以通过[pullDownRatio](../harmonyos-references/ts-container-refresh.md#pulldownratio12)设置跟手系数，当设置为0时，表示不跟随手势下拉，即可禁用下拉刷新。

禁用Refresh组件下拉刷新的示例如下：

```
1. @Entry
2. @Component
3. struct Index {
4. @State isRefreshing: boolean = false;
5. @State arr: String[] = ['0', '1', '2', '3', '4', '5'];
6. @State downRatio: number = 1;

8. build() {
9. Column() {
10. Refresh({ refreshing: $$this.isRefreshing }) {
11. Column() {
12. Row({ space: 10 }) {
13. Button('不允许下拉刷新')
14. .onClick(() => {
15. this.downRatio = 0;
16. })
17. Button('允许下拉刷新')
18. .onClick(() => {
19. this.downRatio = 1;
20. })
21. }

23. List() {
24. ForEach(this.arr, (item: string) => {
25. ListItem() {
26. Text('' + item)
27. .width('70%')
28. .height(80)
29. .fontSize(16)
30. .margin(10)
31. .textAlign(TextAlign.Center)
32. .borderRadius(10)
33. .backgroundColor(0xFFFFFF)
34. }
35. }, (item: string) => item)
36. }
37. .onScrollIndex((first: number) => {
38. console.info(first.toString());
39. })
40. .width('100%')
41. .height('100%')
42. .alignListItem(ListItemAlign.Center)
43. .scrollBar(BarState.Off)
44. }
45. }
46. .onRefreshing(() => {
47. setTimeout(() => {
48. this.isRefreshing = false;
49. }, 2000)
50. console.info('onRefreshing test');
51. })
52. .pullDownRatio(this.downRatio)
53. .backgroundColor(0x89CFF0)
54. .refreshOffset(64)
55. .pullToRefresh(true)
56. }
57. }
58. }
```

[DisablePullDownRefresh.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/abce1db5a4cf676fd100dbd3a0acd02f5bb30358/ArkUI/entry/src/main/ets/pages/DisablePullDownRefresh.ets#L6-L64)
