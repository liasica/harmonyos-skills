---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-hwasan
title: 使用HWASan检测内存错误
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 日志与故障分析 > 故障分析 > 使用HWASan检测内存错误
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:46+08:00
doc_updated_at: 2026-11-23
content_hash: sha256:f2380fcc278f46c610ed2a838a9cd96c17a612f3f4315eeae55cf510ae2322bf
---

HWASan（Hardware-Assisted Address Sanitizer）是一款类似于[ASan](ide-hmos-asan.md)的内存错误检测工具。与ASan相比，HWASan使用的内存减少很多，因而更适合用于整个系统的清理。关于HWASan的检测原理请参考[HWASan检测原理](../best-practices/bpta-stability-address-sanitizer-principle.md#section187526511146)。

在适配过程中，若遇到应用崩溃等问题，可参考[适配常见问题](../best-practices/bpta-stability-address-sanitizer-faq.md)。

## 使用约束

* HWASan检测仅适用于AArch64架构的硬件。
* ASan、TSan、UBSan、HWASan不能同时开启，四个只能开启其中一个。

## 开启HWASan

### 方式一

1. 点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/mUlEgSNdQ4iosQ72SjfsGA/zh-cn_image_0000002791841126.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=5F1D576C591739857B534108CFEF255B5A9BA7C3805DEEA96136A30A8898CC5D)按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/T86b5p8iRrWwPFxzH9z62Q/zh-cn_image_0000002792001098.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=ACB86F6864E0138588A6850DE806DD9BD6846A9F2BA409D211C8B00FB5EA0C3A "点击放大")按钮打开配置界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/F0dnyKQKS0CMijkOwNXNcQ/zh-cn_image_0000002791841124.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=36BC88E3CD642F2894B970F0389A20A413FB3E0BD977E7E39CCCA5695E74A8D4)
2. 在配置界面点击**故障分析**，勾选**硬件辅助地址检测**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/P7ovVLphTg685rGRgXSVNg/zh-cn_image_0000002791841128.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=5ECB3A320695B08179DBCD91B7B4D44AF0F042DCA60596A0C86E84BC164D165B)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/MiPjsSnUTj265iTdJCSS6A/zh-cn_image_0000002820681057.png?HW-CC-KV=V1&HW-CC-Date=20261124T044246Z&HW-CC-Expire=31536000000&HW-CC-Sign=F96CDFFD7F13B69F15FCADCD31AF184B0B98C4F31E30AC1FCD8A2E19488AFF17)
