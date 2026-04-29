---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-start-guard-strategy
title: 启动策略
breadcrumb: 指南 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > 守护策略管理 > 启动策略
category: harmonyos-guides
scraped_at: 2026-04-29T13:40:30+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:dc52bd6ebb893b0837c1d033afdac5339d50f09e0c31731d2897a055e6b15414
---

## 场景介绍

当应用希望启动某个管控规则时，可以调用启动管控策略的接口。根据参数中传入的策略名，应用可以启动对应管控策略。一旦策略被创建并启用，系统将根据规则对用户的屏幕使用行为进行监管。

## 用户体验设计

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/U_ec3LjbRz6ro8xqUaCWNA/zh-cn_image_0000002589325543.png?HW-CC-KV=V1&HW-CC-Date=20260429T054029Z&HW-CC-Expire=86400&HW-CC-Sign=5E8A557F06CB167FBE8D79B925ED351B69C79262F471415BE932857AFEC23BF4)

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/14PCE5l_TECRrTcsu2NFPQ/zh-cn_image_0000002589245481.png?HW-CC-KV=V1&HW-CC-Date=20260429T054029Z&HW-CC-Expire=86400&HW-CC-Sign=B7120AAAEBCC96EAEDB27541722B24B65EAC54EF531BDD66848F2DAC642982C2)

流程说明：

1. 继承TimeGuardExtensionAbility，实现onStart方法，此步非必需。
2. 调用启动管控策略的接口，拉起健康使用设备查询开发者是否已申请权限，以及用户是否授权。
3. 若开发者没有权限或用户未授权，则抛出相应错误码。若开发者有权限且用户已授权，则解析参数中传入的策略名称，判断策略是否存在。
4. 若策略不存在，则抛出相应错误码；若存在，则查询该策略是否正在执行。
5. 若查询的策略未执行，则正常启动策略，并记录启动状态；否则，抛出策略已在执行中的错误码。
6. 策略启动后，系统时间被设置为不可修改，管控发起应用被设置为不可卸载。
7. 当到了管控生效的时间，管控开始生效，拉起extension进程，执行TimeGuardExtensionAbility的onStart回调。

## 接口说明

启动策略的关键接口如下表所示：

| 接口名 | 描述 |
| --- | --- |
| [startGuardStrategy](../harmonyos-references/screentimeguard-guardservice.md#startguardstrategy)(strategyName: string): Promise<void> | 根据策略名称，启动其管控策略。 |
| [onStart](../harmonyos-references/screentimeguard-timeguardextensionability.md#onstart)(strategyName: string): Promise<void> | 在策略启动时执行特定逻辑。 |

## 开发前提

启动管控策略需要申请用户授权，请先参考[请求用户授权](screentimeguard-request-user-auth.md)章节完成用户授权。

## 开发步骤

1. 导入相关模块。

   ```
   1. import { guardService, TimeGuardExtensionAbility } from '@kit.ScreenTimeGuardKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 继承TimeGuardExtensionAbility，重写onStart回调。

   ```
   1. export default class EntryAbility extends TimeGuardExtensionAbility {
   2. async onStart(strategyName: string): Promise<void> {
   3. hilog.info(0x0000, 'test --- onStart', strategyName);
   4. }
   5. }
   ```
3. 调用startGuardStrategy，启动管控策略。

   ```
   1. async function testStartGuardStrategy() {
   2. try {
   3. const strategyName = "TestStrategy";
   4. await guardService.startGuardStrategy(strategyName);
   5. } catch (err) {
   6. const message = (err as BusinessError).message;
   7. const code = (err as BusinessError).code;
   8. hilog.error(0x0000, `ScreenTimeGuard:startGuardStrategy`, `startGuardStrategy failed with error code: ${code}, message: ${message}`);
   9. }
   10. }
   ```
