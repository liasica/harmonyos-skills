---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-telephony
title: 电话子系统错误码
breadcrumb: API参考 > 系统 > 网络 > Telephony Kit（蜂窝通信服务） > 错误码 > 电话子系统错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:09:23+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:5e29d440f5bc905b8a856e4767da3ef10b5573edd2c644f78cb69d2e25dc2ae8
---

说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 8300001 输入参数不在处理范围内

PhonePC/2in1TabletWearable

**错误信息**

The input parameter value is out of range.

**错误描述**

输入参数不在处理范围内，如slotId无效等，将无法进行相应的操作。

**可能原因**

输入参数无效。

**处理步骤**

请输入正确的有效参数。

## 8300002 服务连接失败

PhonePC/2in1TabletWearable

**错误信息**

Service connection failed.

**错误描述**

操作失败。无法连接到服务。

**可能原因**

服务启动失败，IPC连接失败等。

**处理步骤**

本次操作异常，请稍后重试。

## 8300003 系统内部错误

PhonePC/2in1TabletWearable

**错误信息**

System internal error.

**错误描述**

系统内部错误。

**可能原因**

网络异常，数据读写失败等。

**处理步骤**

本次操作异常，请稍后重试。

## 8300004 未识别SIM卡

PhoneTabletWearable

**错误信息**

No SIM card found.

**错误描述**

没有识别到SIM卡。

**可能原因**

未插入SIM卡或未正常插入SIM卡。

**处理步骤**

请插卡或重新拔插SIM卡。

## 8300999 内部错误

PhonePC/2in1TabletWearable

**错误信息**

Internal error.

**错误描述**

内部错误。

**可能原因**

内存不足、内存操作失误、空指针。

**处理步骤**

操作异常，请稍后再试。

## 8301001 SIM卡未激活

PhoneTabletWearable

**错误信息**

SIM card is not activated.

**错误描述**

SIM卡未激活。

**可能原因**

没有激活SIM卡。

**处理步骤**

请激活SIM卡。

## 8301002 SIM卡读取数据或者更新数据失败

PhoneTabletWearable

**错误信息**

The SIM card failed to read or update data.

**错误描述**

SIM卡读取数据或者更新数据失败。

**可能原因**

SIM不支持该操作，或者SIM卡已损坏。

**处理步骤**

请联系SIM卡运营商，或者更换SIM卡。

## 8301003 随卡配置错误

**错误信息**

Operator config error.

**错误描述**

随卡配置错误。

**可能原因**

未预置对应SIM卡的随卡配置文件。

**处理步骤**

请检查是否插入正确的SIM卡。

## 8401001 UT连接失败

**错误信息**

UT is not connected.

**错误描述**

UT未连接。

**可能原因**

当前运营商不支持从Wi-Fi下发UT请求，但是当前设备Wi-Fi已连上。

**处理步骤**

断开Wi-Fi，再重发UT请求。

## 3120001 服务连接失败

PhoneWearable

**错误信息**

Service connection failed.

**错误描述**

操作失败。无法连接到服务。

**可能原因**

服务启动失败，IPC连接失败等。

**处理步骤**

本次操作异常，请稍后重试。

## 3120002 系统内部错误

PhoneWearable

**错误信息**

System internal error.

**错误描述**

系统内部错误。

**可能原因**

网络异常，数据读写失败等。

**处理步骤**

本次操作异常，请稍后重试。

## 8800001 输入参数不在处理范围内

PhoneTabletWearable

**错误信息**

The input parameter value is out of range.

**错误描述**

输入参数不在处理范围内，如slotId无效等，将无法进行相应的操作。

**可能原因**

输入参数无效。

**处理步骤**

请输入正确的有效参数。

## 8800002 服务连接失败

PhoneTabletWearable

**错误信息**

Service connection failed.

**错误描述**

操作失败。无法连接到服务。

**可能原因**

服务启动失败，IPC连接失败等。

**处理步骤**

本次操作异常，请稍后重试。

## 8800003 系统内部错误

PhoneTabletWearable

**错误信息**

System internal error.

**错误描述**

系统内部错误。

**可能原因**

网络异常，数据读写失败等。

**处理步骤**

本次操作异常，请稍后重试。

## 8800999 内部错误

PhoneTabletWearable

**错误信息**

Internal error.

**错误描述**

内部错误。

**可能原因**

内存不足、内存操作失误、空指针。

**处理步骤**

操作异常，请稍后再试。
