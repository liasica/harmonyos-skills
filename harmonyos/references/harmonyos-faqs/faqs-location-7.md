---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-location-7
title: 获取当前设备位置信息不准确
breadcrumb: FAQ > 应用服务开发 > 位置服务（Location Kit） > 获取当前设备位置信息不准确
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8bbc6c836ba73e1d07e9c682696198f9ff0846ea2b0870495b3140f6bef46307
---

## 问题现象

使用Location Kit位置服务获取当前设备位置时，返回的位置与实际位置有误差。

## 背景知识

[Location Kit（位置服务）](../harmonyos-guides/location-kit-intro.md)：位置子系统使用多种定位技术提供服务，如GNSS定位、基站定位、WLAN/蓝牙定位（基站定位和WLAN/蓝牙定位后续统称为“网络定位技术”）；通过这些定位技术，无论用户设备在室内或是户外，都可以准确地确定设备位置。

1. [申请位置权限](../harmonyos-guides/location-permission-guidelines.md)：应用可以通过[checkAccessToken](../harmonyos-references/js-apis-abilityaccessctrl.md#checkaccesstoken9)接口检查用户是否已向您的应用授予特定权限，然后使用[requestPermissionsFromUser](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)接口请求相应的权限（参考[应用权限申请开发实践](../best-practices/bpta-permission-application.md)）。系统提供的定位权限有：

   ohos.permission.LOCATION：用于获取精准位置，精准度在米级别。

   ohos.permission.APPROXIMATELY\_LOCATION：用于获取模糊位置，精确度为5公里。

   ohos.permission.LOCATION\_IN\_BACKGROUND：用于应用切换到后台仍然需要获取定位信息的场景。

   **须知** 

   使用获取设备位置功能前请在module.json5中添加位置相关权限，权限的添加方法请参考[声明权限](../harmonyos-guides/declare-permissions.md)，更多权限申请内容请参考[申请应用权限](../harmonyos-guides/request-app-permissions.md)。
2. [获取设备的位置信息](../harmonyos-guides/location-guidelines.md)：本模块能力仅支持WGS84坐标系，需注意[坐标纠偏](../harmonyos-guides/map-convert-coordinate.md)。

## 问题定位

1. 检查module.json5配置文件的requestPermissions标签中是否声明了ohos.permission.LOCATION权限。同时，检查是否通过requestPermissionsFromUser接口请求ohos.permission.LOCATION精准位置权限。
2. 检查代码中获取定位信息的API接口，位置请求参数的定位策略设置是否以精度优先。以单次定位的请求参数（[SingleLocationRequest](../harmonyos-references/js-apis-geolocationmanager.md#singlelocationrequest12)）为例，检查locatingPriority是否设置为PRIORITY\_ACCURACY。
3. 确定设备定位的环境是否为空旷的室外。室内环境和有高大建筑遮挡时，无GPS信号，此时位置服务会使用网络定位，网络定位的精度相对较低。

## 分析结论

* **场景一**：

  定位权限设置错误，仅声明了模糊定位权限，未声明精准定位权限，或者用户误操作未授予精准定位权限。
* **场景二**：

  位置请求参数中的定位策略设置错误，主要以快速获取位置优先（蓝牙、基站、WLAN等网络定位方式）而非精度优先（GNSS卫星定位方式）。
* **场景三**：

  设备在室内进行定位或者所在位置存在高大建筑物遮挡，导致没有GPS信号，使用网络定位，位置精度不高。

## 修改建议

* **场景一**：
  1. 针对定位权限设置错误，需要申请精准定位权限ohos.permission.LOCATION，并在应用中授权获取精准位置。详情请参考[申请位置权限开发指导](../harmonyos-guides/location-permission-guidelines.md)。
  2. 对于用户误操作关闭了精准定位权限，可以使用通过[checkAccessToken()](../harmonyos-references/js-apis-abilityaccessctrl.md#checkaccesstoken9)函数检查用户是否授予权限，进行友好提醒。
* **场景二**：

  针对定位策略设置错误问题，需要将定位策略设置为精度优先，优先采用GNSS卫星定位方式。

  使用[CurrentLocationRequest](../harmonyos-references/js-apis-geolocationmanager.md#currentlocationrequest)时，配置priority为geoLocationManager.LocationRequestPriority.ACCURACY；使用SingleLocationRequest时，配置locatingPriority为geoLocationManager.LocatingPriority.PRIORITY\_ACCURACY。
* **场景三**：

  此场景非问题，建议根据业务场景，适当配置CurrentLocationRequest中maxAccuracy的值，当返回位置的精度大于maxAccuracy值时，则认为位置不准确，不返回位置。
