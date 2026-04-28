---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-revoke-user-auth
title: 取消用户授权
breadcrumb: 指南 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > 用户授权管理 > 取消用户授权
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:52+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4c9ad27d121f9f8ce99ec803aa370edeb6a42fb0966937cff2949051ca5effde
---

## 场景介绍

当开发者希望取消应用的Screen Time Guard Kit授权时，可以通过调用取消用户授权的接口进行取消。一旦权限被取消，应用将无法再访问或使用对用户设备的时间管理等功能。如果应用尝试继续调用与屏幕守护时间模块相关的接口，系统会返回用户未授权使用的错误码，以确保功能的安全性和隐私保护。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/vN16Fc2KSKmqmEgVn10FjA/zh-cn_image_0000002583479165.png?HW-CC-KV=V1&HW-CC-Date=20260427T235051Z&HW-CC-Expire=86400&HW-CC-Sign=B332788BAC433C1BEAA9D13D73656EB2DA02BF43485EF136B322E0DAB4AE3D69)

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
