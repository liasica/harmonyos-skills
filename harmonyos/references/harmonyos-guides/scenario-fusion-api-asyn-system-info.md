---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-api-asyn-system-info
title: 通过API异步获取系统信息属性
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a90793ac8f25034d1974f22a2fde7f3aadec53998826df4651f09c6cf2d305c3
---

## 场景介绍

Scenario Fusion Kit提供获取系统信息属性API，调用该接口可以获取设备、网络状态、屏幕、语言、主题等系统信息属性。

## 约束与限制

场景化API支持Phone、Tablet和2in1设备，并且从5.1.0(18)版本开始，新增支持Wearable和TV设备。

## 接口说明

以下是使用Promise异步回调获取系统信息属性的接口说明，更多接口及使用方法请参见[atomicService（融合场景化API）](../harmonyos-references/scenario-fusion-atomicservice.md)。

| 接口名 | 描述 |
| --- | --- |
| [getSystemInfo](../harmonyos-references/scenario-fusion-atomicservice.md#getsysteminfo)(properties?: Array<[SystemInfoType](../harmonyos-references/scenario-fusion-atomicservice.md#systeminfotype)>): Promise<[SystemInfo](../harmonyos-references/scenario-fusion-atomicservice.md#systeminfo)> | 获取系统信息属性的方法，支持获取设备、网络状态、屏幕、语言、主题等系统信息的请求对象，包含请求参数。 |

## 开发步骤

1. 导入Scenario Fusion Kit模块以及相关公共模块。

   ```
   1. import { atomicService } from '@kit.ScenarioFusionKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { window } from '@kit.ArkUI';
   ```
2. 传入属性参数，调用接口获取对应属性值，代码如下：

   ```
   1. let stateArray: Array<atomicService.SystemInfoType> =
   2. ['brand', 'deviceModel', 'screenWidth', 'screenHeight', 'statusBarHeight', 'screenSafeArea', 'language', 'osFullName',
   3. 'fontSizeSetting', 'sdkApiVersion', 'bluetoothEnabled', 'wifiEnabled', 'locationEnabled', 'deviceOrientation',
   4. 'theme', 'windowWidth', 'windowHeight'];
   5. try {
   6. atomicService.getSystemInfo(stateArray).then((data: atomicService.SystemInfo) => {
   7. hilog.info(0x0000, 'testTag', 'succeeded in getting system info asynchronously');
   8. let brand: string | undefined = data.brand;
   9. let deviceModel: string | undefined = data.deviceModel;
   10. let screenWidth: number | undefined = data.screenWidth;
   11. let screenHeight: number | undefined = data.screenHeight;
   12. let statusBarHeight: number | undefined = data.statusBarHeight;
   13. let screenSafeArea: window.AvoidArea | undefined = data.screenSafeArea;
   14. let language: string | undefined = data.language;
   15. let osFullName: string | undefined = data.osFullName;
   16. let fontSizeSetting: number | undefined = data.fontSizeSetting;
   17. let sdkApiVersion: number | undefined = data.sdkApiVersion;
   18. let bluetoothEnabled: boolean | undefined = data.bluetoothEnabled;
   19. let wifiEnabled: boolean | undefined = data.wifiEnabled;
   20. let locationEnabled: boolean | undefined = data.locationEnabled;
   21. let deviceOrientation: string | undefined = data.deviceOrientation;
   22. let theme: ColorMode | undefined = data.theme;
   23. let windowWidth: number | undefined = data.windowWidth;
   24. let windowHeight: number | undefined = data.windowHeight;
   25. }).catch((error: BusinessError) => {
   26. hilog.error(0x0000, 'testTag', 'Promise error: %{public}d %{public}s', error.code, error.message);
   27. })
   28. } catch (error) {
   29. hilog.error(0x0000, 'testTag', 'failReason: %{public}d %{public}s', error.code, error.message);
   30. }
   ```
