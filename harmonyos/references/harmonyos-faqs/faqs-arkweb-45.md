---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-45
title: Web组件使用rawFile加载离线html时,如何在url后拼接参数
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web组件使用rawFile加载离线html时,如何在url后拼接参数
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5e2d8137bcabe1cbef604110aa359f63f23028ec289de88609639507b029f3c3
---

使用Web组件加载时，可直接在URL中拼接参数。加载后，H5侧获取并使用这些参数。

**参考代码**

通过Web组件使用rawFile加载离线HTML，URL中包含参数。

```ts
import { webview } from '@kit.ArkWeb'

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController()

  build() {
    Column() {
      Web({ src: 'resource://rawfile/LoadingURLTransferParameters.html?key=value', controller: this.controller })
        .javaScriptAccess(true)
        .domStorageAccess(true)
    }
    .width('100%')
    .height('100%')
  }
}
```

H5侧通过以下方式获取URL中的参数并使用。

```html
<!DOCTYPE html>
<html>
<head>
    <title>Parameter-based HTML</title>
</head>
<body>
<h1>Welcome!</h1>
<h1 id="params"></h1>

<script>
    function getParams() {
        var params = {};
        window.location.search.substring(1).split('&').forEach(function(param) {
            var pair = param.split('=');
            params[pair[0]] = decodeURIComponent(pair[1]);
        });
        return params;
    }
    document.getElementById('params').innerHTML = JSON.stringify(getParams());
</script>
</body>
</html>
```
