---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-faq-3
title: 如何设置游戏登录界面不显示官方账号登录
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > Game Service Kit常见问题 > 基础游戏服务 > 如何设置游戏登录界面不显示官方账号登录
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:24+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:5da68e919d3dfa1919dd6895bd177395c1c848a84fd9cadb558b85f7acfb1051
---

在游戏调用[unionLogin()](../harmonyos-references/gameservice-gameplayer.md#gameplayerunionlogin)接口时，将thirdAccountInfos参数传空数组，即可实现玩家登录游戏时不展示联合登录面板，默认使用华为账号登录。
