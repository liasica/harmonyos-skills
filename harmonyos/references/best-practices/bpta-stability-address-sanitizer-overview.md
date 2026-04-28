---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-address-sanitizer-overview
title: 地址越界检测能力概述
breadcrumb: 最佳实践 > 稳定性 > 稳定性检测 > 开发态稳定性检测 > 地址越界类问题检测 > 地址越界检测能力概述
category: best-practices
scraped_at: 2026-04-28T08:22:48+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:086d3428e310a83fb17046a3ea367f2334dfc50ce53af330f120ac6a16fa1133
---

地址越界检测功能主要用于帮助开发者在调试和压力测试阶段发现内存非法访问问题，如越界读写、Use-After-Free、Double-Free等。这些问题通常难以通过崩溃日志直接确定根本原因。为此，DevEco Studio提供了ASan（Address Sanitizer）、HWASan（Hardware-Assisted Address Sanitizer）、MemDebug（Memory Debug）、GWP-ASan等多种检测工具，在运行时监控内存访问行为，及时捕获并报告潜在的地址越界问题，提高问题发现的效率和定位的准确性。这些工具在检测精度、性能开销和适用场景上各有侧重，分别适用于开发调试和商用发布的不同阶段。

| 能力项 | ASan | HWASan | MemDebug | GWP-ASan |
| --- | --- | --- | --- | --- |
| **概述** | 基于Shadow Memory与红区机制来检测越界问题。 | 基于指针Tag与Shadow Memory机制，通过硬件支持实现Tag校验来检测越界问题。 | 采用隔离区加投毒填充的机制，并复用 HWASan的Tag校验对一部分问题进行检测。 | 通过采样插桩拦截部分堆分配，检测释放后使用、堆溢出等典型内存错误。 |
| **优势** | 检测能力较强，覆盖类型多。 | 1. 与ASan相比，HWASan无需安全区来检测buffer overflow，这不仅显著减少了工具对内存的消耗，还避免了ASan中某些overflow无法检测的问题。 2. HWASan也不需要隔离区来检测UseAfterFree，因此不会出现ASan中某些UseAfterFree检测不到的情况。 3. 对于内存的二次释放free场景，启用HWASan后，无需代码插桩即可进行检测。 4. HWASan还能检测返回后的堆栈使用情况。 | 无需应用适配。 | 1. 无需应用适配。 2. <5%性能影响，很轻量。 |
| **劣势** | 1. 需要应用适配插桩。 2. 2倍CPU和内存开销。 | 1. 需要应用适配插桩。 2. 2倍CPU开销和10%~35%的内存影响。 | 1. 检测能力有限。 2. 10-20%性能和内存影响。 | 检测能力有限。 |
| **适用场景** | 开发态（调试压测）。 | 开发态（调试压测）。 | 开发态（调试压测）。 | 运行态（商用）。 |

说明

1. ASan、HWASan、MemDebug对应用性能有影响，仅适用于开发调试和压力测试阶段。在应用上架前，请确保已关闭这些功能（检查方法：解压hap包，检查module.json文件中是否包含asanEnable或hwasanEnable字段，并且字段值为true）。
2. ASan相较于HWASan资源消耗更大，建议优先使用HWASan。
