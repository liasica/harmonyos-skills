---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-60
title: 如何控制编译过程的cpu使用
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何控制编译过程的cpu使用
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:54+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:09fd407fc69daa5a1f5007a162992dcf62f008381f7ab35ea12771bd9bc9f04e
---

在模块级 build-profile.json5 的 buildOption.arguments 中添加相关配置，指定 CMake 编译参数。示例如下：

```json
{
  "buildOption": {
    "arguments": [
      "-DCMAKE_BUILD_PARALLEL_LEVEL=2",
      "-DCMAKE_LINK_PARALLEL_LEVEL=2"
    ]
  }
}
```

此配置指定编译和链接分别使用 2 个处理器。

```json
"buildOption": {
  "externalNativeOptions": {
    "path": "../cpp/CMakeLists.txt",
    "arguments": "-DCMAKE_JOB_POOL_COMPILE:STRING=compile -DCMAKE_JOB_POOL_LINK:STRING=link -DCMAKE_JOB_POOLS:STRING=compile=2;link=2",
    "cppFlags": "",
    "abiFilters": [
      "x86_64",
      "arm64-v8a"
    ]
  }
},
```
