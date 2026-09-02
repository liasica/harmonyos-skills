---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-location-21
title: HarmonyOS在未连接网络时能否获取位置信息
breadcrumb: FAQ > 应用服务开发 > 位置服务（Location Kit） > HarmonyOS在未连接网络时能否获取位置信息
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:50+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a69ad438e9f4cc7a546131409e036f1b9c3d58efffa0f5c4fbbc210580d52f3c
---

## 问题现象

在设备处于断网或未连接至互联网的离线运行模式下，HarmonyOS系统是否仍具备基于其内部定位架构（例如通过整合惯性传感器、本地缓存的地理信息数据、以及接收来自全球导航卫星系统的信号）来完成对终端地理位置的判定与数据提取能力？

## 解决方案

在未连接网络的前提下，可通过在本地运行以下代码实现位置信息的获取。

1. 配置位置权限，示例代码如下：

   ```json
   {
     "module": {
       "name": "entry",
       "type": "entry",
       "description": "$string:module_desc",
       "mainElement": "EntryAbility",
       "deviceTypes": [
         "phone"
       ],
       "deliveryWithInstall": true,
       "installationFree": false,
       "pages": "$profile:main_pages",
       "abilities": [
         {
           "name": "EntryAbility",
           "srcEntry": "./ets/entryability/EntryAbility.ets",
           "description": "$string:EntryAbility_desc",
           "icon": "$media:layered_image",
           "label": "$string:EntryAbility_label",
           "startWindowIcon": "$media:startIcon",
           "startWindowBackground": "$color:start_window_background",
           "exported": true,
           "skills": [
             {
               "entities": [
                 "entity.system.home"
               ],
               "actions": [
                 "ohos.want.action.home"
               ]
             }
           ]
         }
       ],
       "extensionAbilities": [
         {
           "name": "EntryBackupAbility",
           "srcEntry": "./ets/entrybackupability/EntryBackupAbility.ets",
           "type": "backup",
           "exported": false,
           "metadata": [
             {
               "name": "ohos.extension.backup",
               "resource": "$profile:backup_config"
             }
           ],
         }
       ],
       "requestPermissions": [
         {
           "name": "ohos.permission.APPROXIMATELY_LOCATION",
           "reason": "$string:reasondetail",
           "usedScene": {
             "abilities": [
               "EntryAbility"
             ],
             "when": "inuse"
           }
         },
         {
           "name": "ohos.permission.LOCATION",
           "reason": "$string:reasondetail",
           "usedScene": {
             "abilities": [
               "EntryAbility"
             ],
             "when": "inuse"
           }
         }
       ]
     }
   }
   ```
2. 管理用户授权和获取位置信息，示例代码如下：

   ```ts
   import { geoLocationManager } from '@kit.LocationKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { abilityAccessCtrl, common, Permissions } from '@kit.AbilityKit';

   @Entry
   @Component
   struct Index {
     @State message: string = '获取位置信息';
     permissions: Array<Permissions> = ['ohos.permission.APPROXIMATELY_LOCATION', 'ohos.permission.LOCATION'];

     aboutToAppear(): void {
       this.requestPermissions(this.permissions);
     }

     requestPermissions(permissions: Array<Permissions>): void {
       let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
       let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
       atManager.requestPermissionsFromUser(context, permissions);
     }

     testMethod() {
       let request: geoLocationManager.SingleLocationRequest = {
         'locatingPriority': geoLocationManager.LocatingPriority.PRIORITY_LOCATING_SPEED,
         'locatingTimeoutMs': 10000
       };
       try {
         geoLocationManager.getCurrentLocation(request).then((result) => { // 调用getCurrentLocation获取当前设备位置，通过promise接收上报的位置
           console.info('current location: ', JSON.stringify(result));
         })
           .catch((error: BusinessError) => { // 接收上报的错误码
             console.error('promise, getCurrentLocation: error=' + JSON.stringify(error));
           });
       } catch (err) {
         console.error('errCode:' + JSON.stringify(err));
       }
     }

     build() {
       RelativeContainer() {
         Text(this.message)
           .fontSize($r('app.float.page_text_font_size'))
           .fontWeight(FontWeight.Bold)
           .alignRules({
             center: { anchor: '__container__', align: VerticalAlign.Center },
             middle: { anchor: '__container__', align: HorizontalAlign.Center }
           })
           .onClick(() => {
             this.message = '成功获取位置信息';
             this.testMethod();
           });
       }
       .height('100%')
       .width('100%');
     }
   }
   ```
