---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-390
title: Navigation跳转页面白屏，可能原因是什么
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Navigation跳转页面白屏，可能原因是什么
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:43+08:00
doc_updated_at: 2026-04-27
content_hash: sha256:9f8fc859927f6be4982a32145feae2970148eee40997e8c68f2ba7b171cc055d
---

**可能原因一**

跨模块跳转配置错误。

**解决措施**

路由表配置时，可以根据[系统路由表](../harmonyos-guides/arkts-navigation-cross-package.md#系统路由表)配置步骤一步一步来配置。

* 路由表中的页面，需要配置入口函数Builder，并且需要使用NavDestination组件才能展示页面。

  ```
  1. // Jump Page Entry Function
  2. @Builder
  3. export function pageOneBuilder() {
  4. NavigationJumpToPageWithWhiteScreen();
  5. }

  7. @Entry
  8. @Component
  9. struct NavigationJumpToPageWithWhiteScreen {
  10. pathStack: NavPathStack = new NavPathStack();

  12. build() {
  13. NavDestination() {
  14. // ...
  15. }
  16. .title('PageOne')
  17. .onReady((context: NavDestinationContext) => {
  18. this.pathStack = context.pathStack;
  19. })
  20. }
  21. }
  ```

  [NavigationJumpToPageWithWhiteScreen.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/NavigationJumpToPageWithWhiteScreen.ets#L21-L42)
* HAR/HSP模块可以跳转，可以通过module.json5文件查看type类型是否为“har”或者“shared”，如果是feature则会出现错误。

  ```
  1. "module": {
  2. "name": "feature_splash",
  3. "type": "feature",
  4. // The type needs to be either "har" or "shared"
  ```

  [moduleNavigationJumpToPageWithWhiteScreen.json5](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/moduleNavigationJumpToPageWithWhiteScreen.json5#L21-L24)

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
