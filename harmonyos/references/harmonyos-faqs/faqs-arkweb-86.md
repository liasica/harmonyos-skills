---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-86
title: Webview如何加载带有#路由的链接
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Webview如何加载带有#路由的链接
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1b243c4d0ad3439be59fe163cd055cd4de47da67161647e902893ec20b7d85ae
---

Web组件的src使用'resource://rawfile/LoadWebLink.html#AAA'这种格式进行加载，具体可参考如下代码：

```typescript
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct LoadWebLink {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    RelativeContainer() {
      Web({ src: 'resource://rawfile/LoadWebLink.html#AAA', controller: this.controller })
    }
    .height('100%')
    .width('100%')
  }
}
```
