---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-865
title: 修改头像后其他页面头像未同步更新
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 修改头像后其他页面头像未同步更新
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8d0bb886f8d23f8c27835f485d6d5ceb631bd80c69b7250c4e21dc5544004582
---

## 问题现象

重新上传修改头像后，应用主页面头像仍保持旧头像。

## 背景知识

* [Navigation](../harmonyos-references/ts-basic-components-navigation.md)组件是路由导航的根视图容器，一般作为Page页面的根容器使用，其内部默认包含了标题栏、内容区和工具栏，其中内容区默认首页显示导航内容（Navigation的子组件）或非首页显示（[NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)的子组件），首页和非首页通过路由进行切换。
* [@system.router](../harmonyos-references/js-apis-system-router.md)通过不同的uri访问不同的页面。**注意接口已经停止维护，建议使用Navigation**。

## 问题定位

根据问题现象可知，页面跳转后，图片未实时更新，需要排查图片可用的更新方式，是否对图片进行更新。

1. **根据跳转过程中，是否刷新对应头像参数。**

   根据日志可知，日志中存在AceNavigation，但是对应日志仅有can't find inner navigation，没有相应跳转信息，说明使用Navigation作为容器容纳了页面，但未实际使用Navigation提供的跳转方式。

   ```txt
   07-18 10:46:25.561   15980-15980   C03922/example.hw...AceNavigation  example.hw.com     I     [(100000:100000:scope)] can't find inner navigation
   ```

   同时，排查日志中的AceRouter可知，跳转使用了router.back。

   ```txt
   07-18 10:53:22.282   64555-64555   C03925/example.hw.../AceRouter  example.hw.com  I     [(100000:100000:scope)] Router back path:
   07-18 10:53:22.282   64555-64555   C03925/example.hw.../AceRouter  example.hw.com  I     [(100000:100000:scope)] Router back start PopPage
   ```

   因此，需排查头像未刷新页面的onPageShow和aboutToAppear，以及组件级onAppear等回调中，是否进行了头像组件内容的刷新。
2. **排查头像参数刷新后，组件UI是否刷新。**

   查看对应头像参数是否被装饰器修饰。

## 分析结论

* 若对应回调中未对头像进行更新，则是跳转过程中，没有头像刷新逻辑。
* 若对应回调中对头像进行更新，则是头像参数使用装饰器存在问题。

## 修改建议

* 针对没有头像刷新逻辑的问题，建议针对头像新建一个自定义组件，在头像自定义组件中的aboutToAppear回调中，添加头像刷新加载逻辑，页面直接使用该组件即可。
* 针对无装饰器问题，建议添加@State或者@Local等，具体参考[状态管理概述](../harmonyos-guides/arkts-state-management-overview.md)。

  **注意** 

  因为当前@system.router已不再维护，建议参考[Router切换Navigation](../harmonyos-guides/arkts-router-to-navigation.md)对路由接口进行切换。当使用Navigation时，路由过程中更新逻辑需在[onShown](../harmonyos-references/ts-basic-components-navdestination.md#onshown10)中实现。
