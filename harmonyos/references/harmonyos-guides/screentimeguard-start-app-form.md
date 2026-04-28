---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-start-app-form
title: 拉起许可应用跳转页
breadcrumb: 指南 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > 应用选择页 > 拉起许可应用跳转页
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:53+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5d953fed1e37b87e8cacd4e3aa2e2c590c0a7972ddbe1c5cd06bfd51318e9798
---

## 场景介绍

从6.0.2(22)版本开始，新增支持拉起许可应用跳转页功能。为实现用户在被管控期间快速跳转到许可应用的诉求，开发者可调用startAppForm接口拉起应用跳转页，页面中将展示通过接口参数传入的许可应用token对应的应用列表。用户点击其中的应用图标后能跳转到该应用。

## 用户体验设计

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/vB0bi4l-Ty6ZWP91KdxBFg/zh-cn_image_0000002583439213.png?HW-CC-KV=V1&HW-CC-Date=20260427T235052Z&HW-CC-Expire=86400&HW-CC-Sign=EA624F288EA07FDA66702EF3C93EE6E8475C3D396D4B49B43D9473409B3E6339)

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/TwGFHWiVRxa7zwsXWr2qKQ/zh-cn_image_0000002552959168.png?HW-CC-KV=V1&HW-CC-Date=20260427T235052Z&HW-CC-Expire=86400&HW-CC-Sign=102399B210667F1A1867D8CD45884587645BDDA3EB2E45C0D2E66E5BB6ADF89C)

流程说明：

1. 应用调用拉起许可应用跳转页的接口，拉起健康使用设备查询开发者是否已申请权限，以及用户是否授权。
2. 若状态为未授权，则抛出对应错误码；若状态为已授权，应用将根据传入的应用token信息获取全量应用信息，判断是否展示TrustApp，并拉起应用列表Form。
3. 用户点击跳转页中的应用，跳转到相应的应用。

## 接口说明

拉起许可应用跳转页的关键接口如下表所示：

| 接口名 | 描述 |
| --- | --- |
| [startAppForm](../harmonyos-references/screentimeguard-app-picker.md#startappform)(context: [common.Context](../harmonyos-references/js-apis-inner-application-context.md), appSelection: [guardService.AppInfo](../harmonyos-references/screentimeguard-guardservice.md#appinfo), appSubTitle: string, displayTrustApp: boolean): Promise<void> | 拉起许可应用跳转页。 |

## 开发前提

拉起许可应用跳转页需要申请用户授权，请先参考[请求用户授权](screentimeguard-request-user-auth.md)章节完成用户授权。

## 开发步骤

1. 导入相关模块。

   ```
   1. import { appPicker } from '@kit.ScreenTimeGuardKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用startAppForm，拉起许可应用跳转页。

   ```
   1. @Entry
   2. @Component
   3. struct TestPage {
   4. build() {
   5. Column() {
   6. Button("TestStartAppForm")
   7. .onClick(async () => {
   8. try {
   9. // 先调用startAppPicker获取相应应用的token
   10. const tokens = await appPicker.startAppPicker(this.getUIContext().getHostContext(), { appTokens: [] });

   12. await appPicker.startAppForm(this.getUIContext().getHostContext(), { appTokens: tokens }, "TestStartAppForm", false);
   13. } catch (err) {
   14. const message = (err as BusinessError).message;
   15. const code = (err as BusinessError).code;
   16. hilog.error(0x0000, `ScreenTimeGuard:startAppForm`, `startAppForm failed error code: ${code}, message: ${message}`);
   17. }
   18. })
   19. }
   20. }
   21. }
   ```
