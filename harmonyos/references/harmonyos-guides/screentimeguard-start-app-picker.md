---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-start-app-picker
title: 拉起应用选择页
breadcrumb: 指南 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > 应用选择页 > 拉起应用选择页
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:53+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d558583dc39cf010aa2bde2095f13d8762f1f1e75063ac3a3396d78be3f1e056
---

## 场景介绍

在用户需要为特定应用设置使用时长或使用限制策略的场景下，开发者通过调用拉起应用选择页的接口拉起选择页后，使得用户能够选择目标应用。在用户选择完毕并点击完成按钮后，接口会返回应用的token。开发者获取到目标应用的token后，可以根据token为选定应用配置管控策略。

## 用户体验设计

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/nRRWH0BJSlml3lLPWuBE2g/zh-cn_image_0000002583479167.png?HW-CC-KV=V1&HW-CC-Date=20260427T235052Z&HW-CC-Expire=86400&HW-CC-Sign=10A501DA311F5461BA8DAE8639D19E3087F110DC0D006E2DE8F9C379991970E1)

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/Qlo55AyjTQC6-zbY7xcRdg/zh-cn_image_0000002552799518.png?HW-CC-KV=V1&HW-CC-Date=20260427T235052Z&HW-CC-Expire=86400&HW-CC-Sign=DB6C81284207D8AEA7AF0DEB74BF7A87EACEE2ED707E5A9EC84586A544CE5983)

流程说明：

1. 应用调用拉起应用选择页的接口，拉起健康使用设备查询开发者是否已申请权限，以及用户是否授权。
2. 若状态为未授权，则抛出对应错误码；若状态为已授权，应用将拉起应用选择列表，并根据传入应用token信息预勾选对应应用。
3. 应用选择页将用户选中的应用列表转化为token列表返回给调用接口的应用。

## 接口说明

拉起应用选择页关键接口如下表所示：

| 接口名 | 描述 |
| --- | --- |
| [startAppPicker](../harmonyos-references/screentimeguard-app-picker.md#startapppicker)(context: [common.Context](../harmonyos-references/js-apis-inner-application-context.md), appSelection: [guardService.AppInfo](../harmonyos-references/screentimeguard-guardservice.md#appinfo)): Promise<string[]> | 拉起应用选择页。 |

说明

1. 应用选择页面中的应用列表不包含的系统应用包括：电话、联系人、设置、未成年模式等。
2. 应用选择页面中的应用列表不包含管控发起应用本身和已授权的管控应用。

## 开发前提

拉起应用选择页需要申请用户授权，请先参考[请求用户授权](screentimeguard-request-user-auth.md)章节完成用户授权。

## 开发步骤

1. 导入相关模块。

   ```
   1. import { appPicker } from '@kit.ScreenTimeGuardKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用startAppPicker，拉起应用选择页。

   ```
   1. @Entry
   2. @Component
   3. struct TestPage {
   4. build() {
   5. Column() {
   6. Button("TestStartAppPicker")
   7. .onClick(async () => {
   8. try {
   9. await appPicker.startAppPicker(this.getUIContext().getHostContext(), { appTokens: [] });
   10. } catch (err) {
   11. const message = (err as BusinessError).message;
   12. const code = (err as BusinessError).code;
   13. hilog.error(0x0000, `ScreenTimeGuard:startAppPicker`, `startAppPicker failed error code: ${code}, message: ${message}`);
   14. }
   15. })
   16. }
   17. }
   18. }
   ```
