---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-178
title: Web组件页面加载失败后如何获取加载异常的信息
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web组件页面加载失败后如何获取加载异常的信息
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:33+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6df26525da8d514bc608edecabc06c8cf3b3646c1862e6a61d672d874f5a7e1a
---

## 问题现象

Web组件加载页面时可能会出现加载异常的情况，此时如何获取加载异常的信息？场景1：网页加载时使用什么方法可以获取到异常信息？场景2：如何获取网络请求和响应的异常信息？场景3：如何监听SSL校验出错？

## 背景知识

* [onErrorReceive](../harmonyos-references/arkts-basic-components-web-events.md#onerrorreceive)：网页加载遇到错误或无网络的情况下触发该回调。主资源与子资源出错都会回调该接口，可以通过isMainFrame来判断是否是主资源报错。出于性能考虑，建议此回调中尽量执行简单逻辑。错误码范围：[@ohos.web.netErrorList (ArkWeb网络协议栈错误列表)](../harmonyos-references/arkts-apis-neterrorlist.md)。
* [onHttpErrorReceive](../harmonyos-references/arkts-basic-components-web-events.md#onhttperrorreceive)：网页加载资源遇到的HTTP错误（响应码>=400）时触发该回调。
* [onSslErrorEventReceive](../harmonyos-references/arkts-basic-components-web-events.md#onsslerroreventreceive9)：通知用户加载资源时发生SSL错误，只支持主资源。
* [onSslErrorEvent](../harmonyos-references/arkts-basic-components-web-events.md#onsslerrorevent12)：通知用户加载资源（主资源+子资源）时发生SSL错误，如果只想处理主资源的SSL错误，请用isMainFrame字段进行区分。
  + 主资源：浏览器加载网页的入口文件，通常是HTML文档。
  + 子资源：主资源中引用的依赖文件，由主资源解析过程中遇到特定标签时触发加载。

## 解决方案

* 场景一：网页加载中可以使用onErrorReceive获取到异常信息，根据ArkWeb的网络协议栈错误列表可知，获取的值为0表示正常，其他值表示加载异常。创建Web组件时建议使用此回调及时获取到加载异常的信息，以便定位问题。

  示例代码如下：

  ```ts
  .onErrorReceive((event) => {
    if (event) {
      // 部分打印，其他打印可参考onErrorReceive接口
      console.info('getErrorInfo:' + event.error.getErrorInfo());
      console.info('getErrorCode:' + event.error.getErrorCode());
      console.info('url:' + event.request.getRequestUrl());
      // 根据isMainFrame判断是主资源还是子资源报错
      console.info('isMainFrame:' + event.request.isMainFrame());
    }
  })
  ```
* 场景二：如果只想获取到网络请求和响应的错误信息可以使用onHttpErrorReceive回调，根据错误码可以通过ArkWeb网络协议栈错误列表确定具体问题。通过onErrorReceive回调也可以获取到。

  示例代码如下：

  ```ts
  .onHttpErrorReceive((event) => {
    if (event) {
      // 部分打印，其他打印可参考onHttpErrorReceive接口
      console.info('url:' + event.request.getRequestUrl());
      // 根据isMainFrame判断是主资源还是子资源报错
      console.info('isMainFrame:' + event.request.isMainFrame());
      console.info('getResponseCode:' + event.response.getResponseCode());
      console.info('getReasonMessage:' + event.response.getReasonMessage());
    }
  })
  ```
* 场景三：如果只加载主资源可以使用onSslErrorEventReceive监听SSL校验错误。如果加载的资源有主资源和子资源需要使用onSslErrorEvent监听SSL校验错误。SSL校验出错时推荐使用[handleCancel](../harmonyos-references/arkts-basic-components-web-sslerrorhandler.md#handlecancel9)通知Web取消此请求，[避免在SSL校验出错时继续加载页面](../best-practices/bpta-harmony-application-security.md#section1256314434316)，以避免中间人攻击风险。

  示例代码如下：

  ```ts
  // 只加载主资源时通过此方法监听SSL校验错误
  .onSslErrorEventReceive((event) => {
    if (event) {
      console.error('ssl check failed,error is : ' + event.error.toString());
      event.handler.handleCancel();
    }
  })
    // 加载的资源有主资源和子资源时使用此方法监听SSL校验错误
    .onSslErrorEvent((event: SslErrorEvent) => {
      if (event) {
        // 根据isMainFrame判断是主资源还是子资源报错
        console.info('onSslErrorEvent isMainFrame: ' + event.isMainFrame);
        event.handler.handleCancel();
      }
    });
  ```

完整参考代码如下：

```ts
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      // src可更换为自己业务地址
      Web({ src: 'www.example.com', controller: this.controller })
        .fileAccess(false)
        .geolocationAccess(false)
        .onErrorReceive((event) => {
          if (event) {
            // 部分打印，其他打印可参考onErrorReceive接口
            console.info('getErrorInfo:' + event.error.getErrorInfo());
            console.info('getErrorCode:' + event.error.getErrorCode());
            console.info('url:' + event.request.getRequestUrl());
            // 根据isMainFrame判断是主资源还是子资源报错
            console.info('isMainFrame:' + event.request.isMainFrame());
          }
        })

        .onHttpErrorReceive((event) => {
          if (event) {
            // 部分打印，其他打印可参考onHttpErrorReceive接口
            console.info('url:' + event.request.getRequestUrl());
            // 根据isMainFrame判断是主资源还是子资源报错
            console.info('isMainFrame:' + event.request.isMainFrame());
            console.info('getResponseCode:' + event.response.getResponseCode());
            console.info('getReasonMessage:' + event.response.getReasonMessage());
          }
        })

          // 只加载主资源时通过此方法监听SSL校验错误
        .onSslErrorEventReceive((event) => {
          if (event) {
            console.error('ssl check failed,error is : ' + event.error.toString());
            event.handler.handleCancel();
          }
        })
          // 加载的资源有主资源和子资源时使用此方法监听SSL校验错误
        .onSslErrorEvent((event: SslErrorEvent) => {
          if (event) {
            // 根据isMainFrame判断是主资源还是子资源报错
            console.info('onSslErrorEvent isMainFrame: ' + event.isMainFrame);
            event.handler.handleCancel();
          }
        });
    };
  }
}
```

## 总结

| 回调方法 | 使用场景说明 |
| --- | --- |
| onErrorReceive | 可以获取到ArkWeb网络协议栈错误列表中的所有错误码，此回调中尽量执行简单逻辑。开发中建议使用此回调，及时获取到错误码，以便定位问题。 |
| onHttpErrorReceive | 只可以获取到ArkWeb网络协议栈错误列表大于等于400的HTTP错误，只想获取到网络加载错误时可以使用此回调。 |
| onSslErrorEventReceive | 只加载主资源时发生SSL错误会被调用，SSL校验出错时推荐使用handleCancel通知Web取消此请求。 |
| onSslErrorEvent | 加载主资源和子资源时发生SSL错误会被调用，可通过isMainFrame判断是否为主资源，SSL校验出错时推荐使用handleCancel通知Web取消此请求。 |
