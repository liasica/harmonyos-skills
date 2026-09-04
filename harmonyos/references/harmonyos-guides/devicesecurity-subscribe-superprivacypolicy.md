---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-subscribe-superprivacypolicy
title: 订阅超级隐私模式管控策略改变事件
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 超级隐私模式 > 订阅超级隐私模式管控策略改变事件
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a923d144c8d8fb55a2babdb6313861026c2e7b341f05c82c8a98f3669e2643dd
---

## 场景介绍

从26.0.0开始，超级隐私模式新增订阅超级隐私管控策略改变事件场景的能力。

超级隐私模式支持一键关闭位置、相机和麦克风等敏感器件。该模式管控的器件范围将随版本更新动态调整。应用可通过Device Security Kit提供的接口实时监听超级隐私模式的状态变化及各类隐私传感器的管控策略更新。

## 约束与限制

本特性需要设备上存在超级隐私模式选项。开发者可通过在设备上选择"设置 > 隐私和安全 > 超级隐私模式"查看超级隐私模式选项。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/xVckI88VT0erPKa2bJuA0A/zh-cn_image_0000002742123463.png)

**流程说明：**

1. 开发者应用调用[onSuperPrivacyModeOrPolicyChange](../harmonyos-references/devicesecurity-superprivacymode-api.md#onsuperprivacymodeorpolicychange)接口订阅超级隐私模式管控策略改变事件。
2. Device Security Kit调用回调函数通知开发者应用。
3. 开发者应用根据当前超级隐私模式的状态和控制策略信息进行业务处理。
4. 当开发者应用不需要使用超级隐私模式状态及控制策略信息时，取消订阅超级隐私模式管控策略改变事件。

## 接口说明

以下是超级隐私模式管控策略改变事件的订阅与取消订阅接口，更多接口及使用方法请参见[API参考](../harmonyos-references/devicesecurity-superprivacymode-api.md)。

| 接口名 | 描述 |
| --- | --- |
| [onSuperPrivacyModeOrPolicyChange](../harmonyos-references/devicesecurity-superprivacymode-api.md#onsuperprivacymodeorpolicychange)(callback: Callback<[SuperPrivacyPolicyInfo](../harmonyos-references/devicesecurity-superprivacymode-api.md#superprivacypolicyinfo)>): void | 订阅超级隐私模式或策略变化事件 |
| [offSuperPrivacyModeOrPolicyChange](../harmonyos-references/devicesecurity-superprivacymode-api.md#offsuperprivacymodeorpolicychange)(callback?: Callback<[SuperPrivacyPolicyInfo](../harmonyos-references/devicesecurity-superprivacymode-api.md#superprivacypolicyinfo)>): void | 取消订阅超级隐私模式或策略变化事件 |

## 开发步骤

1. 导入超级隐私模块及相关公共模块。

   ```typescript
   import { superPrivacyMode } from '@kit.DeviceSecurityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 定义超级隐私模式管控策略改变时触发的回调函数。

   ```typescript
   const superPrivacyPolicyChangedCallback = (policyInfo: superPrivacyMode.SuperPrivacyPolicyInfo): void => {
     hilog.info(DOMAIN, TAG, `super privacy mode or policy changed`);
     hilog.info(DOMAIN, TAG, `Super privacy mode = ${policyInfo.superPrivacyMode}`);
     hilog.info(DOMAIN, TAG, `Super privacy policies = ${JSON.stringify(policyInfo.superPrivacyPolicies)}`);
     // ...
   }
   ```
3. 调用[onSuperPrivacyModeOrPolicyChange](../harmonyos-references/devicesecurity-superprivacymode-api.md#onsuperprivacymodeorpolicychange)接口订阅超级隐私模式管控策略改变事件。

   ```typescript
   const DOMAIN = 0x0000;
   const TAG = 'SuperPrivacyModeTest';
   ```

   ```typescript
   hilog.info(DOMAIN, TAG, 'start register super privacy mode or policy changed listener');
   try {
     superPrivacyMode.onSuperPrivacyModeOrPolicyChange(superPrivacyPolicyChangedCallback);
     hilog.info(DOMAIN, TAG, 'register super privacy mode or policy change listener success');
     // ...
   } catch (err) {
     hilog.error(DOMAIN, TAG, `register super privacy mode or policy changed listener failed, errCode:${err?.code}, errMessage:${err?.message}`);
     // ...
   }
   ```
4. 调用[offSuperPrivacyModeOrPolicyChange](../harmonyos-references/devicesecurity-superprivacymode-api.md#offsuperprivacymodeorpolicychange)接口取消订阅超级隐私模式管控策略改变事件。

   ```typescript
   const DOMAIN = 0x0000;
   const TAG = 'SuperPrivacyModeTest';
   ```

   ```typescript
   hilog.info(DOMAIN, TAG, 'start unregister super privacy mode or policy changed listener');
   try {
     superPrivacyMode.offSuperPrivacyModeOrPolicyChange(superPrivacyPolicyChangedCallback);
     hilog.info(DOMAIN, TAG, 'unregister super privacy mode or policy changed listener success');
     // ...
   } catch (err) {
     hilog.error(DOMAIN, TAG, `unregister super privacy mode or policy changed listener failed, errCode:${err?.code}, errMessage:${err?.message}`);
     // ...
   }
   ```
