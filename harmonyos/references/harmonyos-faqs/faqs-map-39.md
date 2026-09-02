---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-39
title: 如何在WGS84坐标系实现FOLLOW_ROTATE相同定位展示效果
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > 如何在WGS84坐标系实现FOLLOW_ROTATE相同定位展示效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:222961bde8b76fdfec2816a5dd17acfc6b7af3178b5f3702537bf0f88e0bac80
---

## 问题现象

Map Kit使用GCJ02坐标系，当使用WGS84坐标图源时，使用Map Kit自带的setMyLocation设置我的位置时，我的位置图标是GCJ02坐标系，在WGS84坐标地图上会产生偏移，所以无法使用自带的我的位置相关能力。

使用WGS84坐标图源时，如何通过Marker实现MyLocationDisplayType.FOLLOW\_ROTATE相同效果，即连续定位，且将相机移动到地图中心点，定位蓝点依照设备方向旋转，并且会跟随设备移动。

## 背景知识

[sensor.on](../harmonyos-references/js-apis-sensor.md#sensoronsensoridorientation9)：传感器订阅，其中[ORIENTATION](../harmonyos-references/js-apis-sensor.md#sensoronsensoridorientation9)表示订阅方向传感器数据。

[setRotation](../harmonyos-references/map-map-marker.md#setrotation)：设置标记的旋转角度，即标记围绕标记锚点顺时针旋转的角度，旋转轴垂直于标记。

[setPosition](../harmonyos-references/map-map-marker.md#setposition)：设置标记的位置坐标。

[geoLocationManager.on('locationChange')](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanageronlocationchange)：开启位置变化订阅，并发起定位请求。

## 解决方案

前提条件：需申请ohos.permission.LOCATION、ohos.permission.APPROXIMATELY\_LOCATION、ohos.permission.ACCELEROMETER权限。

1. 创建Marker标记。

   ```ts
   let markerOptions: mapCommon.MarkerOptions = {
     position: {
       latitude: 31.984410259206815,
       longitude: 118.76625379397866
     },
     rotation: 0,
     visible: true,
     zIndex: 0,
     alpha: 1,
     anchorU: 0.5,
     anchorV: 0.5,
     clickable: true,
     draggable: true,
     flat: false
   };
   this.marker = await this.mapController.addMarker(markerOptions);
   ```
2. 通过sensor.on(sensor.SensorId.ORIENTATION)监听设备方向，通过setRotation设置Marker标记的旋转角度为设备方向角度。

   ```ts
   try {
     sensor.on(sensor.SensorId.ORIENTATION, (data: sensor.OrientationResponse) => {
       let direction = Math.round(data.alpha);
       let nowOrientation = display.getDefaultDisplaySync().orientation;
       if (nowOrientation !== 0) {
         direction = direction - 90 * nowOrientation;
         if (direction < 0) {
           direction = direction + 360;
         }
       }
       this.marker?.setRotation(direction);
     }, { interval: 100000000 });
   } catch (error) {
     console.error(`Failed to invoke on. Code: ${error.code}, message: ${error.message}`);
   }
   ```
3. 通过geoLocationManager.on('locationChange')监听位置变化，使用setPosition设置标记的位置为监听返回的坐标。注意位置监听返回的坐标是WGS84坐标系，在WGS84图源上直接使用该坐标设置Marker位置即可，无需转换为GCJ02坐标系。

   同时配置moveCamera接口将相机移动至marker为屏幕中心点。

   ```ts
   let requestInfo: geoLocationManager.LocationRequest = {
     'priority': geoLocationManager.LocationRequestPriority.FIRST_FIX,
     'scenario': geoLocationManager.LocationRequestScenario.UNSET,
     'timeInterval': 1,
     'distanceInterval': 0,
     'maxAccuracy': 0
   };
   let locationChange = (location: geoLocationManager.Location): void => {
     console.info('locationChange: data: ' + JSON.stringify(location));
     // 添加WGS84坐标Marker
     this.marker?.setPosition(location);
     // 并将相机移动到地图中心点
     let cameraUpdate = map.newLatLng(location);
     this.mapController?.moveCamera(cameraUpdate);
   };
   ```

完整代码：

Index.ets:

```ts
import { map, mapCommon, MapComponent } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';
import { geoLocationManager } from '@kit.LocationKit';
import { sensor } from '@kit.SensorServiceKit';
import { display } from '@kit.ArkUI';
import { Permissions } from '@kit.AbilityKit';
import PermissionsRequest from '../utils/PermissionsRequest';

@Entry
@Component
struct Index {
  private mapOptions?: mapCommon.MapOptions;
  private mapController?: map.MapComponentController;
  private callback?: AsyncCallback<map.MapComponentController>;
  private marker?: map.Marker;

  async aboutToAppear() {
    this.mapOptions = {
      position: {
        target: {
          latitude: 31.984410259206815,
          longitude: 118.76625379397866
        },
        zoom: 15
      }
    };

    this.callback = async (err, mapController) => {
      if (!err) {
        this.mapController = mapController;
        let permissions: Array<Permissions> = ['ohos.permission.LOCATION', 'ohos.permission.APPROXIMATELY_LOCATION'];
        await PermissionsRequest.commonRequestPermissions(this.getUIContext(), permissions);
        let markerOptions: mapCommon.MarkerOptions = {
          position: {
            latitude: 31.984410259206815,
            longitude: 118.76625379397866
          },
          rotation: 0,
          visible: true,
          zIndex: 0,
          alpha: 1,
          anchorU: 0.5,
          anchorV: 0.5,
          clickable: true,
          draggable: true,
          flat: false
        };
        this.marker = await this.mapController.addMarker(markerOptions);
        // 监听设备方向，设置Marker的旋转角度
        try {
          sensor.on(sensor.SensorId.ORIENTATION, (data: sensor.OrientationResponse) => {
            let direction = Math.round(data.alpha);
            let nowOrientation = display.getDefaultDisplaySync().orientation;
            if (nowOrientation !== 0) {
              direction = direction - 90 * nowOrientation;
              if (direction < 0) {
                direction = direction + 360;
              }
            }
            this.marker?.setRotation(direction);
          }, { interval: 100000000 });
        } catch (error) {
          console.error(`Failed to invoke on. Code: ${error.code}, message: ${error.message}`);
        }

        // 持续监听设备位置，更新Marker点的位置
        let requestInfo: geoLocationManager.LocationRequest = {
          'priority': geoLocationManager.LocationRequestPriority.FIRST_FIX,
          'scenario': geoLocationManager.LocationRequestScenario.UNSET,
          'timeInterval': 1,
          'distanceInterval': 0,
          'maxAccuracy': 0
        };
        let locationChange = (location: geoLocationManager.Location): void => {
          console.info('locationChange: data: ' + JSON.stringify(location));
          // 添加WGS84坐标Marker
          this.marker?.setPosition(location);
          // 并将相机移动到地图中心点
          let cameraUpdate = map.newLatLng(location);
          this.mapController?.moveCamera(cameraUpdate);
        };
        try {
          geoLocationManager.on('locationChange', requestInfo, locationChange);
        } catch (err) {
          console.error(`监听位置失败, code is: ${err.code}, message is: ${err.message}`);
        }
      } else {
        console.error(`地图初始化失败, code is：${err.code}, message is ${err.message}`);
      }
    };
  }

  build() {
    Stack({ alignContent: Alignment.End }) {
      Column() {
        MapComponent({
          mapOptions: this.mapOptions,
          mapCallback: this.callback,
        })
          .width('100%')
          .height('100%');
      }.width('100%');
    }.height('100%');
  }
}
```

utils/PermissionsRequest.ets:

```ts
import { abilityAccessCtrl, bundleManager, common, Permissions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { preferences } from '@kit.ArkData';
import { hilog } from '@kit.PerformanceAnalysisKit';

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

export default new PermissionsRequest();
```
