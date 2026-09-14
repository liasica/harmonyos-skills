---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-park-scene-qr
title: 生成展示二维码
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 园区卡 > 开发场景 > 生成展示二维码
category: harmonyos-guides
scraped_at: 2026-09-15T07:02:59+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:57b86b90352825d2f6a8ad9a61eec71c4c840af79894e00029d2513371d597ce
---

用户可以通过钱包动态展示的二维码，实现支付功能，同时支持实时通知扫码结果并刷新页面。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/uiTp_cHWRdqcD-WCd0uGpQ/zh-cn_image_0000002723696386.png)

## 服务端开发

接入Wallet Kit服务时，若选择动态二维码方式，开发者服务器需要实现以下服务器接口，以便钱包实时请求二维码，并支持扫码后跳转到结果页。

1. 用户操作钱包进入刷卡页，请求开发者服务器[申请二维码](../harmonyos-references/wallet-rest-api-park.md#申请二维码)。
2. 钱包使用二维码进行扫码，开发者服务器[通知扫码结果](../harmonyos-references/wallet-rest-api-park.md#通知扫码结果)给钱包服务器，钱包进行扫码结果刷新。
