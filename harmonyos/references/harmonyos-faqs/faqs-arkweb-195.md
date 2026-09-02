---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-195
title: Web组件的请求拦截接口使用场景总结
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web组件的请求拦截接口使用场景总结
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:b844d36f71bd5bd0e1b406ff92ca85cd317741bf19cb36f98bfe370807af37a5
---

## 问题现象

Web组件中onLoadIntercept、onInterceptRequest、WebSchemeHandler、onOverrideUrlLoading都是用于请求的拦截，这几个接口的作用分别是什么，适用于哪些场景？

## 背景知识

* [onLoadIntercept](../harmonyos-references/arkts-basic-components-web-events.md#onloadintercept10)：当Web组件加载url之前触发该回调，用于判断是否阻止此次访问。
* [onInterceptRequest](../harmonyos-references/arkts-basic-components-web-events.md#oninterceptrequest9)：当Web组件加载url之前触发该回调，用于拦截url并返回响应数据。
* [WebSchemeHandler](../harmonyos-references/arkts-apis-webview-webschemehandler.md)：用于拦截指定Scheme的请求的拦截器。
* [onOverrideUrlLoading](../harmonyos-references/arkts-basic-components-web-events.md#onoverrideurlloading12)：当url将要加载到当前Web中时触发该回调，让宿主应用程序有机会获得控制权，判断是否阻止Web加载url。

## 解决方案

**接口使用场景汇总说明：**

| 场景 | [onLoadIntercept](../harmonyos-references/arkts-basic-components-web-events.md#onloadintercept10) | [onInterceptRequest](../harmonyos-references/arkts-basic-components-web-events.md#oninterceptrequest9) | [WebSchemeHandler](../harmonyos-references/arkts-apis-webview-webschemehandler.md) | [onOverrideUrlLoading](../harmonyos-references/arkts-basic-components-web-events.md#onoverrideurlloading12) |
| --- | --- | --- | --- | --- |
| 拦截时机 | Web组件加载url之前触发（在请求发起前） | Web组件加载url之前触发（仅在onLoadIntercept返回false后执行） | 当请求匹配注册的Scheme时触发 | url将要加载到当前Web组件时触发（针对用户交互行为） |
| 拦截范围 | 页面主url请求（包括页面及iframe导航行为），不包括子资源（如js/css/图片） | 页面主url请求和所有子资源请求（包括HTTP/HTTPS请求） | 仅限于注册了特定Scheme的请求，不匹配Scheme的请求由Web组件默认处理 | 1. 页面内导航请求（用户触发的跳转，如点击链接或按钮） 2. iframe加载HTTP(s)协议或about:blank时不会触发该回调，而加载非HTTP(s)协议的跳转会触发 3. 调用loadUrl(url: string)主动触发的跳转不会触发该回调 4. POST请求不会触发该回调 |
| 适用场景 | 1. 请求重定向（例如域名更换或登录引导） 2. 页面白名单/黑名单配置（阻止访问危险网页） 3. 应用的跳转与拉起（如拦截支付链接跳转到支付应用） | 1. 本地资源替换（缓存静态资源提升加载速度） 2. 处理本地资源跨域 3. 提示或拦截恶意请求 | 1. 配置公共请求头 2. 处理远程请求跨域 3. POST请求拦截 | 1. 拦截网页内导航（如点击跳转链接时阻止或重定向） 2. 处理用户交互触发的跳转行为 |
| 性能影响 | 低（仅页面加载时触发一次，对性能影响小） | 中到高（所有请求均触发回调，逻辑复杂时可能影响性能） | 低到中（仅处理注册Scheme请求，性能开销小） | 低到中（仅在用户交互时触发，性能影响一般） |
| 关键特性 | 1. 支持获取请求url、是否为主frame等信息 2. 只能拦截或放行请求，无法返回自定义响应 | 1. 支持替换请求内容（通过文件句柄、Resource资源或ByteBuffer） 2. 轻量级实现，适合简单拦截需求 | 1. 支持获取POST请求体和buffer类型数据 2. 结构化设计，职责分离明确 3. 需提前注册Scheme | 1. 对iframe行为有特殊处理：iframe加载HTTP(s)协议或about:blank时不会触发该回调，而加载非HTTP(s)协议的跳转会触发 2. 返回true表示中止加载，false表示允许加载 |

**接口常用使用场景：**

* onLoadIntercept常用于拦截请求重定向、拉起应用等场景，如拦截请求，跳转ArkTS页面；拦截支付链接拉起支付应用。实现方式可参考：
  + 拦截请求跳转ArkTS页面，参考文档：[ArkWeb页面与ArkTS页面互相跳转](../harmonyos-guides/navigating-between-web-and-apps.md#arkweb页面与arkts页面互相跳转)。
  + 拦截请求跳转应用，参考文档：[ArkWeb页面指定应用跳转](../harmonyos-guides/navigating-between-web-and-apps.md#arkweb页面指定应用跳转)。
* onInterceptRequest可拦截所有跳转请求并返回响应数据，但无法访问POST请求体（Body）内容，且不支持分片缓冲（buffer）类型数据获取。此类场景需改用[WebSchemeHandler](../harmonyos-references/arkts-apis-webview-webschemehandler.md)实现。onInterceptRequest常用于拦截请求进行本地资源替换，提升加载速度；解决本地资源跨域等问题。实现方式可参考：
  + 拦截请求进行本地资源替换，提升加载速度，参考文档：[资源拦截替换的JavaScript生成字节码缓存](../best-practices/bpta-web-develop-optimization.md#section1495115588211)。
  + 解决本地资源跨域问题，参考文档：[本地资源跨域问题解决方法#方法一](../harmonyos-guides/web-cross-origin.md#本地资源跨域问题解决方法)。
* WebSchemeHandler用于拦截指定Scheme的请求，常用于处理代理请求、解决请求跨域问题，实现方式可参考文档：[远程请求跨域](../best-practices/bpta-cross-domain-solutions-for-web-pages.md#section1281615241211)。
* onOverrideUrlLoading常用于页面内导航请求的拦截，判断是否阻止url加载。实现方式可参考接口文档中示例代码：[onOverrideUrlLoading#示例](../harmonyos-references/arkts-basic-components-web-events.md#onoverrideurlloading12)。

## 常见FAQ

Q：使用onLoadIntercept如何实现重定向？

A：请参考文档：[请求重定向](../harmonyos-guides/web-component-intercept-capab-usage.md#请求重定向)。

Q：如何实现页面白名单，只允许加载白名单内的网页？

A：可通过[onLoadIntercept](../harmonyos-references/arkts-basic-components-web-events.md#onloadintercept10)拦截所有页面请求，判断是否在白名单清单内，在白名单内则放行，不在白名单内需用户同意才可访问，具体实现请参考文档：[页面白名单配置](../harmonyos-guides/web-component-intercept-capab-usage.md#页面白名单配置)。

Q：[onInterceptRequest](../harmonyos-references/arkts-basic-components-web-events.md#oninterceptrequest9)处理本地资源跨域与[WebSchemeHandler](../harmonyos-references/arkts-apis-webview-webschemehandler.md)处理远程请求跨域有什么区别？

A：跨域指浏览器从一个域名的网页去请求另一个域名的资源时，域名、端口、协议任一不同时为跨域。

* 本地资源跨域：将前端静态资源存放于应用安装包rawfile、resfile、沙箱目录下时，访问前端静态资源路径为file://，服务端请求一般为http/https，由于请求协议不一致，此场景为本地资源跨域。
* 远程请求跨域：指前端静态资源可以在远端，也可以在本地，由于访问协议、域名、端口不同造成跨域，为远程请求跨域。即远程请求跨域包含本地资源跨域。

Q：使用[WebSchemeHandler](../harmonyos-references/arkts-apis-webview-webschemehandler.md)拦截POST请求时，如何获取POST请求体？

A：可参考如下代码：

```ts
import { WebNetErrorList, webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { buffer, util } from '@kit.ArkTS';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  schemeHandler: webview.WebSchemeHandler = new webview.WebSchemeHandler();
  htmlData: string = '<html><body bgcolor="white">Source:<pre>source</pre></body></html>';

  build() {
    Column() {
      Web({
        // 使用时请替换为真实url
        src: 'https://*****',
        controller: this.controller
      })
        .onControllerAttached(() => {
          try {
            this.schemeHandler.onRequestStart((request: webview.WebSchemeHandlerRequest,
              resourceHandler: webview.WebResourceHandler) => {
              console.info('[schemeHandler] onRequestStart');
              try {
                // 可以指定请求不做拦截
                if (request.getRequestMethod() !== 'POST') {
                  return false;
                }

                // 获取POST请求体
                let stream = request.getHttpBodyStream();
                if (stream) {
                  stream.initialize().then(() => {
                    if (!stream) {
                      console.error('[schemeHandler] HttpBodyStream initialize failed.');
                      return;
                    }
                    let size = stream.getSize();
                    console.info(`[schemeHandler] HttpBodyStream size is ${size}`);
                    stream.read(size).then((result: ArrayBuffer) => {
                      console.info(`[schemeHandler] HttpBodyStream buffer length is ${result.byteLength}`);
                      // 从buffer中转换请求体内容
                      let decoder = util.TextDecoder.create('utf-8');
                      let requestBodyStr = decoder.decodeToString(new Uint8Array(result));
                      console.info(`[schemeHandler] HttpBodyStream requestBody is ${requestBodyStr}`);
                    }).catch((error: BusinessError) => {
                      console.error(`[schemeHandler] HttpBodyStream read failed, message is ${error.message}`);
                    });
                  });
                } else {
                  console.info('[schemeHandler] onRequestStart has no http body stream');
                }
              } catch (error) {
                console.error(`[schemeHandler] ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
              }

              // 构造响应体返回
              let response = new webview.WebSchemeHandlerResponse();
              try {
                response.setNetErrorCode(WebNetErrorList.NET_OK);
                response.setStatus(200);
                response.setStatusText('OK');
                response.setMimeType('text/html');
                response.setEncoding('utf-8');
                response.setHeaderByName('header1', 'value1', false);
              } catch (error) {
                console.error(`[schemeHandler] ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
              }

              // 调用didFinish/didFail前需要优先调用didReceiveResponse将构造的响应头传递给被拦截的请求。
              let buf = buffer.from(this.htmlData);
              try {
                if (buf.length == 0) {
                  console.info('[schemeHandler] length 0');
                  resourceHandler.didReceiveResponse(response);
                  // 如果认为buf.length为0是正常情况，则调用resourceHandler.didFinish，否则调用resourceHandler.didFail
                  resourceHandler.didFail(WebNetErrorList.ERR_FAILED);
                } else {
                  console.info('[schemeHandler] length 1');
                  resourceHandler.didReceiveResponse(response);
                  resourceHandler.didReceiveResponseBody(buf.buffer);
                  resourceHandler.didFinish();
                }
              } catch (error) {
                console.error(`[schemeHandler] ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
              }
              return true;
            });

            this.schemeHandler.onRequestStop((request: webview.WebSchemeHandlerRequest) => {
              console.info('[schemeHandler] onRequestStop, url：' + request.getRequestUrl());
            });

            this.controller.setWebSchemeHandler('https', this.schemeHandler);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
        .javaScriptAccess(true)
        .domStorageAccess(true)
        .fileAccess(true)
        .geolocationAccess(false);
    };
  }
}
```

Q：H5通过Web组件加载，想要拦截所有网络请求，对请求进行加解密、或者代理请求，替换header等，如何实现？

A：可通过[WebSchemeHandler](../harmonyos-references/arkts-apis-webview-webschemehandler.md)定义schema，拦截网页所有请求后，获取请求体，请求header等，可进行加密，修改请求体、url等操作，修改完成后，通过[rcp](../harmonyos-references/remote-communication-rcp.md)重新发送请求，获取rcp响应之后，再获取rcp响应报文，对响应报文进行解密、修改响应体等操作，修改完成之后，再返回给Web请求的响应。

参考如下代码：

```ts
import { WebNetErrorList, webview } from '@kit.ArkWeb';
import { rcp } from '@kit.RemoteCommunicationKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 源url
const SOURCE_URL: string = 'https://***1';
// 目标url
const TARGET_URL: string = 'https://***2';

export class HttpProxy {
  session = rcp.createSession();

  constructor(sessionConfiguration?: rcp.SessionConfiguration | undefined) {
    try {
      this.session = rcp.createSession(sessionConfiguration);
    } catch (error) {
      console.error(`ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`);
    }
  }

  /**
   * 处理响应
   * @param res
   * @param resourceHandler
   */
  private handleResponse(res: rcp.Response, resourceHandler: webview.WebResourceHandler): void {
    let response = new webview.WebSchemeHandlerResponse();
    response.setStatus(res.statusCode);
    response.setStatusText('OK');
    response.setNetErrorCode(WebNetErrorList.NET_OK);
    // 将rcp响应头塞到Web响应头中，此处响应头也可自定义
    Object.keys(res.headers).forEach((key: string) => {
      const value = res.headers[key];
      if (value) {
        console.log(`请求头：${key}:${value}`);
        response.setHeaderByName(key, value?.toString(), true);
      }
    });
    // 不涉及跨域，可手动删除下面的header
    response.setHeaderByName('Access-Control-Allow-Origin', '*', true);
    response.setHeaderByName('Access-Control-Allow-Credentials', 'true', true);
    response.setHeaderByName('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE', true);
    response.setHeaderByName('Access-Control-Allow-Headers', 'Content-Type, Authorization', true);
    try {
      // 将响应返回给Web
      resourceHandler.didReceiveResponse(response);
      resourceHandler.didReceiveResponseBody(res.body);
      resourceHandler.didFinish();
    } catch (error) {
      console.error(`ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`);
    }
  }

  /**
   * 代理请求
   * @param request
   * @param resourceHandler
   */
  public fetch(request: webview.WebSchemeHandlerRequest, resourceHandler: webview.WebResourceHandler): void {
    try {
      // 替换请求url
      let url = request.getRequestUrl().replace(SOURCE_URL, TARGET_URL);
      // 此处rcp请求，可自定义增加header、cookie、请求参数、对请求体加解密等
      let req = new rcp.Request(url, request.getRequestMethod());
      this.session?.fetch(req).then((res) => {
        this.handleResponse(res, resourceHandler);
      }).catch((error: BusinessError) => {
        console.error(`ErrorCode: ${error.code}, Message: ${error.message}`);
      });
    } catch (error) {
      console.error(`ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`);
    }
  }
}

@Entry
@Component
struct WebRequestProxyDemo {
  controller: webview.WebviewController = new webview.WebviewController();
  schemeHandler: webview.WebSchemeHandler = new webview.WebSchemeHandler();
  httpProxy: HttpProxy = new HttpProxy();
  uiContext: UIContext = this.getUIContext();

  aboutToAppear(): void {
    webview.WebviewController.setWebDebuggingAccess(true);
  }

  build() {
    Column() {
      Web({ src: SOURCE_URL, controller: this.controller })
        .onControllerAttached(() => {
          try {
            this.schemeHandler.onRequestStart((request: webview.WebSchemeHandlerRequest,
              resourceHandler: webview.WebResourceHandler) => {
              console.info('[schemeHandler] onRequestStart');
              // 对请求进行拦截，拦截规则可自定义
              if (request.getRequestUrl().includes(SOURCE_URL)) {
                // 使用rcp代理请求
                this.httpProxy.fetch(request, resourceHandler);
                return true;
              } else {
                return false;
              }
            });

            // 通过WebSchemeHandler，拦截所有https协议请求
            this.controller.setWebSchemeHandler('https', this.schemeHandler);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`);
          }
        })
        .fileAccess(true)
        .geolocationAccess(false);
    }
    .width('100%')
    .height('100%');
  }
}
```
