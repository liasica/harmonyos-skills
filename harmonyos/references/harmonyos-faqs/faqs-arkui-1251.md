---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1251
title: 右滑时，页面会反复自动跳转
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 右滑时，页面会反复自动跳转
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7b0305ddc9c512af4de9256563ea1dabf1a4d5b91f831709b4636c16d02953a0
---

## 问题现象

页面在右滑返回后会立即跳转回前一个页面，然后会再一次返回，如此往复导致页面之间持续自动切换。

## 背景知识

* [router（不推荐）](../harmonyos-guides/arkts-routing.md)：页面路由指在应用程序中实现不同页面之间的跳转和数据传递。router模块通过不同的url地址，可以方便地进行页面路由，轻松地访问不同的页面。（Navigation具有更强的功能和自定义能力，推荐使用该组件作为应用的路由框架。）
* [自定义组件的生命周期](../harmonyos-guides/arkts-page-custom-components-lifecycle.md)：自定义组件的生命周期是指其从创建、渲染、更新到销毁过程中，所经历的一系列由框架自动调用的钩子函数和状态变化阶段。
* [Navigation组件导航](../harmonyos-guides/arkts-navigation-navigation.md)：主要用于实现页面间以及组件内部的页面跳转，支持在不同组件间传递跳转参数，提供灵活的跳转栈操作，从而更便捷地实现对不同页面的访问和复用。

## 问题定位

1. 排查代码中的页面跳转逻辑是否设置合理。

   检查中转页跳转至二级页面的逻辑是否具备幂等性（幂等性是指接口可重复调用，在调用方多次调用的情况下，接口最终得到的结果是一致的）或跳转标记，避免在返回时重复触发跳转。
2. 排查代码中页面生命周期函数（如onResume/onPageShow）中是否实现了自动跳转逻辑。

   确认中转页在resume时是否无条件执行跳转，是否缺少“是否首次进入”判断。
3. 排查日志中是否存在关键字can't find inner navigation。

   若出现相关日志，可能表明页面导航栈异常或页面未正确注册，结合录屏可定位跳转异常发生点。

再根据日志及录屏分析，（日志打印can't find inner navigation，录屏返回时跳转到中转页。）用户在搜索了某个关键词后点入了一个二级页面并进行右滑返回，而该二级页面通过中转页跳转，致使右滑返回到了中转页触发了跳转逻辑又跳转回了二级页面。对照实验直接搜索一级页面或者无需跳转的二级页面则未触发此问题。

## 分析结论

* 页面跳转是基于栈模型的，默认使用router.push()留下了跳转轨迹。
* 中转页面带跳转逻辑且页面未被销毁，导致它的生命周期函数重复触发。

## 修改建议

推荐使用Navigation + NavPathStack的方式进行页面管理，直接把返回页设定回搜索主页，或是在中转页中设置一次性跳转标志，避免循环跳转。

```ts
@Component
struct LaunchPage {
  pageStack: NavPathStack = new NavPathStack();
  @State hasRedirected: boolean = false;

  build() {
    Navigation(this.pageStack) {
      Column() {
        Text('中转页，准备跳转...')
      }
    }
    .onAppear(() => {
      // 自动跳转，仅执行一次
      if (!this.hasRedirected) {
        this.hasRedirected = true;
        this.pageStack.pushPathByName('TargetPage',null);
      }
    })
  }
}
```

```ts
@Component
struct TargetPage {
  @State pageStack: NavPathStack = new NavPathStack();

  build() {
    NavDestination() {
      Column() {
        Text('目标页')
          .fontSize(24)
          .margin(20)
      }
    }
    .onReady((ctx: NavDestinationContext) => {
      this.pageStack = ctx.pathStack;
    })
  }
}
```

```ts
@Entry
struct LaunchPageAndTargetPage{
  build() {
    Column() {
      LaunchPage()
      TargetPage()
    }
  }
}
```
