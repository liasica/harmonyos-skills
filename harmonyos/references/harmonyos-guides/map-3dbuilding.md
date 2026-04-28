---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-3dbuilding
title: 3D建筑
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 在地图上绘制 > 3D建筑
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1c090a72739c1e6f1c118e2466e618f74edab3337d3d11594165f0c0abd7d4b7
---

## 场景介绍

本章节将向您介绍如何在地图上绘制3D建筑。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/FCH0gbjjSdGaB7eUITxGGA/zh-cn_image_0000002583479043.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234950Z&HW-CC-Expire=86400&HW-CC-Sign=A52627B3B2358EF8EB15BDE91CDDA6A40BCCE4F222CF627F3E2A10EAB06A0510 "点击放大")

## 接口说明

添加3D建筑功能主要由[BuildingOverlayParams](../harmonyos-references/map-common.md#buildingoverlayparams)、[addBuildingOverlay](../harmonyos-references/map-map-mapcomponentcontroller.md#addbuildingoverlay)和[BuildingOverlay](../harmonyos-references/map-map-buildingoverlay.md)提供，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-map-buildingoverlay.md)。

| 接口名 | 描述 |
| --- | --- |
| [BuildingOverlayParams](../harmonyos-references/map-common.md#buildingoverlayparams) | 3D建筑参数。 |
| [addBuildingOverlay](../harmonyos-references/map-map-mapcomponentcontroller.md#addbuildingoverlay)(params: [mapCommon.BuildingOverlayParams](../harmonyos-references/map-common.md#buildingoverlayparams)): Promise<[BuildingOverlay](../harmonyos-references/map-map-buildingoverlay.md)> | 在地图上添加3D建筑。 |
| [BuildingOverlay](../harmonyos-references/map-map-buildingoverlay.md) | 3D建筑，支持更新和查询相关属性。 |

## 开发步骤

### 添加3D建筑

1. 导入相关模块。

   ```
   1. import { mapCommon, map, MapComponent } from '@kit.MapKit';
   2. import { AsyncCallback } from '@kit.BasicServicesKit';
   ```
2. 添加3D建筑。

   ```
   1. @Entry
   2. @Component
   3. struct BuildingOverlayDemo {
   4. private TAG = "OHMapSDK_BuildingOverlayDemo";
   5. private mapOptions?: mapCommon.MapOptions;
   6. private mapController?: map.MapComponentController;
   7. private callback?: AsyncCallback<map.MapComponentController>;
   8. private buildingOverlay?: map.BuildingOverlay;

   10. aboutToAppear(): void {
   11. // 初始化地图参数
   12. this.mapOptions = {
   13. position: {
   14. target: {
   15. latitude: 31.984794,
   16. longitude: 118.765865
   17. },
   18. zoom: 18
   19. },
   20. scaleControlsEnabled: true
   21. }

   23. this.callback = async (err, mapController) => {
   24. console.info(this.TAG, "addBuildingOverlay");
   25. if (!err) {
   26. this.mapController = mapController;
   27. let points: Array<mapCommon.LatLng> = [
   28. {
   29. latitude: 31.984794,
   30. longitude: 118.765865
   31. },
   32. {
   33. latitude: 31.98468,
   34. longitude: 118.766076
   35. },
   36. {
   37. latitude: 31.98472,
   38. longitude: 118.766116
   39. },
   40. {
   41. latitude: 31.98463,
   42. longitude: 118.766292
   43. },
   44. {
   45. latitude: 31.984586,
   46. longitude: 118.766251
   47. },
   48. {
   49. latitude: 31.984536,
   50. longitude: 118.766344
   51. },
   52. {
   53. latitude: 31.984633,
   54. longitude: 118.766446
   55. },
   56. {
   57. latitude: 31.9848,
   58. longitude: 118.766285
   59. },
   60. {
   61. latitude: 31.984925,
   62. longitude: 118.766312
   63. },
   64. {
   65. latitude: 31.985282,
   66. longitude: 118.766661
   67. },
   68. {
   69. latitude: 31.985438,
   70. longitude: 118.766419
   71. },
   72. {
   73. latitude: 31.985801,
   74. longitude: 118.766755
   75. },
   76. {
   77. latitude: 31.985856,
   78. longitude: 118.766504
   79. },
   80. {
   81. latitude: 31.985785,
   82. longitude: 118.766434
   83. },
   84. {
   85. latitude: 31.985821,
   86. longitude: 118.766278
   87. },
   88. {
   89. latitude: 31.985897,
   90. longitude: 118.766311
   91. },
   92. {
   93. latitude: 31.985944,
   94. longitude: 118.766095
   95. },
   96. {
   97. latitude: 31.985909,
   98. longitude: 118.766069
   99. },
   100. {
   101. latitude: 31.985794,
   102. longitude: 118.765989
   103. },
   104. {
   105. latitude: 31.9857,
   106. longitude: 118.766029
   107. },
   108. {
   109. latitude: 31.985658,
   110. longitude: 118.766164
   111. },
   112. {
   113. latitude: 31.985647,
   114. longitude: 118.766271
   115. },
   116. {
   117. latitude: 31.985574,
   118. longitude: 118.766297
   119. },
   120. {
   121. latitude: 31.985458,
   122. longitude: 118.766285
   123. },
   124. {
   125. latitude: 31.985271,
   126. longitude: 118.766002
   127. },
   128. {
   129. latitude: 31.985219,
   130. longitude: 118.766002
   131. },
   132. {
   133. latitude: 31.985135,
   134. longitude: 118.766029
   135. },
   136. {
   137. latitude: 31.985093,
   138. longitude: 118.766083
   139. },
   140. {
   141. latitude: 31.985019,
   142. longitude: 118.766109
   143. },
   144. {
   145. latitude: 31.984978,
   146. longitude: 118.766083
   147. },
   148. {
   149. latitude: 31.984794,
   150. longitude: 118.765865
   151. }
   152. ];
   153. points.reverse();
   154. // 3D建筑参数
   155. let buildingOverlayOptions: mapCommon.BuildingOverlayParams =
   156. {
   157. // 3D建筑的范围参数（点为顺时针绘制）
   158. points: points,
   159. // 3D建筑的高度
   160. totalHeight: 51,
   161. // 3D建筑的选中楼层高度
   162. floorBottomHeight: 33,
   163. // 3D建筑的顶部颜色
   164. topFaceColor: 0xffa4b8f7,
   165. // 3D建筑的侧面颜色
   166. sideFaceColor: 0x44a4b8f7,
   167. // 3D建筑的选中楼层颜色
   168. floorColor: 0xff000000,
   169. // 3D建筑的展示层级
   170. showLevel: 14,
   171. // 3D建筑选中楼层从底部升起的动画时长
   172. animationDuration: 5000,
   173. // 3D建筑侧面的纹理，需要替换您自己的资源图片，存放在resources/base/media目录下
   174. sideTexture: { image: $r("app.media.side_tex"), height: 3, width: 3 },
   175. // 3D建筑选中楼层的纹理，需要替换您自己的资源图片，存放在resources/base/media目录下
   176. floorTexture: { image: $r("app.media.floor_tex"), height: 3, width: 3 }
   177. };
   178. let cameraUpdate = map.newCameraPosition({
   179. target: {
   180. latitude: 31.984794,
   181. longitude: 118.765865
   182. },
   183. zoom: 18,
   184. tilt: 70
   185. });
   186. // 将地图镜头移动到3D建筑区域
   187. this.mapController?.moveCamera(cameraUpdate);
   188. // 新建3D建筑
   189. try {
   190. this.buildingOverlay = await this.mapController?.addBuildingOverlay(buildingOverlayOptions);
   191. } catch (e) {
   192. console.error(`Failed to create the buildingOverlay, code is：${e.code}, message is ${e.message}`);
   193. }
   194. } else {
   195. console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
   196. }
   197. }
   198. }

   200. build() {
   201. Stack() {
   202. Column() {
   203. MapComponent({
   204. mapOptions: this.mapOptions,
   205. mapCallback: this.callback,
   206. }).width('100%').height('100%');
   207. }.width('100%')
   208. }.height('100%')
   209. }
   210. }
   ```
