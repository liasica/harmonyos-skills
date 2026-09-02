---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-20
title: Map Kit地图服务如何设置我的位置图标实时指向当前设备移动方向
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > Map Kit地图服务如何设置我的位置图标实时指向当前设备移动方向
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:25+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:feb5d97f3077235a799f9322e89053a161b076a6140f741b661f1fa1532c0043
---

## 问题现象

Map Kit地图中，我的位置当前可以通过设置mapCommon.MyLocationDisplayType.FOLLOW\_ROTATE，实现我的位置图标实时指向设备旋转方向。

如何实现我的位置图标实时指向设备的移动方向，比如在跑步场景，我的位置实时指向跑步的方向。

## 背景知识

* [MyLocationDisplayType](../harmonyos-references/map-common.md#mylocationdisplaytype)：定位图标的展示模式。类型设置为FOLLOW时，表示连续定位，且将相机移动到地图中心点，定位蓝点跟随设备移动。
* [setMyLocationStyle](../harmonyos-references/map-map-mapcomponentcontroller.md#setmylocationstyle)：设置用户的位置样式。设置icon参数可以自定义我的位置图标样式。displayType参数设置可以设置定位图标的展示样式，可以设置相机是否跟随移动、我的位置图标是否跟随设备旋转等。
* [setMyLocation](../harmonyos-references/map-map-mapcomponentcontroller.md#setmylocation)：Map Kit默认使用系统的连续定位能力显示用户位置，如果希望定制显示频率或者精准度等，可以调用此接口设置“我的位置”坐标。
* [geoLocationManager.on('locationChange')](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanageronlocationchange)：开启位置变化订阅，并发起定位请求。可实时监听当前设备的位置信息，其中包括设备的移动方向信息。

## 解决方案

前提条件：

* 需要申请"ohos.permission.LOCATION"和"ohos.permission.APPROXIMATELY\_LOCATION"位置权限。
* 需要[开通地图服务](../harmonyos-guides/map-config-agc.md#开通地图服务)。

1. 设置我的位置图标自定义样式和移动效果，此方案场景，需设置displayType参数为mapCommon.MyLocationDisplayType.FOLLOW（我的位置图标不跟随或设备方向旋转）。

   ```ts
   let style: mapCommon.MyLocationStyle = {
     anchorU: 0.5,
     anchorV: 0.5,
     icon: $r('app.media.startIcon'), // 此处替换为自定义的我的位置图标
     displayType: mapCommon.MyLocationDisplayType.FOLLOW
   };
   await this.mapController.setMyLocationStyle(style);
   this.mapController.setMyLocationEnabled(true);
   ```
2. 通过geoLocationManager.on('locationChange')监听当前设备的位置信息[Location](../harmonyos-references/js-apis-geolocationmanager.md#location)，其中包括设备的移动方向信息（direction）。在监听回调中通过setMyLocation接口设置地图上我的位置图标的位置信息，其中包括显示我的位置图标方向为direction设备移动方向。

   ```ts
   let requestInfo: geoLocationManager.LocationRequest = {
     'priority': geoLocationManager.LocationRequestPriority.FIRST_FIX,
     'scenario': geoLocationManager.LocationRequestScenario.UNSET,
     'timeInterval': 1,
     'distanceInterval': 0,
     'maxAccuracy': 0
   };
   let locationChange = (location: geoLocationManager.Location): void => {
     location.accuracy = 0;
     this.mapController?.setMyLocation(location);
   };
   try {
     geoLocationManager.on('locationChange', requestInfo, locationChange);
   } catch (err) {
     console.error("errCode:" + err.code + ", message:" + err.message);
   }
   ```

**说明** 

direction设备移动方向只有在使用GPS定位时才返回有效值，请在空旷的室外进行测试验证。

完整示例参考如下：

```ts
import { mapCommon, MapComponent, map } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';
import { geoLocationManager } from '@kit.LocationKit';

@Entry
@Component
struct MyLocationDirection {
  private mapOptions?: mapCommon.MapOptions;
  private callback?: AsyncCallback<map.MapComponentController>;
  private mapController?: map.MapComponentController;

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
        let style: mapCommon.MyLocationStyle = {
          anchorU: 0.5,
          anchorV: 0.5,
          icon: $r('app.media.startIcon'), // 此处替换为自定义的我的位置图标
          displayType: mapCommon.MyLocationDisplayType.FOLLOW
        };
        await this.mapController.setMyLocationStyle(style);
        this.mapController.setMyLocationEnabled(true);

        let requestInfo: geoLocationManager.LocationRequest = {
          'priority': geoLocationManager.LocationRequestPriority.FIRST_FIX,
          'scenario': geoLocationManager.LocationRequestScenario.UNSET,
          'timeInterval': 1,
          'distanceInterval': 0,
          'maxAccuracy': 0
        };
        let locationChange = (location: geoLocationManager.Location): void => {
          location.accuracy = 0;
          this.mapController?.setMyLocation(location);
        };
        try {
          geoLocationManager.on('locationChange', requestInfo, locationChange);
        } catch (err) {
          console.error("errCode:" + err.code + ", message:" + err.message);
        }
      }
    };
  }

  build() {
    Stack() {
      // 调用MapComponent组件初始化地图
      MapComponent({
        mapOptions: this.mapOptions,
        mapCallback: this.callback,
      })
        .width('100%')
        .height('100%');
    }.height('100%')
  }
}
```
