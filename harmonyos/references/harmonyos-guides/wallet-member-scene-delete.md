---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-member-scene-delete
title: 删除会员卡
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 会员卡 > 开发场景 > 删除会员卡
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:85cb5f31c43384926d8ce2c47d02750996acac40162367745ad84ec42f01768c
---

用户主动删除，将会员卡从钱包中移除。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/w6V9ap2wThaoObhgD9Gaag/zh-cn_image_0000002815400143.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=50D83A15B623246FBC7C48A6EC181C02FEA05F67BF18345540BA7EF46C3B611C)

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
