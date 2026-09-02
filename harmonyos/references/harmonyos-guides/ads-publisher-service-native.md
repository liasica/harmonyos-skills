---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ads-publisher-service-native
title: 原生广告
breadcrumb: 指南 > 应用服务 > Ads Kit（广告服务） > 流量变现服务开发 > 原生广告
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:52+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:22181b5ea0f8840f920b5aa223249ae4df1dd4267137975c60bfc8866c3e8680
---

## 场景介绍

原生广告是与应用内容融于一体的广告，通过“和谐”的内容呈现广告信息，在不破坏用户体验的前提下，为用户提供有价值的信息，展示形式包含图片和视频，支持您自由定制界面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/aZzCkjU6QN64Lyg2fgeYhg/zh-cn_image_0000002736433929.png)

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

   ```typescript
   import { abilityAccessCtrl, common, PermissionRequestResult } from '@kit.AbilityKit';
   import { AdComponent, advertising, identifier } from '@kit.AdsKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 获取OAID。

   若需提升广告推送精准度，可以在请求参数[AdRequestParams](../harmonyos-references/js-apis-advertising.md#adrequestparams)中添加oaid属性。

   如何获取OAID参见[获取OAID信息](oaid-service.md)。

   **说明** 

   使用以下示例中提供的测试广告位时，必须先获取OAID信息。
3. 请求广告。

   请求广告需要创建一个AdLoader对象。

   * 如果要请求单广告位广告，通过AdLoader的[loadAd](../harmonyos-references/js-apis-advertising.md#loadad)方法请求广告，通过[AdLoadListener](../harmonyos-references/js-apis-advertising.md#adloadlistener)来监听广告的加载状态。
   * 如果要请求多广告位广告，通过AdLoader的[loadAdWithMultiSlots](../harmonyos-references/js-apis-advertising.md#loadadwithmultislots)方法请求广告，通过[MultiSlotsAdLoadListener](../harmonyos-references/js-apis-advertising.md#multislotsadloadlistener)来监听广告的加载状态。

   请求广告关键参数如下所示：

   | 请求广告参数名 | 类型 | 必填 | 说明 |
   | --- | --- | --- | --- |
   | adType | number | 否 | 请求广告类型，原生广告类型为3。不填默认为原生广告类型。 |
   | adId | string | 是 | 广告位ID。  - 如果仅调测广告，可使用测试广告位ID：f5n0u5i3wd（原生视频），h8asowxwhq（原生大图），k94abyn2z4（原生小图），u17l1u6wg1（原生三图）。  - 如果要接入正式广告，则需要申请正式的广告位ID。可在应用发布前进入[流量变现官网](https://developer.huawei.com/consumer/cn/monetize)，点击“开始变现”，登录[鲸鸿动能媒体服务平台](https://developer.huawei.com/consumer/cn/service/ads/publisher/html/index.html?lang=zh)进行申请，具体操作详情请参见[展示位创建](../monetize/zhanshiweichuangjian-0000001132700049.md)。 |
   | oaid | string | 否 | 开放匿名设备标识符，用于精准推送广告。不填无法获取到个性化广告。 |

   以请求多广告位广告为例，示例代码如下所示：

   ```typescript
   @Entry
   @Component
   struct Index {
     @State ads: advertising.Advertisement[] = [];
     // ...
     private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

     aboutToAppear(): void {
       // 调用loadAd加载广告
       // ...
     }

     private async loadAd(...adIds: string[]): Promise<void> {
       // 广告请求参数
       const adRequestParamsArray: advertising.AdRequestParams[] = [];
       const oaid: string | undefined = await requestOAID(this.context);
       for (const adId of adIds) {
         adRequestParamsArray.push({
           // 广告位ID
           adId: adId,
           // 原生广告类型
           adType: 3,
           // 原生广告扩展参数，是否直接返回广告，不用等待所有广告素材下载完成
           enableDirectReturnVideoAd: true,
           // 开放匿名设备标识符
           oaid: oaid
         });
       }
       // 广告配置参数，开发者可根据项目实际情况设置
       const adOptions: advertising.AdOptions = {};
       // 广告请求回调监听
       const multiSlotsAdLoaderListener: advertising.MultiSlotsAdLoadListener = {
         onAdLoadFailure: (errorCode: number, errorMsg: string) => {
           hilog.error(0x0000, 'testTag', `Failed to load multiSlots ad. Code is ${errorCode}, message is ${errorMsg}`);
         },
         onAdLoadSuccess: (ads: Map<string, Array<advertising.Advertisement>>) => {
           hilog.info(0x0000, 'testTag', 'Succeeded in loading multiSlots ad');
           const returnAds: advertising.Advertisement[] = [];
           ads.forEach((adsArray) => returnAds.push(...adsArray));
           this.ads = returnAds;
         }
       };
       // 创建AdLoader广告对象
       const adLoader: advertising.AdLoader = new advertising.AdLoader(this.context);
       try {
         // 调用广告请求接口
         adLoader.loadAdWithMultiSlots(adRequestParamsArray, adOptions, multiSlotsAdLoaderListener);
       } catch (e) {
         hilog.error(0x0000, 'testTag', `Failed to load multiSlots ad. Code is ${e.code}, message is ${e.message}`);
       }
     }

     build() {
       // ...
     }

     // ...
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
   import { AdComponent, advertising, identifier } from '@kit.AdsKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
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

   ```typescript
   @Entry
   @Component
   struct Index {
     @State ads: advertising.Advertisement[] = [];
     @State visibilityState: Visibility = Visibility.Visible;
     // ...

     build() {
       Column() {
         if (this.ads.length > 0) {
           this.inFeedNativeAd(this.ads[0]);
           // ...
         }
       }
       .width('100%')
       .height('100%')
     }

     @Builder
     inFeedNativeAd(ad: advertising.Advertisement): void {
       Row() {
         AdComponent({
           ads: [ad],
           // 广告展示参数，开发者可根据项目实际情况设置
           displayOptions: {
             // 是否静音
             mute: true
           },
           interactionListener: {
             onStatusChanged: (status: string, ad: advertising.Advertisement, data: string) => {
               switch (status) {
                 case 'onAdOpen':
                   hilog.info(0x0000, 'testTag', 'Status is onAdOpen');
                   break;
                 case 'onAdClick':
                   hilog.info(0x0000, 'testTag', 'Status is onAdClick');
                   break;
                 case 'onAdClose':
                   hilog.info(0x0000, 'testTag', 'Status is onAdClose');
                   this.visibilityState = Visibility.None;
                   break;
                 case 'onAdFail':
                   hilog.error(0x0000, 'testTag', 'Status is onAdFail');
                   this.visibilityState = Visibility.None;
                   break;
                 default:
                   break;
               }
             }
           }
         })
         // 原生信息流样式，不建议设置高度，宽度建议设置为100%，撑满父容器
           .width('100%')
       }
       .width('100%')
       .padding({ left: 16, right: 16 })
       .visibility(this.visibilityState)
     }

     // ...
   }
   ```

   原生插图广告宽高为固定值312vp\*284vp，开发者可以将广告展示组件[AdComponent](../harmonyos-references/js-apis-adcomponent.md)居中展示。

   示例代码如下所示：

   ```typescript
   @Entry
   @Component
   struct Index {
     @State ads: advertising.Advertisement[] = [];
     @State visibilityState: Visibility = Visibility.Visible;
     // ...

     build() {
       Column() {
         if (this.ads.length > 0) {
           // ...
           this.nativeCardAd(this.ads[0]);
         }
       }
       .width('100%')
       .height('100%')
     }

     // ...

     @Builder
     nativeCardAd(ad: advertising.Advertisement): void {
       Row() {
         AdComponent({
           ads: [ad],
           // 广告展示参数，开发者可根据项目实际情况设置
           displayOptions: {
             // 是否静音
             mute: true
           },
           interactionListener: {
             onStatusChanged: (status: string, ad: advertising.Advertisement, data: string) => {
               switch (status) {
                 case 'onAdOpen':
                   hilog.info(0x0000, 'testTag', 'Status is onAdOpen');
                   break;
                 case 'onAdClick':
                   hilog.info(0x0000, 'testTag', 'Status is onAdClick');
                   break;
                 case 'onAdClose':
                   hilog.info(0x0000, 'testTag', 'Status is onAdClose');
                   this.visibilityState = Visibility.None;
                   break;
                 case 'onAdFail':
                   hilog.error(0x0000, 'testTag', 'Status is onAdFail');
                   this.visibilityState = Visibility.None;
                   break;
                 default:
                   break;
               }
             }
           }
         })
         // 原生插图样式，宽高为固定值，为312vp*284vp
           .width(312)
           .height(284)
       }
       .width('100%')
       // 宽高固定无法撑满父容器，将广告居中展示
       .justifyContent(FlexAlign.Center)
       .visibility(this.visibilityState)
     }
   }
   ```

## 测试原生广告

原生广告测试广告位ID，仅可用于调测原生广告功能，不可用于广告变现，在应用正式发布前需替换为正式的原生广告位ID。您应在应用发布前先进入[流量变现官网](https://developer.huawei.com/consumer/cn/monetize)，点击“开始变现”，登录[鲸鸿动能媒体服务平台](https://developer.huawei.com/consumer/cn/service/ads/publisher/html/index.html?lang=zh)，申请正式的广告位ID并替换测试广告位ID，具体操作详情请参见[展示位创建](../distribution/monetize/zhanshiweichuangjian-0000001132700049.md)。

原生广告测试广告位ID列表如下：

| 广告位类型 | 测试广告位ID | 展示形式 | 比例 | 推广类型 |
| --- | --- | --- | --- | --- |
| 原生 | h8asowxwhq | 大图 | 16:9 | 网页推广 |
| 原生 | k94abyn2z4 | 小图 | 4:3 | 应用下载 |
| 原生 | u17l1u6wg1 | 三图 | 4:3 | 应用下载 |
| 原生 | f5n0u5i3wd | 视频 | 16:9 | 网页推广 |
