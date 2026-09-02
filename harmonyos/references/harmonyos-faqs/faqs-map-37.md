---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-37
title: 如何修改地图的折线纹理间距
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > 如何修改地图的折线纹理间距
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:0bd4768fcf14572021c876a1a6b830526484436f23ad287e93c1a95757dc9d53
---

## 问题现象

使用地图服务addPolyline添加箭头样式的纹理，会出现折线上箭头之间的间距太小、箭头过于密集的情况，如何修改折线纹理的间距？

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/CzT80x0_RLGzl_mcjR9Kzg/zh-cn_image_0000002628554274.png "点击放大")

## 背景知识

* 开发准备：使用地图服务，需要先[开通地图服务](../harmonyos-guides/map-config-agc.md#开通地图服务)。
* [addPolyline](../harmonyos-references/map-map-mapcomponentcontroller.md#addpolyline)：在地图上添加一条折线。
* customTextures：[折线设置分段纹理](../harmonyos-guides/map-polyline.md#折线设置分段纹理)时，通过customTextures设置每个折线线段的纹理图片。

## 解决方案

方案逻辑：通过customTexture配置折线纹理时，折线上纹理图片的间距默认为线宽的2倍，并且没有接口可以直接设置纹理图片的间距。而使用customTextures配置纹理时，添加的纹理图片间没有间距，可以配置纹理图片为带纯色底色的纹理，调整图片宽度，使图片之间的真实纹理的距离为预期的宽度。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/ynUaQaE5T3uP6awTOrvn_A/zh-cn_image_0000002658913595.png)

1. 获取路线的坐标点列表。
2. 添加调整后的纹理图到customTextures列表。

   ```ts
   let customTextures: Array<ResourceStr | image.PixelMap> = new Array();
   customTextures.push('icon/arrow.png'); // 设置为目标纹理图片
   ```
3. 配置customTextureIndexes纹理图片索引列表，索引值为customTextures纹理图列表中希望添加的纹理图的对应索引，列表中需要设置每个坐标线段的目标纹理图片索引值。如果规划整条路线为相同的纹理图时，则每个坐标线段配置相同的图片索引值，本案例场景全部配置为0。

   ```ts
   let cusIndexNumber: Array<number> = new Array();
   for (let i = 0; i < this.points.length; ++i) {
     cusIndexNumber.push(0);
   }
   ```
4. 配置MapPolylineOptions中points、customTextures、customTextureIndexes的值为步骤1/2/3中的值，并添加折线图。

   ```ts
   let polylineOption: mapCommon.MapPolylineOptions = {
     points: this.points,
     clickable: true,
     startCap: mapCommon.CapStyle.BUTT,
     endCap: mapCommon.CapStyle.BUTT,
     jointType: mapCommon.JointType.BEVEL,
     width: 20,
     customTextures: customTextures,
     customTextureIndexes: cusIndexNumber
   };

   await this.mapController?.addPolyline(polylineOption);
   ```

   效果图如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/FnyxQueaSqWmTg2er4IcGg/zh-cn_image_0000002628394382.png "点击放大")

完整代码如下：

```ts
import { map, mapCommon, MapComponent } from '@kit.MapKit';
import { AsyncCallback } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';
import { display } from '@kit.ArkUI';

@Entry
@Component
struct CustomTexture {
  private mapOptions?: mapCommon.MapOptions;
  private mapController?: map.MapComponentController;
  private callback?: AsyncCallback<map.MapComponentController>;
  @State points: mapCommon.LatLng[] = [];
  @State mapHeight: number = 0;

  async aboutToAppear() {
    let displayClass = display.getDefaultDisplaySync();
    this.mapHeight = this.getUIContext().px2vp(displayClass.height);
    // 地图初始化参数
    this.mapOptions = {
      position: {
        target: {
          latitude: 31.984410259206815,
          longitude: 118.76625379397866
        },
        zoom: 18
      }
    };

    this.callback = async (err, mapController) => {
      if (!err) {
        this.mapController = mapController;

      }
    };
  }

  async addRoute() {
    // 实际使用时根据获取的路线坐标进行赋值
    this.points = [{ longitude: 116.31084, latitude: 39.992281 },
      { longitude: 116.31084, latitude: 39.99218 },
      { longitude: 116.31083, latitude: 39.99215 },
      { longitude: 116.31081, latitude: 39.99212 },
      { longitude: 116.31076, latitude: 39.99205 },
      { longitude: 116.31075, latitude: 39.9920199 },
      { longitude: 116.31075, latitude: 39.99191 },
      { longitude: 116.31074, latitude: 39.99187 },
      { longitude: 116.31075, latitude: 39.9918 },
      { longitude: 116.31076, latitude: 39.99176 },
      { longitude: 116.31079, latitude: 39.99172 },
      { longitude: 116.31082, latitude: 39.9917 },
      { longitude: 116.31084, latitude: 39.99166 },
      { longitude: 116.31085, latitude: 39.9914599 },
      { longitude: 116.31085, latitude: 39.99135 },
      { longitude: 116.31081, latitude: 39.9913 },
      { longitude: 116.31078, latitude: 39.99129 },
      { longitude: 116.31067, latitude: 39.99129 },
      { longitude: 116.31054, latitude: 39.99128 },
      { longitude: 116.31053, latitude: 39.9911699 }];
    let customTextures: Array<ResourceStr | image.PixelMap> = new Array();
    customTextures.push('icon/arrow.png'); // 设置为目标纹理图片
    let cusIndexNumber: Array<number> = new Array();
    for (let i = 0; i < this.points.length; ++i) {
      cusIndexNumber.push(0);
    }

    let polylineOption: mapCommon.MapPolylineOptions = {
      points: this.points,
      clickable: true,
      startCap: mapCommon.CapStyle.BUTT,
      endCap: mapCommon.CapStyle.BUTT,
      jointType: mapCommon.JointType.BEVEL,
      width: 20,
      customTextures: customTextures,
      customTextureIndexes: cusIndexNumber
    };

    await this.mapController?.addPolyline(polylineOption);
    let cameraUpdate = map.newLatLng(polylineOption.points[0]);
    this.mapController?.moveCamera(cameraUpdate);
  }

  build() {
    Stack({ alignContent: Alignment.Bottom }) {
      Column() {
        MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
          .height(this.mapHeight)
          .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
      }.width('100%')

      Button('查看路线')
        .onClick(() => {
          this.addRoute();
        })
        .margin({ bottom: 20 })
    }.height('100%')
    .ignoreLayoutSafeArea()
  }
}
```

## 常见FAQ

Q：为什么把[MapPolylineOptions](../harmonyos-references/map-common.md#mappolylineoptions)中的color设置为Color.Red不生效？

A：color参数类型为number，只能输入ARGB格式。
