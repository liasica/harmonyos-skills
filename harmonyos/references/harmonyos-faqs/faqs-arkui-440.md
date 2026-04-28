---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-440
title: 如何给Swiper组件添加节流，控制Swiper的切换频率
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何给Swiper组件添加节流，控制Swiper的切换频率
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:55+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:9bb86ab9f7ad53f0b2505a556217fe571c611ac1a29710213f43c37b74e240ae
---

**问题描述**

Swiper组件可以添加节流么，快速滑动的话容易造成页面卡顿，请问如何添加节流控制Swiper的切换频率？

**解决措施**

在快速滑动时，在每次松手时都会触发onAnimationEnd，此时可以识别目标index，可以设置[onContentWillScroll](../harmonyos-references/ts-container-swiper.md#oncontentwillscroll15)中拦截的index，控制Swiper无法滑动，实现节流，在一段时间后，取消拦截，需在节流期间忽略所有滑动事件，避免队列堆积。
