---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-start-app-picker
title: 拉起应用选择页
breadcrumb: 指南 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > 应用选择页 > 拉起应用选择页
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:39+08:00
doc_updated_at: 2026-09-23
content_hash: sha256:8679a1f11d957c4726bbc3a7955ce497ae2a215585cd5d7c8c3c64c60f37823b
---

## 场景介绍

在需要为指定应用设置管控规则的场景下，管控应用通过调用拉起应用选择页的接口拉起选择页后，使得用户能够选择目标应用。在用户选择完毕并点击完成按钮后，接口会返回选中应用的token。管控应用获取到目标应用的token后，可以根据token为选定应用设置管控规则。

## 用户体验设计

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/JNs_SwC_QQKnX84sZDb_bg/zh-cn_image_0000002821838205.png?HW-CC-KV=V1&HW-CC-Date=20261121T011238Z&HW-CC-Expire=31536000000&HW-CC-Sign=256B0BBE237E776A32A5C27787B0814188AB78D9E184CBCD6F1FB0D1C8D0FD77)

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/EF_NahucSIKC7qpsdwA2AQ/zh-cn_image_0000002821758207.png?HW-CC-KV=V1&HW-CC-Date=20261121T011238Z&HW-CC-Expire=31536000000&HW-CC-Sign=DAA48BABD202EB4F12E61DB91AFCF5F2716A847410BE2683C9C995CC8E6466D9)

流程说明：

1. 应用调用拉起应用选择页的接口，拉起健康使用设备查询开发者是否已申请权限，以及用户是否授权。
2. 若开发者没有权限或用户没有授权，则抛出相应错误码。若开发者有权限且用户已授权，应用将拉起应用选择列表，并根据传入应用token信息预勾选对应应用。
3. 应用选择页将用户选中的应用列表转化为token列表返回给调用接口的应用。

## 接口说明

拉起应用选择页关键接口如下表所示：

| 接口名 | 描述 |
| --- | --- |
| [startAppPicker](../harmonyos-references/screentimeguard-app-picker.md#startapppicker)(context: [common.Context](../harmonyos-references/js-apis-inner-application-context.md), appSelection: [guardService.AppInfo](../harmonyos-references/screentimeguard-guardservice.md#appinfo)): Promise<string[]> | 拉起应用选择页。 |

**说明** 

1. 为保证系统基础功能正常，电话、时钟、联系人、设置、未成年人模式等不会出现在应用选择列表中。
2. 为确保管控逻辑清晰，管控发起应用本身和已授权的管控应用不会出现在应用选择列表中。

## 开发前提

拉起应用选择页需要申请用户授权，请先参考[请求用户授权](screentimeguard-request-user-auth.md)章节完成用户授权。

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { appPicker } from '@kit.ScreenTimeGuardKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 调用startAppPicker，拉起应用选择页。

   ```typescript
   private async getAppTokens(selectedAppTokens: string[]): Promise<string[]> {
     try {
       let newSelectedAppTokens: string[] =
         await appPicker.startAppPicker(this.getUIContext().getHostContext(), { appTokens: selectedAppTokens });
       return newSelectedAppTokens;
     } catch(error) {
       let err: BusinessError = error as BusinessError;
       hilog.error(0x0000, 'GuardService',
         `startAppPicker fail, errCode is ${err.code}, errMessage is ${err.message}`);
       return selectedAppTokens;
     }
   }
   ```
