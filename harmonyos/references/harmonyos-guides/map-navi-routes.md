---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-navi-routes
title: 出行路线规划
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 路径规划 > 出行路线规划
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:58+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:45c4f8fcfe30c5bece56cc0e05389bb229968a48b7f3bff4c5fcee4d700f8679
---

## 场景介绍

从5.1.1(19)开始，支持公共交通规划功能。

提供两点之间驾车、步行、骑行和公共交通的路径规划能力。其中驾车路径规划支持添加途经点。

## 接口说明

以下是路径规划功能相关接口，主要由[navi](../harmonyos-references/map-navi-api.md)命名空间下的方法提供，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-navi-api.md)。

| 接口名 | 描述 |
| --- | --- |
| [getDrivingRoutes](../harmonyos-references/map-navi-api.md#getdrivingroutes)(params: [DrivingRouteParams](../harmonyos-references/map-navi-api.md#drivingrouteparams)): Promise<[RouteResult](../harmonyos-references/map-navi-api.md#routeresult)> | 驾车路径规划。 |
| [getDrivingRoutes](../harmonyos-references/map-navi-api.md#getdrivingroutes-1)(context: [common.Context](../harmonyos-references/js-apis-inner-application-context.md), params: [DrivingRouteParams](../harmonyos-references/map-navi-api.md#drivingrouteparams)): Promise<[RouteResult](../harmonyos-references/map-navi-api.md#routeresult)> | 驾车路径规划。支持传入Context上下文。 |
| [getWalkingRoutes](../harmonyos-references/map-navi-api.md#getwalkingroutes)(params: [RouteParams](../harmonyos-references/map-navi-api.md#routeparams)): Promise<[RouteResult](../harmonyos-references/map-navi-api.md#routeresult)> | 步行路径规划。 |
| [getWalkingRoutes](../harmonyos-references/map-navi-api.md#getwalkingroutes-1)(context: [common.Context](../harmonyos-references/js-apis-inner-application-context.md), params: [RouteParams](../harmonyos-references/map-navi-api.md#routeparams)): Promise<[RouteResult](../harmonyos-references/map-navi-api.md#routeresult)> | 步行路径规划。支持传入Context上下文。 |
| [getCyclingRoutes](../harmonyos-references/map-navi-api.md#getcyclingroutes)(params: [RouteParams](../harmonyos-references/map-navi-api.md#routeparams)): Promise<[RouteResult](../harmonyos-references/map-navi-api.md#routeresult)> | 骑行路径规划。 |
| [getCyclingRoutes](../harmonyos-references/map-navi-api.md#getcyclingroutes-1)(context: [common.Context](../harmonyos-references/js-apis-inner-application-context.md), params: [RouteParams](../harmonyos-references/map-navi-api.md#routeparams)): Promise<[RouteResult](../harmonyos-references/map-navi-api.md#routeresult)> | 骑行路径规划。支持传入Context上下文。 |
| [getTransitRoutes](../harmonyos-references/map-navi-api.md#gettransitroutes)(context: [common.Context](../harmonyos-references/js-apis-inner-application-context.md), params: [TransitRouteParams](../harmonyos-references/map-navi-api.md#transitrouteparams)): Promise<[TransitRouteResult](../harmonyos-references/map-navi-api.md#transitrouteresult)> | 公共交通规划。支持传入Context上下文。 |
| [DrivingRouteParams](../harmonyos-references/map-navi-api.md#drivingrouteparams) | 驾车路径规划的参数。 |
| [RouteParams](../harmonyos-references/map-navi-api.md#routeparams) | 步行、骑行路径规划的参数。 |
| [TransitRouteParams](../harmonyos-references/map-navi-api.md#transitrouteparams) | 公共交通规划的参数。 |
| [RouteResult](../harmonyos-references/map-navi-api.md#routeresult) | 路径规划的结果。 |
| [TransitRouteResult](../harmonyos-references/map-navi-api.md#transitrouteresult) | 公共交通规划的结果。 |

## 开发步骤

导入相关模块。

```typescript
import { navi } from '@kit.MapKit';
import { BusinessError } from '@kit.BasicServicesKit';
```

### 驾车路径规划

根据起终点坐标检索符合条件的驾车路径规划方案。支持以下功能：

* 支持一次请求返回多条路线，最多支持3条路线。
* 最多支持5个途经点。
* 支持未来出行规划。
* 支持根据实时路况进行合理路线规划。
* 支持多种路线偏好选择，如时间最短、避免经过收费的公路、避开高速公路、距离优先等。

```typescript
async testDrivingRoutes() {
  let params: navi.DrivingRouteParams = {
    // 起点的经纬度
    origins: [{
      latitude: 31.982129213545843,
      longitude: 120.27745557768591
    }],
    // 终点的经纬度
    destination: {
      latitude: 31.986129213545843,
      longitude: 120.32745557768591
    },
    // 路径的途经点
    waypoints: [{
      latitude: 31.967236140819114,
      longitude: 120.27142088866847
    }, {
      latitude: 31.972868002238872,
      longitude: 120.2943211817165
    }, {
      latitude: 31.98469327973332,
      longitude: 120.29101107384068
    }],
    language: 'zh_CN'
  };
  try {
    const result = await navi.getDrivingRoutes(params);
    console.info(`Succeeded in getting driving routes. result is ${JSON.stringify(result)}`);
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(`Failed in getting driving routes. Code is ${err.code}, message is ${err.message}`);
  }
}
```

### 步行路径规划

根据起终点坐标检索符合条件的步行路径规划方案。支持以下功能：

* 支持直线距离150km以内的步行路径规划能力。
* 融入出行策略（时间最短、避免轮渡）。

```typescript
async testWalkingRoutes() {
  let params: navi.RouteParams = {
    // 起点的经纬度
    origins: [{
      latitude: 39.992281,
      longitude: 116.31088
    }, {
      latitude: 39.996,
      longitude: 116.311
    }],
    // 终点的经纬度
    destination: {
      latitude: 39.94,
      longitude: 116.311
    },
    language: 'zh_CN'
  };
  try {
    const result = await navi.getWalkingRoutes(params);
    console.info(`Succeeded in getting walking routes. result is ${JSON.stringify(result)}`);
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(`Failed in getting walking routes. Code is ${err.code}, message is ${err.message}`);
  }
}
```

### 骑行路径规划

根据起终点坐标检索符合条件的骑行路径规划方案。支持以下功能：

* 支持直线距离500km以内的骑行路径规划能力。
* 融入出行策略（时间最短、避免轮渡）。

```typescript
async testCyclingRoutes() {
  let params: navi.RouteParams = {
    // 起点的经纬度
    origins: [{
      latitude: 31.9844102,
      longitude: 118.7662537
    }],
    // 终点的经纬度
    destination: {
      latitude: 31.9874102,
      longitude: 118.7362537
    },
    language: 'zh_CN'
  };
  try {
    const result = await navi.getCyclingRoutes(params);
    console.info(`Succeeded in getting cycling routes. result is ${JSON.stringify(result)}`);
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(`Failed in getting cycling routes. Code is ${err.code}, message is ${err.message}`);
  }
}
```

### 公共交通规划

根据起点终点坐标规划道路，从而返回两地之间的多种公共交通中转路线，仅支持中国大陆。

```typescript
async testGetTransitRoutes() {
  let params: navi.TransitRouteParams = {
    // 起点经纬度
    origin: {
      latitude: 39.921619,
      longitude: 116.356587
    },
    // 终点经纬度
    destination: {
      latitude: 39.94161,
      longitude: 116.353621
    },
    // 设置出发时间为当前时间（单位s）
    departureTime: new Date().getTime() / 1000
  };
  try {
    const result = await navi.getTransitRoutes(this.getUIContext().getHostContext(), params);
    console.info(`Succeeded in getting transit routes. result is ${JSON.stringify(result)}`);
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(`Failed in getting transit routes. Code is ${err.code}, message is ${err.message}`);
  }
}
```
