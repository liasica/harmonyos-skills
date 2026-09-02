---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/linx-kit-introduction
title: Linx Kit简介
breadcrumb: 指南 > 系统 > 基础功能 > Linx Kit（灵犀加速库） > Linx Kit简介
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:37+08:00
doc_updated_at: 2026-08-07
content_hash: sha256:cfe0c28ca970d65e132ed649769dedb8a3a2d52d83f1553c9826038700c1d6a2
---

Linx Kit（灵犀加速库）是一套性能优化开发框架，基于芯片底层架构实现软硬协同优化。该框架提供热点加速能力，通过对线程执行过程中的热点流程进行针对性优化，提升应用与游戏的流畅度和能效表现，带来更流畅的使用体验。其核心原理在于通过帧间信息或CPU簇间信息的复用，利用灵犀CPU核进行高效计算，释放灵犀CPU核特有计算能力。适用于需要高帧率、低延迟的游戏、视频播放及复杂UI交互等场景。

## 能力范围

**游戏性能优化**：支持游戏引擎复用帧间及CPU簇间数据，充分发挥灵犀CPU核算力，降低延迟并提升帧率。

## 约束与限制

### 支持的国家/地区

仅使用于中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

### 设备限制

Linx Kit只能在具备灵犀CPU核的目标设备上运行，不同设备支持的特性范围有所差异，可以通过API返回的错误码进行判断。

支持的设备类型有：Phone、Tablet、PC/2in1、TV。

## 模拟器支持情况

本Kit暂不支持模拟器。
