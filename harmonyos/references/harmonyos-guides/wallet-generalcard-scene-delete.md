---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-generalcard-scene-delete
title: 删除通用凭证
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 通用凭证 > 开发场景 > 删除通用凭证
category: harmonyos-guides
scraped_at: 2026-09-10T06:23:32+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:07459bc8cc78cfd8f80d093d20d6679cc8b02c271b87681159c45e8899a5e89b
---

用户主动删除，将通用凭证从钱包中移除。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/oLksK6xjROmuRd7D_rRCxg/zh-cn_image_0000002747211973.png)

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

## 删除成功回调

当通用凭证删除成功之后，钱包App携带删除成功回调请求钱包服务器，钱包服务器通过[NFC相关事件回调通知接口](../harmonyos-references/wallet-rest-api-public.md#nfc相关事件回调通知接口)通知开发者服务器。
