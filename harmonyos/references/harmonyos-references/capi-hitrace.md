---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hitrace
title: HiTrace
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 模块 > HiTrace
category: harmonyos-references
scraped_at: 2026-09-02T14:52:41+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7f7cc51d38b796ed654b18b34cb958dcb9ab0b60d40fcaa922e04e8e7352f09b
---

## 概述

HiTraceMeter为开发者提供系统性能打点接口。

开发者通过在业务逻辑的关键位置调用HiTraceMeter的API接口，能够有效进行关键执行流程耗时度量和问题定位。适用于需要分析应用性能瓶颈、优化关键路径执行效率的场景，可帮助开发者快速定位性能问题并优化系统性能。

HiTraceChain为开发者提供跨线程、跨进程的分布式跟踪能力。

HiTraceChain支持在业务执行流程中，生成和传递唯一跟踪标识，在业务流程中输出的各类调试信息中（包括HiTraceMeter打点、应用事件、hilog日志等）记录该跟踪标识。唯一跟踪标识是一个跨线程、跨进程传递的追踪ID，用于关联同一业务流程的所有调试信息。在调试、问题定位过程中，开发人员可以通过该标识将本次业务流程端到端的各类信息快速关联起来。适用于分布式应用、微服务架构等需要追踪跨服务调用链路的场景，可帮助开发者快速定位跨服务故障，提升问题排查效率。

**系统能力：** SystemCapability.HiviewDFX.HiTrace

**起始版本：** 10

## 文件汇总

| 名称 | 描述 |
| --- | --- |
| [trace.h](capi-trace-h.md) | HiTraceMeter和HiTraceChain模块接口定义，通过这些接口实现性能打点和分布式跟踪功能。支持应用性能分析、跨服务调用链追踪、性能瓶颈定位等场景，能够解决分布式系统中调用链路难以追踪、性能问题难以定位的问题，提升系统可观测性和问题排查效率。性能打点通过在代码关键位置插入标记，记录函数执行时间；分布式跟踪通过HiTraceId实现跨线程、跨进程、跨设备的调用链追踪。  用户态trace格式使用竖线字符作为分隔符，所以通过HiTraceMeter接口传递的字符串类型参数应避免包含该字符，防止trace解析异常。  用户态trace总长度限制512字符，超过的部分将会被截断。 |
