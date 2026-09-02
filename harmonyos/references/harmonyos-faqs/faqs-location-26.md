---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-location-26
title: 如何解决经纬度坐标在地图上显示与实际地点有偏差问题
breadcrumb: FAQ > 应用服务开发 > 位置服务（Location Kit） > 如何解决经纬度坐标在地图上显示与实际地点有偏差问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:50+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:b61ba22420fbdb43021d62c458b11dfaa7610039912bbf9ee7891759660a2d91
---

## 问题现象

开发者通过Location Kit位置服务获取位置坐标后，在Map Kit地图上将坐标通过[addMarker](../harmonyos-references/map-map-mapcomponentcontroller.md#addmarker)添加标记，发现Marker标记显示位置与实际位置相差500米左右。

## 背景知识

* Map Kit地图服务涉及2种坐标系：
  + GCJ02：由中国国家测绘局制订，是对WGS84坐标系进行加密后的坐标系，也称为火星坐标系，广泛应用于中国各种地图和位置服务应用，Map Kit在中国大陆的使用的是GCJ02坐标系。
  + WGS84：这是一种全球定位系统（GPS）使用的坐标系，基于地球的椭球模型定义，广泛应用于全球地图和定位服务。
* [Location Kit](../harmonyos-guides/location-kit-intro.md)提供的默认坐标系是WGS84坐标系。
* [地图开发准备](../harmonyos-guides/map-config-agc.md)：请优先[开通地图服务](../harmonyos-guides/map-config-agc.md#开通地图服务)后，再参考[应用开发准备](../harmonyos-guides/application-dev-overview.md)完成基本准备工作。
* [申请位置权限开发](../harmonyos-guides/location-permission-guidelines.md)：应用在使用Location Kit系统能力前，需要检查是否已经获取用户授权访问设备位置信息。如未获得授权，可以向用户申请需要的位置权限。

## 问题定位

1. 检查代码中是否使用Location Kit获取位置后，直接使用位置坐标在Map Kit地图上进行了标记绘制，未进行[坐标纠偏](../harmonyos-guides/map-convert-coordinate.md)。
2. 将获取的坐标通过[setMyLocation](../harmonyos-references/map-map-mapcomponentcontroller.md#setmylocation)接口在地图上显示“我的位置”，如果“我的位置”与真实位置一致，说明坐标是WGS84坐标系。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/Aprw5LszR-2vQndWU_sl2g/zh-cn_image_0000002628394540.png "点击放大")

## 分析结论

Location Kit提供的默认坐标是WGS84坐标系，开发者使用的[getCurrentLocation](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetcurrentlocation)获取的经纬度是WGS84坐标系，Map Kit的setMyLocation接口使用的是WGS84坐标系，所以显示位置是正确的。但Map Kit的addMarker等在地图上绘制元素的接口，在中国大陆的使用的是GCJ02坐标系，所以需要将WGS84坐标系转为GCJ02坐标系，再进行绘制，否则显示的位置会产生偏差。

## 修改建议

使用[convertCoordinateSync](../harmonyos-references/map-map-functions.md#convertcoordinatesync)函数将WGS84坐标系转为GCJ02坐标系，再使用转换后的坐标设置Marker位置，关键代码如下：

```ts
import { map, mapCommon, MapComponent } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';
import { geoLocationManager } from '@kit.LocationKit';

@Entry
@Component
struct HwMapLocationPage {
  private mapOption?: mapCommon.MapOptions;
  private mapController?: map.MapComponentController;
  private callback?: AsyncCallback<map.MapComponentController>;
  myWGS84Position: mapCommon.LatLng = {
    latitude: 31.25498003568704,
    longitude: 121.45347333871776,
  };
  // 我的位置信息
  myLocation: geoLocationManager.Location = {
    "latitude": 31.25498003568704,
    "longitude": 121.45347333871776,
    "altitude": 0,
    "accuracy": 0,
    "speed": 0,
    "timeStamp": 0,
    "direction": 0,
    "timeSinceBoot": 0,
    altitudeAccuracy: 0,
    speedAccuracy: 0,
    directionAccuracy: 0,
    uncertaintyOfTimeSinceBoot: 0,
    sourceType: geoLocationManager.LocationSourceType.GNSS
  };

  aboutToAppear(): void {
    this.mapOption = {
      position: {
        target: this.myWGS84Position,
        zoom: 11,
      },
      dayNightMode: mapCommon.DayNightMode.AUTO
    };

    // 地图初始化的回调
    this.callback = async (err, mapController) => {
      if (!err) {
        this.mapController = mapController;
        this.mapController.setMyLocationEnabled(true);
        this.mapController.setMyLocationControlsEnabled(false);
        this.mapController?.setMyLocation(this.myLocation);
      };
    };
  };

  build() {
    RelativeContainer() {
      MapComponent({ mapOptions: this.mapOption, mapCallback: this.callback })
        .width('100%')
        .height('100%');

      Button('单个Marker')
        .alignRules({
          top: { anchor: "id_image", align: VerticalAlign.Bottom }
        })
        .onClick(async () => {
          let wgs84Position: mapCommon.LatLng = this.myWGS84Position;
          // 转换经纬度坐标
          let gcj02Position: mapCommon.LatLng =
            map.convertCoordinateSync(mapCommon.CoordinateType.WGS84, mapCommon.CoordinateType.GCJ02, wgs84Position);

          let markerOptions: mapCommon.MarkerOptions = {
            position: {
              latitude: gcj02Position.latitude,
              longitude: gcj02Position.longitude
            },
            rotation: 0,
            visible: true,
            zIndex: 0,
            alpha: 0.9,
            anchorU: 0.5,
            anchorV: 1,
            clickable: true,
            draggable: true,
            flat: false,
          };
          await this.mapController?.addMarker(markerOptions);
        });
    }
    .height('100%')
    .width('100%')
  }
}
```

## 常见FAQ

Q：除了上述convertCoordinate方法可以转换坐标，还有什么方式可以把WGS84坐标系转为GCJ02坐标系？

A：使用[rectifyCoordinate](../harmonyos-references/map-map-functions.md#rectifycoordinate)接口可以解决原始坐标与华为地图展示偏转的问题，且仅支持WGS84坐标系转为GCJ02坐标系。

Q：convertCoordinateSync和rectifyCoordinate两种坐标纠偏接口有什么差异？

A：[convertCoordinateSync](../harmonyos-references/map-map-functions.md#convertcoordinatesync)接口仅固定的将输入坐标数据进行WGS84坐标系转GCJ02坐标系。[rectifyCoordinate](../harmonyos-references/map-map-functions.md#rectifycoordinate)接口会判断输入坐标数据信息，自动决定是否进行坐标系转换纠偏，如应用涉及海外使用地图场景，建议使用该接口。
