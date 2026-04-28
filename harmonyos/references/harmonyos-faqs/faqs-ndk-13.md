---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-13
title: 如何在Native侧区分ArkTS侧创建的ArrayBuffer和Uint8Array对象
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何在Native侧区分ArkTS侧创建的ArrayBuffer和Uint8Array对象
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:31+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1dd6bfac0791bc0cda1c759f90dad6970a05dfb70bdeb36c7c01fdfa12b2657b
---

**问题详情**

ArkTS层创建的ArrayBuffer和Uint8Array对象在Native层无法正确区分。

**解决措施**

1. 使用[napi\_is\_arraybuffer](../harmonyos-guides/use-napi-about-arraybuffer.md#napi_is_arraybuffer)接口判断数据是否为ArrayBuffer类型，若类型符合则结果为true。
2. 使用[napi\_is\_typedarray](../harmonyos-guides/use-napi-about-array.md#napi_is_typedarray)接口判断Uint8Array类型数据，若类型符合则结果为true。
