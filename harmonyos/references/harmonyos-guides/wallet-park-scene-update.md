---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-park-scene-update
title: 更新园区卡
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 园区卡 > 开发场景 > 更新园区卡
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:14+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:12d6f3ab4f740b09342b9d3092ba7ac891d9d753035f53aa2832f9e06b0d6944
---

当园区卡信息发生变更时，如园区卡权限、信息变更等，更新钱包中的园区卡数据。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/sBBRi_oaTDqcLgcyMjoSmQ/zh-cn_image_0000002791566694.png?HW-CC-KV=V1&HW-CC-Date=20261119T014914Z&HW-CC-Expire=31536000000&HW-CC-Sign=01CD3787A0A9EC1EF655DCCA2F2490ED559CB51D34B14BC67B2EDDBEE2D95B81)

## 服务端开发

开发者服务器通知钱包服务端进行[园区卡数据更新](../harmonyos-references/wallet-rest-api-park.md#园区卡数据更新)，钱包服务端给钱包推送更新通知。
