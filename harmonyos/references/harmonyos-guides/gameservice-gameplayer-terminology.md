---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-gameplayer-terminology
title: 基础游戏服务术语
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > 基础游戏服务（必选） > 基础游戏服务术语
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:04+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3b23b0a8166a76b762ad89063b9122c21228b39a6ce1b258cb7ea8b876ac513f
---

## H

### HarmonyOS 4及以下

包含HarmonyOS 3.1/4.0及以下、EMUI在内的老系统。

### HarmonyOS 5.0及以上

HarmonyOS 5.0及以上商用版本的新系统。

## I

### Interoperability

互通是HarmonyOS 4及以下系统与HarmonyOS 5.0及以上系统的玩家标识进行统一化，支持玩家使用华为账号登录新老系统的游戏。并且新老系统下的账号资产保持一致。

## S

### Standalone Games

单机游戏，是指游戏数据本地化存储，不依赖服务器。

## U

### User ID

HarmonyOS 4及以下系统或HarmonyOS 5.0及以上系统的玩家标识。

说明

玩家标识严格区分大小写，例如gamePlayerId=xxx和gamePlayerId=XXX表示两个不同的玩家。

| 系统 | 名称 | 组成 | 说明 |
| --- | --- | --- | --- |
| HarmonyOS 5.0及以上系统 | gamePlayerId | 根据[配置APP ID映射关系](gameservice-gameplayer-huawei.md#配置app-id映射关系)时的选择openId或playerId。 | 用于华为账号登录的玩家标识。  不同游戏下，同一玩家的gamePlayerId不同。 |
| HarmonyOS 5.0及以上系统 | teamPlayerId | teamPlayerId≈uid+developerid | 同一个开发者账号developerid下的不同游戏，玩家使用同一个华为账号登录后获取的teamPlayerId相同。  新接入基础游戏服务的游戏无需关注该玩家标识。 |
| HarmonyOS 4及以下系统 | openId | 由华为账号（用户账号）和应用唯一标识组合加密起来的用户标识。  简单理解：openid≈uid+clientid | openId是应用内唯一账号标识。若应用主体转移后，该openId标识不会发生改变。  使用相同华为账号登录不同的游戏（包括同一个开发者的不同游戏），获取到的openId唯一且不相同。 |
| HarmonyOS 4及以下系统 | playerId | 华为游戏服务给华为账号（用户账号）封装处理后的对外开放的游戏玩家标识。  简单理解：playerId≈uid | playerId仅跟华为账号（用户账号）有关，不会随着应用或开发者账号信息变化而变化，用于游戏类应用。 |
| HarmonyOS 4及以下系统 | unionId | 由华为账号（用户账号）和开发者账号组合加密后的用户标识。  简单理解：unionid≈uid+developerid | unionId是同一个开发者主体下的唯一账号标识。若应用主体转移后，unionId会发生改变。  同一个开发者主体下的不同游戏，使用华为账号登录后获取的unionId相同。 |
