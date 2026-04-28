---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nearlink-faq
title: NearLink Kit常见问题
breadcrumb: 指南 > 系统 > 网络 > NearLink Kit（星闪服务） > NearLink Kit常见问题
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fe8852541a7d64f955eef89f9bc6f9cd1cda6c8b20fd6ef89cc7afcde64dda2d
---

## 连续进行数据传输时数据发送失败的问题

连续多次调用[writeData](../harmonyos-references/nearlink-data-transfer-api.md#writedata)接口可能会导致发送队列拥塞，从而发送失败。

您可以通过设置数据发送间隔来解决连续传输数据时失败的问题。使用[setInterval](../harmonyos-references/js-apis-timer.md#setinterval)设置函数调用的时间间隔，建议的数据发送时间间隔为10ms。

## 星闪标准服务UUID的格式

通用唯一标识（UUID）用来指示条目描述的具体内容。标准服务或标准服务成员使用 16 比特通用唯一标识。

星闪目前支持的UUID格式形如：37BEA880-FC70-11EA-B720-00000000FDEE，包含128比特。其中前112比特由基础标识决定，128比特基础标识为固定值：37BEA880-FC70-11EA-B720-000000000000；后16比特通用唯一标识指示标准服务或标准服务成员。

标准服务或标准服务成员使用的 16 比特通用唯一标识由星闪联盟统一进行分配，具有全局的唯一性。通过标识，客户端可以明确条目承载的是某一个服务、属性、方法、事件和引用了某一个服务。详情可查阅“[星闪标准服务标识](https://sparklink.org.cn/trial/identCid/identListSsid)”。
