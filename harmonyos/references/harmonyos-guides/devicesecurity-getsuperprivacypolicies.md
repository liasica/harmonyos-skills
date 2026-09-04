---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-getsuperprivacypolicies
title: 查询超级隐私模式管控策略
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 超级隐私模式 > 查询超级隐私模式管控策略
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a86c764365c6eab2fd470a07172457ce76cb382f030cf992ecb8f48067edf23d
---

## 场景介绍

从26.0.0开始，超级隐私模式新增查询设备当前的超级隐私管控策略信息的功能。

超级隐私模式支持一键关闭位置、相机和麦克风等敏感器件。该模式管控的器件范围将随版本更新动态调整。应用可通过Device Security Kit提供的接口获取超级隐私模式的状态及各类隐私传感器的管控策略。

## 约束与限制

本特性需要设备上存在超级隐私模式选项。开发者可通过在设备上选择"设置 > 隐私和安全 > 超级隐私模式"查看超级隐私模式选项。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/YBB2kcArSMynAG6Coe4rrg/zh-cn_image_0000002742003501.png)

**流程说明：**

1. 开发者应用调用[getSuperPrivacyPolicies](../harmonyos-references/devicesecurity-superprivacymode-api.md#getsuperprivacypolicies)接口查询当前超级隐私模式状态及控制策略信息。
2. Device Security Kit收到请求后，返回当前超级隐私模式状态及各隐私传感器控制策略给开发者应用。
3. 开发者应用根据返回的超级隐私模式状态和控制策略信息进行业务处理。

## 接口说明

以下是超级隐私管控策略查询接口，更多接口及使用方法请参见[API参考](../harmonyos-references/devicesecurity-superprivacymode-api.md)。

| 接口名 | 描述 |
| --- | --- |
| [getSuperPrivacyPolicies](../harmonyos-references/devicesecurity-superprivacymode-api.md#getsuperprivacypolicies)() : Promise<[SuperPrivacyPolicyInfo](../harmonyos-references/devicesecurity-superprivacymode-api.md#superprivacypolicyinfo)> | 查询当前超级隐私模式状态及控制策略信息。 |

## 开发步骤

1. 导入超级隐私模块及相关公共模块。

   ```typescript
   import { superPrivacyMode } from '@kit.DeviceSecurityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 调用[getSuperPrivacyPolicies](../harmonyos-references/devicesecurity-superprivacymode-api.md#getsuperprivacypolicies)接口查询超级隐私模式状态及控制策略信息。

   ```typescript
   const DOMAIN = 0x0000;
   const TAG = 'SuperPrivacyModeTest';
   ```

   ```typescript
   try {
     const policyInfo = await superPrivacyMode.getSuperPrivacyPolicies();
     hilog.info(DOMAIN, TAG, `Super privacy mode = ${policyInfo.superPrivacyMode}`);
     hilog.info(DOMAIN, TAG, `Super privacy policies = ${JSON.stringify(policyInfo.superPrivacyPolicies)}`);
     // ...
   } catch (err) {
     hilog.error(DOMAIN, TAG, `call getSuperPrivacyPolicies interface failed, errCode:${err?.code}, errMessage:${err?.message}`);
     // ...
   }
   ```
