---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1152
title: 如何使用组件导航切换页面并保持顶部组件展示
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何使用组件导航切换页面并保持顶部组件展示
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:20+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ad49c2d2570035e2684cebf0fd6b59d0dc06f8d5ac87a454eff48493c1004446
---

## 问题现象

页面使用组件导航实现路由跳转，期望自定义一个半屏组件能够始终保持在所有页面的顶部。

## 背景知识

* [层叠布局](../harmonyos-guides/arkts-layout-development-stack-layout.md)用于在屏幕上预留一块区域来显示组件中的元素，提供元素可以重叠的布局。层叠布局通过[Stack](../harmonyos-references/ts-container-stack.md)容器组件实现位置的固定定位与层叠，容器中的子元素依次入栈，后一个子元素覆盖前一个子元素，子元素可以叠加，也可以设置位置。
* [组件导航](../harmonyos-references/ts-basic-components-navigation.md)主要用于实现页面间以及组件内部的页面跳转，支持在不同组件间传递跳转参数，提供灵活的跳转栈操作，从而更便捷地实现对不同页面的访问和复用。

## 解决方案

1. 若要实现顶层组件处于最顶层可以通过Stack层叠布局实现，在Stack内需要置顶的组件的[Z序控制（zIndex）](../harmonyos-references/ts-universal-attributes-z-order.md#zindex)值置为最高，如代码中Navigation组件的zIndex为1，TextInput组件的zIndex为2，那TextInput将会显示在Navigation上层。

   ```ts
   @Entry
   @Component
   struct NavigationExample {
     pageInfos: NavPathStack = new NavPathStack();

     build() {
       Column() {
         Stack() {
           Navigation(this.pageInfos) {
             Column({ space: 12 }) {
               Button('页面一', { stateEffect: true, type: ButtonType.Capsule })
                 .width('75%')
                 .height('30')
                 .onClick(() => {
                   // 点击筛选后的列表项跳转到展示页面
                   this.pageInfos.pushPathByName('PageOne', null);
                 })
               Button('页面二', { stateEffect: true, type: ButtonType.Capsule })
                 .width('75%')
                 .height('30')
                 .onClick(() => {
                   this.pageInfos.pushPathByName('PageTwo', null);
                 })
             }
             .width('100%')
             .height('100%')
             .justifyContent(FlexAlign.Start)
           }
           .title('Page')
           .zIndex(1)

           TextInput({ placeholder: '请输入内容' })
             .zIndex(2)
             .width('100%')
             .height(300)
             .position({ bottom: 0 })
             .alignSelf(ItemAlign.Center)
         }

       }
     }
   }
   ```
2. 在底层组件中通过[NavPathStack](../harmonyos-references/ts-basic-components-navigation.md#navpathstack10)的[pushPathByName](../harmonyos-references/ts-basic-components-navigation.md#pushpathbyname10)传入指定页面实现跳转，同时保证顶层组件不变。

   页面一代码：

   ```ts
   @Builder
   export function PageOneBuilder() {
     PageOne()
   }

   @Entry
   @Component
   export struct PageOne {
     pageInfos: NavPathStack = new NavPathStack();
     keyWord: string = 'page one';

     build() {
       NavDestination() {
         Column({ space: 12 }) {
           Button('页面二', { stateEffect: true, type: ButtonType.Capsule })
             .width('75%')
             .height('30')
             .onClick(() => {
               this.pageInfos.pushPathByName('PageTwo', this.keyWord);
             })

         }
         .width('100%')
         .height('100%')
         .justifyContent(FlexAlign.Start)

       }
       .title('页面一')
       .onReady((context: NavDestinationContext) => {
         this.pageInfos = context.pathStack;
       })
     }
   }
   ```

   页面二代码：

   ```ts
   @Builder
   export function PageTwoBuilder() {
     PageTwo()
   }

   @Entry
   @Component
   export struct PageTwo {
     pageInfos: NavPathStack = new NavPathStack();
     keyWord: string = '';

     build() {
       NavDestination() {
         Column({ space: 12 }) {
           Button('页面一', { stateEffect: true, type: ButtonType.Capsule })
             .width('75%')
             .height('30')
             .onClick(() => {
               this.pageInfos.pushPathByName('PageOne', null);
             })
         }
         .width('100%')
         .height('100%')
         .justifyContent(FlexAlign.Start)
       }
       .title('页面二')
       .onReady((context: NavDestinationContext) => {
         this.pageInfos = context.pathStack;
       })
     }
   }
   ```

   router\_map.json配置如下：

   ```json
   {
     "routerMap": [
       {
         "name": "PageOne",
         "pageSourceFile": "src/main/ets/pages/PageOne.ets",
         "buildFunction": "PageOneBuilder"
       },
       {
         "name": "PageTwo",
         "pageSourceFile": "src/main/ets/pages/PageTwo.ets",
         "buildFunction": "PageTwoBuilder"
       }
     ]
   }
   ```

## 常见FAQ

Q：pushPathByName传入的路径为字符串，页面名称是否区分大小写？

A：区分大小写，如果传入的页面名称和实际的页面名称不一致会导致需跳转页面无法显示。
