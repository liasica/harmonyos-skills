---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-api-system-info
title: 通过API获取系统信息属性
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > 场景化API > 通过API获取系统信息属性
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:32+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:92198e508c70b17f683d31ce7f4389dc34b41d41a5f043371d70d6d0cc7ca8d2
---

## 场景介绍

Scenario Fusion Kit提供获取系统信息属性API，调用该接口可以获取设备、网络状态、屏幕、语言、主题等系统信息属性。

## 约束与限制

场景化API支持Phone、Tablet和PC/2in1设备，并且从5.1.0(18)版本开始，新增支持Wearable和TV设备。

## 接口说明

以下是获取系统信息属性的接口说明，更多接口及使用方法请参见[atomicService（融合场景化API）](../harmonyos-references/scenario-fusion-atomicservice.md)。

| 接口名 | 描述 |
| --- | --- |
| [getSystemInfoSync](../harmonyos-references/scenario-fusion-atomicservice.md#getsysteminfosync)(properties?: Array<[SystemInfoType](../harmonyos-references/scenario-fusion-atomicservice.md#systeminfotype)>): [SystemInfo](../harmonyos-references/scenario-fusion-atomicservice.md#systeminfo) | 获取系统信息属性的方法，支持获取设备、网络状态、屏幕、语言、主题等系统信息的请求对象，包含请求参数。  **说明：**  getSystemInfoSync接口不支持获取windowWidth、windowHeight、statusBarHeight和screenSafeArea属性，如需获取可使用[getSystemInfo](../harmonyos-references/scenario-fusion-atomicservice.md#getsysteminfo)接口。 |

## 开发步骤

1. 导入Scenario Fusion Kit模块以及相关公共模块。

   ```typescript
   import { atomicService } from '@kit.ScenarioFusionKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 传入属性参数，调用接口获取对应属性值，代码如下：

   ```typescript
   let stateArray: atomicService.SystemInfoType[] =
     ['brand', 'deviceModel', 'screenWidth', 'screenHeight', 'language', 'osFullName', 'fontSizeSetting',
       'sdkApiVersion', 'bluetoothEnabled', 'wifiEnabled', 'locationEnabled', 'deviceOrientation', 'theme'];
   try {
     let data = atomicService.getSystemInfoSync(stateArray);
     hilog.info(0x0000, 'testTag', 'succeeded in getting system info');
     // 当前参数未调用，开发者自行实现参数的逻辑处理
     let brand: string | undefined = data.brand;
     let deviceModel: string | undefined = data.deviceModel;
     let screenWidth: number | undefined = data.screenWidth;
     let screenHeight: number | undefined = data.screenHeight;
     let language: string | undefined = data.language;
     let osFullName: string | undefined = data.osFullName;
     let fontSizeSetting: number | undefined = data.fontSizeSetting;
     let sdkApiVersion: number | undefined = data.sdkApiVersion;
     let bluetoothEnabled: boolean | undefined = data.bluetoothEnabled;
     let wifiEnabled: boolean | undefined = data.wifiEnabled;
     let locationEnabled: boolean | undefined = data.locationEnabled;
     let deviceOrientation: string | undefined = data.deviceOrientation;
     let theme: ColorMode | undefined = data.theme;
   } catch (error) {
     hilog.error(0x0000, 'testTag', 'Failed to get system info, failReason: %{public}d %{public}s', error.code, error.message);
   }
   ```
