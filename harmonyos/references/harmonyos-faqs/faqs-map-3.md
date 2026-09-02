---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-3
title: 地图标记点在缩放地图时发生位置偏移
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > 地图标记点在缩放地图时发生位置偏移
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:92ceca1d0da1400fa38bf6c95331377804058deb022a39d272059c23f7477e47
---

## 问题现象

地图某个位置上的标记点，在缩放地图的时候，标记位置会发生变化，偏移原来的位置。

## 背景知识

* [开通地图服务](../harmonyos-guides/map-config-agc.md#开通地图服务)：需先开通地图服务后，参考“应用开发准备”完成基本准备工作。

* [标记](../harmonyos-guides/map-marker.md)：MapKit地图上使用Marker向指定位置添加标记以标识位置。
* [MarkerOptions](../harmonyos-references/map-common.md#markeroptions)：添加Marker的参数，其中，锚点中心通过以下参数指定：

  | 参数 | 类型 | 说明 |
  | --- | --- | --- |
  | anchorU | number | 锚点的水平坐标，以图像宽度的比例，建议取值[0, 1]，默认值为0.5，异常值按默认值处理。 |
  | anchorV | number | 锚点的垂直坐标，以图像高度的比例，建议取值[0, 1]，默认值为1，异常值按默认值处理。 |

## 问题定位

1. 通过问题现象观察，标记点在地图缩放时，随着缩放比例发生了一定的漂移，但是依然在标记位置附近，尤其在地图放大的时候，标记的位置是准确的。
2. 结合地图标记的参数，锚点的垂直坐标默认为1，即以图片最低点为锚点中心，那么图片的中心点，在地图缩放的时候就会发生变化。
3. 查看代码，MarkerOptions设置的锚点参数，未配置锚点的垂直坐标，此时使用默认值：

   ```ts
   let markerOptions: mapCommon.MarkerOptions = {
     position: {
   	latitude: 39.9,
   	longitude: 116.4
     },
     icon: $r('app.media.icon'),
   };
   this.mapController?.addMarker(markerOptions);
   ```

## 分析结论

默认的标记参数，anchorV的值为1，以图片下边沿中心作为锚点中心，在缩放地图时，标记图片大小不变的情况下，图片中心点在地图上的位置就会发生变化，图片越大（原问题中图片圆点周围留白越多），现象越明显。需要将标记锚点的中心设置成图片的中心，即可解决问题。

## 修改建议

参考代码，将标记参数中的anchorV参数修改为0.5，以图片中心点作为锚点中心。

```ts
import { MapComponent, mapCommon, map } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';

@Entry
@Component
struct MapPage {
  private TAG = "HuaweiMapDemo";
  private mapOptions?: mapCommon.MapOptions;
  private callback?: AsyncCallback<map.MapComponentController>;
  private mapController?: map.MapComponentController;
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
        let callback = () => {
          console.info(this.TAG, `on-mapLoad`);
        };
        this.mapEventManager.on("mapLoad", callback);
        let markerOptions: mapCommon.MarkerOptions = {
          position: {
            latitude: 39.9,
            longitude: 116.4
          },
          icon: $r('app.media.icon'),
          anchorU: 0.5,
          anchorV: 0.5
        };
        this.mapController?.addMarker(markerOptions);
      }
    };
  }

  build() {
    Stack() {
      // 调用MapComponent组件初始化地图
      MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback }).width('100%').height('100%')
    }.height('100%')
  }
}
```
