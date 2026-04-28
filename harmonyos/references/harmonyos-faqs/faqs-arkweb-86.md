---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-86
title: Webview如何加载带有#路由的链接
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Webview如何加载带有#路由的链接
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:49+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:13f57a6b51fc3649ab95ccd1bbb4fba9990b457b7b0452a0e1124a04c5314c64
---

Web组件的src使用'resource://rawfile/LoadWebLink.html#AAA'这种格式进行加载，具体可参考如下代码：

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct LoadWebLink {
6. controller: webview.WebviewController = new webview.WebviewController();

8. build() {
9. RelativeContainer() {
10. Web({ src: 'resource://rawfile/LoadWebLink.html#AAA', controller: this.controller })
11. }
12. .height('100%')
13. .width('100%')
14. }
15. }
```

[RouteLink.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/ets/pages/RouteLink.ets#L21-L35)
