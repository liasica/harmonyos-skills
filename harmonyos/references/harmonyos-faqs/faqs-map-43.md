---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-43
title: Map Kit地图如何不显示各省份名称
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > Map Kit地图如何不显示各省份名称
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:e57a37b1fb47f4e027ed83bc9c93cd83e2facda1924de73eaeb5787dbb740bde
---

## 问题现象

地图缩放到全国的场景下，如何实现不显示各省份名称？

## 背景知识

* 开发准备：使用地图服务，需要先[开通地图服务](../harmonyos-guides/map-config-agc.md#开通地图服务)。
* Map Kit提供两种方法设置自定义地图样式：
  + 设置样式ID：使用[Petal Maps Studio](https://developer.petalmaps.com/console/studio/)管理地图样式，并使用样式ID将它们链接到您的地图上。您可以在[Petal Maps Studio](https://developer.petalmaps.com/console/studio/)上创建新样式，或导入现有样式定义。样式一旦发布，使用此样式的应用都会自动应用新样式。
  + 设置样式内容：通过传入自定义JSON更改地图样式，JSON的定义参见[样式参考](../harmonyos-guides/map-style.md#样式参考)。

## 解决方案

配置地图自定义JSON的administrative.province为不显示。

代码示例如下：

```ts
import { map, mapCommon, MapComponent } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';
import { display } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  private mapOptions?: mapCommon.MapOptions;
  private mapController?: map.MapComponentController;
  private callback?: AsyncCallback<map.MapComponentController>;
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
        zoom: 4
      }
    };
    this.callback = async (err, mapController) => {
      if (!err) {
        this.mapController = mapController;
        // 自定义样式参数
        let param: mapCommon.CustomMapStyleOptions = {
          styleContent: `[
                            {
                                "mapFeature": "administrative.province",
                                "options": "all",
                                "visibility": false
                            }
                        ]`
        };
        // 设置自定义样式
        await this.mapController.setCustomMapStyle(param);
      }
    };
  }

  build() {
    Stack() {
      Column() {
        MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
          .height(this.mapHeight);
      }.width('100%');
    }.height('100%')
    .ignoreLayoutSafeArea();
  }
}
```

实现效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/tgpftYEvRJmRB9dTJY4JuQ/zh-cn_image_0000002656002802.png "点击放大")
