---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-location-11
title: 持续定位首次定位之后间隔很久才开始二次定位
breadcrumb: FAQ > 应用服务开发 > 位置服务（Location Kit） > 持续定位首次定位之后间隔很久才开始二次定位
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0059207918f4b97f3e4278520bcc4bc62bdcefd2b4377a5594432307ef0806f3
---

## 问题现象

位置信息请求参数[LocationRequest](../harmonyos-references/js-apis-geolocationmanager.md#locationrequest)指定优先级类型priority为LocationRequestPriority.ACCURACY，scenario取值UNSET，使priority参数生效，设置上报位置信息的时间间隔为1秒。

传入位置请求参数，调用[geoLocationManager.on('locationChange')](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanageronlocationchange)开启位置变化订阅，并在回调函数中打印定位信息，查看打印内容，发现首次定位后间隔20秒左右才打印二次定位信息，没有按照设置1秒间隔进行打印，之后信息打印正常。

问题代码示例参考如下：

```ts
let requestInfo: geoLocationManager.LocationRequest = {
  'priority': geoLocationManager.LocationRequestPriority.ACCURACY, // 精度优先
  'scenario': geoLocationManager.LocationRequestScenario.UNSET,
  'timeInterval': options.intervalTime || 1,
  'distanceInterval': options.spacing || 0,
  'maxAccuracy': 0
}

geoLocationManager.on('locationChange', requestInfo, (location) => {
  locationChange(location) // 处理location数据
  console.warn(`pcb callback ${JSON.stringify(location)}`)
});
```

## 解决方案

位置请求中位置信息优先级类型(LocationRequestPriority)为精度优先(ACCURACY)，该定位精度优先策略主要以GNSS定位技术为主，但是在GNSS提供稳定位置结果之前会使用网络定位技术提供服务。

这两种定位模式允许的最小时间间隔不同，GNSS定位时为1秒，网络定位时为20秒，当设置值小于最小间隔时，以最小时间间隔生效；所以导致初始时使用的是网络定位时间间隔大概是20秒，在GNSS提供稳定位置结果后时间间隔大概是1秒。在持续定位过程中，如果超过30秒无法获取GNSS定位结果则使用网络定位技术。

对设备的硬件资源消耗较大，功耗较大。

**说明** 

用户处于室内场景时，会使用网络定位技术获取位置。即使在请求参数[LocationRequest](../harmonyos-references/js-apis-geolocationmanager.md#locationrequest)或[ContinuousLocationRequest](../harmonyos-references/js-apis-geolocationmanager.md#continuouslocationrequest12)设置上报时间间隔为1秒，也会20秒上报一次。在室外GNSS定位信号稳定时，会按照指定时间间隔上报。
