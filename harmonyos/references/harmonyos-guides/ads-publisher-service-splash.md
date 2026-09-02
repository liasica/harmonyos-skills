---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ads-publisher-service-splash
title: 开屏广告
breadcrumb: 指南 > 应用服务 > Ads Kit（广告服务） > 流量变现服务开发 > 开屏广告
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:52+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:b69d4dc8d32b65f64beeaf4ea2c7c738878cfec8d89642e66d7b6b5d826b11d9
---

## 场景介绍

开屏广告是一种在应用启动时且在应用主界面显示之前需要被展示的广告。您需要预先为App设计一张开屏默认的Slogan图片，确保在未获取到开屏广告之前展示默认的Slogan，提供良好的用户体验。

开屏广告分为全屏开屏广告、半屏开屏广告，其中全屏开屏广告展示形式为广告铺满整个页面；半屏开屏广告展示形式会根据媒体页面自定义布局渲染广告、icon和版权信息，一般情况下建议将icon和版权信息展示在广告下方。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/SaXosTD_Q2qIY4fp-CWbvQ/zh-cn_image_0000002706674846.png)

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
   import { router, window } from '@kit.ArkUI';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 获取OAID。

   若需提升广告推送精准度，可以在请求参数[AdRequestParams](../harmonyos-references/js-apis-advertising.md#adrequestparams)中添加oaid属性。

   如何获取OAID参见[获取OAID信息](oaid-service.md)。

   **说明** 

   使用以下示例中提供的测试广告位时，必须先获取OAID信息。
3. 请求单广告位广告。

   需要创建一个AdLoader对象，通过AdLoader的[loadAd](../harmonyos-references/js-apis-advertising.md#loadad)方法请求广告，最后通过[AdLoadListener](../harmonyos-references/js-apis-advertising.md#adloadlistener)来监听广告的加载状态。测试开屏广告时，需要使用专门的测试广告位来获取测试开屏广告，示例代码中提供了两种开屏广告类型对应的广告位：半屏开屏（图片）（g3tl51sqih）和全屏开屏（视频）（r145sz31dp），测试广告位ID仅作为调试使用，不可用于广告变现。

   请求广告关键参数如下所示：

   | 请求广告参数名 | 类型 | 必填 | 说明 |
   | --- | --- | --- | --- |
   | adType | number | 否 | 请求广告类型，开屏广告类型为1。不填默认为原生广告类型。 |
   | adId | string | 是 | 广告位ID。  - 如果仅调测广告，可使用测试广告位ID：g3tl51sqih半屏开屏（图片）和r145sz31dp全屏开屏（视频）。  - 如果要接入正式广告，则需要申请正式的广告位ID。可在应用发布前进入[流量变现官网](https://developer.huawei.com/consumer/cn/monetize)，点击“开始变现”，登录[鲸鸿动能媒体服务平台](https://developer.huawei.com/consumer/cn/service/ads/publisher/html/index.html?lang=zh)进行申请，具体操作详情请参见[展示位创建](../monetize/zhanshiweichuangjian-0000001132700049.md)。 |
   | adCount | number | 否 | 广告数量。 |
   | orientation | number | 否 | 媒体请求广告的屏幕方向。1表示竖屏，0表示横屏，不设置则默认为1。当前未上架横屏开屏素材，若设置请求屏幕方向为横屏则不展示开屏广告。如果媒体设置应用固定横屏展示，但该参数未设置或者设置为1，则展示效果会受影响。 |

   | 返回广告参数名 | 类型 | 说明 |
   | --- | --- | --- |
   | isFullScreen | boolean | 标识返回的广告是否为全屏，true为全屏广告，false为半屏广告。 |

   **说明** 

   1、如果超时没有请求到广告，应用自行跳转到默认首页。

   2、为保证开屏展示效果，建议开发者在请求广告前，设置屏幕方向为竖屏。

   ```typescript
   @Entry
   @Component
   struct Index {
     @State ad: advertising.Advertisement | undefined = undefined;
     // ...
     private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
     // 是否超时
     private isTimeOut: boolean = false;
     // 超时时间(单位毫秒)，开发者可根据实际情况修改
     private timeOutDuration: number = 1000;
     // 超时index
     private timeOutIndex: number = -1;

     aboutToAppear(): void {
       // 开启全屏模式沉浸页面
       void this.setWindowLayoutFullScreen(true).catch((error: BusinessError) => {
         hilog.error(0x0000, 'testTag',
           `Failed to setWindowLayoutFullScreen. Code is ${error.code}, message is ${error.message}`);
       });
       // 设置屏幕方向为竖屏
       void this.setWindowPreferredOrientation(window.Orientation.PORTRAIT).catch((error: BusinessError) => {
         hilog.error(0x0000, 'testTag',
           `Failed to setWindowPreferredOrientation. Code is ${error.code}, message is ${error.message}`);
       });
       // 调用loadAd加载广告
       // ...
     }

     aboutToDisappear(): void {
       // 关闭全屏模式，开发者可根据实际情况修改
       void this.setWindowLayoutFullScreen(false).catch((error: BusinessError) => {
         hilog.error(0x0000, 'testTag',
           `Failed to setWindowLayoutFullScreen. Code is ${error.code}, message is ${error.message}`);
       });
       // 设置屏幕方向为默认值，开发者可根据实际情况修改
       void this.setWindowPreferredOrientation(window.Orientation.UNSPECIFIED).catch((error: BusinessError) => {
         hilog.error(0x0000, 'testTag',
           `Failed to setWindowPreferredOrientation. Code is ${error.code}, message is ${error.message}`);
       });
     }

     private async setWindowLayoutFullScreen(isLayoutFullScreen: boolean): Promise<void> {
       try {
         const win: window.Window = await window.getLastWindow(this.context);
         await win.setWindowLayoutFullScreen(isLayoutFullScreen);
       } catch (e) {
         hilog.error(0x0000, 'testTag', `Failed to set window layout. Code is ${e.code}, message is ${e.message}`);
       }
     }

     private async setWindowPreferredOrientation(orientation: Orientation): Promise<void> {
       try {
         const win: window.Window = await window.getLastWindow(this.context);
         await win.setPreferredOrientation(orientation);
       } catch (e) {
         hilog.error(0x0000, 'testTag', `Failed to set preferred orientation. Code is ${e.code}, message is ${e.message}`);
       }
     }

     build() {
       // ...
     }

     // ...
     private async loadAd(adId: string): Promise<void> {
       // 广告请求参数
       const adRequestParams: advertising.AdRequestParams = {
         // 广告位ID
         adId: adId,
         // 开屏广告类型
         adType: 1,
         // 请求的广告数量
         adCount: 1,
         // 开放匿名设备标识符
         oaid: await requestOAID(this.context)
       };
       // 广告请求回调监听
       const adLoadListener: advertising.AdLoadListener = {
         onAdLoadFailure: (errorCode: number, errorMsg: string) => {
           hilog.error(0x0000, 'testTag', `Failed to load ad. Code is ${errorCode}, message is ${errorMsg}`);
         },
         onAdLoadSuccess: (ads: Array<advertising.Advertisement>) => {
           clearTimeout(this.timeOutIndex);
           if (this.isTimeOut) {
             return;
           }
           hilog.info(0x0000, 'testTag', 'Succeeded in loading ad');
           this.ad = ads[0];
         }
       };
       // 广告配置参数，开发者可根据项目实际情况设置
       const adOptions: advertising.AdOptions = {};
       // 创建AdLoader广告对象
       const adLoader: advertising.AdLoader = new advertising.AdLoader(this.context);
       // 启动超时定时器
       this.timeOutHandler();
       try {
         // 调用广告请求接口
         adLoader.loadAd(adRequestParams, adOptions, adLoadListener);
       } catch (e) {
         hilog.error(0x0000, 'testTag', `Failed to load ad. Code is ${e.code}, message is ${e.message}`);
       }
     }

     private timeOutHandler(): void {
       this.isTimeOut = false;
       // 超时处理
       this.timeOutIndex = setTimeout(() => {
         this.isTimeOut = true;
         this.routeToHome();
         hilog.error(0x0000, 'testTag', 'Load ad time out');
       }, this.timeOutDuration);
     }

     private routeToHome(): void {
       // 开发者可根据项目实际情况修改超时之后要跳转的目标页面
       this.getUIContext().getRouter().replaceUrl({ url: 'pages/Index' }, router.RouterMode.Single)
         .catch((e: BusinessError) => {
           hilog.error(0x0000, 'testTag', `Failed to route to home. Code is ${e.code}, message is ${e.message}`);
         });
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
   import { AdComponent, advertising, identifier } from '@kit.AdsKit';
   import { router, window } from '@kit.ArkUI';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 展示广告。

   展示广告通过[AdInteractionListener](../harmonyos-references/js-apis-advertising.md#adinteractionlistener)监听广告状态回调，涉及的回调状态如下所示：

   | 回调状态 | 说明 | 使用建议 |
   | --- | --- | --- |
   | onAdOpen | 打开广告。 | - |
   | onAdClick | 点击广告。 | - |
   | onAdClose | 关闭广告。 | 广告倒计时结束、用户点击跳过按钮或广告从后台返回时触发，需要跳转到应用首页。回调状态包含了具体的关闭原因，详情见：[data说明](../harmonyos-references/js-apis-advertising.md#onstatuschanged)。 |
   | onAdFail | 广告加载失败。 | 广告展示失败时触发，需要跳转到应用首页。 |

   **说明** 

   1、请求到广告之前需要展示默认的Slogan图片。

   2、由请求广告中获取的isFullScreen参数判断展示全屏或者半屏广告。

   3、目前只支持展示竖屏广告。

   ```typescript
   @Entry
   @Component
   struct Index {
     @State ad: advertising.Advertisement | undefined = undefined;
     // 广告展示参数
     private adDisplayOptions: advertising.AdDisplayOptions = {
       // 是否静音
       mute: true
     };
     // ...

     build() {
       RelativeContainer() {
         // 展示开发者自定义Slogan图片
         Image($r('app.media.slogan'))
           .width('100%')
           .height('100%')
           .zIndex(0)
         // 展示开发者自定义icon、应用名称、版权信息
         Column() {
           Row() {
             Image($r('app.media.video'))
               .width(24)
               .height(24)
               .margin(8)
             Text($r('app.string.video'))
               .fontColor('#1A1A1A')
               .fontSize(16)
           }
           .margin({ bottom: 8 })

           Column() {
             Text($r('app.string.copyright'))
               .fontColor('#1A1A1A')
               .fontSize(9)
           }
         }
         .zIndex(1)
         .alignRules({ bottom: { anchor: '__container__', align: VerticalAlign.Bottom } })
         .width('100%')
         .height('13%')

         if (this.ad) {
           if (this.ad.isFullScreen) {
             // 全屏开屏广告
             this.splashFullScreen();
           } else {
             // 半屏开屏广告
             this.splashHalfScreen();
           }
         }
       }
       .width('100%')
       .height('100%')
     }

     /**
      * 半屏开屏广告
      */
     @Builder
     private splashHalfScreen() {
       AdComponent({
         ads: [this.ad!],
         displayOptions: this.adDisplayOptions,
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
                 this.routeToHome();
                 break;
               case 'onAdFail':
                 hilog.error(0x0000, 'testTag', 'Status is onAdFail');
                 this.routeToHome();
                 break;
               default:
                 break;
             }
           }
         }
       })
         .zIndex(1)
         .width('100%')
         .height('87%')
         // 自定义组件动画
         .transition(TransitionEffect.OPACITY.animation({ duration: 1000, curve: Curve.Friction}))
         .alignRules({ top: { anchor: '__container__', align: VerticalAlign.Top } })
     }

     /**
      * 全屏开屏广告
      */
     @Builder
     private splashFullScreen() {
       AdComponent({
         ads: [this.ad!],
         displayOptions: this.adDisplayOptions,
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
                 this.routeToHome();
                 break;
               case 'onAdFail':
                 hilog.error(0x0000, 'testTag', 'Status is onAdFail');
                 this.routeToHome();
                 break;
               default:
                 break;
             }
           }
         }
       })
         .zIndex(1)
         .width('100%')
         .height('100%')
     }
     // ...

     private routeToHome(): void {
       // 开发者可根据项目实际情况修改超时之后要跳转的目标页面
       this.getUIContext().getRouter().replaceUrl({ url: 'pages/Index' }, router.RouterMode.Single)
         .catch((e: BusinessError) => {
           hilog.error(0x0000, 'testTag', `Failed to route to home. Code is ${e.code}, message is ${e.message}`);
         });
     }
   }

   // ...
   ```

## 测试开屏广告

测试开屏广告时，需要使用专门的测试广告位ID来获取测试广告，以避免在测试过程中产生无效的广告点击量。测试广告位ID仅作为功能调试使用，不可用于广告变现。您应在应用发布前先进入[流量变现官网](https://developer.huawei.com/consumer/cn/monetize)，点击“开始变现”，登录[鲸鸿动能媒体服务平台](https://developer.huawei.com/consumer/cn/service/ads/publisher/html/index.html?lang=zh)，申请正式的广告位ID并替换测试广告位ID，具体操作详情请参见[展示位创建](../distribution/monetize/zhanshiweichuangjian-0000001132700049.md)。

以下表格中提供了开屏广告的专用测试广告位ID：

| 广告位类型 | 测试广告位ID | 展示形式 | 比例 | 推广类型 |
| --- | --- | --- | --- | --- |
| 开屏 | u7w58nlimb | 视频 | 9:16 | 元服务推广 |
| 开屏 | f068vmywiu | 图片 | 2:3 | 网页推广 |
