---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-navigation-navdestination
title: Navigation子页面
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 设置组件导航和页面路由 > 组件导航(Navigation) (推荐) > Navigation子页面
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8d1db94106412cbd0fc9e22c0909633e84967e266855b7f17f32180928685a71
---

[NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)是Navigation子页面的根容器，用于承载子页面的特殊属性和生命周期。NavDestination可以配置独立的标题栏、菜单栏与工具栏等属性，使用方法与Navigation一致。NavDestination还支持通过mode属性设置不同的显示模式，以适应不同页面的需求。

## 页面显示类型

NavDestination提供了两种类型。

* 标准类型：

  NavDestination页面默认为标准类型，此时[mode](../harmonyos-references/ts-basic-components-navdestination.md#mode11)属性为[NavDestinationMode.STANDARD](../harmonyos-references/ts-basic-components-navdestination.md#navdestinationmode枚举说明11)。Navigation中只能显示一个标准类型的NavDestination页面。
* 弹窗类型：

  NavDestination设置mode为NavDestinationMode.DIALOG弹窗类型，此时整个NavDestination默认透明显示。弹窗类型的NavDestination显示和消失时不会影响下层标准类型的NavDestination的显示和生命周期，两者可以同时显示。

  ```
  1. // Dialog NavDestination
  2. @Entry
  3. @Component
  4. struct PageDisplayType {
  5. @Provide('NavPathStack') pageStack: NavPathStack = new NavPathStack();

  7. @Builder
  8. PagesMap(name: string) {
  9. if (name == 'DialogPage') {
  10. DialogPage();
  11. }
  12. }

  14. build() {
  15. Navigation(this.pageStack) {
  16. Button('Push DialogPage')
  17. .margin(20)
  18. .width('80%')
  19. .onClick(() => {
  20. this.pageStack.pushPathByName('DialogPage', '');
  21. })
  22. }
  23. .mode(NavigationMode.Stack)
  24. .title('Main')
  25. .navDestination(this.PagesMap)
  26. }
  27. }

  29. @Component
  30. export struct DialogPage {
  31. @Consume('NavPathStack') pageStack: NavPathStack;

  33. build() {
  34. NavDestination() {
  35. Stack({ alignContent: Alignment.Center }) {
  36. Column() {
  37. Text('Dialog NavDestination')
  38. .fontSize(20)
  39. .margin({ bottom: 100 })
  40. Button('Close').onClick(() => {
  41. this.pageStack.pop();
  42. }).width('30%')
  43. }
  44. .justifyContent(FlexAlign.Center)
  45. .backgroundColor(Color.White)
  46. .borderRadius(10)
  47. .height('30%')
  48. .width('80%')
  49. }.height('100%').width('100%')
  50. }
  51. .backgroundColor('rgba(0,0,0,0.5)')
  52. .hideTitleBar(true)
  53. .mode(NavDestinationMode.DIALOG)
  54. }
  55. }
  ```

  [PageDisplayType.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template1/PageDisplayType.ets#L15-L71)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/Tbt7efjgRSacccfTlXuf1g/zh-cn_image_0000002552957682.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233925Z&HW-CC-Expire=86400&HW-CC-Sign=55B6B35D80C5E9C7B4C8437DD1F7848F9263397D03CEF2CA68736218A5095761)

## 页面生命周期

页面生命周期承载在NavDestination组件上，可分为三类：自定义组件生命周期、通用组件生命周期和[NavDestination生命周期](../harmonyos-references/ts-basic-components-navdestination.md#事件)。其中，[aboutToAppear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoappear)和[aboutToDisappear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttodisappear)是自定义组件的生命周期（NavDestination外层包含的自定义组件），[onAppear](../harmonyos-references/ts-universal-events-show-hide.md#onappear)和[onDisAppear](../harmonyos-references/ts-universal-events-show-hide.md#ondisappear)是组件的通用生命周期。剩下的生命周期为NavDestination独有。

生命周期时序如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/iCJEA28eRH6HMHapDjm4Lw/zh-cn_image_0000002583477683.png?HW-CC-KV=V1&HW-CC-Date=20260427T233925Z&HW-CC-Expire=86400&HW-CC-Sign=4970A71E171A3E21CACC17E6C59F7E2F755515B6D91F4767044499903697649F)

* **[aboutToAppear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoappear)**：在创建自定义组件后，执行其build()函数之前执行（NavDestination创建之前），允许在该方法中改变状态变量，更改将在后续执行build()函数中生效。
* **[onWillAppear](../harmonyos-references/ts-basic-components-navdestination.md#onwillappear12)**：NavDestination创建后，挂载到组件树之前执行，在该方法中更改状态变量会在当前帧显示生效。
* **[onAppear](../harmonyos-references/ts-universal-events-show-hide.md#onappear)**：通用生命周期事件，NavDestination组件挂载到组件树时执行。
* **[onWillShow](../harmonyos-references/ts-basic-components-navdestination.md#onwillshow12)**：NavDestination组件布局显示之前执行，此时页面不可见（应用切换到前台不会执行）。
* **[onShown](../harmonyos-references/ts-basic-components-navdestination.md#onshown10)**：NavDestination组件布局显示之后执行，此时页面已完成布局。
* **[onActive](../harmonyos-references/ts-basic-components-navdestination.md#onactive17)**：NavDestination处于激活态（处于栈顶可操作，且上层无特殊组件遮挡）执行。
* **[onWillHide](../harmonyos-references/ts-basic-components-navdestination.md#onwillhide12)**：NavDestination组件执行隐藏之前执行（应用切换到后台不会执行）。
* **[onInactive](../harmonyos-references/ts-basic-components-navdestination.md#oninactive17)**：NavDestination组件处于非激活态（处于非栈顶不可操作，或处于栈顶时上层有特殊组件遮挡）执行。
* **[onHidden](../harmonyos-references/ts-basic-components-navdestination.md#onhidden10)**：NavDestination组件执行隐藏后执行（非栈顶页面push进栈，栈顶页面pop出栈或应用切换到后台）。
* **[onWillDisappear](../harmonyos-references/ts-basic-components-navdestination.md#onwilldisappear12)**：NavDestination组件即将销毁之前执行，如果有转场动画，会在动画前执行（栈顶页面pop出栈）。
* **[onDisAppear](../harmonyos-references/ts-universal-events-show-hide.md#ondisappear)**：通用生命周期事件，NavDestination组件从组件树上卸载销毁时执行。
* **[aboutToDisappear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttodisappear)**：自定义组件析构销毁之前执行，不允许在该方法中改变状态变量。

此外还有两个特殊生命周期：

* **onResult**：从其他NavDestination页面通过pop或者侧滑返回时，将执行当前NavDestination页面的onResult回调。
* **onNewParam**：当之前存在于栈中的NavDestination页面通过[launchMode.MOVE\_TO\_TOP\_SINGLETON](../harmonyos-references/ts-basic-components-navigation.md#launchmode12枚举说明)或[launchMode.POP\_TO\_SINGLETON](../harmonyos-references/ts-basic-components-navigation.md#launchmode12枚举说明)移动到栈顶时，执行该回调。

## 页面监听和查询

在NavDestination子页面内部的自定义组件可以通过全局方法监听或查询到页面的一些状态信息，从而实现组件与页面解耦。

* 页面信息查询：

  自定义组件提供[queryNavDestinationInfo](../harmonyos-references/ts-custom-component-api.md#querynavdestinationinfo)方法，可以在NavDestination内部查询到当前所属页面的信息，返回值为[NavDestinationInfo](../harmonyos-references/js-apis-arkui-observer.md#navdestinationinfo)，若查询不到则返回undefined。

  ```
  1. import { uiObserver } from '@kit.ArkUI';

  3. // NavDestination内的自定义组件
  4. @Component
  5. struct MyComponent {
  6. navDesInfo: uiObserver.NavDestinationInfo | undefined;
  7. context = this.getUIContext().getHostContext();

  9. aboutToAppear() {
  10. this.navDesInfo = this.queryNavDestinationInfo();
  11. }

  13. build() {
  14. // ...
  15. Column() {
  16. // $r('app.string.onPageName')资源文件中的value值为“所属页面Name:”
  17. Text(this.context!.resourceManager.getStringSync($r('app.string.onPageName').id) + `${this.navDesInfo?.name}`)
  18. }.width('100%').height('100%')
  19. // ...
  20. }
  21. }
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/observer/template1/Index.ets#L15-L41)
* 页面状态监听：

  通过[observer.on('navDestinationUpdate')](../harmonyos-references/js-apis-arkui-observer.md#uiobserveronnavdestinationupdate)提供的注册接口可以注册NavDestination生命周期变化的监听。

  也可以通过[observer.on('navDestinationSwitch')](../harmonyos-references/js-apis-arkui-observer.md#uiobserveronnavdestinationswitch12)注册页面切换的状态回调。该回调能在页面发生路由切换时拿到对应的页面信息[NavDestinationSwitchInfo](../harmonyos-references/js-apis-arkui-observer.md#navdestinationswitchinfo12)，并提供了[UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md)和[UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)不同范围的监听。
