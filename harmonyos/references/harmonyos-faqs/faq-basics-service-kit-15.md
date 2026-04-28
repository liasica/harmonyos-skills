---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-15
title: 通过公共事件服务CES发布、订阅事件，发布事件达到一定数量后，订阅者接收不到发布的事件
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 通过公共事件服务CES发布、订阅事件，发布事件达到一定数量后，订阅者接收不到发布的事件
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:22+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c86dec18ecc7b67977c8bf1467b14da8313e001c9e11db8ac7befe87448fdef3
---

通过commonEventManager.createSubscriber()创建订阅者时，需要保存返回的订阅者对象subscriber。应用切换后台之后，如果预测能回收的对象尺寸大于2M会触发一次[Full GC](../harmonyos-guides/gc-introduction.md#hpp-gc的类型)，未保存的subscriber会被清理掉，进而导致订阅取消、收不到数据。

**参考链接**

[动态订阅公共事件](../harmonyos-guides/common-event-subscription.md)
