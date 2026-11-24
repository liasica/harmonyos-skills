---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-ubsan
title: 使用UBSan检测未定义行为
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 日志与故障分析 > 故障分析 > 使用UBSan检测未定义行为
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:46+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:16969a661c713389e321e32cbd21c41ea3394e7164e48d2f6b9d707f8bd6d06d
---

代码中出现未定义行为，最初可能不会产生任何问题，但是随着代码的复杂度提高，未定义行为可能造成程序崩溃或发生错误，检测出根源会变得更加困难。UBSan（Undefined Behavior Sanitizer）可以检测代码中出现的未定义行为，帮助用户清除未定义行为引起的运行时错误。

常见的未定义行为有：

* 除数为零。
* 使用未对齐的指针，或未对齐的引用。
* 浮点数转换导致的溢出。
* 访问空指针。

## 使用约束

ASan、TSan、UBSan、HWASan不能同时开启，四个只能开启其中一个。

## 开启UBSan

可通过以下两种方式开启UBSan。

### 方式一

1. 点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/ltXAms8UTuay1gX0SUvacA/zh-cn_image_0000002791841252.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=93F657F41014486E025232A7361EB895F739986B2A1D870E21275879FB8B5E51)按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/T0R2XMJ9RryfS4KgVYphEg/zh-cn_image_0000002820721197.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=EFDBFD32CF34B9B3BC44BC7DD09CEC4330AADCF972582A07204DF7D09B676B2E "点击放大")按钮打开配置界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/Dn9g5DqvS16tqdGbtS_zJg/zh-cn_image_0000002820681185.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=39C031D9215E4E194CF415EEAC896624942A458F5EB3BC477CF208DC57112F47)
2. 在配置界面点击**故障分析**，勾选**未定义行为检测**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/ySCssZN_QEmUjuoCw1Egbw/zh-cn_image_0000002792001222.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=8F28EF3613ABD63654AA079ABA43102A9C15A58367ECA8A4AA8B081A28659CA8)

### 方式二

1. 修改工程目录下的AppScope/app.json5文件，添加UBSan配置开关。

   ```screen
    "ubsanEnabled": true
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/m1pMBsE0RNuOZxZ-nHseqA/zh-cn_image_0000002792001226.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=988772854474F4E20C159FF6FED583D44C0CB5B5442E5755E5C53AB5FEFDAF9A)
2. 在需要开启UBSan的模块中，通过添加构建参数开启UBSan检测插桩，在对应模块的模块级build-profile.json5中添加命令参数：

   ```screen
   "arguments": "-DOHOS_ENABLE_UBSAN=ON"
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/VFSBEhpPQzamZ7HZqoAfow/zh-cn_image_0000002791841248.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=47E4527B50EB2B548137CD77FBB6E2B5EE90BE0FE00C18A01D24CA439D821D4B)

## 使用UBSan

1. 运行或调试当前应用。
2. 当检测出未定义行为时，弹出UBSan log信息，点击信息中的链接即可跳转到未定义行为的代码处。日志中的异常检测类型请参考[UBSan异常检测类型](../best-practices/bpta-stability-ubsan-detection.md#section124211321406)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/OsmdhZ5iTBm7mjxURclrvQ/zh-cn_image_0000002791841246.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=6F88975D9685DF323EFE544C4012265320F60422B0D7BEC9B8C89807283E8BCF)
