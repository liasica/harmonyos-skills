---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ads-3
title: 如何解决获取OAID异常的问题
breadcrumb: FAQ > 应用服务开发 > 广告变现服务（Ads Kit） > 如何解决获取OAID异常的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:dfe186c862f994f66a388eb02c09e4695c23a56e4c76e20216ee7992880f24a2
---

## 问题现象

获取OAID会遇到以下常见的问题，应该如何解决？

* 调用identifier.getOAID获取到的OAID值是00000000-0000-0000-0000-000000000000，且没有授权弹窗。
* 调用identifier.getOAID接口报错。
* 应用审核被拒，提示OAID违规使用，未申请隐私权限的场景获取了OAID。

## 背景知识

[OAID](../harmonyos-guides/oaid-service.md#获取oaid信息)是一种非永久性设备标识符，基于开放匿名设备标识符，可在保护用户个人数据隐私安全的前提下，向用户提供个性化广告，同时三方监测平台也可以向广告主提供转化归因分析。OAID的获取方式参考[identifier.getOAID](../harmonyos-references/js-apis-oaid.md#identifiergetoaid)。

## 问题定位

1. 应用是否正确的配置了ohos.permission.APP\_TRACKING\_CONSENT权限。
2. 应用是否开启"跨应用关联访问权限"。
3. 应用授权弹窗是否点击确认。
4. 是否在用户同意隐私协议前获取了OAID，可通过以下步骤排查：
   * 全局搜索getOAID、AdvertisingIdClient、APP\_TRACKING\_CONSENT等关键词，确认所有调用点。
   * 检查第三方SDK的初始化时机，是否在用户点击隐私协议"同意"按钮之前执行。
   * 在手机设置中将应用权限全部关闭，在不点击隐私弹窗的情况下运行应用，通过hilog观察是否有OAID相关的错误或调用日志。
   * 使用DevEco Studio的Profiler工具抓取应用启动时的函数调用栈，查看是否有非预期的OAID获取行为。

## 分析结论

针对identifier.getOAID获取异常的问题，主要有以下几种可能的原因：

1. 应用未在当前模块的module.json5文件中配置ohos.permission.APP\_TRACKING\_CONSENT权限。
2. 应用配置了ohos.permission.APP\_TRACKING\_CONSENT权限，但是"跨应用关联访问权限"设置为"禁止"。
3. 应用配置了ohos.permission.APP\_TRACKING\_CONSENT权限，但在弹窗提示用户授权时，用户未选择手动授权。
4. 应用在用户同意隐私协议前获取了OAID，常见于第三方SDK（如推送SDK）在初始化时自动获取OAID。

## 修改建议

1. 配置相关权限：

   在应用的module.json5文件中添加ohos.permission.APP\_TRACKING\_CONSENT权限配置。确保该权限被正确声明，以便应用能够请求获取OAID的权限。该权限为user\_grant权限，当申请的权限为user\_grant权限时，reason，abilities标签必填，具体申请方式请参见[声明权限](../harmonyos-guides/declare-permissions.md)。
2. 跨应用关联访问权限：

   可以通过在应用内提供明确的指引或说明，引导用户前往设置-隐私安全-跨应用关联，手动开启允许"跨应用关联访问权限"，告知用户开启该权限的必要性和用途，以提高用户的授权意愿。比如通过代码跳转设置-隐私二级页面。
3. 用户手动授权：

   调用requestPermissionsFromUser接口弹窗，提示并引导用户允许对应权限，示例代码如下所示：

   ```ts
   import { BusinessError } from '@kit.BasicServicesKit';
   import { abilityAccessCtrl, common, Want } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { identifier } from '@kit.AdsKit';

   @Entry
   @Component
   struct Index {
     context = this.getUIContext().getHostContext() as common.UIAbilityContext;
     @State oaid: string = '';

     jumpToSetting() {
       let want: Want = {
         bundleName: 'com.huawei.hmos.settings',
         abilityName: 'com.huawei.hmos.settings.MainAbility',
         uri: 'privacy_settings',
         parameters: {
           // 传对应应用的包名
           pushParams: 'com.example.myapplication'
         }
       };
       this.context.startAbility(want);
     }

     requestOAIDTrackingConsentPermissions(context: common.Context): void {
       // 进入页面时，向用户请求授权广告跨应用关联访问权限
       const atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
       try {
         atManager.requestPermissionsFromUser(context, ['ohos.permission.APP_TRACKING_CONSENT']).then((data) => {
           if (data.authResults[0] === 0) {
             hilog.info(0x0000, 'testTag', '%{public}s', 'succeeded in requesting permission');
             identifier.getOAID((err: BusinessError, data: string) => {
               if (err.code) {
                 hilog.error(0x0000, 'testTag', '%{public}s', `get oaid failed, error: ${err.code} ${err.message}`);
               } else {
                 this.oaid = data;
                 hilog.info(0x0000, 'testTag', '%{public}s', `succeeded in getting oaid by callback , oaid: ${this.oaid}`);
               }
             });
           } else {
             hilog.error(0x0000, 'testTag', '%{public}s', 'user rejected');
           }
         }).catch((err: BusinessError) => {
           hilog.error(0x0000, 'testTag', '%{public}s', `request permission failed, error: ${err.code} ${err.message}`);
         });
       } catch (err) {
         hilog.error(0x0000, 'testTag', '%{public}s', `catch err->${err.code}, ${err.message}`);
       }
     }

     build() {
       Column({ space: 20 }) {
         Button('跳转设置')
           .onClick(() => {
             this.jumpToSetting();
           });
         Button('获取oaid')
           .onClick(() => {
             this.requestOAIDTrackingConsentPermissions(this.context);
           });
         Text(this.oaid);
       }
       .height('100%')
       .width('100%');
     }
   }
   ```
4. 延迟第三方SDK初始化：将所有第三方SDK的初始化代码延迟到用户点击隐私协议"同意"按钮之后执行，避免在用户授权前触发OAID获取。通过上述排查步骤定位到具体模块后，调整该模块的初始化时机。

## 常见FAQ

Q：如何分辨接口异常是权限问题导致的？

A：一些常见的Kit（比如推送服务、地图服务等）需要在AppGallery Connect网站上先开通服务并完成[手动签名](../harmonyos-guides/ide-signing.md#section297715173233)，或者在项目中需要配置相应的权限（可参考[申请应用权限](../harmonyos-guides/request-app-permissions.md)），因此需要先确认集成的Kit是否需要配置这些权限，在开发之前应该做好相应的开发准备，确保不会因为权限问题阻塞开发。

Q：OAID获取方式是否有变更？

A：OAID获取方式未有变更，获取OAID仍需要先申请ohos.permission.APP\_TRACKING\_CONSENT权限，获得权限后才能访问OAID，详情请参考[获取OAID信息](../harmonyos-guides/oaid-service.md)。
