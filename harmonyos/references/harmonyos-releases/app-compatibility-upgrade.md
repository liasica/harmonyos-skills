---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/app-compatibility-upgrade
title: 应用升级targetSDKVersion兼容低版本指导
breadcrumb: 版本说明 > 应用升级适配与兼容性 > 应用兼容性说明 > 应用开发中的兼容性场景开发指导 > 应用升级targetSDKVersion兼容低版本指导
category: harmonyos-releases
scraped_at: 2026-09-02T14:59:07+08:00
doc_updated_at: 2026-07-06
content_hash: sha256:9bcbd70fb3eef77aaba14b03862a91117d2ee139760fc084f9bec47a08315d56
---

**说明** 

API版本号格式从26.0.0开始进行调整（详见[版本号格式调整说明](version-number-26.md)），不影响对API兼容性判断的基本逻辑，因此在文档的示意性描述中暂时仍保持旧版本格式的说明。

近期API版本号的大小关系如下：

26.0.0 > 6.1.1(24) > 6.1.0(23) > 6.0.2(22) > 6.0.1(21) > 6.0.0(20) > 5.1.1(19) > 5.1.0(18) > 5.0.5(17)

应用的源码工程配置项（build-profile.json5文件）中通过targetSdkVersion和compatibleSdkVersion定义了应用运行的目标SDK版本和最低SDK版本。

推荐开发者适配最新发布的API版本，即推荐开发者配置targetSDKVersion和CompileSdkVersion一样，享受到最新版本特性。开发者可根据自身实际情况升级targetSDKVersion。

部分应用升级targetSDKVersion时，可能不升级compatibleSdkVersion，下面介绍这种场景如何进行兼容性适配。

例如：接口A在SDK版本5.0.2(14)产生行为变更并进行了版本隔离，应用升级targetSDKVersion≥5.0.2(14)并适配了新版本行为， compatibleSdkVersion还保持设置为5.0.1(13)， 则若应用分发到低版本设备5.0.1(13)上，需保证该应用在低版本设备能够兼容运行正常（如下图所示）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/prNNt8xaThGqmbzp3tBBkA/zh-cn_image_0000002448697365.png "点击放大")

这种场景开发者可以使用如下方式进行兼容处理：

## 基于C/ArkTS语言API接口兼容低版本行为

* 针对HarmonyOS设备独有特性接口，即接口标记为since M.F.S(N)（文档中标记“起始版本：M.F.S(N)”, SDK物理包中hms路径下所包含的接口），使用distributionOSApiVersion接口进行兼容性判断保护。

  ArkTS API:

  ```screen
  import { deviceInfo } from '@kit.BasicServicesKit';
  //针对HarmonyOS专有接口，即接口标记为since M.F.S(N)的接口
  getTestData(): void {
      // 兼容性判断，50002是由新接口的since字段M*10000+F*100+S转换而来
      if (deviceInfo.distributionOSApiVersion >=  50002) {
          // 适配5.0.2(14)版本某API行为变更后的处理
      } else {
          // 兼容原有逻辑
      }
  }
  ```

  C API：

  ```screen
  #include <deviceinfo.h>
  #include <stdio.h>
  //针对HarmonyOS专有接口，即接口标记为since M.F.S(N)的接口
  void GetTestData() {
      // 兼容性判断，50002是由新接口的since字段M*10000+F*100+S转换而来
      if (OH_GetDistributionOSApiVersion() >=  50002) {
          // 适配5.0.2(14)版本某API行为变更后的处理
      } else {
          // 兼容原有逻辑
      }
  }
  ```
* 针对OpenHarmony底座接口，即接口标记为since N（文档中标记“起始版本：N”，SDK物理包中openharmony路径下所包含的接口），使用sdkApiVersion接口进行兼容性判断保护。

  ArkTS API:

  ```screen
  import { deviceInfo } from '@kit.BasicServicesKit';
  //针对OpenHarmony底座公共接口，即接口标记为since N
  getTestData(): void {
      // 增加兼容性判断
      if (deviceInfo.sdkApiVersion >= 14) {
          // 适配5.0.2(14)版本某API行为变更后的处理
      } else {
          // 兼容原有逻辑
      }
  }
  ```

  C API：

  ```screen
  #include <deviceinfo.h>
  #include <stdio.h>
  //针对OpenHarmony底座公共接口，即接口标记为since N
  void GetTestData() {
      // 增加兼容性判断
      if (OH_GetSdkApiVersion() >=  14) {
          // 适配5.0.2(14)版本某API行为变更后的处理
      } else {
          // 兼容原有逻辑
      }
  }
  ```
