---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-location-8
title: 获取当前位置信息有一定的延迟
breadcrumb: FAQ > 应用服务开发 > 位置服务（Location Kit） > 获取当前位置信息有一定的延迟
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c4de8da377b6fd1410dfc27f12144bfc612c38307a2919091534771d9e69a4f1
---

## 问题现象

在用户打开应用并进入位置信息显示页面后，当前地理位置信息未能及时呈现，需要经过一段时间的等待才能获取。期间未向用户显示任何提示信息或仅显示定位失败的提示，这可能造成用户的等待焦虑。

## 背景知识

* [Location Kit（位置服务）](../harmonyos-guides/location-kit-intro.md)：位置子系统使用多种定位技术提供服务，如**GNSS定位**、**基站定位**、**WLAN/蓝牙定位**（基站定位和WLAN/蓝牙定位后续统称“网络定位技术”）；通过这些定位技术，无论用户设备在室内或是户外，都可以准确地确定设备位置（[Location Kit相关API](../harmonyos-references/location-arkts.md)）。
* [获取设备的位置信息](../harmonyos-guides/location-guidelines.md)：本模块能力仅支持WGS-84坐标系，因此要注意[坐标转换](../harmonyos-guides/map-convert-coordinate.md)。

  | 主要涉及的接口 | 功能描述 |
  | --- | --- |
  | [getCurrentLocation()](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetcurrentlocation) | 获取当前位置。 |
  | [getLastLocation()](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetlastlocation) | 获取最近一次定位结果。 |
  | [on('locationChange')](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanageronlocationchange) | 开启位置变化订阅，并发起定位请求。 |
  | [off('locationChange')](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagerofflocationchange) | 关闭位置变化订阅，并删除对应的定位请求。 |

  **注意** 

  如果应用在后台运行时也需要访问设备位置，除了申请权限外，还需要申请LOCATION类型的[长时任务](../harmonyos-guides/continuous-task.md)。

  | 接口 | 相关请求参数（设置优先级信息和场景） | 描述 |
  | --- | --- | --- |
  | on('locationChange') | [LocationRequest](../harmonyos-references/js-apis-geolocationmanager.md#locationrequest) | 位置信息请求参数。 |
  | on('locationChange') | [ContinuousLocationRequest](../harmonyos-references/js-apis-geolocationmanager.md#continuouslocationrequest12) | 持续定位的请求参数。 |
  | getCurrentLocation() | [CurrentLocationRequest](../harmonyos-references/js-apis-geolocationmanager.md#currentlocationrequest) | 当前位置信息请求参数。 |
  | getCurrentLocation() | [SingleLocationRequest](../harmonyos-references/js-apis-geolocationmanager.md#singlelocationrequest12) | 单次定位的请求参数。 |

  + [Location（位置信息）](../harmonyos-references/js-apis-geolocationmanager.md#location)：其中可以获取经纬度、高度和定位结果的来源（[LocationSourceType](../harmonyos-references/js-apis-geolocationmanager.md#locationsourcetype12)）等信息。
  + [位置服务错误码](../harmonyos-references/errorcode-geolocationmanager.md)：介绍本模块特有错误码。

## 问题定位

打开应用进入定位信息页面，使用UI布局结合背景知识中相关API接口分析定位信息的获取逻辑。

1. 搜索getCurrentLocation，检查是否在位置信息页面展示前调用并获取位置。
2. 对于单次获取位置信息的场景，检查是否优先通过getLastLocation()获取缓存的最新位置。
3. 根据背景知识中请求参数，搜索并查看其priority（优先级信息）和scenario（场景信息）设置是否合理，符合当前场景需求。
4. 对于需要后台运行时也访问设备位置的场景（持续定位），查看module.json5配置文件中是否有ohos.permission.KEEP\_BACKGROUND\_RUNNING的权限声明，并搜索startBackgroundRunning和stopBackgroundRunning，检查申请和取消长时任务的逻辑是否完善。

## 分析结论

### 场景一

使用[getCurrentLocation()](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetcurrentlocation)接口是异步获取当前定位，同时定位服务（GNSS定位、基站定位、WLAN/蓝牙定位）需要时间来获取位置，可能由于场地、网络等原因导致定位信息获取延迟，影响用户体验。

### 场景二

对于单次获取位置信息的场景，未优先通过[getLastLocation()](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetlastlocation)获取缓存的最新位置。

### 场景三

对于当前定位场景选用了不合理的请求参数，比如priority优先级信息和scenario场景信息设置不正确。

### 场景四

对于需要后台运行时也访问设备位置的场景，未申请长时任务导致每次打开应用需要重新获取位置。

## 修改建议

### 场景一

优化定位信息获取逻辑：

1. 进入页面前获取定位。
2. 进入页面加载（或获取定位）时显示“加载中”（或“定位中”）提示。

### 场景二

单次定位场景，优先使用[getLastLocation()](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetlastlocation)接口获取系统缓存的最新位置，可以减少系统功耗（如果系统当前没有缓存位置会返回错误码）。

**注意** 

如果对位置的新鲜度比较敏感，可以先获取缓存位置，将位置中的时间戳与当前时间对比，若新鲜度不满足预期可以使用[getCurrentLocation()](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetcurrentlocation)再去获取。

### 场景三

优化定位请求参数，根据[LocationRequestScenario](../harmonyos-references/js-apis-geolocationmanager.md#locationrequestscenario)位置请求中定位场景类型和[LocationRequestPriority](../harmonyos-references/js-apis-geolocationmanager.md#locationrequestpriority)位置请求中位置信息优先级类型介绍，采用合理的定位策略优化用户体验。

### 场景四

应用在后台运行时也需要访问设备位置，需要申请LOCATION类型的[长时任务](../harmonyos-guides/continuous-task.md)。
