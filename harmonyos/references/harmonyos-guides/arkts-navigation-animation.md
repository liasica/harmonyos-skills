---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-navigation-animation
title: Navigation转场动画
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 设置组件导航和页面路由 > 组件导航(Navigation) (推荐) > Navigation转场动画
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e4f9a0a323263e6426d27201181fdd413209149e410c76fe24fc6f21caebf64f
---

[Navigation](../harmonyos-references/ts-basic-components-navigation.md)存在默认转场动画，此外也提供了自定义转场和共享元素转场能力。

## 系统默认转场

系统提供了多种默认转场类型，可以通过[NavDestination.systemTransition](../harmonyos-references/ts-basic-components-navdestination.md#systemtransition14)接口实现，具体示例请参考[设置指定的NavDestination系统转场](../harmonyos-references/ts-basic-components-navdestination.md#示例3设置指定的navdestination系统转场)。

说明

* NavDestination的默认转场动画使用[弹簧曲线](arkts-spring-curve.md)，其时长与物理曲线参数有关，而且不同设备上的默认动画不同，因此默认转场动画时长不可控，不建议与业务耦合，若需要监听动画结束，建议使用[自定义转场](arkts-navigation-animation.md#自定义转场)。
* [Dialog](../harmonyos-references/ts-basic-components-navdestination.md#navdestinationmode枚举说明11)类型的NavDestination默认无转场动画；从API version 13开始，Dialog类型的NavDestination默认存在系统转场动画。

默认转场动画支持关闭，有两种方式：

* 全局关闭。

  Navigation可以通过NavPathStack提供的[disableAnimation](../harmonyos-references/ts-basic-components-navigation.md#disableanimation11)接口，关闭或打开当前Navigation的所有转场动画。

  ```
  1. pageStack: NavPathStack = new NavPathStack();

  3. aboutToAppear(): void {
  4. this.pageStack.disableAnimation(true);
  5. }
  ```

  [PageAnimated.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template1/PageAnimated.ets#L34-L40)
* 单次关闭。

  NavPathStack中提供的[pushPath](../harmonyos-references/ts-basic-components-navigation.md#pushpath10)、[pop](../harmonyos-references/ts-basic-components-navigation.md#pop10)、[replacePath](../harmonyos-references/ts-basic-components-navigation.md#replacepath11)等接口可以设置animated参数，该参数用于设置是否有转场动画。需要单次关闭转场动画，可以将animated置为false，设置后不影响下次转场动画。

## 自定义转场

Navigation提供了两种自定义转场接口：Navigation自定义转场、NavDestination自定义转场。

* Navigation自定义转场动画由[customNavContentTransition](../harmonyos-references/ts-basic-components-navigation.md#customnavcontenttransition11)事件提供，适用于控制Navigation内所有页面的场景，统一转场动画效果。步骤如下，具体示例代码请参考[设置可交互转场动画](../harmonyos-references/ts-basic-components-navigation.md#示例3设置可交互转场动画)。

  1. 实现一个自定义转场动画工具类CustomNavigationUtils，通过一个Map管理各页面的自定义动画对象CustomTransition。页面在创建时注册其自定义转场动画对象，在销毁时取消注册。
  2. 实现一个转场协议对象[NavigationAnimatedTransition](../harmonyos-references/ts-basic-components-navigation.md#navigationanimatedtransition11)。其中，transition属性为自定义转场动画的具体实现，开发者需在此实现自己的转场动画逻辑，系统在转场开始时会调用此方法。timeout属性表示转场结束的超时时间，默认为1000ms。onTransitionEnd为转场结束时的回调。
  3. 调用customNavContentTransition方法并返回实现的转场协议对象，若返回undefined，则使用系统默认转场。
* NavDestination支持自定义转场动画，适用于控制单个页面的转场效果。通过设置[customTransition](../harmonyos-references/ts-basic-components-navdestination.md#customtransition15)属性即可实现单个页面的自定义转场效果。步骤如下，示例代码请参考[设置NavDestination自定义转场](../harmonyos-references/ts-basic-components-navdestination.md#示例2设置navdestination自定义转场)。

  1. 实现[NavDestination的转场代理](../harmonyos-references/ts-basic-components-navdestination.md#navdestinationtransitiondelegate15)，针对不同的堆栈操作类型返回自定义的转场协议对象[NavDestinationTransition](../harmonyos-references/ts-basic-components-navdestination.md#navdestinationtransition15)。其中，event是必填参数，需在此处实现自定义转场动画的逻辑，onTransitionEnd、duration、curve与delay为可选参数，分别对应动画结束后的回调、动画持续时间、动画曲线类型与开始前的延时。如果在转场代理中返回多个转场协议对象，这些动画效果将逐层叠加。
  2. 通过调用NavDestination组件的customTransition属性，并传入上述实现的转场代理，完成自定义转场的设置。

说明

同时使用[customNavContentTransition](../harmonyos-references/ts-basic-components-navigation.md#customnavcontenttransition11)和[customTransition](../harmonyos-references/ts-basic-components-navdestination.md#customtransition15)时，customNavContentTransition优先级更高。

## 共享元素转场

NavDestination之间切换时可以通过[geometryTransition](../harmonyos-references/ts-transition-animation-geometrytransition.md#geometrytransition)实现共享元素转场，示例如下。配置了共享元素转场的页面，同时需要关闭系统默认的转场动画，否则默认动画会与共享元素动画叠加，导致效果异常。

1. 为需要实现共享元素转场的组件添加geometryTransition属性，id参数必须在两个NavDestination之间保持一致。

   ```
   1. // 起始页配置共享元素id
   2. NavDestination() {
   3. Column() {
   4. // ...
   5. // 请将$r('app.media.startIcon')替换为实际资源文件
   6. Image($r('app.media.startIcon'))
   7. .geometryTransition('sharedId')
   8. .width(100)
   9. .height(100)
   10. }
   11. }.title('FromPage')
   ```

   [GeometryTransition.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template1/GeometryTransition.ets#L21-L48)

   ```
   1. // 目的页配置共享元素id
   2. NavDestination() {
   3. Column() {
   4. // 请将$r('app.media.startIcon')替换为实际资源文件
   5. Image($r('app.media.startIcon'))
   6. .geometryTransition('sharedId')
   7. .width(200)
   8. .height(200)
   9. }
   10. }
   11. .title('ToPage')
   ```

   [GeometryTransition.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template1/GeometryTransition.ets#L57-L69)
2. 将页面路由的操作，放到[animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)动画闭包中，配置对应的动画参数以及关闭系统默认的转场。

   ```
   1. NavDestination() {
   2. Column() {
   3. // $r('app.string.ToPage')需要开发者替换为实际的资源文件，资源文件中的value值为“跳转到目的页”

   5. Button($r('app.string.ToPage'))
   6. .width('80%')
   7. .height(40)
   8. .margin(20)
   9. .onClick(() => {
   10. this.getUIContext()?.animateTo({ duration: 1000 }, () => {
   11. this.navPathStack.pushPath({ name: 'ToPage' }, false)
   12. });
   13. })
   14. // ...
   15. }
   16. }.title('FromPage')
   ```

   [GeometryTransition.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template1/GeometryTransition.ets#L23-L47)
