---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-revoke-user-auth
title: 取消用户授权
breadcrumb: 指南 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > 用户授权管理 > 取消用户授权
category: harmonyos-guides
scraped_at: 2026-04-29T13:40:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7aa8ee1f0a18d8e677f5308142d69b4af47f7046878a523c7d3fe1418bad9ae9
---

## 场景介绍

当开发者希望取消应用的Screen Time Guard Kit授权时，可以通过调用取消用户授权的接口进行取消。一旦权限被取消，应用将无法再访问或使用对用户设备的时间管理等功能。如果应用尝试继续调用与屏幕守护时间模块相关的接口，系统会返回用户未授权使用的错误码，以确保功能的安全性和隐私保护。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/dtuDcQ1vRHSL0NH7BMZQ2A/zh-cn_image_0000002558765666.png?HW-CC-KV=V1&HW-CC-Date=20260429T054025Z&HW-CC-Expire=86400&HW-CC-Sign=C9BB464BD95E082691ABE6B8C21C7770DC47B277455D2DAD47849FC777A35EF7)

流程说明：

1. 应用想要取消访问Screen Time Guard Kit的权限，需要调用拉起取消用户授权的接口，拉起健康使用设备查询本地数据库中该应用的授权状态。
2. 若状态为未授权，则直接正常返回；若状态为已授权，修改为未授权状态后正常返回。

## 接口说明

取消用户授权关键接口如下表所示：

| 接口名 | 描述 |
| --- | --- |
| [revokeUserAuth](../harmonyos-references/screentimeguard-guardservice.md#revokeuserauth)(): Promise<void> | 取消用户授权访问Screen Time Guard Kit的相关管控接口。 |
| [getUserAuthStatus](../harmonyos-references/screentimeguard-guardservice.md#getuserauthstatus)(): Promise<[AuthStatus](../harmonyos-references/screentimeguard-guardservice.md#authstatus)> | 获取用户授权状态。 |

## 开发步骤

1. 导入相关模块。

   ```
   1. import { guardService } from '@kit.ScreenTimeGuardKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 调用revokeUserAuth，取消用户授权。

   ```
   1. async function testRevokeUserAuth() {
   2. try {
   3. await guardService.revokeUserAuth();
   4. } catch (err) {
   5. const message = (err as BusinessError).message;
   6. const code = (err as BusinessError).code;
   7. hilog.error(0x0000, `ScreenTimeGuard:revokeUserAuth`, `revokeUserAuth failed with error code: ${code}, message: ${message}`);
   8. }
   9. }
   ```
3. 获取用户授权状态。

   ```
   1. async function testGetUserAuthStatus() {
   2. try {
   3. const status = await guardService.getUserAuthStatus();
   4. hilog.info(0x0000, `ScreenTimeGuard:getUserAuthStatus`, `user auth status: ${status}`);
   5. } catch (err) {
   6. const message = (err as BusinessError).message;
   7. const code = (err as BusinessError).code;
   8. hilog.error(0x0000, `ScreenTimeGuard:getUserAuthStatus`, `getUserAuthStatus failed with error code: ${code}, message: ${message}`);
   9. }
   10. }
   ```
