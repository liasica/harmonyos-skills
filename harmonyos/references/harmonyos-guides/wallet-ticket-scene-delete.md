---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-ticket-scene-delete
title: 删除活动/景点门票
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 活动/景点门票 > 开发场景 > 删除活动/景点门票
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:42+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:dc5197c8430211e5098d40edd6a09c209936aca5863dea49ec248e8a4bd8ac0c
---

用户主动删除，将门票从钱包中移除。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/q0LB8t6vTz6AMGtAFrUZDA/zh-cn_image_0000002793038326.png?HW-CC-KV=V1&HW-CC-Date=20261121T011114Z&HW-CC-Expire=31536000000&HW-CC-Sign=2C4D45FA33C22E93ABDFB7B38674800331FBF0C469A929C1CA4B33B638D0EB85)

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
