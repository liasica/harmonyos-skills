---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-navi-matrix
title: 批量算路
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > 路径规划 > 批量算路
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:58+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:95f4d8f71e6db3c71fb99eccaf9b0c33f148dff49c699109cb8b72eafc55a5f2
---

## 场景介绍

多个起点到多个终点的批量算路功能，在驾车、步行、骑行模式下，快速批量计算多个起点分别到多个终点的路线距离和耗时。

## 接口说明

以下是路径规划功能相关接口，主要由[navi](../harmonyos-references/map-navi-api.md)命名空间下的方法提供，更多接口及使用方法请参见[接口文档](../harmonyos-references/map-navi-api.md)。

| 接口名 | 描述 |
| --- | --- |
| [getDrivingMatrix](../harmonyos-references/map-navi-api.md#getdrivingmatrix)(params: [DrivingMatrixParams](../harmonyos-references/map-navi-api.md#drivingmatrixparams)): Promise<[MatrixResult](../harmonyos-references/map-navi-api.md#matrixresult)> | 驾车批量算路。 |
| [getDrivingMatrix](../harmonyos-references/map-navi-api.md#getdrivingmatrix-1)(context: [common.Context](../harmonyos-references/js-apis-inner-application-context.md), params: [DrivingMatrixParams](../harmonyos-references/map-navi-api.md#drivingmatrixparams)): Promise<[MatrixResult](../harmonyos-references/map-navi-api.md#matrixresult)> | 驾车批量算路。支持传入Context上下文。 |
| [getWalkingMatrix](../harmonyos-references/map-navi-api.md#getwalkingmatrix)(params: [MatrixParams](../harmonyos-references/map-navi-api.md#matrixparams)): Promise<[MatrixResult](../harmonyos-references/map-navi-api.md#matrixresult)> | 步行批量算路。 |
| [getWalkingMatrix](../harmonyos-references/map-navi-api.md#getwalkingmatrix-1)(context: [common.Context](../harmonyos-references/js-apis-inner-application-context.md), params: [MatrixParams](../harmonyos-references/map-navi-api.md#matrixparams)): Promise<[MatrixResult](../harmonyos-references/map-navi-api.md#matrixresult)> | 步行批量算路。支持传入Context上下文。 |
| [getCyclingMatrix](../harmonyos-references/map-navi-api.md#getcyclingmatrix)(params: [MatrixParams](../harmonyos-references/map-navi-api.md#matrixparams)): Promise<[MatrixResult](../harmonyos-references/map-navi-api.md#matrixresult)> | 骑行批量算路。 |
| [getCyclingMatrix](../harmonyos-references/map-navi-api.md#getcyclingmatrix-1)(context: [common.Context](../harmonyos-references/js-apis-inner-application-context.md), params: [MatrixParams](../harmonyos-references/map-navi-api.md#matrixparams)): Promise<[MatrixResult](../harmonyos-references/map-navi-api.md#matrixresult)> | 骑行批量算路。支持传入Context上下文。 |
| [DrivingMatrixParams](../harmonyos-references/map-navi-api.md#drivingmatrixparams) | 驾车批量算路的参数。 |
| [MatrixParams](../harmonyos-references/map-navi-api.md#matrixparams) | 步行、骑行批量算路的参数。 |
| [MatrixResult](../harmonyos-references/map-navi-api.md#matrixresult) | 批量算路的结果。 |

## 开发步骤

导入相关模块。

```typescript
import { navi } from '@kit.MapKit';
import { BusinessError } from '@kit.BasicServicesKit';
```

### 驾车批量算路

根据多组起终点坐标批量检索符合条件的驾车路径规划方案。支持以下功能：

* 支持未来出行规划。
* 支持根据实时路况进行合理路线规划。
* 支持多种路线偏好选择，如时间最短、避免经过收费的公路、避开高速公路、距离优先等。

**说明** 

为保证性能与准确性，单次请求中的起点数量乘以终点数量应小于100。

```typescript
async testDrivingMatrix() {
  let params: navi.DrivingMatrixParams = {
    // 起点的经纬度
    origins: [{
      latitude: 31.9844,
      longitude: 118.766253
    }, {
      latitude: 31.9644,
      longitude: 118.746253
    }],
    // 终点的经纬度
    destinations: [{
      latitude: 31.9344,
      longitude: 118.706253
    }],
    // 时间预估模型
    trafficMode: 2,
    language: 'zh_CN'
  };
  try {
    const result = await navi.getDrivingMatrix(params);
    console.info(`Succeeded in getting driving matrix. result is ${JSON.stringify(result)}`);
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(`Failed in getting driving matrix. Code is ${err.code}, message is ${err.message}`);
  }
}
```

### 步行批量算路

根据多组起终点坐标批量检索符合条件的步行路径规划方案。支持以下功能：

* 支持150km以内的步行路径规划能力。
* 融入出行策略（时间最短、避免轮渡）。

**说明** 

为保证性能与准确性，单次请求中的起点数量乘以终点数量应小于100。

```typescript
async testWalkingMatrix() {
  let params: navi.MatrixParams = {
    // 起点的经纬度
    origins: [
      {
        latitude: 31.9844,
        longitude: 118.766253
      }, {
      latitude: 31.9644,
      longitude: 118.746253
    }],
    // 终点的经纬度
    destinations: [{
      latitude: 31.9344,
      longitude: 118.706253
    }],
    language: 'zh_CN'
  };
  try {
    const result = await navi.getWalkingMatrix(params);
    console.info(`Succeeded in getting walking matrix. result is ${JSON.stringify(result)}`);
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(`Failed in getting walking matrix. Code is ${err.code}, message is ${err.message}`);
  }
}
```

### 骑行批量算路

根据多组起终点坐标批量检索符合条件的骑行路径规划方案。支持以下功能：

* 支持500km以内的骑行路径规划能力。
* 融入出行策略（时间最短、避免轮渡）。

**说明** 

为保证性能与准确性，单次请求中的起点数量乘以终点数量应小于100。

```typescript
async testCyclingMatrix() {
  let params: navi.MatrixParams = {
    // 起点的经纬度
    origins: [{
      latitude: 31.9844,
      longitude: 118.766253
    }, {
      latitude: 31.9644,
      longitude: 118.746253
    }],
    // 终点的经纬度
    destinations: [{
      latitude: 31.9344,
      longitude: 118.706253
    }],
    language: 'zh_CN'
  };
  try {
    const result = await navi.getCyclingMatrix(params);
    console.info(`Succeeded in getting cycling matrix. result is ${JSON.stringify(result)}`);
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(`Failed in getting cycling matrix. Code is ${err.code}, message is ${err.message}`);
  }
}
```
