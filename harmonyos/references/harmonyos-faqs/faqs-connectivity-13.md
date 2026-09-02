---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-13
title: 怎样获取本机的IP地址
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > 怎样获取本机的IP地址
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:16+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:824eb5d673fd899643692c2ca345eb21705d9e3e05e481a75cd639a0c6d382a4
---

## 问题现象

请问设备连接Wi-Fi，或者在蜂窝网下怎样获取本机的IP？

## 背景知识

* [@ohos.wifiManager (WLAN)](../harmonyos-references/js-apis-wifimanager.md)模块主要提供WLAN基础功能（无线接入、无线加密、无线漫游等）、P2P（peer-to-peer）服务的基础功能和WLAN消息通知的相应服务，让应用可以通过WLAN和其他设备互联互通。
* [@ohos.net.connection](../harmonyos-references/js-apis-net-connection.md)模块提供管理网络一些基础能力，包括获取默认激活的数据网络、获取所有激活数据网络列表、开启关闭飞行模式、获取网络能力信息等功能。
* [connection.getConnectionPropertiesSync](../harmonyos-references/js-apis-net-connection.md#connectiongetconnectionpropertiessync10)获取netHandle对应的网络的连接信息，返回值[ConnectionProperties](../harmonyos-references/js-apis-net-connection.md#connectionproperties)的linkAddresses链路信息包含address链路地址。

## 解决方案

* 场景一：设备连接Wi-Fi后，如何获取当前设备的IP地址？

  使用@ohos.wifiManager模块[getIpInfo](../harmonyos-references/js-apis-wifimanager.md#wifimanagergetipinfo)、[getLinkedInfo](../harmonyos-references/js-apis-wifimanager.md#wifimanagergetlinkedinfo)接口获取当前设备的IP地址，其中ipAddress值为number类型，需要转换为IP常用格式，具体请参考[IP格式转换](faqs-connectivity-4.md)。
* 场景二：设备连接蜂窝网络后，如何获取当前设备的IP地址？

  使用@ohos.net.connection模块的[getconnectionproperties](../harmonyos-references/js-apis-net-connection.md#connectiongetconnectionproperties)接口获取ConnectionProperties信息，linkAddresses包含链路信息，dnses网络地址包含的IP地址。

  **说明** 

  需要权限ohos.permission.GET\_NETWORK\_INFO。

## 常见FAQ

Q：connection.getConnectionProperties方法在5.1.5.150下为何无法获取到IPv6的IP地址？

A：目前6.0版本支持fe80，[connection.getconnectionproperties](../harmonyos-references/js-apis-net-connection.md#connectiongetconnectionproperties)可以正常获取IPv6地址。
