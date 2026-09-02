---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-26
title: 登录信息的cookie应该在什么时机注入？如何确保刚刚打开的web能注入登录信息cookie
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 登录信息的cookie应该在什么时机注入？如何确保刚刚打开的web能注入登录信息cookie
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6c66790be9212a684ca9e116fe00f0de78ed5cec803e676691dc9646c404d5c7
---

[webview.once](../harmonyos-references/arkts-apis-webview-f.md#webviewonce)可以订阅一次指定类型Web事件的回调。一般在web初始化完成后可以注入。

```ts
import { webview } from '@kit.ArkWeb'

webview.once("webInited", () => {
  console.log("setCookie");
  webview.WebCookieManager.configCookie("https://www.example.com", 'a=b,c=d,e=f');
})

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```
