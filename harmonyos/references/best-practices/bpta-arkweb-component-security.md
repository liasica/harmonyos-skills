---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-arkweb-component-security
title: ArkWeb组件安全开发
breadcrumb: 最佳实践 > 应用安全 > ArkWeb组件安全开发
category: best-practices
scraped_at: 2026-09-02T15:03:21+08:00
doc_updated_at: 2026-07-09
content_hash: sha256:139f946cf92a342c841970c9da28521dbe1216c530e75287b09013b7d02fdba0
---

## 概述

### 目标

本文旨在指导应用开发者在Hybrid混合应用开发模式下安全地使用ArkWeb组件。Hybrid混合开发指，开发者通过Web H5技术构建可动态加载与渲染的页面（如商品推广、隐私政策等），并通过应用内置的ArkWeb组件进行展示。同时，开发者可依托[JSBridge](../harmonyos-guides/arkweb-ndk-jsbridge.md)的能力，让Web页面能够方便地使用应用原生功能，例如获取地理位置、调用摄像头甚至移动支付等功能。

该模式在提升开发灵活性与Web交互能力的同时，也使大量敏感能力暴露至Web侧，显著扩大攻击面。此外，诸如跨站脚本攻击、身份混淆、明文数据传输等常见Web漏洞，会进一步削弱混合应用的整体安全性，增加了恶意代码注入、权限滥用、敏感信息泄露等高危风险的发生概率。

因此，本文基于大量真实漏洞案例，为应用开发者提供了若干关于ArkWeb安全开发的最佳实践，涵盖[安全的Web资源访问](bpta-arkweb-component-security.md#section37021234194614)、[恰当的权限管控](bpta-arkweb-component-security.md#section18547133101712)、[确保敏感数据传输安全](bpta-arkweb-component-security.md#section74092496444)三种典型开发场景，以系统性提升应用的整体安全水平。

### 适用范围

本文适用于采用ArkWeb组件进行混合开发的应用，包括加载动态H5页面、JSBridge调用原生能力等场景。

注：纯网页浏览、资源搜索等需要访问全网内容的场景（例如开发浏览器应用）不受本文限制。

## 安全的Web资源访问

遵循以下最佳实践使用ArkWeb进行Web资源访问，能够提升Web运行环境的可信度，保护应用的关键业务和数据。

### 设置允许加载白名单来限制ArkWeb组件加载的网页内容

**【描述】**

开发者应当限制ArkWeb仅能加载受信任的业务网页，而非任意来源的网页。建议使用[setUrlTrustList()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#seturltrustlist12)为ArkWeb配置允许加载白名单。配置成功后，ArkWeb组件能够在网页加载或跳转前自动校验目标URL，仅允许符合白名单的URL被加载或跳转，其他URL将被自动拦截，同时展示告警页。

**【风险说明】**

攻击者会向应用ArkWeb中加载恶意URL，其具体影响因ArkWeb使用环境而异，可能会导致账户劫持、隐私泄露、任意代码执行等严重后果。

**【正例】**

```typescript
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  urlTrustList: string =
    '{\'UrlPermissionList\':[{\'scheme\':\'https\', \'host\':\'trust.example.com\', \'port\':80, \'path\':\'test\'}]}'

  build() {
    Column() {
      Button('Setting the trustList')
        .onClick(() => {
          try {
            // Set up an allowlist to allow access only to trusted web pages.
            this.controller.setUrlTrustList(this.urlTrustList);
          } catch (error) {
            hilog.error(0x0000, 'ArkWebSecurity',
              `ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`);
          }
        })
      Button('Access the trust web')
        .onClick(() => {
          try {
            // Allowlist activated, access to trusted web pages is permitted.
            this.controller.loadUrl('https://trust.example.com/test');
          } catch (error) {
            hilog.error(0x0000, 'ArkWebSecurity',
              `ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`);
          }
        })
      Button('Access the untrusted web')
        .onClick(() => {
          try {
            // Allowlist activated, blocking access to untrusted web and displaying an alarm page.
            this.controller.loadUrl('http://untrust.example.com/test');
          } catch (error) {
            hilog.error(0x0000, 'ArkWebSecurity',
              `ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`);
          }
        })
    }
  }
}
```

### 避免将不可信域名配置到允许加载白名单

**【描述】**

避免将公共CDN域名（如cdn.example.com）等非业务拥有者专属的域名配置到允许加载白名单中。

**【风险说明】**

攻击者可能绕过允许加载白名单，加载恶意URL。

**【反例】**

```screen
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct WebComponent {
  webviewController: webview.WebviewController = new webview.WebviewController();
  urlTrustList: string = '{\'UrlPermissionList\':'
    + '[{\'scheme\':\'https\', \'host\':\'cdnjs.cloudflare.com\'},' // Public CDN domains are untrusted.
    + '{\'scheme\':\'https\', \'host\':\'cdn.ampproject.org\'}]}' // Public service domains are at risk of being abused.
  urlStr: string = '' // Any URL to be loaded.

  build() {
    Column() {
      Web({ src: this.urlStr, controller: this.webviewController })
        .javaScriptAccess(true)
        .onControllerAttached(() => {
          try {
            this.webviewController.setUrlTrustList(this.urlTrustList);
          } catch (error) {
            hilog.error(0x0000, 'ArkWebSecurity',
              `ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`);
          }
        })
    }
  }
}
```

### 加载外部来源的脚本或资源时，务必对不可信内容进行安全校验或过滤

**【描述】**

[WebviewController](../harmonyos-references/arkts-apis-webview-webviewcontroller.md)提供了[loadData()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#loaddata)方法用于加载资源，以及[runJavaScript()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascript)和[runJavaScriptExt()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascriptext10)方法用于执行脚本，并通过回调方式返回脚本执行结果。

若待加载的JavaScript脚本或者资源来自外部可控的不可信来源（例如通过[Want](../harmonyos-references/js-apis-app-ability-want.md#want)传入），务必在加载前对资源内容进行检查和过滤。

**【风险说明】**

如果加载的资源或者脚本不可信，则会导致恶意代码注入，造成跨站脚本攻击（XSS）；此外，若ArkWeb组件注册了敏感JavaScriptProxy接口，还可能导致[JavaScriptProxy](../harmonyos-references/arkts-basic-components-web-i.md#javascriptproxy12)接口被恶意调用，影响Hybrid应用安全性。

**【反例】**

```typescript
Web({ src: $rawfile('index.html'), controller: this.controller })
  .javaScriptAccess(true)
  .onPageEnd(error => {
    try {
      let jsMethod: string = 'alert("xss")' // External controlled string
      this.controller.runJavaScript(jsMethod)
        .then((result) => {
          hilog.info(0x0000, 'ArkWebSecurity', 'result: ' + result);
        })
        .catch((error: BusinessError) => {
          hilog.error(0x0000, 'ArkWebSecurity', 'error: ' + error);
        })
      if (error) {
        hilog.error(0x0000, 'ArkWebSecurity', 'url: ', error.url);
      }
    } catch (error) {
      hilog.error(0x0000, 'ArkWebSecurity', `ErrorCode: ${error.code}, Message: ${error.message}`);
    }
  })
```

index.html内容如下：

```
<html>
<meta charset="UTF-8">
<body>
Hello world!
</body>
<script type="text/javascript">
    function test() {
        console.log('Ark WebComponent')
        return "This value is from index.html"
    }
</script>
</html>
```

**【正例】**

```typescript
Web({ src: $rawfile('index.html'), controller: this.controller })
  .javaScriptAccess(true)
  .onPageEnd(event => {
    try {
      let whiteMethods = ['test()']
      let jsMethod: string = 'alert("xss")' // External controlled string
      if (whiteMethods.indexOf(jsMethod) === -1) {
        hilog.error(0x0000, 'ArkWebSecurity', 'input method not in whiteList')
        return;
      }
      this.controller.runJavaScript(jsMethod)
        .then((result) => {
          hilog.info(0x0000, 'ArkWebSecurity', 'result: ' + result);
        })
        .catch((error: BusinessError) => {
          hilog.error(0x0000, 'ArkWebSecurity', 'error: ' + error);
        })
      if (event) {
        hilog.info(0x0000, 'ArkWebSecurity', 'url: ', event.url);
      }
    } catch (error) {
      let e: BusinessError = error;
      hilog.error(0x0000, 'ArkWebSecurity', `ErrorCode: ${e.code}, Message: ${e.message}`);
    }
  })
```

### 若要在onInterceptRequest中加载本地文件，务必校验文件URL，以防止本地数据被窃取

**【描述】**

通过[onInterceptRequest()](../harmonyos-references/arkts-basic-components-web-i.md#oninterceptrequestevent12)拦截URL资源访问，可以定制返回状态、内容等Response报文。若应用需要通过[getRequestUrl()](../harmonyos-references/arkts-basic-components-web-webresourcerequest.md#getrequesturl)打开本地文件，务必对URL进行路径检查，并判断是否存在路径遍历符号“../”，防止目录穿越。

**【风险说明】**

目录穿越是指攻击者能够利用路径遍历符访问到本不应该读取的目录下的文件，一旦被利用，则可能导致应用内敏感文件遭到窃取，甚至造成远程代码执行等严重安全后果。

**【正例】**

```typescript
import { webview } from '@kit.ArkWeb';
import { fileIo } from '@kit.CoreFileKit';
import { util } from '@kit.ArkTS';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  responseWeb: WebResourceResponse = new WebResourceResponse();
  heads: Header[] = [];

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
      // Intercept URL resource access through onInterceptRequest and customize the response message.
        .onInterceptRequest((event) => {
          // The URL passed by event.request.getRequestUrl() should be restricted to a specific path,
          // and the presence of '../' should be checked.
          if (event.request.getRequestUrl().startsWith('file:///data/trusted_path') &&
            event.request.getRequestUrl().includes('../') !== true) {
            try {
              let file =
                fileIo.openSync(event.request.getRequestUrl(), fileIo.OpenMode.READ_ONLY | fileIo.OpenMode.CREATE);
              let arrayBuffer: ArrayBuffer = new ArrayBuffer(6);
              fileIo.readSync(file.fd, arrayBuffer, { offset: 0, length: arrayBuffer.byteLength });
              fileIo.closeSync(file);
              let decoder = util.TextDecoder.create('utf-8');
              let stringData = decoder.decodeToString(new Uint8Array(arrayBuffer));
              let head1: Header = {
                headerKey: 'Connection',
                headerValue: 'keep-alive'
              }
              let head2: Header = {
                headerKey: 'Cache-Control',
                headerValue: 'no-cache'
              }
              this.heads.push(head1);
              this.heads.push(head2);

              const promise: Promise<String> = new Promise((resolve: Function) => {
                this.responseWeb.setResponseHeader(this.heads);
                // After the file is read, it will be encapsulated and the response will be called back to the web page.
                this.responseWeb.setResponseData(stringData);
                this.responseWeb.setResponseEncoding('utf-8');
                this.responseWeb.setResponseMimeType('text/html');
                this.responseWeb.setResponseCode(200);
                this.responseWeb.setReasonMessage('OK');
                resolve('success');
              })
              promise.then(() => {
                hilog.info(0x0000, 'ArkWebSecurity', 'prepare response ready');
                this.responseWeb.setResponseIsReady(true);
              })
              this.responseWeb.setResponseIsReady(false);
            } catch (error) {
              hilog.error(0x0000, 'ArkWebSecurity', `ErrorCode: ${error.code}, Message: ${error.message}`);
            }
          }
          return this.responseWeb;
        })
    }
  }
}
```

### 避免在允许跨域访问的本地文件目录中包含敏感资源

**【描述】**

ArkWeb默认不允许跨域访问本地文件资源，除非使用[setPathAllowingUniversalAccess()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#setpathallowinguniversalaccess12)设置了允许跨域访问的本地文件目录。在此情况下，务必最小化允许访问的文件目录范围，且目录中不得存放敏感资源，如用户数据、cookie、各类token等。

注：鸿蒙系统仅开放针对应用文件目录（Context.filesDir）、应用资源目录（Context.resourceDir）设置允许跨域访问。若设置路径列表不符合要求，则会导致设置失败。

**【风险说明】**

若设置了允许跨域访问本地文件目录，可能会让攻击者访问本地文件，导致敏感资源泄露，并发起“应用克隆攻击”。

### 避免HTTP与HTTPS混合内容加载

**【描述】**

[mixedMode()](../harmonyos-references/arkts-basic-components-web-attributes.md#mixedmode)设置是否允许加载超文本传输协议（HTTP）和超文本传输安全协议（HTTPS）的混合内容，ArkWeb默认不允许加载HTTP和HTTPS的混合内容（mixedMode默认设为None），应当避免设置为All。开发者若在调试场景下需要访问HTTP，则务必在调试完成后将mixedMode设置为None。

**【风险说明】**

若允许ArkWeb组件同时加HTTP和HTTPS的混合内容，则会引入中间人攻击风险。

**【反例】**

```typescript
Web({ src: 'www.huawei.com', controller: this.controller })
  .mixedMode(MixedMode.All)
```

**【正例】**

```typescript
Web({ src: 'www.huawei.com', controller: this.controller })
  .mixedMode(MixedMode.None)
```

### 避免在SSL校验出错时继续加载页面

**【描述】**

当用户加载的网页资源发生SSL校验错误（如目标网站的证书或协议校验出现错误），ArkWeb组件会通过[onSslErrorEvent()](../harmonyos-references/arkts-basic-components-web-events.md#onsslerrorevent12)通知应用。默认情况下，ArkWeb组件会取消加载发生该错误的资源，若业务场景要求继续执行，开发者务必在调用confirm之前做显式校验或者说明。建议使用onSslErrorEvent捕获全量资源错误，不建议使用[onSslErrorEventReceive()](../harmonyos-references/arkts-basic-components-web-events.md#onsslerroreventreceive9)。

**【风险说明】**

如果在SSL校验出错时忽略SSL错误并继续加载，容易导致中间人攻击等风险。

**例外情况：**用于加载全网URL的应用（例如浏览器）可以例外，但需要在页面显式告知用户待加载页面存在安全风险。

**【反例】**

```typescript
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onSslErrorEvent((event: SslErrorEvent) => {
          console.log('ssl check failed, error is: ' + event.error.toString());
          event.handler.handleConfirm();
        })
    }
  }
}
```

**【正例】**

```typescript
import { webview } from '@kit.ArkWeb';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onSslErrorEvent((event: SslErrorEvent) => {
          hilog.info(0x0000, 'ArkWebSecurity', 'onSslErrorEvent url: ' + event.url);
          hilog.info(0x0000, 'ArkWebSecurity', 'onSslErrorEvent error: ' + event.error);
          hilog.info(0x0000, 'ArkWebSecurity', 'onSslErrorEvent originalUrl: ' + event.originalUrl);
          hilog.info(0x0000, 'ArkWebSecurity', 'onSslErrorEvent referrer: ' + event.referrer);
          hilog.info(0x0000, 'ArkWebSecurity', 'onSslErrorEvent isFatalError: ' + event.isFatalError);
          hilog.info(0x0000, 'ArkWebSecurity', 'onSslErrorEvent isMainFrame: ' + event.isMainFrame);
          this.getUIContext().showAlertDialog({
            title: 'onSslErrorEvent',
            message: 'text',
            primaryButton: {
              value: 'Confirm',
              action: () => {
                event.handler.handleConfirm();
              }
            },
            secondaryButton: {
              value: 'cancel',
              action: () => {
                event.handler.handleCancel();
              }
            },
            cancel: () => {
              event.handler.handleCancel();
            }
          })
        })
    }
  }
}
```

### 正式Release版本务必关闭ArkWeb的网页调试功能

**【描述】**

[setWebDebuggingAccess()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#setwebdebuggingaccess)可以用于开启ArkWeb网页调试功能，默认配置下，调试功能处于关闭状态。在正式Release版本上务必保持关闭该功能。

**【风险说明】**

若开发者主动开启调试功能，将增加业务对外接口被恶意利用的风险。

**【反例】**

```typescript
try {
  webview.WebviewController.setWebDebuggingAccess(true);
} catch (error) {
  hilog.error(0x0000, 'ArkWebSecurity', `ErrorCode: ${error.code}`);
}
```

## 恰当的权限管控

遵循以下最佳实践，确保ArkWeb运行时满足最小特权原则，仅授予受信任的Web页面所需权限。

### 注册JavaScriptProxy接口时，务必同时设置允许调用白名单检查调用接口的页面身份

**【描述】**

[JavaScriptProxy](../harmonyos-references/arkts-basic-components-web-i.md#javascriptproxy12)接口，尤其是访问敏感资源的接口，务必在调用前通过白名单来检查调用页面的合法性，以满足最小特权原则。建议开发者在注册JavaScriptProxy时，通过设置permission参数配置允许调用接口白名单。完成配置后，当Web侧调用该JavaScriptProxy接口时，ArkWeb会对调用页面的URL进行检查，仅符合白名单要求的URL的请求才会被允许，其余请求将被拦截。

**说明** 

避免利用[onPageBegin()](../harmonyos-references/arkts-basic-components-web-events.md#onpagebegin)等生命周期函数自行实现接口白名单校验，务必统一通过permission参数进行控制。

**【风险说明】**

通过JavaScriptProxy接口注册的方法能被攻击者利用，导致加载恶意内容、执行恶意代码、滥用敏感资源等风险。

参考文档：[如何建立应用侧与H5侧的交互通道](../harmonyos-guides/web-in-page-app-function-invoking.md#如何建立应用侧与h5侧的交互通道)

### 注册JavaScriptProxy接口时遵循最小必要原则

**【描述】**

仅向Web页面注册业务必须的[JavaScriptProxy](../harmonyos-references/arkts-basic-components-web-i.md#javascriptproxy12)接口，建议避免将调试接口、内部逻辑接口等直接暴露给Web页面。同时，开发者应通过设置访问控制（例如允许调用白名单）检查调用者的合法性。

**【风险说明】**

若暴露的接口涉及返回敏感信息或执行敏感操作，一旦被攻击者调用，将导致账户仿冒攻击、执行恶意代码等风险。

**【反例】**

```typescript
import { webview } from '@kit.ArkWeb';
import { hilog } from '@kit.PerformanceAnalysisKit';

class InsecureObj {
  executeSQL(cmd: string) {
    // Do something dangerous here
    hilog.info(0x0000, 'ArkWebSecurity', 'Execute: ' + cmd);
  }
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  testObj = new InsecureObj();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .javaScriptAccess(true)
        .javaScriptProxy({
          object: this.testObj,
          name: 'objName',
          methodList: ['executeSQL'],
          controller: this.controller,
        })
    }
  }
}
```

### 避免在onOverrideUrlLoading中进行页面加载

**【描述】**

当URL将要加载到Web组件中时，Hybrid应用可以通过[onOverrideUrlLoading()](../harmonyos-references/arkts-basic-components-web-events.md#onoverrideurlloading12)接收通知，接管加载流程的控制权。onOverrideUrlLoading()是不可信的生命周期，不建议在此方法中执行任何业务逻辑。开发者应避免在onOverrideUrlLoading()函数实现中调用[loadUrl()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#loadurl)进行页面加载。

**【风险说明】**

此操作不仅可能导致当前加载流程意外终止，还会打破ArkWeb的安全限制，增加额外的安全风险（onOverrideUrlLoading()由页面发起，loadUrl()由Hybrid应用发起，ArkWeb内核对两种流程的安全校验有差别，因此不可以混用）。

**【反例】**

```typescript
import { webview } from '@kit.ArkWeb';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .onOverrideUrlLoading((webResourceRequest: WebResourceRequest) => {
          if (webResourceRequest && webResourceRequest.getRequestUrl() === 'http://www.example.com') {
            try {
              this.controller.loadUrl('www.example.com');
              return true;
            } catch (error) {
              hilog.error(0x0000, 'ArkWebSecurity', `ErrorCode: ${error.code}, Message: ${error.message}`);
            }
          }
          return false;
        })
    }
  }
}
```

### 避免使用getUrl/getOriginalUrl函数获取URL进行调用白名单校验

**【描述】**

在[JavaScriptProxy](../harmonyos-references/arkts-basic-components-web-i.md#javascriptproxy12)调用过程中，[getUrl()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#geturl)或[getOriginalUrl()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#getoriginalurl)可能获取到不准确的页面的URL，若将其用于校验，则可能出现错误判断，引入安全风险。建议通过[getLastJavascriptProxyCallingFrameUrl()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#getlastjavascriptproxycallingframeurl12)函数来获取准确的发起调用的页面URL。

注：getLastJavascriptProxyCallingFrameUrl仅能在JavaScriptProxy中使用，请勿在其他场景中使用该函数获取URL，否则可能获取到错误值。

**【风险说明】**

对不准确的页面URL进行安全校验，将导致安全校验失效，可能让攻击者发起越权攻击等。

**【反例】**

```typescript
let url: string = this.controller.getUrl();
if (url === 'https://www.huawei.com') {
  hilog.info(0x0000, 'ArkWebSecurity', 'Pass the check');
  // do some native invoke
} else {
  hilog.error(0x0000, 'ArkWebSecurity', 'Not allowed to execute: ' + cmd);
}
```

**【正例】**

```typescript
let url: string = this.controller.getLastJavascriptProxyCallingFrameUrl();
if (url === 'https://www.huawei.com') {
  hilog.info(0x0000, 'ArkWebSecurity', 'Pass the check');
  // do some native invoke
} else {
  hilog.error(0x0000, 'ArkWebSecurity', 'Not allowed to execute: ' + cmd);
}
```

### 避免在JavaScriptProxy中提供页面加载功能

**【描述】**

开发者应避免在[JavaScriptProxy](../harmonyos-references/arkts-basic-components-web-i.md#javascriptproxy12)中调用[loadUrl()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#loadurl)进行页面加载。如果业务有加载页面的需求，应当通过HTML跳转实现。

**【风险说明】**

不当操作不仅会导致当前页面生命周期意外终止，还会打破ArkWeb的安全限制，增加额外风险。

**【反例】**

```typescript
import { webview } from '@kit.ArkWeb';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestObj {
  controller: webview.WebviewController

  constructor(webview_controller: webview.WebviewController) {
    this.controller = webview_controller
  }

  goto(uri: string) {
    try {
      this.controller.loadUrl(uri);
    } catch (error) {
      hilog.error(0x0000, 'ArkWebSecurity', `ErrorCode: ${error.code}, Message: ${error.message}`);
    }
  }
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  testObj = new TestObj(this.controller);

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .javaScriptAccess(true)
        .javaScriptProxy({
          object: this.testObj,
          name: 'objName',
          methodList: ['goto'],
          controller: this.controller,
        })
    }
  }
}
```

### 避免在JavaScriptProxy中提供脚本执行功能

**【描述】**

开发者应避免在[JavaScriptProxy](../harmonyos-references/arkts-basic-components-web-i.md#javascriptproxy12)中提供[runJavaScript()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascript)和[runJavaScriptExt()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascriptext10)等代码执行功能。

**【风险说明】**

由于JavaScriptProxy注册在Web组件上，因此通过JavaScriptProxy执行的JS脚本可以影响在Web组件上运行的所有页面。受攻击者控制的子页面能借助此能力在父页面上执行代码，造成跨域风险。

**【反例】**

```typescript
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class TestObj {
  controller: webview.WebviewController

  constructor(webview_controller: webview.WebviewController) {
    this.controller = webview_controller
  }

  eval(uri: string) {
    this.controller.runJavaScript(uri, (error) => {
      if (error) {
        hilog.error(0x0000, 'ArkWebSecurity',
          `run JavaScript error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        return;
      }
    });
    return 'AceString';
  }
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  testObj: TestObj = new TestObj(this.controller);

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .javaScriptAccess(true)
        .javaScriptProxy({
          object: this.testObj,
          name: 'objName',
          methodList: ['eval'],
          controller: this.controller,
        })
    }
  }
}
```

### 务必在onPermissionRequest函数中显式通知用户进行授权

**【描述】**

Web页面能够通过getUserMedia()标准接口访问设备摄像头/麦克风。ArkWeb组件会触发[onPermissionRequest()](../harmonyos-references/arkts-basic-components-web-events.md#onpermissionrequest9)函数来管理当前Web页面的授权，应当创建显式弹窗进行用户授权，如使用[AlertDialog](../harmonyos-references/ohos-arkui-advanced-dialog.md#alertdialog)，避免直接授予页面权限。默认情况下，ArkWeb组件拒绝权限授予。

**【风险说明】**

若未经用户授权进行访问，则可能导致隐私泄露和违规风险。

**【反例】**

```typescript
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { abilityAccessCtrl, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  aboutToAppear(): void {
    let atManager = abilityAccessCtrl.createAtManager();
    let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    atManager.requestPermissionsFromUser(context, ['ohos.permission.CAMERA', 'ohos.permission.MICROPHONE'])
      .then((data) => {
        hilog.info(0x0000, 'ArkWebSecurity', 'data: ' + JSON.stringify(data));
        hilog.info(0x0000, 'ArkWebSecurity', 'data permission: ' + data.permissions);
        hilog.info(0x0000, 'ArkWebSecurity', 'data authResults: ' + data.authResults);
      }).catch((error: BusinessError) => {
      hilog.error(0x0000, 'ArkWebSecurity',
        `Failed to request permissions from user. Code is ${error.code}, message is ${error.message}`);
    })
  }

  build() {
    Column() {
      Web({ src: 'https://example.com/index.html', controller: this.controller })
        .onPermissionRequest((event) => {
          // Directly granting page permissions is a wrong approach.
          event.request.grant(event.request.getAccessibleResource());
        })
    }
  }
}
```

index.html内容如下：

```
<html>
<head>
    <meta charset="UTF-8">
</head>
<body>
<video id="video" width="500px" height="500px" autoplay="autoplay"></video>
<canvas id="canvas" width="500px" height="500px"></canvas>
<br>
<input type="button" title="HTML5 Camera" value="Open Camera" onclick="getMedia()">
<script>
    function getMedia() {
        let constraints = {
            video: {width: 500, height: 500},
            audio: true
        };
        // Get video
        let video = document.getElementById("video");
        // Return Promise object
        let promise = navigator.mediaDevices.getUserMedia(constraints);
        // then() sync，invoke MediaStream as param
        promise.then(function (MediaStream) {
            video.srcObject = MediaStream;
            video.play();
        });
    }
</script>
</body>
</html>
```

**【正例】**

```typescript
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { abilityAccessCtrl, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  aboutToAppear(): void {
    let atManager = abilityAccessCtrl.createAtManager();
    let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    atManager.requestPermissionsFromUser(context, ['ohos.permission.CAMERA', 'ohos.permission.MICROPHONE'])
      .then((data) => {
        hilog.info(0x0000, 'ArkWebSecurity', 'data: ' + JSON.stringify(data));
        hilog.info(0x0000, 'ArkWebSecurity', 'data permission: ' + data.permissions);
        hilog.info(0x0000, 'ArkWebSecurity', 'data authResults: ' + data.authResults);
      }).catch((error: BusinessError) => {
        hilog.error(0x0000, 'ArkWebSecurity',
        `Failed to request permissions from user. Code is ${error.code}, message is ${error.message}`);
    })
  }

  build() {
    Column() {
      Web({ src: 'https://example.com/index.html', controller: this.controller })
        .onPermissionRequest((event) => {
          if (event) {
            this.getUIContext().showAlertDialog({
              title: 'title',
              message: 'text',
              primaryButton: {
                value: 'deny',
                action: () => {
                  event.request.deny();
                }
              },
              secondaryButton: {
                value: 'onConfirm',
                action: () => {
                  // Explicit pop-ups that ask user for authorization, e.g., using AlertDialog, is the correct approach.
                  event.request.grant(event.request.getAccessibleResource());
                }
              },
              cancel: () => {
                event.request.deny();
              }
            })
          }
        })
    }
  }
}
```

### 务必在onGeolocationShow函数中显式通知用户进行授权

**【描述】**

在Web页面访问设备地理位置时，务必在[onGeolocationShow()](../harmonyos-references/arkts-basic-components-web-events.md#ongeolocationshow)回调函数内发起显式弹窗，明确告知用户进行授权。由于[geolocationAccess](../harmonyos-references/arkts-basic-components-web-attributes.md#geolocationaccess)属性默认为true，ArkWeb会默认允许网页发起访问地理位置的请求，因此开发者务必在获得用户确认和同意后才能向网页返回位置信息；否则应当将geolocationAccess设置为false，禁止网页获取定位数据。

**【风险说明】**

若未经用户授权进行访问，可能导致隐私泄露和违规风险。

**【反例】**

```typescript
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .geolocationAccess(true)
        .onGeolocationShow((event) => {
          event.geolocation.invoke(event.origin, true, true);
        })
    }
  }
}
```

**【正例】**

```typescript
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .geolocationAccess(true)
        .onGeolocationShow((event) => {
          if (event) {
            this.getUIContext().showAlertDialog({
              title: 'title',
              message: 'text',
              confirm: {
                value: 'onConfirm',
                action: () => {
                  event.geolocation.invoke(event.origin, true, true);
                }
              },
              cancel: () => {
                event.geolocation.invoke(event.origin, false, true);
              }
            })
          }
        })
    }
  }
}
```

### 避免未经检查拼接和执行Web侧传递的JavaScript内容

**【描述】**

应用侧（ArkTS）可能会通过开放接口、生命周期拦截等方式接收Web页面（HTML+JS）传递的数据，再通过调用[runJavaScript()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascript)和[runJavaScriptExt()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#runjavascriptext10)异步执行JS，回传执行结果。开发者务必对传递的数据进行安全过滤，再执行异步回调。

**【风险说明】**

从Web页面传递至应用侧（ArkTS）的内容不可信，若被攻击者控制，可能导致通用型跨站脚本攻击（UXSS）。

**【反例】**

```typescript
this.controller.runJavaScript(
  // Trusting data_from_H5 passed through web pages will result in the execution of arbitrary JS code,
  // e.g., enclose the alert and execute other JS code through data_from_H5.
  'javascript:alert(' + this.dataFromH5 + ')',
  (error, result) => {
    if (error) {
      hilog.error(0x0000, 'ArkWebSecurity',
        `run JavaScript error, ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`);
      return;
    }
    if (result) {
      this.webResult = result;
      hilog.info(0x0000, 'ArkWebSecurity', `The test() return value is: ${result}`);
    }
  });
```

**【正例】**

```typescript
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  dataFromH5: string = '' // Messages passed from web pages
  @State webResult: string = '';

  build() {
    Column() {
      Text(this.webResult).fontSize(20)
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .javaScriptAccess(true)
        .onPageEnd(event => {
          try {
            // Use regular expressions to match all single and double quotes.
            const regex = /['"\(\)]/g;
            // Use the replace method to replace all matched characters with an empty string.
            let sanitizedStr = this.dataFromH5.replace(regex, '');
            this.controller.runJavaScript(
              // Perform security filtering on the data_from_H5 passed through the web page before calling back.
              'javascript:alert(' + sanitizedStr + ')',
              (error, result) => {
                if (error) {
                  hilog.error(0x0000, 'ArkWebSecurity',
                    `run JavaScript error, ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`);
                  return;
                }
                if (result) {
                  this.webResult = result;
                  hilog.info(0x0000, 'ArkWebSecurity', `The test() return value is: ${result}`);
                }
              });
            if (event) {
              hilog.info(0x0000, 'ArkWebSecurity', 'url: ', event.url);
            }
          } catch (error) {
            hilog.error(0x0000, 'ArkWebSecurity',
              `ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`);
          }
        })
    }
  }
}
```

index.html内容如下：

```
<html>
<meta charset="UTF-8">
<body>
Hello world!
</body>
<script type="text/javascript">
    function test() {
        console.log('Ark WebComponent')
        return "This value is from index.html"
    }
</script>
</html>
```

## 确保敏感数据的传输安全

遵循以下最佳实践，确保应用与Web网页安全地进行数据传递，提升应用安全性，同时为用户提供隐私安全保障。

### 避免直接向Web页面追加认证Cookie

**【描述】**

出于业务需要进行用户状态同步时，其中一种方式是使用[WebCookieManager](../harmonyos-references/arkts-apis-webview-webcookiemanager.md)为指定URL的页面传递Cookie。

务必在校验待追加Cookie的URL符合业务预期后，再使用[configCookieSync()](../harmonyos-references/arkts-apis-webview-webcookiemanager.md#configcookiesync11)向其追加认证Cookie。建议使用[setUrlTrustList()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#seturltrustlist12)配置加载白名单后，再对待追加Cookie的URL进行一次合法性判断。

**【风险说明】**

向未经校验的URL直接追加认证Cookie是非常危险的行为，可能导致认证Cookie被窃取。

**【反例】**

```screen
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  unknownUrl: string = ''; // unknownUrl from external source

  build() {
    Column() {
      Button('configCookieSync')
        .onClick(() => {
          try {
            // unknownUrl is not verified.
            webview.WebCookieManager.configCookieSync(this.unknownUrl, 'a=b');
          } catch (error) {
            hilog.error(0x0000, 'ArkWebSecurity',
              `ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: this.unknownUrl, controller: this.controller })
    }
  }
}
```

**【正例】**

```screen
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  unknownUrl: string = ''; // unknownUrl from external source
  urlTrustList: string =
    '{\'UrlPermissionList\':[{\'scheme\':\'http\', \'host\':\'trust.example.com\', \'port\':80, \'path\':\'test\'}]}'

  build() {
    Column() {
      Button('configCookieSync')
        .onClick(() => {
          try {
            // Set up an allowlist to allow access only to trusted web pages.
            this.controller.setUrlTrustList(this.urlTrustList);
          } catch (error) {
            hilog.error(0x0000, 'ArkWebSecurity',
              `ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`);
          }
          try {
            // Perform another validity check on unknown_url to implement more granular control.
            if (this.unknownUrl === 'https://www.example.com') {
              webview.WebCookieManager.configCookieSync(this.unknownUrl, 'a=b');
            }
          } catch (error) {
            hilog.error(0x0000, 'ArkWebSecurity',
              `ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: this.unknownUrl, controller: this.controller })
    }
  }
}
```

### 避免将用户敏感信息直接拼接到URL中进行加载

**【描述】**

避免将用户敏感信息，如OAuth Token、Session ID、手机号等，直接拼接到URL中并访问加载，例如调用[loadUrl()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#loadurl)。

**【风险说明】**

当URL为外部可控时，将导致敏感信息泄露。

**【反例】**

```typescript
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  @State message: string = 'Hello World';
  webviewController: webview.WebviewController = new webview.WebviewController();
  accessToken: string = 'xxxx'; // After the user completes the login operation, the token returned by the server.
  untrustedURL: string = '' // Any URL to be loaded

  build() {
    Column() {
      Web({ src: this.untrustedURL + '?token=' + this.accessToken, controller: this.webviewController })
    }
  }
}
```

### 应用通过postMessage接口向网页传送敏感数据时，务必指定接收该消息的URI

**【描述】**

在使用[WebMessagePort](../harmonyos-references/arkts-apis-webview-webmessageport.md)和网页建立连接时，需要保证通信对端网页可信。

**【风险说明】**

缺少访问控制可能会意外的将应用侧ArkTS代码暴露给网页的JavaScript，导致敏感资源泄露。

**【反例】**

```typescript
this.ports = this.controller.createWebMessagePorts();
this.controller.postMessage('__init_port__', [this.ports[0]], '*');
this.ports[1].postMessageEvent('Post message event to html');
```

**【正例】**

```typescript
this.ports = this.controller.createWebMessagePorts();
this.controller.postMessage('__init_port__', [this.ports[0]], this.url_in_whitelist);
```
