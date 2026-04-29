---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-style
title: 显示自定义地图
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 创建地图 > 显示自定义地图
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6a5dbbf61c45a6f9e9157a82cf7d19c3cb3e31743daa2c16d386581555dc3965
---

## 场景介绍

本章节将向您介绍如何在应用中添加自定义样式的地图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/hk9ULeDKSDGFRbZ3wvBp8Q/zh-cn_image_0000002589245321.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053859Z&HW-CC-Expire=86400&HW-CC-Sign=33308AF460F5870D898740BA31C7B8BAD7C5765C5C41BAC180B32FE67BE9C2CB "点击放大")

## 接口说明

自定义样式功能主要由[CustomMapStyleOptions](../harmonyos-references/map-common.md#custommapstyleoptions)、[setCustomMapStyle](../harmonyos-references/map-map-mapcomponentcontroller.md#setcustommapstyle)提供，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-map-mapcomponentcontroller.md#setcustommapstyle)。

| 接口名 | 描述 |
| --- | --- |
| [CustomMapStyleOptions](../harmonyos-references/map-common.md#custommapstyleoptions) | 自定义样式参数。 |
| [setCustomMapStyle](../harmonyos-references/map-map-mapcomponentcontroller.md#setcustommapstyle)(customMapStyleOptions: [mapCommon.CustomMapStyleOptions](../harmonyos-references/map-common.md#custommapstyleoptions)): Promise<void> | 将地图样式修改为自定义样式。 |

## 开发步骤

Map Kit提供两种方法设置自定义地图样式：

* 设置样式ID：使用[Petal Maps Studio](https://developer.petalmaps.com/console/studio/)管理地图样式，并使用样式ID将它们链接到您的地图上。您可以在[Petal Maps Studio](https://developer.petalmaps.com/console/studio/)上创建新样式，或导入现有样式定义。样式一旦发布，使用此样式的应用都会自动应用新样式。
* 设置样式内容：通过传入自定义JSON更改地图样式，JSON的定义参见[样式参考](map-style.md#样式参考)。

### 设置样式ID

1. 导入相关模块。

   ```
   1. import { MapComponent, mapCommon, map } from '@kit.MapKit';
   2. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
   ```
2. 创建样式ID。

   a.登录[Petal Maps Studio](https://developer.petalmaps.com/console/studio/)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/KkUqA9LKQNaq68FaxVhExg/zh-cn_image_0000002558765516.png?HW-CC-KV=V1&HW-CC-Date=20260429T053859Z&HW-CC-Expire=86400&HW-CC-Sign=55BE3B8B2CF04AB6F57FEE5345D1CE5B29C57A8B323FE6D112CE38700674C732)

   b.点击“Create map”创建自定义样式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/PJcb5LbLQUuVSEFwz-LoFw/zh-cn_image_0000002558605860.png?HW-CC-KV=V1&HW-CC-Date=20260429T053859Z&HW-CC-Expire=86400&HW-CC-Sign=8FAE27BF5AC3645807C9EDAC02C15D46D76C6F6ED9F6BE809E8B5712F0DE229C)

   c.导入JSON样式文件，点击“Import”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/1ThjqBs5QN-G2pvm5yko6A/zh-cn_image_0000002589325387.png?HW-CC-KV=V1&HW-CC-Date=20260429T053859Z&HW-CC-Expire=86400&HW-CC-Sign=B963BBC222177FAA25A15B2E4010F350082EB374A3CACBFBDACCE0D67100FCA3)

   d.在编辑器里修改样式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/EeI2pSeTRPyVdg7iRKlmrw/zh-cn_image_0000002589245323.png?HW-CC-KV=V1&HW-CC-Date=20260429T053859Z&HW-CC-Expire=86400&HW-CC-Sign=C9BD0C2087303645D288DD23AC0F2ADC4D3C3DCC8E960DA4D87548D634614908)

   e.点击“SAVE”生成预览ID，预览ID在编辑样式时会重新生成，您可以通过预览ID测试样式效果。点击“PUBLISH”发布生成样式ID，样式ID是唯一ID，一旦发布生效不会变化。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/lZ31v0HyQ2S4IJ-5DkMEZg/zh-cn_image_0000002558765518.png?HW-CC-KV=V1&HW-CC-Date=20260429T053859Z&HW-CC-Expire=86400&HW-CC-Sign=B1CBDDCE1ED896479016E5301F463ACADA152EBE845D4234CC058E0565CFB22D)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/BWvbeeGETrOkpWOMR-6hWg/zh-cn_image_0000002558605862.png?HW-CC-KV=V1&HW-CC-Date=20260429T053859Z&HW-CC-Expire=86400&HW-CC-Sign=37D3E8F5847159F6EFCCE4ADE576439552BF28369640869BDF9DD73AC0F58DE7)
3. Map Kit提供两种方法设置样式ID：

   * 在创建地图后设置样式ID

     ```
     1. @Entry
     2. @Component
     3. struct CustomMapStyleDemo {
     4. private TAG = "CustomMapStyleDemo";
     5. private mapOptions?: mapCommon.MapOptions;
     6. private mapController?: map.MapComponentController;
     7. private callback?: AsyncCallback<map.MapComponentController>;

     9. aboutToAppear(): void {
     10. // 地图初始化参数
     11. this.mapOptions = {
     12. position: {
     13. target: {
     14. latitude: 31.984410259206815,
     15. longitude: 118.76625379397866
     16. },
     17. zoom: 15
     18. }
     19. };
     20. this.callback = async (err, mapController) => {
     21. if (!err) {
     22. this.mapController = mapController;
     23. // 自定义样式参数，styleId需要替换为您自己的样式ID或者预览ID，样式ID或者预览ID可在Petal Maps Studio平台上创建
     24. let param: mapCommon.CustomMapStyleOptions = {
     25. styleId: "XXX"
     26. };
     27. // 设置自定义样式
     28. await this.mapController.setCustomMapStyle(param).then(() => {
     29. console.info(this.TAG + `setCustomMapStyle OK`);
     30. }).catch((error: BusinessError) => {
     31. console.error(this.TAG + `Failed in getting CustomMapStyle, code is：${error.code},message is ${error.message}`);
     32. })
     33. } else {
     34. console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
     35. }
     36. };
     37. }

     39. build() {
     40. Stack() {
     41. Column() {
     42. MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback });
     43. }.width('100%')
     44. }.height('100%')
     45. }
     46. }
     ```
   * 在初始化地图时设置样式ID

     ```
     1. @Entry
     2. @Component
     3. struct CustomMapStyleDemo {
     4. private mapOptions?: mapCommon.MapOptions;
     5. private mapController?: map.MapComponentController;
     6. private callback?: AsyncCallback<map.MapComponentController>;

     8. aboutToAppear(): void {
     9. // 地图初始化参数
     10. this.mapOptions = {
     11. position: {
     12. target: {
     13. latitude: 31.984410259206815,
     14. longitude: 118.76625379397866
     15. },
     16. zoom: 15
     17. },
     18. // 自定义样式参数，styleId需要替换为您自己的样式ID或者预览ID，样式ID或者预览ID可在Petal Maps Studio平台上创建
     19. styleId: "XXX"
     20. };
     21. this.callback = async (err, mapController) => {
     22. if (!err) {
     23. this.mapController = mapController;
     24. } else {
     25. console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
     26. }
     27. };
     28. }

     30. build() {
     31. Stack() {
     32. Column() {
     33. MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback });
     34. }.width('100%')
     35. }.height('100%')
     36. }
     37. }
     ```

     设置样式ID之后效果如下：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/Nv75yTCDSOevfzKNyEoGYA/zh-cn_image_0000002589325389.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053859Z&HW-CC-Expire=86400&HW-CC-Sign=D37BF86F62C226C8ACFE9567482DE7ACB0A3B35C28B16FEC4A5252EB63449AE7 "点击放大")

### 设置样式内容

1. 导入相关模块。

   ```
   1. import { MapComponent, mapCommon, map } from '@kit.MapKit';
   2. import { AsyncCallback } from '@kit.BasicServicesKit';
   ```
2. 设置样式内容。

   ```
   1. @Entry
   2. @Component
   3. struct CustomMapStyleDemo {
   4. private mapOptions?: mapCommon.MapOptions;
   5. private mapController?: map.MapComponentController;
   6. private callback?: AsyncCallback<map.MapComponentController>;

   8. aboutToAppear(): void {
   9. // 地图初始化参数
   10. this.mapOptions = {
   11. position: {
   12. target: {
   13. latitude: 31.984410259206815,
   14. longitude: 118.76625379397866
   15. },
   16. zoom: 15
   17. }
   18. };
   19. this.callback = async (err, mapController) => {
   20. if (!err) {
   21. this.mapController = mapController;
   22. // 自定义样式参数
   23. let param: mapCommon.CustomMapStyleOptions = {
   24. styleContent: `[{
   25. "mapFeature": "landcover.natural",
   26. "options": "geometry.fill",
   27. "paint": {
   28. "color": "#8FBC8F"
   29. }},
   30. {
   31. "mapFeature": "water",
   32. "options": "geometry.fill",
   33. "paint": {
   34. "color": "#4682B4"
   35. }}]`
   36. };
   37. // 设置自定义样式
   38. await this.mapController.setCustomMapStyle(param);
   39. } else {
   40. console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
   41. }
   42. };
   43. }

   45. build() {
   46. Stack() {
   47. Column() {
   48. MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback });
   49. }.width('100%')
   50. }.height('100%')
   51. }
   52. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/q9NZTsC0TFyYcayE6-La0g/zh-cn_image_0000002589245327.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053859Z&HW-CC-Expire=86400&HW-CC-Sign=56FB56B7A6D13682B6D251A0839280B9972AFC97497CA132A6F26CFB7D0F0FAE "点击放大")

### 样式参考

自定义地图样式JSON内容通过下列4个元素来定义地图样式：

* mapFeature：地图要素
* options：元素选项

  + geometry.fill：几何填充
  + geometry.stroke：几何描边
  + geometry.icon：几何图标
  + labels.text.fill：文本填充
  + labels.text.stroke：文本描边
* paint：绘制属性

  + color：颜色，16进制颜色，例如“#FFFF00”
  + weight：线条宽度。整型值，[1, 24]，默认为1，大于1表示加宽
  + icon-type：图标类型，目前支持night、simple、standard
* visibility：可见属性，默认为可见

  + true：可见
  + false：不可见

下列各表将向您展示支持修改的地图元素。

说明

* 图标类型icon-type支持范围为：standard/night/simple。

1. All

   All代表全部，即所有类别的集合，支持能力范围同其他所有列表，All仅可调整visibility（可见属性）。
2. Administrative

   | **元素类型**  **Feature type** | **填充颜色**  **Geometry.**  **fill.**  **color** | **填充宽度**  **Geometry.**  **fill.**  **weight** | **描边颜色**  **Geometry.**  **stroke.**  **color** | **描边宽度**  **Geometry.**  **stroke.**  **weight** | **填充颜色**  **Labels.**  **fill.**  **color** | **文本大小**  **Labels.**  **fill.**  **weight** | **描边颜色**  **Labels.**  **stroke.**  **color** | **描边大小**  **Labels.**  **stroke.**  **weight** | **图标类型**  **Icon.**  **icon-type** |
   | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
   | Capital  首都 | - | - | - | - |  |  |  |  |  |
   | Country  国家 |  |  |  |  |  |  |  |  | - |
   | District  区/县 | - | - | - | - |  |  |  |  |  |
   | Locality  乡村、城镇 | - | - | - | - |  |  |  |  |  |
   | Major-city  1-4级城市 | - | - | - | - |  |  |  |  |  |
   | Province  省 |  |  |  |  |  |  |  |  | - |
3. Landcover

   | 元素类型  Feature type | 填充颜色  Geometry.  fill.  color | 描边颜色  Geometry.  stroke.  color | 填充颜色  Labels.  fill.  color | 文本大小  Labels.  fill.  weight | 描边颜色  Labels.  stroke.  color | 描边大小  Labels.  stroke.  weight |
   | --- | --- | --- | --- | --- | --- | --- |
   | Attraction  游乐场、动植物园等 |  | - |  |  |  |  |
   | Business  购物中心、商业区等 |  | - |  |  |  |  |
   | College  学校 |  | - |  |  |  |  |
   | Hospital  医院 |  | - |  |  |  |  |
   | Human-made  聚集区、小区、工业区、监狱地面等 |  |  |  |  |  |  |
   | Human-made  建筑物 |  |  | - | - | - | - |
   | Natural  陆地、岛屿、海滩、冰川等 |  | - |  |  |  |  |
   | Parkland  森林、公园、荒地、高尔夫球场等 |  | - |  |  |  |  |
4. Poi

   | 元素类型  Feature type | 填充颜色  Labels.  fill.  color | 文本大小  Labels.  fill.  weight | 描边颜色  Labels.  stroke.  color | 描边大小  Labels.  stroke.  weight | 图标类型  Icon.  icon-type |
   | --- | --- | --- | --- | --- | --- |
   | Airport  飞机场 |  |  |  |  |  |
   | Automotive  汽修、充电桩、洗车等 |  |  |  |  |  |
   | Beauty  美容中心 |  |  |  |  |  |
   | Business  公司、商业楼等 |  |  |  |  |  |
   | Eating&drinking  饮食快餐 |  |  |  |  |  |
   | Health-care  医院、诊所、药店等 |  |  |  |  |  |
   | Leisure  休闲娱乐 |  |  |  |  |  |
   | Lodging  酒店、住宿点 |  |  |  |  |  |
   | Miscellaneous  自然地物 |  |  |  |  |  |
   | Natural  山峰、森林等 |  |  |  |  |  |
   | Public-service  医院、诊所、药店等 |  |  |  |  |  |
   | Railway  铁路 |  |  |  |  |  |
   | Shopping  购物中心、市场等 |  |  |  |  |  |
   | Sports-outdoor  户外运动、爬山、骑车等 |  |  |  |  |  |
   | Tourism  旅游景点、历史遗迹、教堂等 |  |  |  |  |  |
5. Road

   | 元素类型  Feature type | 填充颜色  Geometry.  fill.  color | 填充宽度  Geometry.  fill.  weight | 描边颜色  Geometry.  stroke.  color | 描边宽度  Geometry.  stroke.  weight | 填充颜色  Labels.  fill.  color | 文本大小  Labels.  fill.  weight | 描边颜色  Labels.  stroke.  color | 描边大小  Labels.  stroke.  weight | 图标类型  Icon.  icon-type |
   | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
   | City-arterial  城市主干道 |  |  |  |  |  |  |  |  |  |
   | Highway  城市高速 |  |  |  |  |  |  |  |  |  |
   | Minor-road  市区内支线等 |  |  |  |  |  |  |  |  | - |
   | National  国道 |  |  |  |  |  |  |  |  |  |
   | Province  省道 |  |  |  |  |  |  |  |  |  |
   | Sidewalk  人行道 |  |  |  |  |  |  |  |  | - |
6. Trafficinfo

   | 元素类型  Feature type | 填充颜色  Geometry.  fill.  color | 填充颜色  Labels.  fill.  color | 文本大小  Labels.  fill.  weight |
   | --- | --- | --- | --- |
   | Closed  封路 |  |  |  |
7. Transit

   | 元素类型  Feature type | 填充颜色  Geometry.  fill.  color | 填充宽度  Geometry.  fill.  weight | 描边颜色  Geometry.  stroke.  color | 描边宽度  Geometry.  stroke.  weight | 填充颜色  Labels.  fill.  color | 文本大小  Labels.  fill.  weight | 描边颜色  Labels.  stroke.  color | 描边大小  Labels.  stroke.  weight | 图标类型  Icon.  icon-type |
   | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
   | Airport  机场 |  | - | - | - |  |  |  |  |  |
   | Airport Runway  机场跑道 |  |  |  |  | - | - | - | - | - |
   | Airport Runway Taxiway  机场跑道滑行道 |  |  |  |  | - | - | - | - | - |
   | Bus  公交 | - | - | - | - |  |  |  |  |  |
   | Ferry-line  航线 |  | - | - | - |  |  |  |  | - |
   | Ferry-terminal  港口 |  | - | - | - |  |  |  |  |  |
   | Other  出租车、  出入口等 | - | - | - | - |  |  |  |  |  |
   | Rail-station  火车站、  高铁站 |  | - | - | - |  |  |  |  |  |
   | Railway  铁路线、  高铁线 |  |  |  |  | - | - | - | - | - |
   | Subway  地铁 |  |  |  |  |  |  |  |  |  |
   | Traffic\_light  交通灯 | - | - | - | - | - | - | - | - |  |
8. Water

   | 元素类型  Feature type | 填充颜色  Geometry.  fill.  color | 填充颜色  Labels.  fill.  color | 文本大小  Labels.  fill.  weight |
   | --- | --- | --- | --- |
   | Ocean  水系、海洋、湖泊、河流 |  |  |  |
