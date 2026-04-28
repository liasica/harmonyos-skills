---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-habit-rec-introduction
title: 概述
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 习惯推荐方案 > 概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:aab6ab09891307615ee44c359d1df8edf8067400d3f5780a02e0b79d876de41d
---

习惯推荐是HarmonyOS学习用户的行为习惯后做出的主动预测推荐。

1. 开发者将用户在应用/元服务内的使用行为向HarmonyOS共享，使得HarmonyOS可以基于共享的数据学习用户的行为习惯。
2. 在HarmonyOS学习到用户的行为习惯后，会给用户推荐相应功能，并且尝试补充详细功能参数，减少用户执行任务的步骤。

以听音乐为例，意图框架设计了统一的意图——播放歌单意图，该意图可以让应用/元服务与HarmonyOS交互。

当用户使用应用/元服务播放歌单时，应用/元服务可以向Intents Kit共享该意图，并提供一些用于学习的特征，例如播放开始/结束时间、播放时长、歌单名等。HarmonyOS会结合底层采集的时间、空间、设备状态等数据共同理解用户行为上下文。最后HarmonyOS结合应用/元服务历史上共享过的数据重建响应意图任务并进行预测推荐，例如在用户每天早上上车后，为其推荐“每日推荐”歌单卡片，用户点击实现一键播放。
