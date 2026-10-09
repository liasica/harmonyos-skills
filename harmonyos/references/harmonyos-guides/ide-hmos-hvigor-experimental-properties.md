---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-hvigor-experimental-properties
title: 实验特性
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 构建应用 > 提升构建效率 > 实验特性
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:36+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:30215f9716540ecfeaf8435a4147aed5b2e5bf5bdd7095fa1e0e32c5bd5dfe79
---

为了打造更敏捷流畅的使用体验，新版本的Hvigor带来了一系列的编译构建性能优化实验特性，这些优化特性将显著提高工程的编译速度，降低峰值内存占用等。由于部分优化方案仍处于试验性阶段，您可能在这些特性中体验到效率的提升，也可能在特定场景中遇到待完善的问题，因此，这些特性提供了开关，用户可以根据业务需求开启后使用。

## 通过IClang提升C++增量编译效率

**使用场景：**

如果需要频繁修改某个cpp源文件，可开启IClang相关的开关，提升C++增量编译效率。IClang是一项C++函数级增量编译优化技术，详细介绍请参考[毕昇编译器](bisheng-compiler.md#主要编译优化特性)。

**使用约束****：**

* 仅支持在debug编译模式下使用。
* 需要使用毕昇编译器进行编译，即工程级build-profile.json5的nativeCompiler配置为BiSheng。
* 首次修改cpp文件时，IClang会将该文件识别为频繁修改的目标文件，并为其生成缓存。因此，当第二次修改cpp文件并进行增量编译时，才会提升编译效率。
* 修改头文件的内容或头文件的导入语句，包括顺序、语句间的空行或任何格式上的调整，都会导致缓存失效，无法提升编译效率。

**开启方式：**

模块级build-profile.json5的cppFlags、cFlags配置"-iclang"参数。

```json5
"buildOption": {
  "externalNativeOptions": {
    "cppFlags": "-iclang",
    "cFlags": "-iclang",
  }
}
```

**可能影响：**build-profile.json5文件会纳入项目版本管理，在该文件中增加-iclang参数后，项目其他开发人员会被动开启该实验特性。因此请在充分验证功能正确性后，再通过配置文件上传到代码仓。
