---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-faq-6
title: 应用内通话消息在设备重启后的首次锁屏状态问题
breadcrumb: 指南 > 应用服务 > Push Kit（推送服务） > Push Kit常见问题 > 应用内通话消息在设备重启后的首次锁屏状态问题
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:35+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:8218e03a7e345f79732bd2f2689b9a72125712fd9ef26efe8fe992d31c5376b3
---

当终端处于设备重启后的首次锁屏状态时，应用子进程可能会因数据区加密而导致访问失败，进而出现业务无法正常执行的情况。请您在开发时适配此种场景，进行相关异常保护。
