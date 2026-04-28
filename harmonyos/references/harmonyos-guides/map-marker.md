---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-marker
title: 标记
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 在地图上绘制 > 标记
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:79f274aa42869afd4088e4946384526621dd60d5815392095b8ffa480a3fa266
---

## 场景介绍

本章节将向您介绍如何在地图的指定位置添加标记以标识位置、商家、建筑等。

点标记用来在地图上标记任何位置，例如用户位置、车辆位置、店铺位置等一切带有位置属性的事物。Map Kit提供的点标记功能（又称 Marker）封装了大量的触发事件，例如点击事件、长按事件、拖拽事件。

Marker有默认风格，同时也支持自定义。由于内容丰富，以下只能展示一些基础功能的使用。

5.1.1(19)开始，支持控制Marker文字显隐功能。

6.0.0(20)开始，支持自定义组件实现marker图标功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/XQucWsStTISfgQx_Fwxh4w/zh-cn_image_0000002552799378.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234946Z&HW-CC-Expire=86400&HW-CC-Sign=B992C710B45A73AFC77D72BEDDACD919205F53210C4B27FA23A4AC5F40EC63E8 "点击放大")

## 接口说明

添加标记功能主要由[MarkerOptions](../harmonyos-references/map-common.md#markeroptions)、[addMarker](../harmonyos-references/map-map-mapcomponentcontroller.md#addmarker)和[Marker](../harmonyos-references/map-map-marker.md)提供，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-map-marker.md)。

| 接口名 | 描述 |
| --- | --- |
| [MarkerOptions](../harmonyos-references/map-common.md#markeroptions) | 标记参数。 |
| [addMarker](../harmonyos-references/map-map-mapcomponentcontroller.md#addmarker)(options: [mapCommon.MarkerOptions](../harmonyos-references/map-common.md#markeroptions)): Promise<[Marker](../harmonyos-references/map-map-marker.md)> | 在地图上添加标记。 |
| [Marker](../harmonyos-references/map-map-marker.md) | 标记，支持更新和查询相关属性。 |

## 开发步骤

### 添加标记

1. 导入相关模块。

   ```
   1. import { MapComponent, mapCommon, map } from '@kit.MapKit';
   2. import { AsyncCallback } from '@kit.BasicServicesKit';
   ```
2. 添加标记，在callback方法中创建初始化参数并新建[Marker](../harmonyos-references/map-map-marker.md)。

   ```
   1. @Entry
   2. @Component
   3. struct MarkerDemo {
   4. private mapOptions?: mapCommon.MapOptions;
   5. private mapController?: map.MapComponentController;
   6. private callback?: AsyncCallback<map.MapComponentController>;
   7. private mapEventManager?: map.MapEventManager;
   8. private marker?: map.Marker;

   10. aboutToAppear(): void {
   11. // 地图初始化参数
   12. this.mapOptions = {
   13. position: {
   14. target: {
   15. latitude: 31.984410259206815,
   16. longitude: 118.76625379397866
   17. },
   18. zoom: 15
   19. }
   20. };
   21. this.callback = async (err, mapController) => {
   22. if (!err) {
   23. this.mapController = mapController;
   24. this.mapEventManager = this.mapController.getEventManager();
   25. // Marker初始化参数
   26. let markerOptions: mapCommon.MarkerOptions = {
   27. position: {
   28. latitude: 31.984410259206815,
   29. longitude: 118.76625379397866
   30. },
   31. rotation: 0,
   32. visible: true,
   33. zIndex: 0,
   34. alpha: 1,
   35. anchorU: 0.5,
   36. anchorV: 1,
   37. clickable: true,
   38. draggable: true,
   39. flat: false
   40. };
   41. // 新建marker
   42. try {
   43. this.marker = await this.mapController.addMarker(markerOptions);
   44. } catch (e) {
   45. console.error(`Failed to create the marker, code is：${e.code}, message is ${e.message}`);
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/VFrAuGpsQKahjA1Bnb-5TA/zh-cn_image_0000002583439073.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234946Z&HW-CC-Expire=86400&HW-CC-Sign=80BBE36F9C36AE991B6DBA3F2B73393F00E66E727A3BDB0950EA1947287005EF "点击放大")
3. 在添加标记之后，修改已经设置的标记属性。

   ```
   1. // 设置标记可拖拽
   2. this.marker.setDraggable(true);
   3. // 设置标记锚点
   4. this.marker.setMarkerAnchor(1.0, 1.0);
   ```

### 自定义标记

通过在[MarkerOptions](../harmonyos-references/map-common.md#markeroptions)中将icon属性设置为自定义图标的资源，可将默认标记图标修改成自定义图标。

```
1. let markerOptions: mapCommon.MarkerOptions = {
2. position: {
3. latitude: 31.984410259206815,
4. longitude: 118.76625379397866
5. },
6. rotation: 0,
7. visible: true,
8. zIndex: 0,
9. alpha: 1,
10. anchorU: 0.5,
11. anchorV: 1,
12. clickable: true,
13. draggable: true,
14. flat: false,
15. // 图标存放在resources/rawfile，icon参数传入rawfile文件夹下的相对路径
16. icon: 'test.png'
17. };
18. this.marker = await this.mapController.addMarker(markerOptions);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/Yt5t0IBmTpKd4_Vk3cHYdg/zh-cn_image_0000002552959028.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234946Z&HW-CC-Expire=86400&HW-CC-Sign=17011FBB6F0E78A1C2BE448229DACFF5712352E223FFF3ACC55CC84131A0A25E "点击放大")

### 控制Marker文字显隐

通过[setAnnotationVisible](../harmonyos-references/map-map-marker.md#setannotationvisible)方法可以控制Marker文字显隐，还可以通过[isAnnotationVisible](../harmonyos-references/map-map-marker.md#isannotationvisible)方法来获取Marker文字显隐的状态。

```
1. // Marker初始化参数
2. let markerOptions: mapCommon.MarkerOptions = {
3. position: {
4. latitude: 31.984410259206815,
5. longitude: 118.76625379397866
6. },
7. rotation: 0,
8. visible: true,
9. zIndex: 0,
10. alpha: 1,
11. anchorU: 0.5,
12. anchorV: 1,
13. clickable: true,
14. draggable: true,
15. flat: false,
16. annotations: [{
17. // 定义标题内容
18. content: "text",
19. fontStyle: 1,
20. strokeWidth: 3,
21. fontSize: 15
22. }]
23. };
24. // 创建Marker
25. this.marker = await this.mapController.addMarker(markerOptions);
26. // 设置文字隐藏
27. this.marker.setAnnotationVisible(false);
28. // 查询当前显隐状态
29. let isAnnotationVisible: boolean = this.marker.isAnnotationVisible();
30. console.info(`isAnnotationVisible is: ` + isAnnotationVisible);
```

**图1** 隐藏Marker文字之前

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/xmz_F26tSJWm9saSi2wsBw/zh-cn_image_0000002583479029.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234946Z&HW-CC-Expire=86400&HW-CC-Sign=F3B9CEE6FA702CF0408121C530433FC0E590D7E599D270D0FCD2296EAD92157C "点击放大")

**图2** 隐藏Marker文字之后

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/KOm1bpQ-RVOzi-uRKpoYng/zh-cn_image_0000002552799380.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234946Z&HW-CC-Expire=86400&HW-CC-Sign=CA8910A95819A111321D6C5F555E7156B626CA77FDBCA389537436AECA9D8BD4 "点击放大")

### 碰撞检测

通过在[MarkerOptions](../harmonyos-references/map-common.md#markeroptions)中设置collisionRule属性，可以设置标记的冲突处理规则。

```
1. let markerOptions: mapCommon.MarkerOptions = {
2. position: {
3. latitude: 31.984410259206815,
4. longitude: 118.76625379397866
5. },
6. rotation: 0,
7. visible: true,
8. zIndex: 0,
9. alpha: 1,
10. anchorU: 0.5,
11. anchorV: 1,
12. clickable: true,
13. draggable: true,
14. flat: false,
15. // 图标存放在resources/rawfile，icon参数传入rawfile文件夹下的相对路径
16. icon: 'icon.png',
17. annotations:  [{
18. // 定义标题内容
19. content: "Test",
20. fontStyle: 1,
21. strokeWidth: 3,
22. fontSize: 15
23. }],
24. // 设置碰撞规则为图标和名称都参与碰撞
25. collisionRule: mapCommon.CollisionRule.ALL,
26. annotationPosition: mapCommon.TextPosition.TOP
27. };
28. this.marker = await this.mapController.addMarker(markerOptions);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/oJFX31PbTHK5tRXlkkmUZQ/zh-cn_image_0000002583439075.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234946Z&HW-CC-Expire=86400&HW-CC-Sign=9459898CA0D4093D02B204A775DE3BF94B4FDBDAB1AB72D793A1EFF4590403FA "点击放大")

### 设置监听标记点击事件

```
1. let callback = (marker: map.Marker) => {
2. console.info(`on-markerClick marker = ${marker.getId()}`);
3. };
4. this.mapEventManager.on("markerClick", callback);
```

### 设置监听标记拖动事件

通过如下步骤设置监听标记拖动事件：

1. 将[Marker](../harmonyos-references/map-map-marker.md)的拖拽属性设置为true。
2. 调用[on(type: 'markerDragStart' , callback: Callback<Marker>)](../harmonyos-references/map-map-mapeventmanager.md#onmarkerdragstart)方法监听标记是否开始拖拽。
3. 调用[on(type: 'markerDrag' , callback: Callback<Marker>)](../harmonyos-references/map-map-mapeventmanager.md#onmarkerdrag)，监听标记拖动过程。
4. 调用[on(type: 'markerDragEnd' , callback: Callback<Marker>)](../harmonyos-references/map-map-mapeventmanager.md#onmarkerdragend)，监听标记拖动结束事件。

```
1. // 设置标记可拖拽
2. this.marker.setDraggable(true);

4. // 监听标记开始拖拽
5. let markerCallback = (marker: map.Marker) => {
6. console.info(`on-markerDragStart marker = ${marker.getId()}`);
7. };
8. this.mapEventManager.on("markerDragStart", markerCallback);

10. // 监听标记拖拽事件
11. let markerDragCallback = (marker: map.Marker) => {
12. console.info(`on-markerDrag marker = ${marker.getId()}`);
13. };
14. this.mapEventManager.on("markerDrag", markerDragCallback);

16. // 监听标记拖拽结束
17. let markerDragEndCallback = (marker: map.Marker) => {
18. console.info(`on-markerDragEnd marker = ${marker.getId()}`);
19. };
20. this.mapEventManager.on("markerDragEnd", markerDragEndCallback);
```

### 信息窗

```
1. // 添加信息窗
2. let markerOptions: mapCommon.MarkerOptions = {
3. position: {
4. latitude: 31.984410259206815,
5. longitude: 118.76625379397866
6. }
7. };
8. this.marker = await this.mapController?.addMarker(markerOptions);
9. // 设置信息窗的标题
10. this.marker.setTitle('南京');
11. // 设置信息窗的子标题
12. this.marker.setSnippet('华东地区');
13. // 设置标记可点击
14. this.marker.setClickable(true);
15. // 设置信息窗的锚点位置
16. this.marker.setInfoWindowAnchor(1, 1);
17. // 设置信息窗可见，点击标记后可展示信息窗
18. this.marker.setInfoWindowVisible(true);
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/s_mUKLfDStCuq8MVta67MA/zh-cn_image_0000002552959030.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234946Z&HW-CC-Expire=86400&HW-CC-Sign=20F52E03582627BBDB8E381C6A87993E9AF223AB0291BF9E08ED9D9FB8251AE4 "点击放大")

### 自定义信息窗

```
1. @Entry
2. @Component
3. struct MarkerDemo {
4. private mapOptions?: mapCommon.MapOptions;
5. private mapController?: map.MapComponentController;
6. private callback?: AsyncCallback<map.MapComponentController>;

8. aboutToAppear(): void {
9. this.mapOptions = {
10. position: {
11. target: {
12. latitude: 32.120750,
13. longitude: 118.788765
14. },
15. zoom: 15
16. }
17. }

19. this.callback = async (err, mapController) => {
20. if (!err) {
21. this.mapController = mapController;
22. let markerOptions: mapCommon.MarkerOptions = {
23. position: {
24. latitude: 32.120750,
25. longitude: 118.788765
26. },
27. clickable: true,
28. // 设置信息窗标题，点击标记后可展示信息窗
29. title: "自定义信息窗"
30. };
31. // 创建Marker
32. await this.mapController?.addMarker(markerOptions);
33. } else {
34. console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
35. }
36. }
37. }

39. build() {
40. Stack() {
41. Column() {
42. MapComponent({
43. mapOptions: this.mapOptions,
44. mapCallback: this.callback,
45. // 自定义信息窗
46. customInfoWindow: this.customInfoWindow
47. })
48. .width('100%')
49. .height('100%');
50. }.width('100%')
51. }.height('100%')
52. }
53. // 自定义信息窗BuilderParam
54. @BuilderParam customInfoWindow: ($$: map.MarkerDelegate) => void = this.customInfoWindowBuilder;
55. // 自定义信息窗Builder
56. @Builder
57. customInfoWindowBuilder($$: map.MarkerDelegate) {
58. if ($$.marker) {
59. Text($$.marker.getTitle())
60. .width("50%")
61. .height(50)
62. .backgroundColor(Color.Green)
63. .textAlign(TextAlign.Center)
64. .fontColor(Color.Black)
65. .font({ size: 25, weight: 10, style: FontStyle.Italic })
66. .border({ width: 3, color: Color.Black, radius: 25, style: BorderStyle.Dashed })
67. }
68. }
69. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/4t3XjscZRQmAzgxOs8Fe-w/zh-cn_image_0000002583479031.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234946Z&HW-CC-Expire=86400&HW-CC-Sign=CCFA37ADBC11FFD29CB3EDB3B01228743AC8258D0505330CDD4036CBF58A8DAD "点击放大")

### 标记动画

Marker支持设置旋转、缩放、平移、透明、图片动画播放和组合动画效果。

| 接口名 | 描述 |
| --- | --- |
| [AlphaAnimation](../harmonyos-references/map-map-alphaanimation.md) | 控制透明度的动画类。 |
| [RotateAnimation](../harmonyos-references/map-map-rotateanimation.md) | 控制旋转的动画类。 |
| [ScaleAnimation](../harmonyos-references/map-map-scaleanimation.md) | 控制缩放的动画类。 |
| [TranslateAnimation](../harmonyos-references/map-map-translateanimation.md) | 控制平移的动画类。 |
| [PlayImageAnimation](../harmonyos-references/map-map-playimageanimation.md) | 控制多张图片的动画类。 |
| [AnimationSet](../harmonyos-references/map-map-animationset.md) | 动画集合。 |

旋转动画效果的示例代码如下：

```
1. import { map, mapCommon, MapComponent } from '@kit.MapKit';
2. import { AsyncCallback } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct MarkerDemo {
7. private mapOptions?: mapCommon.MapOptions;
8. private callback?: AsyncCallback<map.MapComponentController>;

10. aboutToAppear(): void {
11. this.mapOptions = {
12. position: {
13. target: {
14. latitude: 32.020750,
15. longitude: 118.788765
16. },
17. zoom: 11
18. }
19. }

21. this.callback = async (err, mapController) => {
22. if (!err) {
23. // 构造MarkerOptions对象
24. let markerOptions: mapCommon.MarkerOptions = {
25. position: {
26. latitude: 32.020750,
27. longitude: 118.788765
28. }
29. };
30. // 新建marker
31. let marker: map.Marker = await mapController.addMarker(markerOptions);
32. // 构造RotateAnimation对象
33. let animation = new map.RotateAnimation(0, 270);
34. // 动画执行时间
35. animation.setDuration(2000);

37. // 动画结束状态
38. animation.setFillMode(map.AnimationFillMode.BACKWARDS);

40. // 动画重复模式
41. animation.setRepeatMode(map.AnimationRepeatMode.REVERSE);

43. // 动画重复次数
44. animation.setRepeatCount(100);

46. // 设置动画开始监听
47. let callbackStart = () => {
48. console.info("animationStart", `callback`);
49. };
50. animation.on("animationStart", callbackStart);

52. // 设置动画结束监听
53. let callbackEnd = () => {
54. console.info("animationEnd", `callback`);
55. };
56. animation.on("animationEnd", callbackEnd);

58. // 设置动画
59. marker.setAnimation(animation);
60. // 开启动画
61. marker.startAnimation();
62. } else {
63. console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
64. }
65. }
66. }

68. build() {
69. Stack() {
70. Column() {
71. MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
72. }.width('100%')
73. }.height('100%')
74. }
75. }
```

展示效果如图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/cI2OW4J0TsWdBsH2BgErmA/zh-cn_image_0000002552799382.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234946Z&HW-CC-Expire=86400&HW-CC-Sign=E3723DCF4180C67D2ABF96D0D91589180C9EEA73331CFB9F1C56C112888986D1 "点击放大")

### 图片动画播放

```
1. import { map, mapCommon, MapComponent } from '@kit.MapKit';
2. import { AsyncCallback } from '@kit.BasicServicesKit';
3. import { image } from '@kit.ImageKit';

5. @Entry
6. @Component
7. struct MarkerDemo {
8. private mapOptions?: mapCommon.MapOptions;
9. private callback?: AsyncCallback<map.MapComponentController>;

11. aboutToAppear(): void {
12. this.mapOptions = {
13. position: {
14. target: {
15. latitude: 32.020750,
16. longitude: 118.788765
17. },
18. zoom: 11
19. }
20. }

22. this.callback = async (err, mapController) => {
23. if (!err) {
24. // 构造MarkerOptions对象
25. let markerOptions: mapCommon.MarkerOptions = {
26. position: {
27. latitude: 32.020750,
28. longitude: 118.788765
29. },
30. };
31. let images: Array<ResourceStr | image.PixelMap> = [
32. // 图标需存放在resources/rawfile目录下
33. 'icon/avocado.png',
34. 'icon/20231027.png',
35. // 图标需存放在resources/base/media目录下
36. $r('app.media.maps_blue_dot')
37. ]
38. let mContext = this.getUIContext().getHostContext();
39. if (mContext) {
40. const fileData: Uint8Array = await mContext?.resourceManager?.getRawFileContent('icon/icon.png');
41. let imageSource: image.ImageSource =
42. image.createImageSource(fileData.buffer.slice(0, fileData.buffer.byteLength));
43. let pixelMap: PixelMap = await imageSource.createPixelMap();
44. images.push(pixelMap);
45. }
46. // 新建marker
47. let marker: map.Marker = await mapController.addMarker(markerOptions);
48. // 构造PlayImageAnimation对象
49. let animation: map.PlayImageAnimation = new map.PlayImageAnimation();
50. // 添加图片
51. await animation.addImages(images)
52. // 动画执行时间
53. animation.setDuration(3000);

55. // 动画结束状态
56. animation.setFillMode(map.AnimationFillMode.BACKWARDS);

58. // 动画重复模式
59. animation.setRepeatMode(map.AnimationRepeatMode.REVERSE);

61. // 动画重复次数
62. animation.setRepeatCount(100);

64. // 设置动画开始监听
65. let callbackStart = () => {
66. console.info("animationStart", `callback`);
67. };
68. animation.on("animationStart", callbackStart);
69. // 设置动画结束监听
70. let callbackEnd = () => {
71. console.info("animationEnd", `callback`);
72. };
73. animation.on("animationEnd", callbackEnd);
74. // 设置动画
75. marker.setAnimation(animation);
76. // 开启动画
77. marker.startAnimation();
78. } else {
79. console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
80. }
81. }
82. }

84. build() {
85. Stack() {
86. Column() {
87. MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
88. }.width('100%')
89. }.height('100%')
90. }
91. }
```

展示效果如图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/GgzL0eTERjCGlaTu5tIIiw/zh-cn_image_0000002583439077.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234946Z&HW-CC-Expire=86400&HW-CC-Sign=3E8488F7174B08A260EA2FE9EDFF925D74B4C356AD0EF66817FFEB08550731BE "点击放大")

### 自定义组件实现marker图标

通过自定义组件生成marker图标。

```
1. import { map, mapCommon, MapComponent } from '@kit.MapKit';
2. import { AsyncCallback } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct MarkerDemo {
7. private mapOption?: mapCommon.MapOptions;
8. private mapController?: map.MapComponentController;
9. private callback?: AsyncCallback<map.MapComponentController>;
10. private marker?: map.Marker;
11. aboutToAppear(): void {
12. this.mapOption = {
13. position: {
14. target: {
15. latitude: 32.120750,
16. longitude: 118.788765
17. },
18. zoom: 14
19. },
20. scaleControlsEnabled: true
21. }
22. this.callback = async (err, mapController) => {
23. if (!err) {
24. this.mapController = mapController;
25. // 构造MarkerOptions对象
26. let markerOptions: mapCommon.MarkerOptions = {
27. position: {
28. latitude: 32.120750,
29. longitude: 118.788765
30. },
31. // 自定义组件
32. iconBuilder: () => {
33. this.renderBuilder();
34. }
35. };
36. this.marker = await this.mapController?.addMarker(markerOptions);
37. }
38. }
39. }
40. @Builder
41. renderBuilder() {
42. Stack({ alignContent: Alignment.Center }) {
43. // 需要替换您自己的资源图片，存放在resources/base/media目录下
44. Image($r('app.media.iconbuilder'))
45. .syncLoad(true)
46. }
47. .height(50)
48. .width(50)
49. }

51. build() {
52. Stack() {
53. Column() {
54. MapComponent({ mapOptions: this.mapOption, mapCallback: this.callback })
55. .width('100%')
56. .height('100%');
57. }.width('100%')
58. }.height('100%')
59. }
60. }
```

展示效果如图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/A9WigGcHSnWbskRPO-194g/zh-cn_image_0000002552959032.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234946Z&HW-CC-Expire=86400&HW-CC-Sign=6479926F4C41A32F10DD10C95CC5C388E3A82A8B5EE5F82DE1E58A383E867451 "点击放大")
