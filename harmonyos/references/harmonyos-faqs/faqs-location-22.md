---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-location-22
title: 如何判断“访问我的位置”配置是否开启，若关闭如何跳转对应设置页面
breadcrumb: FAQ > 应用服务开发 > 位置服务（Location Kit） > 如何判断“访问我的位置”配置是否开启，若关闭如何跳转对应设置页面
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:50+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:193647501894659301b01b3a0221feaa7164062519912bcf442f7153771151d2
---

## 问题现象

如何判断“访问我的位置”是否已经开启，在“访问我的位置”配置是关闭的情况，提醒用户打开“访问我的位置”，或者跳转到“访问我的位置”页面（设置--隐私与安全--位置--访问我的位置）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/bJQg4drXRFmlWkC1IW3lfg/zh-cn_image_0000002628394538.png "点击放大")

## 背景知识

* 可使用[geoLocationManager.isLocationEnabled](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagerislocationenabled)确认当前应用是否开启“访问我的位置”开关。
* 开发者可以调用[startAbility](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability-2)接口，打开设置位置的页面。

## 解决方案

完整流程如下：

1. 使用[geoLocationManager.isLocationEnabled](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagerislocationenabled)判断当前应用是否开启“访问我的位置”开关。

   ```ts
   isLocationEnabled(): void {
     // 判断当前位置开关状态是否开启
     let locationEnabled = geoLocationManager.isLocationEnabled();
     if (locationEnabled) {
       this.message = `“访问我的位置”开关已开启`;
       this.openDialog();
     } else {
       this.message = `“访问我的位置”开关未开启`;
       this.openDialog();
     }
   }
   ```
2. 若“访问我的位置”开关关闭，提醒用户打开“访问我的位置”，跳转到“访问我的位置”页面（设置--隐私与安全--位置--访问我的位置）。

   ```ts
   toLocationInfo() {
     let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
     let want: Want = {
       bundleName: 'com.huawei.hmos.settings',
       abilityName: 'com.huawei.hmos.settings.MainAbility',
       uri: 'location_manager_settings',
     };
     // 跳转访问我的位置信息
     context.startAbility(want);
   }
   ```
3. “访问我的位置”开关被关闭，可以调用[requestGlobalSwitch()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestglobalswitch12)方法拉起半模态对话框，打开“访问我的位置”开关。

   ```ts
   isLocationToggle(): void {
     let atManager = abilityAccessCtrl.createAtManager();
     // 判断当前位置开关状态是否开启
     let isLocationEnabled = geoLocationManager.isLocationEnabled();
     let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
     if (!isLocationEnabled) {
       // 拉起全局开关设置弹框
       atManager.requestGlobalSwitch(context, abilityAccessCtrl.SwitchType.LOCATION).then((data: boolean) => {
         if (data) {
           this.message = `“访问我的位置”开关已开启`;
           this.openDialog();
         } else {
           this.message = `“访问我的位置”开关未开启`;
           this.openDialog();
         }
       }).catch((err: BusinessError) => {
         console.error(`Failed to request global switch. Code is ${err.code}, message is ${err.message}`);
       });
     } else {
       this.message = `“访问我的位置”开关已开启`;
       this.openDialog();
     }
   }
   ```
4. 完整示例参考如下：

   ```ts
   import common from '@ohos.app.ability.common';
   import Want from '@ohos.app.ability.Want';
   import { geoLocationManager } from '@kit.LocationKit';
   import { abilityAccessCtrl } from '@kit.AbilityKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   @Entry
   @Component
   struct LocationPage {
     @State message: string = '';
     private customDialogComponentId: number = 0;

     @Builder
     normalCustomDialog() {
       Column() {
         Text(this.message)
           .fontSize(14)
           .padding({
             left: 16,
             right: 16,
             bottom: 8.5,
             top: 8.5
           })
       }
       .width('100%')
       .height('100%')
       .borderRadius(18)
       .justifyContent(FlexAlign.Center)
       .alignItems(HorizontalAlign.Center)
       .onClick(() => {
         // 关闭弹窗
         this.getUIContext().getPromptAction().closeCustomDialog(this.customDialogComponentId);
       })
     }

     // 打开弹窗
     openDialog() {
       this.getUIContext().getPromptAction().openCustomDialog({
         builder: () => {
           this.normalCustomDialog();
         },
         width: 238,
         height: 36,
         alignment:DialogAlignment.Bottom,
         offset:{ dx: 0 , dy: -100 }
       })
         .then((dialogId: number) => {
           this.customDialogComponentId = dialogId;
         });
     }

     isLocationEnabled(): void {
       // 判断当前位置开关状态是否开启
       let locationEnabled = geoLocationManager.isLocationEnabled();
       if (locationEnabled) {
         this.message = `“访问我的位置”开关已开启`;
         this.openDialog();
       } else {
         this.message = `“访问我的位置”开关未开启`;
         this.openDialog();
       }
     }

     isLocationToggle(): void {
       let atManager = abilityAccessCtrl.createAtManager();
       // 判断当前位置开关状态是否开启
       let isLocationEnabled = geoLocationManager.isLocationEnabled();
       let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
       if (!isLocationEnabled) {
         // 拉起全局开关设置弹框
         atManager.requestGlobalSwitch(context, abilityAccessCtrl.SwitchType.LOCATION).then((data: boolean) => {
           if (data) {
             this.message = `“访问我的位置”开关已开启`;
             this.openDialog();
           } else {
             this.message = `“访问我的位置”开关未开启`;
             this.openDialog();
           }
         }).catch((err: BusinessError) => {
           console.error(`Failed to request global switch. Code is ${err.code}, message is ${err.message}`);
         });
       } else {
         this.message = `“访问我的位置”开关已开启`;
         this.openDialog();
       }
     }

     toLocationInfo() {
       let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
       let want: Want = {
         bundleName: 'com.huawei.hmos.settings',
         abilityName: 'com.huawei.hmos.settings.MainAbility',
         uri: 'location_manager_settings',
       };
       // 跳转访问我的位置信息
       context.startAbility(want);
     }

     build() {
       Column() {
         Button('是否开启“访问我的位置”开关')
           .backgroundColor('#0a59f7')
           .onClick(() => {
             // 判断当前位置开关状态是否开启
             this.isLocationEnabled();
           }).margin(30)
         Button('跳转访问我的位置信息')
           .backgroundColor('#0a59f7')
           .onClick(() => {
             // 跳转访问我的位置信息
             this.toLocationInfo();
           }).margin(30)
         Button('拉起半模态对话框')
           .backgroundColor('#0a59f7')
           .onClick(() => {
             // 拉起半模态对话框
             this.isLocationToggle();
           }).margin(30)
       }
       .width('100%')
       .height('100%')
     }
   }
   ```
