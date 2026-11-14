---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-member-scene-update
title: 更新会员卡
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 会员卡 > 开发场景 > 更新会员卡
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:34+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:db78b1e5d11813fa784740b514a0f681e98826253e9eed49e96978454e407f2b
---

当会员卡信息发生变更时，如会员信息修改、权益发生变更等，更新钱包中的会员卡数据。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/SXHK2N58T3-0xG_5Ynyk-A/zh-cn_image_0000002788308372.png?HW-CC-KV=V1&HW-CC-Date=20261114T004649Z&HW-CC-Expire=31536000000&HW-CC-Sign=DE34A6DE04D83AA31E5D20B2CFD46AC9032435EA40182E8D73937FB9A8CC7AEC)

## 服务端开发

开发者服务器通知钱包服务端进行[会员卡数据更新](../harmonyos-references/wallet-rest-api-member.md#会员卡数据更新)，钱包服务端给钱包推送更新通知。
