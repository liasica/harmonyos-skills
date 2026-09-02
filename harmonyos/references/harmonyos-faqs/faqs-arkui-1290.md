---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1290
title: HAP和HAR之间页面跳转
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > HAP和HAR之间页面跳转
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:46+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:cd56bbacc3bfc2486f261223e3452f8d4c8537ef968a5196e4402454cc751b44
---

## 问题现象

HAP如何跳转到HAR模块页面？HAR模块内页面如何跳至HAP模块页面？

## 背景知识

* [组件导航（Navigation）](../harmonyos-guides/arkts-navigation-navigation.md)主要用于实现页面间以及组件内部的页面跳转，支持在不同组件间传递跳转参数，提供灵活的跳转栈操作，从而更便捷地实现对不同页面的访问和复用。
* [页面路由](../harmonyos-guides/arkts-routing.md)指在应用程序中实现不同页面之间的跳转和数据传递。Router模块通过不同的url地址，可以方便地进行页面路由，轻松地访问不同的页面。
* 在项目中使用HAR模块：[HAR构建](../harmonyos-guides/ide-hvigor-build-har.md)，[HAR包导入](../harmonyos-guides/ide-har-import.md)。

## 解决方案

**说明** 

跨包跳转场景，以下是**关键注意事项**：

1. 模块类型限制：仅适用于HAR（静态库）或HSP（动态库）模块。
2. HAP跳转到其他HAP的页面，必须使用UIAbility的startAbility方法拉起目标HAP的Ability。参考[跨HAP包页面跳转方案](faqs-package-structure-76.md)。

HAP和HAR之间页面跳转的两种实现方案：**Navigation路由**和**Router路由**。

跳转示例：HAP包入口页面->HAR包CustomPage页面->HAP包Page页面。如下所示：

* **方案一**：Navigation路由配置**。**
  1. 在HAR模块内配置HAR页面的路由表：配置CustomPage的页面路由。即配置HAR中的module.json5文件和route\_map.json文件，详细可参考官网跨包路由的[系统路由表](../harmonyos-guides/arkts-navigation-cross-package.md#系统路由表)实现。
  2. 在HAP模块配置Page页面路由，和第1步在HAR模块配置CustomPage页面路由类似。

     ```ts
     @Builder
     export function PageBuilder() {
       Page();
     }

     @Entry
     @Component
     struct Page {
       build() {
         NavDestination() {
           Column() {
             Text('Hello World')
               .fontSize(20);
           }.height('100%').width('100%')
           .justifyContent(FlexAlign.Center);
         };
       }
     }
     ```

     ```json
     {
       "routerMap": [
         {
           "name": "Page",
           "pageSourceFile": "src/main/ets/pages/Page.ets",
           "buildFunction": "PageBuilder"
         }
       ]
     }
     ```
  3. 在HAP模块的oh-package.json5文件中引用HAR模块。

     ```json
     "dependencies": {
         "testhar": "file:../testHar"
       },
     ```
  4. 从HAP模块入口页面跳转至HAR页面CustomPage：

     ```ts
     @Entry
     @Component
     struct NavigationSolution {
       @State pathStack: NavPathStack = new NavPathStack();

       build() {
         Navigation(this.pathStack) {
           Column() {
             Button('ToHarPage', { stateEffect: true, type: ButtonType.Capsule })
               .width('80%')
               .height(40)
               .margin(20)
               .onClick(() => {
                 // 跳转至目标testHar模块所在页面
                 this.pathStack.pushPathByName('CustomPage', null, false);
               });
           }.width('100%').height('100%')
           .justifyContent(FlexAlign.Center);
         };
       }
     }
     ```
  5. 从HAR模块页面跳转至HAP模块Page页面。

     ```ts
     @Builder
     export function CustomPageBuilder() {
       CustomPage();
     }

     @Component
     export struct CustomPage {
       pathStack: NavPathStack = new NavPathStack();

       build() {
         NavDestination() {
           Column() {
             Button('跳转回HAP页面');
           }.width('100%').height('100%')
           .justifyContent(FlexAlign.Center)
           .onClick(() => {
             try {
               this.pathStack.pushPathByName('Page', null, false); // 跳转到HAP下的页面
             } catch (error) {
               console.error(`Failed to route. Code: ${error.code}, message:${error.message}`);
             }
           });
         }
         .onReady((context: NavDestinationContext) => {
           this.pathStack = context.pathStack;
         });
       }
     }
     ```

     ```json
     {
       "routerMap": [
         {
           "name": "CustomPage",
           "pageSourceFile": "src/main/ets/components/CustomPage2.ets",
           "buildFunction": "CustomPageBuilder"
         }
       ]
     }
     ```
* **方案二**：Router路由配置。
  1. 在HAR模块内src/main/ets/components目录下创建CustomPage.ets文件，作为跳转目的页面，并给@Entry修饰的自定义组件[EntryOptions](../harmonyos-guides/arkts-create-custom-components.md)命名，内容如下：

     ```ts
     @Entry({ routeName: 'CustomPage' })
     @Component
     export struct CustomPage {
       build() {
         Column() {
           Button('跳转回HAP页面');
         }.width('100%').height('100%')
         .justifyContent(FlexAlign.Center)
         .onClick(() => {
           this.getUIContext().getRouter().pushUrl({
             url: 'pages/Page'
           });
         });
       }
     }
     ```
  2. HAR模块的Index.ets中导出组件。
  3. 在HAP模块的oh-package.json5文件中引用HAR模块。同方案一的步骤三。
  4. HAP模块的RouterSolution页面import引入HAR模块内跳转目标页面，并通过pushNamedRoute方法跳转。

     ```ts
     import 'testhar/src/main/ets/components/CustomPage';

     @Entry
     @Component
     struct RouterSolution {
       build() {
         Column() {
           Button('ToHarPage', { stateEffect: true, type: ButtonType.Capsule })
             .width('80%')
             .onClick(() => {
               // 跳转至目标testHar模块所在页面
               this.getUIContext().getRouter().pushNamedRoute({
                 name: 'CustomPage'
               });
             });
         }.width('100%').height('100%')
         .justifyContent(FlexAlign.Center);
       }
     }
     ```

## 总结

组件导航（Navigation）和页面路由（@ohos.router）均支持应用内的页面跳转，但组件导航支持在组件内部进行跳转，使用更灵活。组件导航具备更强的一次开发多端部署能力，可以进行更加灵活的页面栈操作，同时支持更丰富的动效和生命周期。因此，推荐使用组件导航（Navigation）来实现页面跳转以及组件内的跳转，以获得更佳的使用体验。

## 常见FAQ

Q：使用pushNamedRoute跳转HAR页面时报100004错误（Named route error. The named route does not exist.）怎么办？

A：该错误通常是因为未正确引入HAR中命名路由页面导致。请检查以下两点：

1. 确认当前应用包的oh-package.json5文件中已正确配置HAR模块依赖：

   ```json
   "dependencies": {
       "library": "file:../library"
   }
   ```
2. 确认执行跳转的页面中已import引入HAR中命名路由页面：

   ```ts
   import 'library/Index';
   ```
