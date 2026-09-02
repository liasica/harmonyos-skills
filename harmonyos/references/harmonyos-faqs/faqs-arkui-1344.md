---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1344
title: H5页面实现的登录界面可以被截屏
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > H5页面实现的登录界面可以被截屏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:13+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6301b5a6727d368f3ef3a16030584ce2839db89c2f3464c9c3f67a0303005d59
---

## 问题现象

* 场景1：用户在使用应用时，打开账号登录页面，发现该页面可以被截屏。
* 场景2：用户在使用应用时，打开账号登录页面，发现该页面在密码输入框获取焦点时无法被截屏。但是，当焦点不在密码输入框时，可以被截屏。

## 背景知识

* [ohos.permission.PRIVACY\_WINDOW](../harmonyos-guides/permissions-for-all.md#ohospermissionprivacy_window)：允许应用将窗口设置为隐私窗口，禁止截屏录屏。
* [ArkWeb简介](../harmonyos-guides/web-component-overview.md)：ArkWeb（方舟Web）提供了Web组件，用于在应用程序中显示Web页面内容。
* [Web组件的生命周期](../harmonyos-guides/web-event-sequence.md)：Web组件提供生命周期回调接口，用于感知状态变化和处理业务。
* [setWindowPrivacyMode](../harmonyos-references/arkts-apis-window-window.md#setwindowprivacymode9)：设置窗口是否为隐私模式，使用callback异步回调。设置为隐私模式的窗口，窗口内容将无法被截屏或录屏。此接口可用于禁止截屏/录屏的场景。

## 问题定位

1. 使用DevEco Testing工具查看应用的页面结构，发现使用了ArkWeb组件，应用内的页面都为H5页面。
2. 登录页面为ArkWeb组件加载的一个云端的H5页面。
3. 检查应用代码，module.json5配置文件中是否有ohos.permission.PRIVACY\_WINDOW配置项。
4. 检查应用代码，检查是否调用setWindowPrivacyMode方法设置窗口为隐私模式。

## 分析结论

* 未配置ohos.permission.PRIVACY\_WINDOW配置项。
* 未调用setWindowPrivacyMode方法设置窗口为隐私模式。

## 修改建议

1. 在module.json5文件中声明需要使用的ohos.permission.PRIVACY\_WINDOW权限。
2. 使用ArkWeb组件加载用于登录的H5页面时，可以在ArkWeb的生命周期的onPageEnd事件中检查当前页面的title是否为登录页面。如果当前加载的H5页面为登录页面，则可以调用setWindowPrivacyMode方法设置窗口为隐私模式，否则设置为非隐私模式。
3. H5页面上，定义title标签为login，表示当前页面为登录页面。

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <title>login</title>
       <meta charset="UTF-8">
       <meta name="viewport" content="initial-scale=1.0,maximum-scale=1.0,minimum-scale=1.0,user-scalable=no">
   </head>
   <body>
   <div>
       <span id="test">模拟登录页的H5页面！</span><br/>
   </div>
   </body>
   </html>
   ```
4. ArkTS中定义一个js脚本读取当前页面的title信息，之后在ArkWeb组件的onPageEnd事件上，调用该脚本获取H5页面的title，并根据结果判断是否为登录页。如果为登录页，则当前窗口为隐私模式。

   ```ts
   import { webview } from '@kit.ArkWeb';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { common } from '@kit.AbilityKit';
   import { window } from '@kit.ArkUI';

   class windowUtils {
     static setWindowPrivacyModeInPage(context: common.UIAbilityContext, isFlag: boolean) {
       window.getLastWindow(context).then((lastWindow) => {
         lastWindow.setWindowPrivacyMode(isFlag, (err: BusinessError) => {
           const errCode: number = err.code;
           if (errCode) {
             console.error('Failed to set the window to privacy mode. 1Cause:' + JSON.stringify(err));
             return;
           }
           console.info('Succeeded in setting the window to privacy mode.');
         });
       });
     }
   }

   @Entry
   @Component
   struct WebComponent {
     // 读取网页标题
     controller: webview.WebviewController = new webview.WebviewController();
     jsCode: string = `function test(){
       return document.title
     }
     test();`;
     @State htmlTitle: string = '网页标题是：';
     context = this.getUIContext();

     build() {
       Column() {
         Text(this.htmlTitle)
         // H5页面路径请替换为实际路径
         // 根据网页标题判断如果为登录页，设置隐私模式
         Web({ src: $rawfile("loginTest.html"), controller: this.controller }).fileAccess(false).geolocationAccess(false)
           .onPageEnd((event) => {
             if (event) {
               this.controller.runJavaScript(this.jsCode)
                 .then((result) => {
                   this.htmlTitle = result.replaceAll('"', '');
                   if (this.htmlTitle === 'login') {
                     windowUtils.setWindowPrivacyModeInPage(this.context.getHostContext() as common.UIAbilityContext,
                       true);
                   } else {
                     windowUtils.setWindowPrivacyModeInPage(this.context.getHostContext() as common.UIAbilityContext,
                       false);
                   }
                 });
             }
           })
       }
     }
   }
   ```
