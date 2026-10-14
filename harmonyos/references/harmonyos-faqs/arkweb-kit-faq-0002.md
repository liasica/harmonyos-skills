---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkweb-kit-faq-0002
title: ArkWeb网页加载问题排查与解决
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 常见问题 > ArkWeb网页加载问题排查与解决
category: harmonyos-faqs
scraped_at: 2026-10-15T07:15:10+08:00
doc_updated_at: 2026-10-14
content_hash: sha256:d22e44e336ad22e8b1931eb1a05381bfd9fd1652650a4f662c89511e90909a61
---

**Q：Web组件加载发生错误对应错误码如何获取？**

**A**：网页加载遇到错误时触发[onErrorReceive](../harmonyos-references/arkts-basic-components-web-events.md#onerrorreceive)回调。回调函数会返回相关错误码，需要了解错误码的具体含义。相关错误码可以参考[@ohos.web.netErrorList (ArkWeb网络协议栈错误列表)](../harmonyos-references/arkts-apis-neterrorlist.md)。

**Q：Webview如何加载带有#路由的链接？**

**A**：Web组件的src使用'resource://rawfile/LoadWebLink.html#AAA'这种格式进行加载，具体可参考如下代码：

```ts
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
