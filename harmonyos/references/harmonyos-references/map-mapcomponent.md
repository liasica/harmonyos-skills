---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-mapcomponent
title: MapComponent（地图组件）
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS组件 > MapComponent（地图组件）
category: harmonyos-references
scraped_at: 2026-04-28T08:17:29+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:506a5d9fc79231a2651ee641d8cc8d2fb6a22cd303160f4fe3bae760a61d5a78
---

本模块提供Map组件，您需要提供mapOptions和回调，通过回调获取MapComponentController对象。

**起始版本：** 4.1.0(11)

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { MapComponent } from '@kit.MapKit';
```

## MapComponent

PhonePC/2in1TabletWearable

MapComponent提供map组件，通过回调获取MapComponentController对象。

**装饰器类型：** @Component

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数**：

| **名称** | **类型** | 只读 | 可选 | 装饰器类型 | **说明** |
| --- | --- | --- | --- | --- | --- |
| mapOptions | [mapCommon.MapOptions](map-common.md#mapoptions) | 否 | 否 | NA | 地图初始化参数。 |
| mapCallback | AsyncCallback<[map.MapComponentController](map-map-mapcomponentcontroller.md)> | 否 | 否 | NA | 回调函数，当地图初始化成功，err为undefined，data为获取到的[map.MapComponentController](map-map-mapcomponentcontroller.md)；否则为错误对象。 |
| customInfoWindow | [customInfoWindowCallback](map-mapcomponent.md#custominfowindowcallback) | 否 | 是 | @BuilderParam | 自定义信息窗，显示一个自定义样式的信息窗，可用于展示标记相关的详细信息。 |

**示例：**

```
1. import { map, mapCommon, MapComponent } from '@kit.MapKit';
2. import { AsyncCallback } from '@kit.BasicServicesKit';
3. import { customInfoWindowCallback } from '@hms.core.map.MapComponent';

5. @Entry
6. @Component
7. struct MarkerDemo {
8. private mapOptions?: mapCommon.MapOptions;
9. private mapController?: map.MapComponentController;
10. private mapCallback?: AsyncCallback<map.MapComponentController>;

12. aboutToAppear(): void {
13. this.mapOptions = {
14. position: {
15. target: {
16. latitude: 32.120750,
17. longitude: 118.788765
18. },
19. zoom: 15
20. }
21. }

23. this.mapCallback = async (err, mapController) => {
24. if (!err) {
25. this.mapController = mapController;
26. let markerOptions: mapCommon.MarkerOptions = {
27. position: {
28. latitude: 32.120750,
29. longitude: 118.788765
30. },
31. clickable: true,
32. // 设置信息窗标题
33. title: "自定义信息窗"
34. };
35. await this.mapController?.addMarker(markerOptions);
36. }
37. }
38. }

40. build() {
41. Stack() {
42. Column() {
43. MapComponent({
44. mapOptions: this.mapOptions,
45. mapCallback: this.mapCallback,
46. // 自定义信息窗
47. customInfoWindow: this.customInfoWindow
48. })
49. .width('100%')
50. .height('100%')
51. }.width('100%')
52. }.height('100%')
53. }

55. // 自定义信息窗BuilderParam
56. @BuilderParam customInfoWindow: customInfoWindowCallback = this.customInfoWindowBuilder;

58. // 自定义信息窗Builder
59. @Builder
60. customInfoWindowBuilder($$: map.MarkerDelegate) {
61. if ($$.marker) {
62. Text($$.marker.getTitle())
63. .width("50%")
64. .height(50)
65. .backgroundColor(Color.Green)
66. .textAlign(TextAlign.Center)
67. .fontColor(Color.Black)
68. .font({ size: 25, weight: 10, style: FontStyle.Italic })
69. .border({
70. width: 3,
71. color: Color.Black,
72. radius: 25,
73. style: BorderStyle.Dashed
74. })
75. }
76. }
77. }
```

### build

PhonePC/2in1TabletWearable

build(): void

struct的默认构造函数，无法直接调用此方法。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

## customInfoWindowCallback

PhonePC/2in1TabletWearable

type customInfoWindowCallback = (markerDelegate: map.MarkerDelegate) => void

自定义信息窗回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数**：

| 参数名 | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| markerDelegate | [map.MarkerDelegate](map-map-markerdelegate.md) | 是 | 用于表示代理对象的标记。 |
