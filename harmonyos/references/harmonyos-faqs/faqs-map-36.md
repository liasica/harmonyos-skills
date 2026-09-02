---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-36
title: 如何在地图上绘制虚线
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > 如何在地图上绘制虚线
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:52c075b33a8d920da602005e427be3f401e21e99d5e9345f9f4e77b891bf0eee
---

## 问题现象

参考官网的文档，可以实现在地图上添加折线，如何实现虚线效果？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/1lfXEhVjR9mF5ePRffaglw/zh-cn_image_0000002658793639.png "点击放大")

## 背景知识

* Map Kit（地图服务）为开发者提供强大而便捷的地图能力，开发前需开通地图服务，参考：[开通地图服务](../harmonyos-guides/map-config-agc.md#开通地图服务)。
* 添加[折线](../harmonyos-guides/map-polyline.md)功能主要由[MapPolylineOptions](../harmonyos-references/map-common.md#mappolylineoptions)、[addPolyline](../harmonyos-references/map-map-mapcomponentcontroller.md#addpolyline)和[MapPolyline](../harmonyos-references/map-map-mappolyline.md)提供。
* [PatternItemType](../harmonyos-references/map-common.md#patternitemtype)：描述圆、多边形或折线的边框样式类型。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DASH | 0 | 表示折线、多边形或圆的边框中的短划线。 |
| DOT | 1 | 表示折线、多边形或圆的边框的点。 |
| GAP | 2 | 表示折线、多边形或圆中边框的间隙。 |

## 解决方案

patterns可配置折线的样式，将patterns设置成patterns: [{ type: 0, length: 10 }, { type: 2, length: 10 }]表示短划线与间隙1：1相间，即呈现虚线效果。完整示例参考如下：

```ts
import { MapComponent, mapCommon, map } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';
import { display } from '@kit.ArkUI';

@Entry
@Component
struct PolylinePage {
  private mapOptions?: mapCommon.MapOptions;
  private mapController?: map.MapComponentController;
  private callback?: AsyncCallback<map.MapComponentController>;
  @State mapHeight: number = 0;

  aboutToAppear(): void {
    try {
      let displayClass = display.getDefaultDisplaySync();
      this.mapHeight = this.getUIContext().px2vp(displayClass.height);
    } catch (error) {
      console.error(`getDefaultDisplaySync error. Code is ${error.code}, message is ${error.message}.`);
    }

    // 地图初始化参数
    this.mapOptions = {
      position: {
        target: {
          latitude: 31.985,
          longitude: 118.78
        },
        zoom: 15
      }
    };

    this.callback = async (err, mapController) => {
      if (!err) {
        this.mapController = mapController;

        // polyline初始化参数
        let polylineOption: mapCommon.MapPolylineOptions = {
          points: [
            { longitude: 118.78, latitude: 31.975 },
            { longitude: 118.78, latitude: 31.982 },
            { longitude: 118.79, latitude: 31.985 }
          ],
          clickable: true,
          startCap: mapCommon.CapStyle.ROUND,
          endCap: mapCommon.CapStyle.ROUND,
          jointType: mapCommon.JointType.BEVEL,
          visible: true,
          width: 10,
          zIndex: 1,
          gradient: false,
          patterns: [{ type: 0, length: 10 }, { type: 2, length: 10 }]
        };
        // 创建polyline
        try {
          await this.mapController.addPolyline(polylineOption);
        } catch (error) {
          console.error(`创建polyline失败, code is：${error.code}, message is ${error.message}`);
        }
      } else {
        console.error(`地图初始化失败, code is：${err.code}, message is ${err.message}`);
      }
    };
  }

  build() {
    Stack() {
      MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
        .width('100%')
        .height(this.mapHeight)
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
    }.height('100%');
  }
}
```
