---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-bubble
title: 气泡
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 在地图上绘制 > 气泡
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:261b0a498b95169c72c415d87ce54827a404ec10571d563425e6ca51dbc20036
---

## 场景介绍

本章节将向您介绍如何在地图的指定位置添加气泡。

您可以通过气泡在道路上指定位置显示测速、拥堵情况。气泡支持功能：

* 支持设置四个方向的图标（传入的图标宽高需要相同）。
* 支持设置图标碰撞规则。
* 支持设置当前气泡的候选坐标段，通过计算使气泡在最佳的线段位置上。
* 支持设置图标动画。
* 支持添加点击事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/2AYbNwRnQGWVgTVHbLZFfg/zh-cn_image_0000002558605886.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053908Z&HW-CC-Expire=86400&HW-CC-Sign=7FFA6B28486315FB1F8783D9C10ECAF2ECEEF1545113D018E1D8B7FFE884DDBC "点击放大")

## 接口说明

添加气泡功能主要由[BubbleParams](../harmonyos-references/map-common.md#bubbleparams)、[addBubble](../harmonyos-references/map-map-mapcomponentcontroller.md#addbubble)和[Bubble](../harmonyos-references/map-map-bubble.md)提供，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-map-bubble.md)。

| 接口名 | 描述 |
| --- | --- |
| [BubbleParams](../harmonyos-references/map-common.md#bubbleparams) | 气泡参数。 |
| [addBubble](../harmonyos-references/map-map-mapcomponentcontroller.md#addbubble)(params: [mapCommon.BubbleParams](../harmonyos-references/map-common.md#bubbleparams)): Promise<[Bubble](../harmonyos-references/map-map-bubble.md)> | 在地图上添加气泡。 |
| [Bubble](../harmonyos-references/map-map-bubble.md) | 气泡，支持更新和查询相关属性。 |

## 开发步骤

### 添加气泡

1. 导入相关模块。

   ```
   1. import { MapComponent, mapCommon, map } from '@kit.MapKit';
   2. import { AsyncCallback } from '@kit.BasicServicesKit';
   ```
2. 添加气泡，在callback方法中创建初始化参数并新建气泡。

   ```
   1. @Entry
   2. @Component
   3. struct BubbleDemo {
   4. private mapOptions?: mapCommon.MapOptions;
   5. private mapController?: map.MapComponentController;
   6. private callback?: AsyncCallback<map.MapComponentController>;
   7. private bubble?: map.Bubble;

   9. aboutToAppear(): void {
   10. this.mapOptions = {
   11. position: {
   12. target: {
   13. latitude: 39.918,
   14. longitude: 116.397
   15. },
   16. zoom: 14
   17. }
   18. };

   20. this.callback = async (err, mapController) => {
   21. if (!err) {
   22. this.mapController = mapController;
   23. let bubbleOptions: mapCommon.BubbleParams = {
   24. // 气泡位置
   25. positions: [[{
   26. latitude: 39.918,
   27. longitude: 116.397
   28. }]],
   29. // 设置图标，必须提供4个方向的图标，图标存放在resources/rawfile
   30. icons: [
   31. 'speed_limit_10.png',
   32. 'speed_limit_20.png',
   33. 'speed_limit_30.png',
   34. 'speed_limit_40.png'
   35. ],
   36. // 定义气泡的显示属性，为true时，在被碰撞后仍能显示
   37. forceVisible: true,
   38. // 定义气泡碰撞优先级，数值越大，优先级越低
   39. priority: 3,
   40. // 定义气泡展示的最小层级
   41. minZoom: 2,
   42. // 定义气泡展示的最大层级
   43. maxZoom: 20,
   44. // 定义气泡是否可见
   45. visible: true,
   46. // 定义气泡叠加层级属性
   47. zIndex: 1
   48. }

   50. // 添加气泡
   51. try {
   52. this.bubble = await this.mapController.addBubble(bubbleOptions);
   53. } catch (e) {
   54. console.error(`Failed to create the bubble, code is：${e.code}, message is ${e.message}`);
   55. }
   56. } else {
   57. console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
   58. }
   59. };
   60. }

   62. build() {
   63. Stack() {
   64. Column() {
   65. MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback });
   66. }.width('100%')
   67. }.height('100%')
   68. }
   69. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/8rXtr7pwQuCXPIudf4pGUQ/zh-cn_image_0000002589325413.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053908Z&HW-CC-Expire=86400&HW-CC-Sign=567A8CD9F234697E53F5E6F5008BFA98A19CCA549CD672B35285BF70504E8349 "点击放大")

### 设置监听气泡点击事件

```
1. let callback = (bubble: map.Bubble) => {
2. console.info("bubbleClick", `callback bubble = ${bubble.getId()}`);
3. };
4. this.mapController?.on("bubbleClick", callback);
```

### 气泡动画

[Bubble](../harmonyos-references/map-map-bubble.md)调用[setAnimation](../harmonyos-references/map-map-basepriorityoverlay.md#setanimation)设置动画。

[Bubble](../harmonyos-references/map-map-bubble.md)调用[startAnimation](../harmonyos-references/map-map-basepriorityoverlay.md#startanimation)启动动画。

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
22. this.bubble.setAnimation(animation);
23. this.bubble.startAnimation();
```
