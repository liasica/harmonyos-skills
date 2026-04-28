---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-samplepoint-manage
title: 运动健康采样数据
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > Phone/Tablet应用开发 > 管理运动健康数据 > 运动健康采样数据
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6a195bda31c7b3a7ea72cb2731ba82cc0ec279837e6bf18d9fc67e79f8f04f3f
---

## 场景介绍

运动健康采样数据(SamplePoint)，表示在某时刻（或一段时间）采集到的特定数据类型的样本，由时间、样本值及采样的数据源组成，支持保存、读取和删除等操作。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [saveData](../harmonyos-references/health-api-healthstore.md#healthstoresavedata)(sampleData: [SamplePoint](../harmonyos-references/health-api-healthstore.md#samplepoint)[] | [SamplePoint](../harmonyos-references/health-api-healthstore.md#samplepoint)): Promise<void> | 保存运动健康采样数据，入参为单个[SamplePoint](../harmonyos-references/health-api-healthstore.md#samplepoint)或[SamplePoint](../harmonyos-references/health-api-healthstore.md#samplepoint)数组。 |
| [readData](../harmonyos-references/health-api-healthstore.md#healthstorereaddata)<T extends [SamplePoint](../harmonyos-references/health-api-healthstore.md#samplepoint)>(request: [SamplePointReadRequest](../harmonyos-references/health-api-healthstore.md#samplepointreadrequest)): Promise<T[]> | 查询运动健康采样数据，通过[SamplePointReadRequest](../harmonyos-references/health-api-healthstore.md#samplepointreadrequest)设置查询条件，可按数据类型，字段、时间范围等条件查询。 |
| [deleteData](../harmonyos-references/health-api-healthstore.md#healthstoredeletedata-3)(samplePoint: [SamplePoint](../harmonyos-references/health-api-healthstore.md#samplepoint) | [SamplePoint](../harmonyos-references/health-api-healthstore.md#samplepoint)[]): Promise<void> | 删除运动健康采样数据，按入参删除指定的采样数据，可传入单个[SamplePoint](../harmonyos-references/health-api-healthstore.md#samplepoint)或[SamplePoint](../harmonyos-references/health-api-healthstore.md#samplepoint)数组。 |
| [deleteData](../harmonyos-references/health-api-healthstore.md#healthstoredeletedata)(request: [SamplePointDeleteRequest](../harmonyos-references/health-api-healthstore.md#samplepointdeleterequest) | [SamplePointDeleteRequest](../harmonyos-references/health-api-healthstore.md#samplepointdeleterequest)[]): Promise<void> | 删除运动健康采样数据，按[SamplePointDeleteRequest](../harmonyos-references/health-api-healthstore.md#samplepointdeleterequest)条件删除，可设置数据类型、时间范围、数据源等删除条件。 |
| [aggregateData](../harmonyos-references/health-api-healthstore.md#healthstoreaggregatedata)<T extends [AggregateResult](../harmonyos-references/health-api-healthstore.md#aggregateresult)>(request: [AggregateRequest](../harmonyos-references/health-api-healthstore.md#aggregaterequest) | [AggregateRequest](../harmonyos-references/health-api-healthstore.md#aggregaterequest)[]): Promise<T[]> | 聚合查询运动健康采样数据，通过[AggregateRequest](../harmonyos-references/health-api-healthstore.md#aggregaterequest)设置查询的数据类型、聚合策略。 |

说明

aggregateData接口读取今日日常活动数据，数据上报存在延时，读取实时日常活动数据建议使用[读取实时三环数据](health-three-ring-read.md)接口。

## 开发前检查

* 完成[申请运动健康服务](health-apply.md)与[配置Client ID](health-configuration-client-id.md)。
* 接口首次调用前，需先使用[init](../harmonyos-references/health-api-healthstore.md#healthstoreinit)方法进行初始化。
* 需先通过[用户授权](health-add-permissions.md#用户授权)接口引导用户授权，用户授权对应数据类型权限后，才有权限调用接口操作相关数据类型数据。
* 错误码请参考[ArkTS API错误码](../harmonyos-references/errorcode-healthservice.md)，常见问题请参考[Health Service Kit常见问题](health-faqs.md)。

## 开发步骤

### 保存用户的运动健康数据

1. 导入运动健康服务功能模块及相关公共模块。

   ```
   1. import { healthStore } from '@kit.HealthServiceKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 获取dataSourceId，参考[管理数据源](health-datasource-manage.md)，插入一个新的数据源或读取已有数据源。
3. 创建运动健康采样数据。

   ```
   1. let samplePoint: healthStore.samplePointHelper.bodyTemperature.Model = {
   2. dataType: healthStore.samplePointHelper.bodyTemperature.DATA_TYPE,
   3. startTime: 1698633801000,
   4. endTime: 1698633801000,
   5. localDate: '10/30/2023',
   6. timeZone: '+0800',
   7. modifiedTime: 1698633801000,
   8. // insertDataSource插入数据源接口返回的dataSourceId，或读取已有数据源的dataSourceId
   9. dataSourceId: 'xxx',
   10. fields: {
   11. bodyTemperature: 39
   12. }
   13. }
   ```
4. 调用[saveData](../harmonyos-references/health-api-healthstore.md#healthstoresavedata)方法执行保存数据请求，并处理返回结果。

   ```
   1. try {
   2. await healthStore.saveData(samplePoint);
   3. hilog.info(0x0000, 'testTag', 'Succeeded in saving data.');
   4. } catch (err) {
   5. hilog.error(0x0000, 'testTag', `Failed to save data. Code: ${err.code}, message: ${err.message}`);
   6. }
   ```

### 读取用户的运动健康数据

1. 导入运动健康服务功能模块及相关公共模块。

   ```
   1. import { healthStore } from '@kit.HealthServiceKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 创建查询请求。

   ```
   1. let samplePointReadRequest: healthStore.SamplePointReadRequest = {
   2. samplePointDataType: healthStore.samplePointHelper.bodyTemperature.DATA_TYPE,
   3. startTime: 1698633801000,
   4. endTime: 1698633801000,
   5. fields: {
   6. bodyTemperature: 39
   7. }
   8. }
   ```
3. 调用[readData](../harmonyos-references/health-api-healthstore.md#healthstorereaddata)方法执行查询请求，并处理返回结果。

   ```
   1. try {
   2. let samplePoints = await healthStore.readData(samplePointReadRequest);
   3. samplePoints.forEach((samplePoint) => {
   4. hilog.info(0x0000, 'testTag', `Succeeded in reading data, the bodyTemperature is ${samplePoint.fields.bodyTemperature}.`);
   5. });
   6. } catch (err) {
   7. hilog.error(0x0000, 'testTag', `Failed to read data. Code: ${err.code}, message: ${err.message}`);
   8. }
   ```

### 删除指定的运动健康采样数据

1. 导入运动健康服务功能模块及相关公共模块。

   ```
   1. import { healthStore } from '@kit.HealthServiceKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 查询待删除的运动健康采样数据。

   ```
   1. let samplePointReadRequest: healthStore.SamplePointReadRequest = {
   2. samplePointDataType: healthStore.samplePointHelper.bodyTemperature.DATA_TYPE,
   3. startTime: 1698633801000,
   4. endTime: 1698633801000
   5. }
   6. let samplePoints: healthStore.SamplePoint[] = await healthStore.readData(samplePointReadRequest);
   ```
3. 调用[deleteData](../harmonyos-references/health-api-healthstore.md#healthstoredeletedata-3)方法执行删除请求，并处理返回结果。

   ```
   1. try {
   2. for (let index = 0; index < samplePoints.length; index++) {
   3. const samplePoint = samplePoints[index];
   4. await healthStore.deleteData(samplePoint);
   5. }
   6. hilog.info(0x0000, 'testTag', 'Succeeded in deleting data.');
   7. } catch (err) {
   8. hilog.error(0x0000, 'testTag', `Failed to delete data. Code: ${err.code}, message: ${err.message}`);
   9. }
   ```

### 根据请求删除用户运动健康数据

1. 导入运动健康服务功能模块及相关公共模块。

   ```
   1. import { healthStore } from '@kit.HealthServiceKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 创建删除请求。

   ```
   1. let samplePointDeleteRequest: healthStore.SamplePointDeleteRequest = {
   2. dataType: healthStore.samplePointHelper.bodyTemperature.DATA_TYPE,
   3. startTime: 1698633801000,
   4. endTime: 1698633801000
   5. }
   ```
3. 调用[deleteData](../harmonyos-references/health-api-healthstore.md#healthstoredeletedata-3)方法执行删除请求，并处理返回结果。

   ```
   1. try {
   2. await healthStore.deleteData(samplePointDeleteRequest);
   3. hilog.info(0x0000, 'testTag', 'Succeeded in deleting data.');
   4. } catch (err) {
   5. hilog.error(0x0000, 'testTag', `Failed to delete data. Code: ${err.code}, message: ${err.message}`);
   6. }
   ```

### 聚合查询

1. 导入运动健康服务功能模块及相关公共模块。

   ```
   1. import { healthStore } from '@kit.HealthServiceKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 创建聚合查询请求。

   ```
   1. let aggregateRequest: healthStore.AggregateRequest<healthStore.samplePointHelper.dailyActivities.AggregateFields> = {
   2. dataType: healthStore.samplePointHelper.dailyActivities.DATA_TYPE,
   3. metrics: {
   4. step: ['sum'],
   5. calorie: ['sum'],
   6. distance: ['sum'],
   7. climbHighAltitude:['sum'],
   8. isIntensity: ['sum'],
   9. isStand: ['sum']
   10. },
   11. groupBy: {
   12. unitType: healthStore.GroupUnitType.DAY
   13. },
   14. startLocalDate: '10/30/2023',
   15. endLocalDate: '10/30/2023'
   16. }
   ```
3. 调用[aggregateData](../harmonyos-references/health-api-healthstore.md#healthstoreaggregatedata)方法执行查询请求，并处理返回结果。

   ```
   1. try {
   2. const aggregateResults = await healthStore.aggregateData<healthStore.samplePointHelper.dailyActivities.AggregateResult>(aggregateRequest);
   3. hilog.info(0x0000, 'testTag', 'Succeeded in reading data.');
   4. aggregateResults.forEach((aggregateResult) => {
   5. hilog.info(0x0000, 'testTag', `the start time is ${aggregateResult.startTime}.`);
   6. hilog.info(0x0000, 'testTag', `the end time is ${aggregateResult.endTime}.`);
   7. Object.keys(aggregateResult.fields).forEach((fieldName) => {
   8. hilog.info(0x0000, 'testTag', `the sum of ${fieldName} is ${aggregateResult.fields[fieldName].sum}.`);
   9. });
   10. });
   11. } catch (err) {
   12. hilog.error(0x0000, 'testTag', `Failed to read data. Code: ${err.code}, message: ${err.message}`);
   13. }
   ```
