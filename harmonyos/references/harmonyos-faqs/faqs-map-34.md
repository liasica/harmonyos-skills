---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-34
title: 如何实现地图自动缩放并移动到中心点
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > 如何实现地图自动缩放并移动到中心点
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:13f82ab74ff3fcc382ff897ef4031aea3c6827234c8a8d733ccef8cd08a442a7
---

## 问题现象

怎么实现自动调整缩放和移动到中心点，将所有的Marker全部显示在屏幕上？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/MxQjis7bQwefsARFFVoSTg/zh-cn_image_0000002628394374.png "点击放大")

## 背景知识

* Map Kit（地图服务）为开发者提供强大而便捷的地图能力，开发前需开通地图服务，参考：[开通地图服务](../harmonyos-guides/map-config-agc.md#开通地图服务)。
* LatLngBoundsUtils类的[include](../harmonyos-references/map-map-latlngboundsutils.md#include)：获取一个包含指定位置的LatLngBounds对象。
* [moveCamera](../harmonyos-references/map-map-mapcomponentcontroller.md#movecamera)：更新相机状态。

## 解决方案

1. 使用LatLngBoundsUtils类的include接口获取一个包含所有标记点的LatLngBounds对象。

   ```ts
   getLatLngBounds(): mapCommon.LatLngBounds | undefined {
     let latLngs: Array<mapCommon.LatLng> = [{
       latitude: 12,
       longitude: 110
     }, {
       latitude: 31.18,
       longitude: 121.43
     }, {
       latitude: 8,
       longitude: 90
     }];
     let resultBounds: mapCommon.LatLngBounds | undefined;
     for (let index = 0; index < latLngs.length; index++) {
       let markerOptions: mapCommon.MarkerOptions = {
         position: {
           latitude: latLngs[index].latitude,
           longitude: latLngs[index].longitude
         },
         rotation: 0,
         visible: true,
         zIndex: 0,
         alpha: 0.9,
         anchorU: 0.5,
         anchorV: 1,
         clickable: true,
         draggable: true,
         flat: false
       };

       this.mapController?.addMarker(markerOptions).catch(() => {
         console.error('addMarker error');
       });
       resultBounds = map.LatLngBoundsUtils.include(latLngs[index], resultBounds);
     }
     return resultBounds;
   }
   ```
2. 通过移动地图相机的方式设置地图显示区域。

   ```ts
   aboutToAppear(): void {
     try {
     let displayClass = display.getDefaultDisplaySync();
     this.mapHeight = this.getUIContext().px2vp(displayClass.height);
   } catch (error) {
     console.error(`getDefaultDisplaySync error. Code is ${error.code}, message is ${error.message}.`);
   }

   this.mapOptions = {
     position: {
       target: {
         longitude: 121.47, latitude: 31.23
       },
       zoom: 11
     }
   };

   // 地图初始化的回调
   this.callback = async (err, mapController) => {
     if (!err) {
       this.mapController = mapController;
     }
   };
   }

   build() {
     Stack({ alignContent: Alignment.Bottom }) {
       Column() {
         MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
           .height(this.mapHeight)
           .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
       }
       .width('100%');

       Button('LatLngBounds')
         .onClick(() => {
           if (this.getLatLngBounds()) {
             let cameraUpdate: map.CameraUpdate = map.newLatLngBounds(this.getLatLngBounds(), 100);
             // 移动相机
             this.mapController?.moveCamera(cameraUpdate);
           }
         })
         .margin({ bottom: -40 });
     }
     .height('100%')
     .ignoreLayoutSafeArea();
   }
   ```

完整示例代码如下：

```ts
import { MapComponent, mapCommon, map } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';
import { display } from '@kit.ArkUI';

@Entry
@Component
struct MarkerPage {
  private mapOptions?: mapCommon.MapOptions;
  private mapController?: map.MapComponentController;
  private callback?: AsyncCallback<map.MapComponentController>;
  @State mapHeight: number = 0;

  getLatLngBounds(): mapCommon.LatLngBounds | undefined {
    let latLngs: Array<mapCommon.LatLng> = [{
      latitude: 12,
      longitude: 110
    }, {
      latitude: 31.18,
      longitude: 121.43
    }, {
      latitude: 8,
      longitude: 90
    }];
    let resultBounds: mapCommon.LatLngBounds | undefined;
    for (let index = 0; index < latLngs.length; index++) {
      let markerOptions: mapCommon.MarkerOptions = {
        position: {
          latitude: latLngs[index].latitude,
          longitude: latLngs[index].longitude
        },
        rotation: 0,
        visible: true,
        zIndex: 0,
        alpha: 0.9,
        anchorU: 0.5,
        anchorV: 1,
        clickable: true,
        draggable: true,
        flat: false
      };

      this.mapController?.addMarker(markerOptions).catch(() => {
        console.error('addMarker error');
      });
      resultBounds = map.LatLngBoundsUtils.include(latLngs[index], resultBounds);
    }
    return resultBounds;
  }

  aboutToAppear(): void {
    try {
      let displayClass = display.getDefaultDisplaySync();
      this.mapHeight = this.getUIContext().px2vp(displayClass.height);
    } catch (error) {
      console.error(`getDefaultDisplaySync error. Code is ${error.code}, message is ${error.message}.`);
    }

    this.mapOptions = {
      position: {
        target: {
          longitude: 121.47, latitude: 31.23
        },
        zoom: 11
      }
    };

    // 地图初始化的回调
    this.callback = async (err, mapController) => {
      if (!err) {
        this.mapController = mapController;
      }
    };
  }

  build() {
    Stack({ alignContent: Alignment.Bottom }) {
      Column() {
        MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
          .height(this.mapHeight)
          .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
      }
      .width('100%');

      Button('LatLngBounds')
        .onClick(() => {
          if (this.getLatLngBounds()) {
            let cameraUpdate: map.CameraUpdate = map.newLatLngBounds(this.getLatLngBounds(), 100);
            // 移动相机
            this.mapController?.moveCamera(cameraUpdate);
          }
        })
        .margin({ bottom: -40 });
    }
    .height('100%')
    .ignoreLayoutSafeArea();
  }
}
```
