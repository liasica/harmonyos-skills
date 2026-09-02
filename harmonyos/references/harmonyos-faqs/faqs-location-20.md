---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-location-20
title: 地图添加标记返回undefined如何解决
breadcrumb: FAQ > 应用服务开发 > 位置服务（Location Kit） > 地图添加标记返回undefined如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:50+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:05d48d569bdb7e532e32c497eea05a14c60ef0cd024e89a232345773950cae87
---

## 问题现象

在地图的指定位置添加标记，但地图没有显示标记，添加标记返回undefined，如何解决？

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/zWVZ4Dh4QqO4xTXg2EsM8Q/zh-cn_image_0000002658913755.png "点击放大")

问题代码示例如下：

```screen
@Entry
@Component
struct MarkerPage {

  aboutToAppear(): void {
    this.mapOptions = {
      position: {
        target: {
          latitude: 31.984410259206815,
          longitude: 118.76625379397866
        },
        zoom: 10
      },
      myLocationControlsEnabled: true
    };

    this.callback = async (err, mapController) => {
      if (!err) {
        this.mapController = mapController;
        this.mapEventManager = this.mapController.getEventManager();
        mapController.setMyLocationEnabled(true);
        mapController.setMyLocationControlsEnabled(true)
        let callback = () => {
        }
        this.mapEventManager.on("mapLoad", callback);
      }
    };
  }

  build() {
    NavDestination() {
      Stack() {
        MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
      }
    }
    .onReady(async (context) => {
      if (context) {
        this.pathStack = context.pathStack
        let position: mapCommon.LatLng = {
          latitude: 31.984410259206815,
          longitude: 118.76625379397866
        };
        let markerOptions: mapCommon.MarkerOptions = {
          position: position
        };
        this.marker = await this.mapController?.addMarker(markerOptions)
      }
    })
  }
}
```

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/Xy6Gs4UjRpijQinzukq1Xg/zh-cn_image_0000002658793809.png "点击放大")

## 背景知识

点标记用来在地图上标记任何位置，例如用户位置、车辆位置、店铺位置等一切带有位置属性的事物，具体实现可参考：[开发步骤](../harmonyos-guides/map-marker.md#开发步骤)。

## 问题定位

1. 从代码中看出，添加marker的代码是在NavDestination组件的onReady()方法中实现。
2. NavDestination组件即将构建完时会触发onReady()方法，而这时并不能保证Mapkit的callback回调方法已经执行完了，如果执行onReady()方法之前，Mapkit的callback回调方法还没有被触发，那么在onReady()方法中调用mapController对象就会是undefined。

## 分析结论

在调用this.mapController对象之前要保证callback回调方法已经执行完成，另外callback回调方法是地图组件MapComponent加载完成之后才会触发。

## 修改建议

将this.marker = await this.mapController?.addMarker(markerOptions)相关的代码挪到Mapkit的callback方法里执行，代码示例如下：

```ts
import { MapComponent, mapCommon, map } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';

@Entry
@Component
struct MarkerPage {
  private mapOptions?: mapCommon.MapOptions;
  private callback?: AsyncCallback<map.MapComponentController>;
  private mapController?: map.MapComponentController;
  private mapEventManager?: map.MapEventManager;
  pathStack: NavPathStack = new NavPathStack();

  aboutToAppear(): void {
    this.mapOptions = {
      position: {
        target: {
          latitude: 31.984410259206815,
          longitude: 118.76625379397866
        },
        zoom: 10
      },
      myLocationControlsEnabled: true
    };
    // 地图初始化的回调
    this.callback = async (err, mapController) => {
      if (!err) {
        // 获取地图的控制器类，用来操作地图
        this.mapController = mapController;
        this.mapEventManager = this.mapController.getEventManager();
        mapController.setMyLocationEnabled(true);
        mapController.setMyLocationControlsEnabled(true);
        let callback = () => {
        };
        this.mapEventManager.on('mapLoad', callback);

        let position: mapCommon.LatLng = {
          latitude: 31.984410259206815,
          longitude: 118.76625379397866
        };
        let markerOptions: mapCommon.MarkerOptions = {
          position: position
        };
        try {
          await this.mapController?.addMarker(markerOptions);
        } catch (error) {
          console.error('addMarker error');
        }
      }
    };
  }

  build() {
    NavDestination() {
      Stack() {
        // 调用MapComponent组件初始化地图
        MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
          .width('100%')
          .height('75%');
      }
      .height('100%');
    }
    .hideTitleBar(true)
    .onReady(async (context) => {
      if (context) {
        this.pathStack = context.pathStack;
      }
    })
    .onShown(() => {
      if (this.mapController) {
        this.mapController.show();
      }
    })
    .onHidden(() => {
      if (this.mapController) {
        this.mapController.hide();
      }
    });
  }
}
```
