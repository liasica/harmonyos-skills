---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-39
title: 如何实现跨模块的页面跳转功能
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 如何实现跨模块的页面跳转功能
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:33+08:00
doc_updated_at: 2026-04-27
content_hash: sha256:833d9a7e08451fd0993a1b003f6c175c3e9e48ea0ba329b21ab8f6f2d6f10753
---

在业务体系庞大或复杂的情况下，会将业务拆分成多个子业务模块，每个子业务模块为一个HAR/HSP。在该场景下，存在从主业务入口跳转到不同子页面模块，或从一个子业务模块A页面跳转到另一个子业务模块B页面的需求。例如，从应用首页跳转到登录子业务模块页面。针对该场景，有以下三种解决方案：

* 方案一：使用router的命名路由接口router.pushNamedRoute()跳转。

  参考地址：[页面路由 (@ohos.router)](../harmonyos-guides/arkts-routing.md)
* 方案二：使用navigation组件跳转。

  以从应用入口模块的页面NavigationPage跳转到Login子业务模块页面LoginPage为例。主要包含以下步骤：

  1. 在Login模块中开发自定义组件LoginPage作为路由跳转目的地，并对外导出。

     ```
     1. @Component
     2. export struct LoginPage {
     3. @Consume('pathStack') pathStack: NavPathStack;
     4. @State message: string = 'Login Page';

     6. build() {
     7. NavDestination() {
     8. Column() {
     9. Text(this.message)
     10. .fontSize(50)
     11. .fontWeight(FontWeight.Bold)
     12. }
     13. .width('100%')
     14. .height('100%')
     15. }
     16. .onBackPressed(() => {
     17. this.pathStack.pop();
     18. return true;
     19. })
     20. }
     21. }
     ```

     [LoginPage.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/PackageStructureKit/LoginModule/src/main/ets/components/LoginPage.ets#L21-L41)
  2. 在Login模块的入口文件Index.ets中导出自定义组件。export { LoginPage } from './src/main/ets/pages/loginPage';
  3. 在入口模块的oh-package.json5文件中添加对Login模块的依赖项。

     ```
     1. {
     2. // ...
     3. "dependencies": {
     4. "@ohos/login": "file:../LoginModule"
     5. }
     6. }
     ```

     [oh-package.json5](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/PackageStructureKit/entry/oh-package.json5#L21-L33)
  4. 入口模块导入Login模块的自定义组件，并添加到Navigation组件的路由表中。

     ```
     1. // Import a custom component of the Login module
     2. import { LoginPage } from '@ohos/login';

     4. @Entry
     5. @Component
     6. struct NavigationPage {
     7. @Provide('pathStack') pathStack: NavPathStack = new NavPathStack();

     9. @Builder
     10. pageMap(name: string) {
     11. if (name === 'loginPage') {
     12. LoginPage()
     13. }
     14. }

     16. build() {
     17. Navigation(this.pathStack) {
     18. Button('jump to login page')
     19. .onClick(() => {
     20. // The second parameter of NavPathInfo is a custom parameter that can be used for message transfer
     21. let pathInfo: NavPathInfo = new NavPathInfo('loginPage', new Object());
     22. this.pathStack.pushDestination(pathInfo, true);
     23. })
     24. }
     25. .navDestination(this.pageMap)
     26. }
     27. }
     ```

     [CrossModulePageJump.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/PackageStructureKit/entry/src/main/ets/pages/CrossModulePageJump.ets#L22-L48)
* 方案三：使用基于navigation组件的自定义路由框架跳转。

  方案二虽然可以实现跨模块跳转的功能，但当模块间跳转需求增多，各个模块间将存在非常复杂的依赖关系，甚至会导致多个HAR/HSP间循环依赖。为了解决模块间的强耦合关系，并且提升页面加载性能，推荐[跨包路由](../harmonyos-guides/arkts-router-to-navigation.md#跨包路由)。
