---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-wearable-samplepoint-manage
title: 读取运动健康采样数据
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > Wearable应用开发 > 管理运动健康数据 > 读取运动健康采样数据
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9a9509236c6d10d7f832d4ba9817c11a781a6e18994800cbad54e761f081fb07
---

## 场景介绍

读取最新一条运动健康采样数据。

## 约束与限制

从5.1.1(19) Release版本开始支持。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [readData](../harmonyos-references/health-api-healthstore.md#healthstorereaddata)<T extends [SamplePoint](../harmonyos-references/health-api-healthstore.md#samplepoint)>(request: [SamplePointReadRequest](../harmonyos-references/health-api-healthstore.md#samplepointreadrequest)): Promise<T[]> | 查询最新一条运动健康采样数据。 |

说明

当前SamplePointReadRequest里的时间参数暂不生效，仅支持返回手表侧最新一条数据，读取实时日常活动数据使用[读取实时三环数据](health-wearable-three-ring-read.md)接口。

## 开发前检查

* 完成[申请运动健康服务](health-apply.md)与[配置Client ID](health-configuration-client-id.md)。
* 接口首次调用前，需先使用[init](../harmonyos-references/health-api-healthstore.md#healthstoreinit)方法进行初始化。
* 需先通过[用户授权](health-add-permissions.md#用户授权)接口引导用户授权，用户授权对应数据类型权限后，才有权限调用接口操作相关数据类型数据。
* 错误码请参考[ArkTS API错误码](../harmonyos-references/errorcode-healthservice.md)，常见问题请参考[Health Service Kit常见问题](health-faqs.md)。

## 开发步骤

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
