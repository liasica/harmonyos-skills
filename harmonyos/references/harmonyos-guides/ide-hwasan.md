---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hwasan
title: 使用HWASan检测内存错误
breadcrumb: 指南 > 编写与调试应用 > 日志与故障分析 > 故障分析 > 使用HWASan检测内存错误
category: harmonyos-guides
scraped_at: 2026-04-29T13:46:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f4f3aa02a9e0da6ac833c1697c61b29d196d8fe52e314e6e622b9128c54d4cb4
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/zng6ovtURF6_0VHL9IHSWA/zh-cn_image_0000002561833227.png?HW-CC-KV=V1&HW-CC-Date=20260429T054654Z&HW-CC-Expire=86400&HW-CC-Sign=54F4D19C10A68BF283D25A8101CEFE712D6266EF95A86E7F1413F217C6AAB683)
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/PwpoIjjZQMaje9gNlxY9PA/zh-cn_image_0000002561753241.png?HW-CC-KV=V1&HW-CC-Date=20260429T054654Z&HW-CC-Expire=86400&HW-CC-Sign=823BF10DDC32A4E1ADE2DFAF26FAC21A13EC41D452F17EC60F7DE58395DD557B)
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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/ypeAV7WVRiaUY6_rXIrHFQ/zh-cn_image_0000002530913298.png?HW-CC-KV=V1&HW-CC-Date=20260429T054654Z&HW-CC-Expire=86400&HW-CC-Sign=958707E199180B1EB26A5C1F76C679EACB0747E1119E573E457AC399D16847F3)
3. 如果是release应用，本地无工程代码，可以使用AnalyzeStackTrace功能，提供要解析堆栈的so，解析结果为源码地址。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/COPoz615RW-TVPzHU6HS0A/zh-cn_image_0000002530753308.png?HW-CC-KV=V1&HW-CC-Date=20260429T054654Z&HW-CC-Expire=86400&HW-CC-Sign=C5A887747F191305445001CCC042B3972D699174E08128EEAAA0F7168886AF59)
