---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-wearable-healthsequence-manage
title: 读取健康记录
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > Wearable应用开发 > 管理运动健康数据 > 读取健康记录
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:08+08:00
doc_updated_at: 2026-09-04
content_hash: sha256:08e5b979ad2ae96b2145bea95b3815cceb4c63baafc9243eeeb1ef4ba15afeec
---

## 场景介绍

从5.1.1(19) Release版本开始，支持读取最新一条健康记录。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [readData](../harmonyos-references/health-api-healthstore.md#healthstorereaddata-2)<T extends [HealthSequence](../harmonyos-references/health-api-healthstore.md#healthsequence)>(request: [HealthSequenceReadRequest](../harmonyos-references/health-api-healthstore.md#healthsequencereadrequest)): Promise<T[]> | 查询最新一条健康记录。 |

**说明** 

当前HealthSequenceReadRequest里的时间参数暂不生效，仅支持返回手表侧最新一条数据。

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
