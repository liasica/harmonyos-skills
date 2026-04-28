---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-worker-taskpool
title: 调试场景说明
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 调试场景说明
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:46+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:0be6fd7063bebff3b67e6ee84700a536cb1d1e1d309c5eebfb7c72b863ae8240
---

DevEco Studio支持对ArkTS代码进行调试，包括以下场景。

* 在[Worker/TaskPool代码](multi-thread-concurrency-overview.md)中添加断点进行调试。
* 对[Extension Ability](extensionability-overview.md)生命周期函数进行调试，具体请参考[extension调试](ide-debug-arkts-extension.md)。
* 部分设备上，UIAbility支持以独立进程的方式运行并调试，具体请参考[多进程调试](ide-debug-multi-process.md)。
* 在Native代码中，通过[创建ArkTS运行时](use-napi-ark-runtime.md)的方式调用ArkTS方法，在ArkTS代码中添加断点即可进行调试。（设备系统版本需要升级到6.0.0.35及以上）
