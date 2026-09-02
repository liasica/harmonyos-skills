---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-504
title: 实现Navigation首页和子页面互相跳转时的显隐监听
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 实现Navigation首页和子页面互相跳转时的显隐监听
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:bcdb6081709826b5bdf08d3525496441deff7a3cdcb9bf5234a6a3a0951b0c2d
---

## 问题现象

一个应用的UI页面采用Navigation组件作为根视图，并使用NavPathStack进行页面跳转。在onPageShow事件不支持或不执行的情况下，如何监听Navigation首页和子页面互相跳转的过程中两个页面的显示和隐藏？

问题关键代码如下：

```ts
// Index.ets
@Entry
@Component
struct NavigationPage {
  @Provide('pageInfos') pageInfos: NavPathStack = new NavPathStack();

  // 从子页返回根页面不会触发
  onPageShow(): void {
    console.info('NavigationPage onPageShow');
  }

  build() {
    Navigation(this.pageInfos) {
    };
  }
}
```

```ts
// PageOne.ets
@Entry
@Component
export struct PageOne {
  @Consume('pageInfos') pageInfos: NavPathStack;

  // onPageShow不会被触发
  onPageShow(): void {
    console.info('NavDestination PageOne onPageShow');
  }

  build() {
    NavDestination() {
    };
  }
}
```

## 背景知识

* [onPageShow](../harmonyos-references/ts-custom-component-lifecycle.md#onpageshow)和[onPageHide](../harmonyos-references/ts-custom-component-lifecycle.md#onpagehide)仅在router路由页面每次显示隐藏时触发。其他[自定义组件生命周期](../harmonyos-guides/arkts-page-custom-components-lifecycle.md)无法触发。
* [Navigation](../harmonyos-guides/arkts-navigation-navigation.md)是路由导航的根视图容器，一般作为页面（@Entry）的根容器，[NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)是Navigation子页面的根容器。
* [@ohos.arkui.observer (无感监听)](../harmonyos-references/js-apis-arkui-observer.md)提供UI组件行为变化的无感监听能力。可通过[uiObserver.on('navDestinationSwitch')](../harmonyos-references/js-apis-arkui-observer.md#uiobserveronnavdestinationswitch12)监听Navigation的页面切换事件。

## 解决方案

Navigation组件通常被用作Page页面的根容器，它内部默认包含标题栏、内容区域和工具栏。在内容区域中，默认情况下，首页会展示导航内容（即Navigation的子组件），而子页面则展示NavDestination的子组件。当从首页跳转至子页面时，实际打开的是NavDestination组件，而不是一个router页面，因此不会触发应用页面特有的onPageShow和onPageHide生命周期方法。

* **场景一**：监听NavDestination组件的显示和隐藏。

  可以使用[onShown](../harmonyos-references/ts-basic-components-navdestination.md#onshown10)事件和[onHidden](../harmonyos-references/ts-basic-components-navdestination.md#onhidden10)事件来监听NavDestination组件的显示和隐藏。示例可参考[NavDestination生命周期时序](../harmonyos-references/ts-basic-components-navigation.md#示例8navdestination生命周期时序)。
* **场景二**：监听Navigation首页的显示和隐藏。

  在Navigation不使用[hideNavBar](../harmonyos-references/ts-basic-components-navigation.md#hidenavbar9)隐藏导航栏的场景下，监听Navigation的[onNavBarStateChange](../harmonyos-references/ts-basic-components-navigation.md#onnavbarstatechange9)事件。在回调函数中，如果变量isVisible为true，表明首页正在显示。

  ```screen
  @Entry
  @Component
  struct NavBarStateChangePage {
    pageInfos: NavPathStack = new NavPathStack();

    @Builder
    pageMap() {
      PageB();
    }

    build() {
      Navigation(this.pageInfos) {
        Column() {
          Button('跳转NavDestination页面')
            .onClick(() => {
              this.pageInfos.pushPath({ name: 'PageB' });
            });
        };
      }.navDestination(this.pageMap)
      .onNavBarStateChange((isVisible: boolean) => {
        if (isVisible) {
          console.info('Navigation显示');
        } else {
          console.info('Navigation隐藏');
        }
      });
    }
  }

  @Component
  struct PageB {
    pageInfos: NavPathStack = new NavPathStack();

    build() {
      NavDestination() {
        Button('返回Navigation')
          .onClick(() => {
            this.pageInfos.pop();
          });
      }.onReady((ctx: NavDestinationContext) => {
        this.pageInfos = ctx.pathStack;
      });
    }
  }
  ```

* **场景三**：监听首页和子页的显示和隐藏。

  在首页的aboutToAppear函数中使用无感监听uiObserver.on('navDestinationSwitch')监听页面切换。回调函数的入参为[NavDestinationSwitchInfo](../harmonyos-references/js-apis-arkui-observer.md#navdestinationswitchinfo12)，可以根据from和to的信息判断隐藏和显示的页面。

  ```screen
  import { uiObserver } from '@kit.ArkUI';

  @Entry
  @Component
  struct NavDestinationSwitchPage {
    pageInfos: NavPathStack = new NavPathStack();

    aboutToAppear(): void {
      // 监听navigation页面切换事件
      uiObserver.on('navDestinationSwitch', this.getUIContext(), (switchInfo) => {
        // 可根据from和to判断显隐的页面，类型为NavDestinationInfo表示子页，为NavBar表示Navigation页面
        console.info(`from ${JSON.stringify(switchInfo.from)} -> to ${JSON.stringify(switchInfo.to)}`);
      });
    }

    aboutToDisappear() {
      uiObserver.off('navDestinationSwitch', this.getUIContext()); // 取消监听
    }

    @Builder
    pageMap() {
      PageA();
    }

    build() {
      Navigation(this.pageInfos) {
        Column() {
          Button('跳转NavDestination页面')
            .onClick(() => {
              this.pageInfos.pushPath({ name: 'PageA' });
            });
        };
      }.navDestination(this.pageMap);
    }
  }

  @Component
  struct PageA {
    pageInfos: NavPathStack = new NavPathStack();

    build() {
      NavDestination() {
        Button('返回Navigation')
          .onClick(() => {
            this.pageInfos.pop();
          });
      }.onReady((ctx: NavDestinationContext) => {
        this.pageInfos = ctx.pathStack;
      });
    }
  }
  ```

## 常见FAQ

Q：Navigation子页面A跳转到子页面B后，重新返回页面A，如何监听A页面重新展示了？

A：[onActive](../harmonyos-references/ts-basic-components-navdestination.md#onactive17)在NavDestination处于激活态（处于栈顶可操作，且上层无特殊组件遮挡）时，触发该回调。当重新返回A页面后会触发onActive函数。
