---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-park-scene-update
title: 更新园区卡
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 园区卡 > 开发场景 > 更新园区卡
category: harmonyos-guides
scraped_at: 2026-09-10T06:23:31+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:bf606299ae486aa4d68bb28aa2b164b760605509425df8c0d04ef310caebc6a8
---

当园区卡信息发生变更时，如园区卡权限、信息变更等，更新钱包中的园区卡数据。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/8IAheyTgSO6viEZnAnta2g/zh-cn_image_0000002717772030.png)

## 服务端开发

开发者服务器通知钱包服务端进行[园区卡数据更新](../harmonyos-references/wallet-rest-api-park.md#园区卡数据更新)，钱包服务端给钱包推送更新通知。
