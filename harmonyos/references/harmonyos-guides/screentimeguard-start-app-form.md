---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-start-app-form
title: 拉起许可应用跳转页
breadcrumb: 指南 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > 应用选择页 > 拉起许可应用跳转页
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:32+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:68aff566e7132965e09a584be30f95632cea12bf4914c34d4a0c71bbbc7fe835
---

## 场景介绍

从6.0.2(22)版本开始，新增支持拉起许可应用跳转页功能。为实现用户在被管控期间快速跳转到许可应用的诉求，开发者可调用startAppForm接口拉起应用跳转页，页面中将展示通过接口参数传入的许可应用token对应的应用列表。用户点击其中的应用图标后能跳转到该应用。

## 用户体验设计

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/6YYdTuUmQsOxvBlavDzGiw/zh-cn_image_0000002817427679.png?HW-CC-KV=V1&HW-CC-Date=20261114T004831Z&HW-CC-Expire=31536000000&HW-CC-Sign=97DDAA860969247E93616C6E8687D9CBEBB7B888BE26829D36070A35472D305B)

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/PMb6azUIQD6VOGpAgYukYQ/zh-cn_image_0000002788468260.png?HW-CC-KV=V1&HW-CC-Date=20261114T004831Z&HW-CC-Expire=31536000000&HW-CC-Sign=340B1DBEFB58350B8348DF4D1C7B52225EA115F4F4179E86770A77D614B41C70)

流程说明：

1. 应用调用拉起许可应用跳转页的接口，拉起健康使用设备查询开发者是否已申请权限，以及用户是否授权。
2. 若开发者没有权限或用户没有授权，则抛出相应错误码。若开发者有权限且用户已授权，将根据传入的token获取对应应用信息，同时判断是否展示TrustApp，并拉起应用列表Form。
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

   ```typescript
   import { appPicker } from '@kit.ScreenTimeGuardKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 调用startAppForm，拉起许可应用跳转页。

   ```typescript
   private async jumpToOtherApp(selectedAppTokens: string[], subtitle: string): Promise<void> {
     try {
       // appTokens为在许可应用跳转页中展示应用对应的token数组，可通过调用startAppPicker接口获取
       // subtitle为许可应用跳转页的子标题，可根据业务需求设置
       await appPicker.startAppForm(
         this.getUIContext().getHostContext(), { appTokens: selectedAppTokens }, subtitle, true);
     } catch(error) {
       let err: BusinessError = error as BusinessError;
       hilog.error(0x0000, 'GuardService',
         `startAppForm fail, errCode is ${err.code}, errMessage is ${err.message}`);
     }
   }
   ```
