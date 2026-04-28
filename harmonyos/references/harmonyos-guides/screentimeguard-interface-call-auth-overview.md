---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-interface-call-auth-overview
title: 概述
breadcrumb: 指南 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > 用户授权管理 > 概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:52+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:659bc578e1e56acac61908cbe9b6ff3f93a76e92d6b9d02d67d94b3c60c03f81
---

Screen Time Guard Kit需要经过用户授权才能对用户设备做时间管控和应用限制。Screen Time Guard Kit提供了请求用户授权和取消授权的接口，并且在健康使用设备的授权列表页面中，提供了用户主动打开/关闭授权的入口。开发者也可通过实现指定ExtensionAbility的回调方法，感知用户在健康使用设备的授权列表页中打开/关闭授权的行为。
