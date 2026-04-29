---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/app-compatibility-upgrade
title: 应用升级targetSDKVersion兼容低版本指导
breadcrumb: 版本说明 > 应用兼容性说明 > 应用开发中的兼容性场景开发指导 > 应用升级targetSDKVersion兼容低版本指导
category: harmonyos-releases
scraped_at: 2026-04-29T13:25:20+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:93e3e12d1b424435f6165697b036e501f576354148b5e9d9695bcafb5ff08a4a
---

应用的源码工程配置项（build-profile.json5文件）中通过targetSdkVersion和compatibleSdkVersion定义了应用运行的目标SDK版本和最低SDK版本。

推荐开发者适配最新发布的API版本，即推荐开发者配置targetSDKVersion和CompileSdkVersion一样，享受到最新版本特性。开发者可根据自身实际情况升级targetSDKVersion。

部分应用升级targetSDKVersion时，可能不升级compatibleSdkVersion，下面介绍这种场景如何进行兼容性适配。

例如：接口A在SDK版本5.0.2(14)产生行为变更并进行了版本隔离，应用升级targetSDKVersion≥5.0.2(14)并适配了新版本行为， compatibleSdkVersion还保持设置为5.0.1(13)， 则若应用分发到低版本设备5.0.1(13)上，需保证该应用在低版本设备能够兼容运行正常（如下图所示）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/AwG3E2qPSAaE0CmqrlfkkA/zh-cn_image_0000002448697365.png?HW-CC-KV=V1&HW-CC-Date=20260429T052520Z&HW-CC-Expire=86400&HW-CC-Sign=E238D7423616961FB384BB645B0179BCB75A7224F43331004316D992A469F6E2 "点击放大")

这种场景开发者可以使用如下方式进行兼容处理：

## 基于C/ArkTS语言API接口兼容低版本行为

* 针对HarmonyOS设备独有特性接口，即接口标记为since M.F.S(N)（文档中标记“起始版本：M.F.S(N)”, SDK物理包中hms路径下所包含的接口），使用distributionOSApiVersion接口进行兼容性判断保护。

  ArkTS API:

  ```
  1. import { deviceInfo } from '@kit.BasicServicesKit';
  2. //针对HarmonyOS专有接口，即接口标记为since M.F.S(N)的接口
  3. getTestData(): void {
  4. // 兼容性判断，50002是由新接口的since字段M*10000+F*100+S转换而来
  5. if (deviceInfo.distributionOSApiVersion >=  50002) {
  6. // 适配5.0.2(14)版本某API行为变更后的处理
  7. } else {
  8. // 兼容原有逻辑
  9. }
  10. }
  ```

  C API：

  ```
  1. #include <deviceinfo.h>
  2. #include <stdio.h>
  3. //针对HarmonyOS专有接口，即接口标记为since M.F.S(N)的接口
  4. void GetTestData() {
  5. // 兼容性判断，50002是由新接口的since字段M*10000+F*100+S转换而来
  6. if (OH_GetDistributionOSApiVersion() >=  50002) {
  7. // 适配5.0.2(14)版本某API行为变更后的处理
  8. } else {
  9. // 兼容原有逻辑
  10. }
  11. }
  ```
* 针对OpenHarmony底座接口，即接口标记为since N（文档中标记“起始版本：N”，SDK物理包中openharmony路径下所包含的接口），使用sdkApiVersion接口进行兼容性判断保护。

  ArkTS API:

  ```
  1. import { deviceInfo } from '@kit.BasicServicesKit';
  2. //针对OpenHarmony底座公共接口，即接口标记为since N
  3. getTestData(): void {
  4. // 增加兼容性判断
  5. if (deviceInfo.sdkApiVersion >= 14) {
  6. // 适配5.0.2(14)版本某API行为变更后的处理
  7. } else {
  8. // 兼容原有逻辑
  9. }
  10. }
  ```

  C API：

  ```
  1. #include <deviceinfo.h>
  2. #include <stdio.h>
  3. //针对OpenHarmony底座公共接口，即接口标记为since N
  4. void GetTestData() {
  5. // 增加兼容性判断
  6. if (OH_GetSdkApiVersion() >=  14) {
  7. // 适配5.0.2(14)版本某API行为变更后的处理
  8. } else {
  9. // 兼容原有逻辑
  10. }
  11. }
  ```
