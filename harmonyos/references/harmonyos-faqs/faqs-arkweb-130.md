---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-130
title: H5页面实现页面后退
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > H5页面实现页面后退
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:33+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:35b6b5b44645d0526beac98af3b177cf042663d3674534a629c01807dd4586da
---

## 问题现象

* 场景一：如何在H5页面中监听侧滑手势，实现H5页面逐级后退功能？
* 场景二：如何实现点击本地H5页面后返回应用侧页面？

## 背景知识

* [onBackPress](../harmonyos-references/ts-custom-component-lifecycle.md#onbackpress)：当用户侧滑/点击返回按钮时触发，在router路由页面（即@Entry装饰的自定义组件）生效。
* 通过[WebMessagePort](../harmonyos-references/arkts-apis-webview-webmessageport.md)可以进行消息的发送以及接收，发送WebMessageType/WebMessage类型消息给HTML5侧：
  + [postMessageEvent](../harmonyos-references/arkts-apis-webview-webmessageport.md#postmessageevent)：发送WebMessage类型消息给HTML5侧，必须先调用onMessageEvent，否则会发送失败。
  + [onMessageEvent](../harmonyos-references/arkts-apis-webview-webmessageport.md#onmessageevent)：在应用侧的消息端口上注册回调函数，接收HTML5侧发送过来的WebMessage类型消息。

## 解决方案

* 场景一：针对在H5页面中监听侧滑手势，来实现页面回退功能，根据Web组件所在层级不同方案分别如下：
  1. 如果是在@Entry装饰的组件中，可以直接通过onBackPress拦截侧滑事件，然后通过WebView的[forward()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#forward)和[backward()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#backward)接口向前/向后浏览上一个/下一个历史记录，实现页面的前进和后退。

     示例代码如下：

     ```ts
     import { webview } from '@kit.ArkWeb';
     import { BusinessError } from '@kit.BasicServicesKit';

     @Entry
     @Component
     struct Method1 {
       private webviewController: webview.WebviewController = new webview.WebviewController();
       private url: string = 'https://www.***.com'; // 需要替换为真实的url

       onBackPress(): boolean | void {
         try {
           const result = this.webviewController.accessBackward();
           if (result) {
             this.webviewController.backward();
             return true;
           }
           return false;
         } catch (error) {
           console.error(`catch exception: ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
           return false;
         }
       }

       build() {
         Column() {
           Web({
             src: this.url,
             controller: this.webviewController
           })
             .fileAccess(false)
             .geolocationAccess(false);
         }
         .height('100%')
         .width('100%');
       }
     }
     ```
  2. 在NavDestination组件中，采用onBackPressed回调对返回事件进行拦截，实现页面的前进和后退。

     示例代码如下：

     ```ts
     import { WebPage } from './WebPage';

     @Entry
     @Component
     struct Method2 {
       @Provide('NavPathStack') stack: NavPathStack = new NavPathStack();

       @Builder
       pageMap(name: string) {
         if (name === 'WebPage') {
           WebPage();
         }
       }

       build() {
         Column() {
           Navigation(this.stack) {
             Button('Navigation到Web页面')
               .onClick(() => {
                 this.stack.pushPathByName('WebPage', null, false);
               });
           }
           .titleMode(NavigationTitleMode.Full)
           .mode(NavigationMode.Stack)
           .hideToolBar(true)
           .navDestination(this.pageMap);
         }
         .height('100%')
         .width('100%');
       }
     }
     ```

     ```ts
     import { webview } from '@kit.ArkWeb';
     import { BusinessError } from '@kit.BasicServicesKit';

     @Component
     export struct WebPage {
       @Consume('NavPathStack') stack: NavPathStack;
       private webVC: webview.WebviewController = new webview.WebviewController();
       private url: string = 'https://www.***.com'; // 需要替换为真实的url

       build() {
         NavDestination() {
           Column() {
             Web({
               src: this.url,
               controller: this.webVC,
             })
               .fileAccess(false)
               .geolocationAccess(false)
               .javaScriptAccess(true)
               .domStorageAccess(true)
               .onlineImageAccess(true);
           };
         }
         .height('100%')
         .width('100%')
         .onBackPressed(() => {
           try {
             // 判断是否可以返回，如果可以的话调用backward()接口返回
             const result = this.webVC.accessBackward();
             if (result) {
               this.webVC.backward();
               return true;
             }
             return false;
           } catch (error) {
             console.error(`catch exception: ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
             return false;
           }
         });
       }
     }
     ```
* 场景二：如果要实现在H5页面中点击返回到应用侧，可以通过[WebMessagePort](../harmonyos-references/arkts-apis-webview-webmessageport.md)进行消息的发送以及接收，H5页面接收到消息后调用应用侧方法，实现点击H5页面按钮页面后退。
  1. Web页面代码如下：

     ```ts
     import { webview } from '@kit.ArkWeb';
     import { common } from '@kit.AbilityKit';
     import { BusinessError } from '@kit.BasicServicesKit';

     interface JSBridgeModel {
       method: string,
       name?: string,
       password?: string
       appId?: string
       shareType?: number
       newWebUrl?: string
       orientation?: number
     }

     @Component
     export struct WebPage {
       pageInfos: NavPathStack = new NavPathStack();
       controller: webview.WebviewController = new webview.WebviewController();
       ports: webview.WebMessagePort[] = [];
       context = this.getUIContext().getHostContext() as common.UIAbilityContext;

       onBackPress() {
         if (this.controller.accessBackward()) {
           this.controller.backward();
           return true;
         }
         return false;
       }

       handleJsMsg(model: JSBridgeModel) {
         if (model.method === 'back') {
           // 返回上一级页面
           this.pageInfos.pop();
         }
       }

       build() {
         NavDestination() {
           Column() {
             Web({ src: $rawfile('index.html'), controller: this.controller })
               .domStorageAccess(true) // 是否开启文档对象模型存储接口
               .imageAccess(true) // 是否允许自动加载图片资源，默认允许
               .javaScriptAccess(true) // 是否允许执行JavaScript
               .databaseAccess(true) // 是否开启数据库存储API权限，默认不开启
               .onlineImageAccess(true) // 是否允许从网络加载图片资源
               .fileAccess(false)
               .geolocationAccess(false)
               .onPageEnd(() => {
                 try {
                   // 1、创建两个消息端口。
                   this.ports = this.controller.createWebMessagePorts();
                   // 2、在应用侧的消息端口(如端口1)上注册回调事件。
                   this.ports[1].onMessageEvent((result: webview.WebMessage) => {
                     if (typeof (result) === 'string') {
                       const resStr = result.toString();
                       // 处理js回调事件
                       const objData: JSBridgeModel = JSON.parse(resStr) as JSBridgeModel;
                       this.handleJsMsg(objData);
                     }
                   });
                   // 3、将另一个消息端口(如端口0)发送到HTML侧，由HTML侧保存并使用。
                   this.controller.postMessage('__init_port__', [this.ports[0]], '*');
                 } catch (error) {
                   console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
                 }
               });
           }
           .height('100%')
           .width('100%')
           .backgroundColor('#ace');
         }
         .hideBackButton(true)
         .onReady((context: NavDestinationContext) => {
           this.pageInfos = context.pathStack;
         });
       }
     }
     ```
  2. 应用侧页面通过路由跳转Web页面：

     ```ts
     import { WebPage } from './WebPage';

     @Entry
     @Component
     struct Index {
       @Provide('NavPathStack') stack: NavPathStack = new NavPathStack();

       @Builder
       pageMap(name: string) {
         if (name === 'WebPage') {
           WebPage();
         }
       }

       build() {
         Column() {
           Navigation(this.stack) {
             Button('Navigation到本地H5页面')
               .onClick(() => {
                 this.stack.pushPathByName('WebPage', null, false);
               });
           }
           .titleMode(NavigationTitleMode.Full)
           .mode(NavigationMode.Stack)
           .hideToolBar(true)
           .navDestination(this.pageMap);
         }
         .height('100%')
         .width('100%');
       }
     }
     ```
  3. 本地H5页面代码：

     ```html
     <!DOCTYPE html>
     <html>
     <head>
         <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
     </head>

     <body>
     <div class="button" onclick="buttonClicked('back')">返回上一级页面</div>
     </body>
     <script>
         let jsPort;
         window.onload = function() {
           console.info("网页加载完毕")
           window.addEventListener('message', function(event) {
             if (event.data === '__init_port__') {
               console.info("__init_port__", JSON.stringify(event.ports[0]))
               if (event.ports[0] != null) {
                 // 1.保存从ets侧发送过来的端口
                 jsPort = event.ports[0];
                 jsPort.onmessage = function(event) {
                   // 2.接收ets侧发送过来的消息.
                   let msg = 'Got message from ets:';
                 }
               }
             }
           })
         }

         function buttonClicked(value) {
           let data = {
             "method": value
           };
           if (jsPort) {
             jsPort.postMessage(JSON.stringify(data));
           }
         }
     </script>
     </html>
     ```
