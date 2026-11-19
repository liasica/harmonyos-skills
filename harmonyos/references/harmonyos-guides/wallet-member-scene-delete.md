---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-member-scene-delete
title: 删除会员卡
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 会员卡 > 开发场景 > 删除会员卡
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:15+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:19875aa0978c5a717d34602ccf7c87a96932b58411066e760a41e1753c35dd32
---

用户主动删除，将会员卡从钱包中移除。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/STWJdQ28TMuBJTtxmT7n5A/zh-cn_image_0000002791726674.png?HW-CC-KV=V1&HW-CC-Date=20261119T014914Z&HW-CC-Expire=31536000000&HW-CC-Sign=C45DF3A3FD2669CDC8E60554EDC0218541B42373449AE7E0BFC97CDCE75788CF)

## 服务端开发

删除会员卡的场景主要分为如下两个场景：

* **钱包侧触发删除**

  用户在钱包App中手动删除（包括恢复出厂、退出账号等场景）。
* **开发者客户端侧触发删除**

  用户在开发者客户端中手动删除，开发者客户端请求开发者服务器触发删除。

服务端开发参考[会员卡更新](../harmonyos-references/wallet-rest-api-member.md#会员卡数据更新)，采用PATCH方式进行局部更新，请求体如下：

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

当会员卡删除成功之后，钱包App携带删除成功回调请求钱包服务器，钱包服务器通过[NFC相关事件回调通知接口](../harmonyos-references/wallet-rest-api-public.md#nfc相关事件回调通知接口)通知开发者服务器。
