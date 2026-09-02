---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-location-6
title: 自动获取定位信息失败
breadcrumb: FAQ > 应用服务开发 > 位置服务（Location Kit） > 自动获取定位信息失败
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2da58c4aed1f28adb9f23ad075da40c3b189bf4eb3a741f666942fbaca26f94c
---

## 问题现象

打开应用进入相关位置信息显示的页面，没有实现自动定位，包括但不限于：

1. 显示的位置信息并非当前位置，需要用户手动点击或选择来获取。
2. 持续定位的场景未达到预期效果。

## 背景知识

[Location Kit（位置服务）](../harmonyos-guides/location-kit-intro.md)：位置子系统使用多种定位技术提供服务，如**GNSS定位**、**基站定位**、**WLAN/蓝牙定位**（基站定位、WLAN/蓝牙定位后续统称“网络定位技术”）；通过这些定位技术，无论用户设备在室内或户外，都可以准确地确定设备位置（[Location Kit相关API](../harmonyos-references/location-arkts.md)）。

1. [获取设备的位置信息](../harmonyos-guides/location-guidelines.md)：本模块能力仅支持WGS-84坐标系，因此要注意[坐标纠偏](../harmonyos-guides/map-convert-coordinate.md)。

   | 主要涉及的接口 | 功能描述 |
   | --- | --- |
   | [getCurrentLocation()](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetcurrentlocation) | 获取当前位置。 |
   | [getLastLocation()](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetlastlocation) | 获取最近一次定位结果。 |
   | [on('locationChange')](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanageronlocationchange) | 开启位置变化订阅，并发起定位请求。 |
   | [off('locationChange')](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagerofflocationchange) | 关闭位置变化订阅，并删除对应的定位请求。 |

   **须知** 

   如果应用在后台运行时也需要访问设备位置，除了申请权限外，还需要申请LOCATION类型的[长时任务](../harmonyos-guides/continuous-task.md)。

   | 接口 | 相关请求参数（设置优先级信息和场景） | 描述 |
   | --- | --- | --- |
   | on('locationChange') | [LocationRequest](../harmonyos-references/js-apis-geolocationmanager.md#locationrequest) | 位置信息请求参数。 |
   | on('locationChange') | [ContinuousLocationRequest](../harmonyos-references/js-apis-geolocationmanager.md#continuouslocationrequest12) | 持续定位的请求参数。 |
   | getCurrentLocation() | [CurrentLocationRequest](../harmonyos-references/js-apis-geolocationmanager.md#currentlocationrequest) | 当前位置信息请求参数。 |
   | getCurrentLocation() | [SingleLocationRequest](../harmonyos-references/js-apis-geolocationmanager.md#singlelocationrequest12) | 单次定位的请求参数。 |
2. [Location](../harmonyos-references/js-apis-geolocationmanager.md#location)（位置信息）：其中可以定位结果的来源（[LocationSourceType](../harmonyos-references/js-apis-geolocationmanager.md#locationsourcetype12)）等信息。
3. [on('locationError')](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanageronlocationerror12)：订阅持续定位过程中的错误码。
4. [位置服务错误码](../harmonyos-references/errorcode-geolocationmanager.md)：介绍本模块特有错误码。

## 问题定位

根据背景知识提供的相关API接口，结合具体位置获取场景（单次定位/持续定位）分析位置定位的实现原理，继而分析故障原因：

1. 未使用位置服务获取位置：查看位置信息获取来源，如果是预设数据，检查是否对用户选择的地址做[应用数据持久化](../harmonyos-guides/app-data-persistence.md)处理，避免重启应用位置刷新。
2. 使用位置服务获取位置：
   * 单次定位：可以查看调用getCurrentLocation()接口获取当前位置信息的逻辑，检查是否在页面生命周期的适当时机自动获取。
   * 持续定位：位置请求参数的interval/timeInterval、priority和scenario等字段是否设置正确。

     **须知** 

     对于后台运行需要持续定位的场景，检查是否申请长时任务。

## 分析结论

### 场景一

无法自动定位，每次只能手动点击或选择获取的原因有以下两种情况：

1. 位置信息获取来源是预设数据，未对用户选择的地址做[应用数据持久化](../harmonyos-guides/app-data-persistence.md)。
2. 应用获取位置信息动作和点击事件绑定，并非在页面显示时自动触发。

### 场景二

持续定位的场景未达到预期效果，有以下两种情况：

1. 对于需要后台运行时也访问设备位置的场景，未申请长时任务导致自动定位失败。
2. 对于需要持续定位的场景未使用位置变化订阅并发起定位请求，或者设置的请求参数（如上报位置信息的时间间隔interval等）不合理导致。

## 修改建议

### 场景一

1. 对于非必要位置服务获取位置的场景（如只需用户选择对应市区获取对应场地服务），建议完成一次地址选择后做持久化处理，实现方式参考[通过用户首选项实现数据持久化](../harmonyos-guides/data-persistence-by-preferences.md)。
2. 修改位置信息获取的逻辑。在进入页面时，通过[UIAbility组件生命周期](../harmonyos-guides/uiability-lifecycle.md)主动获取，优化用户体验。

### 场景二

1. 应用在后台运行时也需要访问设备位置，需要申请LOCATION类型的[长时任务](../harmonyos-guides/continuous-task.md)。
2. 对于持续定位场景（多用于导航、运动轨迹、出行等）开启位置变化订阅并设置合理的请求参数。首先实例化[ContinuousLocationRequest](../harmonyos-references/js-apis-geolocationmanager.md#continuouslocationrequest12)对象，用于告知系统该向应用提供何种类型的位置服务，以及位置结果上报的频率。
   * 设置locationScenario（定位的场景信息）：建议locationScenario参数优先根据应用的使用场景进行设置，该参数枚举值定义参见[UserActivityScenario](../harmonyos-references/js-apis-geolocationmanager.md#useractivityscenario12)。
   * 设置interval：表示上报位置信息的时间间隔，单位是秒，默认值为1秒。如果对位置上报时间间隔无特殊要求，可以不填写该字段。

   调用[on('locationChange')](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanageronlocationchange)开启位置变化订阅，并发起定位请求。最后在不需要获取定位信息时及时结束定位。详情参考[开发步骤](../harmonyos-guides/location-guidelines.md#开发步骤)。
