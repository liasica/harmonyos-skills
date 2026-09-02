---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-distributedkvstore
title: 分布式键值数据库错误码
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > 错误码 > 分布式键值数据库错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:00:44+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:466ca28b1ebc058d80384cd9cb0657197ded6c692177f450a1321d319c99bbae
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 15100000 无效的参数

**错误信息**

Parameter error. Possible causes:

1. Mandatory parameters are left unspecified.
2. Incorrect parameter types.
3. Parameter verification failed.

**错误描述**

无效的参数。

**可能原因**

入参不符合接口要求，如取值范围、长度、格式等。

**处理步骤**

参考接口参数说明，将参数修改为符合要求的值。

## 15100001 超过最大订阅数量或结果集数量

**错误信息**

Over max limits.

**错误描述**

数据库订阅数目或打开结果集数目超过最大支持上限，当前最大限制数目都是8。

**可能原因**

1. 在调用订阅数据库变化接口[on('dataChange')](js-apis-distributedkvstore.md#ondatachange)时，对数据库的订阅数目已超过最大限制数目8。
2. 调用获取数据库结果集接口[getResultSet](js-apis-distributedkvstore.md#getresultset)时，数据库当前打开的结果集数目超过最大限制数目8。

**处理步骤**

1. 如果在调用订阅数据库变化接口[on('dataChange')](js-apis-distributedkvstore.md#ondatachange)时，对数据库的订阅数量已超过最大限制，调用[off('dataChange')](js-apis-distributedkvstore.md#offdatachange)接口取消对数据库的部分订阅后，再次尝试订阅。
2. 如果在调用获取数据库结果集接口[getResultSet](js-apis-distributedkvstore.md#getresultset)时数据库当前打开的结果集数目超过最大限制，调用[closeResultSet](js-apis-distributedkvstore.md#closeresultset)接口关闭部分打开的结果集后重试。

## 15100002 打开已有数据库时参数配置发生变化

**错误信息**

Open existed database with changed options.

**错误描述**

调用[getKVStore](js-apis-distributedkvstore.md#getkvstore)接口打开已创建的数据库时，传入的options配置参数与创建该数据库时使用的options配置参数不一致。

**可能原因**

打开已创建的数据库时，options参数配置发生了变化，可能原因如下：

1. 期望新建数据库时，使用了已创建过的数据库名称storeId。
2. 期望改变已创建数据库的options参数配置。

**处理步骤**

1. 新建数据库前，请检查数据库名称storeId不与已创建数据库的storeId重名。
2. 期望改变已创建数据库的options参数配置时，当前不支持该操作，请自行删除数据库后使用新的options参数重新创建。

## 15100003 数据库损坏

**错误信息**

Database corrupted.

**错误描述**

该错误码表示在调用[put](js-apis-distributedkvstore.md#put)、[delete](js-apis-distributedkvstore.md#delete)、[get](js-apis-distributedkvstore.md#get)、[sync](js-apis-distributedkvstore.md#sync)等接口时，数据库已损坏。

**可能原因**

调用数据库增、删、查、数据同步等接口操作数据库时，数据库文件已损坏。

**处理步骤**

1. 如果之前备份过数据库，可尝试使用已备份的数据库文件恢复数据库。
2. 如果之前没有备份过数据库，可尝试删除数据库后重新创建。

## 15100004 未找到相关数据

**错误信息**

Not found.

**错误描述**

该错误码表示在调用[deleteKVStore](js-apis-distributedkvstore.md#deletekvstore)、[sync](js-apis-distributedkvstore.md#sync)、[get](js-apis-distributedkvstore.md#get)等接口时，未找到相关数据。

**可能原因**

在调用删除数据库、数据查询、数据同步等接口时未找到相关数据，可能原因如下：

1. 删除数据库操作时，数据库不存在或已删除。
2. 数据库数据查询操作时，相关数据不存在或已删除。
3. 数据库数据同步操作时，数据库不存在或已删除。

**处理步骤**

1. 在删除数据库操作前，请检查数据库名称是否正确或是否重复删除。
2. 在数据库数据查询操作前，请检查查询关键字是否正确。
3. 在数据库数据同步操作前，请检查相关数据库是否已经删除。

## 15100005 数据库或查询结果集已关闭

**错误信息**

Database or result set already closed.

**错误描述**

该错误码表示在调用数据库或查询结果集相关接口时，数据库或查询结果集处于关闭状态。

**可能原因**

在数据库或查询结果集操作前，已经手动关闭了数据库或查询结果集。

**处理步骤**

1. 在数据库相关操作前，请重新打开数据库之后再重试当前操作。
2. 在查询结果集相关操作前，请重新查询获取结果集之后再重试当前操作。

## 15100006 更新数据库加密密钥失败

**错误信息**

Failed to update the key.

**错误描述**

在调用[rekey](js-apis-distributedkvstore.md#rekey)接口更新数据库加密密钥时失败。

**可能原因**

1. 在调用[getKVStore](js-apis-distributedkvstore.md#getkvstore)接口创建数据库时，未使用加密方式（即encrypt为false）。
2. 密钥更新过程中发生内部错误。

**处理步骤**

1. 在使用[rekey](js-apis-distributedkvstore.md#rekey)接口更新加密数据库密钥前，请确保当前数据库为加密数据库（即调用[getKVStore](js-apis-distributedkvstore.md#getkvstore)接口创建数据库时配置encrypt为true）。
2. 重新尝试更新密钥。
