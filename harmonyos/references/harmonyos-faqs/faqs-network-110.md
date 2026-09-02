---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-110
title: 应用网络类型与显示状态不匹配
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 应用网络类型与显示状态不匹配
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:255a1517984b9c88c01ace775075b3eae763724402707a1324c42a4e81965f21
---

## 问题现象

在应用使用过程中，需要根据不同的网络类型执行相应的操作。例如，根据当前的网络环境（如移动数据或Wi-Fi）来决定是否自动播放下载的视频。同时，应用有需要显示当前手机的网络制式（如4G、5G或Wi-Fi）的场景，但有时显示的网络状态与实际网络环境不符。

## 背景知识

* [网络连接管理](../harmonyos-guides/net-connection-manager.md)：Network Kit（网络服务）中网络连接管理提供管理网络一些基础能力，包括WiFi/蜂窝/Ethernet等多网络连接优先级管理、网络质量评估、订阅默认/指定网络连接状态变化、查询网络连接信息、DNS解析等功能。
  1. [接收指定网络的状态变化通知](../harmonyos-guides/net-connection-manager.md#接收指定网络的状态变化通知)。

     | 接口 | 描述 |
     | --- | --- |
     | [register](../harmonyos-references/js-apis-net-connection.md#register) | 订阅指定网络状态变化的通知。如需监听特定事件，确保调用on监听事件后再调用register进行注册。 |
     | [on('netAvailable')](../harmonyos-references/js-apis-net-connection.md#onnetavailable) | 订阅网络可用事件，即启动应用时有网络，或者断开网络后再重连，会被netAvailable监听到。此接口需在调用register接口之前调用。 |
     | [on('netUnavailable')](../harmonyos-references/js-apis-net-connection.md#onnetunavailable) | 订阅网络不可用事件，即启动应用时没有网络连接（没有连接WIFI和蜂窝数据，连接一个没有联网的WIFI也不行）会被netUnavailable监听到。此接口要在register接口调用前调用。 |
     | [on('netLost')](../harmonyos-references/js-apis-net-connection.md#onnetlost) | 订阅网络丢失事件，即启动应用时有网络连接，后面断开连接的情况下，会被netLost监听到。此接口要在register接口调用前调用。 |
     | [unregister](../harmonyos-references/js-apis-net-connection.md#unregister) | 取消订阅默认网络状态变化的通知。 |
  2. [监控默认网络变化并主动重建网络连接](../harmonyos-guides/net-connection-manager.md#监控默认网络变化并主动重建网络连接)：根据当前网络状态及网络质量情况，默认网络可能会发生变化，监控默认网络的变化后，应用报文能够快速迁移到新默认网络上。
  3. [获取所有注册的网络](../harmonyos-guides/net-connection-manager.md#获取所有注册的网络)：调用[getAllNets](../harmonyos-references/js-apis-net-connection.md#connectiongetallnets)方法，获取所有处于连接状态的网络列表。
  4. [查询默认网络或者指定网络的连接信息](../harmonyos-guides/net-connection-manager.md#查询默认网络或者指定网络的连接信息)。

     | 方法名 | 描述 |
     | --- | --- |
     | [getDefaultNet](../harmonyos-references/js-apis-net-connection.md#connectiongetdefaultnet) | 异步获取默认激活的数据网络。 |
     | [getNetCapabilities](../harmonyos-references/js-apis-net-connection.md#connectiongetnetcapabilities) | 获取netHandle对应网络的能力信息。能力信息包含了网络类型(蜂窝网络、Wi-Fi网络、以太网网络等)、网络具体能力等网络信息。 |
     | [getConnectionProperties](../harmonyos-references/js-apis-net-connection.md#connectiongetconnectionproperties) | 获取netHandle对应的网络的连接信息。 |
  5. [判断默认网络是否可以访问互联网](../harmonyos-guides/net-connection-manager.md#判断默认网络是否可以访问互联网)。

     | 方法名 | 描述 |
     | --- | --- |
     | [getDefaultNetSync](../harmonyos-references/js-apis-net-connection.md#connectiongetdefaultnetsync9) | 使用同步方法获取默认激活的数据网络。 |
     | [getNetCapabilitiesSync](../harmonyos-references/js-apis-net-connection.md#connectiongetnetcapabilitiessync10) | netHandle有效的情况下，获取netHandle对应网络的能力信息，使用同步方式返回。 |
* radio模块（网络搜索）：应用可以调用API获取当前注册网络名称、网络服务状态以及信号强度相关信息，详情请参考[@ohos.telephony.radio (网络搜索)](../harmonyos-references/js-apis-radio.md)。
  1. [getSignalInformation](../harmonyos-references/js-apis-radio.md#radiogetsignalinformation7)：获取指定SIM卡槽对应的注册网络信号强度信息列表。
  2. [SignalInformation](../harmonyos-references/js-apis-radio.md#signalinformation)：网络信号强度信息对象。

## 问题定位

1. 搜索[register](../harmonyos-references/js-apis-net-connection.md#register)，检查是否注册网络监听（当网络可用时，会收到netAvailable事件的回调；当网络不可用时，会收到netUnavailable事件的回调）。
2. 搜索[on('netAvailable')](../harmonyos-references/js-apis-net-connection.md#onnetavailable)/[on('netLost')](../harmonyos-references/js-apis-net-connection.md#onnetlost)等，检查是否在调用register接口后订阅网络可用/丢失等事件，并执行相应的操作。
3. 搜索[getDefaultNet](../harmonyos-references/js-apis-net-connection.md#connectiongetdefaultnet)/[getDefaultNetSync](../harmonyos-references/js-apis-net-connection.md#connectiongetdefaultnetsync9)，检查是否在on('netAvailable')事件中获取默认激活的数据网络。继续搜索[getNetCapabilities](../harmonyos-references/js-apis-net-connection.md#connectiongetnetcapabilities)/[getNetCapabilitiesSync](../harmonyos-references/js-apis-net-connection.md#connectiongetnetcapabilitiessync10)，检查是否获取netHandle对应网络的能力信息，能力信息包含了网络类型(蜂窝网络、Wi-Fi网络、以太网网络等)。
   * 默认网络是Wi-Fi，则直接确认网络类型是Wi-Fi。
   * 默认网络是蜂窝网络，搜索[getSignalInformation](../harmonyos-references/js-apis-radio.md#radiogetsignalinformation7)，检查是否获取指定SIM卡槽对应的注册网络信号强度信息列表，返回[SignalInformation](../harmonyos-references/js-apis-radio.md#signalinformation)对象的数组中携带网络类型NetworkType。

## 分析结论

由于未通过register监听网络状态变化，并使用on('netAvailable')/on('netLost')订阅网络可用/丢失等事件来动态更新网络类型和业务逻辑，或者相应逻辑不完善导致故障现象。

## 修改建议

1. 调用[createNetConnection](../harmonyos-references/js-apis-net-connection.md#connectioncreatenetconnection)方法，创建一个NetConnection对象。
2. 调用该对象的register方法，订阅指定网络状态变化的通知。当网络可用时，会收到netAvailable事件的回调；当网络不可用时，会收到netUnavailable事件的回调。
3. 调用该对象的on('netAvailable')、[on('netUnavailable')](../harmonyos-references/js-apis-net-connection.md#onnetunavailable)和on('netLost')等方法，传入type和callback，订阅关心的事件，并获取相应网络类型。
4. 当不使用该网络时，可以调用该对象的[unregister](../harmonyos-references/js-apis-net-connection.md#unregister)方法，取消订阅。

详情请参考[管理网络连接](../harmonyos-guides/net-connection-manager.md)。
