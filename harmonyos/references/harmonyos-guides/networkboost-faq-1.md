---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/networkboost-faq-1
title: 在进行多网并发传输时，如何判断当前使用的网络是Wi-Fi还是流量
breadcrumb: 指南 > 系统 > 网络 > Network Boost Kit（网络加速服务） > Network Boost Kit常见问题 > 在进行多网并发传输时，如何判断当前使用的网络是Wi-Fi还是流量
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:01+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:0aad58577b2bbe43f8eb12ee582e95ceea59b993bb8025709ad2e61b2320f9aa
---

请求多网成功后可以获取到多个可用的netHandle，通过[connection.getNetCapabilities()](../harmonyos-references/js-apis-net-connection.md#connectiongetnetcapabilities)方法查询网络信息，通过[NetBearType](../harmonyos-references/js-apis-net-connection.md#netbeartype)字段判断网络类型，其中BEARER\_CELLULAR是蜂窝网络，BEARER\_WIFI是Wi-Fi网络。在设计多网并发策略时可以通过网络类型和网络能力调整对应网络通路的网络任务。
