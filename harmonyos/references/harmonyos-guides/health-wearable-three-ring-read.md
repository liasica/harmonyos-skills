---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-wearable-three-ring-read
title: 实时三环数据
breadcrumb: 指南 > 应用服务 > Health Service Kit（运动健康服务） > 开发接入 > Wearable应用开发 > 管理运动健康数据 > 实时三环数据
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:14415f69353abacf5f37814091e02ff006ed7e0328d925ce21b3cb579f6b88c4
---

## 场景介绍

实时三环数据，包括实时步数，活动热量，锻炼时长，活动小时数以及目标类数据。

说明

此接口使用日常活动数据类型读权限，参考[权限说明](health-permission-description.md)。

## 约束与限制

从5.1.1(19) Release版本开始支持。

## OAuth权限

联盟卡片申请的权限名称：日常活动 > 日常活动数据（读）

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| [readActivityReport](../harmonyos-references/health-api-healthservice.md#workoutreadactivityreport)(): Promise<[ActivityReport](../harmonyos-references/health-api-healthservice.md#activityreport)> | 读取实时三环数据。 |

## 开发前检查

* 完成[申请运动健康服务](health-apply.md)与[配置Client ID](health-configuration-client-id.md)。
* 接口首次调用前，需先使用[init](../harmonyos-references/health-api-healthstore.md#healthstoreinit)方法进行初始化。
* 需先通过[用户授权](health-add-permissions.md#用户授权)接口引导用户授权，用户授权日常活动数据类型读权限（参考[权限说明](health-permission-description.md)）后，才有权限读取实时三环数据。
* 错误码请参考[ArkTS API错误码](../harmonyos-references/errorcode-healthservice.md)，常见问题请参考[Health Service Kit常见问题](health-faqs.md)。

## 开发步骤

1. 导入运动健康服务功能模块及相关公共模块。

   ```
   1. import { healthService } from '@kit.HealthServiceKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 调用[readActivityReport](../harmonyos-references/health-api-healthservice.md#workoutreadactivityreport)方法读取实时三环数据，并处理返回结果。

   ```
   1. try {
   2. const result: healthService.workout.ActivityReport = await healthService.workout.readActivityReport();

   4. hilog.info(0x0000, 'testTag', 'Succeeded in reading ActivityReport');
   5. Object.keys(result).forEach(key => {
   6. hilog.info(0x0000, 'testTag', `the ${key} is ${result[key]}`);
   7. });
   8. } catch(err) {
   9. hilog.error(0x0000, 'testTag', `Failed to read ActivityReport. Code: ${err.code}, message: ${err.message}`);
   10. }
   ```
