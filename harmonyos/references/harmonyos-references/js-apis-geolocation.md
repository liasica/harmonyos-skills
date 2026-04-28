---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-geolocation
title: @ohos.geolocation (位置服务)
breadcrumb: API参考 > 应用服务 > Location Kit（位置服务） > ArkTS API > 已停止维护的接口 > @ohos.geolocation (位置服务)
category: harmonyos-references
scraped_at: 2026-04-28T08:17:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d69ac0348bad10fb1109b8a1f077779011863932d8c736d7c5b0db2a64425b61
---

位置服务提供GNSS定位、网络定位、地理编码、逆地理编码、国家码和地理围栏等基本功能。

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API Version 9开始，该接口不再维护，推荐使用新接口[geoLocationManager](js-apis-geolocationmanager.md)。

本模块能力仅支持WGS-84坐标系。

## 申请权限

PhonePC/2in1TabletTVWearable

应用在使用系统能力前，需要检查是否已经获取用户授权访问设备位置信息。如未获得授权，可以向用户申请需要的位置权限，申请方式请参考下文。

系统提供的定位权限有：

* ohos.permission.LOCATION
* ohos.permission.APPROXIMATELY\_LOCATION
* ohos.permission.LOCATION\_IN\_BACKGROUND

访问设备的位置信息，必须申请权限，并且获得用户授权。

API9之前的版本，申请ohos.permission.LOCATION即可。

API9及之后的版本，需要申请ohos.permission.APPROXIMATELY\_LOCATION或者同时申请ohos.permission.APPROXIMATELY\_LOCATION和ohos.permission.LOCATION；无法单独申请ohos.permission.LOCATION。

| 使用的API版本 | 申请位置权限 | 申请结果 | 位置的精确度 |
| --- | --- | --- | --- |
| 小于9 | ohos.permission.LOCATION | 成功 | 获取到精准位置，精准度在米级别。 |
| 大于等于9 | ohos.permission.LOCATION | 失败 | 无法获取位置。 |
| 大于等于9 | ohos.permission.APPROXIMATELY\_LOCATION | 成功 | 获取到模糊位置，精确度为5公里。 |
| 大于等于9 | ohos.permission.APPROXIMATELY\_LOCATION和ohos.permission.LOCATION | 成功 | 获取到精准位置，精准度在米级别。 |

如果应用在后台运行时也需要访问设备位置，需要申请LOCATION类型的长时任务，这样应用在切入后台之后，系统可以继续上报位置信息。长时任务申请可参考[长时任务](../harmonyos-guides/continuous-task.md)。

应用如需使用ohos.permission.LOCATION\_IN\_BACKGROUND权限，需要在设置界面由用户手动授予，具体授权方式可参考[ohos.permission.LOCATION\_IN\_BACKGROUND权限说明](../harmonyos-guides/permissions-for-all-user.md#ohospermissionlocation_in_background)。

开发者可以在应用配置文件中声明所需要的权限，具体可参考[向用户申请授权](../harmonyos-guides/request-user-authorization.md)。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import geolocation from '@ohos.geolocation';
```

## geolocation.on('locationChange')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'locationChange', request: LocationRequest, callback: Callback<Location>): void

开启位置变化订阅，并发起定位请求。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[geoLocationManager.on('locationChange')](js-apis-geolocationmanager.md#geolocationmanageronlocationchange)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“locationChange”，表示位置变化。 |
| request | [LocationRequest](js-apis-geolocation.md#locationrequestdeprecated) | 是 | 设置位置请求参数。 |
| callback | Callback<[Location](js-apis-geolocation.md#locationdeprecated)> | 是 | 回调函数，返回位置信息。 |

**示例**

```
1. import geolocation from '@ohos.geolocation';
2. let requestInfo:geolocation.LocationRequest = {'priority': 0x203, 'scenario': 0x300, 'timeInterval': 0, 'distanceInterval': 0, 'maxAccuracy': 0};
3. let locationChange = (location:geolocation.Location):void => {
4. console.info('locationChanger: data: ' + JSON.stringify(location));
5. };
6. geolocation.on('locationChange', requestInfo, locationChange);
```

## geolocation.off('locationChange')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'locationChange', callback?: Callback<Location>): void

关闭位置变化订阅，并删除对应的定位请求。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[geoLocationManager.off('locationChange')](js-apis-geolocationmanager.md#geolocationmanagerofflocationchange)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“locationChange”，表示位置变化。 |
| callback | Callback<[Location](js-apis-geolocation.md#locationdeprecated)> | 否 | 需要取消订阅的回调函数。该回调函数需要与on接口传入的回调函数保持一致。若无此参数，则取消当前类型的所有订阅。 |

**示例**

```
1. import geolocation from '@ohos.geolocation';
2. let requestInfo:geolocation.LocationRequest = {'priority': 0x203, 'scenario': 0x300, 'timeInterval': 0, 'distanceInterval': 0, 'maxAccuracy': 0};
3. let locationChange = (location:geolocation.Location):void => {
4. console.info('locationChanger: data: ' + JSON.stringify(location));
5. };
6. geolocation.on('locationChange', requestInfo, locationChange);
7. geolocation.off('locationChange', locationChange);
```

## geolocation.on('locationServiceState')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'locationServiceState', callback: Callback<boolean>): void

订阅位置服务状态变化。使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[geoLocationManager.on('locationEnabledChange')](js-apis-geolocationmanager.md#geolocationmanageronlocationenabledchange)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“locationServiceState”，表示位置服务状态。 |
| callback | Callback<boolean> | 是 | 回调函数。返回true表示打开位置服务；返回false表示关闭位置服务。 |

**示例**

```
1. import geolocation from '@ohos.geolocation';
2. let locationServiceState = (state:boolean):void => {
3. console.info('locationServiceState: ' + JSON.stringify(state));
4. }
5. geolocation.on('locationServiceState', locationServiceState);
```

## geolocation.off('locationServiceState')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'locationServiceState', callback?: Callback<boolean>): void

取消订阅位置服务状态变化。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[geoLocationManager.off('locationEnabledChange')](js-apis-geolocationmanager.md#geolocationmanagerofflocationenabledchange)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“locationServiceState”，表示位置服务状态。 |
| callback | Callback<boolean> | 否 | 需要取消订阅的回调函数。Callback返回true表示位置服务处于开启状态；返回false表示位置服务处于关闭状态。该回调函数需要与on接口传入的回调函数保持一致。若无此参数，则取消当前类型的所有订阅。 |

**示例**

```
1. import geolocation from '@ohos.geolocation';
2. let locationServiceState = (state:boolean):void => {
3. console.info('locationServiceState: state: ' + JSON.stringify(state));
4. }
5. geolocation.on('locationServiceState', locationServiceState);
6. geolocation.off('locationServiceState', locationServiceState);
```

## geolocation.on('cachedGnssLocationsReporting')(deprecated)

PhoneTabletWearable

on(type: 'cachedGnssLocationsReporting', request: CachedGnssLocationsRequest, callback: Callback<Array<Location>>): void

订阅缓存GNSS定位结果上报事件。使用callback异步回调。

说明

从API version 8开始支持。

从API version 9开始废弃，建议使用[geoLocationManager.on('cachedGnssLocationsChange')](js-apis-geolocationmanager.md#geolocationmanageroncachedgnsslocationschange)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“cachedGnssLocationsReporting”，表示GNSS缓存定位结果上报。 |
| request | [CachedGnssLocationsRequest](js-apis-geolocation.md#cachedgnsslocationsrequestdeprecated) | 是 | GNSS缓存功能配置参数。 |
| callback | Callback<Array<[Location](js-apis-geolocation.md#locationdeprecated)>> | 是 | 回调函数，返回GNSS缓存位置。 |

**示例**

```
1. import geolocation from '@ohos.geolocation';
2. let cachedLocationsCb = (locations:Array<geolocation.Location>):void => {
3. console.info('cachedGnssLocationsReporting: locations: ' + JSON.stringify(locations));
4. }
5. let requestInfo:geolocation.CachedGnssLocationsRequest = {'reportingPeriodSec': 10, 'wakeUpCacheQueueFull': true};
6. geolocation.on('cachedGnssLocationsReporting', requestInfo, cachedLocationsCb);
```

## geolocation.off('cachedGnssLocationsReporting')(deprecated)

PhoneTabletWearable

off(type: 'cachedGnssLocationsReporting', callback?: Callback<Array<Location>>): void

取消订阅缓存GNSS定位结果上报事件。

说明

从API version 8开始支持。

从API version 9开始废弃，建议使用[geoLocationManager.off('cachedGnssLocationsChange')](js-apis-geolocationmanager.md#geolocationmanageroffcachedgnsslocationschange)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“cachedGnssLocationsReporting”，表示GNSS缓存定位结果上报。 |
| callback | Callback<Array<[Location](js-apis-geolocation.md#locationdeprecated)>> | 否 | 需要取消订阅的回调函数。该回调函数需要与on接口传入的回调函数保持一致。若无此参数，则取消当前类型的所有订阅。 |

**示例**

```
1. import geolocation from '@ohos.geolocation';
2. let cachedLocationsCb = (locations:Array<geolocation.Location>):void => {
3. console.info('cachedGnssLocationsReporting: locations: ' + JSON.stringify(locations));
4. }
5. let requestInfo:geolocation.CachedGnssLocationsRequest = {'reportingPeriodSec': 10, 'wakeUpCacheQueueFull': true};
6. geolocation.on('cachedGnssLocationsReporting', requestInfo, cachedLocationsCb);
7. geolocation.off('cachedGnssLocationsReporting');
```

## geolocation.on('gnssStatusChange')(deprecated)

PhoneTabletWearable

on(type: 'gnssStatusChange', callback: Callback<SatelliteStatusInfo>): void

订阅GNSS卫星状态信息上报事件。使用callback异步回调。

说明

从API version 8开始支持。

从API version 9开始废弃，建议使用[geoLocationManager.on('satelliteStatusChange')](js-apis-geolocationmanager.md#geolocationmanageronsatellitestatuschange)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“gnssStatusChange”，表示订阅GNSS卫星状态信息上报。 |
| callback | Callback<[SatelliteStatusInfo](js-apis-geolocation.md#satellitestatusinfodeprecated)> | 是 | 回调函数，返回GNSS卫星状态信息。 |

**示例**

```
1. import geolocation from '@ohos.geolocation';
2. let gnssStatusCb = (satelliteStatusInfo:geolocation.SatelliteStatusInfo):void => {
3. console.info('gnssStatusChange: ' + JSON.stringify(satelliteStatusInfo));
4. }
5. geolocation.on('gnssStatusChange', gnssStatusCb);
```

## geolocation.off('gnssStatusChange')(deprecated)

PhoneTabletWearable

off(type: 'gnssStatusChange', callback?: Callback<SatelliteStatusInfo>): void

取消订阅GNSS卫星状态信息上报事件。

说明

从API version 8开始支持。

从API version 9开始废弃，建议使用[geoLocationManager.off('satelliteStatusChange')](js-apis-geolocationmanager.md#geolocationmanageroffsatellitestatuschange)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“gnssStatusChange”，表示订阅GNSS卫星状态信息上报。 |
| callback | Callback<[SatelliteStatusInfo](js-apis-geolocation.md#satellitestatusinfodeprecated)> | 否 | 需要取消订阅的回调函数。该回调函数需要与on接口传入的回调函数保持一致。若无此参数，则取消当前类型的所有订阅。 |

**示例**

```
1. import geolocation from '@ohos.geolocation';
2. let gnssStatusCb = (satelliteStatusInfo:geolocation.SatelliteStatusInfo) => {
3. console.info('gnssStatusChange: ' + JSON.stringify(satelliteStatusInfo));
4. }
5. geolocation.on('gnssStatusChange', gnssStatusCb);
6. geolocation.off('gnssStatusChange', gnssStatusCb);
```

## geolocation.on('nmeaMessageChange')(deprecated)

PhoneTabletWearable

on(type: 'nmeaMessageChange', callback: Callback<string>): void

订阅GNSS NMEA信息上报事件。使用callback异步回调。

说明

从API version 8开始支持。

从API version 9开始废弃，建议使用[geoLocationManager.on('nmeaMessage')](js-apis-geolocationmanager.md#geolocationmanageronnmeamessage)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“nmeaMessageChange”，表示订阅GNSS NMEA信息上报。 |
| callback | Callback<string> | 是 | 回调函数，返回GNSS NMEA信息。 |

**示例**

```
1. import geolocation from '@ohos.geolocation';
2. let nmeaCb = (str:string):void => {
3. console.info('nmeaMessageChange: ' + JSON.stringify(str));
4. }
5. geolocation.on('nmeaMessageChange', nmeaCb );
```

## geolocation.off('nmeaMessageChange')(deprecated)

PhoneTabletWearable

off(type: 'nmeaMessageChange', callback?: Callback<string>): void

取消订阅GNSS NMEA信息上报事件。

说明

从API version 8开始支持。

从API version 9开始废弃，建议使用[geoLocationManager.off('nmeaMessage')](js-apis-geolocationmanager.md#geolocationmanageroffnmeamessage)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“nmeaMessageChange”，表示订阅GNSS NMEA信息上报。 |
| callback | Callback<string> | 否 | 需要取消订阅的回调函数。该回调函数需要与on接口传入的回调函数保持一致。若无此参数，则取消当前类型的所有订阅。 |

**示例**

```
1. import geolocation from '@ohos.geolocation';
2. let nmeaCb = (str:string):void => {
3. console.info('nmeaMessageChange: ' + JSON.stringify(str));
4. }
5. geolocation.on('nmeaMessageChange', nmeaCb);
6. geolocation.off('nmeaMessageChange', nmeaCb);
```

## geolocation.on('fenceStatusChange')(deprecated)

PhoneTablet

on(type: 'fenceStatusChange', request: GeofenceRequest, want: WantAgent): void

添加一个围栏，并订阅地理围栏事件。使用callback异步回调。

说明

从API version 8开始支持。

从API version 9开始废弃，建议使用[geoLocationManager.on('gnssFenceStatusChange')](js-apis-geolocationmanager.md#geolocationmanagerongnssfencestatuschange)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Geofence

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“fenceStatusChange”，表示订阅围栏事件上报。 |
| request | [GeofenceRequest](js-apis-geolocation.md#geofencerequestdeprecated) | 是 | 围栏的配置参数。 |
| want | [WantAgent](js-apis-app-ability-wantagent.md) | 是 | 用于接收地理围栏事件上报（进出围栏）。 |

**示例**

```
1. import geolocation from '@ohos.geolocation';
2. import wantAgent from '@ohos.app.ability.wantAgent';

4. let wantAgentInfo:wantAgent.WantAgentInfo = {
5. wants: [
6. {
7. bundleName: "com.example.myapplication",
8. abilityName: "EntryAbility",
9. action: "action1"
10. }
11. ],
12. operationType: wantAgent.OperationType.START_ABILITY,
13. requestCode: 0,
14. wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG],
15. };

17. wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj) => {
18. let requestInfo:geolocation.GeofenceRequest = {'priority': 0x201, 'scenario': 0x301, "geofence": {"latitude": 31.12, "longitude": 121.11, "radius": 100, "expiration": 10000}};
19. geolocation.on('fenceStatusChange', requestInfo, wantAgentObj);
20. });
```

## geolocation.off('fenceStatusChange')(deprecated)

PhoneTablet

off(type: 'fenceStatusChange', request: GeofenceRequest, want: WantAgent): void

删除一个围栏，并取消订阅该围栏事件。

说明

从API version 8开始支持。

从API version 9开始废弃，建议使用[geoLocationManager.off('gnssFenceStatusChange')](js-apis-geolocationmanager.md#geolocationmanageroffgnssfencestatuschange)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Geofence

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“fenceStatusChange”，表示订阅围栏事件上报。 |
| request | [GeofenceRequest](js-apis-geolocation.md#geofencerequestdeprecated) | 是 | 围栏的配置参数。 |
| want | [WantAgent](js-apis-app-ability-wantagent.md) | 是 | 用于接收地理围栏事件上报（进出围栏）。 |

**示例**

```
1. import geolocation from '@ohos.geolocation';
2. import wantAgent from '@ohos.app.ability.wantAgent';

4. let wantAgentInfo:wantAgent.WantAgentInfo = {
5. wants: [
6. {
7. bundleName: "com.example.myapplication",
8. abilityName: "EntryAbility",
9. action: "action1",
10. }
11. ],
12. operationType: wantAgent.OperationType.START_ABILITY,
13. requestCode: 0,
14. wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
15. };

17. wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj) => {
18. let requestInfo:geolocation.GeofenceRequest = {'priority': 0x201, 'scenario': 0x301, "geofence": {"latitude": 31.12, "longitude": 121.11, "radius": 100, "expiration": 10000}};
19. geolocation.on('fenceStatusChange', requestInfo, wantAgentObj);
20. geolocation.off('fenceStatusChange', requestInfo, wantAgentObj);
21. });
```

## geolocation.getCurrentLocation(deprecated)

PhonePC/2in1TabletTVWearable

getCurrentLocation(request: CurrentLocationRequest, callback: AsyncCallback<Location>): void

获取当前位置，使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[geoLocationManager.getCurrentLocation](js-apis-geolocationmanager.md#geolocationmanagergetcurrentlocation)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [CurrentLocationRequest](js-apis-geolocation.md#currentlocationrequestdeprecated) | 是 | 设置位置请求参数。 |
| callback | AsyncCallback<[Location](js-apis-geolocation.md#locationdeprecated)> | 是 | 回调函数，返回当前位置信息。 |

**示例**

```
1. import geolocation from '@ohos.geolocation';
2. import BusinessError from "@ohos.base"
3. let requestInfo:geolocation.CurrentLocationRequest = {'priority': 0x203, 'scenario': 0x300,'maxAccuracy': 0};
4. let locationChange = (err:BusinessError.BusinessError, location:geolocation.Location) => {
5. if (err) {
6. console.info('locationChanger: err=' + JSON.stringify(err));
7. }
8. if (location) {
9. console.info('locationChanger: location=' + JSON.stringify(location));
10. }
11. };
12. geolocation.getCurrentLocation(requestInfo, locationChange);
```

## geolocation.getCurrentLocation(deprecated)

PhonePC/2in1TabletTVWearable

getCurrentLocation(callback: AsyncCallback<Location>): void

获取当前位置，使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[geoLocationManager.getCurrentLocation](js-apis-geolocationmanager.md#geolocationmanagergetcurrentlocation)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[Location](js-apis-geolocation.md#locationdeprecated)> | 是 | 回调函数，返回当前位置信息。 |

**示例**

```
1. import geolocation from '@ohos.geolocation';
2. import BusinessError from "@ohos.base"
3. let locationChange = (err:BusinessError.BusinessError, location:geolocation.Location):void => {
4. if (err) {
5. console.info('locationChanger: err=' + JSON.stringify(err));
6. }
7. if (location) {
8. console.info('locationChanger: location=' + JSON.stringify(location));
9. }
10. };
11. geolocation.getCurrentLocation(locationChange);
```

## geolocation.getCurrentLocation(deprecated)

PhonePC/2in1TabletTVWearable

getCurrentLocation(request?: CurrentLocationRequest): Promise<Location>

获取当前位置，使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[geoLocationManager.getCurrentLocation](js-apis-geolocationmanager.md#geolocationmanagergetcurrentlocation-2)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [CurrentLocationRequest](js-apis-geolocation.md#currentlocationrequestdeprecated) | 否 | 设置位置请求参数。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[Location](js-apis-geolocation.md#locationdeprecated)> | Promise对象，返回当前位置信息。 |

**示例**

```
1. import geolocation from '@ohos.geolocation';
2. let requestInfo:geolocation.CurrentLocationRequest = {'priority': 0x203, 'scenario': 0x300,'maxAccuracy': 0};
3. geolocation.getCurrentLocation(requestInfo).then((result) => {
4. console.info('current location: ' + JSON.stringify(result));
5. });
```

## geolocation.getLastLocation(deprecated)

PhonePC/2in1TabletTVWearable

getLastLocation(callback: AsyncCallback<Location>): void

获取上一次位置，使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[geoLocationManager.getLastLocation](js-apis-geolocationmanager.md#geolocationmanagergetlastlocation)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[Location](js-apis-geolocation.md#locationdeprecated)> | 是 | 回调函数，返回上次位置信息。 |

**示例**

```
1. import geolocation from '@ohos.geolocation';
2. geolocation.getLastLocation((err, data) => {
3. if (err) {
4. console.info('getLastLocation: err=' + JSON.stringify(err));
5. }
6. if (data) {
7. console.info('getLastLocation: data=' + JSON.stringify(data));
8. }
9. });
```

## geolocation.getLastLocation(deprecated)

PhonePC/2in1TabletTVWearable

getLastLocation(): Promise<Location>

获取上一次位置，使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[geoLocationManager.getLastLocation](js-apis-geolocationmanager.md#geolocationmanagergetlastlocation)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[Location](js-apis-geolocation.md#locationdeprecated)> | Promise对象，返回上次位置信息。 |

**示例**

```
1. import geolocation from '@ohos.geolocation';
2. geolocation.getLastLocation().then((result) => {
3. console.info('getLastLocation: result: ' + JSON.stringify(result));
4. });
```

## geolocation.isLocationEnabled(deprecated)

PhonePC/2in1TabletTVWearable

isLocationEnabled(callback: AsyncCallback<boolean>): void

判断位置服务是否已经打开，使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[geoLocationManager.isLocationEnabled](js-apis-geolocationmanager.md#geolocationmanagerislocationenabled)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示位置服务已经开启；返回false表示位置服务已经关闭。 |

**示例**

```
1. import geolocation from '@ohos.geolocation';
2. geolocation.isLocationEnabled((err, data) => {
3. if (err) {
4. console.info('isLocationEnabled: err=' + JSON.stringify(err));
5. }
6. if (data) {
7. console.info('isLocationEnabled: data=' + JSON.stringify(data));
8. }
9. });
```

## geolocation.isLocationEnabled(deprecated)

PhonePC/2in1TabletTVWearable

isLocationEnabled(): Promise<boolean>

判断位置服务是否已经开启，使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[geoLocationManager.isLocationEnabled](js-apis-geolocationmanager.md#geolocationmanagerislocationenabled)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回true表示位置服务已经开启；返回false表示位置服务已经关闭。 |

**示例**

```
1. import geolocation from '@ohos.geolocation';
2. geolocation.isLocationEnabled().then((result) => {
3. console.info('promise, isLocationEnabled: ' + JSON.stringify(result));
4. });
```

## geolocation.requestEnableLocation(deprecated)

PhonePC/2in1TabletTVWearable

requestEnableLocation(callback: AsyncCallback<boolean>): void

请求打开位置服务，使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议由应用本身弹框请求用户跳转到settings开启位置开关，并且在弹框上写清楚会在什么场景下使用位置信息。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示打开位置服务；返回false表示关闭位置服务。 |

**示例**

```
1. import geolocation from '@ohos.geolocation';
2. geolocation.requestEnableLocation((err, data) => {
3. if (err) {
4. console.info('requestEnableLocation: err=' + JSON.stringify(err));
5. }
6. if (data) {
7. console.info('requestEnableLocation: data=' + JSON.stringify(data));
8. }
9. });
```

## geolocation.requestEnableLocation(deprecated)

PhonePC/2in1TabletTVWearable

requestEnableLocation(): Promise<boolean>

请求打开位置服务，使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议由应用本身弹框请求用户跳转到settings开启位置开关，并且在弹框上写清楚会在什么场景下使用位置信息。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回true表示位置服务已经开启；返回false表示位置服务已经关闭。 |

**示例**

```
1. import geolocation from '@ohos.geolocation';
2. geolocation.requestEnableLocation().then((result) => {
3. console.info('promise, requestEnableLocation: ' + JSON.stringify(result));
4. });
```

## geolocation.isGeoServiceAvailable(deprecated)

PhonePC/2in1TabletWearable

isGeoServiceAvailable(callback: AsyncCallback<boolean>): void

判断（逆）地理编码服务状态，使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[geoLocationManager.isGeocoderAvailable](js-apis-geolocationmanager.md#geolocationmanagerisgeocoderavailable)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Geocoder

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数，返回true表示地理编码服务可用；返回false表示地理编码服务不可用。 |

**示例**

```
1. import geolocation from '@ohos.geolocation';
2. geolocation.isGeoServiceAvailable((err, data) => {
3. if (err) {
4. console.info('isGeoServiceAvailable: err=' + JSON.stringify(err));
5. }
6. if (data) {
7. console.info('isGeoServiceAvailable: data=' + JSON.stringify(data));
8. }
9. });
```

## geolocation.isGeoServiceAvailable(deprecated)

PhonePC/2in1TabletWearable

isGeoServiceAvailable(): Promise<boolean>

判断（逆）地理编码服务状态，使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[geoLocationManager.isGeocoderAvailable](js-apis-geolocationmanager.md#geolocationmanagerisgeocoderavailable)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Geocoder

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回true表示地理编码服务可用；返回false表示地理编码服务不可用。 |

**示例**

```
1. import geolocation from '@ohos.geolocation';
2. geolocation.isGeoServiceAvailable().then((result) => {
3. console.info('promise, isGeoServiceAvailable: ' + JSON.stringify(result));
4. });
```

## geolocation.getAddressesFromLocation(deprecated)

PhonePC/2in1TabletWearable

getAddressesFromLocation(request: ReverseGeoCodeRequest, callback: AsyncCallback<Array<GeoAddress>>): void

调用逆地理编码服务，将坐标转换为地理描述，使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[geoLocationManager.getAddressesFromLocation](js-apis-geolocationmanager.md#geolocationmanagergetaddressesfromlocation)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Geocoder

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [ReverseGeoCodeRequest](js-apis-geolocation.md#reversegeocoderequestdeprecated) | 是 | 设置逆地理编码请求的相关参数。 |
| callback | AsyncCallback<Array<[GeoAddress](js-apis-geolocation.md#geoaddressdeprecated)>> | 是 | 回调函数，返回逆地理编码结果。 |

**示例**

```
1. import geolocation from '@ohos.geolocation';
2. let reverseGeocodeRequest:geolocation.ReverseGeoCodeRequest = {"latitude": 31.12, "longitude": 121.11, "maxItems": 1};
3. geolocation.getAddressesFromLocation(reverseGeocodeRequest, (err, data) => {
4. if (err) {
5. console.info('getAddressesFromLocation: err=' + JSON.stringify(err));
6. }
7. if (data) {
8. console.info('getAddressesFromLocation: data=' + JSON.stringify(data));
9. }
10. });
```

## geolocation.getAddressesFromLocation(deprecated)

PhonePC/2in1TabletWearable

getAddressesFromLocation(request: ReverseGeoCodeRequest): Promise<Array<GeoAddress>>

调用逆地理编码服务，将坐标转换为地理描述，使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[geoLocationManager.getAddressesFromLocation](js-apis-geolocationmanager.md#geolocationmanagergetaddressesfromlocation-1)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Geocoder

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [ReverseGeoCodeRequest](js-apis-geolocation.md#reversegeocoderequestdeprecated) | 是 | 设置逆地理编码请求的相关参数。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[GeoAddress](js-apis-geolocation.md#geoaddressdeprecated)>> | Promise对象，返回地理描述信息。 |

**示例**

```
1. import geolocation from '@ohos.geolocation';
2. let reverseGeocodeRequest:geolocation.ReverseGeoCodeRequest = {"latitude": 31.12, "longitude": 121.11, "maxItems": 1};
3. geolocation.getAddressesFromLocation(reverseGeocodeRequest).then((data) => {
4. console.info('getAddressesFromLocation: ' + JSON.stringify(data));
5. });
```

## geolocation.getAddressesFromLocationName(deprecated)

PhonePC/2in1TabletWearable

getAddressesFromLocationName(request: GeoCodeRequest, callback: AsyncCallback<Array<GeoAddress>>): void

调用地理编码服务，将地理描述转换为具体坐标，使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[geoLocationManager.getAddressesFromLocationName](js-apis-geolocationmanager.md#geolocationmanagergetaddressesfromlocationname)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Geocoder

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [GeoCodeRequest](js-apis-geolocation.md#geocoderequestdeprecated) | 是 | 设置地理编码请求的相关参数。 |
| callback | AsyncCallback<Array<[GeoAddress](js-apis-geolocation.md#geoaddressdeprecated)>> | 是 | 回调函数，返回地理编码结果。 |

**示例**

```
1. import geolocation from '@ohos.geolocation';
2. let geocodeRequest:geolocation.GeoCodeRequest = {"description": "上海市浦东新区xx路xx号", "maxItems": 1};
3. geolocation.getAddressesFromLocationName(geocodeRequest, (err, data) => {
4. if (err) {
5. console.info('getAddressesFromLocationName: err=' + JSON.stringify(err));
6. }
7. if (data) {
8. console.info('getAddressesFromLocationName: data=' + JSON.stringify(data));
9. }
10. });
```

## geolocation.getAddressesFromLocationName(deprecated)

PhonePC/2in1TabletWearable

getAddressesFromLocationName(request: GeoCodeRequest): Promise<Array<GeoAddress>>

调用地理编码服务，将地理描述转换为具体坐标，使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[geoLocationManager.getAddressesFromLocationName](js-apis-geolocationmanager.md#geolocationmanagergetaddressesfromlocationname-1)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Geocoder

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [GeoCodeRequest](js-apis-geolocation.md#geocoderequestdeprecated) | 是 | 设置地理编码请求的相关参数。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[GeoAddress](js-apis-geolocation.md#geoaddressdeprecated)>> | Promise对象，返回地理编码查询结果。 |

**示例**

```
1. import geolocation from '@ohos.geolocation';
2. let geocodeRequest:geolocation.GeoCodeRequest = {"description": "上海市浦东新区xx路xx号", "maxItems": 1};
3. geolocation.getAddressesFromLocationName(geocodeRequest).then((result) => {
4. console.info('getAddressesFromLocationName: ' + JSON.stringify(result));
5. });
```

## geolocation.getCachedGnssLocationsSize(deprecated)

PhoneTabletWearable

getCachedGnssLocationsSize(callback: AsyncCallback<number>): void

获取GNSS芯片缓存位置的个数。使用callback异步回调。

说明

从API version 8开始支持。

从API version 9开始废弃，建议使用[geoLocationManager.getCachedGnssLocationsSize](js-apis-geolocationmanager.md#geolocationmanagergetcachedgnsslocationssize)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数，返回GNSS芯片缓存位置个数。 |

**示例**

```
1. import geolocation from '@ohos.geolocation';
2. geolocation.getCachedGnssLocationsSize((err, size) => {
3. if (err) {
4. console.info('getCachedGnssLocationsSize: err=' + JSON.stringify(err));
5. }
6. if (size) {
7. console.info('getCachedGnssLocationsSize: size=' + JSON.stringify(size));
8. }
9. });
```

## geolocation.getCachedGnssLocationsSize(deprecated)

PhoneTabletWearable

getCachedGnssLocationsSize(): Promise<number>;

获取GNSS芯片缓存位置的个数。使用Promise异步回调。

说明

从API version 8开始支持。

从API version 9开始废弃，建议使用[geoLocationManager.getCachedGnssLocationsSize](js-apis-geolocationmanager.md#geolocationmanagergetcachedgnsslocationssize-1)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回GNSS缓存位置的个数。 |

**示例**

```
1. import geolocation from '@ohos.geolocation';
2. geolocation.getCachedGnssLocationsSize().then((result) => {
3. console.info('promise, getCachedGnssLocationsSize: ' + JSON.stringify(result));
4. });
```

## geolocation.flushCachedGnssLocations(deprecated)

PhoneTabletWearable

flushCachedGnssLocations(callback: AsyncCallback<boolean>): void

读取并清空GNSS芯片所有缓存位置。使用callback异步回调。

说明

从API version 8开始支持。

从API version 9开始废弃，建议使用[geoLocationManager.flushCachedGnssLocations](js-apis-geolocationmanager.md#geolocationmanagerflushcachedgnsslocations)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示操作成功；返回false表示操作失败。 |

**示例**

```
1. import geolocation from '@ohos.geolocation';
2. geolocation.flushCachedGnssLocations((err, result) => {
3. if (err) {
4. console.info('flushCachedGnssLocations: err=' + JSON.stringify(err));
5. }
6. if (result) {
7. console.info('flushCachedGnssLocations: result=' + JSON.stringify(result));
8. }
9. });
```

## geolocation.flushCachedGnssLocations(deprecated)

PhoneTabletWearable

flushCachedGnssLocations(): Promise<boolean>

读取并清空GNSS芯片所有缓存位置。使用Promise异步回调。

说明

从API version 8开始支持。

从API version 9开始废弃，建议使用[geoLocationManager.flushCachedGnssLocations](js-apis-geolocationmanager.md#geolocationmanagerflushcachedgnsslocations-1)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回true表示操作成功；返回false表示操作失败。 |

**示例**

```
1. import geolocation from '@ohos.geolocation';
2. geolocation.flushCachedGnssLocations().then((result) => {
3. console.info('promise, flushCachedGnssLocations: ' + JSON.stringify(result));
4. });
```

## geolocation.sendCommand(deprecated)

PhonePC/2in1TabletTVWearable

sendCommand(command: LocationCommand, callback: AsyncCallback<boolean>): void

给位置服务子系统的各个部件发送扩展命令。使用callback异步回调。

说明

从API version 8开始支持。

从API version 9开始废弃，建议使用[geoLocationManager.sendCommand](js-apis-geolocationmanager.md#geolocationmanagersendcommand)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| command | [LocationCommand](js-apis-geolocation.md#locationcommanddeprecated) | 是 | 指定目标场景，和将要发送的命令（字符串）。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回true表示命令发送成功；返回false表示命令发送失败。 |

**示例**

```
1. import geolocation from '@ohos.geolocation';
2. let requestInfo:geolocation.LocationCommand = {'scenario': 0x301, 'command': "command_1"};
3. geolocation.sendCommand(requestInfo, (err, result) => {
4. if (err) {
5. console.info('sendCommand: err=' + JSON.stringify(err));
6. }
7. if (result) {
8. console.info('sendCommand: result=' + JSON.stringify(result));
9. }
10. });
```

## geolocation.sendCommand(deprecated)

PhonePC/2in1TabletTVWearable

sendCommand(command: LocationCommand): Promise<boolean>

给位置服务子系统的各个部件发送扩展命令。使用Promise异步回调。

说明

从API version 8开始支持。

从API version 9开始废弃，建议使用[geoLocationManager.sendCommand](js-apis-geolocationmanager.md#geolocationmanagersendcommand)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| command | [LocationCommand](js-apis-geolocation.md#locationcommanddeprecated) | 是 | 指定目标场景，和将要发送的命令（字符串）。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回true表示命令发送成功；返回false表示命令发送失败。 |

**示例**

```
1. import geolocation from '@ohos.geolocation';
2. let requestInfo:geolocation.LocationCommand = {'scenario': 0x301, 'command': "command_1"};
3. geolocation.sendCommand(requestInfo).then((result) => {
4. console.info('promise, sendCommand: ' + JSON.stringify(result));
5. });
```

## ReverseGeoCodeRequest(deprecated)

PhonePC/2in1TabletWearable

逆地理编码请求参数。

说明

从API version 9开始废弃，建议使用[geoLocationManager.ReverseGeoCodeRequest](js-apis-geolocationmanager.md#reversegeocoderequest)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Geocoder

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| locale | string | 否 | 是 | 指定位置描述信息的语言，“zh”代表中文，“en”代表英文。 |
| latitude | number | 否 | 否 | 表示纬度信息，正值表示北纬，负值表示南纬。取值范围为-90到90。 |
| longitude | number | 否 | 否 | 表示经度信息，正值表示东经，负值表示西经。取值范围为-180到180。 |
| maxItems | number | 否 | 是 | 指定返回位置信息的最大个数。取值范围为大于等于0，推荐该值小于10。 |

## GeoCodeRequest(deprecated)

PhonePC/2in1TabletWearable

地理编码请求参数。

说明

从API version 9开始废弃，建议使用[geoLocationManager.GeoCodeRequest](js-apis-geolocationmanager.md#geocoderequest)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Geocoder

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| locale | string | 否 | 是 | 表示位置描述信息的语言，“zh”代表中文，“en”代表英文。 |
| description | string | 否 | 否 | 表示位置信息描述，如“上海市浦东新区xx路xx号”。 |
| maxItems | number | 否 | 是 | 表示返回位置信息的最大个数。取值范围为大于等于0，推荐该值小于10。 |
| minLatitude | number | 否 | 是 | 表示最小纬度信息，与下面三个参数一起，表示一个经纬度范围。取值范围为-90到90。 |
| minLongitude | number | 否 | 是 | 表示最小经度信息。取值范围为-180到180。 |
| maxLatitude | number | 否 | 是 | 表示最大纬度信息。取值范围为-90到90。 |
| maxLongitude | number | 否 | 是 | 表示最大经度信息。取值范围为-180到180。 |

## GeoAddress(deprecated)

PhonePC/2in1TabletWearable

地理编码地址信息。

说明

从API version 9开始废弃，建议使用[geoLocationManager.GeoAddress](js-apis-geolocationmanager.md#geoaddress)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Geocoder

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| latitude7+ | number | 否 | 是 | 表示纬度信息，正值表示北纬，负值表示南纬。取值范围为-90到90。 |
| longitude7+ | number | 否 | 是 | 表示经度信息，正值表示东经，负值表是西经。取值范围为-180到180。 |
| locale7+ | string | 否 | 是 | 表示位置描述信息的语言，“zh”代表中文，“en”代表英文。 |
| placeName7+ | string | 否 | 是 | 表示地区信息。 |
| countryCode7+ | string | 否 | 是 | 表示国家码信息。 |
| countryName7+ | string | 否 | 是 | 表示国家信息。 |
| administrativeArea7+ | string | 否 | 是 | 表示省份区域信息。 |
| subAdministrativeArea7+ | string | 否 | 是 | 表示子区域信息。 |
| locality7+ | string | 否 | 是 | 表示城市信息。 |
| subLocality7+ | string | 否 | 是 | 表示子城市信息。 |
| roadName7+ | string | 否 | 是 | 表示路名信息。 |
| subRoadName7+ | string | 否 | 是 | 表示子路名信息。 |
| premises7+ | string | 否 | 是 | 表示门牌号信息。 |
| postalCode7+ | string | 否 | 是 | 表示邮政编码信息。 |
| phoneNumber7+ | string | 否 | 是 | 表示联系方式信息。 |
| addressUrl7+ | string | 否 | 是 | 表示位置信息附件的网址信息。 |
| descriptions7+ | Array<string> | 否 | 是 | 表示附加的描述信息。 |
| descriptionsSize7+ | number | 否 | 是 | 表示附加的描述信息数量。取值范围为大于等于0，推荐该值小于10。 |

## LocationRequest(deprecated)

PhonePC/2in1TabletTVWearable

位置信息请求参数。

说明

从API version 9开始废弃，建议使用[geoLocationManager.LocationRequest](js-apis-geolocationmanager.md#locationrequest)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| priority | [LocationRequestPriority](js-apis-geolocation.md#locationrequestprioritydeprecated) | 否 | 是 | 表示优先级信息。取值范围见[LocationRequestPriority](js-apis-geolocation.md#locationrequestprioritydeprecated)的定义。 |
| scenario | [LocationRequestScenario](js-apis-geolocation.md#locationrequestscenariodeprecated) | 否 | 是 | 表示场景信息。取值范围见[LocationRequestScenario](js-apis-geolocation.md#locationrequestscenariodeprecated)的定义。 |
| timeInterval | number | 否 | 是 | 表示上报位置信息的时间间隔，单位是秒。取值范围为大于0。 |
| distanceInterval | number | 否 | 是 | 表示上报位置信息的距离间隔。单位是米，取值范围为大于0。 |
| maxAccuracy | number | 否 | 是 | 表示精度信息，单位是米。  仅在精确位置功能场景（同时授予了ohos.permission.APPROXIMATELY\_LOCATION和ohos.permission.LOCATION 权限）下有效，模糊位置功能生效场景（仅授予了ohos.permission.APPROXIMATELY\_LOCATION 权限）下该字段无意义。  默认值为0，取值范围为大于等于0。  当scenario为NAVIGATION/TRAJECTORY\_TRACKING/CAR\_HAILING或者priority为ACCURACY时建议设置maxAccuracy为大于10的值。  当scenario为DAILY\_LIFE\_SERVICE/NO\_POWER或者priority为LOW\_POWER/FIRST\_FIX时建议设置maxAccuracy为大于100的值。 |

## CurrentLocationRequest(deprecated)

PhonePC/2in1TabletTVWearable

当前位置信息请求参数。

说明

从API version 9开始废弃，建议使用[geoLocationManager.CurrentLocationRequest](js-apis-geolocationmanager.md#currentlocationrequest)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| priority | [LocationRequestPriority](js-apis-geolocation.md#locationrequestprioritydeprecated) | 否 | 是 | 表示优先级信息。取值范围见[LocationRequestPriority](js-apis-geolocation.md#locationrequestprioritydeprecated)的定义。 |
| scenario | [LocationRequestScenario](js-apis-geolocation.md#locationrequestscenariodeprecated) | 否 | 是 | 表示场景信息。取值范围见[LocationRequestScenario](js-apis-geolocation.md#locationrequestscenariodeprecated)的定义。 |
| maxAccuracy | number | 否 | 是 | 表示精度信息，单位是米。  仅在精确位置功能场景（同时授予了ohos.permission.APPROXIMATELY\_LOCATION和ohos.permission.LOCATION 权限）下有效，模糊位置功能生效场景（仅授予了ohos.permission.APPROXIMATELY\_LOCATION 权限）下该字段无意义。  默认值为0，取值范围为大于等于0。  当scenario为NAVIGATION/TRAJECTORY\_TRACKING/CAR\_HAILING或者priority为ACCURACY时建议设置maxAccuracy为大于10的值。  当scenario为DAILY\_LIFE\_SERVICE/NO\_POWER或者priority为LOW\_POWER/FIRST\_FIX时建议设置maxAccuracy为大于100的值。 |
| timeoutMs | number | 否 | 是 | 表示超时时间，单位是毫秒，最小为1000毫秒。取值范围为大于等于1000。 |

## SatelliteStatusInfo(deprecated)

PhoneTabletWearable

卫星状态信息。

说明

从API version 8开始支持。

从API version 9开始废弃，建议使用[geoLocationManager.SatelliteStatusInfo](js-apis-geolocationmanager.md#satellitestatusinfo)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| satellitesNumber | number | 否 | 否 | 表示卫星个数。取值范围为大于等于0。 |
| satelliteIds | Array<number> | 否 | 否 | 表示每个卫星的ID，数组类型。取值范围为大于等于0。 |
| carrierToNoiseDensitys | Array<number> | 否 | 否 | 表示载波噪声功率谱密度比，即cn0。取值范围为大于0。 |
| altitudes | Array<number> | 否 | 否 | 表示卫星高度角信息。单位是“度”，取值范围为-90到90。 |
| azimuths | Array<number> | 否 | 否 | 表示方位角。单位是“度”，取值范围为0到360。 |
| carrierFrequencies | Array<number> | 否 | 否 | 表示载波频率。单位是Hz，取值范围为大于等于0。 |

## CachedGnssLocationsRequest(deprecated)

PhoneTabletWearable

请求订阅GNSS缓存位置上报功能接口的配置参数。

说明

从API version 8开始支持。

从API version 9开始废弃，建议使用[geoLocationManager.CachedGnssLocationsRequest](js-apis-geolocationmanager.md#cachedgnsslocationsrequest)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| reportingPeriodSec | number | 否 | 否 | 表示GNSS缓存位置上报的周期，单位是毫秒。取值范围为大于0。 |
| wakeUpCacheQueueFull | boolean | 否 | 否 | true表示GNSS芯片底层缓存队列满之后会主动唤醒AP芯片，并把缓存位置上报给应用。  false表示GNSS芯片底层缓存队列满之后不会主动唤醒AP芯片，会把缓存位置直接丢弃。 |

## Geofence(deprecated)

PhoneTablet

GNSS围栏的配置参数。目前只支持圆形围栏。

说明

从API version 8开始支持。

从API version 9开始废弃，建议使用[geoLocationManager.Geofence](js-apis-geolocationmanager.md#geofence)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Geofence

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| latitude | number | 否 | 否 | 表示纬度。取值范围为-90到90。 |
| longitude | number | 否 | 否 | 表示经度。取值范围为-180到180。 |
| radius | number | 否 | 否 | 表示圆形围栏的半径。单位是米，取值范围为大于0。 |
| expiration | number | 否 | 否 | 围栏存活的时间，单位是毫秒。取值范围为大于0。 |

## GeofenceRequest(deprecated)

PhoneTablet

请求添加GNSS围栏消息中携带的参数，包括定位场景和围栏信息。

说明

从API version 8开始支持。

从API version 9开始废弃，建议使用[geoLocationManager.GeofenceRequest](js-apis-geolocationmanager.md#geofencerequest)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Geofence

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| priority | [LocationRequestPriority](js-apis-geolocation.md#locationrequestprioritydeprecated) | 否 | 否 | 表示位置信息优先级。 |
| scenario | [LocationRequestScenario](js-apis-geolocation.md#locationrequestscenariodeprecated) | 否 | 否 | 表示定位场景。 |
| geofence | [Geofence](js-apis-geolocation.md#geofencedeprecated) | 否 | 否 | 表示围栏信息。 |

## LocationCommand(deprecated)

PhonePC/2in1TabletTVWearable

扩展命令参数。

说明

从API version 8开始支持。

从API version 9开始废弃，建议使用[geoLocationManager.LocationCommand](js-apis-geolocationmanager.md#locationcommand)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scenario | [LocationRequestScenario](js-apis-geolocation.md#locationrequestscenariodeprecated) | 否 | 否 | 表示定位场景。 |
| command | string | 否 | 否 | 扩展命令字符串。 |

## Location(deprecated)

PhonePC/2in1TabletTVWearable

位置信息。

说明

从API version 9开始废弃，建议使用[geoLocationManager.Location](js-apis-geolocationmanager.md#location)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| latitude7+ | number | 否 | 否 | 表示纬度信息，正值表示北纬，负值表示南纬。取值范围为-90到90。 |
| longitude7+ | number | 否 | 否 | 表示经度信息，正值表示东经，负值表是西经。取值范围为-180到180。 |
| altitude7+ | number | 否 | 否 | 表示高度信息，单位米。 |
| accuracy7+ | number | 否 | 否 | 表示精度信息，单位米。 |
| speed7+ | number | 否 | 否 | 表示速度信息，单位米每秒。 |
| timeStamp7+ | number | 否 | 否 | 表示位置时间戳，UTC格式。 |
| direction7+ | number | 否 | 否 | 表示航向信息。单位是“度”，取值范围为0到360。 |
| timeSinceBoot7+ | number | 否 | 否 | 表示位置时间戳，开机时间格式。 |
| additions7+ | Array<string> | 否 | 是 | 附加信息。 |
| additionSize7+ | number | 否 | 是 | 附加信息数量。取值范围为大于等于0。 |

## LocationPrivacyType(deprecated)

PhonePC/2in1TabletTVWearable

定位服务隐私协议类型。

说明

从API version 8开始支持。

从API version 9开始废弃，替代接口geoLocationManager.LocationPrivacyType仅供系统应用使用。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OTHERS | 0 | 其他场景。预留字段。 |
| STARTUP | 1 | 开机向导场景下的隐私协议。在开机时弹出协议，提醒用户阅读并选择是否授权。 |
| CORE\_LOCATION | 2 | 开启网络定位时弹出的隐私协议。 |

## LocationRequestPriority(deprecated)

PhonePC/2in1TabletTVWearable

位置请求中位置信息优先级类型。

说明

从API version 9开始废弃，建议使用[geoLocationManager.LocationRequestPriority](js-apis-geolocationmanager.md#locationrequestpriority)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNSET | 0x200 | 表示未设置优先级，表示[LocationRequestPriority](js-apis-geolocation.md#locationrequestprioritydeprecated)无效。 |
| ACCURACY | 0x201 | 表示精度优先。  定位精度优先策略主要以GNSS定位技术为主，在开阔场景下可以提供米级的定位精度，具体性能指标依赖用户设备的定位硬件能力，但在室内等强遮蔽定位场景下，无法提供准确的位置服务。 |
| LOW\_POWER | 0x202 | 表示低功耗优先。  低功耗定位优先策略主要使用基站定位和WLAN、蓝牙定位技术，也可以同时提供室内和户外场景下的位置服务，因为其依赖周边基站、可见WLAN、蓝牙设备的分布情况，定位结果的精度波动范围较大，如果对定位结果精度要求不高，或者使用场景多在有基站、可见WLAN、蓝牙设备高密度分布的情况下，推荐使用，可以有效节省设备功耗。 |
| FIRST\_FIX | 0x203 | 表示快速获取位置优先，如果应用希望快速拿到一个位置，可以将优先级设置为该字段。  快速定位优先策略会同时使用GNSS定位、基站定位和WLAN、蓝牙定位技术，以便室内和户外场景下，通过此策略都可以获得位置结果，当各种定位技术都有提供位置结果时，系统会选择其中精度较好的结果返回给应用。因为对各种定位技术同时使用，对设备的硬件资源消耗较大，功耗也较大。 |

## LocationRequestScenario(deprecated)

PhonePC/2in1TabletTVWearable

位置请求中定位场景类型。

说明

从API version 9开始废弃，建议使用[geoLocationManager.LocationRequestScenario](js-apis-geolocationmanager.md#locationrequestscenario)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNSET | 0x300 | 表示未设置场景信息。  表示[LocationRequestScenario](js-apis-geolocation.md#locationrequestscenariodeprecated)字段无效。 |
| NAVIGATION | 0x301 | 表示导航场景。  适用于在户外定位设备实时位置的场景，如车载、步行导航。  在此场景下，为保证系统提供位置结果精度最优，主要使用GNSS定位技术提供定位服务。  此场景默认以最小1秒间隔上报定位结果。 |
| TRAJECTORY\_TRACKING | 0x302 | 表示运动轨迹记录场景。  适用于记录用户位置轨迹的场景，如运动类应用记录轨迹功能。主要使用GNSS定位技术提供定位服务。  此场景默认以最小1秒间隔上报定位结果。 |
| CAR\_HAILING | 0x303 | 表示打车场景。  适用于用户出行打车时定位当前位置的场景，如网约车类应用。  此场景默认以最小1秒间隔上报定位结果。 |
| DAILY\_LIFE\_SERVICE | 0x304 | 表示日常服务使用场景。  适用于不需要定位用户精确位置的使用场景，如新闻资讯、网购、点餐类应用，做推荐、推送时定位用户大致位置即可。  此场景默认以最小1秒间隔上报定位结果。 |
| NO\_POWER | 0x305 | 表示无功耗功场景，这种场景下不会主动触发定位，会在其他应用定位时，才给当前应用返回位置。 |

## GeoLocationErrorCode(deprecated)

PhonePC/2in1TabletTVWearable

位置服务中的错误码信息。

说明

从API version 9开始废弃，建议使用[位置服务错误码](errorcode-geolocationmanager.md)替代。

**需要权限**：ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INPUT\_PARAMS\_ERROR7+ | 101 | 表示输入参数错误。 |
| REVERSE\_GEOCODE\_ERROR7+ | 102 | 表示逆地理编码接口调用失败。 |
| GEOCODE\_ERROR7+ | 103 | 表示地理编码接口调用失败。 |
| LOCATOR\_ERROR7+ | 104 | 表示定位失败。 |
| LOCATION\_SWITCH\_ERROR7+ | 105 | 表示定位开关。 |
| LAST\_KNOWN\_LOCATION\_ERROR7+ | 106 | 表示获取上次位置失败。 |
| LOCATION\_REQUEST\_TIMEOUT\_ERROR7+ | 107 | 表示单次定位，没有在指定时间内返回位置。 |
