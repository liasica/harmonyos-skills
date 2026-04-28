---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/request_user_authorization
title: 请求用户授权
breadcrumb: 指南 > 系统 > 硬件 > Wear Engine Kit（穿戴服务） > 手机侧应用开发 > 应用开发 > 请求用户授权
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:52+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:39adb5d75caf399cdec934eabaf3c7bc4800417133d51fc2b0f2cb90b218fa82
---

为保护用户隐私，Wear Engine的API需要用户授权才可以正常访问。建议开发者在用户首次调用Wear Engine开放能力的时候执行本章节操作。

## 申请用户穿戴设备权限

应用拉起华为账号登录和授权界面，由用户授权相应的数据访问权限。用户可以自主选择授权的数据类型，可以只授权部分数据权限。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/5y4jFQxcR1uj2xJgK8p-CA/zh-cn_image_0000002552958488.png?HW-CC-KV=V1&HW-CC-Date=20260427T234451Z&HW-CC-Expire=86400&HW-CC-Sign=AEA7417E583FF5CBC1C953CDA0F493673A7D2175B943DB1A4AF1EB3E9AC6CCEE)

1. 应用调用[wearEngine](../harmonyos-references/wearengine_api.md)中的[getAuthClient](../harmonyos-references/wearengine_api.md#wearenginegetauthclient)方法，获取[AuthClient](../harmonyos-references/wearengine_api.md#authclient)对象。
2. 定义需要用户授权的权限请求类[AuthorizationRequest](../harmonyos-references/wearengine_api.md#authorizationrequest)。
3. 调用[requestAuthorization](../harmonyos-references/wearengine_api.md#requestauthorization)方法，向用户请求权限。执行成功后，会弹出授权界面，让用户选择授予权限（若未登录华为账号则会先弹出登录界面）。当用户允许后才能正常使用接口，否则会遇到错误码为201的提示。

   说明

   * 请确保向用户请求的权限已在[申请接入Wear Engine服务](wearengine_apply.md)中审批通过，否则会遇到错误码为1008500004的提示。
   * 该功能可以多次调用，如果申请的权限之前已经授予了，不会再弹出授权页面，接口会返回已经授权的权限。
   * 通过入参的[AuthorizationRequest](../harmonyos-references/wearengine_api.md#authorizationrequest)对象，获取应用需要的权限。参见步骤3中[权限说明](wearengine_apply.md)了解应用所需请求的权限类型。
   * 通过[AuthorizationResponse](../harmonyos-references/wearengine_api.md#authorizationresponse)对象，返回用户的授权结果。

   ```
   1. // 在使用Wear Engine服务前，请导入WearEngine与相关模块
   2. import { wearEngine } from '@kit.WearEngine';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. // 步骤1：获取AuthClient对象
   6. let authClient: wearEngine.AuthClient = wearEngine.getAuthClient(this.getUIContext().getHostContext());

   8. // 步骤2：基于需要用户授权的权限定义权限请求类
   9. let request: wearEngine.AuthorizationRequest = {
   10. permissions: [wearEngine.Permission.USER_STATUS]
   11. }

   13. // 步骤3：请求用户授权
   14. authClient.requestAuthorization(request).then(result => {
   15. console.info(`Succeeded in requesting authorize, authorized permissions is ${result.permissions}`);
   16. }).catch((error: BusinessError) => {
   17. console.error(`Failed to request authorize. Code is ${error.code}, message is ${error.message}`);
   18. })
   ```

## 查询用户授权结果

用于查询已被用户授予的应用权限。如果所需权限用户未授权，请参见上一节[申请用户穿戴设备权限](request_user_authorization.md#申请用户穿戴设备权限)向用户请求权限。建议在请求用户授权前，先使用该接口查询应用是否已有相关权限。

说明

请确保权限已在[申请接入Wear Engine服务](wearengine_apply.md)中审批通过，否则会遇到错误码为1008500004的提示。

1. 应用调用[wearEngine](../harmonyos-references/wearengine_api.md)中的[getAuthClient](../harmonyos-references/wearengine_api.md#wearenginegetauthclient)方法，获取[AuthClient](../harmonyos-references/wearengine_api.md#authclient)对象。
2. 调用[getAuthorization](../harmonyos-references/wearengine_api.md#getauthorization)方法，查询用户已授权的权限。

   ```
   1. // 在使用Wear Engine服务前，请导入WearEngine与相关模块
   2. import { wearEngine } from '@kit.WearEngine';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. // 步骤1：获取AuthClient对象
   6. let authClient: wearEngine.AuthClient = wearEngine.getAuthClient(this.getUIContext().getHostContext());

   8. // 步骤2：调用API查询已授权权限
   9. authClient.getAuthorization().then(result => {
   10. console.info(`Succeeded in getting authorized permissions, authorized permissions is ${result.permissions}`);
   11. }).catch((error: BusinessError) => {
   12. console.error(`Failed to get authorized permissions. Code is ${error.code}, message is ${error.message}`);
   13. })
   ```
