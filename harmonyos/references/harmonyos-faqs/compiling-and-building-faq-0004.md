---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/compiling-and-building-faq-0004
title: 应用编译打包CPU架构配置常见问题
breadcrumb: FAQ > DevEco Studio > 编译构建 > 常见问题 > 应用编译打包CPU架构配置常见问题
category: harmonyos-faqs
scraped_at: 2026-10-21T07:12:39+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:0453cf56d3c200896256dc32fee13fedfa174c6ea4bddc327acf6fb49fa4eb3f
---

**Q：在编译打包时，若需移除v7a，应如何配置？**

**A**：可参考[bm工具](../harmonyos-guides/bm-tool.md)。

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
