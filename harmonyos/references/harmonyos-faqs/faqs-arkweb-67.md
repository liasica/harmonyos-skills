---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-67
title: WebView如何设置mixcontent策略，用以解决http与https混合加载的问题
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > WebView如何设置mixcontent策略，用以解决http与https混合加载的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c52c77f15501aec9d8450c7d95856c9b9f2f17691ac6cc3ce542bccbf806cc2c
---

ArkWeb提供mixedMode(mixedMode: MixedMode)接口，用于设置是否允许加载HTTP和HTTPS混合内容。默认情况下，不允许加载混合内容。

在工程的module.json5配置文件中添加网络访问权限ohos.permission.INTERNET。

参考代码如下：

```screen
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  // MixedMode.All indicates that all mixed content is allowed to be loaded (HTTP/HTTPS)
  @State mixedMode: MixedMode = MixedMode.All;
  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .mixedMode(this.mixedMode)
    }
  }
}
```

**参考链接**

[mixedMode](../harmonyos-references/arkts-basic-components-web-attributes.md#mixedmode)
