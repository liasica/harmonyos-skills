---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-generalcard-scene-update
title: 更新通用凭证
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 通用凭证 > 开发场景 > 更新通用凭证
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b4fdbe28d0e96b9944147918cedcbb5277ddefcdb6c2e6f6a89d645ace75cbad
---

当通用凭证信息发生变更时，如预约时间变更、状态更新等，更新钱包中的凭证数据。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/qQEOpgAFRsux_xsMQT21kA/zh-cn_image_0000002712405452.png)

## 服务端开发

1. 用户进入钱包卡详情页面后，钱包服务器向开发者服务器主动触发[检测更新](../harmonyos-references/wallet-rest-api-public.md#检测更新)。
2. 开发者服务器检测到变化，通知钱包服务器进行[通用凭证数据更新](../harmonyos-references/wallet-rest-api-generalcard.md#通用凭证数据更新)，钱包服务端给钱包推送更新通知。
