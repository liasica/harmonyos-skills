---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-annotation
title: 点注释
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 在地图上绘制 > 点注释
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:44f0b2f3dec8aba91166b9be5bb390b6bfed0e8a77b5440a3004d57037e4641d
---

## 场景介绍

本章节将向您介绍如何在地图的指定位置添加点注释以标识位置、商家、建筑等，并可以通过信息窗口展示详细信息。

点注释支持功能：

* 支持设置图标、文字、碰撞规则等。
* 支持添加点击事件。

[PointAnnotation](../harmonyos-references/map-map-pointannotation.md)有默认风格，同时也支持自定义。由于内容丰富，以下只展示一些基础功能的使用，详细内容可参见[接口文档](../harmonyos-references/map-map-pointannotation.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/5fQiU1E5SYeF26a0aDWMGg/zh-cn_image_0000002583479039.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234949Z&HW-CC-Expire=86400&HW-CC-Sign=782CF2AD2557E967616BB44102C563FF3E8357F41FFD4CDE0F1C0CAFD5EA0669 "点击放大")

## 接口说明

添加点注释功能主要由[PointAnnotationParams](../harmonyos-references/map-common.md#pointannotationparams)、[addPointAnnotation](../harmonyos-references/map-map-mapcomponentcontroller.md#addpointannotation)、[PointAnnotation](../harmonyos-references/map-map-pointannotation.md)、[on](../harmonyos-references/map-map-mapeventmanager.md#onpointannotationclick)、[off](../harmonyos-references/map-map-mapeventmanager.md#offpointannotationclick)提供，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-map-pointannotation.md)。

| 接口名 | 描述 |
| --- | --- |
| [PointAnnotationParams](../harmonyos-references/map-common.md#pointannotationparams) | 点注释参数。 |
| [addPointAnnotation](../harmonyos-references/map-map-mapcomponentcontroller.md#addpointannotation)(params: [mapCommon.PointAnnotationParams](../harmonyos-references/map-common.md#pointannotationparams)): Promise<[PointAnnotation](../harmonyos-references/map-map-pointannotation.md)> | 在地图上添加点注释。 |
| [PointAnnotation](../harmonyos-references/map-map-pointannotation.md) | 点注释，支持更新和查询相关属性。 |
| [on](../harmonyos-references/map-map-mapeventmanager.md#onpointannotationclick)(type: 'pointAnnotationClick', callback: Callback<[PointAnnotation](../harmonyos-references/map-map-pointannotation.md)>): void | 设置点注释点击事件监听器。 |
| [off](../harmonyos-references/map-map-mapeventmanager.md#offpointannotationclick)(type: 'pointAnnotationClick', callback?: Callback<[PointAnnotation](../harmonyos-references/map-map-pointannotation.md)>): void | 取消监听点注释点击事件。 |

## 开发步骤

### 添加点注释

1. 导入相关模块。

   ```
   1. import { MapComponent, mapCommon, map } from '@kit.MapKit';
   2. import { AsyncCallback } from '@kit.BasicServicesKit';
   ```
2. 添加点注释，在callback方法中创建初始化参数并新建点注释。

   ```
   1. @Entry
   2. @Component
   3. struct PointAnnotationDemo {
   4. private mapOptions?: mapCommon.MapOptions;
   5. private mapController?: map.MapComponentController;
   6. private callback?: AsyncCallback<map.MapComponentController>;
   7. private mapEventManager?: map.MapEventManager;
   8. private pointAnnotation?: map.PointAnnotation;
   9. aboutToAppear(): void {
   10. this.mapOptions = {
   11. position: {
   12. target: {
   13. latitude: 32.020750,
   14. longitude: 118.788765
   15. },
   16. zoom: 14
   17. }
   18. };
   19. this.callback = async (err, mapController) => {
   20. if (!err) {
   21. this.mapController = mapController;
   22. this.mapEventManager = this.mapController.getEventManager();
   23. let pointAnnotationOptions: mapCommon.PointAnnotationParams = {
   24. // 定义点注释图标锚点
   25. position: {
   26. latitude: 32.020750,
   27. longitude: 118.788765
   28. },
   29. // 定义点注释名称与地图POI名称相同时，是否支持去重
   30. repeatable: true,
   31. // 定义点注释的碰撞规则
   32. collisionRule: mapCommon.CollisionRule.NAME,
   33. // 定义点注释的标题，数组长度最小为1，最大为3
   34. titles: [{
   35. // 定义标题内容
   36. content: "南京夫子庙",
   37. // 定义标题字体颜色
   38. color: 0xFF000000,
   39. // 定义标题字体大小
   40. fontSize: 15,
   41. // 定义标题描边颜色
   42. strokeColor: 0xFFFFFFFF,
   43. // 定义标题描边宽度
   44. strokeWidth: 2,
   45. // 定义标题字体样式
   46. fontStyle: mapCommon.FontStyle.ITALIC
   47. }],
   48. // 定义点注释的图标，图标存放在resources/rawfile
   49. icon: "",
   50. // 定义点注释是否展示图标
   51. showIcon: true,
   52. // 定义点注释的锚点在水平方向上的位置
   53. anchorU: 0.5,
   54. // 定义点注释的锚点在垂直方向上的位置
   55. anchorV: 1,
   56. // 定义点注释的显示属性，为true时，在被碰撞后仍能显示
   57. forceVisible: false,
   58. // 定义碰撞优先级，数值越大，优先级越低
   59. priority: 3,
   60. // 定义点注释展示的最小层级
   61. minZoom: 2,
   62. // 定义点注释展示的最大层级
   63. maxZoom: 20,
   64. // 定义点注释是否可见
   65. visible: true,
   66. // 定义点注释叠加层级属性
   67. zIndex: 10
   68. }

   70. // 创建pointAnnotation
   71. try {
   72. this.pointAnnotation = await this.mapController.addPointAnnotation(pointAnnotationOptions);
   73. } catch (e) {
   74. console.error(`Failed to create the pointAnnotation, code is：${e.code}, message is ${e.message}`);
   75. }
   76. } else {
   77. console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
   78. }
   79. };
   80. }
   81. build() {
   82. Stack() {
   83. Column() {
   84. MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback });
   85. }.width('100%')
   86. }.height('100%')
   87. }
   88. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/RaB7-UsUS12UIQ-7BHDlJg/zh-cn_image_0000002552799390.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234949Z&HW-CC-Expire=86400&HW-CC-Sign=C4FED5FF541E682FE3665054815E00801F2CC29469C56B227E11E61BBE54547E "点击放大")
3. 在添加点注释之后，修改已经设置的点注释属性。

   ```
   1. // 设置点注释的显示层级为3~14级
   2. this.pointAnnotation.setZoom(3,14);
   3. // 设置点注释的碰撞优先级为10
   4. this.pointAnnotation.setPriority(10);
   ```

### 设置监听点注释点击事件

```
1. let callback = (pointAnnotation: map.PointAnnotation) => {
2. console.info("pointAnnotationClick", `pointAnnotationClick: ${pointAnnotation.getId()}`);
3. };
4. this.mapEventManager.on("pointAnnotationClick", callback);
```

### 点注释动画

使用[PointAnnotation](../harmonyos-references/map-map-pointannotation.md)的[setAnimation](../harmonyos-references/map-map-basepriorityoverlay.md#setanimation)方法设置动画。

调用[PointAnnotation](../harmonyos-references/map-map-pointannotation.md)的[startAnimation](../harmonyos-references/map-map-basepriorityoverlay.md#startanimation)方法启动动画。

```
1. let animation: map.ScaleAnimation = new map.ScaleAnimation(1, 3, 1, 3);
2. // 设置动画单次的时长
3. animation.setDuration(3000);
4. // 设置动画开始监听
5. let callbackStart = () => {
6. console.info("animationStart", `callback`);
7. };
8. animation.on("animationStart", callbackStart);
9. // 设置动画结束监听
10. let callbackEnd = () => {
11. console.info("animationEnd", `callback`);
12. };
13. animation.on("animationEnd", callbackEnd);
14. // 设置动画执行完成的状态
15. animation.setFillMode(map.AnimationFillMode.BACKWARDS);
16. // 设置动画重复的方式
17. animation.setRepeatMode(map.AnimationRepeatMode.REVERSE);
18. // 设置动画插值器
19. animation.setInterpolator(Curve.Linear);
20. // 设置动画的重复次数
21. animation.setRepeatCount(100);
22. this.pointAnnotation.setAnimation(animation);
23. this.pointAnnotation.startAnimation();
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/bQRkx3WQS8maKf0Nn0VkdA/zh-cn_image_0000002583439085.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234949Z&HW-CC-Expire=86400&HW-CC-Sign=F2F859CA126D72FD080A7A98AB5DB9CF844ADEC3663D3B98049DAF3F896FD9C0 "点击放大")

### 点注释标题动画

使用[PointAnnotation](../harmonyos-references/map-map-pointannotation.md)的[setTitleAnimation](../harmonyos-references/map-map-pointannotation.md#settitleanimation)方法设置标题动画。

调用[PointAnnotation](../harmonyos-references/map-map-pointannotation.md)的[startTitleAnimation](../harmonyos-references/map-map-pointannotation.md#starttitleanimation)方法启动标题动画。

```
1. let animation: map.FontSizeAnimation = new map.FontSizeAnimation(15, 45);
2. // 设置动画单次的时长
3. animation.setDuration(3000);
4. // 设置动画开始监听
5. let callbackStart = () => {
6. console.info("animationStart", `callback`);
7. };
8. animation.on("animationStart", callbackStart);
9. // 设置动画结束监听
10. let callbackEnd = () => {
11. console.info("animationEnd", `callback`);
12. };
13. animation.on("animationEnd", callbackEnd);
14. // 设置动画执行完成的状态
15. animation.setFillMode(map.AnimationFillMode.FORWARDS);
16. // 设置动画重复的方式
17. animation.setRepeatMode(map.AnimationRepeatMode.REVERSE);
18. // 设置动画插值器
19. animation.setInterpolator(Curve.Linear);
20. // 设置动画的重复次数
21. animation.setRepeatCount(100);
22. this.pointAnnotation.setTitleAnimation(animation);
23. this.pointAnnotation.startTitleAnimation();
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/hwFdD4R_R9KCwwbN9OegwA/zh-cn_image_0000002552959040.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234949Z&HW-CC-Expire=86400&HW-CC-Sign=B114767A0D74359744305EC1DAC878919E1495828F564C910B32B5834F84FA89 "点击放大")
