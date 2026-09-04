---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-getsuperprivacymode
title: 查询超级隐私模式状态
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 超级隐私模式 > 查询超级隐私模式状态
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:414095b17daea5c8fea11015669808093420c0f5510a1d833b7da33cbd6a48ab
---

## 场景介绍

从6.0.2(22)开始，新增了查询设备当前超级隐私模式状态的功能。

超级隐私模式支持一键关闭位置、相机和麦克风等敏感器件。该模式管控的器件范围将随版本更新动态调整。应用可通过Device Security Kit提供的接口获取超级隐私模式的状态。

## 约束与限制

本特性需要设备上存在超级隐私模式选项。开发者可通过在设备上选择“设置 > 隐私和安全 > 超级隐私模式”查看超级隐私模式选项。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/h5ENJa4jTfCrjZiIDNzCRw/zh-cn_image_0000002712244548.png)

**流程说明：**

1. 开发者应用调用[getSuperPrivacyMode](../harmonyos-references/devicesecurity-superprivacymode-api.md#getsuperprivacymode)接口查询当前超级隐私模式状态。
2. Device Security Kit接口同步返回当前超级隐私模式状态给开发者应用。
3. 开发者应用根据返回的超级隐私模式状态进行业务处理。

## 接口说明

以下是超级隐私模式状态查询接口，更多接口及使用方法请参见[API参考](../harmonyos-references/devicesecurity-superprivacymode-api.md)。

| 接口名 | 描述 |
| --- | --- |
| [getSuperPrivacyMode](../harmonyos-references/devicesecurity-superprivacymode-api.md#getsuperprivacymode)() : Promise<[SuperPrivacyMode](../harmonyos-references/devicesecurity-superprivacymode-api.md#superprivacymode)> | 查询当前超级隐私模式状态 |

## 开发步骤

1. 导入超级隐私模块及相关公共模块。

   ```typescript
   import { superPrivacyMode } from '@kit.DeviceSecurityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 调用[getSuperPrivacyMode](../harmonyos-references/devicesecurity-superprivacymode-api.md#getsuperprivacymode)接口查询超级隐私模式的状态。

   ```typescript
   const DOMAIN = 0x0000;
   const TAG = 'SuperPrivacyModeTest';
   ```

   ```typescript
   let mode: superPrivacyMode.SuperPrivacyMode = superPrivacyMode.SuperPrivacyMode.OFF;
   try {
     mode = await superPrivacyMode.getSuperPrivacyMode();
     hilog.info(DOMAIN, TAG, `Super privacy mode = ${mode}`);
     // ...
   } catch (err) {
     hilog.error(DOMAIN, TAG, `call getSuperPrivacyMode interface failed, errCode:${err?.code}, errMessage:${err?.message}`);
     // ...
   }
   ```
