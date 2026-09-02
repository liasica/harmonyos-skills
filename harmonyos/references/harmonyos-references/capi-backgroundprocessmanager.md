---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-backgroundprocessmanager
title: BackgroundProcessManager
breadcrumb: API参考 > 应用框架 > Background Tasks Kit（后台任务开发服务） > C API > 模块 > BackgroundProcessManager
category: harmonyos-references
scraped_at: 2026-09-02T14:51:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:70985e7ece98e49c620338a8ec8e67ef17923d57369efa453a6db37b27ff7c6d
---

## 概述

提供后台子进程调度策略管控C接口。

**起始版本：** 17

## 文件汇总

| 名称 | 描述 |
| --- | --- |
| [background\_process\_manager.h](capi-background-process-manager-h.md) | 本模块提供了后台子进程管控接口。开发者可以通过本模块接口对子进程进行压制、解压制，避免子进程过多占用系统资源，导致系统使用卡顿。本模块接口仅对通过OH\_Ability\_StartNativeChildProcess接口创建的子进程生效。 |
