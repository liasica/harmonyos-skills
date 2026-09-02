---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-inputdevice
title: 输入设备错误码
breadcrumb: API参考 > 系统 > 基础功能 > Input Kit（多模输入服务） > 错误码 > 输入设备错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:02:09+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:977904c93ecc727b70ea0ceab2a05b31ad82a7b33cde007fa47aa06b1e28ce23
---

**说明** 

* 以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码](errorcode-universal.md)。

## 3900002 键盘设备没有连接

**错误信息**

There is currently no keyboard device connected.

**错误描述**

当前未检测到已连接的键盘设备。

**可能原因**

输入设备的物理连接断开。

**处理步骤**

检查设备的物理连接是否断开。

## 3900003 非输入法应用调用

**错误信息**

It is prohibited for non-input applications.

**错误描述**

禁止非输入法应用调用此接口。

**可能原因**

非输入法应用调用此接口。

**处理步骤**

请使用输入法应用调用该接口。

## 3800001 多模输入服务内部错误

**错误信息**

Input service exception. Possible causes: 1. Memory allocation failure. 2. Thread busy. 3. Service terminated abnormally. 4. Other unexpected errors. Try again later.

**错误描述**

多模输入服务内部错误。

**可能原因**

内存分配失败，线程繁忙，服务运行异常等非预期错误。

**处理步骤**

建议稍后重试。
