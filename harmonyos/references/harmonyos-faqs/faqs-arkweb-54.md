---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-54
title: PDF预览如何隐藏PDF操作按钮栏
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > PDF预览如何隐藏PDF操作按钮栏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e0a8ddfdb73b4c606e1e37d1e5da22d5dcf8b09f3122833fb884683481d979d7
---

**解决措施**

在URL中加入#toolbar=0&navpanes=0参数即可隐藏PDF操作栏按钮。

**参考代码**

```ts
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct HidePDFToolbar {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      // Hide the toolbar (toolbar=0) and navigation pane (navpanes=0) through URL parameters
      Web({ src: 'resource://rawfile/test.pdf#toolbar=0&navpanes=0', controller: this.controller })
        .domStorageAccess(true)
        .width('100%')
        .height('100%')
    }
    .width('100%')
    .height('100%')
  }
}
```
