---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-hmrouter
title: 基于HMRouter的页面跳转
breadcrumb: 最佳实践 > 手势与导航 > 基于HMRouter的页面跳转
category: best-practices
scraped_at: 2026-04-28T08:19:56+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:f3a522257c3d7a481be2965a609e6a793c7e3018f24b0133feb115e283ac9dcc
---

## 概述

HMRouter是HarmonyOS上页面跳转的场景解决方案，主要解决页面间相互跳转的问题，开发者可以参考[HMRouter使用说明](https://gitcode.com/harmonyos_samples/HMRouter#hmrouter使用说明)进行安装配置与快速上手，本文主要以实际开发中的各项场景为例，介绍HMRouter路由框架的使用。HMRouter路由框架提供了下列功能特性：

* 使用自定义注解实现路由跳转。
* 支持HAR/HSP。
* 支持路由拦截、路由生命周期。
* 简化自定义动画配置：配置全局动画，单独指定某个页面的切换动画。
* 支持不同的页面类型：单例页面、Dialog页面。

该框架底层对Navigation相关能力进行了封装，帮助开发者减少对Navigation相关细节内容的关注、提高开发效率，同时该框架对页面跳转能力进行了增强，例如其中的路由拦截、单例页面等。下文以页面跳转、弹窗提示、转场动效、数据加载、维测场景为切入点，介绍HMRouter路由框架的使用。

## 页面跳转场景

### 页面跳转与返回

HMRouter提供了基于自定义注解的页面跳转与返回功能，使用步骤如下：

1. 为需要跳转的页面添加@HMRouter注解，并配置其中的pageUrl参数，例如此处配置为ProductContent。

   ```
   1. @HMRouter({ pageUrl: 'ProductContent' })
   2. @Component
   3. export struct ProductContent {
   4. // ...
   5. @State param: ParamsType | null = null;

   7. aboutToAppear(): void {
   8. this.param = HMRouterMgr.getCurrentParam() as ParamsType;
   9. }

   11. // ...
   12. }
   ```

   [ProductContent.ets](https://gitcode.com/harmonyos_samples/HMRouter/blob/master/entry/src/main/ets/component/product/ProductContent.ets#L28-L69)
2. 在需要进行页面跳转的位置，使用HMRouterMgr提供的to方法进行页面跳转，在参数中配置目标页面的页面地址，如需传参可配置withParam参数。此外，也可以配置页面栈唯一标识navigationId，当使用多个HMNavigation时建议开发者手动指定navigationId，当使用单个HMNavigation时，开发者可以不传递navigationId参数，系统会默认处理。onResult参数可用于配置当从其他页面返回到当前页面时的回调函数，在回调函数内可以通过参数的srcPageInfo.name属性获取由哪个页面跳转到当前页，还可以通过参数的result属性获取返回当前页面时携带的参数。

   ```
   1. HMRouterMgr.to('ProductContent')
   2. .withNavigation('mainNavigationId')
   3. .withParam({ a: 1, b: 2 })
   4. .onResult((popInfo: HMPopInfo) => {
   5. const pageName = popInfo.srcPageInfo.name;
   6. const params = popInfo.result;
   7. console.log(`page name is ${pageName}, params is ${JSON.stringify(params)}`);
   8. })
   9. .pushAsync()
   ```

   [HomeContent.ets](https://gitcode.com/harmonyos_samples/HMRouter/blob/master/entry/src/main/ets/component/home/HomeContent.ets#L257-L265)
3. 在跳转的目标页面使用HMRouterMgr.getCurrentParam()获取到传递的页面参数。

   ```
   1. @Component
   2. export struct ProductContent {
   3. // ...
   4. @State param: ParamsType | null = null;

   6. aboutToAppear(): void {
   7. this.param = HMRouterMgr.getCurrentParam() as ParamsType;
   8. }

   10. // ...
   11. }
   ```

   [ProductContent.ets](https://gitcode.com/harmonyos_samples/HMRouter/blob/master/entry/src/main/ets/component/product/elements/ProductContent.ets#L7-L22)
4. 如需使用页面返回功能，在对应的业务逻辑位置使用HMRouterMgr提供的pop方法实现页面返回，同样的pop方法支持传入navigationId，同时HMRouter还支持在返回时通过配置param参数向其所返回的页面传递参数。

   ```
   1. HMRouterMgr.pop({ navigationId: 'mainNavigationId', param: this.param })
   ```

   [segment1.ets](https://gitcode.com/HarmonyOS_Samples/HMRouter/blob/master/entry/src/main/ets/segment/segment1.ets#L33-L33)

### 多次页面跳转，返回指定页面

当页面跳转路径如HomePage->PageA->PageB->PageC，开发者希望在PageC的页面逻辑中直接返回到HomePage并携带参数，开发者仅需使用HMRouterMgr提供的to方法，并传入需要返回的目标页面的地址以及携带的参数，即可直接带参返回到指定页面。

```
1. HMRouterMgr.to('MainPage')
2. .withNavigation('mainNavigationId')
3. .withParam(0)
4. .pushAsync()
```

[PaySuccessPageComponent.ets](https://gitcode.com/harmonyos_samples/HMRouter/blob/master/entry/src/main/ets/component/pay/PaySuccessPageComponent.ets#L94-L97)

**图1** 返回指定页面示意图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/fABt8azrQgCyzytINCrRTA/zh-cn_image_0000002505304640.png?HW-CC-KV=V1&HW-CC-Date=20260428T001954Z&HW-CC-Expire=86400&HW-CC-Sign=286AFD781CDE7F363CBA477C751E0C6115425137979524A8991E40CABA5C89A4 "点击放大")

### 应用未登录，点击跳转登录页的校验场景

应用中经常会有当用户未登录应用时，点击某些应用内容会自动跳转到登录页面的场景，在使用HMRouter对此场景进行实现时，可以采用以下步骤：

1. 定义拦截器类LoginCheckInterceptor实现IHMInterceptor接口。
2. 为定义的拦截器类添加@HMInterceptor注解，通过interceptorName配置拦截器名称LoginCheckInterceptor。
3. 实现IHMInterceptor的intercept异步拦截器方法，在该方法中根据当前的登录状态来控制页面跳转的目标。
   1. 当用户已登录，通过执行chain.onContinue()，正常执行后续页面跳转逻辑。
   2. 当用户未登录，通过Toast弹窗向用户提示登录，然后跳转到登录页面，最后通过执行chain.onIntercept()来拦截此次跳转请求。

      ```
      1. @HMInterceptor({ interceptorName: 'LoginCheckInterceptor' })
      2. export class LoginCheckInterceptor implements IHMInterceptor {
      3. async intercept(chain: IHMInterceptorChain): Promise<void> {
      4. const info = chain.getRouterInfo();
      5. const context = chain.getContext();
      6. // ...
      7. if (!!AppStorage.get('isLogin')) {
      8. await chain.onContinue()
      9. } else {
      10. info.context.getPromptAction().showToast({ message: '请先登录' });
      11. HMRouterMgr.push({
      12. pageUrl: 'loginPage',
      13. skipAllInterceptor: true
      14. });
      15. await chain.onIntercept();
      16. }
      17. // ...
      18. }
      19. }
      ```

      [LoginCheckInterceptor.ets](https://gitcode.com/harmonyos_samples/HMRouter/blob/master/entry/src/main/ets/interceptor/LoginCheckInterceptor.ets#L25-L60)
4. 在需要进行拦截的页面中配置@HMRouter的interceptors参数即可，由于一个页面可以配置多个拦截器，所以需要将关联的拦截器名称封装为一个数组进行传入。

运行效果如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/j1vwVnTBQyuNCnloeRUG6w/zh-cn_image_0000002229450657.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001954Z&HW-CC-Expire=86400&HW-CC-Sign=4FEC42D0A43A315831C2B08BD7D9EF70B010E3AD8FE6CBF54D358BCE45BE4FEB "点击放大")

### 实现单例页面的跳转

当应用中存在初始化加载资源消耗大且有复用需求的页面时，就可以使用单例页面。典型的业务场景如视频类应用中的视频播放页面，此类页面通常需要加载视频解码器资源并对其初始化，且该页面在视频类应用中会频繁出现。实现上开发者只需要配置@HMRouter注解参数中的singleton参数为true即可。

```
1. @HMRouter({
2. pageUrl: 'liveHome',
3. singleton: true,
4. animator: 'liveInteractiveAnimator',
5. lifecycle: 'liveHomeLifecycle'
6. })
7. @Component
8. export struct LiveHome {
9. // ...
10. }
```

[LiveHome.ets](https://gitcode.com/harmonyos_samples/HMRouter/blob/master/entry/src/main/ets/component/live/LiveHome.ets#L162-L198)

## 弹窗提示场景

### 实现弹窗类型的页面

在HMRouter路由框架中，开发者只需要设置@HMRouter注解的dialog配置为true即可将当前页面作为弹窗使用。

```
1. @HMRouter({
2. pageUrl: PageConstant.PRIVACY_DIALOG_DETAIL,
3. dialog: true,
4. // ...
5. })
6. @Component
7. export struct PrivacyDialogDetail {
8. // ...
9. }
```

[PrivacyDialogDetail.ets](https://gitcode.com/HarmonyOS_Samples/HMRouter/blob/master/entry/src/main/ets/component/privacy/PrivacyDialogDetail.ets#L33-L127)

### 返回时弹窗，提示用户是否确认返回

当从某些页面返回时，应用希望通过弹窗方式让用户确认是否要执行返回操作，例如在订单支付页面中用户执行返回操作时，通常会弹窗提示用户是否确认退出，当用户点击确认后才会执行页面退出逻辑，此场景下就可以考虑使用弹窗类型页面加上自定义生命周期来实现。操作步骤如下：

1. 开发者首先需要根据自己的业务需求，来进行自定义弹窗的开发。

   ```
   1. @HMRouter({ pageUrl: 'PayCancel', dialog: true,animator:'PayCancelDialog' })
   2. @Component
   3. export struct PayCancel {
   4. // ...
   5. build() {
   6. Stack({ alignContent: Alignment.Center }) {
   7. ConfirmDialog({
   8. title: '取消订单',
   9. content: '您确认要取消此订单吗?',
   10. leftButtonName: '再看看',
   11. rightButtonName: '取消订单',
   12. leftButtonFunc: () => {
   13. HMRouterMgr.popAsync({
   14. navigationId: this.queryNavigationInfo()?.navigationId
   15. });
   16. },
   17. rightButtonFunc: () => {
   18. // ...
   19. }
   20. });
   21. }
   22. .width('100%')
   23. .height('100%')
   24. .position({
   25. x: '50%',
   26. y: '50%'
   27. })
   28. .markAnchor({
   29. x: '50%',
   30. y: '50%'
   31. });
   32. }
   33. }
   ```

   [PayCancel.ets](https://gitcode.com/harmonyos_samples/HMRouter/blob/master/entry/src/main/ets/component/pay/PayCancel.ets#L61-L104)
2. 定义ExitPayLifecycle类来实现IHMLifecycle接口，为ExitPayLifecycle加上@HMLifecycle注解，传入生命周期名称ExitPayLifecycle，在类的内部，重写onBackPressed回调函数，当用户执行返回操作时，该回调函数触发，弹出刚刚定义的PayCancel弹窗。

   ```
   1. @HMLifecycle({ lifecycleName: 'ExitPayLifecycle' })
   2. export class ExitPayLifecycle implements IHMLifecycle {
   3. model: ObservedModel = new ObservedModel();

   5. onBackPressed(): boolean {
   6. HMRouterMgr.to('PayCancel')
   7. .withParam(this.model.pageUrl)
   8. .pushAsync()
   9. return true;
   10. }
   11. }
   ```

   [PayDialogContent.ets](https://gitcode.com/harmonyos_samples/HMRouter/blob/master/entry/src/main/ets/component/pay/PayDialogContent.ets#L169-L180)
3. 将定义的生命周期与支付页面绑定，只需要将刚刚定义的生命周期传入对应组件@HMRouter注解的lifecycle参数即可。

   ```
   1. @HMRouter({
   2. pageUrl: 'PayDialogContent',
   3. dialog: true,
   4. lifecycle: 'ExitPayDialog',
   5. interceptors: ['LoginCheckInterceptor']
   6. })
   7. @Component
   8. export struct PayDialogContent {
   9. // ...
   10. }
   ```

   [PayDialogContent.ets](https://gitcode.com/harmonyos_samples/HMRouter/blob/master/entry/src/main/ets/component/pay/PayDialogContent.ets#L78-L152)

运行效果如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/cAraqQvAQ2uKOHmKqSQG8w/zh-cn_image_0000002193850796.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001954Z&HW-CC-Expire=86400&HW-CC-Sign=06A354C9BCB8825EEF395AF6042C10DB510E5DB83876407FFE5E9F0B90FB2D60 "点击放大")

### 首页两次返回退出应用

该场景下用户第一次触发应用返回退出时向用户提示“再次返回退出”，第二次用户触发返回操作时应用真正退出。实现上可参考以下步骤：

1. 定义一个生命周期类ExitAppLifecycle实现IHMLifecycle接口。
2. 使用@HMLifecycle注解传入生命周期名称参数lifecycleName为ExitAppLifecycle。
3. 重写其中的onBackPressed方法（此处是由于上述业务场景需要，实际开发中根据实际业务场景按需重写方法），通过判断上次返回操作与当前返回操作的时间间隔，按如下逻辑处理：
   1. 当两次返回操作的时间间隔大于设置值时（此处为1000ms），重新弹窗对用户进行提示，此处返回true，表示不执行默认返回逻辑。
   2. 当两次返回操作的时间间隔小于设置值时（此处为1000ms），返回为false表示执行默认返回逻辑，退出应用。

      ```
      1. @HMLifecycle({ lifecycleName: 'ExitAppLifecycle' })
      2. export class ExitAppLifecycle implements IHMLifecycle {
      3. private lastTime: number = 0;

      5. onBackPressed(ctx: HMLifecycleContext): boolean {
      6. let time = new Date().getTime();
      7. if (time - this.lastTime > 1000) {
      8. this.lastTime = time;
      9. ctx.uiContext.getPromptAction().showToast({
      10. message: '再次返回退出应用',
      11. duration: 1000
      12. });
      13. return true;
      14. } else {
      15. return false;
      16. }
      17. }
      18. }
      ```

      [ExitAppLifecycle.ets](https://gitcode.com/harmonyos_samples/HMRouter/blob/master/entry/src/main/ets/lifecycle/ExitAppLifecycle.ets#L24-L42)
4. 将定义好的生命周期类与页面进行关联，开发者只需在@HMRouter注解中配置lifecycle为要关联的生命周期名称即可。

运行效果如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/jRw7XXayRKa0GgOpf9HPFw/zh-cn_image_0000002193850804.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001954Z&HW-CC-Expire=86400&HW-CC-Sign=070F1F36EA08A28257CF96D1BE282FBB587FB95B2250F9BE04D0205582DCE028 "点击放大")

## 转场动效场景

### 全局自定义转场动效

* 定义全局页面转场效果。开发者只需要创建出IHMAnimator.Effect实例，在参数中按照业务需求对动画方向direction，透明度opacity，横纵方向页面缩放效果scale进行配置即可。

  ```
  1. const globalPageTransitionEffect: IHMAnimator.Effect = new IHMAnimator.Effect({
  2. direction: IHMAnimator.Direction.BOTTOM_TO_TOP,
  3. opacity: { opacity: 0.5 },
  4. scale: { x: 0.5, y: 0.2 }
  5. })
  ```

  [DialogAnimator.ets](https://gitcode.com/harmonyos_samples/HMRouter/blob/master/entry/src/main/ets/component/live/DialogAnimator.ets#L24-L29)

  定义完成后，只需要将实例传入HMNavigation组件的dialogAnimator参数即可。

  ```
  1. HMNavigation({
  2. navigationId: 'mainNavigationId', homePageUrl: 'HomeContent', options: {
  3. dialogAnimator: globalPageTransitionEffect,
  4. }
  5. })
  ```

  [DialogAnimator.ets](https://gitcode.com/harmonyos_samples/HMRouter/blob/master/entry/src/main/ets/component/live/DialogAnimator.ets#L38-L42)
* 定义全局弹窗效果。同样的，开发者也只需要按照业务需求创建出对应的IHMAnimator.Effect实例，代码示例如下。

  ```
  1. const globalPageTransitionEffect: IHMAnimator.Effect = new IHMAnimator.Effect({
  2. direction: IHMAnimator.Direction.BOTTOM_TO_TOP,
  3. opacity: { opacity: 0.5 },
  4. scale: { x: 0.5, y: 0.2 }
  5. })
  ```

  [DialogAnimator.ets](https://gitcode.com/harmonyos_samples/HMRouter/blob/master/entry/src/main/ets/component/live/DialogAnimator.ets#L24-L29)

  将创建好的实例作为dialogAnimator的参数进行传入即可。

  ```
  1. HMNavigation({
  2. navigationId: 'mainNavigationId', homePageUrl: 'HomeContent', options: {
  3. dialogAnimator: globalPageTransitionEffect,
  4. }
  5. })
  ```

  [DialogAnimator.ets](https://gitcode.com/harmonyos_samples/HMRouter/blob/master/entry/src/main/ets/component/live/DialogAnimator.ets#L38-L42)

### 特定页面设置自定义转场

开发者可以自定义动画类并实现IHMAnimator接口中的effect方法，该方法会将页面进出场的效果对象enterHandle与exitHandle作为参数传入，可通过参数对象上的start、finish方法，设置对应效果的起止状态，支持设置的常用属性还有：

* curve：设置动画速度曲线，支持通过Curve枚举传入值，默认Curve.EaseInOut。
* duration：动画持续时长，单位ms。

以下代码示例表示入场时由屏幕底部以线性速度向屏幕顶部运动，入场动画持续时长为400ms。出场时从屏幕顶部以线性速度向屏幕底部运动，出场动画持续时长也为400ms。

```
1. @HMAnimator({ animatorName: 'CustomAnimator' })
2. export class CustomAnimator implements IHMAnimator {
3. effect(enterHandle: HMAnimatorHandle, exitHandle: HMAnimatorHandle): void {
4. // to animator
5. enterHandle.start((modifier: AttributeUpdater<NavDestinationAttribute>) => {
6. modifier.attribute?.translate({ y: '100%' }).scale({ x: 0.7 }).opacity(0.3)
7. }).finish((modifier: AttributeUpdater<NavDestinationAttribute>) => {
8. modifier.attribute?.translate({ y: '0' }).scale({ x: 1 }).opacity(1)
9. })
10. enterHandle.duration = 400;
11. enterHandle.curve = Curve.Linear;

13. // cut animator
14. exitHandle.start((modifier: AttributeUpdater<NavDestinationAttribute>) => {
15. modifier.attribute?.translate({ y: '0' }).scale({ x: 1 }).opacity(1)
16. }).finish((modifier: AttributeUpdater<NavDestinationAttribute>) => {
17. modifier.attribute?.translate({ y: '100%' }).scale({ x: 0.7 }).opacity(0.3)
18. })
19. exitHandle.duration = 400;
20. enterHandle.curve = Curve.Linear;
21. }
22. }
```

[CustomCutToAnimator.ets](https://gitcode.com/harmonyos_samples/HMRouter/blob/master/entry/src/main/ets/animation/CustomCutToAnimator.ets#L29-L52)

自定义动画定义完成后，其实例可以作为新版链式API跳转方法的animator参数进行传入。

```
1. HMRouterMgr.to('ProductContent')
2. .withAnimator(new CustomAnimator())
3. .pushAsync()
```

[CustomCutToAnimator.ets](https://gitcode.com/harmonyos_samples/HMRouter/blob/master/entry/src/main/ets/animation/CustomCutToAnimator.ets#L58-L60)

运行效果如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/DTrRSd6USDGWjl-N1T1pYA/zh-cn_image_0000002194010372.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001954Z&HW-CC-Expire=86400&HW-CC-Sign=835C7105DF15C0F1F82DB8C4AA4EECDE89DD3A532765841A8ACF082A7B08A9F6 "点击放大")

### 根据条件呈现不同转场动效

相同的页面可能在不同情况下出现不同的转场效果，常见的有短视频播放时的评论页面弹出时的转场：

* 当短视频横屏播放时，评论页面由右至左弹出，视频向左缩放。
* 当短视频竖屏播放时，评论页面由下至上弹出，视频向上缩放。

此处以评论区组件打开的视角进行动画定义，定义竖屏播放时评论区进出场动画如下：

```
1. @HMAnimator({ animatorName: 'myAnimator1' })
2. export class MyAnimator1 implements IHMAnimator {
3. effect(enterHandle: HMAnimatorHandle, exitHandle: HMAnimatorHandle): void {
4. enterHandle.start((modifier: AttributeUpdater<NavDestinationAttribute>) => {
5. modifier.attribute?.translate({ y: '100%' })
6. }).finish((modifier: AttributeUpdater<NavDestinationAttribute>) => {
7. modifier.attribute?.translate({ y: '0' })
8. })

10. exitHandle.start((modifier: AttributeUpdater<NavDestinationAttribute>) => {
11. modifier.attribute?.translate({ y: '0' })
12. }).finish((modifier: AttributeUpdater<NavDestinationAttribute>) => {
13. modifier.attribute?.translate({ y: '100%' })
14. })
15. }
16. }
```

[CustomDifferentTransition.ets](https://gitcode.com/harmonyos_samples/HMRouter/blob/master/entry/src/main/ets/animation/CustomDifferentTransition.ets#L29-L45)

定义短视频横屏播放时评论区进出场动画如下：

```
1. @HMAnimator({ animatorName: 'myAnimator2' })
2. export class MyAnimator2 implements IHMAnimator {
3. effect(enterHandle: HMAnimatorHandle, exitHandle: HMAnimatorHandle): void {
4. enterHandle.start((modifier: AttributeUpdater<NavDestinationAttribute>) => {
5. modifier.attribute?.translate({ x: '100%', y: '0' })
6. }).finish((modifier: AttributeUpdater<NavDestinationAttribute>) => {
7. modifier.attribute?.translate({ x: 0 })
8. })
9. enterHandle.duration = 500;

11. exitHandle.start((modifier: AttributeUpdater<NavDestinationAttribute>) => {
12. modifier.attribute?.translate({ x: '0' })
13. }).finish((modifier: AttributeUpdater<NavDestinationAttribute>) => {
14. modifier.attribute?.translate({ x: '100%' })
15. })
16. exitHandle.duration = 500;
17. }
18. }
```

[CustomDifferentTransition.ets](https://gitcode.com/harmonyos_samples/HMRouter/blob/master/entry/src/main/ets/animation/CustomDifferentTransition.ets#L49-L67)

最后根据条件选择不同的动效，例如此处根据视频播放方向是否为横向，在页面跳转时使用不同的animator值。

```
1. @Component
2. export struct CommentInput {
3. // ...

5. build() {
6. Row() {
7. Image($r('app.media.icon_comments'))
8. .width(24)
9. .height(24)
10. .margin({ right: 16 })
11. .onClick(() => {
12. if (this.isLandscape) {
13. HMRouterMgr.to('liveComments')
14. .withNavigation(this.queryNavigationInfo()?.navigationId)
15. .withParam({commentRenderNode: ''})
16. .withAnimator(new MyAnimator2())
17. .onResult((paramInfo: PopInfo)=>{
18. this.videoWidth = '100%';
19. })
20. .pushAsync()
21. this.videoWidth = '50%';
22. } else {
23. HMRouterMgr.to('liveComments')
24. .withNavigation(this.queryNavigationInfo()?.navigationId)
25. .withParam({commentRenderNode: ''})
26. .withAnimator(new MyAnimator1())
27. .onResult((paramInfo: PopInfo)=>{
28. this.videoHeight = '100%';
29. })
30. .pushAsync()
31. this.videoHeight = '30%'
32. }
33. });
34. }
35. }
36. }
```

[CustomDifferentTransition.ets](https://gitcode.com/harmonyos_samples/HMRouter/blob/master/entry/src/main/ets/animation/CustomDifferentTransition.ets#L71-L112)

运行效果如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/ZQqem70SSoW8Le8mMImdKA/zh-cn_image_0000002194010392.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001954Z&HW-CC-Expire=86400&HW-CC-Sign=3346955FE1FF41133B492B0170A066AE07270122BE645F9A949C82B1785927C1)

### 交互式转场

当应用中有页面的进出场效果与用户手势操作同步的诉求时，即当用户手指在屏幕上移动时，页面跟随用户手势移动，可以参考以下实现，通过IHMAnimator的interactive函数控制动画播放进度，在actionStart中判断向右移动执行页面返回操作，在updateProgress更新动画进度，在actionEnd中获取到动画的最终状态，根据最终状态判断是继续执行动画与页面返回还是关闭动画取消页面返回。

```
1. @HMAnimator({ animatorName: 'liveInteractiveAnimator' })
2. export class LiveInteractiveAnimator implements IHMAnimator {
3. effect(enterHandle: HMAnimatorHandle, exitHandle: HMAnimatorHandle): void {
4. // ...
5. }

7. interactive(handle: HMAnimatorHandle): void {
8. handle.actionStart((event: GestureEvent) => {
9. if (event.offsetX > 0) {
10. HMRouterMgr.popAsync();
11. }
12. handle.startOffset = event.fingerList[0].localX;
13. });
14. handle.updateProgress((event, proxy, operation, startOffset) => {
15. if (!proxy?.updateTransition || !startOffset) {
16. return;
17. }
18. let offset = 0;
19. if (event.fingerList[0]) {
20. offset = Math.abs(event.fingerList[0].localX - startOffset);
21. }
22. if (offset < 0) {
23. proxy?.updateTransition(0);
24. return;
25. }
26. let rectWidth = event.target.area.width as number;
27. let rate = offset / rectWidth;
28. proxy?.updateTransition(rate);
29. });
30. handle.actionEnd((event, proxy, operation, startOffset) => {
31. if (!startOffset) {
32. return;
33. }
34. let rectWidth = event.target.area.width as number;
35. let rate = 0;
36. if (event.fingerList[0]) {
37. rate = Math.abs(event.fingerList[0].localX - startOffset) / rectWidth;
38. }
39. if (rate > 0.4) {
40. proxy?.finishTransition();
41. } else {
42. proxy?.cancelTransition?.();
43. }
44. });
45. }
46. }
```

[LiveHome.ets](https://gitcode.com/harmonyos_samples/HMRouter/blob/master/entry/src/main/ets/component/live/LiveHome.ets#L96-L158)

运行效果如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/F0UE_fo0RHqi9Ahh3Y7P3g/zh-cn_image_0000002194010388.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001954Z&HW-CC-Expire=86400&HW-CC-Sign=1BE65A72C6ACE626A4AF21877887ABD256119A5B35DF7C23AE78C5DF0093274D "点击放大")

## 数据加载场景

### 数据请求预加载，与页面跳转并行化

该场景下，开发者希望提前网络请求的位置并在其他线程中执行网络请求而不阻塞主线程，代码实现参考如下步骤。

1. 定义网络请求函数，可使用[TaskPool](../harmonyos-guides/taskpool-introduction.md)在其他线程执行网络请求并返回请求结果。

   ```
   1. @Concurrent
   2. async function networkRequest(lifecycle: string): Promise<string> {
   3. // ...
   4. }
   ```

   [ShoppingBagContent.ets](https://gitcode.com/harmonyos_samples/HMRouter/blob/master/entry/src/main/ets/component/shoppingBag/ShoppingBagContent.ets#L36-L46)
2. 定义生命周期，在onPrepare回调函数中，执行对应的网络请求函数，该回调触发时机为拦截器执行后，路由栈真正push前。

   ```
   1. @HMLifecycle({ lifecycleName: 'requestLifecycle' })
   2. export class ExampleLifecycle implements IHMLifecycle {
   3. private requestModel: RequestModel = new RequestModel();

   5. onPrepare(): void {
   6. console.log(this.requestModel.data);
   7. let task: taskpool.Task = new taskpool.Task(networkRequest, 'onPrepare');
   8. taskpool.execute(task).then((res: Object) => {
   9. console.log(res + '');
   10. });
   11. }

   13. // ...
   14. }
   ```

   [ShoppingBagContent.ets](https://gitcode.com/harmonyos_samples/HMRouter/blob/master/entry/src/main/ets/component/shoppingBag/ShoppingBagContent.ets#L50-L70)
3. 关联生命周期与对应组件。将生命周期的lifecycleName作为@HMRouter注解的lifecycle参数进行传入完成关联。

**图2** 数据请求预加载流程  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/6SDs-uO1STCKWl5SropPlA/zh-cn_image_0000002428190130.png?HW-CC-KV=V1&HW-CC-Date=20260428T001954Z&HW-CC-Expire=86400&HW-CC-Sign=6461952C4ED46DAF042442182A1BCBB85A1DE325C3DA0B3328477E856F865739 "点击放大")

### 页面重开数据恢复

该场景下当页面关闭时，之前浏览的相关记录依然存在，典型的场景例如短视频评论，当用户打开评论区页进行翻阅后停留在某处，此时关闭评论区再打开，评论内容会仍然停留在上一次浏览的位置。实现上可以参考如下步骤。

1. 使用[BuilderNode](../harmonyos-guides/arkts-user-defined-arktsnode-buildernode.md)构造出评论区组件，在makeNode函数中，若评论区不存在则创建，存在便直接返回。

   ```
   1. @Builder
   2. function buildComment(liveComments: LiveCommentsProduct[]) {
   3. // ...
   4. }

   6. export class CommentNodeController extends NodeController {
   7. commentList: BuilderNode<[LiveCommentsProduct[]]> | null = null;
   8. commentListData: LiveCommentsProduct[] = new LiveCommentsModel().getLiveCommentsList();

   10. constructor() {
   11. super();
   12. }

   14. makeNode(context: UIContext): FrameNode | null {
   15. if (this.commentList === null) {
   16. this.nodeBuild(context);
   17. }
   18. return this.commentList!.getFrameNode();
   19. }

   21. nodeBuild(context: UIContext) {
   22. this.commentList = new BuilderNode(context);
   23. if (this.commentList !== null) {
   24. this.commentList.build(wrapBuilder<[LiveCommentsProduct[]]>(buildComment), this.commentListData);
   25. }
   26. }

   28. dispose() {
   29. if (this.commentList !== null) {
   30. this.commentList.dispose();
   31. }
   32. }
   33. }
   ```

   [CommentInput.ets](https://gitcode.com/harmonyos_samples/HMRouter/blob/master/entry/src/main/ets/component/live/CommentInput.ets#L134-L200)
2. 通过在@HMLifecycle生命周期中，将CommentNodeController类的实例跟随视频播放页面的生命周期创建与释放，而非跟随评论区组件的生命周期创建与释放，使得当用户处在视频播放页时，内存中保存着评论区组件的BuilderNode，从而达成当用户关闭评论区再打开，浏览进度与关闭前一致的诉求。

   ```
   1. @HMLifecycle({ lifecycleName: 'liveHomeLifecycle' })
   2. export class LiveHomeLifecycle implements IHMLifecycle {
   3. commentRenderNode: CommentNodeController = new CommentNodeController();
   4. // ...
   5. onAppear(ctx: HMLifecycleContext): void {
   6. this.commentRenderNode.makeNode(ctx.uiContext);
   7. }

   9. onDisAppear(ctx: HMLifecycleContext): void {
   10. this.commentRenderNode.dispose();
   11. }
   12. }
   ```

   [LiveHome.ets](https://gitcode.com/harmonyos_samples/HMRouter/blob/master/entry/src/main/ets/component/live/LiveHome.ets#L53-L92)
3. 在对应的UI组件处获取到生命周期内的commentRenderNode，并在后续业务逻辑中使用NodeContainer进行挂载。

   ```
   1. @Component
   2. export struct CommentInput {
   3. @StorageLink('changeVideoHeight') videoHeight: string | number = CommonConstants.FULL_PERCENT;
   4. commentRenderNode: CommentNodeController = new CommentNodeController();

   6. // ...
   7. }
   ```

   [CommentInput.ets](https://gitcode.com/harmonyos_samples/HMRouter/blob/master/entry/src/main/ets/component/live/CommentInput.ets#L52-L129)

**图3** 页面重开数据恢复流程  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/GOy2R7FBQl69eB_QTPVllQ/zh-cn_image_0000002461709833.png?HW-CC-KV=V1&HW-CC-Date=20260428T001954Z&HW-CC-Expire=86400&HW-CC-Sign=521A3A757029FB13ABFF701A2F4F029CF92167AE2E96F2DC1D6D6D1AFADF4F70 "点击放大")

## 维测场景

### 页面埋点开发

当需要统计类似于页面加载耗时等数据，或者有其他自定义打点数据需要统计时，可以使用生命周期回调，在对应的位置进行打点，以下示例为页面停留时长的数据打点统计，实现上参考以下步骤：

1. 定义一个类PageDurationLifecycle实现IHMLifecycle接口。
2. 为该类添加@HMLifecycle注解，并配置global为true，将该生命周期配置到全局，所有页面都会执行该生命周期。
3. 在页面显示时（onShown）记录当前的时间戳，在页面隐藏时（onHidden）计算页面停留时长。

   ```
   1. @HMLifecycle({ lifecycleName: 'PageDurationLifecycle', global: true })
   2. export class PageDurationLifecycle implements IHMLifecycle {
   3. private time: number = 0;

   5. onShown(): void {
   6. this.time = new Date().getTime();
   7. }

   9. onHidden(ctx: HMLifecycleContext): void {
   10. const duration = new Date().getTime() - this.time;
   11. console.log(`Page ${ctx.navContext?.pathInfo.name} stay ${duration}`);
   12. }
   13. }
   ```

   [PageDurationLifecycle.ets](https://gitcode.com/harmonyos_samples/HMRouter/blob/master/entry/src/main/ets/lifecycle/PageDurationLifecycle.ets#L23-L36)

**图4** 页面埋点日志记录

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/w03tFmeMT7WOchafA1my6Q/zh-cn_image_0000002194010384.png?HW-CC-KV=V1&HW-CC-Date=20260428T001954Z&HW-CC-Expire=86400&HW-CC-Sign=8DDF8786ADDAC7B2F448D911D8A13BA90282D53425C017693AFB5E8806DDF67D "点击放大")

## 示例代码

* [HMRouter](https://gitcode.com/harmonyos_samples/HMRouter)
