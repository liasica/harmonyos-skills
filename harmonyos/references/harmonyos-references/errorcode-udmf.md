---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-udmf
title: 统一数据管理框架错误码
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > 错误码 > 统一数据管理框架错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:00:44+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e372d19b9db772b56f544774c425f1b6d75d903ee8f7cfe62e8a9e9bb0585cb0
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 20400001 设置已存在，若要重新配置请删除现有的共享选项

**错误信息**

Settings already exist. To reconfigure, remove the existing sharing options.

**错误描述**

应用程序设置拖拽通道数据可使用的范围时，将要设置的信息在数据库中已存在。

**可能原因**

调用[setAppShareOptions](js-apis-data-unifieddatachannel.md#unifieddatachannelsetappshareoptions14)重复设置拖拽通道数据可使用的范围时，系统会产生此错误码。

**处理步骤**

先调用[removeAppShareOptions](js-apis-data-unifieddatachannel.md#unifieddatachannelremoveappshareoptions14)清除当前拖拽通道数据可使用的范围，再调用[setAppShareOptions](js-apis-data-unifieddatachannel.md#unifieddatachannelsetappshareoptions14)重新设置。
