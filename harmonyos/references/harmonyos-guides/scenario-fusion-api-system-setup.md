---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-api-system-setup
title: 通过API获取系统设置属性
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > 场景化API > 通过API获取系统设置属性
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:32+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:551d7196ecb6aef6a11995973ac5836f378156d94a2d98f74b61892940323e5a
---

## 场景介绍

Scenario Fusion Kit提供获取系统设置属性API，调用该接口可以获取蓝牙、定位、Wi-Fi开关信息，以及设备方向信息等系统信息属性。

## 约束与限制

场景化API支持Phone、Tablet和PC/2in1设备，并且从5.1.0(18)版本开始，新增支持Wearable和TV设备。

## 接口说明

以下是获取系统设置属性的接口说明，更多接口及使用方法请参见[atomicService（融合场景化API）](../harmonyos-references/scenario-fusion-atomicservice.md)。

| 接口名 | 描述 |
| --- | --- |
| [getSystemSetting](../harmonyos-references/scenario-fusion-atomicservice.md#getsystemsetting)(properties?: Array<[SystemSettingType](../harmonyos-references/scenario-fusion-atomicservice.md#systemsettingtype)>): [SystemSettingInfo](../harmonyos-references/scenario-fusion-atomicservice.md#systemsettinginfo) | 获取系统设置属性的方法，支持获取蓝牙、定位、Wi-Fi开关信息，以及设备方向信息的请求对象。 |

## 开发步骤

1. 导入Scenario Fusion Kit模块以及相关公共模块。

   ```typescript
   import { atomicService } from '@kit.ScenarioFusionKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 传入属性参数，调用接口获取对应属性值，代码如下：

   ```typescript
   let stateArray: atomicService.SystemSettingType[] =
     ['bluetoothEnabled', 'locationEnabled', 'deviceOrientation', 'wifiEnabled'];
   try {
     let data = atomicService.getSystemSetting(stateArray);
     hilog.info(0x0000, 'testTag', 'succeeded in getting system setting info');
     // 当前参数未调用，开发者自行实现参数的逻辑处理
     let bluetoothEnabled: boolean | undefined = data.bluetoothEnabled;
     let locationEnabled: boolean | undefined = data.locationEnabled;
     let deviceOrientation: string | undefined = data.deviceOrientation;
     let wifiEnabled: boolean | undefined = data.wifiEnabled;
   } catch (error) {
     hilog.error(0x0001, 'testTag', 'Failed to get system setting info, failReason: %{public}d %{public}s', error.code, error.message);
   }
   ```
