---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-healthsequence-manage
title: 健康记录
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > Phone/Tablet应用开发 > 管理运动健康数据 > 健康记录
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:18b71bdf0e4c5355bcebcd13084df32cf7eb2032e00b55d13f8b07b7e2ff0714
---

## 场景介绍

健康记录，记录健康记录的基本信息，包括健康记录的起止时间，数据类型，字段值，明细数据等，支持写入、读取和删除，每条健康记录需要关联数据源。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [saveData](../harmonyos-references/health-api-healthstore.md#healthstoresavedata-2)(healthSequence: [HealthSequence](../harmonyos-references/health-api-healthstore.md#healthsequence)[] | [HealthSequence](../harmonyos-references/health-api-healthstore.md#healthsequence)): Promise<void> | 保存健康记录，入参为单个[HealthSequence](../harmonyos-references/health-api-healthstore.md#healthsequence)或[HealthSequence](../harmonyos-references/health-api-healthstore.md#healthsequence)数组。 |
| [readData](../harmonyos-references/health-api-healthstore.md#healthstorereaddata-2)<T extends [HealthSequence](../harmonyos-references/health-api-healthstore.md#healthsequence)>(request: [HealthSequenceReadRequest](../harmonyos-references/health-api-healthstore.md#healthsequencereadrequest)): Promise<T[]> | 查询健康记录，通过[HealthSequenceReadRequest](../harmonyos-references/health-api-healthstore.md#healthsequencereadrequest)设置查询条件，可按数据类型，字段、时间范围等条件查询。 |
| [deleteData](../harmonyos-references/health-api-healthstore.md#healthstoredeletedata-5)(healthSequence: [HealthSequence](../harmonyos-references/health-api-healthstore.md#healthsequence) | [HealthSequence](../harmonyos-references/health-api-healthstore.md#healthsequence)[]): Promise<void> | 删除健康记录，按入参删除指定的健康记录，可传入单个[HealthSequence](../harmonyos-references/health-api-healthstore.md#healthsequence)或[HealthSequence](../harmonyos-references/health-api-healthstore.md#healthsequence)数组。 |
| [deleteData](../harmonyos-references/health-api-healthstore.md#healthstoredeletedata-2)(request: [HealthSequenceDeleteRequest](../harmonyos-references/health-api-healthstore.md#healthsequencedeleterequest) | [HealthSequenceDeleteRequest](../harmonyos-references/health-api-healthstore.md#healthsequencedeleterequest)[]): Promise<void> | 删除健康记录，按[HealthSequenceDeleteRequest](../harmonyos-references/health-api-healthstore.md#healthsequencedeleterequest)删除，可设置数据类型、时间范围、数据源等删除条件。 |

## 开发前检查

* 完成[申请运动健康服务](health-apply.md)与[配置Client ID](health-configuration-client-id.md)。
* 接口首次调用前，需先使用[init](../harmonyos-references/health-api-healthstore.md#healthstoreinit)方法进行初始化。
* 需先通过[用户授权](health-add-permissions.md#用户授权)接口引导用户授权，用户授权对应数据类型权限后，才有权限调用接口操作相关数据类型数据。
* 错误码请参考[ArkTS API错误码](../harmonyos-references/errorcode-healthservice.md)，常见问题请参考[Health Service Kit常见问题](health-faqs.md)。

## 开发步骤

### 保存用户的健康记录

1. 导入运动健康服务功能模块及相关公共模块。

   ```typescript
   import { healthStore } from '@kit.HealthServiceKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 获取dataSourceId，参考[管理数据源](health-datasource-manage.md)，插入一个新的数据源或读取已有数据源。
3. 创建健康记录。

   ```typescript
   let healthSequence: healthStore.healthSequenceHelper.sleepRecord.Model = {
     summaries: {
       fallAsleepTime: 1695740400000, // 2023-09-26 23:00:00
       wakeupTime: 1695769200000, // 2023-09-27 7:00:00
       sleepScore: 80,
       wakeCount: 2,
       sleepType: 1,
       shallowDuration: 14400,
       deepDuration: 7200,
       dreamDuration: 7200,
       wakeDuration: 0,
       duration: 28800
     },
     dataType: healthStore.healthSequenceHelper.sleepRecord.DATA_TYPE,
     // insertDataSource插入数据源接口返回的dataSourceId，或读取已有数据源的dataSourceId
     dataSourceId: 'xxx',
     localDate: '09/26/2023',
     startTime: 1695740400000,
     endTime: 1695769200000,
     timeZone: '+0800',
     modifiedTime: 1695769200000,
     details: {
       sleepSegment: [
         {
           startTime: 1695740400000, // 2023-09-26 23:00:00
           endTime: 1695747600000, // 2023-09-27 01:00:00
           sleepStatus: 2
         },
         {
           startTime: 1695747600000, // 2023-09-27 01:00:00
           endTime: 1695754800000, // 2023-09-27 03:00:00
           sleepStatus: 1
         },
         {
           startTime: 1695754800000, // 2023-09-27 03:00:00
           endTime: 1695762000000, // 2023-09-27 05:00:00
           sleepStatus: 3
         },
         {
           startTime: 1695762000000, // 2023-09-27 05:00:00
           endTime: 1695769200000, // 2023-09-27 07:00:00
           sleepStatus: 2
         }
       ]
     }
   }
   ```
4. 调用[saveData](../harmonyos-references/health-api-healthstore.md#healthstoresavedata-2)方法执行保存数据请求，并处理返回结果。

   ```typescript
   try {
     await healthStore.saveData(healthSequence);
     hilog.info(0x0000, 'testTag', 'Succeeded in saving data.');
   } catch (err) {
     hilog.error(0x0000, 'testTag', `Failed to save data. Code: ${err.code}, message: ${err.message}`);
   }
   ```

### 读取用户的健康记录

1. 导入运动健康服务功能模块及相关公共模块。

   ```typescript
   import { healthStore } from '@kit.HealthServiceKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 创建查询健康记录请求。

   ```typescript
   let healthSequenceReadRequest: healthStore.HealthSequenceReadRequest = {
     healthSequenceDataType: healthStore.healthSequenceHelper.sleepRecord.DATA_TYPE,
     startTime: 1695740400000,
     endTime: 1695769200000,
     readOptions: {
       withDetails: true
     }
   }
   ```
3. 调用[readData](../harmonyos-references/health-api-healthstore.md#healthstorereaddata-2)方法执行查询请求，并处理返回结果。

   ```typescript
   try {
     const healthSequences = await healthStore.readData(healthSequenceReadRequest);
     hilog.info(0x0000, 'testTag', 'Succeeded in reading data.');
     healthSequences.forEach((healthSequence) => {
       hilog.info(0x0000, 'testTag', `the start time is ${healthSequence.startTime}.`);
       hilog.info(0x0000, 'testTag', `the end time is ${healthSequence.endTime}.`);
       Object.keys(healthSequence.summaries).forEach((key) => {
         hilog.info(0x0000, 'testTag', `the summaries of ${key} is ${healthSequence.summaries[key]}.`);
       });
     });
   } catch (err) {
     hilog.error(0x0000, 'testTag', `Failed to read data. Code: ${err.code}, message: ${err.message}`);
   }
   ```

### 删除指定的健康记录

1. 导入运动健康服务功能模块及相关公共模块。

   ```typescript
   import { healthStore } from '@kit.HealthServiceKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 查询待删除健康记录。

   ```typescript
   let healthSequenceReadRequest: healthStore.HealthSequenceReadRequest = {
     healthSequenceDataType: healthStore.healthSequenceHelper.sleepRecord.DATA_TYPE,
     startTime: 1695740400000,
     endTime: 1695769200000
   }
   const healthSequences = await healthStore.readData(healthSequenceReadRequest);
   ```
3. 调用[deleteData](../harmonyos-references/health-api-healthstore.md#healthstoredeletedata-5)方法执行删除请求，并处理返回结果。

   ```typescript
   try {
     for (let index = 0; index < healthSequences.length; index++) {
       const healthSequence = healthSequences[index];
       await healthStore.deleteData(healthSequence);
     }
     hilog.info(0x0000, 'testTag', 'Succeeded in deleting data.');
   } catch (err) {
     hilog.error(0x0000, 'testTag', `Failed to delete data. Code: ${err.code}, message: ${err.message}`);
   }
   ```

### 根据请求删除用户健康记录

1. 导入运动健康服务功能模块及相关公共模块。

   ```typescript
   import { healthStore } from '@kit.HealthServiceKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 创建删除健康记录请求。

   ```typescript
   const healthSequenceDeleteRequest: healthStore.HealthSequenceDeleteRequest= {
     healthSequenceDataType: healthStore.healthSequenceHelper.sleepRecord.DATA_TYPE,
     startTime: 1695740400000,
     endTime: 1695769200000
   }
   ```
3. 调用[deleteData](../harmonyos-references/health-api-healthstore.md#healthstoredeletedata-2)方法执行删除请求，并处理返回结果。

   ```typescript
   try {
     await healthStore.deleteData(healthSequenceDeleteRequest);
     hilog.info(0x0000, 'testTag', 'Succeeded in deleting data.');
   } catch (err) {
     hilog.error(0x0000, 'testTag', `Failed to delete data. Code: ${err.code}, message: ${err.message}`);
   }
   ```
