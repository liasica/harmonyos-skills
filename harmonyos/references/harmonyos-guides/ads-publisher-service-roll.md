---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ads-publisher-service-roll
title: 贴片广告
breadcrumb: 指南 > 应用服务 > Ads Kit（广告服务） > 流量变现服务开发 > 贴片广告
category: harmonyos-guides
scraped_at: 2026-04-29T13:37:05+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:9c26f85382e93eef5264a110a2b85b2835bcc5558af3d44515d179601dd68e6d
---

## 场景介绍

贴片广告是一种在视频播放前、视频播放中或视频播放结束后插入的视频或图片广告。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/XpdXIsP8SQKkkTo3fexDKQ/zh-cn_image_0000002589325139.png?HW-CC-KV=V1&HW-CC-Date=20260429T053704Z&HW-CC-Expire=86400&HW-CC-Sign=90CDED09CBCB01319D8F1CC0693A1D9D715C32E5AC28D7A0EFA202DB83A5F793)

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
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 获取OAID。

   若需提升广告推送精准度，可以在请求参数[AdRequestParams](../harmonyos-references/js-apis-advertising.md#adrequestparams)中添加oaid属性。

   如何获取OAID参见[获取OAID信息](oaid-service.md)。

   说明

   使用以下示例中提供的测试广告位时，必须先获取OAID信息。
3. 请求单广告位广告。

   需要创建一个AdLoader对象，通过AdLoader的[loadAd](../harmonyos-references/js-apis-advertising.md#loadad)方法请求广告，最后通过[AdLoadListener](../harmonyos-references/js-apis-advertising.md#adloadlistener)来监听广告的加载状态。

   在请求贴片广告时，需要在[AdOptions](../harmonyos-references/js-apis-advertising.md#adoptions)中设置参数：totalDuration。

   请求广告关键参数如下所示：

   | 请求广告参数名 | 类型 | 必填 | 说明 |
   | --- | --- | --- | --- |
   | adType | number | 是 | 请求广告类型，贴片广告类型为60。 |
   | adId | string | 是 | 广告位ID。  - 如果仅调测广告，可使用测试广告位ID：o2e960bnfz。  - 如果要接入正式广告，则需要申请正式的广告位ID。可在应用发布前进入[流量变现官网](https://developer.huawei.com/consumer/cn/monetize)，点击“开始变现”，登录[鲸鸿动能媒体服务平台](https://developer.huawei.com/consumer/cn/service/ads/publisher/html/index.html?lang=zh)进行申请，具体操作详情请参见[展示位创建](../monetize/zhanshiweichuangjian-0000001132700049.md)。 |
   | oaid | string | 否 | 开放匿名设备标识符，用于精准推送广告。不填无法获取到个性化广告。 |

   示例代码如下所示：

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. // 请求到的广告内容
   5. @State ads: advertising.Advertisement[] = [];
   6. // ...
   7. private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

   9. aboutToAppear(): void {
   10. // 调用loadAd加载广告
   11. void this.loadAd().catch((error: BusinessError) => {
   12. hilog.error(0x0000, 'testTag', `Failed to loadAd. Code is ${error.code}, message is ${error.message}`);
   13. });
   14. }

   16. // ...

   18. build() {
   19. // ...
   20. }

   22. // ...

   24. private async loadAd(): Promise<void> {
   25. // 广告请求回调监听
   26. const adLoadListener: advertising.AdLoadListener = {
   27. onAdLoadFailure: (errorCode: number, errorMsg: string) => {
   28. hilog.error(0x0000, 'testTag', `Failed to load ad. Code is ${errorCode}, message is ${errorMsg}`);
   29. },
   30. onAdLoadSuccess: (ads: Array<advertising.Advertisement>) => {
   31. hilog.info(0x0000, 'testTag', 'Succeeded in loading ad');
   32. this.ads = ads;
   33. }
   34. };
   35. // 广告请求参数
   36. const adRequestParams: advertising.AdRequestParams = {
   37. // 'o2e960bnfz'为测试专用的广告位ID，App正式发布时需要改为正式的广告位ID
   38. adId: 'o2e960bnfz',
   39. // 贴片广告类型
   40. adType: 60,
   41. // 用于区分普通在线请求和素材预加载请求 true: 素材预加载请求 false: 普通在线请求
   42. isPreload: false,
   43. // 开放匿名设备标识符
   44. oaid: await requestOAID(this.context)
   45. };
   46. // 广告配置参数，开发者可根据项目实际情况设置
   47. const adOptions: advertising.AdOptions = {
   48. // 设置贴片广告展示时长（贴片广告必填）
   49. totalDuration: 30
   50. };
   51. // 创建AdLoader广告对象
   52. const adLoader: advertising.AdLoader = new advertising.AdLoader(this.context);
   53. try {
   54. // 调用广告请求接口
   55. adLoader.loadAd(adRequestParams, adOptions, adLoadListener);
   56. } catch (e) {
   57. hilog.error(0x0000, 'testTag', `Failed to load ad. Code is ${e.code}, message is ${e.message}`);
   58. }
   59. }
   60. }

   62. async function requestOAID(context: Context): Promise<string | undefined> {
   63. // 向用户请求授权广告跨应用关联访问权限
   64. let isPermissionGranted: boolean = false;
   65. try {
   66. const atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
   67. const result: PermissionRequestResult =
   68. await atManager.requestPermissionsFromUser(context, ['ohos.permission.APP_TRACKING_CONSENT']);
   69. isPermissionGranted = result.authResults[0] === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED;
   70. } catch (err) {
   71. hilog.error(0x0000, 'testTag', `Failed to request permission. Code is ${err.code}, message is ${err.message}`);
   72. }
   73. if (isPermissionGranted) {
   74. hilog.info(0x0000, 'testTag', 'Succeeded in requesting permission');
   75. try {
   76. const oaid = await identifier.getOAID();
   77. hilog.info(0x0000, 'testTag', 'Succeeded in getting OAID');
   78. return oaid;
   79. } catch (err) {
   80. hilog.error(0x0000, 'testTag', `Failed to get OAID. Code is ${err.code}, message is ${err.message}`);
   81. }
   82. } else {
   83. hilog.error(0x0000, 'testTag', 'Failed to request permission. User rejected');
   84. }
   85. return undefined;
   86. }
   ```

### 展示广告

1. 导入相关模块。

   ```
   1. import { common } from '@kit.AbilityKit';
   2. import { AdComponent, advertising } from '@kit.AdsKit';
   3. import { window } from '@kit.ArkUI';
   4. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 展示广告。

   展示广告通过[AdInteractionListener](../harmonyos-references/js-apis-advertising.md#adinteractionlistener)监听广告状态回调，涉及的回调状态如下所示：

   | 回调状态 | 说明 | 扩展信息 | 使用建议 |
   | --- | --- | --- | --- |
   | onAdFail | 广告加载失败。 | - | 广告展示失败时触发，需要将广告组件隐藏，播放正片。 |
   | onPortrait | 全屏状态下点击返回按钮。 | - | 用户在全屏状态下点击返回按钮时触发，需要设置屏幕方向为竖屏，按需显示导航栏、状态栏、底部导航条和设置广告组件宽高。 |
   | onLandscape | 竖屏状态下点击全屏按钮。 | - | 用户在竖屏状态下点击全屏按钮时触发，需要设置屏幕方向为横屏，按需隐藏导航栏、状态栏、底部导航条和设置广告组件宽高。 |
   | onMediaProgress | 广告播放进度。 | - playTime：类型number，单位ms，广告播放时长。  - percentage：类型number，单位百分比，广告播放进度。 | - |
   | onMediaStart | 广告开始播放。 | - playTime：类型number，单位ms，广告播放时长。 | - |
   | onMediaPause | 广告暂停播放。 | - playTime：类型number，单位ms，广告播放时长。 | - |
   | onMediaStop | 广告停止播放。 | - playTime：类型number，单位ms，广告播放时长。 | - |
   | onMediaComplete | 广告播放完成。 | - playTime：类型number，单位ms，广告播放时长。 | 单个广告播放完成时触发，当所有广告播放完成后，需要将广告组件隐藏，播放正片。 |
   | onMediaError | 广告播放失败。 | - playTime：类型number，单位ms，广告播放时长，-1为异常值。  - errorCode：类型number，错误码ID。  - errorMsg：类型string，错误信息。  错误码的详细介绍请参见AVPlayer.[on('error')](../harmonyos-references/arkts-apis-media-avplayer.md#onerror9)错误码。 | - |
   | onMediaCountdown | 广告倒计时。 | - countdownTime：类型number，单位s，倒计时时长。 | 广告倒计时时触发，需要根据扩展信息的倒计时时长绘制倒计时控件。 |
   | onBackClicked | 点击返回按钮。 | - | 用户在非全屏状态下或系统锁定全屏状态下点击返回按钮时触发，需要返回上一页面。 |

   在您的页面中使用AdComponent组件展示贴片广告。以前贴广告为例，前贴广告播放完成后进入正片播放。

   示例代码如下所示：

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. // 请求到的广告内容
   5. @State ads: advertising.Advertisement[] = [];
   6. // 倒计时文案
   7. @State countDownText: string = '';
   8. // 贴片广告播放状态
   9. @State rollPlayState: number = 1;
   10. // 是否播放正片
   11. @State isPlayVideo: boolean = false;
   12. // 视频宽高比
   13. @State ratio: number = 16 / 9;
   14. // 广告展示参数，开发者可根据项目实际情况设置
   15. private adDisplayOptions: advertising.AdDisplayOptions = {
   16. // 是否静音
   17. mute: true
   18. };
   19. // 已经播放的贴片广告数量
   20. private playedAdSize: number = 0;
   21. // 用于渲染右上角倒计时
   22. private countDownTxtPlaceholder: string = '%d | VIP免广告';
   23. private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

   25. // ...

   27. aboutToDisappear(): void {
   28. // 设置屏幕方向为默认值，开发者可根据项目实际情况修改
   29. void this.setWindowPreferredOrientation(window.Orientation.UNSPECIFIED).catch((error: BusinessError) => {
   30. hilog.error(0x0000, 'testTag',
   31. `Failed to setWindowPreferredOrientation. Code is ${error.code}, message is ${error.message}`);
   32. });
   33. // 显示导航栏、状态栏、底部导航条，开发者可根据项目实际情况修改
   34. void this.setWindowSystemBar(['status', 'navigation']).catch((error: BusinessError) => {
   35. hilog.error(0x0000, 'testTag',
   36. `Failed to setWindowSystemBar. Code is ${error.code}, message is ${error.message}`);
   37. });
   38. }

   40. build() {
   41. Stack({ alignContent: Alignment.TopEnd }) {
   42. if (!this.isPlayVideo && this.ads.length > 0) {
   43. AdComponent({
   44. ads: [...this.ads],
   45. rollPlayState: this.rollPlayState,
   46. displayOptions: this.adDisplayOptions,
   47. interactionListener: {
   48. // 广告状态变化回调
   49. onStatusChanged: (status: string, ad: advertising.Advertisement, data: string) => {
   50. switch (status) {
   51. case 'onAdFail':
   52. hilog.error(0x0000, 'testTag', 'Status is onAdFail');
   53. this.isPlayVideo = true;
   54. break;
   55. case 'onPortrait':
   56. hilog.info(0x0000, 'testTag', 'Status is onPortrait');
   57. // 设置屏幕方向为竖屏
   58. void this.setWindowPreferredOrientation(window.Orientation.PORTRAIT).catch((error: BusinessError) => {
   59. hilog.error(0x0000, 'testTag',
   60. `Failed to setWindowPreferredOrientation. Code is ${error.code}, message is ${error.message}`);
   61. });
   62. // 显示导航栏、状态栏、底部导航条
   63. void this.setWindowSystemBar(['status', 'navigation']).catch((error: BusinessError) => {
   64. hilog.error(0x0000, 'testTag',
   65. `Failed to setWindowSystemBar. Code is ${error.code}, message is ${error.message}`);
   66. });
   67. // 竖屏时还原宽高比
   68. this.ratio = 16 / 9;
   69. break;
   70. case 'onLandscape':
   71. hilog.info(0x0000, 'testTag', 'Status is onLandscape');
   72. // 设置屏幕方向为横屏
   73. void this.setWindowPreferredOrientation(window.Orientation.LANDSCAPE).catch((error: BusinessError) => {
   74. hilog.error(0x0000, 'testTag',
   75. `Failed to setWindowPreferredOrientation. Code is ${error.code}, message is ${error.message}`);
   76. });
   77. // 隐藏导航栏、状态栏、底部导航条
   78. void this.setWindowSystemBar([]).catch((error: BusinessError) => {
   79. hilog.error(0x0000, 'testTag',
   80. `Failed to setWindowSystemBar. Code is ${error.code}, message is ${error.message}`);
   81. });
   82. // 横屏时忽略宽高比
   83. this.ratio = -1;
   84. break;
   85. case 'onMediaProgress':
   86. hilog.info(0x0000, 'testTag', 'Status is onMediaProgress');
   87. break;
   88. case 'onMediaStart':
   89. hilog.info(0x0000, 'testTag', 'Status is onMediaStart');
   90. break;
   91. case 'onMediaPause':
   92. hilog.info(0x0000, 'testTag', 'Status is onMediaPause');
   93. break;
   94. case 'onMediaStop':
   95. hilog.info(0x0000, 'testTag', 'Status is onMediaStop');
   96. break;
   97. case 'onMediaComplete':
   98. hilog.info(0x0000, 'testTag', 'Status is onMediaComplete');
   99. // 所有广告都播放完毕后，开始播放正片
   100. this.playedAdSize++;
   101. if (this.playedAdSize === this.ads.length) {
   102. this.isPlayVideo = true;
   103. }
   104. break;
   105. case 'onMediaError':
   106. hilog.error(0x0000, 'testTag', 'Status is onMediaError');
   107. break;
   108. case 'onMediaCountdown':
   109. hilog.info(0x0000, 'testTag', 'Status is onMediaCountdown');
   110. const parseData: Record<string, Object> = this.safeParseData(data);
   111. this.countDownText = this.countDownTxtPlaceholder.replace('%d', String(parseData.countdownTime));
   112. break;
   113. case 'onBackClicked':
   114. hilog.info(0x0000, 'testTag', 'Status is onBackClicked');
   115. this.getUIContext().getRouter().back();
   116. break;
   117. }
   118. }
   119. }
   120. })
   121. .visibility(!this.isPlayVideo ? Visibility.Visible : Visibility.None)
   122. .width('100%')
   123. .height('100%')

   125. Text(this.countDownText)
   126. .fontSize(12)
   127. .lineHeight(12)
   128. .maxLines(1)
   129. .textAlign(TextAlign.Center)
   130. .fontColor(Color.White)
   131. .textOverflow({ overflow: TextOverflow.Ellipsis })
   132. .backgroundColor('#66000000')
   133. .border({ radius: 25 })
   134. .padding(8)
   135. .margin(16)
   136. .height(24)
   137. .onClick(() => {
   138. hilog.info(0x0000, 'testTag', 'OnVipClicked, do something...');
   139. this.isPlayVideo = true;
   140. })
   141. .visibility(this.countDownText ? Visibility.Visible : Visibility.None)
   142. }

   144. Video({
   145. // 广告后播放的视频，开发者需根据项目实际情况设置
   146. src: $rawfile('videoTest.mp4'),
   147. // 播放视频的预览图，开发者需根据项目实际情况设置
   148. previewUri: $r('app.media.video_preview'),
   149. controller: new VideoController()
   150. })
   151. .visibility(this.isPlayVideo ? Visibility.Visible : Visibility.None)
   152. .autoPlay(this.isPlayVideo)
   153. .controls(false)
   154. .width('100%')
   155. .height('100%')
   156. }
   157. .width('100%')
   158. .height('100%')
   159. .aspectRatio(this.ratio)
   160. }

   162. private async setWindowPreferredOrientation(orientation: Orientation): Promise<void> {
   163. try {
   164. const win: window.Window = await window.getLastWindow(this.context);
   165. await win.setPreferredOrientation(orientation);
   166. } catch (e) {
   167. hilog.error(0x0000, 'testTag', `Failed to set preferred orientation. Code is ${e.code}, message is ${e.message}`);
   168. }
   169. }

   171. private async setWindowSystemBar(names: Array<'status' | 'navigation'>): Promise<void> {
   172. try {
   173. const win: window.Window = await window.getLastWindow(this.context);
   174. await win.setWindowSystemBarEnable(names);
   175. } catch (e) {
   176. hilog.error(0x0000, 'testTag', `Failed to set window system bar. Code is ${e.code}, message is ${e.message}`);
   177. }
   178. }

   180. private safeParseData(data: string): Record<string, Object> {
   181. try {
   182. if (typeof data === 'string') {
   183. return JSON.parse(data);
   184. }
   185. return JSON.parse(JSON.stringify(data));
   186. } catch (e) {
   187. hilog.error(0x0000, 'testTag', `Failed to parse data. Code is ${e.code}, message is ${e.message}`);
   188. }
   189. return {};
   190. }

   192. // ...
   193. }
   ```

## 测试贴片广告

测试贴片广告时，需要使用专门的测试广告位ID来获取测试广告，以避免在测试过程中产生无效的广告点击量。

测试广告位ID仅作为功能调试使用，不可用于广告变现。您应在应用发布前先进入[流量变现官网](https://developer.huawei.com/consumer/cn/monetize)，点击“开始变现”，登录[鲸鸿动能媒体服务平台](https://developer.huawei.com/consumer/cn/service/ads/publisher/html/index.html?lang=zh)，申请正式的广告位ID并替换测试广告位ID，具体操作详情请参见[展示位创建](../distribution/monetize/zhanshiweichuangjian-0000001132700049.md)。

以下表格中提供了贴片广告的专用测试广告位ID：

| 广告位类型 | 测试广告位ID | 展示形式 | 比例 | 推广类型 |
| --- | --- | --- | --- | --- |
| 贴片 | o2e960bnfz | 视频 | 16:9 | 应用下载 |
