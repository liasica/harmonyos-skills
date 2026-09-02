---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-location-18
title: maxAccuracy设置太小导致定位API失败
breadcrumb: FAQ > 应用服务开发 > 位置服务（Location Kit） > maxAccuracy设置太小导致定位API失败
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1a144241a6d87f5dacc9f7fc7f3e3fe731ac683356162e127b41adc103b66bba
---

## 问题现象

第一次安装应用的时候调用系统定位API失败，并且失败的时候超时时间也很长。具体错误信息如下：

```ts
{
  "code": 3301200,
  "message": "BusinessError 3301200: Failed to obtain the geographical location."
}
```

问题代码如下：

```ts
let requestInfo: geoLocationManager.CurrentLocationRequest = {
  'priority': geoLocationManager.LocationRequestPriority.FIRST_FIX,
  'maxAccuracy': 4
};
return geoLocationManager.getCurrentLocation(requestInfo)
```

## 背景知识

* [Location](../harmonyos-references/js-apis-geolocationmanager.md#location)：位置信息设置，可通过accuracy参数设置精度。
* [getCurrentLocation](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetcurrentlocation)：位置请求参数设置。可通过maxAccuracy参数指定请求位置信息时要求的精度值。
* [位置服务错误码3301200](../harmonyos-references/errorcode-geolocationmanager.md#section3301200-定位失败未获取到定位结果)：定位结果不满足精度要求导致定位超时。

## 问题定位

从问题代码可知，参数priority值为geoLocationManager.LocationRequestPriority.FIRST\_FIX，而参数maxAccuracy值为4。

根据官方文档的参数说明，系统会对比GNSS或网络定位服务上报的位置信息与应用的位置信息申请。当位置信息Location中的精度值（accuracy）小于等于应用要求的精度值（maxAccuracy）时，位置信息会返回给应用；否则系统将丢弃本次收到的位置信息。

## 分析结论

定位失败的原因主要是因为maxAccuracy设置的太小，导致定位坐标被认定为不符合要求而被忽略。

## 修改建议

根据官方参考文档中的参数说明，当priority设置为LOW\_POWER/FIRST\_FIX时，可将maxAccuracy设置大于100的值。因此这里建议将maxAccuracy的值设定为100。代码可参考[getCurrentLocation](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetcurrentlocation)接口示例代码的方式一，将其中maxAccuracy值改为100即可。
