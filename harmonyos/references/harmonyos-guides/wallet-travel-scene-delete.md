---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-travel-scene-delete
title: 删除出行凭证
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 出行凭证 > 开发场景 > 删除出行凭证
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:e636d37e57f4bce7df556495783bb6550674adbbc17857f7a7cc4f7f5b260bc3
---

用户主动删除，将出行凭证从钱包中移除。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/2Tpunne8Q0qgqaI-kpv6UQ/zh-cn_image_0000002815400143.png?HW-CC-KV=V1&HW-CC-Date=20261112T233237Z&HW-CC-Expire=31536000000&HW-CC-Sign=F4E40D04F16893C1A89A03433ACB815884A91EFA847CF5AE478F7C2D068E5961)

## 服务端开发

删除出行凭证的场景主要分为如下两个场景：

* **钱包侧触发删除**

  用户在钱包App中手动删除（包括恢复出厂、退出账号等场景）。
* **开发者客户端侧触发删除**

  用户在开发者客户端中手动删除，开发者客户端请求开发者服务器触发删除。

服务端开发参考[出行凭证更新](../harmonyos-references/wallet-rest-api-travel.md#出行凭证数据更新)，采用PATCH方式进行局部更新，请求体如下：

```json
{
  "fields": {
    "status": {
      "state": "expired"
    }
  }
}
```
