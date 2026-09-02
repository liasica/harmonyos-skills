---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-6
title: 路径规划场景中绘制颜色渐变的路径，颜色不生效问题如何解决
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > 路径规划场景中绘制颜色渐变的路径，颜色不生效问题如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:590e21dab99c03fbf6090a0ffa16ebe6cf0eb872d8bb542f8b702aa147dd5066
---

## 问题现象

地图两点之间需要绘制一条颜色渐变的多点折线，设置MapPolylineOptions.colors数组，渐变样式不生效。

## 背景知识

* 初始化地图：新建地图初始化参数mapOptions，设置地图中心点坐标及层级。通过callback回调的方式获取[MapComponentController](../harmonyos-references/map-map-mapcomponentcontroller.md)对象，用来操作地图。调用[MapComponent](../harmonyos-references/map-mapcomponent.md)组件，传入mapOptions和callback参数，初始化地图。详见[显示地图](../harmonyos-guides/map-presenting.md)。
* 绘制折线：新建折线时在[MapPolylineOptions](../harmonyos-references/map-common.md#mappolylineoptions)的colors属性中设置折线分段颜色值，详见[折线](../harmonyos-guides/map-polyline.md)。

## 问题定位

绘制颜色渐变的折线，首先要绘制折线，并设置折线的颜色渐变。这里颜色渐变不生效，可能是MapPolylineOptions.gradient或MapPolylineOptions.colors设置不正确。

## 分析结论

MapPolylineOptions.gradient要设置为true，开启过渡色。MapPolylineOptions.colors数组长度要等于折线点数量，以确保每段折线都有过渡色。数组长度小于折线点数量会导致后半段折线缺少过渡色而显示默认颜色。

## 修改建议

MapPolylineOptions.colors过渡段颜色数组，会按照折线点顺序依次取色。MapPolylineOptions.gradient设置为true，两个折线点之间颜色会呈现过渡色。

```ts
import { map, mapCommon, MapComponent } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';

// 地图折线点的坐标数组
const markers: Array<mapCommon.LatLng> =
  [{ longitude: 121.47, latitude: 31.23 }, { longitude: 121.43, latitude: 31.18 },
    { longitude: 121.46, latitude: 31.13 }, { longitude: 121.43, latitude: 31.05 },
    { longitude: 121.34, latitude: 31.02 }];

@Entry
@Component
struct HwMapDrawPage {
  private mapOption?: mapCommon.MapOptions; // 地图参数
  private mapController?: map.MapComponentController; // 地图组件控制器
  private callback?: AsyncCallback<map.MapComponentController>; // 地图初始化回调

  aboutToAppear(): void {
    this.mapOption = {
      position: {
        target: {
          longitude: 121.47, latitude: 31.23 // 地图中心坐标
        },
        zoom: 11, // 屏幕中心的缩放级别
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
    Column() {
      MapComponent({ mapOptions: this.mapOption, mapCallback: this.callback })
        .width('100%')
        .height('80%')
      Column() {
        Button('划线').onClick(async () => {
          // 绘制颜色渐变折线
          // polyline初始化参数
          let polylineOption: mapCommon.MapPolylineOptions = {
            points: markers, // 折线点坐标的数组
            clickable: true, // 折线可点击
            startCap: mapCommon.CapStyle.BUTT, // 折线起始顶点的样式
            endCap: mapCommon.CapStyle.BUTT, // 折线结束顶点的样式
            geodesic: false, // 折线线段是否为大地曲线
            jointType: mapCommon.JointType.BEVEL, // 折线的线条拐角样式
            visible: true,
            width: 10,
            zIndex: 10,
            gradient: true, // 颜色过渡开启
            colors: [0xffffff00, 0xff000000, 0xffCCCCCC, 0xffCF0983, 0xffee0000] // 过渡段颜色数组对应markers数组
            /**
             colors:[0xffffff00,0xff000000] // 过渡段颜色数组数量少于折线点数量，后半段颜色无渐变效果
             */
          };
          // 创建polyline
          await this.mapController?.addPolyline(polylineOption);
        })
        Button('marker').onClick(async () => {
          // 绘制多个坐标点的标记
          for (let i = 0; i < markers.length; i++) {
            // Marker初始化参数
            let markerOptions: mapCommon.MarkerOptions = {
              position: {
                latitude: markers[i].latitude,  // 标记点坐标
                longitude: markers[i].longitude
              },
              rotation: 0, // 标记点旋转角度
              visible: true,
              zIndex: 0,
              alpha: 0.9, // 标记点透明度
              anchorU: 0.5, // 锚点水平坐标
              anchorV: 1, // 锚点垂直坐标
              clickable: true, // 是否可点击
              draggable: true, // 是否可拖拽
              flat: false // 是否平贴地图
            };
            await this.mapController?.addMarker(markerOptions);
          }
        })
      }
    }
    .height('100%')
    .width('100%')
  }
}
```

## 总结

绘制颜色渐变的路径需要注意以下几点：

1. 显示地图要在AGC上开通地图服务，地图服务刚开通需24小时后生效。详见[Map Kit开发准备](../harmonyos-guides/map-config-agc.md)。
2. module.json5配置client\_id。打包使用手动签名，签名指纹要与AGC上一致。详见[Map Kit开发准备](../harmonyos-guides/map-config-agc.md)。
3. 折线参数gradient设置为true，colors数组长度要等于折线点数量以保证每段折线都有过渡色。
