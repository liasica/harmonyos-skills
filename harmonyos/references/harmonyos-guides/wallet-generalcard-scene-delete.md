---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-generalcard-scene-delete
title: 删除通用凭证
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 通用凭证 > 开发场景 > 删除通用凭证
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:42+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:7dc995466f960bda1555c9dcee0d4b6dd3055ba9a3dc5bd858ed25967c524611
---

用户主动删除，将通用凭证从钱包中移除。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/x-iYdpizQSaopoxrISjIbQ/zh-cn_image_0000002793038326.png?HW-CC-KV=V1&HW-CC-Date=20261121T011242Z&HW-CC-Expire=31536000000&HW-CC-Sign=8BFF580A4B98EEE32AA694E47A67A5B338C2B54681F0BE224958373908BE534D)

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
