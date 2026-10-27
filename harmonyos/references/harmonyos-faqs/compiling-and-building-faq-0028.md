---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/compiling-and-building-faq-0028
title: 编译内存不足报错排查
breadcrumb: FAQ > DevEco Studio > 编译构建 > 常见问题 > 编译内存不足报错排查
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:51+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:b048ce8dc18d711eec57d1caf6efc66fe568e431a01754fe7a66b98c2a11abe0
---

**Q：编译构建时，出现报错“JS heap out of memory”。**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/yaASzJtNTey87vhWyStRPA/zh-cn_image_0000002773076174.png "点击放大")

**A**：出现该报错的原因是hvigor运行时内存不足。在使用Deveco Studio 5.0.0 Release及以上版本是时，可通过以下方式修改hvigor运行时内存的最大值。

勾选 Enable the Daemon for tasks：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/g1kj2heiQ_u3f9KeqBIMuQ/zh-cn_image_0000002802275937.png "点击放大")

在hvigor-config.json5中修改maxOldSpaceSize字段，根据工程大小适当增大，例如设置为 8192。

**Q：在Linux环境下，系统内存为64G，Hvigorw脚本中配置--max-old-space-size=40960，但在编译构建时，实际在使用内存未达到配置的内存（例如使用到20G左右）就出现报错“JavaScript heap out of memory”。**

```text
FATAL ERROR: NewSpace::Rebalance Allocation failed - JavaScript heap out of memory
Writing Node.js report to file: report.20200512.172528.47517.24.011.json
Node.js report completed
1: 0xa295e0 node::Abort() [node]
2: 0x9782df node::FatalError(char const*, char const*) [node]
3: 0xb99c2e v8::Utils::ReportOOMFailure(v8::internal::Isolate*, char const*, bool) [node]
4: 0xb99fa7 v8::internal::V8::FatalProcessOutOfMemory(v8::internal::Isolate*, char const*, bool) [node]
5: 0xd3a3b5 [node]
6: 0xd74f27 [node]
7: 0xd84707 v8::internal::MarkCompactCollector::CollectGarbage() [node]
8: 0xd481b9 v8::internal::Heap::MarkCompact() [node]
9: 0xd48f0b v8::internal::Heap::PerformGarbageCollection(v8::internal::GarbageCollector, v8::internal::GCCallbackFlags) [node]
10: 0xd499a5 v8::internal::Heap::CollectGarbage(v8::internal::AllocationSpace, v8::internal::GarbageCollectionReason, v8::internal::GCCallbackFlags) [node]
11: 0xd4aebf v8::internal::Heap::HandleGCRequest() [node]
12: 0xcf5f97 v8::internal::StackGuard::HandleInterrupts() [node]
13: 0x104b803 v8::internal::Runtime_StackGuard(int, unsigned long*, v8::internal::Isolate*) [node]
14: 0x13a5a99 [node]
Aborted (core dumped)
```

**A**：vm.max\_map\_count是一个与内核虚拟内存子系统相关的参数，用于控制进程可以拥有的内存映射区域的最大数量。它通常用于限制一个进程可以打开的文件数量，特别是在使用大量内存映射文件的情况下。

在Linux系统上，vm.max\_map\_count参数的默认值通常是较小的数值，例如65530。对于需要大量内存映射的应用程序或特定使用场景，建议将该参数值增加到更高，以支持更多内存映射区域。

当vm.max\_map\_count不足时，即使物理内存充足，V8引擎也无法建立足够的内存映射区域，导致提前触发OOM。

修改vm.max\_map\_count的值：

* 临时修改，建议设置为262144（即默认值的4倍）或更高，具体数值需根据应用需求调整：

  ```bash
  sysctl -w vm.max_map_count=新值
  ```
* 永久修改：如果希望永久修改参数的值，可以编辑/etc/sysctl.conf文件，并添加或修改以下行：

  ```bash
  # 需要root权限执行
  # 修改后需重启服务或执行sysctl -p生效
  vm.max_map_count=新值
  ```

保存文件后，使用以下命令使更改生效：

```bash
sysctl -p
```
