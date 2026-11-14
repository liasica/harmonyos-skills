---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-wearable-exercisesequence-manage
title: 管理锻炼记录数据
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 应用开发 > Wearable应用开发 > 管理运动健康数据 > 管理锻炼记录数据
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:20+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:b78d44fddda3d872f2eb79311e4c1f8b8d6449fefc2807e3c23fb018b726d7c6
---

## 场景介绍

从5.1.1(19) Release版本开始，支持读取最新一条锻炼记录。

从26.0.1 版本开始，支持保存单条锻炼记录。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [saveData](../harmonyos-references/health-api-healthstore.md#healthstoresavedata-1)(exerciseSequence: [ExerciseSequence](../harmonyos-references/health-api-healthstore.md#exercisesequence)[] | [ExerciseSequence](../harmonyos-references/health-api-healthstore.md#exercisesequence)): Promise<void> | 保存锻炼记录，入参为单个[ExerciseSequence](../harmonyos-references/health-api-healthstore.md#exercisesequence)或[ExerciseSequence](../harmonyos-references/health-api-healthstore.md#exercisesequence)数组。 |
| [readData](../harmonyos-references/health-api-healthstore.md#healthstorereaddata-1)<T extends [ExerciseSequence](../harmonyos-references/health-api-healthstore.md#exercisesequence)>(request: [ExerciseSequenceReadRequest](../harmonyos-references/health-api-healthstore.md#exercisesequencereadrequest)): Promise<T[]> | 查询最新一条锻炼记录。 |

**说明** 

当前ExerciseSequenceReadRequest里的时间参数暂不生效，仅支持返回手表侧最新一条数据。

## 开发前检查

* 完成[申请运动健康服务](health-apply.md)与[配置Client ID](health-configuration-client-id.md)。
* 接口首次调用前，需先使用[init](../harmonyos-references/health-api-healthstore.md#healthstoreinit)方法进行初始化。
* 需先通过[用户授权](health-add-permissions.md#用户授权)接口引导用户授权，用户授权对应数据类型权限后，才有权限调用接口操作相关数据类型数据。
* 错误码请参考[ArkTS API错误码](../harmonyos-references/errorcode-healthservice.md)，常见问题请参考[Health Service Kit常见问题](health-faqs.md)。

## 开发步骤

1. 导入运动健康服务功能模块及相关公共模块。

   ```typescript
   import { healthStore } from '@kit.HealthServiceKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 创建查询请求。

   ```typescript
   // 查询跑步记录
   const sequenceReadRequest:
     healthStore.ExerciseSequenceReadRequest<healthStore.exerciseSequenceHelper.running.DetailFields> = {
     startTime: 1698040800000,
     endTime: 1698042600000,
     exerciseType: healthStore.exerciseSequenceHelper.running.EXERCISE_TYPE,
     count: 1,
     sortOrder: 1,
     readOptions: {
       withPartialDetails: ['exerciseHeartRate', 'altitude']
     }
   };
   ```
3. 调用[readData](../harmonyos-references/health-api-healthstore.md#healthstorereaddata-1)方法执行查询请求，并处理返回结果。

   ```typescript
   try {
     const runningSequences =
       await healthStore.readData<healthStore.exerciseSequenceHelper.running.Model>(sequenceReadRequest);
     hilog.info(0x0000, 'testTag', 'Succeeded in reading data.');
     runningSequences.forEach((runningSequence) => {
       hilog.info(0x0000, 'testTag', `the start time is ${runningSequence.startTime}.`);
       hilog.info(0x0000, 'testTag', `the end time is ${runningSequence.endTime}.`);
       Object.keys(runningSequence.summaries).forEach((key) => {
         Object.keys(runningSequence.summaries[key]).forEach((fieldName) => {
           hilog.info(0x0000, 'testTag',
             `the summaries of ${key} field ${fieldName} is ${runningSequence.summaries[key][fieldName]}.`);
         });
       });
     });
   } catch (err) {
     hilog.error(0x0000, 'testTag', `Failed to read data. Code: ${err.code}, message: ${err.message}`);
   }
   ```
4. 调用[saveData](../harmonyos-references/health-api-healthstore.md#healthstoresavedata-1)方法执行保存数据请求，并处理返回结果。

   ```typescript
   try {
     await healthStore.saveData(runningSequence);
     hilog.info(0x0000, 'testTag', 'Succeeded in saving data.');
   } catch (err) {
     hilog.error(0x0000, 'testTag', `Failed to save data. Code: ${err.code}, message: ${err.message}`);
   }
   ```
