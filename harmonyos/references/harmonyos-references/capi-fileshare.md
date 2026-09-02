---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-fileshare
title: fileShare
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 模块 > fileShare
category: harmonyos-references
scraped_at: 2026-09-02T14:51:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:cf29673cef34c14290aa52f5110db8f7b954c5f71cf6d6cc07efc6abb5991730
---

## 概述

此模块提供文件分享功能，支持将公共目录文件的统一资源标识符（URI）授权给其他应用程序，使其他应用可按授权访问对应文件或目录。该模块适用于跨应用文件共享场景，通过URI授权机制管理文件访问权限。

**起始版本：** 12

## 文件汇总

| 名称 | 描述 |
| --- | --- |
| [oh\_file\_share.h](capi-oh-file-share-h.md) | 提供基于URI的文件及目录持久化授权、取消持久化授权、权限激活、权限查询等方法，适用于跨应用文件共享场景。持久化授权用于保存访问策略，权限激活用于使已持久化的权限生效。 |
