---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/system-memory-manage-standards-overview
title: 概述
breadcrumb: 指南 > 应用体验建议 > 应用系统资源管理体验建议 > 系统内存使用与优化 > 概述
category: harmonyos-guides
scraped_at: 2026-11-27T10:45:09+08:00
doc_updated_at: 2026-11-26
content_hash: sha256:774aad73b742be869bf0cc8ca9cab69967bd740e69667108fb1abf7d84867d63
---

## 制定目的

系统内存作为鸿蒙设备硬件提供的关键资源，应得到合理高效的使用，从而为消费者带来流畅的使用体验。因此，HarmonyOS应用应具备良好的性能体验，合理使用设备内存。

然而，随着HarmonyOS应用规模持续扩大，部分应用缺乏对系统内存使用的正确处理，存在后台不释放资源、大对象未及时回收等问题，导致系统可回收内存降低、后台应用驻留率下降、卡顿与内存溢出（OOM，Out Of Memory）概率上升，进而影响设备流畅度和用户使用体验。

为帮助HarmonyOS应用规范使用系统内存行为，减少因应用内存泄漏、内存劣化等原因导致的整体系统性能下降，保障用户的鸿蒙设备和应用使用体验，特制定本规范。本规范适用于在华为应用市场分发的应用和元服务。

## 使用对象

HarmonyOS应用和元服务的设计、开发、测试、运营等角色。

## 术语定义

### 系统内存（System Memory）

设备整机运行内存（RAM），供系统内核、系统后台服务、所有前台和后台应用、驱动、图形渲染、缓存等共享使用，是整机所有程序运行的唯一物理内存载体。按鸿蒙设备型号的差异，内存大小分别有6GB、8GB、12GB、16GB、20GB等档位。

### 内存泄漏（Memory Leak）

应用和元服务申请分配的堆内存，在逻辑上已经完全不再需要使用，但开发者代码存在引用残留、循环引用、对象持有未释放等问题，导致系统无法回收这部分内存，该块内存永久被App占用，直至进程终止，这种现象即为内存泄漏。

### 前台内存峰值占用（Peak Foreground Memory Usage）

应用进程处于前台活跃状态（拥有焦点窗口、用户可交互、系统高优先级调度）期间，全生命周期采集到的瞬时最大内存占用值。

### 后台内存均值占用（Average Background Memory Footprint）

应用切后台后（UI不可见、失去焦点、系统降低进程优先级等），持续采样周期内内存占用算术平均值。

### USS（Unique Set Size）

仅属于当前进程、不与任何其他进程共享的物理内存总量，无共享内存分摊。

### RSS（Resident Set Size）

进程当前已映射至物理 RAM、未交换至磁盘的全部内存页总和，包含私有内存和完整共享内存，不做分摊处理。

### PSS（Proportional Set Size）

进程独占内存与按比例分摊共享内存的总和。

### VSS（Virtual Set Size）

进程能访问的所有虚拟内存的总和。
