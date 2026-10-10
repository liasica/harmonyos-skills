---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-hwasan
title: 使用HWASan检测内存错误
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 日志与故障分析 > 故障分析 > 使用HWASan检测内存错误
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:21+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:e033867b7750c0ee8360598dc253779d1c8732dfa6c8dfae98b0648ac434eced
---

HWASan（Hardware-Assisted Address Sanitizer）是一款类似于[Asan](ide-hmos-asan.md)的内存错误检测工具。与ASan相比，HWASan使用的内存减少很多，因而更适合用于整个系统的清理。关于HWASan的检测原理请参考[HWASan检测原理](../best-practices/bpta-stability-address-sanitizer-principle.md#section187526511146)。

在适配过程中，若遇到应用崩溃等问题，可参考[适配常见问题](../best-practices/bpta-stability-address-sanitizer-faq.md)。

## 使用约束

* HWASan检测仅适用于AArch64架构的硬件。
* ASan、TSan、UBSan、HWASan不能同时开启，四个只能开启其中一个。

## 开启HWASan

### 方式一

1. 点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/PsTI3ME6Qs-nd003BT2joA/zh-cn_image_0000002779728997.png)按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/BZjtqc1cSwe15ouUo3A9-Q/zh-cn_image_0000002750009934.png "点击放大")按钮打开配置界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/KRoZUuiqQiyLzlnIMZS9PQ/zh-cn_image_0000002750009936.png)
2. 在配置界面点击**故障分析**，勾选**硬件辅助地址检测**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/EyayiZFFQh-HavxXqzgGoQ/zh-cn_image_0000002779608851.png)

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
   ```

## 使用HWASan

1. 运行或调试当前应用。
2. 当程序出现内存错误时，弹出HWASan log信息，点击信息中的链接即可跳转至引起内存错误的代码处。日志中各字段的说明请参考[HWASan日志规格](address-sanitizer-guidelines.md#hwasan日志规格)，异常检测类型请参考[HWASan异常检测类型](../best-practices/bpta-stability-hwasan-detection.md#section207321025115510)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/-ZdDMBAsR9qKKO6KtZtVKg/zh-cn_image_0000002750169828.png)
