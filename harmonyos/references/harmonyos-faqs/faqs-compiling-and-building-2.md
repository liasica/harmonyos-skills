---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-2
title: Linux环境下编译报错“JavaScript heap out of memory”
breadcrumb: FAQ > DevEco Studio > 编译构建 > Linux环境下编译报错“JavaScript heap out of memory”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:07+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:7ff7aee6dff88257c172b2f4fdd75f1efd4194c26b85ca87793dfff834319acb
---

**问题现象**

在Linux环境下，系统内存为64G，Hvigorw脚本中配置--max-old-space-size=40960，但在编译构建时，实际在使用内存未达到配置的内存（例如使用到20G左右）就出现报错“JavaScript heap out of memory”。

```
1. FATAL ERROR: NewSpace::Rebalance Allocation failed - JavaScript heap out of memory
2. Writing Node.js report to file: report.20200512.172528.47517.24.011.json
3. Node.js report completed
4. 1: 0xa295e0 node::Abort() [node]
5. 2: 0x9782df node::FatalError(char const*, char const*) [node]
6. 3: 0xb99c2e v8::Utils::ReportOOMFailure(v8::internal::Isolate*, char const*, bool) [node]
7. 4: 0xb99fa7 v8::internal::V8::FatalProcessOutOfMemory(v8::internal::Isolate*, char const*, bool) [node]
8. 5: 0xd3a3b5 [node]
9. 6: 0xd74f27 [node]
10. 7: 0xd84707 v8::internal::MarkCompactCollector::CollectGarbage() [node]
11. 8: 0xd481b9 v8::internal::Heap::MarkCompact() [node]
12. 9: 0xd48f0b v8::internal::Heap::PerformGarbageCollection(v8::internal::GarbageCollector, v8::GCCallbackFlags) [node]
13. 10: 0xd499a5 v8::internal::Heap::CollectGarbage(v8::internal::AllocationSpace, v8::internal::GarbageCollectionReason, v8::GCCallbackFlags) [node]
14. 11: 0xd4aebf v8::internal::Heap::HandleGCRequest() [node]
15. 12: 0xcf5f97 v8::internal::StackGuard::HandleInterrupts() [node]
16. 13: 0x104b803 v8::internal::Runtime_StackGuard(int, unsigned long*, v8::internal::Isolate*) [node]
17. 14: 0x13a5a99 [node]
18. Aborted (core dumped)
```

**问题原因**

vm.max\_map\_count是一个与内核虚拟内存子系统相关的参数，用于控制进程可以拥有的内存映射区域的最大数量。它通常用于限制一个进程可以打开的文件数量，特别是在使用大量内存映射文件的情况下。

在Linux系统上，vm.max\_map\_count参数的默认值通常是较小的数值，例如65530。对于需要大量内存映射的应用程序或特定使用场景，建议将该参数值增加到更高，以支持更多内存映射区域。

当vm.max\_map\_count不足时，即使物理内存充足，V8引擎也无法建立足够的内存映射区域，导致提前触发OOM。

**解决措施**

修改vm.max\_map\_count的值：

* 临时修改，建议设置为262144（即默认值的4倍）或更高，具体数值需根据应用需求调整：

  ```
  1. sysctl -w vm.max_map_count=新值
  ```
* 永久修改：如果希望永久修改参数的值，可以编辑/etc/sysctl.conf文件，并添加或修改以下行：

  ```
  1. # 需要root权限执行
  2. # 修改后需重启服务或执行sysctl -p生效
  3. vm.max_map_count=新值
  ```

  保存文件后，使用以下命令使更改生效：

  ```
  1. sysctl -p
  ```
