---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cpu-features
title: CPU特性
breadcrumb: 指南 > NDK开发 > 硬件兼容性 > CPU特性
category: harmonyos-guides
scraped_at: 2026-04-28T07:54:33+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:686450e59d5a26d50867c164fbc7b241a6d79e4e08d734556605559b7e8d36ed
---

CPU特性是CPU提供的一些硬件扩展。开发者可以通过调用指令，设置特殊寄存器来使用这些CPU特性，例如ARMv7a架构上的VFP-v32d32、NEON、IDIV、AES等CPU特性。很多CPU特性是可选的，不同厂商的CPU通常有不同的特性。

在HarmonyOS原生库开发中，如何使用CPU特性？如何在代码中处理CPU特性相关的代码？本章节将提供一些方法，以便帮助开发者开发出既能保持兼容性，又能利用CPU特性能力的应用。

HarmonyOS系统当前没有提供获取CPU特性的接口，开发者可以导入现有开源社区的库函数，具体可以参考如下的例子；也可直接读取/proc/cpuinfo，或者调用libc getauxval(AT\_HWCAP)接口来获取设备的CPU特性。

## 使用建议

1. 在HarmonyOS系统C++工程中引入开源库，下载[cpu\_features库](https://github.com/google/cpu_features)，解压到工程的cpp目录下，解压后的文件名改为cpu\_features。如下以DevEco Studio C++模板示例应用举例：

   * 解压后目录结构如下

     ```
     1. MyApplication
     2. |-- entry
     3. |-- src
     4. |-- main
     5. |-- cpp
     6. |--cpu_features
     7. |--CMakeLists.txt
     8. |--hello.cpp
     ```
   * 在CMakeLists.txt添加导入目录

     ```
     1. add_subdirectory(cpu_features) # 添加子目录到工程
     2. target_link_libraries(entry PUBLIC cpu_features) # 添加需要链接依赖的库文件
     ```
2. 在代码中加入判断CPU特性支持能力语句，如下以支持ARM与AARCH64两种架构举例：

   ```
   1. // ...
   2. // 包含CPU架构目标检测头文件
   3. #include "cpu_features_macros.h"
   4. // 在ARM架构上，这个宏在上面头文件中根据目标自动定义
   5. #if defined (CPU_FEATURES_ARCH_ARM)
   6. #include "cpuinfo_arm.h" // 包含ARM架构的cpuinfo头文件
   7. #elif defined (CPU_FEATURES_ARCH_AARCH64)
   8. #include "cpuinfo_aarch64.h" // 包含ARM64架构的cpuinfo头文件
   9. #endif
   10. // C++代码, 需要添加`using namespace cpu_features;`
   11. // 根据不同架构，获取相应的CPU特性信息；
   12. #if defined (CPU_FEATURES_ARCH_ARM)
   13. static const ArmFeatures features = GetArmInfo().features;
   14. #elif defined (CPU_FEATURES_ARCH_AARCH64)
   15. static const Aarch64Features features = GetAarch64Info().features;
   16. #endif
   17. void Compute(void) {
   18. // 根据features的字段进行支持CPU features的特性判断
   19. if (features.aes) {
   20. // ...
   21. } else {
   22. // ...
   23. }
   24. }
   ```

   说明

   cpu\_features库实际上是通过/proc/cpuinfo，与getauxval接口从内核中读取对应的CPU特性信息，有可能由于应用沙盒的原因导致无法读取对应的信息，注意错误处理。
