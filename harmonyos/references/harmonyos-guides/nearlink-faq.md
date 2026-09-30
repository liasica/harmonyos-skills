---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nearlink-faq
title: NearLink Kit常见问题
breadcrumb: 指南 > 系统 > 网络 > NearLink Kit（星闪服务） > NearLink Kit常见问题
category: harmonyos-guides
scraped_at: 2026-10-01T07:34:31+08:00
doc_updated_at: 2026-09-30
content_hash: sha256:0b8f9b23c106887c2f5678a66ce410bb8cce79a7a9f23fbef59cc0c3672020a5
---

## 连续进行数据传输时数据发送失败的问题

连续多次调用[writeData](../harmonyos-references/nearlink-data-transfer-api.md#writedata)接口可能会导致发送队列拥塞，从而发送失败。

您可以通过设置数据发送间隔来解决连续传输数据时失败的问题。使用[setInterval](../harmonyos-references/js-apis-timer.md#setinterval)设置函数调用的时间间隔，建议的数据发送时间间隔为10ms。

## 星闪标准服务UUID的格式

通用唯一标识（UUID）用来指示条目描述的具体内容。标准服务或标准服务成员使用 16 比特通用唯一标识。

星闪目前支持的UUID格式形如：37BEA880-FC70-11EA-B720-00000000FDEE，包含128比特。其中前112比特由基础标识决定，128比特基础标识为固定值：37BEA880-FC70-11EA-B720-000000000000；后16比特通用唯一标识指示标准服务或标准服务成员。

标准服务或标准服务成员使用的 16 比特通用唯一标识由星闪联盟统一进行分配，具有全局的唯一性。通过标识，客户端可以明确条目承载的是某一个服务、属性、方法、事件和引用了某一个服务。详情可查阅“[星闪标准服务标识](https://sparklink.org.cn/trial/identCid/identListSsid)”。

## 星闪数据传输方式的选择

星闪提供了基于[SSAP交互](nearlink-ssap-server-connect.md)和基于[端口数据传输](nearlink-start-data-transfer.md)两种数据传输方式。

其中，对于低功耗、小数据量场景，建议使用基于SSAP的数据传输；对于高吞吐量、大文件传输场景，建议使用基于端口的数据传输。

## 客户端如何接收属性变化通知

客户端接收属性变化通知（即收到[on('propertyChange')](../harmonyos-references/nearlink-ssap.md#on-propertychange)回调）需同时满足以下条件：

1. 服务端在创建该属性时声明了通知（NOTIFY）操作和客户端属性值配置描述符（CLIENT\_PROPERTY\_CONFIG）；
2. 客户端已与服务端成功建立SSAP连接；
3. 客户端已通过[getServices()](../harmonyos-references/nearlink-ssap.md#getservices)获取到该属性；
4. 客户端已调用[setPropertyNotification()](../harmonyos-references/nearlink-ssap.md#setpropertynotification)启用该属性的通知；
5. 客户端已调用[on('propertyChange')](../harmonyos-references/nearlink-ssap.md#on-propertychange)注册属性变化回调。

满足上述条件后，服务端调用[notifyPropertyChanged()](../harmonyos-references/nearlink-ssap.md#notifypropertychanged)更新属性值时，会向客户端发送属性变化通知。若上述任一条件不满足，客户端将收不到通知。

**说明** 

连接断开后，已启用的通知会失效，重新连接后需重新调用[setPropertyNotification()](../harmonyos-references/nearlink-ssap.md#setpropertynotification)启用。
