---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-park-scene-update
title: 更新园区卡
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 园区卡 > 开发场景 > 更新园区卡
category: harmonyos-guides
scraped_at: 2026-11-04T08:30:45+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:bcdc257406674ba3cfc840b886d289f40f25cdab5aabe8c47338e391b772761f
---

当园区卡信息发生变更时，如园区卡权限、信息变更等，更新钱包中的园区卡数据。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/80do3iCmREGyRtOzffHOhw/zh-cn_image_0000002809011327.png)

## 服务端开发

开发者服务器通知钱包服务端进行[园区卡数据更新](../harmonyos-references/wallet-rest-api-park.md#园区卡数据更新)，钱包服务端给钱包推送更新通知。
