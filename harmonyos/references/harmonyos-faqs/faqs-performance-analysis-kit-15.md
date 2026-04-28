---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-15
title: 如何查询应用堆内存的已分配内存大小和堆内存的空闲内存大小
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何查询应用堆内存的已分配内存大小和堆内存的空闲内存大小
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:15+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1d949ddb52d53308964a9ac11d76ce5fd931c2bc8683cce22e43a3ca394b7986
---

目前有两种方法可以查询当前CPU占用，如下：

在代码中查询：

查询应用堆内存的已分配内存大小使用 hidebug.getNativeHeapAllocatedSize，查询空闲内存大小使用 hidebug.getNativeHeapFreeSize。

参考代码如下：

```
1. let nativeHeapAllocatedSize: bigint = hidebug.getNativeHeapAllocatedSize(); // Get the allocated memory size of the heap memory in this application
2. let nativeHeapFreeSize: bigint = hidebug.getNativeHeapFreeSize(); // Get the free memory size of the heap memory in this application
```

[Hidebug.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AnalysisKit/entry/src/main/ets/pages/Hidebug.ets#L12-L13)

在命令行中查询：

使用 --mem pid 命令可以获取总内存占用率；如果指定了 pid，则获取该 pid 对应的内存占用率。

```
1. hidumper --mem pid
```

**参考链接**

[hidebug.getNativeHeapFreeSize](../harmonyos-references/js-apis-hidebug.md#hidebuggetnativeheapfreesize)

[hidebug.getNativeHeapAllocatedSize](../harmonyos-references/js-apis-hidebug.md#hidebuggetnativeheapallocatedsize)

[hidumper](../harmonyos-guides/hidumper.md)
