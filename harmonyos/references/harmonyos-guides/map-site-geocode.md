---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-site-geocode
title: 地理编码
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 位置搜索 > 地理编码
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:52+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a9768145c5b92593cc7c044d9ab6ea5fcd8f173b4a721fb43c0e80a68736a618
---

## 场景介绍

提供正地理编码、逆地理编码的能力：

* 正地理编码：根据地址获取地点的经纬度。
* 逆地理编码：获取经纬度对应的地点信息。

## 接口说明

以下是地理编码相关接口，主要由[site](../harmonyos-references/map-site.md)命名空间下的方法提供，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-site.md)。

| 接口名 | 描述 |
| --- | --- |
| [geocode](../harmonyos-references/map-site.md#geocode)(geocodeParams: [GeocodeParams](../harmonyos-references/map-site.md#geocodeparams)): Promise<[GeocodeResult](../harmonyos-references/map-site.md#geocoderesult)> | 正地理编码。 |
| [geocode](../harmonyos-references/map-site.md#geocode-1)(context: [common.Context](../harmonyos-references/js-apis-inner-application-context.md), geocodeParams: [GeocodeParams](../harmonyos-references/map-site.md#geocodeparams)): Promise<[GeocodeResult](../harmonyos-references/map-site.md#geocoderesult)> | 正地理编码。支持上传Context上下文。 |
| [reverseGeocode](../harmonyos-references/map-site.md#reversegeocode)(reverseGeocodeParams: [ReverseGeocodeParams](../harmonyos-references/map-site.md#reversegeocodeparams)): Promise<[ReverseGeocodeResult](../harmonyos-references/map-site.md#reversegeocoderesult)> | 逆地理编码。 |
| [reverseGeocode](../harmonyos-references/map-site.md#reversegeocode-1)(context: [common.Context](../harmonyos-references/js-apis-inner-application-context.md), reverseGeocodeParams: [ReverseGeocodeParams](../harmonyos-references/map-site.md#reversegeocodeparams)): Promise<[ReverseGeocodeResult](../harmonyos-references/map-site.md#reversegeocoderesult)> | 逆地理编码。支持上传Context上下文。 |
| [GeocodeParams](../harmonyos-references/map-site.md#geocodeparams) | 正地理编码的参数。 |
| [GeocodeResult](../harmonyos-references/map-site.md#geocoderesult) | 正地理编码的结果。 |
| [ReverseGeocodeParams](../harmonyos-references/map-site.md#reversegeocodeparams) | 逆地理编码的参数。 |
| [ReverseGeocodeResult](../harmonyos-references/map-site.md#reversegeocoderesult) | 逆地理编码的结果。 |

## 开发步骤

导入相关模块。

```
1. import { site } from '@kit.MapKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
```

### 正地理编码

说明

根据地址获取地点的空间坐标，如经纬度，最多返回10条记录。

```
1. let params: site.GeocodeParams = {
2. // 地址信息
3. query: 'Piazzale Dante, 41, 55049 Viareggio',
4. language: 'en'
5. };
6. try {
7. // 调用正地理编码接口进行地址查询
8. const result = await site.geocode(params);
9. console.info(`Succeeded in geocoding. result is ${JSON.stringify(result)}`);
10. } catch (error) {
11. const err: BusinessError = error as BusinessError;
12. console.error(`Failed in geocoding. Code is ${err.code}, message is ${err.message}`);
13. }
```

### 逆地理编码

```
1. let params: site.ReverseGeocodeParams = {
2. // 位置经纬度
3. location: {
4. latitude: 31.984410259206815,
5. longitude: 118.76625379397866
6. },
7. language: "en",
8. radius: 0,
9. isExtension: true,
10. isNearbyAoi: true
11. };
12. try {
13. // 调用逆地理编码接口进行坐标地址查询
14. const result = await site.reverseGeocode(params);
15. console.info(`Succeeded in reversing. result is ${JSON.stringify(result)}`);
16. } catch (error) {
17. const err: BusinessError = error as BusinessError;
18. console.error(`Failed in reversing. Code is ${err.code}, message is ${err.message}`);
19. }
```
