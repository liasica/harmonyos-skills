---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-15
title: 如何查询应用堆内存的已分配内存大小和堆内存的空闲内存大小
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何查询应用堆内存的已分配内存大小和堆内存的空闲内存大小
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:09e242eee77e1464c26d5fa8823658f6f1501dfada2327d878ad70c7d2206cae
---

目前有两种方法可以应用堆内存的已分配内存大小和堆内存的空闲内存大小。

在代码中查询：

查询应用堆内存的已分配内存大小使用 hidebug.getNativeHeapAllocatedSize，查询空闲内存大小使用 hidebug.getNativeHeapFreeSize。

参考代码如下：

```typescript
let nativeHeapAllocatedSize: bigint = hidebug.getNativeHeapAllocatedSize(); // Get the allocated memory size of the heap memory in this application
let nativeHeapFreeSize: bigint = hidebug.getNativeHeapFreeSize(); // Get the free memory size of the heap memory in this application
```

在命令行中查询：

使用 --mem pid 命令可以获取总内存占用率；如果指定了 pid，则获取该 pid 对应的内存占用率。

```powershell
hidumper --mem pid
```

**参考链接**

[hidebug.getNativeHeapFreeSize](../harmonyos-references/js-apis-hidebug.md#hidebuggetnativeheapfreesize)

[hidebug.getNativeHeapAllocatedSize](../harmonyos-references/js-apis-hidebug.md#hidebuggetnativeheapallocatedsize)

[hidumper](../harmonyos-guides/hidumper.md)
