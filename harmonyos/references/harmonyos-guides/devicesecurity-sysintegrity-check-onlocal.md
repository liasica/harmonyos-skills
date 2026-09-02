---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-sysintegrity-check-onlocal
title: 本地系统完整性检测
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 安全检测 > 本地系统完整性检测
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:30+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:be9866e155bd0bbdb941d0edf75aceb00291f9c3b3eb30bfdd1efa835e380433
---

## 场景介绍

在不接入服务端的场景下，应用通过调用Device Security Kit的[checkSysIntegrityOnLocal](../harmonyos-references/devicesecurity-safetydetectenhanced-api.md#safetydetectchecksysintegrityonlocal)接口获取系统完整性检测结果，用于判断设备环境是否安全，比如是否被越狱、非真实设备等。

应用可以根据检测结果评估如何进行业务操作。

**说明** 

* 系统完整性检测结果可以用作系统整体安全的一个环节，需要考虑检测结果误报带来的风险以及给用户带来的影响，不建议将系统完整性检测结果作为判断当前设备是否安全的唯一依据，更好的做法是通过额外的步骤降低风险。
* 该功能仅在无法接入服务端的场景下使用。

## 约束与限制

* 本地系统完整性检测能力支持Phone、Tablet、PC/2in1、Wearable设备。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/wKISD141SSKniIw1dU3eGQ/zh-cn_image_0000002706834286.png)

**流程说明：**

1. 开发者应用调用[checkSysIntegrityOnLocal](../harmonyos-references/devicesecurity-safetydetectenhanced-api.md#safetydetectchecksysintegrityonlocal)接口，发起本地系统完整性检测请求。
2. Device Security Kit收到请求后，采集系统完整性检测数据，检测系统完整性。
3. 通过[checkSysIntegrityOnLocal](../harmonyos-references/devicesecurity-safetydetectenhanced-api.md#safetydetectchecksysintegrityonlocal)接口将检测结果返回给开发者应用。
4. 开发者应用可以根据检测结果进行业务处理。当本地系统完整性检测结果为false时，请进一步判断detail中的具体风险分类，您可以根据风险分类以及自身功能对安全的要求决定是否提醒用户。

**说明** 

* 本地系统完整性检测结果可以用作系统整体安全的一个环节，需要考虑检测结果误报带来的风险以及给用户带来的影响，不建议将本地系统完整性检测结果作为判断当前设备是否安全的唯一依据，更好的做法是通过额外的步骤降低风险。
* 如果需要在应用中提醒用户，为了提升用户体验，建议采用友好的提示语，可参考：

  您的设备疑似存在风险或运行在不安全环境中，请谨慎使用xxx功能。

## 接口说明

以下是系统完整性检测相关接口，包括ArkTS API，更多接口及使用方法请参见[API参考](../harmonyos-references/devicesecurity-safetydetectenhanced-api.md#safetydetectchecksysintegrityonlocal)。

| 接口名 | 描述 |
| --- | --- |
| [checkSysIntegrityOnLocal](../harmonyos-references/devicesecurity-safetydetectenhanced-api.md#safetydetectchecksysintegrityonlocal)(): Promise<string> | 检测系统完整性 |

## 开发步骤

**说明** 

请确保已打开“[安全检测服务](devicesecurity-deviceverify-activateservice.md)”开关并[申请Profile](../app/agc-help-profile-0000002270709473.md)。

1. 导入Device Security Kit模块及相关公共模块。

   ```typescript
   import { safetyDetect } from '@kit.DeviceSecurityKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 调用[checkSysIntegrityOnLocal](../harmonyos-references/devicesecurity-safetydetectenhanced-api.md#safetydetectchecksysintegrityonlocal)接口获取本地系统完整性检测结果。

   ```typescript
   const TAG = 'SafetyDetectJsTest';

   // 请求本地系统完整性检测，并处理结果
   try {
     hilog.info(0x0000, TAG, 'CheckSysIntegrityOnLocal begin.');
     const result: string = await safetyDetect.checkSysIntegrityOnLocal();
     hilog.info(0x0000, TAG, 'Succeeded in checkSysIntegrityOnLocal: %{public}s', result);
     // ...
   } catch (err) {
     let e: BusinessError = err as BusinessError;
     hilog.error(0x0000, TAG, 'CheckSysIntegrityOnLocal failed: %{public}d %{public}s', e.code, e.message);
     // ...
   }
   ```
3. 开发者应用可以根据检测结果进行业务处理，当本地系统完整性检测结果为false时，您可以根据自身功能对安全的要求决定是否提醒用户。
