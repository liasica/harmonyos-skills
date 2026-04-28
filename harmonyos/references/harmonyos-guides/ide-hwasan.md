---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hwasan
title: 使用HWASan检测内存错误
breadcrumb: 指南 > 编写与调试应用 > 日志与故障分析 > 故障分析 > 使用HWASan检测内存错误
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bf6dff537630ef0e9836a67ba8534edf72034b940c042e14be0802117e0b0d34
---

HWASan（Hardware-Assisted Address Sanitizer）是一款类似于[ASan](ide-asan.md)的内存错误检测工具。 与ASan相比，HWASan使用的内存减少很多，因而更适合用于整个系统的检测。关于HWASan的检测原理请参考[HWASan检测原理](../best-practices/bpta-stability-address-sanitizer-principle.md#section187526511146)。

## 约束条件

* HWASan检测仅适用于AArch64架构的硬件。
* ASan、TSan、UBSan、HWASan不能同时开启，只能开启其中一个。

## 开启HWASan

DevEco Studio 6.1.0 Beta1之前的版本，仅支持对C++源码开启HWASan。

从DevEco Studio 6.1.0 Beta1版本开始，同时支持对C++编译生成的无源码so文件进行二进制插桩，进而开启HWASan功能。

### 方式一

1. 点击**Run > Edit Configurations > Diagnostics**，勾选**Hardware-Assisted Address Sanitizer**开启C++源码检测插桩。

   从DevEco Studio 6.1.0 Beta1版本开始，可以同时勾选**BinXO check**，开启无源码的so文件的HWASan检测插桩。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/J83B5xtQScuuimHUKpIvNQ/zh-cn_image_0000002561833227.png?HW-CC-KV=V1&HW-CC-Date=20260427T235657Z&HW-CC-Expire=86400&HW-CC-Sign=3CB1342B70FD5615A43B70204A1CADFD9A19C4407CD887846F4FE439D83D0C16)
2. （可选）如果部分无源码so不需要进行HWASan检测插桩，可以在工程级或模块级build-profile.json5文件中，配置excludeSoFromBinXO字段，填写需要忽略的so列表，支持正则匹配。

   ```
   1. "buildOption": {
   2. "nativeLib": {
   3. "excludeSoFromBinXO": ["**/liblibrary.so"]
   4. }
   5. }
   ```

### 方式二

1. 修改工程目录下的AppScope/app.json5文件，添加HWASan配置开关。

   ```
   1. "hwasanEnabled": true
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/74SDS46GRIyVlHZ3ahqTXw/zh-cn_image_0000002561753241.png?HW-CC-KV=V1&HW-CC-Date=20260427T235657Z&HW-CC-Expire=86400&HW-CC-Sign=175C4E808CF23A1054765E806EA0A80832482187E832C3E174FB95BB355E5C44)
2. 在需要开启HWASan的模块级build-profile.json5中，添加构建参数开启HWASan检测插桩。

   ```
   1. // DevEco Studio 6.1.0 Beta1以下版本
   2. "buildOption": {
   3. "externalNativeOptions": {
   4. "arguments": ["-DOHOS_ENABLE_HWASAN=ON"]
   5. }
   6. // DevEco Studio 6.1.0 Beta1及以上版本，同时开启有源码和无源码的C++的HWASan检测插桩
   7. "buildOption": {
   8. "externalNativeOptions": {
   9. "arguments": ["-DOHOS_ENABLE_HWASAN=ON", "-DOHOS_ENABLE_BINXO=ON"]
   10. }
   ```
3. 如果部分无源码so不需要进行HWASan检测插桩，可以在工程级或模块级build-profile.json5文件中，配置excludeSoFromBinXO字段，填写需要忽略的so列表，支持正则匹配。

   ```
   1. "buildOption": {
   2. "nativeLib": {
   3. "excludeSoFromBinXO": ["**/liblibrary.so"]
   4. }
   5. }
   ```

## 使用HWASan

1. 运行或调试当前应用。
2. 当程序出现内存错误时，弹出HWASan log信息，点击信息中的链接即可跳转至引起内存错误的代码处。日志中各字段的说明请参考[HWASan日志规格](address-sanitizer-guidelines.md#hwasan日志规格)，异常检测类型请参考[HWASan异常检测类型](../best-practices/bpta-stability-hwasan-detection.md#section207321025115510)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/ci0lPZB_RBiaZVlxtppVeg/zh-cn_image_0000002530913298.png?HW-CC-KV=V1&HW-CC-Date=20260427T235657Z&HW-CC-Expire=86400&HW-CC-Sign=0E8CC2C2A405065FA8C0AF0B696BF07067444187BC99485515D77B88E5729B8E)
3. 如果是release应用，本地无工程代码，可以使用AnalyzeStackTrace功能，提供要解析堆栈的so，解析结果为源码地址。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/HPl5YaRORGGeai8GSqYdYg/zh-cn_image_0000002530753308.png?HW-CC-KV=V1&HW-CC-Date=20260427T235657Z&HW-CC-Expire=86400&HW-CC-Sign=D92BB89D7D21BDA135254AAB606A2A00D0E47BE1D5BDCD5C82481BC90E6C93DF)
