---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-child-process
title: 调试Native子进程
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 调试Native子进程
category: harmonyos-guides
scraped_at: 2026-09-15T07:03:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e1ce5bd547dcdce7538f1a56da03a7c6b180da3b2dbfc818ca79c36e11f29a30
---

从26.0.0版本开始，DevEco Studio支持对[Native子进程](capi-nativechildprocess-development-guideline.md)进行调试，包括OH\_Ability\_StartNativeChildProcess和OH\_Ability\_CreateNativeChildProcess接口创建的Native子进程。

## 使用约束

* 支持API 26.0.0及以上版本的2in1设备。
* 通过OH\_Ability\_StartNativeChildProcess接口创建Native子进程时，不支持调试[隔离模式](../harmonyos-references/capi-native-child-process-h.md#oh_ability_childprocessconfigs_setisolationmode)（NCP\_ISOLATION\_MODE\_ISOLATED = 1）的Native子进程。
* 通过OH\_Ability\_CreateNativeChildProcess接口创建Native子进程时，不支持调试[独立uid](../harmonyos-references/capi-native-child-process-h.md#oh_ability_childprocessconfigs_setisolationuid)的Native子进程。

## 调试方式

通过attach方式对Native子进程进行调试，在attach窗口中直接选择子进程进行调试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/dF62aU-iRtGv3s5cJtgcsw/zh-cn_image_0000002731381977.png)

或者先attach调试主进程，再点击调试面板的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/5NI-GMqWR0Gr-29jQc28vA/zh-cn_image_0000002701662750.png)，打开attach窗口选择子进程进行调试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/-KQXCVh4RrS-jwIDpCZs6Q/zh-cn_image_0000002701822674.png)
