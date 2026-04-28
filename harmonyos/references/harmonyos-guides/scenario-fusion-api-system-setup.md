---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-api-system-setup
title: 通过API获取系统设置属性
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > 场景化API > 通过API获取系统设置属性
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ca91233ecbadbc0fc9cc2ef6e544f592dfff9b8fc5857f725fe5ef40e9fc2348
---

## 场景介绍

Scenario Fusion Kit提供获取系统设置属性API，调用该接口可以获取蓝牙、定位、Wi-Fi开关信息，以及设备方向信息等系统信息属性。

## 约束与限制

场景化API支持Phone、Tablet和2in1设备，并且从5.1.0(18)版本开始，新增支持Wearable和TV设备。

## 接口说明

以下是获取系统设置属性的接口说明，更多接口及使用方法请参见[atomicService（融合场景化API）](../harmonyos-references/scenario-fusion-atomicservice.md)。

| 接口名 | 描述 |
| --- | --- |
| [getSystemSetting](../harmonyos-references/scenario-fusion-atomicservice.md#getsystemsetting)(properties?: Array<[SystemSettingType](../harmonyos-references/scenario-fusion-atomicservice.md#systemsettingtype)>): [SystemSettingInfo](../harmonyos-references/scenario-fusion-atomicservice.md#systemsettinginfo) | 获取系统设置属性的方法，支持获取蓝牙、定位、Wi-Fi开关信息，以及设备方向信息的请求对象。 |

## 开发步骤

1. 导入Scenario Fusion Kit模块以及相关公共模块。

   ```
   1. import { atomicService } from '@kit.ScenarioFusionKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 传入属性参数，调用接口获取对应属性值，代码如下：

   ```
   1. let stateArray: Array<atomicService.SystemSettingType> =
   2. ['bluetoothEnabled', 'locationEnabled', 'deviceOrientation', 'wifiEnabled'];
   3. try {
   4. let data = atomicService.getSystemSetting(stateArray);
   5. hilog.info(0x0000, 'testTag', 'succeeded in getting system setting info');
   6. let bluetoothEnabled: boolean | undefined = data.bluetoothEnabled;
   7. let locationEnabled: boolean | undefined = data.locationEnabled;
   8. let deviceOrientation: string | undefined = data.deviceOrientation;
   9. let wifiEnabled: boolean | undefined = data.wifiEnabled;
   10. } catch (error) {
   11. hilog.error(0x0001, 'testTag', 'failReason: %{public}d %{public}s', error.code, error.message);
   12. }
   ```
