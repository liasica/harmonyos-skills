---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-hwasan
title: 使用HWASan检测内存错误
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 日志与故障分析 > 故障分析 > 使用HWASan检测内存错误
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:56+08:00
doc_updated_at: 2026-11-23
content_hash: sha256:e5a07130c1dd0c574e34aad4064e035a2f75f54c5c47585b68987b7b7aeb7fe0
---

HWASan（Hardware-Assisted Address Sanitizer）是一款类似于[ASan](ide-hmos-asan.md)的内存错误检测工具。与ASan相比，HWASan使用的内存减少很多，因而更适合用于整个系统的清理。关于HWASan的检测原理请参考[HWASan检测原理](../best-practices/bpta-stability-address-sanitizer-principle.md#section187526511146)。

在适配过程中，若遇到应用崩溃等问题，可参考[适配常见问题](../best-practices/bpta-stability-address-sanitizer-faq.md)。

## 使用约束

* HWASan检测仅适用于AArch64架构的硬件。
* ASan、TSan、UBSan、HWASan不能同时开启，四个只能开启其中一个。

## 开启HWASan

### 方式一

1. 点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/VxGyDt_zTq6miKgVRU_g6Q/zh-cn_image_0000002791841126.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=F2C8F02EC6CD1D686A84768C4DF85D767017C4C6E741F291917C27DB81BA73B2)按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/yjBf1nkZS9yszefm6rzaMQ/zh-cn_image_0000002792001098.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=B4F94DBE8738C4CE62DD99DB3E7328458BB78F10A00B4067D3EB13BF3DFE21D0 "点击放大")按钮打开配置界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/qegoS2mvQGGPryAA-Mvqkg/zh-cn_image_0000002791841124.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=CE87B2F1394B60FB012EB123CF07F46EF73944269E7FF2CF1409C9EFD4966D63)
2. 在配置界面点击**故障分析**，勾选**硬件辅助地址检测**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/4X40QnY8T7u8BKwW0594aw/zh-cn_image_0000002791841128.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=FD5627D70521F8999BE3F698531590B5C6955B1B1A3133DF66BA34677F10477B)

### 方式二

1. 修改工程目录下的AppScope/app.json5文件，添加HWASan配置开关。

   ```json5
   "hwasanEnabled": true
   ```
2. 在需要开启HWASan的模块级build-profile.json5中，添加构建参数开启HWASan检测插桩。

   ```json5
   "buildOption": {
     "externalNativeOptions": {
       "arguments": ["-DOHOS_ENABLE_HWASAN=ON"]
     }
   }
   ```

## 使用HWASan

1. 运行或调试当前应用。
2. 当程序出现内存错误时，弹出HWASan log信息，点击信息中的链接即可跳转至引起内存错误的代码处。日志中各字段的说明请参考[HWASan日志规格](address-sanitizer-guidelines.md#hwasan日志规格)，异常检测类型请参考[HWASan异常检测类型](../best-practices/bpta-stability-hwasan-detection.md#section207321025115510)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/zBqbYZvLQYyYl4_HdM41PQ/zh-cn_image_0000002820681057.png?HW-CC-KV=V1&HW-CC-Date=20261128T023455Z&HW-CC-Expire=31536000000&HW-CC-Sign=DC193AFB50DA998734A7FE7821AC63E328F0AEBF8CF976514DF7AF98941BCFA7)
