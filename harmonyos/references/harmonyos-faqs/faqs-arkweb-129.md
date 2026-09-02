---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-129
title: loadUrl加载Web页面时添加headers参数失败
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > loadUrl加载Web页面时添加headers参数失败
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:224f8f06ab3b2f30f2c5b89b7a6e9280f094f2ef6fb3079f216590e517434343
---

## 问题现象

通过loadUrl加载页面后，在设置header时遇到以下问题：

使用this.webviewController.loadUrl(toUrl, toHeader)方法重新加载页面，方法里面带上了header的参数会出现如下报错：

```txt
Error message:Init error. The WebviewController must be associated with a Web component
```

## 背景知识

* [loadUrl](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#loadurl)：用于加载指定的URL，该API除了指定需要加载的URL外，还可以设置URL的附加HTTP请求头。
* [onControllerAttached](../harmonyos-references/arkts-basic-components-web-events.md#oncontrollerattached10)：当Controller成功绑定到Web组件时触发该回调，并且该Controller必须为WebviewController，且禁止在该事件回调前调用Web组件相关的接口，否则会抛出js-error异常。

## 问题定位

判断loadUrl方法是否在WebviewController与Web组件关联前就被调用。

## 分析结论

在[onDidBuild](../harmonyos-references/ts-custom-component-lifecycle.md#ondidbuild12)中调用了loadUrl方法，此时WebviewController还没有和具体的Web组件关联，无法进行相应的操作。

## 修改建议

当WebviewController成功绑定到Web组件时触发onControllerAttached回调，在此回调中调用loadUrl即可解决问题。

```ts
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct Index {
  private webviewController: webview.WebviewController = new webview.WebviewController();
  // 此处地址实际使用过程中替换为真实地址
  private url = 'xx.xx.xx';

  build() {
    Column() {
      Web({
        src: '',
        // 将WebviewController绑定到Web组件
        controller: this.webviewController
      })
        .geolocationAccess(false)
        .fileAccess(false)
        .width('100%')
        .onControllerAttached(() => {
          // 当WebviewController成功绑定到Web组件时触发该回调，然后调用loadUrl方法加载页面和设置URL的附加HTTP请求头
          this.webviewController.loadUrl(this.url, [{ headerKey: 'headerKey', headerValue: 'headerValue' }]);
        });
    }
    .height('100%')
    .width('100%');
  }
}
```
