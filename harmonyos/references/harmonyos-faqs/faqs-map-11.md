---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-11
title: 在地图上实现定位功能
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > 在地图上实现定位功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:d992ce741055885f9e333a5719275d5caa5bb0cf4bc1bedf43db7b816bb0f2bc
---

## 问题现象

获取当前位置并显示在地图上。

## 背景知识

[MapComponent（地图组件）](../harmonyos-references/map-mapcomponent.md)是地图服务提供的特殊组件，允许开发者自定义一个地图并显示在自己的应用中。

## 解决方案

1. 使用地图服务，必须使用手动签名，并在AGC平台配置开启地图服务，参考[地图开发准备](../harmonyos-guides/map-config-agc.md)。
2. 打开设备状态栏，开启“位置功能”开关。
3. 使用定位功能，需要声明相关权限，可在module.json5中配置requestPermissions字段。申请如下权限：ohos.permission.APPROXIMATELY\_LOCATION，ohos.permission.LOCATION，ohos.permission.LOCATION\_IN\_BACKGROUND。
4. 完成申请权限函数，用于向用户弹窗申请定位权限。主要实现原理为调用[requestPermissionsFromUser](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)接口。

   ```ts
   // 校验应用是否被授权定位权限，可以通过调用checkAccessToken()方法来校验当前是否已经授权。
   async checkPermission(): Promise<void> {

     let applyResult: boolean = false;
     const permissions: Array<Permissions> =
       ['ohos.permission.LOCATION', 'ohos.permission.APPROXIMATELY_LOCATION'];
     for (let permission of permissions) {
       let grantStatus: abilityAccessCtrl.GrantStatus = await this.checkAccessToken(permission);
       if (grantStatus === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED) {
         applyResult = true;
       } else {
         applyResult = false;
       }
     }

     if (!applyResult) {
       this.requestPermissions();
     } else {
       // 启用我的位置图层，mapController为地图操作类对象，获取方式详见地图呈现章节
       this.mapController?.setMyLocationEnabled(true);
       // 启用我的位置按钮
       this.mapController?.setMyLocationControlsEnabled(true);
     }
   }

   // 向用户申请授权
   requestPermissions(): void {
     let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
     atManager.requestPermissionsFromUser(this.getUIContext().getHostContext() as common.UIAbilityContext,
       ['ohos.permission.LOCATION', 'ohos.permission.APPROXIMATELY_LOCATION', 'ohos.permission.INTERNET'])
       .then(() => {
         // 启用我的位置图层
         this.mapController?.setMyLocationEnabled(true);
         // 启用我的位置按钮
         this.mapController?.setMyLocationControlsEnabled(true);
         this.getMyLocation();

       })
       .catch((err: BusinessError) => {
         console.error(`Failed to request permissions from user. Code is ${err.code}, message is ${err.message}`);
       });
   }

   // 获取相应的权限
   async checkAccessToken(permission: Permissions): Promise<abilityAccessCtrl.GrantStatus> {
     let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
     let grantStatus:
       abilityAccessCtrl.GrantStatus = abilityAccessCtrl.GrantStatus.PERMISSION_DENIED;

     // 获取应用程序的accessTokenID
     let tokenId: number = 0;
     try {
       let bundleInfo: bundleManager.BundleInfo =
         await bundleManager.getBundleInfoForSelf(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION);
       let appInfo: bundleManager.ApplicationInfo = bundleInfo.appInfo;
       tokenId = appInfo.accessTokenId;
     } catch (error) {
       let err: BusinessError = error as BusinessError;
       console.error(`Failed to get bundle info for self. Code is ${err.code},message is ${err.message}`);
     }

     // 校验应用是否被授予权限
     try {
       grantStatus = await atManager.checkAccessToken(tokenId, permission);
     } catch (error) {
       let err: BusinessError = error as BusinessError;
       console.error(`Failed to check access token. Code is ${err.code}, message is ${err.message}`);
     }
     return grantStatus;
   }
   ```
5. 完成定位函数，主要用于获取当前的位置信息，并将当前的地图视图相机移动到该位置。主要实现原理是调用[getCurrentLocation](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetcurrentlocation)接口获取当前位置信息，调用[setMyLocation](../harmonyos-references/map-map-mapcomponentcontroller.md#setmylocation)接口将当前的地图视图相机移动过去。需要注意：[getCurrentLocation](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetcurrentlocation)接口获取的是WGS-84坐标系坐标，而地图显示的是GCJ02坐标系坐标，需要使用[convertCoordinate](../harmonyos-references/map-map-functions.md#convertcoordinate)接口进行一次转换。

   ```ts
   // 获取当前位置并视图移动过去
   getMyLocation() {
     // getCurrentLocation获取当前位置，使用Promise异步回调。
     geoLocationManager.getCurrentLocation()
       .then(async (result) => {
         console.info(`MapSignIn getMyLocation = ${JSON.stringify(result)}`);
         let position: geoLocationManager.Location = {
           'latitude': result.latitude,
           'longitude': result.longitude,
           'altitude': 0,
           'accuracy': 0,
           'speed': 0,
           'timeStamp': 0,
           'direction': 0,
           'timeSinceBoot': 0
         };

         // 在地图组件上设置“我的位置”坐标。
         this.mapController?.setMyLocation(position);

         // 创建CameraUpdate对象
         let gcj02Position: mapCommon.LatLng = await this.convertCoordinate(result.latitude, result.longitude);
         let latLng: mapCommon.LatLng = {
           latitude: gcj02Position.latitude,
           longitude: gcj02Position.longitude
         };
         let zoom = 17;
         let cameraUpdate = map.newLatLng(latLng, zoom);

         // 以动画方式移动地图相机
         this.mapController?.animateCamera(cameraUpdate, 1000);
       })
       .catch((error:BusinessError) => {
         console.error('promise, getCurrentLocation: error=' + JSON.stringify(error));
       });
   }

   // 将WGS84坐标转为GCJ02坐标
   async convertCoordinate(latitude: number, longitude: number): Promise<mapCommon.LatLng> {
     let wgs84Position: mapCommon.LatLng = {
       latitude: latitude,
       longitude: longitude
     };

     let gcj02Postion: mapCommon.LatLng =
       await map.convertCoordinate(mapCommon.CoordinateType.WGS84, mapCommon.CoordinateType.GCJ02, wgs84Position);

     return gcj02Postion;
   }
   ```
6. 完成以上函数后，最后使用[MapComponent](../harmonyos-references/map-mapcomponent.md)组件，生成一张新的地图。在aboutToAppear函数中向用户弹窗并获取定位授权。设置启用“我的位置”按钮，运行应用后点击按钮，即可进行我的位置定位。

   ```ts
   import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
   import { abilityAccessCtrl, bundleManager, common, Permissions } from '@kit.AbilityKit';
   import { geoLocationManager } from '@kit.LocationKit';
   import { map, MapComponent, mapCommon } from '@kit.MapKit';

   @Entry
   @Component
   struct HuaweiMapDemo {
     // 定义参数mapOption,设置地图中心点坐标以及层级。
     private mapOption?: mapCommon.MapOptions;
     // 定义参数callback,通过callback回调的方式获取MapComponentController对象，用来操作地图。
     private callback?: AsyncCallback<map.MapComponentController>;
     // 定义地图参数mapController，获取地图的控制器类，用来操作地图
     private mapController?: map.MapComponentController;

     aboutToAppear(): void {
       this.checkPermission();

       // 地图初始化参数，设置地图中心坐标以及层级
       this.mapOption = {
         position: {
           target: {
             latitude: 39.9,
             longitude: 116.4
           },
           zoom: 10
         },
         myLocationControlsEnabled: true,
         scaleControlsEnabled: true,
       };
       // 地图初始化的回调
       this.callback = async (err, mapController) => {
         if (!err) {

           // 获取地图的控制器类，用来操作地图
           this.mapController = mapController;
           // 开启3d建筑图层
           let cameraUpdate = map.zoomTo(18);
           this.mapController?.moveCamera(cameraUpdate);
           this.mapController?.setBuildingEnabled(true);

           // 启用我的位置图层
           this.mapController?.setMyLocationEnabled(true);
           // 启用我的位置按钮
           this.mapController?.setMyLocationControlsEnabled(true);

           let style: mapCommon.MyLocationStyle = {
             anchorU: 0.5,
             anchorV: 0.5,
             radiusFillColor: 0xffff0000,
             // icon为自定义图标资源，使用时需要替换
             icon: $r('app.media.there'),
           };
           await this.mapController.setMyLocationStyle(style);

           // 初始化我的位置
           this.getMyLocation();
         }
       };
     }

     build() {
       Stack() {

         MapComponent({ mapOptions: this.mapOption, mapCallback: this.callback }).width('100%').height('100%');
       }.height('100%')
     }

     // 校验应用是否被授权定位权限，可以通过调用checkAccessToken()方法来校验当前是否已经授权。
     async checkPermission(): Promise<void> {

       let applyResult: boolean = false;
       const permissions: Array<Permissions> =
         ['ohos.permission.LOCATION', 'ohos.permission.APPROXIMATELY_LOCATION'];
       for (let permission of permissions) {
         let grantStatus: abilityAccessCtrl.GrantStatus = await this.checkAccessToken(permission);
         if (grantStatus === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED) {
           applyResult = true;
         } else {
           applyResult = false;
         }
       }

       if (!applyResult) {
         this.requestPermissions();
       } else {
         // 启用我的位置图层，mapController为地图操作类对象，获取方式详见地图呈现章节
         this.mapController?.setMyLocationEnabled(true);
         // 启用我的位置按钮
         this.mapController?.setMyLocationControlsEnabled(true);
       }
     }

     // 向用户申请授权
     requestPermissions(): void {
       let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
       atManager.requestPermissionsFromUser(this.getUIContext().getHostContext() as common.UIAbilityContext,
         ['ohos.permission.LOCATION', 'ohos.permission.APPROXIMATELY_LOCATION', 'ohos.permission.INTERNET'])
         .then(() => {
           // 启用我的位置图层
           this.mapController?.setMyLocationEnabled(true);
           // 启用我的位置按钮
           this.mapController?.setMyLocationControlsEnabled(true);
           this.getMyLocation();

         })
         .catch((err: BusinessError) => {
           console.error(`Failed to request permissions from user. Code is ${err.code}, message is ${err.message}`);
         });
     }

     // 获取相应的权限
     async checkAccessToken(permission: Permissions): Promise<abilityAccessCtrl.GrantStatus> {
       let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
       let grantStatus:
         abilityAccessCtrl.GrantStatus = abilityAccessCtrl.GrantStatus.PERMISSION_DENIED;

       // 获取应用程序的accessTokenID
       let tokenId: number = 0;
       try {
         let bundleInfo: bundleManager.BundleInfo =
           await bundleManager.getBundleInfoForSelf(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION);
         let appInfo: bundleManager.ApplicationInfo = bundleInfo.appInfo;
         tokenId = appInfo.accessTokenId;
       } catch (error) {
         let err: BusinessError = error as BusinessError;
         console.error(`Failed to get bundle info for self. Code is ${err.code},message is ${err.message}`);
       }

       // 校验应用是否被授予权限
       try {
         grantStatus = await atManager.checkAccessToken(tokenId, permission);
       } catch (error) {
         let err: BusinessError = error as BusinessError;
         console.error(`Failed to check access token. Code is ${err.code}, message is ${err.message}`);
       }
       return grantStatus;
     }

     // 获取当前位置并视图移动过去
     getMyLocation() {
       // getCurrentLocation获取当前位置，使用Promise异步回调。
       geoLocationManager.getCurrentLocation()
         .then(async (result) => {
           console.info(`MapSignIn getMyLocation = ${JSON.stringify(result)}`);
           let position: geoLocationManager.Location = {
             'latitude': result.latitude,
             'longitude': result.longitude,
             'altitude': 0,
             'accuracy': 0,
             'speed': 0,
             'timeStamp': 0,
             'direction': 0,
             'timeSinceBoot': 0
           };

           // 在地图组件上设置“我的位置”坐标。
           this.mapController?.setMyLocation(position);

           // 创建CameraUpdate对象
           let gcj02Position: mapCommon.LatLng = await this.convertCoordinate(result.latitude, result.longitude);
           let latLng: mapCommon.LatLng = {
             latitude: gcj02Position.latitude,
             longitude: gcj02Position.longitude
           };
           let zoom = 17;
           let cameraUpdate = map.newLatLng(latLng, zoom);

           // 以动画方式移动地图相机
           this.mapController?.animateCamera(cameraUpdate, 1000);
         })
         .catch((error:BusinessError) => {
           console.error('promise, getCurrentLocation: error=' + JSON.stringify(error));
         });
     }

     // 将WGS84坐标转为GCJ02坐标
     async convertCoordinate(latitude: number, longitude: number): Promise<mapCommon.LatLng> {
       let wgs84Position: mapCommon.LatLng = {
         latitude: latitude,
         longitude: longitude
       };

       let gcj02Postion: mapCommon.LatLng =
         await map.convertCoordinate(mapCommon.CoordinateType.WGS84, mapCommon.CoordinateType.GCJ02, wgs84Position);

       return gcj02Postion;
     }

   }
   ```

## 常见FAQ

Q：地图白屏不显示。

A：请参考官方文档[地图不显示](../harmonyos-guides/map-faq-1.md)。

Q：如何获取当前显示页面的中心点。

A：可以使用[getCameraPosition](../harmonyos-references/map-map-mapcomponentcontroller.md#getcameraposition)接口，返回的数据中target字段就是地图中心位置的经纬度坐标。

Q：地图中我的位置功能失效如何排查？

A：按照以下步骤进行排查：

* 确认是否获取到定位权限。
  1. 检查下module.json5里面是否申请ohos.permission.LOCATION和ohos.permission.APPROXIMATELY\_LOCATION权限。
  2. 位置服务需要用户授权。
  3. 系统设置-应用和元服务-应用里检查是否有位置权限。
* 确认是否开启“我的位置”图层功能开关。使用[setMyLocationEnabled](../harmonyos-references/map-map-mapcomponentcontroller.md#setmylocationenabled)接口，参数设置为true时启用“我的位置”图层。

Q：如何用代码判断是否启动我的位置图层和我的位置按钮？

A：使用[isMyLocationEnabled](../harmonyos-references/map-map-mapcomponentcontroller.md#ismylocationenabled)获取“我的位置”图层的开启状态，使用[isMyLocationControlsEnabled](../harmonyos-references/map-map-mapcomponentcontroller.md#ismylocationcontrolsenabled)获取“我的位置”按钮的启用状态。
