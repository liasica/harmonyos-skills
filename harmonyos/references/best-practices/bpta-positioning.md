---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-positioning
title: 位置定位
breadcrumb: 最佳实践 > 应用服务 > 位置定位
category: best-practices
scraped_at: 2026-04-29T14:11:47+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:b2ddd141f812b264d83034e8d8d2b984db16eb72c3080562365e6b474f13fe9c
---

## 概述

在实际应用开发过程中，经常需要用到移动终端设备的位置信息，比如查看所在城市天气、出行打车、旅行导航以及观察运动轨迹等。关于位置定位，位置服务提供了两种[定位方式](../harmonyos-guides/location-kit-intro.md#section884410581151)，分别为GNSS定位和网络定位，如下表所示：

**表1** 定位方式介绍

| 定位方式 | 说明 | 优点 |
| --- | --- | --- |
| GNSS定位 | 基于全球导航卫星系统，包含GPS、GLONASS、北斗、Galileo等，通过导航卫星、设备芯片提供的定位算法，来确定设备准确位置。 | 定位精准 |
| 网络定位 | 通过网络进行定位，包括WLAN、蓝牙定位、基站定位。 | 定位速度快 |

利用系统的位置定位能力，可以在多种开发场景中获得实时准确的位置信息。本文将介绍如下四种常见的定位场景，并给出其具体实现方案，帮助开发者更好地掌握位置定位的基本原理和开发流程。

* [当前位置定位](bpta-positioning.md#section15711161035812)：获取设备的当前位置信息。开发者可以根据实际需求将其应用于多种业务场景，如外卖定位、打车定位等。
* [实时位置定位](bpta-positioning.md#section189692202585)：持续获取设备的实时位置信息。开发者可以将此能力应用于需要实时定位的场景，如步行导航、驾车出行等。
* [应用后台定位](bpta-positioning.md#section32954110416)：将应用切换到后台仍然可以持续获取位置信息。该能力可以用于实现后台应用实时记录运动轨迹等业务场景。
* [历史定位获取](bpta-positioning.md#section1920418138118)：获取系统缓存的最新位置，即最近一次的历史定位信息。该能力可以用于在设备网络信号较弱或对系统功耗比较敏感的场景下获取位置信息。

## 当前位置定位

开发者可以根据实际业务诉求，设置相应的定位策略获取设备的当前位置信息，不同定位策略对应[表1 定位方式介绍](bpta-positioning.md#table1916823418349)中不同的定位方式。

**实现原理**

位置服务提供[getCurrentLocation()](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetcurrentlocation-2)接口来获取当前位置信息，该接口需要用户设置关键参数——定位请求信息。定位请求信息包含定位方式优先级、单次定位超时时间等，分为[CurrentLocationRequest](../harmonyos-references/js-apis-geolocationmanager.md#currentlocationrequest)和[SingleLocationRequest](../harmonyos-references/js-apis-geolocationmanager.md#singlelocationrequest12)两种类型。两种类型对应的定位优先级分别为[LocationRequestPriority](../harmonyos-references/js-apis-geolocationmanager.md#locationrequestpriority)和[LocatingPriority](../harmonyos-references/js-apis-geolocationmanager.md#locatingpriority12)。

**开发步骤**

1. 申请定位权限，具体内容可参考[申请位置权限开发指导](../harmonyos-guides/location-permission-guidelines.md)。
2. 实例化位置信息请求对象，确认当前定位策略。以实例化SingleLocationRequest对象为例，将其定位方式优先级设置为快速获取位置优先，定位超时时间设置为10秒，具体代码如下：

   ```
   1. let request: geoLocationManager.SingleLocationRequest = {
   2. locatingPriority: 0x502,
   3. locatingTimeoutMs: 10000
   4. };
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/location-service/blob/master/entry/src/main/ets/pages/Index.ets#L101-L104)
3. 根据定位策略，调用getCurrentLocation()接口获取当前位置信息。

   ```
   1. geoLocationManager.getCurrentLocation(request).then((location: geoLocationManager.Location) => {
   2. // ...
   3. }).catch((err: BusinessError) => {
   4. hilog.error(0x0000, TAG, `getCurrentLocationPosition failed, code: ${err.code}, message: ${err.message}`);
   5. // ...
   6. });
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/location-service/blob/master/entry/src/main/ets/pages/Index.ets#L107-L119)
4. 调用[getAddressesFromLocation()](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetaddressesfromlocation)接口进行逆地理编码转化，将位置坐标信息转换为对应的地理位置描述。

   ```
   1. geoLocationManager.getAddressesFromLocation(reverseGeocodeRequest, async (err, data) => {
   2. if (data) {
   3. this.address = data[0]?.placeName || '';
   4. // ...
   5. } else {
   6. hilog.error(0x0000, TAG, `getAddressesFromLocation failed, code: ${err.code}, message: ${err.message}`);
   7. // ...
   8. }
   9. });
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/location-service/blob/master/entry/src/main/ets/pages/Index.ets#L216-L235)
5. 运行效果如下图所示

   **图1** 获取当前位置信息效果展示  
   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/1gPcp46SSGKkAmvLVHgVAA/zh-cn_image_0000002193852028.png?HW-CC-KV=V1&HW-CC-Date=20260429T061146Z&HW-CC-Expire=86400&HW-CC-Sign=A9542B9519710BCBBA15633A459BF340B3862E1E86659038DD595CFDF44F9342 "点击放大")

## 实时位置定位

开发者可以根据实际[用户活动场景](../harmonyos-references/js-apis-geolocationmanager.md#useractivityscenario12)或[功耗场景](../harmonyos-references/js-apis-geolocationmanager.md#powerconsumptionscenario12)，设置相应的定位策略持续获取设备的位置信息，不同定位策略对应[表1 定位方式介绍](bpta-positioning.md#table1916823418349)中不同的定位方式。

**实现原理**

位置服务通过[on('locationChange')](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanageronlocationchange)接口订阅位置变化情况，实现持续获取设备位置信息的场景诉求。该订阅服务需要申请定位请求信息[LocationRequest](../harmonyos-references/js-apis-geolocationmanager.md#locationrequest)或者[ContinuousLocationRequest](../harmonyos-references/js-apis-geolocationmanager.md#continuouslocationrequest12)，并在请求信息中设置定位场景类型和位置信息上报时间间隔。

**开发步骤**

1. 申请定位权限，具体内容可参考[申请位置权限开发指导](../harmonyos-guides/location-permission-guidelines.md)。
2. 实例化位置信息请求对象，确认持续定位策略。以实例化ContinuousLocationRequest为例，将定位场景类型设置为导航场景，位置信息上报时间间隔设置为1秒，具体代码如下：

   ```
   1. let request: geoLocationManager.ContinuousLocationRequest = {
   2. interval: 1,
   3. locationScenario: 0x401
   4. };
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/location-service/blob/master/entry/src/main/ets/pages/Index.ets#L129-L132)
3. 根据定位策略，调用on('locationChange')开启位置变化订阅，并发起定位请求，持续获取当前位置信息。

   ```
   1. geoLocationManager.on('locationChange', request, this.locationChange);
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/location-service/blob/master/entry/src/main/ets/pages/Index.ets#L136-L136)
4. 在on('locationChange')的回调函数中，调用[getAddressesFromLocation()](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetaddressesfromlocation)接口进行逆地理编码转化，将坐标信息转换为对应的地理位置描述。

   ```
   1. geoLocationManager.getAddressesFromLocation(reverseGeocodeRequest, async (err, data) => {
   2. if (data) {
   3. this.address = data[0]?.placeName || '';
   4. // ...
   5. } else {
   6. hilog.error(0x0000, TAG, `getAddressesFromLocation failed, code: ${err.code}, message: ${err.message}`);
   7. // ...
   8. }
   9. });
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/location-service/blob/master/entry/src/main/ets/pages/Index.ets#L216-L235)
5. 在不需要获取位置信息时，及时关闭位置变化订阅，并删除对应的定位请求，减少设备功耗。

   ```
   1. try {
   2. geoLocationManager.off('locationChange', this.locationChange);
   3. } catch (err) {
   4. hilog.error(0x0000, TAG, `offLocationChange failed, code: ${err.code}, message: ${err.message}`);
   5. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/location-service/blob/master/entry/src/main/ets/pages/Index.ets#L163-L167)
6. 运行效果如下图所示

   **图2** 持续获取实时位置信息效果展示  
   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/PhAhypwrRDSXt55e6E5R_Q/zh-cn_image_0000002194011616.png?HW-CC-KV=V1&HW-CC-Date=20260429T061146Z&HW-CC-Expire=86400&HW-CC-Sign=B6E8F47811DC1D9F27BB8E0FAC1AA9070ACEF4BACEE097E84B31CA450A5F5682 "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/he6uBgs8QcmNLjBeFTmfqw/zh-cn_image_0000002229451909.png?HW-CC-KV=V1&HW-CC-Date=20260429T061146Z&HW-CC-Expire=86400&HW-CC-Sign=5C2361828AFBF9B9B4EFB0BEC48EE57DF161744DC6607FE75E205C613BE5B452)

## 应用后台定位

当用户将应用切至后台且依然需要获取设备的位置信息时，可以使用该方式进行后台定位。

**实现原理**

应用后台定位需要申请后台定位权限ohos.permission.LOCATION\_IN\_BACKGROUND和长时任务权限ohos.permission.KEEP\_BACKGROUND\_RUNNING。申请了相关权限后，开启[任务模式](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundmode)为定位导航的[长时任务](../harmonyos-guides/continuous-task.md)，并在其回调接口中通过[on('locationChange')](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanageronlocationchange)订阅位置变化情况，在应用后台持续获取当前位置信息。

**开发步骤**

1. 申请后台定位权限，具体内容可参考[申请位置权限开发指导](../harmonyos-guides/location-permission-guidelines.md)。
2. 在模块的module.json5文件中，申请长时任务权限，并将长时任务模式设置为定位导航类型。

   申请长时任务权限

   ```
   1. {
   2. "name": "ohos.permission.KEEP_BACKGROUND_RUNNING",
   3. "reason": "$string:running_background",
   4. "usedScene": {
   5. "abilities": [
   6. "EntryAbility"
   7. ],
   8. "when": "always"
   9. }
   10. },
   ```

   [module.json5](https://gitcode.com/HarmonyOS_Samples/location-service/blob/master/entry/src/main/module.json5#L93-L102)

   设置长时任务模式为定位导航类型

   ```
   1. "abilities": [
   2. {
   3. // ...
   4. "backgroundModes": [
   5. "location"
   6. ],
   7. // ...
   8. }
   9. ],
   ```

   [module.json5](https://gitcode.com/HarmonyOS_Samples/location-service/blob/master/entry/src/main/module.json5#L31-L59)
3. 开启任务模式为定位导航类型的长时任务，在其回调接口中开启位置变化订阅，并发起定位请求，在应用后台持续获取当前位置信息。

   开启长时任务

   ```
   1. startContinuousTask(): void {
   2. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   3. if (!context) {
   4. return;
   5. }
   6. let wantAgentInfo: wantAgent.WantAgentInfo = {
   7. wants: [
   8. {
   9. bundleName: context.abilityInfo.bundleName,
   10. abilityName: context.abilityInfo.name
   11. }
   12. ],
   13. operationType: wantAgent.OperationType.START_ABILITY,
   14. requestCode: 1,
   15. wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
   16. };

   18. wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj) => {
   19. backgroundTaskManager.startBackgroundRunning(context,
   20. backgroundTaskManager.BackgroundMode.LOCATION, wantAgentObj).then(() => {
   21. this.onLocationChange();
   22. hilog.info(0x0000, TAG, 'startBackgroundRunning succeeded');
   23. }).catch((err: BusinessError) => {
   24. hilog.error(0x0000, TAG, `startBackgroundRunning failed, cause:  ${JSON.stringify(err)}`);
   25. });
   26. }).catch((err: BusinessError) => {
   27. hilog.error(0x0000, TAG, `getWantAgent failed, cause:  ${JSON.stringify(err)}`);
   28. });
   29. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/location-service/blob/master/entry/src/main/ets/pages/Index.ets#L246-L274)

   订阅位置变化情况

   ```
   1. onLocationChange(): void {
   2. let request: geoLocationManager.ContinuousLocationRequest = {
   3. interval: 1,
   4. locationScenario: 0x401
   5. };
   6. try {
   7. geoLocationManager.on('locationChange', request, this.locationChange);
   8. // ...
   9. } catch (err) {
   10. hilog.error(0x0000, TAG, `onLocationChange failed, code: ${err.code}, message: ${err.message}`);
   11. // ...
   12. }
   13. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/location-service/blob/master/entry/src/main/ets/pages/Index.ets#L127-L154)
4. 在位置变化的回调中，调用[getAddressesFromLocation()](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetaddressesfromlocation)接口进行逆地理编码转化，将坐标信息转换为对应的地理位置描述。

   ```
   1. geoLocationManager.getAddressesFromLocation(reverseGeocodeRequest, async (err, data) => {
   2. if (data) {
   3. this.address = data[0]?.placeName || '';
   4. // ...
   5. } else {
   6. hilog.error(0x0000, TAG, `getAddressesFromLocation failed, code: ${err.code}, message: ${err.message}`);
   7. // ...
   8. }
   9. });
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/location-service/blob/master/entry/src/main/ets/pages/Index.ets#L216-L235)
5. 当不需要在应用后台获取位置信息时，及时关闭长时任务和位置变化订阅，并删除对应的定位请求，减少设备功耗。

   关闭长时任务

   ```
   1. stopContinuousTask(): void {
   2. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   3. if (!context) {
   4. return;
   5. }
   6. backgroundTaskManager.stopBackgroundRunning(context).then(() => {
   7. if (!this.isOnLocationChange) {
   8. this.offLocationChange();
   9. }
   10. hilog.info(0x0000, TAG, 'stopBackgroundRunning succeeded');
   11. }).catch((err: BusinessError) => {
   12. hilog.error(0x0000, TAG, `stopBackgroundRunning failed, cause:  ${JSON.stringify(err)}`);
   13. });
   14. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/location-service/blob/master/entry/src/main/ets/pages/Index.ets#L281-L294)

   关闭位置变化订阅

   ```
   1. offLocationChange(): void {
   2. try {
   3. geoLocationManager.off('locationChange', this.locationChange);
   4. } catch (err) {
   5. hilog.error(0x0000, TAG, `offLocationChange failed, code: ${err.code}, message: ${err.message}`);
   6. }
   7. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/location-service/blob/master/entry/src/main/ets/pages/Index.ets#L161-L169)
6. 运行效果如下图所示

**图3** 在应用后台持续获取位置信息效果展示  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/IUVzzdrqTtyjsVoxw7pizA/zh-cn_image_0000002229337413.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061146Z&HW-CC-Expire=86400&HW-CC-Sign=DC6BAF9FBB42A5FA1F59FCC40599235B3CB72E8142587B7FFE36309159F517EB "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/9Uh88wwuRUeNa1KlZw9A-g/zh-cn_image_0000002229451897.png?HW-CC-KV=V1&HW-CC-Date=20260429T061146Z&HW-CC-Expire=86400&HW-CC-Sign=0C195B14157AB8B215819B833980D7C8EA608A18A9B26BB780788E8FB98DCA07)

## 历史定位获取

当用户设备网络信号较弱或者对系统功耗比较敏感时，可以先获取系统缓存的最新位置，即最近一次的历史定位信息。

**实现原理**

位置服务通过[getLastLocation()](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetlastlocation)接口来获取系统缓存的最新位置信息。该接口参数列表为空，返回值为[Location](../harmonyos-references/js-apis-geolocationmanager.md#location)位置信息。

**开发步骤**

1. 申请定位权限，具体内容可参考[申请位置权限开发指导](../harmonyos-guides/location-permission-guidelines.md)。
2. 调用getLastLocation()接口获取系统缓存的最新位置信息。

   ```
   1. let location = geoLocationManager.getLastLocation();
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/location-service/blob/master/entry/src/main/ets/pages/Index.ets#L84-L84)
3. 调用[getAddressesFromLocation()](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetaddressesfromlocation)接口进行逆地理编码转化，将坐标信息转换为对应的地理位置描述。

   ```
   1. geoLocationManager.getAddressesFromLocation(reverseGeocodeRequest, async (err, data) => {
   2. if (data) {
   3. this.address = data[0]?.placeName || '';
   4. // ...
   5. } else {
   6. hilog.error(0x0000, TAG, `getAddressesFromLocation failed, code: ${err.code}, message: ${err.message}`);
   7. // ...
   8. }
   9. });
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/location-service/blob/master/entry/src/main/ets/pages/Index.ets#L216-L235)
4. 运行效果如下图所示

   **图4** 获取缓存位置信息效果展示  
   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/Ge-eBsyWRuWhN7E8gfOSmQ/zh-cn_image_0000002193852040.png?HW-CC-KV=V1&HW-CC-Date=20260429T061146Z&HW-CC-Expire=86400&HW-CC-Sign=57F71F2FCCD1551DADDCC5A7A6004BE147E95F09F01ACD53AC594E5C70B61814 "点击放大")

## 常见问题

### 位置定位不准或者位置信息有偏差

**问题现象**

在定位过程中，获取的定位结果不准确，或者将定位结果标记在地图上时出现偏差。

**可能原因**

* 定位权限设置错误，例如设置的定位权限为模糊定位而非精准定位。
* 定位策略设置错误，例如设置的策略为快速获取位置优先（蓝牙、基站、WLAN等网络定位方式）而非精度优先（GNSS卫星定位方式）。
* 在获取定位结果后，未进行坐标纠偏就将结果标记在地图上。华为地图在中国大陆、中国香港和中国澳门使用的是GCJ02坐标系，而定位返回结果使用的是WGS84坐标系，若直接将结果标记在华为地图上，因坐标值不同，展示位置会有偏移。

**解决措施**

* 针对定位权限设置错误问题，需要申请精准定位权限ohos.permission.LOCATION，并在应用中授权获取精准位置。
* 针对定位策略设置错误问题，需要将定位策略设置为精度优先，采用GNSS卫星定位方式。
* 针对定位结果在地图上的标记偏差问题，在中国大陆、中国香港和中国澳门如果使用WGS84坐标调用Map Kit服务，需要先将其转换为GCJ02坐标系再访问，详情见[坐标纠偏](../harmonyos-guides/map-convert-coordinate.md)。

### 位置定位失败

**问题现象**

无法使用定位功能获取位置信息。

**可能原因**

* 系统位置开关为关闭状态。
* 网络信号不佳，导致定位超时。
* 系统无缓存位置信息，导致获取上一次位置失败。

**解决措施**

* 打开系统位置开关。
* 检查设备是否联网、是否插入SIM卡、WiFi开关是否开启等。
* 移动至开阔地带再发起定位。
* 在系统无缓存位置的情况下，使用[getCurrentLocation()](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetcurrentlocation-2)接口获取当前位置信息。

### 系统缓存位置信息不准确

**问题现象**

使用[getCurrentLocation()](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetcurrentlocation-2)接口获取当前定位信息后，再使用[getLastLocation()](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetlastlocation)接口获取缓存定位信息，两次获取的定位信息不一致。

**可能原因**

所有应用公用系统中的同一份缓存定位信息，有可能在两次接口调用之间有其他应用发起定位，刷新了系统中的缓存定位信息。

**解决措施**

对比获取定位信息的时间，根据时间判断缓存定位信息是否更新。

## 示例代码

* [基于位置服务获取设备定位信息](https://gitcode.com/harmonyos_samples/location-service)
