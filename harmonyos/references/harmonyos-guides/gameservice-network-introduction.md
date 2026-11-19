---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-network-introduction
title: 网络游戏登录概述
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > 基础游戏服务（必选） > 游戏登录 > 网络游戏登录 > 网络游戏登录概述
category: harmonyos-guides
scraped_at: 2026-11-19T09:48:57+08:00
doc_updated_at: 2026-07-03
content_hash: sha256:763ddbe3de032c93e9f2177c111eb1a95ed9a8d04f1f1e9b5013b770b9515aff
---

网络游戏是指需要联网的游戏。

接入基础游戏服务后，网络游戏支持用户在联合登录面板选择华为账号登录或游戏官方账号登录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/v3y1eXllRPq07l5hl_G8JA/zh-cn_image_0000002791566340.png?HW-CC-KV=V1&HW-CC-Date=20261119T014857Z&HW-CC-Expire=31536000000&HW-CC-Sign=CA18010F6A6D30EB7E6D8133CE695EFB17232FF7974F88789DA69A473D37D050)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/zGzH-Cu1Qjq9nRI0WrNEPw/zh-cn_image_0000002820526293.png?HW-CC-KV=V1&HW-CC-Date=20261119T014857Z&HW-CC-Expire=31536000000&HW-CC-Sign=80796C0E05572AD33CDE1D06E82AFCA6DD5E7428519CBE6CC1AFB12D7BBAC51F)

## 网络游戏登录场景介绍

### 接入华为账号登录

网络游戏必须接入华为账号登录。

接入后，华为平台会将HarmonyOS 4及以下游戏的玩家标识playerId/openId赋值给HarmonyOS 5.0及以上游戏的玩家标识gamePlayerId，为新老系统游戏的账号资产（角色、区服信息、游戏进度等）实现互通。互通前后，华为账号ID不会发生变化，也不涉及开发者服务器和数据库层面的变动。

华为账号的实名认证、未成年人防沉迷由基础游戏服务实现，华为账号的支付合规控制（例如未成年人支付限额）由IAP Kit（应用内支付服务）实现。

### 接入游戏官方账号登录

若游戏有官包且有官方账号体系，网络游戏还需要接入游戏官方账号登录，且游戏开发者需要正确实现HarmonyOS 5.0及以上系统游戏包与游戏官包之间账号资产的互通。

游戏官方账号的实名认证、未成年人防沉迷、支付合规控制需要游戏开发者自行实现。

**说明** 

用户使用游戏官方账号登录游戏时，设备上基础游戏服务也会基于设备上登录的华为账号实现实名认证、未成年人防沉迷，这属于HarmonyOS 5.0及以上设备的额外要求。游戏官方账号登录游戏时，开发者仍需要基于游戏官方账号实现实名认证、未成年人防沉迷、支付合规控制。

### 账号关系总览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/NhPFsy0CT-OdhPRo4izurg/zh-cn_image_0000002820406293.png?HW-CC-KV=V1&HW-CC-Date=20261119T014857Z&HW-CC-Expire=31536000000&HW-CC-Sign=FFB07A7688794573477471C0EE606C9446F39F1ED41F5F7289C149FC6039B458)

## 网络游戏用户体验

玩家侧的游戏登录体验。

### 首次登录

首次启动游戏时，向用户展示联合登录面板。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/95UtUEiwTGi9fTx9P8mWZA/zh-cn_image_0000002820526293.png?HW-CC-KV=V1&HW-CC-Date=20261119T014857Z&HW-CC-Expire=31536000000&HW-CC-Sign=283D4943705234B7F90720B47797E80552DA539F7F9E3ED0564C2CEB36A90331)

* 点击游戏官方账号，弹出游戏官方账号的登录界面，用户正确输入账号后进入游戏。
* 点击华为账号，用户使用华为账号进入游戏，顶部展示欢迎横幅。

### 非首次登录

用户非首次启动游戏时，游戏会沿用之前的登录账号。涉及切换账号再登录等特殊场景的接入方式请参见[游戏内切换账号](gameservice-gameplayer-official.md#游戏内切换账号)。
