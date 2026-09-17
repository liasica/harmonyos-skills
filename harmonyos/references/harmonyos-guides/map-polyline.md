---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-polyline
title: 折线
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 在地图上绘制 > 折线
category: harmonyos-guides
scraped_at: 2026-09-18T06:46:21+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:92838592f6015db678d5a6e4d7402b347d6010671b9561d0c595cb23ff12dc46
---

## 场景介绍

本章节将向您介绍如何在地图上绘制折线、设置折线分段颜色、设置折线可渐变、绘制纹理。

折线主要用于展示步行、驾车、骑行等各类导航路线，同时可记录并呈现用户的运动轨迹及历史行程信息。此外，在区域边界标注、距离测量、管网线路布局以及活动路径可视化等场景中也有广泛应用。

5.0.3(15)开始，支持折线绘制纹理功能；26.0.0开始，支持折线添加文字。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/eB-R2zZ4T0OTlz6E4WHKqg/zh-cn_image_0000002727751710.jpg "点击放大")

## 接口说明

添加折线功能主要由[MapPolylineOptions](../harmonyos-references/map-common.md#mappolylineoptions)、[addPolyline](../harmonyos-references/map-map-mapcomponentcontroller.md#addpolyline)和[MapPolyline](../harmonyos-references/map-map-mappolyline.md)提供，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-map-mappolyline.md)。

| 接口名 | 描述 |
| --- | --- |
| [MapPolylineOptions](../harmonyos-references/map-common.md#mappolylineoptions) | 折线参数。 |
| [addPolyline](../harmonyos-references/map-map-mapcomponentcontroller.md#addpolyline)(options: [mapCommon.MapPolylineOptions](../harmonyos-references/map-common.md#mappolylineoptions)): Promise<[MapPolyline](../harmonyos-references/map-map-mappolyline.md)> | 在地图上添加一条折线。 |
| [MapPolyline](../harmonyos-references/map-map-mappolyline.md) | 折线，支持更新和查询相关属性。 |

## 开发步骤

### 添加折线

1. 导入相关模块。

   ```typescript
   import { MapComponent, mapCommon, map } from '@kit.MapKit';
   import { AsyncCallback } from '@kit.BasicServicesKit';
   ```
2. 添加折线，在callback方法中创建初始化参数并新建[MapPolyline](../harmonyos-references/map-map-mappolyline.md)。

   ```typescript
   @Entry
   @Component
   struct MapPolylineDemo {
     // ...
     private mapOptions?: mapCommon.MapOptions;
     private mapController?: map.MapComponentController;
     private callback?: AsyncCallback<map.MapComponentController>;
     private mapPolyline?: map.MapPolyline;

     aboutToAppear(): void {
       // 地图初始化参数
       this.mapOptions = {
         position: {
           target: {
             latitude: 31.98,
             longitude: 118.78
           },
           zoom: 14
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
             startCap: mapCommon.CapStyle.BUTT,
             endCap: mapCommon.CapStyle.BUTT,
             geodesic: false,
             jointType: mapCommon.JointType.BEVEL,
             visible: true,
             width: 10,
             zIndex: 10,
             gradient: false
           }
           // 创建polyline
           try {
             this.mapPolyline = await this.mapController.addPolyline(polylineOption);
           } catch (e) {
             console.error(`Failed to create the mapPolyline, code is：${e.code}, message is ${e.message}`);
           }
         } else {
           console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
         }
       };
     }

     build() {
       // ...
         Stack() {
           Column() {
             MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback });
           }.width('100%')
         }.height('100%')

         // ...
     }
   }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/1o4bYHSFQTK2GguW1cVedw/zh-cn_image_0000002757311425.jpg "点击放大")

### 设置折线分段颜色

方法一：新建折线时在[MapPolylineOptions](../harmonyos-references/map-common.md#mappolylineoptions)的colors属性中设置折线分段颜色值。

```typescript
let polylineOption: mapCommon.MapPolylineOptions = {
  points: [
    { longitude: 118.78, latitude: 31.975 },
    { longitude: 118.78, latitude: 31.982 },
    { longitude: 118.79, latitude: 31.985 }
  ],
  clickable: true,
  startCap: mapCommon.CapStyle.BUTT,
  endCap: mapCommon.CapStyle.BUTT,
  geodesic: false,
  jointType: mapCommon.JointType.BEVEL,
  visible: true,
  width: 10,
  zIndex: 10,
  // 设置颜色
  colors: [0xffffff00, 0xff000000],
  gradient: false
};
```

方法二：调用[MapPolyline](../harmonyos-references/map-map-mappolyline.md)的[setColors](../harmonyos-references/map-map-mappolyline.md#setcolors)()方法。

```typescript
let colors = [0xffffff00, 0xff000000];
this.mapPolyline.setColors(colors);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/auSOKjtxRo6etnOiQ5Nnlw/zh-cn_image_0000002757231545.jpg "点击放大")

### 设置折线可渐变

方法一：[MapPolylineOptions](../harmonyos-references/map-common.md#mappolylineoptions)的gradient属性设置为true。

```typescript
let polylineOption: mapCommon.MapPolylineOptions = {
  points: [
    { longitude: 118.78, latitude: 31.975 },
    { longitude: 118.78, latitude: 31.982 },
    { longitude: 118.79, latitude: 31.985 }
  ],
  clickable: true,
  startCap: mapCommon.CapStyle.BUTT,
  endCap: mapCommon.CapStyle.BUTT,
  geodesic: false,
  jointType: mapCommon.JointType.BEVEL,
  visible: true,
  width: 10,
  zIndex: 10,
  colors: [0xffffff00, 0xff000000],
  // 设置颜色折线可渐变
  gradient: true
};
```

方法二：调用[MapPolyline](../harmonyos-references/map-map-mappolyline.md)的[setGradient](../harmonyos-references/map-map-mappolyline.md#setgradient)()方法。

```typescript
this.mapPolyline.setGradient(true);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/DbOjjRiMT6KNwu5Gwjgqtg/zh-cn_image_0000002727591854.jpg "点击放大")

### 绘制纹理

方法一：新建折线时在[MapPolylineOptions](../harmonyos-references/map-common.md#mappolylineoptions)的customTexture属性设置折线纹理。

```typescript
let polylineOption: mapCommon.MapPolylineOptions = {
  points: [
    { latitude: 32.220750, longitude: 118.788765 },
    { latitude: 32.120750, longitude: 118.788765 },
    { latitude: 32.020750, longitude: 118.788765 },
    { latitude: 31.920750, longitude: 118.788765 },
    { latitude: 31.820750, longitude: 118.788765 }
  ],
  clickable: true,
  jointType: mapCommon.JointType.DEFAULT,
  width: 20,
  // 图标需存放在resources/rawfile目录下
  customTexture: 'icon/naviline_arrow.png'
}
```

方法二：调用[MapPolyline](../harmonyos-references/map-map-mappolyline.md)的[setCustomTexture](../harmonyos-references/map-map-mappolyline.md#setcustomtexture)方法。

```typescript
await this.mapPolyline.setCustomTexture('icon/naviline_arrow.png');
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/qxLQyBYlRou14SYp7IV2-w/zh-cn_image_0000002727751712.jpg "点击放大")

### 折线设置分段纹理

新建折线时利用在[MapPolylineOptions](../harmonyos-references/map-common.md#mappolylineoptions)的customTextures和customTextureIndexes属性设置折线分段纹理。

```typescript
import { image } from '@kit.ImageKit';

// ...
// 数组存放图片内容
let customTextures: (ResourceStr | image.PixelMap)[] = [];
// 图标存放在resources/rawfile，'icon/img.png'参数值传入rawfile文件夹下的相对路径
customTextures.push('icon/img.png');
customTextures.push('icon/img_1.png');
let cusIndexNumber: number[] = [];
// cusIndexNumber数组长度与折线点数量必须相同，数组元素内容与customTextures下标相对应，图片从数组第二个元素开始选择
cusIndexNumber.push(0, 0, 1);
// polyline初始化参数
let polylineOption: mapCommon.MapPolylineOptions = {
  points: [
    { longitude: 118.78, latitude: 31.975 },
    { longitude: 118.78, latitude: 31.982 },
    { longitude: 118.79, latitude: 31.985 }
  ],
  clickable: true,
  startCap: mapCommon.CapStyle.BUTT,
  endCap: mapCommon.CapStyle.BUTT,
  jointType: mapCommon.JointType.BEVEL,
  width: 30,
  // 图标需存放在resources/rawfile目录下
  customTextures: customTextures,
  customTextureIndexes: cusIndexNumber
};
let mapPolyline = await this.mapController.addPolyline(polylineOption);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/x8y2LXgkSY-HB9kZpNub4w/zh-cn_image_0000002757311427.jpg "点击放大")

### 折线添加文字

新建折线后可调用[MapPolyline](../harmonyos-references/map-map-mappolyline.md)的[addLineText](../harmonyos-references/map-map-mappolyline.md#addlinetext)方法给折线添加文字，通过[removeLineText](../harmonyos-references/map-map-mappolyline.md#removelinetext)方法可删除折线文字。

```typescript
// 添加折线文字
let textLine: mapCommon.LineText = {
  lineNames: ['第一段文字', '第二段文字'],
  lineNameIndexes: [0, 1, 1, 2],
  nameOnRight: false,
  color: 0xFF000000,
  fontSize: 15,
  strokeColor: 0xFFFFFFFF,
  fontStyle: 0
};
this.mapPolyline.addLineText(textLine);
// ...

// 删除折线文字
this.mapPolyline.removeLineText();
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/x2RaWKowQmCqD45lwFYTrQ/zh-cn_image_0000002757231547.jpg "点击放大")
