---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-navi-routes
title: 出行路线规划
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 路径规划 > 出行路线规划
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:53+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:8f3a9b216c8359936b2a11414dcc0cb36afd5811ad185610f249c693585668b2
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

```
1. import { navi } from '@kit.MapKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
```

### 驾车路径规划

根据起终点坐标检索符合条件的驾车路径规划方案。支持以下功能：

* 支持一次请求返回多条路线，最多支持3条路线。
* 最多支持5个途经点。
* 支持未来出行规划。
* 支持根据实时路况进行合理路线规划。
* 支持多种路线偏好选择，如时间最短、避免经过收费的公路、避开高速公路、距离优先等。

```
1. async testDrivingRoutes() {
2. let params: navi.DrivingRouteParams = {
3. // 起点的经纬度
4. origins: [{
5. latitude: 31.982129213545843,
6. longitude: 120.27745557768591
7. }],
8. // 终点的经纬度
9. destination: {
10. latitude: 31.986129213545843,
11. longitude: 120.32745557768591
12. },
13. // 路径的途经点
14. waypoints: [{
15. latitude: 31.967236140819114,
16. longitude: 120.27142088866847
17. }, {
18. latitude: 31.972868002238872,
19. longitude: 120.2943211817165
20. }, {
21. latitude: 31.98469327973332,
22. longitude: 120.29101107384068
23. }],
24. language: 'zh_CN'
25. };
26. try {
27. const result = await navi.getDrivingRoutes(params);
28. console.info(`Succeeded in getting driving routes. result is ${JSON.stringify(result)}`);
29. } catch (error) {
30. const err: BusinessError = error as BusinessError;
31. console.error(`Failed in getting driving routes. Code is ${err.code}, message is ${err.message}`);
32. }
33. }
```

### 步行路径规划

根据起终点坐标检索符合条件的步行路径规划方案。支持以下功能：

* 支持直线距离150km以内的步行路径规划能力。
* 融入出行策略（时间最短、避免轮渡）。

```
1. async testWalkingRoutes() {
2. let params: navi.RouteParams = {
3. // 起点的经纬度
4. origins: [{
5. latitude: 39.992281,
6. longitude: 116.31088
7. }, {
8. latitude: 39.996,
9. longitude: 116.311
10. }],
11. // 终点的经纬度
12. destination: {
13. latitude: 39.94,
14. longitude: 116.311
15. },
16. language: 'zh_CN'
17. };
18. try {
19. const result = await navi.getWalkingRoutes(params);
20. console.info(`Succeeded in getting walking routes. result is ${JSON.stringify(result)}`);
21. } catch (error) {
22. const err: BusinessError = error as BusinessError;
23. console.error(`Failed in getting walking routes. Code is ${err.code}, message is ${err.message}`);
24. }
25. }
```

### 骑行路径规划

根据起终点坐标检索符合条件的骑行路径规划方案。支持以下功能：

* 支持直线距离500km以内的骑行路径规划能力。
* 融入出行策略（时间最短、避免轮渡）。

```
1. async testCyclingRoutes() {
2. let params: navi.RouteParams = {
3. // 起点的经纬度
4. origins: [{
5. latitude: 31.9844102,
6. longitude: 118.7662537
7. }],
8. // 终点的经纬度
9. destination: {
10. latitude: 31.9874102,
11. longitude: 118.7362537
12. },
13. language: 'zh_CN'
14. };
15. try {
16. const result = await navi.getCyclingRoutes(params);
17. console.info(`Succeeded in getting cycling routes. result is ${JSON.stringify(result)}`);
18. } catch (error) {
19. const err: BusinessError = error as BusinessError;
20. console.error(`Failed in getting cycling routes. Code is ${err.code}, message is ${err.message}`);
21. }
22. }
```

### 公共交通规划

根据起点终点坐标规划道路，从而返回两地之间的多种公共交通中转路线，仅支持中国大陆。

```
1. async testGetTransitRoutes() {
2. let params: navi.TransitRouteParams = {
3. // 起点经纬度
4. origin: {
5. latitude: 39.921619,
6. longitude: 116.356587
7. },
8. // 终点经纬度
9. destination: {
10. latitude: 39.94161,
11. longitude: 116.353621
12. },
13. // 设置出发时间为当前时间（单位s）
14. departureTime: new Date().getTime() / 1000
15. };
16. try {
17. const result = await navi.getTransitRoutes(this.getUIContext().getHostContext(), params);
18. console.info(`Succeeded in getting transit routes. result is ${JSON.stringify(result)}`);
19. } catch (error) {
20. const err: BusinessError = error as BusinessError;
21. console.error(`Failed in getting transit routes. Code is ${err.code}, message is ${err.message}`);
22. }
23. }
```
