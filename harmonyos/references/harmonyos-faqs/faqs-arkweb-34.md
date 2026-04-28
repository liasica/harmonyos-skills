---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-34
title: 如何控制只在Web组件第一次加载url的时候触发onPageBegin，onPageEnd
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 如何控制只在Web组件第一次加载url的时候触发onPageBegin，onPageEnd
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:39+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b4274d2a65009917fc7c06b5f66d609117506a5a6c2fa7520c35b3d16e70692e
---

使用onAppear事件控制仅在首次加载URL时触发onPageBegin和onPageEnd，参考代码如下：

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct OnlyOnTheFirstTrigger {
6. controller: webview.WebviewController = new webview.WebviewController();
7. isFirst: boolean = false;

9. build() {
10. Column() {
11. Web({
12. src: 'www.example.com', controller: this.controller
13. })
14. .onAppear(() => {
15. this.isFirst = true;
16. })
17. .onPageBegin(() => {
18. if (this.isFirst) {
19. this.isFirst = false;
20. console.info('First page loading triggered');
21. }
22. })
23. }
24. .width('100%')
25. .height('100%')
26. }
27. }
```

[OnlyOnTheFirstTrigger.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/ets/pages/OnlyOnTheFirstTrigger.ets#L21-L47)
