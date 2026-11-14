---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-hwasan
title: 使用HWASan检测内存错误
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 日志与故障分析 > 故障分析 > 使用HWASan检测内存错误
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:17+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:d1a28577e166e337486caa60ad8234d32faece7e3359662fa794a2c3ebc5c005
---

HWASan（Hardware-Assisted Address Sanitizer）是一款类似于[Asan](ide-hmos-asan.md)的内存错误检测工具。与ASan相比，HWASan使用的内存减少很多，因而更适合用于整个系统的清理。关于HWASan的检测原理请参考[HWASan检测原理](../best-practices/bpta-stability-address-sanitizer-principle.md#section187526511146)。

在适配过程中，若遇到应用崩溃等问题，可参考[适配常见问题](../best-practices/bpta-stability-address-sanitizer-faq.md)。

## 使用约束

* HWASan检测仅适用于AArch64架构的硬件。
* ASan、TSan、UBSan、HWASan不能同时开启，四个只能开启其中一个。

## 开启HWASan

### 方式一

1. 点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/EcQD9dLkSi-7rbI4V0MI1Q/zh-cn_image_0000002810750975.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=FAE5E1FC032E93A3FF707900BF46C52C17A6B75D8B1BADE084F8C170C40881E2)按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/DFXIFdpDR3K6OZHG0V2odQ/zh-cn_image_0000002781311376.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=65821A07A8DCFA6B33C9DB093D8621E8A7B677B76E59DE5B1331CF671ACE8000 "点击放大")按钮打开配置界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/tgn3yULYS2u0EbqElXhFmA/zh-cn_image_0000002810630873.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=52DFF61DF66D74CEE9F4FA8B46E31E983119AF4F4F70DEDD51EF38DE69F366E9)
2. 在配置界面点击**故障分析**，勾选**硬件辅助地址检测**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/SdE9PZd4S-GMQ55CRunv3Q/zh-cn_image_0000002781471316.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=9D8EECA1E0C9CA072C1967D4AA964794ACA211B3856E9500EFDBAA9EC654B2E2)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/fwIX2C1dRXS0gSomYv5sOA/zh-cn_image_0000002810630861.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=C12768CBD0A5F4DDECFAD3A3B601501BBD11A362F95A6D445FCA1CF8E5C37DF2)
