---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-api-system-info
title: 通过API获取系统信息属性
breadcrumb: 指南 > 应用服务 > Scenario Fusion Kit（融合场景服务） > 场景化API > 通过API获取系统信息属性
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9340777896e15dc208e2d9d88ca4fad18485fe2733babfa65f8013c2dc83708c
---

## 场景介绍

Scenario Fusion Kit提供获取系统信息属性API，调用该接口可以获取设备、网络状态、屏幕、语言、主题等系统信息属性。

## 约束与限制

场景化API支持Phone、Tablet和2in1设备，并且从5.1.0(18)版本开始，新增支持Wearable和TV设备。

## 接口说明

以下是获取系统信息属性的接口说明，更多接口及使用方法请参见[atomicService（融合场景化API）](../harmonyos-references/scenario-fusion-atomicservice.md)。

| 接口名 | 描述 |
| --- | --- |
| [getSystemInfoSync](../harmonyos-references/scenario-fusion-atomicservice.md#getsysteminfosync)(properties?: Array<[SystemInfoType](../harmonyos-references/scenario-fusion-atomicservice.md#systeminfotype)>): [SystemInfo](../harmonyos-references/scenario-fusion-atomicservice.md#systeminfo) | 获取系统信息属性的方法，支持获取设备、网络状态、屏幕、语言、主题等系统信息的请求对象，包含请求参数。  **说明：**  getSystemInfoSync接口不支持获取windowWidth、windowHeight、statusBarHeight和screenSafeArea属性，如需获取可使用[getSystemInfo](../harmonyos-references/scenario-fusion-atomicservice.md#getsysteminfo)接口。 |

## 开发步骤

1. 导入Scenario Fusion Kit模块以及相关公共模块。

   ```
   1. import { atomicService } from '@kit.ScenarioFusionKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 传入属性参数，调用接口获取对应属性值，代码如下：

   ```
   1. let stateArray: Array<atomicService.SystemInfoType> =
   2. ['brand', 'deviceModel', 'screenWidth', 'screenHeight', 'language', 'osFullName', 'fontSizeSetting',
   3. 'sdkApiVersion', 'bluetoothEnabled', 'wifiEnabled', 'locationEnabled', 'deviceOrientation', 'theme'];
   4. try {
   5. let data = atomicService.getSystemInfoSync(stateArray);
   6. hilog.info(0x0000, 'testTag', 'succeeded in getting system info');
   7. let brand: string | undefined = data.brand;
   8. let deviceModel: string | undefined = data.deviceModel;
   9. let screenWidth: number | undefined = data.screenWidth;
   10. let screenHeight: number | undefined = data.screenHeight;
   11. let language: string | undefined = data.language;
   12. let osFullName: string | undefined = data.osFullName;
   13. let fontSizeSetting: number | undefined = data.fontSizeSetting;
   14. let sdkApiVersion: number | undefined = data.sdkApiVersion;
   15. let bluetoothEnabled: boolean | undefined = data.bluetoothEnabled;
   16. let wifiEnabled: boolean | undefined = data.wifiEnabled;
   17. let locationEnabled: boolean | undefined = data.locationEnabled;
   18. let deviceOrientation: string | undefined = data.deviceOrientation;
   19. let theme: ColorMode | undefined = data.theme;
   20. } catch (error) {
   21. hilog.error(0x0000, 'testTag', 'failReason: %{public}d %{public}s', error.code, error.message);
   22. }
   ```
