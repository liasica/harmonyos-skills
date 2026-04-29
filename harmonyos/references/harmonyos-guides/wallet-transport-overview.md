---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-transport-overview
title: 概述
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 接入交通卡 > 概述
category: harmonyos-guides
scraped_at: 2026-04-29T13:40:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a1114c08f2325d57c961ec3a74dcc901769f375d899d1573cfeb067dee439ce5
---

Wallet Kit中的交通卡服务提供了开通新卡、在线充值、卡片更新和删卡的开放能力。由于交通卡的实际发行方是交通卡公司，所以开发者的app想要实现上述功能，需要：

1. 对接支付机构（如：华为支付、微信、支付宝、银联等），完成开卡、充值的订单支付。
2. 获得交通卡公司的同意并且用开发者的业务服务器对接交通卡公司的系统完成上述功能对应的业务申请。

说明

交通卡服务开放能力**仅对受邀应用**开放使用。

## 整体架构

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/t2as6BlDRMaoaDzcOGmlDA/zh-cn_image_0000002589245513.png?HW-CC-KV=V1&HW-CC-Date=20260429T054044Z&HW-CC-Expire=86400&HW-CC-Sign=A2361DC5CF56869C96279704584A33F6F1E2DC47F93728D212D928146C0AAFFB)

* **角色分工：**

**Your App：** 开发者的客户端app，实现开卡、卡信息展示、充值、更新和删卡等UX体验

**Your Server：** 开发者的业务服务器。负责受理来自开发者的客户端的开卡、充值和卡片管理的业务请求，并将相应的任务下发给交通卡公司的SP TSM系统。还需对接支付机构完成开卡、充值场景的订单支付。

**支付机构：** 完成支付订单的支付。

**SP TSM：** 交通卡公司的TSM系统，负责开卡、充值和卡片管理的指令生成。

**Wallet App：** 负责实现Wallet Kit的api。将来自于SP TSM系统的开卡、充值和卡片管理的指令下发到安全芯片。

**Wallet Server：** 对接SP TSM系统，实现开卡、充值和卡片管理的指令的获取。

* **接口说明**

| 接口 | 调用方向 | 接口功能说明 |
| --- | --- | --- |
| IF1 | Your App ->  Wallet App | Wallet Kit api，包括卡片状态和信息查询接口、开卡条件检查接口、开卡接口、充值接口、卡片更新接口和删卡接口。 |
| IF2 | Your App -> Your Server | 向开发者的业务服务器发起开卡、充值、卡片更新和删卡的业务操作请求。 |
| IF3 | Your Server-> 支付机构 | 完成开卡和充值的订单支付。 |
| IF4 | Your Server-> SP TSM | 向交通卡公司的SP TSM系统提交开卡、充值、卡片更新和删卡的业务请求。 |
| IF5 | Wallet Server-> SP TSM | 向交通卡公司的SP TSM系统获取开卡、充值、卡片更新和删卡的业务请求以及实现这些业务功能的指令。 |
