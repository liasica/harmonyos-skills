---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netethernet
title: NetEthernet
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 模块 > NetEthernet
category: harmonyos-references
scraped_at: 2026-09-02T14:52:21+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4d63b2589318e83ab493785f52bd30b79be47ddcf29e1bd4eec4c6b5df9c5380
---

## 概述

该模块主要用于获取设备上所有以太网网卡的MAC地址列表和IP地址列表，适用于需要获取有线网络连接信息的场景。

以太网网卡是指设备上的有线网络接口，每个以太网网卡都有唯一的MAC地址（物理地址）和可能配置的IP地址。MAC地址用于在网络中唯一标识网络设备，IP地址用于网络通信。

使用方法：调用OH\_Ethernet\_GetMacAddress获取以太网网卡的MAC地址列表，调用OH\_Ethernet\_GetNetAddress获取以太网网卡的IP地址列表。返回的数据结构中包含接口名称和对应的地址信息。

**起始版本：** 26.0.0

## 文件汇总

| 名称 | 描述 |
| --- | --- |
| [net\_ethernet.h](capi-net-ethernet-h.md) | 为以太网网卡模块提供C接口。 |
| [net\_ethernet\_type.h](capi-net-ethernet-type-h.md) | 为以太网网卡模块C接口定义数据结构。 |
