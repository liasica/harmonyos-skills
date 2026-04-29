---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-add-guard-strategy
title: 添加策略
breadcrumb: 指南 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > 守护策略管理 > 添加策略
category: harmonyos-guides
scraped_at: 2026-04-29T13:40:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c7cfc7298d3d64f79945c13bf9e764e9d8d8db6f918eb4f0dba7ecc80b048b75
---

## 场景介绍

当用户希望创建新的屏幕时间守护规则时，可以调用添加管控策略的接口。根据参数中传入的策略，用户可以添加各种策略，如设置各个应用的停用起止时间。一旦策略被创建并启用，系统将根据规则对用户的屏幕使用行为进行监管。

## 用户体验设计

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/pKkZLzVSTESCvS9an8j2tw/zh-cn_image_0000002558765670.png?HW-CC-KV=V1&HW-CC-Date=20260429T054027Z&HW-CC-Expire=86400&HW-CC-Sign=26FB405E834B0582B3617E2DA57D4ACC67E7F5EF3A25D4A690CCFC143A013FF0)

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/SwAUzEBPSbOSkArkdsQsEA/zh-cn_image_0000002558606014.png?HW-CC-KV=V1&HW-CC-Date=20260429T054027Z&HW-CC-Expire=86400&HW-CC-Sign=6D513EECC85F029E0D169B1AE7AA3198C9DD3DA1C71472EECE4CCEB83AD6795B)

流程说明：

1. 应用调用添加管控策略的接口，拉起健康使用设备查询本应用是否已申请权限，以及用户是否已给本应用授权。
2. 若没有权限，则抛出相应错误码；若有权限，则解析参数中传入的策略，判断策略是否有效、是否重复、数量是否超限。
3. 若策略正常，则记录到本地数据库；否则，抛出相应错误码。

说明

1. 管控策略可以设置为起止时间策略，表示策略在一天内配置的起始时间和结束时间内生效；也可以设置为总时长策略类型，表示一天内策略生效的总时长；也可以设置为共享时长策略类型，表示策略关联的所有应用共享同一可用时长配额。具体可参考[TimeStrategyType](../harmonyos-references/screentimeguard-guardservice.md#timestrategytype) 。
2. 管控策略可以设置限制类型，按允许清单做限制表示对传入的应用之外的应用进行管控，按禁止清单做限制表示对传入的应用进行限制。具体可参考[RestrictionType](../harmonyos-references/screentimeguard-guardservice.md#restrictiontype) 。
3. 管控策略可以设置一周内重复执行时间，支持填写含有1-7数字的number数组，表示在周一到周日的某些天重复执行。具体可参考[TimeStrategy](../harmonyos-references/screentimeguard-guardservice.md#timestrategy) 。

## 接口说明

添加策略的关键接口如下表所示：

| 接口名 | 描述 |
| --- | --- |
| [addGuardStrategy](../harmonyos-references/screentimeguard-guardservice.md#addguardstrategy)(guardStrategy: [GuardStrategy](../harmonyos-references/screentimeguard-guardservice.md#guardstrategy)): Promise<void> | 添加屏幕时间管控策略。 |

## 开发前提

添加管控策略需要申请用户授权，请先参考[请求用户授权](screentimeguard-request-user-auth.md)章节完成用户授权。

## 开发步骤

1. 导入相关模块。

   ```
   1. import { guardService, appPicker } from '@kit.ScreenTimeGuardKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用addGuardStrategy，添加屏幕时间管控策略。

   ```
   1. @Entry
   2. @Component
   3. struct TestPage {
   4. build() {
   5. Column() {
   6. Button("TestAddGuardStrategy")
   7. .onClick(async () => {
   8. try {
   9. // 先调用startAppPicker获取相应应用的token
   10. const tokens = await appPicker.startAppPicker(this.getUIContext().getHostContext(), { appTokens: [] });

   12. const time: guardService.TimeStrategy = {
   13. type: guardService.TimeStrategyType.START_END_TIME_TYPE,
   14. startTime: "08:00",
   15. endTime: "19:00",
   16. repeat: [1,2,3]
   17. }
   18. const info: guardService.AppInfo = {
   19. appTokens: tokens
   20. }
   21. const strategy: guardService.GuardStrategy = {
   22. name: "TestStrategy",
   23. timeStrategy: time,
   24. appInfo: info,
   25. appRestrictionType: guardService.RestrictionType.BLOCKLIST_TYPE
   26. }
   27. await guardService.addGuardStrategy(strategy);
   28. } catch (err) {
   29. const message = (err as BusinessError).message;
   30. const code = (err as BusinessError).code;
   31. hilog.error(0x0000, `ScreenTimeGuard:addGuardStrategy`, `addGuardStrategy failed with error code: ${code}, message: ${message}`);
   32. }
   33. })
   34. }
   35. }
   36. }
   ```
