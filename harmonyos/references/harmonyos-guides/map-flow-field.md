---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-flow-field
title: 流场图层
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 在地图上绘制 > 流场图层
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:52+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2c3448052559cde3c676655af7843050808fb24dba3868d957c76d5845452bcb
---

## 场景介绍

新增流场图层，用于在基础地图之上叠加数据。通常用于实时展示天气风场、洋流等场景。

6.0.0(20)开始，支持流场图层功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/I5ptFakjTImi0YjsANYUyQ/zh-cn_image_0000002583439091.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234951Z&HW-CC-Expire=86400&HW-CC-Sign=63EA16D88444C7FD6B0C74486B78743279A1C2A0833D72A0E88D0940A53C7CE8 "点击放大")

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

   ```
   1. import { mapCommon, map, MapComponent } from '@kit.MapKit';
   2. import { AsyncCallback } from '@kit.BasicServicesKit';
   ```
2. 绘制流场图层。

   ```
   1. @Entry
   2. @Component
   3. struct MapFlowFieldOverlayDemo {
   4. private TAG = "OHMapSDK_MapFlowFieldOverlayDemo";
   5. private mapOption?: mapCommon.MapOptions;
   6. private mapController?: map.MapComponentController;
   7. private callback?: AsyncCallback<map.MapComponentController>;
   8. private fieldOverlay?: map.FlowFieldOverlay;

   10. aboutToAppear(): void {
   11. this.mapOption = {
   12. position: {
   13. target: {
   14. latitude: 31.984410259206815,
   15. longitude: 118.76625379397866
   16. },
   17. zoom: 4
   18. },
   19. scaleControlsEnabled: true
   20. }

   22. this.callback = async (err, mapController) => {
   23. if (!err) {
   24. this.mapController = mapController;
   25. let params: mapCommon.FlowFieldOverlayParams = {
   26. // data为GRIB2规范的json数据，需开发者自行传输，可参考流场数据格式
   27. data:
   28. `[{
   29. "header": {
   30. "parameterUnit": "m.s-1",
   31. "parameterNumber": 2,
   32. "dx": 10,
   33. "dy": 20,
   34. "parameterNumberName": "U-component-wind",
   35. "la2": -90,
   36. "la1": 90,
   37. "parameterCategory": 2,
   38. "lo1": 0,
   39. "lo2": 359.75,
   40. "ny": 4,
   41. "nx": 4,
   42. "numberPoints": 16
   43. },
   44. "data": [2, 2, 2, 2, 2, 2, 2, 2, -10, -10, -1, -1, -1, -1, -3, 2]
   45. }, {
   46. "header": {
   47. "parameterUnit": "m.s-1",
   48. "parameterNumber": 3,
   49. "dx": 4,
   50. "dy": 4,
   51. "parameterNumberName": "U-component-wind",
   52. "la2": -90,
   53. "la1": 90,
   54. "parameterCategory": 2,
   55. "lo1": 0,
   56. "lo2": 359.75,
   57. "ny": 4,
   58. "nx": 4,
   59. "numberPoints": 16
   60. },
   61. "data": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -2, -3, -1]
   62. }]`,
   63. style: {
   64. count: 10000,
   65. color: 0xff0000ff,
   66. maxSpeed: 100,
   67. speedFactor: 1
   68. }
   69. };

   71. try {
   72. // 添加流场图层
   73. this.fieldOverlay = await this.mapController?.addFlowFieldOverlay(params);
   74. } catch (e) {
   75. console.error(this.TAG, `code:${e.code}, message:${e.message}`);
   76. }
   77. } else {
   78. console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
   79. }
   80. }
   81. }

   83. build() {
   84. Stack() {
   85. Column() {
   86. MapComponent({ mapOptions: this.mapOption, mapCallback: this.callback })
   87. .width('100%')
   88. .height('100%');
   89. }.width('100%')
   90. }.height('100%')
   91. }
   92. }
   ```

### 流场数据格式参考

[FlowFieldOverlayParams](../harmonyos-references/map-common.md#flowfieldoverlayparams)类的data参数格式为GRIB2规范的json数据。GRIB2是一种由世界气象组织（WMO）定义的二进制数据格式，主要用于存储和传输气象和气候数据。

```
1. [
2. // header表示数据的整体信息，data表示横向速度
3. {"header":{},"data":[]},
4. // header表示数据的整体信息，data表示纵向速度
5. {"header":{},"data":[]}
6. ]
```

下面是风场数据的示例：

```
1. [{
2. "header": {
3. "parameterUnit": "m.s-1",   // 风速单位
4. "parameterNumber": 2,       // 风速方向，2为U方向（横向），3为V方向（纵向）
5. "dx": 10,                   // 横向步长，即每个格子占用的经度值，类型为整数
6. "dy": 20,                   // 纵向步长，即每个格子占用的纬度值，类型为整数
7. "parameterNumberName": "U-component-wind",   // 风速方向名称，U方向
8. "la2": -90,                 // 纬度范围，la2需要小于la1
9. "la1": 90,                  // 纬度范围，la2需要小于la1
10. "parameterCategory": 2,     // 数据类别
11. "lo1": 0,                   // 经度范围，lo1需要小于lo2
12. "lo2": 359.75,              // 经度范围，lo1需要小于lo2
13. "nx": 4,                    // 横向格子数量，类型为整数
14. "ny": 4,                    // 纵向格子数量，类型为整数
15. "numberPoints": 16          // 表示风速的点数量，即单个data中的数据量
16. },
17. // 横向速度，数据量需等于numberPoints
18. "data": [2, 2, 2, 2, 2, 2, 2, 2, -10, -10, -1, -1, -1, -1, -3, 2]
19. }, {
20. "header": {
21. "parameterUnit": "m.s-1",   // 风速单位
22. "parameterNumber": 3,       // 风速方向，2为U方向（横向），3为V方向（纵向）
23. "dx": 4,                    // 横向步长，即每个格子占用的经度值，类型为整数
24. "dy": 4,                    // 纵向步长，即每个格子占用的纬度值，类型为整数
25. "parameterNumberName": "V-component-wind",   // 风速方向名称，V方向
26. "la2": -90,                 // 纬度范围，la2需要小于la1
27. "la1": 90,                  // 纬度范围，la2需要小于la1
28. "parameterCategory": 2,     // 数据类别
29. "lo1": 0,                   // 经度范围，lo1需要小于lo2
30. "lo2": 359.75,              // 经度范围，lo1需要小于lo2
31. "nx": 4,                    // 横向格子数量，类型为整数
32. "ny": 4,                    // 纵向格子数量，类型为整数
33. "numberPoints": 16          // 表示风速的点数量，即单个data中的数据量
34. },
35. // 横向速度，数据量需等于numberPoints
36. "data": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -2, -3, -1]
37. }]
```
