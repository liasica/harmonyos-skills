---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-travel-scene-delete
title: 删除出行凭证
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 出行凭证 > 开发场景 > 删除出行凭证
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:41+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:a19231fdb40a18c04b43f1b307b5699d0857fa83441d40bf8ae739e6fc26cd43
---

用户主动删除，将出行凭证从钱包中移除。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/YX4YNxDcSVuYZ-I340Ab9Q/zh-cn_image_0000002793038326.png?HW-CC-KV=V1&HW-CC-Date=20261121T011114Z&HW-CC-Expire=31536000000&HW-CC-Sign=FCD749D96DC528863BEDB969739FC59D475B774D4E7FA3BDCC288DFE7B3DEA02)

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
