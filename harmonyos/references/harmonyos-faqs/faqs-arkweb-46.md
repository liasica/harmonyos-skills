---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-46
title: 如何在webview中使用H5中的alert
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 如何在webview中使用H5中的alert
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:20701b5ca225a5188819ba308984acd3d22e194c91a84b63bf46d314d34b9a2f
---

**参考代码**

使用Web组件的[onAlert](../harmonyos-references/arkts-basic-components-web-events.md#onalert)属性可以监听网页触发alert()告警弹窗事件，之后使用[警告弹窗 (AlertDialog)](../harmonyos-references/ts-methods-alert-dialog-box.md)实现弹窗的效果与逻辑。

```ts
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebviewAlert {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile('WebviewAlert.html'), controller: this.controller })
        .onAlert((event) => {
          if (event) {
            console.log('event.url:' + event.url);
            console.log('event.message:' + event.message);
            this.getUIContext().showAlertDialog({
              title: 'onAlert',
              message: 'text',
              primaryButton: {
                value: 'cancel',
                action: () => {
                  event.result.handleCancel();
                }
              },
              secondaryButton: {
                value: 'ok',
                action: () => {
                  event.result.handleConfirm();
                }
              },
              cancel: () => {
                event.result.handleCancel();
              }
            })
          }
          return true;
        })
    }
  }
}
```

H5侧：

```html
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" charset="utf-8">
</head>
<body>
<h1>WebView onAlert Demo</h1>
<button onclick="myFunction()">Click here</button>
<script>
    function myFunction() {
      alert("Hello World");
    }
</script>
</body>
</html>
```
