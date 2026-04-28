---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-exercisesequence-manage
title: 锻炼记录
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > Phone/Tablet应用开发 > 管理运动健康数据 > 锻炼记录
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:46ed6c4a9628bafca2a062b30c0c713339f581beb28454bad108501da89d63fa
---

## 场景介绍

锻炼记录，记录用户一次活动的基本信息，包括锻炼的起止时间，运动类型，统计数据，详情数据等，支持写入、读取和删除，每条锻炼记录数据需要关联数据源。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [saveData](../harmonyos-references/health-api-healthstore.md#healthstoresavedata-1)(exerciseSequence: [ExerciseSequence](../harmonyos-references/health-api-healthstore.md#exercisesequence)[] | [ExerciseSequence](../harmonyos-references/health-api-healthstore.md#exercisesequence)): Promise<void> | 保存锻炼记录，入参为单个[ExerciseSequence](../harmonyos-references/health-api-healthstore.md#exercisesequence)或[ExerciseSequence](../harmonyos-references/health-api-healthstore.md#exercisesequence)数组。 |
| [readData](../harmonyos-references/health-api-healthstore.md#healthstorereaddata-1)<T extends [ExerciseSequence](../harmonyos-references/health-api-healthstore.md#exercisesequence)>(request: [ExerciseSequenceReadRequest](../harmonyos-references/health-api-healthstore.md#exercisesequencereadrequest)): Promise<T[]> | 查询锻炼记录，通过[ExerciseSequenceReadRequest](../harmonyos-references/health-api-healthstore.md#exercisesequencereadrequest)设置查询条件，可按数据类型，字段、时间范围等条件查询。 |
| [deleteData](../harmonyos-references/health-api-healthstore.md#healthstoredeletedata-4)(exerciseSequence: [ExerciseSequence](../harmonyos-references/health-api-healthstore.md#exercisesequence) | [ExerciseSequence](../harmonyos-references/health-api-healthstore.md#exercisesequence)[]): Promise<void> | 删除锻炼记录，按入参删除指定的锻炼记录，可传入单个[ExerciseSequence](../harmonyos-references/health-api-healthstore.md#exercisesequence)或[ExerciseSequence](../harmonyos-references/health-api-healthstore.md#exercisesequence)数组。 |
| [deleteData](../harmonyos-references/health-api-healthstore.md#healthstoredeletedata-1)(request: [ExerciseSequenceDeleteRequest](../harmonyos-references/health-api-healthstore.md#exercisesequencedeleterequest) | [ExerciseSequenceDeleteRequest](../harmonyos-references/health-api-healthstore.md#exercisesequencedeleterequest)[]): Promise<void> | 删除锻炼记录，按[ExerciseSequenceDeleteRequest](../harmonyos-references/health-api-healthstore.md#exercisesequencedeleterequest)删除，可设置数据类型、时间范围、数据源等删除条件。 |

## 开发前检查

* 完成[申请运动健康服务](health-apply.md)与[配置Client ID](health-configuration-client-id.md)。
* 接口首次调用前，需先使用[init](../harmonyos-references/health-api-healthstore.md#healthstoreinit)方法进行初始化。
* 需先通过[用户授权](health-add-permissions.md#用户授权)接口引导用户授权，用户授权对应数据类型权限后，才有权限调用接口操作相关数据类型数据。
* 错误码请参考[ArkTS API错误码](../harmonyos-references/errorcode-healthservice.md)，常见问题请参考[Health Service Kit常见问题](health-faqs.md)。

## 开发步骤

### 保存用户的锻炼记录

1. 导入运动健康服务功能模块及相关公共模块。

   ```
   1. import { healthStore } from '@kit.HealthServiceKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 获取dataSourceId，参考[管理数据源](health-datasource-manage.md)，插入一个新的数据源或读取已有数据源。
3. 创建锻炼记录。

   ```
   1. // 构造跑步记录
   2. const startTime = 1698040800000; // 2023-10-23 14:00:00
   3. const endTime = 1698042600000; // 2023-10-23 14:30:00

   5. const runningSequence: healthStore.exerciseSequenceHelper.running.Model = {
   6. dataType: healthStore.exerciseSequenceHelper.DATA_TYPE,
   7. // insertDataSource插入数据源接口返回的dataSourceId，或读取已有数据源的dataSourceId
   8. dataSourceId: 'xxx',
   9. startTime: startTime, // 2023-10-23 14:00:00
   10. endTime: endTime, // 2023-10-23 14:30:00
   11. localDate: '10/23/2023',
   12. timeZone: '+0800',
   13. modifiedTime: new Date().getTime(),
   14. exerciseType: healthStore.exerciseSequenceHelper.running.EXERCISE_TYPE,
   15. duration: 1800,
   16. summaries: {
   17. distance: {
   18. totalDistance: 2000
   19. },
   20. calorie: {
   21. totalCalories: 20
   22. },
   23. speed: {
   24. avg: 5,
   25. max: 6
   26. }
   27. },
   28. details: {
   29. exerciseHeartRate: [
   30. {
   31. startTime: startTime,
   32. bpm: 88
   33. },
   34. {
   35. startTime: startTime + 5000,
   36. bpm: 89
   37. }
   38. ],
   39. speed: [
   40. {
   41. startTime: startTime,
   42. speed: 2.5
   43. },
   44. {
   45. startTime: startTime + 5000,
   46. speed: 2.3
   47. }
   48. ],
   49. altitude: [
   50. {
   51. startTime: startTime,
   52. altitude: 100
   53. },
   54. {
   55. startTime: startTime + 5000,
   56. altitude: 101
   57. }
   58. ]
   59. }
   60. };
   ```
4. 调用[saveData](../harmonyos-references/health-api-healthstore.md#healthstoresavedata-1)方法执行保存数据请求，并处理返回结果。

   ```
   1. try {
   2. await healthStore.saveData(runningSequence);
   3. hilog.info(0x0000, 'testTag', 'Succeeded in saving data.');
   4. } catch (err) {
   5. hilog.error(0x0000, 'testTag', `Failed to save data. Code: ${err.code}, message: ${err.message}`);
   6. }
   ```

### 读取用户的锻炼记录

1. 导入运动健康服务功能模块及相关公共模块。

   ```
   1. import { healthStore } from '@kit.HealthServiceKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 创建查询请求。

   ```
   1. // 查询跑步记录
   2. const sequenceReadRequest: healthStore.ExerciseSequenceReadRequest<healthStore.exerciseSequenceHelper.running.DetailFields> = {
   3. startTime: 1698040800000,
   4. endTime: 1698042600000,
   5. exerciseType: healthStore.exerciseSequenceHelper.running.EXERCISE_TYPE,
   6. count: 1,
   7. sortOrder: 1,
   8. readOptions: {
   9. withPartialDetails: ['exerciseHeartRate', 'altitude']
   10. }
   11. };
   ```
3. 调用[readData](../harmonyos-references/health-api-healthstore.md#healthstorereaddata-1)方法执行查询请求，并处理返回结果。

   ```
   1. try {
   2. const runningSequences = await healthStore.readData<healthStore.exerciseSequenceHelper.running.Model>(sequenceReadRequest);
   3. hilog.info(0x0000, 'testTag', 'Succeeded in reading data.');
   4. runningSequences.forEach((runningSequence) => {
   5. hilog.info(0x0000, 'testTag', `the start time is ${runningSequence.startTime}.`);
   6. hilog.info(0x0000, 'testTag', `the end time is ${runningSequence.endTime}.`);
   7. Object.keys(runningSequence.summaries).forEach((key) => {
   8. Object.keys(runningSequence.summaries[key]).forEach((fieldName) => {
   9. hilog.info(0x0000, 'testTag', `the summaries of ${key} field ${fieldName} is ${runningSequence.summaries[key][fieldName]}.`);
   10. });
   11. });
   12. });
   13. } catch (err) {
   14. hilog.error(0x0000, 'testTag', `Failed to read data. Code: ${err.code}, message: ${err.message}`);
   15. }
   ```

### 删除指定的锻炼记录

1. 导入运动健康服务功能模块及相关公共模块。

   ```
   1. import { healthStore } from '@kit.HealthServiceKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 查询待删除的锻炼记录。

   ```
   1. // 查询跑步记录
   2. const sequenceReadRequest: healthStore.ExerciseSequenceReadRequest<healthStore.exerciseSequenceHelper.running.DetailFields> = {
   3. startTime: 1698040800000,
   4. endTime: 1698042600000,
   5. exerciseType: healthStore.exerciseSequenceHelper.running.EXERCISE_TYPE
   6. };
   7. const runningSequences = await healthStore.readData<healthStore.exerciseSequenceHelper.running.Model>(sequenceReadRequest);
   ```
3. 调用[deleteData](../harmonyos-references/health-api-healthstore.md#healthstoredeletedata-4)方法执行删除请求，并处理返回结果。

   ```
   1. try {
   2. for (let index = 0; index < runningSequences.length; index++) {
   3. const runningSequence = runningSequences[index];
   4. await healthStore.deleteData(runningSequence);
   5. }
   6. hilog.info(0x0000, 'testTag', 'Succeeded in deleting data.');
   7. } catch (err) {
   8. hilog.error(0x0000, 'testTag', `Failed to delete data. Code: ${err.code}, message: ${err.message}`);
   9. }
   ```

### 根据请求删除用户锻炼记录

1. 导入运动健康服务功能模块及相关公共模块。

   ```
   1. import { healthStore } from '@kit.HealthServiceKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 创建删除请求。

   ```
   1. let exerciseSequenceDeleteRequest: healthStore.ExerciseSequenceDeleteRequest= {
   2. exerciseType: healthStore.exerciseSequenceHelper.running.EXERCISE_TYPE,
   3. startTime: 1698633801000,
   4. endTime: 1698633801000
   5. }
   ```
3. 调用[deleteData](../harmonyos-references/health-api-healthstore.md#healthstoredeletedata-1)方法执行删除请求，并处理返回结果。

   ```
   1. try {
   2. await healthStore.deleteData(exerciseSequenceDeleteRequest);
   3. hilog.info(0x0000, 'testTag', 'Succeeded in deleting data.');
   4. } catch (err) {
   5. hilog.error(0x0000, 'testTag', `Failed to delete data. Code: ${err.code}, message: ${err.message}`);
   6. }
   ```
