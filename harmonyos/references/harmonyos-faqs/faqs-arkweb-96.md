---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-96
title: Web加载失败时的白屏页面如何改为自定义错误页
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web加载失败时的白屏页面如何改为自定义错误页
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f58bebdf802020cf95119e24a57aafd94fdd589d21dfe3fe42001793a422ccec
---

**问题场景：**

在网络条件较差或链接资源有问题时，Web组件加载失败会出现白屏状态，这种场景下用户无法感知页面加载状态，导致体验较差，需要将白屏替换为自定义错误页面的方案。

**解决措施：**

应用可以监听页面加载异常的相关事件如[onErrorReceive](../harmonyos-references/arkts-basic-components-web-events.md#onerrorreceive)、[onHttpErrorReceive](../harmonyos-references/arkts-basic-components-web-events.md#onhttperrorreceive)和[onSslErrorEventReceive](../harmonyos-references/arkts-basic-components-web-events.md#onsslerroreventreceive9)等，在对应的回调中按需实现业务逻辑，如使用[loadurl](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#loadurl)加载自定义错误页；本文以[onErrorReceive](../harmonyos-references/arkts-basic-components-web-events.md#onerrorreceive)为例对主资源报错的场景进行处理，加载本地错误页面资源文件。

```ts
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Stack() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onErrorReceive((event) => {
          // Only handle loading errors of the main framework to avoid duplicate processing of errors in sub-resources
          if (event && event.request.isMainFrame()) {
            try {
              // 加载自定义错误页面
              this.controller.loadUrl($rawfile('custom_failure_page.html'));
            } catch (error) {
              console.error(`ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`);
            }
          }
        })
    }
  }
}
```
