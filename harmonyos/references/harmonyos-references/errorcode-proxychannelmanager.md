---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-proxychannelmanager
title: 代理通道管理错误码
breadcrumb: API参考 > 系统 > 网络 > Distributed Service Kit（分布式管理服务） > 错误码 > 代理通道管理错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:01:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ef4fdf5026af5439377ef3e447f34ede67456f5680e36b889b957a9652eaecbe
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 32390001 蓝牙已关闭

**错误信息**

BR is disabled.

**错误描述**

本端设备已关闭蓝牙。

**可能原因**

本端设备蓝牙已关闭。

**处理步骤**

打开本端设备蓝牙，重新尝试操作。

## 32390002 设备未配对

**错误信息**

Device not paired.

**错误描述**

本端设备蓝牙未配对成功。

**可能原因**

1. 本端设备未与目标设备完成蓝牙配对。
2. 目标设备未启动服务监听。
3. 使用了无效的MAC或者UUID。

**处理步骤**

1. 使用运动健康应用完成设备添加及配对。
2. 检查目标设备服务监听情况。
3. 检查输入的MAC和UUID的有效性，MAC应为XX:XX:XX:XX:XX:XX格式的蓝牙MAC地址字符串，UUID应为标准UUID格式字符串，如xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx。

## 32390004 通道ID非法或者不可用

**错误信息**

ChannelId is invalid or unavailable.

**错误描述**

调用代理通道接口时传入的通道ID不符合要求或该通道已失效，导致操作无法继续。

**可能原因**

1. 传入了非法的channelId，channelId应为openProxyChannel返回的number类型通道标识。
2. 该channelId对应的通道已通过closeProxyChannel关闭，关闭后channelId不再可用。

**处理步骤**

1. 检查代码逻辑，确认传入的channelId是否为openProxyChannel返回的channelId。
2. 检查代码逻辑，确认该channelId对应的通道是否已关闭，若已关闭则不应继续使用该channelId；如需继续通信，请重新调用openProxyChannel建立新通道。

## 32390006 参数错误

**错误信息**

Parameter error.

**错误描述**

调用代理通道接口时传入的参数不符合要求，如MAC或UUID格式异常、入参类型错误等，导致接口调用失败。

**可能原因**

1. 传入的MAC或者UUID格式异常（MAC应为XX:XX:XX:XX:XX:XX格式的蓝牙MAC地址字符串，UUID应为标准UUID格式字符串，如xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx）。
2. 函数入参类型错误。

**处理步骤**

1. 检查代码逻辑，确认MAC为XX:XX:XX:XX:XX:XX格式的蓝牙MAC地址字符串，UUID为标准UUID格式字符串，如xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx。
2. 检查代码逻辑，确认入参类型与接口定义一致。

## 32390100 内部异常

**错误信息**

Internal error.

**错误描述**

系统内部发生异常，可能导致当前操作执行失败或服务不可用。

**可能原因**

系统错误，如空指针、内存不足、分布式服务异常重启、IPC异常、JS引擎异常等。

**处理步骤**

1. 重试操作。
2. 若问题仍存在，重启应用。
3. 若重启无效，升级应用或升级设备版本。

## 32390101 调用受限

**错误信息**

Call is restricted.

**错误描述**

未授权调用，调用受限。

**可能原因**

未授权进程进行了访问。

**处理步骤**

申请代理通道管理所需权限（请从代理通道管理API接口文档中确认具体权限名称），并在应用配置中声明对应权限后重新尝试。

## 32390102 操作失败或者连接超时

**错误信息**

Operation failed or Connection timed out.

**错误描述**

蓝牙底层故障导致代理通道操作未成功完成，或在规定时间内未建立连接而超时。

**可能原因**

底层蓝牙故障导致连接失败或者连接超时。

**处理步骤**

1. 关闭后重新开启本端设备和目标设备的蓝牙。
2. 重启本端设备和目标设备后，再打开设备的蓝牙。

## 32390103 发送数据超长

**错误信息**

Data too long.

**错误描述**

通过代理通道发送的数据长度超过最大限制（4096字节），导致发送失败。

**可能原因**

发送的数据长度超过了4096个字节。

**处理步骤**

确保发送的数据长度不超过4096字节，如数据过长请分段发送。

## 32390104 发送数据失败

**错误信息**

Send failed.

**错误描述**

通过代理通道发送数据时因蓝牙故障导致数据未能成功送达目标设备。

**可能原因**

底层蓝牙连接故障或协议异常。

**处理步骤**

1. 尝试重启本端设备蓝牙和目标设备蓝牙。
2. 尝试重启本端设备和目标设备。
