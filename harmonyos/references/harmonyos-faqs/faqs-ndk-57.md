---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-57
title: HarmonyOS编译构建时如何指定编译架构信息
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > HarmonyOS编译构建时如何指定编译架构信息
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:39+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:930435ae2c7f89c167039a0ced6d35c19a5d7c4e91ace239056a265eddae5466
---

**问题现象**

webrtc gn里面通过binary\_prefix来区分不同架构下的编译工具。HarmonyOS系统如何设置target指定架构信息？

**解决措施**

HarmonyOS通过–target 来设置架构。--target aarch64-linux-ohos 和--target arm-linux-ohos 分别对应64位和32位的架构。
