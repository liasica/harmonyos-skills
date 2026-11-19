---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-member-scene-update
title: 更新会员卡
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 会员卡 > 开发场景 > 更新会员卡
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:15+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:26c3b50572952309730b52650f43dfc1503a23ab4744894c1cece7c8d81983c7
---

当会员卡信息发生变更时，如会员信息修改、权益发生变更等，更新钱包中的会员卡数据。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/2JfKfJdVRuK6ZdTxoXELtg/zh-cn_image_0000002820406653.png?HW-CC-KV=V1&HW-CC-Date=20261119T014820Z&HW-CC-Expire=31536000000&HW-CC-Sign=FDD1E865EAF97215AA948E761EB8F18329A6BAF17DF0E0CD304FD052F61B6062)

## 服务端开发

开发者服务器通知钱包服务端进行[会员卡数据更新](../harmonyos-references/wallet-rest-api-member.md#会员卡数据更新)，钱包服务端给钱包推送更新通知。
