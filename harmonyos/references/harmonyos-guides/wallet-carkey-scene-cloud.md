---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-carkey-scene-cloud
title: 上传车端数据到DK服务器
breadcrumb: 指南 > 应用服务 > Wallet Kit（钱包服务） > 数字车钥匙 > 开发场景 > 上传车端数据到DK服务器
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:33+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:c50e1f5702e3f5712085ac0f2b8fbad0ff7ad89303439d7d34f80ef5864db4eb
---

车端可通过钱包提供的通道上传自定义数据，用于获取DK服务器存储的钥匙状态、权限信息等云端数据，钱包作为中间桥梁透传交互数据，提供完整的业务闭环渠道。

## 交互流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/CRhiQOCmTQaVf_turYmHfg/zh-cn_image_0000002706835234.png)

## 典型场景

当车辆的车钥匙**首次**开通且完成认证之后，车端需要上传数据给DK服务器，DK服务器处理之后返回结果给车端。可参考[上传车端数据到DK服务器](../harmonyos-references/wallet-rest-api-carkey.md#上传车端数据到dk服务器)进行适配。
