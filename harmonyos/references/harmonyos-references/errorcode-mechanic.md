---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-mechanic
title: 机械体控制模块错误码
breadcrumb: API参考 > 系统 > 硬件 > Mechanic Kit（机械设备管理服务） > 错误码 > 机械体控制模块错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:02:15+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b9a5ced0f71d9cb8a01591c93678ae14b858627753bc62aeeb85f6382d642ea9
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 33300001 系统错误

**错误信息**

Service exception.

**错误描述**

系统错误。

**可能原因**

服务侧业务逻辑处理发生不可恢复的错误。

**处理步骤**

系统错误不可恢复。

## 33300002 设备未连接

**错误信息**

Device not connected.

**错误描述**

设备未连接。

**可能原因**

没有可用的已连接设备。

**处理步骤**

确保开发设备与机械体通过蓝牙连接正常。

## 33300003 功能不支持

**错误信息**

Feature not supported.

**错误描述**

当前开发设备不支持该功能。

**可能原因**

当前开发设备的相机驱动不支持目标检测功能。

**处理步骤**

为当前开发设备的相机驱动增加目标检测功能或者更换支持相机驱动目标检测功能的开发设备。
