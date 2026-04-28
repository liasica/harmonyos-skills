---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-wearable-healthsequence-manage
title: 读取健康记录
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > Wearable应用开发 > 管理运动健康数据 > 读取健康记录
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:923ec0d60ce21af27904989c870f4b05fcccdfab87850db1e53eaa54c9cb0c74
---

## 场景介绍

读取最新一条健康记录。

## 约束与限制

从5.1.1(19) Release版本开始支持。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [readData](../harmonyos-references/health-api-healthstore.md#healthstorereaddata-2)<T extends [HealthSequence](../harmonyos-references/health-api-healthstore.md#healthsequence)>(request: [HealthSequenceReadRequest](../harmonyos-references/health-api-healthstore.md#healthsequencereadrequest)): Promise<T[]> | 查询最新一条健康记录。 |

说明

当前HealthSequenceReadRequest里的时间参数暂不生效，仅支持返回手表侧最新一条数据。

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
2. 创建查询健康记录请求。

   ```
   1. let healthSequenceReadRequest: healthStore.HealthSequenceReadRequest = {
   2. healthSequenceDataType: healthStore.healthSequenceHelper.sleepRecord.DATA_TYPE,
   3. startTime: 1695740400000,
   4. endTime: 1695769200000,
   5. readOptions: {
   6. withDetails: true
   7. }
   8. }
   ```
3. 调用[readData](../harmonyos-references/health-api-healthstore.md#healthstorereaddata-2)方法执行查询请求，并处理返回结果。

   ```
   1. try {
   2. const healthSequences = await healthStore.readData(healthSequenceReadRequest);
   3. hilog.info(0x0000, 'testTag', 'Succeeded in reading data.');
   4. healthSequences.forEach((healthSequence) => {
   5. hilog.info(0x0000, 'testTag', `the start time is ${healthSequence.startTime}.`);
   6. hilog.info(0x0000, 'testTag', `the end time is ${healthSequence.endTime}.`);
   7. Object.keys(healthSequence.summaries).forEach((key) => {
   8. hilog.info(0x0000, 'testTag', `the summaries of ${key} is ${healthSequence.summaries[key]}.`);
   9. });
   10. });
   11. } catch (err) {
   12. hilog.error(0x0000, 'testTag', `Failed to read data. Code: ${err.code}, message: ${err.message}`);
   13. }
   ```
