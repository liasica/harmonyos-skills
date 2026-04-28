---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-278
title: 如何实现List/Swiper/Grid嵌套滚动的下拉刷新和上拉加载更多
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现List/Swiper/Grid嵌套滚动的下拉刷新和上拉加载更多
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:12+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:98b382f46da5e4e5a16c6dd673270881c8883aee033446f1112952be0a709da4
---

开发者可通过Refresh组件嵌套List实现下拉刷新。刷新逻辑在onRefreshing回调方法中执行。上拉加载更多给List添加onReachEnd事件回调，列表滑动到底部时触发。示例代码如下：

```
1. build() {
2. Column() {
3. // Search box at the top
4. this.searchBarBuilder()
5. // Pull down refresh component
6. Refresh({ refreshing: $$this.isRefreshing }) {
7. // List component as long list layout
8. List({ space: 10 }) {
9. // ListItem Customize the Swiper carousel module
10. ListItem() {
11. this.bannerBuilder()
12. }
13. // ListItem Custom Grid Quick Access Module
14. ListItem() {
15. this.quickBuilder()
16. }
17. // ListItem Custom Column Flash Sale Module
18. ListItem() {
19. this.flashBuilder()
20. }
21. // ListItemGroup Product Classification List
22. this.productsBuilder()
23. // 最后ListItem Customize bottom loading for more
24. ListItem() {
25. this.footerLoadingBuilder()
26. }.height(50).width('100%').backgroundColor(0xeeeeee)
27. }
28. .sticky(StickyStyle.Header)
29. .height('100%')
30. // List component hits bottom to simulate network requests
31. .onReachEnd(() => {
32. // Load more data logic
33. })
34. }
35. // Pull down refresh simulation network request
36. .onRefreshing(() => {
37. // Data refresh logic
38. })
39. .layoutWeight(1)
40. .width('100%')
41. }
42. }
```

[ListWiperGridPullDownPullUp.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ListWiperGridPullDownPullUp.ets#L31-L72)
