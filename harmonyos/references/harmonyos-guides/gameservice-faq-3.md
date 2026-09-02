---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-faq-3
title: 如何设置游戏登录界面不显示官方账号登录
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > Game Service Kit常见问题 > 基础游戏服务 > 如何设置游戏登录界面不显示官方账号登录
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:26+08:00
doc_updated_at: 2026-07-03
content_hash: sha256:441339ec870172e418dbe0587716a8b106cb73804ead43b614a5b90e5983f3aa
---

在游戏调用[unionLogin](../harmonyos-references/gameservice-gameplayer.md#gameplayerunionlogin)接口时，将thirdAccountInfos参数传空数组，即可实现玩家登录游戏时不展示联合登录面板，默认使用华为账号登录。
