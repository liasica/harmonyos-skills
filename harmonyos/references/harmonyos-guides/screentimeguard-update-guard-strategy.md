---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-update-guard-strategy
title: 修改策略
breadcrumb: 指南 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > 守护策略管理 > 修改策略
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bf03659269ffbdcd0bc9ed79646cfbfd509f1c5656b56242dd75d055dc7f0c7e
---

## 场景介绍

当用户希望调整现有的屏幕时间守护规则时，可以调用更新管控策略的接口。我们kit支持根据参数中传入的策略名以及修改策略的方案，用户可以修改各种策略，如调整各个应用的停用起止时间。一旦修改完成并保存，系统将根据新的规则对用户的屏幕使用行为进行管控。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/vXtPyvSwRRaaWb-WU8rL4w/zh-cn_image_0000002583439215.png?HW-CC-KV=V1&HW-CC-Date=20260427T235053Z&HW-CC-Expire=86400&HW-CC-Sign=84D9C3713D6707596B54BC40BB2E720F2112670DCF23B43A9C3E4280DBF80586)

流程说明：

1. 应用调用更新管控策略的接口时，会拉起健康使用设备查询本应用是否已申请权限，以及用户是否对本应用授权。
2. 若没有权限，则抛出相应错误码；若有权限，则解析参数中传入的策略，并判断策略是否有效、是否存在。
3. 若策略有效，则记录到本地数据库，策略完成修改；否则，抛出相应错误码。

说明

1. 更新管控策略的策略名需和当前已有的策略一致，否则会抛出策略不存在错误。

## 接口说明

修改策略的关键接口如下表所示：

| 接口名 | 描述 |
| --- | --- |
| [updateGuardStrategy](../harmonyos-references/screentimeguard-guardservice.md#updateguardstrategy)(strategyName: string, guardStrategy: [GuardStrategy](../harmonyos-references/screentimeguard-guardservice.md#guardstrategy)): Promise<void> | 修改屏幕时间管控策略。 |

## 开发前提

修改管控策略需要申请用户授权，请先参考[请求用户授权](screentimeguard-request-user-auth.md)章节完成用户授权。

## 开发步骤

1. 导入相关模块。

   ```
   1. import { guardService, appPicker } from '@kit.ScreenTimeGuardKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用updateGuardStrategy，修改管控策略。

   ```
   1. @Entry
   2. @Component
   3. struct TestPage {
   4. build() {
   5. Column() {
   6. Button("TestUpdateGuardStrategy")
   7. .onClick(async () => {
   8. try {
   9. // 先调用startAppPicker获取相应应用的token
   10. const tokens = await appPicker.startAppPicker(this.getUIContext().getHostContext(), { appTokens: [] });

   12. const strategyName = "TestStrategy";
   13. const time: guardService.TimeStrategy = {
   14. type: guardService.TimeStrategyType.START_END_TIME_TYPE,
   15. startTime: "08:00",
   16. endTime: "19:00",
   17. repeat: [1,2,3]
   18. }
   19. const info: guardService.AppInfo = {
   20. appTokens: tokens
   21. }
   22. const strategy: guardService.GuardStrategy = {
   23. name: strategyName,
   24. timeStrategy: time,
   25. appInfo: info,
   26. appRestrictionType: guardService.RestrictionType.BLOCKLIST_TYPE
   27. }
   28. await guardService.updateGuardStrategy(strategyName, strategy);
   29. } catch (err) {
   30. const message = (err as BusinessError).message;
   31. const code = (err as BusinessError).code;
   32. hilog.error(0x0000, `ScreenTimeGuard:updateGuardStrategy`, `updateGuardStrategy failed with error code: ${code}, message: ${message}`);
   33. }
   34. })
   35. }
   36. }
   37. }
   ```
