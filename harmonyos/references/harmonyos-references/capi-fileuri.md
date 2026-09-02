---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-fileuri
title: fileUri
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 模块 > fileUri
category: harmonyos-references
scraped_at: 2026-09-02T14:51:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7fa63c7249a1d59f217942b6608215e6b56be2d655e895a41eaee03bfdeac822
---

## 概述

文件统一资源标识符（File Uniform Resource Identifier）。

支持fileUri与路径之间的转换，以及fileUri的格式校验。该模块主要用于URI格式验证和URI转换处理，URI用于应用间文件分享场景，可将应用沙箱路径按系统规则转换为URI，避免直接传递沙箱路径。调用者需保证所有接口入参的有效性，接口按照固定规则转换输出结果，并不检查对应文件或目录是否存在。

**系统能力：** SystemCapability.FileManagement.AppFileService

**起始版本：** 12

## 文件汇总

| 名称 | 描述 |
| --- | --- |
| [oh\_file\_uri.h](capi-oh-file-uri-h.md) | 提供URI和路径之间的相互转换、目录URI获取以及URI格式校验的方法，适用于文件分享场景中的URI转换和校验。 |
