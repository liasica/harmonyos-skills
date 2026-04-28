---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-location
title: @system.geolocation (地理位置)
breadcrumb: API参考 > 应用服务 > Location Kit（位置服务） > ArkTS API > 已停止维护的接口 > @system.geolocation (地理位置)
category: harmonyos-references
scraped_at: 2026-04-28T08:17:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:09deaf69d7399bdddaacc7ac3fa33541b542f413504731b94fcc8f2b07c302e7
---

本模块仅提供GNSS定位、网络定位等基本功能。

说明

* 本模块首批接口从API version 3开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 对于Lite Wearable设备类型，该模块长期维护，正常使用。
* 对于支持该模块的其他设备类型，该模块从API Version 9开始，该接口不再维护，推荐使用新接口[geoLocationManager](js-apis-geolocationmanager.md)。

## 导入模块

WearableLite Wearable

```
1. import geolocation from '@system.geolocation';
```

## 权限列表

WearableLite Wearable

ohos.permission.LOCATION

## geolocation.getLocation(deprecated)

WearableLite Wearable

getLocation(options?: GetLocationOption): void

获取设备的地理位置。

说明

除Lite Wearable外，从API version 9开始废弃，建议使用[geoLocationManager.getCurrentLocation](js-apis-geolocationmanager.md#geolocationmanagergetcurrentlocation)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力：** SystemCapability.Location.Location.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [GetLocationOption](js-apis-system-location.md#getlocationoptiondeprecated) | 否 | 单次定位请求的配置参数。 |

**JS示例：**

```
1. <div class="container">
2. <text class="title" style="font-size: {{fontSize}}; color: {{fontColor}};">
3. getLocation
4. </text>
5. <input type="button" value="获取设备的地理位置" style="width: 240px; height: 50px;" onclick="getLocation"></input>
6. </div>
```

```
1. .container {
2. display: flex;
3. flex-direction: column;
4. align-items: center;
5. left: 0px;
6. top: 0px;
7. width: 454px;
8. height: 454px;
9. }

11. .title {
12. font-size: 100px;
13. text-align: center;
14. width: 200px;
15. height: 100px;
16. }

18. .button {
19. font-size: 30px;
20. text-align: center;
21. width: 200px;
22. height: 100px;
23. }
```

```
1. export default {
2. getLocation() {
3. geolocation.getLocation({
4. success: function(data) {
5. console.info('success get location data. latitude:' + data.latitude);
6. },
7. fail: function(data, code) {
8. console.info('fail to get location. code:' + code + ', data:' + data);
9. }
10. });
11. },
12. }
```

## geolocation.getLocationType(deprecated)

WearableLite Wearable

getLocationType(options?: GetLocationTypeOption): void

获取当前设备支持的定位类型。

说明

除Lite Wearable外，从API version 9开始废弃。位置服务子系统仅支持gnss和network两种定位类型，后续不再提供接口查询支持的定位类型。

**系统能力：** SystemCapability.Location.Location.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [GetLocationTypeOption](js-apis-system-location.md#getlocationtypeoptiondeprecated) | 否 | 回调函数，用于接收查询结果，或者接收查询失败的结果。 |

**JS示例：**

```
1. <div class="container">
2. <text class="title" style="font-size: {{fontSize}}; color: {{fontColor}};">
3. getLocationType
4. </text>
5. <input type="button" value="获取当前设备支持的定位类型" style="width: 240px; height: 50px;" onclick="getLocationType"></input>
6. </div>
```

```
1. .container {
2. display: flex;
3. flex-direction: column;
4. align-items: center;
5. left: 0px;
6. top: 0px;
7. width: 454px;
8. height: 454px;
9. }

11. .title {
12. font-size: 100px;
13. text-align: center;
14. width: 200px;
15. height: 100px;
16. }

18. .button {
19. font-size: 30px;
20. text-align: center;
21. width: 200px;
22. height: 100px;
23. }
```

```
1. export default {
2. getLocationType() {
3. geolocation.getLocationType({
4. success: function(data) {
5. console.info('success get location type:' + data.types[0]);
6. },
7. fail: function(data, code) {
8. console.info('fail to get location. code:' + code + ', data:' + data);
9. },
10. });
11. },
12. }
```

## geolocation.subscribe(deprecated)

WearableLite Wearable

subscribe(options: SubscribeLocationOption): void

订阅设备的地理位置信息。多次调用的话，只有最后一次的调用生效。

说明

除Lite Wearable外，从API version 9开始废弃，建议使用[geoLocationManager.on('locationChange')](js-apis-geolocationmanager.md#geolocationmanageronlocationchange)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力：** SystemCapability.Location.Location.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SubscribeLocationOption](js-apis-system-location.md#subscribelocationoptiondeprecated) | 是 | 持续定位的配置参数。 |

**JS示例：**

```
1. <div class="container">
2. <text class="title" style="font-size: {{fontSize}}; color: {{fontColor}};">
3. subscribe
4. </text>
5. <input type="button" value="订阅设备的地理位置信息" style="width: 240px; height: 50px;" onclick="subscribe"></input>
6. </div>
```

```
1. .container {
2. display: flex;
3. flex-direction: column;
4. align-items: center;
5. left: 0px;
6. top: 0px;
7. width: 454px;
8. height: 454px;
9. }

11. .title {
12. font-size: 100px;
13. text-align: center;
14. width: 200px;
15. height: 100px;
16. }

18. .button {
19. font-size: 30px;
20. text-align: center;
21. width: 200px;
22. height: 100px;
23. }
```

```
1. export default {
2. subscribe() {
3. geolocation.subscribe({
4. success: function(data) {
5. console.info('get location. latitude:' + data.latitude);
6. },
7. fail: function(data, code) {
8. console.info('fail to get location. code:' + code + ', data:' + data);
9. },
10. });
11. },
12. }
```

## geolocation.unsubscribe(deprecated)

WearableLite Wearable

unsubscribe(): void

取消订阅设备的地理位置信息。

说明

除Lite Wearable外，从API version 9开始废弃，建议使用[geoLocationManager.off('locationChange')](js-apis-geolocationmanager.md#geolocationmanagerofflocationchange)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力：** SystemCapability.Location.Location.Lite

**JS示例：**

```
1. <div class="container">
2. <text class="title" style="font-size: {{fontSize}}; color: {{fontColor}};">
3. unsubscribe
4. </text>
5. <input type="button" value="取消订阅设备的地理位置信息" style="width: 240px; height: 50px;" onclick="unsubscribe"></input>
6. </div>
```

```
1. .container {
2. display: flex;
3. flex-direction: column;
4. align-items: center;
5. left: 0px;
6. top: 0px;
7. width: 454px;
8. height: 454px;
9. }

11. .title {
12. font-size: 100px;
13. text-align: center;
14. width: 200px;
15. height: 100px;
16. }

18. .button {
19. font-size: 30px;
20. text-align: center;
21. width: 200px;
22. height: 100px;
23. }
```

```
1. export default {
2. unsubscribe() {
3. geolocation.unsubscribe();
4. },
5. }
```

## geolocation.getSupportedCoordTypes(deprecated)

WearableLite Wearable

getSupportedCoordTypes(): Array<string>

获取设备支持的坐标系类型。

说明

除Lite Wearable外，从API version 9开始废弃。位置服务子系统仅支持WGS-84坐标系，后续不再提供接口查询支持的坐标系类型。

**系统能力：** SystemCapability.Location.Location.Lite

**返回值：**

| 类型 | 非空 | 说明 |
| --- | --- | --- |
| Array<string> | 是 | 表示坐标系类型，如[wgs84, gcj02]。 |

**JS示例：**

```
1. <div class="container">
2. <text class="title" style="font-size: {{fontSize}}; color: {{fontColor}};">
3. getSupportedCoordTypes
4. </text>
5. <input type="button" value="获取设备支持的坐标系类型" style="width: 240px; height: 50px;" onclick="getSupportedCoordTypes"></input>
6. </div>
```

```
1. .container {
2. display: flex;
3. flex-direction: column;
4. align-items: center;
5. left: 0px;
6. top: 0px;
7. width: 454px;
8. height: 454px;
9. }

11. .title {
12. font-size: 100px;
13. text-align: center;
14. width: 200px;
15. height: 100px;
16. }

18. .button {
19. font-size: 30px;
20. text-align: center;
21. width: 200px;
22. height: 100px;
23. }
```

```
1. export default {
2. getSupportedCoordTypes() {
3. var types = geolocation.getSupportedCoordTypes();
4. console.info('getSupportedCoordTypes:' types);
5. },
6. }
```

## GetLocationOption(deprecated)

WearableLite Wearable

单次定位请求的配置参数。

说明

除Lite Wearable外，从API version 9开始废弃，建议使用[geoLocationManager.CurrentLocationRequest](js-apis-geolocationmanager.md#currentlocationrequest)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Lite

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeout | number | 否 | 超时时间，单位为ms，默认值为30000。  设置超时，是为了防止出现权限被系统拒绝、定位信号弱或者定位设置不当，导致请求阻塞的情况。超时后会使用fail回调函数。  取值范围为32位正整数。如果设置值小于等于0，系统按默认值处理。 |
| coordType | string | 否 | 坐标系的类型，可通过getSupportedCoordTypes获取可选值，缺省值为wgs84。 |
| success | (data: [GeolocationResponse](js-apis-system-location.md#geolocationresponsedeprecated)) => void | 否 | 接口调用成功的回调函数。 |
| fail | (data: string, code: number) => void | 否 | 接口调用失败的回调函数。data为错误信息，code为错误码。 |
| complete | () => void | 否 | 接口调用结束的回调函数。 |

fail返回错误代码：

| 错误码 | 说明 |
| --- | --- |
| 601 | 获取定位权限失败，失败原因：用户拒绝。 |
| 602 | 权限未声明。 |
| 800 | 超时，失败原因：网络状况不佳或GNSS不可用。 |
| 801 | 系统位置开关未打开。 |
| 802 | 该次调用结果未返回前接口又被重新调用，该次调用失败返回错误码。 |

## GeolocationResponse(deprecated)

WearableLite Wearable

位置信息，包含经度、纬度、定位精度等信息。

说明

除Lite Wearable外，从API version 9开始废弃，建议使用[geoLocationManager.Location](js-apis-geolocationmanager.md#location)替代。

**系统能力**：SystemCapability.Location.Location.Lite

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| longitude | number | 否 | 否 | 设备位置信息：经度。 |
| latitude | number | 否 | 否 | 设备位置信息：纬度。 |
| altitude | number | 否 | 否 | 设备位置信息：海拔。 |
| accuracy | number | 否 | 否 | 设备位置信息：精确度。（该字段由GNSS定位芯片或网络定位服务提供，如果不支持该功能则返回默认值0。Wearable设备上该字段有效；Lite Wearable设备上该字段无效，返回默认值0。） |
| time | number | 否 | 否 | 设备位置信息：时间。 |

## GetLocationTypeOption(deprecated)

WearableLite Wearable

查询定位类型接口的入参，用于存放回调函数，在查询成功或者失败时接收查询结果。

说明

除Lite Wearable外，从API version 9开始废弃。

**系统能力**：SystemCapability.Location.Location.Lite

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| success | (data: [GetLocationTypeResponse](js-apis-system-location.md#getlocationtyperesponsedeprecated)) => void | 否 | 接口调用成功的回调函数。 |
| fail | (data: string, code: number) => void | 否 | 接口调用失败的回调函数。 |
| complete | () => void | 否 | 接口调用结束的回调函数。 |

## GetLocationTypeResponse(deprecated)

WearableLite Wearable

当前设备支持的定位类型列表

说明

除Lite Wearable外，从API version 9开始废弃。

**系统能力**：SystemCapability.Location.Location.Lite

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| types | Array<string> | 否 | 否 | 可选的定位类型['gps', 'network']。 |

## SubscribeLocationOption(deprecated)

WearableLite Wearable

持续定位请求的配置参数。

说明

除Lite Wearable外，从API version 9开始废弃，建议使用[geoLocationManager.CurrentLocationRequest](js-apis-geolocationmanager.md#currentlocationrequest)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Lite

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| coordType | string | 否 | 坐标系的类型，可通过getSupportedCoordTypes获取可选值，默认值为wgs84。 |
| success | (data: [GeolocationResponse](js-apis-system-location.md#geolocationresponsedeprecated)) => void | 是 | 位置信息发生变化的回调函数。 |
| fail | (data: string, code: number) => void | 否 | 接口调用失败的回调函数。 |

fail返回错误代码：

| 错误码 | 说明 |
| --- | --- |
| 601 | 获取定位权限失败，失败原因：用户拒绝。 |
| 602 | 权限未声明。 |
| 801 | 系统位置开关未打开。 |
