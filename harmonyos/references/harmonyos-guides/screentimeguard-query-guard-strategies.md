---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-query-guard-strategies
title: 查询策略配置数据
breadcrumb: 指南 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > 守护策略管理 > 查询策略配置数据
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:32+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:9cb89bb00bb83831aac1071c35a64629bd1c03a97432271ba104b179cd232989
---

## 场景介绍

当管控应用希望查看已添加的所有管控策略时，可以调用查询管控策略的接口。调用成功后，管控应用可以查看所有已添加管控策略的配置数据，如查看被管控应用的停用时间或可使用时长。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/ia9zLH9nRZOqLy8VyAh4Bw/zh-cn_image_0000002736434347.png)

流程说明：

1. 应用调用查询管控策略的接口，拉起健康使用设备查询本应用是否已申请权限，以及用户是否对本应用授权。
2. 若开发者没有权限或用户没有授权，则抛出相应错误码。若开发者有权限且用户已授权，则返回对应应用下的所有管控策略。

## 接口说明

查询策略的关键接口如下表所示：

| 接口名 | 描述 |
| --- | --- |
| [queryGuardStrategies](../harmonyos-references/screentimeguard-guardservice.md#queryguardstrategies)(): Promise<[GuardStrategy](../harmonyos-references/screentimeguard-guardservice.md#guardstrategy)[]> | 查询该应用下的所有管控策略。 |

## 开发前提

查询管控策略需要申请用户授权，请先参考[请求用户授权](screentimeguard-request-user-auth.md)章节完成用户授权。

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { guardService } from '@kit.ScreenTimeGuardKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用queryGuardStrategies，查询对应应用下的所有管控策略。

   ```typescript
   private async isStrategyExist(strategyName: string): Promise<boolean> {
     try {
       let guardStrategies: guardService.GuardStrategy[] = await guardService.queryGuardStrategies();
       for (let i = 0; i < guardStrategies.length; i++) {
         if (guardStrategies[i].name === strategyName) {
           return true;
         }
       }
     } catch (error) {
       let err: BusinessError = error as BusinessError;
       hilog.error(0x0000, 'GuardService',
         `queryGuardStrategies failed, errCode is ${err.code}, errMessage is ${err.message}`);
     }
     return false;
   }
   ```
