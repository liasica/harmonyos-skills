---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-fileuri
title: fileUri
breadcrumb: API参考 > 应用框架 > Core File Kit（文件基础服务） > C API > 模块 > fileUri
category: harmonyos-references
scraped_at: 2026-04-28T08:05:49+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:d5a5ffa42f21c7f1cd27adcb67081aeaf24b1e76f93984f3dc899bb2b10fef92
---

## 概述

PhonePC/2in1TabletTVWearable

文件统一资源标识符（File Uniform Resource Identifier）。

支持fileuri与路径path的转换，和fileuri的有效性校验。

该类主要用于 URI 格式验证和 URI 转换处理。且uri用于应用间文件分享场景，将应用沙箱路径按照固定关系转换为URI;

调用者需保证所有接口入参的有效性，接口按照固定规则转换输出结果，并不检查其是否存在。

**系统能力：** SystemCapability.FileManagement.AppFileService

**起始版本：** 12

## 文件汇总

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [oh\_file\_uri.h](capi-oh-file-uri-h.md) | 提供uri和路径path之间的相互转换，目录uri获取，以及uri的有效性校验的方法。 |
