---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-454
title: 如何监听Tabs里面TabContent页面显示
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何监听Tabs里面TabContent页面显示
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:58+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5b55b2287d14315e7d624ded37ab1f3b800d24f3286cf55fc5726e1396ee725d
---

**背景知识**

TabContent将要显示的时候触发onWillShow回调。场景包括：

1. TabContent首次显示
2. TabContent切换
3. 页面切换
4. 窗口前后台切换

TabContent将要隐藏的时候触发onWillHide回调。场景包括：

1. TabContent切换
2. 页面切换
3. 窗口前后台切换

**解决方案**

可以使用TabContent的[onWillShow()](../harmonyos-references/ts-container-tabcontent.md#onwillshow12)和[onWillHide()](../harmonyos-references/ts-container-tabcontent.md#onwillhide12)事件，在Tab页切换时上报TabContent的消失和出现。

**常见问题**

Q：如果要感知TabContent的子组件的出现或消失，如何实现？

A：可以使用onVisibleAreaChange监控子组件在屏幕上的显示或消失，当组件的可见面积与自身面积的比值变大为出现，比值变小为消失。示例代码如下：

```
1. @Component
2. struct MonitorTabContent {
3. build() {
4. Column() {
5. Tabs() {
6. TabContent() {
7. ChildrenComponent1();
8. }
9. // ...
10. }
11. .height('60%')
12. .barMode(BarMode.Fixed)
13. .backgroundColor(0xf1f3f5)
14. }
15. .width('100%')
16. .height(500)
17. .padding(24)
18. }
19. }

21. @Component
22. struct ChildrenComponent1 {
23. build() {
24. Column() {
25. Text('Tab 1 Content')
26. }
27. .onVisibleAreaChange([0, 1], (isExpanding, currentRatio) => {
28. if(isExpanding && currentRatio > 0) {
29. console.log('Tab 1 出现');
30. } else if(!isExpanding && currentRatio === 0) {
31. console.log('Tab 1 消失');
32. }
33. })
34. }
35. }
```

[MonitorTabContent.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/b9d6551b75b078dfbf00850327a0896f97877d23/ArkUI/entry/src/main/ets/pages/MonitorTabContent.ets#L21-L55)
