---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-hotel-scene-delete
title: 删除酒店房卡
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 酒店房卡 > 开发场景 > 删除酒店房卡
category: harmonyos-guides
scraped_at: 2026-09-10T06:23:32+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:478290e05964bb734c6c3fd50ec5b4674ee0a1bb094399ba361f43db88f25739
---

用户主动删除，将酒店房卡从钱包中移除。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/__CFXFjsS9qKWVN3vfuq2A/zh-cn_image_0000002717612112.png)

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
