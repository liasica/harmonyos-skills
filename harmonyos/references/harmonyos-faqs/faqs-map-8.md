---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-8
title: 地图绘制在使用点聚合时并支持设置点信息窗和点注释功能
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > 地图绘制在使用点聚合时并支持设置点信息窗和点注释功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-08-19
content_hash: sha256:d6caa08d814fa1e48cfd4c18ce9effc8dfbdafe38c5fb1cf637de96a49f7f80c
---

## 问题现象

地图绘制时在使用了[点聚合](../harmonyos-guides/map-aggregate.md)功能的基础上，并设置了标记的[自定义信息窗](../harmonyos-guides/map-marker.md#自定义信息窗)和添加了[点注释](../harmonyos-guides/map-annotation.md)。但实际效果中，自定义信息窗无法显示，并且点注释与点聚合效果存在冲突。

## 背景知识

* [addMarker](../harmonyos-references/map-map-mapcomponentcontroller.md#addmarker)方法可以在地图上添加一个标记，并使用[setInfoWindowVisible](../harmonyos-references/map-map-marker.md#setinfowindowvisible)方法设置信息窗是否可见。
* [addClusterOverlay](../harmonyos-references/map-map-mapcomponentcontroller.md#addclusteroverlay)方法支持点聚合能力。
* [addPointAnnotation](../harmonyos-references/map-map-mapcomponentcontroller.md#addpointannotation)方法可在地图上添加一个点注释。

## 解决方案

在使用点聚合能力时，可以使用[on('markerClusterClick')](../harmonyos-references/map-map-clusteroverlay.md)监听聚合图层的标记点击事件。可在该事件中为标记添加自定义信息窗及添加点注释。

1. 在on('markerClusterClick')监听事件中判断当前点击的聚合图层的节点数量，当数量仅为1时，可为该聚合层的标记动态添加自定义信息窗。
2. 点注释的添加与删除也在on('markerClusterClick')监听事件中进行操作。当点击的聚合节点数量为1时，使用[addPointAnnotation](../harmonyos-references/map-map-mapcomponentcontroller.md#addpointannotation)方法为被点击的标记添加点注释。并使用[on('cameraMove')](../harmonyos-references/map-map-mapeventmanager.md#oncameramove)监听相机移动事件，在该事件中进行点注释的删除操作，以防止点注释与点聚合存在冲突。

具体实现可参考下述demo：

```ts
import { map, mapCommon, MapComponent } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';

@Entry
@Component
struct MapPages {
  private mapOptions?: mapCommon.MapOptions;
  private mapController?: map.MapComponentController;
  private callback?: AsyncCallback<map.MapComponentController>;
  pointAnnotation?: map.PointAnnotation;

  aboutToAppear(): void {
    this.mapOptions = {
      position: {
        target: {
          latitude: 31.98,
          longitude: 118.7
        },
        zoom: 7
      }
    };

    this.callback = async (err, mapController) => {
      if (!err) {
        this.mapController = mapController;
        // 生成待聚合点
        let clusterItem1: mapCommon.ClusterItem = {
          position: {
            latitude: 31.98,
            longitude: 118.7
          }
        };
        let clusterItem2: mapCommon.ClusterItem = {
          position: {
            latitude: 32.99,
            longitude: 118.9
          }
        };
        let clusterItem3: mapCommon.ClusterItem = {
          position: {
            latitude: 31.5,
            longitude: 118.7
          }
        };
        let clusterItem4: mapCommon.ClusterItem = {
          position: {
            latitude: 30,
            longitude: 118.7
          }
        };
        let clusterItem5: mapCommon.ClusterItem = {
          position: {
            latitude: 29.98,
            longitude: 117.7
          }
        };
        let clusterItem6: mapCommon.ClusterItem = {
          position: {
            latitude: 31.98,
            longitude: 120.7
          }
        };
        let clusterItem7: mapCommon.ClusterItem = {
          position: {
            latitude: 25.98,
            longitude: 119.7
          }
        };
        let clusterItem8: mapCommon.ClusterItem = {
          position: {
            latitude: 30.98,
            longitude: 110.7
          }
        };
        let clusterItem9: mapCommon.ClusterItem = {
          position: {
            latitude: 30.98,
            longitude: 115.7
          }
        };
        let clusterItem10: mapCommon.ClusterItem = {
          position: {
            latitude: 28.98,
            longitude: 122.7
          }
        };
        let array: Array<mapCommon.ClusterItem> = [
          clusterItem1,
          clusterItem2,
          clusterItem3,
          clusterItem4,
          clusterItem5,
          clusterItem6,
          clusterItem7,
          clusterItem8,
          clusterItem9,
          clusterItem10
        ];

        // 生成聚合图层的入参，聚合distance设置为100vp
        let clusterOverlayParams: mapCommon.ClusterOverlayParams = { distance: 100, clusterItems: array };
        // 调用addClusterOverlay生成聚合图层
        let clusterOverlay: map.ClusterOverlay = await this.mapController.addClusterOverlay(clusterOverlayParams);

        // 监听聚合图层的标记点击事件
        let callback1 = async (markerClusterInfo: map.MarkerClusterInfo) => {
          this.pointAnnotation?.remove();
          console.info('markerClusterClick', `callback1 markerClusterInfo:` + markerClusterInfo.clusterItems.length);
          if (markerClusterInfo.clusterItems.length > 1) {
            // 缩放地图展开聚合
            this.mapController?.animateCamera(map.newLatLng(markerClusterInfo.clusterItems[0].position), 1000);
            this.mapController?.animateCamera(map.zoomIn(), 1000);
          } else {
            // 当聚合节点数组为1时显示信息窗
            markerClusterInfo.marker.setClickable(true);
            markerClusterInfo.marker.setTitle('信息窗');
            markerClusterInfo.marker.setInfoWindowVisible(true);

            // 点注释
            let pointAnnotationOptions: mapCommon.PointAnnotationParams = {
              // 定义点注释图标锚点
              position: {
                latitude: markerClusterInfo.marker.getPosition().latitude,
                longitude: markerClusterInfo.marker.getPosition().longitude
              },
              // 点注释显示的位置
              textPosition: mapCommon.TextPosition.BOTTOM,
              // 定义点注释名称与地图POI名称相同时，是否支持去重
              repeatable: true,
              // 定义点注释的碰撞规则
              collisionRule: mapCommon.CollisionRule.NAME,
              // 定义点注释的标题，数组长度最小为1，最大为3
              titles: [{
                // 定义标题内容
                content: '标点注释',
                // 定义标题字体颜色
                color: 0xFF000000,
                // 定义标题字体大小
                fontSize: 15,
              }
              ],
              // 定义点注释的锚点在水平方向上的位置
              anchorU: 0.5,
              // 定义点注释的锚点在垂直方向上的位置
              anchorV: 1,
              // 定义点注释的显示属性，为true时，在被碰撞后仍能显示
              forceVisible: false,
              // 定义碰撞优先级，数值越大，优先级越低
              priority: Number.MAX_VALUE,
              // 定义点注释展示的最小层级
              minZoom: 5,
              // 定义点注释展示的最大层级
              maxZoom: 20,
              // 定义点注释是否可见
              visible: true,
              // 定义点注释叠加层级属性
              zIndex: 10
            };

            this.pointAnnotation = await this.mapController?.addPointAnnotation(pointAnnotationOptions);

          }
        };
        // 添加监听
        clusterOverlay.on('markerClusterClick', callback1);

        // 监听移动事件，当移动时删除点注释
        this.mapController.on('cameraMove', () => {
          this.pointAnnotation?.remove();
          console.info('cameraMove', `on-cameraMove`);
        });
      }
    };
  }

  build() {
    Stack() {
      Column() {
        MapComponent({
          mapOptions: this.mapOptions,
          mapCallback: this.callback,
          // 自定义信息窗，点击标记后可展示信息窗
          customInfoWindow: this.customInfoWindow
        })
          .width('100%')
          .height('100%');
      }.width('100%');
    }.height('100%');
  }

  // 自定义信息窗BuilderParam
  @BuilderParam customInfoWindow: ($$: map.MarkerDelegate) => void = this.customInfoWindowBuilder;

  // 自定义信息窗Builder
  @Builder
  customInfoWindowBuilder($$: map.MarkerDelegate) {
    if ($$.marker) {
      Text($$.marker.getTitle())
        .width('50%')
        .height(50)
        .backgroundColor(Color.White)
        .textAlign(TextAlign.Center)
        .fontColor(Color.Black)
        .font({ size: 25, weight: 10, style: FontStyle.Italic });
    }
  }
}
```
