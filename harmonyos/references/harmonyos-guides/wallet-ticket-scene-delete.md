---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-ticket-scene-delete
title: 删除活动/景点门票
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 活动/景点门票 > 开发场景 > 删除活动/景点门票
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:7e0d78638103dab8f06b0fb3de95c520026965186f6dd21298ba2e5e5d5a9a8b
---

用户主动删除，将门票从钱包中移除。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/3m3j9UmDToKpHVtpxr8kJg/zh-cn_image_0000002815400143.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=7DF5C3ED140C4C43365133067C88B27576282AF2BDEDAFACD0978E476A7DC751)

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
