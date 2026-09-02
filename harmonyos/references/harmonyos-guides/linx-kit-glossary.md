---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/linx-kit-glossary
title: Linx Kit术语
breadcrumb: 指南 > 系统 > 基础功能 > Linx Kit（灵犀加速库） > Linx Kit术语
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:37+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:a767f9396018cd330a5e57ac97b9ec6e6a00b829caa746fd6585f260af3d3e79
---

## B

### Branch Jump；分支跳转

程序运行过程中的条件分支跳转行为，是热点加速模块记录和重放的关键信息之一，用于在下一帧中预判执行路径以提升效率。

## C

### Context Index；上下文索引

热点加速API中用于标识一次加速会话的uint32\_t类型索引。需在HMS\_LINX\_HotspotAccelerateBegin和HMS\_LINX\_HotspotAccelerateEnd调用中保持一致，以确保加速与释放操作对应同一会话。

## I

### Inter-frame Information Reuse；帧间信息复用

利用相邻帧之间执行行为的相似性，将上一帧记录的关键信息（如分支跳转）在下一帧进行重放，减少重复计算开销，是热点加速的核心优化原理。
