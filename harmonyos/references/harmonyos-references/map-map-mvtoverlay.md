---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mvtoverlay
title: MvtOverlay
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > MvtOverlay
category: harmonyos-references
scraped_at: 2026-04-28T08:17:20+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:de48da4369c446e7e8a07022336aa4880806eb0c95de9e602a6c322820f1889c
---

## 导入模块

PhonePC/2in1Tablet

```
1. import { map, mapCommon } from '@kit.MapKit';
```

## MvtOverlay

PhonePC/2in1Tablet

矢量图层的管理对象。在调用map.[MapComponentController](map-map-mapcomponentcontroller.md)类的[addMvtOverlay](map-map-mapcomponentcontroller.md#addmvtoverlay)方法时会返回该类型的实例，继承[BaseOverlay](map-map-baseoverlay.md)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core.EnhancedOverlay

**起始版本：** 6.0.0(20)

**示例：**

```
1. let params: mapCommon.MvtOverlayParams = {
2. source: {
3. // 设置矢量图层的地址,必须是以http或者https开头的URL且包含占位符{x}、{y}和{z}
4. tileUrl: 'http://xxx/tiles/{z}/{x}/{y}.pbf',
5. minZoom: 2,
6. maxZoom: 15
7. },
8. layers: [{
9. id: 'layer-map',
10. type: mapCommon.MvtLayerType.FILL,
11. // 对应矢量图层数据中图层的name字段
12. sourceLayer: 'XX',
13. paint: {
14. fillColor: {
15. operator: mapCommon.Operator.GET,
16. args: 'fill'
17. },
18. fillOpacity: {
19. operator: mapCommon.Operator.GET,
20. args: 'fill-opacity'
21. }
22. }
23. }]
24. };
25. let mvtOverlay = this.mapController?.addMvtOverlay(params);
```

### addLayers

PhonePC/2in1Tablet

addLayers(layers: mapCommon.MvtLayer[]): void

添加新矢量图层。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core.EnhancedOverlay

**起始版本：** 6.0.0(20)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| layers | [mapCommon.MvtLayer](map-common.md#mvtlayer)[] | 是 | 矢量图层，建议矢量图层少于2000层，确保矢量图层的流畅度。 |

**示例：**

```
1. let renderLayers: Array<mapCommon.MvtLayer> = []
2. let staticLayerIds = [-12, -8, -4, 0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44];
3. for (let index = 0; index < staticLayerIds.length; index++) {
4. let layer: mapCommon.MvtLayer = {
5. id: index.toString(),
6. type: mapCommon.MvtLayerType.FILL,
7. sourceLayer: staticLayerIds[index].toString(),
8. paint: {
9. fillColor: {
10. operator: mapCommon.Operator.GET,
11. args: 'fill'
12. },
13. fillOpacity: {
14. operator: mapCommon.Operator.GET,
15. args: 'fill-opacity'
16. }
17. }
18. }
19. renderLayers.push(layer)
20. };

22. mvtOverlay.addLayers(renderLayers);
```

### removeLayers

PhonePC/2in1Tablet

removeLayers(layerIds: string[]): void

移除指定的图层。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core.EnhancedOverlay

**起始版本：** 6.0.0(20)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| layerIds | string[] | 是 | 需要删除的图层ID。 |

**示例：**

```
1. let layerIds = ['111'];
2. mvtOverlay.removeLayers(layerIds);
```

### changeLayers

PhonePC/2in1Tablet

changeLayers(addedLayers: mapCommon.MvtLayer[], removedLayerIds: string[]): void

新增矢量图层，根据图层ID删除图层。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core.EnhancedOverlay

**起始版本：** 6.0.0(20)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| addedLayers | [mapCommon.MvtLayer](map-common.md#mvtlayer)[] | 是 | 矢量图层。 |
| removedLayerIds | string[] | 是 | 需要删除的图层ID。 |

**示例：**

```
1. let renderLayers: Array<mapCommon.MvtLayer> = [];
2. let staticLayerIds = [-12, -8, -4, 0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44];
3. for (let index = 0; index < staticLayerIds.length; index++) {
4. let layer: mapCommon.MvtLayer = {
5. id: index.toString(),
6. type: mapCommon.MvtLayerType.FILL,
7. sourceLayer: staticLayerIds[index].toString(),
8. paint: {
9. fillColor: {
10. operator: mapCommon.Operator.GET,
11. args: 'fill'
12. },
13. fillOpacity: {
14. operator: mapCommon.Operator.GET,
15. args: 'fill-opacity'
16. }
17. }
18. }
19. renderLayers.push(layer)
20. }
21. let layerIds = ['111'];

23. mvtOverlay.changeLayers(renderLayers, layerIds);
```

### setBlur

PhonePC/2in1Tablet

setBlur(blurIntensity: number | Record<number, number>): void

更新矢量图层的模糊度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.2(22)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core.EnhancedOverlay

**起始版本：** 6.0.2(22)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| blurIntensity | number | Record<number, number> | 是 | 矢量图层的模糊度，不支持3D地球。  模糊度范围：[0, 20]，小数向下取整，默认值为0，异常值按默认值处理。  若传数字，表示所有缩放层级按同一模糊度处理。  若传键值对，key为缩放层级，value为模糊度，有效层级范围：[2，20]，层级异常值大于20取20，小于2取2。例如：{ 5: 5, 10: 8, 18: 15 }，2到4层级为0，默认不模糊，5到9层级模糊度为5，10到17层级模糊度为8，18到20层级模糊度为15。 |

**示例：**

```
1. mvtOverlay.setBlur(8);
```

### getBlur

PhonePC/2in1Tablet

getBlur(): number | Record<number, number>

获取矢量图层的模糊度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.2(22)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core.EnhancedOverlay

**起始版本：** 6.0.2(22)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | Record<number, number> | 矢量图层的模糊度。  模糊度范围：[0, 20]。  若为数字，表示所有缩放层级按同一模糊度处理。  若为键值对，key为缩放层级，value为模糊度，有效层级范围：[2，20]。例如：{ 5: 5, 10: 8, 18: 15 }，2到4层级为0，默认不模糊，5到9层级模糊度为5，10到17层级模糊度为8，18到20层级模糊度为15。 |

**示例：**

```
1. let blur: number | Record<number, number> = mvtOverlay.getBlur()
```
