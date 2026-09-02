---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-86
title: 编译打包CPU架构设置
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译打包CPU架构设置
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e0d2a733f219f48dd11c492bfbc00127e534ca07c8c02bccd6c83e36c337f7d7
---

**问题描述**

在编译打包时，若需移除v7a，可以参考以下配置文档。

**解决方案**

可参考 [bm工具](../harmonyos-guides/bm-tool.md)

```json
"externalNativeOptions": {
  "path": "./src/main/cpp/CMakeLists.txt",
  // CMake configuration file, providing CMake build scripts
  "arguments": "",
  // Optional compilation parameters passed to CMake
  "abiFilters": [
    "x86_64",
    "arm64-v8a"
  ],
  // Used to set up the local ABI compilation environment
  "cppFlags": ""
  // Set optional parameters for the C++ compiler
},
```
