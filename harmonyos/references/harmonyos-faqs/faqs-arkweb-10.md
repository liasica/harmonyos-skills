---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-10
title: Web组件中如何通过手势滑动返回上一个Web页面
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web组件中如何通过手势滑动返回上一个Web页面
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:38+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:656ba6659a29402823b060abcf5362b66d16784f6626a78f504659ad4845166d
---

重写onBackPress函数，自定义返回逻辑，通过WebViewController提供的两种接口：accessBackward或accessStep(-1)，都可以实现对web页面是否可以后退情况的判断，进而对web页面进行返回操作。参考代码如下：

```
1. import { webview } from "@kit.ArkWeb";

3. @Entry
4. @Component
5. struct PageOne {
6. pageInfos: NavPathStack = new NavPathStack();
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. NavDestination() {
11. Column() {
12. Web({ src: 'https://www.XXX.com/', controller: this.controller }) // It needs to be manually replaced with the actual website
13. }
14. .width('100%')
15. .height('100%')
16. }
17. .title('pageOne')
18. .onBackPressed(() => {
19. if (this.controller.accessBackward()) { // Determine whether the web page can be navigated back
20. this.controller.backward() // Navigate back to the previous webpage
21. return true
22. } else {
23. const popDestinationInfo = this.pageInfos.pop(); // Pop the top element of the routing stack
24. return true;
25. }
26. }).onReady((context: NavDestinationContext) => {
27. this.pageInfos = context.pathStack;
28. })
29. }
30. }
```

[BackPageByGestures.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/ets/pages/BackPageByGestures.ets#L21-L50)

**参考链接**

[accessBackward](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#accessbackward)

[accessStep](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#accessstep)
