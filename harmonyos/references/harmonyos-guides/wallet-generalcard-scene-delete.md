---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-generalcard-scene-delete
title: 删除通用凭证
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 通用凭证 > 开发场景 > 删除通用凭证
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:34+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:8f2c132ff5a66402ee07cb6e1bbbec195a5938b182ea13ab572e4028fd89731e
---

用户主动删除，将通用凭证从钱包中移除。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/B5qWdBjNRPG1o5lSpcz03g/zh-cn_image_0000002817427735.png?HW-CC-KV=V1&HW-CC-Date=20261114T004650Z&HW-CC-Expire=31536000000&HW-CC-Sign=37A386BB63E14AE78D08614076001F83813897B59FB423AF119EBFE3568652C9)

## 服务端开发

删除通用凭证的场景主要分为如下两个场景：

* **钱包侧触发删除**

  用户在钱包App中手动删除（包括恢复出厂、退出账号等场景）。
* **开发者客户端侧触发删除**

  用户在开发者客户端中手动删除，开发者客户端请求开发者服务器触发删除。

服务端开发参考[通用凭证更新](../harmonyos-references/wallet-rest-api-generalcard.md#通用凭证数据更新)，采用PATCH方式进行局部更新，请求体如下：

```json
{
  "fields": {
    "status": {
      "state": "expired"
    }
  }
}
```
