---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-generalcard-scene-update
title: 更新通用凭证
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 通用凭证 > 开发场景 > 更新通用凭证
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:42+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6522c153feb42f6a1bbaf85901d7c4ef996a2e470edd33817afff933fd2eab06
---

当通用凭证信息发生变更时，如预约时间变更、状态更新等，更新钱包中的凭证数据。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/A5ATx1WiQhyu97fqseKmJw/zh-cn_image_0000002821758263.png?HW-CC-KV=V1&HW-CC-Date=20261121T011114Z&HW-CC-Expire=31536000000&HW-CC-Sign=DB99A03A195C0DD95A99937425FDABB023B82D7E80D20CE3F205AEC4052ACF72)

## 服务端开发

1. 用户进入钱包卡详情页面后，钱包服务器向开发者服务器主动触发[检测更新](../harmonyos-references/wallet-rest-api-public.md#检测更新)。
2. 开发者服务器检测到变化，通知钱包服务器进行[通用凭证数据更新](../harmonyos-references/wallet-rest-api-generalcard.md#通用凭证数据更新)，钱包服务端给钱包推送更新通知。
