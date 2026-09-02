---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-12
title: Map Kit点聚合场景中，如何更新标记的图标
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > Map Kit点聚合场景中，如何更新标记的图标
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:cfbcc58adb490ae4968f2b1fc937b92af9056006d56245d8a5a9c9d546c2e209
---

## 问题现象

Map Kit点聚合场景中，如何在点绘制之后再进行图标更改？

## 背景知识

地图服务[开发准备](../harmonyos-guides/map-config-agc.md)：开通地图服务后再继续进行开发活动。

[点聚合](../harmonyos-guides/map-aggregate.md)场景，可以通过比例尺缩放自适应聚合效果，聚合图标可点击。聚合支持功能：

* 支持绘制聚合Overlay的自定义图标。
* 支持监听聚合Overlay的点击事件。
* 支持删除聚合Overlay。

## 解决方案

更新点图标有2种方式：

* 先使用[remove()](../harmonyos-references/map-map-baseoverlay.md#remove)删除老的点，再增加更换图片后新的点，达到更新图标效果，适用于应用自动触发更新场景。
* 使用[on('imageOverlayClick')](../harmonyos-references/map-map-mapcomponentcontroller.md#onimageoverlayclick)监听点击事件，在事件处理中直接更新点图标，适用于用户手动触发更新场景。

参考代码：

```ts
import { map, mapCommon, MapComponent } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';

@Entry
@Component
struct ImageOverlay {
  private mapOption?: mapCommon.MapOptions;
  private callback?: AsyncCallback<map.MapComponentController>;
  private mapController?: map.MapComponentController;
  private imageOverlayParams: mapCommon.ImageOverlayParams = {
    position: {
      latitude: 30.246, longitude: 120.145
    },
    width: 120,
    height: 120,
    image: $r('app.media.reboot'),
    transparency: 0.3,
    zIndex: 101,
    anchorU: 0.5,
    anchorV: 0.5,
    clickable: true,
    visible: true,
    bearing: 0
  };

  aboutToAppear(): void {
    // 地图初始化参数，设置地图中心点坐标及层级
    this.mapOption = {
      position: {
        target: {
          latitude: 30.246,
          longitude: 120.145
        },
        zoom: 16
      },
      zoomControlsEnabled: false,
      myLocationControlsEnabled: true
    };

    // 地图初始化的回调
    this.callback = async (err, mapController) => {
      if (!err) {
        // 获取地图的控制器类，用来操作地图
        this.mapController = mapController;
        // 启用我的位置图层
        this.mapController?.setMyLocationEnabled(true);

        // 增加图片点聚合
        let imageOverlay = await this.mapController?.addImageOverlay(this.imageOverlayParams);

        // 5秒后更换点图片，先删除老的点，再增加更换图片后新的点，达到更新图片效果
        setTimeout(async () => {
          this.imageOverlayParams.image = $r('app.media.emoji_happy');
          this.imageOverlayParams.width = 80;
          this.imageOverlayParams.height = 80;
          await imageOverlay.remove();
          this.mapController?.addImageOverlay(this.imageOverlayParams);
        }, 5000);

        // 使用点击事件直接更新点图片
        let imageOverlayCallback: Callback<map.ImageOverlay> = (imageOverlay: map.ImageOverlay) => {
          imageOverlay.setImage($r('app.media.startIcon'));
        };
        this.mapController.on('imageOverlayClick', imageOverlayCallback);
      }
    };
  }

  build() {
    Column() {
      MapComponent({ mapOptions: this.mapOption, mapCallback: this.callback }).width('100%').height('100%');
    };
  }
}
```
