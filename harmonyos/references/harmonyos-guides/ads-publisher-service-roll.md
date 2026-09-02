---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ads-publisher-service-roll
title: 贴片广告
breadcrumb: 指南 > 应用服务 > Ads Kit（广告服务） > 流量变现服务开发 > 贴片广告
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:52+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:941cc238fc02d51f54a326b9e772bdc6beb551bf92f58198733c6c931055dfd8
---

## 场景介绍

贴片广告是一种在视频播放前、视频播放中或视频播放结束后插入的视频或图片广告。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/Va7VCQWZQTKlpwdpanCSmw/zh-cn_image_0000002736433933.png)

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

   ```typescript
   import { abilityAccessCtrl, common, PermissionRequestResult } from '@kit.AbilityKit';
   import { AdComponent, advertising, identifier } from '@kit.AdsKit';
   // ...
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 获取OAID。

   若需提升广告推送精准度，可以在请求参数[AdRequestParams](../harmonyos-references/js-apis-advertising.md#adrequestparams)中添加oaid属性。

   如何获取OAID参见[获取OAID信息](oaid-service.md)。

   **说明** 

   使用以下示例中提供的测试广告位时，必须先获取OAID信息。
3. 请求单广告位广告。

   需要创建一个AdLoader对象，通过AdLoader的[loadAd](../harmonyos-references/js-apis-advertising.md#loadad)方法请求广告，最后通过[AdLoadListener](../harmonyos-references/js-apis-advertising.md#adloadlistener)来监听广告的加载状态。

   在请求贴片广告时，需要在[AdOptions](../harmonyos-references/js-apis-advertising.md#adoptions)中设置参数：totalDuration。

   请求广告关键参数如下所示：

   | 请求广告参数名 | 类型 | 必填 | 说明 |
   | --- | --- | --- | --- |
   | adType | number | 否 | 请求广告类型，贴片广告类型为60。不填默认为原生广告类型。 |
   | adId | string | 是 | 广告位ID。  - 如果仅调测广告，可使用测试广告位ID：o2e960bnfz。  - 如果要接入正式广告，则需要申请正式的广告位ID。可在应用发布前进入[流量变现官网](https://developer.huawei.com/consumer/cn/monetize)，点击“开始变现”，登录[鲸鸿动能媒体服务平台](https://developer.huawei.com/consumer/cn/service/ads/publisher/html/index.html?lang=zh)进行申请，具体操作详情请参见[展示位创建](../monetize/zhanshiweichuangjian-0000001132700049.md)。 |
   | oaid | string | 否 | 开放匿名设备标识符，用于精准推送广告。不填无法获取到个性化广告。 |

   示例代码如下所示：

   ```typescript
   @Entry
   @Component
   struct Index {
     // 请求到的广告内容
     @State ads: advertising.Advertisement[] = [];
     // ...
     private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

     aboutToAppear(): void {
       // 调用loadAd加载广告
       void this.loadAd().catch((error: BusinessError) => {
         hilog.error(0x0000, 'testTag', `Failed to loadAd. Code is ${error.code}, message is ${error.message}`);
       });
     }

     // ...

     build() {
       // ...
     }

     // ...

     private async loadAd(): Promise<void> {
       // 广告请求回调监听
       const adLoadListener: advertising.AdLoadListener = {
         onAdLoadFailure: (errorCode: number, errorMsg: string) => {
           hilog.error(0x0000, 'testTag', `Failed to load ad. Code is ${errorCode}, message is ${errorMsg}`);
         },
         onAdLoadSuccess: (ads: Array<advertising.Advertisement>) => {
           hilog.info(0x0000, 'testTag', 'Succeeded in loading ad');
           this.ads = ads;
         }
       };
       // 广告请求参数
       const adRequestParams: advertising.AdRequestParams = {
         // 'o2e960bnfz'为测试专用的广告位ID，App正式发布时需要改为正式的广告位ID
         adId: 'o2e960bnfz',
         // 贴片广告类型
         adType: 60,
         // 用于区分普通在线请求和素材预加载请求 true: 素材预加载请求 false: 普通在线请求
         isPreload: false,
         // 开放匿名设备标识符
         oaid: await requestOAID(this.context)
       };
       // 广告配置参数，开发者可根据项目实际情况设置
       const adOptions: advertising.AdOptions = {
         // 设置贴片广告展示时长（贴片广告必填）
         totalDuration: 30
       };
       // 创建AdLoader广告对象
       const adLoader: advertising.AdLoader = new advertising.AdLoader(this.context);
       try {
         // 调用广告请求接口
         adLoader.loadAd(adRequestParams, adOptions, adLoadListener);
       } catch (e) {
         hilog.error(0x0000, 'testTag', `Failed to load ad. Code is ${e.code}, message is ${e.message}`);
       }
     }
   }

   async function requestOAID(context: Context): Promise<string | undefined> {
     // 向用户请求授权广告跨应用关联访问权限
     let isPermissionGranted: boolean = false;
     try {
       const atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
       const result: PermissionRequestResult =
         await atManager.requestPermissionsFromUser(context, ['ohos.permission.APP_TRACKING_CONSENT']);
       isPermissionGranted = result.authResults[0] === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED;
     } catch (err) {
       hilog.error(0x0000, 'testTag', `Failed to request permission. Code is ${err.code}, message is ${err.message}`);
     }
     if (isPermissionGranted) {
       hilog.info(0x0000, 'testTag', 'Succeeded in requesting permission');
       try {
         const oaid = await identifier.getOAID();
         hilog.info(0x0000, 'testTag', 'Succeeded in getting OAID');
         return oaid;
       } catch (err) {
         hilog.error(0x0000, 'testTag', `Failed to get OAID. Code is ${err.code}, message is ${err.message}`);
       }
     } else {
       hilog.error(0x0000, 'testTag', 'Failed to request permission. User rejected');
     }
     return undefined;
   }
   ```

### 展示广告

1. 导入相关模块。

   ```typescript
   import { abilityAccessCtrl, common, PermissionRequestResult } from '@kit.AbilityKit';
   import { AdComponent, advertising, identifier } from '@kit.AdsKit';
   import { window } from '@kit.ArkUI';
   import { hilog } from '@kit.PerformanceAnalysisKit';
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
   | onAdClick | 点击广告。 | - | - |

   在您的页面中使用AdComponent组件展示贴片广告。以前贴广告为例，前贴广告播放完成后进入正片播放。

   示例代码如下所示：

   ```typescript
   @Entry
   @Component
   struct Index {
     // 请求到的广告内容
     @State ads: advertising.Advertisement[] = [];
     // 倒计时文案
     @State countDownText: string = '';
     // 贴片广告播放状态
     @State rollPlayState: number = 1;
     // 是否播放正片
     @State isPlayVideo: boolean = false;
     // 视频宽高比
     @State ratio: number = 16 / 9;
     // 广告展示参数，开发者可根据项目实际情况设置
     private adDisplayOptions: advertising.AdDisplayOptions = {
       // 是否静音
       mute: true
     };
     // 已经播放的贴片广告数量
     private playedAdSize: number = 0;
     // 用于渲染右上角倒计时
     private countDownTxtPlaceholder: string = '%d | VIP免广告';
     private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

     // ...

     aboutToDisappear(): void {
       // 设置屏幕方向为默认值，开发者可根据项目实际情况修改
       void this.setWindowPreferredOrientation(window.Orientation.UNSPECIFIED).catch((error: BusinessError) => {
         hilog.error(0x0000, 'testTag',
           `Failed to setWindowPreferredOrientation. Code is ${error.code}, message is ${error.message}`);
       });
       // 显示导航栏、状态栏、底部导航条，开发者可根据项目实际情况修改
       void this.setWindowSystemBar(['status', 'navigation']).catch((error: BusinessError) => {
         hilog.error(0x0000, 'testTag',
           `Failed to setWindowSystemBar. Code is ${error.code}, message is ${error.message}`);
       });
     }

     build() {
       Stack({ alignContent: Alignment.TopEnd }) {
         if (!this.isPlayVideo && this.ads.length > 0) {
           AdComponent({
             ads: [...this.ads],
             rollPlayState: this.rollPlayState,
             displayOptions: this.adDisplayOptions,
             interactionListener: {
               // 广告状态变化回调
               onStatusChanged: (status: string, ad: advertising.Advertisement, data: string) => {
                 switch (status) {
                   case 'onAdFail':
                     hilog.error(0x0000, 'testTag', 'Status is onAdFail');
                     this.isPlayVideo = true;
                     break;
                   case 'onPortrait':
                     hilog.info(0x0000, 'testTag', 'Status is onPortrait');
                     // 设置屏幕方向为竖屏
                     void this.setWindowPreferredOrientation(window.Orientation.PORTRAIT).catch((error: BusinessError) => {
                       hilog.error(0x0000, 'testTag',
                         `Failed to setWindowPreferredOrientation. Code is ${error.code}, message is ${error.message}`);
                     });
                     // 显示导航栏、状态栏、底部导航条
                     void this.setWindowSystemBar(['status', 'navigation']).catch((error: BusinessError) => {
                       hilog.error(0x0000, 'testTag',
                         `Failed to setWindowSystemBar. Code is ${error.code}, message is ${error.message}`);
                     });
                     // 竖屏时还原宽高比
                     this.ratio = 16 / 9;
                     break;
                   case 'onLandscape':
                     hilog.info(0x0000, 'testTag', 'Status is onLandscape');
                     // 设置屏幕方向为横屏
                     void this.setWindowPreferredOrientation(window.Orientation.LANDSCAPE)
                       .catch((error: BusinessError) => {
                       hilog.error(0x0000, 'testTag',
                         `Failed to setWindowPreferredOrientation. Code is ${error.code}, message is ${error.message}`);
                     });
                     // 隐藏导航栏、状态栏、底部导航条
                     void this.setWindowSystemBar([]).catch((error: BusinessError) => {
                       hilog.error(0x0000, 'testTag',
                         `Failed to setWindowSystemBar. Code is ${error.code}, message is ${error.message}`);
                     });
                     // 横屏时忽略宽高比
                     this.ratio = -1;
                     break;
                   case 'onMediaProgress':
                     hilog.info(0x0000, 'testTag', 'Status is onMediaProgress');
                     break;
                   case 'onMediaStart':
                     hilog.info(0x0000, 'testTag', 'Status is onMediaStart');
                     break;
                   case 'onMediaPause':
                     hilog.info(0x0000, 'testTag', 'Status is onMediaPause');
                     break;
                   case 'onMediaStop':
                     hilog.info(0x0000, 'testTag', 'Status is onMediaStop');
                     break;
                   case 'onMediaComplete':
                     hilog.info(0x0000, 'testTag', 'Status is onMediaComplete');
                     // 所有广告都播放完毕后，开始播放正片
                     this.playedAdSize++;
                     if (this.playedAdSize === this.ads.length) {
                       this.isPlayVideo = true;
                     }
                     break;
                   case 'onMediaError':
                     hilog.error(0x0000, 'testTag', 'Status is onMediaError');
                     break;
                   case 'onMediaCountdown':
                     hilog.info(0x0000, 'testTag', 'Status is onMediaCountdown');
                     const parseData: Record<string, Object> = this.safeParseData(data);
                     this.countDownText = this.countDownTxtPlaceholder.replace('%d', String(parseData.countdownTime));
                     break;
                   case 'onBackClicked':
                     hilog.info(0x0000, 'testTag', 'Status is onBackClicked');
                     this.getUIContext().getRouter().back();
                     break;
                   case 'onAdClick':
                     hilog.info(0x0000, 'testTag', 'Status is onAdClick');
                     break;
                   default:
                     break;
                 }
               }
             }
           })
             .visibility(!this.isPlayVideo ? Visibility.Visible : Visibility.None)
             .width('100%')
             .height('100%')

           Text(this.countDownText)
             .fontSize(12)
             .lineHeight(12)
             .maxLines(1)
             .textAlign(TextAlign.Center)
             .fontColor(Color.White)
             .textOverflow({ overflow: TextOverflow.Ellipsis })
             .backgroundColor('#66000000')
             .border({ radius: 25 })
             .padding(8)
             .margin(16)
             .height(24)
             .onClick(() => {
               hilog.info(0x0000, 'testTag', 'OnVipClicked, do something...');
               this.isPlayVideo = true;
             })
             .visibility(this.countDownText ? Visibility.Visible : Visibility.None)
         }

         Video({
           // 广告后播放的视频，开发者需根据项目实际情况设置
           src: $rawfile('videoTest.mp4'),
           // 播放视频的预览图，开发者需根据项目实际情况设置
           previewUri: $r('app.media.video_preview'),
           controller: new VideoController()
         })
           .visibility(this.isPlayVideo ? Visibility.Visible : Visibility.None)
           .autoPlay(this.isPlayVideo)
           .controls(false)
           .width('100%')
           .height('100%')
       }
       .width('100%')
       .height('100%')
       .aspectRatio(this.ratio)
     }

     private async setWindowPreferredOrientation(orientation: Orientation): Promise<void> {
       try {
         const win: window.Window = await window.getLastWindow(this.context);
         await win.setPreferredOrientation(orientation);
       } catch (e) {
         hilog.error(0x0000, 'testTag', `Failed to set preferred orientation. Code is ${e.code}, message is ${e.message}`);
       }
     }

     private async setWindowSystemBar(names: Array<'status' | 'navigation'>): Promise<void> {
       try {
         const win: window.Window = await window.getLastWindow(this.context);
         await win.setWindowSystemBarEnable(names);
       } catch (e) {
         hilog.error(0x0000, 'testTag', `Failed to set window system bar. Code is ${e.code}, message is ${e.message}`);
       }
     }

     private safeParseData(data: string): Record<string, Object> {
       try {
         if (typeof data === 'string') {
           return JSON.parse(data);
         }
         return JSON.parse(JSON.stringify(data));
       } catch (e) {
         hilog.error(0x0000, 'testTag', `Failed to parse data. Code is ${e.code}, message is ${e.message}`);
       }
       return {};
     }

     // ...
   }
   ```

## 测试贴片广告

测试贴片广告时，需要使用专门的测试广告位ID来获取测试广告，以避免在测试过程中产生无效的广告点击量。

测试广告位ID仅作为功能调试使用，不可用于广告变现。您应在应用发布前先进入[流量变现官网](https://developer.huawei.com/consumer/cn/monetize)，点击“开始变现”，登录[鲸鸿动能媒体服务平台](https://developer.huawei.com/consumer/cn/service/ads/publisher/html/index.html?lang=zh)，申请正式的广告位ID并替换测试广告位ID，具体操作详情请参见[展示位创建](../distribution/monetize/zhanshiweichuangjian-0000001132700049.md)。

以下表格中提供了贴片广告的专用测试广告位ID：

| 广告位类型 | 测试广告位ID | 展示形式 | 比例 | 推广类型 |
| --- | --- | --- | --- | --- |
| 贴片 | o2e960bnfz | 视频 | 16:9 | 应用下载 |
| 贴片 | v6dk3uf538 | 视频 | 16:9 | 网页推广 |
