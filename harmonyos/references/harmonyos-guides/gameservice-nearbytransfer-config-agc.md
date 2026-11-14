---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-nearbytransfer-config-agc
title: 开发准备
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > 游戏近场快传（可选） > 开发准备
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:17+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:27ee7a14e6b1459e392f69b2121180440497b3676c0e9e72b46f6d39ba0c6e5b
---

## 创建游戏

若在华为应用市场发布游戏，或使用AGC控制台提供的服务，需要前往AGC控制台创建游戏类应用，具体操作请参见[创建HarmonyOS应用](../app/agc-help-create-app-0000002247955506.md)。其中：

* “应用类型”：选择“HarmonyOS应用”。
* “应用分类”：选择“游戏”。

## 生成签名证书

数字证书和Profile文件等签名信息可以确保游戏的完整性，请参见[配置签名信息](application-dev-overview.md#配置签名信息)完成配置。

## 配置APP ID和相关权限

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)平台，在“开发与服务”中选择目标应用，获取“项目设置 > 常规 > 应用”的**APP ID**。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/FgGzkoeGQpWkvorPuionIQ/zh-cn_image_0000002817507465.png?HW-CC-KV=V1&HW-CC-Date=20261114T004634Z&HW-CC-Expire=31536000000&HW-CC-Sign=12B286EA74BB259B0748F8C76D41421505D078076EDDE58E7F9835401B9CADFF)
2. 在工程的entry模块module.json5文件中，新增metadata并配置app\_id，同时新增requestPermissions并配置如下权限。

   ```typescript
   "module": {
     "name": "entry",
     "type": "entry",
     "description": "xxxx",
     "mainElement": "xxxx",
     "deviceTypes": [
       "phone"
     ],
     "deliveryWithInstall": true,
     "pages": "$profile:main_pages",
     "abilities": [],
     "metadata": [ // 配置如下信息
       {
         "name": "app_id",
         "value": "xxxxxx" // 配置为前面步骤中获取的APP ID
       }
     ],
      "requestPermissions": [ // 配置权限
        {
          "name": "ohos.permission.INTERNET" // 允许使用Internet网络权限
        },
        {
          "name": "ohos.permission.GET_NETWORK_INFO"  // 允许应用获取数据网络信息权限
        },
        {
          "name": "ohos.permission.SET_NETWORK_INFO" // 允许应用配置数据网络权限
        },
        {
          "name": "ohos.permission.DISTRIBUTED_DATASYNC", // 允许不同设备间的数据交换权限
          "reason": "$string:distributed_permission",
          "usedScene": {
            "abilities": [
              "EntryAbility"
            ],
            "when": "inuse"
          }
        }
      ]
   }
   ```
