---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-request-user-auth
title: 请求用户授权
breadcrumb: 指南 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > 用户授权管理 > 请求用户授权
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:02+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:92ac722fff1d1cf9f7f5ebcdd8dcb1e3b10bc168527f5164356c4d52651eae50
---

## 场景介绍

Screen Time Guard Kit支持对用户设备的时间管理和应用限制，因此在功能启用前，必须获得用户的明确授权。应用可以调用请求用户授权接口，系统会弹出授权请求界面，明确告知用户功能的作用和必要性，并在用户允许之后，才可正常访问。如果用户未同意授权，则无法再提供相关管控能力，此时如果继续调用管控相关接口，会抛出用户未授权使用的错误码。

## 用户体验设计

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/7Fz2VwaTQX-kZ_qmP5EqnQ/zh-cn_image_0000002736434341.png)

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/clwaDHACQKe5X9eBVFZZuw/zh-cn_image_0000002706835192.png)

流程说明：

1. 应用请求访问Screen Time Guard Kit的权限，需要调用拉起请求用户授权的接口，拉起健康使用设备查询本地数据库中该应用的授权状态。
2. 若状态为已授权，则直接正常返回；若状态为未授权，则拉起授权弹框。
3. 若用户取消授权，则抛出对应错误码，若用户允许授权，则正常返回。

## 接口说明

请求用户授权关键接口如下表所示：

| 接口名 | 描述 |
| --- | --- |
| [requestUserAuth](../harmonyos-references/screentimeguard-guardservice.md#requestuserauth)(context: [common.UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md)): Promise<void> | 请求用户授权访问Screen Time Guard Kit的相关管控接口。 |
| [requestUserAuth](../harmonyos-references/screentimeguard-guardservice.md#requestuserauth-1)(context: [common.UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md), appConfig: [AppConfig](../harmonyos-references/screentimeguard-guardservice.md#appconfig)): Promise<void> | 请求用户授权访问Screen Time Guard Kit的相关管控接口，同时设置授权应用相关配置。 |
| [getUserAuthStatus](../harmonyos-references/screentimeguard-guardservice.md#getuserauthstatus)(): Promise<[AuthStatus](../harmonyos-references/screentimeguard-guardservice.md#authstatus)> | 获取用户授权状态。 |

**说明** 

若需更改授权应用配置信息，需要[取消用户授权](screentimeguard-revoke-user-auth.md)后，重新调用接口请求用户授权，同时设置授权应用相关配置。

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { guardService } from '@kit.ScreenTimeGuardKit';
   // ...
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 调用requestUserAuth，请求用户授权。

   ```typescript
   const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   // this.isUninstallable为boolean型变量，通过该变量设置此应用是否可卸载
   guardService.requestUserAuth(context, { isSupportAppUninstall: this.isUninstallable })
     .then(async () => {
       // ...
     })
     .catch((error: BusinessError) => {
       hilog.error(0x0000, 'GuardService',
         `requestUserAuth fail, errCode is ${error.code}, errMessage is ${error.message}`);
     })
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
