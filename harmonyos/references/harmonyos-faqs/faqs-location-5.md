---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-location-5
title: 无法获取设备当前定位信息
breadcrumb: FAQ > 应用服务开发 > 位置服务（Location Kit） > 无法获取设备当前定位信息
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:27+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:746c5e403cb75691698b7a3deab9f446fd630da64f973a244f3a215e2be2a409
---

## 问题现象

用户打开应用进入相关位置信息显示的页面，无法通过执行相关操作获取当前位置信息。包括但不限于：

* 显示未获取定位权限。
* 获取定位信息失败或超时。

## 背景知识

* [Location Kit（位置服务）](../harmonyos-guides/location-kit-intro.md)：位置子系统使用多种定位技术提供服务，如**GNSS定位**、**基站定位**、**WLAN/蓝牙定位**（基站定位、WLAN/蓝牙定位后续统称“网络定位技术”）；通过这些定位技术，无论用户设备在室内或是户外，都可以准确地确定设备位置（[Location Kit相关API](../harmonyos-references/location-arkts.md)）。
  + [约束与限制](../harmonyos-guides/location-kit-intro.md#约束与限制)：设备位置信息属于用户敏感数据，所以即使用户已经开启位置开关，应用在获取设备位置前仍需向用户申请位置访问权限。在用户确认允许后，系统才会向应用提供定位服务。
  + [申请位置权限](../harmonyos-guides/location-permission-guidelines.md)：应用可以通过[checkAccessToken](../harmonyos-references/js-apis-abilityaccessctrl.md#checkaccesstoken9)函数检查用户是否已向您的应用授予特定权限，然后使用[requestPermissionsFromUser](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)接口请求相应的权限（参考[应用权限申请](../best-practices/bpta-permission-application.md)开发实践）。系统提供的定位权限有：**ohos.permission.LOCATION**：用于获取精准位置，精准度在米级别。**ohos.permission.APPROXIMATELY\_LOCATION**：用于获取模糊位置，精确度为5公里。**ohos.permission.LOCATION\_IN\_BACKGROUND**：用于应用切换到后台仍然需要获取定位信息的场景。

    **须知** 

    使用获取设备位置功能前请在module.json5中添加位置相关权限，权限的添加方法请参考[声明权限](../harmonyos-guides/declare-permissions.md)，更多权限申请内容请参考[申请应用权限](../harmonyos-guides/request-app-permissions.md)。
  + [获取设备的位置信息](../harmonyos-guides/location-guidelines.md)：本模块能力仅支持WGS-84坐标系，因此要注意[坐标纠偏](../harmonyos-guides/map-convert-coordinate.md)。

    | 主要涉及的接口 | 功能描述 |
    | --- | --- |
    | [isLocationEnabled](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagerislocationenabled) | 判断位置服务是否已经开启。 |
    | [getCurrentLocation](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetcurrentlocation) | 获取当前位置。 |
    | [getLastLocation](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetlastlocation) | 获取最近一次定位结果。 |
    | [on('locationChange')](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanageronlocationchange) | 开启位置变化订阅，并发起定位请求。 |

    **须知** 

    如果应用在后台运行时也需要访问设备位置，除了按照上述申请权限外，还需要申请LOCATION类型的[长时任务](../harmonyos-guides/continuous-task.md)。

    | 接口 | 相关请求参数（设置优先级信息和场景） | 描述 |
    | --- | --- | --- |
    | on('locationChange') | [LocationRequest](../harmonyos-references/js-apis-geolocationmanager.md#locationrequest) | 位置信息请求参数。 |
    | on('locationChange') | [ContinuousLocationRequest](../harmonyos-references/js-apis-geolocationmanager.md#continuouslocationrequest12) | 持续定位的请求参数。 |
    | getCurrentLocation | [CurrentLocationRequest](../harmonyos-references/js-apis-geolocationmanager.md#currentlocationrequest) | 当前位置信息请求参数。 |
    | getCurrentLocation | [SingleLocationRequest](../harmonyos-references/js-apis-geolocationmanager.md#singlelocationrequest12) | 单次定位的请求参数。 |
  + [位置服务错误码](../harmonyos-references/errorcode-geolocationmanager.md)：介绍本模块特有错误码。
* [Map Kit（地图服务）](../harmonyos-guides/map-introduction.md)：为开发者提供强大而便捷的地图能力，助力全球开发者实现个性化显示地图、位置搜索和路径规划等功能，轻松完成地图构建工作。可以轻松地在HarmonyOS应用/元服务中集成地图相关的功能，全方位提升用户体验（[Map Kit相关API](../harmonyos-references/map-api.md)）。
  + [显示我的位置](../harmonyos-guides/map-location.md)：介绍如何开启和展示“我的位置”功能，“我的位置”指的是进入地图后点击“我的位置”显示当前位置点的功能。
  + [ArkTS API错误码](../harmonyos-references/errorcode-map.md)：介绍本模块特有错误码。
* [管理位置权限](../harmonyos-guides/web-geolocation-permission.md)：Web组件提供位置权限管理能力（[应用数据安全](../best-practices/bpta-app-data-security.md)），根据[GeolocationPermissions类](../harmonyos-references/arkts-apis-webview-geolocationpermissions.md)和[onGeolocationShow](../harmonyos-references/arkts-basic-components-web-events.md#ongeolocationshow)方法的响应结果，决定是否赋予前端页面权限。用户可以获取位置信息，以便使用出行导航、天气预报等服务。

## 问题定位

1. 复现问题：首次打开应用，进入相关位置信息显示的页面，期间若有位置权限获取弹窗则跳过步骤2。
2. 排查应用是否在module.json5中声明正确的位置权限（需满足实际定位需求），同时根据关键词requestPermissionsFromUser查看是否有相关申请授权位置权限设置和触发逻辑。可参考**场景一**分析。
3. 查看位置信息展示的页面属于ArkUI页面或者Web页面。
4. 对于ArkUI页面，根据【背景知识】提供的相关接口、结合场景分析位置定位的实现原理：
   * 未使用位置服务获取位置：分析位置信息获取来源，进而排查是否数据请求失败。
   * 使用位置和地图服务获取位置：
     1. 位置服务：搜索位置请求API接口，查看获取位置逻辑是否正确，如，获取当前位置[getCurrentLocation](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetcurrentlocation)，同时排查位置请求参数的优先级和场景与当前场景是否匹配。
     2. 地图服务：查看[setMyLocationControlsEnabled](../harmonyos-references/map-map-mapcomponentcontroller.md#setmylocationcontrolsenabled)设置是否启用“我的位置”按钮。如果设置[setMyLocation](../harmonyos-references/map-map-mapcomponentcontroller.md#setmylocation)，排查通过Location Kit获取用户位置后，传递Map Kit的逻辑是否完善。
5. 对于Web页面，通过调试H5页面，检查位置请求的触发逻辑。同时查看Web组件的[onGeolocationShow](../harmonyos-references/arkts-basic-components-web-events.md#ongeolocationshow)接口对网站进行位置权限管理设置是否正确。

## 分析结论

### 场景一

由于未声明或未授予定位权限导致的定位失败，包括下列三种情况：

1. 用户误操作，未开启位置服务或者拒绝了位置授权。
2. 应用未向用户申请权限，或者未申请满足相应定位场景的位置权限。
3. 位置权限授权弹窗的触发位置和逻辑设置不正确，未在首次打开应用进入需要获取位置的页面前向用户申请。

### 场景二

1. 使用[Location Kit（位置服务）](../harmonyos-guides/location-kit-intro.md)获取当前定位信息，由于相关接口和请求参数设置不正确导致的定位失败。
2. 使用[Map Kit（地图服务）](../harmonyos-guides/map-introduction.md)默认的连续定位能力，未设置[setMyLocationControlsEnabled](../harmonyos-references/map-map-mapcomponentcontroller.md#setmylocationcontrolsenabled)启用“我的位置”按钮，导致点击无响应。

### 场景三

位置权限请求属于Web前端页面发起的，由于未通过[onGeolocationShow](../harmonyos-references/arkts-basic-components-web-events.md#ongeolocationshow)接口对网站进行位置权限管理（或设置不正确），并响应结果赋予前端页面权限导致的定位失败。

## 修改建议

### 场景一

1. 增加提醒机制：通过[isLocationEnabled](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagerislocationenabled)判断位置服务是否已经使能和[二次向用户申请授权](../harmonyos-guides/request-user-authorization-second.md)完成引导用户。
2. 在module.json5中声明相应定位权限，然后使用[requestPermissionsFromUser()](../harmonyos-references/js-apis-abilityaccessctrl.md#requestpermissionsfromuser9)方法向用户申请授权。详情请参考[应用权限申请开发实践](../best-practices/bpta-permission-application.md)。
3. 优化位置权限授权弹窗的触发位置和逻辑设置，在需要获取位置前完成申请。

### 场景二

1. 在确保位置权限获取的前提下，根据实际业务场景配置位置请求参数，获取设备的位置信息。详情参考[开发步骤](../harmonyos-guides/location-guidelines.md#开发步骤)。
2. 初始化地图并获取[MapComponentController](../harmonyos-references/map-map-mapcomponentcontroller.md)地图操作类对象。调用mapController对象的[setMyLocationControlsEnabled](../harmonyos-references/map-map-mapcomponentcontroller.md#setmylocationcontrolsenabled)方法启用“我的位置”功能，详情参考[开发步骤](../harmonyos-guides/location-guidelines.md#开发步骤)。

### 场景三

参考[申请位置权限](../harmonyos-guides/web-geolocation-permission.md#申请位置权限)，实现用户点击前端页面"获取位置"按钮，Web组件通过弹窗通知应用侧位置权限请求消息。

## 常见FAQ

Q：3301200定位失败，未获取到定位结果，错误信息：Failed to obtain the geographical location.

A：请参考错误码[3301200](../harmonyos-references/errorcode-geolocationmanager.md#section3301200-定位失败未获取到定位结果)的可能原因和解决方案。

Q：位置请求参数中maxAccuracy如何设置？

A：maxAccuracy是应用向系统请求位置信息时要求的精度值，当位置信息[Location](../harmonyos-references/js-apis-geolocationmanager.md#location)中的精度值（accuracy）小于等于maxAccuracy时，位置信息会返回给应用；否则系统将丢弃本次收到的位置信息。详情参考[LocationRequest](../harmonyos-references/js-apis-geolocationmanager.md#locationrequest)中对maxAccuracy的描述。

Q：在室内等特殊场地时，在持续定位场景中设置[LocationRequest](../harmonyos-references/js-apis-geolocationmanager.md#locationrequest)的timeInterval为1，为何不生效？

A：在室内因为没有GNSS信号，返回的是网络位置。因为WLAN扫描有较大的功耗，系统限制20秒扫描一次，因此在室内即使timeInterval设置为1，也只能20秒获取到一次位置。

Q：系统缓存位置信息不准确，使用getCurrentLocation()接口获取当前定位信息后，再使用getLastLocation()接口获取缓存定位信息，两次获取的定位信息不一致。

A：所有应用共用系统中的同一份缓存定位信息，有可能在两次接口调用之间有其他应用发起定位，刷新了系统中的缓存定位信息。可以对比获取定位信息的时间，根据时间判断缓存定位信息是否更新。

Q：开启飞行模式，是否可以获取设备当前定位信息？

A：开启飞行模式或者无网络场景下，会使用GPS进行定位，室内可能无GPS信息，需要空旷无遮挡的室外环境。

Q：位置定位中，如何获取当前定位的城市？

A：导入geoLocationManager模块，先调用[isGeoServiceAvailable](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagerisgeocoderavailable)查询正地理编码与逆地理编码服务是否可用，确认服务可用后调用逆地理编码服务接口[getAddressesFromLocation](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetaddressesfromlocation)把经纬度坐标转化为地理位置信息，从回调中获得与此坐标匹配的[GeoAddress](../harmonyos-references/js-apis-geolocationmanager.md#geoaddress)（地理编码地址信息）列表，其中locality表示城市信息。
