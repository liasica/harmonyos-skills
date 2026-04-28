---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-54
title: PDF预览如何隐藏PDF操作按钮栏
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > PDF预览如何隐藏PDF操作按钮栏
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:43+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:75b863761b72d7c00060d7b05fd3c109f7cc73b8cf6ced72ddf90cd3c20ea8aa
---

**解决措施**

在URL中加入#toolbar=0&navpanes=0参数即可隐藏PDF操作栏按钮。

**参考代码**

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct HidePDFToolbar {
6. controller: webview.WebviewController = new webview.WebviewController();

8. build() {
9. Column() {
10. // Hide the toolbar (toolbar=0) and navigation pane (navpanes=0) through URL parameters
11. Web({ src: 'resource://rawfile/test.pdf#toolbar=0&navpanes=0', controller: this.controller })
12. .domStorageAccess(true)
13. .width('100%')
14. .height('100%')
15. }
16. .width('100%')
17. .height('100%')
18. }
19. }
```

[HidePdf.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/ets/pages/HidePdf.ets#L21-L39)
