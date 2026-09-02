---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-29
title: 如何实现地图不显示地铁路线
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > 如何实现地图不显示地铁路线
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:e4fad074bd1302e5a63e9c58280064a8f87d6f354c72ad8e336069789427472e
---

## 问题现象

如何实现在地图上去掉地铁路线的显示？

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/x0BYhQzjTxWHoMUSRetfLg/zh-cn_image_0000002658793631.png "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/Gvl02L3zSSCmGIqrZbJFIg/zh-cn_image_0000002628554264.png "点击放大")

## 背景知识

* Map Kit（地图服务）为开发者提供强大而便捷的地图能力，开发前需开通地图服务，参考：[开通地图服务](../harmonyos-guides/map-config-agc.md#开通地图服务)。
* Map Kit提供两种方法设置自定义地图样式：设置样式ID和设置样式内容，该示例使用[设置样式内容](../harmonyos-guides/map-style.md#设置样式内容)。

## 解决方案

地铁路线使用transit.metro-line属性控制，配置如下：

```ts
// 自定义样式参数
let param: mapCommon.CustomMapStyleOptions = {
  styleContent: `[{
    "mapFeature": "transit.metro-line",
    "options": "all",
    "visibility": false
  }]`
};
```

具体实现代码如下：

```ts
import { MapComponent, mapCommon, map } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';

@Entry
@Component
struct CustomMapStyleDemo {
  private mapOptions?: mapCommon.MapOptions;
  private mapController?: map.MapComponentController;
  private callback?: AsyncCallback<map.MapComponentController>;

  aboutToAppear(): void {
    // 地图初始化参数
    this.mapOptions = {
      position: {
        target: {
          latitude: 31.984410259206815,
          longitude: 118.76625379397866
        },
        zoom: 15
      }
    };
    this.callback = async (err, mapController) => {
      if (!err) {
        this.mapController = mapController;
        // 自定义样式参数
        let param: mapCommon.CustomMapStyleOptions = {
          styleContent: `[{
            "mapFeature": "transit.metro-line",
            "options": "all",
            "visibility": false
          }]`
        };
        // 设置自定义样式
        try {
          await this.mapController.setCustomMapStyle(param);
        } catch (error) {
          console.error(`setCustomMapStyle fail, code is：${error.code}, message is ${error.message}`);
        }
      } else {
        console.error(`init map fail, code is：${err.code}, message is ${err.message}`);
      }
    };
  }

  build() {
    Stack() {
      Column() {
        MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback });
      }.width('100%');
    }.height('100%');
  }
}
```
