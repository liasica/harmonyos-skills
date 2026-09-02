---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-update-guard-strategy
title: 修改策略
breadcrumb: 指南 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > 守护策略管理 > 修改策略
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:02+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:7b2ca1c13d7a60c7f2756792106a9a6b16e8f361365983f7479dbca61db8148a
---

## 场景介绍

当管控应用希望调整现有的管控策略时，可以调用更新管控策略的接口。Screen Time Guard Kit支持根据参数中传入的策略名以及新的管控策略来修改指定策略，如调整被管控应用的停用时间。一旦修改完成并保存，系统将根据新的规则对用户的屏幕使用行为进行管控。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/vJ3Su0mTQW6fPnQlDAITMA/zh-cn_image_0000002706675258.png)

流程说明：

1. 应用调用更新管控策略的接口时，会拉起健康使用设备查询本应用是否已申请权限，以及用户是否对本应用授权。
2. 若开发者没有权限或用户没有授权，则抛出相应错误码。若开发者有权限且用户已授权，则解析参数中传入的策略，并判断策略是否有效、是否存在。
3. 若策略有效，则记录到本地数据库，策略完成修改；否则，抛出相应错误码。

**说明** 

1. 待更新管控策略的策略名需和当前已有的策略一致，否则会抛出策略不存在错误。
2. 新的策略名可以和当前待更新的策略名一致，除此之外，不能和其他当前已有的策略一致，否则会抛出参数错误。

## 接口说明

修改策略的关键接口如下表所示：

| 接口名 | 描述 |
| --- | --- |
| [updateGuardStrategy](../harmonyos-references/screentimeguard-guardservice.md#updateguardstrategy)(strategyName: string, guardStrategy: [GuardStrategy](../harmonyos-references/screentimeguard-guardservice.md#guardstrategy)): Promise<void> | 修改屏幕时间管控策略。 |

## 开发前提

修改管控策略需要申请用户授权，请先参考[请求用户授权](screentimeguard-request-user-auth.md)章节完成用户授权。

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { guardService } from '@kit.ScreenTimeGuardKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用updateGuardStrategy，修改管控策略。

   ```typescript
   private async updateStrategy(strategyName: string, guardStrategy: guardService.GuardStrategy): Promise<void> {
     try {
       await guardService.updateGuardStrategy(strategyName, guardStrategy);
     } catch (error) {
       let err: BusinessError = error as BusinessError;
       hilog.error(0x0000, 'GuardService',
         `updateGuardStrategy failed, errCode is ${err.code}, errMessage is ${err.message}`);
     }
   }
   ```
