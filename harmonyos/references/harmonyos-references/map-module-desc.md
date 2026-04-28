---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-module-desc
title: 模块描述
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > 模块描述
category: harmonyos-references
scraped_at: 2026-04-28T08:17:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c84788dec8e8b410385604d3ae6ae46603bfa99a77b4d01d6417172ccc43abbe
---

map（地图显示功能）为开发者提供易于上手的接口，开发者可以通过相关接口便捷地在HarmonyOS应用/元服务中加入地图相关的功能，包括显示地图、在地图上绘制（覆盖物）、添加动画、与地图交互、更新地图状态、常用工具函数等功能。

该模块提供以下地图常用功能：

* [MapComponentController](map-map-mapcomponentcontroller.md)：显示地图，与地图有关的所有方法从此处接入。

地图覆盖物：

* [Marker](map-map-marker.md)：标记。
* [MapPolyline](map-map-mappolyline.md)：折线。
* [MapArc](map-map-maparc.md)：弧线。
* [MapPolygon](map-map-mappolygon.md)：多边形。
* [MapCircle](map-map-mapcircle.md)：圆形。
* [PointAnnotation](map-map-pointannotation.md)：点注释。
* [Bubble](map-map-bubble.md)：气泡。
* [ClusterOverlay](map-map-clusteroverlay.md)：点聚合。
* [ImageOverlay](map-map-imageoverlay.md)：图片覆盖物。
* [BuildingOverlay](map-map-buildingoverlay.md)：3D建筑。
* [TraceOverlay](map-map-traceoverlay.md)：动态轨迹。
* [TileOverlay](map-map-tileoverlay.md)：瓦片图层。
* [Heatmap](map-map-heatmap.md)：热力图。
* [MvtOverlay](map-map-mvtoverlay.md)：矢量图层。
* [FlowFieldOverlay](map-map-flowfieldoverlay.md)：流场图层。
* [MassPointOverlay](map-map-masspointoverlay.md)：海量点图层。

添加动画：

* [Animation](map-map-animation.md)：动画抽象类。
* [AlphaAnimation](map-map-alphaanimation.md)：控制透明度的动画类。
* [RotateAnimation](map-map-rotateanimation.md)：控制旋转的动画类。
* [ScaleAnimation](map-map-scaleanimation.md)：控制缩放的动画类。
* [TranslateAnimation](map-map-translateanimation.md)：控制移动的动画类。
* [FontSizeAnimation](map-map-fontsizeanimation.md)：控制字体大小的动画类。
* [PlayImageAnimation](map-map-playimageanimation.md)：控制多张图片的帧动画类。
* [AnimationSet](map-map-animationset.md)：动画类集合。

与地图交互：

* [MapEventManager](map-map-mapeventmanager.md)：地图监听事件管理器。

更新地图状态：

* [newLatLng](map-map-newlatlng.md)：设置地图的中心点和缩放层级。
* [newLatLngBounds](map-map-newlatlngbounds.md)：设置地图经纬度范围、地图区域和边界之间的距离。
* [scrollBy](map-map-scrollby.md)：按像素移动地图中心点。
* [zoomBy](map-map-zoomby.md)：根据给定增量并以给定的屏幕像素点为中心点缩放地图级别。
* [zoomIn](map-map-zoomin.md)：放大地图缩放级别，在当前地图显示的级别基础上加1。
* [zoomOut](map-map-zoomout.md)：缩小地图缩放级别，在当前地图显示的级别基础上减1。
* [zoomTo](map-map-zoomto.md)：设置地图缩放级别。

常用工具函数：

* [calculateDistance](map-map-calculatedistance.md)：计算坐标点之间的距离。
* [convertCoordinate](map-map-convertcoordinate.md)：坐标系转换，使用Promise异步回调。
* [convertCoordinateSync](map-map-convertcoordinatesync.md)：坐标系转换。
* [rectifyCoordinate](map-map-rectifycoordinate.md)：根据用户输入的坐标系和坐标以及获取当前的路由地，判断是否需要修正坐标。

## 导入模块

```
1. import { map } from '@kit.MapKit';
```
