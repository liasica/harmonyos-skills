---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/geocode-guidelines
title: 正地理编码与逆地理编码开发指导
breadcrumb: 指南 > 应用服务 > Location Kit（位置服务） > 正地理编码与逆地理编码开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d3b3ec4f72c5f161a10539dc1eca6922cc3919a4b63b78b3e8f46227d7e273cb
---

## 场景概述

使用经纬度坐标描述一个位置，非常准确，但是并不直观，面向用户表达并不友好。系统向开发者提供了以下两种转化能力。

* 正地理编码：将地理编码转化为具体经纬度坐标。
* 逆地理编码：将具体的经纬度坐标转化为地理编码。

其中地理编码包含多个属性来描述位置信息，包括国家、行政区划、街道、门牌号、地址描述等等，这样的信息更便于用户理解。

## 接口说明

进行经纬度坐标和地理编码的相互转化，所使用的接口说明如下，详细信息参见Location Kit API参考：[@ohos.geoLocationManager (位置服务)](../harmonyos-references/js-apis-geolocationmanager.md)。

| 接口名 | 功能描述 |
| --- | --- |
| [isGeocoderAvailable(): boolean](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagerisgeocoderavailable) | 判断地理编码与逆地理编码服务是否可用。 |
| [getAddressesFromLocation(request: ReverseGeoCodeRequest, callback: AsyncCallback<Array<GeoAddress>>): void](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetaddressesfromlocation) | 调用逆地理编码服务，将坐标转换为地理描述，使用callback回调异步返回结果。 |
| [getAddressesFromLocationName(request: GeoCodeRequest, callback: AsyncCallback<Array<GeoAddress>>): void](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetaddressesfromlocationname) | 调用地理编码服务，将地理描述转换为具体坐标，使用callback回调异步返回结果。 |

## 开发步骤

说明

正地理编码与逆地理编码功能需要访问后端服务，请确保设备联网，以进行信息获取。

1. 导入geoLocationManager模块，所有与正地理编码和逆地理编码能力相关的功能API，都是通过该模块提供的。

   ```
   1. import { geoLocationManager } from '@kit.LocationKit';
   ```
2. 查询正地理编码与逆地理编码服务是否可用。

   * 调用isGeocoderAvailable查询正地理编码与逆地理编码服务是否可用，如果服务可用再继续进行步骤3。如果服务不可用，说明该设备不具备地理编码与逆地理编码能力，请勿使用相关接口。

     ```
     1. import { geoLocationManager } from '@kit.LocationKit';
     2. try {
     3. let isAvailable = geoLocationManager.isGeocoderAvailable();
     4. } catch (err) {
     5. console.error("errCode:" + JSON.stringify(err));
     6. }
     ```
3. 获取转化结果。

   * 调用getAddressesFromLocation，把经纬度坐标转化为地理编码（即位置信息）。应用可以获得与此坐标匹配的[GeoAddress](../harmonyos-references/js-apis-geolocationmanager.md#geoaddress)（地理编码地址信息）列表，应用可以根据实际使用需求，读取相应的参数数据。

     ```
     1. let reverseGeocodeRequest:geoLocationManager.ReverseGeoCodeRequest = {"latitude": 31.12, "longitude": 121.11, "maxItems": 1};
     2. try {
     3. geoLocationManager.getAddressesFromLocation(reverseGeocodeRequest, (err, data) => {
     4. if (err) {
     5. console.error('getAddressesFromLocation err: ' + JSON.stringify(err));
     6. } else {
     7. console.info('getAddressesFromLocation data: ' + JSON.stringify(data));
     8. }
     9. });
     10. } catch (err) {
     11. console.error("errCode:" + JSON.stringify(err));
     12. }
     ```
   * 调用getAddressesFromLocationName把地理编码（即位置信息）转化为经纬度坐标。

     ```
     1. let geocodeRequest:geoLocationManager.GeoCodeRequest = {"description": "上海市浦东新区xx路xx号", "maxItems": 1};
     2. try {
     3. geoLocationManager.getAddressesFromLocationName(geocodeRequest, (err, data) => {
     4. if (err) {
     5. console.error('getAddressesFromLocationName err: ' + JSON.stringify(err));
     6. } else {
     7. console.info('getAddressesFromLocationName data: ' + JSON.stringify(data));
     8. }
     9. });
     10. } catch (err) {
     11. console.error("errCode:" + JSON.stringify(err));
     12. }
     ```

     应用可以获得与位置信息相匹配的[GeoAddress](../harmonyos-references/js-apis-geolocationmanager.md#geoaddress)（地理编码地址信息）列表，其中包含对应的坐标数据。

     如果需要查询的位置信息可能出现多地重名的请求，可以设置[GeoCodeRequest](../harmonyos-references/js-apis-geolocationmanager.md#geocoderequest)，通过设置一个经纬度范围，以高效地获取期望的准确结果。
