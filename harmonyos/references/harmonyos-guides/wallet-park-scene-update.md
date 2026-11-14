---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-park-scene-update
title: 更新园区卡
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 园区卡 > 开发场景 > 更新园区卡
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:34+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:41905615bc67f135b5ba722004236a51a51204ea4321795a54e2d2e6a7478549
---

当园区卡信息发生变更时，如园区卡权限、信息变更等，更新钱包中的园区卡数据。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/iNfeOzKDSOqyKTKiF4qmPw/zh-cn_image_0000002788468308.png?HW-CC-KV=V1&HW-CC-Date=20261114T004834Z&HW-CC-Expire=31536000000&HW-CC-Sign=E29A180D24D0BFB9854FBB1DC89652FC70AEE6A3D1D8ED65C6060AF7710239E6)

## 服务端开发

开发者服务器通知钱包服务端进行[园区卡数据更新](../harmonyos-references/wallet-rest-api-park.md#园区卡数据更新)，钱包服务端给钱包推送更新通知。
