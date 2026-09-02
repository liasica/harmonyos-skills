---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-13
title: Map Kit如何知道地图进行了缩放
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > Map Kit如何知道地图进行了缩放
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:1a4437a52b94136b0c945a6dedbe9965cc95a5f0d6a49024074238492982a30a
---

## 问题现象

应用在用户使用过程中需要知道用户是否进行了地图缩放，是否有地图缩放事件通知？

## 背景知识

[Map Kit](../harmonyos-guides/map-introduction.md)：具备丰富地图的细节呈现能力，提供了包括缩放、旋转、移动、倾斜等流畅的交互体验。

## 解决方案

通过[on(type: 'cameraChange')](../harmonyos-references/map-map-mapeventmanager.md#oncamerachange)监听地图相机状态变化事件，回调里通过zoom是否变化来判断是否有缩放行为。zoom获取方式为：this.mapController?.getCameraPosition().zoom。

```ts
import { map, mapCommon, MapComponent } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';
import { geoLocationManager } from '@kit.LocationKit';

/**
 *
 * 1、监听用户是否进行地图缩放
 * 2、监听“我的位置”按钮点击事件，并初始化我的位置
 */
@Entry
@Component
struct MapOnChangeZoom {
  private mapOption?: mapCommon.MapOptions;
  private callback?: AsyncCallback<map.MapComponentController>;
  private mapController?: map.MapComponentController;

  aboutToAppear(): void {
    // 地图初始化参数，设置地图中心点坐标及层级
    this.mapOption = {
      position: {
        target: {
          latitude: 30.246,
          longitude: 120.145
        },
        zoom: 17
      },
      zoomControlsEnabled: false,
      myLocationControlsEnabled: true
    };

    // 地图初始化的回调
    this.callback = async (err, mapController) => {
      if (!err) {
        // 获取地图的控制器类，用来操作地图
        this.mapController = mapController;
        // 启用我的位置图层
        this.mapController?.setMyLocationEnabled(true);

        let mapEventManager = mapController.getEventManager();
        let cameraChangeCallback = (position: mapCommon.LatLng) => {
          console.info('cameraChange', `callback position = ${position.longitude}`);
          // 获取当前地图缩放级别，通过zoom是否变化来判断是否有缩放行为
          let zoom = this.mapController?.getCameraPosition().zoom;
          console.info('cameraChange', `callback zoom = ${zoom}`);
        };
        mapEventManager.on('cameraChange', cameraChangeCallback);

        // 监听“我的位置”按钮点击事件
        this.mapController.on('myLocationButtonClick', () => {
          console.info('myLocationButtonClick', `myLocationButtonClick`);
          this.getMyLocation();
        });

        // 初始化我的位置
        this.getMyLocation();
      }
    };
  }

  build() {
    Column() {
      MapComponent({ mapOptions: this.mapOption, mapCallback: this.callback }).width('100%').height('100%');
    };
  }

  // 获取当前位置并视图移动过去
  getMyLocation() {
    geoLocationManager.getCurrentLocation().then(async (result) => {
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
    });
  }

  async convertCoordinate(latitude: number, longitude: number): Promise<mapCommon.LatLng> {
    let wgs84Position: mapCommon.LatLng = {
      latitude: latitude,
      longitude: longitude
    };
    let gcj02Position: mapCommon.LatLng =
      await map.convertCoordinate(mapCommon.CoordinateType.WGS84, mapCommon.CoordinateType.GCJ02, wgs84Position);

    return gcj02Position;
  }
}
```
