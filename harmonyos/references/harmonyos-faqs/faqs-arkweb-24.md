---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-24
title: 通过网络请求而来的 Cookie 如何同步配置到web中
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 通过网络请求而来的 Cookie 如何同步配置到web中
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3740463beab537cae7c28417db678da70e0f07e3c96a71c044b52ad5014792df
---

获取到的cookie利用[Class (WebCookieManager)](../harmonyos-references/arkts-apis-webview-webcookiemanager.md)提供的[configCookieSync](../harmonyos-references/arkts-apis-webview-webcookiemanager.md#configcookiesync11)方法与[configCookie](../harmonyos-references/arkts-apis-webview-webcookiemanager.md#configcookie11)方法可以实现对Cookie值的同步与异步设置，这样将请求而来的cookie同步到web中。

```ts
import { webview } from '@kit.ArkWeb'
@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  headers : Array<webview.WebHeader> = [{ headerKey : "msg",headerValue : 'hello'}];
  build() {
    Column() {
      Button('configCookieSync')
        .onClick(() => {
          try {
            webview.WebCookieManager.configCookieSync('https://www.example.com', 'a=b;c=d;e=f');
          } catch (error) {
            console.error(`ErrorCode: ${error.code},  Message: ${error.message}`);
          }
        })
      Button('fetchCookieSync')
        .onClick(() => {
          try {
            let value = webview.WebCookieManager.fetchCookieSync('https://www.example.com');
            console.log("fetchCookieSync cookie = " + value);
          } catch (error) {
            console.error(`ErrorCode: ${error.code},  Message: ${error.message}`);
          }
        })
      Column() {
        Web({ src: 'www.example.com', controller: this.controller })
          .width('100%')
          .height('100%')
      }
      .layoutWeight(1)
    }
  }
}
```
