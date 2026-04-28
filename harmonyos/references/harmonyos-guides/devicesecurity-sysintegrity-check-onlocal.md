---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-sysintegrity-check-onlocal
title: 本地系统完整性检测
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 安全检测 > 本地系统完整性检测
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c7c54c468f744ad9ea329173c16ba1e51a4a1eba18849f85bad217daeadc87fa
---

## 场景介绍

在不接入服务端的场景下，应用通过调用Device Security Kit的checkSysIntegrityOnLocal接口获取系统完整性检测结果，用于判断设备环境是否安全，比如是否被越狱、非真实设备等。

应用可以根据检测结果评估如何进行业务操作。

说明

* 系统完整性检测结果可以用作系统整体安全的一个环节，需要考虑检测结果误报带来的风险以及给用户带来的影响，不建议将系统完整性检测结果作为判断当前设备是否安全的唯一依据，更好的做法是通过额外的步骤降低风险。
* 该功能仅在无法接入服务端的场景下使用。

## 约束与限制

* 本地系统完整性检测能力支持Phone、Tablet、PC/2in1、Wearable设备。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/E-xCt0lSQEmo3egPm7XLNA/zh-cn_image_0000002583478387.png?HW-CC-KV=V1&HW-CC-Date=20260427T234254Z&HW-CC-Expire=86400&HW-CC-Sign=B7C6D73B7F035110711264378AA83D2FB3C8263F62599BCD0ECA5F788E01F874)

**流程说明：**

1. 开发者应用调用checkSysIntegrityOnLocal接口，发起本地系统完整性检测请求。
2. Device Security Kit收到请求后，采集系统完整性检测数据，检测系统完整性。
3. 通过checkSysIntegrityOnLocal接口将检测结果返回给开发者应用。
4. 开发者应用可以根据检测结果进行业务处理。当本地系统完整性检测结果为false时，请进一步判断detail中的具体风险分类，您可以根据风险分类以及自身功能对安全的要求决定是否提醒用户。

说明

* 本地系统完整性检测结果可以用作系统整体安全的一个环节，需要考虑检测结果误报带来的风险以及给用户带来的影响，不建议将本地系统完整性检测结果作为判断当前设备是否安全的唯一依据，更好的做法是通过额外的步骤降低风险。
* 如果需要在应用中提醒用户，为了提升用户体验，建议采用友好的提示语，可参考：

  您的设备疑似存在风险或运行在不安全环境中，请谨慎使用xxx功能。

## 接口说明

以下是系统完整性检测相关接口，包括ArkTS API，更多接口及使用方法请参见[API参考](../harmonyos-references/devicesecurity-safetydetectenhanced-api.md#checksysintegrityonlocal)。

| 接口名 | 描述 |
| --- | --- |
| [checkSysIntegrityOnLocal](../harmonyos-references/devicesecurity-safetydetectenhanced-api.md#checksysintegrityonlocal)(): Promise<string> | 检测系统完整性 |

## 开发步骤

说明

请确保已打开“[安全检测服务](devicesecurity-deviceverify-activateservice.md)”开关并[申请Profile](../app/agc-help-profile-0000002270709473.md)。

1. 导入Device Security Kit模块及相关公共模块。

   ```
   1. import { safetyDetect } from '@kit.DeviceSecurityKit';
   2. import { BusinessError } from '@ohos.base';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 调用接口获取系统完整性检测结果。

   ```
   1. const TAG = "SafetyDetectJsTest";

   3. // 请求本地系统完整性检测，并处理结果
   4. try {
   5. hilog.info(0x0000, TAG, 'CheckSysIntegrityOnLocal begin.');
   6. const result: string = await safetyDetect.checkSysIntegrityOnLocal();
   7. hilog.info(0x0000, TAG, 'Succeeded in checkSysIntegrityOnLocal: %{public}s', result);
   8. } catch (err) {
   9. let e: BusinessError = err as BusinessError;
   10. hilog.error(0x0000, TAG, 'CheckSysIntegrityOnLocal failed: %{public}d %{public}s', e.code, e.message);
   11. }
   ```
3. 开发者应用可以根据检测结果进行业务处理，当本地系统完整性检测结果为false时，您可以根据自身功能对安全的要求决定是否提醒用户。

   本地系统完整性检测结果是一个格式为JSON格式的字符串，内容示例如下：

   ```
   1. {
   2. "basicIntegrity": false,
   3. "detail": [
   4. "attack",
   5. "jailbreak",
   6. "emulator"
   7. ]
   8. }
   ```

   说明

   basicIntegrity：系统完整性检测的结果，true表示检测结果完整，false表示存在风险。

   detail：可选字段，当basicIntegrity结果为false时，该字段将提供存在风险的原因，App开发者可以根据不同风险做出不同的决策，详情如下：

   * jailbreak：设备被越狱。
   * emulator：非真实设备。
   * attack：设备被攻击。
   * unlock：设备被解锁。
