---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-ubsan
title: 使用UBSan检测未定义行为
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 日志与故障分析 > 故障分析 > 使用UBSan检测未定义行为
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:34+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:20f20741797cc3af1967c5b6c66664377f4952f730092d62aac1d5f3111be262
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

1. 点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/JTUSbI3wRSuEK9IGSJsihw/zh-cn_image_0000002749483796.png)按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/hVhcfVd9RcSLH0i-CHy_0w/zh-cn_image_0000002779082859.png "点击放大")按钮打开配置界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/_s2VbJC4QwaGQeCMFy6r3g/zh-cn_image_0000002778923011.png)
2. 在配置界面点击**故障分析**，勾选**未定义行为检测**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/xwzIL_BIRfGcaBXVnP1cvg/zh-cn_image_0000002779082857.png)

### 方式二

1. 修改工程目录下的AppScope/app.json5文件，添加UBSan配置开关。

   ```screen
    "ubsanEnabled": true
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/vgGeozsIQBq2c9I-pZfvuw/zh-cn_image_0000002749323924.png)
2. 在需要开启UBSan的模块中，通过添加构建参数开启UBSan检测插桩，在对应模块的模块级build-profile.json5中添加命令参数：

   ```screen
   "arguments": "-DOHOS_ENABLE_UBSAN=ON"
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/kGgCxX3GTN-5nXdPfxGY4g/zh-cn_image_0000002749323926.png)

## 使用UBSan

1. 运行或调试当前应用。
2. 当检测出未定义行为时，弹出UBSan log信息，点击信息中的链接即可跳转到未定义行为的代码处。日志中的异常检测类型请参考[UBSan异常检测类型](../best-practices/bpta-stability-ubsan-detection.md#section124211321406)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/jACPTrfJTiS0FGgWJLUlaA/zh-cn_image_0000002778923013.png)
