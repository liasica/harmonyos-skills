---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-153
title: Web组件loadUrl加载修改hash参数的链接页面未刷新
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web组件loadUrl加载修改hash参数的链接页面未刷新
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:33+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cbfc71674738a37da737f21091f25e695d668ba0f1306360b3ff24887a0c0f1d
---

## 问题现象

Web组件使用WebviewController的loadUrl加载仅修改URL的hash后的参数的链接，页面没有刷新。

## 背景知识

* [Web组件](../harmonyos-guides/web-component-overview.md)可通过src设置初始页面，但不可以通过状态管理（如：[@State](../harmonyos-guides/arkts-state.md)）的变量改变来变更页面。Web组件需要通过[WebviewController](../harmonyos-references/arkts-apis-webview-webviewcontroller.md)的[loadUrl](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#loadurl)方法去变更页面。
* [refresh](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#refresh)：调用此接口通知Web组件刷新网页。
* [setTimeout](../atomic-ascf/apis-timer.md#settimeout)：设定一个定时器，仅执行一次，等待delay时长后，执行callback函数。

## 问题定位

1. Web组件先后加载相同域名相同path仅URL的hash不同的页面，页面正常刷新。
2. Web组件先后加载相同域名相同path相同hash仅hash后携带参数不同的页面，页面没有刷新。
3. 在电脑浏览器上使用location.href按步骤2中的URL变更加载页面，浏览器页面也没有刷新。

## 分析结论

Web组件仅改变hash的携带参数会被默认是同一个地址，再使用loadUrl加载页面不会触发页面加载。

## 修改建议

此类情况建议使用WebviewController的loadUrl后调用refresh进行刷新，loadUrl之后直接refresh刷新，此时Web组件的URL并未实际变更，refresh进行刷新还是使用之前的URL刷新，所以需要setTimeout延迟10-100毫秒执行refresh方法。

```ts
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct Index {
  url: string = 'resource://rawfile/alertUrlHash.html#vip?token=token';
  controller: webview.WebviewController = new webview.WebviewController();
  uiContext: UIContext = this.getUIContext();

  build() {
    Column() {
      Button('变更hash参数重新加载页面').onClick(() => {
        this.changeHashParams();
      });
      Web({
        src: this.url,
        controller: this.controller
      })
        .javaScriptAccess(true)
        .fileAccess(true)
        .domStorageAccess(true)
        .geolocationAccess(false)
        .onAlert((event) => {
          if (event) {
            this.uiContext.showAlertDialog({
              title: `来自${event.url}的消息`,
              message: event.message,
              confirm: {
                value: '确认',
                action: () => {
                  console.info('Alert confirmed.');
                  event.result.handleConfirm();
                }
              },
              cancel: () => {
                event.result.handleCancel();
              }
            });
          }
          return true;
        });
    }
    .height('100%')
    .width('100%');
  }

  changeHashParams() {
    this.url = 'resource://rawfile/alertUrlHash.html#vip?token=123456';
    this.controller.loadUrl(this.url);
    // loadUrl后需要setTimeout延迟执行refresh方法，实测设置为5毫秒问题未解决，设置为10毫秒以上问题得以解决，此处延迟建议设置为10-100。
    setTimeout(() => {
      this.controller.refresh();
    }, 100);
  }
}
```

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Document</title>
</head>
<body>
<div>Hello World</div>
</body>
</html>
<script>
    alert(location.hash);
</script>
```
