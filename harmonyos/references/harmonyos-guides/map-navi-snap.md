---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-navi-snap
title: 轨迹绑路
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 路径规划 > 轨迹绑路
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8200e655ac5c1ed2ee43a268f864be52719ad06869988ae7e7b431a298f122c5
---

## 场景介绍

根据给定的坐标点捕捉道路，将用户的轨迹纠正到道路上，从而返回用户实际驾车经过的道路坐标。

## 接口说明

以下是路径规划功能相关接口，主要由[navi](../harmonyos-references/map-navi-api.md)命名空间下的方法提供，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-navi-api.md)。

| 接口名 | 描述 |
| --- | --- |
| [SnapToRoadsParams](../harmonyos-references/map-navi-api.md#snaptoroadsparams) | 轨迹绑路的参数。 |
| [snapToRoads](../harmonyos-references/map-navi-api.md#snaptoroads)(params: [SnapToRoadsParams](../harmonyos-references/map-navi-api.md#snaptoroadsparams)): Promise<[SnapToRoadsResult](../harmonyos-references/map-navi-api.md#snaptoroadsresult)> | 轨迹绑路。 |
| [snapToRoads](../harmonyos-references/map-navi-api.md#snaptoroads-1)(context: [common.Context](../harmonyos-references/js-apis-inner-application-context.md), params: [SnapToRoadsParams](../harmonyos-references/map-navi-api.md#snaptoroadsparams)): Promise<[SnapToRoadsResult](../harmonyos-references/map-navi-api.md#snaptoroadsresult)> | 轨迹绑路。支持传入Context上下文。 |
| [SnapToRoadsResult](../harmonyos-references/map-navi-api.md#snaptoroadsresult) | 轨迹绑路的结果。 |

## 开发步骤

导入相关模块。

```
1. import { navi } from '@kit.MapKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
```

### 轨迹绑路

根据给定的坐标点捕捉道路，将用户的轨迹纠正到道路上，从而返回用户实际驾车经过的道路坐标。

```
1. async testSnapToRoads() {
2. let params: navi.SnapToRoadsParams = {
3. // 道路贴合点集合，不能超过100个，且相邻两个点距离需小于等于500米
4. points: [{
5. latitude: 31.984410259206815,
6. longitude: 118.76625379397866
7. }]
8. };
9. try {
10. const result = await navi.snapToRoads(params);
11. console.info(`Succeeded in snapping to roads. result is ${JSON.stringify(result)}`);
12. } catch (error) {
13. const err: BusinessError = error as BusinessError;
14. console.error(`Failed in snapping to roads. Code is ${err.code}, message is ${err.message}`);
15. }
16. }
```
