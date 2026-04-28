---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/location-guidelines
title: 获取设备的位置信息开发指导(ArkTS)
breadcrumb: 指南 > 应用服务 > Location Kit（位置服务） > 获取设备的位置信息开发指导 > 获取设备的位置信息开发指导(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d60a54286744818467874ef52e3976f00a6e75de4d9a321494065ddb87446c5f
---

## 场景概述

开发者可以调用HarmonyOS位置相关接口，获取设备实时位置，或者最近的历史位置，以及监听设备的位置变化。

对于位置敏感的应用业务，建议获取设备实时位置信息。如果不需要设备实时位置信息，并且希望尽可能的节省耗电，开发者可以考虑获取最近的历史位置。

## 接口说明

获取设备的位置信息所使用的接口如下，详细说明参见Location Kit API参考：[@ohos.geoLocationManager (位置服务)](../harmonyos-references/js-apis-geolocationmanager.md)。

本模块能力仅支持WGS-84坐标系。如需转换成其他坐标系，请参考[坐标转换工具](map-convert-coordinate.md)。

| 接口名 | 功能描述 |
| --- | --- |
| [geoLocationManager.on('locationChange')](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanageronlocationchange) | 开启位置变化订阅，并发起定位请求。 |
| [geoLocationManager.off('locationChange')](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagerofflocationchange) | 关闭位置变化订阅，并删除对应的定位请求。 |
| [geoLocationManager.getCurrentLocation](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetcurrentlocation) | 获取当前位置，使用callback回调异步返回结果。 |
| [geoLocationManager.getCurrentLocation](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetcurrentlocation-2) | 获取当前位置，使用Promise方式异步返回结果。 |
| [geoLocationManager.getLastLocation](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetlastlocation) | 获取最近一次定位结果。 |
| [geoLocationManager.isLocationEnabled](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagerislocationenabled) | 判断位置服务是否已经开启。 |

## 开发步骤

1. 获取设备的位置信息，需要有位置权限，位置权限申请的方法和步骤见[申请位置权限开发指导](location-permission-guidelines.md)。
2. 导入geoLocationManager模块，所有与基础定位能力相关的功能API，都是通过该模块提供的。

   ```
   1. import { geoLocationManager } from '@kit.LocationKit';
   ```
3. 调用获取位置接口之前需要先判断位置开关是否打开。

   查询当前位置开关状态，返回结果为布尔值，true代表位置开关开启，false代表位置开关关闭，示例代码如下：

   ```
   1. import { geoLocationManager } from '@kit.LocationKit';
   2. try {
   3. let locationEnabled = geoLocationManager.isLocationEnabled();
   4. } catch (err) {
   5. console.error("errCode:" + err.code + ", message:"  + err.message);
   6. }
   ```

   如果位置开关未开启，可以拉起全局开关设置弹框，引导用户打开位置开关，具体可参考[requestGlobalSwitch](../harmonyos-references/js-apis-abilityaccessctrl.md#requestglobalswitch12)。
4. 单次获取当前设备位置。多用于查看当前位置、签到打卡、服务推荐等场景。

   * 方式一：获取系统缓存的最新位置。

     如果系统当前没有缓存位置会返回错误码。

     推荐优先使用该接口获取位置，可以减少系统功耗。

     如果对位置的新鲜度比较敏感，可以先获取缓存位置，将位置中的时间戳与当前时间对比，若新鲜度不满足预期可以使用方式二获取位置。

     ```
     1. import { geoLocationManager } from '@kit.LocationKit';
     2. import { BusinessError } from '@kit.BasicServicesKit';
     3. try {
     4. let location = geoLocationManager.getLastLocation();
     5. } catch (err) {
     6. console.error("errCode:" + JSON.stringify(err));
     7. }
     ```
   * 方式二：获取当前位置。

     首先要实例化[SingleLocationRequest](../harmonyos-references/js-apis-geolocationmanager.md#singlelocationrequest12)对象，用于告知系统该向应用提供何种类型的位置服务，以及单次定位超时时间。

     + 设置LocatingPriority：

       如果对位置的返回精度要求较高，建议LocatingPriority参数优先选择PRIORITY\_ACCURACY，会将一段时间内精度较好的结果返回给应用。

       如果对定位速度要求较高，建议LocatingPriority参数选择PRIORITY\_LOCATING\_SPEED，会将最先拿到的定位结果返回给应用。

       两种定位策略均会同时使用GNSS定位和网络定位技术，以便在室内和户外场景下均可以获取到位置结果，对设备的硬件资源消耗较大，功耗也较大。
     + 设置locatingTimeoutMs：

       因为设备环境、设备所处状态、系统功耗管控策略等的影响，定位返回的时延会有较大波动，建议把单次定位超时时间设置为10秒。

     以快速定位策略(PRIORITY\_LOCATING\_SPEED)为例，调用方式如下：

     ```
     1. import { geoLocationManager } from '@kit.LocationKit';
     2. import { BusinessError } from '@kit.BasicServicesKit';
     3. let request: geoLocationManager.SingleLocationRequest = {
     4. 'locatingPriority': geoLocationManager.LocatingPriority.PRIORITY_LOCATING_SPEED,
     5. 'locatingTimeoutMs': 10000
     6. }
     7. try {
     8. geoLocationManager.getCurrentLocation(request).then((result) => { // 调用getCurrentLocation获取当前设备位置，通过promise接收上报的位置
     9. console.info('current location: ' + JSON.stringify(result));
     10. })
     11. .catch((error:BusinessError) => { // 接收上报的错误码
     12. console.error('promise, getCurrentLocation: error=' + JSON.stringify(error));
     13. });
     14. } catch (err) {
     15. console.error("errCode:" + JSON.stringify(err));
     16. }
     ```

   通过本模块获取到的坐标均为WGS-84坐标系坐标点，如需使用其它坐标系类型的坐标点，请进行坐标系转换后再使用。

   可参考Map Kit提供的地图计算工具进行[坐标转换](map-convert-coordinate.md)。
5. 持续定位。多用于导航、运动轨迹、出行等场景。

   首先要实例化[ContinuousLocationRequest](../harmonyos-references/js-apis-geolocationmanager.md#continuouslocationrequest12)对象，用于告知系统该向应用提供何种类型的位置服务，以及位置结果上报的频率。

   * 设置locationScenario：

     建议locationScenario参数优先根据应用的使用场景进行设置，该参数枚举值定义参见[UserActivityScenario](../harmonyos-references/js-apis-geolocationmanager.md#useractivityscenario12)，例如地图在导航时使用NAVIGATION参数，可以持续在室内和室外场景获取位置用于导航。
   * 设置interval：

     表示上报位置信息的时间间隔，单位是秒，默认值为1秒。如果对位置上报时间间隔无特殊要求，可以不填写该字段。

   以地图导航场景为例，调用方式如下：

   ```
   1. import { geoLocationManager } from '@kit.LocationKit';
   2. let request: geoLocationManager.ContinuousLocationRequest= {
   3. 'interval': 1,
   4. 'locationScenario': geoLocationManager.UserActivityScenario.NAVIGATION
   5. }
   6. let locationCallback = (location:geoLocationManager.Location):void => {
   7. console.info('locationCallback: data: ' + JSON.stringify(location));
   8. };
   9. try {
   10. geoLocationManager.on('locationChange', request, locationCallback);
   11. } catch (err) {
   12. console.error("errCode:" + JSON.stringify(err));
   13. }
   ```

   如果不主动结束定位可能导致设备功耗高，耗电快；建议在不需要获取定位信息时及时结束定位。

   ```
   1. // 该回调函数需要与on接口传入的回调函数保持一致。
   2. geoLocationManager.off('locationChange', locationCallback);
   ```
