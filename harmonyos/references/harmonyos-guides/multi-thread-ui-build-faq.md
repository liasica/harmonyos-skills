---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multi-thread-ui-build-faq
title: UI并行化常见问题
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发调试调优 > UI开发常见问题 > UI并行化常见问题
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:40+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:00670469a14a44b3e1c1f8fbe6f59b7555cce0ad8465397d991873a5861f05a6
---

## 如何获取和使用支持多线程调用的NDK接口

从API version 22开始，[ArkUI\_NativeAPIVariantKind](../harmonyos-references/capi-native-interface-h.md#arkui_nativeapivariantkind)中新增ARKUI\_MULTI\_THREAD\_NATIVE\_NODE枚举。

调用[OH\_ArkUI\_GetModuleInterface](../harmonyos-references/capi-native-interface-h.md#oh_arkui_getmoduleinterface)接口，入参传入ARKUI\_MULTI\_THREAD\_NATIVE\_NODE，可以获取多线程NDK接口集合，完整示例请参考[多线程NDK接口使用方式](ndk-build-on-multi-thread.md#多线程ndk接口使用方式)。

## 调用多线程NDK接口返回ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD错误码

**问题现象**

调用多线程NDK接口返回ARKUI\_ERROR\_CODE\_NODE\_ON\_INVALID\_THREAD错误码。

**解决措施**

首先参考[多线程NDK接口集合规格](ndk-build-on-multi-thread.md#多线程ndk接口集合规格)，查看调用的接口是否支持多线程调用，之后按照如下步骤排查。

1. 如果接口只支持在UI线程调用，需要调整函数调用时机，在UI线程调用接口。
2. 如果接口支持多线程调用，报错原因是接口操作的节点处于Attached状态。
   * 确认节点是由多线程[createNode](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#createnode)接口创建的。
   * 参考[多线程NDK接口调用规范](ndk-build-on-multi-thread.md#多线程ndk接口调用规范)，将组件所在组件树中所有不可转换的Attached组件移除。

## 如何保证多线程操作ArkUI组件时线程安全

在使用多线程NDK接口时，多个线程同时操作同一个组件或组件树，无法保证线程安全，需要开发者通过合理的架构设计避免出现上述情况。

可以参考[多线程NDK接口调用规范](ndk-build-on-multi-thread.md#多线程ndk接口调用规范)，按照文档中的约束使用多线程NDK接口来保证线程安全。
