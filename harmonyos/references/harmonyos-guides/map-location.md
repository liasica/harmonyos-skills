---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-location
title: 显示我的位置
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 创建地图 > 显示我的位置
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:13+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:180a8bf305f461af41d7fcc789fd06073216f509daac7ac1f5b135c13ca43b4b
---

## 场景介绍

从6.0.1(21)开始，支持更改我的位置相对覆盖物的顺序。

本章节将向您介绍如何开启和展示“我的位置”功能，“我的位置”指的是进入地图后点击“我的位置”显示当前位置点的功能。效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/a2Aeub7AQQKOSFgYTCmTSw/zh-cn_image_0000002712405232.jpg "点击放大")

## 接口说明

“我的位置”功能主要由[MapComponentController](../harmonyos-references/map-map-mapcomponentcontroller.md)的方法实现，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-map-mapcomponentcontroller.md#setmylocationenabled)。

| 接口名 | 描述 |
| --- | --- |
| [setMyLocationEnabled](../harmonyos-references/map-map-mapcomponentcontroller.md#setmylocationenabled)(myLocationEnabled: boolean): void | “我的位置”图层功能开关，默认使用系统的连续定位能力显示用户位置。开关打开后，“我的位置”按钮默认显示在地图的右下角。点击“我的位置”按钮，将会在屏幕中心显示当前定位，以蓝色圆点的形式呈现。 |
| [setMyLocationControlsEnabled](../harmonyos-references/map-map-mapcomponentcontroller.md#setmylocationcontrolsenabled)(enabled: boolean): void | 设置是否启用“我的位置”按钮。只显示按钮，在不开启“我的位置”图层功能的情况下，点击按钮没反应。 |
| [setMyLocation](../harmonyos-references/map-map-mapcomponentcontroller.md#setmylocation)(location: [geoLocationManager.Location](../harmonyos-references/js-apis-geolocationmanager.md#location)): void | 设置“我的位置”坐标。  如果不使用Map Kit提供的默认定位行为，可以通过[Location Kit](../harmonyos-references/location-api.md)获取用户位置后，传给Map Kit。 |
| [setMyLocationStyle](../harmonyos-references/map-map-mapcomponentcontroller.md#setmylocationstyle)(style: [mapCommon.MyLocationStyle](../harmonyos-references/map-common.md#mylocationstyle)): Promise<void> | 设置“我的位置”样式。 |
| [on](../harmonyos-references/map-map-mapeventmanager.md#onmylocationbuttonclick)(type: 'myLocationButtonClick', callback: Callback<void>): void | 监听“我的位置”按钮点击事件。 |
| [off](../harmonyos-references/map-map-mapeventmanager.md#offmylocationbuttonclick)(type: 'myLocationButtonClick', callback?: Callback<void>): void | 取消监听“我的位置”按钮点击事件。 |

## 开发步骤

### 开启“我的位置”按钮

1. 在启用“我的位置”功能前，开发者应确保应用已申请并获得用户定位权限，以便正确显示用户当前位置。

   申请ohos.permission.LOCATION和ohos.permission.APPROXIMATELY\_LOCATION权限，您需要在module.json5配置文件中声明所需要的权限，具体可参考[声明权限](declare-permissions.md)。

   ```json5
   {
     "module": {
       // ...
       // ...
       "requestPermissions":[
         {
           // 允许应用在前台运行时获取位置信息
           "name" : "ohos.permission.LOCATION",
           // reason需要在/resources/base/element/string.json中新建
           "reason": "$string:location_permission",
           "usedScene": {
             "abilities": [
               "EntryAbility"
             ],
             "when":"inuse"
           }
         },
         {
           // 允许应用获取设备模糊位置信息
           "name" : "ohos.permission.APPROXIMATELY_LOCATION",
           // reason需要在/resources/base/element/string.json中新建
           "reason": "$string:fuzzy_location_permission",
           "usedScene": {
             "abilities": [
               "EntryAbility"
             ],
             "when":"inuse"
           }
         }
       ]
     }
   }
   ```
2. 初始化地图并获取[MapComponentController](../harmonyos-references/map-map-mapcomponentcontroller.md)地图操作类对象。调用mapController对象的[setMyLocationEnabled](../harmonyos-references/map-map-mapcomponentcontroller.md#setmylocationenabled)方法启用“我的位置”功能。

   建议在获得用户授权后开启“我的位置”功能。

   ```typescript
   import { abilityAccessCtrl, bundleManager, common, PermissionRequestResult, Permissions } from '@kit.AbilityKit';
   import { BusinessError, AsyncCallback } from '@kit.BasicServicesKit';
   import { MapComponent, mapCommon, map } from '@kit.MapKit';

   // ...
   @Entry
   @Component
   struct MapLocationDemo {
     // ...
     private mapOptions?: mapCommon.MapOptions;
     private mapController?: map.MapComponentController;
     private callback?: AsyncCallback<map.MapComponentController>;
     private mapEventManager?: map.MapEventManager;

     aboutToAppear(): void {
       // 地图初始化参数，设置地图中心点坐标及层级
       this.mapOptions = {
         position: {
           target: {
             latitude: 39.9,
             longitude: 116.4
           },
           zoom: 10
         }
       };

       // 地图初始化的回调
       this.callback = async (err, mapController) => {
         if (!err) {
           // 获取地图的控制器类，用来操作地图
           this.mapController = mapController;
           this.mapEventManager = this.mapController.getEventManager();
           let permission = await this.checkPermissions();
           if (!permission) {
             this.requestPermissions();
             // 启用我的位置按钮
             this.mapController?.setMyLocationControlsEnabled(true);
           }
         } else {
           console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
         }
       };
     }

     // 校验应用是否被授予定位权限，可以通过调用checkAccessToken()方法来校验当前是否已经授权。
     async checkPermissions(): Promise<boolean> {
       const permissions: Permissions[] = ['ohos.permission.LOCATION', 'ohos.permission.APPROXIMATELY_LOCATION'];
       for (let permission of permissions) {
         let grantStatus: abilityAccessCtrl.GrantStatus = await this.checkAccessToken(permission);
         if (grantStatus === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED) {
           // 启用我的位置图层，mapController为地图操作类对象
           this.mapController?.setMyLocationEnabled(true);
           // 启用我的位置按钮
           this.mapController?.setMyLocationControlsEnabled(true);
           return true;
         }
       }
       return false;
     }

     // 如果没有被授予定位权限，动态向用户申请授权
     requestPermissions(): void {
       let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
       atManager.requestPermissionsFromUser(this.getUIContext().getHostContext() as common.UIAbilityContext,
         ['ohos.permission.LOCATION', 'ohos.permission.APPROXIMATELY_LOCATION'])
         .then((data: PermissionRequestResult) => {
           // 启用我的位置图层
           this.mapController?.setMyLocationEnabled(true);
         })
         .catch((err: BusinessError) => {
           console.error(`Failed to request permissions from user. Code is ${err.code}, message is ${err.message}`);
         })
     }

     async checkAccessToken(permission: Permissions): Promise<abilityAccessCtrl.GrantStatus> {
       let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
       let grantStatus: abilityAccessCtrl.GrantStatus = abilityAccessCtrl.GrantStatus.PERMISSION_DENIED;

       // 获取应用程序的accessTokenID
       let tokenId: number = 0;
       let bundleInfo: bundleManager.BundleInfo =
         await bundleManager.getBundleInfoForSelf(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION);
       console.info('Succeeded in getting Bundle.');
       let appInfo: bundleManager.ApplicationInfo = bundleInfo.appInfo;
       tokenId = appInfo.accessTokenId;

       // 校验应用是否被授予权限
       grantStatus = await atManager.checkAccessToken(tokenId, permission);
       console.info('Succeeded in checking access token.');
       return grantStatus;
     }

     build() {
       // ...
         Stack() {
           // 调用MapComponent组件初始化地图
           MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback }).width('100%').height('100%');
         }

         // ...
     }
   }
   ```
3. 检查“我的位置”功能是否成功启用。

   “我的位置”按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/UmNE8eS8TRSc3T5BPd_1Dg/zh-cn_image_0000002742124181.png)默认显示在地图的右下角。点击“我的位置”按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/n5LUIBPLQeCONyYfj2i1ZQ/zh-cn_image_0000002712245274.png)，将会在屏幕中心显示当前定位，以蓝色圆点的形式呈现，效果如下图所示，效果根据获取到的用户位置会有变化。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/BQ0fYYL8SxqRbC9O5HIUBw/zh-cn_image_0000002742004223.jpg "点击放大")
4. 获取用户位置坐标并设置用户的位置。

   Map Kit默认使用系统的连续定位能力，如果您希望定制显示频率或者精准度，可以调用[geoLocationManager](../harmonyos-references/js-apis-geolocationmanager.md)相关接口获取用户位置坐标（WGS84坐标系）。注意访问设备的位置信息必须申请权限，并且获得用户授权，详情见[geoLocationManager](../harmonyos-references/js-apis-geolocationmanager.md)。

   下面的示例仅显示一次定位结果，在获取到用户坐标后，调用mapController对象的[setMyLocation](../harmonyos-references/map-map-mapcomponentcontroller.md#setmylocation)设置用户的位置，[setMyLocation](../harmonyos-references/map-map-mapcomponentcontroller.md#setmylocation)接口使用的是WGS84坐标系。

   ```typescript
   // 需要引入@kit.LocationKit模块
   import { geoLocationManager } from '@kit.LocationKit';

   // ...
                 // 获取用户位置坐标
                 let location = await geoLocationManager.getCurrentLocation();

                 // 设置用户的位置
                 this.mapController.setMyLocation(location);
   ```

### 监听“我的位置”按钮点击事件

通过调用[on('myLocationButtonClick')](../harmonyos-references/map-map-mapeventmanager.md#onmylocationbuttonclick)方法，设置'myLocationButtonClick'事件监听。设置监听后“我的位置按钮”点击事件自定义，反之不设置则由Map Kit执行点击后默认事件，即地图移动到当前用户位置。

```typescript
let callback = () => {
  console.info('myLocationButtonClick', `myLocationButtonClick`);
};
this.mapEventManager.on('myLocationButtonClick', callback);
```

### 隐藏“我的位置”按钮

控制是否显示“我的位置”按钮。

```typescript
this.mapController.setMyLocationControlsEnabled(false);
```

### 自定义位置图标样式

通过调用mapController.[setMyLocationStyle](../harmonyos-references/map-map-mapcomponentcontroller.md#setmylocationstyle)方法，设置用户位置图标样式。效果如下：

```typescript
let style: mapCommon.MyLocationStyle = {
  anchorU: 0.5,
  anchorV: 0.5,
  radiusFillColor: 0xffff0000,
  // icon为自定义图标资源，使用时需要替换
  // 图标存放在resources/rawfile，icon参数传入rawfile文件夹下的相对路径
  icon: 'test.png'
};
await this.mapController.setMyLocationStyle(style);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/Z8f2MLoZTiu8KOzUZv0YHw/zh-cn_image_0000002712405234.jpg "点击放大")

### 更改我的位置图层相对于覆盖物的压盖顺序

通过调用mapController.[changeMyLocationLayerOrder](../harmonyos-references/map-map-mapcomponentcontroller.md#changemylocationlayerorder)方法，更改我的位置图层相对于覆盖物的压盖顺序。效果如下：

```typescript
// true：我的位置图层位于覆盖物之下
this.mapController?.changeMyLocationLayerOrder(true);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/ZlPQU33UR-ini6vhQx1CZw/zh-cn_image_0000002742124183.jpg "点击放大")
