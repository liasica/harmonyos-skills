---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-query-guard-strategies
title: 查询策略
breadcrumb: 指南 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > 守护策略管理 > 查询策略
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a6cf83f83d6304579a44f1a956e1a438402352ccc47f915ab02cf486f3edd7ae
---

## 场景介绍

当用户希望查看现有的屏幕时间守护规则时，可以调用查询管控策略的接口。通过成功调用查询策略接口，用户可以浏览已创建的所有管控策略，如查看各个应用的停用起止时间或可使用时长。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/w34BXWoUT8yUQyvoY5k4Ag/zh-cn_image_0000002552959170.png?HW-CC-KV=V1&HW-CC-Date=20260427T235053Z&HW-CC-Expire=86400&HW-CC-Sign=4004F05FE06659486E0B211B19B5055932194ED457723D12C76881C4E1427FFC)

流程说明：

1. 应用调用查询管控策略的接口，拉起健康使用设备查询本应用是否已申请权限，以及用户是否对本应用授权。
2. 若没有权限，则抛出相应错误码；若有权限，则返回对应应用下的所有管控策略。

## 接口说明

查询策略的关键接口如下表所示：

| 接口名 | 描述 |
| --- | --- |
| [queryGuardStrategies](../harmonyos-references/screentimeguard-guardservice.md#queryguardstrategies)(): Promise<[GuardStrategy](../harmonyos-references/screentimeguard-guardservice.md#guardstrategy)[]> | 查询该应用下的所有管控策略。 |

## 开发前提

查询管控策略需要申请用户授权，请先参考[请求用户授权](screentimeguard-request-user-auth.md)章节完成用户授权。

## 开发步骤

1. 导入相关模块。

   ```
   1. import { guardService } from '@kit.ScreenTimeGuardKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用queryGuardStrategy，查询对应应用下的所有管控策略。

   ```
   1. async function testQueryGuardStrategies() {
   2. try {
   3. let guardStrategy: guardService.GuardStrategy[] = await guardService.queryGuardStrategies();
   4. guardStrategy.forEach((element) => {
   5. hilog.info(0x0000, `ScreenTimeGuard:queryGuardStrategies`, `${element.name}`)
   6. })
   7. } catch (err) {
   8. const message = (err as BusinessError).message;
   9. const code = (err as BusinessError).code;
   10. hilog.error(0x0000, `ScreenTimeGuard:queryGuardStrategies`, `queryGuardStrategies failed with error code: ${code}, message: ${message}`);
   11. }
   12. }
   ```
