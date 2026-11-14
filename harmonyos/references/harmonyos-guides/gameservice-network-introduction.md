---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-network-introduction
title: 网络游戏登录概述
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > 基础游戏服务（必选） > 游戏登录 > 网络游戏登录 > 网络游戏登录概述
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:17+08:00
doc_updated_at: 2026-07-03
content_hash: sha256:d45707cc221aa7d51c97b5b12f2f861b8f5b920284a3e178ea216cfae679b8c9
---

网络游戏是指需要联网的游戏。

接入基础游戏服务后，网络游戏支持用户在联合登录面板选择华为账号登录或游戏官方账号登录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/c3APC-C4SB6ggIOCb3PezA/zh-cn_image_0000002788467954.png?HW-CC-KV=V1&HW-CC-Date=20261114T004817Z&HW-CC-Expire=31536000000&HW-CC-Sign=9804E0526CF5D6C0B38712E026E726D3DDEEB0B6826E1675ED43A45A2B561FA1)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/F7fHh2S_RC-Bd3Zvnw49TQ/zh-cn_image_0000002817507443.png?HW-CC-KV=V1&HW-CC-Date=20261114T004817Z&HW-CC-Expire=31536000000&HW-CC-Sign=92462985A2A675B877DA99E7F8610639A04C86D9CF8C86B79C4DBBC3339F3600)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/SlxPEpM3Td6PQf5iKq69sw/zh-cn_image_0000002788308012.png?HW-CC-KV=V1&HW-CC-Date=20261114T004817Z&HW-CC-Expire=31536000000&HW-CC-Sign=06DB81949D24DC15A541A02D009C49C0F0CCE71B39D0B530939DC6A10AA35F46)

## 网络游戏用户体验

玩家侧的游戏登录体验。

### 首次登录

首次启动游戏时，向用户展示联合登录面板。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/03KRR2QaRn6v7S0aGm2_FA/zh-cn_image_0000002817507443.png?HW-CC-KV=V1&HW-CC-Date=20261114T004817Z&HW-CC-Expire=31536000000&HW-CC-Sign=136E0A753D3972A65FB2967651A49B29A524916F7A9ECADDCFCD565E9534F55D)

* 点击游戏官方账号，弹出游戏官方账号的登录界面，用户正确输入账号后进入游戏。
* 点击华为账号，用户使用华为账号进入游戏，顶部展示欢迎横幅。

### 非首次登录

用户非首次启动游戏时，游戏会沿用之前的登录账号。涉及切换账号再登录等特殊场景的接入方式请参见[游戏内切换账号](gameservice-gameplayer-official.md#游戏内切换账号)。
