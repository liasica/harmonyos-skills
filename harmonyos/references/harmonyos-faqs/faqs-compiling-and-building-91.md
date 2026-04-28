---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-91
title: armeabi-v7a是否支持Neon指令扩展
breadcrumb: FAQ > DevEco Studio > 编译构建 > armeabi-v7a是否支持Neon指令扩展
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:27+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:48527a5f73ffbd9dcb99de4fc6cb7336e31e288b63e844e9711813c283e035aa
---

**问题描述**

使用CMake编译现有工程为armeabi-v7a架构时出现问题。

D:/DeveloperTools/Huawei/SDK/default/base/native/llvm/lib/clang/15.0.4/include/arm\_neon.h:28:2: error: “NEON intrinsics not available with the soft-float ABI. Please use -mfloat-abi=softfp or -mfloat-abi=hard”#error “NEON intrinsics not available with the soft-float ABI. Please use -mfloat-abi=softfp or -mfloat-abi=hard”

**解决方案**

可以进行如下验证：Neon指令集的引入方案如下：

在entry目录的build-profile.json5文件中，externalNativeOptions节点添加配置项：

```
1. "externalNativeOptions": {
2. "path": "./src/main/cpp/CMakeLists.txt",
3. "arguments": "",
4. "abiFilters": [
5. "x86_64",
6. "arm64-v8a"
7. ],
8. // This is a configuration item to be added
9. "cppFlags": "-mfloat-abi=hard",
10. // This is a configuration item to be added
11. },
```

[build-profile.json5](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/CompilingAndBuilding/library/build-profile.json5#L7-L17)

引入头文件#include <arm\_neon.h>
