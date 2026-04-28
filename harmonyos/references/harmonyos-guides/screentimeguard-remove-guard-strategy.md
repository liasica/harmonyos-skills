---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-remove-guard-strategy
title: 删除策略
breadcrumb: 指南 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > 守护策略管理 > 删除策略
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8ba643e40180fa3aa34115107ffd59ea80b7bd27a305bbf2f57ef5e101ea2da1
---

## 场景介绍

当应用希望删除现有的屏幕时间守护规则时，可以调用删除管控策略的接口。根据参数中传入的策略名删除对应的策略。一旦策略被删除，系统将不再根据该规则对用户的屏幕使用行为进行监管。

## 用户体验设计

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/vQ8PkhCLThWT0Cb5LIBRFQ/zh-cn_image_0000002583479171.png?HW-CC-KV=V1&HW-CC-Date=20260427T235053Z&HW-CC-Expire=86400&HW-CC-Sign=13061277D6969772DF0E36F3A48021F8248F340FE044C0CCF669586BECBD334C)

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/sNwsQQK3T0eVlGzJsJfRVA/zh-cn_image_0000002552799522.png?HW-CC-KV=V1&HW-CC-Date=20260427T235053Z&HW-CC-Expire=86400&HW-CC-Sign=69DF99DA125317594F6916272E0C57DB92C851337C71558730CF8762127A9D92)

流程说明：

1. 应用调用删除管控策略的接口，拉起健康使用设备查询本应用是否已申请权限，以及用户是否对本应用授权。
2. 若没有权限，则抛出相应错误码。若有权限，则解析参数中传入的策略名称，判断策略是否存在。
3. 若策略不存在，则抛出相应错误码；若存在，则查询该策略是否正在执行。
4. 若策略在执行，则会先停止管控策略再删除。

## 接口说明

删除策略的关键接口如下表所示：

| 接口名 | 描述 |
| --- | --- |
| [removeGuardStrategy](../harmonyos-references/screentimeguard-guardservice.md#removeguardstrategy)(strategyName: string): Promise<void> | 删除管控策略。 |

## 开发前提

删除管控策略需要申请用户授权，请先参考[请求用户授权](screentimeguard-request-user-auth.md)章节完成用户授权。

## 开发步骤

1. 导入相关模块。

   ```
   1. import { guardService } from '@kit.ScreenTimeGuardKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用removeGuardStrategy，删除管控策略。

   ```
   1. async function testRemoveGuardStrategy() {
   2. try {
   3. const strategyName = "TestStrategy";
   4. await guardService.removeGuardStrategy(strategyName);
   5. } catch (err) {
   6. const message = (err as BusinessError).message;
   7. const code = (err as BusinessError).code;
   8. hilog.error(0x0000, `ScreenTimeGuard:removeGuardStrategy`, `removeGuardStrategy failed with error code: ${code}, message: ${message}`);
   9. }
   10. }
   ```
