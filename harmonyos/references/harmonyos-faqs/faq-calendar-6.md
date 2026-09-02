---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-calendar-6
title: 日历中的日程类型有什么区别
breadcrumb: FAQ > 应用服务开发 > 日历服务（Calendar Kit） > 日历中的日程类型有什么区别
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2cd768a34a9820dd2d2e0afd2bbacd15b3e62655219a8b735dbd695e3a9137ca
---

## 问题现象

日历中的日程类型有什么区别？为什么添加日程时会在日历中显示纪念日？

## 解决方案

在日历应用中点击右上角"+"按钮时，会显示"日程"和"重要日"两个页签选项：

* 日程：指普通日程（对应枚举类型：calendarManager.EventType.NORMAL），例如用于会议、提醒等日常事务。
* 重要日：指重要日程（对应枚举类型：calendarManager.EventType.IMPORTANT），例如结婚纪念日等具有纪念意义的日期。

当选择创建重要日类型时，系统会将其归类为纪念日相关日程。关于事件类型的完整定义，请参考：[EventType](../harmonyos-references/js-apis-calendarmanager.md#eventtype)。
