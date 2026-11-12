---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk
title: CloudDisk
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 模块 > CloudDisk
category: harmonyos-references
scraped_at: 2026-11-12T09:55:05+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:b40f220210cd8ca67655b3df8c564fa8e7b33b37c7bf6ec362aceb5e9b3b2f7a
---

## 概述

此模块提供云盘管理模块的接口和错误码。应用注册一个同步路径的作为根节点，以该路径为父目录的所有子目录都属于同步的范围，该目录简称为：同步根路径。

注册成功后，可以监听该同步根路径下文件的变更，可以查询同步根路径下文件的历史操作记录，以及设置或查询同步根路径下文件的同步状态。

**起始版本：** 21

## 文件汇总

| 名称 | 描述 |
| --- | --- |
| [cloud\_disk\_error\_code.h](capi-cloud-disk-error-code-h.md) | 提供云盘管理模块的错误码定义，用于标识云盘管理接口调用过程中的异常情况，帮助开发者定位和处理权限校验失败、参数无效、路径冲突、IPC连接失败等问题。 |
| [oh\_cloud\_disk\_manager.h](capi-oh-cloud-disk-manager-h.md) | 云盘管理模块的接口定义，提供云盘同步根路径的注册、激活、监听和查询能力，支持监听文件变更、设置和查询文件同步状态，并提供占位符文件的创建、水合、脱水及回调注册能力，适用于需要在应用内实现云盘文件同步、变更监听和按需下载的场景。 |
