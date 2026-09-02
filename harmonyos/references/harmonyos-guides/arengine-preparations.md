---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-preparations
title: 开发准备
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 开发准备
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:19+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:26579e6cc3184f238fde4e7b4fd4725c7800e7e3505fec78a97a052a56c5e762
---

## 硬件要求

开发者可根据实际的开发语言，选择对应接口判断当前设备是否支持AR Engine。接口的调用参考如下方式：

ArkTS（[arViewController.isARTypeSupported](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)）：

```typescript
import { arEngine, arViewController } from '@kit.AREngine';
   
let ret: boolean = arViewController.isARTypeSupported(arEngine.ARFeatureType.ARENGINE_FEATURE_TYPE_FACE);
```

C/C++（[HMS\_AREngine\_CheckSupported](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_checksupported)）：

```cpp
#include "ar/ar_engine_core.h"

auto ret = HMS_AREngine_CheckSupported(ARENGINE_FEATURE_TYPE_FACE);
```

若对应接口返回错误码为801或ARENGINE\_ERROR\_DEVICE\_NOT\_SUPPORTED，则表示AR Engine不支持当前设备。

## 环境搭建

请参考[应用开发准备](application-dev-overview.md)完成基本准备工作。

## 申请权限

在开发AR应用时，需要先申请相机相关权限，确保应用拥有访问相机硬件及其他功能的权限，需要的权限如下。在申请权限前，请保证符合[权限使用的基本原则](app-permission-mgmt-overview.md#权限使用的基本原则)。

* 使用相机拍摄前，需要申请**ohos.permission.CAMERA**相机权限。
* 当需要使用加速计感知设备运动状态时，需要申请**ohos.permission.ACCELEROMETER**加速计权限。
* 当需要陀螺仪感知设备位姿信息时，需要申请**ohos.permission.GYROSCOPE**陀螺仪权限。

## 前置准备

推荐使用[组件导航(Navigation) (推荐)](arkts-navigation-navigation.md)作为页面路由，使用[Navigation](../harmonyos-references/ts-basic-components-navigation.md)的[页面生命周期](arkts-navigation-navdestination.md#页面生命周期)所示方法。

开发者需先创建首页，通过首页选择进入AR Engine场景。

1. 导入所需模块。

   ```typescript
   import { abilityAccessCtrl, PermissionRequestResult } from '@kit.AbilityKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { logger } from '../utils/Logger';
   import { requestPermissionOnSetting } from '../utils/Utils';
   ```
2. 创建一个基础的页面，具体可参考[组件导航(Navigation) (推荐)](arkts-navigation-navigation.md)。

   ```typescript
   @Entry
   @Component
   struct Selector {
     pageInfos: NavPathStack = new NavPathStack();
     @State context: Context = this.getUIContext().getHostContext() as Context;
     private hasPermission: boolean = false;
     build(): void {
       // ...
       }
       // ...
       .mode(NavigationMode.Stack)
       .hideTitleBar(true)
       .hideBackButton(true)
       .hideToolBar(true)
     }
   ```
3. 创建sampleButton，封装Button及权限校验功能，使用@Builder装饰，并配置routerMap进行页面跳转。

   ```typescript
   @Entry
   @Component
   struct Selector {
     pageInfos: NavPathStack = new NavPathStack();
     @State context: Context = this.getUIContext().getHostContext() as Context;
     private hasPermission: boolean = false;
     build(): void {
       // ...
     }
     @Builder
     sampleButton(sampleName: string): void {
       Button(sampleName, { type: ButtonType.Normal, stateEffect: true })
         .borderRadius(8)
         .width('50%')
         .height('5%')
         .onClick(async () => {
           if (!this.hasPermission) {
             this.hasPermission = await requestPermissionOnSetting(this.context);
             if (!this.hasPermission) {
               return;
             }
           }
           this.pageInfos.clear();
           this.pageInfos.pushDestinationByName(sampleName, null).catch((err: BusinessError) => {
             logger.error(`Failed to pushDestinationByName. Code is ${err.code}, message is ${err.message}.`);
           });
         })
     }
   ```
4. 创建requestPermissionOnSetting方法用于校验在进入AR场景时是否已经获取相机权限。

   ```typescript
   export async function requestPermissionOnSetting(context: Context): Promise<boolean> {
     let requestResult: boolean = false;
     let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
     await atManager.requestPermissionOnSetting(context, ['ohos.permission.CAMERA'])
       .then((data: abilityAccessCtrl.GrantStatus[]) => {
         logger.info('data:' + JSON.stringify(data));
         if (data[0] === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED) {
           requestResult = true;
         }
       })
       .catch((err: BusinessError) => {
         logger.error('data:' + JSON.stringify(err));
       })
     return requestResult;
   }
   ```
5. 在页面上创建按钮，用于进入AR场景。

   ```typescript
   build(): void {
     Navigation(this.pageInfos) {
       Column() {
         this.sampleButton('ARWorld');
         // ...
       }
       .justifyContent(FlexAlign.SpaceEvenly)
       .width('100%')
       .height('100%')
     }
     // ...
     .mode(NavigationMode.Stack)
     .hideTitleBar(true)
     .hideBackButton(true)
     .hideToolBar(true)
   }
   ```
6. 在onAppear中配置应用首次启动时的权限校验方法requestPermissionOnFirstStartup。

   ```typescript
   @Entry
   @Component
   struct Selector {
     // ...
     build(): void {
       Navigation(this.pageInfos) {
         Column() {
           this.sampleButton('ARWorld');
           // ...
         }
         .justifyContent(FlexAlign.SpaceEvenly)
         .width('100%')
         .height('100%')
       }
       .onAppear(() => {
         this.requestPermissionOnFirstStartup();
       })
       .mode(NavigationMode.Stack)
       .hideTitleBar(true)
       .hideBackButton(true)
       .hideToolBar(true)
     }
     @Builder
     sampleButton(sampleName: string): void {
       // ...
     }
     private requestPermissionOnFirstStartup(): void {
       abilityAccessCtrl.createAtManager()
         .requestPermissionsFromUser(this.context, ['ohos.permission.CAMERA'])
         .then((data: PermissionRequestResult) => {
           let grantStatus: number[] = data.authResults;
           if (grantStatus[0] === 0) {
             this.hasPermission = true;
             logger.info('Succeeded in getting requestPermission.');
           } else {
             this.hasPermission = false;
             logger.error('Failed to get requestPermission, user rejected.');
           }
         })
         .catch((err: BusinessError) => {
           logger.error(`Failed to request permissions from user. Code is ${err.code}, message is ${err.message}.`);
         })
     }
   ```
