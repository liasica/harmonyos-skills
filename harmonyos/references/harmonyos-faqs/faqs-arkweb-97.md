---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-97
title: 返回的html里包含数学公式，怎么合理渲染到页面
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 返回的html里包含数学公式，怎么合理渲染到页面
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:51+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:2150b870a8f2beb3db75e1c2803875a3d8da1c99dad5f2a44ab87965c3cc1870
---

HarmonyOS目前没有提供专门的数学公式渲染组件，可以使用WebView组件来加载支持数学公式渲染的网页。

示例代码如下：

```
1. import { webview } from "@kit.ArkWeb"

3. @Component
4. export struct CourseLearning {
5. private webviewController: webview.WebviewController = new webview.WebviewController();

7. build() {
8. Column() {
9. Web({ src: $rawfile('Mathematics.html'), controller: this.webviewController })
10. .domStorageAccess(true)
11. .javaScriptAccess(true)
12. }
13. }
14. }
```

[CourseLearning.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/b39fe4e5abece291bdac1b844563003b397ce87d/ArkWebKit/entry/src/main/ets/pages/CourseLearning.ets#L18-L31)

示例代码中提供的html可参考[Mathematics.html](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/b39fe4e5abece291bdac1b844563003b397ce87d/ArkWebKit/entry/src/main/resources/rawfile/Mathematics.html)。
