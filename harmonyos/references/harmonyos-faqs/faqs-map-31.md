---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-31
title: 基于指定的经纬度坐标点，如何进行地图缩放
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > 基于指定的经纬度坐标点，如何进行地图缩放
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:8bd891f9d83c501a66f12a6bc7eb88ef3e66f6cfe310f5a3cc8c0d11f528a564
---

## 问题现象

在不移动地图相机中心点的情况下，基于指定的经纬度坐标点，如何进行地图缩放（改变zoom级别）？

## 背景知识

* 开发准备：使用地图服务，需要先[开通地图服务](../harmonyos-guides/map-config-agc.md#开通地图服务)。
* [zoomBy](../harmonyos-references/map-map-functions.md#zoomby)：根据给定增量并以给定的屏幕像素点为中心点缩放地图级别。
* [toScreenLocation](../harmonyos-references/map-map-projection.md#toscreenlocation)：将经纬度转换为对应的屏幕上的点的坐标。屏幕上的点的坐标是以相对于地图左上角（而不是整个屏幕的左上角）的屏幕像素（而非显示像素）指定的。

## 解决方案

方案逻辑：通过toScreenLocation将指定的经纬度坐标点转换为屏幕上的点的坐标，将此坐标点作为zoomBy的缩放中心点，进行指定级别的地图缩放。

完整代码：

```ts
import { map, mapCommon, MapComponent } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';
import { display } from '@kit.ArkUI';

@Entry
@Component
struct CustomScale {
  private mapOptions?: mapCommon.MapOptions;
  private mapController?: map.MapComponentController;
  private callback?: AsyncCallback<map.MapComponentController>;
  private screenX: number = 0;
  private screenY: number = 0;
  private latitudeA: number = 0;
  private longitudeA: number = 0;
  private markerNumber: number = 0;
  @State mapHeight: number = 0;

  aboutToAppear(): void {
    let displayClass = display.getDefaultDisplaySync();
    this.mapHeight = this.getUIContext().px2vp(displayClass.height);
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
    Stack({ alignContent: Alignment.Bottom }) {
      Column() {
        MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
          .height(this.mapHeight)
          .onTouch((event: TouchEvent) => {
            if (this.markerNumber === 0) {
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
                this.markerNumber += 1;
              }
            }
            return true;
          });
      }.width('100%');

      Column() {
        Button('放大地图')
          .margin({ bottom: 12 })
          .onClick(() => {
            let projection: map.Projection | undefined = this.mapController?.getProjection();
            let position: mapCommon.MapPoint | undefined =
              projection?.toScreenLocation({ latitude: this.latitudeA, longitude: this.longitudeA });
            let focus: mapCommon.MapPoint | undefined = position;
            let cameraUpdate: map.CameraUpdate = map.zoomBy(1, focus);
            this.mapController?.animateCamera(cameraUpdate);
          });
        Button('缩小地图')
          .margin({ bottom: 12 })
          .onClick(() => {
            let projection: map.Projection | undefined = this.mapController?.getProjection();
            let position: mapCommon.MapPoint | undefined =
              projection?.toScreenLocation({ latitude: this.latitudeA, longitude: this.longitudeA });
            let focus: mapCommon.MapPoint | undefined = position;
            let cameraUpdate: map.CameraUpdate = map.zoomBy(-1, focus);
            this.mapController?.animateCamera(cameraUpdate);
          });
        Button('删除Marker')
          .onClick(() => {
            this.mapController?.clear();
            this.markerNumber -= 1;
          });
      };
    }
    .ignoreLayoutSafeArea();
  }
}
```

实现效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/h1aYfZxUQ-2nO9EULRN3aA/zh-cn_image_0000002628394370.png "点击放大")

## 常见FAQ

Q：如何实时获取当前地图的缩放级别（zoom）？

A：Map Kit并没有直接提供获取当前地图的缩放级别的接口，可以通过获取相机的当前状态信息得到zoom的值。更准确地说，zoom实质上就是相机状态的缩放级别，即为屏幕中心附近的缩放级别。

可通过[getCameraPosition](../harmonyos-references/map-map-mapcomponentcontroller.md#getcameraposition)获取相机的当前状态信息，再从[CameraPosition](../harmonyos-references/map-common.md#cameraposition)获取缩放级别（zoom）。
