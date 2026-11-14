---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-ticket-scene-delete
title: 删除活动/景点门票
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 活动/景点门票 > 开发场景 > 删除活动/景点门票
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:34+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:d52567e7eaaaa6cff60a8052cb3e8da55ffa3912097a63449b00cbc983a44fda
---

用户主动删除，将门票从钱包中移除。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/IA8PTjegSw6-CbHjGCORXA/zh-cn_image_0000002817427735.png?HW-CC-KV=V1&HW-CC-Date=20261114T004650Z&HW-CC-Expire=31536000000&HW-CC-Sign=3C18007E9EF485703BDF8E04744C3242548647F0C24EA134F55F3B510A76859D)

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
