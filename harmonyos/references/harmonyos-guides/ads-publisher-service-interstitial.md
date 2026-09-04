---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ads-publisher-service-interstitial
title: 插屏广告
breadcrumb: 指南 > 应用服务 > Ads Kit（广告服务） > 流量变现服务开发 > 插屏广告
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:02+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:562cf6f9a301494eb20b2a252bcbdc5ce7bdb24f5f1e488d2930aed9dd9b21db
---

## 场景介绍

插屏广告是一种在应用开启、暂停或退出时以全屏或半屏的形式弹出的广告形式，展示时机巧妙避开用户对应用的正常体验，尺寸大，曝光效果好。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/mCO0gsojT0u05lVZtEnLSg/zh-cn_image_0000002742003975.png)

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

   ```typescript
   import { abilityAccessCtrl, common, PermissionRequestResult } from '@kit.AbilityKit';
   import { advertising, identifier } from '@kit.AdsKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 获取OAID。

   若需提升广告推送精准度，可以在请求参数[AdRequestParams](../harmonyos-references/js-apis-advertising.md#adrequestparams)中添加oaid属性。

   如何获取OAID参见[获取OAID信息](oaid-service.md)。

   **说明** 

   使用以下示例中提供的测试广告位时，必须先获取OAID信息。
3. 请求单广告位广告。

   需要先创建一个AdLoader对象，通过AdLoader的[loadAd](../harmonyos-references/js-apis-advertising.md#loadad)方法请求广告，最后通过[AdLoadListener](../harmonyos-references/js-apis-advertising.md#adloadlistener)来监听广告的加载状态。

   请求广告关键参数如下所示：

   | 请求广告参数名 | 类型 | 必填 | 说明 |
   | --- | --- | --- | --- |
   | adType | number | 否 | 请求广告类型，插屏广告类型为12。不填默认为原生广告类型。 |
   | adId | string | 是 | 广告位ID。  - 如果仅调测广告，可使用测试广告位ID：v1rknehtfa。  - 如果要接入正式广告，则需要申请正式的广告位ID。可在应用发布前进入[流量变现官网](https://developer.huawei.com/consumer/cn/monetize)，点击“开始变现”，登录[鲸鸿动能媒体服务平台](https://developer.huawei.com/consumer/cn/service/ads/publisher/html/index.html?lang=zh)进行申请，具体操作详情请参见[展示位创建](../monetize/zhanshiweichuangjian-0000001132700049.md)。 |
   | oaid | string | 否 | 开放匿名设备标识符，用于精准推送广告。不填无法获取到个性化广告。 |

   示例代码如下所示：

   ```typescript
   @Entry
   @Component
   struct Index {
     private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

     build() {
       Column() {
         Button('LoadAd')
           .onClick(async () => {
             await this.loadAd();
           })
       }
       .width('100%')
       .height('100%')
       .justifyContent(FlexAlign.Center)
     }

     private async loadAd(): Promise<void> {
       // 广告请求回调监听
       const adLoadListener: advertising.AdLoadListener = {
         onAdLoadFailure: (errorCode: number, errorMsg: string) => {
           hilog.error(0x0000, 'testTag', `Failed to load ad. Code is ${errorCode}, message is ${errorMsg}`);
         },
         onAdLoadSuccess: (ads: Array<advertising.Advertisement>) => {
           hilog.info(0x0000, 'testTag', 'Succeeded in loading ad');
           // ...
         }
       };
       // 广告请求参数
       const adRequestParams: advertising.AdRequestParams = {
         // 'v1rknehtfa'为测试专用的广告位ID，App正式发布时需要改为正式的广告位ID
         adId: 'v1rknehtfa',
         // 插屏广告类型
         adType: 12,
         // 开放匿名设备标识符
         oaid: await requestOAID(this.context)
       };
       // 广告配置参数，开发者可根据项目实际情况设置
       const adOptions: advertising.AdOptions = {};
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

### 事件订阅

1. 导入相关模块。

   ```typescript
   import { BusinessError, commonEventManager } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
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

   ```typescript
   const KEY_INTERSTITIAL_STATUS = 'interstitial_ad_status';

   export class InterstitialAdStatusHandler {
     // 用于保存创建成功的订阅者对象，后续使用其完成订阅及退订的动作
     private subscriber: commonEventManager.CommonEventSubscriber | null = null;

     // 订阅方法，需要在每次展示广告前调用
     public registerPPSReceiver(): void {
       if (this.subscriber) {
         this.unRegisterPPSReceiver();
       }
       // 订阅者信息
       const subscribeInfo: commonEventManager.CommonEventSubscribeInfo = {
         events: ['com.huawei.hms.pps.action.PPS_INTERSTITIAL_STATUS_CHANGED'],
         // publisherBundleName被设置为"com.huawei.hms.adsservice"，表示只有来自该包名的事件才会被订阅者接收和处理。
         // 如果没有明确声明publisherBundleName，那么订阅者可能会收到来自其它包名的伪造事件，从而导致安全性问题或误导。
         publisherBundleName: 'com.huawei.hms.adsservice'
       };
       // 创建订阅者回调
       commonEventManager.createSubscriber(subscribeInfo,
         (err: BusinessError, commonEventSubscriber: commonEventManager.CommonEventSubscriber) => {
           if (err) {
             hilog.error(0x0000, 'testTag', `Failed to create subscriber. Code is ${err.code}, message is ${err.message}`);
             return;
           }
           hilog.info(0x0000, 'testTag', 'Succeeded in creating subscriber');
           this.subscriber = commonEventSubscriber;
           // 订阅公共事件回调
           commonEventManager.subscribe(this.subscriber,
             (err: BusinessError, commonEventData: commonEventManager.CommonEventData) => {
               if (err) {
                 hilog.error(0x0000, 'testTag', `Failed to subscribe. Code is ${err.code}, message is ${err.message}`);
               } else {
                 // 订阅者成功接收到公共事件
                 hilog.info(0x0000, 'testTag', 'Succeeded in subscribing data');
                 // 获取插屏广告页面变化状态
                 const status: string = commonEventData?.parameters?.[KEY_INTERSTITIAL_STATUS];
                 switch (status) {
                   case 'onAdOpen':
                     hilog.info(0x0000, 'testTag', 'Status is onAdOpen');
                     break;
                   case 'onAdClick':
                     hilog.info(0x0000, 'testTag', 'Status is onAdClick');
                     break;
                   case 'onAdClose':
                     hilog.info(0x0000, 'testTag', 'Status is onAdClose');
                     this.unRegisterPPSReceiver();
                     break;
                   case 'onVideoPlayBegin':
                     hilog.info(0x0000, 'testTag', 'Status is onVideoPlayBegin');
                     break;
                   case 'onVideoPlayEnd':
                     hilog.info(0x0000, 'testTag', 'Status is onVideoPlayEnd');
                     break;
                   default:
                     break;
                 }
               }
             });
         });
     }

     // 取消订阅
     public unRegisterPPSReceiver(): void {
       commonEventManager.unsubscribe(this.subscriber, (err: BusinessError) => {
         if (err) {
           hilog.error(0x0000, 'testTag', `Failed to unsubscribe. Code is ${err.code}, message is ${err.message}`);
         } else {
           hilog.info(0x0000, 'testTag', 'Succeeded in unsubscribing');
           this.subscriber = null;
         }
       });
     }
   }
   ```

### 展示广告

1. 导入相关模块。

   ```typescript
   import { abilityAccessCtrl, common, PermissionRequestResult } from '@kit.AbilityKit';
   import { advertising, identifier } from '@kit.AdsKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { InterstitialAdStatusHandler } from './InterstitialAdStatusHandler';
   ```
2. 展示广告。

   开发者需要调用[showAd](../harmonyos-references/js-apis-advertising.md#advertisingshowad)方法来展示广告，ads为[请求广告](ads-publisher-service-interstitial.md#请求广告)返回的广告信息，在每次展示广告前需要注册[事件订阅](ads-publisher-service-interstitial.md#事件订阅)中定义的监听器。

   示例代码如下所示：

   ```typescript
   @Entry
   @Component
   struct Index {
     private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

     build() {
       // ...
     }

     private async loadAd(): Promise<void> {
       // 广告请求回调监听
       const adLoadListener: advertising.AdLoadListener = {
         onAdLoadFailure: (errorCode: number, errorMsg: string) => {
           hilog.error(0x0000, 'testTag', `Failed to load ad. Code is ${errorCode}, message is ${errorMsg}`);
         },
         onAdLoadSuccess: (ads: Array<advertising.Advertisement>) => {
           hilog.info(0x0000, 'testTag', 'Succeeded in loading ad');
           try {
             // 注册插屏广告状态监听器
             new InterstitialAdStatusHandler().registerPPSReceiver();
             // 广告展示参数，开发者可根据项目实际情况设置
             const adDisplayOptions: advertising.AdDisplayOptions = {
               // 是否静音
               mute: true
             };
             // 此处ads[0]表示请求到的第一个广告，开发者可根据项目实际情况选择
             advertising.showAd(ads[0], adDisplayOptions, this.context);
           } catch (e) {
             hilog.error(0x0000, 'testTag', `Failed to show ad. Code is ${e.code}, message is ${e.message}`);
           }
         }
       };
       // ...
     }
   }
   ```

## 测试插屏广告

测试插屏广告时，需要使用专门的测试广告位ID来获取测试广告，以避免在测试过程中产生无效的广告点击量。测试广告位ID仅作为功能调试使用，不可用于广告变现。您应在应用发布前先进入[流量变现官网](https://developer.huawei.com/consumer/cn/monetize)，点击“开始变现”，登录[鲸鸿动能媒体服务平台](https://developer.huawei.com/consumer/cn/service/ads/publisher/html/index.html?lang=zh)，申请正式的广告位ID并替换测试广告位ID，具体操作详情请参见[展示位创建](../distribution/monetize/zhanshiweichuangjian-0000001132700049.md)。

以下表格中提供了插屏广告的专用测试广告位ID：

| 广告位类型 | 测试广告位ID | 展示形式 | 比例 | 推广类型 |
| --- | --- | --- | --- | --- |
| 插屏 | p540739a8w | 图片 | 16:9 | 网页推广 |
| 插屏 | v1rknehtfa | 视频 | 9:16 | 元服务推广 |
