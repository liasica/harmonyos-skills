---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-45
title: Web组件使用rawFile加载离线html时,如何在url后拼接参数
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web组件使用rawFile加载离线html时,如何在url后拼接参数
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:41+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:25c5a24703a6ad55e658346eee550db792254b6425ad3c914b2516227fe2a67f
---

使用Web组件加载时，可直接在URL中拼接参数。加载后，H5侧获取并使用这些参数。

**参考代码**

通过Web组件使用rawFile加载离线HTML，URL中包含参数。

```
1. import { webview } from '@kit.ArkWeb'

3. @Entry
4. @Component
5. struct WebComponent {
6. controller: webview.WebviewController = new webview.WebviewController()

8. build() {
9. Column() {
10. Web({ src: 'resource://rawfile/LoadingURLTransferParameters.html?key=value', controller: this.controller })
11. .javaScriptAccess(true)
12. .domStorageAccess(true)
13. }
14. .width('100%')
15. .height('100%')
16. }
17. }
```

[UrlAdd.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/ets/pages/UrlAdd.ets#L21-L37)

H5侧通过以下方式获取URL中的参数并使用。

```
1. <!DOCTYPE html>
2. <html>
3. <head>
4. <title>Parameter-based HTML</title>
5. </head>
6. <body>
7. <h1>Welcome!</h1>
8. <h1 id="params"></h1>

10. <script>
11. function getParams() {
12. var params = {};
13. window.location.search.substring(1).split('&').forEach(function(param) {
14. var pair = param.split('=');
15. params[pair[0]] = decodeURIComponent(pair[1]);
16. });
17. return params;
18. }
19. document.getElementById('params').innerHTML = JSON.stringify(getParams());
20. </script>
21. </body>
22. </html>
```

[LoadingURLTransferParameters.html](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/resources/rawfile/LoadingURLTransferParameters.html#L7-L28)
