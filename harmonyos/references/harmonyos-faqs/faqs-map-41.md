---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-41
title: 点击添加的marker位置与点击的位置不一致
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > 点击添加的marker位置与点击的位置不一致
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:49e7a64254372c2edc9b3c2110d93ddf56e220a8f97b34f1e2b04dd85709e05c
---

## 问题现象

在地图上通过手指点击添加marker，添加的marker的位置与手指点击的位置不一致，总是显示在左上角。

原问题代码如下：

```ts
import { map, mapCommon, MapComponent } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';

@Entry
@Component
struct IncorrectCode {
  private mapOptions?: mapCommon.MapOptions;
  private mapController?: map.MapComponentController;
  private callback?: AsyncCallback<map.MapComponentController>;
  @State screenX: number = 0;
  @State screenY: number = 0;
  @State latitudeA: number = 0;
  @State longitudeA: number = 0;
  @State latitudeB: number = 0;
  @State longitudeB: number = 0;

  aboutToAppear(): void {
    // 地图初始化参数
    this.mapOptions = {
      position: {
        target: {
          latitude: 31.984410259206815,
          longitude: 118.76625379397866
        },
        zoom: 15
      },
    };
    this.callback = async (err, mapController) => {
      if (!err) {
        this.mapController = mapController;
      } else {
        console.error(`地图初始化失败, code is：${err.code}, message is ${err.message}`);
      }
    };
  }

  build() {
    Stack() {
      Column() {
        MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
          .onTouch((event: TouchEvent) => {
            if (event.type === TouchType.Up) {
              this.screenX = event.touches[0].x;
              this.screenY = event.touches[0].y;

              const projection = this.mapController?.getProjection();
              const screenPoint: mapCommon.MapPoint = {
                positionX: this.screenX,
                positionY: this.screenY
              };
              const latLng = projection?.fromScreenLocation(screenPoint);
              this.latitudeA = latLng?.latitude as number;
              this.longitudeA = latLng?.longitude as number;

              let wgs84Position: mapCommon.LatLng = {
                latitude: this.latitudeA,
                longitude: this.longitudeA
              };

              // 转换经纬度坐标
              let gcj02Position: mapCommon.LatLng =
                map.convertCoordinateSync(mapCommon.CoordinateType.WGS84, mapCommon.CoordinateType.GCJ02,
                  wgs84Position);
              this.latitudeB = gcj02Position.latitude;
              this.longitudeB = gcj02Position.longitude;

              // 添加一个红色标记点
              const markerOptions: mapCommon.MarkerOptions = {
                position: {
                  latitude: this.latitudeB,
                  longitude: this.longitudeB
                },
              };
              this.mapController?.addMarker(markerOptions);
            }
            return true;
          })
      }.width('100%')
    }.height('100%')
  }
}
```

## 背景知识

* [fromScreenLocation](../harmonyos-references/map-map-projection.md#fromscreenlocation)：将屏幕像素点坐标转换成经纬度。添加的像素点坐标，单位为px。
* 开通地图服务：需先[开通地图服务](../harmonyos-guides/map-config-agc.md#开通地图服务)，再进行后续地图开发活动。

## 问题定位

1. 问题代码中，获取点击位置的像素点坐标后，直接将像素点坐标值用于转换经纬度。此时获取的像素点的坐标单位是vp，而将屏幕像素点坐标转换成经纬度fromScreenLocation接口需要传入px单位，导致像素点坐标输入值与实际点击位置有差异。

   ```ts
   this.screenX = event.touches[0].x;
   this.screenY = event.touches[0].y;

   const projection = this.mapController?.getProjection();
   const screenPoint: mapCommon.MapPoint = {
     positionX: this.screenX,
     positionY: this.screenY
   };
   ```
2. 问题代码中，对屏幕像素点坐标转换后的经纬度，又进行了一次WGS84坐标系转换GCJ02坐标系，屏幕像素点坐标转换后的经纬度本身应就GCJ02坐标系，无需再转换。

   ```ts
   let wgs84Position: mapCommon.LatLng = {
     latitude: this.latitudeA,
     longitude: this.longitudeA
   };

   // 转换经纬度坐标
   let gcj02Position: mapCommon.LatLng =
     map.convertCoordinateSync(mapCommon.CoordinateType.WGS84, mapCommon.CoordinateType.GCJ02,
       wgs84Position);
   this.latitudeB = gcj02Position.latitude;
   this.longitudeB = gcj02Position.longitude;
   ```

## 分析结论

问题代码存在两处错误导致添加marker不准确。

1. onTouch获取的像素点坐标单位是vp，fromScreenLocation转化为经纬度坐标时，需要输入的单位是px，没有进行像素点坐标单位转换。
2. 屏幕像素点坐标转换后的经纬度本身应是GCJ02坐标系，问题代码中额外进行了一次WGS84坐标系转换GCJ02坐标系。

## 修改建议

1. onTouch获取的像素点坐标进行vp转px单位转换。

   ```ts
   const screenPoint: mapCommon.MapPoint = {
     positionX: this.getUIContext().vp2px(this.screenX),
     positionY: this.getUIContext().vp2px(this.screenY)
   };
   ```
2. 去掉WGS84坐标系转换GCJ02坐标系的操作。

修改后的完整代码：

```ts
import { map, mapCommon, MapComponent } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';

@Entry
@Component
struct IncorrectCode {
  private mapOptions?: mapCommon.MapOptions;
  private mapController?: map.MapComponentController;
  private callback?: AsyncCallback<map.MapComponentController>;
  @State screenX: number = 0;
  @State screenY: number = 0;
  @State latitudeA: number = 0;
  @State longitudeA: number = 0;

  aboutToAppear(): void {
    // 地图初始化参数
    this.mapOptions = {
      position: {
        target: {
          latitude: 31.984410259206815,
          longitude: 118.76625379397866
        },
        zoom: 15
      },
    };
    this.callback = async (err, mapController) => {
      if (!err) {
        this.mapController = mapController;
      } else {
        console.error(`地图初始化失败, code is：${err.code}, message is ${err.message}`);
      }
    };
  }

  build() {
    Stack() {
      Column() {
        MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
          .onTouch((event: TouchEvent) => {
            if (event.type === TouchType.Up) {
              this.screenX = event.touches[0].x;
              this.screenY = event.touches[0].y;

              const projection = this.mapController?.getProjection();
              const screenPoint: mapCommon.MapPoint = {
                positionX: this.getUIContext().vp2px(this.screenX),
                positionY: this.getUIContext().vp2px(this.screenY)
              };
              const latLng = projection?.fromScreenLocation(screenPoint);
              this.latitudeA = latLng?.latitude as number;
              this.longitudeA = latLng?.longitude as number;

              // 添加一个红色标记点
              const markerOptions: mapCommon.MarkerOptions = {
                position: {
                  latitude: this.latitudeA,
                  longitude: this.longitudeA
                },
              };
              this.mapController?.addMarker(markerOptions);
            }
            return true;
          })
      }.width('100%')
    }.height('100%')
  }
}
```
