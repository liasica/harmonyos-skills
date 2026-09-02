---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-site-search
title: POI搜索
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 位置搜索 > POI搜索
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:58+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:e769fb5f9a834de3f8b897b757244436d84f7850f16a201b18839f668aec16b4
---

## 场景介绍

提供多种查询POI信息的能力：

* 关键字搜索：通过用户输入的关键字，返回地点列表。
* 周边搜索：基于用户设备位置进行地点查找。
* 自动补全：根据输入的关键字返回预测的输入关键字和地点查询建议。
* 地点详情：查询某个地点更详细的信息。

## 接口说明

以下是POI搜索相关接口，主要由[site](../harmonyos-references/map-site.md)命名空间下的方法提供，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-site.md)。

| 接口名 | 描述 |
| --- | --- |
| [searchByText](../harmonyos-references/map-site.md#searchbytext)(searchByTextParams: [SearchByTextParams](../harmonyos-references/map-site.md#searchbytextparams)): Promise<[SearchByTextResult](../harmonyos-references/map-site.md#searchbytextresult)> | 关键字搜索。 |
| [searchByText](../harmonyos-references/map-site.md#searchbytext-1)(context: [common.Context](../harmonyos-references/js-apis-inner-application-context.md), searchByTextParams: [SearchByTextParams](../harmonyos-references/map-site.md#searchbytextparams)): Promise<[SearchByTextResult](../harmonyos-references/map-site.md#searchbytextresult)> | 关键字搜索。支持上传Context上下文。 |
| [nearbySearch](../harmonyos-references/map-site.md#nearbysearch)(nearbySearchParams: [NearbySearchParams](../harmonyos-references/map-site.md#nearbysearchparams)): Promise<[NearbySearchResult](../harmonyos-references/map-site.md#nearbysearchresult)> | 周边搜索。 |
| [nearbySearch](../harmonyos-references/map-site.md#nearbysearch-1)(context: [common.Context](../harmonyos-references/js-apis-inner-application-context.md), nearbySearchParams: [NearbySearchParams](../harmonyos-references/map-site.md#nearbysearchparams)): Promise<[NearbySearchResult](../harmonyos-references/map-site.md#nearbysearchresult)> | 周边搜索。支持上传Context上下文。 |
| [queryAutoComplete](../harmonyos-references/map-site.md#queryautocomplete)(queryAutoCompleteParams: [QueryAutoCompleteParams](../harmonyos-references/map-site.md#queryautocompleteparams)): Promise<[QueryAutoCompleteResult](../harmonyos-references/map-site.md#queryautocompleteresult)> | 自动补全。 |
| [queryAutoComplete](../harmonyos-references/map-site.md#queryautocomplete-1)(context: [common.Context](../harmonyos-references/js-apis-inner-application-context.md), queryAutoCompleteParams: [QueryAutoCompleteParams](../harmonyos-references/map-site.md#queryautocompleteparams)): Promise<[QueryAutoCompleteResult](../harmonyos-references/map-site.md#queryautocompleteresult)> | 自动补全。支持上传Context上下文。 |
| [searchById](../harmonyos-references/map-site.md#searchbyid)(searchByIdParams: [SearchByIdParams](../harmonyos-references/map-site.md#searchbyidparams)): Promise<[SearchByIdResult](../harmonyos-references/map-site.md#searchbyidresult)> | 地点详情。 |
| [searchById](../harmonyos-references/map-site.md#searchbyid-1)(context: [common.Context](../harmonyos-references/js-apis-inner-application-context.md), searchByIdParams: [SearchByIdParams](../harmonyos-references/map-site.md#searchbyidparams)): Promise<[SearchByIdResult](../harmonyos-references/map-site.md#searchbyidresult)> | 地点详情。支持上传Context上下文。 |

## 开发步骤

导入相关模块。

```typescript
import { site } from '@kit.MapKit';
import { BusinessError } from '@kit.BasicServicesKit';
```

### 关键字搜索

通过指定的关键字和可选的地理范围，查询诸如旅游景点、企业和学校之类的地点。

```typescript
let params: site.SearchByTextParams = {
  // 根据自定义关键字进行搜索，例如：“故宫”、“夫子庙”
  query: 'Piazzale Dante, 41, 55049 Viareggio, Tuscany, Italy',
  // 经纬度坐标
  location: {
    latitude: 31.984,
    longitude: 118.76625
  },
  // 指定地理位置的范围半径
  radius: 10000,
  // 搜索结果的语言类型
  language: 'en'
};
// 返回关键字搜索结果
try {
  const result = await site.searchByText(params);
  console.info(`Succeeded in searching by text. result is ${JSON.stringify(result)}`);
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`Failed in searching by text. Code is ${err.code}, message is ${err.message}`);
}
```

### 周边搜索

通过用户传入自己的位置，可以返回周边地点列表。您可以通过提供关键字或指定要搜索的地点的类型来优化搜索结果。

```typescript
let params: site.NearbySearchParams = {
  location: {
    latitude: 51.50811219132287,
    longitude: -0.07594896472392065
  },
  poiTypes: [
    'Watch_Store',
    'SUBWAY',
    'PRIMARY_SCHOOL',
    'GENERAL_AUTO_REPAIR_SERVICE_CENTER'
  ]
}
// 返回周边搜索结果
try {
  const result = await site.nearbySearch(params);
  console.info(`Succeeded in searching nearby. result is ${JSON.stringify(result)}`);
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`Failed in searching nearby. Code is ${err.code}, message is ${err.message}`);
}
```

### 自动补全

根据输入的关键字，将最有可能的搜索词呈现给用户，以减少用户输入信息，提升用户体验。如：输入“北京”，提示“北京市”、“北京站”、“北京西站”等。

```typescript
let params: site.QueryAutoCompleteParams = {
  // 自定义关键字
  query: 'hotel',
  // 经纬度坐标
  location: {
    latitude: 31.984410259206815,
    longitude: 118.76625379397866
  },
  language: 'en',
  // 返回子节点
  isChildren: true
};
// 返回自动补全结果
try {
  const result = await site.queryAutoComplete(params);
  console.info(`Succeeded in querying. result is ${JSON.stringify(result)}`);
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`Failed in querying. Code is ${err.code}, message is ${err.message}`);
}
```

### 地点详情

根据地点的唯一主键地点ID（siteId）获取地点详情。地点详细信息请求返回有关指定地点的更全面的信息，如地点名称、地址详细信息、经纬度等。siteId可通过其他接口（关键字搜索、周边搜索、地点详情、自动补全、正地理编码）的返回结果中获取。

```typescript
let params: site.SearchByIdParams = {
  // 指定主键地点ID
  siteId: '144129739873977856',
  language: 'en',
  // 返回子节点
  isChildren: true
};
// 返回地点详情结果
try {
  const result = await site.searchById(params);
  console.info(`Succeeded in searching. result is ${JSON.stringify(result)}`);
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`Failed in searching. Code is ${err.code}, message is ${err.message}`);
}
```
