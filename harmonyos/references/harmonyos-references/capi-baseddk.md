---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-baseddk
title: Ddk
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 模块 > Ddk
category: harmonyos-references
scraped_at: 2026-09-02T14:52:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2f134f74a1be98d37fee9798bf3112536d5ba5f0076c262c3a0536971b2ddad4
---

## 概述

提供Base DDK接口，包括创建、映射、取消映射以及销毁共享内存。

**起始版本：** 12

## 文件汇总

| 名称 | 描述 |
| --- | --- |
| [ddk\_api.h](capi-ddk-api-h.md) | 声明主机侧访问的Base DDK接口。提供共享内存的创建、映射、销毁等功能，支持开发者在驱动程序中高效管理共享内存资源，适用于需要与驱动侧共享数据的场景，有助于简化内存管理、提升数据传输效率。 |
| [ddk\_types.h](capi-ddk-types-h.md) | 提供基础DDK接口所使用的Base DDK类型、枚举值和数据结构。 |
