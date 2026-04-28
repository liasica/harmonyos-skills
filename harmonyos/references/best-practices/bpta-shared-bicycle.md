---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-shared-bicycle
title: 快捷骑行体验
breadcrumb: 最佳实践 > 行业场景解决方案 > 出行导航 > 快捷骑行体验
category: best-practices
scraped_at: 2026-04-28T08:22:14+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:9708cf1b069a96463100bee1da0b1af89bc6ce463c8f3b1b7e714dcc76e7815a
---

## 概述

本场景解决方案涉及共享租赁、即时配送等应用，以共享单车为例，使用实况窗、地图导航和统一扫码等技术，为消费者提供更好的骑行体验。

## 效果展示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/pLPqksUyTpmubjB5h8n3zg/zh-cn_image_0000002229450033.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002211Z&HW-CC-Expire=86400&HW-CC-Sign=BE916E1DFF1E015D24CD7B33169099D2F16696E6F7DBA4B34D993ECE8E500761)

## 场景说明

### 场景整体介绍

为了简化骑行流程，提升用户体验，建议如下：

1. 用户可以从应用内或者系统扫码入口进行扫码，直接进入共享单车解锁页面。

2. 点击解锁按钮后，拉起实况窗显示骑行状态。

3. 完成还车、支付等操作后，实况窗状态实时更新。

这样，用户无需重复寻找应用和功能入口，整个流程更加简便。

### 场景优势

本场景结合提供的实况窗、地图导航、扫码等系统能力，可以带给用户更加便捷高效的体验。具体优势如下：

1.使用实况窗技术帮助用户聚焦任务，快速查看和即时处理。支持在锁屏、通知中心显示卡片，在状态栏显示胶囊，点击胶囊后展开悬浮卡片，方便用户查看重点信息。多种显示方式确保信息即时触达，减少用户进出应用或服务页面的次数。

2.基于Map Kit实现个性化地图呈现、地图搜索和路线规划等功能，提供缩放、旋转、移动等流畅的手势交互体验。

## 场景分析

### 典型场景

|  |  |  |  |
| --- | --- | --- | --- |
| **编号** | **场景名称** | **描述** | **实现方案** |
| 1 | 扫码解锁 | 首页和共享单车页面均可扫码直达解锁页面。 | 基于ScanKit能够快速实现扫码能力 |
| 2 | 地图规划路径 | 选中目的地，展示最短路径。 | 基于MapKit能够快速实现路径规划和路线绘制能力 |
| 3 | 实况窗展示骑行状态 | 骑行过程中，用户需要查看骑行状态。 | 使用实况窗，用户在锁屏状态下也能查看骑行状态，无需解锁应用。 |

## 场景实现

### 业务流程图

左图展示了当前骑行场景的流程，右图展示了优化后的流程。优化后，省去了在应用间切换和寻找功能入口的步骤，简化了用户操作，提升了用户体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/T6R3xBqgQFWh4eEbcEzXcA/zh-cn_image_0000002193850172.png?HW-CC-KV=V1&HW-CC-Date=20260428T002211Z&HW-CC-Expire=86400&HW-CC-Sign=F1EF6E7DE29C1D29286A603FA3AC1B94E51987828DFC208E75E8B9DA903CB575)

### 骑行状态图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/cGUzAnPTSU29iNGYIdz-QQ/zh-cn_image_0000002194009740.png?HW-CC-KV=V1&HW-CC-Date=20260428T002211Z&HW-CC-Expire=86400&HW-CC-Sign=F0C91606D95965C817D05E803D39A3F5625120365C049B64147B72D64C52D875)

### 时序图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/qMZXyPXPTo6R0-RRWCZovQ/zh-cn_image_0000002193850156.png?HW-CC-KV=V1&HW-CC-Date=20260428T002211Z&HW-CC-Expire=86400&HW-CC-Sign=C86BCA6846A87602597B0B0E08A3CF835A9C9E1B63C25802814FE3812B8B5803 "点击放大")

## 扫码解锁

### 效果展示

在首页或者共享单车页面，点击扫码进入扫码界面，可以使用后置摄像头进行扫码，也可以点击图库选择二维码图片进行扫码。“扫码直达”相关的使用请参见“[接入扫码直达服务](../harmonyos-guides/scan-directservice.md)”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/PKDJpaSFQKScMmEyYDMpXQ/zh-cn_image_0000002229335549.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002211Z&HW-CC-Expire=86400&HW-CC-Sign=ECFF2CFD89E89C2A527526BFCAFDD3A62BF22A762EAAAE809289388ECEB83E08)

### 时序图

主要业务流程如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/GuLloAiGS5OqlaESY1CcRw/zh-cn_image_0000002193850148.png?HW-CC-KV=V1&HW-CC-Date=20260428T002211Z&HW-CC-Expire=86400&HW-CC-Sign=8076792DF14C4FBD10370EB2CCB81709765C10AEAE5D6B28613F2870B3243310 "点击放大")

### 关键点说明

1、使用[Scan Kit](../harmonyos-guides/scan-kit-guide.md)实现扫码能力，Scan Kit应用了多项计算机视觉技术和AI算法技术，不仅实现了远距离自动扫码，同时还针对多种复杂扫码场景（如暗光、污损、模糊、小角度、曲面码等）做了识别优化，提升扫码成功率与用户体验。

2、在Entry模块的module.json5文件的requestPermissions字段中添加ohos.permission.CAMERA权限，以申请系统相机权限。

```
1. "requestPermissions": [
2. // ...
3. {
4. "name": "ohos.permission.CAMERA",
5. "reason": "$string:reason_camera",
6. "usedScene": {
7. "abilities": [
8. "EntryAbility"
9. ],
10. "when": "always"
11. }
12. }
13. ]
14. },
```

[module.json5](https://gitcode.com/harmonyos_samples/bicycle-sharing/blob/master/entry/src/main/module.json5#L52-L110)

3、支持多种识码类型，常用的是二维码，也支持条形码扫描。

### 关键代码片段

```
1. import { scanBarcode, scanCore } from '@kit.ScanKit';
2. import { CyclingConstants, CyclingStatus } from '../constants/CyclingConstants';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import Logger from './Logger';

6. export class ScanUtil {
7. public static scan(obj: Object, uiContext: UIContext): void {
8. let options: scanBarcode.ScanOptions = {
9. scanTypes: [scanCore.ScanType.ALL, scanCore.ScanType.ONE_D_CODE],
10. enableMultiMode: true,
11. enableAlbum: true
12. };
13. try {
14. scanBarcode.startScanForResult(uiContext?.getHostContext(), options).then((result: scanBarcode.ScanResult) => {
15. Logger.info('[BicycleSharing]', 'Promise scan result: %{public}s', JSON.stringify(result));
16. if (result.scanType === CyclingConstants.SCAN_TYPE) {
17. AppStorage.setOrCreate(CyclingConstants.CYCLING_STATUS, CyclingStatus.WAITING_UNLOCK);
18. uiContext?.getRouter().pushUrl({ url: 'pages/ConfirmUnlock' });
19. }
20. }).catch((error: BusinessError) => {
21. Logger.error(0x0001, '[BicycleSharing]', 'Promise error: %{public}s', JSON.stringify(error));
22. });
23. } catch (error) {
24. Logger.error(0x0001, '[BicycleSharing]', 'failReason: %{public}s', JSON.stringify(error));
25. }
26. }
27. }
```

[ScanUtil.ets](https://gitcode.com/harmonyos_samples/bicycle-sharing/blob/master/entry/src/main/ets/utils/ScanUtil.ets#L16-L43)

## 地图路径规划

### 效果展示

进入找车页面后，可以点击任意位置模拟自行车的所在地，地图将进行步行路线规划并增加标记点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/-ej08bhgRN6OE0n6j4QLkQ/zh-cn_image_0000002193850168.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002211Z&HW-CC-Expire=86400&HW-CC-Sign=C620EC210480A810F3316B4732C2DB60B6D04B6E1F51D837F9138F6952820226)

### 时序图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/rCWjpKyDQYOQG4UwFHdddg/zh-cn_image_0000002194009744.png?HW-CC-KV=V1&HW-CC-Date=20260428T002211Z&HW-CC-Expire=86400&HW-CC-Sign=1E2750299D3498778B4AF0F1DFDFDDE8AEFF2B562E6A69E68C43BADDD9FA0733 "点击放大")

### 关键点说明

1、使用[Map Kit](../harmonyos-guides/map-kit-guide.md)实现地图能力，Map Kit可以帮助开发者实现个性化地图呈现、地图搜索和路线规划等功能，轻松完成地图构建工作。

2、参考文档[开通地图服务](../harmonyos-guides/map-config-agc.md#section16133115441516)去AppGallery Connect开通地图服务。注意要在工程中entry模块的module.json5文件中配置client\_id。

3、启用“我的位置”之前，确保应用已获取用户定位权限。需要申请ohos.permission.LOCATION和ohos.permission.APPROXIMATELY\_LOCATION权限。

### 关键代码片段

1、导入Map Kit

```
1. import { MapComponent, mapCommon, map } from '@kit.MapKit';
```

[CyclingPage.ets](https://gitcode.com/harmonyos_samples/bicycle-sharing/blob/master/entry/src/main/ets/pages/CyclingPage.ets#L16-L16)

2、集成地图组件，初始化地图页面

```
1. aboutToAppear(): void {
2. // initialize map
3. this.callback = async (err, mapController) => {
4. let hasPermissions = false;
5. if (!err) {
6. this.mapController = mapController;
7. this.mapController.on('mapLoad', async () => {
8. hasPermissions = await MapUtil.checkPermissions(this.mapController);
9. if (!hasPermissions) {
10. this.requestPermissions();
11. }
12. if (hasPermissions) {
13. let requestInfo: geoLocationManager.CurrentLocationRequest = {
14. 'priority': geoLocationManager.LocationRequestPriority.FIRST_FIX,
15. 'scenario': geoLocationManager.LocationRequestScenario.UNSET,
16. 'maxAccuracy': 0
17. };
18. let locationChange = async (): Promise<void> => {
19. };
20. geoLocationManager.on('locationChange', requestInfo, locationChange);
21. geoLocationManager.getCurrentLocation(requestInfo).then(async (result) => {
22. let mapPosition: mapCommon.LatLng =
23. await map.convertCoordinate(mapCommon.CoordinateType.WGS84, mapCommon.CoordinateType.GCJ02, result);
24. AppStorage.setOrCreate('longitude', mapPosition.longitude);
25. AppStorage.setOrCreate('latitude', mapPosition.latitude);
26. let cameraPosition: mapCommon.CameraPosition = {
27. target: mapPosition,
28. zoom: 15,
29. tilt: 0,
30. bearing: 0
31. };
32. let cameraUpdate = map.newCameraPosition(cameraPosition);
33. mapController?.animateCamera(cameraUpdate, 1000);
34. })
35. }
36. });
37. this.mapController.on('mapClick', async (position) => {
38. this.mapController?.clear();
39. this.marker?.remove();
40. let requestInfo: geoLocationManager.CurrentLocationRequest = {
41. 'priority': geoLocationManager.LocationRequestPriority.FIRST_FIX,
42. 'scenario': geoLocationManager.LocationRequestScenario.UNSET,
43. 'maxAccuracy': 0
44. };
45. let locationChange = async (location: geoLocationManager.Location): Promise<void> => {
46. let wgs84Position: mapCommon.LatLng = {
47. latitude: location.latitude,
48. longitude: location.longitude
49. };
50. let gcj02Posion: mapCommon.LatLng =
51. await map.convertCoordinate(mapCommon.CoordinateType.WGS84, mapCommon.CoordinateType.GCJ02,
52. wgs84Position);
53. this.myPosition = gcj02Posion
54. };
55. geoLocationManager.on('locationChange', requestInfo, locationChange);
56. // add walking marker
57. this.marker = await MapUtil.addMarker(position, this.mapController);
58. const walkingRoutes = await MapUtil.walkingRoutes(position, this.myPosition);
59. await MapUtil.paintRoute(walkingRoutes!, this.mapPolyline, this.mapController);
60. });
61. }
62. };
63. }
```

[CyclingPage.ets](https://gitcode.com/harmonyos_samples/bicycle-sharing/blob/master/entry/src/main/ets/pages/CyclingPage.ets#L48-L113)

3、向用户申请授予定位权限，启动“我的位置”功能

```
1. requestPermissions(): void {
2. let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
3. atManager.requestPermissionsFromUser(this.getUIContext().getHostContext() as common.UIAbilityContext,
4. ['ohos.permission.LOCATION', 'ohos.permission.APPROXIMATELY_LOCATION'])
5. .then(() => {
6. this.mapController?.setMyLocationEnabled(true);
7. this.mapController?.setMyLocationControlsEnabled(true);
8. this.mapController?.setCompassControlsEnabled(false);
9. this.mapController?.setMyLocationStyle({ displayType: mapCommon.MyLocationDisplayType.FOLLOW });
10. geoLocationManager.getCurrentLocation().then(async (result) => {
11. let mapPosition: mapCommon.LatLng =
12. await map.convertCoordinate(mapCommon.CoordinateType.WGS84, mapCommon.CoordinateType.GCJ02, result);
13. AppStorage.setOrCreate('longitude', mapPosition.longitude);
14. AppStorage.setOrCreate('latitude', mapPosition.latitude);
15. let cameraPosition: mapCommon.CameraPosition = {
16. target: mapPosition,
17. zoom: 15,
18. tilt: 0,
19. bearing: 0
20. };
21. let cameraUpdate = map.newCameraPosition(cameraPosition);
22. this.mapController?.animateCamera(cameraUpdate, 1000);
23. })
24. })
25. .catch((err: BusinessError) => {
26. Logger.error(`Failed to request permissions from user. Code is ${err.code}, message is ${err.message}`);
27. })
28. }
```

[CyclingPage.ets](https://gitcode.com/harmonyos_samples/bicycle-sharing/blob/master/entry/src/main/ets/pages/CyclingPage.ets#L282-L310)

4、监听点击事件

```
1. this.mapController.on('mapClick', async (position) => {
2. this.mapController?.clear();
3. this.marker?.remove();

5. if (!this.myPosition) {
6. Logger.error('Current position is not available');
7. return;
8. }

10. this.marker = await MapUtil.addMarker(position, this.mapController);
11. const walkingRoutes = await MapUtil.walkingRoutes(position, this.myPosition);
12. await MapUtil.paintRoute(walkingRoutes!, this.mapPolyline, this.mapController);
13. });
```

[FindBike.ets](https://gitcode.com/harmonyos_samples/bicycle-sharing/blob/master/entry/src/main/ets/pages/FindBike.ets#L92-L104)

5、启动步行路径规划

```
1. public static async walkingRoutes(position: mapCommon.LatLng, myPosition?: mapCommon.LatLng) {
2. let params: navi.RouteParams = {
3. origins: [myPosition!],
4. destination: position,
5. language: 'zh_CN'
6. };
7. try {
8. const result = await navi.getWalkingRoutes(params);
9. Logger.info('naviDemo', 'getWalkingRoutes success result =' + JSON.stringify(result));
10. return result;
11. } catch (err) {
12. Logger.error('naviDemo', 'getWalkingRoutes fail err =' + JSON.stringify(err));
13. }
14. return undefined;
15. }
```

[MapUtil.ets](https://gitcode.com/harmonyos_samples/bicycle-sharing/blob/master/entry/src/main/ets/utils/MapUtil.ets#L51-L66)

6、绘制路线

```
1. public static async paintRoute(routeResult: navi.RouteResult, mapPolyline?: map.MapPolyline,
2. mapController?: map.MapComponentController) {
3. mapPolyline?.remove();
4. let polylineOption: mapCommon.MapPolylineOptions = {
5. points: routeResult.routes[0].overviewPolyline!,
6. clickable: true,
7. startCap: mapCommon.CapStyle.BUTT,
8. endCap: mapCommon.CapStyle.BUTT,
9. geodesic: false,
10. jointType: mapCommon.JointType.BEVEL,
11. visible: true,
12. width: 20,
13. zIndex: 10,
14. gradient: false,
15. color: 0xFF2970FF
16. }
17. try {
18. mapPolyline = await mapController?.addPolyline(polylineOption);
19. } catch (error) {
20. Logger.error('naviDemo', `addPolyline error: ${JSON.stringify(error)}`);
21. }
22. }
```

[MapUtil.ets](https://gitcode.com/harmonyos_samples/bicycle-sharing/blob/master/entry/src/main/ets/utils/MapUtil.ets#L69-L91)

## 实况窗展示骑行状态

### 效果展示

点击解锁后，实况窗显示骑行状态。完成还车、支付等操作后，实况窗的状态实时更新。支持在锁屏、通知中心显示卡片，状态栏显示胶囊形态。点击状态栏的胶囊后，展开悬浮卡片，方便用户查看骑行状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/vsWC5WknRSq2cNdaPIDkMg/zh-cn_image_0000002229335553.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002211Z&HW-CC-Expire=86400&HW-CC-Sign=529B90D22D98641E0C5A256AD72D2FA099545CA8C1593856132739980C8B5F64)

### 时序图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/5Bk1AQETRFKiVfd2fSF33w/zh-cn_image_0000002194009760.png?HW-CC-KV=V1&HW-CC-Date=20260428T002211Z&HW-CC-Expire=86400&HW-CC-Sign=2A8885FEF66E557A767BE66CFA15ACF70ABC4E3C5BF171A95005F73A005BC726 "点击放大")

### 关键点说明

1、使用Live View Kit实现实况窗服务，支持应用在设备的关键界面展示订单或服务的实时状态信息。

2、参考文档[申请实况窗正式权限](../harmonyos-guides/liveview-formal-authority.md)去AppGallery Connect开通实况窗服务。

3、此场景中仅使用了本地实况窗的能力。本地更新或结束实况窗依赖于您的应用进程。若业务需要，可使用Push Kit远程更新或结束实况窗。

### 关键代码片段

1、导入Live View Kit

```
1. import { liveViewManager } from '@kit.LiveViewKit';
```

[LiveViewController.ets](https://gitcode.com/harmonyos_samples/bicycle-sharing/blob/master/entry/src/main/ets/liveview/LiveViewController.ets#L16-L16)

2、创建实况窗

```
1. public async startLiveView(context: LiveViewContext,
2. liveViewEnvironment?: LiveViewEnvironment): Promise<liveViewManager.LiveViewResult | undefined> {
3. // build liveView
4. this.liveViewData = await LiveViewController.buildDefaultView(context);
5. let env = liveViewEnvironment;
6. if (!env) {
7. env = {
8. id: 0,
9. event: 'RENT'
10. };
11. }
12. this.liveNotification = LiveNotification.from(context, env);
13. return await this.liveNotification.create(this.liveViewData);
14. }
```

[LiveViewController.ets](https://gitcode.com/harmonyos_samples/bicycle-sharing/blob/master/entry/src/main/ets/liveview/LiveViewController.ets#L49-L63)

3、更新和结束实况窗

```
1. public async updateLiveView(status: number,
2. context: LiveViewContext): Promise<liveViewManager.LiveViewResult | undefined> {
3. // update liveView
4. const liveViewData = this.liveViewData!;
5. switch (status) {
6. case CyclingStatus.WAITING_PAYMENT:
7. liveViewData.primary.title = CyclingConstants.WAITING_PAYMENT_TITLE;
8. liveViewData.primary.content = [
9. {
10. text: CyclingConstants.WAITING_PAYMENT_CONTENT,
11. textColor: CyclingConstants.CONTENT_COLOR
12. }
13. ];
14. liveViewData.primary.clickAction = await LiveViewController.buildWantAgent(context.want);
15. liveViewData.primary.layoutData = new TextLayoutBuilder()
16. .setTitle(CyclingConstants.WAITING_PAYMENT_LAYOUT_TITLE)
17. .setContent(CyclingConstants.WAITING_PAYMENT_LAYOUT_CONTENT)
18. .setDescPic('bike_page.png');

20. liveViewData.capsule = new TextCapsuleBuilder()
21. .setIcon('white_bike.png')
22. .setBackgroundColor(CyclingConstants.CAPSULE_COLOR)
23. .setTitle(CyclingConstants.WAITING_PAYMENT_LAYOUT_TITLE)
24. break;
25. case CyclingStatus.PAYMENT_COMPLETED:
26. liveViewData.primary.title = CyclingConstants.WAITING_PAYMENT_TITLE;
27. liveViewData.primary.clickAction = await LiveViewController.buildWantAgent(context.want);
28. liveViewData.primary.content = [
29. {
30. text: CyclingConstants.WAITING_PAYMENT_PAY,
31. textColor: CyclingConstants.CONTENT_COLOR
32. },
33. {
34. text: CyclingConstants.WAITING_PAYMENT_PAY_SUCCESS,
35. textColor: CyclingConstants.CONTENT_COLOR
36. }
37. ];

39. liveViewData.primary.layoutData = new TextLayoutBuilder()
40. .setTitle(CyclingConstants.WAITING_PAYMENT_PAY_END)
41. .setContent(CyclingConstants.WAITING_PAYMENT_LAYOUT_CONTENT)
42. .setDescPic('bike_page.png');

44. liveViewData.capsule = new TextCapsuleBuilder()
45. .setIcon('white_bike.png')
46. .setBackgroundColor(CyclingConstants.CAPSULE_COLOR)
47. .setTitle(CyclingConstants.PAYMENT_COMPLETED_CAPSULE_TITLE)

49. return await this.liveNotification!.stop(liveViewData);
50. default:
51. break;
52. }

54. return await this.liveNotification!.update(liveViewData);
55. }
```

[LiveViewController.ets](https://gitcode.com/harmonyos_samples/bicycle-sharing/blob/master/entry/src/main/ets/liveview/LiveViewController.ets#L66-L121)

4、开发用户自定义沉浸态实况窗

```
1. export default class LiveViewLockScreenExtAbility extends LiveViewLockScreenExtensionAbility {
2. onCreate() {
3. hilog.info(0x0000, 'LiveViewLockScreenTag', 'LiveViewLockScreenExtAbility onCreate begin.');
4. }

6. onForeground() {
7. hilog.info(0x0000, 'LiveViewLockScreenTag', 'LiveViewLockScreenExtAbility onForeground begin.');
8. }

10. onBackground() {
11. hilog.info(0x0000, 'LiveViewLockScreenTag', 'LiveViewLockScreenExtAbility onBackground begin.');
12. }

14. onDestroy() {
15. hilog.info(0x0000, 'LiveViewLockScreenTag', 'LiveViewLockScreenExtAbility onDestroy begin.');
16. }

18. onSessionCreate(_want: Want, session: UIExtensionContentSession) {
19. hilog.info(0x0000, 'LiveViewLockScreenTag', 'LiveViewLockScreenExtAbility onSessionCreate begin.');
20. try {
21. session.loadContent('pages/LiveViewLockScreenPage');
22. } catch (error) {
23. hilog.error(0x0000, 'LiveViewLockScreenTag', `onSessionCreate error: ${JSON.stringify(error)}.`)
24. }
25. }

27. onSessionDestroy(_session: UIExtensionContentSession) {
28. }
29. }
```

[LiveViewLockScreenExtAbility.ets](https://gitcode.com/harmonyos_samples/bicycle-sharing/blob/master/entry/src/main/ets/entryability/LiveViewLockScreenExtAbility.ets#L21-L50)

5、在LiveViewDataBuilder中配置沉浸态实况窗参数

```
1. this.primary = {
2. title: '',
3. content: [
4. {
5. text: '',
6. textColor: ''
7. }
8. ],
9. keepTime: CyclingConstants.KEEP_TIME,
10. clickAction: undefined,
11. layoutData: undefined,
12. liveViewLockScreenPicture: 'icBike.png',
13. liveViewLockScreenAbilityName: 'LiveViewLockScreenExtAbility',
14. liveViewLockScreenAbilityParameters: parameters
15. };
```

[LiveViewDataBuilder.ets](https://gitcode.com/harmonyos_samples/bicycle-sharing/blob/master/entry/src/main/ets/liveview/LiveViewDataBuilder.ets#L30-L44)

6、在module.json5中配置拓展的ability

```
1. "extensionAbilities": [
2. {
3. "name": "LiveViewLockScreenExtAbility",
4. "type": "liveViewLockScreen",
5. "srcEntry": "./ets/entryability/LiveViewLockScreenExtAbility.ets",
6. "exported": true
7. }
8. ],
```

[module.json5](https://gitcode.com/harmonyos_samples/bicycle-sharing/blob/master/entry/src/main/module.json5#L36-L43)

## 示例代码

* [基于实况窗和扫码功能实现快捷触达的骑行场景](https://gitcode.com/HarmonyOS_Samples/bicycle-sharing)
