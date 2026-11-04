---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-child-process
title: 调试Native子进程
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 调试Native子进程
category: harmonyos-guides
scraped_at: 2026-11-04T08:31:28+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:32f1a6ecc6378e0dc50bbacede254dddf073265c1aea3b238c5dea311753d4d6
---

从26.0.0版本开始，DevEco Studio支持对[Native子进程](capi-nativechildprocess-development-guideline.md)进行调试，包括OH\_Ability\_StartNativeChildProcess和OH\_Ability\_CreateNativeChildProcess接口创建的Native子进程。

## 使用约束

* 支持API 26.0.0及以上版本的2in1设备。
* 通过OH\_Ability\_StartNativeChildProcess接口创建Native子进程时，不支持调试[隔离模式](../harmonyos-references/capi-native-child-process-h.md#oh_ability_childprocessconfigs_setisolationmode)（NCP\_ISOLATION\_MODE\_ISOLATED = 1）的Native子进程。
* 通过OH\_Ability\_CreateNativeChildProcess接口创建Native子进程时，不支持调试[独立uid](../harmonyos-references/capi-native-child-process-h.md#oh_ability_childprocessconfigs_setisolationuid)的Native子进程。

## 调试方式

通过attach方式对Native子进程进行调试，在attach窗口中直接选择子进程进行调试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/b2fTi4OrTFCiTzt4x_CrCQ/zh-cn_image_0000002731381977.png)

或者先attach调试主进程，再点击调试面板的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/oxfTXq3sR8Wa1VTrkMsqNg/zh-cn_image_0000002701662750.png)，打开attach窗口选择子进程进行调试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/Ypofp4y-Twi9BYRjJqMlFQ/zh-cn_image_0000002701822674.png)
