---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ads-publisher-service-splash
title: 开屏广告
breadcrumb: 指南 > 应用服务 > Ads Kit（广告服务） > 流量变现服务开发 > 开屏广告
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:11+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:645891becb9db5731fdee316f7176323a4613eed08afbb4cfe86b60f1f6a847c
---

## 场景介绍

开屏广告是一种在应用启动时且在应用主界面显示之前需要被展示的广告。您需要预先为App设计一张开屏默认的Slogan图片，确保在未获取到开屏广告之前展示默认的Slogan，提供良好的用户体验。

开屏广告分为全屏开屏广告、半屏开屏广告，其中全屏开屏广告展示形式为广告铺满整个页面；半屏开屏广告展示形式会根据媒体页面自定义布局渲染广告、icon和版权信息，一般情况下建议将icon和版权信息展示在广告下方。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/kh_AuXvJRquVFc4OGa1oTQ/zh-cn_image_0000002583478769.png?HW-CC-KV=V1&HW-CC-Date=20260427T234810Z&HW-CC-Expire=86400&HW-CC-Sign=32039D5D91B20D91C58C4EAB4D3563A9219350F7099362AF4F69D6E9F9583E23)

## 约束与限制

支持Phone、Tablet、PC/2in1设备。

使用PC/2in1设备时，需要确保设备上智慧营销服务或广告服务的版本在8.4.80.300及以上，版本号可通过选择“设置> 应用和元服务 > 更多应用”查看。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [loadAd](../harmonyos-references/js-apis-advertising.md#loadad)(adParam: AdRequestParams, adOptions: AdOptions, listener: AdLoadListener): void | 请求单广告位广告，通过AdRequestParams、AdOptions进行广告请求参数设置，通过AdLoadListener监听广告请求回调。 |
| [AdComponent](../harmonyos-references/js-apis-adcomponent.md)({ads: advertising.Advertisement[], displayOptions: advertising.AdDisplayOptions, interactionListener: advertising.AdInteractionListener, @BuilderParam adRenderer?: () => void, @Prop rollPlayState?: number}) | 展示广告，通过AdDisplayOptions进行广告展示参数设置，通过AdInteractionListener监听广告状态回调。  说明：为了保证广告能正确展示，该接口必须和请求广告接口配套使用。 |

## 开发步骤

### 请求广告

1. 导入相关模块。

   ```
   1. import { abilityAccessCtrl, common, PermissionRequestResult } from '@kit.AbilityKit';
   2. import { advertising, identifier } from '@kit.AdsKit';
   3. import { router, window } from '@kit.ArkUI';
   4. import { BusinessError } from '@kit.BasicServicesKit';
   5. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 获取OAID。

   若需提升广告推送精准度，可以在请求参数[AdRequestParams](../harmonyos-references/js-apis-advertising.md#adrequestparams)中添加oaid属性。

   如何获取OAID参见[获取OAID信息](oaid-service.md)。

   说明

   使用以下示例中提供的测试广告位时，必须先获取OAID信息。
3. 请求单广告位广告。

   需要创建一个AdLoader对象，通过AdLoader的[loadAd](../harmonyos-references/js-apis-advertising.md#loadad)方法请求广告，最后通过[AdLoadListener](../harmonyos-references/js-apis-advertising.md#adloadlistener)来监听广告的加载状态。测试开屏广告时，需要使用专门的测试广告位来获取测试开屏广告，示例代码中提供了两种开屏广告类型对应的广告位：半屏开屏（图片）（g3tl51sqih）和全屏开屏（视频）（r145sz31dp），测试广告位ID仅作为调试使用，不可用于广告变现。

   请求广告关键参数如下所示：

   | 请求广告参数名 | 类型 | 必填 | 说明 |
   | --- | --- | --- | --- |
   | adType | number | 是 | 请求广告类型，开屏广告类型为1。 |
   | adId | string | 是 | 广告位ID。  - 如果仅调测广告，可使用测试广告位ID：g3tl51sqih半屏开屏（图片）和r145sz31dp全屏开屏（视频）。  - 如果要接入正式广告，则需要申请正式的广告位ID。可在应用发布前进入[流量变现官网](https://developer.huawei.com/consumer/cn/monetize)，点击“开始变现”，登录[鲸鸿动能媒体服务平台](https://developer.huawei.com/consumer/cn/service/ads/publisher/html/index.html?lang=zh)进行申请，具体操作详情请参见[展示位创建](../monetize/zhanshiweichuangjian-0000001132700049.md)。 |
   | adCount | number | 否 | 广告数量。 |
   | orientation | number | 否 | 媒体请求广告的屏幕方向。1表示竖屏，0表示横屏，不设置则默认为1。当前未上架横屏开屏素材，若设置请求屏幕方向为横屏则不展示开屏广告。如果媒体设置应用固定横屏展示，但该参数未设置或者设置为1，则展示效果会受影响。 |

   | 返回广告参数名 | 类型 | 说明 |
   | --- | --- | --- |
   | isFullScreen | boolean | 标识返回的广告是否为全屏，true为全屏广告，false为半屏广告。 |

   说明

   1、如果超时没有请求到广告，应用自行跳转到默认首页。

   2、为保证开屏展示效果，建议开发者在请求广告前，设置屏幕方向为竖屏。

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. @State ad: advertising.Advertisement | undefined = undefined;
   5. // ...
   6. private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
   7. // 是否超时
   8. private isTimeOut: boolean = false;
   9. // 超时时间(单位毫秒)，开发者可根据实际情况修改
   10. private timeOutDuration: number = 1000;
   11. // 超时index
   12. private timeOutIndex: number = -1;

   14. aboutToAppear(): void {
   15. // 开启全屏模式沉浸页面
   16. this.setWindowLayoutFullScreen(true);
   17. // 设置屏幕方向为竖屏
   18. this.setWindowPreferredOrientation(window.Orientation.PORTRAIT);
   19. // 调用loadAd加载广告
   20. // ...
   21. }

   23. aboutToDisappear(): void {
   24. // 关闭全屏模式，开发者可根据实际情况修改
   25. this.setWindowLayoutFullScreen(false);
   26. // 设置屏幕方向为默认值，开发者可根据实际情况修改
   27. this.setWindowPreferredOrientation(window.Orientation.UNSPECIFIED);
   28. }

   30. private async setWindowLayoutFullScreen(isLayoutFullScreen: boolean): Promise<void> {
   31. try {
   32. const win: window.Window = await window.getLastWindow(this.context);
   33. await win.setWindowLayoutFullScreen(isLayoutFullScreen);
   34. } catch (e) {
   35. hilog.error(0x0000, 'testTag', `Failed to set window layout. Code is ${e.code}, message is ${e.message}`);
   36. }
   37. }

   39. private async setWindowPreferredOrientation(orientation: Orientation): Promise<void> {
   40. try {
   41. const win: window.Window = await window.getLastWindow(this.context);
   42. await win.setPreferredOrientation(orientation);
   43. } catch (e) {
   44. hilog.error(0x0000, 'testTag', `Failed to set preferred orientation. Code is ${e.code}, message is ${e.message}`);
   45. }
   46. }

   48. build() {
   49. // ...
   50. }

   52. // ...
   53. private async loadAd(adId: string): Promise<void> {
   54. // 广告请求参数
   55. const adRequestParams: advertising.AdRequestParams = {
   56. // 广告位ID
   57. adId: adId,
   58. // 开屏广告类型
   59. adType: 1,
   60. // 请求的广告数量
   61. adCount: 1,
   62. // 开放匿名设备标识符
   63. oaid: await requestOAID(this.context)
   64. };
   65. // 广告请求回调监听
   66. const adLoadListener: advertising.AdLoadListener = {
   67. onAdLoadFailure: (errorCode: number, errorMsg: string) => {
   68. hilog.error(0x0000, 'testTag', `Failed to load ad. Code is ${errorCode}, message is ${errorMsg}`);
   69. },
   70. onAdLoadSuccess: (ads: Array<advertising.Advertisement>) => {
   71. clearTimeout(this.timeOutIndex);
   72. if (this.isTimeOut) {
   73. return;
   74. }
   75. hilog.info(0x0000, 'testTag', 'Succeeded in loading ad');
   76. this.ad = ads[0];
   77. }
   78. };
   79. // 广告配置参数，开发者可根据项目实际情况设置
   80. const adOptions: advertising.AdOptions = {};
   81. // 创建AdLoader广告对象
   82. const adLoader: advertising.AdLoader = new advertising.AdLoader(this.context);
   83. // 启动超时定时器
   84. this.timeOutHandler();
   85. try {
   86. // 调用广告请求接口
   87. adLoader.loadAd(adRequestParams, adOptions, adLoadListener);
   88. } catch (e) {
   89. hilog.error(0x0000, 'testTag', `Failed to load ad. Code is ${e.code}, message is ${e.message}`);
   90. }
   91. }

   93. private timeOutHandler(): void {
   94. this.isTimeOut = false;
   95. // 超时处理
   96. this.timeOutIndex = setTimeout(() => {
   97. this.isTimeOut = true;
   98. this.routeToHome();
   99. hilog.error(0x0000, 'testTag', 'Load ad time out');
   100. }, this.timeOutDuration);
   101. }

   103. private routeToHome(): void {
   104. // 开发者可根据项目实际情况修改超时之后要跳转的目标页面
   105. this.getUIContext().getRouter().replaceUrl({ url: 'pages/Index' }, router.RouterMode.Single)
   106. .catch((e: BusinessError) => {
   107. hilog.error(0x0000, 'testTag', `Failed to route to home. Code is ${e.code}, message is ${e.message}`);
   108. });
   109. }
   110. }

   112. async function requestOAID(context: Context): Promise<string | undefined> {
   113. // 向用户请求授权广告跨应用关联访问权限
   114. let isPermissionGranted: boolean = false;
   115. try {
   116. const atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
   117. const result: PermissionRequestResult =
   118. await atManager.requestPermissionsFromUser(context, ['ohos.permission.APP_TRACKING_CONSENT']);
   119. isPermissionGranted = result.authResults[0] === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED;
   120. } catch (err) {
   121. hilog.error(0x0000, 'testTag', `Failed to request permission. Code is ${err.code}, message is ${err.message}`);
   122. }
   123. if (isPermissionGranted) {
   124. hilog.info(0x0000, 'testTag', 'Succeeded in requesting permission');
   125. try {
   126. const oaid = await identifier.getOAID();
   127. hilog.info(0x0000, 'testTag', 'Succeeded in getting OAID');
   128. return oaid;
   129. } catch (err) {
   130. hilog.error(0x0000, 'testTag', `Failed to get OAID. Code is ${err.code}, message is ${err.message}`);
   131. }
   132. } else {
   133. hilog.error(0x0000, 'testTag', 'Failed to request permission. User rejected');
   134. }
   135. return undefined;
   136. }
   ```

### 展示广告

1. 导入相关模块。

   ```
   1. import { AdComponent, advertising } from '@kit.AdsKit';
   2. import { router } from '@kit.ArkUI';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 展示广告。

   展示广告通过[AdInteractionListener](../harmonyos-references/js-apis-advertising.md#adinteractionlistener)监听广告状态回调，涉及的回调状态如下所示：

   | 回调状态 | 说明 | 使用建议 |
   | --- | --- | --- |
   | onAdOpen | 打开广告。 | - |
   | onAdClick | 点击广告。 | - |
   | onAdClose | 关闭广告。 | 广告倒计时结束、用户点击跳过按钮或广告从后台返回时触发，需要跳转到应用首页。回调状态包含了具体的关闭原因，详情见：[data说明](../harmonyos-references/js-apis-advertising.md#onstatuschanged)。 |
   | onAdFail | 广告加载失败。 | 广告展示失败时触发，需要跳转到应用首页。 |

   说明

   1、请求到广告之前需要展示默认的Slogan图片。

   2、由请求广告中获取的isFullScreen参数判断展示全屏或者半屏广告。

   3、目前只支持展示竖屏广告。

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. @State ad: advertising.Advertisement | undefined = undefined;
   5. // 广告展示参数
   6. private adDisplayOptions: advertising.AdDisplayOptions = {
   7. // 是否静音
   8. mute: true
   9. };
   10. // ...

   12. build() {
   13. RelativeContainer() {
   14. // 展示开发者自定义Slogan图片
   15. Image($r('app.media.slogan'))
   16. .width('100%')
   17. .height('100%')
   18. .zIndex(0)
   19. // 展示开发者自定义icon、应用名称、版权信息
   20. Column() {
   21. Row() {
   22. Image($r('app.media.video'))
   23. .width(24)
   24. .height(24)
   25. .margin(8)
   26. Text($r('app.string.video'))
   27. .fontColor('#1A1A1A')
   28. .fontSize(16)
   29. }
   30. .margin({ bottom: 8 })

   32. Column() {
   33. Text($r('app.string.copyright'))
   34. .fontColor('#1A1A1A')
   35. .fontSize(9)
   36. }
   37. }
   38. .zIndex(1)
   39. .alignRules({ bottom: { anchor: '__container__', align: VerticalAlign.Bottom } })
   40. .width('100%')
   41. .height('13%')

   43. if (this.ad) {
   44. if (this.ad.isFullScreen) {
   45. // 全屏开屏广告
   46. this.splashFullScreen()
   47. } else {
   48. // 半屏开屏广告
   49. this.splashHalfScreen()
   50. }
   51. }
   52. }
   53. .width('100%')
   54. .height('100%')
   55. }

   57. /**
   58. * 半屏开屏广告
   59. */
   60. @Builder
   61. private splashHalfScreen() {
   62. AdComponent({
   63. ads: [this.ad!],
   64. displayOptions: this.adDisplayOptions,
   65. interactionListener: {
   66. onStatusChanged: (status: string, ad: advertising.Advertisement, data: string) => {
   67. switch (status) {
   68. case 'onAdOpen':
   69. hilog.info(0x0000, 'testTag', 'Status is onAdOpen');
   70. break;
   71. case 'onAdClick':
   72. hilog.info(0x0000, 'testTag', 'Status is onAdClick');
   73. break;
   74. case 'onAdClose':
   75. hilog.info(0x0000, 'testTag', 'Status is onAdClose');
   76. this.routeToHome();
   77. break;
   78. case 'onAdFail':
   79. hilog.error(0x0000, 'testTag', 'Status is onAdFail');
   80. this.routeToHome();
   81. break;
   82. }
   83. }
   84. }
   85. })
   86. .zIndex(1)
   87. .width('100%')
   88. .height('87%')
   89. // 自定义组件动画
   90. .transition(TransitionEffect.OPACITY.animation({ duration: 1000, curve: Curve.Friction}))
   91. .alignRules({ top: { anchor: '__container__', align: VerticalAlign.Top } })
   92. }

   94. /**
   95. * 全屏开屏广告
   96. */
   97. @Builder
   98. private splashFullScreen() {
   99. AdComponent({
   100. ads: [this.ad!],
   101. displayOptions: this.adDisplayOptions,
   102. interactionListener: {
   103. onStatusChanged: (status: string, ad: advertising.Advertisement, data: string) => {
   104. switch (status) {
   105. case 'onAdOpen':
   106. hilog.info(0x0000, 'testTag', 'Status is onAdOpen');
   107. break;
   108. case 'onAdClick':
   109. hilog.info(0x0000, 'testTag', 'Status is onAdClick');
   110. break;
   111. case 'onAdClose':
   112. hilog.info(0x0000, 'testTag', 'Status is onAdClose');
   113. this.routeToHome();
   114. break;
   115. case 'onAdFail':
   116. hilog.error(0x0000, 'testTag', 'Status is onAdFail');
   117. this.routeToHome();
   118. break;
   119. }
   120. }
   121. }
   122. })
   123. .zIndex(1)
   124. .width('100%')
   125. .height('100%')
   126. }
   127. // ...

   129. private routeToHome(): void {
   130. // 开发者可根据项目实际情况修改超时之后要跳转的目标页面
   131. this.getUIContext().getRouter().replaceUrl({ url: 'pages/Index' }, router.RouterMode.Single)
   132. .catch((e: BusinessError) => {
   133. hilog.error(0x0000, 'testTag', `Failed to route to home. Code is ${e.code}, message is ${e.message}`);
   134. });
   135. }
   136. }

   138. // ...
   ```

## 测试开屏广告

测试开屏广告时，需要使用专门的测试广告位ID来获取测试广告，以避免在测试过程中产生无效的广告点击量。测试广告位ID仅作为功能调试使用，不可用于广告变现。您应在应用发布前先进入[流量变现官网](https://developer.huawei.com/consumer/cn/monetize)，点击“开始变现”，登录[鲸鸿动能媒体服务平台](https://developer.huawei.com/consumer/cn/service/ads/publisher/html/index.html?lang=zh)，申请正式的广告位ID并替换测试广告位ID，具体操作详情请参见[展示位创建](../distribution/monetize/zhanshiweichuangjian-0000001132700049.md)。

以下表格中提供了开屏广告的专用测试广告位ID：

| 广告位类型 | 测试广告位ID | 展示形式 | 比例 | 推广类型 |
| --- | --- | --- | --- | --- |
| 开屏 | g3tl51sqih | 图片 | 9:16 | 应用促活 |
| 开屏 | r145sz31dp | 视频 | 9:16 | 应用促活 |
