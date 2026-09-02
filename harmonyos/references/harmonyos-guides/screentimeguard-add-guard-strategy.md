---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-add-guard-strategy
title: 添加策略
breadcrumb: 指南 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > 守护策略管理 > 添加策略
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:02+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:f0ba52f8c5da1c60ef15c2161e05b260ff50916ca1bb25d30265c03014e94181
---

## 场景介绍

当管控应用希望创建新的屏幕时间守护规则时，可以调用添加管控策略的接口。根据参数中传入的策略设置指定应用的停用时间。一旦策略被创建并启用，系统将根据策略规则对用户的屏幕使用行为进行管控。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/et4CdnKeS8O39HIXTUB1Ww/zh-cn_image_0000002736314301.png)

流程说明：

1. 应用调用添加管控策略的接口，拉起健康使用设备查询本应用是否已申请权限，以及用户是否已给本应用授权。
2. 若开发者没有权限或用户没有授权，则抛出相应错误码。若开发者有权限且用户已授权，则解析参数中传入的策略，判断策略是否有效、是否重复、数量是否超限。
3. 若策略正常，则记录到本地数据库；否则，抛出相应错误码。

**说明** 

1. 管控策略可以设置为起止时间策略，表示策略在一天内配置的起始时间和结束时间内生效；也可以设置为总时长策略类型，表示一天内策略生效的总时长；也可以设置为共享时长策略类型，表示策略关联的所有应用共享同一可用时长配额。具体可参考[TimeStrategyType](../harmonyos-references/screentimeguard-guardservice.md#timestrategytype) 。
2. 管控策略可以设置限制类型，按允许清单做限制表示对传入的应用之外的应用进行管控，按禁止清单做限制表示对传入的应用进行限制。具体可参考[RestrictionType](../harmonyos-references/screentimeguard-guardservice.md#restrictiontype) 。
3. 管控策略可以设置一周内重复执行时间，支持填写含有1-7数字的number数组，表示在周一到周日的某些天重复执行。若不设置重复执行时间，则策略只执行一次。具体可参考[TimeStrategy](../harmonyos-references/screentimeguard-guardservice.md#timestrategy) 。

## 接口说明

添加策略的关键接口如下表所示：

| 接口名 | 描述 |
| --- | --- |
| [addGuardStrategy](../harmonyos-references/screentimeguard-guardservice.md#addguardstrategy)(guardStrategy: [GuardStrategy](../harmonyos-references/screentimeguard-guardservice.md#guardstrategy)): Promise<void> | 添加屏幕时间管控策略。 |

## 开发前提

添加管控策略需要申请用户授权，请先参考[请求用户授权](screentimeguard-request-user-auth.md)章节完成用户授权。

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { guardService } from '@kit.ScreenTimeGuardKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 定义屏幕时间管理策略。

   ```typescript
   private guardStrategy: guardService.GuardStrategy = {
     name: 'GuardStrategy', // 策略名称，由开发者自定义
     timeStrategy: {
       type: guardService.TimeStrategyType.START_END_TIME_TYPE, // 时间策略类型，此处为起止时间策略
       startTime: '19:00', // 管控起始时间，此处表示管控于19点开始
       endTime: '21:00', // 管控结束时间，此处表示管控于21点结束
       repeat: [1, 2, 3, 4, 5, 6, 7] // 重复执行时间，此处表示管控在周一至周日均生效
     },
     appInfo: { appTokens: [] }, // 应用token，可通过startAppPicker接口获取
     appRestrictionType: guardService.RestrictionType.BLOCKLIST_TYPE // 限制类型，此处为禁用清单类型，表示对appInfo指定的应用进行管控
   };
   ```
3. 调用addGuardStrategy，添加屏幕时间管控策略。

   ```typescript
   private async addStrategy(guardStrategy: guardService.GuardStrategy): Promise<void> {
     try {
       await guardService.addGuardStrategy(guardStrategy);
     } catch (error) {
       let err: BusinessError = error as BusinessError;
       hilog.error(0x0000, 'GuardService',
         `addGuardStrategy failed, errCode is ${err.code}, errMessage is ${err.message}`);
     }
   }
   ```
