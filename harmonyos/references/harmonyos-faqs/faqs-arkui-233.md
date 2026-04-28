---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-233
title: 如何实现页面加载的loading效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现页面加载的loading效果
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:00+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:2f5bf2ec48effa7dd2cc6e4381306e4cf0b0681d04867a1a67a332bc216fe706
---

使用Stack堆叠组件和LoadingProgress加载组件实现页面首次加载时的等待效果。参考代码如下：

```
1. @Entry
2. @Component
3. struct PageLoading {
4. @State isLoading: boolean = true;

6. aboutToAppear(): void {
7. // Simulate network request operation, request data from the network 3 seconds later, notify the component, and change the list data
8. setTimeout(() => {
9. this.isLoading = false;
10. }, 3000);
11. }

13. build() {
14. Stack() {
15. if (this.isLoading) {
16. Column() {
17. LoadingProgress()
18. .color(Color.White)
19. .width(80).height(80)
20. Text('Effortlessly loading..')
21. .fontSize(16)
22. .fontColor(Color.White)
23. }
24. .width('100%')
25. .height('100%')
26. .backgroundColor('#40000000')
27. .justifyContent(FlexAlign.Center)
28. } else {
29. Column(){
30. Text('主页')
31. }
32. }
33. }
34. .width('100%')
35. .height('100%')
36. .backgroundColor(Color.White)
37. }
38. }
```

[ImplementingPageLoading.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ImplementingPageLoading.ets#L21-L58)
