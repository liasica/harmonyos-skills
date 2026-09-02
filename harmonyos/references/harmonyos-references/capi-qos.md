---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-qos
title: QoS
breadcrumb: API参考 > 系统 > 基础功能 > Kernel Enhance Kit（内核增强能力） > C API > 模块 > QoS
category: harmonyos-references
scraped_at: 2026-09-02T14:52:35+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0b8d89a3e1830ce9ee40e2389a83848521d4d066168a545c216f89196cdd13af
---

## 概述

本模块包含QoS（Quality of Service，服务质量）接口，用于设置、取消和查询线程QoS等级，从而影响系统对线程的调度优先级与资源分配；同时提供格物服务（端侧AI推理加速服务）相关C接口，用于端侧推理会话管理。QoS适用于需要区分关键任务与普通任务优先级、提升关键任务响应性能的场景，例如实时音视频处理、游戏渲染和用户交互响应等。QoS通过调整线程调度策略实现优先级控制，详细接口说明请参见[qos.h](capi-qos-h.md)。

**起始版本：** 12

## 文件汇总

| 名称 | 描述 |
| --- | --- |
| [qos.h](capi-qos-h.md) | 声明QoS和格物服务相关C接口。 |
