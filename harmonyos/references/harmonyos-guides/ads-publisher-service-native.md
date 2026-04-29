---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ads-publisher-service-native
title: 原生广告
breadcrumb: 指南 > 应用服务 > Ads Kit（广告服务） > 流量变现服务开发 > 原生广告
category: harmonyos-guides
scraped_at: 2026-04-29T13:37:03+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:9adce0a78faa97f6f0b17c36c7545e0e0afec2f841faff9a14cc8fa868cb4009
---

## 场景介绍

原生广告是与应用内容融于一体的广告，通过“和谐”的内容呈现广告信息，在不破坏用户体验的前提下，为用户提供有价值的信息，展示形式包含图片和视频，支持您自由定制界面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/JbYeIxNKTYeveHfJ5XRdSQ/zh-cn_image_0000002589325135.png?HW-CC-KV=V1&HW-CC-Date=20260429T053702Z&HW-CC-Expire=86400&HW-CC-Sign=CA1F18941F4F16F665B9379AB66F9A63D0787E6695ED23A0AF5AB9A9A08E7044)

## 约束与限制

支持Phone、Tablet、PC/2in1设备。

使用PC/2in1设备时，需要确保设备上智慧营销服务或广告服务的版本在8.4.80.300及以上，版本号可通过选择“设置> 应用和元服务 > 更多应用”查看。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [loadAd](../harmonyos-references/js-apis-advertising.md#loadad)(adParam: AdRequestParams, adOptions: AdOptions, listener: AdLoadListener): void | 请求单广告位广告，通过AdRequestParams、AdOptions进行广告请求参数设置，通过AdLoadListener监听广告请求回调。 |
| [loadAdWithMultiSlots](../harmonyos-references/js-apis-advertising.md#loadadwithmultislots)(adParams: AdRequestParams[], adOptions: AdOptions, listener: MultiSlotsAdLoadListener): void | 请求多广告位广告，通过AdRequestParams[]、AdOptions进行广告请求参数设置，通过MultiSlotsAdLoadListener监听广告请求回调。 |
| [AdComponent](../harmonyos-references/js-apis-adcomponent.md)({ads: advertising.Advertisement[], displayOptions: advertising.AdDisplayOptions, interactionListener: advertising.AdInteractionListener, @BuilderParam adRenderer?: () => void, @Prop rollPlayState?: number}) | 展示广告，通过AdDisplayOptions进行广告展示参数设置，通过AdInteractionListener监听广告状态回调。  说明：为了保证广告能正确展示，该接口必须和请求广告接口配套使用。 |

## AdComponent组件建议宽高

| 样式 | 建议宽高 |
| --- | --- |
| 原生信息流/原生瀑布流 | width：与信息流内容保持一致。  height：无需设置。 |
| 原生插图 | width：312vp。  height：284vp。 |

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
3. 请求广告。

   请求广告需要创建一个AdLoader对象。

   * 如果要请求单广告位广告，通过AdLoader的[loadAd](../harmonyos-references/js-apis-advertising.md#loadad)方法请求广告，通过[AdLoadListener](../harmonyos-references/js-apis-advertising.md#adloadlistener)来监听广告的加载状态。
   * 如果要请求多广告位广告，通过AdLoader的[loadAdWithMultiSlots](../harmonyos-references/js-apis-advertising.md#loadadwithmultislots)方法请求广告，通过[MultiSlotsAdLoadListener](../harmonyos-references/js-apis-advertising.md#multislotsadloadlistener)来监听广告的加载状态。

   请求广告关键参数如下所示：

   | 请求广告参数名 | 类型 | 必填 | 说明 |
   | --- | --- | --- | --- |
   | adType | number | 是 | 请求广告类型，原生广告类型为3。 |
   | adId | string | 是 | 广告位ID。  - 如果仅调测广告，可使用测试广告位ID：s7moc0jc6m（原生视频），h8asowxwhq（原生大图），k94abyn2z4（原生小图），o7dj7qsbvy（原生三图）。  - 如果要接入正式广告，则需要申请正式的广告位ID。可在应用发布前进入[流量变现官网](https://developer.huawei.com/consumer/cn/monetize)，点击“开始变现”，登录[鲸鸿动能媒体服务平台](https://developer.huawei.com/consumer/cn/service/ads/publisher/html/index.html?lang=zh)进行申请，具体操作详情请参见[展示位创建](../monetize/zhanshiweichuangjian-0000001132700049.md)。 |
   | oaid | string | 否 | 开放匿名设备标识符，用于精准推送广告。不填无法获取到个性化广告。 |

   以请求多广告位广告为例，示例代码如下所示：

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. @State ads: advertising.Advertisement[] = [];
   5. // ...
   6. private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

   8. aboutToAppear(): void {
   9. // 调用loadAd加载广告
   10. // ...
   11. }

   13. private async loadAd(...adIds: string[]): Promise<void> {
   14. // 广告请求参数
   15. const adRequestParamsArray: advertising.AdRequestParams[] = [];
   16. const oaid: string | undefined = await requestOAID(this.context);
   17. for (const adId of adIds) {
   18. adRequestParamsArray.push({
   19. // 广告位ID
   20. adId: adId,
   21. // 原生广告类型
   22. adType: 3,
   23. // 原生广告扩展参数，是否直接返回广告，不用等待所有广告素材下载完成
   24. enableDirectReturnVideoAd: true,
   25. // 开放匿名设备标识符
   26. oaid: oaid
   27. });
   28. }
   29. // 广告配置参数，开发者可根据项目实际情况设置
   30. const adOptions: advertising.AdOptions = {};
   31. // 广告请求回调监听
   32. const multiSlotsAdLoaderListener: advertising.MultiSlotsAdLoadListener = {
   33. onAdLoadFailure: (errorCode: number, errorMsg: string) => {
   34. hilog.error(0x0000, 'testTag', `Failed to load multiSlots ad. Code is ${errorCode}, message is ${errorMsg}`);
   35. },
   36. onAdLoadSuccess: (ads: Map<string, Array<advertising.Advertisement>>) => {
   37. hilog.info(0x0000, 'testTag', 'Succeeded in loading multiSlots ad');
   38. const returnAds: advertising.Advertisement[] = [];
   39. ads.forEach((adsArray) => returnAds.push(...adsArray));
   40. this.ads = returnAds;
   41. }
   42. };
   43. // 创建AdLoader广告对象
   44. const adLoader: advertising.AdLoader = new advertising.AdLoader(this.context);
   45. try {
   46. // 调用广告请求接口
   47. adLoader.loadAdWithMultiSlots(adRequestParamsArray, adOptions, multiSlotsAdLoaderListener);
   48. } catch (e) {
   49. hilog.error(0x0000, 'testTag', `Failed to load multiSlots ad. Code is ${e.code}, message is ${e.message}`);
   50. }
   51. }

   53. build() {
   54. // ...
   55. }

   57. // ...
   58. }

   60. async function requestOAID(context: Context): Promise<string | undefined> {
   61. // 向用户请求授权广告跨应用关联访问权限
   62. let isPermissionGranted: boolean = false;
   63. try {
   64. const atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
   65. const result: PermissionRequestResult =
   66. await atManager.requestPermissionsFromUser(context, ['ohos.permission.APP_TRACKING_CONSENT']);
   67. isPermissionGranted = result.authResults[0] === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED;
   68. } catch (err) {
   69. hilog.error(0x0000, 'testTag', `Failed to request permission. Code is ${err.code}, message is ${err.message}`);
   70. }
   71. if (isPermissionGranted) {
   72. hilog.info(0x0000, 'testTag', 'Succeeded in requesting permission');
   73. try {
   74. const oaid = await identifier.getOAID();
   75. hilog.info(0x0000, 'testTag', 'Succeeded in getting OAID');
   76. return oaid;
   77. } catch (err) {
   78. hilog.error(0x0000, 'testTag', `Failed to get OAID. Code is ${err.code}, message is ${err.message}`);
   79. }
   80. } else {
   81. hilog.error(0x0000, 'testTag', 'Failed to request permission. User rejected');
   82. }
   83. return undefined;
   84. }
   ```

### 展示广告

1. 导入相关模块。

   ```
   1. import { AdComponent, advertising } from '@kit.AdsKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 展示广告。

   展示广告通过[AdInteractionListener](../harmonyos-references/js-apis-advertising.md#adinteractionlistener)监听广告状态回调，涉及的回调状态如下所示：

   | 回调状态 | 说明 | 使用建议 |
   | --- | --- | --- |
   | onAdOpen | 打开广告。 | - |
   | onAdClick | 点击广告。 | - |
   | onAdClose | 关闭广告。 | 用户点击负反馈或关闭广告时触发，需要将广告组件隐藏。回调状态包含了具体的关闭原因，详情见：[data说明](../harmonyos-references/js-apis-advertising.md#onstatuschanged)。 |
   | onAdFail | 广告加载失败。 | 广告展示失败时触发，需要将广告组件隐藏。 |

   原生信息流广告通常不需要显式设置广告展示组件[AdComponent](../harmonyos-references/js-apis-adcomponent.md)的高度，组件会自动调整高度以适应需要展示的内容。

   示例代码如下所示：

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. @State ads: advertising.Advertisement[] = [];
   5. @State visibilityState: Visibility = Visibility.Visible;
   6. // ...

   8. build() {
   9. Column() {
   10. if (this.ads.length > 0) {
   11. this.inFeedNativeAd(this.ads[0])
   12. // ...
   13. }
   14. }
   15. .width('100%')
   16. .height('100%')
   17. }

   19. @Builder
   20. inFeedNativeAd(ad: advertising.Advertisement): void {
   21. Row() {
   22. AdComponent({
   23. ads: [ad],
   24. // 广告展示参数，开发者可根据项目实际情况设置
   25. displayOptions: {
   26. // 是否静音
   27. mute: true
   28. },
   29. interactionListener: {
   30. onStatusChanged: (status: string, ad: advertising.Advertisement, data: string) => {
   31. switch (status) {
   32. case 'onAdOpen':
   33. hilog.info(0x0000, 'testTag', 'Status is onAdOpen');
   34. break;
   35. case 'onAdClick':
   36. hilog.info(0x0000, 'testTag', 'Status is onAdClick');
   37. break;
   38. case 'onAdClose':
   39. hilog.info(0x0000, 'testTag', 'Status is onAdClose');
   40. this.visibilityState = Visibility.None;
   41. break;
   42. case 'onAdFail':
   43. hilog.error(0x0000, 'testTag', 'Status is onAdFail');
   44. this.visibilityState = Visibility.None;
   45. break;
   46. }
   47. }
   48. }
   49. })
   50. // 原生信息流样式，不建议设置高度，宽度建议设置为100%，撑满父容器
   51. .width('100%')
   52. }
   53. .width('100%')
   54. .padding({ left: 16, right: 16 })
   55. .visibility(this.visibilityState)
   56. }

   58. // ...
   59. }
   ```

   原生插图广告宽高为固定值312vp\*284vp，开发者可以将广告展示组件[AdComponent](../harmonyos-references/js-apis-adcomponent.md)居中展示。

   示例代码如下所示：

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. @State ads: advertising.Advertisement[] = [];
   5. @State visibilityState: Visibility = Visibility.Visible;
   6. // ...

   8. build() {
   9. Column() {
   10. if (this.ads.length > 0) {
   11. // ...
   12. this.nativeCardAd(this.ads[0])
   13. }
   14. }
   15. .width('100%')
   16. .height('100%')
   17. }

   19. // ...

   21. @Builder
   22. nativeCardAd(ad: advertising.Advertisement): void {
   23. Row() {
   24. AdComponent({
   25. ads: [ad],
   26. // 广告展示参数，开发者可根据项目实际情况设置
   27. displayOptions: {
   28. // 是否静音
   29. mute: true
   30. },
   31. interactionListener: {
   32. onStatusChanged: (status: string, ad: advertising.Advertisement, data: string) => {
   33. switch (status) {
   34. case 'onAdOpen':
   35. hilog.info(0x0000, 'testTag', 'Status is onAdOpen');
   36. break;
   37. case 'onAdClick':
   38. hilog.info(0x0000, 'testTag', 'Status is onAdClick');
   39. break;
   40. case 'onAdClose':
   41. hilog.info(0x0000, 'testTag', 'Status is onAdClose');
   42. this.visibilityState = Visibility.None;
   43. break;
   44. case 'onAdFail':
   45. hilog.error(0x0000, 'testTag', 'Status is onAdFail');
   46. this.visibilityState = Visibility.None;
   47. break;
   48. }
   49. }
   50. }
   51. })
   52. // 原生插图样式，宽高为固定值，为312vp*284vp
   53. .width(312)
   54. .height(284)
   55. }
   56. .width('100%')
   57. // 宽高固定无法撑满父容器，将广告居中展示
   58. .justifyContent(FlexAlign.Center)
   59. .visibility(this.visibilityState)
   60. }
   61. }
   ```

## 测试原生广告

原生广告测试广告位ID，仅可用于调测原生广告功能，不可用于广告变现，在应用正式发布前需替换为正式的原生广告位ID。您应在应用发布前先进入[流量变现官网](https://developer.huawei.com/consumer/cn/monetize)，点击“开始变现”，登录[鲸鸿动能媒体服务平台](https://developer.huawei.com/consumer/cn/service/ads/publisher/html/index.html?lang=zh)，申请正式的广告位ID并替换测试广告位ID，具体操作详情请参见[展示位创建](../distribution/monetize/zhanshiweichuangjian-0000001132700049.md)。

原生广告测试广告位ID列表如下：

| 广告位类型 | 测试广告位ID | 展示形式 | 比例 | 推广类型 |
| --- | --- | --- | --- | --- |
| 原生 | h8asowxwhq | 大图 | 16:9 | 网页推广 |
| 原生 | k94abyn2z4 | 小图 | 4:3 | 应用下载 |
| 原生 | o7dj7qsbvy | 三图 | 4:3 | 应用促活 |
| 原生 | s7moc0jc6m | 视频 | 16:9 | 应用下载 |
