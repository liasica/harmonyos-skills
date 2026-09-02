---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-api-asyn-system-info
title: 通过API异步获取系统信息属性
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > 场景化API > 通过API异步获取系统信息属性
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:32+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:cfb0bcf25f70515a79aaf690e8ab05457d4e882c8111ec73d07c16ede353ce80
---

## 场景介绍

Scenario Fusion Kit提供获取系统信息属性API，调用该接口可以获取设备、网络状态、屏幕、语言、主题等系统信息属性。

## 约束与限制

场景化API支持Phone、Tablet和PC/2in1设备，并且从5.1.0(18)版本开始，新增支持Wearable和TV设备。

## 接口说明

以下是使用Promise异步回调获取系统信息属性的接口说明，更多接口及使用方法请参见[atomicService（融合场景化API）](../harmonyos-references/scenario-fusion-atomicservice.md)。

| 接口名 | 描述 |
| --- | --- |
| [getSystemInfo](../harmonyos-references/scenario-fusion-atomicservice.md#getsysteminfo)(properties?: Array<[SystemInfoType](../harmonyos-references/scenario-fusion-atomicservice.md#systeminfotype)>): Promise<[SystemInfo](../harmonyos-references/scenario-fusion-atomicservice.md#systeminfo)> | 获取系统信息属性的方法，支持获取设备、网络状态、屏幕、语言、主题等系统信息的请求对象，包含请求参数。 |

## 开发步骤

1. 导入Scenario Fusion Kit模块以及相关公共模块。

   ```typescript
   import { atomicService } from '@kit.ScenarioFusionKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { window } from '@kit.ArkUI';
   ```
2. 传入属性参数，调用接口获取对应属性值，代码如下：

   ```typescript
   let stateArray: atomicService.SystemInfoType[] =
     ['brand', 'deviceModel', 'screenWidth', 'screenHeight', 'statusBarHeight', 'screenSafeArea', 'language', 'osFullName',
       'fontSizeSetting', 'sdkApiVersion', 'bluetoothEnabled', 'wifiEnabled', 'locationEnabled', 'deviceOrientation',
       'theme', 'windowWidth', 'windowHeight'];
   try {
     atomicService.getSystemInfo(stateArray).then((data: atomicService.SystemInfo) => {
       hilog.info(0x0000, 'testTag', 'succeeded in getting system info asynchronously');
       // 当前参数未调用，开发者自行实现参数的逻辑处理
       let brand: string | undefined = data.brand;
       let deviceModel: string | undefined = data.deviceModel;
       let screenWidth: number | undefined = data.screenWidth;
       let screenHeight: number | undefined = data.screenHeight;
       let statusBarHeight: number | undefined = data.statusBarHeight;
       let screenSafeArea: window.AvoidArea | undefined = data.screenSafeArea;
       let language: string | undefined = data.language;
       let osFullName: string | undefined = data.osFullName;
       let fontSizeSetting: number | undefined = data.fontSizeSetting;
       let sdkApiVersion: number | undefined = data.sdkApiVersion;
       let bluetoothEnabled: boolean | undefined = data.bluetoothEnabled;
       let wifiEnabled: boolean | undefined = data.wifiEnabled;
       let locationEnabled: boolean | undefined = data.locationEnabled;
       let deviceOrientation: string | undefined = data.deviceOrientation;
       let theme: ColorMode | undefined = data.theme;
       let windowWidth: number | undefined = data.windowWidth;
       let windowHeight: number | undefined = data.windowHeight;
     }).catch((error: BusinessError) => {
       hilog.error(0x0000, 'testTag', 'Promise error: %{public}d %{public}s', error.code, error.message);
     });
   } catch (error) {
     hilog.error(0x0000, 'testTag', 'Failed to get system info asynchronously, failReason: %{public}d %{public}s', error.code, error.message);
   }
   ```
