---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-390
title: Navigation跳转页面白屏，可能原因是什么
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Navigation跳转页面白屏，可能原因是什么
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0721f7f7b88f9c4d51b1093895ee86cd7c8f77167f55baaf4534d910853947ab
---

**可能原因一**

跨模块跳转配置错误。

**解决措施**

路由表配置时，可以根据[系统路由表](../harmonyos-guides/arkts-navigation-cross-package.md#系统路由表)配置步骤一步一步来配置。

* 路由表中的页面，需要配置入口函数Builder，并且需要使用NavDestination组件才能展示页面。

  ```ts
  // Jump Page Entry Function 
  @Builder
  export function pageOneBuilder() {
    NavigationJumpToPageWithWhiteScreen();
  }

  @Entry
  @Component
  struct NavigationJumpToPageWithWhiteScreen {
    pathStack: NavPathStack = new NavPathStack();

    build() {
      NavDestination() {
        // ...
      }
      .title('PageOne')
      .onReady((context: NavDestinationContext) => {
        this.pathStack = context.pathStack;
      })
    }
  }
  ```
* HAR/HSP模块可以跳转，可以通过module.json5文件查看type类型是否为“har”或者“shared”，如果是feature则会出现错误。

  ```json
  "module": {
    "name": "feature_splash",
    "type": "feature",
    // The type needs to be either "har" or "shared"
  ```

  即使配置正确，跳转时仍可能出现白屏。可以尝试清理项目，以恢复正常跳转。

**可能原因二**

NavBar处于隐藏状态。

**解决措施**

通过[hideNavBar](../harmonyos-references/ts-basic-components-navigation.md#hidenavbar9)属性确认当前NavBar是否处于隐藏状态，当设置为true时，NavBar会被隐藏。如果此时页面栈为空，页面表现上会处于白屏。

**可能原因三**

使用的是Previewer调试。

**解决措施**

建议使用模拟器或者真机来调试复杂页面的跳转，Previewer不支持系统路由表跳转。

**其他可能原因**

跳转的Name为空或者不存在时，会跳转白屏。
