---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-hotel-scene-delete
title: 删除酒店房卡
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 酒店房卡 > 开发场景 > 删除酒店房卡
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:41+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:db937391735de7a8e16072d4c0ab5b3f3c3e5c522c69f1428dec6013249c13f5
---

用户主动删除，将酒店房卡从钱包中移除。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/AKeIznGEQlKeJodOwvrJ7w/zh-cn_image_0000002821838269.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=40115577F4DA5A6A6753595D35EA7C74DA0A50E0E61965FE7F3D229025A1AB62)

## 服务端开发

删除酒店房卡的场景主要分为如下两个场景：

* **钱包侧触发删除**

  用户在钱包App中手动删除（包括恢复出厂、退出账号等场景）。
* **开发者客户端侧触发删除**

  用户在开发者客户端中手动删除，开发者客户端请求开发者服务器触发删除。

服务端开发参考[酒店房卡更新](../harmonyos-references/wallet-rest-api-hotel.md#酒店房卡数据更新)，采用PATCH方式进行局部更新，请求体如下：

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

当酒店房卡删除成功之后，钱包App携带删除成功回调请求钱包服务器，钱包服务器通过[NFC相关事件回调通知接口](../harmonyos-references/wallet-rest-api-public.md#nfc相关事件回调通知接口)通知开发者服务器。
