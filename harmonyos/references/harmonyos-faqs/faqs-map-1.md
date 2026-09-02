---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-map-1
title: 定位结果在地图上显示时存在偏差
breadcrumb: FAQ > 应用服务开发 > 地图服务（Map Kit） > 定位结果在地图上显示时存在偏差
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:47+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:a3a184aedea187021a582a2aff04b068b08a89511d8f923f1bfee25c466f0dc4
---

## 问题现象

应用在使用Map Kit地图服务时，地图上显示的位置标记点与实际地理位置存在偏差。

## 背景知识

* 华为地图涉及2种坐标系：
  1. WGS84：一种大地坐标系，也是目前广泛使用的GPS全球卫星定位系统使用的坐标系。
  2. GCJ02：由中国国家测绘局制订的地理信息系统的坐标系统，是由WGS84坐标系经过加密后的坐标系。
* 华为地图在中国大陆、中国香港和中国澳门使用GCJ02坐标系，中国台湾和海外使用WGS84坐标系，若使用WGS84坐标系直接叠加在华为地图上，因坐标值不同，展示位置会有偏移。所以，在中国大陆如果使用WGS84坐标调用Map Kit服务，需要先将其转换为GCJ02坐标系再访问，参考：[坐标纠偏](../harmonyos-guides/map-convert-coordinate.md#坐标纠偏-1)。
* [ohos.permission.LOCATION](../harmonyos-guides/permissions-for-all-user.md#ohospermissionlocation)：精准定位权限，允许应用获取设备位置信息。
* [LocatingPriority](../harmonyos-references/js-apis-geolocationmanager.md#locatingpriority12)：位置请求中的优先级类型，PRIORITY\_ACCURACY表示精度优先，PRIORITY\_LOCATING\_SPEED表示速度优先。

## 问题定位

1. 是否坐标来源是位置服务的[getCurrentLocation](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetcurrentlocation)或[geoLocationManager.on('locationChange')](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanageronlocationchange)接口，位置服务获取的坐标为WGS84坐标系，需要转换为GCJ02坐标系。
2. 如果使用位置服务获取的坐标已经转换为GCJ02坐标，显示的位置仍不准确，可能是位置服务获取的位置不准确，需排查定位权限和定位策略是否配置正确，参见[获取当前设备位置信息不准确](faqs-location-7.md)。
3. 如果传入Map Kit的坐标不是WGS84坐标，需确定坐标来源和坐标系，使用相应的算法转换为GCJ02坐标后，在Map Kit中使用。

## 分析结论

传入的坐标非GCJ02坐标系；未申请精准定位权限ohos.permission.LOCATION；未配置定位策略为精度优先。

## 修改建议

1. 将位置服务获取的WGS84坐标转换为GCJ02坐标，再传入地图，参见坐标纠偏。
2. 申请精准定位权限ohos.permission.LOCATION，配置定位策略为精度优先（LocatingPriority配置为PRIORITY\_ACCURACY），具体操作参见获取当前设备位置信息不准确。

## 常见FAQ

Q：除了[convertCoordinate](../harmonyos-references/map-map-functions.md#convertcoordinate)方法可以转换坐标，还有什么方式可以把WGS84坐标系转为GCJ02坐标系？

A：使用[rectifyCoordinate](../harmonyos-references/map-map-functions.md#rectifycoordinate)接口可以解决原始坐标与华为地图展示偏转的问题，且仅支持WGS84坐标系转为GCJ02坐标系。

Q：convertCoordinateSync和rectifyCoordinate两种坐标纠偏接口有什么差异？

A：[convertCoordinateSync](../harmonyos-references/map-map-functions.md#convertcoordinatesync)接口仅固定的将输入坐标数据进行WGS84坐标系转GCJ02坐标系。rectifyCoordinate接口会判断输入坐标数据信息，自动决定是否进行坐标系转换纠偏，如应用涉及海外使用地图场景，建议使用该接口。
