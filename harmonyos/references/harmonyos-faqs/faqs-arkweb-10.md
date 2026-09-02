---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-10
title: Web组件中如何通过手势滑动返回上一个Web页面
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web组件中如何通过手势滑动返回上一个Web页面
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3c2311ad6a21ea43bf130bb9a3669ca290c582b2604c9f50923d5904e9b5a61a
---

重写onBackPress函数，自定义返回逻辑，通过WebViewController提供的两种接口：accessBackward或accessStep(-1)，都可以实现对web页面是否可以后退情况的判断，进而对web页面进行返回操作。参考代码如下：

```ts
import { webview } from "@kit.ArkWeb";

@Entry
@Component
struct PageOne {
  pageInfos: NavPathStack = new NavPathStack();
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    NavDestination() {
      Column() {
        Web({ src: 'https://www.XXX.com/', controller: this.controller }) // It needs to be manually replaced with the actual website
      }
      .width('100%')
      .height('100%')
    }
    .title('pageOne')
    .onBackPressed(() => {
      if (this.controller.accessBackward()) { // Determine whether the web page can be navigated back
        this.controller.backward() // Navigate back to the previous webpage
        return true
      } else {
        const popDestinationInfo = this.pageInfos.pop(); // Pop the top element of the routing stack 
        return true;
      }
    }).onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
    })
  }
}
```

**参考链接**

[accessBackward](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#accessbackward)

[accessStep](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#accessstep)
