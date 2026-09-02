---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hwasan
title: 使用HWASan检测内存错误
breadcrumb: 指南 > 编写与调试应用 > 日志与故障分析 > 故障分析 > 使用HWASan检测内存错误
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:25+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b3b21eb556342a3eb1f22b4065d7ad8dd2a0fed0038d93c09f25fd214db2c487
---

HWASan（Hardware-Assisted Address Sanitizer）是一款类似于[ASan](ide-asan.md)的内存错误检测工具。与ASan相比，HWASan使用的内存减少很多，因而更适合用于整个系统的检测。关于HWASan的检测原理请参考[HWASan检测原理](../best-practices/bpta-stability-address-sanitizer-principle.md#section187526511146)。

在适配过程中，若遇到应用崩溃等问题，可参考[适配常见问题](../best-practices/bpta-stability-address-sanitizer-faq.md)。

## 使用约束

* HWASan检测仅适用于AArch64架构的硬件。
* ASan、TSan、UBSan、HWASan不能同时开启，只能开启其中一个。

## 开启HWASan

DevEco Studio 6.1.0 Beta1之前的版本，仅支持对C++源码开启HWASan。

从DevEco Studio 6.1.0 Beta1版本开始，同时支持对C++编译生成的无源码so文件进行二进制插桩，进而开启HWASan功能。

### 方式一

1. 点击**Run > Edit Configurations > Diagnostics**，勾选**Hardware-Assisted Address Sanitizer**开启C++源码检测插桩。

   从DevEco Studio 6.1.0 Beta1版本开始，可以同时勾选**BinXO check**，开启无源码的so文件的HWASan检测插桩。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/2L5zLv5ISnKRGa_KR_DQyg/zh-cn_image_0000002701663452.png)
2. （可选）如果部分无源码so不需要进行HWASan检测插桩，可以在工程级或模块级build-profile.json5文件中，配置excludeSoFromBinXO字段，填写需要忽略的so列表，支持正则匹配。

   ```json5
   "buildOption": {
     "nativeLib": {
       "excludeSoFromBinXO": ["**/liblibrary.so"]
     }
   }
   ```

### 方式二

1. 修改工程目录下的AppScope/app.json5文件，添加HWASan配置开关。

   ```json5
   "hwasanEnabled": true
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/ZWHCDU9iQAiWQvygCAAcvw/zh-cn_image_0000002731382677.png)
2. 在需要开启HWASan的模块级build-profile.json5中，添加构建参数开启HWASan检测插桩。

   ```json5
   // DevEco Studio 6.1.0 Beta1以下版本
   "buildOption": {
     "externalNativeOptions": {
       "arguments": ["-DOHOS_ENABLE_HWASAN=ON"]
     }
   // DevEco Studio 6.1.0 Beta1及以上版本，同时开启有源码和无源码的C++的HWASan检测插桩
   "buildOption": {
     "externalNativeOptions": {
       "arguments": ["-DOHOS_ENABLE_HWASAN=ON", "-DOHOS_ENABLE_BINXO=ON"]
     }
   ```
3. 如果部分无源码so不需要进行HWASan检测插桩，可以在工程级或模块级build-profile.json5文件中，配置excludeSoFromBinXO字段，填写需要忽略的so列表，支持正则匹配。

   ```json5
   "buildOption": {
     "nativeLib": {
       "excludeSoFromBinXO": ["**/liblibrary.so"]
     }
   }
   ```

## 使用HWASan

1. 运行或调试当前应用。
2. 当程序出现内存错误时，弹出HWASan log信息，点击信息中的链接即可跳转至引起内存错误的代码处。日志中各字段的说明请参考[HWASan日志规格](address-sanitizer-guidelines.md#hwasan日志规格)，异常检测类型请参考[HWASan异常检测类型](../best-practices/bpta-stability-hwasan-detection.md#section207321025115510)。

   从26.0.0版本开始，支持解析错误堆栈对应的伪代码、方法入参及变量的名称、值。仅解析前三行堆栈（#0~#2），其中#0行会解析入参、变量的名称和值，另外两行（#1、#2）仅解析入参和变量名称。

   为确保正确解析堆栈，需保留代码中的调试信息，具体请参考[注意事项](ide-hwasan.md#section1665820539148)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/VWkZsGp_TMOBsq--4_bC4w/zh-cn_image_0000002731542647.png)
3. 如果是release应用，本地无工程代码，可以使用AnalyzeStackTrace功能，提供要解析堆栈的so，解析结果为源码地址。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/0FAhEDmPT6yTOw2w9UTa7A/zh-cn_image_0000002701823374.png)

## 注意事项

为确保正确解析堆栈，需保留代码中的调试信息，请遵循以下配置。

1. 引用har包时，需在har的build-profile.json5中配置strip参数为false。

   ```json5
   "nativeLib": {
     "debugSymbol": {
       "strip": false
     }
   }
   ```
2. 编译优化可能会清除代码中的调试信息，请在CMakeLists.txt文件中配置关闭编译优化选项的参数。

   ```txt
   set_source_files_properties(
       filename.cpp
       PROPERTIES COMPILE_FLAGS "-O0"
   )
   string(REPLACE "-O2" "-O0"
       CMAKE_CXX_FLAGS_RELEASE
       "${CMAKE_CXX_FLAGS_RELEASE}"
   )
   string(REPLACE "-O2" "-O0"
       CMAKE_C_FLAGS_RELEASE
       "${CMAKE_C_FLAGS_RELEASE}"
   )
   ```
