---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-60
title: 如何控制编译过程的cpu使用
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何控制编译过程的cpu使用
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:20+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:9f8e550cf7d2dac13c2aad96f10ba9e0182e040cf361023c949429d0c1ee6fba
---

在模块级 build-profile.json5 的 buildOption.arguments 中添加相关配置，指定 CMake 编译参数。示例如下：

```
1. {
2. "buildOption": {
3. "arguments": [
4. "-DCMAKE_BUILD_PARALLEL_LEVEL=2",
5. "-DCMAKE_LINK_PARALLEL_LEVEL=2"
6. ]
7. }
8. }
```

此配置指定编译和链接分别使用 2 个处理器。

```
1. "buildOption": {
2. "externalNativeOptions": {
3. "path": "../cpp/CMakeLists.txt",
4. "arguments": "-DCMAKE_JOB_POOL_COMPILE:STRING=compile -DCMAKE_JOB_POOL_LINK:STRING=link -DCMAKE_JOB_POOLS:STRING=compile=2;link=2",
5. "cppFlags": "",
6. "abiFilters": [
7. "x86_64",
8. "arm64-v8a"
9. ]
10. }
11. },
```

[build-profile.json5](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CompilingAndBuilding/entry/build-profile.json5#L6-L16)
