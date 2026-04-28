---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-site
title: site（地点搜索）
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > site（地点搜索）
category: harmonyos-references
scraped_at: 2026-04-28T08:17:27+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:e675e9de20c8f1e49da3de9c822356b2a52ca436077a36ad5052081d60fa243f
---

本模块提供地点搜索服务。

**起始版本：** 4.1.0(11)

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { site } from '@kit.MapKit';
```

## searchByText

PhonePC/2in1TabletWearable

searchByText(searchByTextParams: SearchByTextParams): Promise<SearchByTextResult>

通过指定的关键字和可选的地理范围，查询诸如旅游景点、企业和学校之类的地点。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| searchByTextParams | [SearchByTextParams](map-site.md#searchbytextparams) | 是 | 关键字搜索的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SearchByTextResult](map-site.md#searchbytextresult)> | Promise对象，返回[SearchByTextResult](map-site.md#searchbytextresult)。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002600001 | System internal error. |
| 1002600002 | Failed to connect to the Map Kit server. |
| 1002600003 | App authentication failed. |
| 1002600004 | The Map permission is not enabled. |
| 1002603001 | Zero result. |

**示例：**

```
1. let params: site.SearchByTextParams = {
2. query: "Piazzale Dante, 41, 55049 Viareggio, Tuscany, Italy",
3. location: {
4. latitude: 31.984410259206815,
5. longitude: 118.76625379397866
6. },
7. radius: 10000,
8. language: "en"
9. };
10. const result = await site.searchByText(params);
11. console.info("Succeeded in searching by text.");
```

## searchByText

PhonePC/2in1TabletWearable

searchByText(context: common.Context, searchByTextParams: SearchByTextParams): Promise<SearchByTextResult>

通过指定的关键字和可选的地理范围，查询诸如旅游景点、企业和学校之类的地点，支持传入Context上下文。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md) | 是 | Context上下文。 |
| searchByTextParams | [SearchByTextParams](map-site.md#searchbytextparams) | 是 | 关键字搜索的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SearchByTextResult](map-site.md#searchbytextresult)> | Promise对象，返回[SearchByTextResult](map-site.md#searchbytextresult)。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002600001 | System internal error. |
| 1002600002 | Failed to connect to the Map Kit server. |
| 1002600003 | App authentication failed. |
| 1002600004 | The Map permission is not enabled. |
| 1002603001 | Zero result. |

**示例：**

```
1. let params: site.SearchByTextParams = {
2. query: "Piazzale Dante, 41, 55049 Viareggio, Tuscany, Italy",
3. location: {
4. latitude: 31.984410259206815,
5. longitude: 118.76625379397866
6. },
7. radius: 10000,
8. language: "en"
9. };
10. const result = await site.searchByText(this.getUIContext().getHostContext(), params);
11. console.info("Succeeded in searching by text.");
```

## nearbySearch

PhonePC/2in1TabletWearable

nearbySearch(nearbySearchParams: NearbySearchParams): Promise<NearbySearchResult>

通过用户传入自己的位置，可以返回周边地点列表。您可以通过提供关键字或指定要搜索的地点的类型来优化搜索结果。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| nearbySearchParams | [NearbySearchParams](map-site.md#nearbysearchparams) | 是 | 周边搜索的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[NearbySearchResult](map-site.md#nearbysearchresult)> | Promise对象，返回[NearbySearchResult](map-site.md#nearbysearchresult)。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002600001 | System internal error. |
| 1002600002 | Failed to connect to the Map Kit server. |
| 1002600003 | App authentication failed. |
| 1002600004 | The Map permission is not enabled. |
| 1002603001 | Zero result. |

**示例：**

```
1. let params: site.NearbySearchParams = {
2. location: {
3. latitude:51.50811219132287,
4. longitude:-0.07594896472392065
5. },
6. poiTypes: [
7. "Watch_Store",
8. "SUBWAY",
9. "PRIMARY_SCHOOL",
10. "GENERAL_AUTO_REPAIR_SERVICE_CENTER"
11. ]
12. }
13. // 返回周边搜索结果
14. const result = await site.nearbySearch(params);
15. console.info(`Succeeded in searching nearby. result is ${result}`);
```

## nearbySearch

PhonePC/2in1TabletWearable

nearbySearch(context: common.Context, nearbySearchParams: NearbySearchParams): Promise<NearbySearchResult>

通过用户传入自己的位置，可以返回周边地点列表，支持传入Context上下文。您可以通过提供关键字或指定要搜索的地点的类型来优化搜索结果。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md) | 是 | Context上下文。 |
| nearbySearchParams | [NearbySearchParams](map-site.md#nearbysearchparams) | 是 | 周边搜索的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[NearbySearchResult](map-site.md#nearbysearchresult)> | Promise对象，返回[NearbySearchResult](map-site.md#nearbysearchresult)。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002600001 | System internal error. |
| 1002600002 | Failed to connect to the Map Kit server. |
| 1002600003 | App authentication failed. |
| 1002600004 | The Map permission is not enabled. |
| 1002603001 | Zero result. |

**示例：**

```
1. let params: site.NearbySearchParams = {
2. location: {
3. latitude:51.50811219132287,
4. longitude:-0.07594896472392065
5. },
6. poiTypes: [
7. "Watch_Store",
8. "SUBWAY",
9. "PRIMARY_SCHOOL",
10. "GENERAL_AUTO_REPAIR_SERVICE_CENTER"
11. ]
12. }
13. // 返回周边搜索结果
14. const result = await site.nearbySearch(this.getUIContext().getHostContext(), params);
15. console.info(`Succeeded in searching nearby. result is ${result}`);
```

## queryAutoComplete

PhonePC/2in1TabletWearable

queryAutoComplete(queryAutoCompleteParams: QueryAutoCompleteParams): Promise<QueryAutoCompleteResult>

根据输入的关键字返回预测的输入关键字和地点查询建议。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| queryAutoCompleteParams | [QueryAutoCompleteParams](map-site.md#queryautocompleteparams) | 是 | 自动补全的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[QueryAutoCompleteResult](map-site.md#queryautocompleteresult)> | Promise对象，返回[QueryAutoCompleteResult](map-site.md#queryautocompleteresult)。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002600001 | System internal error. |
| 1002600002 | Failed to connect to the Map Kit server. |
| 1002600003 | App authentication failed. |
| 1002600004 | The Map permission is not enabled. |
| 1002603001 | Zero result. |

**示例：**

```
1. let params: site.QueryAutoCompleteParams = {
2. query: "hotel",
3. location: {
4. latitude: 31.984410259206815,
5. longitude: 118.76625379397866
6. },
7. language: "en",
8. isChildren: true
9. };
10. const result = await site.queryAutoComplete(params);
11. console.info("Succeeded in querying.");
```

## queryAutoComplete

PhonePC/2in1TabletWearable

queryAutoComplete(context: common.Context, queryAutoCompleteParams: QueryAutoCompleteParams): Promise<QueryAutoCompleteResult>

根据输入的关键字返回预测的输入关键字和地点查询建议，支持传入Context上下文。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md) | 是 | Context上下文。 |
| queryAutoCompleteParams | [QueryAutoCompleteParams](map-site.md#queryautocompleteparams) | 是 | 自动补全的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[QueryAutoCompleteResult](map-site.md#queryautocompleteresult)> | Promise对象，返回[QueryAutoCompleteResult](map-site.md#queryautocompleteresult)。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002600001 | System internal error. |
| 1002600002 | Failed to connect to the Map Kit server. |
| 1002600003 | App authentication failed. |
| 1002600004 | The Map permission is not enabled. |
| 1002603001 | Zero result. |

**示例：**

```
1. let params: site.QueryAutoCompleteParams = {
2. query: "hotel",
3. location: {
4. latitude: 31.984410259206815,
5. longitude: 118.76625379397866
6. },
7. language: "en",
8. isChildren: true
9. };
10. const result = await site.queryAutoComplete(this.getUIContext().getHostContext(), params);
11. console.info("Succeeded in querying.");
```

## searchById

PhonePC/2in1TabletWearable

searchById(searchByIdParams: SearchByIdParams): Promise<SearchByIdResult>

根据地点ID获取地点详情。地点详情包括：地点名称、地址详细信息、经纬度等。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| searchByIdParams | [SearchByIdParams](map-site.md#searchbyidparams) | 是 | 地点详情的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SearchByIdResult](map-site.md#searchbyidresult)> | Promise对象，返回[SearchByIdResult](map-site.md#searchbyidresult)。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002600001 | System internal error. |
| 1002600002 | Failed to connect to the Map Kit server. |
| 1002600003 | App authentication failed. |
| 1002600004 | The Map permission is not enabled. |
| 1002603001 | Zero result. |

**示例：**

```
1. let params: site.SearchByIdParams = {
2. siteId: "144129739873977856",
3. language: "en",
4. isChildren: true
5. };
6. const result = await site.searchById(params);
7. console.info("Succeeded in searching by id.");
```

## searchById

PhonePC/2in1TabletWearable

searchById(context: common.Context, searchByIdParams: SearchByIdParams): Promise<SearchByIdResult>

根据地点ID获取地点详情，支持传入Context上下文。地点详情包括：地点名称、地址详细信息、经纬度等。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md) | 是 | Context上下文。 |
| searchByIdParams | [SearchByIdParams](map-site.md#searchbyidparams) | 是 | 地点详情的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SearchByIdResult](map-site.md#searchbyidresult)> | Promise对象，返回[SearchByIdResult](map-site.md#searchbyidresult)。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002600001 | System internal error. |
| 1002600002 | Failed to connect to the Map Kit server. |
| 1002600003 | App authentication failed. |
| 1002600004 | The Map permission is not enabled. |
| 1002603001 | Zero result. |

**示例：**

```
1. let params: site.SearchByIdParams = {
2. siteId: "144129739873977856",
3. language: "en",
4. isChildren: true
5. };
6. const result = await site.searchById(this.getUIContext().getHostContext(), params);
7. console.info("Succeeded in searching by id.");
```

## geocode

PhonePC/2in1TabletWearable

geocode(geocodeParams: GeocodeParams): Promise<GeocodeResult>

根据结构化地址获取地点的经纬度。使用Promise异步回调。

说明

根据地址获取地点的空间坐标，如经纬度，最多返回10条记录。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| geocodeParams | [GeocodeParams](map-site.md#geocodeparams) | 是 | 正地理编码的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[GeocodeResult](map-site.md#geocoderesult)> | Promise对象，返回[GeocodeResult](map-site.md#geocoderesult)。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002600001 | System internal error. |
| 1002600002 | Failed to connect to the Map Kit server. |
| 1002600003 | App authentication failed. |
| 1002600004 | The Map permission is not enabled. |
| 1002603001 | Zero result. |

**示例：**

```
1. let params: site.GeocodeParams = {
2. "query": "Piazzale Dante, 41, 55049 Viareggio",
3. "language": "en"
4. };
5. const result = await site.geocode(params);
6. console.info("Succeeded in geocoding.");
```

## geocode

PhonePC/2in1TabletWearable

geocode(context: common.Context, geocodeParams: GeocodeParams): Promise<GeocodeResult>

根据结构化地址获取地点的经纬度，支持传入Context上下文。使用Promise异步回调。

说明

根据地址获取地点的空间坐标，如经纬度，最多返回10条记录。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md) | 是 | Context上下文。 |
| geocodeParams | [GeocodeParams](map-site.md#geocodeparams) | 是 | 正地理编码的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[GeocodeResult](map-site.md#geocoderesult)> | Promise对象，返回[GeocodeResult](map-site.md#geocoderesult)。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002600001 | System internal error. |
| 1002600002 | Failed to connect to the Map Kit server. |
| 1002600003 | App authentication failed. |
| 1002600004 | The Map permission is not enabled. |
| 1002603001 | Zero result. |

**示例：**

```
1. let params: site.GeocodeParams = {
2. "query": "Piazzale Dante, 41, 55049 Viareggio",
3. "language": "en"
4. };
5. const result = await site.geocode(this.getUIContext().getHostContext(), params);
6. console.info("Succeeded in geocoding.");
```

## reverseGeocode

PhonePC/2in1TabletWearable

reverseGeocode(reverseGeocodeParams: ReverseGeocodeParams): Promise<ReverseGeocodeResult>

逆地理编码接口能够根据经纬度返回对应的地址信息，包括位置描述信息、结构化区划信息、周边POI地点等详细信息。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| reverseGeocodeParams | [ReverseGeocodeParams](map-site.md#reversegeocodeparams) | 是 | 逆地理编码的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ReverseGeocodeResult](map-site.md#reversegeocoderesult)> | Promise对象，返回[ReverseGeocodeResult](map-site.md#reversegeocoderesult)。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002600001 | System internal error. |
| 1002600002 | Failed to connect to the Map Kit server. |
| 1002600003 | App authentication failed. |
| 1002600004 | The Map permission is not enabled. |
| 1002603001 | Zero result. |

**示例：**

```
1. let params: site.ReverseGeocodeParams = {
2. location: {
3. latitude: 31.984410259206815,
4. longitude: 118.76625379397866
5. },
6. language: "en",
7. radius: 200
8. };
9. const result = await site.reverseGeocode(params);
10. console.info("Succeeded in reversing geocode.");
```

## reverseGeocode

PhonePC/2in1TabletWearable

reverseGeocode(context: common.Context, reverseGeocodeParams: ReverseGeocodeParams): Promise<ReverseGeocodeResult>

逆地理编码接口能够根据经纬度返回对应的地址信息，包括位置描述信息、结构化区划信息、周边POI地点等详细信息，支持传入Context上下文。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | [common.Context](js-apis-inner-application-context.md) | 是 | Context上下文。 |
| reverseGeocodeParams | [ReverseGeocodeParams](map-site.md#reversegeocodeparams) | 是 | 逆地理编码的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ReverseGeocodeResult](map-site.md#reversegeocoderesult)> | Promise对象，返回[ReverseGeocodeResult](map-site.md#reversegeocoderesult)。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-map.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid input parameter. |
| 1002600001 | System internal error. |
| 1002600002 | Failed to connect to the Map Kit server. |
| 1002600003 | App authentication failed. |
| 1002600004 | The Map permission is not enabled. |
| 1002603001 | Zero result. |

**示例：**

```
1. let params: site.ReverseGeocodeParams = {
2. location: {
3. latitude: 31.984410259206815,
4. longitude: 118.76625379397866
5. },
6. language: "en",
7. radius: 200
8. };
9. const result = await site.reverseGeocode(this.getUIContext().getHostContext(), params);
10. console.info("Succeeded in reversing geocode.");
```

## SortRule

PhonePC/2in1TabletWearable

结果排序规则。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COMPOSITE | 0 | 综合排序。 |
| DISTANCE | 1 | 按距离排序。 |

## SearchByTextParams

PhonePC/2in1TabletWearable

SearchByTextParams定义了搜索关键字的参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| query | string | 否 | 否 | 搜索关键字，例如“故宫”。参数的长度范围：[1, 512]。 |
| location | [mapCommon.LatLng](map-common.md#latlng) | 否 | 是 | 搜索结果的经纬度。 |
| radius | number | 否 | 是 | Location的搜索半径，单位：米。取值范围：[1, 50000]，默认50000米。小数点后数字忽略。异常值返回错误码401。 |
| poiTypes | Array<string> | 否 | 是 | 返回指定的华为分类体系的地点，取值范围参见[HwLocationType](map-poi.md#hwlocationtype)。 |
| countryCodes | Array<string> | 否 | 是 | 在指定的国家内搜索，采用ISO 3166-1 alpha-2。  最多传5个国家或地区码。 |
| cityId | string | 否 | 是 | 在指定的城市内搜索，参数的长度范围：[1, 32]。  **说明：**  - 支持中国大陆和港澳的中文城市名。  - 对中国大陆城市及港澳地区，支持传入3-4位数字cityCode或6位数字adminCode，参见[城市码及区划代码表](map-citycode.md)。  - 支持传入16-18位数字cityId。 |
| isCityLimit | boolean | 否 | 是 | 搜索结果是否强限制在指定城市内，默认值：false，需配合cityId参数使用，若未传cityId按默认值false处理。  - true：强限制在指定城市内  - false：不强限制在指定城市内 |
| language | string | 否 | 是 | 返回结果的语言类型，参数的长度范围：[1, 16]。语种取值请参见[位置搜索支持语言](../harmonyos-guides/map-language.md#位置搜索支持语言)列表。  如果不传，默认返回地点的当地语言。异常值按默认值处理。 |
| pageSize | number | 否 | 是 | 每页返回的记录数。取值范围：[1, 20]，默认值为20。 |
| pageIndex | number | 否 | 是 | 当前页数。取值范围：[1, 500]，默认值为1。  **说明：**  pageIndex \* pageSize <= 500 |
| isChildren | boolean | 否 | 是 | 是否返回子节点，默认为false。  - true：如果有子节点信息，则返回子节点的全量信息  - false：不返回 |

## NearbySearchParams

PhonePC/2in1TabletWearable

周边搜索的参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| location | [mapCommon.LatLng](map-common.md#latlng) | 否 | 否 | 当前用户的定位。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| radius | number | 否 | 是 | 搜索结果限定的半径范围，单位：米。取值范围：[1, 50000]，默认值为1000米。小数点后数字忽略。异常值返回错误码401。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| query | string | 否 | 是 | 搜索关键字，参数的长度范围：[1, 512]。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| poiTypes | Array<string> | 否 | 是 | 返回指定的华为分类体系的地点，取值范围参见[HwLocationType](map-poi.md#hwlocationtype)。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| language | string | 否 | 是 | 输入语言，参数的长度范围：[1, 16]。语种取值请参见[位置搜索支持语言](../harmonyos-guides/map-language.md#位置搜索支持语言)列表。  如果不传，默认返回地点的当地语言。异常值按默认值处理。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| pageSize | number | 否 | 是 | 每页返回的记录数。取值范围：[1, 20]，默认值为20。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| pageIndex | number | 否 | 是 | 当前页数。取值范围：[1, 500]，默认值为1。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。  **说明：**  pageIndex \* pageSize <= 500 |
| sortRule | [SortRule](map-site.md#sortrule) | 否 | 是 | 排序规则，默认值为[SortRule](map-site.md#sortrule).COMPOSITE。  **起始版本：** 5.0.0(12)  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |

## QueryAutoCompleteParams

PhonePC/2in1TabletWearable

自动补全的参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| query | string | 否 | 否 | 搜索关键字，参数的长度范围：[1, 512]。 |
| location | [mapCommon.LatLng](map-common.md#latlng) | 否 | 是 | 搜索结果的经纬度。 |
| radius | number | 否 | 是 | Location的搜索半径，单位：米。取值范围：[1, 50000]，默认值为50000米。小数点后数字忽略。异常值返回错误码401。 |
| poiTypes | Array<string> | 否 | 是 | 返回指定的华为分类体系的地点，取值范围参见[HwLocationType](map-poi.md#hwlocationtype)。 |
| cityId | string | 否 | 是 | 在指定的城市内搜索，参数的长度范围：[1, 32]。  **说明：**  - 支持中国大陆和港澳的中文城市名。  - 对中国大陆城市及港澳地区，支持传入3-4位数字cityCode或6位数字adminCode，参见[城市码及区划代码表](map-citycode.md)。  - 支持传入16-18位数字cityId。 |
| isCityLimit | boolean | 否 | 是 | 搜索结果是否强限制在指定城市内，默认值：false，需配合cityId参数使用，若未传cityId按默认值false处理。  - false：不强限制在指定城市内 |
| language | string | 否 | 是 | 输入语言，参数的长度范围：[1, 16]。语种取值请参见[位置搜索支持语言](../harmonyos-guides/map-language.md#位置搜索支持语言)列表。  如果不传，默认返回地点的当地语言。异常值按默认值处理。 |
| isChildren | boolean | 否 | 是 | 是否返回子节点，默认为false。  - true：如果有子节点信息，则返回子节点的全量信息  - false：不返回 |

## SearchByIdParams

PhonePC/2in1TabletWearable

地点详情的参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| siteId | string | 否 | 否 | 地址ID，参数的长度范围：[1, 256]。 |
| language | string | 否 | 是 | 输入语言，参数的长度范围：[1, 16]。语种取值请参见[位置搜索支持语言](../harmonyos-guides/map-language.md#位置搜索支持语言)列表。  如果不传，默认返回地点的当地语言。异常值按默认值处理。 |
| isChildren | boolean | 否 | 是 | 是否返回子节点，默认为false。  - true：如果有子节点信息，则返回子节点的全量信息  - false：不返回 |

## ReverseGeocodeParams

PhonePC/2in1TabletWearable

逆地理编码的参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| location | [mapCommon.LatLng](map-common.md#latlng) | 否 | 否 | 经纬度。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| language | string | 否 | 是 | 输入语言，参数的长度范围：[1, 16]。语种取值请参见[位置搜索支持语言](../harmonyos-guides/map-language.md#位置搜索支持语言)列表。  如果不传，默认返回地点的当地语言。异常值按默认值处理。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| radius | number | 否 | 是 | 搜索半径，单位：米 。取值范围：[0, 1000]，默认值为1000。小数点后数字忽略。异常值返回错误码401。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| isExtension | boolean | 否 | 是 | 是否扩展返回POI、Aoi、Road、交叉口等信息，推荐设置为true，默认为false。  - true：扩展信息  - false：不扩展，仅返回区划信息  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。  **说明：**  拓展返回信息时，POI信息最多展示30个，Aoi信息最多展示10个，Road信息最多展示3个，交叉口信息最多展示1个。 |
| poiTypes | Array<string> | 否 | 是 | 返回指定的华为分类体系的地点，取值范围参见[HwLocationType](map-poi.md#hwlocationtype)。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| isNearbyAoi | boolean | 否 | 是 | 是否返回附近的Aoi。  仅当isExtension=true时生效。  推荐设置为true，默认值为false。  - true：返回附近的Aoi  - false：仅返回传入经纬度所在的Aoi  **起始版本：** 5.0.0(12)  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| sortRule | [SortRule](map-site.md#sortrule) | 否 | 是 | POI的排序规则。  默认值为[SortRule](map-site.md#sortrule).DISTANCE，即按距离排序。  **起始版本：** 5.0.0(12)  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |

## GeocodeParams

PhonePC/2in1TabletWearable

正地理编码的参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| query | string | 否 | 否 | 地址信息，参数的长度范围：[1, 512]。 |
| language | string | 否 | 是 | 输入语言，参数的长度范围：[1, 16]。语种取值请参见[位置搜索支持语言](../harmonyos-guides/map-language.md#位置搜索支持语言)列表。  如果不传，默认返回地点的当地语言。异常值按默认值处理。 |
| bounds | [mapCommon.LatLngBounds](map-common.md#latlngbounds) | 否 | 是 | 查询结果的搜索范围。 |

## SearchByTextResult

PhonePC/2in1TabletWearable

关键字搜索的结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| totalCount | number | 否 | 否 | 如果查询成功，返回满足搜索条件的记录总数。 |
| sites | Array<[Site](map-site.md#site)> | 否 | 是 | 如果查询成功，返回搜索结果。 |

## NearbySearchResult

PhonePC/2in1TabletWearable

周边搜索的结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| totalCount | number | 否 | 否 | 如果查询成功，返回满足搜索条件的记录总数。 |
| sites | Array<[Site](map-site.md#site)> | 否 | 是 | 如果查询成功，返回搜索结果。 |

## QueryAutoCompleteResult

PhonePC/2in1TabletWearable

自动补全的结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| sites | Array<[Site](map-site.md#site)> | 否 | 是 | 如果查询成功，返回搜索结果。 |

## SearchByIdResult

PhonePC/2in1TabletWearable

地点详情的结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| site | [Site](map-site.md#site) | 否 | 是 | 如果查询成功，返回地点详情。 |

## ReverseGeocodeResult

PhonePC/2in1TabletWearable

逆地理编码的结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| addressComponent | [AddressComponent](map-site.md#addresscomponent) | 否 | 否 | 地址详细信息。 |
| addressDescription | string | 否 | 否 | 非结构化的地址文本。 |
| aois | Array<[Aoi](map-site.md#aoi)> | 否 | 是 | Aoi面信息。 |
| pois | Array<[ReverseGeocodePoi](map-site.md#reversegeocodepoi)> | 否 | 是 | POI信息。 |
| roads | Array<[Road](map-site.md#road)> | 否 | 是 | 道路信息。 |
| intersections | Array<[Intersection](map-site.md#intersection)> | 否 | 是 | 交叉点信息。 |

## GeocodeResult

PhonePC/2in1TabletWearable

正地理编码的结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| sites | Array<[Site](map-site.md#site)> | 否 | 是 | 如果查询成功，返回搜索结果。 |

## Site

PhonePC/2in1TabletWearable

地点详情。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| siteId | string | 否 | 否 | 地点的唯一主键。 |
| name | string | 否 | 是 | 地点名称。 |
| formatAddress | string | 否 | 是 | 格式化的地点详细地址。 |
| addressComponent | [AddressComponent](map-site.md#addresscomponent) | 否 | 否 | 地址详细信息。 |
| location | [mapCommon.LatLng](map-common.md#latlng) | 否 | 是 | 地点的经纬度。 |
| viewport | [mapCommon.LatLngBounds](map-common.md#latlngbounds) | 否 | 是 | 地点的视口范围。  **说明：**  [queryAutoComplete](map-site.md#queryautocomplete)不支持返回此字段。 |
| distance | number | 否 | 是 | 预测地点和传参location之间的直线距离，单位：米。  **说明：**  目前仅关键字搜索和周边搜索支持返回此字段。 |
| poi | [Poi](map-site.md#poi) | 否 | 是 | 如果地点是POI类型，返回POI信息。 |
| utcOffset | number | 否 | 是 | 位置所在时区和UTC时区的差值，单位：分钟。  **说明：** 自动补全不支持返回此字段。 |

## AddressComponent

PhonePC/2in1TabletWearable

地址详细信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| countryCode | string | 否 | 是 | 国家/地区码。 |
| countryName | string | 否 | 是 | 国家名。 |
| adminLevel1 | string | 否 | 是 | 一级行政区。 |
| adminLevel2 | string | 否 | 是 | 二级行政区。 |
| adminLevel3 | string | 否 | 是 | 三级行政区。 |
| adminLevel4 | string | 否 | 是 | 四级行政区。 |
| adminLevel5 | string | 否 | 是 | 五级行政区。 |
| locality | string | 否 | 是 | 地区、区域。 |
| subLocality1 | string | 否 | 是 | 一级子区域。 |
| subLocality2 | string | 否 | 是 | 二级子区域。 |
| neighborhoods | Array<string> | 否 | 是 | 街区、城区。 |
| adminCode | string | 否 | 是 | [行政区划码](map-citycode.md)。  **说明：**  接口返回的行政区划码覆盖中国大陆及港澳地区，包括省份、城市、区/县、乡镇/街道等层级，文档附录中仅提供部分城市行政区划码示例。 |
| postalCode | string | 否 | 是 | 邮政编码。 |
| city | [City](map-site.md#city) | 否 | 是 | 城市信息。 |
| streetNumber | [StreetNumber](map-site.md#streetnumber) | 否 | 是 | 街道号。 |

## City

PhonePC/2in1TabletWearable

城市信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| cityCode | string | 否 | 是 | 城市码。 |
| cityId | string | 否 | 是 | 城市ID。 |
| cityName | string | 否 | 是 | 城市名称。 |

## StreetNumber

PhonePC/2in1TabletWearable

街道号。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| direction | string | 否 | 是 | 该输入点在街道的方向。 |
| distance | number | 否 | 是 | 地点和传参location之间的直线距离，单位：米。 |
| location | [mapCommon.LatLng](map-common.md#latlng) | 否 | 是 | 街道经纬度。 |
| streetNumber | string | 否 | 是 | 街道号。 |
| streetName | string | 否 | 是 | 街道名称。 |
| formatAddress | string | 否 | 是 | 格式化的街道地址。 |

## Poi

PhonePC/2in1TabletWearable

POI信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| poiTypes | Array<string> | 否 | 是 | 华为POI分类体系，取值范围请参见[HwLocationType](map-poi.md#hwlocationtype)。 |
| poiTypeIds | Array<string> | 否 | 是 | 华为POI分类体系Id，预留字段，当前无使用场景。 |
| phone | string | 否 | 是 | 电话号码。 |
| internationalPhone | string | 否 | 是 | 国际电话号码。 |
| rating | number | 否 | 是 | 评分。 |
| websiteUrl | string | 否 | 是 | 网址。 |
| openingHours | [OpeningHours](map-site.md#openinghours) | 否 | 是 | 营业时间。 |
| businessStatus | string | 否 | 是 | 营业状态，其中包括：  - OPEN\_NOW：正在营业。  - CLOSE\_NOW：已休息。  - CLOSED\_TEMPORARILY：临时关闭。  - CLOSED\_PERMANENTLY：永久关闭。  - STATUS\_UNKNOWN：未知。  **说明：**  仅地点详情接口返回。 |
| brand | string | 否 | 是 | 品牌名称。 |
| email | string | 否 | 是 | 邮箱地址。 |
| starRating | number | 否 | 是 | 星级评定。 |
| childNodes | Array<[ChildNode](map-site.md#childnode)> | 否 | 是 | POI的子节点信息。 |
| icon | string | 否 | 是 | POI图标地址。 |
| description | string | 否 | 是 | 描述信息。 |
| abstractText | string | 否 | 是 | 摘要信息。 |
| comment | [Comment](map-site.md#comment) | 否 | 是 | POI的评论信息。 |

## OpeningHours

PhonePC/2in1TabletWearable

营业时间。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| texts | Array<string> | 否 | 是 | 每个星期的开放时间段的描述。 |
| periods | Array<[Period](map-site.md#period)> | 否 | 是 | 开放时间段的详细说明。 |

## Period

PhonePC/2in1TabletWearable

开放时间段的详细说明。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| open | [TimeOfWeek](map-site.md#timeofweek) | 否 | 是 | 开放时间。 |
| close | [TimeOfWeek](map-site.md#timeofweek) | 否 | 是 | 关闭时间。 |

## TimeOfWeek

PhonePC/2in1TabletWearable

时间模型。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| week | number | 否 | 是 | 0：星期日  1：星期一  2：星期二  3：星期三  4：星期四  5：星期五  6：星期六 |
| time | string | 否 | 是 | 24小时制时间，hhmm格式。 |

## ChildNode

PhonePC/2in1TabletWearable

POI的子节点信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| siteId | string | 否 | 是 | 位置ID。 |
| name | string | 否 | 是 | 地点名称。 |
| formatAddress | string | 否 | 是 | 格式化的地点详细地址。 |
| location | [mapCommon.LatLng](map-common.md#latlng) | 否 | 是 | 地点的经纬度。 |
| poiTypes | Array<string> | 否 | 是 | 华为分类体系，取值范围参见[HwLocationType](map-poi.md#hwlocationtype)。 |

## Comment

PhonePC/2in1TabletWearable

POI的评论信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| averageRating | number | 否 | 是 | 平均分。 |
| total | number | 否 | 是 | 总数。 |

## Aoi

PhonePC/2in1TabletWearable

Aoi面信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| area | number | 否 | 是 | Aoi面积。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| distance | number | 否 | 是 | 地点和传参location之间的直线距离，单位：米。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| siteId | string | 否 | 是 | Aoi ID。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| location | [mapCommon.LatLng](map-common.md#latlng) | 否 | 是 | 地点的经纬度。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| name | string | 否 | 是 | 地点名称。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| poiType | string | 否 | 是 | 华为POI分类体系，取值范围请参见[HwLocationType](map-poi.md#hwlocationtype)。  **元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。 |
| direction | string | 否 | 是 | 该Aoi在输入点的方向。  **起始版本：** 5.0.0(12)  **元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |

## ReverseGeocodePoi

PhonePC/2in1TabletWearable

逆地理结果POI信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| address | string | 否 | 是 | 地址。 |
| direction | string | 否 | 是 | 该输入点在POI的方向。 |
| distance | number | 否 | 是 | 地点和传参location之间的直线距离，单位：米。 |
| siteId | string | 否 | 是 | 地点ID。 |
| location | [mapCommon.LatLng](map-common.md#latlng) | 否 | 是 | 地点的经纬度。 |
| name | string | 否 | 是 | 地点名称。 |
| poiType | string | 否 | 是 | 华为POI分类体系，取值范围请参见[HwLocationType](map-poi.md#hwlocationtype)。 |

## Road

PhonePC/2in1TabletWearable

道路信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| direction | string | 否 | 是 | 该输入点在道路的方向。 |
| distance | number | 否 | 是 | 道路和传参location之间的直线距离，单位：米。 |
| siteId | string | 否 | 是 | 道路ID。 |
| location | [mapCommon.LatLng](map-common.md#latlng) | 否 | 是 | 道路的经纬度。 |
| name | string | 否 | 是 | 道路名称。 |

## Intersection

PhonePC/2in1TabletWearable

交叉点信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| direction | string | 否 | 是 | 该输入点交在叉口的方向。 |
| distance | number | 否 | 是 | 交叉点和传参location之间的直线距离，单位：米。 |
| siteId | string | 否 | 是 | 交叉点ID。 |
| location | [mapCommon.LatLng](map-common.md#latlng) | 否 | 是 | 交叉点的经纬度。 |
| name | string | 否 | 是 | 交叉点名称。 |
