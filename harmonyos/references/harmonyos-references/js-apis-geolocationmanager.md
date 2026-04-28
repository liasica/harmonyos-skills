---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-geolocationmanager
title: @ohos.geoLocationManager (位置服务)
breadcrumb: API参考 > 应用服务 > Location Kit（位置服务） > ArkTS API > @ohos.geoLocationManager (位置服务)
category: harmonyos-references
scraped_at: 2026-04-28T08:17:04+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1e77da1a9a3a5dfb7b670687d1c9e48b828dd84a0abdd5872980c9e004668916
---

位置服务提供GNSS定位、网络定位（蜂窝基站、WLAN、蓝牙定位技术）、地理编码、逆地理编码、国家码和地理围栏等基本功能。

使用位置服务时请打开设备“位置”开关。如果“位置”开关关闭并且代码未设置捕获异常，可能导致应用异常。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块能力仅支持WGS-84坐标系。

## 申请权限

PhonePC/2in1TabletTVWearable

请参考[申请位置权限开发指导](../harmonyos-guides/location-permission-guidelines.md)。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { geoLocationManager } from '@kit.LocationKit';
```

## ReverseGeoCodeRequest

PhonePC/2in1TabletWearable

逆地理编码请求参数。

**系统能力**：SystemCapability.Location.Location.Geocoder

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| locale | string | 否 | 是 | 指定位置描述信息的语言，“zh”代表中文，“en”代表英文。默认值从设置中的“语言和地区”获取。 |
| country12+ | string | 否 | 是 | 限制查询结果在指定的国家内，采用ISO 3166-1 alpha-2 。“CN”代表中国。默认值从设置中的“语言和地区”获取。 |
| latitude | number | 否 | 否 | 表示纬度信息，正值表示北纬，负值表示南纬。取值范围为-90到90。仅支持WGS84坐标系。 |
| longitude | number | 否 | 否 | 表示经度信息，正值表示东经，负值表示西经。取值范围为-180到180。仅支持WGS84坐标系。 |
| maxItems | number | 否 | 是 | 指定返回位置信息的最大个数。取值范围为大于等于0，推荐该值小于10。默认值是1。 |

## GeoCodeRequest

PhonePC/2in1TabletWearable

地理编码请求参数。

**系统能力**：SystemCapability.Location.Location.Geocoder

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| locale | string | 否 | 是 | 表示位置描述信息的语言，“zh”代表中文，“en”代表英文。默认值从设置中的“语言和地区”获取。 |
| country12+ | string | 否 | 是 | 限制查询结果在指定的国家内，采用ISO 3166-1 alpha-2 。“CN”代表中国。默认值从设置中的“语言和地区”获取。 |
| description | string | 否 | 否 | 表示位置信息描述，如“上海市浦东新区xx路xx号”，字符串长度不超过100。 |
| maxItems | number | 否 | 是 | 表示返回位置信息的最大个数。取值范围为大于等于0，推荐该值小于10。默认值是1。 |
| minLatitude | number | 否 | 是 | 表示最小纬度信息，与下面三个参数一起，表示一个经纬度范围。取值范围为-90到90。仅支持WGS84坐标系。默认值是0。如果该参数有值时，下面三个参数必填。 |
| minLongitude | number | 否 | 是 | 表示最小经度信息。取值范围为-180到180。仅支持WGS84坐标系。默认值是0。 |
| maxLatitude | number | 否 | 是 | 表示最大纬度信息。取值范围为-90到90。仅支持WGS84坐标系。默认值是0。 |
| maxLongitude | number | 否 | 是 | 表示最大经度信息。取值范围为-180到180。仅支持WGS84坐标系。默认值是0。 |

## GeoAddress

PhonePC/2in1TabletWearable

地理编码地址信息。

**系统能力**：SystemCapability.Location.Location.Geocoder

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| latitude | number | 否 | 是 | 表示纬度信息，正值表示北纬，负值表示南纬。取值范围为-90到90。仅支持WGS84坐标系。 |
| longitude | number | 否 | 是 | 表示经度信息，正值表示东经，负值表示西经。取值范围为-180到180。仅支持WGS84坐标系。 |
| locale | string | 否 | 是 | 表示位置描述信息的语言，“zh”代表中文，“en”代表英文。 |
| placeName | string | 否 | 是 | 表示详细地址信息。 |
| countryCode | string | 否 | 是 | 表示国家码信息。 |
| countryName | string | 否 | 是 | 表示国家信息。 |
| administrativeArea | string | 否 | 是 | 表示国家以下的一级行政区，一般是省/州。 |
| subAdministrativeArea | string | 否 | 是 | 表示国家以下的二级行政区，一般是市。 |
| locality | string | 否 | 是 | 表示城市信息，一般是市。 |
| subLocality | string | 否 | 是 | 表示子城市信息，一般是区/县。 |
| roadName | string | 否 | 是 | 表示路名信息。 |
| subRoadName | string | 否 | 是 | 表示子路名信息。 |
| premises | string | 否 | 是 | 表示门牌号信息。 |
| postalCode | string | 否 | 是 | 表示邮政编码信息。 |
| phoneNumber | string | 否 | 是 | 表示联系方式信息。 |
| addressUrl | string | 否 | 是 | 表示位置信息附件的网址信息。 |
| descriptions | Array<string> | 否 | 是 | 表示附加的描述信息。目前包含城市编码cityCode（Array下标为0）和区划编码adminCode（Array下标为1），例如["025","320114001"]。 |
| descriptionsSize | number | 否 | 是 | 表示附加的描述信息数量。取值范围为大于等于0，推荐该值小于10。 |

## LocationRequest

PhonePC/2in1TabletTVWearable

位置信息请求参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| priority | [LocationRequestPriority](js-apis-geolocationmanager.md#locationrequestpriority) | 否 | 是 | 表示优先级信息。当scenario取值为UNSET时，priority参数生效，否则priority参数不生效；当scenario和priority均取值为UNSET时，无法发起定位请求。取值范围见[LocationRequestPriority](js-apis-geolocationmanager.md#locationrequestpriority)的定义。默认值为FIRST\_FIX。 |
| scenario | [LocationRequestScenario](js-apis-geolocationmanager.md#locationrequestscenario) | 否 | 是 | 表示场景信息。当scenario取值为UNSET时，priority参数生效，否则priority参数不生效；当scenario和priority均取值为UNSET时，无法发起定位请求。取值范围见[LocationRequestScenario](js-apis-geolocationmanager.md#locationrequestscenario)的定义。默认值为UNSET。 |
| timeInterval | number | 否 | 是 | 表示上报位置信息的时间间隔，单位为秒。  取值范围为大于等于0的值。  默认值为对应定位模式下允许的最小时间间隔：  默认值在GNSS定位时为1秒，网络定位时为20秒。  当设置值小于最小间隔时，以最小时间间隔生效。  设置为0时不对时间间隔进行校验，直接上报位置信息。 |
| distanceInterval | number | 否 | 是 | 表示上报位置信息的距离间隔。单位是米，默认值为0，取值范围为大于等于0。等于0时对位置上报距离间隔无限制。 |
| maxAccuracy | number | 否 | 是 | 应用向系统请求位置信息时要求的精度值，单位为米。该参数仅在精确位置功能场景（即同时授权了ohos.permission.APPROXIMATELY\_LOCATION和ohos.permission.LOCATION 权限）下有效，模糊位置功能生效场景（即仅授权了ohos.permission.APPROXIMATELY\_LOCATION 权限）下该字段无意义。  该参数生效的情况下，系统会对比GNSS或网络定位服务上报的位置信息与应用的位置信息申请。当位置信息[Location](js-apis-geolocationmanager.md#location)中的精度值（accuracy）小于等于应用要求的精度值（maxAccuracy）时，位置信息会返回给应用；否则系统将丢弃本次收到的位置信息。  默认值为0，表示不限制位置信息的精度，取值范围为大于等于0。  当scenario为NAVIGATION/TRAJECTORY\_TRACKING/CAR\_HAILING或者priority为ACCURACY时建议设置maxAccuracy为大于10的值。  当scenario为DAILY\_LIFE\_SERVICE/NO\_POWER或者priority为LOW\_POWER/FIRST\_FIX时建议设置maxAccuracy为大于100的值。 |

## CurrentLocationRequest

PhonePC/2in1TabletTVWearable

当前位置信息请求参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| priority | [LocationRequestPriority](js-apis-geolocationmanager.md#locationrequestpriority) | 否 | 是 | 表示优先级信息。当scenario取值为UNSET时，priority参数生效，否则priority参数不生效；当scenario和priority均取值为UNSET时，无法发起定位请求。取值范围见[LocationRequestPriority](js-apis-geolocationmanager.md#locationrequestpriority)的定义。默认值为FIRST\_FIX。 |
| scenario | [LocationRequestScenario](js-apis-geolocationmanager.md#locationrequestscenario) | 否 | 是 | 表示场景信息。当scenario取值为UNSET时，priority参数生效，否则priority参数不生效；当scenario和priority均取值为UNSET时，无法发起定位请求。取值范围见[LocationRequestScenario](js-apis-geolocationmanager.md#locationrequestscenario)的定义。默认值为UNSET。 |
| maxAccuracy | number | 否 | 是 | 应用向系统请求位置信息时要求的精度值，单位为米。该参数仅在精确位置功能场景（即同时授权了ohos.permission.APPROXIMATELY\_LOCATION和ohos.permission.LOCATION 权限）下有效，模糊位置功能生效场景（即仅授权了ohos.permission.APPROXIMATELY\_LOCATION 权限）下该字段无意义。  该参数生效的情况下，系统会对比GNSS或网络定位服务上报的位置信息与应用的位置信息申请。当位置信息[Location](js-apis-geolocationmanager.md#location)中的精度值（accuracy）小于等于应用要求的精度值（maxAccuracy）时，位置信息会返回给应用；否则系统将丢弃本次收到的位置信息。  默认值为0，表示不限制位置信息的精度，取值范围为大于等于0。  当scenario为NAVIGATION/TRAJECTORY\_TRACKING/CAR\_HAILING或者priority为ACCURACY时建议设置maxAccuracy为大于10的值。  当scenario为DAILY\_LIFE\_SERVICE/NO\_POWER或者priority为LOW\_POWER/FIRST\_FIX时建议设置maxAccuracy为大于100的值。 |
| timeoutMs | number | 否 | 是 | 表示超时时间，单位是毫秒，最小为1000毫秒。默认值是5000。取值范围为大于等于1000。 |

## ContinuousLocationRequest12+

PhonePC/2in1TabletTVWearable

持续定位的请求参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| interval | number | 否 | 否 | 表示上报位置信息的时间间隔，单位是秒。默认值为1，取值范围为大于等于0。等于0时对位置上报时间间隔无限制。 |
| locationScenario | [UserActivityScenario](js-apis-geolocationmanager.md#useractivityscenario12) | [PowerConsumptionScenario](js-apis-geolocationmanager.md#powerconsumptionscenario12) | 否 | 否 | 表示定位的场景信息。取值范围见[UserActivityScenario](js-apis-geolocationmanager.md#useractivityscenario12)和[PowerConsumptionScenario](js-apis-geolocationmanager.md#powerconsumptionscenario12)的定义。 |
| needPoi19+ | boolean | 否 | 是 | 表示是否需要获取当前位置附近的POI信息。false代表不需要获取当前位置附近的POI信息，true代表需要获取当前位置附近的POI信息。不设置时，默认值为false。  该参数仅在精确位置功能场景（即同时授权了ohos.permission.APPROXIMATELY\_LOCATION和ohos.permission.LOCATION 权限）下有效，模糊位置功能生效场景（即仅授权了ohos.permission.APPROXIMATELY\_LOCATION 权限）下不返回POI信息。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |

## SingleLocationRequest12+

PhonePC/2in1TabletTVWearable

单次定位的请求参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| locatingPriority | [LocatingPriority](js-apis-geolocationmanager.md#locatingpriority12) | 否 | 否 | 表示优先级信息。取值范围见[LocatingPriority](js-apis-geolocationmanager.md#locatingpriority12)的定义。 |
| locatingTimeoutMs | number | 否 | 否 | 表示超时时间，单位是毫秒，最小为1000毫秒。取值范围为大于等于1000。 |
| needPoi19+ | boolean | 否 | 是 | 表示是否需要获取当前位置附近的POI信息。false代表不需要获取当前位置附近的POI信息，true代表需要获取当前位置附近的POI信息。不设置时，默认值为false。  该参数仅在精确位置功能场景（即同时授权了ohos.permission.APPROXIMATELY\_LOCATION和ohos.permission.LOCATION 权限）下有效，模糊位置功能生效场景（即仅授权了ohos.permission.APPROXIMATELY\_LOCATION 权限）下不返回POI信息。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |

## SatelliteStatusInfo

PhoneTabletWearable

卫星状态信息。

**系统能力**：SystemCapability.Location.Location.Gnss

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| satellitesNumber | number | 否 | 否 | 表示卫星个数。取值范围为大于等于0。 |
| satelliteIds | Array<number> | 否 | 否 | 表示每个卫星的ID，数组类型。取值范围为大于等于0。 |
| carrierToNoiseDensitys | Array<number> | 否 | 否 | 表示载波噪声功率谱密度比，即cn0。取值范围为大于0。 |
| altitudes | Array<number> | 否 | 否 | 表示卫星高度角信息。单位是“度”，取值范围为-90到90。 |
| azimuths | Array<number> | 否 | 否 | 表示方位角。单位是“度”，取值范围为0到360。 |
| carrierFrequencies | Array<number> | 否 | 否 | 表示载波频率。单位是Hz，取值范围为大于等于0。 |
| satelliteConstellation12+ | Array<[SatelliteConstellationCategory](js-apis-geolocationmanager.md#satelliteconstellationcategory12)> | 否 | 是 | 表示卫星星座类型。 |
| satelliteAdditionalInfo12+ | Array<number> | 否 | 是 | 表示卫星的附加信息。  每个比特位代表不同含义，具体定义参见[SatelliteAdditionalInfo](js-apis-geolocationmanager.md#satelliteadditionalinfo12)。 |

## CachedGnssLocationsRequest

PhoneTabletWearable

请求订阅GNSS缓存位置上报功能接口的配置参数。

**系统能力**：SystemCapability.Location.Location.Gnss

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| reportingPeriodSec | number | 否 | 否 | 表示GNSS缓存位置上报的周期，单位是毫秒。取值范围为大于0。 |
| wakeUpCacheQueueFull | boolean | 否 | 否 | true表示GNSS芯片底层缓存队列满之后会主动唤醒AP芯片，并把缓存位置上报给应用。  false表示GNSS芯片底层缓存队列满之后不会主动唤醒AP芯片，会把缓存位置直接丢弃。 |

## Geofence

PhoneTablet

GNSS围栏的配置参数。目前只支持圆形围栏。

**系统能力**：SystemCapability.Location.Location.Geofence

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| latitude | number | 否 | 否 | 表示纬度。取值范围为-90到90。 |
| longitude | number | 否 | 否 | 表示经度。取值范围为-180到180。 |
| coordinateSystemType12+ | [CoordinateSystemType](js-apis-geolocationmanager.md#coordinatesystemtype12) | 否 | 是 | 表示地理围栏圆心坐标的坐标系。  APP应先使用[getGeofenceSupportedCoordTypes](js-apis-geolocationmanager.md#geolocationmanagergetgeofencesupportedcoordtypes12)查询支持的坐标系，然后传入正确的圆心坐标。 |
| radius | number | 否 | 否 | 表示圆形围栏的半径。单位是米，取值范围为大于0。 |
| expiration | number | 否 | 否 | 围栏存活的时间，单位是毫秒。取值范围为大于0。 |

## GeofenceRequest

PhoneTablet

请求添加GNSS围栏消息中携带的参数，包括定位场景和围栏信息。

**系统能力**：SystemCapability.Location.Location.Geofence

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scenario | [LocationRequestScenario](js-apis-geolocationmanager.md#locationrequestscenario) | 否 | 否 | 表示定位场景。 |
| geofence | [Geofence](js-apis-geolocationmanager.md#geofence) | 否 | 否 | 表示围栏信息。 |

## LocationCommand

PhonePC/2in1TabletTVWearable

扩展命令参数。

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scenario | [LocationRequestScenario](js-apis-geolocationmanager.md#locationrequestscenario) | 否 | 否 | 表示定位场景。 |
| command | string | 否 | 否 | 扩展命令字符串，字符串长度不超过100。 |

## Location

PhonePC/2in1TabletTVWearable

位置信息。

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| latitude | number | 否 | 否 | 表示纬度信息，正值表示北纬，负值表示南纬。取值范围为-90到90。仅支持WGS84坐标系。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| longitude | number | 否 | 否 | 表示经度信息，正值表示东经，负值表示西经。取值范围为-180到180。仅支持WGS84坐标系。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| altitude | number | 否 | 否 | 表示高度信息，单位米。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| accuracy | number | 否 | 否 | 表示精度信息，单位米。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| speed | number | 否 | 否 | 表示速度信息，单位米每秒。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| timeStamp | number | 否 | 否 | 表示位置时间戳，UTC格式，单位毫秒。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| direction | number | 否 | 否 | 表示航向信息。单位是“度”，取值范围为0到360。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| timeSinceBoot | number | 否 | 否 | 表示获取位置成功的时间戳，值表示从本次开机到获取位置成功所经过的时间，单位为纳秒。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| additions | Array<string> | 否 | 是 | 附加信息。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| additionSize | number | 否 | 是 | 附加信息数量。取值范围为大于等于0。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| additionsMap12+ | Map<string, string> | 否 | 是 | 附加信息。具体内容和顺序与additions一致。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| altitudeAccuracy12+ | number | 否 | 是 | 表示高度信息的精度，单位米。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| speedAccuracy12+ | number | 否 | 是 | 表示速度信息的精度，单位米每秒。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| directionAccuracy12+ | number | 否 | 是 | 表示航向信息的精度。单位是“度”，取值范围为0到360。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| uncertaintyOfTimeSinceBoot12+ | number | 否 | 是 | 表示位置时间戳的不确定度。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| sourceType12+ | [LocationSourceType](js-apis-geolocationmanager.md#locationsourcetype12) | 否 | 是 | 表示定位结果的来源。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| poi19+ | [PoiInfo](js-apis-geolocationmanager.md#poiinfo19) | 否 | 是 | 表示当前位置附近的POI信息。  **元服务API：** 从API version 19开始，该接口支持在元服务中使用。 |

## GeofenceTransition12+

PhoneTablet

地理围栏事件信息；包含地理围栏ID和具体的地理围栏事件。

**系统能力**：SystemCapability.Location.Location.Geofence

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| geofenceId | number | 否 | 否 | 表示地理围栏ID。 |
| transitionEvent | [GeofenceTransitionEvent](js-apis-geolocationmanager.md#geofencetransitionevent12) | 否 | 否 | 表示当前发生的地理围栏事件。 |
| beaconFence20+ | [BeaconFence](js-apis-geolocationmanager.md#beaconfence20) | 否 | 是 | beacon围栏的参数配置。仅beacon围栏使用。  从API version 20开始，支持该字段。 |

## GnssGeofenceRequest12+

PhoneTablet

GNSS地理围栏请求参数。

**系统能力**：SystemCapability.Location.Location.Geofence

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| geofence | [Geofence](js-apis-geolocationmanager.md#geofence) | 否 | 否 | 表示地理围栏信息，包含圆形围栏圆心坐标、半径等信息。 |
| monitorTransitionEvents | Array<[GeofenceTransitionEvent](js-apis-geolocationmanager.md#geofencetransitionevent12)> | 否 | 否 | 表示APP监听的地理围栏事件列表。数组长度不超过3。 |
| notifications | Array<[NotificationRequest](js-apis-notification.md#notificationrequest)> | 否 | 是 | 表示地理围栏事件发生后弹出的通知对象列表。  monitorTransitionEvents与notifications中的顺序要一一对应，例如monitorTransitionEvents[0]为[GeofenceTransitionEvent](js-apis-geolocationmanager.md#geofencetransitionevent12).GEOFENCE\_TRANSITION\_EVENT\_ENTER，那notifications[0]中就需要填入用户进入围栏时需要弹出的通知对象。默认值为空数组。 |
| geofenceTransitionCallback | AsyncCallback<[GeofenceTransition](js-apis-geolocationmanager.md#geofencetransition12)> | 否 | 否 | 表示用于接收地理围栏事件的回调函数。 |
| loiterTimeMs23+ | number | 否 | 是 | 徘徊时间，单位为毫秒，需关注GEOFENCE\_TRANSITION\_DWELL事件。若设备在多边形围栏内徘徊时间达到该值，则上报GEOFENCE\_TRANSITION\_DWELL事件。徘徊状态检测周期为10000毫秒。例如：设置15000，将在驻留超过20000毫秒时上报驻留状态；设置5000，将在驻留超过10000毫秒时上报驻留状态。 |
| fenceExtensionAbilityName23+ | string | 否 | 是 | FenceExtensionAbility名称，参见[FenceExtensionAbility](js-apis-app-ability-fenceextensionability.md)。后台拉起需要申请后台定位权限，权限申请方式参见[申请位置权限开发指导](../harmonyos-guides/location-permission-guidelines.md#开发步骤)。 |

## CountryCode

PhonePC/2in1TabletTVWearable

国家码信息，包含国家码字符串和国家码的来源信息。

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| country | string | 否 | 否 | 表示国家码字符串。 |
| type | [CountryCodeType](js-apis-geolocationmanager.md#countrycodetype) | 否 | 否 | 表示国家码信息来源。 |

## LocationRequestPriority

PhonePC/2in1TabletTVWearable

位置请求中位置信息优先级类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNSET | 0x200 | 表示未设置优先级，表示[LocationRequestPriority](js-apis-geolocationmanager.md#locationrequestpriority)无效。 |
| ACCURACY | 0x201 | 表示精度优先。  定位精度优先策略主要以GNSS定位技术为主。我们会在GNSS提供稳定位置结果之前使用网络定位技术提供服务。在持续定位过程中，如果超过30秒无法获取GNSS定位结果则使用网络定位技术。对设备的硬件资源消耗较大，功耗较大。 |
| LOW\_POWER | 0x202 | 表示低功耗优先。  低功耗定位优先策略仅使用网络定位技术，在室内和户外场景均可提供定位服务，因为其依赖周边基站、可见WLAN、蓝牙设备的分布情况，定位结果的精度波动范围较大，推荐在对定位结果精度要求不高的场景下使用该策略，可以有效节省设备功耗。 |
| FIRST\_FIX | 0x203 | 表示快速获取位置优先，如果应用希望快速拿到一个位置，可以将优先级设置为该字段。  快速定位优先策略会同时使用GNSS定位和网络定位技术，以便在室内和户外场景下均可以快速获取到位置结果；当各种定位技术都有提供位置结果时，系统会选择其中精度较好的结果返回给应用。因为对各种定位技术同时使用，对设备的硬件资源消耗较大，功耗也较大。 |

## LocationRequestScenario

PhonePC/2in1TabletTVWearable

位置请求中定位场景类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Core

说明

当使用NAVIGATION/TRAJECTORY\_TRACKING/CAR\_HAILING场景进行单次定位或持续定位时，我们会在GNSS提供稳定位置结果之前使用网络定位技术提供服务；在持续定位时，如果超过30秒无法获取GNSS定位结果则会使用网络定位技术获取位置。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNSET | 0x300 | 表示未设置场景信息。  表示[LocationRequestScenario](js-apis-geolocationmanager.md#locationrequestscenario)字段无效。 |
| NAVIGATION | 0x301 | 表示导航场景。  适用于在户外获取设备实时位置的场景，如车载、步行导航。  主要使用GNSS定位技术提供定位服务，功耗较高。 |
| TRAJECTORY\_TRACKING | 0x302 | 表示运动轨迹记录场景。  适用于记录用户位置轨迹的场景，如运动类应用记录轨迹功能。  主要使用GNSS定位技术提供定位服务，功耗较高。 |
| CAR\_HAILING | 0x303 | 表示打车场景。  适用于用户出行打车时定位当前位置的场景，如网约车类应用。  主要使用GNSS定位技术提供定位服务，功耗较高。 |
| DAILY\_LIFE\_SERVICE | 0x304 | 表示日常服务使用场景。  适用于不需要定位用户精确位置的使用场景，如新闻资讯、网购、点餐类应用。  该场景仅使用网络定位技术提供定位服务，功耗较低。 |
| NO\_POWER | 0x305 | 表示无功耗功场景，这种场景下不会主动触发定位，会在其他应用定位时，才给当前应用返回位置。 |

## CountryCodeType

PhonePC/2in1TabletTVWearable

国家码来源类型。

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COUNTRY\_CODE\_FROM\_LOCALE | 1 | 从全球化模块的语言配置信息中获取到的国家码。 |
| COUNTRY\_CODE\_FROM\_SIM | 2 | 从SIM卡中获取到的国家码。 |
| COUNTRY\_CODE\_FROM\_LOCATION | 3 | 基于用户的位置信息，通过逆地理编码查询到的国家码。 |
| COUNTRY\_CODE\_FROM\_NETWORK | 4 | 从蜂窝网络注册信息中获取到的国家码。 |

## CoordinateSystemType12+

PhoneTablet

坐标系类型。

**系统能力**：SystemCapability.Location.Location.Geofence

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WGS84 | 1 | World Geodetic System 1984，是为GPS全球定位系统使用而建立的坐标系统。 |
| GCJ02 | 2 | GCJ-02是由中国国家测绘局制订的地理信息系统的坐标系统。 |

## GeofenceTransitionEvent12+

PhoneTablet

地理围栏事件。

**系统能力**：SystemCapability.Location.Location.Geofence

| 名称 | 值 | 说明 |
| --- | --- | --- |
| GEOFENCE\_TRANSITION\_EVENT\_ENTER | 1 | 该事件表示设备从地理围栏外进入地理围栏内。 |
| GEOFENCE\_TRANSITION\_EVENT\_EXIT | 2 | 该事件表示设备从地理围栏内退出到地理围栏外。 |
| GEOFENCE\_TRANSITION\_EVENT\_DWELL | 4 | 该事件表示设备在地理围栏范围内，且持续徘徊超过10秒。 |

## SatelliteConstellationCategory12+

PhoneTabletWearable

卫星星座类型。

**系统能力**：SystemCapability.Location.Location.Gnss

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CONSTELLATION\_CATEGORY\_UNKNOWN | 0 | 默认值。 |
| CONSTELLATION\_CATEGORY\_GPS | 1 | GPS（Global Positioning System），即全球定位系统，是美国研制发射的一种以人造地球卫星为基础的高精度无线电导航的定位系统。 |
| CONSTELLATION\_CATEGORY\_SBAS | 2 | SBAS（Satellite-Based Augmentation System），即星基增强系统，通过地球静止轨道（GEO）卫星搭载卫星导航增强信号转发器，可以向用户播发星历误差、卫星钟差、电离层延迟等多种修正信息，实现对于原有卫星导航系统定位精度的改进。 |
| CONSTELLATION\_CATEGORY\_GLONASS | 3 | GLONASS（GLOBAL NAVIGATION SATELLITE SYSTEM），是苏联/俄罗斯研制卫星导航系统。 |
| CONSTELLATION\_CATEGORY\_QZSS | 4 | QZSS（Quasi-Zenith Satellite System），即准天顶卫星系统，是以三颗人造卫星透过时间转移完成全球定位系统区域性功能的卫星扩增系统，是日本研发的卫星系统。 |
| CONSTELLATION\_CATEGORY\_BEIDOU | 5 | 北斗卫星导航系统（Beidou Navigation Satellite System）是中国自行研制的全球卫星导航系统。 |
| CONSTELLATION\_CATEGORY\_GALILEO | 6 | GALILEO（Galileo satellite navigation system），即伽利略卫星导航系统，是由欧盟研制和建立的全球卫星导航定位系统。 |
| CONSTELLATION\_CATEGORY\_IRNSS | 7 | IRNSS（Indian Regional Navigation Satellite System），即印度区域导航卫星系统，是一个由印度空间研究组织（ISRO）发展的自由区域型卫星导航系统。 |

## SatelliteAdditionalInfo12+

PhoneTabletWearable

卫星附加信息类型。

**系统能力**：SystemCapability.Location.Location.Gnss

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SATELLITES\_ADDITIONAL\_INFO\_NULL | 0 | 默认值。 |
| SATELLITES\_ADDITIONAL\_INFO\_EPHEMERIS\_DATA\_EXIST | 1 | 表示本卫星具有星历数据。 |
| SATELLITES\_ADDITIONAL\_INFO\_ALMANAC\_DATA\_EXIST | 2 | 表示本卫星具有年历数据。 |
| SATELLITES\_ADDITIONAL\_INFO\_USED\_IN\_FIX | 4 | 表示在最新的位置解算中使用了本卫星。 |
| SATELLITES\_ADDITIONAL\_INFO\_CARRIER\_FREQUENCY\_EXIST | 8 | 表示本卫星具有载波频率。 |

## PowerConsumptionScenario12+

PhonePC/2in1TabletTVWearable

位置请求中的功耗场景类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| HIGH\_POWER\_CONSUMPTION | 0x601 | 高功耗。  以GNSS定位技术为主。我们会在GNSS提供稳定位置结果之前使用网络定位技术提供服务；在持续定位时，如果超过30秒无法获取GNSS定位结果则会使用网络定位技术获取位置。对设备的硬件资源消耗较大，功耗较大。 |
| LOW\_POWER\_CONSUMPTION | 0x602 | 低功耗。  适用于对用户位置精度要求不高的使用场景，如新闻资讯、网购、点餐类应用。  该场景仅使用网络定位技术提供定位服务，功耗较低。 |
| NO\_POWER\_CONSUMPTION | 0x603 | 无功耗。  这种场景下不会主动触发定位，会在其他应用定位时，才给当前应用返回位置。 |

## UserActivityScenario12+

PhonePC/2in1TabletTVWearable

位置请求中的用户活动场景类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Core

说明

当使用NAVIGATION/SPORT/TRANSPORT场景进行单次定位或持续定位时，我们会在GNSS提供稳定位置结果之前使用网络定位技术提供服务；在持续定位时，如果超过30秒无法获取GNSS定位结果则会使用网络定位技术获取位置。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NAVIGATION | 0x401 | 表示导航场景。  适用于在户外获取设备实时位置的场景，如车载、步行导航。  主要使用GNSS定位技术提供定位服务，功耗较高。 |
| SPORT | 0x402 | 表示运动场景。  适用于记录用户位置轨迹的场景，如运动类应用记录轨迹功能。  主要使用GNSS定位技术提供定位服务，功耗较高。 |
| TRANSPORT | 0x403 | 表示出行场景。  适用于用户出行场景，如打车、乘坐公共交通等场景。  主要使用GNSS定位技术提供定位服务，功耗较高。 |
| DAILY\_LIFE\_SERVICE | 0x404 | 表示日常服务使用场景。  适用于不需要定位用户精确位置的使用场景，如新闻资讯、网购、点餐类应用。  该场景仅使用网络定位技术提供定位服务，功耗较低。 |

## LocatingPriority12+

PhonePC/2in1TabletTVWearable

单次位置请求中的优先级类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PRIORITY\_ACCURACY | 0x501 | 表示精度优先。  定位精度优先策略会同时使用GNSS定位和网络定位技术，并把一段时间内精度较好的结果返回给应用；这个时间段长度为[SingleLocationRequest](js-apis-geolocationmanager.md#singlelocationrequest12).locatingTimeoutMs与“30秒”中的较小者。  对设备的硬件资源消耗较大，功耗较大。 |
| PRIORITY\_LOCATING\_SPEED | 0x502 | 表示快速获取位置优先，如果应用希望快速拿到一个位置，可以将优先级设置为该类型。  快速定位优先策略会同时使用GNSS定位和网络定位技术，以便在室内和户外场景下均可以快速获取到位置结果，我们会把最先拿到的定位结果返回给应用。对设备的硬件资源消耗较大，功耗也较大。 |

## LocationError12+

PhonePC/2in1TabletTVWearable

持续定位过程中的错误信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LOCATING\_FAILED\_DEFAULT | -1 | 默认值。 |
| LOCATING\_FAILED\_LOCATION\_PERMISSION\_DENIED | -2 | 表示ohos.permission.APPROXIMATELY\_LOCATION权限或ohos.permission.LOCATION权限校验失败导致持续定位失败。 |
| LOCATING\_FAILED\_BACKGROUND\_PERMISSION\_DENIED | -3 | 表示应用在后台时位置权限校验失败导致持续定位失败。APP在后台定位时的位置权限申请方式参见[申请位置权限开发指导](../harmonyos-guides/location-permission-guidelines.md)。 |
| LOCATING\_FAILED\_LOCATION\_SWITCH\_OFF | -4 | 表示位置信息开关关闭导致持续定位失败。 |
| LOCATING\_FAILED\_INTERNET\_ACCESS\_FAILURE | -5 | 表示无法访问网络，导致网络定位失败。 |

## LocationSourceType12+

PhonePC/2in1TabletTVWearable

定位结果的来源。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| GNSS | 1 | 表示定位结果来自于GNSS定位技术。 |
| NETWORK | 2 | 表示定位结果来自于网络定位技术。 |
| INDOOR | 3 | 表示定位结果来自于室内高精度定位技术。 |
| RTK | 4 | 表示定位结果来自于室外高精度定位技术。 |

## BluetoothScanResult16+

PhonePC/2in1TabletTVWearable

蓝牙扫描结果。

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 表示扫描到的设备地址。例如："XX:XX:XX:XX:XX:XX"。 |
| rssi | number | 否 | 否 | 表示扫描到的设备的rssi值，单位dBm。 |
| data | ArrayBuffer | 否 | 是 | 表示扫描到的设备发送的广播包。 |
| deviceName | string | 否 | 否 | 表示扫描到的设备名称。 |
| connectable | boolean | 否 | 否 | 表示扫描到的设备是否可连接。true表示可连接，false表示不可连接。 |

## Poi19+

PhonePC/2in1TabletTVWearable

POI(Point of Interest, 兴趣点)信息。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | 表示POI的ID。 |
| confidence | number | 否 | 否 | 表示POI信息的置信度。置信度越高，用户离该POI信息点越近。取值范围为0到1。 |
| name | string | 否 | 否 | 表示POI的名称。 |
| latitude | number | 否 | 否 | 表示POI所在的纬度。取值范围为-90到90。 |
| longitude | number | 否 | 否 | 表示POI所在的经度。取值范围为-180到180。 |
| administrativeArea | string | 否 | 否 | 表示POI所在的国家以下的一级行政区，一般是省/州。 |
| subAdministrativeArea | string | 否 | 否 | 表示POI所在的国家以下的二级行政区，一般是市。 |
| locality | string | 否 | 否 | 表示POI所在的城市信息，一般是市。 |
| subLocality | string | 否 | 否 | 表示POI所在的子城市信息，一般是区/县。 |
| address | string | 否 | 否 | 表示POI的详细地址。 |

## PoiInfo19+

PhonePC/2in1TabletTVWearable

POI信息结构体。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| poiArray | Array<[Poi](js-apis-geolocationmanager.md#poi19)> | 否 | 否 | 表示POI信息列表。 |
| timestamp | number | 否 | 否 | 表示获取到POI信息时的时间戳，UTC时间，单位毫秒。 |

## SportsType18+

PhonePC/2in1TabletTVWearable

运动类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RUNNING | 1 | 表示跑步。 |
| WALKING | 2 | 表示步行。 |
| CYCLING | 3 | 表示骑行。 |

## BeaconFenceInfoType20+

PhoneTablet

beacon围栏信息类型。当前仅支持设备制造商数据过滤。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Geofence

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BEACON\_MANUFACTURE\_DATA | 1 | 标识使用beacon设备制造商数据。 |

## BeaconManufactureData20+

PhoneTablet

beacon设备制造商数据。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Geofence

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| manufactureId | number | 否 | 否 | 制造商标识。 |
| manufactureData | ArrayBuffer | 否 | 否 | 厂商自定义数据。例如：[0x02,0x15,0x00...0xFF,0x11,0x22,0x33,0x44,0x55] |
| manufactureDataMask | ArrayBuffer | 否 | 否 | 搭配manufactureData使用，可设置过滤部分制造商数据，0xFF为全匹配，0x00为模糊匹配。例如：[0xFF,0xFF,0xFF...0xFF,0xFF,0xFF,0xFF,0xFF,0xFF] |

## BeaconFence20+

PhoneTablet

beacon围栏的参数配置。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Geofence

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| identifier | string | 否 | 否 | beacon围栏标识。可自行定义，如："123", "beaconName"。 |
| beaconFenceInfoType | [BeaconFenceInfoType](js-apis-geolocationmanager.md#beaconfenceinfotype20) | 否 | 否 | beacon围栏信息类型。 |
| manufactureData | [BeaconManufactureData](js-apis-geolocationmanager.md#beaconmanufacturedata20) | 否 | 是 | beacon设备制造商数据。 |

## BeaconFenceRequest20+

PhoneTablet

beacon围栏请求参数。transitionCallback与fenceExtensionAbilityName任选其一，都不填则参数无效。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Geofence

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| beacon | [BeaconFence](js-apis-geolocationmanager.md#beaconfence20) | 否 | 否 | beacon围栏的参数配置。 |
| transitionCallback | Callback<[GeofenceTransition](js-apis-geolocationmanager.md#geofencetransition12)> | 否 | 是 | beacon围栏事件信息。默认值为undefined。仅支持前台回调。 |
| fenceExtensionAbilityName | string | 否 | 是 | [FenceExtensionAbility](js-apis-app-ability-fenceextensionability.md)名称。默认值为空字符串。 |

## geoLocationManager.on('locationChange')

PhonePC/2in1TabletTVWearable

on(type: 'locationChange', request: LocationRequest | ContinuousLocationRequest, callback: Callback<Location>): void

开启位置变化订阅，并发起定位请求。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.APPROXIMATELY\_LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“locationChange”，表示位置变化。 |
| request | [LocationRequest](js-apis-geolocationmanager.md#locationrequest) | [ContinuousLocationRequest](js-apis-geolocationmanager.md#continuouslocationrequest12) | 是 | 设置位置请求参数。  ContinuousLocationRequest为API12新增参数。 |
| callback | Callback<[Location](js-apis-geolocationmanager.md#location)> | 是 | 回调函数，返回位置信息。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.on('locationChange')} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';

3. // 方式一：使用LocationRequest作为入参
4. let requestInfo: geoLocationManager.LocationRequest = {
5. 'priority': geoLocationManager.LocationRequestPriority.FIRST_FIX,
6. 'scenario': geoLocationManager.LocationRequestScenario.UNSET,
7. 'timeInterval': 1,
8. 'distanceInterval': 0,
9. 'maxAccuracy': 0
10. };
11. let locationChange = (location: geoLocationManager.Location): void => {
12. console.info('locationChange: data: ' + JSON.stringify(location));
13. };
14. try {
15. geoLocationManager.on('locationChange', requestInfo, locationChange);
16. } catch (err) {
17. console.error("errCode:" + err.code + ", message:" + err.message);
18. }

20. // 方式二：使用ContinuousLocationRequest作为入参
21. let request: geoLocationManager.ContinuousLocationRequest = {
22. 'interval': 1,
23. 'locationScenario': geoLocationManager.UserActivityScenario.NAVIGATION
24. };
25. let locationCallback = (location: geoLocationManager.Location): void => {
26. console.info('locationCallback: data: ' + JSON.stringify(location));
27. };
28. try {
29. geoLocationManager.on('locationChange', request, locationCallback);
30. } catch (err) {
31. console.error("errCode:" + err.code + ", message:" + err.message);
32. }
```

## geoLocationManager.off('locationChange')

PhonePC/2in1TabletTVWearable

off(type: 'locationChange', callback?: Callback<Location>): void

关闭位置变化订阅，并删除对应的定位请求。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.APPROXIMATELY\_LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“locationChange”，表示位置变化。 |
| callback | Callback<[Location](js-apis-geolocationmanager.md#location)> | 否 | 需要取消订阅的回调函数。该回调函数需要与on接口传入的回调函数保持一致。若无此参数，则取消当前类型的所有订阅。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.off('locationChange')} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';

3. let requestInfo: geoLocationManager.LocationRequest = {
4. 'priority': geoLocationManager.LocationRequestPriority.FIRST_FIX,
5. 'scenario': geoLocationManager.LocationRequestScenario.UNSET,
6. 'timeInterval': 1,
7. 'distanceInterval': 0,
8. 'maxAccuracy': 0
9. };
10. let locationChange = (location: geoLocationManager.Location): void => {
11. console.info('locationChange: data: ' + JSON.stringify(location));
12. };
13. try {
14. geoLocationManager.on('locationChange', requestInfo, locationChange);
15. geoLocationManager.off('locationChange', locationChange);
16. } catch (err) {
17. console.error("errCode:" + err.code + ", message:" + err.message);
18. }
```

## geoLocationManager.on('locationError')12+

PhonePC/2in1TabletTVWearable

on(type: 'locationError', callback: Callback<LocationError>): void

订阅持续定位过程中的错误码。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.APPROXIMATELY\_LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“locationError”，表示持续定位过程中的错误码变化。 |
| callback | Callback<[LocationError](js-apis-geolocationmanager.md#locationerror12)> | 是 | 回调函数，返回持续定位过程中的错误码。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.on('locationError')} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';

3. let requestInfo: geoLocationManager.LocationRequest = {
4. 'priority': geoLocationManager.LocationRequestPriority.FIRST_FIX,
5. 'scenario': geoLocationManager.LocationRequestScenario.UNSET,
6. 'timeInterval': 1,
7. 'distanceInterval': 0,
8. 'maxAccuracy': 0
9. };
10. let locationChange = (location: geoLocationManager.Location): void => {
11. console.info('locationChange: data: ' + JSON.stringify(location));
12. };
13. try {
14. geoLocationManager.on('locationChange', requestInfo, locationChange);
15. } catch (err) {
16. console.error("errCode:" + err.code + ", message:" + err.message);
17. }

19. let locationErrorChange = (errcode: geoLocationManager.LocationError): void => {
20. console.info('locationErrorChange: data: ' + JSON.stringify(errcode));
21. };
22. try {
23. geoLocationManager.on('locationError', locationErrorChange);
24. } catch (err) {
25. console.error("errCode:" + err.code + ", message:" + err.message);
26. }
```

## geoLocationManager.off('locationError')12+

PhonePC/2in1TabletTVWearable

off(type: 'locationError', callback?: Callback<LocationError>): void

取消订阅持续定位过程中的错误码。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.APPROXIMATELY\_LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“locationError”，表示持续定位过程中的错误码变化。 |
| callback | Callback<[LocationError](js-apis-geolocationmanager.md#locationerror12)> | 否 | 需要取消订阅的回调函数。该回调函数需要与on接口传入的回调函数保持一致。若无此参数，则取消当前类型的所有订阅。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.off('locationError')} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';

3. let locationErrorChange = (errcode: geoLocationManager.LocationError): void => {
4. console.info('locationErrorChange: data: ' + JSON.stringify(errcode));
5. };
6. try {
7. geoLocationManager.on('locationError', locationErrorChange);
8. geoLocationManager.off('locationError', locationErrorChange);
9. } catch (err) {
10. console.error("errCode:" + err.code + ", message:" + err.message);
11. }
```

## geoLocationManager.on('locationEnabledChange')

PhonePC/2in1TabletTVWearable

on(type: 'locationEnabledChange', callback: Callback<boolean>): void

订阅位置服务状态变化。使用callback异步回调。

**系统能力**：SystemCapability.Location.Location.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“locationEnabledChange”，表示位置服务状态。 |
| callback | Callback<boolean> | 是 | 回调函数。返回true表示位置信息开关已经开启；返回false表示位置信息开关已经关闭。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.on('locationEnabledChange')} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';

3. let locationEnabledChange = (state: boolean): void => {
4. console.info('locationEnabledChange: ' + JSON.stringify(state));
5. }
6. try {
7. geoLocationManager.on('locationEnabledChange', locationEnabledChange);
8. } catch (err) {
9. console.error("errCode:" + err.code + ", message:" + err.message);
10. }
```

## geoLocationManager.off('locationEnabledChange')

PhonePC/2in1TabletTVWearable

off(type: 'locationEnabledChange', callback?: Callback<boolean>): void

取消订阅位置服务状态变化。

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“locationEnabledChange”，表示位置服务状态。 |
| callback | Callback<boolean> | 否 | 需要取消订阅的回调函数。返回true表示位置信息开关已经开启；返回false表示位置信息开关已经关闭。该回调函数需要与on接口传入的回调函数保持一致。若无此参数，则取消当前类型的所有订阅。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.off('locationEnabledChange')} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';

3. let locationEnabledChange = (state: boolean): void => {
4. console.info('locationEnabledChange: state: ' + JSON.stringify(state));
5. }
6. try {
7. geoLocationManager.on('locationEnabledChange', locationEnabledChange);
8. geoLocationManager.off('locationEnabledChange', locationEnabledChange);
9. } catch (err) {
10. console.error("errCode:" + err.code + ", message:" + err.message);
11. }
```

## geoLocationManager.on('cachedGnssLocationsChange')

PhoneTabletWearable

on(type: 'cachedGnssLocationsChange', request: CachedGnssLocationsRequest, callback: Callback<Array<Location>>): void

订阅缓存GNSS定位结果上报事件。该接口功能由GNSS定位芯片提供（仅部分型号支持），如果设备无此芯片或使用的芯片型号不支持该功能，则返回错误码801（Capability not supported）。使用callback异步回调。

**需要权限**：ohos.permission.APPROXIMATELY\_LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“cachedGnssLocationsChange”，表示GNSS缓存定位结果上报。 |
| request | [CachedGnssLocationsRequest](js-apis-geolocationmanager.md#cachedgnsslocationsrequest) | 是 | GNSS缓存功能配置参数。 |
| callback | Callback<Array<[Location](js-apis-geolocationmanager.md#location)>> | 是 | 回调函数，返回GNSS缓存位置。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.on('cachedGnssLocationsChange')} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';

3. let cachedLocationsCb = (locations: Array<geoLocationManager.Location>): void => {
4. console.info('cachedGnssLocationsChange: locations: ' + JSON.stringify(locations));
5. }
6. let requestInfo: geoLocationManager.CachedGnssLocationsRequest = {
7. 'reportingPeriodSec': 10,
8. 'wakeUpCacheQueueFull': true
9. };
10. try {
11. geoLocationManager.on('cachedGnssLocationsChange', requestInfo, cachedLocationsCb);
12. } catch (err) {
13. console.error("errCode:" + err.code + ", message:" + err.message);
14. }
```

## geoLocationManager.off('cachedGnssLocationsChange')

PhoneTabletWearable

off(type: 'cachedGnssLocationsChange', callback?: Callback<Array<Location>>): void

取消订阅缓存GNSS定位结果上报事件。该接口功能由GNSS定位芯片提供（仅部分型号支持），如果设备无此芯片或使用的芯片型号不支持该功能，则返回错误码801（Capability not supported）。

**需要权限**：ohos.permission.APPROXIMATELY\_LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“cachedGnssLocationsChange”，表示GNSS缓存定位结果上报。 |
| callback | Callback<Array<[Location](js-apis-geolocationmanager.md#location)>> | 否 | 需要取消订阅的回调函数。该回调函数需要与on接口传入的回调函数保持一致。若无此参数，则取消当前类型的所有订阅。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.off('cachedGnssLocationsChange')} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';

3. let cachedLocationsCb = (locations: Array<geoLocationManager.Location>): void => {
4. console.info('cachedGnssLocationsChange: locations: ' + JSON.stringify(locations));
5. }
6. let requestInfo: geoLocationManager.CachedGnssLocationsRequest = {
7. 'reportingPeriodSec': 10,
8. 'wakeUpCacheQueueFull': true
9. };
10. try {
11. geoLocationManager.on('cachedGnssLocationsChange', requestInfo, cachedLocationsCb);
12. geoLocationManager.off('cachedGnssLocationsChange');
13. } catch (err) {
14. console.error("errCode:" + err.code + ", message:" + err.message);
15. }
```

## geoLocationManager.on('satelliteStatusChange')

PhoneTabletWearable

on(type: 'satelliteStatusChange', callback: Callback<SatelliteStatusInfo>): void

订阅GNSS卫星状态信息上报事件。使用callback异步回调。

**需要权限**：ohos.permission.APPROXIMATELY\_LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“satelliteStatusChange”，表示订阅GNSS卫星状态信息上报。 |
| callback | Callback<[SatelliteStatusInfo](js-apis-geolocationmanager.md#satellitestatusinfo)> | 是 | 回调函数，返回GNSS卫星状态信息。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.on('satelliteStatusChange')} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';

3. let gnssStatusCb = (satelliteStatusInfo: geoLocationManager.SatelliteStatusInfo): void => {
4. console.info('satelliteStatusChange: ' + JSON.stringify(satelliteStatusInfo));
5. // 表示卫星个数
6. let totalNumber: number = satelliteStatusInfo.satellitesNumber;
7. let satelliteIds: Array<number> = satelliteStatusInfo.satelliteIds;
8. let carrierToNoiseDensitys: Array<number> = satelliteStatusInfo.carrierToNoiseDensitys;
9. let altitudes: Array<number> = satelliteStatusInfo.altitudes;
10. let azimuths: Array<number> = satelliteStatusInfo.azimuths;
11. let carrierFrequencies: Array<number> = satelliteStatusInfo.carrierFrequencies;
12. let satelliteConstellations: Array<geoLocationManager.SatelliteConstellationCategory> | undefined = satelliteStatusInfo.satelliteConstellation;
13. let satelliteAdditionalInfos: Array<number> | undefined = satelliteStatusInfo.satelliteAdditionalInfo;
14. for (let i = 0;i < totalNumber; i++) {
15. // 卫星的ID
16. let satelliteId: number = satelliteIds[i];
17. // 表示卫星的ID为 ${satelliteId} 的卫星的载波噪声功率谱密度比
18. let carrierToNoiseDensity: number = carrierToNoiseDensitys[i];
19. // 表示卫星的ID为 ${satelliteId} 的卫星的高度角信息
20. let altitude: number = altitudes[i];
21. // 表示卫星的ID为 ${satelliteId} 的卫星的方位角
22. let azimuth: number = azimuths[i];
23. // 表示卫星的ID为 ${satelliteId} 的卫星的载波频率
24. let carrierFrequency: number = carrierFrequencies[i];
25. if (satelliteConstellations != undefined) {
26. // 表示卫星的ID为 ${satelliteId} 的卫星的星座类型
27. let satelliteConstellation: geoLocationManager.SatelliteConstellationCategory = satelliteConstellations[i];
28. }
29. if (satelliteAdditionalInfos != undefined) {
30. // 表示卫星的ID为 ${satelliteId} 的卫星的附加信息；表示是否在最新的位置解算中使用了本卫星，是否具有星历数据，是否具有年历数据，是否具有载波频率信息等。
31. let satelliteAdditionalInfo: number = satelliteAdditionalInfos[i];
32. }
33. }
34. }

36. try {
37. geoLocationManager.on('satelliteStatusChange', gnssStatusCb);
38. } catch (err) {
39. console.error("errCode:" + err.code + ", message:" + err.message);
40. }
```

## geoLocationManager.off('satelliteStatusChange')

PhoneTabletWearable

off(type: 'satelliteStatusChange', callback?: Callback<SatelliteStatusInfo>): void

取消订阅GNSS卫星状态信息上报事件。

**需要权限**：ohos.permission.APPROXIMATELY\_LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“satelliteStatusChange”，表示订阅GNSS卫星状态信息上报。 |
| callback | Callback<[SatelliteStatusInfo](js-apis-geolocationmanager.md#satellitestatusinfo)> | 否 | 需要取消订阅的回调函数。该回调函数需要与on接口传入的回调函数保持一致。若无此参数，则取消当前类型的所有订阅。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.off('satelliteStatusChange')} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';

3. let gnssStatusCb = (satelliteStatusInfo: geoLocationManager.SatelliteStatusInfo): void => {
4. console.info('satelliteStatusChange: ' + JSON.stringify(satelliteStatusInfo));
5. }
6. try {
7. geoLocationManager.on('satelliteStatusChange', gnssStatusCb);
8. geoLocationManager.off('satelliteStatusChange', gnssStatusCb);
9. } catch (err) {
10. console.error("errCode:" + err.code + ", message:" + err.message);
11. }
```

## geoLocationManager.on('nmeaMessage')

PhoneTabletWearable

on(type: 'nmeaMessage', callback: Callback<string>): void

订阅GNSS NMEA信息上报事件。使用callback异步回调。

**需要权限**：ohos.permission.LOCATION 和 ohos.permission.APPROXIMATELY\_LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“nmeaMessage”，表示订阅GNSS NMEA信息上报。 |
| callback | Callback<string> | 是 | 回调函数，返回GNSS NMEA信息。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.on('nmeaMessage')} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';

3. let nmeaCb = (str: string): void => {
4. console.info('nmeaMessage: ' + JSON.stringify(str));
5. }

7. try {
8. geoLocationManager.on('nmeaMessage', nmeaCb);
9. } catch (err) {
10. console.error("errCode:" + err.code + ", message:" + err.message);
11. }
```

## geoLocationManager.off('nmeaMessage')

PhoneTabletWearable

off(type: 'nmeaMessage', callback?: Callback<string>): void

取消订阅GNSS NMEA信息上报事件。

**需要权限**：ohos.permission.LOCATION 和 ohos.permission.APPROXIMATELY\_LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“nmeaMessage”，表示订阅GNSS NMEA信息上报。 |
| callback | Callback<string> | 否 | 需要取消订阅的回调函数。该回调函数需要与on接口传入的回调函数保持一致。若无此参数，则取消当前类型的所有订阅。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.off('nmeaMessage')} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';

3. let nmeaCb = (str: string): void => {
4. console.info('nmeaMessage: ' + JSON.stringify(str));
5. }

7. try {
8. geoLocationManager.on('nmeaMessage', nmeaCb);
9. geoLocationManager.off('nmeaMessage', nmeaCb);
10. } catch (err) {
11. console.error("errCode:" + err.code + ", message:" + err.message);
12. }
```

## geoLocationManager.on('gnssFenceStatusChange')

PhoneTablet

on(type: 'gnssFenceStatusChange', request: GeofenceRequest, want: WantAgent): void

添加一个围栏，并订阅地理围栏事件。该接口功能由GNSS定位芯片提供（仅部分型号支持），如果设备无此芯片或使用的芯片型号不支持该功能，则返回错误码801（Capability not supported）。

**需要权限**：ohos.permission.APPROXIMATELY\_LOCATION

**系统能力**：SystemCapability.Location.Location.Geofence

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“gnssFenceStatusChange”，表示订阅围栏事件上报。 |
| request | [GeofenceRequest](js-apis-geolocationmanager.md#geofencerequest) | 是 | 围栏的配置参数。 |
| want | [WantAgent](js-apis-app-ability-wantagent.md) | 是 | 用于接收地理围栏事件上报（进出围栏）。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.on('gnssFenceStatusChange')} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |
| 3301600 | Failed to operate the geofence. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';
2. import { wantAgent } from '@kit.AbilityKit';

5. let wantAgentInfo: wantAgent.WantAgentInfo = {
6. wants: [
7. {
8. bundleName: "com.example.myapplication",
9. abilityName: "EntryAbility",
10. action: "action1"
11. }
12. ],
13. actionType: wantAgent.OperationType.START_ABILITY,
14. requestCode: 0,
15. wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
16. };

18. wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj) => {
19. let requestInfo: geoLocationManager.GeofenceRequest = {
20. 'scenario': 0x301,
21. "geofence": { "latitude": 31.12, "longitude": 121.11, "radius": 100, "expiration": 10000 }
22. };
23. try {
24. geoLocationManager.on('gnssFenceStatusChange', requestInfo, wantAgentObj);
25. } catch (err) {
26. console.error("errCode:" + err.code + ", message:" + err.message);
27. }
28. });
```

## geoLocationManager.off('gnssFenceStatusChange')

PhoneTablet

off(type: 'gnssFenceStatusChange', request: GeofenceRequest, want: WantAgent): void

删除一个围栏，并取消订阅该围栏事件。该接口功能由GNSS定位芯片提供（仅部分型号支持），如果设备无此芯片或使用的芯片型号不支持该功能，则返回错误码801（Capability not supported）。

**需要权限**：ohos.permission.APPROXIMATELY\_LOCATION

**系统能力**：SystemCapability.Location.Location.Geofence

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“gnssFenceStatusChange”，表示订阅围栏事件上报。 |
| request | [GeofenceRequest](js-apis-geolocationmanager.md#geofencerequest) | 是 | 围栏的配置参数。 |
| want | [WantAgent](js-apis-app-ability-wantagent.md) | 是 | 用于接收地理围栏事件上报（进出围栏）。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.off('gnssFenceStatusChange')} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |
| 3301600 | Failed to operate the geofence. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';
2. import { wantAgent } from '@kit.AbilityKit';

5. let wantAgentInfo: wantAgent.WantAgentInfo = {
6. wants: [
7. {
8. bundleName: "com.example.myapplication",
9. abilityName: "EntryAbility",
10. action: "action1",
11. }
12. ],
13. actionType: wantAgent.OperationType.START_ABILITY,
14. requestCode: 0,
15. wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
16. };

18. wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj) => {
19. let requestInfo: geoLocationManager.GeofenceRequest = {
20. 'scenario': 0x301,
21. "geofence": { "latitude": 31.12, "longitude": 121.11, "radius": 100, "expiration": 10000 }
22. };
23. try {
24. geoLocationManager.on('gnssFenceStatusChange', requestInfo, wantAgentObj);
25. geoLocationManager.off('gnssFenceStatusChange', requestInfo, wantAgentObj);
26. } catch (err) {
27. console.error("errCode:" + err.code + ", message:" + err.message);
28. }
29. });
```

## geoLocationManager.on('countryCodeChange')

PhonePC/2in1TabletTVWearable

on(type: 'countryCodeChange', callback: Callback<CountryCode>): void

订阅国家码信息变化事件。使用callback异步回调。

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“countryCodeChange”，表示订阅国家码信息变化事件。 |
| callback | Callback<[CountryCode](js-apis-geolocationmanager.md#countrycode)> | 是 | 回调函数，返回国家码信息。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.on('countryCodeChange')} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301500 | Failed to query the area information. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';

3. let callback = (code: geoLocationManager.CountryCode): void => {
4. console.info('countryCodeChange: ' + JSON.stringify(code));
5. }

7. try {
8. geoLocationManager.on('countryCodeChange', callback);
9. } catch (err) {
10. console.error("errCode:" + err.code + ", message:" + err.message);
11. }
```

## geoLocationManager.off('countryCodeChange')

PhonePC/2in1TabletTVWearable

off(type: 'countryCodeChange', callback?: Callback<CountryCode>): void

取消订阅国家码变化事件。

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“countryCodeChange”，表示取消订阅国家码信息变化事件。 |
| callback | Callback<[CountryCode](js-apis-geolocationmanager.md#countrycode)> | 否 | 需要取消订阅的回调函数。该回调函数需要与on接口传入的回调函数保持一致。若无此参数，则取消当前类型的所有订阅。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.off('countryCodeChange')} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301500 | Failed to query the area information. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';

3. let callback = (code: geoLocationManager.CountryCode): void => {
4. console.info('countryCodeChange: ' + JSON.stringify(code));
5. }

7. try {
8. geoLocationManager.on('countryCodeChange', callback);
9. geoLocationManager.off('countryCodeChange', callback);
10. } catch (err) {
11. console.error("errCode:" + err.code + ", message:" + err.message);
12. }
```

## geoLocationManager.getCurrentLocation

PhonePC/2in1TabletTVWearable

getCurrentLocation(request: CurrentLocationRequest | SingleLocationRequest, callback: AsyncCallback<Location>): void

获取当前位置，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.APPROXIMATELY\_LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [CurrentLocationRequest](js-apis-geolocationmanager.md#currentlocationrequest) | [SingleLocationRequest](js-apis-geolocationmanager.md#singlelocationrequest12) | 是 | 设置位置请求参数。  SingleLocationRequest为API12新增参数。 |
| callback | AsyncCallback<[Location](js-apis-geolocationmanager.md#location)> | 是 | 回调函数，返回当前位置信息。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.getCurrentLocation} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |
| 3301200 | Failed to obtain the geographical location. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. // 方式一：使用CurrentLocationRequest作为入参
4. let requestInfo: geoLocationManager.CurrentLocationRequest = {
5. 'priority': geoLocationManager.LocationRequestPriority.FIRST_FIX,
6. 'scenario': geoLocationManager.LocationRequestScenario.UNSET,
7. 'maxAccuracy': 0
8. };
9. let locationChange = (err: BusinessError, location: geoLocationManager.Location): void => {
10. if (err) {
11. console.error('locationChange: err=' + JSON.stringify(err));
12. }
13. if (location) {
14. console.info('locationChange: location=' + JSON.stringify(location));
15. }
16. };

18. try {
19. geoLocationManager.getCurrentLocation(requestInfo, locationChange);
20. } catch (err) {
21. console.error("errCode:" + err.code + ", message:" + err.message);
22. }

24. // 方式二：使用SingleLocationRequest作为入参
25. let request: geoLocationManager.SingleLocationRequest = {
26. 'locatingTimeoutMs': 10000,
27. 'locatingPriority': geoLocationManager.LocatingPriority.PRIORITY_ACCURACY
28. };
29. let locationCallback = (err: BusinessError, location: geoLocationManager.Location): void => {
30. if (err) {
31. console.error('locationChange: err=' + JSON.stringify(err));
32. }
33. if (location) {
34. console.info('locationChange: location=' + JSON.stringify(location));
35. }
36. };

38. try {
39. geoLocationManager.getCurrentLocation(request, locationCallback);
40. } catch (err) {
41. console.error("errCode:" + err.code + ", message:" + err.message);
42. }
```

## geoLocationManager.getCurrentLocation

PhonePC/2in1TabletTVWearable

getCurrentLocation(callback: AsyncCallback<Location>): void

获取当前位置，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.APPROXIMATELY\_LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[Location](js-apis-geolocationmanager.md#location)> | 是 | 回调函数，返回当前位置信息。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.getCurrentLocation} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |
| 3301200 | Failed to obtain the geographical location. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let locationChange = (err: BusinessError, location: geoLocationManager.Location) => {
5. if (err) {
6. console.error('locationChange: err=' + JSON.stringify(err));
7. }
8. if (location) {
9. console.info('locationChange: location=' + JSON.stringify(location));
10. }
11. };

13. try {
14. geoLocationManager.getCurrentLocation(locationChange);
15. } catch (err) {
16. console.error("errCode:" + err.code + ", message:" + err.message);
17. }
```

## geoLocationManager.getCurrentLocation

PhonePC/2in1TabletTVWearable

getCurrentLocation(request?: CurrentLocationRequest | SingleLocationRequest): Promise<Location>

获取当前位置，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.APPROXIMATELY\_LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [CurrentLocationRequest](js-apis-geolocationmanager.md#currentlocationrequest) | [SingleLocationRequest](js-apis-geolocationmanager.md#singlelocationrequest12) | 否 | 设置位置请求参数。  SingleLocationRequest为API12新增参数。若无此参数设置，则使用CurrentLocationRequest为默认值。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[Location](js-apis-geolocationmanager.md#location)> | Promise对象，返回当前位置信息。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.getCurrentLocation} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |
| 3301200 | Failed to obtain the geographical location. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 方式一：使用CurrentLocationRequest作为入参
5. let requestInfo: geoLocationManager.CurrentLocationRequest = {
6. 'priority': geoLocationManager.LocationRequestPriority.FIRST_FIX,
7. 'scenario': geoLocationManager.LocationRequestScenario.UNSET,
8. 'maxAccuracy': 0
9. };
10. try {
11. geoLocationManager.getCurrentLocation(requestInfo).then((result) => {
12. console.info('current location: ' + JSON.stringify(result));
13. })
14. .catch((error: BusinessError) => {
15. console.error('promise, getCurrentLocation: error=' + JSON.stringify(error));
16. });
17. } catch (err) {
18. console.error("errCode:" + err.code + ", message:" + err.message);
19. }

21. // 方式二：使用SingleLocationRequest作为入参
22. let request: geoLocationManager.SingleLocationRequest = {
23. 'locatingTimeoutMs': 10000,
24. 'locatingPriority': geoLocationManager.LocatingPriority.PRIORITY_ACCURACY
25. };
26. try {
27. geoLocationManager.getCurrentLocation(request).then((result) => {
28. console.info('current location: ' + JSON.stringify(result));
29. })
30. .catch((error: BusinessError) => {
31. console.error('promise, getCurrentLocation: error=' + JSON.stringify(error));
32. });
33. } catch (err) {
34. console.error("errCode:" + err.code + ", message:" + err.message);
35. }
```

## geoLocationManager.getLastLocation

PhonePC/2in1TabletTVWearable

getLastLocation(): Location

获取上一次位置。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.APPROXIMATELY\_LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [Location](js-apis-geolocationmanager.md#location) | 位置信息。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.getLastLocation} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |
| 3301200 | Failed to obtain the geographical location. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';

3. try {
4. let location = geoLocationManager.getLastLocation();
5. } catch (err) {
6. console.error("errCode:" + err.code + ", message:" + err.message);
7. }
```

## geoLocationManager.isLocationEnabled

PhonePC/2in1TabletTVWearable

isLocationEnabled(): boolean

判断位置服务是否已经开启。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Core

**返回值**：

| 类型 | 说明 |
| --- | --- |
| boolean | true：位置信息开关已开启。  false：位置信息开关已关闭。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call ${geoLocationManager.isLocationEnabled} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';

3. try {
4. let locationEnabled = geoLocationManager.isLocationEnabled();
5. } catch (err) {
6. console.error("errCode:" + err.code + ", message:" + err.message);
7. }
```

## geoLocationManager.getAddressesFromLocation

PhonePC/2in1TabletWearable

getAddressesFromLocation(request: ReverseGeoCodeRequest, callback: AsyncCallback<Array<GeoAddress>>): void

调用逆地理编码服务，将坐标转换为地理描述，使用callback异步回调。

**系统能力**：SystemCapability.Location.Location.Geocoder

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [ReverseGeoCodeRequest](js-apis-geolocationmanager.md#reversegeocoderequest) | 是 | 设置逆地理编码请求的相关参数。 |
| callback | AsyncCallback<Array<[GeoAddress](js-apis-geolocationmanager.md#geoaddress)>> | 是 | 回调函数，返回逆地理编码结果。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.getAddressesFromLocation} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301300 | Reverse geocoding query failed. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';

3. let reverseGeocodeRequest: geoLocationManager.ReverseGeoCodeRequest = {
4. "latitude": 31.12,
5. "longitude": 121.11,
6. "maxItems": 1
7. };
8. try {
9. geoLocationManager.getAddressesFromLocation(reverseGeocodeRequest, (err, data) => {
10. if (err) {
11. console.error('getAddressesFromLocation: err=' + JSON.stringify(err));
12. }
13. if (data) {
14. console.info('getAddressesFromLocation: data=' + JSON.stringify(data));
15. }
16. });
17. } catch (err) {
18. console.error("errCode:" + err.code + ", message:" + err.message);
19. }
```

## geoLocationManager.getAddressesFromLocation

PhonePC/2in1TabletWearable

getAddressesFromLocation(request: ReverseGeoCodeRequest): Promise<Array<GeoAddress>>

调用逆地理编码服务，将坐标转换为地理描述，使用Promise异步回调。

**系统能力**：SystemCapability.Location.Location.Geocoder

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [ReverseGeoCodeRequest](js-apis-geolocationmanager.md#reversegeocoderequest) | 是 | 设置逆地理编码请求的相关参数。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[GeoAddress](js-apis-geolocationmanager.md#geoaddress)>> | Promise对象，返回地理描述信息。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.getAddressesFromLocation} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301300 | Reverse geocoding query failed. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let reverseGeocodeRequest: geoLocationManager.ReverseGeoCodeRequest = {
5. "latitude": 31.12,
6. "longitude": 121.11,
7. "maxItems": 1
8. };
9. try {
10. geoLocationManager.getAddressesFromLocation(reverseGeocodeRequest).then((data) => {
11. console.info('getAddressesFromLocation: ' + JSON.stringify(data));
12. })
13. .catch((error: BusinessError) => {
14. console.error('promise, getAddressesFromLocation: error=' + JSON.stringify(error));
15. });
16. } catch (err) {
17. console.error("errCode:" + err.code + ", message:" + err.message);
18. }
```

## geoLocationManager.getAddressesFromLocationName

PhonePC/2in1TabletWearable

getAddressesFromLocationName(request: GeoCodeRequest, callback: AsyncCallback<Array<GeoAddress>>): void

调用地理编码服务，将地理描述转换为具体坐标，使用callback异步回调。

**系统能力**：SystemCapability.Location.Location.Geocoder

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [GeoCodeRequest](js-apis-geolocationmanager.md#geocoderequest) | 是 | 设置地理编码请求的相关参数。 |
| callback | AsyncCallback<Array<[GeoAddress](js-apis-geolocationmanager.md#geoaddress)>> | 是 | 回调函数，返回地理编码结果。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.getAddressesFromLocationName} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301400 | Geocoding query failed. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';

3. let geocodeRequest: geoLocationManager.GeoCodeRequest = { "description": "上海市浦东新区xx路xx号", "maxItems": 1 };
4. try {
5. geoLocationManager.getAddressesFromLocationName(geocodeRequest, (err, data) => {
6. if (err) {
7. console.error('getAddressesFromLocationName: err=' + JSON.stringify(err));
8. }
9. if (data) {
10. console.info('getAddressesFromLocationName: data=' + JSON.stringify(data));
11. }
12. });
13. } catch (err) {
14. console.error("errCode:" + err.code + ", message:" + err.message);
15. }
```

## geoLocationManager.getAddressesFromLocationName

PhonePC/2in1TabletWearable

getAddressesFromLocationName(request: GeoCodeRequest): Promise<Array<GeoAddress>>

调用地理编码服务，将地理描述转换为具体坐标，使用Promise异步回调。

**系统能力**：SystemCapability.Location.Location.Geocoder

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [GeoCodeRequest](js-apis-geolocationmanager.md#geocoderequest) | 是 | 设置地理编码请求的相关参数。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[GeoAddress](js-apis-geolocationmanager.md#geoaddress)>> | Promise对象，返回地理编码查询结果。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.getAddressesFromLocationName} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301400 | Geocoding query failed. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let geocodeRequest: geoLocationManager.GeoCodeRequest = { "description": "上海市浦东新区xx路xx号", "maxItems": 1 };
5. try {
6. geoLocationManager.getAddressesFromLocationName(geocodeRequest).then((result) => {
7. console.info('getAddressesFromLocationName: ' + JSON.stringify(result));
8. })
9. .catch((error: BusinessError) => {
10. console.error('promise, getAddressesFromLocationName: error=' + JSON.stringify(error));
11. });
12. } catch (err) {
13. console.error("errCode:" + err.code + ", message:" + err.message);
14. }
```

## geoLocationManager.isGeocoderAvailable

PhonePC/2in1TabletWearable

isGeocoderAvailable(): boolean

判断地理编码与逆地理编码服务状态。

**系统能力**：SystemCapability.Location.Location.Geocoder

**返回值**：

| 类型 | 说明 |
| --- | --- |
| boolean | true:地理编码与逆地理编码服务可用。  false：地理编码与逆地理编码服务不可用。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call ${geoLocationManager.isGeocoderAvailable} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';

3. try {
4. let isAvailable = geoLocationManager.isGeocoderAvailable();
5. } catch (err) {
6. console.error("errCode:" + err.code + ", message:" + err.message);
7. }
```

## geoLocationManager.getCachedGnssLocationsSize

PhoneTabletWearable

getCachedGnssLocationsSize(callback: AsyncCallback<number>): void

获取GNSS芯片缓存位置的个数。该接口功能由GNSS定位芯片提供（仅部分型号支持），如果设备无此芯片或使用的芯片型号不支持该功能，则返回错误码801（Capability not supported）。使用callback异步回调。

**需要权限**：ohos.permission.APPROXIMATELY\_LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数，返回GNSS芯片缓存位置个数。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.getCachedGnssLocationsSize} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';

3. try {
4. geoLocationManager.getCachedGnssLocationsSize((err, size) => {
5. if (err) {
6. console.error('getCachedGnssLocationsSize: err=' + JSON.stringify(err));
7. }
8. if (size) {
9. console.info('getCachedGnssLocationsSize: size=' + JSON.stringify(size));
10. }
11. });
12. } catch (err) {
13. console.error("errCode:" + err.code + ", message:" + err.message);
14. }
```

## geoLocationManager.getCachedGnssLocationsSize

PhoneTabletWearable

getCachedGnssLocationsSize(): Promise<number>

获取GNSS芯片缓存位置的个数。该接口功能由GNSS定位芯片提供（仅部分型号支持），如果设备无此芯片或使用的芯片型号不支持该功能，则返回错误码801（Capability not supported）。使用Promise异步回调。

**需要权限**：ohos.permission.APPROXIMATELY\_LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回GNSS缓存位置的个数。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.getCachedGnssLocationsSize} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. geoLocationManager.getCachedGnssLocationsSize().then((result) => {
6. console.info('promise, getCachedGnssLocationsSize: ' + JSON.stringify(result));
7. })
8. .catch((error: BusinessError) => {
9. console.error('promise, getCachedGnssLocationsSize: error=' + JSON.stringify(error));
10. });
11. } catch (err) {
12. console.error("errCode:" + err.code + ", message:" + err.message);
13. }
```

## geoLocationManager.flushCachedGnssLocations

PhoneTabletWearable

flushCachedGnssLocations(callback: AsyncCallback<void>): void

读取并清空GNSS芯片所有缓存位置。该接口功能由GNSS定位芯片提供（仅部分型号支持），如果设备无此芯片或使用的芯片型号不支持该功能，则返回错误码801（Capability not supported）。使用callback异步回调。

**需要权限**：ohos.permission.APPROXIMATELY\_LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当操作成功，err为undefined，否则为错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.flushCachedGnssLocations} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |
| 3301200 | Failed to obtain the geographical location. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';

3. try {
4. geoLocationManager.flushCachedGnssLocations((err) => {
5. if (err) {
6. console.error('flushCachedGnssLocations: err=' + JSON.stringify(err));
7. }
8. });
9. } catch (err) {
10. console.error("errCode:" + err.code + ", message:" + err.message);
11. }
```

## geoLocationManager.flushCachedGnssLocations

PhoneTabletWearable

flushCachedGnssLocations(): Promise<void>

读取并清空GNSS芯片所有缓存位置。该接口功能由GNSS定位芯片提供（仅部分型号支持），如果设备无此芯片或使用的芯片型号不支持该功能，则返回错误码801（Capability not supported）。使用Promise异步回调。

**需要权限**：ohos.permission.APPROXIMATELY\_LOCATION

**系统能力**：SystemCapability.Location.Location.Gnss

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.flushCachedGnssLocations} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |
| 3301200 | Failed to obtain the geographical location. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. geoLocationManager.flushCachedGnssLocations().then(() => {
6. console.info('promise, flushCachedGnssLocations success');
7. })
8. .catch((error: BusinessError) => {
9. console.error('promise, flushCachedGnssLocations: error=' + JSON.stringify(error));
10. });
11. } catch (err) {
12. console.error("errCode:" + err.code + ", message:" + err.message);
13. }
```

## geoLocationManager.sendCommand

PhonePC/2in1TabletTVWearable

sendCommand(command: LocationCommand, callback: AsyncCallback<void>): void

给位置服务子系统的各个部件发送扩展命令。使用callback异步回调。

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| command | [LocationCommand](js-apis-geolocationmanager.md#locationcommand) | 是 | 指定目标场景，和将要发送的命令（字符串）。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当命令发送成功，err为undefined，否则为错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.sendCommand} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';

3. let requestInfo: geoLocationManager.LocationCommand = { 'scenario': 0x301, 'command': "command_1" };
4. try {
5. geoLocationManager.sendCommand(requestInfo, (err) => {
6. if (err) {
7. console.error('sendCommand: err=' + JSON.stringify(err));
8. }
9. });
10. } catch (err) {
11. console.error("errCode:" + err.code + ", message:" + err.message);
12. }
```

## geoLocationManager.sendCommand

PhonePC/2in1TabletTVWearable

sendCommand(command: LocationCommand): Promise<void>

给位置服务子系统的各个部件发送扩展命令。使用Promise异步回调。

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| command | [LocationCommand](js-apis-geolocationmanager.md#locationcommand) | 是 | 指定目标场景，和将要发送的命令（字符串）。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.sendCommand} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let requestInfo: geoLocationManager.LocationCommand = { 'scenario': 0x301, 'command': "command_1" };
5. try {
6. geoLocationManager.sendCommand(requestInfo).then(() => {
7. console.info('promise, sendCommand success');
8. })
9. .catch((error: BusinessError) => {
10. console.error('promise, sendCommand: error=' + JSON.stringify(error));
11. });
12. } catch (err) {
13. console.error("errCode:" + err.code + ", message:" + err.message);
14. }
```

## geoLocationManager.getCountryCode

PhonePC/2in1TabletTVWearable

getCountryCode(callback: AsyncCallback<CountryCode>): void

查询当前的国家码。使用callback异步回调。

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[CountryCode](js-apis-geolocationmanager.md#countrycode)> | 是 | 回调函数，返回国家码信息。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.getCountryCode} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301500 | Failed to query the area information. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';

3. try {
4. geoLocationManager.getCountryCode((err, result) => {
5. if (err) {
6. console.error('getCountryCode: err=' + JSON.stringify(err));
7. }
8. if (result) {
9. console.info('getCountryCode: result=' + JSON.stringify(result));
10. }
11. });
12. } catch (err) {
13. console.error("errCode:" + err.code + ", message:" + err.message);
14. }
```

## geoLocationManager.getCountryCode

PhonePC/2in1TabletTVWearable

getCountryCode(): Promise<CountryCode>

查询当前的国家码。使用Promise异步回调。

**系统能力**：SystemCapability.Location.Location.Core

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[CountryCode](js-apis-geolocationmanager.md#countrycode)> | Promise对象，返回国家码信息。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call ${geoLocationManager.getCountryCode} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301500 | Failed to query the area information. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. geoLocationManager.getCountryCode()
6. .then((result) => {
7. console.info('promise, getCountryCode: result=' + JSON.stringify(result));
8. })
9. .catch((error: BusinessError) => {
10. console.error('promise, getCountryCode: error=' + JSON.stringify(error));
11. });
12. } catch (err) {
13. console.error("errCode:" + err.code + ", message:" + err.message);
14. }
```

## geoLocationManager.addGnssGeofence12+

PhoneTablet

addGnssGeofence(fenceRequest: GnssGeofenceRequest): Promise<number>

添加一个GNSS地理围栏，并订阅地理围栏事件。使用Promise异步回调。

APP可以在入参[GnssGeofenceRequest](js-apis-geolocationmanager.md#gnssgeofencerequest12)中传入回调函数用于接收地理围栏事件；也可以传入通知对象[NotificationRequest](js-apis-notification.md#notificationrequest)，在系统识别到地理围栏事件发生时会弹出APP创建的通知。

GNSS地理围栏功能依赖GNSS定位芯片（仅部分型号支持），如果设备无此芯片或使用的芯片型号不支持该功能，则返回错误码801（Capability not supported）。

**需要权限**：ohos.permission.LOCATION 和 ohos.permission.APPROXIMATELY\_LOCATION

**系统能力**：SystemCapability.Location.Location.Geofence

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fenceRequest | [GnssGeofenceRequest](js-apis-geolocationmanager.md#gnssgeofencerequest12) | 是 | 添加GNSS地理围栏请求参数。  包含圆形围栏信息、需要监听的地理围栏事件、地理围栏事件触发后弹出的通知对象和监听地理围栏事件的回调函数。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回地理围栏ID。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.addGnssGeofence} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |
| 3301601 | The number of geofences exceeds the maximum. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { notificationManager } from '@kit.NotificationKit';
4. // 创建围栏
5. let geofence: geoLocationManager.Geofence = {
6. "latitude": 34.12, "longitude": 124.11, "radius": 10000.0, "expiration": 10000.0
7. }
8. // 指定APP需要监听的地理围栏事件类型，这里表示需要监听进入围栏和退出围栏事件
9. let transitionStatusList: Array<geoLocationManager.GeofenceTransitionEvent> = [
10. geoLocationManager.GeofenceTransitionEvent.GEOFENCE_TRANSITION_EVENT_ENTER,
11. geoLocationManager.GeofenceTransitionEvent.GEOFENCE_TRANSITION_EVENT_EXIT,
12. ];
13. // 创建GEOFENCE_TRANSITION_EVENT_ENTER事件对应的通知对象
14. let notificationRequest1: notificationManager.NotificationRequest = {
15. id: 1,
16. content: {
17. notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
18. normal: {
19. title: "围栏通知",
20. text: "围栏进入",
21. additionalText: ""
22. }
23. }
24. };
25. // 创建GEOFENCE_TRANSITION_EVENT_EXIT事件对应的通知对象
26. let notificationRequest2: notificationManager.NotificationRequest = {
27. id: 2,
28. content: {
29. notificationContentType: notificationManager.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
30. normal: {
31. title: '围栏通知',
32. text: '围栏退出',
33. additionalText: ""
34. }
35. }
36. };
37. // 把创建的通知对象存入Array中，存入顺序与transitionStatusList一致
38. let notificationRequestList: Array<notificationManager.NotificationRequest> =
39. [notificationRequest1, notificationRequest2];
40. // 构造GNSS地理围栏请求对象gnssGeofenceRequest
41. let gnssGeofenceRequest: geoLocationManager.GnssGeofenceRequest = {
42. // 围栏属性，包含圆心和半径等信息
43. geofence: geofence,
44. // 指定APP需要监听的地理围栏事件类型
45. monitorTransitionEvents: transitionStatusList,
46. // 地理围栏事件对应的通知对象，该参数为可选
47. notifications: notificationRequestList,
48. // 设备驻留在地理围栏内的时间，该参数为可选
49. loiterTimeMs: 10000,
50. // 围栏回调要拉起的FenceExtensionAbility名称，该参数为可选
51. fenceExtensionAbilityName: "FenceExtensionAbility",
52. // 用于监听围栏事件的callback
53. geofenceTransitionCallback: (err: BusinessError, transition: geoLocationManager.GeofenceTransition) => {
54. if (err) {
55. console.error('geofenceTransitionCallback: err=' + JSON.stringify(err));
56. }
57. if (transition) {
58. console.info("GeofenceTransition: %{public}s", JSON.stringify(transition));
59. }
60. }
61. }
62. try {
63. // 添加围栏
64. geoLocationManager.addGnssGeofence(gnssGeofenceRequest).then((id) => {
65. // 围栏添加成功后返回围栏ID
66. console.info("addGnssGeofence success, fence id: " + id);
67. let fenceId = id;
68. }).catch((err: BusinessError) => {
69. console.error("addGnssGeofence failed, promise errCode:" + (err as BusinessError).code +
70. ",errMessage:" + (err as BusinessError).message);
71. });
72. } catch (error) {
73. console.error("addGnssGeofence failed, err:" + JSON.stringify(error));
74. }
```

## geoLocationManager.removeGnssGeofence12+

PhoneTablet

removeGnssGeofence(geofenceId: number): Promise<void>

删除一个GNSS地理围栏，并取消订阅该地理围栏事件。使用Promise异步回调。

GNSS地理围栏功能依赖GNSS定位芯片（仅部分型号支持），如果设备无此芯片或使用的芯片型号不支持该功能，则返回错误码801（Capability not supported）。

**需要权限**：ohos.permission.LOCATION 和 ohos.permission.APPROXIMATELY\_LOCATION

**系统能力**：SystemCapability.Location.Location.Geofence

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| geofenceId | number | 是 | GNSS地理围栏的ID。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.removeGnssGeofence} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301602 | Failed to delete a geofence due to an incorrect ID. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. // fenceId是在geoLocationManager.addGnssGeofence执行成功后获取的
4. let fenceId = 1;
5. try {
6. geoLocationManager.removeGnssGeofence(fenceId).then(() => {
7. console.info("removeGnssGeofence success fenceId:" + fenceId);
8. }).catch((error: BusinessError) => {
9. console.error("removeGnssGeofence: error=" + JSON.stringify(error));
10. });
11. } catch (error) {
12. console.error("removeGnssGeofence: error=" + JSON.stringify(error));
13. }
```

## geoLocationManager.getGeofenceSupportedCoordTypes12+

PhoneTablet

getGeofenceSupportedCoordTypes(): Array<CoordinateSystemType>

获取地理围栏功能支持的坐标系列表。

**系统能力**：SystemCapability.Location.Location.Geofence

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Array<[CoordinateSystemType](js-apis-geolocationmanager.md#coordinatesystemtype12)> | 地理围栏功能支持的坐标系列表。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call ${geoLocationManager.getGeofenceSupportedCoordTypes} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';

3. try {
4. let supportedCoordTypes: Array<geoLocationManager.CoordinateSystemType> = geoLocationManager.getGeofenceSupportedCoordTypes();
5. console.info("getGeofenceSupportedCoordTypes return:" + JSON.stringify(supportedCoordTypes));
6. } catch (error) {
7. console.error("getGeofenceSupportedCoordTypes: error=" + JSON.stringify(error));
8. }
```

## geoLocationManager.getCurrentWifiBssidForLocating14+

PhonePC/2in1TabletTVWearable

getCurrentWifiBssidForLocating(): string

获取连接的Wi-Fi AP（Access Point）的Bssid（Basic Service Set Identifier）信息。如果当前设备未连接Wi-Fi，调用该接口将抛出错误码3301900。建议参考示例代码，通过try-catch结构捕获异常。

**需要权限**：ohos.permission.LOCATION 和 ohos.permission.APPROXIMATELY\_LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**返回值**：

| 类型 | 说明 |
| --- | --- |
| string | Wi-Fi Bssid |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.getCurrentWifiBssidForLocating()} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |
| 3301900 | Failed to obtain the BSSID of the Wi-Fi hotspot. The Wi-Fi network is not connected. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';

3. try {
4. let bssid: string = geoLocationManager.getCurrentWifiBssidForLocating();
5. console.info("get wifi bssid:" + bssid);
6. } catch (error) {
7. console.error("getCurrentWifiBssidForLocating: errCode" + error.code + ", errMessage" + error.message);
8. }
```

## geoLocationManager.on('bluetoothScanResultChange')16+

PhonePC/2in1TabletTVWearable

on(type: 'bluetoothScanResultChange', callback: Callback<BluetoothScanResult>): void

订阅蓝牙扫描信息上报事件，使用callback异步回调。

本API需要开发者向[locationkit@huawei.com](mailto:locationkit@huawei.com)发送邮件申请，请在邮件中写明使用该API的业务场景和获取蓝牙deviceId（MAC）的真实用途，申请审批通过后会方可使用。

本API会启动蓝牙扫描，为了避免产生较多功耗，需要开发者在适当的时机调用 [geoLocationManager.off('bluetoothScanResultChange')](js-apis-geolocationmanager.md#geolocationmanageroffbluetoothscanresultchange16)接口停止蓝牙扫描。

当前仅支持扫描BLE设备。

**需要权限**：ohos.permission.APPROXIMATELY\_LOCATION 和 ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“bluetoothScanResultChange”，表示订阅蓝牙扫描信息上报事件。 |
| callback | Callback<[BluetoothScanResult](js-apis-geolocationmanager.md#bluetoothscanresult16)> | 是 | 回调函数，返回蓝牙扫描信息。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.on('bluetoothScanResultChange')} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';

4. let callback = (result: geoLocationManager.BluetoothScanResult): void => {
5. console.info('bluetoothScanResultChange: ' + JSON.stringify(result));
6. };
7. try {
8. geoLocationManager.on('bluetoothScanResultChange', callback);
9. } catch (err) {
10. console.error("errCode:" + err.code + ", message:" + err.message);
11. }
```

## geoLocationManager.off('bluetoothScanResultChange')16+

PhonePC/2in1TabletTVWearable

off(type: 'bluetoothScanResultChange', callback?: Callback<BluetoothScanResult>): void

取消订阅蓝牙扫描信息上报事件并停止蓝牙扫描。

**需要权限**：ohos.permission.APPROXIMATELY\_LOCATION 和 ohos.permission.LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置事件类型。type为“bluetoothScanResultChange”，表示停止订阅蓝牙扫描信息上报事件。 |
| callback | Callback<[BluetoothScanResult](js-apis-geolocationmanager.md#bluetoothscanresult16)> | 否 | 需要取消订阅的回调函数。该回调函数需要与on接口传入的回调函数保持一致。若无此参数，则取消当前类型的所有订阅。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.off('bluetoothScanResultChange')} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';

3. let callback = (result: geoLocationManager.BluetoothScanResult): void => {
4. console.info('bluetoothScanResultChange: ' + JSON.stringify(result));
5. };
6. try {
7. geoLocationManager.on('bluetoothScanResultChange', callback);
8. geoLocationManager.off('bluetoothScanResultChange', callback);
9. } catch (err) {
10. console.error("errCode:" + err.code + ", message:" + err.message);
11. }
```

## geoLocationManager.isPoiServiceSupported20+

PhonePC/2in1TabletTVWearable

isPoiServiceSupported(): boolean

查询系统（即软件）是否支持POI服务。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Core

**返回值**：

| 类型 | 说明 |
| --- | --- |
| boolean | true:POI服务可用。  false:POI服务不可用。 |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';

3. let poiServiceState = geoLocationManager.isPoiServiceSupported();
4. console.info("poiServiceState:" + poiServiceState);
```

## geoLocationManager.getPoiInfo20+

PhonePC/2in1TabletTVWearable

getPoiInfo(): Promise<PoiInfo>

获取当前位置附近的POI信息。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.LOCATION 和 ohos.permission.APPROXIMATELY\_LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[PoiInfo](js-apis-geolocationmanager.md#poiinfo19)> | 当前位置附近的POI信息。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.getPoiInfo} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |
| 3301100 | The location switch is off. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';

3. try {
4. if (geoLocationManager.isPoiServiceSupported()) {
5. geoLocationManager.getPoiInfo().then((poiInfo) => {
6. if (poiInfo !== undefined) {
7. console.info("get PoiInfo:" + JSON.stringify(poiInfo));
8. }
9. })
10. }
11. } catch (error) {
12. console.error("getPoiInfo errCode:" + error.code + ", errMessage:" + error.message);
13. }
```

## geoLocationManager.getDistanceBetweenLocations20+

PhonePC/2in1TabletTVWearable

getDistanceBetweenLocations(location1: Location, location2: Location): number

获取两个位置之间的直线距离。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| location1 | [Location](js-apis-geolocationmanager.md#location) | 是 | 位置1。 |
| location2 | [Location](js-apis-geolocationmanager.md#location) | 是 | 位置2。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| number | 两个位置之间的直线距离，单位为米。 |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';

3. try {
4. let location1: geoLocationManager.Location = {
5. "latitude": 30.12,
6. "longitude": 120.11,
7. "altitude": 0,
8. "accuracy": 0,
9. "speed": 0,
10. "timeStamp": 0,
11. "direction": 0,
12. "timeSinceBoot": 0,
13. "additionSize": 0
14. }
15. let location2: geoLocationManager.Location = {
16. "latitude": 30.12,
17. "longitude": 120.11,
18. "altitude": 0,
19. "accuracy": 0,
20. "speed": 0,
21. "timeStamp": 0,
22. "direction": 0,
23. "timeSinceBoot": 0,
24. "additionSize": 0
25. }
26. let distance = geoLocationManager.getDistanceBetweenLocations(location1, location2);
27. console.info("distance:" + distance);
28. } catch (error) {
29. console.error("getDistanceBetweenLocations: errCode" + error.code + ", errMessage" + error.message);
30. }
```

## geoLocationManager.addBeaconFence20+

PhoneTablet

addBeaconFence(fenceRequest: BeaconFenceRequest): Promise<number>

添加一个beacon围栏，并订阅地理围栏事件。使用Promise异步回调。

beacon围栏是指通过蓝牙beacon设备和手机应用配合，实现“虚拟围栏”的功能。当用户靠近或离开某个特定的beacon设备时，手机应用会收到通知。

应用可以在入参[BeaconFenceRequest](js-apis-geolocationmanager.md#beaconfencerequest20)中传入回调函数用于接收围栏事件；也可以传入[FenceExtensionAbility](js-apis-app-ability-fenceextensionability.md)名称，在系统识别到围栏事件发生时通知应用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.LOCATION 和 ohos.permission.APPROXIMATELY\_LOCATION

**系统能力**：SystemCapability.Location.Location.Geofence

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fenceRequest | [BeaconFenceRequest](js-apis-geolocationmanager.md#beaconfencerequest20) | 是 | 添加beacon围栏请求参数。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回beacon围栏ID。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.addBeaconFence} due to limited device capabilities. |
| 3501100 | Failed to add a beacon fence because the location switch is off. |
| 3501101 | Failed to add a beacon fence because the bluetooth switch is off. |
| 3501601 | The number of beacon fence exceeds the maximum. |
| 3501603 | Duplicate beacon fence information. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. // 以iBeacon协议为例，格式如下
6. // 01 byte    type = 0x02
7. // 01 byte    len = 0x15 = 21
8. // 16 byte    UUID
9. // 02 byte    major
10. // 02 byte    minor
11. // 01 byte    tx power
12. let manufactureDataBuffer: Uint8Array = new Uint8Array([0X02, 0X15, 0X00, 0X11, 0X22, 0X33, 0X44, 0X55,
13. 0X66, 0X77, 0X88, 0X99, 0XAA, 0XBB, 0XCC, 0XDD, 0XEE, 0XFF, 0X11, 0X22, 0X33, 0X44, 0X55]);
14. let manufactureDataMaskBuffer: Uint8Array = new Uint8Array([0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
15. 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF]);

17. let manufactureData: geoLocationManager.BeaconManufactureData = {
18. manufactureId: 0X004C,
19. manufactureData: manufactureDataBuffer.buffer,
20. manufactureDataMask: manufactureDataMaskBuffer.buffer
21. };

23. let beacon: geoLocationManager.BeaconFence = {
24. identifier: "11",
25. beaconFenceInfoType: geoLocationManager.BeaconFenceInfoType.BEACON_MANUFACTURE_DATA,
26. manufactureData: manufactureData
27. };

29. let fenceRequest: geoLocationManager.BeaconFenceRequest = {
30. beacon: beacon,
31. transitionCallback: (transition: geoLocationManager.GeofenceTransition) => {
32. if (transition) {
33. console.info("GeofenceTransition: err" + JSON.stringify(transition));
34. }
35. },
36. fenceExtensionAbilityName: "MyFenceExtensionAbility",
37. };
38. geoLocationManager.addBeaconFence(fenceRequest).then((id) => {
39. console.info("addBeaconFence success, fence id:" + id);
40. }).catch((err: BusinessError) => {
41. console.error('promise, addBeaconFence: error=' + JSON.stringify(err));
42. });
43. } catch (error) {
44. console.error("addBeaconFence: errCode" + error.code + ", errMessage" + error.message);
45. }
```

## geoLocationManager.removeBeaconFence20+

PhoneTablet

removeBeaconFence(beaconFence?: BeaconFence): Promise<void>

删除beacon围栏，并取消订阅地理围栏事件。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.LOCATION 和 ohos.permission.APPROXIMATELY\_LOCATION

**系统能力**：SystemCapability.Location.Location.Geofence

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| beaconFence | [BeaconFence](js-apis-geolocationmanager.md#beaconfence20) | 否 | 传入beaconFence参数，删除指定围栏；不传入参数，删除该应用所有围栏。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.removeBeaconFence} due to limited device capabilities. |
| 3501602 | Failed to delete the fence due to incorrect beacon fence information. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. let manufactureDataBuffer: Uint8Array = new Uint8Array([0X02, 0X15, 0X00, 0X11, 0X22, 0X33, 0X44, 0X55,
6. 0X66, 0X77, 0X88, 0X99, 0XAA, 0XBB, 0XCC, 0XDD, 0XEE, 0XFF, 0X11, 0X22, 0X33, 0X44, 0X55]);
7. let manufactureDataMaskBuffer: Uint8Array = new Uint8Array([0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF,
8. 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF, 0XFF]);

10. let manufactureData: geoLocationManager.BeaconManufactureData = {
11. manufactureId: 0X004C,
12. manufactureData: manufactureDataBuffer.buffer,
13. manufactureDataMask: manufactureDataMaskBuffer.buffer
14. };

16. let beacon: geoLocationManager.BeaconFence = {
17. identifier: "11",
18. beaconFenceInfoType: geoLocationManager.BeaconFenceInfoType.BEACON_MANUFACTURE_DATA,
19. manufactureData: manufactureData
20. };
21. geoLocationManager.removeBeaconFence(beacon).then(() => {
22. console.info("promise, removeBeaconFence success");
23. })
24. .catch((error: BusinessError) => {
25. console.error("promise, removeBeaconFence: errCode" + error.code + ", errMessage" + error.message);
26. });
27. } catch (error) {
28. console.error("removeBeaconFence: errCode" + error.code + ", errMessage" + error.message);
29. }
```

## geoLocationManager.isBeaconFenceSupported20+

PhoneTablet

isBeaconFenceSupported(): boolean;

判断当前设备是否支持beacon围栏。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Location.Location.Geofence

**返回值**：

| 类型 | 说明 |
| --- | --- |
| boolean | true：支持beacon围栏。  false：不支持beacon围栏。 |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';

3. try {
4. let isBeaconFenceSupported = geoLocationManager.isBeaconFenceSupported();
5. } catch (err) {
6. console.error("errCode:" + err.code + ", message:" + err.message);
7. }
```

## geoLocationManager.isWlanBssidMatched21+

PhonePC/2in1TabletTVWearable

isWlanBssidMatched(wlanBssidArray: Array<string>, rssiThreshold: number, needStartScan: boolean): Promise<boolean>

判断指定的BSSID是否存在于最新的WLAN扫描结果里。使用Promise异步回调。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.LOCATION 和 ohos.permission.APPROXIMATELY\_LOCATION

**系统能力**：SystemCapability.Location.Location.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wlanBssidArray | Array<string> | 是 | 请求匹配的BSSID列表。单个字符串的长度不超过64，数组的长度不超过1000。 |
| rssiThreshold | number | 是 | RSSI阈值。只匹配RSSI大于此阈值的BSSID，取值范围为-10000至10000（单位：dBm）。 |
| needStartScan | boolean | 是 | 是否需要发起WLAN扫描。需要发起WLAN扫描设置为true。不需要发起WLAN扫描，使用最近一次WLAN扫描结果进行匹配设置为false。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | 表示匹配是否成功。当扫描结果中存在wlanBssidArray中的任意BSSID，且其RSSI值高于rssiThreshold时，返回true，否则返回false。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.isWlanBssidMatched} due to limited device capabilities. |
| 3301100 | The location switch is off. |
| 3301800 | Failed to start WiFi scanning. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';

3. try {
4. let wlanBssidArray: Array<string> = ["02:1b:32:23:ea:91", "02:1b:32:23:ea:93"];
5. let rssiThreshold: number = -70;
6. let needStartScan: boolean = true;
7. geoLocationManager.isWlanBssidMatched(wlanBssidArray, rssiThreshold, needStartScan).then((res) => {
8. console.info("Wlan Bssid Matched Result:" + res);
9. })
10. } catch (error) {
11. console.error("isWlanBssidMatched: errCode" + error.code + ", errMessage" + error.message);
12. }
```

## geoLocationManager.getActiveGeoFences23+

PhoneTablet

getActiveGeoFences(): Promise<Map<number, Geofence>>

查询当前有效的围栏信息。使用Promise异步回调。

**需要权限**：ohos.permission.LOCATION 和 ohos.permission.APPROXIMATELY\_LOCATION

**系统能力**：SystemCapability.Location.Location.Geofence

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Map<number, [Geofence](js-apis-geolocationmanager.md#geofence)>> | Promise对象，返回有效的围栏信息。Map中的key值为fenceId，value值为对应围栏的具体信息。 |

**错误码**：

以下错误码的详细介绍请参见[位置服务错误码](errorcode-geolocationmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. Failed to call ${geoLocationManager.getActiveGeoFences} due to limited device capabilities. |

**示例**

```
1. import { geoLocationManager } from '@kit.LocationKit';

3. try {
4. geoLocationManager.getActiveGeoFences().then((res) => {
5. if (res) {
6. console.info("fence num:" + res.size);
7. for (const item of res) {
8. console.info("data=" + JSON.stringify(item));
9. }
10. }
11. })
12. .catch((error: BusinessError) => {
13. console.error('promise, getActiveGeoFences: error=' + JSON.stringify(error));
14. });
15. } catch (error) {
16. console.error("getActiveGeoFences: errCode" + error.code + ", errMessage" + error.message);
17. }
```
