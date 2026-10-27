---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkweb-kit-troubleshooting-0009
title: loadUrl添加headers参数失败问题定位
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 故障排查 > loadUrl添加headers参数失败问题定位
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:04+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:794f06837481664405cff181ef2feb536bc4aad8ed07b4400920af6e279eadf7
---

## 问题现象

通过loadUrl加载页面后，在设置header时遇到以下问题：

使用this.webviewController.loadUrl(toUrl, toHeader)方法重新加载页面，方法里面带上了header的参数会出现如下报错：

```txt
Error message:Init error. The WebviewController must be associated with a Web component
```

## 定位过程

判断loadUrl方法是否在WebviewController与Web组件关联前就被调用；

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
