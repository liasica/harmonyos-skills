---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-19
title: 如何解决两层Tabs出现滑动冲突的情况
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何解决两层Tabs出现滑动冲突的情况
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:03+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a5d8a37f60cd8ad9dd6874187c9a794dbf01157000a33645b23f1d5d9ad4b953
---

通过给外层Tabs设置scrollable(false)实现两层Tabs嵌套底部导航+顶部导航的组合，参考代码如下：

```
1. @Entry
2. @Component
3. struct TwoLayerTabNestedSliding {
4. build() {
5. Column() {
6. Tabs({ barPosition: BarPosition.End }) {
7. TabContent() {
8. Column() {
9. Tabs() {
10. TabContent() {
11. Text('Focus on content')
12. }
13. .tabBar('follow with interest')
14. TabContent() {
15. Text('The content of the game')
16. }
17. .tabBar('game')
18. }
19. }
20. .backgroundColor('#f08a34')
21. .width('100%')
22. }
23. .tabBar('home page')
24. TabContent() {
25. Column() {
26. Tabs() {
27. TabContent() {
28. Text('The content of technology')
29. }
30. .tabBar('science and technology')
31. TabContent() {
32. Text('The content of the video')
33. }
34. .tabBar('video')
35. }
36. }
37. .backgroundColor('#f08a34')
38. .width('100%')
39. }
40. .tabBar('find')
41. }
42. .scrollable(false)
43. }
44. .width('100%')
45. .height('100%')
46. }
47. }
```

[ResolveTwoLayersOfTabs.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ResolveTwoLayersOfTabs.ets#L21-L67)

[限制导航栏的滑动切换](../harmonyos-guides/arkts-navigation-tabs.md#限制导航栏的滑动切换)
