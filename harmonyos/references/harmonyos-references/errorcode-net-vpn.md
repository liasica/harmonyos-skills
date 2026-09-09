---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-vpn
title: VPN错误码
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > 错误码 > VPN错误码
category: harmonyos-references
scraped_at: 2026-09-10T06:27:16+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:f6c0f79c942fe46a045ba7158de8a0fa1f8f74132330d8b9a97225f35ea6294f
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码](errorcode-universal.md)说明文档。

## 2200001 非法参数值

**错误信息**

Invalid parameter value.

**错误描述**

非法参数值。

**可能原因**

输入参数取值范围错误。

**处理步骤**

检查输入参数的取值范围是否正确。

## 2200002 连接服务失败

**错误信息**

Failed to connect to the service.

**错误描述**

操作失败，连接系统服务发生异常。

**可能原因**

服务发生异常。包括但不限于：连接数据库服务异常，连接应用状态管理服务异常等。

**处理步骤**

请检查系统服务运行状态并重试。如果问题仍然存在，收集完整日志后联系技术支持获取帮助。

## 2200003 系统内部错误

**错误信息**

System internal error.

**错误描述**

系统内部错误。

**可能原因**

1. 内存异常。
2. 空指针。

**处理步骤**

1. 检查内存空间是否充足，清理内存后重试。
2. 系统异常，请稍后重试或重启设备。如果问题仍然存在，收集完整日志后联系技术支持获取帮助。

## 2203001 VPN创建失败

**错误信息**

VPN creation denied, please check the user type.

**错误描述**

拒绝创建VPN，请检查当前用户的类型。

**可能原因**

登录系统的用户类型不匹配，GUEST用户不能调用setUp接口。

**处理步骤**

检查当前登录系统用户的类型。

## 2203002 VPN已存在

**错误信息**

VPN exist already, please execute destroy first.

**错误描述**

VPN连接已存在，请先调用destroy接口销毁VPN连接。

**可能原因**

VPN已经被创建。

**处理步骤**

先执行destroy接口，再调用该接口。

## 2203004 无效描述符

**错误信息**

Invalid socket file descriptor.

**错误描述**

无效的文件描述符。

**可能原因**

tcp链路建立失败。

**处理步骤**

检查socket链路是否建立成功。

## 19900001 无效参数

**错误信息**

Invalid parameter value.

**错误描述**

无效参数。

**可能原因**

参数类型或数量错误。

**处理步骤**

请检查参数数量和类型。

## 19900002 系统内部错误

**错误信息**

System internal error.

**错误描述**

VPN系统内部错误。

**可能原因**

空指针、内存分配异常、IPC通信异常等。

**处理步骤**

1. 检查内存空间是否充足，清理内存后重试。
2. 检查VPN系统服务是否正常。如果问题仍然存在，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。
