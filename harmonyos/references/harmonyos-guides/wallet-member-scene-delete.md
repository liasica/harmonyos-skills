---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-member-scene-delete
title: 删除会员卡
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 会员卡 > 开发场景 > 删除会员卡
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:41+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:402c670e36933f3ae1c9bd3a4751049d72fa74590f871c168f3b1b08796c94b0
---

用户主动删除，将会员卡从钱包中移除。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/v-byiozESiWrui2YeRTM_Q/zh-cn_image_0000002793038326.png?HW-CC-KV=V1&HW-CC-Date=20261121T011241Z&HW-CC-Expire=31536000000&HW-CC-Sign=1C80D2736EED863CE88D8279E3248185598CAB29A0821CE3AF8CE9EAC7320610)

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
