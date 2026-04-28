---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-faq-3
title: 游戏如何实现不展示官方账号登录？
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > Game Service Kit常见问题 > 基础游戏服务 > 游戏如何实现不展示官方账号登录？
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a8defa09381cfce916778a25f3921fa5be0d42ad310f597cf1af657af0fb58c8
---

在游戏调用[unionLogin](../harmonyos-references/gameservice-gameplayer.md#gameplayerunionlogin)接口时，将thirdAccountInfos参数传空数组，即可实现玩家登录游戏时不展示“游戏官方账号登录”选项，默认使用华为账号登录。
