---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-flow-field
title: 流场图层
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 在地图上绘制 > 流场图层
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:13+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:ffb7227ccf80767b943421ecfeb413b0993ec4150e566ee0dd0aa15605de6388
---

## 场景介绍

新增流场图层用于在基础地图之上叠加矢量数据，以可视化显示动态流动信息，如风场、洋流等，适用于需要实时展示流体运动状态的应用场景。

6.0.0(20)开始，支持流场图层功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/BrUAgZ-_RJihAxoTEr7c_w/zh-cn_image_0000002712245312.gif "点击放大")

## 接口说明

流场图层功能主要由[FlowFieldOverlayParams](../harmonyos-references/map-common.md#flowfieldoverlayparams)、[addFlowFieldOverlay](../harmonyos-references/map-map-mapcomponentcontroller.md#addflowfieldoverlay)和[FlowFieldOverlay](../harmonyos-references/map-map-flowfieldoverlay.md)提供，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-map-flowfieldoverlay.md)。

| 接口名 | 描述 |
| --- | --- |
| [FlowFieldOverlayParams](../harmonyos-references/map-common.md#flowfieldoverlayparams) | 流场覆盖物参数。 |
| [addFlowFieldOverlay](../harmonyos-references/map-map-mapcomponentcontroller.md#addflowfieldoverlay)(params: mapCommon.[FlowFieldOverlayParams](../harmonyos-references/map-common.md#flowfieldoverlayparams)): Promise<[FlowFieldOverlay](../harmonyos-references/map-map-flowfieldoverlay.md)> | 新增流场覆盖物。 |
| [FlowFieldOverlay](../harmonyos-references/map-map-flowfieldoverlay.md) | 流场覆盖物管理对象。 |

## 开发步骤

### 添加流场图层

1. 导入相关模块。

   ```typescript
   import { mapCommon, map, MapComponent } from '@kit.MapKit';
   import { AsyncCallback } from '@kit.BasicServicesKit';
   ```
2. 绘制流场图层。

   ```typescript
   @Entry
   @Component
   struct MapFlowFieldOverlayDemo {
     private TAG = "OHMapSDK_MapFlowFieldOverlayDemo";
     private mapOption?: mapCommon.MapOptions;
     private mapController?: map.MapComponentController;
     private callback?: AsyncCallback<map.MapComponentController>;
     private fieldOverlay?: map.FlowFieldOverlay;

     aboutToAppear(): void {
       this.mapOption = {
         position: {
           target: {
             latitude: 31.984410259206815,
             longitude: 118.76625379397866
           },
           zoom: 4
         },
         scaleControlsEnabled: true
       }

       this.callback = async (err, mapController) => {
         if (!err) {
           this.mapController = mapController;
           let params: mapCommon.FlowFieldOverlayParams = {
             // data为GRIB2规范的json数据，需开发者自行传输，可参考流场数据格式
             data:
             `[{
               "header": {
                 "parameterUnit": "m.s-1",
                 "parameterNumber": 2,
                 "dx": 10,
                 "dy": 20,
                 "parameterNumberName": "U-component-wind",
                 "la2": -90,
                 "la1": 90,
                 "parameterCategory": 2,
                 "lo1": 0,
                 "lo2": 359.75,
                 "ny": 4,
                 "nx": 4,
                 "numberPoints": 16
               },
               "data": [2, 2, 2, 2, 2, 2, 2, 2, -10, -10, -1, -1, -1, -1, -3, 2]
             }, {
               "header": {
                 "parameterUnit": "m.s-1",
                 "parameterNumber": 3,
                 "dx": 4,
                 "dy": 4,
                 "parameterNumberName": "U-component-wind",
                 "la2": -90,
                 "la1": 90,
                 "parameterCategory": 2,
                 "lo1": 0,
                 "lo2": 359.75,
                 "ny": 4,
                 "nx": 4,
                 "numberPoints": 16
               },
               "data": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -2, -3, -1]
             }]`,
             style: {
               count: 2000,
               color: 0xff0000ff,
               maxSpeed: 100,
               speedFactor: 1
             }
           };

           try {
             // 添加流场图层
             this.fieldOverlay = await this.mapController?.addFlowFieldOverlay(params);
           } catch (e) {
             console.error(this.TAG, `code:${e.code}, message:${e.message}`);
           }
         } else {
           console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
         }
       }
     }

     build() {
       Stack() {
         Column() {
           MapComponent({ mapOptions: this.mapOption, mapCallback: this.callback })
             .width('100%')
             .height('100%');
         }.width('100%')
       }.height('100%')
     }
   }
   ```

### 流场数据格式参考

[FlowFieldOverlayParams](../harmonyos-references/map-common.md#flowfieldoverlayparams)类的data参数格式为GRIB2规范的json数据。GRIB2是一种由世界气象组织（WMO）定义的二进制数据格式，主要用于存储和传输气象和气候数据。

```typescript
[
  // header表示数据的整体信息，data表示横向速度
  {"header":{},"data":[]},
  // header表示数据的整体信息，data表示纵向速度
  {"header":{},"data":[]}
]
```

下面是风场数据的示例：

```typescript
[{
  "header": {
    "parameterUnit": "m.s-1",   // 风速单位
    "parameterNumber": 2,       // 风速方向，2为U方向（横向），3为V方向（纵向）
    "dx": 10,                   // 横向步长，即每个格子占用的经度值，类型为整数
    "dy": 20,                   // 纵向步长，即每个格子占用的纬度值，类型为整数
    "parameterNumberName": "U-component-wind",   // 风速方向名称，U方向
    "la2": -90,                 // 纬度范围，la2需要小于la1
    "la1": 90,                  // 纬度范围，la2需要小于la1
    "parameterCategory": 2,     // 数据类别
    "lo1": 0,                   // 经度范围，lo1需要小于lo2
    "lo2": 359.75,              // 经度范围，lo1需要小于lo2
    "nx": 4,                    // 横向格子数量，类型为整数
    "ny": 4,                    // 纵向格子数量，类型为整数
    "numberPoints": 16          // 表示风速的点数量，即单个data中的数据量
  },
  // 横向速度，数据量需等于numberPoints
  "data": [2, 2, 2, 2, 2, 2, 2, 2, -10, -10, -1, -1, -1, -1, -3, 2]
}, {
  "header": {
    "parameterUnit": "m.s-1",   // 风速单位
    "parameterNumber": 3,       // 风速方向，2为U方向（横向），3为V方向（纵向）
    "dx": 4,                    // 横向步长，即每个格子占用的经度值，类型为整数
    "dy": 4,                    // 纵向步长，即每个格子占用的纬度值，类型为整数
    "parameterNumberName": "V-component-wind",   // 风速方向名称，V方向
    "la2": -90,                 // 纬度范围，la2需要小于la1
    "la1": 90,                  // 纬度范围，la2需要小于la1
    "parameterCategory": 2,     // 数据类别
    "lo1": 0,                   // 经度范围，lo1需要小于lo2
    "lo2": 359.75,              // 经度范围，lo1需要小于lo2
    "nx": 4,                    // 横向格子数量，类型为整数
    "ny": 4,                    // 纵向格子数量，类型为整数
    "numberPoints": 16          // 表示风速的点数量，即单个data中的数据量
  },
  // 纵向速度，数据量需等于numberPoints
  "data": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -2, -3, -1]
}]
```
