---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk
title: CloudDisk
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 模块 > CloudDisk
category: harmonyos-references
scraped_at: 2026-04-28T08:05:49+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5f61b0835fd0fe86e81b2e457030ae1916b5e845721380b4409004d1872116ed
---

## 概述

PC/2in1Tablet

此模块提供云盘管理模块的接口和错误码。应用注册一个同步路径的作为根节点，以该路径为父目录的所有子目录都属于同步的范围，该目录简称为：同步根路径。

注册成功后，可以监听该同步根路径下文件的变更，可以查询同步根路径下文件的历史操作记录，以及设置或查询同步根路径下文件的同步状态。

**起始版本：** 21

## 文件汇总

PC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [cloud\_disk\_error\_code.h](capi-cloud-disk-error-code-h.md) | 提供云盘管理模块的错误码定义。 |
| [oh\_cloud\_disk\_manager.h](capi-oh-cloud-disk-manager-h.md) | 云盘管理模块的接口定义。 |
