---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-location-23
title: 获取当前海拔高度信息失败
breadcrumb: FAQ > 应用服务开发 > 位置服务（Location Kit） > 获取当前海拔高度信息失败
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:28+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:9cfc431754c6725c32c1ce0835723eb8a6dfe6950deb3575e2a13d295c05f92b
---

## 问题现象

打开应用进入相关海拔信息显示的页面，无法获取相应的海拔高度信息（或者海拔高度信息与实际高度不符）。

## 背景知识

* [Location Kit（位置服务）](../harmonyos-guides/location-kit-intro.md)：位置子系统使用多种定位技术提供服务，如**GNSS定位**、**基站定位**、**WLAN/蓝牙定位**（基站定位、WLAN/蓝牙定位后续统称“网络定位技术”）；通过这些定位技术，无论用户设备在室内或是户外，都可以准确地确定设备位置（[Location Kit相关API](../harmonyos-references/location-arkts.md)）。
  1. [获取设备的位置信息](../harmonyos-guides/location-guidelines.md)：本模块能力仅支持WGS-84坐标系，因此要注意[坐标纠偏](../harmonyos-guides/map-convert-coordinate.md)。
  2. [Location（位置信息）](../harmonyos-references/js-apis-geolocationmanager.md#location)：其中可以获取经纬度、高度和定位结果的来源（[LocationSourceType](../harmonyos-references/js-apis-geolocationmanager.md#locationsourcetype12)）等信息。
* [Map Kit（地图服务）](../harmonyos-guides/map-introduction.md)：为开发者提供强大而便捷的地图能力，助力全球开发者实现个性化显示地图、位置搜索和路径规划等功能，轻松完成地图构建工作。可以轻松地在HarmonyOS应用/元服务中集成地图相关的功能，全方位提升用户体验。

  **须知** 

  海拔高度：设置海拔高度[setAltitude](../harmonyos-references/map-map-marker.md#setaltitude)、获取海拔高度[getAltitude](../harmonyos-references/map-map-marker.md#getaltitude)，getAltitude获取的Marker点的海拔信息来自setAltitude设置的值，所以当未通过setAltitude设置海拔数据时，无法获取到Marker点的海拔信息。
* [Sensor Service Kit（传感器服务）](../harmonyos-guides/sensor-service-kit.md)：使应用程序能够从传感器获取原始数据，并提供振感控制能力。[传感器错误码](../harmonyos-references/errorcode-sensor.md)，介绍本模块特有错误码。

## 问题定位

打开应用进入海拔高度信息页面，分析海拔信息来源。主要分为位置服务、传感器服务和地图服务。

1. 海拔信息来源由位置服务提供，查看位置请求参数相关设置是否正确，主要查看[LocationRequestPriority](../harmonyos-references/js-apis-geolocationmanager.md#locationrequestpriority)优先级信息是否设置正确，也可以根据[位置服务错误码](../harmonyos-references/errorcode-geolocationmanager.md)分析。

   **须知** 

   请求参数中[LocationRequestPriority](../harmonyos-references/js-apis-geolocationmanager.md#locationrequestpriority)优先级信息设置：ACCURACY任何时候都能获取海拔高度，FIRST\_FIX在室外环境能够获取海拔信息，LOW\_POWER无法获取海拔信息。主要原因是部分场地GPS信号弱，优先级信息可以合理的协调多种定位技术。
2. 海拔信息来源由传感器服务提供，主要根据[传感器错误码](../harmonyos-references/errorcode-sensor.md)分析得出结论，同时查看getGeomagneticInfo和getDeviceAltitude接口API是否设置正确。
3. 海拔信息来源由地图服务提供，检查是否通过[setAltitude](../harmonyos-references/map-map-marker.md#setaltitude)正确设置海拔信息。

## 分析结论

* 场景一：

  应用的海拔信息由位置服务提供。由于室内没有GPS信号，同时请求参数中[LocationRequestPriority](../harmonyos-references/js-apis-geolocationmanager.md#locationrequestpriority)优先级信息等设置不对，导致获取海拔信息失败。
* 场景二：

  应用的海拔信息由传感器服务提供：

  1. 错误码14500102：设备不支持导致获取海拔信息失败，当调用GetSingleSensor接口时，若设备不支持该传感器，会报此错误码。
  2. 错误码14500101：传感器服务异常导致获取海拔信息失败，当调用Sensor模块on、once、off接口时，若hdi服务异常，会报此错误码。

* 场景三：

  应用的海拔信息由地图服务提供。由于未正确调用setAltitude设置Marker点的海拔信息，导致后续通过getAltitude获取海拔信息失败。

## 修改建议

* 场景一

  [LocationRequestPriority](../harmonyos-references/js-apis-geolocationmanager.md#locationrequestpriority)设置为ACCURACY任何时候都能获取海拔高度，FIRST\_FIX在室外环境能够获取海拔信息，LOW\_POWER无法获取海拔信息。根据实际业务需求，动态调整优先级设置，以平衡准确性、速度和功耗，在无法获取海拔信息时（如室内），提供友好的提示，帮助用户理解当前情况。
* 场景二：
  1. 增加合理提示，或者在无法通过传感器获取海拔信息时，尽量提供替代方案，例如使用[Location Kit（位置服务）](../harmonyos-guides/location-kit-intro.md)获取。
  2. 增设定时重试操作，如间隔1s或者按照指数增长间隔重试。连续重试3次不可用则停止尝试，期间可优先尝试获取器件列表方式进一步获取设备可用性。

* 场景三：

  在调用getAltitude获取Marker点的海拔信息前，确保已通过setAltitude传入正确的海拔值。

## 常见FAQ

Q：位置服务获取的海拔高度误差较大。

A：海拔高度信息由GPS获取，当设备所在环境存在遮挡和反射时，如周边有高楼或者高架时，获取的海拔高度信息可能误差稍大，请移至空旷的室外环境下验证。
