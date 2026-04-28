---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/liveview-faq-3
title: 关于实况窗生命周期的问题
breadcrumb: 指南 > 应用服务 > Live View Kit（实况窗服务） > Live View Kit常见问题 > 关于实况窗生命周期的问题
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c561948152f23cbfafb99d360322827f13cda6312ec72efa600cc16d60e6d95a
---

## 如何实现“App关闭时，自动关闭构建的实况窗”

当App关闭时，可以调用[liveViewManager.stopLiveView](../harmonyos-references/liveview-liveviewmanager.md#liveviewmanagerstopliveview)方法，设置参数[PrimaryData](../harmonyos-references/liveview-liveviewmanager.md#primarydata)实例的keepTime值为0，即可实现立即关闭实况窗。

## 本地更新如何获取实况窗实例以及实况窗被清除后的限制

1. 本地更新实况窗时，可以通过[liveViewManager.getActiveLiveView](../harmonyos-references/liveview-liveviewmanager.md#liveviewmanagergetactiveliveview)函数获取活动的[LiveView](../harmonyos-references/liveview-liveviewmanager.md#liveview)实例。
2. 如果想要结束实况窗，建议使用[liveViewManager.stopLiveView](../harmonyos-references/liveview-liveviewmanager.md#liveviewmanagerstopliveview)方法。如果实况窗被notificationManager.cancel或notificationManager.cancelAll清除后，无论是Live View Kit还是Push Kit，无法再次通过该id更新或结束实况窗。
3. 再次创建该id的实况窗时，Live View Kit可以通过该id再次创建实况窗，Push Kit在12小时内无法通过该id再次创建实况窗。
