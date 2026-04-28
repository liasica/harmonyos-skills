---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-39
title: Web组件如何访问本地的资源文件，并添加查询参数
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web组件如何访问本地的资源文件，并添加查询参数
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:40+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:91aec036a30dff1e2effc5c659f0e2cd82ca7fc9dd8dae2be64edcbf1d7de07f
---

本地资源文件应存放在模块的“src/main/resources/rawfile”文件夹下，可通过 $rawfile('文件名') 访问。

目前不支持直接添加查询参数。但可以通过Web组件加载HTML文件，使用`window.location.href`跳转到带有参数的本地HTML页面。具体示例代码请参考文档。

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct WebComponent {
6. controller: webview.WebviewController = new webview.WebviewController();

8. build() {
9. Column() {
10. Web({ src: $rawfile('index.html'), controller: this.controller })
11. .javaScriptAccess(true)
12. }
13. }
14. }
```

[GetRawfileHtml.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/ets/pages/GetRawfileHtml.ets#L21-L34)

在“src\\main\\resources\\rawfile”文件夹下创建index.html和details.html文件。

index.html：

```
1. <!DOCTYPE html>
2. <html>
3. <head>
4. <script type="text/javascript"> window.onload = function() { window.location.href = "details.html"; }
5. </script>
6. </head>
7. <body></body>
8. </html>
```

[index.html](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/resources/rawfile/index.html#L7-L14)

details.html：

```
1. <!DOCTYPE html>
2. <html>
3. <head><title>详情页</title></head>
4. <body><h1>欢迎来到详情页！</h1>
5. <p>您已成功从首页跳转到此页，并在URL中添加了参数。</p></body>
6. </html>
```

[details.html](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/resources/rawfile/details.html#L8-L13)
