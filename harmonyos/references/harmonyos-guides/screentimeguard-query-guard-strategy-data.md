---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-query-guard-strategy-data
title: 查询策略运行数据
breadcrumb: 指南 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > 守护策略管理 > 查询策略运行数据
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:02+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:bc1f69e40c9eeeec4bb4b83b0329fea48fcb7d3cd99b981afe02e8997021f424
---

## 场景介绍

从26.0.0版本开始，Screen Time Guard Kit新增支持查询管控策略运行数据，运行数据包括策略的已使用时长。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/v2X_fHApTW-XNO6pqprtnQ/zh-cn_image_0000002706835200.png)

流程说明：

1. 应用调用查询策略运行数据的接口，拉起健康使用设备查询本应用是否已申请权限，以及用户是否对本应用授权。
2. 若开发者没有权限或用户没有授权，则抛出相应错误码。若开发者有权限且用户已授权，则解析参数中传入的策略名称，判断策略是否存在。
3. 若策略不存在，则抛出相应错误码；若存在，则查询该策略类型是否为[INCLUSIVE\_DURATION\_TYPE](../harmonyos-references/screentimeguard-guardservice.md#timestrategytype)。
4. 若策略类型不是INCLUSIVE\_DURATION\_TYPE，则抛出相应错误码；若策略类型是INCLUSIVE\_DURATION\_TYPE，则查询该策略是否正在执行。
5. 若策略未在执行中，则抛出相应错误码；若策略正在执行，查询并返回该策略下应用的使用时长。

## 接口说明

查询策略运行数据的关键接口如下表所示：

| 接口名 | 描述 |
| --- | --- |
| [queryGuardStrategyData](../harmonyos-references/screentimeguard-guardservice.md#queryguardstrategydata)(strategyName: string): Promise<[GuardStrategyData](../harmonyos-references/screentimeguard-guardservice.md#guardstrategydata)> | 查询该管控策略的运行数据。 |

**说明** 

目前仅支持查询[INCLUSIVE\_DURATION\_TYPE](../harmonyos-references/screentimeguard-guardservice.md#timestrategytype)类型的策略运行数据。

## 开发前提

查询策略运行数据需要申请用户授权，请先参考[请求用户授权](screentimeguard-request-user-auth.md)章节完成用户授权。

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { guardService } from '@kit.ScreenTimeGuardKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用queryGuardStrategyData，查询对应管控策略的运行数据。

   ```typescript
   private async getStrategyData(strategyName: string): Promise<guardService.GuardStrategyData> {
     let usageData: guardService.GuardStrategyData = { usageDuration: 0 };
     try {
       // 查询策略类型为INCLUSIVE_DURATION_TYPE策略的已使用时长.
       usageData = await guardService.queryGuardStrategyData(strategyName);
     } catch (error) {
       let err: BusinessError = error as BusinessError;
       hilog.error(0x0000, 'GuardService',
         `queryGuardStrategyData failed, errCode is ${err.code}, errMessage is ${err.message}`);
     }
     return usageData;
   }
   ```
