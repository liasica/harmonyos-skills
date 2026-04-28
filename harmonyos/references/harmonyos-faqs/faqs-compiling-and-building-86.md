---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-86
title: 编译打包CPU架构设置
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译打包CPU架构设置
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:27+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:7b846f796eddf95def37dd9ba9730b8cc01d4fd589ac6b7792dd586f208c56d4
---

**问题描述**

在编译打包时，若需移除v7a，可以参考以下配置文档。

**解决方案**

可参考 [bm工具](../harmonyos-guides/bm-tool.md)

```
1. "externalNativeOptions": {
2. "path": "./src/main/cpp/CMakeLists.txt",
3. //CMake configuration file, providing CMake build scripts
4. "arguments": "",
5. //Optional compilation parameters passed to CMake
6. "abiFilters": [
7. "x86_64",
8. "arm64-v8a"
9. ],
10. //Used to set up the local ABI compilation environment
11. "cppFlags": ""
12. //Set optional parameters for the C++ compiler
13. },
```

[build-profile.json5](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CompilingAndBuilding/library1/build-profile.json5#L6-L18)
