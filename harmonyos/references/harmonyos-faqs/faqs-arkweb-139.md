---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-139
title: 如何解决网页发生重定向后JS对象丢失的问题
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 如何解决网页发生重定向后JS对象丢失的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:33+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:913940bde2ea9f914992bb623320b08d8cdd124b926c920bd447f03f5dbbb9ea
---

## 问题现象

APP中使用Web组件加载在线网页，网页内部会跳转到新网页，JS交互无法响应，方法不执行。

关键代码如下：

```ts
.onControllerAttached(() => {
  this.controller.registerJavaScriptProxy(this.webTestObj, "objTestName", ["webTest", "webString"]);
  this.controller.refresh();
})
```

## 背景知识

* [前端页面调用应用侧函数](../harmonyos-guides/web-in-page-app-function-invoking.md)：开发者使用Web组件将应用侧代码注册到前端页面中，注册完成之后，前端页面中使用注册的对象名称就可以调用应用侧的方法，实现在前端页面中调用应用侧方法。
* [onLoadIntercept](../harmonyos-references/arkts-basic-components-web-events.md#onloadintercept10)：当Web组件加载url之前触发该回调，用于判断是否阻止此次访问。
* [onControllerAttached](../harmonyos-references/arkts-basic-components-web-events.md#oncontrollerattached10)：当Controller成功绑定到Web组件时触发该回调。
* [registerJavaScriptProxy](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#registerjavascriptproxy)：registerJavaScriptProxy提供了应用与Web组件加载的网页之间强大的交互能力。

## 问题定位

页面初始化的情况下加载网页A，然后发现网页A内部跳转网页B时，JS对象丢失了。尝试页面直接加载目标链接，不会出现JS丢失情况。当监听到url和之前的url域名不一致，尝试重新注册一遍JS，问题可以解决。

## 分析结论

当网页发生整页跳转（非单页应用的路由切换）加载新页面时，原页面上下文会被完全重置。因此，之前注册到H5上的自定义JS对象会丢失。

## 修改建议

需要监听页面url是否发生变化，如果发生变化就重新注入对象。

```ts
import { webview } from '@kit.ArkWeb';

// 模拟注入数据，需要根据业务修改注入的对象
class WebObj {
  constructor() {
  }

  webTest(): string {
    console.info('Web test');
    return 'Web test';
  }

  webString(): void {
    console.info('Web test toString');
  }
}

@Entry
@Component
struct WebRedirect {
  private controller: webview.WebviewController = new webview.WebviewController();
  @State webTestObj: WebObj = new WebObj();
  @State loadUrl: string = '';

  build() {
    Column() {
      // src需替换为相应业务的网址
      Web({ src: 'www.example.com', controller: this.controller })
        .domStorageAccess(true)
        .javaScriptAccess(true)
        .fileAccess(false)
        .geolocationAccess(false)
        .onControllerAttached(() => {
          this.controller.registerJavaScriptProxy(this.webTestObj, "objTestName", ["webTest", "webString"]);
          this.controller.refresh();
        })
        .onLoadIntercept((event) => {
          if (this.loadUrl === null) {
            console.info('loginfo: 首次加载');
            this.loadUrl = event.data.getRequestUrl();
          } else if (this.loadUrl !== event.data.getRequestUrl()) {
            console.info(`loginfo: 两次url不一样——上次加载 url：${this.loadUrl == null ? 'null' :
            this.loadUrl} ---- 本次加载 URL：${event.data.getRequestUrl()}`);
            this.loadUrl = event.data.getRequestUrl();
            // 重新注册JS对象
            this.controller.registerJavaScriptProxy(this.webTestObj, "objTestName", ["webTest", "webString"]);
            this.controller.refresh();
          } else {
            console.info('两次url相同，未发生重定向');
          }
          return false;
        });
    };
  }
}
```

## 常见FAQ

Q：ArkWeb如何判断发生了重定向？

A：在ArkTS WebView中判断请求是否发生重定向，可以通过[onLoadIntercept](../harmonyos-references/arkts-basic-components-web-events.md#onloadintercept10)拦截网络请求，再通过[isRedirect](../harmonyos-references/arkts-basic-components-web-webresourcerequest.md#isredirect)请求是否重定向。

```ts
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebRedirectJudge {
  controller: webview.WebviewController = new webview.WebviewController();
  @State loadUrl: string | null = null; // 记录加载的url
  isRedirect: boolean = false; // 是否发生重定向

  build() {
    Column() {
      // scr需替换为相应业务的网址
      Web({ src: 'www.example.com', controller: this.controller })
        .domStorageAccess(true)
        .javaScriptAccess(true)
        .fileAccess(false)
        .geolocationAccess(false)
        .onLoadIntercept((event) => {
          console.info(`onLoadIntercept, url is ${event.data.getRequestUrl()}`);
          if (this.loadUrl === null) { // 首次加载
            console.info('首次加载');
            this.loadUrl = event.data.getRequestUrl(); // 将此次加载路径保存入变量中，为下次对比做参照
            this.isRedirect = false;
          } else { // 非首次加载
            if (this.loadUrl === event.data.getRequestUrl()) { // 和上一次跳转的url相同
              console.info('两次url相同，未发生重定向');
              this.isRedirect = false;
            } else { // 和上一次跳转的url不同
              if (event.data.isRedirect()) { // 判断服务器重定向
                console.info('服务器重定向');
                this.isRedirect = true;
              } else {
                if (event.data.isRequestGesture()) { // 判断是否发生了交互，未交互就跳转认定为代码重定向，发生了交互认定为正常页面跳转
                  console.info('页面跳转'); // 用户交互发生的页面跳转属于正常页面跳转，不属于重定向
                  this.isRedirect = false;
                } else {
                  console.info('客户端页面代码重定向'); // 若未发生交互，直接进行页面跳转则认定发生了重定向
                  this.isRedirect = true;
                }
              }
              this.loadUrl = event.data.getRequestUrl(); // 将此次加载路径保存入变量中，为下次对比做参照
            }
          }
          return this.isRedirect;
        });
    };
  }
}
```

## 总结

任何页面跳转或重定向都会导致当前页面的JavaScript上下文被完全销毁并重建，所以监听到此类事件时需要重新注入JS对象。
