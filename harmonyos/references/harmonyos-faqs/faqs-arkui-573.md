---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-573
title: 如何监听Navigation路由的页面切换事件
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何监听Navigation路由的页面切换事件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:18+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b18c03b973780e11b4cb98369c7cb8f8cbe970cfc3297b85828194a5b16b0dd4
---

## 问题现象

如何监听Navigation的页面切换，以便在页面转场过程中执行自定义操作？如获取进退场页面的相关信息、拦截切换等。

## 背景知识

* [@ohos.arkui.observer(无感监听)](../harmonyos-references/js-apis-arkui-observer.md)提供UI组件行为变化的无感监听能力。如页面生命周期、组件显隐状态、滚动事件等。其中[uiObserver.on('navDestinationSwitch')](../harmonyos-references/js-apis-arkui-observer.md#uiobserveronnavdestinationswitch12)可以监听Navigation的页面切换事件并执行自定义操作。
* [setInterception](../harmonyos-references/ts-basic-components-navigation.md#setinterception12)：用于设置Navigation页面跳转拦截回调。通过setInterception方法实现路由拦截，可用于统一处理页面跳转前的逻辑校验（如登录态验证、页面状态管理等）。

## 解决方案

* **方案一**：使用uiObserver.on('navDestinationSwitch')方法订阅Navigation页面切换事件，并在参数中传入回调函数，用于执行相应的逻辑处理。

  ```screen
  import { uiObserver } from '@kit.ArkUI';

  function callBackFunc(info: uiObserver.NavDestinationSwitchInfo) {
    let from = JSON.stringify(info.from);
    let to = JSON.stringify(info.to);
    console.info(`from:${from} to: ${to}`);
  }

  @Entry
  @Component
  struct NavObserverDemo {
    private stack: NavPathStack = new NavPathStack();

    @Builder
    Page() {
      PageOne();
    }

    aboutToAppear() {
      uiObserver.on('navDestinationSwitch', this.getUIContext(), callBackFunc); // 注册页面切换的监听
    }

    aboutToDisappear() {
      uiObserver.off('navDestinationSwitch', this.getUIContext(), callBackFunc);
    }

    build() {
      Navigation(this.stack) {
        Button('跳转').onClick(() => {
          this.stack.pushPath({ name: 'pageOne' });
        });
      }
      .title('Navigation')
      .navDestination(this.Page);
    }
  }

  @Component
  export struct PageOne {
    build() {
      NavDestination() {
        Text('pageOne');
      }.title('pageOne');
    }
  }
  ```
* **方案二**：使用导航控制器NavPathStack的setInterception方法，在入参[NavigationInterception](../harmonyos-references/ts-basic-components-navigation.md#navigationinterception12)中可以设置页面跳转前后的拦截回调。

  以跳转前拦截为例：在页面跳转前打印跳转目标页面的信息。

  ```screen
  @Entry
  @Component
  struct Index1 {
    pathStack: NavPathStack = new NavPathStack();

    aboutToAppear(): void {
      this.pathStack.setInterception({
        willShow: (from: NavDestinationContext | 'navBar', to: NavDestinationContext | 'navBar') => {
          if (typeof from === 'string') {
            let target = to as NavDestinationContext;
            console.info(`from page is navigation home -> ${target.pathInfo.name}`);
          } else if (typeof to === 'string') {
            let target = from as NavDestinationContext;
            console.info(`${target.pathInfo.name} -> to page is navigation home`);
          }
        }
      });
    }

    @Builder
    pageMap() {
      PageOne();
    }

    build() {
      Navigation(this.pathStack) {
        Column({ space: 30 }) {
          Text('PageOne');
          Button('跳转')
            .onClick(() => {
              this.pathStack.pushPathByName('PageOne', null, false);
            });
        };
      }.navDestination(this.pageMap);
    }
  }

  @Component
  struct PageOne {
    pathStack: NavPathStack = new NavPathStack();

    build() {
      NavDestination() {
        Column({ space: 30 }) {
          Text('PageOne');
          Button('跳转')
            .onClick(() => {
              this.pathStack.pop();
            });
        };
      }.title('PageOne')
      .onReady((context: NavDestinationContext) => {
        this.pathStack = context.pathStack;
      });
    }
  }
  ```

## 常见FAQ

Q：无感监听有哪些常见事件？

A：监听滚动事件[uiObserver.on('scrollEvent')](../harmonyos-references/js-apis-arkui-observer.md#uiobserveronscrollevent12)、监听NavDestination组件的状态变化[uiObserver.on('navDestinationUpdate')](../harmonyos-references/js-apis-arkui-observer.md#uiobserveronnavdestinationupdate)、监听TabContent页面的切换事件[uiObserver.on('tabContentUpdate')](../harmonyos-references/js-apis-arkui-observer.md#uiobserverontabcontentupdate12)等。
