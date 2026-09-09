---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-carkey-scene-migration
title: 迁移车钥匙
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 数字车钥匙 > 开发场景 > 迁移车钥匙
category: harmonyos-guides
scraped_at: 2026-09-10T06:23:31+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:01c9b6dfe6fe7d8f2612f47b1b45fdbecff5058ccefee8f4d4f6a46f28bea3a1
---

用户更换移动设备后，车钥匙自动迁移至新设备，无须重新线下配对，保障用户持续使用数字车钥匙的便捷体验。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/TI-jqrcQTim68NNIGOlVgw/zh-cn_image_0000002747292039.png)

## 服务端开发

1. 在[开通车钥匙](wallet-carkey-scene-open.md#服务端开发)的服务器激活过程中，DK服务器收到钱包App（经过钱包服务器代理）的[设备认证](../harmonyos-references/wallet-rest-api-public.md#设备认证)请求时，需要留存请求中的华为账号OpenId，建立双端账号对应关系，用作后续用户将车钥匙从老设备迁移到新设备。
2. 收到新设备上钱包App（经过钱包服务器代理）的[迁移车钥匙](../harmonyos-references/wallet-rest-api-carkey.md#车钥匙迁移)请求之后，DK服务器向钱包服务器[申请ICCE钥匙](../harmonyos-references/wallet-rest-api-carkey.md#申请icce钥匙)。
3. 申请成功之后，将生成的车钥匙JWE数据作为[迁移车钥匙](../harmonyos-references/wallet-rest-api-carkey.md#车钥匙迁移)请求的响应返回钱包App。
4. 钱包App与DK服务器进行激活车钥匙的服务器交互，激活车钥匙过程参见[开通车钥匙](wallet-carkey-scene-open.md#服务端开发)服务端开发步骤3。
5. 车钥匙激活成功之后，DK服务器收到新设备车钥匙开通成功的[NFC相关事件回调通知接口](../harmonyos-references/wallet-rest-api-public.md#nfc相关事件回调通知接口)之后，触发老设备[删除车钥匙](wallet-carkey-scene-delete.md)。
