---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-ticket-scene-delete
title: 删除活动/景点门票
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 活动/景点门票 > 开发场景 > 删除活动/景点门票
category: harmonyos-guides
scraped_at: 2026-09-21T06:18:51+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:7e35e76e7c234e980c9ac089da8ea37e708cd630a7ed5a37247cbf2379d2a7bc
---

用户主动删除，将门票从钱包中移除。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/fpEDKcuFRse9ci9m25xjBA/zh-cn_image_0000002733435534.png)

## 服务端开发

删除活动/景点门票的场景主要分为如下两个场景：

* **钱包侧触发删除**

  用户在钱包App中手动删除（包括恢复出厂、退出账号等场景）。
* **开发者客户端侧触发删除**

  用户在开发者客户端中手动删除，开发者客户端请求开发者服务器触发删除。

服务端开发参考[活动/景点门票更新](../harmonyos-references/wallet-rest-api-ticket.md#门票数据更新)，采用PATCH方式进行局部更新，请求体如下：

```json
{
  "fields": {
    "status": {
      "state": "expired"
    }
  }
}
```

## 删除成功回调

当活动/景点门票删除成功之后，钱包App携带删除成功回调请求钱包服务器，钱包服务器通过[NFC相关事件回调通知接口](../harmonyos-references/wallet-rest-api-public.md#nfc相关事件回调通知接口)通知开发者服务器。
