---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-ubsan
title: 使用UBSan检测未定义行为
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 日志与故障分析 > 故障分析 > 使用UBSan检测未定义行为
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:476a1bd9c6cfe21c13d6d3a590a67b233baf92c1c188b138289a454818b1ccfb
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

1. 点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/mtv-WObiTk-jPEPZTmGSTg/zh-cn_image_0000002781311260.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=6E0754571FD823ECF118E871FCFE996E1829E6EC6D37346CA6CD2EBA7B515F07)按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/9mjrgzHeTyuQOIqvfCIb2w/zh-cn_image_0000002781471196.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=7435F13AF2BA209D0EBD331F91ADE71E828B8EB42F10A9548A0BBC615AC446AB "点击放大")按钮打开配置界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/6E1WUYrnQCW-Q2LTAcHHBw/zh-cn_image_0000002781311262.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=6162D6CAC32A272E649C05C0630E4E8EE6FB8654AA375C988BFE8ABC689DA303)
2. 在配置界面点击**故障分析**，勾选**未定义行为检测**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/3JCrVllfT-G0f9o_uPuBrQ/zh-cn_image_0000002781471192.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=889D1AB9E17146061A858EAE90C7E7964796A27FFD89BD964F0C1C301400391E)

### 方式二

1. 修改工程目录下的AppScope/app.json5文件，添加UBSan配置开关。

   ```screen
    "ubsanEnabled": true
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/j25DAbaOTMKZEKX-xoOOww/zh-cn_image_0000002781471194.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=D75EDE8DC4C05827B99CADA4C053FC2F5BF3B8B179FE3B45CD2C60D10D5C9EF3)
2. 在需要开启UBSan的模块中，通过添加构建参数开启UBSan检测插桩，在对应模块的模块级build-profile.json5中添加命令参数：

   ```screen
   "arguments": "-DOHOS_ENABLE_UBSAN=ON"
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/iKhkGDAcSn-y2L9k4pzp6A/zh-cn_image_0000002781311264.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=696A1E8F74FF48AF6AC8195CD59FF1049FB6DDE474074E83B30898D3EBA6D913)

## 使用UBSan

1. 运行或调试当前应用。
2. 当检测出未定义行为时，弹出UBSan log信息，点击信息中的链接即可跳转到未定义行为的代码处。日志中的异常检测类型请参考[UBSan异常检测类型](../best-practices/bpta-stability-ubsan-detection.md#section124211321406)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/a1LlDhfaQhGCZsgRaH5h0Q/zh-cn_image_0000002781471198.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=8A4D26184428FC8C01471241BA4A57EF9199062AE1ABAE7A8387A13230BC09CE)
