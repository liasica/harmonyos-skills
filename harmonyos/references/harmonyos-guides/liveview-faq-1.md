---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/liveview-faq-1
title: 更新实况窗被频控的问题
breadcrumb: 指南 > 应用服务 > Live View Kit（实况窗服务） > Live View Kit常见问题 > 更新实况窗被频控的问题
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2061178044e3215fa02810713af5d7488406ca7f05f1ffe34b6c58ec91ea940b
---

通过Push Kit更新实况窗时，单个实况窗消息每个设备每5分钟最多更新10次，每小时最多更新60次。出行打车与赛事比分场景，5分钟最多更新30次，每小时最多更新180次。详情见Push Kit[消息频控](../harmonyos-references/push-msg-freq-control.md)。

实况窗创建和更新有流控机制:

* 系统级流控（针对所有应用），实况通知创建每秒最多15次，实况通知更新每秒最多30次，超过频次部分被丢弃不下发。
* 应用级流控（针对单个应用），实况通知创建每秒最多10次，实况通知更新每秒最多20次，超过频次部分被丢弃不下发。
