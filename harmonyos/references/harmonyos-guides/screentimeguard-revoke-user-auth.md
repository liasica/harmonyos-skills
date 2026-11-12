---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-revoke-user-auth
title: 取消用户授权
breadcrumb: 指南 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > 用户授权管理 > 取消用户授权
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:4639f9f941f3db72edec4a948860a82611b97a16ecaa257cdfeeb06d7290e4bf
---

## 场景介绍

当管控应用希望取消用户的授权时，可以调用取消用户授权的接口。一旦权限被取消，管控应用将无法再使用屏幕时间守护功能。如果管控应用尝试继续调用屏幕时间守护模块的相关接口，系统会返回用户未授权使用的错误码，以确保功能的安全性和隐私保护。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/LtGsP5fURjum_T3IGYzUHA/zh-cn_image_0000002786360580.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=B74B496F81010C97207834A3A07E857F20DE2004296642934E033826336F5240)

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

   ```typescript
   import { guardService } from '@kit.ScreenTimeGuardKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用revokeUserAuth，取消用户授权。

   ```typescript
   public async revokeUserAuth(): Promise<void> {
     try {
       await guardService.revokeUserAuth();
     } catch (error) {
       let err: BusinessError = error as BusinessError;
       hilog.error(0x0000, 'GuardService',
         `revokeUserAuth failed, errCode is ${err.code}, errMessage is ${err.message}`);
     }
   }
   ```
3. 获取用户授权状态。

   ```typescript
   public async getUserAuthStatus(): Promise<void> {
     try {
       const status = await guardService.getUserAuthStatus();
       hilog.info(0x0000, 'GuardService', `user auth status: ${status}`);
     } catch (error) {
       let err: BusinessError = error as BusinessError;
       hilog.error(0x0000, 'GuardService',
         `getUserAuthStatus failed, errCode is ${err.code}, errMessage is ${err.message}`);
     }
   }
   ```
