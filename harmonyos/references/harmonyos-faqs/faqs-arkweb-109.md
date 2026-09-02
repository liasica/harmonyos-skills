---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-109
title: 跳转到的目标页面为空白页
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 跳转到的目标页面为空白页
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c43551f20994fe0b848b6664e55c110bedcef2cfab78b5149ad866199d0c13a5
---

## 问题现象

用户在应用内点击某个功能，发生页面跳转，跳转到的目标页面为空白页。

## 背景知识

* [ArkWeb简介](../harmonyos-guides/web-component-overview.md)：ArkWeb（方舟Web）提供了Web组件，用于在应用程序中显示Web页面内容。
* DevTools：Web组件支持使用DevTools工具调试前端页面。DevTools是一个Web前端开发调试工具，提供了电脑上调试移动设备前端页面的能力。开发者通过setWebDebuggingAccess()接口开启Web组件前端页面调试能力，利用DevTools工具可以在电脑上调试移动设备上的前端网页，设备需为4.1.0及以上版本。更多详细内容可以看[使用DevTools工具调试前端页面](../harmonyos-guides/web-debugging-with-devtools.md)。

## 问题定位

使用DevTools录制页面加载情况。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/QZhJkM5aT0GrK3jiNGcEfQ/zh-cn_image_0000002659138397.png "点击放大")

可看到网页加载时的地址出现ERR\_NAME\_NOT\_RESOLVED错误（域名无法解析），IP地址不正确，资源请求超时。

## 分析结论

应用跳转的页面是加载的一个Web页面，由于该页面实际已经不存在，导致Web组件无法加载，出现白屏现象。

## 修改建议

1. 检查Web网页的地址是否正确，如果不正确更换为正确的Web页面地址。
2. 在ArkWeb组件的生命周期中，通过[onErrorReceive](../harmonyos-references/arkts-basic-components-web-events.md#onerrorreceive)来检查网页是否存在加载错误，如果存在错误，可以在[onPageEnd](../harmonyos-references/arkts-basic-components-web-events.md#onpageend)回调中加载一个默认页面用于提醒用户加载异常。

   ```ts
   // xxx.ets
   import { webview } from '@kit.ArkWeb';
   import { BusinessError } from '@kit.BasicServicesKit';

   @Entry
   @Component
   struct WebComponent {
     isError: boolean = false;
     controller: webview.WebviewController = new webview.WebviewController();
     responseWeb: WebResourceResponse = new WebResourceResponse();
     heads: Header[] = new Array();
     webData: string = '<!DOCTYPE html>\n' +
       '<html>\n' +
       '<head>\n' +
       '<title>intercept test</title>\n' +
       '</head>\n' +
       '<body>\n' +
       '<h1>intercept test</h1>\n' +
       '</body>\n' +
       '</html>';

     aboutToAppear(): void {
       try {
         webview.WebviewController.setWebDebuggingAccess(true);
       } catch (error) {
         console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
       }
     }

     build() {
       Column() {
         // 请使用真实地址
         Web({ src: '', controller: this.controller }).fileAccess(false).geolocationAccess(false)
           .onControllerAttached(() => {
             // 推荐在此loadUrl、设置自定义用户代理、注入JS对象等
             console.info('onControllerAttached execute');
           })
           .onLoadIntercept((event) => {
             if (event) {
             }
             // 返回true表示阻止此次加载，否则允许此次加载
             return false;
           })
           .onOverrideUrlLoading((webResourceRequest: WebResourceRequest) => {
             if (webResourceRequest && webResourceRequest.getRequestUrl() == 'about:blank') {
               return true;
             }
             return false;
           })
           .onPageEnd((event) => {
             // 推荐在此事件中执行JavaScript脚本
             if (event) {
               console.info('onPageEnd url:' + event.url);
             }
             if (this.isError) {
               console.info('isError: ' + this.isError);
               // 当页面加载出错时，给出提示信息或者可以根据业务需要跳转到相应页面。
               this.controller.loadData(this.webData, 'text/html', 'UTF-8');
             }
             this.isError = false;
           })
           .onPageVisible((event) => {
             console.info('onPageVisible url:' + event.url);
           })
           .onRenderExited((event) => {
             if (event) {
               console.info('onRenderExited reason:' + event.renderExitReason);
             }
           })
           .onDisAppear(() => {
             this.getUIContext().getPromptAction().showToast({
               message: 'The web is hidden',
               duration: 2000
             });
           })
           .onErrorReceive((event) => {
             if (event) {
               console.info('onErrorReceive');
               // 页面加载出错
               if (event.request.isMainFrame()) {
                 this.isError = true;
               }
             }
           });
       };
     }
   }
   ```
