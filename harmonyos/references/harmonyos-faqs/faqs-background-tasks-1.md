---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-background-tasks-1
title: 如何在Stage模型中创建后台任务
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 后台任务开发（Background Tasks） > 如何在Stage模型中创建后台任务
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:53+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:73760647674ab3586a70a80d60808ce0d622426af0fe04098077926ac64d90fe
---

**问题现象**

在Stage模型中创建后台任务，可以使用系统提供的API，但第三方应用不支持调用ServiceExtensionAbility。建议使用其他系统接口或方法来实现后台任务。

**解决措施**

后台任务，包括短时任务、长时任务、延迟任务、代理提醒等，例如：在Stage模型中创建长时任务的步骤请参考长时任务[开发步骤](../harmonyos-guides/continuous-task.md#开发步骤)。

**参考链接**

[@ohos.resourceschedule.backgroundTaskManager (后台任务管理)](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md)
