---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-connection
title: 网络连接管理错误码
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > 错误码 > 网络连接管理错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:08:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b70ce9bfe248f05afeaab7e0eec1a345ec30f3d7f84eb8332042f656a66367f7
---

说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码](errorcode-universal.md)说明文档。

## 2100001 非法参数值

PhonePC/2in1TabletTVWearable

**错误信息**

Invalid parameter value.

**错误描述**

非法参数值。

**可能原因**

输入参数取值范围错误。

**处理步骤**

检查输入参数的取值范围是否正确。

## 2100002 连接服务失败

PhonePC/2in1TabletTVWearable

**错误信息**

Failed to connect to the service.

**错误描述**

操作失败，连接系统服务发生异常。

**可能原因**

服务发生异常。

**处理步骤**

检查系统服务运行状态是否正常。

## 2100003 系统内部错误

PhonePC/2in1TabletTVWearable

**错误信息**

System internal error.

**错误描述**

系统内部错误。

**可能原因**

1.内存异常。

2.空指针。

**处理步骤**

1.检查内存空间是否充足，清理内存后重试。

2.系统异常，请稍后重试或重启设备。

## 2101007 callback不存在

PhonePC/2in1TabletTVWearable

**错误信息**

The callback does not exist.

**错误描述**

不存在的callback对象。

**可能原因**

未执行激活&监听指定属性网络请求并注册回调。

**处理步骤**

检查callback对象，确保注销callback对象前，已执行注册函数。

## 2101008 已存在相同的callback

PhonePC/2in1TabletTVWearable

**错误信息**

The callback already exists.

**错误描述**

已经注册的callback。

**可能原因**

激活&监听指定属性网络并注册回调时，callback对象重复注册。

**处理步骤**

1.确保待注册的callback对象未进行过注册。

2.若callback对象已进行过注册，执行已存在的注册。

## 2101022 请求数量超过最大值

PhonePC/2in1TabletTVWearable

**错误信息**

The number of requests exceeded the maximum allowed.

**错误描述**

网络请求数超过了最大值。

**可能原因**

1.激活&监听指定属性网络请求数超过了最大值。

2.NetConnection.register接口超过了最大注册数量限制。

**处理步骤**

1.建议通过日志信息“Over the max request number”定位问题。

2.使用完NetConnection.register接口后，及时调用unregister接口取消注册。

## 2100301 调用方身份验证不通过（非VPN应用）

PhonePC/2in1TabletTVWearable

**错误信息**

Incorrect usage in non-VPN application.

**错误描述**

接口调用方不是VPN应用。

**可能原因**

接口调用方不是VPN应用。

**处理步骤**

确保在VPN应用中调用接口。

## 2100400 传入网卡名不正确（非以太网）

**错误信息**

The input network interface is incorrect.

**错误描述**

接口调用传入的网卡名不正确。

**可能原因**

接口调用传入的网卡名不是eth0等以太网网卡名。

**处理步骤**

确保传入的网卡名为eth0等以太网网卡名。

## 2100401 未找到VLAN上配置的IP地址

**错误信息**

The input ip address not found.

**错误描述**

未找到传入的IP地址。

**可能原因**

未在VLAN上找到传入的IP地址。

**处理步骤**

确保传入的IP地址已配置在VLAN上。
