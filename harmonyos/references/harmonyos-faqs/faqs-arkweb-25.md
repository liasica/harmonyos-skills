---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-25
title: 多个Cookie如何进行批量设置
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 多个Cookie如何进行批量设置
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b9fd944b00c0a8bfb5ffe9ab3f2dd9c0b289562a1bc85e95f0f28f7fa850f8b2
---

[Class (WebCookieManager)](../harmonyos-references/arkts-apis-webview-webcookiemanager.md)提供了[configCookieSync](../harmonyos-references/arkts-apis-webview-webcookiemanager.md#configcookiesync11)方法与[configCookie](../harmonyos-references/arkts-apis-webview-webcookiemanager.md#configcookie11)方法，用于同步和异步设置 Cookie。目前，接口不支持一次性批量设置多个 Cookie，建议通过多次调用 `configCookie` 或 `configCookieSync` 方法来实现多个 Cookie 的设置。

```ts
import { webview } from '@kit.ArkWeb';

webview.once("webInited", () => {
  console.info("webInited setCookie");
  webview.WebCookieManager.configCookie("https://www.example.com", 'a=b');
  webview.WebCookieManager.configCookie("https://www.example.com", 'c=d');
  webview.WebCookieManager.configCookie("https://www.example.com", 'e=f');
})

@Entry
@Component
struct LoginCookieConfig {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('fetchCookieSync')
        .onClick(() => {
          try {
            let value = webview.WebCookieManager.fetchCookieSync('https://www.example.com');
            console.log(`fetchCookieSync cookie value is: ${value}`);
          } catch (error) {
            console.error(`fetchCookieSync failed,error is: ${JSON.stringify(error)}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```
