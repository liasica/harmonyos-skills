---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-park-scene-update
title: 更新园区卡
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 园区卡 > 开发场景 > 更新园区卡
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:41+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:8aaec49df109c70343ad5d448982d426bc8283ded35a38468df079c617b92fa1
---

当园区卡信息发生变更时，如园区卡权限、信息变更等，更新钱包中的园区卡数据。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/WIa8WmQXTuKKN-b_wDjcQQ/zh-cn_image_0000002792878348.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=F840A91615B98FE0047A0E7EF2EA7701CB72649009FD9612CF6E7764015DD972)

## 服务端开发

开发者服务器通知钱包服务端进行[园区卡数据更新](../harmonyos-references/wallet-rest-api-park.md#园区卡数据更新)，钱包服务端给钱包推送更新通知。
