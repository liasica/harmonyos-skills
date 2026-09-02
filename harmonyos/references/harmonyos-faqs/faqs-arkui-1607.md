---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1607
title: 如何解决自定义组件中的onPageShow回调不生效问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何解决自定义组件中的onPageShow回调不生效问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:20+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4f991db5e7fadc32912499735118d89b397fc7320b22ebfcab425ef25f6042f3
---

## 问题现象

进入页面时，自定义组件中设置的onPageShow回调没有生效。

问题代码示例参考如下：

* SplashPage页面：

  ```ts
  @Component
  export struct SplashPage {
    onPageShow() {
      console.info(`onPageShow`);
    }

    build() {
      Text('SplashPage')
        .fontSize(50)
        .textAlign(TextAlign.Center)
        .width('100%')
        .height('100%');
    }
  }
  ```

* Index页面：

  ```ts
  import { SplashPage } from './SplashPage'

  @Entry
  @Component
  struct Index {
    build() {
      Column() {
        SplashPage()
      }
    }
  }
  ```

## 背景知识

* [onPageShow](../harmonyos-references/ts-custom-component-lifecycle.md#onpageshow)在router路由页面（即[@Entry](../harmonyos-guides/arkts-create-custom-components.md#entry)装饰的自定义组件）每次显示时触发一次，包括路由跳转、应用进入前台等场景。
* [aboutToAppear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoappear)函数在创建自定义组件的新实例后，在执行其build()函数之前执行。允许在aboutToAppear函数中改变状态变量，更改将在后续执行build()函数中生效。实现自定义布局的自定义组件的aboutToAppear生命周期在布局过程中触发。

## 解决方案

由背景知识可知，onPageShow回调需要在router路由页面（即@Entry装饰的自定义组件）每次显示时的场景下才会触发，而在问题代码中，并未涉及路由跳转等场景，而且直接调用子组件进行显示，因此onPageShow回调不生效。建议使用aboutToAppear回调。

SplashPage页面：

```ts
@Component
export struct SplashPage {

  aboutToAppear(): void {
    console.info(`aboutToAppear`);
  }

  build() {
    Text('SplashPage')
      .fontSize(50)
      .textAlign(TextAlign.Center)
      .width('100%')
      .height('100%');
  }
}
```

Index页面：

```ts
import { SplashPage } from './SplashPage';

@Entry
@Component
struct Index {
  build() {
    Column() {
      SplashPage();
    };
  }
}
```

## 常见FAQ

Q：如果从后面一个界面使用router.back(1, { info: '来自Home页'})携带参数返回，那么不在子组件中使用onPageShow时应该如何获取参数？

A：可以在父组件的onPageShow获取参数，然后使用[@Provide和@Consume](../harmonyos-guides/arkts-provide-and-consume.md)传递给子组件。

Q：在启动页中，onPageShow回调会执行两次是什么原因？

A：启动页中onPageShow执行两次有以下几种情况导致：

1. Navigation组件生命周期冲突：

   若应用启动时存在多个共享NavPathStack的Navigation组件（例如闪屏页和首页），可能导致生命周期回调重复触发。
2. Web组件重复加载：

   若启动页中包含Web组件，并在[onPageBegin](../harmonyos-references/arkts-basic-components-web-events.md#onpagebegin)回调中调用了[setCustomUserAgent](../harmonyos-references/ohos-atomicservice-atomicserviceweb.md#setcustomuseragent)等触发页面重载的操作，会导致Web生命周期重复执行。此时需将设置逻辑提前到[onControllerAttached](../harmonyos-references/arkts-basic-components-web-events.md#oncontrollerattached10)中，并确保在[loadUrl](../harmonyos-references/ohos-atomicservice-atomicserviceweb.md#loadurl)前完成配置。
3. 页面装饰器与路由机制冲突：

   @Entry装饰器误用：只有被@Entry装饰的组件才能触发onPageShow，但若页面通过NavDestination定义且已包含路由机制，则需使用[onShown](../harmonyos-references/ts-basic-components-navdestination.md#onshown10)替代onPageShow。此时若错误添加@Entry可能导致生命周期混乱。

Q：页面A使用router路由跳转页面并传参给页面B，为什么页面B在onPageShow方法中无法接收到参数导致组件数据渲染失败？

A：onPageShow回调是在自定义组件的build()函数执行之后触发的。相比之下，aboutToAppear函数则是在创建自定义组件的新实例后，在执行其build()函数之前执行。如果需要在组件显示前进行一些设置或初始化操作，应该在aboutToAppear中实现。
