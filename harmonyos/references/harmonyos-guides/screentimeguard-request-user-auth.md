---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-request-user-auth
title: 请求用户授权
breadcrumb: 指南 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > 用户授权管理 > 请求用户授权
category: harmonyos-guides
scraped_at: 2026-04-29T13:40:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fada548c049feac1d69b6a4bb96be549598ed2ec6286c46581846bc5dc01ea2f
---

## 场景介绍

Screen Time Guard Kit支持对用户设备的时间管理和应用限制，因此在功能启用前，必须获得用户的明确授权。应用可以调用请求用户授权接口，系统会弹出授权请求界面，明确告知用户功能的作用和必要性，并在用户允许之后，才可正常访问。如果用户未同意授权，则无法再提供相关管控能力，此时如果继续调用管控相关接口，会抛出用户未授权使用的错误码。

## 用户体验设计

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/LrWZqq3USwKApDe99xsUSg/zh-cn_image_0000002589325535.png?HW-CC-KV=V1&HW-CC-Date=20260429T054025Z&HW-CC-Expire=86400&HW-CC-Sign=184A99B9503A9BB158B5DD1B48145E30676144C7E3A518F792C782B78A8A1C39)

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/QDk--hLWQRa8pXpWq-Jxag/zh-cn_image_0000002589245473.png?HW-CC-KV=V1&HW-CC-Date=20260429T054025Z&HW-CC-Expire=86400&HW-CC-Sign=E24CA10BEBF6294B5C8C3DC2E91457D5D9F427BE9CAA0CD79C99B3EB8D35FF0C)

流程说明：

1. 应用请求访问Screen Time Guard Kit的权限，需要调用拉起请求用户授权的接口，拉起健康使用设备查询本地数据库中该应用的授权状态。
2. 若状态为已授权，则直接正常返回；若状态为未授权，则拉起授权弹框。
3. 若用户取消授权，则抛出对应错误码，若用户允许授权，则正常返回。

## 接口说明

请求用户授权关键接口如下表所示：

| 接口名 | 描述 |
| --- | --- |
| [requestUserAuth](../harmonyos-references/screentimeguard-guardservice.md#requestuserauth)(context: [common.UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md)): Promise<void> | 请求用户授权访问Screen Time Guard Kit的相关管控接口。 |
| [getUserAuthStatus](../harmonyos-references/screentimeguard-guardservice.md#getuserauthstatus)(): Promise<[AuthStatus](../harmonyos-references/screentimeguard-guardservice.md#authstatus)> | 获取用户授权状态。 |

## 开发步骤

1. 导入相关模块。

   ```
   1. import { guardService } from '@kit.ScreenTimeGuardKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { common } from '@kit.AbilityKit';
   ```
2. 调用requestUserAuth，请求用户授权。

   ```
   1. @Entry
   2. @Component
   3. struct TestPage {
   4. build() {
   5. Column() {
   6. Button("TestRequestUserAuth")
   7. .onClick(async () => {
   8. try {
   9. await guardService.requestUserAuth(this.getUIContext().getHostContext() as common.UIAbilityContext);
   10. } catch (err) {
   11. const message = (err as BusinessError).message;
   12. const code = (err as BusinessError).code;
   13. hilog.error(0x0000, `ScreenTimeGuard:requestUserAuth`, `requestUserAuth failed with error code: ${code}, message: ${message}`);
   14. }
   15. })
   16. }
   17. }
   18. }
   ```
3. 获取用户授权状态。

   ```
   1. @Entry
   2. @Component
   3. struct TestPage {
   4. build() {
   5. Column() {
   6. Button("TestGetUserAuthStatus")
   7. .onClick(async () => {
   8. try {
   9. const status = await guardService.getUserAuthStatus();
   10. hilog.info(0x0000, `ScreenTimeGuard:getUserAuthStatus`, `user auth status: ${status}`);
   11. } catch (err) {
   12. const message = (err as BusinessError).message;
   13. const code = (err as BusinessError).code;
   14. hilog.error(0x0000, `ScreenTimeGuard:getUserAuthStatus`, `getUserAuthStatus failed with error code: ${code}, message: ${message}`);
   15. }
   16. })
   17. }
   18. }
   19. }
   ```
