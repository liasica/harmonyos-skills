---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-sideloading
title: 侧载安全管控
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 侧载安全管控
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:29+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:3450ba38d5f6ef951b1b1ec6c09c39070bdb7df5673d967c9063f447b063f822
---

## 场景介绍

从API版本26.0.1开始，支持查询设备是否允许加载外部二进制文件，以及打开外部二进制源控制开关的设置对话框。

侧载安全管控支持对设备外部二进制文件的加载行为进行管控。应用可通过Device Security Kit提供的接口查询设备是否允许加载外部二进制文件，或引导用户打开设置对话框以开启外部二进制文件加载权限，以支撑侧载安全管控业务。

## 查询侧载安全管控状态

### 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/v2w4TPxCQtWT9h_ol5WqkQ/zh-cn_image_0000002817426781.png?HW-CC-KV=V1&HW-CC-Date=20261114T004729Z&HW-CC-Expire=31536000000&HW-CC-Sign=8301252C50A59BDDCDCEAE6A723A3002378F4778A4319AC810984BDAA9B73155)

**流程说明：**

1. 应用调用Device Security Kit的接口查询设备是否允许加载外部二进制文件。
2. Device Security Kit接口返回设备是否允许加载外部二进制文件的结果给应用。
3. 应用依据查询结果做业务处理。

### 接口说明

以下是查询设备是否允许加载外部二进制文件接口，更多接口及使用方法请参见[API参考](../harmonyos-references/devicesecurity-sideloading-api.md)。

| 接口名 | 描述 |
| --- | --- |
| isExternalBinaryLoadingEnabled(): Promise<boolean> | 查询设备是否允许加载外部二进制文件。 |

### 开发步骤

1. 导入侧载安全管控模块及相关公共模块。

   ```typescript
   import { sideloading } from '@kit.DeviceSecurityKit';
   import hilog from '@ohos.hilog';
   ```
2. 查询设备是否允许加载外部二进制文件。

   ```typescript
   const DOMAIN = 0x0000;
   const TAG = 'SideloadingTest';

   try {
     const result: boolean = await sideloading.isExternalBinaryLoadingEnabled();
     hilog.info(DOMAIN, TAG, `isExternalBinaryLoadingEnabled = ${result}`);
     if (result) {
       // Do something.
     } else {
       // Do something.
     }
   } catch (err) {
     hilog.error(DOMAIN, TAG, `call isExternalBinaryLoadingEnabled interface failed, errCode:${err?.code}, errMessage:${err?.message}`);
   }
   ```

## 打开外部二进制源控制开关设置对话框

### 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/QN7bAPp8R-KrKqZSMhfWsA/zh-cn_image_0000002788467362.png?HW-CC-KV=V1&HW-CC-Date=20261114T004729Z&HW-CC-Expire=31536000000&HW-CC-Sign=1BD825FBA4009BA3D6C19FD9E2472057FF262E255368C1B094C287C4262AB240)

**流程说明：**

1. 应用执行自身的业务逻辑，判断需要请求用户打开外部二进制加载控制开关
2. 应用（[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md#uiability)或[UIExtensionAbility](../harmonyos-references/js-apis-app-ability-uiextensionability.md#uiextensionability)）调用Device Security Kit的接口拉起外部二进制加载控制开关的设置弹窗。
3. Device Security Kit向用户展示外部二进制加载控制开关的设置弹窗。
4. 用户在设置弹窗中操作外部二进制加载控制开关。
5. Device Security Kit接口返回外部二进制文件加载状态给应用（[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md#uiability)或[UIExtensionAbility](../harmonyos-references/js-apis-app-ability-uiextensionability.md#uiextensionability)）。
6. 应用（[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md#uiability)或[UIExtensionAbility](../harmonyos-references/js-apis-app-ability-uiextensionability.md#uiextensionability)）依据返回状态做业务处理。

### 接口说明

以下是打开外部二进制加载控制开关设置弹窗接口，更多接口及使用方法请参见[API参考](../harmonyos-references/devicesecurity-sideloading-api.md)。

| 接口名 | 描述 |
| --- | --- |
| enableExternalBinaryLoadingOnSetting(context: common.Context): Promise<ExternalBinaryLoadingStatus> | 用于UIAbility或UIExtensionAbility弹窗请求用户设置二进制加载管控开关状态，返回本次请求的用户选择开关的结果。 |

### 开发步骤

1. 导入侧载安全管控模块及相关公共模块。

   ```typescript
   import { sideloading } from '@kit.DeviceSecurityKit';
   import hilog from '@ohos.hilog';
   ```
2. 调用接口打开外部二进制源控制开关的设置对话框，并根据返回状态进行业务处理。

   ```typescript
   const DOMAIN = 0x0000;
   const TAG = 'SideloadingTest';

   try {
     let context = getContext();
     const result: sideloading.ExternalBinaryLoadingStatus = await sideloading.enableExternalBinaryLoadingOnSetting(context);
     hilog.info(DOMAIN, TAG, `enableExternalBinaryLoadingOnSetting result = ${result}`);
     if (result === sideloading.ExternalBinaryLoadingStatus.ALLOW) {
       // Do something.
     } else if (result === sideloading.ExternalBinaryLoadingStatus.DENY) {
       // Do something.
     }
   } catch (err) {
     hilog.error(DOMAIN, TAG, `call enableExternalBinaryLoadingOnSetting interface failed, errCode:${err?.code}, errMessage:${err?.message}`);
   }
   ```
