---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ads-publisher-service-interstitial
title: 插屏广告
breadcrumb: 指南 > 应用服务 > Ads Kit（广告服务） > 流量变现服务开发 > 插屏广告
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:11+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:de5cc2ac44ae631fff408d0d3d03e61dfb4c9bf998f14ef73a6ab6a92959ff5b
---

## 场景介绍

插屏广告是一种在应用开启、暂停或退出时以全屏或半屏的形式弹出的广告形式，展示时机巧妙避开用户对应用的正常体验，尺寸大，曝光效果好。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/wPqFlEmQTDKRSJd6Srfrmw/zh-cn_image_0000002552958768.png?HW-CC-KV=V1&HW-CC-Date=20260427T234810Z&HW-CC-Expire=86400&HW-CC-Sign=12541B44185864D4A1BEE58D70F3175DB18CA30C617AD6358672B62BADAD00E6)

## 约束与限制

支持Phone、Tablet、PC/2in1设备。

使用PC/2in1设备时，需要确保设备上智慧营销服务或广告服务的版本在8.4.80.300及以上，版本号可通过选择“设置> 应用和元服务 > 更多应用”查看。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [loadAd](../harmonyos-references/js-apis-advertising.md#loadad)(adParam: AdRequestParams, adOptions: AdOptions, listener: AdLoadListener): void | 请求单广告位广告，通过AdRequestParams、AdOptions进行广告请求参数设置，通过AdLoadListener监听广告请求回调。 |
| [showAd](../harmonyos-references/js-apis-advertising.md#advertisingshowad)(ad: Advertisement, options: AdDisplayOptions, context?: common.UIAbilityContext): void | 展示广告，通过AdDisplayOptions进行广告展示参数设置。  说明：为了保证广告能正确展示，该接口必须和请求广告接口配套使用。 |

## 开发步骤

### 请求广告

1. 导入相关模块。

   ```
   1. import { abilityAccessCtrl, common, PermissionRequestResult } from '@kit.AbilityKit';
   2. import { advertising, identifier } from '@kit.AdsKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 获取OAID。

   若需提升广告推送精准度，可以在请求参数[AdRequestParams](../harmonyos-references/js-apis-advertising.md#adrequestparams)中添加oaid属性。

   如何获取OAID参见[获取OAID信息](oaid-service.md)。

   说明

   使用以下示例中提供的测试广告位时，必须先获取OAID信息。
3. 请求单广告位广告。

   需要先创建一个AdLoader对象，通过AdLoader的[loadAd](../harmonyos-references/js-apis-advertising.md#loadad)方法请求广告，最后通过[AdLoadListener](../harmonyos-references/js-apis-advertising.md#adloadlistener)来监听广告的加载状态。

   请求广告关键参数如下所示：

   | 请求广告参数名 | 类型 | 必填 | 说明 |
   | --- | --- | --- | --- |
   | adType | number | 是 | 请求广告类型，插屏广告类型为12。 |
   | adId | string | 是 | 广告位ID。  - 如果仅调测广告，可使用测试广告位ID：p540739a8w。  - 如果要接入正式广告，则需要申请正式的广告位ID。可在应用发布前进入[流量变现官网](https://developer.huawei.com/consumer/cn/monetize)，点击“开始变现”，登录[鲸鸿动能媒体服务平台](https://developer.huawei.com/consumer/cn/service/ads/publisher/html/index.html?lang=zh)进行申请，具体操作详情请参见[展示位创建](../monetize/zhanshiweichuangjian-0000001132700049.md)。 |
   | oaid | string | 否 | 开放匿名设备标识符，用于精准推送广告。不填无法获取到个性化广告。 |

   示例代码如下所示：

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

   6. build() {
   7. Column() {
   8. Button('LoadAd')
   9. .onClick(async () => {
   10. await this.loadAd();
   11. })
   12. }
   13. .width('100%')
   14. .height('100%')
   15. .justifyContent(FlexAlign.Center)
   16. }

   18. private async loadAd(): Promise<void> {
   19. // 广告请求回调监听
   20. const adLoadListener: advertising.AdLoadListener = {
   21. onAdLoadFailure: (errorCode: number, errorMsg: string) => {
   22. hilog.error(0x0000, 'testTag', `Failed to load ad. Code is ${errorCode}, message is ${errorMsg}`);
   23. },
   24. onAdLoadSuccess: (ads: Array<advertising.Advertisement>) => {
   25. hilog.info(0x0000, 'testTag', 'Succeeded in loading ad');
   26. // ...
   27. }
   28. };
   29. // 广告请求参数
   30. const adRequestParams: advertising.AdRequestParams = {
   31. // 'p540739a8w'为测试专用的广告位ID，App正式发布时需要改为正式的广告位ID
   32. adId: 'p540739a8w',
   33. // 插屏广告类型
   34. adType: 12,
   35. // 开放匿名设备标识符
   36. oaid: await requestOAID(this.context)
   37. };
   38. // 广告配置参数，开发者可根据项目实际情况设置
   39. const adOptions: advertising.AdOptions = {};
   40. // 创建AdLoader广告对象
   41. const adLoader: advertising.AdLoader = new advertising.AdLoader(this.context);
   42. try {
   43. // 调用广告请求接口
   44. adLoader.loadAd(adRequestParams, adOptions, adLoadListener);
   45. } catch (e) {
   46. hilog.error(0x0000, 'testTag', `Failed to load ad. Code is ${e.code}, message is ${e.message}`);
   47. }
   48. }
   49. }

   51. async function requestOAID(context: Context): Promise<string | undefined> {
   52. // 向用户请求授权广告跨应用关联访问权限
   53. let isPermissionGranted: boolean = false;
   54. try {
   55. const atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
   56. const result: PermissionRequestResult =
   57. await atManager.requestPermissionsFromUser(context, ['ohos.permission.APP_TRACKING_CONSENT']);
   58. isPermissionGranted = result.authResults[0] === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED;
   59. } catch (err) {
   60. hilog.error(0x0000, 'testTag', `Failed to request permission. Code is ${err.code}, message is ${err.message}`);
   61. }
   62. if (isPermissionGranted) {
   63. hilog.info(0x0000, 'testTag', 'Succeeded in requesting permission');
   64. try {
   65. const oaid = await identifier.getOAID();
   66. hilog.info(0x0000, 'testTag', 'Succeeded in getting OAID');
   67. return oaid;
   68. } catch (err) {
   69. hilog.error(0x0000, 'testTag', `Failed to get OAID. Code is ${err.code}, message is ${err.message}`);
   70. }
   71. } else {
   72. hilog.error(0x0000, 'testTag', 'Failed to request permission. User rejected');
   73. }
   74. return undefined;
   75. }
   ```

### 事件订阅

1. 导入相关模块。

   ```
   1. import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 事件订阅。

   开发者需要在应用中订阅com.huawei.hms.pps.action.PPS\_INTERSTITIAL\_STATUS\_CHANGED事件来监听插屏广告页面变化。

   在订阅到公共事件后，可以从[CommonEventData](../harmonyos-references/js-apis-inner-commonevent-commoneventdata.md)的parameters参数中使用interstitial\_ad\_status作为key值获取插屏广告页面变化状态。

   涉及的页面变化状态如下所示：

   | 页面变化状态 | 说明 |
   | --- | --- |
   | onAdOpen | 打开广告。 |
   | onAdClick | 点击广告。 |
   | onAdClose | 关闭广告。 |
   | onVideoPlayBegin | 广告视频开始播放。 |
   | onVideoPlayEnd | 广告视频播放结束。 |

   示例代码如下所示：

   ```
   1. const KEY_INTERSTITIAL_STATUS = 'interstitial_ad_status';

   3. export class InterstitialAdStatusHandler {
   4. // 用于保存创建成功的订阅者对象，后续使用其完成订阅及退订的动作
   5. private subscriber: commonEventManager.CommonEventSubscriber | null = null;

   7. // 订阅方法，需要在每次展示广告前调用
   8. public registerPPSReceiver(): void {
   9. if (this.subscriber) {
   10. this.unRegisterPPSReceiver();
   11. }
   12. // 订阅者信息
   13. const subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
   14. events: ['com.huawei.hms.pps.action.PPS_INTERSTITIAL_STATUS_CHANGED'],
   15. // publisherBundleName被设置为"com.huawei.hms.adsservice"，这意味着只有来自该包名的事件才会被订阅者接收和处理。
   16. // 如果没有明确声明publisherBundleName，那么订阅者可能会收到来自其它包名的伪造事件，从而导致安全性问题或误导。
   17. publisherBundleName: 'com.huawei.hms.adsservice'
   18. };
   19. // 创建订阅者回调
   20. commonEventManager.createSubscriber(subscribeInfo,
   21. (err: BusinessError, commonEventSubscriber: commonEventManager.CommonEventSubscriber) => {
   22. if (err) {
   23. hilog.error(0x0000, 'testTag', `Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
   24. return;
   25. }
   26. hilog.info(0x0000, 'testTag', 'Succeeded in creating subscriber');
   27. this.subscriber = commonEventSubscriber;
   28. // 订阅公共事件回调
   29. commonEventManager.subscribe(this.subscriber,
   30. (err: BusinessError, commonEventData: commonEventManager.CommonEventData) => {
   31. if (err) {
   32. hilog.error(0x0000, 'testTag', `Failed to subscribe. Code is ${err.code}, message is ${err.message}`);
   33. } else {
   34. // 订阅者成功接收到公共事件
   35. hilog.info(0x0000, 'testTag', 'Succeeded in subscribing data');
   36. // 获取插屏广告页面变化状态
   37. const status: string = commonEventData?.parameters?.[KEY_INTERSTITIAL_STATUS];
   38. switch (status) {
   39. case 'onAdOpen':
   40. hilog.info(0x0000, 'testTag', 'Status is onAdOpen');
   41. break;
   42. case 'onAdClick':
   43. hilog.info(0x0000, 'testTag', 'Status is onAdClick');
   44. break;
   45. case 'onAdClose':
   46. hilog.info(0x0000, 'testTag', 'Status is onAdClose');
   47. this.unRegisterPPSReceiver();
   48. break;
   49. case 'onVideoPlayBegin':
   50. hilog.info(0x0000, 'testTag', 'Status is onVideoPlayBegin');
   51. break;
   52. case 'onVideoPlayEnd':
   53. hilog.info(0x0000, 'testTag', 'Status is onVideoPlayEnd');
   54. break;
   55. default:
   56. break;
   57. }
   58. }
   59. });
   60. });
   61. }

   63. // 取消订阅
   64. public unRegisterPPSReceiver(): void {
   65. commonEventManager.unsubscribe(this.subscriber, (err: BusinessError) => {
   66. if (err) {
   67. hilog.error(0x0000, 'testTag', `Failed to unsubscribe. Code is ${err.code}, message is ${err.message}`);
   68. } else {
   69. hilog.info(0x0000, 'testTag', 'Succeeded in unsubscribing');
   70. this.subscriber = null;
   71. }
   72. });
   73. }
   74. }
   ```

### 展示广告

1. 导入相关模块。

   ```
   1. import { common } from '@kit.AbilityKit';
   2. import { advertising } from '@kit.AdsKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   4. // 事件订阅步骤中创建的文件
   5. import { InterstitialAdStatusHandler } from './InterstitialAdStatusHandler';
   ```
2. 展示广告。

   开发者需要调用[showAd](../harmonyos-references/js-apis-advertising.md#advertisingshowad)方法来展示广告，ads为[请求广告](ads-publisher-service-interstitial.md#请求广告)返回的广告信息，在每次展示广告前需要注册[事件订阅](ads-publisher-service-interstitial.md#事件订阅)中定义的监听器。

   示例代码如下所示：

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

   6. build() {
   7. // ...
   8. }

   10. private async loadAd(): Promise<void> {
   11. // 广告请求回调监听
   12. const adLoadListener: advertising.AdLoadListener = {
   13. onAdLoadFailure: (errorCode: number, errorMsg: string) => {
   14. hilog.error(0x0000, 'testTag', `Failed to load ad. Code is ${errorCode}, message is ${errorMsg}`);
   15. },
   16. onAdLoadSuccess: (ads: Array<advertising.Advertisement>) => {
   17. hilog.info(0x0000, 'testTag', 'Succeeded in loading ad');
   18. try {
   19. // 注册插屏广告状态监听器
   20. new InterstitialAdStatusHandler().registerPPSReceiver();
   21. // 广告展示参数，开发者可根据项目实际情况设置
   22. const adDisplayOptions: advertising.AdDisplayOptions = {
   23. // 是否静音
   24. mute: true
   25. };
   26. // 此处ads[0]表示请求到的第一个广告，开发者可根据项目实际情况选择
   27. advertising.showAd(ads[0], adDisplayOptions, this.context);
   28. } catch (e) {
   29. hilog.error(0x0000, 'testTag', `Failed to show ad. Code is ${e.code}, message is ${e.message}`);
   30. }
   31. }
   32. };
   33. // ...
   34. }
   35. }
   ```

## 测试插屏广告

测试插屏广告时，需要使用专门的测试广告位ID来获取测试广告，以避免在测试过程中产生无效的广告点击量。测试广告位ID仅作为功能调试使用，不可用于广告变现。您应在应用发布前先进入[流量变现官网](https://developer.huawei.com/consumer/cn/monetize)，点击“开始变现”，登录[鲸鸿动能媒体服务平台](https://developer.huawei.com/consumer/cn/service/ads/publisher/html/index.html?lang=zh)，申请正式的广告位ID并替换测试广告位ID，具体操作详情请参见[展示位创建](../distribution/monetize/zhanshiweichuangjian-0000001132700049.md)。

以下表格中提供了插屏广告的专用测试广告位ID：

| 广告位类型 | 测试广告位ID | 展示形式 | 比例 | 推广类型 |
| --- | --- | --- | --- | --- |
| 插屏 | p540739a8w | 图片 | 16:9 | 网页推广 |
| 插屏 | v1rknehtfa | 视频 | 9:16 | 推广元服务 |
