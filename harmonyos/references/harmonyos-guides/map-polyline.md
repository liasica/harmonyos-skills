---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-polyline
title: 折线
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 在地图上绘制 > 折线
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1d470561ab1d551f56af68819cf86e26454a77eea45ecd2007aece1bcf235509
---

## 场景介绍

本章节将向您介绍如何在地图上绘制折线、设置折线分段颜色、设置折线可渐变、绘制纹理。

5.0.3(15)开始，支持折线绘制纹理功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/6JIXacicRmawVMLip-jlgQ/zh-cn_image_0000002558605878.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053510Z&HW-CC-Expire=86400&HW-CC-Sign=F8FF7D26604056ED54B65D4420E89B070B29DEA3D2DC5BCAF19F053C3B01D242 "点击放大")

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

   ```
   1. import { MapComponent, mapCommon, map } from '@kit.MapKit';
   2. import { AsyncCallback } from '@kit.BasicServicesKit';
   ```
2. 添加折线，在callback方法中创建初始化参数并新建[MapPolyline](../harmonyos-references/map-map-mappolyline.md)。

   ```
   1. @Entry
   2. @Component
   3. struct MapPolylineDemo {
   4. private mapOptions?: mapCommon.MapOptions;
   5. private mapController?: map.MapComponentController;
   6. private callback?: AsyncCallback<map.MapComponentController>;
   7. private mapPolyline?: map.MapPolyline;

   9. aboutToAppear(): void {
   10. // 地图初始化参数
   11. this.mapOptions = {
   12. position: {
   13. target: {
   14. latitude: 31.98,
   15. longitude: 118.78
   16. },
   17. zoom: 14
   18. }
   19. };
   20. this.callback = async (err, mapController) => {
   21. if (!err) {
   22. this.mapController = mapController;

   24. // polyline初始化参数
   25. let polylineOption: mapCommon.MapPolylineOptions = {
   26. points: [
   27. { longitude: 118.78, latitude: 31.975 },
   28. { longitude: 118.78, latitude: 31.982 },
   29. { longitude: 118.79, latitude: 31.985 }
   30. ],
   31. clickable: true,
   32. startCap: mapCommon.CapStyle.BUTT,
   33. endCap: mapCommon.CapStyle.BUTT,
   34. geodesic: false,
   35. jointType: mapCommon.JointType.BEVEL,
   36. visible: true,
   37. width: 10,
   38. zIndex: 10,
   39. gradient: false
   40. }
   41. // 创建polyline
   42. try {
   43. this.mapPolyline = await this.mapController.addPolyline(polylineOption);
   44. } catch (e) {
   45. console.error(`Failed to create the mapPolyline, code is：${e.code}, message is ${e.message}`);
   46. }
   47. } else {
   48. console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
   49. }
   50. };
   51. }

   53. build() {
   54. Stack() {
   55. Column() {
   56. MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback });
   57. }.width('100%')
   58. }.height('100%')
   59. }
   60. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/pKDS6qpfQderaHmzY0xIdA/zh-cn_image_0000002589325405.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053510Z&HW-CC-Expire=86400&HW-CC-Sign=413DE86ECAAFFCAB8B70DA99FDE2819806E39224B630A83EF3DA7477EC0EA759 "点击放大")

### 设置折线分段颜色

方法一：新建折线时在[MapPolylineOptions](../harmonyos-references/map-common.md#mappolylineoptions)的colors属性中设置折线分段颜色值。

```
1. let polylineOption: mapCommon.MapPolylineOptions = {
2. points: [
3. { longitude:118.78, latitude:31.975 },
4. { longitude:118.78, latitude:31.982 },
5. { longitude:118.79, latitude:31.985 }
6. ],
7. clickable: true,
8. startCap: mapCommon.CapStyle.BUTT,
9. endCap: mapCommon.CapStyle.BUTT,
10. geodesic: false,
11. jointType: mapCommon.JointType.BEVEL,
12. visible: true,
13. width: 10,
14. zIndex: 10,
15. // 设置颜色
16. colors: [0xffffff00, 0xff000000],
17. gradient: false
18. };
```

方法二：调用[MapPolyline](../harmonyos-references/map-map-mappolyline.md)的[setColors](../harmonyos-references/map-map-mappolyline.md#setcolors)()方法。

```
1. let colors = [0xffffff00, 0xff000000];
2. this.mapPolyline.setColors(colors);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/6pmVTtItSC-EKdND2MlyVg/zh-cn_image_0000002589245343.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053510Z&HW-CC-Expire=86400&HW-CC-Sign=E14FF44CF1970B0AFE166E33DC57050E37CB73D053BEAE870AB014FD352A14BD "点击放大")

### 设置折线可渐变

方法一：[MapPolylineOptions](../harmonyos-references/map-common.md#mappolylineoptions)的gradient属性设置为true。

```
1. let polylineOption: mapCommon.MapPolylineOptions = {
2. points: [
3. { longitude:118.78, latitude:31.975 },
4. { longitude:118.78, latitude:31.982 },
5. { longitude:118.79, latitude:31.985 }
6. ],
7. clickable: true,
8. startCap: mapCommon.CapStyle.BUTT,
9. endCap: mapCommon.CapStyle.BUTT,
10. geodesic: false,
11. jointType: mapCommon.JointType.BEVEL,
12. visible: true,
13. width: 10,
14. zIndex: 10,
15. colors: [0xffffff00, 0xff000000],
16. // 设置颜色折线可渐变
17. gradient: true
18. };
```

方法二：调用[MapPolyline](../harmonyos-references/map-map-mappolyline.md)的[setGradient](../harmonyos-references/map-map-mappolyline.md#setgradient)()方法。

```
1. this.mapPolyline.setGradient(true);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/frcUUeOhTsitDxPF_KWjQw/zh-cn_image_0000002558765536.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053510Z&HW-CC-Expire=86400&HW-CC-Sign=434EA1AA5FA85067FA6612D3E7BF2858372EF5C5C25ACE75D40D4B12D972C29B "点击放大")

### 绘制纹理

方法一：新建折线时在[MapPolylineOptions](../harmonyos-references/map-common.md#mappolylineoptions)的customTexture属性设置折线纹理。

```
1. let polylineOption: mapCommon.MapPolylineOptions = {
2. points: [
3. { latitude: 32.220750, longitude: 118.788765 },
4. { latitude: 32.120750, longitude: 118.788765 },
5. { latitude: 32.020750, longitude: 118.788765 },
6. { latitude: 31.920750, longitude: 118.788765 },
7. { latitude: 31.820750, longitude: 118.788765 }
8. ],
9. clickable: true,
10. jointType: mapCommon.JointType.DEFAULT,
11. width: 20,
12. // 图标需存放在resources/rawfile目录下
13. customTexture: "icon/naviline_arrow.png"
14. }
```

方法二：调用[MapPolyline](../harmonyos-references/map-map-mappolyline.md)的[setCustomTexture](../harmonyos-references/map-map-mappolyline.md#setcustomtexture)方法。

```
1. await this.mapPolyline.setCustomTexture("icon/naviline_arrow.png");
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/UIbRUqmQRv-9Zh7kCNbSsA/zh-cn_image_0000002558605880.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053510Z&HW-CC-Expire=86400&HW-CC-Sign=6E4618F3F25FAF24B0C541A0D13EE5D4C09FAD98BDFCE0593DB8FAABF0FD22EB "点击放大")

### 折线设置分段纹理

新建折线时利用在[MapPolylineOptions](../harmonyos-references/map-common.md#mappolylineoptions)的customTextures和customTextureIndexes属性设置折线分段纹理。

```
1. import { image } from '@kit.ImageKit';

3. // 数组存放图片内容
4. let customTextures: Array<ResourceStr | image.PixelMap> = new Array();
5. // 图标存放在resources/rawfile，'icon/img.png'参数值传入rawfile文件夹下的相对路径
6. customTextures.push('icon/img.png');
7. customTextures.push('icon/img_1.png');
8. let cusIndexNumber: Array<number> = new Array();
9. // cusIndexNumber数组长度与折线点数量必须相同，数组元素内容与customTextures下标相对应，图片从数组第二个元素开始选择
10. cusIndexNumber.push(0, 0, 1);
11. // polyline初始化参数
12. let polylineOption: mapCommon.MapPolylineOptions = {
13. points: [
14. { longitude: 118.78, latitude: 31.975 },
15. { longitude: 118.78, latitude: 31.982 },
16. { longitude: 118.79, latitude: 31.985 }
17. ],
18. clickable: true,
19. startCap: mapCommon.CapStyle.BUTT,
20. endCap: mapCommon.CapStyle.BUTT,
21. jointType: mapCommon.JointType.BEVEL,
22. width: 30,
23. // 图标需存放在resources/rawfile目录下
24. customTextures: customTextures,
25. customTextureIndexes: cusIndexNumber
26. };
27. let mapPolyline = await this.mapController.addPolyline(polylineOption);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/wr8t9RyaRAuH4LirlVv_xA/zh-cn_image_0000002589325407.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053510Z&HW-CC-Expire=86400&HW-CC-Sign=6A52AB89E6B8B84DBCD5672BAEB31C015ACBFC076300182C945D5B1E4BA5CAB8 "点击放大")
