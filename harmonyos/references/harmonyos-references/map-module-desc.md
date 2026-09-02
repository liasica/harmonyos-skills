---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-module-desc
title: 模块描述
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > 模块描述
category: harmonyos-references
scraped_at: 2026-09-02T15:02:58+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b2ca5bd776c520ae580328d3d25d8b7d45590e5b3adb911ac1a482d3c3fe2bec
---

Map Kit支持显示地图、在地图上绘制各类覆盖物（标记、折线、弧线、多边形、圆形等）、添加动画效果、处理地图交互事件、更新地图状态等。

**典型使用场景：**

* 在应用界面中嵌入互动式地图
* 展示地理位置标记和路线信息
* 实现基于位置的服务（LBS）功能
* 创建室内地图导航体验

## 关键Class/Interface介绍

### 核心组件

| Class/Interface | 说明 |
| --- | --- |
| **[MapComponent](map-mapcomponent.md)** | 地图UI组件，通过回调返回MapComponentController |
| **[MapComponentController](map-map-mapcomponentcontroller.md)** | 地图主控制器，所有地图操作的主入口 |
| **[MapEventManager](map-map-mapeventmanager.md)** | 地图事件监听管理器 |
| **[BaseOverlay](map-map-baseoverlay.md)** | 覆盖物基础类，所有覆盖物继承自此类 |

### 覆盖物体系

| Class/Interface | 说明 |
| --- | --- |
| **[Marker](map-map-marker.md)** | 标记 |
| **[MapPolyline](map-map-mappolyline.md)** | 折线 |
| **[MapArc](map-map-maparc.md)** | 弧线 |
| **[MapPolygon](map-map-mappolygon.md)** | 多边形 |
| **[MapCircle](map-map-mapcircle.md)** | 圆形 |
| **[PointAnnotation](map-map-pointannotation.md)** | 点注释 |
| **[Bubble](map-map-bubble.md)** | 气泡 |
| **[ClusterOverlay](map-map-clusteroverlay.md)** | 点聚合 |
| **[ImageOverlay](map-map-imageoverlay.md)** | 图片覆盖物 |
| **[BuildingOverlay](map-map-buildingoverlay.md)** | 3D建筑 |
| **[TraceOverlay](map-map-traceoverlay.md)** | 动态轨迹 |
| **[TileOverlay](map-map-tileoverlay.md)** | 瓦片图层 |
| **[Heatmap](map-map-heatmap.md)** | 热力图 |
| **[MvtOverlay](map-map-mvtoverlay.md)** | 矢量图层 |
| **[FlowFieldOverlay](map-map-flowfieldoverlay.md)** | 流场图层 |
| **[MassPointOverlay](map-map-masspointoverlay.md)** | 海量点图层 |

### 动画体系

| Class/Interface | 说明 |
| --- | --- |
| **[Animation](map-map-animation.md)** | 动画抽象基类 |
| **[AlphaAnimation](map-map-alphaanimation.md)** | 透明度动画 |
| **[RotateAnimation](map-map-rotateanimation.md)** | 旋转动画 |
| **[ScaleAnimation](map-map-scaleanimation.md)** | 缩放动画 |
| **[TranslateAnimation](map-map-translateanimation.md)** | 位移动画 |
| **[FontSizeAnimation](map-map-fontsizeanimation.md)** | 字体大小动画 |
| **[PlayImageAnimation](map-map-playimageanimation.md)** | 帧动画 |
| **[AnimationSet](map-map-animationset.md)** | 动画集合 |

### 数据模型

| Class/Interface | 说明 |
| --- | --- |
| **[MapOptions](map-common.md#mapoptions)** | 地图初始化参数 |
| **[LatLng](map-common.md#latlng)** | 经纬度坐标 |
| **[CameraPosition](map-common.md#cameraposition)** | 相机位置状态 |
| **[LatLngBounds](map-common.md#latlngbounds)** | 经纬度边界矩形 |

## API组合使用关系说明

### 地图初始化与显示

使用MapComponent显示地图需要完成以下步骤：

```typescript
// 1. 导入模块
import { map, mapCommon, MapComponent } from '@kit.MapKit';

// 2. 创建地图初始化参数
let mapOptions: mapCommon.MapOptions = {
  position: {
    target: { latitude: 39.9, longitude: 116.4 },
    zoom: 10
  }
};

// 3. 定义回调函数获取MapComponentController
let mapCallback = async (err, mapController) => {
  if (!err) {
    // 获取控制器成功后，可进行后续操作
    let mapController = mapController;
    let mapEventManager = mapController.getEventManager();
  }
};

// 4. 在UI中使用MapComponent
MapComponent({
  mapOptions: mapOptions,
  mapCallback: mapCallback
})
```

### 添加覆盖物流程

```typescript
// 1. 创建覆盖物配置参数
let markerOptions: mapCommon.MarkerOptions = {
  position: { latitude: 39.9, longitude: 116.4 },
  clickable: true,
  title: "标记标题"
};

// 2. 通过MapComponentController添加覆盖物
let marker = await mapController.addMarker(markerOptions);

// 3. 可对覆盖物进行进一步操作
marker.setTitle("新标题");
marker.showInfoWindow();
```

### 地图动画与交互

```typescript
// 1. 获取MapEventManager
let mapEventManager = mapController.getEventManager();

// 2. 订阅地图事件
mapEventManager.on("mapLoad", () => {
  console.info("地图加载完成");
});

// 3. 创建CameraUpdate并执行动画
let cameraUpdate = map.newCameraPosition({
  target: { latitude: 40.0, longitude: 117.0 },
  zoom: 12
});
mapController.animateCamera(cameraUpdate, 1000);
```

### 动画使用

```typescript
// 1. 创建动画实例
let animation = new map.RotateAnimation(0, 270);

// 2. 配置动画参数
animation.setDuration(2000);
animation.setRepeatCount(map.AnimationRepeatMode.RESTART);

// 3. 订阅动画事件
animation.on("animationStart", () => {});
animation.on("animationEnd", () => {});

// 4. 对覆盖物应用动画
marker.startAnimation(animation);
```
