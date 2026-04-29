---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/networkboost-netmultipath-overview
title: 概述
breadcrumb: 指南 > 系统 > 网络 > Network Boost Kit（网络加速服务） > 连接迁移（多网并发） > 概述
category: harmonyos-guides
scraped_at: 2026-04-29T13:32:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5d783a5c26fb2a29fe86635b6da2a65b3a495ea1076ecb93fb0563037fee1652
---

从6.0.0(20)版本开始，支持连接迁移（多网并发）功能。

多网并发是系统提供接口可以建立多个网络通路，应用发起多网请求后，系统依据业务场景决定并发组合和实施相应的并发管控，并对并发做收益度量。使用多网并发功能的原则是应用申请（受限权限）、系统管控、最小化使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/qsgtAN6aRX-iPlZ0uDi8mA/zh-cn_image_0000002589324797.png?HW-CC-KV=V1&HW-CC-Date=20260429T053247Z&HW-CC-Expire=86400&HW-CC-Sign=9638D45E3636F7D57B94EA06A9597832A3E70B861716DCB4F2EC08B7D50D657F)

其中各步骤功能如下：

监听并发：应用监听多网状态通知获得状态变更信息；同时网络子系统会给出多网拉起和释放等建议措施。

查询配额：应用获取多网并发配额信息(已使用和剩余的多网次数和时长)，自主实现合理使用多网并发能力。

启动并发：应用启动多网并发前，可主动调用业务场景设置接口，告知系统进入特定业务场景，并通过显式的多网发起接口来触发多网并发。

网卡绑定：在多网状态监听接口中，应用获取的新网卡，按socket或按应用来绑定。

终止多网：当应用体验恢复时需主动释放多网，并根据应用实际业务，调用业务场景设置接口，告知系统退出特定业务场景，同时系统也会因管控而主动释放多网，以确保多网不被滥用。

收益度量：根据APP传输体验反馈信息和系统Qoe算法，查看系统计算和应用反馈的一致性。

注：多网并发能力受网络加速开关、权限、配额、功耗等方面管控，同时针对不规范的行为将进行惩罚，包括但不限于并发终止、配额降低、受限权限吊销等。
