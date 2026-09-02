---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-service-support-kit
title: ArkTS API错误码
breadcrumb: API参考 > 系统 > 基础功能 > Service Support Kit（服务与支持） > ArkTS API > ArkTS API错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:02:11+08:00
doc_updated_at: 2026-08-14
content_hash: sha256:5a9d1a1b0ef6210d49f0eb47a497cd31c0e2035d0eb3fffb610d3725a177e9c2
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 1029600001 设备运行内存不足

**错误信息**

Insufficient memory.

**错误描述**

设备运行内存不足。

**可能原因**

系统运行内存耗尽。

**处理步骤**

关闭其他应用后重试。

## 1029600101 设备一致性校验服务异常

**错误信息**

Device detection service exception.

**错误描述**

设备一致性校验服务异常。

**可能原因**

1. 系统内部运行异常。
2. 内部程序运行异常。
3. 智能检测版本不支持。

**处理步骤**

1. 重启设备后重新尝试。
2. 升级系统或智能检测版本后重新尝试。

## 1029600301 网络异常

**错误信息**

Network error.

**错误描述**

网络异常。

**可能原因**

网络未连接或网络异常。

**处理步骤**

确保设备网络连接正常，可尝试切换网络后重试。

## 1029600302 智能检测隐私声明未同意

**错误信息**

Smart Diagnosis privacy statement not accepted.

**错误描述**

智能检测隐私声明未同意。

**可能原因**

智能检测隐私声明未同意。

**处理步骤**

用户打开“智能检测”（操作路径：“我的华为 -> 服务 -> 快捷服务 -> 智能检测”），查看并同意隐私声明。
