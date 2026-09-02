---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-39
title: 如何实现跨模块的页面跳转功能
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 如何实现跨模块的页面跳转功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:16539eb6a2ff718a9a0c890a50c2341ab6e747f7833f75bcc4d05c80cfd98b14
---

在业务体系庞大或复杂的情况下，会将业务拆分成多个子业务模块，每个子业务模块为一个HAR/HSP。在该场景下，存在从主业务入口跳转到不同子页面模块，或从一个子业务模块A页面跳转到另一个子业务模块B页面的需求。例如，从应用首页跳转到登录子业务模块页面。针对该场景，有以下三种解决方案：

* 方案一：使用router的命名路由接口router.pushNamedRoute()跳转。

  参考地址：[页面路由 (@ohos.router)](../harmonyos-guides/arkts-routing.md)
* 方案二：使用navigation组件跳转。

  以从应用入口模块的页面NavigationPage跳转到Login子业务模块页面LoginPage为例。主要包含以下步骤：

  1. 在Login模块中开发自定义组件LoginPage作为路由跳转目的地，并对外导出。

     ```typescript
     @Component
     export struct LoginPage {
       @Consume('pathStack') pathStack: NavPathStack;
       @State message: string = 'Login Page';

       build() {
         NavDestination() {
           Column() {
             Text(this.message)
               .fontSize(50)
               .fontWeight(FontWeight.Bold)
           }
           .width('100%')
           .height('100%')
         }
         .onBackPressed(() => {
           this.pathStack.pop();
           return true;
         })
       }
     }
     ```
  2. 在Login模块的入口文件Index.ets中导出自定义组件。export { LoginPage } from './src/main/ets/pages/loginPage';
  3. 在入口模块的oh-package.json5文件中添加对Login模块的依赖项。

     ```json
     {
       // ...
       "dependencies": {
         "@ohos/login": "file:../LoginModule"
       }
     }
     ```
  4. 入口模块导入Login模块的自定义组件，并添加到Navigation组件的路由表中。

     ```typescript
     // Import a custom component of the Login module
     import { LoginPage } from '@ohos/login';

     @Entry
     @Component
     struct NavigationPage {
       @Provide('pathStack') pathStack: NavPathStack = new NavPathStack();

       @Builder
       pageMap(name: string) {
         if (name === 'loginPage') {
           LoginPage()
         }
       }

       build() {
         Navigation(this.pathStack) {
           Button('jump to login page')
             .onClick(() => {
               // The second parameter of NavPathInfo is a custom parameter that can be used for message transfer
               let pathInfo: NavPathInfo = new NavPathInfo('loginPage', new Object());
               this.pathStack.pushDestination(pathInfo, true);
             })
         }
         .navDestination(this.pageMap)
       }
     }
     ```
* 方案三：使用基于navigation组件的自定义路由框架跳转。

  方案二虽然可以实现跨模块跳转的功能，但当模块间跳转需求增多，各个模块间将存在非常复杂的依赖关系，甚至会导致多个HAR/HSP间循环依赖。为了解决模块间的强耦合关系，并且提升页面加载性能，推荐[跨包路由](../harmonyos-guides/arkts-router-to-navigation.md#跨包路由)。
