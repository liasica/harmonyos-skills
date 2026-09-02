---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1399
title: Navigation如何获取页面名称
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Navigation如何获取页面名称
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:17+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:43528c9abaf0df3775477199c9bd1f9092f6971e0bd1b1ce8c41d225b48685f8
---

## 问题现象

Navigation路由跳转场景下，如何获取当前所在页面的页面名称或者信息？

## 背景知识

* NavPathStack页面路由栈，此对象下保存了当前的路由过程，其中[getAllPathName](../harmonyos-references/ts-basic-components-navigation.md#getallpathname10)返回路由栈中所有NavDestination页面名称的数组，最后一项即为当前页面名称。
* NavDestination：进行路由跳转的时候，NavDestination会响应[onReady](../harmonyos-references/ts-basic-components-navdestination.md#onready11)方法，其响应参数为NavDestinationContext，其包含了页面名称等信息。
* setInterception：Navigation提供的页面跳转拦截回调方法，可以在[setInterception](../harmonyos-references/ts-basic-components-navigation.md#setinterception12)中拦截页面跳转操作，也可以获取到NavDestinationContext的内容。

## 解决方案

获取页面名称的方案有三种：

* 通过NavPathStack的getAllPathName方法拿到所有页面的名称，最后一项即为当前页面名称。
* 在NavDestination的onReady回调中通过NavDestinationContext中的pathInfo拿到页面名称。
* 通过setInterception拦截页面跳转，获取到跳转目标页面名称。

Navigation页面：

```screen
import { NaviDesPagBuilder } from './SubPage';

@Entry
@Component
struct Index {
  navPathStack: NavPathStack = new NavPathStack();

  aboutToAppear(): void {
    // 通过setInterception跳转拦截获取目标页面名称
    this.navPathStack.setInterception({
      willShow: (from: NavDestinationContext | 'navBar', to: NavDestinationContext | 'navBar') => {
        if (typeof from === 'string') {
          console.info(`from: ${from}`);
        }
        if (typeof to === 'string') {
          console.info('target page is navigation home');
          return;
        }
        let target: NavDestinationContext = to as NavDestinationContext;
        console.info(`setInterception currentPageName = ${target.pathInfo.name}`);
      }
    });
  }

  @Builder
  pageMap(name: string) {
    if (name === 'GetNaviPageName_NaviDesPage') {
      NaviDesPagBuilder();
    }
  }

  build() {
    Navigation(this.navPathStack) {
      Button('跳转NavDestination')
        .fontSize('20fp')
        .margin({ top: '50vp' })
        .onClick(() => {
          this.navPathStack.pushPath({ name: 'GetNaviPageName_NaviDesPage' });
        });
    }.navDestination(this.pageMap)
    .height('100%')
    .width('100%');
  }
}
```

NavDestination页面：

```screen
@Builder
export function NaviDesPagBuilder() {
  GetNaviPageName_NaviDesPage();
}

@Entry
@Component
struct GetNaviPageName_NaviDesPage {
  navPathStack: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      Button('GetName')
        .onClick(() => {
          // 调用getAllPageName，拿到所有页面名字，最后一项即为当前页面名称
          let names = this.navPathStack.getAllPathName();
          let pageName = names[names.length-1];
          console.info(`last page of getAllPathName: ${pageName}`);
        });
    }
    .onReady((ctx: NavDestinationContext) => {
      // 通过onReady回调的NavDestinationContext获取当前页面名称
      this.navPathStack = ctx.pathStack;
      console.info(`onReady: ${ctx.pathInfo.name}`);
    }).height('100%').width('100%');
  }
}
```

## 常见FAQ

Q：Navigation获取页面参数getParamByName获取的返回值为什么是Array？

A：getParamByName是路由栈NavPathStack的实例方法，路由栈中一个页面可以入栈多次。例如在页面A中push一个页面A，此时路由栈中就有两个页面A，每次跳转到页面A可能携带不同的参数，所以getParamByName方法的返回值是数组。
