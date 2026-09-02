---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-187
title: 如何避免多个页面同时触发onRenderExited回调
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 如何避免多个页面同时触发onRenderExited回调
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:752468308a940d1be38925f1b5816a412d40c56da146cf5ff7b75fe5a22c0c75
---

## 问题现象

如果多个页面都引入了Web组件，当前页面可能收到其他页面Web组件的[onRenderExited](../harmonyos-references/arkts-basic-components-web-events.md#onrenderexited9)回调。例如，页面A和页面B都引入了Web组件，B页面的Web组件触发onRenderExited时，A页面的Web组件也会较大概率误触发该事件。请问如何避免此问题？

## 解决方案

默认情况下，Web组件采用单渲染子进程模式。当多个Web组件共享同一个渲染进程时，若该进程意外退出，onRenderExited回调将被触发一次，且影响所有共享该进程的Web组件。

为避免相互影响，Web提供了[setRenderProcessMode](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#setrenderprocessmode12)方法，可将Web组件切换至多渲染子进程模式。在此模式下，每个页面拥有独立的渲染进程，仅当某个页面的渲染进程异常退出时，才会触发其对应的onRenderExited回调，不会波及其他页面。

完整示例代码如下：

1. 创建PageA页面，调用setRenderProcessMode将Web组件设置为多渲染子进程模式。

   ```ts
   import { webview } from '@kit.ArkWeb';

   @Entry
   @Component
   struct PageA {
     pageStack: NavPathStack = new NavPathStack();
     controller: webview.WebviewController = new webview.WebviewController();

     aboutToAppear(): void {
       webview.WebviewController.setRenderProcessMode(webview.RenderProcessMode.MULTIPLE);
     }

     build() {
         Navigation(this.pageStack) {
           Column() {
             Button('跳转到PageB', { stateEffect: true, type: ButtonType.Capsule })
               .width('80%')
               .height(40)
               .margin(20)
               .onClick(() => {
                 this.pageStack.pushPathByName('PageB', null);
               });
             Web({ src: 'xxx.xxx.com', controller: this.controller }) // 请根据实际情况填写网址
               .fileAccess(false)
               .geolocationAccess(false)
               .onRenderExited((event) => {
                 if (event) {
                   console.info(`页面A触发onRenderExited: ${event.renderExitReason}`);
                 }
               });

           }.width('100%').height('100%');
         }
         .title('PageA')
         .mode(NavigationMode.Stack)
       };
   }
   ```
2. 创建PageB页面，制造一个渲染进程异常退出的场景，触发onRenderExited回调。

   ```ts
   import { webview } from '@kit.ArkWeb';

   @Builder
   export function PageBBuilder() {
     PageB();
   }

   @Component
   export struct PageB {
     pathStack: NavPathStack = new NavPathStack();
     controller: webview.WebviewController = new webview.WebviewController();

     build() {
       NavDestination() {
         Column() {
           Button('返回PageA', { stateEffect: true, type: ButtonType.Capsule })
             .width('80%')
             .height(40)
             .margin(20)
             .onClick(() => {
               this.pathStack.pop();
             });
           Web({ src: 'chrome://crash/', controller: this.controller })
             .fileAccess(false)
             .geolocationAccess(false)
             .onRenderExited((event) => {
               if (event) {
                 console.info(`页面B触发onRenderExited: ${event.renderExitReason}`);
               }
             });
         }.width('100%').height('100%');
       }.title('PageB')
       .onReady((context: NavDestinationContext) => {
         this.pathStack = context.pathStack;
       });
     }
   }
   ```
3. 配置route\_map.json。

   ```json
   {
     "routerMap": [
       {
         "name": "PageB",
         "pageSourceFile": "src/main/ets/pages/PageB.ets",
         "buildFunction": "PageBBuilder",
         "data": {
           "description" : "this is PageB"
         }
       }
     ]
   }
   ```

   查看日志，只触发了PageB页面的onRenderExited回调。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/5C8J8-U6TmeZIYaxuvSM_A/zh-cn_image_0000002628899174.png "点击放大")

   需要注意的是，setRenderProcessMode是静态方法，设置后对整个应用都生效，无需对每个Web页面重复设置。
