---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-40
title: 如何在打开地图时，自动移动相机到当前设备位置
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > 如何在打开地图时，自动移动相机到当前设备位置
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:06731b945984c5226f2a79ff26589e13acb1059ede8badf5f815736253f97c0e
---

## 问题现象

初始化地图时，会显示初始化配置的默认坐标位置，如何实现在打开地图时，相机视野自动移动到当前设备所在的坐标位置。

## 背景知识

* 开发准备：使用地图服务，需要先[开通地图服务](../harmonyos-guides/map-config-agc.md#开通地图服务)。
* [geoLocationManager.getCurrentLocation](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetcurrentlocation-2)：获取当前设备所在位置。
* [moveCamera](../harmonyos-references/map-map-mapcomponentcontroller.md#movecamera)：更新相机状态。

## 解决方案

前提条件：使用地图服务，需要先[开通地图服务](../harmonyos-guides/map-config-agc.md#开通地图服务)；使用位置服务，需要声明位置权限“ohos.permission.LOCATION”、“ohos.permission.APPROXIMATELY\_LOCATION”，参见[在配置文件中声明权限](../harmonyos-guides/declare-permissions.md#在配置文件中声明权限)。

1. 在地图初始化完成的callback回调函数中，通过getCurrentLocation接口获取当前位置坐标，因为接口获取的是WGS84坐标，需使用convertCoordinateSync接口转换为GCJ02坐标提供给地图使用。

   ```ts
   await geoLocationManager.getCurrentLocation().then(async (location: geoLocationManager.Location) => {
     this.myLocationLatLng =
       await map.convertCoordinateSync(mapCommon.CoordinateType.WGS84, mapCommon.CoordinateType.GCJ02, location);
     this.mapController?.setMyLocationEnabled(true);
   }).catch((err: BusinessError) => {
     console.error(`getCurrentLocationPosition failed, code: ${err.code}, message: ${err.message}`);
   });
   ```
2. 将转换后的当前位置坐标，设置为相机的target位置参数，调用moveCamera接口，移动相机到当前位置。

   ```ts
   let cameraPosition: mapCommon.CameraPosition = {
     target: this.myLocationLatLng,
     zoom: 15
   };
   // 新建CameraUpdate对象
   let cameraUpdate: map.CameraUpdate = map.newCameraPosition(cameraPosition);
   // 移动相机
   this.mapController?.moveCamera(cameraUpdate);
   ```

实现效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/sGXMKjj5Qnq1Fa7QtJ5R0Q/zh-cn_image_0000002658913601.png "点击放大")

完整示例参考如下：

```ts
import { abilityAccessCtrl, bundleManager, common, Permissions } from '@kit.AbilityKit';
import { BusinessError, AsyncCallback } from '@kit.BasicServicesKit';
import { MapComponent, mapCommon, map } from '@kit.MapKit';
import { geoLocationManager } from '@kit.LocationKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { preferences } from '@kit.ArkData';
import { UIContext } from '@ohos.arkui.UIContext';
import { display } from '@kit.ArkUI';

class PermissionsRequest {
  /**
   * 通用申请权限
   */
  async commonRequestPermissions(context: UIContext, permissions: Array<Permissions>) {
    let isPermission: boolean = await this.checkPermissions(permissions);
    if (!isPermission) {
      //一次授权
      let isDialogShown = await this.requestPermissions(context, permissions);
      if (isDialogShown !== true) {
        //二次授权
        this.requestPermissionsOnSetting(context, permissions);
      }
    }
  }

  /**
   * 校验应用是否被授权
   */
  async checkPermissions(permissions: Array<Permissions>) {
    for (let permission of permissions) {
      let grantStatus: abilityAccessCtrl.GrantStatus = await this.checkAccessToken(permission);
      if (grantStatus !== abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED) {
        return false;
      }
    }
    return true;
  }

  async checkAccessToken(permission: Permissions): Promise<abilityAccessCtrl.GrantStatus> {
    let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    let grantStatus: abilityAccessCtrl.GrantStatus = abilityAccessCtrl.GrantStatus.PERMISSION_DENIED;

    // 获取应用程序的accessTokenID
    let tokenId: number = 0;
    try {
      let bundleInfo: bundleManager.BundleInfo =
        await bundleManager.getBundleInfoForSelf(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION);
      let appInfo: bundleManager.ApplicationInfo = bundleInfo.appInfo;
      tokenId = appInfo.accessTokenId;
      grantStatus = await atManager.checkAccessToken(tokenId, permission);
    } catch (error) {
      let err: BusinessError = error as BusinessError;
      hilog.error(0x000, 'testTag', `Failed to check access token  ${err.code}, message is ${err.message}`);
    }
    return grantStatus;
  }

  /**
   * 申请用户授权
   */
  async requestPermissions(context: UIContext, permissions: Array<Permissions>): Promise<boolean | undefined> {
    let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    try {
      let data =
        await atManager.requestPermissionsFromUser(context.getHostContext() as common.UIAbilityContext, permissions);
      hilog.info(0x000, 'testTag', 'requestPermissions1 success', JSON.stringify(data));
      return data.dialogShownResults ? data.dialogShownResults[0] : undefined; // 返回请求是否有弹窗
    } catch (e) {
      hilog.error(0x000, 'testTag', `requestPermissions1 err Code is ${e.code}, message is ${e.message}`);
      return undefined;
    }
  }

  /**
   * 2次申请用户授权
   */
  requestPermissionsOnSetting(context: UIContext, permissions: Array<Permissions>) {
    let keyPerms = JSON.stringify(permissions);
    let store = preferences.getPreferencesSync(context.getHostContext(), { name: 'permsHasOnSetting' });
    let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    atManager.requestPermissionOnSetting(context.getHostContext(), permissions)
      .then((res: Array<abilityAccessCtrl.GrantStatus>) => {
        hilog.info(0x000, 'testTag', 'requestPermissions2 success', JSON.stringify(res));
        store.putSync(keyPerms, 1);
        store.flush();
      })
      .catch((err: BusinessError) => {
        hilog.info(0x000, 'testTag', 'requestPermissions2 err', JSON.stringify(err));
      });
  }
}

@Entry
@Component
struct MoveToMyLocation {
  private mapOptions?: mapCommon.MapOptions;
  private callback?: AsyncCallback<map.MapComponentController>;
  private mapController?: map.MapComponentController;
  private myLocationLatLng: mapCommon.LatLng = {
    latitude: 39.9,
    longitude: 116.4
  };
  @State mapHeight: number = 0;
  PermissionsRequest = new PermissionsRequest();

  async aboutToAppear() {
    let displayClass = display.getDefaultDisplaySync();
    this.mapHeight = this.getUIContext().px2vp(displayClass.height);
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
        let permissions: Array<Permissions> = ['ohos.permission.LOCATION', 'ohos.permission.APPROXIMATELY_LOCATION'];
        await this.PermissionsRequest.commonRequestPermissions(this.getUIContext(), permissions);
        await geoLocationManager.getCurrentLocation().then(async (location: geoLocationManager.Location) => {
          this.myLocationLatLng =
            await map.convertCoordinateSync(mapCommon.CoordinateType.WGS84, mapCommon.CoordinateType.GCJ02, location);
          this.mapController?.setMyLocationEnabled(true);
        }).catch((err: BusinessError) => {
          console.error(`getCurrentLocationPosition failed, code: ${err.code}, message: ${err.message}`);
        });

        let cameraPosition: mapCommon.CameraPosition = {
          target: this.myLocationLatLng,
          zoom: 15
        };
        // 新建CameraUpdate对象
        let cameraUpdate: map.CameraUpdate = map.newCameraPosition(cameraPosition);
        // 移动相机
        this.mapController?.moveCamera(cameraUpdate);
      } else {
        console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
      }
    };
  }

  build() {
    Stack() {
      // 调用MapComponent组件初始化地图
      MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
        .width('100%')
        .height(this.mapHeight)
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
    }.height('100%');
  }
}
```
